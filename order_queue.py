#!/usr/bin/env python3
"""One-shot order queue: applies state/order_queue.json (list of {item, tier, set:{field:value}}; add "transport": <ship id> for a ship route order) then clears it. Run by .github/workflows/order-queue.yml."""
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


def _apply_transport(e, sets):
    """Ship route import/export order. Current API (Oct 2026): GET route.holdings[item].managers
    (a list, like the storehouse), PATCH /transports/{id}/route/inventory/{item} {"managers": [...]}."""
    tid, item = str(e["transport"]), e["item"]
    t = m.get("/transports/%s" % tid) or {}
    route = t.get("route") or {}
    if not route.get("id"):
        return dict(ok=False, error="transport %s has no route" % tid)
    hold = (route.get("holdings") or {}).get(item) or {}
    mgrs = [{k: v for k, v in mg.items() if k != "result"} for mg in (hold.get("managers") or []) if mg]
    before = json.loads(json.dumps(mgrs, default=str))
    tier = int(e.get("tier", 0))
    clean = {k: (str(v) if k in PRICE_FIELDS else int(v)) for k, v in sets.items()}
    if tier < len(mgrs):
        mgrs[tier].update(clean)
    else:
        mgrs.append(clean)
    url = "https://play.mercatorio.io/api/transports/%s/route/inventory/%s" % (tid, urllib.parse.quote(item, safe=""))
    req = urllib.request.Request(
        url, data=json.dumps({"managers": mgrs}, default=str).encode(), method="PATCH",
        headers={"X-Merc-User": m.USER, "Authorization": "Bearer " + m.TOKEN,
                 "Content-Type": "application/json", "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            r.read()
    except urllib.error.HTTPError as ex:
        return dict(ok=False, status=ex.code, body=ex.read().decode()[:300], before=before, after=mgrs)
    # verify it stuck (an ignored payload still returns 200)
    t2 = m.get("/transports/%s" % tid) or {}
    now = (((t2.get("route") or {}).get("holdings") or {}).get(item) or {}).get("managers") or []
    def same(a, b):
        try:
            return abs(float(a) - float(b)) < 1e-6
        except (TypeError, ValueError):
            return str(a) == str(b)
    ok = any(all(same(mg.get(k), v) for k, v in clean.items()) for mg in now if mg)
    return dict(ok=ok, status=200, before=before, after=now, error=None if ok else "200 but not applied")


def _apply_one(e):
    item = e["item"]
    bid = str(e.get("building") or STORE)
    sets = e.get("set") or {}
    bad = set(sets) - FIELDS
    if bad:
        return dict(ok=False, error="refused fields %s" % sorted(bad))
    if e.get("transport"):
        return _apply_transport(e, sets)
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
