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
EMA_CAP = 1.03                 # ... and never over 103% of the town's 12-turn average price for it
MIN_NET_PER_TURN = 15          # a route must clear this after crew, or the ship stays at 0
# route fare per cargo size unit (storehouse operations export_fare / units x size): Blanans 0.04, Etallaen 0.10,
# Kirchwerp 0.19 (timber 13 x 15 = 195 size units paid 36.66, Oct 13). Not modelled per town yet: a middle value.
FARE_PER_SIZE = 0.15
# ---- trade mode (Oct 13, Taylor: "ship smaller amounts of more items, diversify"; config ship_trade.on): also carry
# goods we neither make nor use when the spread pays: buy at home and sell there, or buy there and sell at home. Only
# "clean" goods: no orders on them at home from anyone else and none held, so the home side (the buy that stocks an
# export, or the sell that clears an import) is v2's alone (act.trade_home; v1 skips them via v2_owned). Every good is
# capped by its market's room (30% of what trades there a turn), so the cargo spreads over many small lots by itself.
TRADE_MARGIN_SHARE = 0.06      # stricter than own goods: two legs in two markets
TRADE_SPEND_SHARE = 0.03       # home buys to ship out: at most this share of cash a turn, per ship


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
    trade = bool((cfg.get("ship_trade") or {}).get("on"))
    mine_t = set(cfg.get("_trade_owned") or [])       # goods trade mode already runs (shadow reads act_state)
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

    def tradeable(item, it, fl):
        if item in inter or item in never or _f(fl.get("production")) > 0 or _f(fl.get("consumption")) > 0:
            return False
        if item in mine_t:
            return True
        return not it.get("orders") and _f(it.get("held")) < 1

    # ---- church stock (Oct 14, Taylor: improve the setup): church asks for tapestries and windows are our cheapest
    # prestige (~24-29 coin a point vs ~55-60 for the banquet or a park plot) but nobody sells them at home, so the
    # offers sat as WAIT. With config ship_church.on, a ship buys them where they are sold, up to `keep`, so
    # contracts.py can fill the next ask on sight (Taylor's rule stands: sign only what stock fills now). Valued at
    # value_per_prestige a point so the voyage planner sails for them; capped by cash and a spend share a turn.
    sc = cfg.get("ship_church") or {}
    # ---- stock goods (Oct 18, Taylor: get on track): config ship_stock, same shape as ship_church but its own switch,
    # cash floor and budget. For prestige goods nobody sells at home: furniture (church furniture asks + the household
    # slot), candles (the 3-prestige luxury slot), pasties (basic food 1.3 vs bread 0.3). prestige_per_unit is what one
    # unit is worth in prestige (plus any coin it saves, converted at value_per_prestige).
    ss = cfg.get("ship_stock") or {}
    cash = _f(snap.get("cash"))
    wanted, budget = {}, {}
    if sc.get("on") and cash >= _f(sc.get("min_cash") or 20000):
        budget["church"] = _f(sc.get("spend_share") or 0.15) * cash
        for k, g in (sc.get("goods") or {}).items():
            wanted[k] = (g, "church", _f(sc.get("value_per_prestige") or 57))
    if ss.get("on") and cash >= _f(ss.get("min_cash") or 3000):
        budget["stock"] = _f(ss.get("spend_share") or 0.08) * cash
        for k, g in (ss.get("goods") or {}).items():
            wanted.setdefault(k, (g, "stock", _f(ss.get("value_per_prestige") or 45)))
    for item, m in there.items():
        wg = wanted.get(item)
        if wg and m["ask"] > 0 and m["buy_room"] >= 1:
            cg, grp, vpp = wg
            it = items.get(item) or {}
            want = _f(cg.get("keep")) - _f(it.get("held")) - float((taken or {}).get(item, 0))
            price = routes_snap(min(m["ask"] * 1.02, _f(cg.get("max_price"))), up=False)
            if want >= 1 and price >= m["ask"]:
                vol = int(min(want, m["buy_room"], budget[grp] // price if price else 0))
                gain = _f(cg.get("prestige_per_unit")) * vpp - price \
                    - per_space * size(item) - FARE_PER_SIZE * size(item)
                if vol >= 1 and gain > 0:
                    orders[item] = {"buy_volume": vol, "buy_price": str(price), "max_holding": int(_f(cg.get("keep"))),
                                    "_gain": gain}
                    est += vol * gain
                    space_in += vol * size(item)
                    budget[grp] -= vol * price
                    notes.append("%s: %s %d @ %s (keep %d)" % ("church stock" if grp == "church" else "stock", item, vol, price,
                                                                  int(_f(cg.get("keep")))))
            continue
        if not commodity(item):
            continue
        it = items.get(item) or {}
        h = home.get(item) or {}
        ship_cost = per_space * size(item)
        fare = FARE_PER_SIZE * size(item)        # the route's export/import fare, paid per unit on top of the crew
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
                floor = home_val + ship_cost + fare + max(MIN_MARGIN_ABS, MIN_MARGIN_SHARE * home_val)
                # the best bid can be a one-off spike (Oct 13: Etallaen 33.8, Clairlond 28.4 for garments while
                # garments trade at 22-24 almost everywhere, 12-turn price EMA ~22.3): by the time the route's ask is up
                # it is gone, and the ship sails for nothing. Price off the lower of the bid and 103% of the EMA.
                ref = min(m["bid"], m["ema"] * EMA_CAP) if m.get("ema") else m["bid"]
                price = routes_snap(ref * FILL_SHARE, up=True)
                if price <= m["bid"] and price >= floor:
                    vol = int(min(spare, m["sell_room"]))
                    if vol >= 1:
                        gain = price - home_val - ship_cost - fare
                        orders[item] = {"sell_volume": vol, "sell_price": str(price), "min_holding": int(math.ceil(keep)),
                                        "_gain": gain}
                        est += vol * gain
                        space_out += vol * size(item)
                        continue
        # ---- import: something we use and don't make, cheaper there than our home ask after shipping
        use = _f(fl.get("consumption"))
        # no seller at home (furniture, candles on Oct 18): what we'd otherwise pay is unknown, so value it at 110% of
        # the home 12-turn average price; without even that, skip it
        h_ask = h.get("ask") or (1.10 * h["ema"] if h.get("ema") else 0.0)
        if m["ask"] > 0 and use >= 1 and h_ask and not made and item not in inter:
            ceiling = h_ask - ship_cost - fare - max(MIN_MARGIN_ABS, MIN_MARGIN_SHARE * h_ask)
            price = routes_snap(min(m["ask"] * 1.02, ceiling), up=False)
            if price >= m["ask"]:
                vol = int(min(use, m["buy_room"]))
                if vol >= 1:
                    gain = h_ask - m["ask"] - ship_cost - fare
                    orders[item] = {"buy_volume": vol, "buy_price": str(price),
                                    "max_holding": int(math.ceil(max(_f(it.get("held")), use * 4))), "_gain": gain}
                    est += vol * gain
                    space_in += vol * size(item)
                    continue
        if not trade or not tradeable(item, it, fl):
            continue
        # ---- trade out: buy it at home, sell it there
        if m["bid"] > 0 and h.get("ask") and h.get("buy_room", 0) >= 1:
            hb = routes_snap(h["ask"] * 1.02, up=True)
            ref = min(m["bid"], m["ema"] * EMA_CAP) if m.get("ema") else m["bid"]
            price = routes_snap(ref * FILL_SHARE, up=True)
            gain = price - hb - ship_cost - fare
            vol = int(min(h["buy_room"], m["sell_room"]) - float((taken or {}).get(item, 0)))
            if price <= m["bid"] and gain >= max(MIN_MARGIN_ABS, TRADE_MARGIN_SHARE * hb) and vol >= 1:
                orders[item] = {"sell_volume": vol, "sell_price": str(price), "min_holding": 0, "_gain": gain,
                                "_cost": hb, "_home": {"buy_volume": vol, "buy_price": str(hb), "max_holding": 2 * vol}}
                est += vol * gain
                space_out += vol * size(item)
                continue
        # ---- trade back: buy it there, sell it at home just under their bid
        if m["ask"] > 0 and m["buy_room"] >= 1 and h.get("bid") and h.get("sell_room", 0) >= 1:
            price = routes_snap(m["ask"] * 1.02, up=True)
            href = min(h["bid"], h["ema"] * EMA_CAP) if h.get("ema") else h["bid"]     # a home bid spike won't last
            hs = routes_snap(href * FILL_SHARE, up=True)
            gain = hs - price - ship_cost - fare
            vol = int(min(m["buy_room"], h["sell_room"]))
            if hs <= h["bid"] and gain >= max(MIN_MARGIN_ABS, TRADE_MARGIN_SHARE * hs) and vol >= 1:
                orders[item] = {"buy_volume": vol, "buy_price": str(price), "max_holding": 2 * vol, "_gain": gain,
                                "_home": {"sell_volume": vol, "sell_price": str(hs), "min_holding": 0}}
                est += vol * gain
                space_in += vol * size(item)
    # a ship carries at most `cap` size units a turn each way at full crew: keep the orders that pay most per unit of
    # space (Oct 13: Kirchwerp "beer 63 + timber 26" needed 516 units of a 279 cap; it was scored +158, really ~+35)
    for side, key in (("out", "sell_volume"), ("in", "buy_volume")):
        used = space_out if side == "out" else space_in
        if used <= cap:
            continue
        mine = [(k, o) for k, o in orders.items() if key in o]
        mine.sort(key=lambda ko: -ko[1]["_gain"] / size(ko[0]))
        room = float(cap)
        for k, o in mine:
            fit = int(min(o[key], room // size(k)))
            if fit < 1:
                est -= o[key] * o["_gain"]
                del orders[k]
                continue
            est -= (o[key] - fit) * o["_gain"]
            o[key] = fit
            room -= fit * size(k)
        used = cap - room
        if side == "out":
            space_out = used
        else:
            space_in = used
    # trade mode: cap the home buys that stock exports (worst coin-for-coin first), then the home side follows the
    # route volumes left after fitting
    outs = sorted([(k, o) for k, o in orders.items() if "_home" in o and "sell_volume" in o],
                  key=lambda ko: ko[1]["_gain"] / max(0.01, ko[1]["_cost"]))
    spend = sum(o["sell_volume"] * o["_cost"] for _, o in outs)
    for k, o in outs:
        if spend <= TRADE_SPEND_SHARE * _f(snap.get("cash")):
            break
        spend -= o["sell_volume"] * o["_cost"]
        est -= o["sell_volume"] * o["_gain"]
        space_out -= o["sell_volume"] * size(k)
        del orders[k]
    home_orders = {}
    for k, o in orders.items():
        hside = o.pop("_home", None)
        o.pop("_cost", None)
        if hside:
            if "sell_volume" in o:
                hside.update(buy_volume=o["sell_volume"], max_holding=2 * o["sell_volume"])
            else:
                hside["sell_volume"] = o["buy_volume"]
                o["max_holding"] = 2 * o["buy_volume"]
            home_orders[k] = hside
    for o in orders.values():
        o.pop("_gain", None)
    need = max(space_out, space_in)
    crew = max(routes.MIN_CREW, math.ceil(10.0 * need / cap) / 10.0) if orders else 0.0
    # No "one round trip a turn" minimum: the route's actual_trips is just reserved cargo / 250 (Linen Snake 0.632 =
    # 158 reserved, 0.144 = 36), not a port schedule. Sales tracked the price against their bids, not crew: crew 0.1
    # sold 30 then 0, crew 0.6 sold 6 then 0 (Oct 13, turns 13243-13246). The minimum cost ~50 coin a turn for nothing.
    crew = min(crew, 1.0)
    net = est - crew * cost1 + (space_out + space_in) * per_space   # est already paid per-unit shipping; charge crew once
    if orders and net < MIN_NET_PER_TURN:
        notes.append("best orders clear only %.0f a turn after crew: ship stays at 0" % net)
        orders, crew, home_orders = {}, 0.0, {}
    return {"ship": ship.get("name"), "id": ship.get("id"), "town": d.get("name"), "town_id": town_id,
            "orders": orders, "home_orders": home_orders, "crew": crew, "est_net": round(net if orders else 0.0, 1), "capacity": cap,
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
