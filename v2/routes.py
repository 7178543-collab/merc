"""Bot v2 route finder: which town is worth a ship on a trade route, and with what cargo, at today's world prices.

Read-only. Inputs:
  world market    every town's market (public data, one call: api.mercatorio-tools.tech/data/marketdata)
  sea distances   state/v2/sea_routes.json: sea moves from our dock to every town's dock (tools/sea_distances.py)
  our store       what we hold, keep back, make and use (the v2 snapshot); ship running costs from v2/data/recipes.json

How a ship on a route really works (game client + Flax Wyrm's own numbers, Oct 13; the Oct 12 model was wrong):
  - movement per turn = type moves x crew level (snekkja: 3,000 moves at crew 1.0). A route round trip is 2 x the sea
    distance, so trips per turn = 3,000 x crew / (2 x moves). Flax Wyrm on Blanans (297 moves): 5.03 trips/turn, which is
    the route's own `potential_trips` 5.033 and `capacity` 1,258 = 250 x 5.03.
  - cargo space is counted in each product's `size` (garments 1, beer 2, bread 3, timber 15, limestone 40: the same units
    as storage), and services (labour, porterage, lodging, protection, meat, fish, milk, ...) can't be shipped.
  - running cost = the "snekkja 1" recipe x crew level: 50 labour + 1.6 cloth + 0.5 tar + 0.25 timber, ~128 coin per turn
    at crew 1.0 (Flax Wyrm ran 0.953 of it for 122.5 coin). Per unit carried that is ~0.10 coin on Blanans, the route's own
    `capacity_cost` 0.103. Shipping is cheap; what limits a route is how much each market will take per turn.
  - crew is sized to the cargo in steps of 0.1, as the client does. Range (snekkja 800): past it the extra distance counts
    double, and past twice the range there is no route (client tripCount). A game turn is a month: the client's
    "round trips per month" is per turn.
Per turn, per item (conservative):
  - out: sold there at 95% of their best bid, up to max(units within 10% of that bid, TAKE_SHARE of what they trade per
    turn); our own stock is valued at the home bid (what it would fetch here), else bought at 105% of the home ask
  - back: bought there at 105% of their ask (same depth rule); worth the home ask if we use it (up to our use per turn),
    else 95% of the home bid
  - net per turn = sum of margins - running cost at the crew level needed. Towns beyond the snekkja's RANGE are skipped.
Not modelled: tolls or market fees, prices moving as we sell into them, the one-off trip to set the route up.
"""
import json
import math
import os
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SEA = os.path.join(ROOT, "state", "v2", "sea_routes.json")
WORLD_URL = "https://api.mercatorio-tools.tech/data/marketdata"

SHIP = {"type": "snekkja", "capacity": 250, "moves": 3000, "range": 800, "recipe": "snekkja 1"}   # game transport table
MIN_CREW = 0.1          # the client sizes route crew in steps of 0.1 (ceil(cargo / journey capacity x 10) / 10)


def trips_per_turn(moves, ship=SHIP):
    """Round trips per turn at crew 1.0: the game client's tripCount (a turn is a game month). Past the type's range the
    distance counts double for the extra stretch; beyond twice the range a route is impossible."""
    n, rng = float(ship["moves"]), float(ship["range"])
    if moves > 2 * rng:
        return 0.0
    if moves <= 0:
        return n / 2
    if moves < 100:
        return n / 200
    return n / (2 * (moves + max(moves - rng, 0.0)))


def journey_capacity(moves, ship=SHIP):
    """Cargo units per turn at crew 1.0 (client: floor(tripCount(ceil(moves)) x capacity)); Blanans 297.2 -> 1,258."""
    return math.floor(trips_per_turn(math.ceil(moves), ship) * ship["capacity"])


def world_from_compact(w):
    """state/dump/world.json.gz ({town: {item: [bid, bid depth, ask, ask depth, traded]}}) -> marketdata-like list."""
    return [{"name": town, "markets": {k: {"highest_bid": v[0], "bid_volume_10": v[1], "lowest_ask": v[2],
                                             "ask_volume_10": v[3], "volume_ema_12": v[4]} for k, v in m.items()}}
            for town, m in ((w or {}).get("towns") or {}).items()]
TAKE_SHARE = 0.3
SLIP = 0.05
NOT_CARGO = {"labour", "porterage", "donations", "money", "none"}     # fallback if the product table is missing


