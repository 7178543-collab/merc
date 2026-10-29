#!/usr/bin/env python3
"""Guardian (Oct 28 2026, Taylor: "what failsafes do we put in place so this can't happen").

Why: Oct 25-27 the cash fell 3,974 -> ~140. A stockpile sale (rope) hid that costs weren't covered, the goal planner
switched the flax farm and raised retting on Oct 27 with its model check silently off, the chain starved (retting 0 of
1.0, spinnery 0.4 of 1.9, brewery and mansion 0), and below the hard floor every raise was held - the very moves that
restored income. Nothing put the working configuration back, and nobody was told.

What this does, every order-queue run (hourly :20 and on queue commits):
  1. KNOWN GOOD: when cash is healthy (>= 2 x the floor, not sliding) it records the buildings' recipes and targets
     (state/guardian.json, at most one every 12 turns, last 6 kept).
  2. ROLLBACK: if (a) cash fell >= 30% in 24 turns and is under 2 x the floor while the goal planner moved something in
     that window, or (b) 2+ buildings with a target >= 0.5 ran under 40% of it for 4 turns in a row, it puts the last
     known-good recipes and targets back (through the order queue), freezes the goal planner's raises, recipe switches,
     investments and donations for 48 turns (cuts still go) and writes an alert. One rollback per 48 turns.
  3. FLOOR: once cash has been over 8 turns of fixed cost + 500, the goal planner's hard floor ratchets up to 8 turns of
     fixed cost (it only ever goes up). v2/act.py and failsafe.py read it through floor_override().
  4. ALERT: state/guardian.json "alert" is a one-line message while a rollback, freeze or a long STOP is active
     (alerts.py / the phone app can show it).

Dry run by default. Live only with --live AND v2/config.json guardian.live true.

    python guardian.py          # prints the decision
    python guardian.py --live   # applies it (when guardian.live is on)
"""
import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "state", "guardian.json")
CONFIG = os.path.join(HERE, "v2", "config.json")
SNAP = os.path.join(HERE, "state", "v2", "snapshot.json")
GOAL = os.path.join(HERE, "state", "v2", "goal.json")
GOAL_ACT = os.path.join(HERE, "state", "v2", "goal_act.jsonl")
FAILSAFE = os.path.join(HERE, "state", "failsafe.json")
LOAN = os.path.join(HERE, "state", "loan.json")

DEFAULTS = {"live": False, "slide_pct": 0.30, "slide_turns": 24, "healthy_x_floor": 2.0, "kg_gap_turns": 12,
            "kg_keep": 6, "starve_frac": 0.40, "starve_min_target": 0.5, "starve_turns": 4, "starve_buildings": 2,
            "freeze_turns": 48, "cooldown_turns": 48, "floor_turns": 8, "floor_margin": 500, "long_stop_turns": 6,
            "burn_alert": 100.0, "burn_flat_cash": 0.5}


def _load(path, default):
    try:
        with open(path) as f:
            return json.load(f)
    except (OSError, ValueError):
        return default


def cfg():
    c = dict(DEFAULTS)
    c.update((_load(CONFIG, {}).get("guardian")) or {})
    return c


def load_state():
    return _load(STATE, {})


# ----- readers used by v2/act.py and failsafe.py (never raise) -----
def frozen(turn):
    """True while the guardian's freeze is on: the goal planner may only cut."""
    try:
        return bool(cfg().get("live")) and turn is not None and int(turn) < int(load_state().get("freeze_until_turn") or 0)
    except (TypeError, ValueError):
        return False


def floor_override(default=1000.0):
    """The goal planner's hard floor: the config value, or the ratcheted guardian floor when that is higher."""
    try:
        if not cfg().get("live"):
            return float(default)
        return max(float(default), float(load_state().get("hard_floor") or 0))
    except (TypeError, ValueError):
        return float(default)



# ----- honest burn and debt (Oct 28) -----
def debt_owed():
    """Church loan still owed (state/loan.json written by contracts.py); 0 once repaid or unreadable."""
    d = _load(LOAN, {})
    try:
        if d.get("repaid"):
            return 0.0
        return max(0.0, float(d.get("owed") or 0))
    except (TypeError, ValueError):
        return 0.0


