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


APPRENTICES_WANT = 2                                   # Taylor, Oct 10: buy the 2nd apprentice slot
APPRENTICE_COSTS = [50, 250, 1000, 2500, 5000, 7500, 10000]   # game code: cost of level n is [n-1]
HOUSE_OP = "knight/%s"                                 # the household production slot (runs net duty)
# an apprentice adds 20% to base household sustenance; fish was capped at one turn (6), so lift it
SUSTENANCE_BUMP = [{"item": "fish", "tier": 0, "set": {"buy_volume": 8, "max_holding": 8}, "capacity": 8},
                   {"item": "meat", "tier": 0, "set": {"buy_volume": 8}}]


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
        cost = APPRENTICE_COSTS[level]
        if free < cost or rate <= 0 or int(m.num(pb.get("tenants_level"))) < TENANTS_MAX_LEVEL:
            return
        if not LIVE:
            say("  would buy apprentices level %d for %d" % (level + 1, cost))
            return
        ok, status, body = q._req("POST", "/households/%s/prestige/allocate" % hid, {"track": "apprentices", "cost": str(cost)})
        after = int(m.num(((m.get("/households/%s" % hid) or {}).get("prestige_board") or {}).get("apprentices_level")))
        good = after == level + 1
        q.log({"prestige": "apprentices", "cost": cost, "note": "apprentice rule"},
              dict(ok=good, status=status, body=body[:200], before=level, after=after), source="prestige_rules")
        say("  bought apprentices level %d for %d -> %s" % (level + 1, cost, "OK" if good else "FAILED %s %s" % (status, body[:150])))
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
        for e in SUSTENANCE_BUMP:
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
        nxt = next(((thr, name) for thr, name in TIERS if pts < thr + 50), None)
        say("worker %s %s: top %s %.1f%s" % (wid, w.get("name"), cls, pts,
            ", %s at %d (%.1f to go)" % (nxt[1], nxt[0], max(0, nxt[0] - pts)) if nxt else ""))
        if not nxt or nxt[1] == "master" or pts < nxt[0] - 1:
            continue
        key = "%s:%s:%s" % (wid, cls, nxt[1])
        if key in done:
            continue
        if not LIVE:
            say("  would promote worker %s to %s %s" % (wid, cls, nxt[1]))
            continue
        ok, status, body = q._req("POST", "/households/%s/workers/%s/promote" % (hid, wid), {"class": cls})
        if not ok and status is not None and status < 500:
            done[key] = {"ok": False, "status": status, "body": body[:160]}
            changed = True
            with open(NEEDS_YOU, "w") as f:
                json.dump({"what": "Promote %s to %s %s in-game (the API refused it: %s)." % (w.get("name"), cls, nxt[1], status),
                           "since_turn": None}, f)
        elif ok:
            done[key] = {"ok": True, "status": status}
            changed = True
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
    try:
        apprentice_rule()
    except Exception as ex:
        say("apprentice rule crashed: %s: %s" % (type(ex).__name__, ex))
    try:
        promote_rule()
    except Exception as ex:
        say("promote rule crashed: %s: %s" % (type(ex).__name__, ex))

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
