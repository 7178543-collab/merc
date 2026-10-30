#!/usr/bin/env python3
"""Order queue: applies state/order_queue.json then clears it. Run by .github/workflows/order-queue.yml.

Entry kinds (a JSON list of these):
  storehouse order  {"item": "cloth", "tier": 0, "set": {"sell_volume": 30, "sell_price": "8.00", "min_holding": 600}}
  ship route order  {"transport": "<ship id>", "item": "limestone", "set": {"buy_volume": 20, ...}}
  building producer {"building": "<id>", "producer": {"recipe": "hold banquet 1 (fish)", "target": 1}}
  ship operation    {"transport": "<ship id>", "operation_target": 0}   (0 pauses it in place)
  household slot    {"household": "21623", "item": "light armour", "set": {"buy_volume": 1, "buy_price": "90", "max_holding": 2}}
                    swap a product: {"household": "21623", "item": "pasties", "replace": "bread"} (old one removed first)
  prestige spend    {"prestige": "prestige_management", "cost": 100, "confirm": true, "max_cost": 300}   (permanent; Taylor's go-ahead only;
                    retries once at the game's stated cost if free prestige and max_cost allow)
  rules override    {"override": {"banquet": "auto"|"on"|"off"}}    (phone app)
  contract approval {"contract": "<id>", "confirm": true}           (phone app; contracts.py fills it only if stock covers it now)
  note for Claude   {"message": "..."}                              (phone app; appended to state/notes_for_claude.md)
  donate building   {"donate": "<building id>", "confirm": true}   (permanent; Taylor's say-so only)
  town test         {"town_pick": {}}   (read-only; Season 9 turn-1 town ranking -> state/town_pick.md)
  read-only dump    {"dump": "/scoreboard/main"}   (GET, saved to state/dump/api/<path>.json)
  sea map (read-only) {"seamap": {"x0": 1312, "y0": 2208, "x1": 1535, "y1": 2399}}  (GET map sections, saved as one compact
                    sea/land grid in state/seamap/; used by tools/seapath.py)
  build (new site)  {"build": {"type": "park", "town_id": "152202387", "location": "1522:2388", "sublocation": {"x": 3, "y": 3}}, "confirm": true}
                    (no confirm = dry run: cost + payload only)
  expand building   {"expand": {"building": "<id>", "count": 1}, "confirm": true}   (park plots: adds free centre tiles; no confirm = dry run)
                    district buildings (farmstead etc., map land "x:y"): suitable land in range, quoted by the town; confirm
                    buys it (max_ask 30 a tile) and runs the expansion after the tick; "tiles": [...] expands onto held land
  deferred step     {"later": {"after": "2026-10-13T00:05:00Z", "entry": {...any entry above...}}}   (parked in state/deferred.json;
                    runs on the first workflow run at/after that time; for steps that need a turn tick in between)
  bot v2 item       {"v2": {"suspend": "porterage"}} hands it back to v1 now; {"v2": {"resume": "porterage"}} gives it back to v2
  trade route       {"route": {"transport": id, "start": true}, "confirm": true} / {"route": {"transport": id, "stop": true}, ...}
  world market      {"world": "all"} or {"world": ["Blanans"]}   (public market data, saved compact to state/dump/world.json.gz)
  construction link {"construction": {"building": "<id>", "set": {"provider_id": "<storehouse>"}}}   (PATCH its construction)
  construction pace {"pace": {"building": "<id>", "pace": 100}}   (0/25/50/100; a new construction starts at 0 = no deliveries)
  one more plot     {"plot": {"building": "<id>"}, "confirm": true}   (no map click: expands onto land we own, or claims the
                    nearest free tile and expands after the next tick; skips while building or already waiting)
  new building      {"site": {"type": "net maker"}, "confirm": true}   (no map click: a free town-centre tile nearest the
                    storehouse, bought if nobody owns it, then the site, storehouse link and pace 100; optional "tile",
                    "near"; a tile that settles at the tick defers the rest; no confirm = dry run)
  ship travel       {"travel": {"transport": "<ship id>", "to_town": "<town id>"}, "confirm": true}   (no confirm = dry run:
                    logs the sea path length/cost only)
  move a worker     {"assign": {"worker": 2, "to": "producer/<building id>"}}   (household worker n; "knight/21623" = net
                    duty, "" = unassigned; the head (worker 0) also needs "head": true; a training worker loses 5% of
                    tier progress on a change)
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
import ids as _ids                               # season-proof ids (state/v2/ids.json, written every hour)
STORE = _ids.get("store", "152202386005001")
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


def _apply_assign(e):
    """Move a household worker (Oct 23): the game client's own call, PUT /households/{id}/workers/{n}
    {assignment: <operation ref>, update_buying, mark_to_market}. Buys stay with the bot, so update_buying is off."""
    a = e["assign"]
    hid = str(a.get("household") or _ids.get("household", "21623"))
    n = int(a["worker"])
    to = str(a.get("to") or "")
    if n == 0 and not a.get("head"):
        return dict(ok=False, error='worker 0 is the head of household: add "head": true to move him')

    def cur():
        ws = (m.get("/households/%s" % hid) or {}).get("workers") or []
        return (ws[n].get("assignment") or "") if len(ws) > n else None
    before = cur()
    if before is None:
        return dict(ok=False, error="no worker %d in household %s" % (n, hid))
    if before == to:
        return dict(ok=True, before=before, after=before, note="already there")
    ok, status, resp = _req("PUT", "/households/%s/workers/%d" % (hid, n),
                            {"assignment": to, "update_buying": False, "mark_to_market": False})
    after = cur()
    good = bool(ok) and after == to
    return dict(ok=good, status=status, before=before, after=after, body=None if ok else resp,
                error=None if good else "assignment not applied")


def _apply_household_slot(e):
    """Household sustenance slot (gear / luxury / food): PATCH /households/{id}/sustenance/inventory/{item}
    with its buy manager. Adding a product to an empty gear or luxury slot is how the game fills the slot."""
    hid, item = str(e["household"]), e["item"]
    path = "/households/%s/sustenance/inventory/%s" % (hid, urllib.parse.quote(item, safe=""))

    def holding(name=item):
        h = m.get("/households/%s" % hid) or {}
        return (((h.get("sustenance") or {}).get("inventory") or {}).get("holdings") or {}).get(name)
    old = e.get("replace")
    if old:
        # swap a slot's product (Oct 18): {"household": id, "item": "pasties", "replace": "bread"} = the game client's own
        # replace: DELETE the old product's holding, then PATCH the new one (game client mt(): deleteResource + patchResource)
        if holding(old) is None:
            return dict(ok=False, error="%s is not a slot product now: nothing to replace" % old)
        ok, status, resp = _req("DELETE", "/households/%s/sustenance/inventory/%s" % (hid, urllib.parse.quote(old, safe="")), {})
        if not ok:
            return dict(ok=False, status=status, body=resp, step="delete %s" % old)
        if holding(old) is not None:
            return dict(ok=False, status=status, error="%s still a slot product after delete" % old)
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
            raw = r.read()
            if raw[:2] == b"\x1f\x8b":  # map sections come back gzipped
                import gzip
                raw = gzip.decompress(raw)
            data = json.loads(raw.decode())
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


PRESTIGE_TRACKS = {"tenants", "management", "transports", "prestige_management", "cargo_slots", "apprentices",
                   "luxuries", "scale_luxuries", "contracts"}


def _apply_prestige_want(e):
    """Phone app "Buy when affordable": add or cancel a prestige track in state/prestige_wants.json. prestige_rules'
    wants_rule buys it at the exact price as soon as free prestige covers it (never above max_cost)."""
    w = e["prestige_want"] or {}
    track = str(w.get("track") or "")
    if track not in PRESTIGE_TRACKS:
        return dict(ok=False, error="unknown prestige track %r" % track)
    path = os.path.join(HERE, "state", "prestige_wants.json")
    try:
        with open(path) as f:
            wants = json.load(f) or []
    except (FileNotFoundError, ValueError):
        wants = []
    wants = [x for x in wants if x.get("track") != track]
    if not w.get("cancel"):
        wants.append({"track": track, "max_cost": int(w["max_cost"]) if w.get("max_cost") else None,
                      "level": w.get("level"),
                      "since": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="minutes")})
    with open(path, "w") as f:
        json.dump(wants, f, indent=1)
    return dict(ok=True, wants=[x["track"] for x in wants])


def _apply_town_pick(e):
    """Read-only: the Season 9 turn-1 town test (tools/town_pick.py). GETs /towns and /towns/{id} for every town,
    writes the compact state/town_pick_data.json and the ranking in state/town_pick.md."""
    import sys as _sys
    _sys.path.insert(0, os.path.join(HERE, "tools"))
    import town_pick

    def get(path):
        req = urllib.request.Request("https://play.mercatorio.io/api" + path, method="GET",
                                     headers={"X-Merc-User": m.USER, "Authorization": "Bearer " + m.TOKEN,
                                              "Accept": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                raw = r.read()
                if raw[:2] == b"\x1f\x8b":
                    import gzip
                    raw = gzip.decompress(raw)
                return json.loads(raw.decode())
        except Exception:
            return None
    rows = town_pick.collect(get)
    if not rows:
        return dict(ok=False, error="GET /towns returned nothing")
    with open(town_pick.DATA, "w") as f:
        json.dump(rows, f, separators=(",", ":"))
    ranked, _ = town_pick.run(rows, check=bool((e.get("town_pick") or {}).get("check", True)))
    return dict(ok=True, towns=len(rows), top=[r["name"] for r in ranked[:5]], saved="state/town_pick.md")


def _apply_donate(e):
    """Donate a building to the church (permanent). Needs "confirm": true in the entry, so a stray
    or mistyped entry can never give a building away. POST /buildings/{id}/donate (game code)."""
    bid = str(e["donate"])
    if e.get("confirm") is not True:
        return dict(ok=False, error="donate needs \"confirm\": true")
    # Oct 30 (Taylor, fresh-start guideline 6): no automated donations. The goal planner's trim job gave away the
    # quarry (Oct 25) and the logging camp (Oct 26) against his keep rules. Only an entry Taylor asked for, marked
    # "taylor": true by hand, can donate anything.
    if e.get("taylor") is not True:
        return dict(ok=False, error="donate refused: needs \"taylor\": true (hand-written entry, Taylor's say-so only)")
    before = m.get("/buildings/%s" % bid) or {}
    ok, status, body = _req("POST", "/buildings/%s/donate" % bid, {"confirm_id": bid, "building_id": bid})
    if not ok:
        return dict(ok=False, status=status, body=body, before_owner=before.get("owner_id"))
    ids = ((m.get("/businesses/%s" % before.get("owner_id")) or {}).get("building_ids") or []) if before.get("owner_id") else []
    good = bid not in ids
    return dict(ok=good, status=status, body=body[:200], building=before.get("name"),
                error=None if good else "200 but still ours")


def _apply_prestige(e):
    """Spend prestige on a track (permanent; Taylor's go-ahead only): {"prestige": "prestige_management",
    "cost": 100, "confirm": true}. POST /households/{id}/prestige/allocate (same call as the Tenants rule)."""
    if e.get("confirm") is not True:
        return dict(ok=False, error="prestige spend needs \"confirm\": true")
    track, cost = e["prestige"], int(e["cost"])
    hid = ((m.get("/player") or {}).get("household") or {}).get("id")
    lvl = lambda: int(m.num(((m.get("/households/%s" % hid) or {}).get("prestige_board") or {}).get(track + "_level")))
    before = lvl()
    ok, status, body = _req("POST", "/households/%s/prestige/allocate" % hid, {"track": track, "cost": str(cost)})
    if not ok and status == 409:
        import re
        mm = re.search(r"expected (\d+)", body or "")
        hh = m.get("/households/%s" % hid) or {}
        free = m.num(hh.get("prestige")) - m.num((hh.get("prestige_board") or {}).get("allocated"))
        if mm and int(mm.group(1)) <= free and int(mm.group(1)) <= int(e.get("max_cost", 10 ** 9)):
            cost = int(mm.group(1))
            ok, status, body = _req("POST", "/households/%s/prestige/allocate" % hid, {"track": track, "cost": str(cost)})
    after = lvl()
    good = after == before + 1
    return dict(ok=good, status=status, body=body[:200], before=before, after=after, error=None if good else "level unchanged")


def _apply_override(e):
    """App switches the rules read: {"override": {"banquet": "auto"|"on"|"off"}} -> state/overrides.json."""
    path = os.path.join(HERE, "state", "overrides.json")
    try:
        with open(path) as f:
            cur = json.load(f)
    except (FileNotFoundError, ValueError):
        cur = {}
    allowed = {"banquet": {"auto", "on", "off"}, "chain": {"v2", "v1"}, "ship_trade": {"on", "off"},
               "church_imports": {"on", "off"}, "quarry": {"auto", "slow"}}
    for k, v in (e.get("override") or {}).items():
        if k not in allowed or v not in allowed[k]:
            return dict(ok=False, error="override %s=%s not allowed" % (k, v))
        cur[k] = v
    with open(path, "w") as f:
        json.dump(cur, f, indent=1)
    return dict(ok=True, after=cur)


def _apply_contract_approval(e):
    """Taylor approves a contract from the app: {"contract": "<id>", "confirm": true}. contracts.py (same
    workflow run, right after) signs and delivers it ONLY if stock covers it now (Taylor's rule)."""
    if e.get("confirm") is not True:
        return dict(ok=False, error="contract approval needs \"confirm\": true")
    path = os.path.join(HERE, "state", "contract_approvals.json")
    try:
        with open(path) as f:
            cur = json.load(f)
    except (FileNotFoundError, ValueError):
        cur = []
    cid = str(e["contract"])
    if cid not in [str(x.get("id")) for x in cur]:
        cur.append({"id": cid, "ts": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")})
    with open(path, "w") as f:
        json.dump(cur[-50:], f, indent=1)
    return dict(ok=True, approved=cid, info="contracts.py fills it this run if stock covers it")


def _apply_message(e):
    """A note from Taylor for the next Claude check-in: {"message": "..."} -> state/notes_for_claude.md."""
    text = str(e.get("message") or "").strip()[:1000]
    if not text:
        return dict(ok=False, error="empty message")
    ts = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="minutes")
    with open(os.path.join(HERE, "state", "notes_for_claude.md"), "a") as f:
        f.write("- %s: %s\n" % (ts, text.replace("\n", " ")))
    return dict(ok=True)


def _get_json(path):
    """Authenticated GET returning parsed JSON; handles gzip. Raises on any error."""
    import gzip
    req = urllib.request.Request("https://play.mercatorio.io/api" + path, method="GET",
                                 headers={"X-Merc-User": m.USER, "Authorization": "Bearer " + m.TOKEN,
                                          "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        raw = r.read()
    if raw[:2] == b"\x1f\x8b":
        raw = gzip.decompress(raw)
    return json.loads(raw.decode())


def _apply_seamap(e):
    """Read-only: fetch the map sections covering a bounding box and save one compact grid.
    A tile is navigable when its area id is even and > 0 (game client rule; odd = land). Rows are '1' (navigable) / '0'.
    Saved gzipped as state/seamap/seamap_<x0>_<y0>_<x1>_<y1>.json.gz (tools/seapath.py reads these)."""
    import gzip
    from concurrent.futures import ThreadPoolExecutor
    b = e["seamap"]
    S = 32
    x0, y0 = int(b["x0"]) // S * S, int(b["y0"]) // S * S
    x1, y1 = int(b["x1"]) // S * S + S - 1, int(b["y1"]) // S * S + S - 1
    w, h = x1 - x0 + 1, y1 - y0 + 1
    if w * h > 600 * 600:
        return dict(ok=False, error="bbox too big (%dx%d), max 600x600 per entry" % (w, h))
    rows = [["0"] * w for _ in range(h)]
    failed = []

    def fetch(pos):
        sx, sy = pos
        for attempt in range(3):
            try:
                return pos, _get_json("/map/section/position/%d:%d" % (sx, sy))["plots"], None
            except Exception as ex:
                err = type(ex).__name__
        return pos, None, err

    todo = [(sx, sy) for sy in range(y0, y1 + 1, S) for sx in range(x0, x1 + 1, S)]
    with ThreadPoolExecutor(max_workers=6) as pool:
        for (sx, sy), plots, err in pool.map(fetch, todo):
            if plots is None:
                failed.append("%d:%d %s" % (sx, sy, err))
                continue
            for i, t in enumerate(plots):
                a = t.get("area") or 0
                if a > 0 and a % 2 == 0:  # the game's own ship rule: even area id = water a ship can use
                    rows[sy - y0 + i // S][sx - x0 + i % S] = "1"
    out = os.path.join(HERE, "state", "seamap")
    os.makedirs(out, exist_ok=True)
    name = "seamap_%d_%d_%d_%d.json.gz" % (x0, y0, x1, y1)
    with gzip.open(os.path.join(out, name), "wt") as f:
        json.dump(dict(x0=x0, y0=y0, w=w, h=h, rows=["".join(r) for r in rows]), f)
    return dict(ok=not failed, saved="state/seamap/" + name, sections=len(todo), failed=failed[:5])


def _apply_travel(e):
    """Send a ship to a town: {"travel": {"transport": "<ship id>", "to_town": "<town id>"}, "confirm": true}.
    Without "confirm": true it is a DRY RUN: computes the sea path (tools/seapath.py) and logs tiles/cost, sends nothing.
    Path rules are the game client's own (A*, 8 directions, step 1 / 1.414); the docking tile is the town's nearest
    sea tile (navigation_zones with an even zone number), as in the client."""
    import math
    import sys
    sys.path.insert(0, os.path.join(HERE, "tools"))
    import seapath
    tr = e["travel"]
    sid, tid = str(tr["transport"]), str(tr["to_town"])
    try:
        ship = _get_json("/transports/%s" % sid)
        town = _town(tid)
    except Exception as ex:
        return dict(ok=False, error="read failed: %s: %s" % (type(ex).__name__, ex))
    loc = ship.get("location") or {}
    start = (int(loc["x"]), int(loc["y"]))
    tl = town.get("location") or {}
    docks = []
    for k, zone in (town.get("navigation_zones") or {}).items():
        if int(zone) % 2 == 0:
            docks.append((int(k) // 100000, int(k) % 100000))
    if not docks:
        return dict(ok=False, error="town %s has no sea dock tile" % tid)
    end = min(docks, key=lambda d: math.hypot(d[0] - tl.get("x", 0), d[1] - tl.get("y", 0)))
    if start == end:
        return dict(ok=False, error="ship is already at %s" % (end,))
    try:
        grid = seapath.SeaGrid.load()
    except SystemExit as ex:
        return dict(ok=False, error=str(ex))
    path, cost = seapath.find_path(grid, start, end)
    if not path:
        return dict(ok=False, error="no sea path %s -> %s in the grid (grid too small, or start/end not sea)" % (start, end))
    info = dict(ship=ship.get("name"), to=town.get("name"), start=start, end=end, tiles=len(path), cost=round(cost, 3))
    if e.get("confirm") is not True:
        return dict(ok=True, dry_run=True, **info)
    prev_end = (ship.get("journey") or {}).get("end_town_id")
    # Ships send no use_ferry (that flag is the land-cart branch; the server answers "ferry-path must start on land")
    body = {"location": {"x": end[0], "y": end[1]}, "path": path,
            "end_town_id": int(tid) if isinstance(prev_end, int) or prev_end is None else tid}
    ok, status, resp = _req("POST", "/transports/%s/travel" % sid, body)
    if not ok:
        return dict(ok=False, status=status, body=resp, **info)
    try:
        after = _get_json("/transports/%s" % sid)
        j = after.get("journey") or {}
        held = str(j.get("end_town_id")) == tid
    except Exception:
        held = False
    return dict(ok=held, status=status, **info, error=None if held else "journey not updated after travel")


def _apply_probe_write(e):
    """Schema discovery with NO side effects: {"probe_write": {"method": "POST", "path": "/buildings", "body": {...}}}.
    Refused unless the body's "type" is the impossible value "zzz_probe", so the game can only ever reject it;
    the status and error text show which endpoint exists and which fields it wants."""
    pw = e["probe_write"]
    method, path, body = str(pw.get("method", "POST")).upper(), str(pw.get("path", "")), pw.get("body") or {}
    if method not in ("POST", "PUT", "PATCH") or body.get("type") != "zzz_probe":
        return dict(ok=False, error='probe_write needs method POST/PUT/PATCH and body.type == "zzz_probe"')
    if not path.startswith(("/buildings", "/towns", "/businesses", "/plots", "/place", "/construction")):
        return dict(ok=False, error="probe_write path not allowed: %s" % path[:60])
    ok, status, resp = _req(method, path, body)
    return dict(ok=True, probe=True, sent="%s %s" % (method, path), status=status, accepted=bool(ok), body=resp)


OWNER_ID = _ids.get("business", "39992")  # our business id (owner_id on every building; also the contract participant id)


def _apply_build(e):
    """Start a building: {"build": {"type": "park", "town_id": "152202387", "location": "1522:2388",
    "sublocation": {"x": 3, "y": 3}}, "confirm": true}. No confirm = DRY RUN (checks the type, shows the cost and
    the payload, sends nothing). The create call is POST /buildings {type, owner_id, town_id, location, sublocation,
    construction: {stage: "INITIAL"}} (shape confirmed by probe_write, Oct 12). It only creates the empty site
    (stage INITIAL); materials and labour still have to be supplied to the construction account."""
    b = e["build"]
    typ = str(b.get("type", ""))
    try:
        specs = json.load(open(os.path.join(HERE, "v2", "data", "buildings.json")))
    except Exception as ex:
        return dict(ok=False, error="cannot read v2/data/buildings.json: %s" % ex)
    spec = specs.get(typ)
    if not spec:
        return dict(ok=False, error="unknown building type %r" % typ)
    body = {"type": typ, "owner_id": OWNER_ID, "town_id": str(b["town_id"]), "location": str(b["location"]),
            "construction": {"stage": "INITIAL"}}
    sub = b.get("sublocation")
    if sub:
        body["sublocation"] = {"x": int(sub["x"]), "y": int(sub["y"])}
    cons = spec.get("construction") or {}
    info = dict(type=typ, materials=cons.get("materials"), build_turns=cons.get("time"), payload=body)
    if e.get("confirm") is not True:
        return dict(ok=True, dry_run=True, **info)
    import re
    ok, status, resp = _req("POST", "/buildings", body)
    if not ok:
        return dict(ok=False, status=status, body=resp, **info)
    m_id = re.search(r'"id"\s*:\s*"?(\d{6,})', resp or "")
    new_id = m_id.group(1) if m_id else None
    stage = None
    if new_id:
        try:
            stage = ((_get_json("/buildings/%s" % new_id).get("construction") or {}).get("stage"))
        except Exception:
            pass
    return dict(ok=bool(new_id) and stage == "INITIAL", status=status, building_id=new_id, stage=stage, **info)


def _town(town_id):
    """GET /towns/{id} with its tiles. Oct 20: the game moved tile ownership and structures out of the town record
    ("domain" keyed by tile id) into GET /towns/{id}/domain ("borough": [{owner_id, structure, location "x.sx:y.sy"}],
    "center_sites": ["x:y"]). Without them every tile read as free and unowned: a park plot was aimed at our own
    brewery's tile and the net maker at a tile someone else owns. Rebuilds the old shape so callers are unchanged."""
    t = _get_json("/towns/%s" % town_id)
    if t.get("domain"):
        return t
    try:
        d = _get_json("/towns/%s/domain" % town_id)
    except Exception:
        d = {}
    dom = {}
    for b in d.get("borough") or []:
        try:
            cx, sx, cy, sy = _parse_loc(b["location"])
        except (KeyError, ValueError):
            continue
        dom[str((cx * 100000 + cy) * 1000000 + sx * 1000 + sy)] = {"owner_id": b.get("owner_id"), "structure": b.get("structure")}
    if not dom:
        raise RuntimeError("town %s tile data unreadable (no domain in /towns or /towns/{id}/domain)" % town_id)
    t["domain"] = dom
    if not t.get("center_ids") and d.get("center_sites"):
        t["center_ids"] = [int(a) * 100000 + int(b) for a, b in (str(s).split(":") for s in d["center_sites"])]
    return t


def _tile_str(cx, sx, cy, sy):
    return "%d.%d:%d.%d" % (cx, sx, cy, sy)


def _parse_loc(loc):
    """'1522.2:2388.4' -> (1522, 2, 2388, 4)."""
    a, b = str(loc).split(":")
    cx, sx = a.split(".")
    cy, sy = b.split(".")
    return int(cx), int(sx), int(cy), int(sy)


def _expansion_candidates(bld, town, rng):
    """Free tiles on the town-centre grids (8 x 8 per centre, 8 sub-tiles per map tile) a building could expand onto:
    no structure, not a road (grid column 4 and row 3), not the main centre (reserved plaza/hall), within `rng`
    sub-tiles of the building, ours or unowned. Ours first, then nearest."""
    bx, bsx, by, bsy = _parse_loc(bld["location"])
    gx0, gy0 = bx * 8 + bsx, by * 8 + bsy
    mine = {t for t in (bld.get("domain") or [])}
    main = (int(town["location"]["x"]), int(town["location"]["y"]))
    dom = town.get("domain") or {}
    out = []
    for cid in town.get("center_ids") or []:
        cx, cy = int(cid) // 100000, int(cid) % 100000
        if (cx, cy) == main:
            continue
        for sy in range(8):
            for sx in range(8):
                if sx == 4 or sy == 3:
                    continue
                tile = _tile_str(cx, sx, cy, sy)
                if tile in mine or tile == bld["location"]:
                    continue
                ent = dom.get(str(cid * 1000000 + sx * 1000 + sy)) or {}
                if ent.get("structure"):
                    continue
                owner = str(ent.get("owner_id") or "")
                if owner not in ("", OWNER_ID):
                    continue
                dist = ((cx * 8 + sx - gx0) ** 2 + (cy * 8 + sy - gy0) ** 2) ** 0.5
                if dist <= rng:
                    out.append(dict(tile=tile, dist=round(dist, 2), ours=(owner == OWNER_ID)))
    out.sort(key=lambda c: (not c["ours"], c["dist"]))
    return out


def _tile_owner(town, tile):
    cx, sx, cy, sy = _parse_loc(tile)
    ent = (town.get("domain") or {}).get(str((cx * 100000 + cy) * 1000000 + sx * 1000 + sy)) or {}
    return str(ent.get("owner_id") or "")


def _claim_tile(town_id, tile):
    """Buy a town-centre tile: POST /towns/{id}/expand {claims: [], properties: [{location: "x.sx:y.sy"}]}.
    From the game's own client (Oct 13): a centre tile nobody owns is a PROPERTY the town sells (ask 24 by default) and
    goes in `properties`; `claims` are for unowned map land outside the centres (domain growth, with a landing route).
    Our Oct 12 attempts sent centre tiles as claims: 200, money reserved, tile never became ours. Returns (ok, error)."""
    body = {"claims": [], "properties": [{"location": str(tile)}]}
    ok, status, resp = _req("POST", "/towns/%s/expand" % town_id, body)
    return ok, (None if ok else "claim refused %s: %s" % (status, (resp or "")[:160].replace("\n", " ")))


def _apply_expand(e):
    """Add plots to an existing building (a park plot is an expansion of the park):
    {"expand": {"building": "152202388002004", "count": 1}, "confirm": true}   or  "tiles": ["1522.6:2388.2"].
    PATCH /buildings/{id} {construction: {stage: "EXPANSION", domain: ["x.sx:y.sy", ...]}} (shape confirmed by probe_write).
    No confirm = DRY RUN (lists the free tiles it would try, and the materials). With confirm it tries candidates
    nearest-first (the game rejects a bad tile harmlessly), claims the land first if it is unowned, and verifies
    the building now shows an expansion.
    Materials come from the provider storehouse by the building's own construction settings; the game enforces
    range, prestige-management and capacity, and its refusal text is logged."""
    ex = e["expand"]
    bid = str(ex["building"])
    count = max(1, int(ex.get("count", 1)))
    try:
        specs = json.load(open(os.path.join(HERE, "v2", "data", "buildings.json")))
        bld = _get_json("/buildings/%s" % bid)
    except Exception as exn:
        return dict(ok=False, error="read failed: %s: %s" % (type(exn).__name__, exn))
    if "." not in str(bld.get("location") or ""):
        # Oct 22: a district building (farmstead, farms, camps) sits on map land "x:y", not a centre sub-tile;
        # the centre path below crashed on it ("not enough values to unpack (expected 2, got 1)")
        return _apply_expand_rural(e, bld, specs)
    try:
        town = _town(bld["town_id"])
    except Exception as exn:
        return dict(ok=False, error="read failed: %s: %s" % (type(exn).__name__, exn))
    spec = (specs.get(bld.get("type")) or {}).get("construction") or {}
    rng = float(spec.get("range") or 8)
    stage = (bld.get("construction") or {}).get("stage")
    if stage not in (None, "", "NONE"):
        return dict(ok=False, error="building already under construction (stage %s)" % stage)
    cands = _expansion_candidates(bld, town, rng)
    wanted = [str(t) for t in ex.get("tiles") or []]
    per = spec.get("materials") or {}
    info = dict(building=bld.get("type"), size=bld.get("size"), range=rng,
                materials_per_plot=per, build_turns=spec.get("time"),
                candidates=[("%s%s %.1f" % (c["tile"], "" if c["ours"] else " (unowned)", c["dist"])) for c in cands[:8]])
    if not wanted and not cands:
        return dict(ok=False, error="no free tile in range", **info)
    plan = wanted or [c["tile"] for c in cands[:count]]
    info["would_try"] = plan
    info["claims_needed"] = [t for t in plan if _tile_owner(town, t) != OWNER_ID]
    info["materials_total"] = {k: v * len(plan) for k, v in per.items()}
    if e.get("confirm") is not True:
        return dict(ok=True, dry_run=True, **info)
    attempts, errors = [], []
    options = [plan] if (wanted or count > 1) else [[c["tile"]] for c in cands[:5]]
    for tiles in options:
        claim_err = None
        for t in tiles:
            if _tile_owner(town, t) != OWNER_ID:
                cok, cerr = _claim_tile(bld["town_id"], t)
                if not cok:
                    claim_err = cerr
                    break
        if claim_err:
            errors.append("%s: %s" % (",".join(tiles), claim_err))
            continue
        body = {"construction": {"stage": "EXPANSION", "domain": tiles}}
        ok, status, resp = _req("PATCH", "/buildings/%s" % bid, body)
        attempts.append(tiles)
        if ok:
            try:
                after = (_get_json("/buildings/%s" % bid).get("construction") or {})
            except Exception:
                after = {}
            held = after.get("stage") == "EXPANSION" and set(tiles) <= set(after.get("domain") or [])
            pace = None
            if held:        # a new construction has no provider and sits at pace 0: nothing is delivered until both are set
                prov = bld.get("provider_id")
                if prov:
                    lok, _, lresp = _req("PATCH", "/buildings/%s/construction" % bid, {"provider_id": str(prov)})
                    if not lok:
                        info["provider_error"] = (lresp or "")[:160]
                pok, _, perr, pace = _set_pace(bid, ex.get("pace", 100))
                if not pok:
                    info["pace_error"] = perr
            return dict(ok=held, status=status, tiles=tiles, stage=after.get("stage"), pace=pace,
                        error=None if held else "expansion not visible after PATCH", **info)
        errors.append("%s: %s" % (",".join(tiles), (resp or "")[:160].replace("\n", " ")))
    return dict(ok=False, error="all attempts refused", refusals=errors, **info)


def _map_plots(x0, y0, x1, y1):
    """{(x, y): plot} for the map tiles in a box, read from the game's 32 x 32 map sections
    (GET /map/section/position/x:y, plots row by row: index = dy * 32 + dx). A plot has alt, area (odd = land,
    even > 0 = water), fertility, forest, region."""
    S = 32
    out = {}
    for sy in range(y0 // S * S, y1 // S * S + 1, S):
        for sx in range(x0 // S * S, x1 // S * S + 1, S):
            for i, p in enumerate(_get_json("/map/section/position/%d:%d" % (sx, sy)).get("plots") or []):
                x, y = sx + i % S, sy + i // S
                if x0 <= x <= x1 and y0 <= y <= y1:
                    out[(x, y)] = p
    return out


def _xy(loc):
    """'1516:2398' (or {"x": 1516, "y": 2398}) -> (1516, 2398)."""
    if isinstance(loc, dict):
        return int(loc["x"]), int(loc["y"])
    a, b = str(loc).split(":")
    return int(float(a)), int(float(b))


def _rural_candidates(bld, spec_all, rng, plots, town_dom=None, taken=()):
    """Map tiles a district building could add as plots: land (odd area), the building type's fertility rule met, within
    `rng` tiles of the building, not already in its domain, no known structure and not someone else's (from the old-style
    town domain when the game still sends it). Tiles touching the current domain first (same soil, one connected
    estate), then nearest. Each: {tile, dist, fertility, adjacent}."""
    bx, by = _xy(bld["location"])
    mine = {_xy(t) for t in (bld.get("domain") or [])} | {(bx, by)}
    taken = set(taken) - mine
    fert = ((spec_all.get("requires") or {}).get("fertility")) or {}
    town_dom = town_dom or {}
    out = []
    for (x, y), p in plots.items():
        if (x, y) in mine or (x, y) in taken:
            continue                    # ours already, or under another of our buildings
        area = int(p.get("area") or 0)
        if area <= 0 or area % 2 == 0:
            continue                    # water
        f = float(p.get("fertility") or 0)
        if fert.get("min") and f < float(fert["min"]):
            continue
        if fert.get("max") and f > float(fert["max"]):
            continue
        dist = ((x - bx) ** 2 + (y - by) ** 2) ** 0.5
        if dist > rng:
            continue
        ent = town_dom.get(str(x * 100000 + y)) or {}
        if ent.get("structure") or str(ent.get("owner_id") or "") not in ("", OWNER_ID):
            continue
        adj = any((x + dx, y + dy) in mine for dx in (-1, 0, 1) for dy in (-1, 0, 1) if dx or dy)
        out.append(dict(tile="%d:%d" % (x, y), dist=round(dist, 2), fertility=f, adjacent=adj))
    out.sort(key=lambda c: (not c["adjacent"], c["dist"]))
    return out


def _land_quote(town_id, tile):
    """The town's quote for taking a district tile (the client's own call before 'claim'/'buy'):
    GET /towns/{id}/expand/position/x:y -> {properties: [{location, plot: {ask_price}}], claims: [...], route: ...}.
    Returns (properties [(location, ask)], claims [..], error)."""
    try:
        q = _get_json("/towns/%s/expand/position/%s" % (town_id, tile))
    except urllib.error.HTTPError as ex:
        try:
            body = ex.read().decode()[:400]
        except Exception:
            body = ""
        # Oct 22: a tile already in the town's domain is not quoted; the 409 says what it is, e.g.
        # "already claimed by town: (empty plot, domain of town 152202387, no owner, for sale at 12)" -> buy it from the
        # town as a property; "(empty plot, ..., owned by 39992)" -> ours already; "(plot with grain farm ...)" -> taken
        import re
        mm = re.search(r"\(empty plot, domain of town \d+, (no owner, for sale at ([\d.]+)|owned by (\d+))", body)
        if ex.code == 409 and mm:
            if mm.group(2):
                return [(str(tile), float(mm.group(2)))], [], None
            if mm.group(3) == OWNER_ID:
                return [], [], "ours"
        return [], [], "quote refused %s %s" % (ex.code, body.replace("\n", " ")[:160])
    except Exception as ex:
        return [], [], "quote failed %s" % type(ex).__name__
    q = q or {}
    props = []
    for p in q.get("properties") or []:
        loc = p.get("location")
        if isinstance(loc, dict):
            loc = "%s:%s" % (loc.get("x"), loc.get("y"))
        props.append((str(loc), float(((p.get("plot") or {}).get("ask_price")) or 0)))
    return props, list(q.get("claims") or []), None


def _start_expansion(bid, bld, tiles, pace, info):
    """PATCH the expansion onto `tiles`, verify it shows, then link the storehouse and set the delivery pace
    (a new construction has no provider and sits at pace 0, so nothing is delivered until both are set)."""
    body = {"construction": {"stage": "EXPANSION", "domain": list(tiles)}}
    ok, status, resp = _req("PATCH", "/buildings/%s" % bid, body)
    if not ok:
        return dict(ok=False, status=status, tiles=tiles, error=(resp or "")[:200].replace("\n", " "), **info)
    try:
        after = (_get_json("/buildings/%s" % bid).get("construction") or {})
    except Exception:
        after = {}
    held = after.get("stage") == "EXPANSION" and set(tiles) <= set(after.get("domain") or [])
    pace_now = None
    if held:
        prov = bld.get("provider_id") or STORE
        lok, _, lresp = _req("PATCH", "/buildings/%s/construction" % bid, {"provider_id": str(prov)})
        if not lok:
            info["provider_error"] = (lresp or "")[:160]
        pok, _, perr, pace_now = _set_pace(bid, pace)
        if not pok:
            info["pace_error"] = perr
    return dict(ok=held, status=status, tiles=tiles, stage=after.get("stage"), pace=pace_now,
                error=None if held else "expansion not visible after PATCH", **info)


def _apply_expand_rural(e, bld, specs):
    """Plots for a district building on map land (Oct 22, Taylor: farmstead +5 for the Tenants L12 level):
    {"expand": {"building": "151602398", "count": 5}}               DRY RUN: tiles, fertility, land quote, materials
    {"expand": {"building": "151602398", "count": 5}, "confirm": true}  buys the land the town quotes (POST
        /towns/{id}/expand {claims, properties}, the client's call), then parks the expansion until after the turn tick
        (bought land settles at the tick; a new site was refused on fresh land Oct 20)
    {"expand": {"building": "...", "tiles": ["1517:2395", ...]}, "confirm": true}  expands onto land we already hold
        (what the parked step runs): PATCH /buildings/{id} {construction: {stage: EXPANSION, domain: [...]}}, then the
        storehouse link and pace 100.
    Candidates: land in range with the type's fertility, touching the current domain first. The game still enforces
    tenants, management, range and suitability; its refusal is logged."""
    ex = e["expand"]
    bid = str(ex["building"])
    count = max(1, int(ex.get("count", 1)))
    spec_all = specs.get(bld.get("type")) or {}
    spec = spec_all.get("construction") or {}
    rng = float(spec.get("range") or 8)
    per = spec.get("materials") or {}
    stage = (bld.get("construction") or {}).get("stage")
    if stage not in (None, "", "NONE"):
        return dict(ok=False, error="building already under construction (stage %s)" % stage)
    size = float(bld.get("size") or 0)
    cap = float(spec.get("size") or 0)
    wanted = [str(t) for t in ex.get("tiles") or []]
    n = len(wanted) or count
    info = dict(building=bld.get("type"), location=bld.get("location"), size=size, size_cap=cap or None, range=rng,
                requires=spec_all.get("requires"), materials_per_plot=per, build_turns=spec.get("time"),
                materials_total={k: v * n for k, v in per.items()}, tenants_per_plot=spec_all.get("tenants"))
    if cap and size + n > cap:
        return dict(ok=False, error="size %g + %d plots is over the type's cap %g" % (size, n, cap), **info)
    if wanted:
        info["would_try"] = wanted
        if e.get("confirm") is not True:
            return dict(ok=True, dry_run=True, **info)
        return _start_expansion(bid, bld, wanted, ex.get("pace", 100), info)
    bx, by = _xy(bld["location"])
    r = int(rng) + 1
    try:
        plots = _map_plots(bx - r, by - r, bx + r, by + r)
    except Exception as exn:
        return dict(ok=False, error="map read failed: %s: %s" % (type(exn).__name__, exn), **info)
    try:
        town_dom = (_get_json("/towns/%s" % bld["town_id"]).get("domain")) or {}
    except Exception:
        town_dom = {}
    taken = set()
    try:      # our other district buildings' tiles (ids are their map tile, 9 digits; centre buildings are longer)
        for ob in (_get_json("/businesses/%s" % OWNER_ID).get("building_ids") or []):
            if len(str(ob)) > 9 or str(ob) == bid:
                continue
            o = _get_json("/buildings/%s" % ob)
            taken |= {_xy(t) for t in (o.get("domain") or [])} | {_xy(o["location"])}
    except Exception as exn:
        return dict(ok=False, error="our buildings unreadable: %s: %s" % (type(exn).__name__, exn), **info)
    cands = _rural_candidates(bld, spec_all, rng, plots, town_dom, taken)
    info["candidates"] = ["%s f%g %.1f%s" % (c["tile"], c["fertility"], c["dist"], " adj" if c["adjacent"] else "")
                          for c in cands[:12]]
    if not cands:
        return dict(ok=False, error="no suitable land in range", **info)
    # Oct 22: the town record no longer says who owns district land, and the tiles touching the farmstead are mostly
    # another player's (Oct 20 dump: 58616's logging camp and grain farm, one listed at 9,450). So a tile goes in the
    # plan only when the town quotes it as land to buy at a plain land price (district land sells at ~12): a refused
    # quote, an empty one (owned already, or not for sale) or any part priced over max_ask is skipped and listed.
    max_ask = float(ex.get("max_ask", 30))
    plan, quotes, refused = [], {}, []
    ours = []
    for c in cands[:max(40, 8 * count)]:
        props, claims, err = _land_quote(bld["town_id"], c["tile"])
        if err == "ours":
            ours.append(c["tile"])
            quotes[c["tile"]] = ([], [])
            plan.append(c["tile"])
            if len(plan) >= count:
                break
            continue
        if not err and not props and not claims:
            err = "nothing to buy (ours already, or not for sale)"
        if not err and claims and not ex.get("allow_claims"):
            err = "wilderness claim (%d tiles; set allow_claims to use)" % len(claims)
        if not err and any(a > max_ask for _, a in props):
            err = "priced %s (over max_ask %g)" % (", ".join("%s @%g" % pa for pa in props), max_ask)
        if err:
            refused.append("%s: %s" % (c["tile"], err))
            continue
        quotes[c["tile"]] = (props, claims)
        plan.append(c["tile"])
        if len(plan) >= count:
            break
    info["refused"] = refused[:12]
    if not plan:
        return dict(ok=False, error="the town quoted none of the candidate tiles", **info)
    props = {}
    claims = []
    for t in plan:
        for loc, ask in quotes[t][0]:
            props[loc] = ask
        for c in quotes[t][1]:
            if c not in claims:
                claims.append(c)
    info.update(would_try=plan, already_ours=ours, land_buy={k: v for k, v in props.items()},
                land_cost=round(sum(props.values()), 2), claims=len(claims),
                materials_total={k: v * len(plan) for k, v in per.items()})
    if len(plan) < count:
        info["short"] = "only %d of %d plots quoted" % (len(plan), count)
    if e.get("confirm") is not True:
        return dict(ok=True, dry_run=True, **info)
    if not props and not claims:
        return _start_expansion(bid, bld, plan, ex.get("pace", 100), info)       # all of it ours already
    body = {"claims": claims, "properties": [{"location": loc} for loc in props]}
    ok, status, resp = _req("POST", "/towns/%s/expand" % bld["town_id"], body)
    if not ok:
        return dict(ok=False, status=status, error="land purchase refused: %s" % (resp or "")[:200].replace("\n", " "), **info)
    after = _defer({"expand": {"building": bid, "tiles": plan, "pace": ex.get("pace", 100)}, "confirm": True,
                    "note": "parked by the rural expand: land bought, expansion after the tick"})
    return dict(ok=True, land_bought=True, status=status, expand_after=after, **info)


def _set_pace(bid, pace=100):
    """Construction delivery pace (the game's slider: 0 / 25 / 50 / 100). A new construction starts at 0, which delivers
    nothing, so the build never moves. 100 = the full materials over the build's own time (park plot: 12 turns), drawn
    from the provider storehouse. PUT /buildings/{id}/construction/settings {..settings, pace} (the client's call)."""
    try:
        cur = (_get_json("/buildings/%s" % bid).get("construction") or {}).get("settings") or {}
    except Exception:
        cur = {}
    ok, status, resp = _req("PUT", "/buildings/%s/construction/settings" % bid, dict(cur, pace=int(pace)))
    try:
        now = ((_get_json("/buildings/%s" % bid).get("construction") or {}).get("settings") or {}).get("pace")
    except Exception:
        now = None
    return bool(ok) and _same(now, pace), status, (resp or "")[:160], now


def _apply_v2(e):
    """Hand an item back to v1, or back to v2 (phone app): {"v2": {"suspend": "porterage"}} / {"v2": {"resume": "porterage"}}.
    Writes state/v2/suspended.json, the file every v1 writer and v2's actor read through v2_owned.py."""
    path = os.path.join(HERE, "state", "v2", "suspended.json")
    try:
        with open(path) as f:
            sus = json.load(f)
    except (FileNotFoundError, ValueError):
        sus = {}
    c = e["v2"]
    now = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    if c.get("suspend"):
        sus[str(c["suspend"])] = {"since": now, "why": e.get("note") or "by hand"}
    elif c.get("resume"):
        sus.pop(str(c["resume"]), None)
    else:
        return dict(ok=False, error="v2 entry needs suspend or resume")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(sus, f, indent=1)
    return dict(ok=True, suspended=sorted(sus))


def _apply_world(e):
    """{"world": ["Blanans", ...]} (or {"world": "all"}): the public world market (one call), saved compact to
    state/dump/world.json.gz: {town: {item: [best bid, bid depth 10%, best ask, ask depth 10%, traded per turn]}}."""
    import gzip
    want = e["world"]
    try:
        req = urllib.request.Request("https://api.mercatorio-tools.tech/data/marketdata", headers={"User-Agent": "merc-bot"})
        md = json.loads(urllib.request.urlopen(req, timeout=90).read())
    except Exception as exn:
        return dict(ok=False, error="world market unavailable: %s" % exn)
    out = {}
    for tw in md:
        if want != "all" and tw.get("name") not in want:
            continue
        out[tw.get("name")] = {k: [v.get("highest_bid"), v.get("bid_volume_10"), v.get("lowest_ask"), v.get("ask_volume_10"),
                                   v.get("volume_ema_12"), v.get("price_ema_12")]
                               for k, v in (tw.get("markets") or {}).items() if isinstance(v, dict)}
    path = os.path.join(HERE, "state", "dump", "world.json.gz")
    with gzip.open(path, "wt") as f:
        json.dump({"t": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"), "towns": out}, f)
    return dict(ok=True, towns=len(out), saved="state/dump/world.json.gz")


def _apply_route(e):
    """Start or stop a ship's trade route (the client's own calls):
      {"route": {"transport": "<id>", "start": true, "provider": "<storehouse>"}, "confirm": true}
          PUT /transports/{id}/route {provider_id, journey_id: ""} -> a route on the ship's CURRENT journey (start it with the
          ship docked at the far town after travelling there from home; the cargo must be empty)
      {"route": {"transport": "<id>", "stop": true}, "confirm": true}   DELETE /transports/{id}/route (route config is lost)
    No confirm = dry run (shows the ship's town, journey and cargo)."""
    r = e["route"]
    tid = str(r["transport"])
    try:
        t = _get_json("/transports/%s" % tid)
    except Exception as exn:
        return dict(ok=False, error="read failed: %s" % exn)
    j = t.get("journey") or {}
    cargo = {k: v.get("balance") for k, v in ((((t.get("cargo") or {}).get("inventory") or {}).get("account") or {}).get("assets") or {}).items()
             if k != "money" and _same(v.get("balance"), 0) is False}
    info = dict(town=t.get("town_id"), journey=[j.get("start_town_id"), j.get("end_town_id"), j.get("moves")],
                has_route=bool(t.get("route")), cargo=cargo)
    if e.get("confirm") is not True:
        return dict(ok=True, dry_run=True, **info)
    if r.get("stop"):
        ok, status, resp = _req("DELETE", "/transports/%s/route" % tid, {})
        after = bool(_get_json("/transports/%s" % tid).get("route"))
        return dict(ok=bool(ok) and not after, status=status, reply=(resp or "")[:200], **info)
    if r.get("start"):
        body = {"provider_id": str(r.get("provider") or STORE), "journey_id": str(r.get("journey_id") or "")}
        ok, status, resp = _req("PUT", "/transports/%s/route" % tid, body)
        rt = _get_json("/transports/%s" % tid).get("route") or {}
        return dict(ok=bool(ok) and bool(rt.get("id")), status=status, reply=(resp or "")[:200],
                    route={k: rt.get(k) for k in ("local_town", "remote_town", "capacity", "moves", "potential_trips")}, **info)
    return dict(ok=False, error="route entry needs start or stop")


def _apply_construction(e):
    """{"construction": {"building": "<id>", "set": {"provider_id": "<storehouse id>"}}}: PATCH /buildings/{id}/construction
    (the client's own call for a construction's settings, e.g. {stage: "NONE"} to abort). Oct 13: an expansion started by API
    has no provider, so nothing is delivered even at pace 100; linking the storehouse makes it draw materials from stock."""
    c = e["construction"]
    bid = str(c["building"])
    body = dict(c.get("set") or {})
    if not body:
        return dict(ok=False, error="construction entry needs set")
    ok, status, resp = _req("PATCH", "/buildings/%s/construction" % bid, body)
    try:
        now = _get_json("/buildings/%s" % bid).get("construction") or {}
    except Exception:
        now = {}
    held = all(str(now.get(k)) == str(v) for k, v in body.items())
    return dict(ok=bool(ok) and held, status=status, now={k: now.get(k) for k in body}, reply=(resp or "")[:200])


def _apply_pace(e):
    """{"pace": {"building": "<id>", "pace": 100}}: set a construction's delivery pace and verify."""
    ok, status, resp, now = _set_pace(str(e["pace"]["building"]), e["pace"].get("pace", 100))
    return dict(ok=ok, status=status, pace_now=now, reply=None if ok else resp)


_PENDING = []      # deferred steps added while this run is going (apply_queue keeps them when it rewrites the file)


def _defer(entry, after=None):
    """Park a step until after the next turn tick (default: the first :10 at least ~70 minutes away)."""
    if after is None:
        t = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=70)
        after = t.replace(minute=10, second=0, microsecond=0).isoformat().replace("+00:00", "Z")
    d = dict(after=after, entry=entry)
    _PENDING.append(d)
    cur = _load_deferred()
    cur.append(d)
    os.makedirs(os.path.dirname(DEFERRED), exist_ok=True)
    with open(DEFERRED, "w") as f:
        json.dump(cur, f, indent=1)
    return after


def _apply_plot(e):
    """One more plot on a building, start to finish, no map click: {"plot": {"building": "<id>"}, "confirm": true}.
    Uses land we already own if a free tile is in range (expands now); otherwise claims the nearest free tile now and
    parks the expansion until after the next turn tick (a claim settles at the tick). Does nothing while the building
    is already under construction or a plot step for it is already waiting. No confirm = dry run."""
    bid = str(e["plot"]["building"])
    try:
        specs = json.load(open(os.path.join(HERE, "v2", "data", "buildings.json")))
        bld = _get_json("/buildings/%s" % bid)
        town = _town(bld["town_id"])
    except Exception as exn:
        return dict(ok=False, error="read failed: %s: %s" % (type(exn).__name__, exn))
    stage = (bld.get("construction") or {}).get("stage")
    if stage not in (None, "", "NONE"):
        return dict(ok=True, skipped="already under construction (stage %s)" % stage)
    pend = [d for d in _load_deferred() if str(((d.get("entry") or {}).get("expand") or {}).get("building")) == bid]
    if pend:
        return dict(ok=True, skipped="a plot step is already waiting until %s" % pend[0].get("after"))
    rng = float(((specs.get(bld.get("type")) or {}).get("construction") or {}).get("range") or 8)
    cands = _expansion_candidates(bld, town, rng)
    if not cands:
        return dict(ok=False, error="no free tile in range")
    c = cands[0]
    step = {"expand": {"building": bid, "tiles": [c["tile"]]}, "confirm": True}
    if e.get("confirm") is not True:
        return dict(ok=True, dry_run=True, tile=c["tile"], ours=c["ours"], then="expand now" if c["ours"] else "claim now, expand after the tick")
    if c["ours"]:
        r = _apply_expand(step)
        r["tile"] = c["tile"]
        return r
    cok, cerr = _claim_tile(bld["town_id"], c["tile"])
    if not cok:
        return dict(ok=False, tile=c["tile"], error=cerr)
    try:
        town = _town(bld["town_id"])
    except Exception:
        town = {}
    if _tile_owner(town, c["tile"]) == OWNER_ID:          # bought outright: build now
        r = _apply_expand(step)
        r.update(tile=c["tile"], bought=True)
        return r
    after = _defer(step)
    return dict(ok=True, tile=c["tile"], claimed=True, owner_now=_tile_owner(town, c["tile"]), expand_after=after)


def _apply_site(e):
    """A new building start to finish, no map click (Oct 20, Taylor: build a net maker):
    {"site": {"type": "net maker"}, "confirm": true}; optional "tile": "1522.6:2388.1" and "near": "<building id>"
    (default the storehouse). Picks a free town-centre tile (ours first, then nearest), buys it if nobody owns it
    (a property, ~24), creates the site (POST /buildings via _apply_build), links the storehouse as the construction's
    provider and sets delivery pace 100 (a new construction sits at pace 0 with no provider and never moves). A bought
    tile that only settles at the tick defers the rest until after it. Skips if a site step for this type is already
    waiting. No confirm = DRY RUN (tile, owner, materials)."""
    s = e["site"]
    typ = str(s.get("type") or "")
    try:
        specs = json.load(open(os.path.join(HERE, "v2", "data", "buildings.json")))
        anchor = _get_json("/buildings/%s" % str(s.get("near") or STORE))
        town = _town(anchor["town_id"])
    except Exception as exn:
        return dict(ok=False, error="read failed: %s: %s" % (type(exn).__name__, exn))
    if typ not in specs:
        return dict(ok=False, error="unknown building type %r" % typ)
    now = datetime.datetime.now(datetime.timezone.utc)
    # only steps still waiting count: a due deferred site step is still in the file while it runs (it would skip itself)
    pend = [d for d in _load_deferred() if str(((d.get("entry") or {}).get("site") or {}).get("type")) == typ
            and _utc(d.get("after")) > now and not e.get("site", {}).get("tile")]
    if pend:
        return dict(ok=True, skipped="a %s site step is already waiting until %s" % (typ, pend[0].get("after")))
    materials = ((specs[typ].get("construction") or {}).get("materials"))
    tile = s.get("tile")
    if not tile:
        cands = _expansion_candidates(anchor, town, float(s.get("range") or 64))
        if not cands:
            return dict(ok=False, error="no free town-centre tile")
        tile = cands[0]["tile"]
    owner = _tile_owner(town, tile)
    if e.get("confirm") is not True:
        return dict(ok=True, dry_run=True, type=typ, tile=tile, owner=owner or None, ours=owner == OWNER_ID, materials=materials)
    if owner != OWNER_ID:
        if owner:
            return dict(ok=False, tile=tile, error="tile owned by %s" % owner)
        cok, cerr = _claim_tile(anchor["town_id"], tile)
        if not cok:
            return dict(ok=False, tile=tile, error=cerr)
        # Oct 20: right after the purchase the tile reads as ours, but POST /buildings refuses it ("must own the land
        # ... owned by 0") until the turn tick settles it (a plot expansion doesn't mind). Always build after the tick.
        after = _defer({"site": dict(s, tile=tile), "confirm": True})
        return dict(ok=True, tile=tile, claimed=True, build_after=after)
    cx, sx, cy, sy = _parse_loc(tile)
    # Oct 20: a game update moved building locations to the full tile string ("1522.1:2388.4", with the old map tile
    # under "location_legacy"). The old form, location "1522:2386" + sublocation, now reads as the whole centre map
    # tile, which the town owns ("must own the land ... owned by 0"). New form first, the old one as a fallback.
    tries = [{"location": tile, "sublocation": {"x": sx, "y": sy}}, {"location": tile},
             {"location": "%d:%d" % (cx, cy), "sublocation": {"x": sx, "y": sy}}]
    r, refused = {}, []
    for loc in tries:
        r = _apply_build({"build": dict({"type": typ, "town_id": str(anchor["town_id"])}, **loc), "confirm": True})
        if r.get("ok") or r.get("building_id"):
            break
        refused.append("%s: %s" % (json.dumps(loc), str(r.get("body") or r.get("error"))[:120]))
    if not r.get("ok"):
        r["tile"], r["refusals"] = tile, refused
        return r
    bid = r.get("building_id")
    link = _apply_construction({"construction": {"building": bid, "set": {"provider_id": STORE}}})
    pace = _apply_pace({"pace": {"building": bid, "pace": 100}})
    good = bool(link.get("ok")) and bool(pace.get("ok"))
    return dict(ok=good, tile=tile, building_id=bid, stage=r.get("stage"), linked=link.get("ok"), pace=pace.get("pace_now"),
                materials=materials, error=None if good else "site %s created; link %s, pace %s" % (
                    bid, link.get("reply") or link.get("now"), pace.get("reply") or pace.get("pace_now")))


def _apply_claim(e):
    """Buy town-centre tiles: {"claim": {"town_id": "152202387", "tiles": ["1522.3:2388.5"]}, "confirm": true}.
    No confirm = dry run (lists tiles, owner and asking price from the live town data). Logs the game's reply verbatim."""
    c = e["claim"]
    tid = str(c["town_id"])
    tiles = [str(t) for t in c.get("tiles") or []]
    try:
        town = _town(tid)
    except Exception as exn:
        return dict(ok=False, error="read failed: %s" % exn)
    dom = town.get("domain") or {}
    seen = []
    for t in tiles:
        cx, sx, cy, sy = _parse_loc(t)
        ent = dom.get(str((cx * 100000 + cy) * 1000000 + sx * 1000 + sy))
        seen.append("%s: %s" % (t, ent if ent is not None else "no entry"))
    if e.get("confirm") is not True:
        return dict(ok=True, dry_run=True, tiles=seen)
    body = {"claims": [], "properties": [{"location": t} for t in tiles]}      # centre tiles are bought (see _claim_tile)
    ok, status, resp = _req("POST", "/towns/%s/expand" % tid, body)
    try:
        dom = (_town(tid).get("domain")) or {}
        after = [(t, _tile_owner({"domain": dom}, t)) for t in tiles]
    except Exception:
        after = None
    return dict(ok=bool(ok) and bool(after) and all(o == OWNER_ID for _, o in after), status=status,
                reply=(resp or "")[:300], tiles=seen, owner_after=after)


def apply_entry(e):
    if "override" in e:
        return _apply_override(e)
    if "contract" in e:
        return _apply_contract_approval(e)
    if "message" in e:
        return _apply_message(e)
    if e.get("prestige"):
        return _apply_prestige(e)
    if e.get("donate"):
        return _apply_donate(e)
    if e.get("dump"):
        return _apply_dump(e)
    if "prestige_want" in e:
        return _apply_prestige_want(e)
    if "town_pick" in e:
        return _apply_town_pick(e)
    if e.get("seamap"):
        return _apply_seamap(e)
    if e.get("probe_write"):
        return _apply_probe_write(e)
    if e.get("build"):
        return _apply_build(e)
    if e.get("expand"):
        return _apply_expand(e)
    if e.get("plot"):
        return _apply_plot(e)
    if e.get("site"):
        return _apply_site(e)
    if e.get("pace"):
        return _apply_pace(e)
    if e.get("v2"):
        return _apply_v2(e)
    if e.get("world"):
        return _apply_world(e)
    if isinstance(e.get("route"), dict):
        return _apply_route(e)
    if isinstance(e.get("construction"), dict) and e["construction"].get("building"):
        return _apply_construction(e)
    if e.get("claim"):
        return _apply_claim(e)
    if e.get("travel"):
        return _apply_travel(e)
    if isinstance(e.get("assign"), dict):
        return _apply_assign(e)
    if e.get("household"):
        return _apply_household_slot(e)
    if e.get("producer"):
        return _apply_producer(e)
    if e.get("transport") and "operation_target" in e:
        return _apply_ship_operation(e)
    if not e.get("item"):
        return dict(ok=False, error="unknown queue entry (no item): %s" % json.dumps(e)[:120])
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


SPEND_GUARD = 0.05   # a queued buy costing more than 5% of cash per turn needs "confirm": true
NIGHT = (23, 7)      # Taylor asleep (Toronto time): no hand-queued spending increases at all


def night_now():
    """True between 23:00 and 07:00 Toronto time (Taylor asleep, Oct 11)."""
    from zoneinfo import ZoneInfo
    h = datetime.datetime.now(ZoneInfo("America/Toronto")).hour
    return h >= NIGHT[0] or h < NIGHT[1]


def _cash():
    pl = m.get("/player") or {}
    biz = m.get("/businesses/%s" % (pl.get("household") or {})["business_ids"][0]) or {}
    return m.num(((biz.get("account") or {}).get("assets") or {}).get("money", {}).get("balance"))


def _spend_guard(e, cash):
    """Failsafe (Oct 11): hand-queued buys (Claude check-ins) that would cost more than
    SPEND_GUARD of cash every turn are refused unless the entry says "confirm": true.
    Taylor's own app actions (note "app: ...") are never blocked."""
    s = e.get("set") or {}
    if str(e.get("note", "")).startswith("app:") or not e.get("item"):
        return None
    if e.get("confirm") and not night_now():
        return None
    if "buy_volume" not in s and "buy_price" not in s:
        return None
    if e.get("transport"):
        return None
    cur = _store_managers(str(e.get("building") or STORE), e["item"])
    tier = int(e.get("tier", 0))
    base = cur[tier] if tier < len(cur) else {}
    vol = m.num(s.get("buy_volume", base.get("buy_volume")))
    price = m.num(s.get("buy_price", base.get("buy_price")))
    cost = vol * price
    before = m.num(base.get("buy_volume")) * m.num(base.get("buy_price"))
    if night_now() and cost > before + 1:
        return "night guard: %s buy would rise %.0f -> %.0f/turn while Taylor is asleep (23:00-07:00 Toronto); leave it for the morning check-in" % (
            e["item"], before, cost)
    if cash and cost > before + 1 and cost > SPEND_GUARD * cash:
        return "spend guard: %s buy %.0f x %.2f = %.0f/turn is over %d%% of cash %.0f; add \"confirm\": true if intended" % (
            e["item"], vol, price, cost, SPEND_GUARD * 100, cash)
    return None


DEFERRED = os.path.join(HERE, "state", "deferred.json")


def _utc(ts):
    d = datetime.datetime.fromisoformat(str(ts).replace("Z", "+00:00"))
    return d if d.tzinfo else d.replace(tzinfo=datetime.timezone.utc)


def _load_deferred():
    try:
        with open(DEFERRED) as f:
            cur = json.load(f)
        return cur if isinstance(cur, list) else []
    except (FileNotFoundError, ValueError):
        return []


def apply_queue(live):
    """Apply state/order_queue.json, plus any deferred entries that are due.
    A deferred entry is queued as {"later": {"after": "2026-10-13T00:05:00Z", "entry": {...}}}: it is parked in
    state/deferred.json and runs (same guards, logged with source "deferred") on the first run at or after that time.
    The workflow runs hourly at :20 and on every queue push, so it fires within the hour. Use it for steps that need
    a turn tick in between (claim land now, expand once the claim has settled)."""
    try:
        with open(QUEUE) as f:
            q = json.load(f)
    except (FileNotFoundError, ValueError):
        q = []
    if not live:
        if q:
            print("order queue (dry run, not sent): %s" % json.dumps(q))
        return
    if not (m.USER and m.TOKEN):
        if q:
            print("order queue: no credentials, left in place")
        return
    now = datetime.datetime.now(datetime.timezone.utc)
    waiting, due = [], []
    for d in _load_deferred():
        try:
            (due if _utc(d["after"]) <= now else waiting).append(d)
        except Exception:
            log(d, dict(ok=False, error="bad deferred entry, dropped"), "deferred")
    entries = [("deferred", d["entry"]) for d in due] + [("queue", x) for x in q]
    if not entries and not _load_deferred():
        return
    cash = None
    for source, e in entries:
        if isinstance(e, dict) and "later" in e:
            lt = e["later"] or {}
            try:
                _utc(lt["after"])
                inner = lt["entry"]
                if not isinstance(inner, dict) or "later" in inner:
                    raise ValueError("entry must be a plain entry")
                waiting.append(dict(after=lt["after"], entry=inner))
                log(e, dict(ok=True, deferred_until=lt["after"]), source)
            except Exception as ex:
                log(e, dict(ok=False, error="bad later entry: %s" % ex), source)
            continue
        try:
            if cash is None:
                cash = _cash()
            refuse = _spend_guard(e, cash)
            r = dict(ok=False, error=refuse) if refuse else apply_entry(e)
        except (Exception, SystemExit) as ex:   # merc_status4.get() exits on HTTP errors; never let one entry stall the queue
            r = dict(ok=False, error="%s: %s" % (type(ex).__name__, ex))
        log(e, r, source)
        print("order queue: %s -> %s" % (e.get("item") or e.get("building"), "OK" if r.get("ok") else "FAILED %s" % r.get("error")))
    if q:
        with open(QUEUE, "w") as f:
            f.write("[]\n")
    waiting += [d for d in _PENDING if d not in waiting]
    if due or waiting or _load_deferred():
        os.makedirs(os.path.dirname(DEFERRED), exist_ok=True)
        with open(DEFERRED, "w") as f:
            json.dump(waiting, f, indent=1)


if __name__ == "__main__":
    import sys
    apply_queue("--live" in sys.argv)
