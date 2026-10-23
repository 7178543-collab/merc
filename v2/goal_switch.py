"""Which jobs the goal planner (v2/goal.py) runs live, and its automatic hand-over (Oct 23).

Taylor: "leave it and it just plays the game ... with full control of everything". So the planner takes the jobs
over by itself, one at a time, once its own model check has held, instead of waiting for someone to flip a switch.

    v2/config.json goal:
      "off": true          kill switch: every job back to the old rules at once (beats everything below)
      "live": {job: true}  a job forced live by hand
      "auto": true         automatic hand-over on (state/v2/goal_live.json, committed by the v2-shadow workflow)
      "auto_promote": [...] the order jobs go live in: rates, buys, sells, ships, invest, trim

A job goes live automatically when the model check (predicted vs real value per turn over 24+ turns) has held on
every one of the last `hold_runs` runs, and the last hand-over was at least `promote_gap_turns` turns ago.
It goes back off by itself when the model check fails `drop_runs` runs in a row (newest job first).
Never raises: unreadable files mean nothing is live.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CONFIG = os.path.join(HERE, "config.json")
STATE = os.path.join(ROOT, "state", "v2", "goal_live.json")
JOBS = ("rates", "buys", "sells", "ships", "invest", "trim")


def _load(path, default):
    try:
        with open(path) as f:
            return json.load(f)
    except (OSError, ValueError):
        return default


def owns(job, cfg=None, state=None):
    cfg = _load(CONFIG, {}) if cfg is None else cfg
    g = (cfg or {}).get("goal") or {}
    if g.get("off"):
        return False
    lv = g.get("live")
    if lv is True or (isinstance(lv, dict) and lv.get(job)):
        return True
    if not g.get("auto"):
        return False
    st = _load(STATE, {}) if state is None else state
    return bool(((st or {}).get("live") or {}).get(job))


def model_ok(sc):
    return bool(sc) and abs(sc["predicted"] - sc["real"]) <= max(40.0, 0.5 * abs(sc["real"]))


def promote(cfg, goal_hist, sc, turn, state=None, path=STATE):
    """Run once per shadow run. Returns a short line about what changed (or None). goal_hist rows carry 'check'
    (True/False/None) from earlier runs; sc is this run's scorecard."""
    g = (cfg or {}).get("goal") or {}
    if g.get("off") or not g.get("auto") or turn is None:
        return None
    st = _load(path, {}) if state is None else state
    live = st.setdefault("live", {})
    order = [j for j in (g.get("auto_promote") or JOBS) if j in JOBS]
    hold, drop, gap = int(g.get("hold_runs", 12)), int(g.get("drop_runs", 3)), int(g.get("promote_gap_turns", 24))
    checks = [r.get("check") for r in goal_hist if r.get("check") is not None] + [model_ok(sc) if sc else None]
    checks = [c for c in checks if c is not None]
    msg = None
    if sc and sc.get("turns", 0) >= 24 and len(checks) >= drop and not any(checks[-drop:]):
        on = [j for j in order if live.get(j)]
        if on:
            live[on[-1]] = False
            st["last_turn"] = turn
            msg = "goal planner: model check failed %d runs in a row, %s handed back to the old rules" % (drop, on[-1])
    elif sc and sc.get("turns", 0) >= 24 and len(checks) >= hold and all(checks[-hold:]) \
            and turn - int(st.get("last_turn") or -10 ** 9) >= gap:
        nxt = next((j for j in order if not live.get(j)), None)
        if nxt:
            live[nxt] = True
            st["last_turn"] = turn
            msg = "goal planner: model check held %d runs, it now runs '%s' live" % (hold, nxt)
    if msg:
        st.setdefault("log", []).append({"turn": turn, "msg": msg})
        st["log"] = st["log"][-30:]
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w") as f:
                json.dump(st, f, indent=1)
        except OSError:
            pass
    return msg
