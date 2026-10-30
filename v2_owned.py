"""Which store items bot v2 runs live. Every v1 writer skips these, so the two bots never fight over one order.

v2 owns an item when it is listed in v2/config.json "live" -> "items" and is not suspended in
state/v2/suspended.json (v2's actor suspends an item on its own after repeated risk flags or failed
writes; the item then goes straight back to v1). Delete the suspended entry to hand it back to v2.

Never raises: an unreadable file means v2 owns nothing, and v1 carries on as before.
"""
import json
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
CONFIG = os.path.join(ROOT, "v2", "config.json")
SUSPENDED = os.path.join(ROOT, "state", "v2", "suspended.json")
ACT_STATE = os.path.join(ROOT, "state", "v2", "act_state.json")


def _load(path, default):
    try:
        with open(path) as f:
            return json.load(f)
    except (OSError, ValueError):
        return default


def owned_items():
    cfg = _load(CONFIG, {})
    live = set(((cfg.get("live") or {}).get("items")) or [])
    sus = _load(SUSPENDED, {})
    # ship trade goods (v2/ships.py trade mode, Oct 13): their home orders are v2's alone
    st = _load(ACT_STATE, {})
    trade = set((st.get("trade_items") or {}) if isinstance(st, dict) else [])
    build = set()
    if goal_owns("invest"):          # materials for a building the goal planner started (v2/act.py buys them)
        plan = _load(os.path.join(ROOT, "state", "v2", "plan.json"), {}) or {}
        build = {k for k, o in (plan.get("orders") or {}).items() if isinstance(o, dict) and o.get("build_buy")}
    if goal_owns("buys"):            # inputs the goal planner buys for today's rates (v2/goal.apply_orders)
        plan = _load(os.path.join(ROOT, "state", "v2", "plan.json"), {}) or {}
        build |= {k for k, o in (plan.get("orders") or {}).items() if isinstance(o, dict) and o.get("goal_buy")}
    if goal_owns("sells"):           # goods the goal planner sells that nobody offered
        plan = _load(os.path.join(ROOT, "state", "v2", "plan.json"), {}) or {}
        build |= {k for k, o in (plan.get("orders") or {}).items() if isinstance(o, dict) and o.get("goal_sell")}
    return (live - set(sus if isinstance(sus, dict) else [])) | trade | build


def owned(item):
    return item in owned_items()


def goal_owns(job):
    """True when the goal planner (v2/goal.py) runs this job live: v2/config.json goal.live.<job>, one of
    rates (building rates and duty), buys, sells, invest (plots and builds). Every other writer of that job stands
    aside then, so nothing fights the plan. Off unless switched on; an unreadable config means off."""
    try:
        import sys
        sys.path.insert(0, os.path.join(ROOT, "v2"))
        import goal_switch
        return goal_switch.owns(job)
    except Exception:
        return False


def chain_owned():
    """True when bot v2 sets the textile chain's production targets (v2/config.json live.chain, not suspended as
    "chain"). chain_balancer.py stands aside then."""
    cfg = _load(CONFIG, {})
    if cfg.get("hand_rates"):        # Oct 30 fresh start: building rates are set by hand only; the balancer stands aside
        return True
    sus = _load(SUSPENDED, {})
    ov = (_load(os.path.join(ROOT, "state", "overrides.json"), {}) or {}).get("chain")
    live = (ov == "v2") if ov in ("v2", "v1") else bool((cfg.get("live") or {}).get("chain"))
    return (live and "chain" not in (sus if isinstance(sus, dict) else {})) or goal_owns("rates")