def honest_burn(trend, cash_per_turn, c):
    """Value burn that stock sales cannot hide. trend: goal.json "trend" (business value = cash + stock at market, per
    turn over 6/24/48 turns). cash_per_turn: the cash change per turn over the same 24 turns, from history.
    Returns a dict: value_per_turn (24-turn, falling window beats the 6-turn noise), cash_per_turn, flattered (cash flat
    or rising while value falls: stock is being sold to cover costs) and alert text or None."""
    v24 = trend.get("per_turn_24") if trend else None
    if v24 is None:
        return {"value_per_turn": None, "cash_per_turn": cash_per_turn, "flattered": False, "alert": None}
    flat = cash_per_turn is not None and cash_per_turn > -c["burn_flat_cash"] * abs(v24)
    out = {"value_per_turn": round(float(v24), 1), "cash_per_turn": None if cash_per_turn is None else round(cash_per_turn, 1),
           "flattered": bool(v24 < -c["burn_alert"] and flat), "alert": None}
    if v24 < -c["burn_alert"]:
        out["alert"] = ("HONEST BURN: business value %+.0f/turn over 24 turns%s" % (
            v24, " while cash is %s (stock is being sold to cover costs)" % ("flat" if abs(cash_per_turn or 0) < 5 else
                                                                         "%+.0f/turn" % cash_per_turn) if out["flattered"] else ""))
    return out

# ----- pure decision functions -----
def cash_by_turn(history_lines):
    out = {}
    for d in history_lines:
        if d.get("turn") is not None and d.get("cash") is not None:
            out[int(d["turn"])] = float(d["cash"])
    return out


def is_healthy(cash, ago_cash, floor, c, debt=0.0):
    """Cash over 2 x the floor AFTER the debt owed, and not sliding (the slide test uses raw cash, as history does)."""
    return cash - float(debt or 0) >= c["healthy_x_floor"] * floor and (ago_cash is None or cash >= 0.9 * ago_cash)


def starved_buildings(history_lines, c):
    """Names of buildings whose running rate stayed under starve_frac x target (target >= starve_min_target) on each of
    the last starve_turns distinct turns. history_lines: the bot's history rows, oldest first, each with turn + bld
    rows [name, recipe, running, target, flags]."""
    by_turn = {}
    for d in history_lines:
        if d.get("turn") is not None and d.get("bld"):
            by_turn[int(d["turn"])] = d["bld"]
    turns = sorted(by_turn)[-int(c["starve_turns"]):]
    if len(turns) < int(c["starve_turns"]):
        return []
    names = None
    for t in turns:
        bad = set()
        for row in by_turn[t]:
            try:
                name, run, tgt = row[0], float(row[2] or 0), float(row[3] or 0)
            except (TypeError, ValueError, IndexError):
                continue
            if row[1] and tgt >= c["starve_min_target"] and run < c["starve_frac"] * tgt:
                bad.add(name)
        names = bad if names is None else names & bad
    return sorted(names or [])


def goal_moved_recently(goal_act_rows, turn, window):
    """Goal-planner moves actually sent (ok true, not dry) within `window` turns; returns their turns."""
    out = []
    for r in goal_act_rows:
        try:
            if r.get("ok") is True and not r.get("dry") and turn - int(r["turn"]) <= window:
                out.append(int(r["turn"]))
        except (TypeError, ValueError, KeyError):
            continue
    return out


def pick_known_good(kg, turn, first_move_turn, c):
    """Latest record taken before the goal's first recent move (or, with none, at least kg_gap_turns old)."""
    cands = [k for k in kg if (first_move_turn is not None and k["turn"] < first_move_turn)
             or (first_move_turn is None and turn - k["turn"] >= c["kg_gap_turns"])]
    return cands[-1] if cands else None


