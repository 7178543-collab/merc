"""Bot v2 ship manager: what each ship's trade route should buy and sell, and at what crew, from live world prices.

Pure planning (no game calls). v2/act.py turns the plan into writes for ships listed in config live.ships with
mode "auto" in live.ship_modes; everything else stays a report line.

How a route trades (game client + live tests, Oct 13):
  - a route's sell order posts an ask in the FAR town's market from the storehouse's stock (above its min_holding); it
    only fills against a bid there at or above our price. A buy order buys there and brings the goods home.
  - route capacity per turn = journey_capacity(moves) x crew (cargo `size` units); the order volumes reserve that space
    (Flax Wyrm's limestone import, 30 x size 40 = 1,200, took the whole route for nothing).
  - running cost = recipe "snekkja 1" x crew, ~100-128 coin a turn at crew 1.0.

Rules (conservative):
  - exports: only goods we hold above what we keep back, never chain intermediates or never_drop inputs. Priced just
    under their best bid (98%) so it fills, never under home value + shipping + MIN_MARGIN. Volume: what their bids take
    (max of 10% depth and 30% of per-turn trade), at most our spare per turn.
  - imports: only goods we use, when their ask + shipping + margin is under our home ask. Volume: our use per turn.
  - crew: ceil(cargo space / journey capacity, 0.1 steps), floor 0.1; no profitable order -> crew 0.
"""
import math

import routes

MIN_MARGIN_SHARE = 0.04        # at least 4% of the home value per unit, after shipping
MIN_MARGIN_ABS = 0.25
FILL_SHARE = 0.98              # our ask sits at 98% of their best bid
MIN_NET_PER_TURN = 15          # a route must clear this after crew, or the ship stays at 0


def _f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return 0.0


def _keep(it, cfg, item):
    return max([_f(o.get("min_holding")) for o in it.get("orders") or []] + [_f((cfg.get("stockpiles") or {}).get(item))])


def plan_ship(ship, snap, world, sea, cfg, recipes=None, products=None, taken=None):
    """Orders + crew for one ship's current route town. Returns a dict (see keys below) or None if it has no route.
    taken: {item: units a turn} already given to other ships' routes this run (they share one storehouse)."""
    town_id = str(ship.get("route_to") or "")
    if not town_id:
        return None
    d = sea.get(town_id) or {}
    by_name = {t.get("name"): t for t in world or []}
    home_name = (sea.get(str(snap.get("home_town"))) or {}).get("name")
    there = {k: routes._mk(v) for k, v in ((by_name.get(d.get("name")) or {}).get("markets") or {}).items()}
    home = {k: routes._mk(v) for k, v in ((by_name.get(home_name) or {}).get("markets") or {}).items()}
    prods = products if products is not None else routes._products()
    items = (snap.get("store") or {}).get("items") or {}
    inter = set((cfg.get("chain") or {}).get("intermediates") or [])
    never = set(cfg.get("never_drop") or [])
    cap = routes.journey_capacity(d.get("moves") or 0)
    cost1 = routes.running_cost(snap, recipes)
    if not cap or not there:
        return {"ship": ship.get("name"), "id": ship.get("id"), "town": d.get("name"), "orders": {}, "crew": 0.0,
                "est_net": 0.0, "why": "no capacity or no market data for %s" % d.get("name")}
    per_space = cost1 / cap
    orders, est, space_out, space_in, notes = {}, 0.0, 0.0, 0.0, []

    def size(item):
        return float((prods.get(item) or {}).get("size") or 1)

    def commodity(item):
        return (prods.get(item) or {}).get("type") == "commodity" if prods else item not in routes.NOT_CARGO

    for item, m in there.items():
        if not commodity(item):
            continue
        it = items.get(item) or {}
        h = home.get(item) or {}
        ship_cost = per_space * size(item)
        fl = it.get("flow") or {}
        made = _f(fl.get("production")) > 0
        # ---- export: goods we make, above what we keep back
        if m["bid"] > 0 and made and item not in inter and item not in never:
            keep = _keep(it, cfg, item)
            spare = max(0.0, _f(fl.get("production")) - _f(fl.get("consumption"))) + max(0.0, _f(it.get("held")) - keep) / 12.0
            spare = min(spare, max(0.0, _f(it.get("held")) - keep)) - float((taken or {}).get(item, 0))
            if spare >= 1:
                # what a unit fetches at home: the best of the home bid and what our home sales actually got last turn
                realized = (_f(fl.get("sale_value")) / _f(fl.get("sale"))) if _f(fl.get("sale")) else 0.0
                home_val = max(h.get("bid") or 0.0, realized, _f(it.get("unit_cost")))
                floor = home_val + ship_cost + max(MIN_MARGIN_ABS, MIN_MARGIN_SHARE * home_val)
                price = routes_snap(m["bid"] * FILL_SHARE, up=True)
                if price <= m["bid"] and price >= floor:
                    vol = int(min(spare, m["sell_room"]))
                    if vol >= 1:
                        orders[item] = {"sell_volume": vol, "sell_price": str(price), "min_holding": int(math.ceil(keep))}
                        est += vol * (price - home_val - ship_cost)
                        space_out += vol * size(item)
                        continue
        # ---- import: something we use and don't make, cheaper there than our home ask after shipping
        use = _f(fl.get("consumption"))
        if m["ask"] > 0 and use >= 1 and h.get("ask") and not made and item not in inter:
            ceiling = h["ask"] - ship_cost - max(MIN_MARGIN_ABS, MIN_MARGIN_SHARE * h["ask"])
            price = routes_snap(min(m["ask"] * 1.02, ceiling), up=False)
            if price >= m["ask"]:
                vol = int(min(use, m["buy_room"]))
                if vol >= 1:
                    orders[item] = {"buy_volume": vol, "buy_price": str(price),
                                    "max_holding": int(math.ceil(max(_f(it.get("held")), use * 4)))}
                    est += vol * (h["ask"] - m["ask"] - ship_cost)
                    space_in += vol * size(item)
    need = max(space_out, space_in)
    crew = max(routes.MIN_CREW, math.ceil(10.0 * need / cap) / 10.0) if orders else 0.0
    crew = min(crew, 1.0)
    net = est - crew * cost1 + (space_out + space_in) * per_space   # est already paid per-unit shipping; charge crew once
    if orders and net < MIN_NET_PER_TURN:
        notes.append("best orders clear only %.0f a turn after crew: ship stays at 0" % net)
        orders, crew = {}, 0.0
    return {"ship": ship.get("name"), "id": ship.get("id"), "town": d.get("name"), "town_id": town_id,
            "orders": orders, "crew": crew, "est_net": round(net if orders else 0.0, 1), "capacity": cap,
            "space": [round(space_out), round(space_in)], "notes": notes}


