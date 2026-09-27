#!/usr/bin/env python3
"""Keep the flax -> retting -> spinning -> weaving -> sewing chain in balance.

v2 (Sep 27): PULL model. Sewing is sized to what actually SELLS (average
garments sold over the last 24 turns, from history/), not to the plot count,
and each step upstream makes exactly what the next step uses, plus a small
top-up while its stockpile is below target. Stockpile targets are in TURNS of
use (STOCK_TURNS), so they grow with the chain. Filling only happens when cash
is above FILL_CASH_MIN; below that the mode is HOLD (make what's used, no
top-up), so a finished expansion can never again drain cash to fill stock.

Runs from the merc-actor workflow. It only ACTS when (a) a chain building's
plot count changed (an expansion finished) or (b) the mode flips
(FILLING / FULL / HOLD). Otherwise it never fights manual tweaks.

    python chain_balancer.py            # dry run: print the plan
    python chain_balancer.py --live     # apply it (only if sizes or mode changed)
    python chain_balancer.py --live --force   # apply even if nothing changed

State (last seen sizes + mode) lives in state/chain_sizes.json.
"""
import glob
import json
import os
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request

import merc_status4 as m

LIVE = "--live" in sys.argv
FORCE = "--force" in sys.argv
STORE = "152202386005001"
STATE = os.path.join("state", "chain_sizes.json")

# building id, recipe inputs/outputs per 1x (read from the game's production pages)
CHAIN = {
    "flax":  {"id": "151602400",       "labour": 11,  "tools": 0.6, "out": 18},   # plants
    "ret":   {"id": "151802398",       "labour": 25,  "tools": 2,   "in": 90, "out": 35},   # plants -> fibres
    "spin":  {"id": "152202388002007", "labour": 75,  "tools": 0,   "in": 17, "out": 50},   # fibres -> thread
    "weave": {"id": "152202388001005", "labour": 75,  "tools": 0,   "in": 50, "out": 50},   # thread -> cloth
    "sew":   {"id": "152202388000004", "labour": 155, "tools": 0,   "in": 80, "out": 41},   # cloth -> garments
}
HOUSEHOLD_GARMENTS = 1.8

# Stockpiles between chain steps, in TURNS of what the next step uses.
# fill = extra units per turn made while below target (and cash allows).
STOCK_TURNS = 4
BUFFERS = {
    "flax fibres": {"fill": 5},
    "thread":      {"fill": 15},
    "cloth":       {"fill": 10},
}
LOW_FRACTION = 0.5       # FILLING starts when a stock is under half its target
FILL_CASH_MIN = 8000     # below this cash: HOLD (no top-ups, make only what's used)
SALES_WINDOW = 24        # turns of garment sales to average
SALES_MARGIN = 1.05      # sew 5% over average sales (garment stock covers the rest)
# Thread the household net duty uses (~24/turn). Measured use reads 0 when weaving
# stalled last turn, so never plan with less than this.
OTHER_THREAD_MIN = 24
MIN_CHANGE = 0.02        # ignore target changes smaller than this (x)


def gh(*args):
    try:
        return subprocess.run(["gh", *args], capture_output=True, text=True)
    except FileNotFoundError:
        return subprocess.CompletedProcess(args, 1, "", "no gh")


