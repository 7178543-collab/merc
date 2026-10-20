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

Rule 3, promotions (Oct 10): see promote_rule(); free and no-choice, so automatic.
Rule 4, 2nd apprentice (Taylor, Oct 10): see apprentice_rule(); 250 prestige, then recruit + net duty.
Rule 5, park plots (Oct 10): see park_ready_rule(); places a plot itself when it fits and materials are in.
Rule 6, quarry speed by cash (Oct 14): see quarry_rule(); 1x above 18k cash while park plots still fit, 0.4x under 15k.
Rule 7, buy when affordable (Oct 14): see wants_rule(); prestige buys Taylor queued from the app, bought at the exact price.

Only sends a change when the game differs from the wanted state; every change is verified
and logged to state/order_queue_done.jsonl (source "prestige_rules").

    python prestige_rules.py          # dry run: prints the decision
    python prestige_rules.py --live   # applies it
"""
import datetime
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
FISH_ORDER = {"buy_volume": 6, "buy_price": "26.0", "max_holding": 20}   # 24.60 stopped filling Oct 10
# Oct 14 (Taylor left it to Claude): cured fish had no home sellers, so the banquet falls back to the
# meat version (same +4.2, 35 labour, 15 beer, 6 cured meat). Fish first (cheaper), meat when fish is short.
MEAT_RECIPE = "hold banquet 1 (meat)"
MEAT = "cured meat"
MEAT_ORDER = {"buy_volume": 6, "buy_price": "29", "max_holding": 10}     # storage cap 10; ask ~27.8 Oct 14
FISH_RUN, MEAT_RUN = 5.5, 6
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


PARK = "152202388002004"
PARK_PLOT = {"limestone": 60, "timber": 40}          # per plot (labour 260 is bought)
# Oct 13: when a plot is ready, place it (order queue "plot": expand onto our land, or claim now and expand after the
# tick) instead of asking Taylor for a map click. False = only flag it in needs_you, as before.
AUTO_PLOT = True
AUTO_PLOT_MIN_CASH = 20000   # Oct 15 (Taylor: get back on track): each plot is ~1.9k (60 limestone, 40 timber, 260 labour)
                             # plus 15 labour a turn for good; no new plots while cash is under this


QUARRY = "149602389"
QUARRY_FAST, QUARRY_SLOW = 1.0, 0.4
QUARRY_FAST_CASH, QUARRY_SLOW_CASH = 18000, 15000
LIMESTONE_RESERVE = 120      # contracts.py keeps this for church limestone asks


def quarry_rule(cash, spare=None):
    """Rule 6 (Oct 14, Taylor: turn cash into prestige once profit holds). Banquet tiers 2-3 fail the supply check at
    home (hop beer trades ~5/turn vs 15 needed, wine ~16 vs 15), so the cash goes to park plots instead: limestone is
    their wall (60 a plot) and our quarry runs at 0.4x (5.2/turn, one plot every ~12 turns). With cash over 18k and
    plots still fitting in the prestige pool, the quarry runs at 1x (13/turn, one plot every ~5 turns); under 15k, or
    once limestone covers the plots that still fit plus the church reserve, back to 0.4x. In between: keep.
    Same labour per limestone either way (110 a run), so this only brings the plots, and their prestige, forward."""
    b = m.get("/buildings/%s" % QUARRY) or {}
    prod = b.get("producer") or {}
    if not prod.get("recipe"):
        say("quarry: no recipe set, rule skipped")
        return
    cur = m.num(prod.get("target"))
    pl = m.get("/player") or {}
    hid = (pl.get("household") or {}).get("id")
    cap = m.num(((m.get("/households/%s" % hid) or {}).get("caps") or {}).get("prestige_management"))
    park = m.get("/buildings/%s" % PARK) or {}
    plots = m.num(park.get("size")) + m.num((park.get("construction") or {}).get("size"))
    room = max(0, int((cap - (2 + 0.1 * plots)) / 0.1 + 1e-6))
    store = m.get("/buildings/%s" % q.STORE) or {}
    assets = ((((store.get("storage") or {}).get("inventory") or {}).get("account") or {}).get("assets")) or {}
    held = m.num((assets.get("limestone") or {}).get("balance"))
    need = room * PARK_PLOT["limestone"] + LIMESTONE_RESERVE
    try:
        with open(os.path.join(HERE, "state", "overrides.json")) as f:
            qov = (json.load(f) or {}).get("quarry", "auto")
    except (OSError, ValueError):
        qov = "auto"
    if qov == "slow":
        want, why = QUARRY_SLOW, "Taylor's switch from the app: quarry slow"
    elif cash < AUTO_PLOT_MIN_CASH:
        # Oct 15 recovery: no new plots under 20k cash, so limestone only backs church asks; 44 labour a turn for a
        # pile nobody draws is waste (the home market trades ~2 a turn). Oct 20 (Taylor's one-off park plot takes 60):
        # under 20k the quarry never runs on bought labour, even under the church reserve; spare own labour (Rule 7,
        # below) refills it. Restarts at 0.4x on bought labour once cash is over 20k.
        want, why = 0, "recovery: no bought labour for the quarry under %d cash (limestone %.0f, reserve %d)" % (
            AUTO_PLOT_MIN_CASH, held, LIMESTONE_RESERVE)
    elif cash > QUARRY_FAST_CASH and held < need:
        want, why = QUARRY_FAST, "cash %.0f over %d, %d plot(s) still fit, limestone %.0f of %.0f" % (cash, QUARRY_FAST_CASH, room, held, need)
    elif cash < QUARRY_SLOW_CASH or held >= need:
        want, why = QUARRY_SLOW, ("cash %.0f under %d" % (cash, QUARRY_SLOW_CASH)) if cash < QUARRY_SLOW_CASH else \
            "limestone %.0f covers the %d plot(s) that fit + reserve" % (held, room)
        want = min(want, cur) if cur > 0 else want      # never raises a quarry someone set lower by hand
    else:
        want, why = cur, "in between (cash %.0f): keep" % cash
    if spare is not None and qov != "slow":
        # Rule 7 (Oct 18): spare own labour runs the quarry on top of what this rule wants (see spare_labour_rule)
        alloc = spare(want)
        if alloc and alloc["quarry"] > want:
            want, why = alloc["quarry"], "%s; %s" % (why, alloc["why"])
    say("quarry: %.2fx -> %.2fx (%s)" % (cur, want, why))
    if abs(want - cur) < 0.01 or not LIVE:
        return
    e = {"building": QUARRY, "producer": {"recipe": prod.get("recipe"), "target": want, "provider_id": q.STORE},
         "note": "quarry rule: " + why}
    try:
        r = q.apply_entry(e)
    except Exception as ex:
        r = dict(ok=False, error="%s: %s" % (type(ex).__name__, ex))
    q.log(e, r, source="prestige_rules")
    say("  quarry -> %s" % ("OK" if r.get("ok") else "FAILED %s" % r.get("error")))


CAMP = "151402406"
CAMP_RECIPE = "split timber 2"
SPARE_STATE = os.path.join(HERE, "state", "spare_labour.json")


def _turn_rows():
    """One history line per game turn (the last of each), oldest first."""
    by_turn = {}
    for path in sorted(glob.glob(os.path.join(HERE, "history", "merc-*.jsonl")))[-2:]:
        for line in open(path):
            try:
                d = json.loads(line)
            except ValueError:
                continue
            if d.get("turn") is not None and d.get("items"):
                by_turn[d["turn"]] = d
    return [by_turn[t] for t in sorted(by_turn)]


def spare_labour_rule():
    """Rule 7 (Oct 18, Taylor: "why aren't we making and using maxing free labor"). Own labour nothing draws expires;
    put it on limestone (quarry) then timber (logging camp) instead. Sized on real use (spare_labour.py), so it never
    buys labour, and it backs off by itself when the chain needs the labour. Returns a function quarry_rule calls with
    the quarry rate it wants anyway; that call also sets the camp. At failsafe BRAKE/STOP: no spare (back to base)."""
    import spare_labour as sl
    try:
        st = json.load(open(SPARE_STATE))
    except (OSError, ValueError):
        st = {}
    extra = st.get("extra_by_turn") or {}
    rows = _turn_rows()
    spare = sl.spare_from_history(rows, extra)
    try:
        fs = json.load(open(os.path.join(HERE, "state", "failsafe.json")))
    except (OSError, ValueError):
        fs = {}
    if int(m.num(fs.get("level"))) >= 2:
        spare = 0.0
    store = m.get("/buildings/%s" % q.STORE) or {}
    inv = (store.get("storage") or {}).get("inventory") or {}
    assets = ((inv.get("account") or {}).get("assets")) or {}
    lime = assets.get("limestone") or {}
    lime_held, lime_cap = m.num(lime.get("balance")), m.num(lime.get("capacity"))
    timber_held = m.num((assets.get("timber") or {}).get("balance"))
    turn = rows[-1]["turn"] if rows else None

    def apply(quarry_floor):
        if spare is None:
            say("spare labour: not enough history yet")
            return None
        a = sl.allocate(spare, lime_held, lime_cap, timber_held, quarry_floor=quarry_floor,
                        camp_slowed=bool(fs.get("camp_slowed")))
        say("spare labour: %s -> quarry %.2f, camp %.1f (%.0f labour)" % (a["why"], a["quarry"], a["camp"], a["labour"]))
        prod = q.read_producer(CAMP)
        cur = m.num(prod.get("target"))
        if prod.get("recipe") == CAMP_RECIPE and not fs.get("camp_slowed") and abs(a["camp"] - cur) >= 0.5 \
                and cur <= sl.CAMP_MAX + 1e-6:
            e = {"building": CAMP, "producer": {"recipe": CAMP_RECIPE, "target": a["camp"], "provider_id": q.STORE},
                 "note": "spare labour rule: camp %g -> %g (%s)" % (cur, a["camp"], a["why"])}
            if LIVE:
                try:
                    r = q.apply_entry(e)
                except Exception as ex:
                    r = dict(ok=False, error="%s: %s" % (type(ex).__name__, ex))
                q.log(e, r, source="prestige_rules")
                say("  camp -> %s" % ("OK" if r.get("ok") else "FAILED %s" % r.get("error")))
            else:
                say("  would send:", json.dumps(e))
        if LIVE and turn is not None:
            extra[str(turn + 1)] = a["labour"]          # applies from the next tick, i.e. next turn's history row
            keep = sorted(extra, key=lambda k: int(k))[-12:]
            with open(SPARE_STATE, "w") as f:
                json.dump({"t": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
                           "spare": spare, "alloc": a, "extra_by_turn": {k: extra[k] for k in keep}}, f, indent=1)
        return a
    return apply


def park_ready_rule(cash=None):
    """Rule 5 (Oct 10): tell Taylor when another park plot is ready to place. Prestige pool use is
    mansion 1 + park (1 + 0.1 per plot); a plot fits when that stays within caps.prestige_management.
    Placing a plot is a map pick, so this only writes needs_you (the status email shows it)."""
    pl = m.get("/player") or {}
    hid = (pl.get("household") or {}).get("id")
    cap = m.num(((m.get("/households/%s" % hid) or {}).get("caps") or {}).get("prestige_management"))
    park = m.get("/buildings/%s" % PARK) or {}
    plots = m.num(park.get("size")) + m.num((park.get("construction") or {}).get("size"))
    used = 1 + 1 + 0.1 * plots
    store = m.get("/buildings/%s" % q.STORE) or {}
    assets = ((((store.get("storage") or {}).get("inventory") or {}).get("account") or {}).get("assets")) or {}
    held = {k: m.num((assets.get(k) or {}).get("balance")) for k in PARK_PLOT}
    room = used + 0.1 <= cap + 1e-9
    ready = room and all(held[k] >= v for k, v in PARK_PLOT.items())
    # Taylor's park policy is "fully maintained": keep the maintain target at the number of built plots (Oct 13: the
    # 10th plot was built but the target stayed at 9, so one plot gave no prestige)
    built = int(m.num(park.get("size")))
    prod = park.get("producer") or {}
    if LIVE and built and prod.get("recipe") == "maintain 1" and m.num(prod.get("target")) < built:
        e = {"building": PARK, "producer": {"recipe": "maintain 1", "target": built, "provider_id": q.STORE},
             "note": "park rule: maintain all %d built plots (was %s)" % (built, prod.get("target"))}
        try:
            r = q.apply_entry(e)
        except Exception as ex:
            r = dict(ok=False, error="%s: %s" % (type(ex).__name__, ex))
        q.log(e, r, source="prestige_rules")
        say("  park maintain %s -> %d: %s" % (prod.get("target"), built, "OK" if r.get("ok") else "FAILED %s" % r.get("error")))
    say("park: %d plots, prestige pool %.1f/%.0f, limestone %.0f, timber %.0f -> %s" % (
        plots, used, cap, held["limestone"], held["timber"], "READY for another plot" if ready else ("no pool room" if not room else "waiting on materials")))
    if ready and cash is not None and cash < AUTO_PLOT_MIN_CASH:
        say("  park plot held: cash %.0f under %d (recovery)" % (cash, AUTO_PLOT_MIN_CASH))
        return
    if ready and LIVE and AUTO_PLOT:
        e = {"plot": {"building": PARK}, "confirm": True, "note": "park rule: pool %.1f/%.0f, limestone %.0f, timber %.0f" % (
            used, cap, held["limestone"], held["timber"])}
        try:
            r = q.apply_entry(e)
        except Exception as ex:
            r = dict(ok=False, error="%s: %s" % (type(ex).__name__, ex))
        if not r.get("skipped"):
            q.log(e, r, source="prestige_rules")
        say("  park plot -> %s" % (r.get("skipped") or ("OK %s" % (r.get("tile") or "")) if r.get("ok") else "FAILED %s" % r.get("error")))
        if r.get("ok"):
            return
    if ready and LIVE and not os.path.exists(NEEDS_YOU):
        with open(NEEDS_YOU, "w") as f:
            json.dump({"what": "Add a park plot (park > expand on the map): pool %.1f/%.0f, limestone %.0f, timber %.0f on hand." % (used, cap, held["limestone"], held["timber"]),
                       "since_turn": None}, f)


PM_FIRST = 2                                           # Taylor, Oct 10: buy prestige management level 2 (250) for park plots, then the apprentice
APPRENTICES_WANT = 2                                   # Taylor, Oct 10: buy the 2nd apprentice slot
APPRENTICE_COSTS = [50, 250, 1000, 2500, 5000, 7500, 10000]   # game code: cost of level n is [n-1]
HOUSE_OP = "knight/%s"                                 # the household production slot (runs net duty)
# an apprentice adds 20% to base household sustenance; fish was capped at one turn (6), so lift it
SUSTENANCE_BUMP = [{"item": "fish", "tier": 0, "set": {"buy_volume": 8, "max_holding": 8}, "capacity": 8},
                   {"item": "meat", "tier": 0, "set": {"buy_volume": 8}}]


PM_COSTS = [0, 100, 250, 500, 1000, 2000, 3000, 5000, 10000]   # game table; the game is the judge (see allocate)


def allocate(hid, track, cost, free):
    """POST a prestige allocation. If the game says the cost is different ("expected N"), retry once
    at N when free prestige covers it. Returns (ok, level_after, info)."""
    import re
    key = track + "_level"
    level = lambda: int(m.num(((m.get("/households/%s" % hid) or {}).get("prestige_board") or {}).get(key)))
    before = level()
    ok, status, body = q._req("POST", "/households/%s/prestige/allocate" % hid, {"track": track, "cost": str(cost)})
    if not ok and status == 409:
        mm = re.search(r"expected (\d+)", body or "")
        if mm and int(mm.group(1)) <= free:
            cost = int(mm.group(1))
            ok, status, body = q._req("POST", "/households/%s/prestige/allocate" % hid, {"track": track, "cost": str(cost)})
    after = level()
    return after == before + 1, after, "cost %s, status %s %s" % (cost, status, (body or "")[:120])


def apprentice_rule():
    """Rule 4 (Taylor, Oct 10): get a 2nd apprentice onto net duty. One step per run:
    1) buy apprentices level 2 (250 prestige) once free prestige covers it, income is positive and
       Tenants is maxed; 2) recruit (POST /households/{id}/workers); 3) assign any unassigned
       apprentice to the household slot (PUT /households/{id}/workers/{n} {assignment}) and lift
       the fish/meat buys for the extra sustenance. Endpoints are from the game's own code."""
    pl = m.get("/player") or {}
    hid = (pl.get("household") or {}).get("id")
    hh = m.get("/households/%s" % hid) or {}
    pb = hh.get("prestige_board") or {}
    level = int(m.num(pb.get("apprentices_level")))
    free = m.num(hh.get("prestige")) - m.num(pb.get("allocated"))
    rate = sum(m.num(x.get("impact")) for x in (hh.get("prestige_impacts") or pb.get("prestige_impacts") or []))
    workers = hh.get("workers") or []
    cap = int(m.num((hh.get("caps") or {}).get("apprentices")))
    say("apprentices: level %d (want %d), cap %d, have %d, free prestige %.1f" % (level, APPRENTICES_WANT, cap, len(workers) - 1, free))
    if level < APPRENTICES_WANT:
        pm = int(m.num(pb.get("prestige_management_level")))
        if pm < PM_FIRST:
            pm_cost = PM_COSTS[pm + 1] if pm + 1 < len(PM_COSTS) else 10 ** 9
            say("  prestige management level %d first (cost %d, free %.1f); apprentice after" % (pm + 1, pm_cost, free))
            if free >= pm_cost and rate > 0 and LIVE:
                ok, after, info = allocate(hid, "prestige_management", pm_cost, free)
                q.log({"prestige": "prestige_management", "cost": pm_cost, "note": "park pool (Taylor, Oct 10)"},
                      dict(ok=ok, after=after, info=info), source="prestige_rules")
                say("  bought prestige management level %s -> %s %s" % (pm + 1, "OK" if ok else "FAILED", info))
            return
        cost = APPRENTICE_COSTS[level]
        if free < cost or rate <= 0 or int(m.num(pb.get("tenants_level"))) < TENANTS_MAX_LEVEL:
            return
        if not LIVE:
            say("  would buy apprentices level %d for %d" % (level + 1, cost))
            return
        good, after, info = allocate(hid, "apprentices", cost, free)
        q.log({"prestige": "apprentices", "cost": cost, "note": "apprentice rule"},
              dict(ok=good, before=level, after=after, info=info), source="prestige_rules")
        say("  bought apprentices level %d for %d -> %s %s" % (level + 1, cost, "OK" if good else "FAILED", info))
        return
    if len(workers) - 1 < cap:
        if not LIVE:
            say("  would recruit an apprentice")
            return
        ok, status, body = q._req("POST", "/households/%s/workers" % hid, {})
        now = (m.get("/households/%s" % hid) or {}).get("workers") or []
        good = len(now) == len(workers) + 1
        q.log({"recruit": "apprentice", "note": "apprentice rule"}, dict(ok=good, status=status, body=body[:200]), source="prestige_rules")
        say("  recruit apprentice -> %s" % ("OK" if good else "FAILED %s %s" % (status, body[:150])))
        if not good:
            return
        workers = now
        try:
            import v2_owned
            mine = v2_owned.owned_items()
        except Exception:
            mine = set()
        for e in SUSTENANCE_BUMP:
            if e["item"] in mine:       # v2 sizes it from observed use, the bump would be overwritten anyway
                continue
            r = q.apply_entry(dict(e, note="apprentice rule: +20% sustenance"))
            q.log(e, r, source="prestige_rules")
            say("  %s -> %s" % (e["item"], "OK" if r.get("ok") else "FAILED %s" % r.get("error")))
    for i, w in enumerate(workers):
        if i == 0 or w.get("assignment"):
            continue
        if not LIVE:
            say("  would assign worker %d (%s) to %s" % (i, w.get("name"), HOUSE_OP % hid))
            continue
        ok, status, body = q._req("PUT", "/households/%s/workers/%d" % (hid, i),
                                  {"assignment": HOUSE_OP % hid, "update_buying": False, "mark_to_market": False})
        now = ((m.get("/households/%s" % hid) or {}).get("workers") or [{}] * (i + 1))
        good = len(now) > i and now[i].get("assignment") == HOUSE_OP % hid
        q.log({"assign": i, "to": HOUSE_OP % hid, "note": "apprentice rule"}, dict(ok=good, status=status, body=body[:200]), source="prestige_rules")
        say("  assign worker %d to net duty -> %s" % (i, "OK" if good else "FAILED %s %s" % (status, body[:150])))
        if not good:
            with open(NEEDS_YOU, "w") as f:
                json.dump({"what": "Assign the new apprentice %s to household net duty (household > workers); the API refused it." % w.get("name"),
                           "since_turn": None}, f)


