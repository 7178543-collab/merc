#!/usr/bin/env python3
"""Prestige rules (Taylor, Oct 8 2026): turn idle cash into prestige income, which drains into
legacy (the leaderboard score) at ~0.5% of total prestige per turn.

Rule 1, mansion banquet:
  ON  when cash > 15,000 and profit summed over the last 24 turns > 0 (Growth mode)
  OFF when cash < 10,000 (drops out of Growth)  -- hysteresis in between keeps the current state
  ON  = mansion "hold banquet 1 (fish)" at 1x (+4.2 prestige/turn; 35 labour, 15 beer, 5.5 cured fish)
        + storehouse cured fish buy 6/turn @ max 24.60, stock to 20
  OFF = mansion target 0 + cured fish buy off
Only sends a change when the game differs from the wanted state; every change is verified
and logged to state/order_queue_done.jsonl (source "prestige_rules").

    python prestige_rules.py          # dry run: prints the decision
    python prestige_rules.py --live   # applies it
"""
import glob
import json
import os
import sys

import merc_status4 as m
import order_queue as q

LIVE = "--live" in sys.argv
HERE = os.path.dirname(os.path.abspath(__file__))
MANSION = "152002388"
RECIPE = "hold banquet 1 (fish)"
FISH = "cured fish"
FISH_ORDER = {"buy_volume": 6, "buy_price": "24.60", "max_holding": 20}
ON_CASH, OFF_CASH, PROFIT_TURNS = 15000, 10000, 24


def profit_last_turns(n):
    """Sum of profit over the last n distinct turns, from the bot's history files."""
    by_turn = {}
    for path in sorted(glob.glob(os.path.join(HERE, "history", "merc-*.jsonl")))[-2:]:
        for line in open(path):
            try:
                d = json.loads(line)
            except ValueError:
                continue
            if d.get("turn") is not None and d.get("profit") is not None:
                by_turn[d["turn"]] = d["profit"]
    turns = sorted(by_turn)[-n:]
    return sum(by_turn[t] for t in turns), len(turns)


_LINES = []


def say(*a):
    line = " ".join(str(x) for x in a)
    print(line)
    _LINES.append(line)


def main():
    if not (m.USER and m.TOKEN):
        say("prestige_rules: no credentials")
        return
    pl = m.get("/player") or {}
    biz = m.get("/businesses/%s" % (pl.get("household") or {})["business_ids"][0]) or {}
    cash = m.num(((biz.get("account") or {}).get("assets") or {}).get("money", {}).get("balance"))
    profit, n = profit_last_turns(PROFIT_TURNS)
    prod = q.read_producer(MANSION)
    full = (m.get("/buildings/%s" % MANSION) or {}).get("producer") or {}
    say("mansion producer: recipe=%s target=%s provider=%s limited=%s last_op=%s" % (
        full.get("recipe"), full.get("target"), full.get("provider_id"), full.get("limited"),
        json.dumps(full.get("previous_operation"))[:200]))
    running = prod.get("recipe") == RECIPE and m.num(prod.get("target")) > 0

    if cash < OFF_CASH:
        want_on, why = False, "cash %.0f under %d" % (cash, OFF_CASH)
    elif cash > ON_CASH and profit > 0 and n >= PROFIT_TURNS // 2:
        want_on, why = True, "cash %.0f over %d, profit %+.0f over %d turns" % (cash, ON_CASH, profit, n)
    else:
        want_on, why = running, "in between (cash %.0f, profit %+.0f over %d turns): keep as is" % (cash, profit, n)

    fish_mgrs = q._store_managers(q.STORE, FISH)
    fish_on = any(m.num(mg.get("buy_volume")) > 0 for mg in fish_mgrs)
    say("prestige_rules: banquet %s -> want %s (%s); fish buy %s" % (
        "on" if running else "off", "on" if want_on else "off", why, "on" if fish_on else "off"))

    todo = []
    if want_on:
        if not fish_on:
            todo.append({"item": FISH, "tier": 0, "set": FISH_ORDER, "note": "banquet rule: " + why})
        if not running:
            todo.append({"building": MANSION, "producer": {"recipe": RECIPE, "target": 1}, "note": "banquet rule: " + why})
    else:
        if running:
            todo.append({"building": MANSION, "producer": {"recipe": RECIPE, "target": 0}, "note": "banquet rule: " + why})
        if fish_on:
            todo.append({"item": FISH, "tier": 0, "set": {"buy_volume": 0}, "note": "banquet rule: " + why})

    for e in todo:
        if not LIVE:
            say("  would send:", json.dumps(e))
            continue
        try:
            r = q.apply_entry(e)
        except Exception as ex:
            r = dict(ok=False, error="%s: %s" % (type(ex).__name__, ex))
        q.log(e, r, source="prestige_rules")
        say("  %s -> %s" % (e.get("item") or e.get("building"), "OK" if r.get("ok") else "FAILED %s %s" % (r.get("error"), r.get("tries", ""))))


if __name__ == "__main__":
    import datetime
    try:
        main()
    except Exception as ex:
        say("prestige_rules crashed: %s: %s" % (type(ex).__name__, ex))
    with open(os.path.join(HERE, "state", "prestige_rules_last.txt"), "w") as f:
        f.write(datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds") + "\n" + "\n".join(_LINES) + "\n")
