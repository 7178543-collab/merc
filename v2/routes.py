"""Bot v2 route finder: which town is worth a ship, and with what cargo, at today's world prices.

Read-only. Inputs:
  world market    every town's market (public data, one call: api.mercatorio-tools.tech/data/marketdata)
  sea distances   state/v2/sea_routes.json: sea moves from our dock to every town's dock (tools/sea_distances.py,
                  one Dijkstra over state/seamap; regenerate when the map changes)
  our store       what we hold, keep back, make and use (the v2 snapshot)

Model (deliberately conservative; every number is shown in the report so it can be checked):
  - one ship, cargo CARGO units per leg; out = goods from home sold at their bid, back = goods bought there
    and either sold at home or used by us (saves the home ask, up to our use over the trip)
  - only what the market can take right now: bid_volume_10 / ask_volume_10 (units within 10% of the best price),
    sold at 95% of the bid and bought at 105% of the ask (slippage); our own stock only above what we keep back
  - travel: SPEED moves per turn at crew 0.5 (measured: Linen Snake 150 tiles in one turn, Oct 12), +1 turn at each end
  - crew cost: CREW_COST coin per turn at crew 0.5 (Flax Wyrm at crew 0.23 cost 122.5/turn, scaled linearly)
  - profit per turn = (out margin + back margin - crew cost x trip turns) / trip turns
Not modelled (yet): tolls or market fees, prices moving while the ship sails, the route system's own trips.
"""
import json
import math
import os
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SEA = os.path.join(ROOT, "state", "v2", "sea_routes.json")
WORLD_URL = "https://api.mercatorio-tools.tech/data/marketdata"

CARGO = 250
SPEED = 150.0
CREW_COST = 266.0
SLIP = 0.05
NOT_CARGO = {"labour", "porterage", "donations", "money", "none"}


def _f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return 0.0


def fetch_world(timeout=90):
    req = urllib.request.Request(WORLD_URL, headers={"User-Agent": "merc-bot"})
    return json.loads(urllib.request.urlopen(req, timeout=timeout).read())


def _mk(m):
    return {"bid": _f(m.get("highest_bid")), "ask": _f(m.get("lowest_ask")),
            "bid_vol": _f(m.get("bid_volume_10")), "ask_vol": _f(m.get("ask_volume_10")),
            "traded": _f(m.get("volume_ema_12"))}


def _fill(cands, cap=CARGO):
    """Greedy by margin per unit until the hold is full. cands: (margin_per_unit, units, item, buy, sell)."""
    out, room, total = [], cap, 0.0
    for mg, units, item, buy, sell in sorted(cands, key=lambda c: -c[0]):
        if mg <= 0 or room <= 0:
            continue
        n = int(min(units, room))
        if n <= 0:
            continue
        out.append({"item": item, "units": n, "buy": round(buy, 2), "sell": round(sell, 2), "margin": round(mg * n)})
        room -= n
        total += mg * n
    return out, total