TIERS = [(100, "worker"), (700, "journeyman"), (3700, "master")]   # skill points per tier (game code)
PROMOTIONS = os.path.join(HERE, "state", "promotions.json")


def _next_tier(pts, wid, cls, done):
    ok_idx = [i for i, (_, name) in enumerate(TIERS) if (done.get("%s:%s:%s" % (wid, cls, name)) or {}).get("ok")]
    above = TIERS[(max(ok_idx) + 1 if ok_idx else 0):]
    crossed = [(thr, name) for thr, name in above if pts >= thr]
    return crossed[-1] if crossed else (above[0] if above else None)


WANTS = os.path.join(HERE, "state", "prestige_wants.json")


def learned_price(track, level):
    """The game's own price for track's next level, from a refused offer in the queue log ("expected N"), if it was
    asked at this level. None when unknown."""
    import re
    price = None
    try:
        lines = open(os.path.join(HERE, "state", "order_queue_done.jsonl")).read().splitlines()[-600:]
    except OSError:
        return None
    for line in lines:
        try:
            d = json.loads(line)
        except ValueError:
            continue
        e = d.get("entry") or {}
        if e.get("prestige") != track:
            continue
        mm = re.search(r"expected (\d+)", str(d.get("body") or d.get("error") or ""))
        if mm and (d.get("before") is None or int(m.num(d.get("before"))) == level):
            price = int(mm.group(1))
        elif d.get("ok"):
            price = None
    return price