def restore_entries(kg_rec, snap_buildings):
    """Order-queue entries putting each building back to its recorded recipe/target; only what differs."""
    now = {str(b.get("id")): b for b in snap_buildings or []}
    out = []
    for b in kg_rec.get("buildings", []):
        cur = now.get(str(b["id"]))
        if not cur or cur.get("construction") or not b.get("recipe"):
            continue
        same_recipe = cur.get("recipe") == b["recipe"]
        diff = abs(float(cur.get("target") or 0) - float(b["target"]))
        if same_recipe and diff < max(0.1, 0.15 * float(b["target"])):
            continue                    # a small rate difference is noise, not the cause: leave it
        out.append({"building": str(b["id"]), "producer": {"recipe": b["recipe"], "target": float(b["target"])},
                    "note": "guardian rollback to the known-good config of turn %s (cash %s): %s %s %.3g -> %s %.3g" % (
                        kg_rec["turn"], kg_rec.get("cash"), b.get("name"), cur.get("recipe"), float(cur.get("target") or 0),
                        b["recipe"], float(b["target"]))})
    return out[:12]


def decide(turn, cash, floor, fixed_cost, hist, goal_act_rows, snap_buildings, state, c, debt=0.0, trend=None):
    """Pure. Returns (new_state, entries, notes). hist: history rows oldest first (turn, cash, bld).
    debt: loan still owed; the healthy and floor-ratchet tests use cash - debt (borrowed money is not a cushion)."""
    st = json.loads(json.dumps(state or {}))
    notes = []
    cb = cash_by_turn(hist)
    ago_turns = [t for t in cb if t <= turn - int(c["slide_turns"])]
    ago_cash = cb[max(ago_turns)] if ago_turns else None

    free = cash - float(debt or 0)
    st["debt"] = round(float(debt or 0))
    st["free_cash"] = round(free)

    # 3. floor ratchet
    want_floor = round(c["floor_turns"] * max(float(fixed_cost or 0), 0.0) / 100.0) * 100.0
    if want_floor > 0 and free >= want_floor + c["floor_margin"] and want_floor > float(st.get("hard_floor") or 0):
        st["hard_floor"] = want_floor
        notes.append("floor ratchet: hard_floor -> %.0f (%d turns of fixed cost %.0f)" % (want_floor, c["floor_turns"], fixed_cost))

    # 1. known good
    kg = st.setdefault("known_good", [])
    if is_healthy(cash, ago_cash, floor, c, debt) and (not kg or turn - kg[-1]["turn"] >= c["kg_gap_turns"]):
        recs = [{"id": str(b["id"]), "name": b.get("name"), "recipe": b.get("recipe"), "target": b.get("target")}
                for b in snap_buildings or [] if b.get("recipe") and not b.get("construction") and b.get("target") is not None]
        if recs:
            kg.append({"turn": turn, "cash": round(cash), "buildings": recs})
            del kg[:-int(c["kg_keep"])]
            notes.append("known good recorded at turn %d (cash %.0f, %d buildings)" % (turn, cash, len(recs)))

    # honest burn: value (cash + stock) trend, not cash
    ago_t = [t for t in cb if t <= turn - 24]
    cpt = (cash - cb[max(ago_t)]) / float(turn - max(ago_t)) if ago_t and turn > max(ago_t) else None
    hb = honest_burn(trend or {}, cpt, c)
    st["burn"] = hb
    if hb.get("alert"):
        st["burn_alert"] = hb["alert"]
        notes.append(hb["alert"])
    else:
        st.pop("burn_alert", None)

    # 2. rollback triggers
    entries = []
    moves = goal_moved_recently(goal_act_rows, turn, int(c["slide_turns"]) * 2)
    slide = (ago_cash is not None and ago_cash > 0 and cash <= (1 - c["slide_pct"]) * ago_cash
             and cash < c["healthy_x_floor"] * floor and bool(moves))
    starved = starved_buildings(hist, c)
    starve = len(starved) >= int(c["starve_buildings"])
    cooling = turn - int(st.get("last_rollback_turn") or -10**9) < int(c["cooldown_turns"])
    if (slide or starve) and not cooling:
        rec = pick_known_good(kg, turn, min(moves) if moves else None, c)
        why = ("cash %.0f vs %.0f %d turns ago with %d goal moves in the window" % (cash, ago_cash or 0, c["slide_turns"], len(moves))
               if slide else "starved: %s" % ", ".join(starved))
        if rec:
            entries = restore_entries(rec, snap_buildings)
            st["last_rollback_turn"] = turn
            st["freeze_until_turn"] = turn + int(c["freeze_turns"])
            st["alert"] = ("" if c.get("_live") else "(dry run) ") + "GUARDIAN ROLLBACK turn %d (%s): %d building(s) put back to turn %d, goal raises frozen until turn %d" % (
                turn, why, len(entries), rec["turn"], st["freeze_until_turn"])
            notes.append(st["alert"])
        else:
            st["alert"] = "GUARDIAN: trigger (%s) but no known-good config recorded yet; nothing restored" % why
            notes.append(st["alert"])
    elif (slide or starve) and cooling:
        notes.append("trigger present but a rollback ran %d turns ago: waiting" % (turn - int(st["last_rollback_turn"])))
    elif not frozen_now(st, turn):
        st.pop("alert", None)
    return st, entries, notes