def rank(snap, world, sea, home_name=None, top=10, cfg=None):
    """Routes ranked by estimated coin per turn. Returns {"routes": [...], "assumptions": {...}, "skipped": n}."""
    cfg = cfg or {}
    rc = cfg.get("routes") or {}
    cargo, speed, crew_cost = rc.get("cargo", CARGO), rc.get("speed", SPEED), rc.get("crew_cost", CREW_COST)
    by_name = {t.get("name"): t for t in world or []}
    home_id = str(snap.get("home_town") or "")
    home_name = home_name or (sea.get(home_id) or {}).get("name")
    home = {k: _mk(v) for k, v in ((by_name.get(home_name) or {}).get("markets") or {}).items()}
    items = (snap.get("store") or {}).get("items") or {}
    keep = {}
    for k, it in items.items():
        keep[k] = max([_f(o.get("min_holding")) for o in it.get("orders") or []] + [_f((cfg.get("stockpiles") or {}).get(k))])
    use = {k: _f((it.get("flow") or {}).get("consumption")) for k, it in items.items()}
    routes, skipped = [], 0
    for tid, d in sea.items():
        if tid == home_id or d.get("moves") is None:
            continue
        t = by_name.get(d["name"])
        if not t:
            skipped += 1
            continue
        there = {k: _mk(v) for k, v in (t.get("markets") or {}).items()}
        one_way = math.ceil(d["moves"] / speed)
        trip = 2 * one_way + 2
        out_c, back_c = [], []
        for item, m in there.items():
            if item in NOT_CARGO:
                continue
            h = home.get(item) or {}
            # out: our own stock above what we keep back, valued at what it would fetch at home; else bought at home
            if m["bid"] > 0 and m["bid_vol"] > 0:
                sell = m["bid"] * (1 - SLIP)
                spare = max(0.0, _f((items.get(item) or {}).get("held")) - keep.get(item, 0))
                if spare >= 1:
                    val = h.get("bid") or _f((items.get(item) or {}).get("unit_cost"))
                    out_c.append((sell - val, min(spare, m["bid_vol"]), item, val, sell))
                elif h.get("ask") and h.get("ask_vol"):
                    buy = h["ask"] * (1 + SLIP)
                    out_c.append((sell - buy, min(h["ask_vol"], m["bid_vol"]), item, buy, sell))
            # back: bought there; sold at home, or used by us (saves the home ask, up to our use over the trip)
            if m["ask"] > 0 and m["ask_vol"] > 0:
                buy = m["ask"] * (1 + SLIP)
                if use.get(item, 0) > 0 and h.get("ask"):
                    back_c.append((h["ask"] - buy, min(m["ask_vol"], use[item] * trip), item, buy, h["ask"]))
                elif h.get("bid") and h.get("bid_vol"):
                    back_c.append((h["bid"] * (1 - SLIP) - buy, min(m["ask_vol"], h["bid_vol"]), item, buy, h["bid"] * (1 - SLIP)))
        out_l, out_v = _fill(out_c, cargo)
        back_l, back_v = _fill(back_c, cargo)
        cost = crew_cost * trip
        net = out_v + back_v - cost
        routes.append({"town": d["name"], "town_id": tid, "moves": d["moves"], "trip_turns": trip,
                       "out": out_l, "back": back_l, "gross": round(out_v + back_v), "crew_cost": round(cost),
                       "net_per_trip": round(net), "per_turn": round(net / trip, 1)})
    routes.sort(key=lambda r: -r["per_turn"])
    return {"routes": routes[:top], "considered": len(routes), "skipped": skipped,
            "assumptions": {"cargo": cargo, "speed_moves_per_turn": speed, "crew_cost_per_turn": crew_cost, "slippage": SLIP}}


def report_lines(rr, n=5):
    if not rr or not rr.get("routes"):
        return []
    a = rr["assumptions"]
    L = ["## Ship routes at today's world prices (estimate)", "",
         "%d towns by sea; one ship, %d units each way, %g moves/turn at crew 0.5, crew ~%g coin/turn, %d%% slippage. "
         "Only what each market can take right now is counted." % (rr["considered"], a["cargo"], a["speed_moves_per_turn"],
                                                                     a["crew_cost_per_turn"], a["slippage"] * 100), "",
         "| Town | Trip turns | Out (sell there) | Back (buy there) | Gross | Crew | Net/turn |", "| --- | --- | --- | --- | --- | --- | --- |"]
    for r in rr["routes"][:n]:
        o = ", ".join("%s %d (%g->%g)" % (x["item"], x["units"], x["buy"], x["sell"]) for x in r["out"][:4]) or "-"
        b = ", ".join("%s %d (%g->%g)" % (x["item"], x["units"], x["buy"], x["sell"]) for x in r["back"][:4]) or "-"
        L.append("| %s | %d | %s | %s | %d | %d | %+.0f |" % (r["town"], r["trip_turns"], o, b, r["gross"], r["crew_cost"], r["per_turn"]))
    best = rr["routes"][0]["per_turn"]
    L.append("")
    L.append("**Verdict:** " + ("no route pays at these prices; keep the ships parked (crew costs more than the trade margin)."
                                if best <= 0 else "best is %s at about %+.0f coin/turn; worth a trip if prices hold." % (
                                    rr["routes"][0]["town"], best)))
    L.append("")
    return L


def load_sea(path=SEA):
    try:
        with open(path) as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}
