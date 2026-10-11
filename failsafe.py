#!/usr/bin/env python3
"""Cash failsafe (Taylor, Oct 11 2026, after losing ~20k overnight).

Runs every bot run (merc.yml) and after every queue run (order-queue.yml). It acts on its own;
nothing here waits for a person.

1. Labour waste guard (any level): if bought labour expired last turn (> LABOUR_WASTE), cut the
   labour buy to what was actually used (consumption - own production + buffer). Unlike the
   actor's auto-trim, this is NOT skipped while the chain is stalled or after a manual change:
   that blind spot let ~600 labour/turn expire on Oct 11.

2. Burn-rate brake, from cash now vs cash BURN_TURNS turns ago (history files):
   level 0 OK
   level 1 WATCH  burn >= WATCH_BURN  or cash < WATCH_CASH   -> alert only
   level 2 BRAKE  burn >= BRAKE_BURN  or cash < BRAKE_CASH   -> switch off discretionary buys
                  (build materials, church/gear stockpiles) and cap the labour price
   level 3 STOP   cash < STOP_CASH                           -> also limestone + banquet fish
   Paused orders are saved in state/failsafe.json ("paused": item -> managers before) and are
   NOT restored automatically: restoring is a deliberate call (Taylor or the daily check-in),
   so a drain can't switch itself back on. To restore: queue the saved managers back, then
   delete the item from "paused".

The state file also feeds alerts.py (top alert) and so the phone app.

    python failsafe.py          # dry run: prints the decision
    python failsafe.py --live   # applies it
"""
import datetime
import glob
import json
import math
import os
import sys

import merc_status4 as m
import order_queue as q

LIVE = "--live" in sys.argv
HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "state", "failsafe.json")

BURN_TURNS = 12
WATCH_BURN, BRAKE_BURN = 5000, 9000
WATCH_CASH, BRAKE_CASH, STOP_CASH = 15000, 10000, 6000
LABOUR_WASTE, LABOUR_BUFFER = 30, 10
LABOUR_PRICE_CAP = "2.00"
# tool guard (Oct 11: tools ran dry at 5am, camp + retting stopped, their labour expired)
CAMP, CAMP_RECIPE, CAMP_FULL, CAMP_SLOW = "151402406", "split timber 2", 20, 10
TOOLS_LOW_TURNS, TOOLS_OK_TURNS = 3, 8   # slow the camp under 3 turns of use, restore over 8
TOOLS_ORDER = {"buy_volume": 31, "buy_price": "6.20", "max_holding": 200}   # ~25 turns of normal use          # brake level: labour bid cap (market ~1.80)

# switched off at BRAKE: one-off build materials and stockpiles, never the production chain
BRAKE_ITEMS = ["wheels", "timber", "furniture", "candles", "jewellery", "light armour", "arms",
               "tiles", "nails", "bricks", "tar"]
STOP_ITEMS = ["limestone", "cured fish"]


def say(*a):
    print(" ".join(str(x) for x in a))


def load_state():
    try:
        return json.load(open(STATE))
    except (FileNotFoundError, ValueError):
        return {"level": 0, "paused": {}}


def cash_history():
    """{turn: cash} from the bot's history lines (last line per turn wins)."""
    by_turn = {}
    for path in sorted(glob.glob(os.path.join(HERE, "history", "merc-*.jsonl")))[-2:]:
        for line in open(path):
            try:
                d = json.loads(line)
            except ValueError:
                continue
            if d.get("turn") is not None and d.get("cash") is not None:
                by_turn[int(d["turn"])] = float(d["cash"])
    return by_turn


def level_for(cash, burn):
    if cash < STOP_CASH:
        return 3
    if burn >= BRAKE_BURN or cash < BRAKE_CASH:
        return 2
    if burn >= WATCH_BURN or cash < WATCH_CASH:
        return 1
    return 0


def labour_guard(actions):
    b = m.get("/buildings/%s" % q.STORE) or {}
    inv = (b.get("storage") or {}).get("inventory") or {}
    f = (inv.get("previous_flows") or {}).get("labour") or {}
    exp = m.num(f.get("expiration"))
    mgrs = q._store_managers(q.STORE, "labour")
    idx = next((i for i, mg in enumerate(mgrs) if m.num(mg.get("buy_volume"))), None)
    if idx is None:
        return
    cur = m.num(mgrs[idx].get("buy_volume"))
    need = int(math.ceil(max(0, m.num(f.get("consumption")) + m.num(f.get("shortfall"))
                         - m.num(f.get("production")) + LABOUR_BUFFER)))
    say("labour: buy %d, last turn expired %.0f, used %.0f, own %.0f -> need %d" % (
        cur, exp, m.num(f.get("consumption")), m.num(f.get("production")), need))
    if exp > LABOUR_WASTE and need < cur - 5:
        actions.append({"item": "labour", "tier": idx, "set": {"buy_volume": need},
                        "note": "failsafe: %.0f bought labour expired last turn; buy %d -> %d" % (exp, cur, need)})