def frozen_now(st, turn):
    return turn < int(st.get("freeze_until_turn") or 0)


def history_rows(n_files=2):
    rows = []
    for path in sorted(glob.glob(os.path.join(HERE, "history", "merc-*.jsonl")))[-n_files:]:
        try:
            for line in open(path):
                try:
                    d = json.loads(line)
                except ValueError:
                    continue
                if d.get("turn") is not None:
                    rows.append(d)
        except OSError:
            continue
    rows.sort(key=lambda d: (int(d["turn"]), d.get("t", "")))
    # one row per turn (the last wins), keep the last 200 turns
    by = {}
    for d in rows:
        by[int(d["turn"])] = d
    return [by[t] for t in sorted(by)][-200:]


def goal_act_rows(limit=400):
    rows = []
    try:
        with open(GOAL_ACT) as f:
            for line in f.readlines()[-limit:]:
                try:
                    rows.append(json.loads(line))
                except ValueError:
                    pass
    except OSError:
        pass
    return rows


def main():
    live_flag = "--live" in sys.argv
    c = cfg()
    live = live_flag and bool(c.get("live"))
    c["_live"] = live
    snap = _load(SNAP, {})
    turn, cash = snap.get("turn"), snap.get("cash")
    if turn is None or cash is None or snap.get("errors"):
        print("guardian: snapshot unusable, skipping")
        return
    goal = _load(GOAL, {})
    fixed = float(goal.get("fixed_cost") or 0)
    gcfg = (_load(CONFIG, {}).get("goal")) or {}
    floor = max(float(gcfg.get("hard_floor") or 1000), float(load_state().get("hard_floor") or 0)) if c.get("live") \
        else float(gcfg.get("hard_floor") or 1000)
    st0 = load_state()
    st, entries, notes = decide(int(turn), float(cash), floor, fixed, history_rows(), goal_act_rows(),
                                snap.get("buildings"), st0, c, debt=debt_owed(), trend=goal.get("trend"))
    fs = _load(FAILSAFE, {})
    if fs.get("level") == 3 and fs.get("since"):
        try:
            import datetime
            since = datetime.datetime.fromisoformat(fs["since"])
            hrs = (datetime.datetime.now(datetime.timezone.utc) - since).total_seconds() / 3600.0
            if hrs >= c["long_stop_turns"]:
                st["alert"] = (st.get("alert") or "") + (" | " if st.get("alert") else "") + \
                    "FAILSAFE STOP for %.0f h (cash %.0f)" % (hrs, cash)
                notes.append("long STOP: %.0f h" % hrs)
        except (ValueError, TypeError):
            pass
    print("guardian: turn %s cash %.0f floor %.0f fixed %.0f live=%s" % (turn, cash, floor, fixed, live))
    for n in notes:
        print("guardian:", n)
    for e in entries:
        print("guardian: %s %s" % ("SEND" if live else "would send", json.dumps(e)))
    if live:
        import order_queue as q
        for e in entries:
            try:
                r = q.apply_entry(e)
            except (Exception, SystemExit) as ex:
                r = dict(ok=False, error="%s: %s" % (type(ex).__name__, ex))
            q.log(e, r, source="guardian")
            print("guardian: ->", "OK" if r.get("ok") else "FAILED")
    import datetime
    st["t"] = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    st["last_run"] = {"turn": turn, "cash": round(float(cash)), "live": live, "entries": len(entries)}
    # state is kept in both modes; frozen() and floor_override() ignore it unless guardian.live is on
    os.makedirs(os.path.dirname(STATE), exist_ok=True)
    with open(STATE, "w") as f:
        json.dump(st, f, indent=1)
        f.write("\n")


if __name__ == "__main__":
    main()