def routes_snap(p, up):
    """The game's price grid (same rule as the planner): <= 2 decimals, 3 significant digits; 2-4 leading -> even last
    digit, 5-9 leading -> last digit 0 or 5."""
    if not p or p <= 0:
        return 0.0
    e = math.floor(math.log10(p) + 1e-12) - 2
    lead = int(p / 10 ** (e + 2) + 1e-9)
    step = 10 ** e * (5 if lead >= 5 else 2 if lead >= 2 else 1)
    step = max(step, 0.01)
    n = p / step
    n = math.ceil(n - 1e-9) if up else math.floor(n + 1e-9)
    return round(n * step, 6)


def route_diff(ship, plan):
    """Writes needed to move the live route orders to the plan: {item: new managers list}; items to clear get []."""
    live = ship.get("route_orders") or {}
    out = {}
    for item, o in (plan.get("orders") or {}).items():
        cur = [{k: v for k, v in t.items() if k != "result"} for t in live.get(item) or []]
        want = [dict(o)]
        if _canon(cur) != _canon(want):
            out[item] = want
    for item, cur in live.items():
        if item not in (plan.get("orders") or {}) and any(_f(t.get("sell_volume")) or _f(t.get("buy_volume")) for t in cur or []):
            out[item] = []
    return out


def _canon(tiers):
    def v(x):
        try:
            return round(float(x), 4)
        except (TypeError, ValueError):
            return str(x)
    return sorted([sorted((k, v(x)) for k, x in t.items()) for t in tiers])


def best_towns(snap, world, sea, cfg, top=5, recipes=None, products=None):
    """Where a ship should go: every reachable town scored with plan_ship itself (the orders the bot would really place
    there), so a voyage is never chosen on trades the ship plan would not make. Positive, above MIN_NET_PER_TURN."""
    home = str(snap.get("home_town") or "")
    prods = products if products is not None else routes._products()
    out = []
    for tid, d in sea.items():
        if tid == home or not d.get("moves") or not routes.trips_per_turn(d["moves"]):
            continue
        pl = plan_ship({"name": "?", "id": "?", "route_to": tid}, snap, world, sea, cfg, recipes, prods)
        if pl and pl["orders"] and pl["est_net"] > MIN_NET_PER_TURN:
            out.append({"town": d["name"], "town_id": tid, "per_turn": pl["est_net"], "crew": pl["crew"],
                        "moves": d["moves"], "orders": pl["orders"]})
    out.sort(key=lambda r: -r["per_turn"])
    return out[:top]