def known_price(track, level):
    if track == "prestige_management" and level + 1 < len(PM_COSTS):
        return PM_COSTS[level + 1]
    if track == "apprentices" and level < len(APPRENTICE_COSTS):
        return APPRENTICE_COSTS[level]
    return None


def wants_rule():
    """Rule 7 (Oct 14, Taylor: "buy when affordable" from the phone app). state/prestige_wants.json holds the tracks
    Taylor queued, oldest first: {track, max_cost, since, level}. Each run buys the first one whose price free prestige
    covers (one buy a run), at the game's exact price and never above max_cost; then it leaves the list. A track whose
    price is unknown gets one free price check (a 1-prestige offer the game refuses, naming the price)."""
    try:
        with open(WANTS) as f:
            wants = json.load(f) or []
    except (OSError, ValueError):
        return
    if not wants:
        return
    pl = m.get("/player") or {}
    hid = (pl.get("household") or {}).get("id")
    hh = m.get("/households/%s" % hid) or {}
    pb = hh.get("prestige_board") or {}
    free = m.num(hh.get("prestige")) - m.num(pb.get("allocated"))
    keep = []
    bought = False
    for w in wants:
        track = w.get("track")
        lv = int(m.num(pb.get(track + "_level")))
        if w.get("level") is not None and lv > int(w["level"]):
            say("wants: %s already at level %d (wanted %d -> %d): done" % (track, lv, w["level"], w["level"] + 1))
            continue
        price = learned_price(track, lv) or known_price(track, lv)
        cap = int(m.num(w.get("max_cost"))) if w.get("max_cost") else None
        if price is None:
            say("wants: %s level %d -> %d: price unknown, checking (nothing is spent)" % (track, lv, lv + 1))
            if LIVE:
                e = {"prestige": track, "cost": 1, "max_cost": 1, "confirm": True, "note": "wants rule: price check " + track}
                try:
                    r = q.apply_entry(e)
                except Exception as ex:
                    r = dict(ok=False, error="%s: %s" % (type(ex).__name__, ex))
                q.log(e, r, source="prestige_rules")
            keep.append(w)
            continue
        if cap is None:
            say("wants: %s has no price cap (the app always sends one): kept, not bought" % track)
            keep.append(w)
            continue
        if price > cap:
            say("wants: %s costs %d, over the %d you set: kept, not bought" % (track, price, cap))
            keep.append(w)
            continue
        if bought or free < price:
            say("wants: %s level %d -> %d costs %d, free %.0f: waiting" % (track, lv, lv + 1, price, free))
            keep.append(w)
            continue
        if not LIVE:
            say("wants: would buy %s for %d" % (track, price))
            keep.append(w)
            continue
        ok, after, info = allocate(hid, track, price, min(free, cap or free))
        q.log({"prestige": track, "cost": price, "note": "wants rule (Taylor, from the app)"},
              {"ok": ok, "after": after, "info": info}, source="prestige_rules")
        say("wants: bought %s level %d for %d -> %s" % (track, after, price, "OK" if ok else "FAILED %s" % info))
        if ok:
            bought = True
            free -= price
        else:
            keep.append(w)
    if LIVE:
        with open(WANTS, "w") as f:
            json.dump(keep, f, indent=1)


