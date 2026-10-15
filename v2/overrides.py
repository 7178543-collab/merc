"""Phone-app switches (state/overrides.json, written by the order queue's {"override": {...}} entry) applied on top of
v2/config.json, so a switch flipped on the phone needs no code change and no commit outside state/.

  chain           "v2" | "v1"     who sizes the textile chain (live.chain)
  ship_trade      "on" | "off"    ships also trade goods we neither make nor use (ship_trade.on)
  church_imports  "on" | "off"    ships stock tapestries/windows for church asks (ship_church.on)
(banquet and quarry are read by prestige_rules.py itself.)
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, "state", "overrides.json")


def load():
    try:
        with open(PATH) as f:
            d = json.load(f)
        return d if isinstance(d, dict) else {}
    except (OSError, ValueError):
        return {}


def apply(cfg, ov=None):
    """cfg with the app's switches applied (in place, also returned). Unknown or 'auto' values change nothing."""
    ov = load() if ov is None else ov
    if ov.get("chain") in ("v2", "v1"):
        cfg.setdefault("live", {})["chain"] = ov["chain"] == "v2"
    if ov.get("ship_trade") in ("on", "off"):
        cfg.setdefault("ship_trade", {})["on"] = ov["ship_trade"] == "on"
    if ov.get("church_imports") in ("on", "off"):
        cfg.setdefault("ship_church", {})["on"] = ov["church_imports"] == "on"
    return cfg
