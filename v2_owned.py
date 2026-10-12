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
    return live - set(sus if isinstance(sus, dict) else [])


def owned(item):
    return item in owned_items()
