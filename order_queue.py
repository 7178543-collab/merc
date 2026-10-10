#!/usr/bin/env python3
"""Order queue: applies state/order_queue.json then clears it. Run by .github/workflows/order-queue.yml.

Entry kinds (a JSON list of these):
  storehouse order  {"item": "cloth", "tier": 0, "set": {"sell_volume": 30, "sell_price": "8.00", "min_holding": 600}}
  ship route order  {"transport": "<ship id>", "item": "limestone", "set": {"buy_volume": 20, ...}}
  building producer {"building": "<id>", "producer": {"recipe": "hold banquet 1 (fish)", "target": 1}}
  ship operation    {"transport": "<ship id>", "operation_target": 0}   (0 pauses it in place)
  household slot    {"household": "21623", "item": "light armour", "set": {"buy_volume": 1, "buy_price": "90", "max_holding": 2}}
  donate building   {"donate": "<building id>", "confirm": true}   (permanent; Taylor's say-so only)
  read-only dump    {"dump": "/scoreboard/main"}   (GET, saved to state/dump/api/<path>.json)
Every change is re-read after sending and only logged ok if the game actually holds it.
apply_entry() is also used by rule scripts (prestige_rules.py).
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


def _req(method, path, body):
    req = urllib.request.Request(
        "https://play.mercatorio.io/api" + path, data=json.dumps(body, default=str).encode(), method=method,
        headers={"X-Merc-User": m.USER, "Authorization": "Bearer " + m.TOKEN,
                 "Content-Type": "application/json", "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return True, r.status, r.read().decode()[:300]
    except urllib.error.HTTPError as e:
        return False, e.code, e.read().decode()[:300]
    except Exception as e:
        return False, None, "%s: %s" % (type(e).__name__, e)


def _same(a, b):
    # the game leaves a zeroed field out (buy_volume 0 comes back missing, a stopped
    # producer's target comes back null), so treat missing/blank as 0
    z = lambda x: 0.0 if x is None or x == "" else float(x)
    try:
        return abs(z(a) - z(b)) < 1e-6
    except (TypeError, ValueError):
        return str(a) == str(b)


def _merge(mgrs, tier, clean):
    mgrs = [dict(x) for x in mgrs]
    if tier < len(mgrs):
        mgrs[tier].update(clean)
        # the game refuses a fixed price and a markup on the same side
        if "sell_price" in clean:
            mgrs[tier].pop("sell_markup", None)
            mgrs[tier].pop("markup_price", None)
        if "buy_price" in clean:
            mgrs[tier].pop("buy_markup", None)
    else:
        mgrs.append(clean)
    return mgrs


def _held(now, clean):
    return any(all(_same(mg.get(k), v) for k, v in clean.items()) for mg in now if mg)


def _clean(sets):
    return {k: (str(v) if k in PRICE_FIELDS else int(v)) for k, v in sets.items()}


def _store_holding(bid, item):
    b = m.get("/buildings/%s" % bid) or {}
    return (((b.get("storage") or {}).get("inventory") or {}).get("holdings") or {}).get(item) or {}


def _store_managers(bid, item):
    hold = _store_holding(bid, item)
    return [{k: v for k, v in mg.items() if k != "result"} for mg in (hold.get("managers") or []) if mg]


def _route_managers(tid, item):
    t = m.get("/transports/%s" % tid) or {}
    route = t.get("route") or {}
    hold = (route.get("holdings") or {}).get(item) or {}
    return route.get("id"), [{k: v for k, v in mg.items() if k != "result"} for mg in (hold.get("managers") or []) if mg]


def _apply_store(e, clean):
    """Storehouse order and/or storage capacity ("capacity": N frees or reserves space for the item)."""
    bid, item = str(e.get("building") or STORE), e["item"]
    hold = _store_holding(bid, item)
    before = [{k: v for k, v in mg.items() if k != "result"} for mg in (hold.get("managers") or []) if mg]
    mgrs = _merge(before, int(e.get("tier", 0)), clean) if clean else before
    body = {"managers": mgrs}
    if e.get("capacity") is not None:
        body["capacity"] = int(e["capacity"])
    ok, status, resp = _req("PATCH", "/buildings/%s/storage/inventory/%s" % (bid, urllib.parse.quote(item, safe="")), body)
    if not ok:
        return dict(ok=False, status=status, body=resp, before=before, capacity_before=hold.get("capacity"))
    h2 = _store_holding(bid, item)
    now = [{k: v for k, v in mg.items() if k != "result"} for mg in (h2.get("managers") or []) if mg]
    good = (not clean or _held(now, clean)) and (e.get("capacity") is None or _same(h2.get("capacity"), e["capacity"]))
    return dict(ok=good, status=status, before=before, after=now, capacity_before=hold.get("capacity"),
                capacity_after=h2.get("capacity"), error=None if good else "200 but not applied")


def _apply_transport(e, clean):
    tid, item = str(e["transport"]), e["item"]
    rid, before = _route_managers(tid, item)
    if not rid:
        return dict(ok=False, error="transport %s has no route" % tid)
    mgrs = _merge(before, int(e.get("tier", 0)), clean)
    ok, status, body = _req("PATCH", "/transports/%s/route/inventory/%s" % (tid, urllib.parse.quote(item, safe="")),
                            {"managers": mgrs})
    if not ok:
        return dict(ok=False, status=status, body=body, before=before)
    _, now = _route_managers(tid, item)
    good = _held(now, clean)
    return dict(ok=good, status=status, before=before, after=now, error=None if good else "200 but not applied")


def read_producer(bid):
    p = (m.get("/buildings/%s" % bid) or {}).get("producer") or {}
    return {"recipe": p.get("recipe"), "target": p.get("target"), "provider_id": p.get("provider_id")}


def _apply_producer(e):
    bid, want = str(e["building"]), e["producer"]
    before = read_producer(bid)
    body = {"target": "%.3f" % float(want.get("target", 0)),
            "autoset_buying": False, "autoset_selling": False, "allow_overprod": False}
    if want.get("recipe"):
        body["recipe"] = want["recipe"]
    tries = []
    for method in ("PUT", "POST"):
        ok, status, resp = _req(method, "/buildings/%s/producer" % bid, body)
        tries.append([method, status, resp[:200]])
        if ok:
            break
    if want.get("provider_id") and str(read_producer(bid).get("provider_id")) != str(want["provider_id"]):
        # the storehouse link is a field on the building itself, not the producer
        ok, status, resp = _req("PATCH", "/buildings/%s" % bid, {"provider_id": str(want["provider_id"])})
        tries.append(["PATCH building provider", status, resp[:120]])
    now = read_producer(bid)
    good = (_same(now.get("target"), want.get("target", 0)) and (not want.get("recipe") or now.get("recipe") == want["recipe"])
            and (not want.get("provider_id") or str(now.get("provider_id")) == str(want["provider_id"])))
    return dict(ok=good, before=before, after=now, tries=tries, error=None if good else "not applied")


def _apply_ship_operation(e):
    """Ship crew/operation level: PUT /transports/{id}/operation {"operation_target"} (0 = paused in place,
    route and orders kept). Takes effect at the turn tick; the next turn's previous_operation.target shows it."""
    tid = str(e["transport"])
    before = ((m.get("/transports/%s" % tid) or {}).get("previous_operation") or {}).get("target")
    ok, status, resp = _req("PUT", "/transports/%s/operation" % tid, {"operation_target": "%.3f" % float(e["operation_target"])})
    return dict(ok=ok, status=status, before=before, after=e["operation_target"], body=None if ok else resp,
                note="applies at the turn tick")


