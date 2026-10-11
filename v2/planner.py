"""Bot v2 planner: from one snapshot, decide every order and flag every risk.

One pass, one model of the whole business:
  demand  = recipes x building targets + household duty + sustenance, cross-checked with observed use
  supply  = what our own buildings make
  orders  = per item: perishables bought to need, storable inputs kept at a runway, outputs sold
            above cost, chain intermediates protected
  flags   = anything that will stall, waste or lose money, ranked
Returns a plan dict; never touches the game (shadow.py writes it to files).
"""
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load_json(name):
    with open(os.path.join(HERE, name)) as f:
        return json.load(f)


def snap_price(p, up):
    """The game's price grid (same rule v1 learned from the server): <= 2 decimals, 3 significant
    digits; lead digit 1 any last digit, 2-4 even last digit, 5-9 last digit 0 or 5."""
    if not p or p <= 0:
        return p
    e = math.floor(math.log10(p) + 1e-12) - 2
    lead = int(p / 10 ** (e + 2) + 1e-9)
    step = max(10 ** e * (5 if lead >= 5 else 2 if lead >= 2 else 1), 0.01)
    k = p / step
    k = math.ceil(k - 1e-9) if up else math.floor(k + 1e-9)
    return round(k * step, 6)


def _n(x, d=0.0):
    try:
        return float(x)
    except (TypeError, ValueError):
        return d


def first_tier(orders, field):
    for i, o in enumerate(orders):
        if _n(o.get(field)) > 0:
            return i, o
    return None, None


