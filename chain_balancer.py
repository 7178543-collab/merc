#!/usr/bin/env python3
"""Keep the flax -> retting -> spinning -> weaving -> sewing chain in balance.

Runs hourly from the merc-actor workflow. It only ACTS when a chain building's
size (plot count) has changed since the last run, i.e. an expansion just
finished, so it never fights manual tweaks made in between. When it acts it:

  1. works out the most garments the current plots can support,
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


def plan(sizes, other_thread, thread_stock=0.0):
    """Most garments the plots allow, then the targets that feed exactly that."""
    s = sizes
    ret_cap = min(s["ret"], s["flax"] * CHAIN["flax"]["out"] / CHAIN["ret"]["in"])
    spin_cap = min(s["spin"], ret_cap * CHAIN["ret"]["out"] / CHAIN["spin"]["in"])
    buffer = thread_stock / 40.0   # let thread stock cover a small deficit (~40 turns)
    cloth_cap = min(s["weave"] * CHAIN["weave"]["out"], spin_cap * CHAIN["spin"]["out"] + buffer - other_thread)
    sew = min(s["sew"], max(0, cloth_cap) / CHAIN["sew"]["in"])
    weave = sew * CHAIN["sew"]["in"] / CHAIN["weave"]["out"]
    spin = min(s["spin"], (weave * CHAIN["weave"]["in"] + other_thread) / CHAIN["spin"]["out"])
    ret = spin * CHAIN["spin"]["in"] / CHAIN["ret"]["out"]
    flax = ret * CHAIN["ret"]["in"] / CHAIN["flax"]["out"]
    t = {"sew": sew, "weave": weave, "spin": min(spin, s["spin"]), "ret": min(ret, s["ret"]), "flax": min(flax, s["flax"])}
    return {k: round(v, 2) for k, v in t.items()}


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
            last = json.load(f)
    except (OSError, ValueError):
        last = None

    thread_stock = m.num(((inv.get("account") or {}).get("assets") or {}).get("thread", {}).get("balance"))
    new = plan(sizes, other_thread, thread_stock)
    changed = last is not None and last != sizes
    print("sizes:", sizes, "(last seen: %s)" % last)
    print("current targets:", cur)
    print("planned targets:", new, "| other thread use %.1f" % other_thread)
    print("garments/turn: %.1f -> %.1f" % (cur["sew"] * 41, new["sew"] * 41))

    os.makedirs("state", exist_ok=True)
    if last is None:
        with open(STATE, "w") as f:
            json.dump(sizes, f)
        print("first run: saved sizes, no changes made")
        return
    if not (changed or FORCE):
        print("no expansion finished since last run: nothing to do")
        return
    if any(not r for r in recipes.values()):
        print("a chain building is stopped (%s): not rebalancing" % recipes)
        return

    moves = [(k, cur[k], new[k]) for k in CHAIN if abs(new[k] - cur[k]) >= MIN_CHANGE]
    d_lab = sum((n - c) * CHAIN[k]["labour"] for k, c, n in moves)
    d_tools = sum((n - c) * CHAIN[k]["tools"] for k, c, n in moves)
    lines = ["**Chain rebalanced** (expansion finished: %s)" % ", ".join(
        "%s %s->%s plots" % (k, last.get(k), sizes[k]) for k in CHAIN if last.get(k) != sizes[k])]
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
        with open(STATE, "w") as f:
            json.dump(sizes, f)
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