def promote_rule():
    """Rule 3 (Oct 10): promotions are free and no-choice, so take them as soon as they come up
    (Taylor's standing rule). Each new tier is +1 management for that worker (up to +3) and a small
    output bonus; the head's promotions also unlock recipes. Promote = POST
    /households/{id}/workers/{worker id}/promote {"class": <skill>} (game code: resourceAction).
    Only tries near a fresh crossing (threshold -1 to +50 points), never master (a one-class choice:
    Taylor decides), and never repeats a refused attempt. Logs every worker's top skill each run."""
    pl = m.get("/player") or {}
    hid = (pl.get("household") or {}).get("id")
    hh = m.get("/households/%s" % hid) or {}
    try:
        with open(PROMOTIONS) as f:
            done = json.load(f)
    except (FileNotFoundError, ValueError):
        done = {}
    changed = False
    for i, w in enumerate(hh.get("workers") or []):
        wid = str(w.get("id", i))
        skills = {k: m.num(v) for k, v in (w.get("skills") or {}).items()}
        if not skills:
            continue
        cls, pts = max(skills.items(), key=lambda kv: kv[1])
        # next tier = the highest one reached on points above the last promotion we made (Oct 13: the old
        # "threshold to +50" window gave up for good once a worker passed it while the game still said not ready)
        nxt = _next_tier(pts, wid, cls, done)
        say("worker %s %s: top %s %.1f%s" % (wid, w.get("name"), cls, pts,
            ", %s at %d (%.1f to go)" % (nxt[1], nxt[0], max(0, nxt[0] - pts)) if nxt else ""))
        if not nxt or nxt[1] == "master" or pts < nxt[0]:
            continue
        key = "%s:%s:%s" % (wid, cls, nxt[1])
        rec = done.get(key) or {}
        if rec and "not_ready" not in rec:
            continue
        if rec.get("not_ready"):
            import datetime as _dt
            last = _dt.datetime.fromisoformat(rec["not_ready"])
            if _dt.datetime.now(_dt.timezone.utc) - last < _dt.timedelta(hours=6):
                continue        # the game said not ready: ask again every 6 hours, not every run
        if not LIVE:
            say("  would promote worker %s to %s %s" % (wid, cls, nxt[1]))
            continue
        ok, status, body = q._req("POST", "/households/%s/workers/%s/promote" % (hid, wid), {"class": cls})
        if not ok and "not ready" in (body or ""):
            import datetime as _dt     # Oct 11: the game counts points differently; retry in 6 hours
            done[key] = {"not_ready": _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"), "points": pts}
            changed = True
        elif not ok and status is not None and status < 500:
            done[key] = {"ok": False, "status": status, "body": body[:160]}
            changed = True
            with open(NEEDS_YOU, "w") as f:
                json.dump({"what": "Promote %s to %s %s in-game (the API refused it: %s)." % (w.get("name"), cls, nxt[1], status),
                           "since_turn": None}, f)
        elif ok:
            done[key] = {"ok": True, "status": status}
            changed = True
            # Oct 15 (Taylor): the 2nd apprentice was bought and assigned on Oct 13 but net duty stayed at 2.0 (max was
            # 2.6) for ~55 turns. A promotion raises the duty cap again, so ask for the new max right away.
            with open(NEEDS_YOU, "w") as f:
                json.dump({"what": "%s is now %s %s: raise household net duty to the new max (household > production)." % (
                    w.get("name"), cls, nxt[1]), "since_turn": None}, f)
        q.log({"promote": wid, "class": cls, "tier": nxt[1], "note": "promotion rule"},
              dict(ok=ok, status=status, body=body[:200]), source="prestige_rules")
        say("  promote worker %s to %s %s -> %s" % (wid, cls, nxt[1], "OK" if ok else "FAILED %s %s" % (status, body[:150])))
    if changed:
        with open(PROMOTIONS, "w") as f:
            json.dump(done, f, indent=1)


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
    running = (prod.get("recipe") in (RECIPE, MEAT_RECIPE) and m.num(prod.get("target")) > 0
               and str(prod.get("provider_id")) == q.STORE)
    store = m.get("/buildings/%s" % q.STORE) or {}
    assets = ((((store.get("storage") or {}).get("inventory") or {}).get("account") or {}).get("assets")) or {}
    fish_held = m.num((assets.get(FISH) or {}).get("balance"))
    meat_held = m.num((assets.get(MEAT) or {}).get("balance"))
    # recipe pick: fish when a run's worth is held, else meat when it is, else stay on what's set.
    # Once on meat, stay there until fish is back with two runs held (no hourly flip-flop).
    if prod.get("recipe") == MEAT_RECIPE and meat_held >= MEAT_RUN and fish_held < 2 * FISH_RUN:
        recipe = MEAT_RECIPE
    elif fish_held >= FISH_RUN:
        recipe = RECIPE
    elif meat_held >= MEAT_RUN:
        recipe = MEAT_RECIPE
    else:
        recipe = prod.get("recipe") if prod.get("recipe") in (RECIPE, MEAT_RECIPE) else RECIPE

    try:
        with open(os.path.join(HERE, "state", "overrides.json")) as f:
            ov = (json.load(f) or {}).get("banquet", "auto")
    except (FileNotFoundError, ValueError):
        ov = "auto"
    if ov in ("on", "off"):
        want_on, why = ov == "on", "Taylor's override from the app: banquet %s" % ov
    elif cash < OFF_CASH:
        want_on, why = False, "cash %.0f under %d" % (cash, OFF_CASH)
    elif cash > ON_CASH:
        want_on, why = True, "cash %.0f over %d (profit %+.0f over %d turns, %+.0f over %d)" % (cash, ON_CASH, profit, n, recent, rn)
    else:
        want_on, why = running, "in between (cash %.0f, profit %+.0f over %d turns): keep as is" % (cash, profit, n)

    fish_mgrs = q._store_managers(q.STORE, FISH)
    fish_on = any(m.num(mg.get("buy_volume")) > 0 for mg in fish_mgrs)
    meat_mgrs = q._store_managers(q.STORE, MEAT)
    meat_on = any(m.num(mg.get("buy_volume")) > 0 for mg in meat_mgrs)
    say("prestige_rules: banquet %s -> want %s (%s); fish buy %s, meat buy %s; held fish %.1f meat %.1f -> %s" % (
        "on" if running else "off", "on" if want_on else "off", why, "on" if fish_on else "off",
        "on" if meat_on else "off", fish_held, meat_held, recipe))

    todo = []
    if want_on:
        if not fish_on:
            todo.append({"item": FISH, "tier": 0, "set": FISH_ORDER, "note": "banquet rule: " + why})
        if not meat_on:
            todo.append({"item": MEAT, "tier": 0, "set": MEAT_ORDER, "note": "banquet rule (meat fallback): " + why})
        if not running or prod.get("recipe") != recipe:
            todo.append({"building": MANSION, "producer": {"recipe": recipe, "target": 1, "provider_id": q.STORE},
                         "note": "banquet rule: %s; recipe %s (fish %.1f, meat %.1f held)" % (why, recipe, fish_held, meat_held)})
    else:
        if running:
            todo.append({"building": MANSION, "producer": {"recipe": prod.get("recipe"), "target": 0}, "note": "banquet rule: " + why})
        if fish_on:
            todo.append({"item": FISH, "tier": 0, "set": {"buy_volume": 0}, "note": "banquet rule: " + why})
        if meat_on:
            todo.append({"item": MEAT, "tier": 0, "set": {"buy_volume": 0}, "note": "banquet rule: " + why})

    try:
        tenants_rule()
    except Exception as ex:
        say("tenants rule crashed: %s: %s" % (type(ex).__name__, ex))
    try:
        park_ready_rule(cash)
    except Exception as ex:
        say("park rule crashed: %s: %s" % (type(ex).__name__, ex))
    try:
        try:
            spare = spare_labour_rule()
        except Exception as ex:
            spare = None
            say("spare labour rule crashed: %s: %s" % (type(ex).__name__, ex))
        quarry_rule(cash, spare)
    except Exception as ex:
        say("quarry rule crashed: %s: %s" % (type(ex).__name__, ex))
    try:
        wants_rule()
    except Exception as ex:
        say("wants rule crashed: %s: %s" % (type(ex).__name__, ex))
    try:
        apprentice_rule()
    except Exception as ex:
        say("apprentice rule crashed: %s: %s" % (type(ex).__name__, ex))
    try:
        promote_rule()
    except Exception as ex:
        say("promote rule crashed: %s: %s" % (type(ex).__name__, ex))

    try:
        import v2_owned
        mine = v2_owned.owned_items()
    except Exception:
        mine = set()
    for e in todo:
        if e.get("item") in mine:       # v2 sizes this item from what the mansion actually uses
            say("  %s left to v2 (%s)" % (e["item"], e.get("note")))
            continue
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
