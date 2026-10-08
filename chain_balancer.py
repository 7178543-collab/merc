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

# ---------------------------------------------------------------- OPERATING MODE THRESHOLDS
# Shared with merc-ops.user.js and merc_actor.py (same numbers, no shared state file).
# Hysteresis: leave SOS only when cash > SOS_EXIT_CASH and profit positive SOS_EXIT_PROFIT_TURNS;
# leave GROWTH when cash < GROWTH_EXIT_CASH.
MODE = {
    "SOS_CASH": 2000,
    "SOS_SOFT_CASH": 4000,
    "SOS_NEG_TURNS": 3,
    "SOS_EXIT_CASH": 4000,
    "SOS_EXIT_PROFIT_TURNS": 3,
    "STEADY_MAX": 15000,
    "GROWTH_CASH": 15000,
    "GROWTH_PROFIT_TURNS": 24,
    "GROWTH_EXIT_CASH": 10000,
    "FILL_CASH_MIN": 8000,          # STEADY: stockpile top-ups only above this cash
    "OWN_LABOUR": 300,              # SOS: run only what our own labour covers
    "CONSTRUCTION_PACE_STEADY": 25,
    "STOCK_TURNS_CHAIN": 4,
    "SALES_WINDOW": 12,             # was 24; Ops uses 12 — keep in step
    "SALES_MARGIN": 1.05,
    "HOUSEHOLD_GARMENTS": 1.8,
    "MARKET_DEPTH_MULT": 3,
}

# building id, recipe inputs/outputs per 1x (read from the game's production pages)
CHAIN = {
    "flax":  {"id": "151602400",       "labour": 11,  "tools": 0.6, "out": 18},   # plants
    "ret":   {"id": "151802398",       "labour": 25,  "tools": 2,   "in": 90, "out": 35},   # plants -> fibres
    "spin":  {"id": "152202388002007", "labour": 75,  "tools": 0,   "in": 17, "out": 50},   # fibres -> thread
    "weave": {"id": "152202388001005", "labour": 75,  "tools": 0,   "in": 50, "out": 50},   # thread -> cloth
    "sew":   {"id": "152202388000004", "labour": 155, "tools": 0,   "in": 80, "out": 41},   # cloth -> garments
}

# Stockpiles between chain steps, in TURNS of what the next step uses.
# fill = extra units per turn made while below target (and cash allows).
STOCK_TURNS = MODE['STOCK_TURNS_CHAIN']
BUFFERS = {
    "flax fibres": {"fill": 5},
    "thread":      {"fill": 15},
    "cloth":       {"fill": 10},
}
LOW_FRACTION = 0.5       # FILLING starts when a stock is under half its target
FILL_CASH_MIN = MODE['FILL_CASH_MIN']  # below this cash: HOLD (no top-ups, make only what's used)
SALES_WINDOW = MODE['SALES_WINDOW']   # turns of garment sales to average
SALES_MARGIN = MODE['SALES_MARGIN']   # sew 5% over average sales (garment stock covers the rest)
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
    want = sales + MODE['HOUSEHOLD_GARMENTS'] if sales else s["sew"] * C["sew"]["out"]
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


def profit_streak(sign, n):
    """True if the last n history turns all have trading profit with the given sign (+1/-1)."""
    per_turn = {}
    for path in sorted(glob.glob("history/merc-*.jsonl")):
        with open(path) as f:
            for line in f:
                try:
                    r = json.loads(line)
                    # items[*][3] is sale qty; we need value. Prefer explicit profit if present.
                    profit = r.get("profit")
                    if profit is None:
                        # approximate: sum sale_value - purchase_cost if present in flows-like fields
                        continue
                    per_turn[r["turn"]] = 1 if float(profit) >= 0 else -1
                except (ValueError, KeyError, TypeError):
                    continue
    last = [per_turn[t] for t in sorted(per_turn)[-n:]]
    return len(last) >= n and all(x == sign for x in last)


