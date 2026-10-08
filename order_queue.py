#!/usr/bin/env python3
"""One-shot order queue (Oct 2026): lets Claude (or Taylor) change a storehouse
order by committing a line to state/order_queue.json instead of clicking in-game.

merc_actor.py calls apply_queue() at the start of every LIVE run. Each entry is
applied once, its result is appended to state/order_queue_done.jsonl, and the
queue file is emptied (the workflow's history step commits state/).

Entry format (state/order_queue.json is a JSON list):
  {"item": "cloth", "tier": 0, "set": {"sell_volume": 30, "sell_price": "8.00", "min_holding": 600},
   "note": "why"}
  - "building" optional, defaults to the main storehouse.
  - "tier" = which manager rule (0 = tier 1). If that tier doesn't exist yet,
    a new rule is added with just the "set" fields.
  - Manager fields: buy_volume, buy_price, max_holding, sell_volume, sell_price, min_holding.
Safety: only those six fields are accepted; anything else in "set" is refused.
"""
import datetime
import json
import os
import urllib.error
import urllib.parse
import urllib.request

import merc_status4 as m

HERE = os.path.dirname(os.path.abspath(__file__))
QUEUE = os.path.join(HERE, "state", "order_queue.json")
DONE = os.path.join(HERE, "state", "order_queue_done.jsonl")
STORE = "152202386005001"
FIELDS = {"buy_volume", "buy_price", "max_holding", "sell_volume", "sell_price", "min_holding"}
PRICE_FIELDS = {"buy_price", "sell_price"}


def _patch(building_id, item, managers):
    url = "https://play.mercatorio.io/api/buildings/%s/storage/inventory/%s" % (
        building_id, urllib.parse.quote(item, safe=""))
    req = urllib.request.Request(
        url, data=json.dumps({"managers": managers}, default=str).encode(), method="PATCH",
        headers={"X-Merc-User": m.USER, "Authorization": "Bearer " + m.TOKEN,
                 "Content-Type": "application/json", "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return True, r.status, r.read().decode()[:300]
    except urllib.error.HTTPError as e:
        return False, e.code, e.read().decode()[:300]
    except Exception as e:
        return False, None, "%s: %s" % (type(e).__name__, e)


def _apply_one(e):
    item = e["item"]
    bid = str(e.get("building") or STORE)
    sets = e.get("set") or {}
    bad = set(sets) - FIELDS
    if bad:
        return dict(ok=False, error="refused fields %s" % sorted(bad))
    b = m.get("/buildings/%s" % bid) or {}
    hold = (((b.get("storage") or {}).get("inventory") or {}).get("holdings") or {}).get(item)
    if hold is None:
        return dict(ok=False, error="item %r not in building %s" % (item, bid))
    mgrs = [{k: v for k, v in mg.items() if k != "result"} for mg in (hold.get("managers") or []) if mg]
    tier = int(e.get("tier", 0))
    clean = {k: (str(v) if k in PRICE_FIELDS else int(v)) for k, v in sets.items()}
    before = json.loads(json.dumps(mgrs, default=str))
    if tier < len(mgrs):
        mgrs[tier].update(clean)
    else:
        mgrs.append(clean)
    ok, status, body = _patch(bid, item, mgrs)
    return dict(ok=ok, status=status, body=body, before=before, after=mgrs)


def apply_queue(live):
    """Apply and clear the queue. Dry run (live=False) only prints what it would do."""
    try:
        with open(QUEUE) as f:
            q = json.load(f)
    except (FileNotFoundError, ValueError):
        return
    if not q:
        return
    if not live:
        print("order queue (dry run, not sent): %s" % json.dumps(q))
        return
    if not (m.USER and m.TOKEN):
        print("order queue: no credentials, left in place")
        return
    ts = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    with open(DONE, "a") as f:
        for e in q:
            try:
                r = _apply_one(e)
            except Exception as ex:
                r = dict(ok=False, error="%s: %s" % (type(ex).__name__, ex))
            f.write(json.dumps(dict(ts=ts, entry=e, **r), default=str) + "\n")
            print("order queue: %s %s -> %s" % (e.get("item"), e.get("set"), "OK" if r.get("ok") else "FAILED"))
    with open(QUEUE, "w") as f:
        f.write("[]\n")


if __name__ == "__main__":
    import sys
    apply_queue("--live" in sys.argv)
