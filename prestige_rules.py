#!/usr/bin/env python3
"""Prestige rules (Taylor, Oct 8 2026): turn idle cash into prestige income, which drains into
legacy (the leaderboard score) at ~0.5% of total prestige per turn.

Rule 1, mansion banquet (cash-only since Oct 10, Taylor: cash is worth nothing after the season
  ends 30 Nov, so a noisy 12-turn profit dip shouldn't cost 4.2 prestige/turn):
  ON  when cash > 15,000
  OFF when cash < 10,000
  in between keeps the current state, so it can't flap. Profit sums are still logged for context.
  ON  = mansion "hold banquet 1 (fish)" at 1x (+4.2 prestige/turn; 35 labour, 15 beer, 5.5 cured fish)
        + storehouse cured fish buy 6/turn @ max 24.60, stock to 20
  OFF = mansion target 0 + cured fish buy off
Rule 2, Tenants (moved here from the Ops panel Oct 9, so it no longer depends on a browser tab):
  buy one Tenants level (+5) when free prestige covers the cost (50 x (level - 2)) and prestige
  income is positive, up to TENANTS_MAX_LEVEL. Management has room for ~8 more farmstead plots, so
  only one more level is useful. After buying, writes state/needs_you.json: the +5 farmstead plots
  are a map pick in-game (no API for it yet), and alerts.py puts that in the status email.

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
ON_CASH, OFF_CASH, PROFIT_TURNS, GUARD_TURNS = 15000, 10000, 24, 12
TENANTS_MAX_LEVEL = 11
NEEDS_YOU = os.path.join(HERE, "state", "needs_you.json")


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


def tenants_rule():
    pl = m.get("/player") or {}
    hid = (pl.get("household") or {}).get("id")
    hh = m.get("/households/%s" % hid) or {}
    pb = hh.get("prestige_board") or {}
    level = int(m.num(pb.get("tenants_level")))
    total, allocated = m.num(hh.get("prestige")), m.num(pb.get("allocated"))
    free = total - allocated
    rate = sum(m.num(x.get("impact")) for x in (hh.get("prestige_impacts") or pb.get("prestige_impacts") or []))
    cost = 50 * (level - 2)
    say("tenants: level %d (max %d), cost %d, free %.1f, rate %+.2f" % (level, TENANTS_MAX_LEVEL, cost, free, rate))
    if level >= TENANTS_MAX_LEVEL or cost <= 0 or free < cost or rate <= 0:
        return
    if not LIVE:
        say("  would buy Tenants level %d for %d" % (level + 1, cost))
        return
    ok, status, body = q._req("POST", "/households/%s/prestige/allocate" % hid, {"track": "tenants", "cost": str(cost)})
    after = int(m.num(((m.get("/households/%s" % hid) or {}).get("prestige_board") or {}).get("tenants_level")))
    good = after == level + 1
    q.log({"prestige": "tenants", "cost": cost, "note": "tenants rule"},
          dict(ok=good, status=status, body=body[:200], before=level, after=after), source="prestige_rules")
    say("  bought Tenants level %d for %d -> %s" % (level + 1, cost, "OK" if good else "FAILED %s %s" % (status, body[:150])))
    if good:
        with open(NEEDS_YOU, "w") as f:
            json.dump({"what": "Expand the farmstead +5 plots (map: farmstead > modify > expand). Tenants level %d was bought for %d prestige." % (after, cost),
                       "since_turn": None}, f)


def main():
    if not (m.USER and m.TOKEN):
        say("prestige_rules: no credentials")
        return
    pl = m.get("/player") or {}
    biz = m.get("/businesses/%s" % (pl.get("household") or {})["business_ids"][0]) or {}
    cash = m.num(((biz.get("account") or {}).get("assets") or {}).get("money", {}).get("balance"))
    profit, n = profit_last_turns(PROFIT_TURNS)
    recent, rn = profit_last_turns(GUARD_TURNS)
    prod = q.read_producer(MANSION)
    full = (m.get("/buildings/%s" % MANSION) or {}).get("producer") or {}
    say("mansion producer: recipe=%s target=%s provider=%s limited=%s last_op=%s" % (
        full.get("recipe"), full.get("target"), full.get("provider_id"), full.get("limited"),
        json.dumps(full.get("previous_operation"))[:200]))
    running = (prod.get("recipe") == RECIPE and m.num(prod.get("target")) > 0
               and str(prod.get("provider_id")) == q.STORE)

    if cash < OFF_CASH:
        want_on, why = False, "cash %.0f under %d" % (cash, OFF_CASH)
    elif cash > ON_CASH:
        want_on, why = True, "cash %.0f over %d (profit %+.0f over %d turns, %+.0f over %d)" % (cash, ON_CASH, profit, n, recent, rn)
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
            todo.append({"building": MANSION, "producer": {"recipe": RECIPE, "target": 1, "provider_id": q.STORE}, "note": "banquet rule: " + why})
    else:
        if running:
            todo.append({"building": MANSION, "producer": {"recipe": RECIPE, "target": 0}, "note": "banquet rule: " + why})
        if fish_on:
            todo.append({"item": FISH, "tier": 0, "set": {"buy_volume": 0}, "note": "banquet rule: " + why})

    try:
        tenants_rule()
    except Exception as ex:
        say("tenants rule crashed: %s: %s" % (type(ex).__name__, ex))

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
