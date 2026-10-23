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
WATCH_CASH, BRAKE_CASH, STOP_CASH = 15000, 4000, 2500   # Oct 15: brake 10k -> 8k. At 10k it flapped with cash sitting
# at ~10k: each trip stood v2 down (labour went unmanaged, 146 expired in a turn) and paused the gear slots.
# Oct 18 (Taylor: get on track): brake 8k -> 4k, stop 6k -> 2.5k. Cash sat at ~5.5k in STOP all day with trading back
# in profit (+270-317 a turn): v2 stood down, so nothing reprices, no ship sails, and the household slots ran dry.
# A turn's outflows (labour ~230, taxes 226, household ~120) are ~600, so 2.5k is ~4 turns with no sales at all.
# The burn brake (9k over 12 turns) still catches a fast drain at any cash level.
LABOUR_WASTE, LABOUR_BUFFER = 30, 10
LABOUR_PRICE_CAP = "2.00"
# tool guard (Oct 11: tools ran dry at 5am, camp + retting stopped, their labour expired)
CAMP, CAMP_RECIPE, CAMP_FULL, CAMP_SLOW = "151402406", "split timber 2", 20, 10
TOOLS_LOW_TURNS, TOOLS_OK_TURNS = 3, 8   # slow the camp under 3 turns of use, restore over 8
TOOLS_ORDER = {"buy_volume": 31, "buy_price": "6.20", "max_holding": 200}   # ~25 turns of normal use          # brake level: labour bid cap (market ~1.80)

# switched off at BRAKE: one-off build materials and stockpiles, never the production chain
# Oct 15: tar dropped from the brake. It is the ropewalk's input, not a discretionary buy: the Oct 15 17:10 UTC brake
# paused it, the ropewalk stopped, thread piled 216 -> 402 and the chain's bought labour expired (146 in one turn).
# Oct 18: furniture, candles, light armour and arms dropped from the brake. They feed household sustenance slots
# (prestige every turn: candles alone 3/turn), small and capped buys, not stockpiles; pausing them cost ~4 prestige a
# turn to save ~150 coin. jewellery stays (church stockpile).
BRAKE_ITEMS = ["wheels", "timber", "jewellery", "tiles", "nails", "bricks"]
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


def avg_use(item, turns=12):
    """Average consumption per turn over the last `turns` distinct turns (history files),
    ignoring stalled turns that read 0, so one bad turn can't hide real demand."""
    by_turn = {}
    for path in sorted(glob.glob(os.path.join(HERE, "history", "merc-*.jsonl")))[-2:]:
        for line in open(path):
            try:
                d = json.loads(line)
                by_turn[int(d["turn"])] = float((d.get("items") or {}).get(item, [0, 0, 0])[2] or 0)
            except (ValueError, KeyError, TypeError, IndexError):
                continue
    vals = [by_turn[t] for t in sorted(by_turn)[-turns:] if by_turn[t] > 0]
    return (sum(vals) / len(vals), max(vals)) if vals else (0.0, 0.0)


# bought inputs that stop a building when they run dry (its labour then expires)
INPUTS = {"tools": "logging camp + retting + builds", "grain": "brewery", "firewood": "farmstead/households",
          "fish": "sustenance", "meat": "sustenance", "cured fish": "banquet", "porterage": "ship/sales"}
INPUT_LOW_TURNS = 3
PERISHABLE = {"fish", "meat", "porterage"}     # expire at turn end: bought to need, so a runway in turns means nothing


def input_runway(st):
    """Every run: turns of stock left for each bought input. Under INPUT_LOW_TURNS goes in
    state/failsafe.json "low_inputs" (alerts + the morning check-in read it)."""
    b = m.get("/buildings/%s" % q.STORE) or {}
    inv = (b.get("storage") or {}).get("inventory") or {}
    assets = (inv.get("account") or {}).get("assets") or {}
    flows = inv.get("previous_flows") or {}
    low = {}
    for item, who in INPUTS.items():
        held = m.num((assets.get(item) or {}).get("balance"))
        avg, peak = avg_use(item)
        use = max(avg, m.num((flows.get(item) or {}).get("consumption")))
        if use <= 0:
            continue
        turns = held / use
        bought = m.num((flows.get(item) or {}).get("purchase"))
        if item in PERISHABLE:
            # bought to the turn's need and never held (Oct 14: exact buying; ~0 held is normal). Low only when the buy
            # really fell short last turn: a shortfall, or a purchase under what was used.
            fl = flows.get(item) or {}
            used, short = m.num(fl.get("consumption")), m.num(fl.get("shortfall"))
            if short <= 0.5 and bought >= used - 1:
                continue
            turns = 0.0
        if turns < INPUT_LOW_TURNS and bought < use:
            mgrs = q._store_managers(q.STORE, item)
            bid = max([m.num(mg.get("buy_price")) for mg in mgrs if m.num(mg.get("buy_volume"))] or [0])
            low[item] = "%.1f turns left (held %.0f, use %.1f, bought %.0f, bid %.2f) - feeds %s" % (turns, held, use, bought, bid, who)
            say("LOW INPUT", item, low[item])
    st["low_inputs"] = low