def _products():
    """Game product table (v2/data/products.json, from the client): services can't be shipped, and cargo space is
    counted in `size` per unit (garments 1, beer 2, bread 3, timber 15, limestone 40), the same units as storage."""
    try:
        return {p["name"]: p for p in json.load(open(os.path.join(HERE, "data", "products.json")))}
    except (OSError, ValueError, KeyError, TypeError):
        return {}


def _f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return 0.0


def fetch_world(timeout=90):
    req = urllib.request.Request(WORLD_URL, headers={"User-Agent": "merc-bot"})
    return json.loads(urllib.request.urlopen(req, timeout=timeout).read())


def _mk(m):
    traded = _f(m.get("volume_ema_12"))
    return {"bid": _f(m.get("highest_bid")), "ask": _f(m.get("lowest_ask")),
            "sell_room": max(_f(m.get("bid_volume_10")), TAKE_SHARE * traded),     # what they'd buy from us per turn
            "buy_room": max(_f(m.get("ask_volume_10")), TAKE_SHARE * traded),      # what we could buy there per turn
            "traded": traded}


def running_cost(snap, recipes=None):
    """Coin per turn at crew 1.0, from the ship's recipe at home prices (our unit cost for what we make)."""
    try:
        recipes = recipes or json.load(open(os.path.join(HERE, "data", "recipes.json")))
        r = recipes[SHIP["recipe"]]
    except (OSError, ValueError, KeyError):
        return 128.0
    market = snap.get("market") or {}
    items = (snap.get("store") or {}).get("items") or {}
    c = 0.0
    for i in r.get("inputs") or []:
        # the dearer of the market price and our own unit cost (labour: market 1.63, but our bought labour ran ~2.16
        # in the Flax Wyrm's real flows), so the estimate errs high
        p = max((market.get(i["product"]) or {}).get("price") or 0, (items.get(i["product"]) or {}).get("unit_cost") or 0)
        c += i["amount"] * p
    return round(c, 1) or 128.0