def plan(s, cfg=None, recipes=None):
    cfg = cfg or load_json("config.json")
    recipes = recipes or load_json("data/recipes.json")
    items = (s.get("store") or {}).get("items") or {}
    market = s.get("market") or {}
    flags, orders, notes = [], {}, []

    def flag(sev, item, text, fix=None):
        flags.append({"severity": sev, "item": item, "text": text, "fix": fix})

    # ---------- demand / supply from recipes ----------
    use, make, users = {}, {}, {}
    prestige_ops = []

    def add_recipe(name, target, who):
        r = recipes.get(name or "")
        if not r or target <= 0:
            return
        for i in r.get("inputs") or []:
            use[i["product"]] = use.get(i["product"], 0) + i["amount"] * target
            users.setdefault(i["product"], []).append(who)
        for o in r.get("outputs") or []:
            make[o["product"]] = make.get(o["product"], 0) + o["amount"] * target
        if r.get("prestige"):
            prestige_ops.append((who, name, target, r))

    for b in s.get("buildings") or []:
        add_recipe(b.get("recipe"), b.get("target", 0), b.get("name"))
        # a building running under target because an input is missing
        lim, tgt, prod = b.get("limitation"), b.get("target", 0), b.get("production", 0)
        if tgt > 0 and prod < tgt * 0.9 and lim and lim != "labour" and "space" not in str(lim):
            flag("risk", lim, "%s ran %.1f of %.1f: short of %s" % (b["name"], prod, tgt, lim),
                 "keep a %s buy (or stock) that covers it" % lim)
    hd = s.get("household_duty") or {}
    add_recipe(hd.get("recipe"), hd.get("target", 0), "household")
    for k, v in (s.get("sustenance") or {}).items():
        use[k] = use.get(k, 0) + v
        users.setdefault(k, []).append("household upkeep")

    hist = s.get("history_use") or {}
    perishable = set(cfg.get("perishable") or [])
    never_drop = set(cfg.get("never_drop") or [])
    runway = cfg.get("runway_turns") or {}
    ceil_ = cfg.get("buy_ceiling") or {}
    floor_ = cfg.get("sell_floor") or {}
    inter = set((cfg.get("chain") or {}).get("intermediates") or [])
    buf_turns = (cfg.get("chain") or {}).get("buffer_turns", 4)
    stockpiles = cfg.get("stockpiles") or {}

    # ---------- inputs we buy ----------
    bursty = set(cfg.get("bursty") or [])
    candidates = set(use) | never_drop | set(i for i in items if (items[i].get("flow") or {}).get("consumption")
                                            or (items[i].get("flow") or {}).get("shortfall"))
    for item in sorted(candidates):
        if item in ("money",) or item in inter:
            continue        # chain intermediates are made, not bought: their buffers are checked below
        it = items.get(item) or {"held": 0, "orders": [], "flow": {}}
        fl = it.get("flow") or {}
        observed = fl.get("consumption", 0) + fl.get("shortfall", 0)
        peak = max(hist.get(item) or [0])
        planned = use.get(item, 0)
        own = make.get(item, 0)
        if item == "labour":
            own = max(own, fl.get("production", 0))
        if item in perishable:
            # bought to need, never stockpiled: last turn's real demand, bursts covered by the recent peak
            # labour: what the buildings will use at their set rates, or last turn's real demand
            # (construction, ship crews); porterage: bursty, so the recent peak
            demand = max(observed, planned if item == "labour" else 0, peak if item in bursty else 0)
            net = max(0.0, demand - own)
            want = math.ceil(net * (1 + (cfg.get("labour", {}).get("buffer_share", 0.05) if item == "labour" else 0.10)))
            hold = None
        else:
            demand = max(planned, observed)
            net = max(0.0, demand - own)
            if net <= 0.01 and item not in never_drop:
                continue        # we make enough ourselves (chain intermediates land here)
            r = runway.get(item, runway.get("_default", 4))
            hold = math.ceil(max(net, demand * 0.25) * r) if r else None
            short = (hold or 0) - it.get("held", 0)
            want = math.ceil(net + (min(net, short / 2.0) if short > 0 else 0))
        if want <= 0 and item not in never_drop:
            continue
        cap = ceil_.get(item)
        m = market.get(item) or {}
        ask = m.get("ask")
        price = None
        if ask:
            price = snap_price(min(ask * 1.02, cap) if cap else ask * 1.02, up=False)
            if cap and ask > cap:
                rw = (it.get("held", 0) / net) if net > 0 else 99
                flag("risk" if (item in never_drop and rw < 2) else "tune", item,
                     "home ask %.2f is above our ceiling %.2f: the buy can't fill" % (ask, cap),
                     "raise the ceiling or find another source")
        elif want > 0 and item != "labour":
            flag("tune", item, "no sellers at home right now", "stock covers it, or import")
        o = {"buy_volume": int(want)}
        if price:
            o["buy_price"] = str(price)
        if hold:
            o["max_holding"] = int(min(hold, it.get("capacity") or hold))
        orders.setdefault(item, {})["buy"] = o
        runway_now = (it.get("held", 0) / net) if net > 0 else None
        orders[item]["why"] = "uses %.1f/turn (%s), makes %.1f, holds %.0f%s" % (
            demand, ", ".join(sorted(set(users.get(item, ["observed"])))[:3]), own, it.get("held", 0),
            (" = %.1f turns" % runway_now) if runway_now is not None else "")

        # compare with what v1 has live
        ti, cur = first_tier(it.get("orders") or [], "buy_volume")
        if cur is None:
            covered = (runway_now is not None and runway_now >= 2) or net <= 0.01
            if want > 0 and (item in never_drop or not covered):
                flag("risk", item, "needed (%.1f/turn) but there is NO buy order%s" % (
                    max(net, demand), "" if covered else ", stock %.0f" % it.get("held", 0)),
                     "add buy %d" % want)
        else:
            cv = _n(cur.get("buy_volume"))
            if item in perishable:
                exp = fl.get("expiration", 0)
                if exp > max(5, 0.05 * fl.get("purchase", 0)) and cv >= want * 0.9:
                    flag("waste", item, "%.0f bought %s expired last turn (buy %d vs need %d)" % (exp, item, cv, want),
                         "buy %d" % want)
                elif cv > want * 1.25 + 5:
                    flag("waste", item, "buying %d, need ~%d" % (cv, want), "buy %d" % want)
                elif cv < net * 0.9:
                    flag("risk", item, "buying %d, short of ~%d needed" % (cv, want), "buy %d" % want)
            else:
                if runway_now is not None and runway_now < 1 and cv < net:
                    flag("risk", item, "only %.1f turns of %s left and buying %d (need %d)" % (runway_now, item, cv, want),
                         "buy %d" % want)
                elif abs(cv - want) > max(3, 0.25 * want):
                    flag("tune", item, "buy %d vs v2 %d" % (cv, want), None)

    # ---------- chain intermediates: runway between steps ----------
    for item in inter:
        it = items.get(item) or {}
        u = use.get(item, 0)
        if u <= 0:
            continue
        turns = it.get("held", 0) / u
        target = buf_turns * u
        if turns < 1:
            flag("risk", item, "%s buffer %.1f turns (holds %.0f, next step uses %.0f/turn)" % (item, turns, it.get("held", 0), u),
                 "check the step that makes it")
        orders.setdefault(item, {})["buffer"] = {"target": int(target), "held": int(it.get("held", 0))}

    # ---------- outputs we sell ----------
    for item, mk in make.items():
        it = items.get(item) or {}
        surplus = mk - use.get(item, 0)
        if surplus <= 0.5 or item in inter:
            continue
        uc = it.get("unit_cost") or 0
        floor = max(floor_.get(item, 0), snap_price(uc * 1.02, up=True) if uc else 0)
        m = market.get(item) or {}
        si, cur = first_tier(it.get("orders") or [], "sell_volume")
        floor = min(floor, floor_.get(item) or floor) if floor_.get(item) else floor
        want = {"sell_volume": int(round(surplus)), "sell_price": str(snap_price(floor, up=True)) if floor else None}
        orders.setdefault(item, {})["sell"] = want
        if cur is None:
            flag("tune", item, "we make %.0f/turn more than we use but there is no sell order" % surplus, "sell %d" % surplus)
            continue
        cp = _n(cur.get("sell_price"))
        if uc and cp and cp < uc:
            flag("waste", item, "it costs us %.2f to make, the floor sells at %.2f" % (uc, cp),
                 "cut its cost (labour price) or export it; a higher floor would just stop home sales")
        sold = (it.get("flow") or {}).get("sale", 0)
        if m.get("bid") and cp > m["bid"] * 1.15 and sold < surplus * 0.5:
            flag("tune", item, "floor %.2f vs home bid %.2f: barely selling (%.0f of %.0f)" % (cp, m["bid"], sold, surplus), None)

    # ---------- stockpiles held on purpose ----------
    for item, target in stockpiles.items():
        it = items.get(item) or {}
        orders.setdefault(item, {})["stockpile"] = {"target": target, "held": round(it.get("held", 0), 1)}

    # ---------- prestige: what each sink costs ----------
    def cost_of(r, target=1.0):
        c = 0.0
        for i in r.get("inputs") or []:
            p = (market.get(i["product"]) or {}).get("price") or (items.get(i["product"]) or {}).get("unit_cost") or 0
            if i["product"] == "labour":
                p = p or 2.0
            c += i["amount"] * p * target
        return c
    sinks = []
    for who, name, target, r in prestige_ops:
        c = cost_of(r)
        sinks.append({"sink": "%s (%s)" % (name, who), "prestige_per_turn": r["prestige"] * target,
                      "coin_per_prestige": round(c / r["prestige"], 1) if r["prestige"] else None})
    hhp = s.get("household") or {}
    sinks.sort(key=lambda x: x["coin_per_prestige"] or 1e9)

    # ---------- money ----------
    sev_rank = {"risk": 0, "waste": 1, "tune": 2}
    flags.sort(key=lambda f: (sev_rank.get(f["severity"], 9), f["item"] or ""))
    return {
        "turn": s.get("turn"), "t": s.get("t"), "mode": cfg.get("mode"),
        "cash": s.get("cash"), "prestige": hhp.get("prestige"), "prestige_free": hhp.get("free"),
        "prestige_rate": hhp.get("rate"),
        "counts": {k: sum(1 for f in flags if f["severity"] == k) for k in ("risk", "waste", "tune")},
        "flags": flags, "orders": orders, "sinks": sinks,
        "demand": {k: round(v, 1) for k, v in sorted(use.items())},
        "supply": {k: round(v, 1) for k, v in sorted(make.items())},
        "notes": notes,
    }