def _apply_household_slot(e):
    """Household sustenance slot (gear / luxury / food): PATCH /households/{id}/sustenance/inventory/{item}
    with its buy manager. Adding a product to an empty gear or luxury slot is how the game fills the slot."""
    hid, item = str(e["household"]), e["item"]
    path = "/households/%s/sustenance/inventory/%s" % (hid, urllib.parse.quote(item, safe=""))

    def holding():
        h = m.get("/households/%s" % hid) or {}
        return (((h.get("sustenance") or {}).get("inventory") or {}).get("holdings") or {}).get(item)
    before = holding()
    body = {}
    if e.get("set"):
        body = {"managers": [_clean(e["set"])]}
    ok, status, resp = _req("PATCH", path, body)
    if not ok:
        return dict(ok=False, status=status, body=resp, before=before)
    after = holding()
    good = after is not None and (not e.get("set") or _held([x for x in (after.get("managers") or [])], _clean(e["set"])))
    return dict(ok=good, status=status, before=before, after=after, error=None if good else "200 but not applied")


def _apply_dump(e):
    """Read-only: GET an API path and save it to state/dump/api/<path>.json (for analysis)."""
    import re
    path = e["dump"]
    req = urllib.request.Request("https://play.mercatorio.io/api" + path, method="GET",
                                 headers={"X-Merc-User": m.USER, "Authorization": "Bearer " + m.TOKEN, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            data = json.loads(r.read().decode())
    except urllib.error.HTTPError as ex:
        return dict(ok=False, status=ex.code, error=ex.read().decode()[:200])
    except Exception as ex:
        return dict(ok=False, error="%s: %s" % (type(ex).__name__, ex))
    name = re.sub(r"[^a-z0-9]+", "_", path.lower()).strip("_") or "root"
    out = os.path.join(HERE, "state", "dump", "api")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, name + ".json"), "w") as f:
        json.dump(data, f)
    return dict(ok=data is not None, saved="state/dump/api/%s.json" % name, size=len(json.dumps(data)))