def tool_guard(actions, st):
    """Keep tools from running dry: bid at the cap while under ~25 turns of use, and slow the
    logging camp (the biggest tool user we can spare) under TOOLS_LOW_TURNS of use, so retting and
    the builds keep their tools; put the camp back once stock is over TOOLS_OK_TURNS."""
    b = m.get("/buildings/%s" % q.STORE) or {}
    inv = (b.get("storage") or {}).get("inventory") or {}
    f = (inv.get("previous_flows") or {}).get("tools") or {}
    held = m.num((((inv.get("account") or {}).get("assets") or {}).get("tools") or {}).get("balance"))
    use = max(m.num(f.get("consumption")), 7.0)      # normal use ~7/turn; a stalled turn reads 0
    turns = held / use
    say("tools: held %.1f, use %.1f/turn -> %.1f turns" % (held, use, turns))
    mgrs = q._store_managers(q.STORE, "tools")
    top = mgrs[0] if mgrs else {}
    if m.num(top.get("buy_price")) < float(TOOLS_ORDER["buy_price"]) or m.num(top.get("buy_volume")) < TOOLS_ORDER["buy_volume"]:
        actions.append({"item": "tools", "tier": 0, "set": TOOLS_ORDER,
                        "note": "tool guard: keep the tool bid at the cap (%.1f turns of stock)" % turns})
    prod = q.read_producer(CAMP)
    tgt = m.num(prod.get("target"))
    if turns < TOOLS_LOW_TURNS and tgt > CAMP_SLOW:
        st["camp_slowed"] = True
        actions.append({"building": CAMP, "producer": {"recipe": CAMP_RECIPE, "target": CAMP_SLOW, "provider_id": q.STORE},
                        "note": "tool guard: tools at %.1f turns of use; camp %g -> %d until stock recovers" % (turns, tgt, CAMP_SLOW)})
    elif st.get("camp_slowed") and turns > TOOLS_OK_TURNS:
        st["camp_slowed"] = False
        if tgt < CAMP_FULL:
            actions.append({"building": CAMP, "producer": {"recipe": CAMP_RECIPE, "target": CAMP_FULL, "provider_id": q.STORE},
                            "note": "tool guard: tools back to %.1f turns; camp back to %d" % (turns, CAMP_FULL)})


def main():
    if not (m.USER and m.TOKEN):
        say("failsafe: no credentials")
        return
    pl = m.get("/player") or {}
    biz = m.get("/businesses/%s" % (pl.get("household") or {})["business_ids"][0]) or {}
    cash = m.num(((biz.get("account") or {}).get("assets") or {}).get("money", {}).get("balance"))
    hist = cash_history()
    turns = sorted(hist)
    ref = hist[turns[-BURN_TURNS - 1]] if len(turns) > BURN_TURNS else (hist[turns[0]] if turns else cash)
    burn = ref - cash
    lvl = level_for(cash, burn)
    st = load_state()
    names = ["OK", "WATCH", "BRAKE", "STOP"]
    say("failsafe: cash %.0f, burn %.0f over %d turns -> level %d %s (was %s)" % (
        cash, burn, BURN_TURNS, lvl, names[lvl], st.get("level")))

    actions = []
    try:
        labour_guard(actions)
    except (Exception, SystemExit) as ex:
        say("labour guard crashed: %s: %s" % (type(ex).__name__, ex))

    try:
        tool_guard(actions, st)
    except (Exception, SystemExit) as ex:
        say("tool guard crashed: %s: %s" % (type(ex).__name__, ex))

    paused = st.get("paused") or {}
    if lvl >= 2:
        items = BRAKE_ITEMS + (STOP_ITEMS if lvl >= 3 else [])
        for item in items:
            try:
                mgrs = q._store_managers(q.STORE, item)
            except (Exception, SystemExit):
                continue
            for i, mg in enumerate(mgrs):
                if m.num(mg.get("buy_volume")) > 0:
                    paused.setdefault(item, mgrs)
                    actions.append({"item": item, "tier": i, "set": {"buy_volume": 0},
                                    "note": "failsafe level %d: discretionary buy off (burn %.0f/%d turns, cash %.0f)" % (lvl, burn, BURN_TURNS, cash)})
        lab = q._store_managers(q.STORE, "labour")
        for i, mg in enumerate(lab):
            if m.num(mg.get("buy_volume")) > 0 and m.num(mg.get("buy_price")) > float(LABOUR_PRICE_CAP):
                actions.append({"item": "labour", "tier": i, "set": {"buy_price": LABOUR_PRICE_CAP},
                                "note": "failsafe level %d: labour bid capped at %s" % (lvl, LABOUR_PRICE_CAP)})

    results = []
    for e in actions:
        if not LIVE:
            say("would send:", json.dumps(e))
            continue
        try:
            r = q.apply_entry(e)
        except (Exception, SystemExit) as ex:
            r = dict(ok=False, error="%s: %s" % (type(ex).__name__, ex))
        q.log(e, r, source="failsafe")
        results.append((e, r.get("ok")))
        say("failsafe sent %s -> %s" % (json.dumps(e.get("set")), "OK" if r.get("ok") else "FAILED"))

    now = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    new = {"level": lvl, "name": names[lvl], "cash": round(cash), "burn": round(burn),
           "burn_turns": BURN_TURNS, "t": now,
           "since": st.get("since") if st.get("level") == lvl else now,
           "paused": paused, "camp_slowed": st.get("camp_slowed", False),
           "last_actions": [dict(set=e.get("set"), item=e.get("item"), ok=ok) for e, ok in results] or st.get("last_actions", [])}
    if LIVE:
        with open(STATE, "w") as f:
            json.dump(new, f, indent=1)
            f.write("\n")


if __name__ == "__main__":
    main()