def rank(snap, world, sea, home_name=None, top=10, cfg=None, recipes=None):
    """Routes ranked by estimated coin per turn. Returns {"routes": [...], "assumptions": {...}, ...}."""
    cfg = cfg or {}
    by_name = {t.get("name"): t for t in world or []}
    home_id = str(snap.get("home_town") or "")
    home_name = home_name or (sea.get(home_id) or {}).get("name")
    home = {k: _mk(v) for k, v in ((by_name.get(home_name) or {}).get("markets") or {}).items()}
    items = (snap.get("store") or {}).get("items") or {}
    keep, use, spare = {}, {}, {}
    for k, it in items.items():
        keep[k] = max([_f(o.get("min_holding")) for o in it.get("orders") or []] + [_f((cfg.get("stockpiles") or {}).get(k))])
        fl = it.get("flow") or {}
        use[k] = _f(fl.get("consumption"))
        surplus = max(0.0, _f(fl.get("production")) - use[k])
        spare[k] = surplus + max(0.0, _f(it.get("held")) - keep[k]) / 12.0      # per turn: new surplus + the pile over 12 turns
    cost1 = running_cost(snap, recipes)
    prods = _products()

    def size(item):
        return float((prods.get(item) or {}).get("size") or 1)

    def cargo(item):
        if prods:
            return (prods.get(item) or {}).get("type") == "commodity"
        return item not in NOT_CARGO
    routes, skipped, out_of_range = [], 0, 0
    for tid, d in sea.items():
        if tid == home_id or not d.get("moves"):
            continue
        if not trips_per_turn(d["moves"]):
            out_of_range += 1
            continue
        t = by_name.get(d["name"])
        if not t:
            skipped += 1
            continue
        trips_full = trips_per_turn(d["moves"])                     # round trips per turn at crew 1.0
        per_space = cost1 / max(1, journey_capacity(d["moves"]))    # coin per unit of cargo space, one way loaded
        there = {k: _mk(v) for k, v in (t.get("markets") or {}).items()}
        out_c, back_c = [], []
        for item, m in there.items():
            if not cargo(item):
                continue
            h = home.get(item) or {}
            if m["bid"] > 0 and m["sell_room"] >= 1:
                sell = m["bid"] * (1 - SLIP)
                if spare.get(item, 0) >= 1:
                    val = h.get("bid") or _f((items.get(item) or {}).get("unit_cost"))
                    n = min(spare[item], m["sell_room"])
                    out_c.append((item, n, val, sell))
                elif h.get("ask") and h.get("buy_room", 0) >= 1:
                    buy = h["ask"] * (1 + SLIP)
                    out_c.append((item, min(h["buy_room"], m["sell_room"]), buy, sell))
            if m["ask"] > 0 and m["buy_room"] >= 1:
                buy = m["ask"] * (1 + SLIP)
                if use.get(item, 0) > 0 and h.get("ask"):
                    back_c.append((item, min(m["buy_room"], use[item]), buy, h["ask"]))
                elif h.get("bid") and h.get("sell_room", 0) >= 1:
                    back_c.append((item, min(m["buy_room"], h["sell_room"]), buy, h["bid"] * (1 - SLIP)))

        def pick(cands):
            rows = []
            for item, n, buy, sell in cands:
                mg = sell - buy - per_space * size(item)
                if mg > 0 and n >= 1:
                    rows.append({"item": item, "units": int(n), "space": int(n) * size(item), "buy": round(buy, 2),
                                 "sell": round(sell, 2), "margin": round(mg * int(n))})
            rows.sort(key=lambda r: -r["margin"])
            return rows
        out_l, back_l = pick(out_c), pick(back_c)
        s_out, s_back = sum(r["space"] for r in out_l), sum(r["space"] for r in back_l)
        crew = max(MIN_CREW, math.ceil(10 * max(s_out, s_back) / max(1, journey_capacity(d["moves"]))) / 10.0) \
            if (out_l or back_l) else 0.0
        if crew > 1:            # more than one ship can carry: scale the cargo down to one ship's worth
            f = 1.0 / crew
            for r in out_l + back_l:
                r["units"] = int(r["units"] * f)
                r["space"] = r["space"] * f
                r["margin"] = round(r["margin"] * f)
            crew = 1.0
        u_out, u_back = sum(r["units"] for r in out_l), sum(r["units"] for r in back_l)
        gross_ = sum(r["margin"] for r in out_l + back_l)
        # margins already pay for the space they use (each leg charged as if the other ran empty, so shipping is
        # counted twice when both legs are loaded: conservative); the crew floor costs extra only past that
        floor_extra = max(0.0, crew * cost1 - (s_out + s_back) * per_space) if crew else 0.0
        net = gross_ - floor_extra
        routes.append({"town": d["name"], "town_id": tid, "moves": d["moves"], "trips_per_turn_full": round(trips_full, 2),
                       "cost_per_unit": round(per_space, 3), "crew": round(crew, 2), "crew_cost": round(crew * cost1),
                       "out": out_l, "back": back_l, "units_out": u_out, "units_back": u_back,
                       "per_turn": round(net, 1)})
    routes.sort(key=lambda r: -r["per_turn"])
    return {"routes": routes[:top], "considered": len(routes), "skipped": skipped, "out_of_range": out_of_range,
            "assumptions": {"ship": SHIP["type"], "capacity": SHIP["capacity"], "moves_per_turn_full_crew": SHIP["moves"],
                            "running_cost_full_crew": cost1, "min_crew": MIN_CREW, "take_share": TAKE_SHARE, "slippage": SLIP}}


def report_lines(rr, n=5):
    if not rr or not rr.get("routes") or "running_cost_full_crew" not in (rr.get("assumptions") or {}):
        return []
    a = rr["assumptions"]
    L = ["## Ship routes at today's world prices (estimate, per turn)", "",
         "%d towns in range by sea. A %s on a route: %d units a trip, %d moves a turn at full crew, running cost ~%.0f coin a "
         "turn at full crew (crew is sized to the cargo, floor %.2f). Markets: up to %d%% of what each town trades a turn, "
         "%d%% slippage each way." % (rr["considered"], a["ship"], a["capacity"], a["moves_per_turn_full_crew"],
                                      a["running_cost_full_crew"], a["min_crew"], a["take_share"] * 100, a["slippage"] * 100), "",
         "| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |",
         "| --- | --- | --- | --- | --- | --- | --- |"]
    for r in rr["routes"][:n]:
        o = ", ".join("%s %d (%g->%g)" % (x["item"], x["units"], x["buy"], x["sell"]) for x in r["out"][:4]) or "-"
        b = ", ".join("%s %d (%g->%g)" % (x["item"], x["units"], x["buy"], x["sell"]) for x in r["back"][:4]) or "-"
        L.append("| %s | %.0f | %.2f | %.2f (%d/turn) | %s | %s | %+.0f |" % (
            r["town"], r["moves"], r["cost_per_unit"], r["crew"], r["crew_cost"], o, b, r["per_turn"]))
    best = rr["routes"][0]
    L += ["", "**Best:** %s at about %+.0f coin a turn%s." % (
        best["town"], best["per_turn"], "" if best["per_turn"] > 0 else " (nothing pays at these prices)"), ""]
    return L


def load_sea(path=SEA):
    try:
        with open(path) as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}
