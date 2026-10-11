"""Bot v2 goal queue (shadow): standing goals in plain words that the planner turns into orders.

A goal says what Taylor wants, not which order edit to make. v2/goals.json holds them:

    {"id": "furniture", "kind": "keep", "item": "furniture", "units": 135}                  hold at least 135
    {"id": "spare-timber", "kind": "cap", "item": "timber", "units": 300}                   sell what is above 300
    {"id": "garments-blanans", "kind": "export", "item": "garments", "to": "Blanans"}       (not supported yet)

Optional on any goal: "until" (ISO date; expired goals are skipped), "note".
keep: "max_price" (never above the config buy ceiling), "per_turn" (default: close the gap over "within" turns, 12).
cap:  "min_price" (default: the config sell floor, else 2% over our cost), "per_turn" (same default).

Goals never lift a safety rule: buy ceilings, the cash reserve and the single-buy share still apply, and a goal that
can't be met says why instead of bending them. Lives apart from state/order_queue.json on purpose: that file is v1's
and is applied to the live game; this one is only ever read by the shadow planner.
"""
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(HERE, "goals.json")
KINDS = ("keep", "cap", "export")


def load(path=None):
    """(goals, note). A missing file is no goals; a broken one is no goals plus a note, never an exception."""
    try:
        with open(path or PATH) as f:
            g = json.load(f).get("goals") or []
        return (g if isinstance(g, list) else []), None
    except FileNotFoundError:
        return [], None
    except (OSError, ValueError, AttributeError) as e:
        return [], "goals.json unreadable (%s): no goals applied" % type(e).__name__


def _per_turn(g, amount):
    return max(1, int(g["per_turn"])) if g.get("per_turn") else max(1, math.ceil(amount / max(1, int(g.get("within", 12)))))


def plan_goals(goals, s, cfg, items, market, snap_price):
    """One result per goal: {id, kind, item, status, detail, order?}. status: met | ordering | blocked | conflict |
    expired | unsupported | invalid."""
    today = (s.get("t") or "")[:10]
    cash = s.get("cash") or 0
    budget = max(0.0, cash - (cfg.get("cash") or {}).get("reserve", 0))
    per_buy = (cfg.get("cash") or {}).get("max_single_buy_share", 0.2) * cash
    ceil_, floor_ = cfg.get("buy_ceiling") or {}, cfg.get("sell_floor") or {}
    out, valid = [], []
    for i, g in enumerate(goals):
        if not isinstance(g, dict):
            out.append({"id": "#%d" % i, "kind": None, "item": None, "status": "invalid", "detail": "not an object"})
            continue
        r = {"id": g.get("id") or "%s-%s" % (g.get("kind"), g.get("item")), "kind": g.get("kind"), "item": g.get("item")}
        out.append(r)
        if g.get("kind") not in KINDS:
            r.update(status="invalid", detail="unknown kind %r (use %s)" % (g.get("kind"), ", ".join(KINDS)))
        elif not g.get("item"):
            r.update(status="invalid", detail="no item")
        elif g.get("until") and str(g["until"])[:10] < today:
            r.update(status="expired", detail="until %s" % g["until"])
        elif g["kind"] == "export":
            r.update(status="unsupported", detail="export routes need ship planning (a later hand-over); not planned yet")
        elif not isinstance(g.get("units"), (int, float)) or g["units"] < 0:
            r.update(status="invalid", detail="units must be a number >= 0")
        else:
            valid.append((g, r))

    for g, r in valid:      # a keep above a cap on the same item can't both hold
        for g2, r2 in valid:
            if g["item"] == g2["item"] and g["kind"] == "keep" and g2["kind"] == "cap" and g["units"] > g2["units"]:
                for x in (r, r2):
                    x.update(status="conflict", detail="keep %d is above cap %d for %s" % (g["units"], g2["units"], g["item"]))

    for g, r in valid:
        if r.get("status"):
            continue
        item, units = g["item"], g["units"]
        it = items.get(item) or {}
        held = it.get("held", 0.0)
        m = market.get(item) or {}
        if g["kind"] == "keep":
            gap = units - held
            if gap <= 0:
                r.update(status="met", detail="holding %.0f of %d" % (held, units))
                continue
            cap = ceil_.get(item)
            limit = min(g["max_price"], cap) if g.get("max_price") and cap else (g.get("max_price") or cap)
            ask = m.get("ask")
            if not ask:
                r.update(status="blocked", detail="need %.0f more but no sellers at home" % gap)
            elif limit and ask > limit:
                r.update(status="blocked", detail="need %.0f more but the home ask %.2f is above the %.2f limit" % (gap, ask, limit))
            else:
                price = snap_price(min(ask * 1.02, limit) if limit else ask * 1.02, up=False)
                vol = min(_per_turn(g, gap), int(gap + 0.999), int(min(per_buy, budget) // price) if price else 0)
                if vol <= 0:
                    r.update(status="blocked", detail="cash guard: reserve or single-buy share leaves no room this turn")
                else:
                    budget -= vol * price
                    r.update(status="ordering", detail="holding %.0f of %d; buying %d/turn @ %s" % (held, units, vol, price),
                             order={"buy_volume": vol, "buy_price": str(price), "max_holding": int(units)})
        else:  # cap
            excess = held - units
            if excess <= 0:
                r.update(status="met", detail="holding %.0f, cap %d" % (held, units))
                continue
            uc = it.get("unit_cost") or 0
            floor = g.get("min_price") or max(floor_.get(item, 0), snap_price(uc * 1.02, up=True) if uc else 0)
            if m.get("bid") and floor and m["bid"] < floor:
                r.update(status="blocked", detail="%.0f over the cap but the home bid %.2f is below the %.2f floor" % (excess, m["bid"], floor))
            else:
                vol = min(_per_turn(g, excess), int(excess))
                r.update(status="ordering", detail="holding %.0f, cap %d; selling %d/turn" % (held, units, vol),
                         order={"sell_volume": vol, "sell_price": str(snap_price(floor, up=True)) if floor else None,
                                "min_holding": int(units)})
    return out


def merge(orders, results):
    """Fold goal orders into the plan's orders. A keep adds to what the planner already buys for use; a cap is its own sell."""
    for r in results:
        o = r.get("order")
        if not o:
            continue
        slot = orders.setdefault(r["item"], {})
        slot["goal"] = dict(o, goal=r["id"])
        if "buy_volume" in o:
            pb = slot.get("buy") or {}
            slot["effective_buy"] = {
                "buy_volume": int(pb.get("buy_volume", 0)) + o["buy_volume"],
                "buy_price": str(max(float(pb.get("buy_price") or 0), float(o["buy_price"]))),
                "max_holding": max(int(pb.get("max_holding") or 0), o["max_holding"])}
        else:
            slot.setdefault("sell", o)
