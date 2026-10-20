"""Season-end spend-down (Taylor, Oct 20: "plan the season end around how legacy works").

Why: total prestige drains into legacy at 0.5% a turn, so a point of prestige gained with T turns left becomes
(1 - 0.995**T) legacy by the season's end: ~99% from Oct 20, ~90% from Nov 10, ~70% from Nov 20, ~45% from Nov 25,
~11% on the last day. Cash and stock are worth nothing after the season, so from `start` the bot stops hoarding:
the 20k cash gates on park plots, the banquet, the quarry and church readiness drop to small floors (kept above the
failsafe brake), ships may stock church goods, and outputs are sold down faster.

Switch: v2/config.json "endgame" (merged over DEFAULT below); "on": false turns it all off. Every rule that reads it
logs which floor it used, so a run shows plainly whether the endgame is active.
"""
import datetime
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
CONFIG = os.path.join(HERE, "v2", "config.json")

DEFAULT = {
    "on": False,                            # only v2/config.json "endgame": {"on": true} switches it on
    "start": "2026-11-10T00:00:00Z",        # ~20 days left: prestige gained from here still turns ~90% into legacy
    "season_end": "2026-11-30T11:00:00Z",   # 12:00 CET (game code constant + mercatorio.io)
    "plot_min_cash": 5000,                  # park plots (AUTO_PLOT) and the quarry on bought labour: was 20k
    "banquet_on_cash": 6000,                # banquet back on over this (was 15k) ...
    "banquet_off_cash": 4500,               # ... and off under this (was 10k); both above the failsafe brake (4k)
    "church_min_cash": 5000,                # ship_church (windows, tapestries) and readiness buys kept after a fill
    "sell_drawdown_turns": 3,               # outputs: sell what's over the keep in 3 turns (was 12)
}


def _utc(s):
    return datetime.datetime.fromisoformat(str(s).replace("Z", "+00:00"))


def settings(cfg=None):
    if cfg is None:
        try:
            cfg = json.load(open(CONFIG))
        except (OSError, ValueError):
            cfg = {}
    out = dict(DEFAULT)
    out.update({k: v for k, v in ((cfg or {}).get("endgame") or {}).items() if not str(k).startswith("_")})
    return out


def active(now=None, cfg=None):
    s = settings(cfg)
    now = now or datetime.datetime.now(datetime.timezone.utc)
    try:
        return bool(s.get("on")) and _utc(s["start"]) <= now < _utc(s["season_end"])
    except (KeyError, ValueError, TypeError):
        return False


def turns_left(now=None, cfg=None):
    s = settings(cfg)
    now = now or datetime.datetime.now(datetime.timezone.utc)
    return max(0, int((_utc(s["season_end"]) - now).total_seconds() // 3600))


def legacy_share(turns):
    """Share of a prestige point gained now that becomes legacy by the season's end."""
    return 1 - 0.995 ** max(0, turns)


def floor(key, normal, now=None, cfg=None):
    """The endgame value for `key` while active, else `normal`."""
    return settings(cfg)[key] if active(now, cfg) else normal


if __name__ == "__main__":
    t = turns_left()
    print("endgame %s: start %s, %d turns left, a point gained now becomes %.0f%% legacy" % (
        "ACTIVE" if active() else "not active", settings()["start"], t, 100 * legacy_share(t)))
