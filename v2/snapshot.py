"""Bot v2 snapshot: everything the planner needs, read once per turn into one dict.

Shape (all numbers are floats):
  turn, t, cash, household {prestige, free, rate, levels, caps, workers}, home_town,
  store {id, capacity, used, items: {item: {held, capacity, orders[], flow{...}, unit_cost}}},
  buildings [{id, type, name, recipe, target, production, limitation, flows{}, construction}],
  household_duty {recipe, target}, sustenance {item: use}, ships [...], market {item: {...}},
  history {item: [consumption per run, oldest first]}  (from v1's history files, for burst items)
"""
import datetime
import glob
import json
import os

import api

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def n(x, d=0.0):
    try:
        return float(x)
    except (TypeError, ValueError):
        return d


def _orders(holding):
    return [{k: v for k, v in mg.items() if k != "result"} for mg in ((holding or {}).get("managers") or []) if mg]


def _history_use(turns=24):
    """Per-item consumption over the last `turns` bot runs, from v1's history (one line per run)."""
    rows = []
    for path in sorted(glob.glob(os.path.join(HERE, "history", "merc-*.jsonl")))[-2:]:
        try:
            with open(path) as f:
                rows += [json.loads(l) for l in f if l.strip()]
        except (OSError, ValueError):
            pass
    by_turn = {}
    for r in rows:
        if r.get("turn") is not None:
            by_turn[r["turn"]] = r
    use = {}
    for t in sorted(by_turn)[-turns:]:
        for item, v in (by_turn[t].get("items") or {}).items():
            if isinstance(v, list) and len(v) > 2:
                use.setdefault(item, []).append(n(v[2]))
    return use