def operating_mode(cash, last_op=None):
    """SOS / STEADY / GROWTH from cash + profit (same thresholds as Ops). No shared state file."""
    last_op = last_op or "STEADY"
    if last_op == "SOS":
        if not (cash > MODE["SOS_EXIT_CASH"] and profit_streak(1, MODE["SOS_EXIT_PROFIT_TURNS"])):
            return "SOS"
    elif last_op == "GROWTH":
        if cash < MODE["GROWTH_EXIT_CASH"]:
            if cash < MODE["SOS_CASH"] or (cash < MODE["SOS_SOFT_CASH"] and profit_streak(-1, MODE["SOS_NEG_TURNS"])):
                return "SOS"
            return "STEADY"
        return "GROWTH"
    if cash < MODE["SOS_CASH"] or (cash < MODE["SOS_SOFT_CASH"] and profit_streak(-1, MODE["SOS_NEG_TURNS"])):
        return "SOS"
    if cash > MODE["GROWTH_CASH"] and profit_streak(1, MODE["GROWTH_PROFIT_TURNS"]):
        return "GROWTH"
    return "STEADY"


def buffer_mode(stocks, last_mode, tg, cash, op_mode="STEADY"):
    # Operating mode gates fill behaviour
    if op_mode == "SOS":
        return "HOLD"
    if op_mode == "STEADY" and cash < FILL_CASH_MIN:
        return "HOLD"
    # GROWTH (and STEADY above FILL_CASH_MIN) may fill
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
    # cash is on the business account; /households has no cash field (read as 0 = SOS forever)
    _pl = m.get("/player") or {}
    _biz = m.get("/businesses/%s" % (_pl.get("household") or {})["business_ids"][0]) or {}
    cash = m.num(((_biz.get("account") or {}).get("assets") or {}).get("money", {}).get("balance"))
    sales = garment_sales()
    # operating mode (SOS/STEADY/GROWTH) from cash + profit; last op from state file if present
    last_op = None
    if saved and isinstance(saved, dict):
        last_op = saved.get("op_mode")
    op_mode = operating_mode(cash, last_op)
    _, tg = plan(sizes, other_thread, sales, stocks, "HOLD")
    mode = buffer_mode(stocks, last_mode, tg, cash, op_mode)
    new, tg = plan(sizes, other_thread, sales, stocks, mode)
    # SOS: cap chain to OWN_LABOUR, sewing first
    if op_mode == "SOS":
        left = MODE["OWN_LABOUR"]
        order = ["sew", "weave", "spin", "ret", "flax"]
        for k in order:
            max_x = left / CHAIN[k]["labour"] if CHAIN[k]["labour"] else new[k]
            new[k] = round(min(new[k], sizes[k], max(0, max_x)), 2)
            left -= new[k] * CHAIN[k]["labour"]
    changed = last is not None and last != sizes
    mode_changed = mode != last_mode
    print("sizes:", sizes, "(last seen: %s)" % last)
    print("cash: %.0f (fill only above %d) | garments sold/turn (avg %d turns): %s" % (
        cash, FILL_CASH_MIN, SALES_WINDOW, "%.1f" % sales if sales else "no history"))
    print("stocks:", {k: round(v) for k, v in stocks.items()}, "targets (%d turns):" % STOCK_TURNS,
          {k: round(v) for k, v in tg.items()})
    print("op_mode: %s | buffer mode: %s (last: %s)" % (op_mode, mode, last_mode))
    print("current targets:", cur)
    print("planned targets:", new, "| other thread use %.1f" % other_thread)
    print("garments/turn: %.1f -> %.1f" % (cur["sew"] * 41, new["sew"] * 41))

    def save():
        with open(STATE, "w") as f:
            json.dump({"sizes": sizes, "mode": mode, "op_mode": op_mode}, f)

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

        if abs(d_lab) >= 1 and op_mode != "SOS":
            bump("labour", "buy_volume", d_lab)
        elif abs(d_lab) >= 1 and op_mode == "SOS":
            lines.append("- labour buy skipped (SOS)")
        if abs(d_tools) >= 1:
            bump("tools", "buy_volume", d_tools)
        g_ms = (holds.get("garments") or {}).get("managers") or []
        si = next((i for i, x in enumerate(g_ms) if m.num(x.get("sell_volume"))), None)
        if si is not None:
            want = round(new["sew"] * 41 - MODE['HOUSEHOLD_GARMENTS'])
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