def send(method, path, body):
    req = urllib.request.Request(
        "https://play.mercatorio.io/api" + path, data=json.dumps(body).encode(), method=method,
        headers={"X-Merc-User": m.USER, "Authorization": "Bearer " + m.TOKEN,
                 "Content-Type": "application/json", "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return True, r.status
    except urllib.error.HTTPError as e:
        return False, "%s %s" % (e.code, e.read().decode()[:200])
    except urllib.error.URLError as e:
        return False, str(e.reason)


def garment_sales():
    """Average garments sold per turn over the last SALES_WINDOW turns (None if no history)."""
    per_turn = {}
    for path in sorted(glob.glob("history/merc-*.jsonl")):
        with open(path) as f:
            for line in f:
                try:
                    r = json.loads(line)
                    per_turn[r["turn"]] = m.num(r["items"]["garments"][3])
                except (ValueError, KeyError, IndexError, TypeError):
                    continue
    last = [per_turn[t] for t in sorted(per_turn)[-SALES_WINDOW:]]
    return sum(last) / len(last) if len(last) >= 6 else None


def targets(t, other_thread):
    """Stockpile targets = STOCK_TURNS x what the next step uses per turn."""
    C = CHAIN
    return {
        "cloth": STOCK_TURNS * t["sew"] * C["sew"]["in"],
        "thread": STOCK_TURNS * (t["weave"] * C["weave"]["in"] + other_thread),
        "flax fibres": STOCK_TURNS * t["spin"] * C["spin"]["in"],
    }


def plan(sizes, other_thread, sales, stocks=None, mode="HOLD"):
    """Pull model: sew what sells, each step upstream feeds the next, plus a
    top-up per step while its stockpile is below target and mode is FILLING."""
    s, C = sizes, CHAIN
    stocks = stocks or {}
    want = sales + HOUSEHOLD_GARMENTS if sales else s["sew"] * C["sew"]["out"]
    sew = min(s["sew"], want * SALES_MARGIN / C["sew"]["out"])
    base = {"sew": sew, "weave": sew * C["sew"]["in"] / C["weave"]["out"]}
    base["spin"] = (base["weave"] * C["weave"]["in"] + other_thread) / C["spin"]["out"]
    base["ret"] = base["spin"] * C["spin"]["in"] / C["ret"]["out"]
    tg = targets(base, other_thread)

    def top(item):
        if mode == "FILLING" and stocks.get(item, 0) < tg[item]:
            return BUFFERS[item]["fill"]
        return 0
    weave = min(s["weave"], (sew * C["sew"]["in"] + top("cloth")) / C["weave"]["out"])
    spin = min(s["spin"], (weave * C["weave"]["in"] + other_thread + top("thread")) / C["spin"]["out"])
    ret = min(s["ret"], (spin * C["spin"]["in"] + top("flax fibres")) / C["ret"]["out"])
    flax = min(s["flax"], ret * C["ret"]["in"] / C["flax"]["out"])
    # if plots cap a step upstream, the buffers cover the gap; the alert tells us
    t = {"sew": sew, "weave": weave, "spin": spin, "ret": ret, "flax": flax}
    return {k: round(v, 2) for k, v in t.items()}, tg


def buffer_mode(stocks, last_mode, tg, cash):
    if cash < FILL_CASH_MIN:
        return "HOLD"
    low = any(stocks.get(i, 0) < tg[i] * LOW_FRACTION for i in BUFFERS)
    full = all(stocks.get(i, 0) >= tg[i] for i in BUFFERS)
    if low:
        return "FILLING"
    if full:
        return "FULL"
    if last_mode in (None, "HOLD"):
        return "FILLING"      # cash is back and stock is below target: top up
    return last_mode


def main():
    blds = {k: m.get("/buildings/%s" % v["id"]) for k, v in CHAIN.items()}
    sizes = {k: int(m.num(b.get("size"))) for k, b in blds.items()}
    cur = {k: m.num((b.get("producer") or {}).get("target")) for k, b in blds.items()}
    recipes = {k: (b.get("producer") or {}).get("recipe") for k, b in blds.items()}

    store = m.get("/buildings/%s" % STORE)
    inv = (store.get("storage") or {}).get("inventory") or {}
    flows = inv.get("previous_flows") or {}
    holds = inv.get("holdings") or {}
    # thread used by anything other than the weavery (household net duty)
    other_thread = max(OTHER_THREAD_MIN, m.num((flows.get("thread") or {}).get("consumption")) - cur["weave"] * CHAIN["weave"]["in"])

    try:
        with open(STATE) as f:
            saved = json.load(f)
    except (OSError, ValueError):
        saved = None
    # state file: {"sizes": {...}, "mode": "FILLING"|"FULL"}; older files held just the sizes
    if saved and "sizes" in saved:
        last, last_mode = saved["sizes"], saved.get("mode")
    else:
        last, last_mode = saved, None

    assets = (inv.get("account") or {}).get("assets") or {}
    stocks = {i: m.num((assets.get(i) or {}).get("balance")) for i in BUFFERS}
    cash = m.num(m.get("/households/21623").get("cash"))
    sales = garment_sales()
    _, tg = plan(sizes, other_thread, sales, stocks, "HOLD")
    mode = buffer_mode(stocks, last_mode, tg, cash)
    new, tg = plan(sizes, other_thread, sales, stocks, mode)
    changed = last is not None and last != sizes
    mode_changed = mode != last_mode
    print("sizes:", sizes, "(last seen: %s)" % last)
    print("cash: %.0f (fill only above %d) | garments sold/turn (avg %d turns): %s" % (
        cash, FILL_CASH_MIN, SALES_WINDOW, "%.1f" % sales if sales else "no history"))
    print("stocks:", {k: round(v) for k, v in stocks.items()}, "targets (%d turns):" % STOCK_TURNS,
          {k: round(v) for k, v in tg.items()})
    print("mode: %s (last: %s)" % (mode, last_mode))
    print("current targets:", cur)
    print("planned targets:", new, "| other thread use %.1f" % other_thread)
    print("garments/turn: %.1f -> %.1f" % (cur["sew"] * 41, new["sew"] * 41))

    def save():
        with open(STATE, "w") as f:
            json.dump({"sizes": sizes, "mode": mode}, f)

    os.makedirs("state", exist_ok=True)
    if last is None:
        save()
        print("first run: saved sizes, no changes made")
        return
    if not (changed or mode_changed or FORCE):
        print("no expansion finished and buffer mode unchanged: nothing to do")
        return
    if any(not r for r in recipes.values()):
        print("a chain building is stopped (%s): not rebalancing" % recipes)
        return

    moves = [(k, cur[k], new[k]) for k in CHAIN if abs(new[k] - cur[k]) >= MIN_CHANGE]
    d_lab = sum((n - c) * CHAIN[k]["labour"] for k, c, n in moves)
    d_tools = sum((n - c) * CHAIN[k]["tools"] for k, c, n in moves)
    why = []
    if changed:
        why.append("expansion finished: " + ", ".join(
            "%s %s->%s plots" % (k, last.get(k), sizes[k]) for k in CHAIN if last.get(k) != sizes[k]))
    if mode_changed:
        why.append("mode %s -> %s (cash %.0f; %s)" % (last_mode, mode, cash, ", ".join(
            "%s %.0f/%.0f" % (i, stocks[i], tg[i]) for i in BUFFERS)))
    lines = ["**Chain rebalanced** (%s)" % ("; ".join(why) or "forced")]
    lines += ["- %s %.2fx -> %.2fx" % (k, c, n) for k, c, n in moves] or ["- targets already right"]
    lines.append("- garments %.1f -> %.1f/turn, labour %+.0f/turn, tools %+.1f/turn" % (
        cur["sew"] * 41, new["sew"] * 41, d_lab, d_tools))

    if LIVE:
        errors = []
        for k, c, n in moves:
            ok, res = send("PUT", "/buildings/%s/producer" % CHAIN[k]["id"],
                           {"target": "%.3f" % n, "autoset_buying": False, "autoset_selling": False, "allow_overprod": False})
            if not ok:
                errors.append("%s target: %s" % (k, res))

        def bump(item, field, delta, idx=0):
            ms = [{kk: vv for kk, vv in x.items() if kk != "result"} for x in (holds.get(item) or {}).get("managers") or []]
            if not ms or len(ms) <= idx:
                return
            ms[idx][field] = max(0, round(m.num(ms[idx].get(field)) + delta))
            ok, res = send("PATCH", "/buildings/%s/storage/inventory/%s" % (STORE, urllib.parse.quote(item, safe="")), {"managers": ms})
            if not ok:
                errors.append("%s order: %s" % (item, res))
            else:
                lines.append("- %s %s -> %s" % (item, field, ms[idx][field]))

        if abs(d_lab) >= 1:
            bump("labour", "buy_volume", d_lab)
        if abs(d_tools) >= 1:
            bump("tools", "buy_volume", d_tools)
        g_ms = (holds.get("garments") or {}).get("managers") or []
        si = next((i for i, x in enumerate(g_ms) if m.num(x.get("sell_volume"))), None)
        if si is not None:
            want = round(new["sew"] * 41 - HOUSEHOLD_GARMENTS)
            bump("garments", "sell_volume", want - m.num(g_ms[si].get("sell_volume")), si)
        if errors:
            lines.append("- **errors:** " + "; ".join(errors))
        save()
        text = "\n".join(lines)
        print(text)
        r = gh("issue", "list", "--label", "merc-status", "--state", "open", "--limit", "1", "--json", "number")
        try:
            num = str(json.loads(r.stdout or "[]")[0]["number"])
        except (ValueError, IndexError, KeyError):
            num = "1"
        gh("issue", "comment", num, "--body", text)
    else:
        print("\n".join(lines))
        print("(dry run: nothing sent)")


if __name__ == "__main__":
    try:
        main()
    except SystemExit as e:          # merc_status4.get exits on API errors / turn in progress
        print("balancer skipped:", e)