def take():
    s = {"t": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"), "errors": []}
    s["turn"] = int(n((api.get("/clock") or {}).get("turn"))) or None
    pl = api.get("/player") or {}
    hh_ref = pl.get("household") or {}
    hid = hh_ref.get("id")
    biz_id = (hh_ref.get("business_ids") or [None])[0]
    biz = api.get("/businesses/%s" % biz_id) if biz_id else None
    hh = api.get("/households/%s" % hid) if hid else None
    if not biz or not hh:
        s["errors"].append("could not read player/business/household")
        return s
    s["business_id"], s["household_id"] = str(biz_id), str(hid)
    s["cash"] = n(((biz.get("account") or {}).get("assets") or {}).get("money", {}).get("balance"))
    s["home_town"] = str(hh.get("town_id"))

    pb = hh.get("prestige_board") or {}
    s["household"] = {
        "prestige": n(hh.get("prestige")), "free": n(hh.get("prestige")) - n(pb.get("allocated")),
        "rate": sum(n(x.get("impact")) for x in (hh.get("prestige_impacts") or [])),
        "impacts": {str(x.get("factor")): n(x.get("impact")) for x in (hh.get("prestige_impacts") or [])},
        "legacy": n(hh.get("legacy")),
        "levels": {k[:-6]: int(n(v)) for k, v in pb.items() if k.endswith("_level")},
        "caps": {k: n(v) for k, v in (hh.get("caps") or {}).items()},
        "workers": [{"name": w.get("name"), "assignment": w.get("assignment"),
                     "skills": {k: n(v) for k, v in (w.get("skills") or {}).items()}} for w in hh.get("workers") or []],
    }
    p = hh.get("producer") or {}
    s["household_duty"] = {"recipe": p.get("recipe"), "target": n(p.get("target"))}
    sus = ((hh.get("sustenance") or {}).get("inventory") or {}).get("previous_flows") or {}
    s["sustenance"] = {k: n(v.get("consumption")) for k, v in sus.items()}
    # the goods set in the household's slots, consumed or not (an empty slot eats nothing, so "sustenance" drops it)
    s["sustenance_slots"] = sorted((((hh.get("sustenance") or {}).get("inventory") or {}).get("holdings") or {}).keys())

    s["buildings"], store_id = [], None
    for bb in biz.get("buildings") or []:
        b = api.get("/buildings/%s" % bb["id"]) or {}
        if bb.get("type") in ("warehouse", "storehouse"):
            store_id = str(bb["id"])
            s["_store_raw"] = b
            continue
        pr = b.get("producer") or {}
        po = pr.get("previous_operation") or {}
        cons = b.get("construction") or {}
        s["buildings"].append({
            "id": str(bb["id"]), "type": bb.get("type"), "name": b.get("name") or bb.get("type"),
            "size": n(b.get("size")), "recipe": pr.get("recipe"), "target": n(pr.get("target")),
            "production": n(po.get("production")), "limitation": po.get("limitation"),
            "flows": {k: {kk: n(vv) for kk, vv in (v or {}).items()}
                      for k, v in (((pr.get("inventory") or {}).get("previous_flows")) or {}).items()},
            "construction": ({"progress": n(cons.get("progress")), "stage": cons.get("stage")} if cons else None),
            "remote": n((b.get("delivery_cost") or {}).get("land_distance")) > 0,
        })

    st = (s.pop("_store_raw", None) or {}).get("storage") or {}
    inv = st.get("inventory") or {}
    assets = (inv.get("account") or {}).get("assets") or {}
    holds, flows = inv.get("holdings") or {}, inv.get("previous_flows") or {}
    items = {}
    for k in set(assets) | set(holds) | set(flows):
        if k == "money":
            continue
        a = assets.get(k) or {}
        items[k] = {"held": n(a.get("balance")), "unit_cost": n(a.get("unit_cost")) or None,
                    "capacity": n((holds.get(k) or {}).get("capacity") or a.get("capacity")) or None,
                    "orders": _orders(holds.get(k)),
                    "flow": {kk: n(vv) for kk, vv in (flows.get(k) or {}).items()}}
    s["store"] = {"id": store_id, "capacity": n(inv.get("capacity")), "used": n(inv.get("used")), "items": items}

    # the storehouse's operations: every building, ship and route it supplies, with this turn's set target and
    # last turn's realized flows (a route's sales and purchases show here, not on the ship)
    ops = {}
    if store_id:
        for op in ((api.get("/buildings/%s/operations" % store_id) or {}).get("operations") or []):
            ops[op.get("reference")] = {
                "recipe": op.get("recipe"), "target": n(op.get("target")), "volume": n(op.get("volume")),
                "limitation": op.get("limitation"),
                "flows": {k: {kind: {kk: n(vv) for kk, vv in (v.get(kind) or {}).items()} for kind in ("projection", "realized")}
                          for k, v in (op.get("flows") or {}).items()}}
    s["operations"] = ops

    s["ships"] = []
    for tid in biz.get("transport_ids") or []:
        t = api.get("/transports/%s" % tid) or {}
        po = t.get("previous_operation") or {}
        r = t.get("route") or {}
        fl = ((t.get("inventory") or {}).get("previous_flows")) or {}
        s["ships"].append({"id": str(tid), "name": t.get("name"), "town": str(t.get("town_id")),
                           "target": n(po.get("target")), "production": n(po.get("production")),
                           "set_target": (ops.get("transport/%s" % tid) or {}).get("target"),
                           "running_cost": n((fl.get("none") or {}).get("production_cost")),
                           "route_to": r.get("remote_town"), "route_id": r.get("id"),
                           "route_trips": n(r.get("actual_trips")), "route_capacity_cost": n(r.get("capacity_cost")),
                           "route_orders": {k: _orders(h) for k, h in (r.get("holdings") or {}).items()},
                           "route_results": {k: [(mg or {}).get("result") for mg in ((h or {}).get("managers") or [])]
                                             for k, h in (r.get("holdings") or {}).items()},
                           "route_flows": ((ops.get("route/%s" % tid) or {}).get("flows")) or {},
                           "route_limitation": (ops.get("route/%s" % tid) or {}).get("limitation")})

    md = api.get("/towns/%s/marketdata" % s["home_town"]) or {}
    mk = md.get("markets", md) if isinstance(md, dict) else {}
    s["market"] = {k: {"price": n(v.get("price")), "bid": n(v.get("highest_bid")) or None, "ask": n(v.get("lowest_ask")) or None,
                       "bid_vol": n(v.get("bid_volume_10")), "ask_vol": n(v.get("ask_volume_10")),
                       "traded": n(v.get("volume_prev_12")) / 12.0}
                   for k, v in mk.items() if isinstance(v, dict)}

    s["history_use"] = _history_use()
    s["api"] = {"calls": dict(api.calls), "errors": [list(e[:3]) + [str(e[3])[:120]] for e in api.errors]}
    return s
