"""Season-proof ids (Oct 23): our business, household, home town and storehouse, as the last v2 shadow run read them
from the game (state/v2/ids.json, written every hour from the snapshot). Scripts take their ids from here, so a new
season (new town, new buildings) needs no code change: the first shadow run of the season writes the new ids.
Never raises: a missing file gives the fallback each caller passes (this season's ids)."""
import json
import os

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "state", "v2", "ids.json")


def _load():
    try:
        with open(PATH) as f:
            d = json.load(f)
            return d if isinstance(d, dict) else {}
    except (OSError, ValueError):
        return {}


def get(key, fallback):
    v = _load().get(key)
    return str(v) if v else fallback


def save(snap):
    """Called by v2/shadow.py with a fresh snapshot."""
    d = {"business": snap.get("business_id"), "household": snap.get("household_id"),
         "home_town": snap.get("home_town"), "store": (snap.get("store") or {}).get("id"), "turn": snap.get("turn")}
    if not all(d[k] for k in ("business", "household", "home_town", "store")):
        return False
    if {k: v for k, v in _load().items() if k != "turn"} == {k: v for k, v in d.items() if k != "turn"}:
        return True
    os.makedirs(os.path.dirname(PATH), exist_ok=True)
    with open(PATH, "w") as f:
        json.dump(d, f, indent=1)
    return True
