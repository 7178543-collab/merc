#!/usr/bin/env python3
"""Keep the flax -> retting -> spinning -> weaving -> sewing chain in balance.

Runs hourly from the merc-actor workflow. It only ACTS when (a) a chain
building's size (plot count) has changed since the last run, i.e. an expansion
just finished, or (b) the buffer mode flips (FILLING <-> FULL, see BUFFERS).
Otherwise it never fights manual tweaks made in between. When it acts it:

  1. works out the most garments the current plots can support, holding back
     a little thread/cloth each turn while the stockpiles are below target
     (FILLING) and running flax/retting/spinning flat out to refill them,
  2. sets every chain building's production target to feed exactly that,
  3. adjusts the storehouse labour buy by the labour difference, the tools
     buy by the tools difference, and the garments sell volume to the new
     output, and
  4. posts what it did as a comment on the hourly status issue.

    python chain_balancer.py            # dry run: print the plan
    python chain_balancer.py --live     # apply it (only if sizes changed)
    python chain_balancer.py --live --force   # apply even if sizes didn't change

State (last seen sizes) lives in state/chain_sizes.json, committed by the workflow.
"""
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

# Stockpiles between chain steps, so one bad turn upstream doesn't empty the chain.
# target = stock we want held; fill = units per turn held back while below target.
# FILLING starts when any stock drops under LOW_FRACTION of its target and ends when
# every stock is back at target (hysteresis, so it doesn't flip every run).
BUFFERS = {
    "flax fibres": {"target": 200, "fill": 0},    # filled by flax/retting headroom, not held back
    "thread":      {"target": 450, "fill": 15},
    "cloth":       {"target": 400, "fill": 10},
}
LOW_FRACTION = 0.5
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


def plan(sizes, other_thread, stocks=None, filling=False):
    """Most garments the plots allow, with stockpile top-up while FILLING.

    Upstream (flax -> retting -> spinning) runs as hard as the plots allow so
    fibres/thread build up; weaving and sewing are set to what is left after
    holding back each buffer's 'fill' amount (only while FILLING)."""
    s, C = sizes, CHAIN
    stocks = stocks or {}
    hold = lambda item: BUFFERS[item]["fill"] if filling and stocks.get(item, 0) < BUFFERS[item]["target"] else 0
    # upstream flat out, limited by plots
    flax = s["flax"]
    ret = min(s["ret"], flax * C["flax"]["out"] / C["ret"]["in"])
    spin = min(s["spin"], ret * C["ret"]["out"] / C["spin"]["in"])
    # downstream: use what's made, minus nets thread and the top-ups
    thread_for_weave = spin * C["spin"]["out"] - other_thread - hold("thread")
    weave = min(s["weave"], max(0, thread_for_weave) / C["weave"]["in"])
    cloth_for_sew = weave * C["weave"]["out"] - hold("cloth")
    sew = min(s["sew"], max(0, cloth_for_sew) / C["sew"]["in"])
    if not filling:
        # stockpiles full: don't overproduce upstream, just feed what's used
        weave = sew * C["sew"]["in"] / C["weave"]["out"]
        spin = min(s["spin"], (weave * C["weave"]["in"] + other_thread) / C["spin"]["out"])
        fib_need = spin * C["spin"]["in"] + (0 if stocks.get("flax fibres", 0) >= BUFFERS["flax fibres"]["target"] else 5)
        ret = min(s["ret"], fib_need / C["ret"]["out"])
        flax = min(s["flax"], ret * C["ret"]["in"] / C["flax"]["out"])
    t = {"sew": sew, "weave": weave, "spin": spin, "ret": ret, "flax": flax}
    return {k: round(v, 2) for k, v in t.items()}


def buffer_mode(stocks, last_mode):
    low = any(stocks.get(i, 0) < b["target"] * LOW_FRACTION for i, b in BUFFERS.items())
    full = all(stocks.get(i, 0) >= b["target"] for i, b in BUFFERS.items())
    if low:
        return "FILLING"
    if full:
        return "FULL"
    return last_mode or "FILLING"


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
    other_thread = max(0.0, m.num((flows.get("thread") or {}).get("consumption")) - cur["weave"] * CHAIN["weave"]["in"])

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
    mode = buffer_mode(stocks, last_mode)
    new = plan(sizes, other_thread, stocks, filling=(mode == "FILLING"))
    changed = last is not None and last != sizes
    mode_changed = mode != last_mode
    print("sizes:", sizes, "(last seen: %s)" % last)
    print("stocks:", {k: round(v) for k, v in stocks.items()}, "targets:", {k: b["target"] for k, b in BUFFERS.items()})
    print("buffer mode: %s (last: %s)" % (mode, last_mode))
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
        why.append("stockpiles %s -> %s (%s)" % (last_mode, mode, ", ".join(
            "%s %.0f/%d" % (i, stocks[i], BUFFERS[i]["target"]) for i in BUFFERS)))
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