def _apply_donate(e):
    """Donate a building to the church (permanent). Needs "confirm": true in the entry, so a stray
    or mistyped entry can never give a building away. POST /buildings/{id}/donate (game code)."""
    bid = str(e["donate"])
    if e.get("confirm") is not True:
        return dict(ok=False, error="donate needs \"confirm\": true")
    before = m.get("/buildings/%s" % bid) or {}
    ok, status, body = _req("POST", "/buildings/%s/donate" % bid, {"confirm_id": bid, "building_id": bid})
    if not ok:
        return dict(ok=False, status=status, body=body, before_owner=before.get("owner_id"))
    ids = ((m.get("/businesses/%s" % before.get("owner_id")) or {}).get("building_ids") or []) if before.get("owner_id") else []
    good = bid not in ids
    return dict(ok=good, status=status, body=body[:200], building=before.get("name"),
                error=None if good else "200 but still ours")


def apply_entry(e):
    if e.get("donate"):
        return _apply_donate(e)
    if e.get("dump"):
        return _apply_dump(e)
    if e.get("household"):
        return _apply_household_slot(e)
    if e.get("producer"):
        return _apply_producer(e)
    if e.get("transport") and "operation_target" in e:
        return _apply_ship_operation(e)
    sets = e.get("set") or {}
    bad = set(sets) - FIELDS
    if bad:
        return dict(ok=False, error="refused fields %s" % sorted(bad))
    clean = _clean(sets)
    if e.get("transport"):
        return _apply_transport(e, clean)
    return _apply_store(e, clean)


def log(e, r, source="queue"):
    ts = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    with open(DONE, "a") as f:
        f.write(json.dumps(dict(ts=ts, source=source, entry=e, **r), default=str) + "\n")


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
    for e in q:
        try:
            r = apply_entry(e)
        except (Exception, SystemExit) as ex:   # merc_status4.get() exits on HTTP errors; never let one entry stall the queue
            r = dict(ok=False, error="%s: %s" % (type(ex).__name__, ex))
        log(e, r)
        print("order queue: %s -> %s" % (e.get("item") or e.get("building"), "OK" if r.get("ok") else "FAILED %s" % r.get("error")))
    with open(QUEUE, "w") as f:
        f.write("[]\n")


if __name__ == "__main__":
    import sys
    apply_queue("--live" in sys.argv)
