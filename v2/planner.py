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
    """(index of the first tier using field, that tier with field summed over ALL tiers): several buy
    or sell tiers on one item (e.g. two labour bids) count together."""
    idx, total, first = None, 0.0, None
    for i, o in enumerate(orders):
        if _n(o.get(field)) > 0:
            total += _n(o.get(field))
            if idx is None:
                idx, first = i, dict(o)
    if first is not None:
        first[field] = total
    return idx, first


def plan(s, cfg=None, recipes=None, goals=None):
    cfg = cfg or load_json("config.json")
    recipes = recipes or load_json("data/recipes.json")
    items = (s.get("store") or {}).get("items") or {}
    market = s.get("market") or {}
    flags, orders, notes = [], {}, []

    def flag(sev, item, text, fix=None):
        flags.append({"severity": sev, "item": item, "text": text, "fix": fix})

    min_coin = cfg.get("flag_min_coin_per_turn", 25)

    def buy_state(item):
        """(what our buy for item looks like now, what to do about it)."""
        it = items.get(item) or {}
        tier = next((o for o in it.get("orders") or [] if _n(o.get("buy_volume")) > 0 or o.get("buy_price")), None)
        if not tier:
            return "no buy order", "add a %s buy" % item
        m_ = market.get(item) or {}
        px, vol, ask = _n(tier.get("buy_price")), _n(tier.get("buy_volume")), m_.get("ask")
        d = "buy is live (%s @ %s)" % ("%d" % vol if vol else "no volume cap", tier.get("buy_price"))
        if ask and px and ask > px:
            return d + ", but the home ask %.2f is above it" % ask, "raise the buy price (or ceiling) or find another source"
        if (it.get("flow") or {}).get("purchase", 0) <= 0:
            return (d + ", home ask %.2f x%.0f, yet 0 bought last turn" % (ask or 0, m_.get("ask_vol") or 0),
                    "find out why the buy isn't filling")
        return d + ", %.0f bought last turn" % it["flow"]["purchase"], "the buy is too small for the stalled buildings: raise it"

    # ---------- stalled buildings, and the one input that really stalls them ----------
    blds = s.get("buildings") or []
    stalled = {}        # building name -> the input it ran short of (a bin full of output is a throttle, not a stall)
    for b in blds:
        lim, tgt, prod = b.get("limitation"), b.get("target", 0), b.get("production", 0)
        if tgt > 0 and prod < tgt * 0.9 and lim and lim != "labour" and "space" not in str(lim):
            stalled[b["name"]] = lim
    outputs = {b["name"]: {o["product"] for o in ((recipes.get(b.get("recipe") or "") or {}).get("outputs") or [])}
               for b in blds}

    def makers_stalled(item):
        return [n for n in stalled if item in outputs.get(n, ())]

    def root_item(name, depth=0):
        ups = makers_stalled(stalled[name])
        return stalled[name] if not ups or depth > 6 else root_item(ups[0], depth + 1)

    roots = {}          # input item -> {"buildings": [...], "knock_on": [...]}: one entry per real cause
    for name, lim in stalled.items():
        r_ = roots.setdefault(root_item(name), {"buildings": [], "knock_on": []})
        (r_["knock_on"] if makers_stalled(lim) else r_["buildings"]).append((name, lim))
    stalled_items = set(roots) | set(stalled.values())
    starved = set().union(*(outputs[n] for n in stalled)) if stalled else set()   # items the stalled buildings should be making

    # ---------- demand / supply from recipes ----------
    use, use_full, make, users = {}, {}, {}, {}      # use = buildings running now; use_full adds the stalled ones
    prestige_ops = []

    def add_recipe(name, target, who, running=True):
        r = recipes.get(name or "")
        if not r or target <= 0:
            return
        for i in r.get("inputs") or []:
            use_full[i["product"]] = use_full.get(i["product"], 0) + i["amount"] * target
            if running:
                use[i["product"]] = use.get(i["product"], 0) + i["amount"] * target
                users.setdefault(i["product"], []).append(who)
        if not running:
            return          # a stalled building makes nothing and consumes nothing until its input comes back
        for o in r.get("outputs") or []:
            make[o["product"]] = make.get(o["product"], 0) + o["amount"] * target
        if r.get("prestige"):
            prestige_ops.append((who, name, target, r))

    for b in blds:
        add_recipe(b.get("recipe"), b.get("target", 0), b.get("name"), running=b["name"] not in stalled)
    hd = s.get("household_duty") or {}
    add_recipe(hd.get("recipe"), hd.get("target", 0), "household")
    for k, v in (s.get("sustenance") or {}).items():
        use[k] = use.get(k, 0) + v
        use_full[k] = use_full.get(k, 0) + v
        users.setdefault(k, []).append("household upkeep")

    # one flag per real cause: the farm, the retting pit and everything downstream of them are one problem
    for lim, g in sorted(roots.items()):
        names = [n for n, _ in g["buildings"]]
        d, fix = buy_state(lim)
        restart = sum(i["amount"] * b_.get("target", 0)
                      for b_ in blds if b_["name"] in stalled and root_item(b_["name"]) == lim
                      for i in ((recipes.get(b_.get("recipe") or "") or {}).get("inputs") or []) if i["product"] == "labour")
        text = "%s ran short of %s (%s)" % (", ".join(names), lim, d)
        if g["knock_on"]:
            text += "; knock-on: " + ", ".join("%s (no %s)" % kv for kv in g["knock_on"])
        if restart > 0:
            text += "; labour need rises ~%.0f/turn when they restart" % restart
        flag("risk", lim, text, fix)

    # ---------- build manager: sites under construction (sized before the buy loop, because labour for a site that can
    # progress is real demand) ----------
    bp = None
    try:
        import builds
        sites = builds.scan_sites(s, cfg)
        if sites:
            bp = builds.plan_builds(sites, s, cfg, items, market, use, snap_price)
            for item, n in bp["drip"].items():
                use[item] = use.get(item, 0) + n
                use_full[item] = use_full.get(item, 0) + n
                users.setdefault(item, []).append("construction")
    except Exception as e:      # a new module must never blank the hourly report
        notes.append("builds skipped: %s: %s" % (type(e).__name__, e))

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
            m0 = market.get(item) or {}
            if r and net > 0 and (m0.get("ask_vol") or 0) >= 20 * net:
                r = min(r, 1)   # a deep market (donations at 1 coin, 99k offered) needs no runway
            hold = math.ceil(max(net, demand * 0.25) * r) if r else None
            short = (hold or 0) - it.get("held", 0)
            want = math.ceil(net + (min(net, short / 2.0) if short > 0 else 0))
            if hold and it.get("held", 0) >= 2 * hold and item not in never_drop:
                continue        # already stocked well past the runway: no order needed
        if want <= 0 and item not in never_drop:
            continue
        cap = ceil_.get(item)
        m = market.get(item) or {}
        ask = m.get("ask")
        price = None
        # a buy price is a LIMIT: trades clear at the market, not at our bid (Oct 12 turn 13237: labour bid 2.00
        # paid 1.66, fish 2.50 paid 1.70, meat 3.02 paid 2.28, tools 6.20 paid 5.14, cured fish 26 paid 24.8).
        # Bidding just over the lowest ask only under-fills a deep need (labour 490 vs 430 offered near the ask),
        # so bid at our ceiling; with no ceiling, a little over the ask.
        if cap:
            price = snap_price(cap, up=False)
        elif ask:
            price = snap_price(ask * 1.05, up=False)
        if ask:
            if cap and ask > cap:
                # the lowest ask above our ceiling only matters if the buy is really failing: the bid side can still
                # clear (porterage fills at 0.42 against a 1.1 ask). Flag only when last turn's purchases fell short
                # of need, or stock is under the runway.
                rw = (it.get("held", 0) / net) if net > 0 else 99
                bought = fl.get("purchase", 0)
                failing = (net > 0.01 and bought < 0.8 * net) or (hold and it.get("held", 0) < hold)
                if failing:
                    flag("risk" if (item in never_drop and rw < 2) else "tune", item,
                         "home ask %.2f is above our ceiling %.2f and last turn bought %.0f of ~%.0f needed: the buy can't fill" % (
                             ask, cap, bought, net),
                         "raise the ceiling or find another source")
        elif want > 0 and item != "labour" and (hold is None or it.get("held", 0) < hold):
            flag("tune", item, "no sellers at home right now and stock is below the runway", "import it or find another source")
        o = {"buy_volume": int(want)}
        if price:
            o["buy_price"] = str(price)
        if hold:
            # the stop-at never sits under two turns of use: if the game checks it before the turn's use is
            # drawn, a one-turn cap (donations: hold 40, use 40) would skip the buy every other turn
            stop = max(hold, math.ceil(2 * demand))
            o["max_holding"] = int(min(stop, it.get("capacity") or stop))
        orders.setdefault(item, {})["buy"] = o
        runway_now = (it.get("held", 0) / net) if net > 0 else None
        orders[item]["why"] = "uses %.1f/turn (%s), makes %.1f, holds %.0f%s" % (
            demand, ", ".join(sorted(set(users.get(item, ["observed"])))[:3]), own, it.get("held", 0),
            (" = %.1f turns" % runway_now) if runway_now is not None else "")

        # compare with what v1 has live
        ti, cur = first_tier(it.get("orders") or [], "buy_volume")
        # a buy with a price but no volume (arms, tar, timber) is a standing order v1 left open: it counts as a buy
        standing = cur is None and any(o.get("buy_price") for o in it.get("orders") or [])
        unit = ask or it.get("unit_cost") or 0
        stalled_here = item in stalled_items     # demand seen while its own consumers are stalled is understated
        if cur is None and not standing:
            covered = (runway_now is not None and runway_now >= 2) or net <= 0.01
            if want > 0 and (item in never_drop or not covered):
                flag("risk", item, "needed (%.1f/turn) but there is NO buy order%s" % (
                    max(net, demand), "" if covered else ", stock %.1f" % it.get("held", 0)),
                     "add buy %d" % want)
        elif cur is not None:
            cv = _n(cur.get("buy_volume"))
            if item in perishable:
                exp = fl.get("expiration", 0)
                share = cfg.get("labour", {}).get("buffer_share", 0.05) if item == "labour" else 0.10
                target_buf = math.ceil(demand * share)
                if exp > max(5, 0.05 * fl.get("purchase", 0)) and exp * unit >= min_coin and it.get("held", 0) > 2 * target_buf:
                    # the loss is the standing stock rotting, not the size of the buy: more buying would make it worse
                    flag("waste", item, "%.0f %s expired last turn (~%.0f coin): holding %.0f against a ~%d buffer target" % (
                        exp, item, exp * unit, it.get("held", 0), target_buf),
                         "trim the buy until the stock is near %d" % target_buf)
                elif cv > want * 1.25 + 5 and not stalled_here and (cv - want) * unit >= min_coin:
                    flag("waste", item, "buying %d, need ~%d" % (cv, want), "buy %d" % want)
                elif cv < net * 0.9:
                    flag("risk", item, "buying %d, short of ~%d needed" % (cv, want), "buy %d" % want)
            else:
                if runway_now is not None and runway_now < 1 and cv < net:
                    flag("risk", item, "only %.1f turns of %s left and buying %d (need %d)" % (runway_now, item, cv, want),
                         "buy %d" % want)
                elif hold and it.get("held", 0) >= 2 * hold:
                    # buying well past the runway; v1 smaller or equal to v2 is just a different buffer policy
                    room = (it.get("capacity") or 1e9) - it.get("held", 0)
                    extra = min(cv, max(room, 0.0)) - net
                    if extra * unit >= min_coin:
                        flag("tune", item, "buying %d/turn with %.0f in stock (%.0f turns at current use); v2 buys %d" % (
                            cv, it.get("held", 0), runway_now if runway_now is not None else 0, want), None)

    # ---------- chain intermediates: runway between steps ----------
    for item in inter:
        it = items.get(item) or {}
        u = use.get(item, 0)
        if u <= 0:
            continue
        turns = it.get("held", 0) / u
        target = buf_turns * u
        if turns < 1 and item not in starved:       # a buffer empty because its maker is stalled is a knock-on, flagged once above
            flag("risk", item, "%s buffer %.1f turns (holds %.0f, next step uses %.0f/turn)" % (item, turns, it.get("held", 0), u),
                 "check the step that makes it")
        elif turns < min(2, buf_turns) and item not in starved:
            flag("tune", item, "%s buffer thin: %.1f turns (target %d)" % (item, turns, buf_turns),
                 "lift the maker's rate or hold back sales until it reaches %d" % int(target))
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
        fl_ = it.get("flow") or {}
        sold = fl_.get("sale", 0)
        # realized margin: what we got vs what the units we sold cost us. (The store's unit_cost is the average of
        # everything held, and a floor under it only loses money if we are actually selling at it.)
        if sold > 0 and fl_.get("sale_cost", 0) > 0 and fl_.get("sale_value", 0) < fl_["sale_cost"] * 0.995:
            loss = fl_["sale_cost"] - fl_.get("sale_value", 0)
            if loss >= min_coin:
                flag("waste", item, "sold %.0f at %.2f avg against %.2f cost each: losing %.0f coin/turn" % (
                    sold, fl_.get("sale_value", 0) / sold, fl_["sale_cost"] / sold, loss),
                     "cut its cost (labour price) or export it; a higher floor would just stop home sales")
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

    # every coin -> prestige sink ranked at today's prices, and the agreed permanent purchases (shadow)
    pp = None
    try:
        import prestige
        pp = prestige.rank_sinks(s, cfg, recipes, items, market, make)
        pp["agreed"] = prestige.agreed_status(s, cfg)
        for row in pp["ranked"]:        # a clearly cheaper tier at a site we already run is worth a look
            cur = next((r for r in pp["ranked"] if r["running"] and r["site"] == row["site"]), None)
            if cur and not row["running"] and row["owned"] and not row["thin"] and row["effective"] < 0.85 * cur["effective"]:
                flag("tune", row["sink"], "%s costs %.1f coin per prestige at %s, vs %.1f for the running %s" % (
                    row["sink"], row["effective"], row["site"], cur["effective"], cur["sink"]),
                     "check it is unlocked, then switch")
    except Exception as e:
        notes.append("prestige skipped: %s: %s" % (type(e).__name__, e))

    # ---------- build buys: the one-off orders, once the regular ones exist ----------
    if bp:
        try:
            builds.annotate(bp, orders, items)
            for item, e in bp["buys"].items():
                if e["action"] == "buy":
                    orders.setdefault(item, {})["build_buy"] = {k: e[k] for k in ("buy_volume", "buy_price", "max_holding") if k in e}
                if e.get("switch_off"):
                    flag("tune", item, "build materials for %s are in (%s held, %d needed) but a buy is still live" % (
                        ", ".join(x["building"] for x in bp["sites"]), e["held"], e["need"]), "switch the %s buy off" % item)
        except Exception as e:
            notes.append("builds skipped: %s: %s" % (type(e).__name__, e))

    # ---------- goal queue: standing goals become orders (shadow: written to the plan, never sent) ----------
    goal_results = []
    try:
        import goals as goals_mod
        if goals is None:
            goals, gnote = goals_mod.load()
            if gnote:
                notes.append(gnote)
        goal_results = goals_mod.plan_goals(goals, s, cfg, items, market, snap_price)
        goals_mod.merge(orders, goal_results)
        for r in goal_results:
            if r["status"] in ("blocked", "conflict", "invalid"):
                flag("tune", r["item"] or "goals", "goal %s: %s" % (r["id"], r["detail"]), None)
    except Exception as e:
        notes.append("goals skipped: %s: %s" % (type(e).__name__, e))

    # ---------- money ----------
    sev_rank = {"risk": 0, "waste": 1, "tune": 2}
    flags.sort(key=lambda f: (sev_rank.get(f["severity"], 9), f["item"] or ""))
    return {
        "turn": s.get("turn"), "t": s.get("t"), "mode": cfg.get("mode"),
        "live_items": sorted(((cfg.get("live") or {}).get("items")) or []),
        "cash": s.get("cash"), "prestige": hhp.get("prestige"), "prestige_free": hhp.get("free"),
        "prestige_rate": hhp.get("rate"),
        "counts": {k: sum(1 for f in flags if f["severity"] == k) for k in ("risk", "waste", "tune")},
        "flags": flags, "orders": orders, "sinks": sinks, "builds": bp, "goals": goal_results, "prestige_plan": pp,
        "stalls": {k: {"buildings": [n for n, _ in g["buildings"]], "knock_on": [n for n, _ in g["knock_on"]]}
                   for k, g in roots.items()},
        "demand": {k: round(v, 1) for k, v in sorted(use.items())},
        "supply": {k: round(v, 1) for k, v in sorted(make.items())},
        "notes": notes,
    }