def tool_guard(actions, st):
    """Keep tools from running dry: bid at the cap while under ~25 turns of use, and slow the
    logging camp (the biggest tool user we can spare) under TOOLS_LOW_TURNS of use, so retting and
    the builds keep their tools; put the camp back once stock is over TOOLS_OK_TURNS."""
    b = m.get("/buildings/%s" % q.STORE) or {}
    inv = (b.get("storage") or {}).get("inventory") or {}
    f = (inv.get("previous_flows") or {}).get("tools") or {}
    held = m.num((((inv.get("account") or {}).get("assets") or {}).get("tools") or {}).get("balance"))
    avg, peak = avg_use("tools")
    # plan on the worst of: last turn, the 12-turn peak (builds draw in bursts), normal ~7/turn
    use = max(m.num(f.get("consumption")), peak, 7.0)
    turns = held / use
    say("tools: held %.1f, use %.1f/turn -> %.1f turns" % (held, use, turns))
    mgrs = q._store_managers(q.STORE, "tools")
    top = mgrs[0] if mgrs else {}
    if m.num(top.get("buy_price")) < float(TOOLS_ORDER["buy_price"]) or m.num(top.get("buy_volume")) < TOOLS_ORDER["buy_volume"]:
        actions.append({"item": "tools", "tier": 0, "set": TOOLS_ORDER,
                        "note": "tool guard: keep the tool bid at the cap (%.1f turns of stock)" % turns})
    prod = q.read_producer(CAMP)
    tgt = m.num(prod.get("target"))
    try:
        import v2_owned
        goal_rates = v2_owned.goal_owns("rates")
    except Exception:
        goal_rates = False
    if goal_rates:
        pass            # the goal planner owns building rates (it prices tool wear into the camp's rate)
    elif turns < TOOLS_LOW_TURNS and tgt > CAMP_SLOW:
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
        input_runway(st)
    except (Exception, SystemExit) as ex:
        say("input runway crashed: %s: %s" % (type(ex).__name__, ex))
    try:
        tool_guard(actions, st)
    except (Exception, SystemExit) as ex:
        say("tool guard crashed: %s: %s" % (type(ex).__name__, ex))

    paused = st.get("paused") or {}
    if lvl == 0:
        # bot v2's self-diagnosis (v2/diagnose.py R1) restored these at level 0 with a fresh bid: no longer paused
        try:
            unp = (json.load(open(os.path.join(HERE, "state", "v2", "diagnose_state.json"))).get("unpaused")) or {}
        except (OSError, ValueError):
            unp = {}
        for item in list(paused):
            if item in unp and str(unp[item]) >= str(st.get("since") or ""):     # restored after the last brake ended
                say("paused %s restored by v2 diagnose at %s: dropped from paused" % (item, unp[item]))
                paused.pop(item)
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

    # items bot v2 runs live are left to v2 below brake level; at BRAKE/STOP v2 stands down
    # (v2/act.py reads state/failsafe.json) and the failsafe acts on everything
    try:
        import v2_owned
        mine = v2_owned.owned_items() if lvl < 2 else set()
    except Exception:
        mine = set()
    if mine:
        left = [e for e in actions if e.get("item") in mine]
        actions = [e for e in actions if e.get("item") not in mine]
        for e in left:
            say("left to v2:", e.get("item"), e.get("note"))

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
           "low_inputs": st.get("low_inputs", {}),
           "last_actions": [dict(set=e.get("set"), item=e.get("item"), ok=ok) for e, ok in results] or st.get("last_actions", [])}
    if LIVE:
        with open(STATE, "w") as f:
            json.dump(new, f, indent=1)
            f.write("\n")


if __name__ == "__main__":
    main()
