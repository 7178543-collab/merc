"""Goal planner (shadow, Oct 23): one goal, one budget. See v2/GOAL.md.

Goal (Taylor, Oct 22): grow BUSINESS VALUE = cash + stock at market value.

Each run solves one linear program over a turn of steady flow: building rates, household duty, buys, sells, pile
draw-down and stock build, maximising value gained per turn, subject to item balances, own labour, building sizes,
home market depth, the free-prestige floor and the cash floor. Duals and re-solves price every change and investment.
Pure functions over the snapshot; never touches the game.
"""
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

DEFAULTS = {
    "prestige_floor": 300,       # free prestige never planned under this (Taylor Oct 22: keep 300 free)
    "prestige_horizon": 240,     # turns over which free prestige may drift down to the floor
    "prestige_recover_turns": 24,
    "cash_floor": 4000,          # under it the plan must earn cash back
    "cash_recover_turns": 24,
    "building_tax": 226,         # per turn, all plots (doc, Oct 18); charged whether buildings run or not
    "sales_window": 12,          # turns of our own sales history behind the first sales step
    "sales_growth": 0.25,        # home sales count up to this much over what we really sold (the rest is a trial)
    "trial_turns": 12,           # an idle pile is offered over this many turns (not counted in the plan)
    "undercut": 0.93,            # price of the second sales step, which can win up to market_share of the town
    "market_share": 0.3,
    "keep_value": 0.5,           # stock made but not sold counts at this share of its market value
    "mark_share": 0.9,           # market value of stock = this x home last price
    "mark_no_market": 0.3,       # ... or this x our unit cost when the home market never trades it
    "drain_turns": 12,           # a pile over its reserve may be drawn down over this many turns
    "buffer_turns": 3,           # stock of an input never drawn under this many turns of current use
    "invest_horizon": 240,       # an investment must pay back within this many turns
    "max_target": {"logging camp": 20},   # forest regrowth (clearcut lesson); otherwise the building size
    "tenants_labour": 50,        # own labour per Tenants level (10 per tenant, 5 tenants a level)
    "change_min": 0.05,          # building target changes smaller than this are noise
    "reserve": {"tools": 100},   # never drawn under (Taylor: tools stockpile 100+); config stockpiles and sell
                                 # min_holding are reserves too
    "urban_plot_tax": 6.0,       # per plot per turn (rural 0.5): the conservative case for a new plot
}

NOT_STOCK = {"money", "labour", "porterage", "lodging", "protection"}
SHORT_COST = 1e5            # per unit of a fixed need left unmet: only when nothing can supply it (see solve)


def _n(x, d=0.0):
    try:
        v = float(x)
    except (TypeError, ValueError):
        return d
    return v if math.isfinite(v) else d          # NaN / inf from a market feed would break the solver


def load_cfg(cfg=None):
    c = dict(DEFAULTS)
    c.update(((cfg or {}).get("goal")) or {})
    return c


# ---------------------------------------------------------------- history (our sales, business value over time)

def read_history(path=None, last=60):
    """Distinct turns from history/merc-YYYY-MM.jsonl (newest last), at most `last` of them."""
    rows = []
    if path is None:
        d = os.path.join(ROOT, "history")
        try:
            files = sorted(f for f in os.listdir(d) if f.startswith("merc-") and f.endswith(".jsonl"))
        except OSError:
            files = []
        paths = [os.path.join(d, f) for f in files[-2:]]
    else:
        paths = [path]
    for p in paths:
        try:
            with open(p) as f:
                for line in f:
                    try:
                        rows.append(json.loads(line))
                    except ValueError:
                        pass
        except OSError:
            pass
    by_turn = {}
    for r in rows:
        if r.get("turn") is not None and r.get("items"):
            by_turn[r["turn"]] = r          # the later line of a turn wins (end-of-turn state)
    return [by_turn[t] for t in sorted(by_turn)][-last:]


def sales_avg(hist, window):
    """item -> average units sold per turn over the last `window` turns (col 3 of history items)."""
    h = hist[-window:]
    out = {}
    for r in h:
        for item, v in (r.get("items") or {}).items():
            if isinstance(v, list) and len(v) > 3:
                out[item] = out.get(item, 0.0) + _n(v[3])
    return {k: v / max(1, len(h)) for k, v in out.items()}


def value_of(row, perishable=()):
    """Business value of one history row: cash + held x price for every storable item."""
    stock = 0.0
    for item, v in (row.get("items") or {}).items():
        if item in NOT_STOCK or item in perishable or not isinstance(v, list) or len(v) < 7:
            continue
        stock += max(0.0, _n(v[0])) * _n(v[6])
    return _n(row.get("cash")) + stock, stock


def value_trend(hist, perishable=()):
    pts = [(r.get("turn"), value_of(r, perishable)[0]) for r in hist]
    out = {"now": pts[-1][1] if pts else None, "turn": pts[-1][0] if pts else None}
    for n in (6, 24, 48):
        if len(pts) > n:
            out["per_turn_%d" % n] = (pts[-1][1] - pts[-1 - n][1]) / n
    return out


# ---------------------------------------------------------------- game rules the model needs

def rank_tier(points):
    """Skill rank from points (game code): novice 0 (<100), worker 1 (<700), journeyman 2 (<3700), master 3."""
    p = _n(points)
    return 0 if p < 100 else 1 if p < 700 else 2 if p < 3700 else 3


def recipe_allowed(r, head_skills):
    """A recipe of tier t runs when the head of household's rank in its class is at least t - 1: tier-1 recipes are
    open to a novice (we run tier-1 textile at textile 62), make rope 2 (tier 3) runs on a maritime journeyman. Only
    the head's rank counts (game: only his promotions unlock recipes). Recipes that need a building upgrade, household
    duties and resident-only recipes are left out."""
    if not r or r.get("upgrades") or r.get("resident_only") or r.get("site") == "household":
        return False
    t = int(_n(r.get("tier"), 1.0))
    return rank_tier((head_skills or {}).get(r.get("class") or "", 0)) >= t - 1


def plot_tax_rate(btype, bdata):
    """Building tax per plot per turn when the game didn't tell us (it does, per operation): town-centre buildings 6,
    the quarry 20, rural land 0.5 (operations seen Oct 23)."""
    if btype == "quarry":
        return 20.0
    req = (bdata.get(btype) or {}).get("requires")
    return 6.0 if isinstance(req, dict) and req.get("center") else 0.5


def mgmt_per_plot(btype, bdata):
    """Management per extra plot (game client R()): building types with room for 75+ plots 0.01, up to 10 plots 0.25,
    else 0.1."""
    size = _n(((bdata.get(btype) or {}).get("construction") or {}).get("size"))
    if not size:
        return 0.1
    return 0.01 if size >= 75 else 0.25 if size <= 10 else 0.1


def is_prestige_building(btype, bdata):
    return bool((bdata.get(btype) or {}).get("prestige")) or btype in ("park", "mansion")


def management_used(s, bdata):
    """Regular management our buildings use (game client U()): 1 for the first building of a type, 0.5 for each
    further one, plus (plots - 1) x mgmt_per_plot. Prestige buildings use the separate prestige pool. Upgrades are
    not in the snapshot, so this reads a little low."""
    seen, used = set(), 1.0                         # the storehouse
    for b in s.get("buildings") or []:
        t = b.get("type")
        if not t or is_prestige_building(t, bdata):
            continue
        size = _n(b.get("size")) + _n((b.get("construction") or {}).get("size"))
        used += (0.5 if t in seen else 1.0) + max(0.0, size - 1) * mgmt_per_plot(t, bdata)
        seen.add(t)
    return used


def materials_thin(btype, bdata, goods, turns=24, share=0.3):
    """Materials the home market can't supply within `turns` (what we hold over the reserve + share x what the town
    trades a turn x turns). Bricks trade ~2 a turn at home: a building needing 120 would sit unbuilt for months."""
    mats = ((bdata.get(btype) or {}).get("construction") or {}).get("materials") or {}
    thin = []
    for item, q in mats.items():
        gd = goods.get(item) or {}
        if gd.get("perishable"):
            continue                      # labour: deep market, bought per turn as the site works
        have = max(0.0, gd.get("held", 0.0) - gd.get("reserve", 0.0))
        if have + share * gd.get("traded", 0.0) * turns < _n(q):
            thin.append(item)
    return thin


def materials_cost(btype, bdata, goods):
    """Coin for one plot of a building type: the full construction materials (a new building is one plot; a park
    plot cost the park's full materials, as the game charged), at home asks, else last price, else our unit cost."""
    mats = ((bdata.get(btype) or {}).get("construction") or {}).get("materials") or {}
    cost = 0.0
    for item, q in mats.items():
        gd = goods.get(item) or {}
        px = gd.get("buy_px") or gd.get("last") or gd.get("cost") or 0.0
        cost += _n(q) * px
    return cost


# ---------------------------------------------------------------- the model

def _coeffs(b, recipes, memory=None):
    """Per unit of target: (inputs, outputs, prestige). Live flows when it produced (they carry the real porterage,
    tool wear and worker bonuses); when it didn't (starved last turn), the last flows it ran on with this recipe
    (memory, kept by shadow.py), else the recipe. Oct 23: a starved remote building fell back to the recipe, which has
    no porterage, so the plan under-bought porterage for the farm, pit and camp."""
    r = recipes.get(b.get("recipe") or "") or {}
    prod = _n(b.get("production"))
    ins, outs = {}, {}
    fl = b.get("flows") or {}
    mem = (memory or {}).get(str(b.get("id"))) or {}
    if not (prod > 0 and fl) and mem.get("recipe") == b.get("recipe") and mem.get("ins"):
        return dict(mem["ins"]), dict(mem.get("outs") or {}), _n(r.get("prestige"))
    if prod > 0 and fl:
        for item, f in fl.items():
            if _n(f.get("consumption")) > 0:
                ins[item] = _n(f["consumption"]) / prod
            if _n(f.get("production")) > 0:
                outs[item] = _n(f["production"]) / prod
    else:
        ins, outs = _recipe_io(r)
    return ins, outs, _n(r.get("prestige"))


def _recipe_io(r):
    ins, outs = {}, {}
    for i in (r or {}).get("inputs") or []:
        ins[i["product"]] = ins.get(i["product"], 0) + _n(i["amount"])
    for o in (r or {}).get("outputs") or []:
        outs[o["product"]] = outs.get(o["product"], 0) + _n(o["amount"])
    return ins, outs


def _act_name(b):
    nm = b.get("name") or b.get("type")
    if b.get("id") and str(b["id"]) in str(nm):
        nm = b.get("type") or nm            # the game names some buildings '<type><id>'
    return nm


def new_building_candidates(s, recipes, bdata):
    """(type, recipe name, recipe) for every town-centre building type we could build and run: a recipe the head's
    rank allows, at a site of that type. Prestige buildings, storehouses and hosted buildings are left out."""
    head = (((s.get("household") or {}).get("workers") or [{}])[0] or {}).get("skills") or {}
    out = []
    for name, r in sorted(recipes.items()):
        t = r.get("site")
        b = bdata.get(t) or {}
        req = b.get("requires")
        if not t or not isinstance(req, dict) or set(req) != {"center"} or is_prestige_building(t, bdata):
            continue
        if t in ("warehouse", "storehouse", "outpost") or not (b.get("construction") or {}).get("materials"):
            continue
        if not recipe_allowed(r, head):
            continue
        ins, outs = _recipe_io(r)
        if not outs:
            continue
        out.append((t, name, r))
    return out


def coef_memory(s, recipes, memory=None):
    """Update the per-building flow memory from this snapshot: buildings that produced store their per-unit flows."""
    mem = dict(memory or {})
    for b in s.get("buildings") or []:
        if _n(b.get("production")) > 0 and b.get("flows") and recipes.get(b.get("recipe") or ""):
            ins, outs, _ = _coeffs(dict(b), recipes)
            mem[str(b.get("id"))] = {"recipe": b.get("recipe"), "ins": ins, "outs": outs, "turn": s.get("turn")}
    return mem


def build_model(s, cfg, recipes, drip=None, hist=None, buildings_data=None, extra_items=(), memory=None):
    """Collect everything the LP needs into plain dicts (separate from solving, so tests can poke at it)."""
    g = load_cfg(cfg)
    bdata = buildings_data or {}
    perishable = set((cfg or {}).get("perishable") or []) | {"labour"}
    items = (s.get("store") or {}).get("items") or {}
    market = s.get("market") or {}
    ops = s.get("operations") or {}
    hh = s.get("household") or {}
    head = ((hh.get("workers") or [{}])[0] or {}).get("skills") or {}
    hist = hist if hist is not None else []
    sold = {}
    if hist:
        a12, a24 = sales_avg(hist, int(g["sales_window"])), sales_avg(hist, 2 * int(g["sales_window"]))
        sold = {k: max(a12.get(k, 0.0), a24.get(k, 0.0)) for k in set(a12) | set(a24)}
    reserves = dict((cfg or {}).get("stockpiles") or {})
    reserves.pop("_about", None)
    for k, v in (g.get("reserve") or {}).items():
        reserves[k] = max(_n(v), _n(reserves.get(k)))

    acts = []            # activities: {name, kind, ins, outs, prestige, lb, ub, cur, group}
    groups = {}          # building id -> plots it can run in total (its recipe and any alternative share them)
    fixed_supply, fixed_demand = {}, {}
    taxes = {}           # building id -> tax per turn
    notes = []

    for b in s.get("buildings") or []:
        bid = str(b.get("id"))
        op = ops.get("producer/%s" % bid) or {}
        size = _n(b.get("size")) or 1.0
        if op.get("tax") is not None:
            taxes[bid] = _n(op.get("tax"))
        else:
            taxes[bid] = plot_tax_rate(b.get("type"), bdata) * size
        if b.get("construction"):
            continue                          # a site: its materials are fixed demand (drip), not an activity
        rec = b.get("recipe")
        r = recipes.get(rec or "")
        if rec and not r:                     # e.g. the farmstead's 'service 1': its flows are fixed supply/demand
            for item, f in (b.get("flows") or {}).items():
                if _n(f.get("production")):
                    fixed_supply[item] = fixed_supply.get(item, 0) + _n(f["production"])
                if _n(f.get("consumption")):
                    fixed_demand[item] = fixed_demand.get(item, 0) + _n(f["consumption"])
            continue
        ub = size
        cap = (g.get("max_target") or {}).get(b.get("type"))
        if cap is not None:
            ub = min(ub, float(cap))
        ub = max(ub, _n(b.get("target")))     # never plan a building smaller than it already runs by hand
        groups[bid] = ub
        nm = _act_name(b)
        if r:
            ins, outs, pr = _coeffs(b, recipes, memory)
            if outs or pr:
                acts.append({"name": nm, "kind": "building", "id": bid, "type": b.get("type"), "recipe": rec,
                             "ins": ins, "outs": outs, "prestige": pr, "lb": 0.0, "ub": ub,
                             "cur": _n(b.get("target")), "size": size, "group": bid, "main": True})
        # alternative recipes for the same building (not for prestige buildings: their recipe follows its own rules)
        if is_prestige_building(b.get("type"), bdata):
            continue
        for alt, ar in sorted(recipes.items()):
            if alt == rec or ar.get("site") != b.get("type") or not recipe_allowed(ar, head):
                continue
            ins, outs = _recipe_io(ar)
            if not outs:
                continue
            acts.append({"name": "%s [%s]" % (nm, alt), "kind": "building", "id": bid, "type": b.get("type"),
                         "recipe": alt, "ins": ins, "outs": outs, "prestige": _n(ar.get("prestige")), "lb": 0.0,
                         "ub": ub, "cur": 0.0, "size": size, "group": bid, "main": not r, "alt": True})

    # resident (worker) labour inside building operations is free labour already there
    for k, op in ops.items():
        if k.startswith("producer/"):
            res = _n((((op.get("flows") or {}).get("labour") or {}).get("projection") or {}).get("resident"))
            if res:
                fixed_supply["labour"] = fixed_supply.get("labour", 0) + res

    # household duty: resident labour only, so its labour is not in the balance
    hd = s.get("household_duty") or {}
    r = recipes.get(hd.get("recipe") or "")
    if r:
        kop = next((v for k, v in ops.items() if k.startswith("knight/")), {}) or {}
        lab = (((kop.get("flows") or {}).get("labour") or {}).get("projection") or {})
        resident = _n(lab.get("resident"))
        per = sum(_n(i["amount"]) for i in r.get("inputs") or [] if i["product"] == "labour") or 1.0
        ins = {i["product"]: _n(i["amount"]) for i in r.get("inputs") or [] if i["product"] != "labour"}
        outs = {o["product"]: _n(o["amount"]) for o in r.get("outputs") or []}
        acts.append({"name": "household duty", "kind": "duty", "recipe": hd.get("recipe"), "ins": ins, "outs": outs,
                     "prestige": 0.0, "lb": 0.0, "ub": resident / per if resident else _n(hd.get("target")),
                     "cur": min(_n(hd.get("target")), resident / per if resident else _n(hd.get("target")))})

    for item, v in (s.get("sustenance") or {}).items():
        fixed_demand[item] = fixed_demand.get(item, 0) + _n(v)
    for item, v in (drip or {}).items():
        fixed_demand[item] = fixed_demand.get(item, 0) + _n(v)

    names = set(fixed_supply) | set(fixed_demand) | set(items) | set(extra_items)
    names |= {k for k, m in market.items() if _n(m.get("traded")) > 0}
    for a in acts:
        names |= set(a["ins"]) | set(a["outs"])
    names.discard("money")

    use_now = {}
    for a in acts:
        for i, q in a["ins"].items():
            use_now[i] = use_now.get(i, 0) + q * a["cur"]
    for i, q in fixed_demand.items():
        use_now[i] = use_now.get(i, 0) + q

    try:
        import goal_switch
        own_sells = goal_switch.owns("sells", cfg) if (cfg or {}).get("goal") else False
    except Exception:
        own_sells = False
    never_sell = set((cfg or {}).get("never_drop") or []) - {"labour"}
    goods = {}
    for item in sorted(names):
        it = items.get(item) or {}
        m = market.get(item) or {}
        last, bid, ask = _n(m.get("price")), m.get("bid"), m.get("ask")
        traded = _n(m.get("traded"))
        held = _n(it.get("held"))
        cost = _n(it.get("unit_cost"))
        fl = it.get("flow") or {}
        perish = item in perishable
        mark = g["mark_share"] * last if (last and traded > 0) else g["mark_no_market"] * cost
        orders = it.get("orders") or []
        sell_px = next((_n(o.get("sell_price")) for o in orders if o.get("sell_price")), 0.0)
        reserve = max([_n(o.get("min_holding")) for o in orders] + [_n(reserves.get(item))])
        # buy step: the home ask, as deep as the town trades (labour is a deep market)
        buy_px = _n(ask) if ask else (last if traded > 0 else 0.0)
        buy_cap = 0.0
        if buy_px:
            buy_cap = max(traded, _n(m.get("ask_vol")), _n(fl.get("purchase")))
        # sell steps: what we really sold at our price, then an undercut step for town share. With the goal owning
        # sells, the old config floors no longer bind (Oct 23: garments 135 held at a 20.0 floor while the town
        # traded at 19.5, 0 sold for days, cash under 1k); v2 still keeps a sanity floor at 85% of the market. Never
        # a sale of a never-drop good (no order of ours would make it: tools 6 a turn were planned, v1 buys them).
        steps = []
        avg = sold.get(item, 0.0)
        floor = 0.0 if own_sells else _n(((cfg or {}).get("sell_floor") or {}).get(item))
        p1 = sell_px or last
        if avg > 0 and p1:
            steps.append((p1, avg))
        if bid and _n(m.get("bid_vol")) > 0 and (not floor or _n(bid) >= floor):
            steps.append((_n(bid), _n(m.get("bid_vol"))))       # instant fill at the home bid (resting buyers; a bid
                                                                # over the last price is still there to take)
        p2 = g["undercut"] * last
        if ask:
            # just under the cheapest seller (and never over the last price): we take the buyers first. Selling
            # over the ask we'd buy at would be a false arbitrage. (Oct 23: garments planned at 18.1 = 93% of 19.5
            # when 19.3 under the 19.5 wall of asks sells the same.)
            p2 = min(0.99 * _n(ask), last) if last else 0.99 * _n(ask)
        room = g["market_share"] * traded - avg - (_n(m.get("bid_vol")) if bid else 0.0)
        if p2 and room > 0.5 and (not floor or p2 >= floor):
            steps.append((p2, room))
        # stock: piles over max(reserve, buffer) may be drawn; free bin space may take output (at keep_value)
        draw_cap = stock_cap = keep = 0.0
        if not perish and item not in NOT_STOCK:
            keep = max(reserve, g["buffer_turns"] * use_now.get(item, 0.0))
            draw_cap = max(0.0, held - keep) / g["drain_turns"]
            capy = _n(it.get("capacity"))
            stock_cap = max(0.0, capy - held) / g["drain_turns"] if capy else 0.0
        if item in never_sell:
            steps = []
        # home sales count only up to (1 + sales_growth) x what we really sold a turn (Oct 23 evening: the plan
        # counted ~200 a turn of undercut sales of thread, garments and cloth; offered, they sold nothing). A good we
        # haven't sold counts nothing here: idle piles are offered as trials outside the plan (apply_orders) and
        # count once they sell.
        left = (1.0 + _n(g.get("sales_growth", 0.25))) * avg
        capped = []
        for px_, c_ in steps:
            q_ = min(c_, left)
            if q_ > 1e-6:
                capped.append((px_, q_))
                left -= q_
        steps = capped
        if buy_px and buy_cap > 0:
            # never sell a good for more than we could buy it back: a crossed book (bid over ask) or a stale last
            # price would otherwise read as free arbitrage (buy at the ask, sell at the bid)
            steps = [(min(p_, 0.99 * buy_px), c_) for p_, c_ in steps]
        goods[item] = {"held": held, "cost": cost, "mark": mark, "buy_px": buy_px, "buy_cap": buy_cap,
                       "sell": steps, "draw_cap": draw_cap, "stock_cap": stock_cap, "perishable": perish,
                       "reserve": reserve, "last": last, "traded": traded, "keep": keep}

    # prestige: impacts that no activity of ours explains are fixed (sustenance, legacy drain)
    imp = hh.get("impacts") or {}
    act_recipes = {a.get("recipe") for a in acts if not a.get("alt")}
    fixed_pr = sum(_n(v) for k, v in imp.items() if k not in act_recipes)
    free = _n(hh.get("free"))
    if free >= g["prestige_floor"]:
        pr_min = -(free - g["prestige_floor"]) / g["prestige_horizon"]
    else:
        pr_min = (g["prestige_floor"] - free) / g["prestige_recover_turns"]

    cash = _n(s.get("cash"))
    seen_tax = any((ops.get("producer/%s" % k) or {}).get("tax") is not None for k in taxes)
    tax = sum(taxes.values()) if (taxes and (seen_tax or bdata)) else _n(g["building_tax"])
    ship_running = sum(_n(sh.get("running_cost")) for sh in s.get("ships") or [])
    if cash < g["cash_floor"]:
        cash_min = (g["cash_floor"] - cash) / g["cash_recover_turns"]
    else:
        cash_min = -(cash - g["cash_floor"]) / g["cash_recover_turns"]

    cap = _n((hh.get("caps") or {}).get("regular_management"))
    return {"acts": acts, "groups": groups, "goods": goods, "fixed_supply": fixed_supply, "fixed_demand": fixed_demand,
            "fixed_prestige": fixed_pr, "prestige_min": pr_min, "free_prestige": free,
            "cash": cash, "cash_min": cash_min, "fixed_cost": tax, "taxes": taxes, "ship_running": ship_running,
            "cfg": g, "notes": notes, "tenants_level": _n((hh.get("levels") or {}).get("tenants")),
            "mgmt_cap": cap, "mgmt_used": management_used(s, bdata) if bdata else None}


# ---------------------------------------------------------------- ships

def proven_exports(lines, turns=None, boost=None):
    """{item: units a turn the ships have really sold abroad}: v2 history "exports" (each run's last-turn route flows;
    two runs in one turn count once) over the last `turns` turns, x boost. Oct 23: the plan counted beer 75, thread 55,
    timber 23, cloth 11 and garments 10 a turn of route sales on today's routes while the routes had no such orders
    and had sold beer 463, garments 196, timber 78 in all over 12 days; cash fell ~300 a turn against a planned +360.
    The plan now counts no more route sales of a good than the routes have shown they make."""
    turns = int(turns or EXPORT_PROVEN_TURNS)
    boost = float(boost or EXPORT_PROVEN_BOOST)
    per_turn = {}
    for h in lines or []:
        t = (h or {}).get("turn")
        if t is None:
            continue
        per_turn[int(t)] = (h.get("exports") or {})
    if not per_turn:
        return {}
    last = max(per_turn)
    span = [t for t in per_turn if t > last - turns]
    n = max(1, last - min(span) + 1)
    tot = {}
    for t in span:
        for k, v in per_turn[t].items():
            tot[k] = tot.get(k, 0.0) + _n(v)
    return {k: round(boost * v / n, 2) for k, v in sorted(tot.items()) if v > 0}


def cash_check(goal_hist, v2_hist, turns=3, margin_abs=150.0, margin_share=0.5):
    """Does real cash follow the plan? Each run's prediction for today's settings (goal history cash_today, made
    before a tick) against the real cash change over that tick (v2 history cash, the last run of each turn). Fails
    when the last `turns` ticks together came in more than max(2 x margin_abs, margin_share x |predicted|) under
    them: the goal
    then only cuts (no raises, recipe switches, buy raises or investments) until a tick passes. Oct 23: cash fell
    2.33k -> 1.10k over 4 ticks against a predicted +310..+560 a turn, and the plan kept raising until the kill switch;
    this would have held it after the third tick. Returns {"ok", "why", "ticks": [[turn, predicted, real], ...]}."""
    pred, cash = {}, {}
    for h in goal_hist or []:
        if (h or {}).get("turn") is not None and h.get("cash_today") is not None:
            pred[int(h["turn"])] = _n(h["cash_today"])
    for h in v2_hist or []:
        if (h or {}).get("turn") is not None and h.get("cash") is not None:
            cash[int(h["turn"])] = _n(h["cash"])
    ticks = [[t, round(pred[t - 1], 1), round(cash[t] - cash[t - 1], 1)] for t in sorted(cash)
             if t - 1 in cash and t - 1 in pred]
    last = ticks[-turns:]
    # judged on the sum over the ticks: a single reading moves +-130 with when in the turn it is taken (turn 13502
    # read 948, then 1,077 half an hour later), the sum only carries that noise at its two ends
    p_sum, r_sum = sum(x[1] for x in last), sum(x[2] for x in last)
    if len(last) == turns and r_sum < p_sum - max(margin_abs * 2, margin_share * abs(p_sum)):
        return {"ok": False, "ticks": last,
                "why": "real cash %+.0f over %d ticks against %+.0f planned (%s): cuts only" % (
                    r_sum, turns, p_sum, ", ".join("%+.0f vs %+.0f" % (x[2], x[1]) for x in last))}
    return {"ok": True, "ticks": last, "why": None}


EXPORT_PROVEN_TURNS = 72
EXPORT_PROVEN_BOOST = 1.25


def ship_options(s, M, world, sea, products=None, recipes=None, proven=None, cfg=None):
    """{ship id: {"name", "current": town id or None, "options": {town id: option}}}: for every town a ship can run a
    route to (sea distance within twice the snekkja's range, a market in the world data), what it could sell there
    (95% of their bid, or 90% of their 12-turn average price, as deep as max(bid depth, 30% of what they trade)) and
    buy there (105% of their ask, same depth), for goods in our model. Crew: snekkja recipe cost per turn at crew 1
    (v2/routes.running_cost), moving journey_capacity(moves) cargo units each way per turn at crew 1."""
    import routes
    prods = products if products is not None else routes._products()
    goods = M["goods"]
    by_name = {t.get("name"): t for t in world or []}
    home = str(s.get("home_town") or "")
    cost1 = routes.running_cost(s, recipes)

    def cargo(item):
        p_ = prods.get(item) or {}
        return p_.get("type") == "commodity" if prods else item not in routes.NOT_CARGO

    def size(item):
        return float((prods.get(item) or {}).get("size") or 1)

    import ships as ships_mod
    cf = cfg or {}
    no_out = set((cf.get("chain") or {}).get("intermediates") or []) | set(cf.get("never_drop") or [])
    held = (s.get("store") or {}).get("items") or {}
    stock_goods = set(((cf.get("ship_stock") or {}).get("goods") or {})) if (cf.get("ship_stock") or {}).get("on") else set()
    no_in = set((cf.get("chain") or {}).get("intermediates") or []) | (
        {k for k, it in held.items() if _n(((it or {}).get("flow") or {}).get("production")) > 0} if cfg else set())
    # the route buys only goods we use a unit a turn or more (or ship_stock goods): v2/ships.py's import rule
    use_ok = ({k for k, it in held.items() if _n(((it or {}).get("flow") or {}).get("consumption")) >= 1}
              | stock_goods) if cfg else None
    opts = {}
    for tid, d in (sea or {}).items():
        if tid == home or not d.get("moves"):
            continue
        jcap = routes.journey_capacity(d["moves"])
        t = by_name.get(d.get("name"))
        if jcap <= 0 or not t:
            continue
        out, back = [], []
        for item, raw in (t.get("markets") or {}).items():
            if item not in goods or not cargo(item):
                continue
            m = {k: _n(v) for k, v in routes._mk(raw).items()}
            fare = ships_mod.FARE_PER_SIZE * size(item)
            # the price and the rules of the orders that really go on the route (v2/ships.py): just under the lower of
            # their bid and 103% of their average, only against a live bid, after the route fare; never chain
            # intermediates or never-drop goods out, never goods we make (or intermediates) in
            px = 0.0
            if m["bid"] > 0 and item not in no_out:
                ref = min(m["bid"], m["ema"] * ships_mod.EMA_CAP) if m["ema"] > 0 else m["bid"]
                px = ref * ships_mod.FILL_SHARE - fare
            room = m["sell_room"] if m["sell_room"] >= 1 else 0.0
            if proven is not None:
                room = min(room, _n(proven.get(item)))
            if px > 0 and room > 0:
                out.append((item, px, room, size(item)))
            if m["ask"] > 0 and m["buy_room"] >= 1 and item not in no_in and (use_ok is None or item in use_ok):
                back.append((item, m["ask"] * (1 + routes.SLIP) + fare, m["buy_room"], size(item)))
        if out or back:
            opts[tid] = {"town": tid, "name": d.get("name"), "moves": d["moves"], "jcap": float(jcap),
                         "cost1": cost1, "out": out, "back": back}
    res = {}
    for sh in s.get("ships") or []:
        cur = str(sh.get("route_to")) if sh.get("route_to") else None
        res[str(sh.get("id"))] = {"name": sh.get("name"), "current": cur, "options": opts}
    return res


def _ship_bound(opt, shadow):
    """Upper bound on what a town is worth to one ship at the plan's own item prices (for screening)."""
    per = opt["cost1"] / opt["jcap"]
    b = 0.0
    for item, px, cap, sz in opt["out"]:
        b += max(0.0, px - sz * per - shadow.get(item, 0.0)) * min(cap, opt["jcap"] / sz)
    for item, px, cap, sz in opt["back"]:
        b += max(0.0, shadow.get(item, 0.0) - px - sz * per) * min(cap, opt["jcap"] / sz)
    return b


# ---------------------------------------------------------------- the solver

def solve(M, fix=None, extra_supply=None, prestige_min=None, cash_min=None, ships=None, extra_acts=None):
    """Solve the LP. fix: {activity name: level} pins those activities. ships: route options to include (one per
    ship); None = ships not modelled (today's crew cost counted as fixed). Returns a result dict whose "value" is
    value gained per turn NET of taxes and crew."""
    from scipy.optimize import linprog
    acts = list(M["acts"]) + list(extra_acts or [])
    goods = M["goods"]
    g = M["cfg"]
    fix = fix or {}
    sup = dict(M["fixed_supply"])
    for k, v in (extra_supply or {}).items():
        sup[k] = sup.get(k, 0) + v
    item_names = sorted(goods)
    idx = {k: i for i, k in enumerate(item_names)}
    fixed = M["fixed_cost"] + (M.get("ship_running", 0.0) if ships is None else 0.0)

    cols = []      # (kind, key, step) ; c = objective coefficient (we minimise -value)
    c, lb, ub = [], [], []
    for a in acts:
        cols.append(("act", a["name"], None))
        c.append(0.0)
        if a["name"] in fix:
            v = max(0.0, float(fix[a["name"]]))
            lb.append(v)
            ub.append(v)
        else:
            lb.append(a["lb"])
            ub.append(a["ub"])
    for k in item_names:
        gd = goods[k]
        if gd["buy_cap"] > 0:
            cols.append(("buy", k, None)); c.append(gd["buy_px"]); lb.append(0.0); ub.append(gd["buy_cap"])
        for j, (px, cap) in enumerate(gd["sell"]):
            cols.append(("sell", k, j)); c.append(-px); lb.append(0.0); ub.append(cap)
        if gd["draw_cap"] > 0:
            cols.append(("draw", k, None)); c.append(gd["mark"]); lb.append(0.0); ub.append(gd["draw_cap"])
        if gd["stock_cap"] > 0:
            cols.append(("stock", k, None)); c.append(-g["keep_value"] * gd["mark"]); lb.append(0.0); ub.append(gd["stock_cap"])
        # free disposal of an output nobody takes (waste, worth 0) keeps the balance feasible
        cols.append(("waste", k, None)); c.append(0.0); lb.append(0.0); ub.append(None)
        # a need nothing can supply (household upkeep with no market, or a pinned rate whose inputs can't be had):
        # priced so high it is only used when there is no other way, reported, and charged in the value at twice
        # the good's price, so a starved setting reads worse, never infeasible (Oct 23: today's pinned rates outran
        # their inputs and the whole plan failed)
        cols.append(("short", k, None)); c.append(SHORT_COST); lb.append(0.0); ub.append(None)
    for si, so in enumerate(ships or []):
        for j, (item, px, cap, sz) in enumerate(so["out"]):
            cols.append(("exp", item, (si, j))); c.append(-px); lb.append(0.0); ub.append(cap)
        for j, (item, px, cap, sz) in enumerate(so["back"]):
            cols.append(("imp", item, (si, j))); c.append(px); lb.append(0.0); ub.append(cap)
        cols.append(("crew", so.get("ship"), si)); c.append(so["cost1"]); lb.append(0.0); ub.append(1.0)

    n = len(cols)
    A_eq = [[0.0] * n for _ in item_names]
    b_eq = [0.0] * len(item_names)
    for k in item_names:
        b_eq[idx[k]] = M["fixed_demand"].get(k, 0.0) - sup.get(k, 0.0)
    pr_row = [0.0] * n
    cash_row = [0.0] * n
    extra_ub, extra_b = [], []
    by_name = {a["name"]: a for a in acts}
    group_cols = {}
    ship_rows = {}
    for j, (kind, key, step) in enumerate(cols):
        if kind == "act":
            a = by_name[key]
            for i, q in a["outs"].items():
                if i in idx:
                    A_eq[idx[i]][j] += q
            for i, q in a["ins"].items():
                if i in idx:
                    A_eq[idx[i]][j] -= q
            pr_row[j] = -a["prestige"]          # >= written as <=: -prestige * x <= fixed - min
            if a.get("group"):
                group_cols.setdefault(a["group"], []).append(j)
        elif kind == "buy":
            A_eq[idx[key]][j] += 1.0
            cash_row[j] = goods[key]["buy_px"]  # -cashflow <= -cash_min
        elif kind == "sell":
            A_eq[idx[key]][j] -= 1.0
            cash_row[j] = -goods[key]["sell"][step][0]
        elif kind in ("draw", "short"):
            A_eq[idx[key]][j] += 1.0
        elif kind in ("stock", "waste"):
            A_eq[idx[key]][j] -= 1.0
        elif kind == "exp":
            si, jj = step
            A_eq[idx[key]][j] -= 1.0
            cash_row[j] = -ships[si]["out"][jj][1]
            ship_rows.setdefault((si, "out"), []).append((j, ships[si]["out"][jj][3]))
        elif kind == "imp":
            si, jj = step
            A_eq[idx[key]][j] += 1.0
            cash_row[j] = ships[si]["back"][jj][1]
            ship_rows.setdefault((si, "back"), []).append((j, ships[si]["back"][jj][3]))
        elif kind == "crew":
            cash_row[j] = ships[step]["cost1"]
    # one building runs one recipe at a time: its recipe and the alternatives share its plots
    for grp, js in group_cols.items():
        if len(js) > 1:
            row = [0.0] * n
            for j in js:
                row[j] = 1.0
            extra_ub.append(row)
            extra_b.append(M["groups"].get(grp, max(ub[j] for j in js)))
    # ships carry only what we make or hold (out) and what we use (back), like v2's own route orders (trade mode
    # off): exp(item) <= made + drawn, imp(item) <= used. Without this the plan would buy at home to export, or import
    # to resell at home, which no order of ours carries out.
    if ships:
        exp_cols, imp_cols = {}, {}
        for j, (kind, key, step) in enumerate(cols):
            if kind == "exp":
                exp_cols.setdefault(key, []).append(j)
            elif kind == "imp":
                imp_cols.setdefault(key, []).append(j)
        for item, js in exp_cols.items():
            row = [0.0] * n
            for j in js:
                row[j] = 1.0
            for j, (kind, key, step) in enumerate(cols):
                if kind == "act":
                    row[j] -= by_name[key]["outs"].get(item, 0.0)
                elif kind == "draw" and key == item:
                    row[j] -= 1.0
            extra_ub.append(row)
            extra_b.append(0.0)
        for item, js in imp_cols.items():
            row = [0.0] * n
            for j in js:
                row[j] = 1.0
            for j, (kind, key, step) in enumerate(cols):
                if kind == "act":
                    row[j] -= by_name[key]["ins"].get(item, 0.0)
            extra_ub.append(row)
            extra_b.append(M["fixed_demand"].get(item, 0.0))
    # cargo each way within what the crew level carries: sum(size x units) <= journey capacity x crew
    for (si, side), lst in ship_rows.items():
        row = [0.0] * n
        for j, sz in lst:
            row[j] = sz
        crew_j = next(j for j, col in enumerate(cols) if col[0] == "crew" and col[2] == si)
        row[crew_j] = -ships[si]["jcap"]
        extra_ub.append(row)
        extra_b.append(0.0)

    pmin = M["prestige_min"] if prestige_min is None else prestige_min
    cmin = M["cash_min"] if cash_min is None else cash_min
    relaxed = []

    # The floors are soft: a slack column per floor, priced so high the plan only uses it when nothing else can meet
    # the floor. So an impossible floor still gets as close as it can (never "ignored"), and is reported.
    PEN_P, PEN_C = 10000.0, 100.0
    use_cash = cmin is not None
    ext = 1 + (1 if use_cash else 0)
    cc = list(c) + [PEN_P] + ([PEN_C] if use_cash else [])
    bb = list(zip(lb, ub)) + [(0, None)] * ext
    A_eq2 = [row + [0.0] * ext for row in A_eq]
    A_ub = [pr_row + [-1.0] + ([0.0] if use_cash else [])]       # -prestige - slack <= fixed - min
    b_ub = [M["fixed_prestige"] - pmin]
    if use_cash:
        A_ub.append(cash_row + [0.0, -1.0])                       # -cashflow - slack <= -(min + fixed)
        b_ub.append(-(cmin + fixed))
    for row, bv in zip(extra_ub, extra_b):
        A_ub.append(row + [0.0] * ext)
        b_ub.append(bv)
    res = linprog(cc, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq2, b_eq=b_eq, bounds=bb, method="highs")
    if res.status != 0:
        return {"ok": False, "why": res.message, "relaxed": relaxed}
    sp = res.x[n]
    sc = res.x[n + 1] if use_cash else 0.0
    if sp > 1e-6:
        relaxed.append("prestige floor")
    if sc > 1e-6:
        relaxed.append("cash floor")

    x = res.x[:n]
    levels = {key: x[j] for j, (kind, key, _) in enumerate(cols) if kind == "act"}
    flows, ship_use = {}, {}
    for j, (kind, key, step) in enumerate(cols):
        if kind in ("act",) or x[j] <= 1e-6:
            continue
        if kind == "crew":
            ship_use.setdefault(str(key), {})["crew"] = x[j]
            continue
        f = flows.setdefault(key, {})
        f[kind] = f.get(kind, 0.0) + x[j]
        if kind == "sell":           # the lowest price the plan sells at: the price a home sell order must ask
            px_ = goods[key]["sell"][step][0]
            f["sell_px"] = min(f.get("sell_px", px_), px_)
        if kind in ("exp", "imp"):
            su = ship_use.setdefault(str(ships[step[0]].get("ship")), {})
            su.setdefault(kind, {})[key] = su.get(kind, {}).get(key, 0.0) + x[j]
    value = -sum(c[j] * x[j] for j in range(n) if cols[j][0] != "short") - fixed
    for j, (kind, key, step) in enumerate(cols):
        if kind == "short" and x[j] > 1e-9:
            gd = goods.get(key) or {}
            value -= x[j] * 2.0 * max(gd.get("buy_px") or 0.0, gd.get("last") or 0.0, gd.get("cost") or 0.0, 1.0)
    cashflow = -sum(cash_row[j] * x[j] for j in range(n)) - fixed
    # the same turn in book terms, the way the model check measures real turns (cash + held x home price): stock
    # change = stocked + unsold output - drawn, at the home last price (perishables and services never count)
    book = cashflow
    for j, (kind, key, step) in enumerate(cols):
        if kind in ("stock", "waste", "draw") and x[j] > 1e-9:
            gd = goods.get(key) or {}
            if gd.get("perishable") or key in NOT_STOCK:
                continue
            book += (-1.0 if kind == "draw" else 1.0) * x[j] * (gd.get("last") or 0.0)
    prestige = M["fixed_prestige"] - sum(pr_row[j] * x[j] for j in range(n))
    shadow = {}
    try:
        for k in item_names:
            shadow[k] = res.eqlin.marginals[idx[k]]
        shadow["_prestige"] = -res.ineqlin.marginals[0]
        shadow["_cash"] = -res.ineqlin.marginals[1] if use_cash else 0.0
    except Exception:
        pass
    return {"ok": True, "value": value, "book": book, "levels": levels, "flows": flows, "cashflow": cashflow,
            "prestige_rate": prestige, "shadow": shadow, "relaxed": relaxed, "ships": ship_use, "fixed": fixed,
            "prestige_short": sp}


# ---------------------------------------------------------------- the plan

def _ensure_scipy():
    """The Actions runner has no scipy: install it on first use (~15 s, wheels only). True when importable."""
    try:
        import scipy.optimize  # noqa: F401
        return True
    except ImportError:
        pass
    import subprocess
    import sys
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-q", "--only-binary=:all:", "scipy"],
                       timeout=150, check=False, capture_output=True)
        import importlib
        importlib.invalidate_caches()
        import scipy.optimize  # noqa: F401
        return True
    except Exception:
        return False


def _with_ship(opt, sid):
    o = dict(opt)
    o["ship"] = sid
    return o


def plan_goal(s, cfg, recipes, drip=None, hist=None, buildings_data=None, world=None, sea=None, products=None,
              memory=None, proven=None):
    if not _ensure_scipy():
        return {"ok": False, "why": "scipy not installed and pip install failed"}
    bdata = buildings_data or {}
    cands = new_building_candidates(s, recipes, bdata) if bdata else []
    extra = set()
    for _, _, r in cands:
        i_, o_ = _recipe_io(r)
        extra |= set(i_) | set(o_)
    for t, _, _ in cands:
        extra |= set(((bdata.get(t) or {}).get("construction") or {}).get("materials") or {})
    M = build_model(s, cfg, recipes, drip=drip, hist=hist, buildings_data=bdata, extra_items=extra, memory=memory)
    g = M["cfg"]

    def ok_like(r, ref):
        """r keeps every limit ref keeps, and never sinks further under a prestige floor ref already misses: value
        leaves the floor's slack out, so without this a broken floor made prestige worth 0 to trims and builds
        (Oct 28: the park, +8 prestige/turn, scored +379/turn to donate with the floor already broken)."""
        if not (bool(r.get("ok")) and set(r.get("relaxed") or []) <= set(ref.get("relaxed") or [])):
            return False
        return _n(r.get("prestige_short")) <= _n(ref.get("prestige_short")) + 0.05

    # ---- ships: today's routes, then each ship's best town (screened by the plan's own prices, then re-solved)
    sopt = ship_options(s, M, world, sea, products, recipes, proven=proven, cfg=cfg) if (world and sea) else None
    cur_ships, chosen, ship_moves = None, {}, []
    if sopt is not None:
        cur_ships = [_with_ship(v["options"][v["current"]], sid) for sid, v in sorted(sopt.items())
                     if v["current"] and v["current"] in v["options"]]
        base = solve(M, ships=[])
        sh0 = base.get("shadow") or {}
        for sid, v in sorted(sopt.items()):
            others = [_with_ship(sopt[s2]["options"][t2], s2) for s2, t2 in chosen.items() if t2]
            ref = solve(M, ships=others)
            if not ref.get("ok"):           # the solver failed on this base: keep the ship where it is
                chosen[sid] = v["current"] if v["current"] in v["options"] else None
                ship_moves.append({"ship": sid, "name": v["name"], "current": v["current"],
                                   "current_name": (v["options"].get(v["current"]) or {}).get("name") or v["current"],
                                   "town": chosen[sid], "town_name": (v["options"].get(chosen[sid] or "") or {}).get("name"),
                                   "worth": None, "gain_over_current": None, "note": "solver failed: kept"})
                continue
            scored = sorted(v["options"].values(), key=lambda o: -_ship_bound(o, sh0))
            look = [o for o in scored[:int(g.get("ship_screen", 8))]]
            if v["current"] and v["current"] in v["options"] and v["options"][v["current"]] not in look:
                look.append(v["options"][v["current"]])
            best, best_r = None, ref
            for o in look:
                if o["town"] in chosen.values():
                    continue                    # two ships never share a town (they would undercut each other)
                r = solve(M, ships=others + [_with_ship(o, sid)])
                if ok_like(r, ref) and r["value"] > best_r["value"] + 1e-6:
                    best, best_r = o, r
            chosen[sid] = best["town"] if best else None
            gain_now = None
            if v["current"] and v["current"] in v["options"]:
                rc = solve(M, ships=others + [_with_ship(v["options"][v["current"]], sid)])
                gain_now = (best_r["value"] - rc["value"]) if rc.get("ok") else None
            ship_moves.append({"ship": sid, "name": v["name"], "current": v["current"],
                               "current_name": (v["options"].get(v["current"]) or {}).get("name") or v["current"],
                               "town": chosen[sid], "town_name": (best or {}).get("name"),
                               "worth": best_r["value"] - ref["value"], "gain_over_current": gain_now})
    if sopt is not None and not solve(M, ships=[_with_ship(sopt[sid]["options"][t], sid)
                                                for sid, t in sorted(chosen.items()) if t]).get("ok"):
        chosen = {sid: None for sid in chosen}        # the joint ship plan won't solve: plan without ships
    # Production is planned on the routes the ships really run today. The towns chosen above only decide the pins;
    # once a ship is on its new route, the next run plans on it. (Oct 23: planning rates on routes the ships hadn't
    # sailed yet raised the spinnery and flax for thread exports that weren't happening; thread piled up and cash fell.)
    plan_ships = cur_ships
    chosen_ships = [_with_ship(sopt[sid]["options"][t], sid) for sid, t in sorted(chosen.items()) if t] if sopt else None

    # one recipe per building: the LP may split a building's plots between recipes; keep its main recipe and the
    # best alternative, and run only the one with more plots (the other is pinned to 0 in the plan)
    opt0 = solve(M, ships=plan_ships)
    if not opt0["ok"]:
        return {"ok": False, "why": "no feasible plan: %s" % opt0.get("why")}
    keep, off = [], {}
    for a in M["acts"]:
        if not a.get("group"):
            keep.append(a)
    for grp in M["groups"]:
        acts_g = [a for a in M["acts"] if a.get("group") == grp]
        main = next((a for a in acts_g if not a.get("alt")), None)
        alts = sorted([a for a in acts_g if a.get("alt")], key=lambda a: -opt0["levels"].get(a["name"], 0.0))
        best_alt = alts[0] if alts and opt0["levels"].get(alts[0]["name"], 0.0) > 1e-6 else None
        pair = [x for x in (main, best_alt) if x is not None]
        if not pair:
            pair = alts[:1]
        keep.extend(pair)
        if len(pair) == 2:
            lo = min(pair, key=lambda a: (opt0["levels"].get(a["name"], 0.0), a is main))
            off[lo["name"]] = 0.0
    M_all = M                   # every recipe still open: what the chosen ship towns would carry (information)
    M = dict(M, acts=keep)
    M_run = dict(M, acts=[dict(a, ub=0.0) if a["name"] in off else a for a in M["acts"]])
    opt = solve(M_run, ships=plan_ships)
    if not opt["ok"]:
        return {"ok": False, "why": "no feasible plan: %s" % opt.get("why")}
    M = M_run                   # pins below set both bounds, so today's levels still price correctly
    cur_fix = {a["name"]: a["cur"] for a in M["acts"]}

    def free(fix, ships):   # value with the levels pinned and the limits set aside: like-for-like comparisons
        return solve(M, fix=fix, prestige_min=-1e9, cash_min=None, ships=ships)

    cur = free(cur_fix, cur_ships)                    # what today's settings earn
    cur_lim = solve(M, fix=cur_fix, ships=cur_ships)  # ... and which limits they break
    breaks = cur_lim.get("relaxed") if cur_lim.get("ok") else ["no feasible flow"]
    now_flows = (cur_lim if cur_lim.get("ok") else cur).get("flows") or {}

    # changes, priced one at a time on top of each other (best first), so the gains add up to plan - today.
    changes = []
    base_r = cur
    if sopt is not None:
        applied_sh = {str(x["ship"]): x for x in (cur_ships or [])}
        for mv in ship_moves:
            if mv["town"] == mv["current"]:
                continue
            if mv["town"]:
                applied_sh[mv["ship"]] = _with_ship(sopt[mv["ship"]]["options"][mv["town"]], mv["ship"])
            else:
                applied_sh.pop(mv["ship"], None)
            r = free(cur_fix, list(applied_sh.values()))
            changes.append({"name": "%s -> %s" % (mv["name"], mv["town_name"] or "no route"), "kind": "ship",
                            "ship": mv["ship"], "from": mv["current"], "to": mv["town"],
                            "gain": (r["value"] - base_r["value"]) if (r.get("ok") and base_r.get("ok")) else None})
            if r.get("ok"):
                base_r = r
        base_r = cur            # rates are planned on today's routes: their attribution starts from today
    pending = [a for a in M["acts"] if abs(opt["levels"].get(a["name"], 0.0) - a["cur"]) >= g["change_min"]]
    applied = dict(cur_fix)
    while pending and base_r.get("ok"):
        best = None
        for a in pending:
            trial = dict(applied)
            trial[a["name"]] = opt["levels"][a["name"]]
            r = free(trial, plan_ships)
            if r.get("ok") and (best is None or r["value"] - base_r["value"] > best[2]):
                best = (a, r, r["value"] - base_r["value"])
        if best is None:
            break
        a, r, gain = best
        applied[a["name"]] = opt["levels"][a["name"]]
        base_r = r
        pending.remove(a)
        changes.append({"name": a["name"], "id": a.get("id"), "kind": a["kind"], "recipe": a.get("recipe"),
                        "from": round(a["cur"], 3), "to": round(opt["levels"][a["name"]], 3), "gain": gain})

    # the plan per building: the recipe it gives most plots, its target, and what switching recipe is worth
    bplan = {}
    for grp in M["groups"]:
        acts_g = [a for a in M["acts"] if a.get("group") == grp]
        top = max(acts_g, key=lambda a: (opt["levels"].get(a["name"], 0.0), not a.get("alt")))
        main = next((a for a in acts_g if not a.get("alt")), None)
        lvl = opt["levels"].get(top["name"], 0.0)
        e = {"id": grp, "name": (main or top)["name"].split(" [")[0], "recipe": top["recipe"], "target": round(lvl, 3),
             "cur_recipe": main["recipe"] if main else None, "cur": round(main["cur"], 3) if main else 0.0}
        if main and top is not main and lvl > 1e-3:
            M2 = dict(M, acts=[a for a in M["acts"] if not (a.get("group") == grp and a.get("alt"))])
            r = solve(M2, ships=plan_ships)
            e["switch_gain"] = (opt["value"] - r["value"]) if r.get("ok") else None
        bplan[grp] = e

    # ---- investments and trims, each priced by re-solving under the same limits (value is net of tax)
    inv = []
    lvl = int(M["tenants_level"]) + 1
    t_cost = 50 * (lvl - 3)          # 450 for L12, 500 for L13 (game prices seen Oct 22)
    left = M["free_prestige"] - t_cost
    M_t = dict(M)
    M_t["prestige_min"] = -(left - g["prestige_floor"]) / g["prestige_horizon"] if left >= g["prestige_floor"] else M["prestige_min"]
    tl = solve(M_t, extra_supply={"labour": g["tenants_labour"]}, ships=plan_ships)
    if ok_like(tl, opt):
        inv.append({"kind": "tenants", "what": "Tenants L%d" % lvl, "cost": "%d prestige" % t_cost,
                    "gain": tl["value"] - opt["value"], "pays": left >= g["prestige_floor"],
                    "note": ("free after %.0f" % left) if left >= g["prestige_floor"] else
                            "waits until %.0f free (keeps %d after)" % (t_cost + g["prestige_floor"], g["prestige_floor"])})
    room = (M["mgmt_cap"] - M["mgmt_used"]) if M.get("mgmt_used") is not None and M.get("mgmt_cap") else None
    owned_types = {b.get("type") for b in s.get("buildings") or []}
    # +1 plot of a building the plan runs flat out
    for grp, cap_ in M["groups"].items():
        acts_g = [a for a in M["acts"] if a.get("group") == grp]
        if sum(opt["levels"].get(a["name"], 0.0) for a in acts_g) < cap_ - 1e-6:
            continue
        a0 = acts_g[0]
        if a0["type"] in (g.get("max_target") or {}):
            continue
        most = _n(((bdata.get(a0["type"]) or {}).get("construction") or {}).get("size"))
        if most and a0["size"] >= most:
            continue                  # already at the most plots the building type allows
        need = mgmt_per_plot(a0["type"], bdata) if not is_prestige_building(a0["type"], bdata) else 0.0
        if room is not None and need > room + 1e-9:
            continue
        M2 = dict(M, groups=dict(M["groups"], **{grp: cap_ + 1}),
                  acts=[dict(x, ub=x["ub"] + 1) if x.get("group") == grp else x for x in M["acts"]])
        r = solve(M2, ships=plan_ships)
        if not ok_like(r, opt):
            continue
        gain = r["value"] - opt["value"] - plot_tax_rate(a0["type"], bdata)
        if gain <= 0.5:
            continue
        cost = materials_cost(a0["type"], bdata, M["goods"])
        thin = materials_thin(a0["type"], bdata, M["goods"])
        inv.append({"kind": "plot", "building": grp, "what": "+1 plot %s" % a0["name"].split(" [")[0],
                    "cost": "~%.0f coin" % cost, "coin": cost, "gain": gain, "mgmt": need,
                    "payback": cost / gain, "pays": cost / gain <= g["invest_horizon"] and not thin,
                    "note": ("materials thin at home: %s" % ", ".join(thin)) if thin else None})
    # new buildings: each type's best recipe as a one-plot building (screened at the plan's prices first)
    sh = opt["shadow"]
    scored = []
    for t, rn, r_ in cands:
        i_, o_ = _recipe_io(r_)
        margin = sum(q * sh.get(k, 0.0) for k, q in o_.items()) - sum(q * sh.get(k, 0.0) for k, q in i_.items())
        if margin > plot_tax_rate(t, bdata):
            scored.append((margin, t, rn, r_))
    best_new = {}
    for margin, t, rn, r_ in sorted(scored, reverse=True)[:int(g.get("new_screen", 12))]:
        i_, o_ = _recipe_io(r_)
        act = {"name": "new %s [%s]" % (t, rn), "kind": "new", "type": t, "recipe": rn, "ins": i_, "outs": o_,
               "prestige": _n(r_.get("prestige")), "lb": 0.0, "ub": 1.0, "cur": 0.0}
        r = solve(M, ships=plan_ships, extra_acts=[act])
        if not ok_like(r, opt):
            continue
        gain = r["value"] - opt["value"] - plot_tax_rate(t, bdata)
        if gain > 0.5 and gain > best_new.get(t, (0,))[0]:
            best_new[t] = (gain, rn)
    plot_types = {next((a["type"] for a in M["acts"] if a.get("group") == d["building"]), None)
                  for d in inv if d.get("kind") == "plot"}
    for t, (gain, rn) in best_new.items():
        if t in owned_types:
            most = _n(((bdata.get(t) or {}).get("construction") or {}).get("size"))
            sizes = [_n(b.get("size")) for b in s.get("buildings") or [] if b.get("type") == t]
            if t in plot_types or (most and sizes and min(sizes) < most):
                continue            # growing the one we have is cheaper on management than a second building
        need = 0.5 if t in owned_types else 1.0
        cost = materials_cost(t, bdata, M["goods"])
        fits = room is None or need <= room + 1e-9
        thin = materials_thin(t, bdata, M["goods"])
        inv.append({"kind": "build", "type": t, "recipe": rn, "what": "new %s (%s)" % (t, rn),
                    "cost": "~%.0f coin" % cost, "coin": cost, "gain": gain, "mgmt": need,
                    "payback": cost / gain if gain > 0 else None,
                    "pays": bool(fits and not thin and cost / gain <= g["invest_horizon"]),
                    "note": ("no management room (%.2f free, needs %.1f)" % (room or 0, need)) if not fits else
                            ("materials thin at home: %s" % ", ".join(thin)) if thin else None})
    inv.sort(key=lambda d: -(d["gain"] or 0))
    # trims: a building whose removal (its plots idle AND its tax gone) beats keeping it
    trims = []
    for grp in M["groups"]:
        acts_g = [a for a in M["acts"] if a.get("group") == grp]
        tax_b = M["taxes"].get(grp, 0.0)
        M2 = dict(M, fixed_cost=M["fixed_cost"] - tax_b,
                  acts=[dict(x, ub=0.0) if x.get("group") == grp else x for x in M["acts"]])
        r = solve(M2, ships=plan_ships)
        if not ok_like(r, opt):
            continue
        gain = r["value"] - opt["value"]
        if gain >= g.get("trim_min", 5.0):
            trims.append({"kind": "donate", "building": grp, "what": "donate %s" % acts_g[0]["name"].split(" [")[0],
                          "type": acts_g[0]["type"], "gain": gain, "tax": tax_b})
    trims.sort(key=lambda d: -d["gain"])

    hist = hist or []
    trend = value_trend(hist, set((cfg or {}).get("perishable") or [])) if hist else {}
    keys = ["labour", "thread", "cloth", "flax fibres", "garments", "nets", "beer", "timber"]
    return {
        "ok": True, "goal": "business value", "turn": s.get("turn"), "t": s.get("t"),
        "value_now": trend.get("now"), "trend": trend,
        "plan_value": opt["value"], "current_value": cur.get("value") if cur.get("ok") else None,
        "plan_free": (free({k: v for k, v in opt["levels"].items()}, plan_ships) or {}).get("value"),
        "current_breaks": breaks,
        "plan_cashflow": opt["cashflow"], "current_cashflow": cur.get("cashflow"),
        "current_book": cur_lim.get("book") if cur_lim.get("ok") else cur.get("book"),
        "buy": {k: round(v.get("buy", 0), 2) for k, v in opt["flows"].items() if v.get("buy")},
        # buys and sells for the rates that run today (the 'buys'/'sells' jobs use these: rates move in steps,
        # so orders follow the real targets, not the plan's end state)
        "orders_now": {"buy": {k: round(v.get("buy", 0), 2) for k, v in now_flows.items() if v.get("buy")},
                       "sell": {k: round(v.get("sell", 0), 2) for k, v in now_flows.items() if v.get("sell")}},
        "sell": {k: round(v.get("sell", 0), 2) for k, v in opt["flows"].items() if v.get("sell")},
        "plan_prestige_rate": opt["prestige_rate"], "current_prestige_rate": cur.get("prestige_rate"),
        "prestige_min": M["prestige_min"], "cash_min": M["cash_min"], "fixed_cost": opt.get("fixed"),
        "relaxed": opt["relaxed"], "levels": {k: round(v, 3) for k, v in opt["levels"].items()},
        "changes": changes, "buildings": bplan, "investments": inv, "trims": trims,
        "route_proven": proven,
        "buy_px": {k: round(_n((M["goods"].get(k) or {}).get("buy_px")), 3) for k, v in now_flows.items() if v.get("buy")},
        "sell_px": {k: round(_n(v.get("sell_px")), 3) for k, v in now_flows.items() if v.get("sell")},
        "idle": idle_piles(M, s, cfg, now_flows),
        "sell_keep": {k: round(_n((M["goods"].get(k) or {}).get("keep")), 1) for k, v in now_flows.items() if v.get("sell")},
        "ships": ship_moves, "ship_plan": {k: {kk: (round(vv, 2) if isinstance(vv, float) else
                                                    {i: round(q, 1) for i, q in vv.items()}) for kk, vv in v.items()}
                                           for k, v in ((solve(M_all, ships=chosen_ships) if chosen_ships else opt)
                                                        .get("ships") or {}).items()},
        "mgmt": {"cap": M.get("mgmt_cap"), "used": M.get("mgmt_used")},
        "short": {k: round(v["short"], 2) for k, v in opt["flows"].items() if v.get("short")},
        "shadow": {k: round(sh[k], 3) for k in keys + ["_prestige", "_cash"] if k in sh},
        "flows": {k: {kk: round(vv, 2) for kk, vv in v.items()} for k, v in opt["flows"].items()},
    }


def report_lines(G):
    if not G:
        return []
    lj = [j for j, v in (G or {}).get("live_jobs", {}).items() if v] if G else []
    out = ["## Goal: business value (%s)" % (("live: " + ", ".join(lj)) if lj else "shadow")]
    if not G.get("ok"):
        return out + ["- no plan: %s" % G.get("why")]
    tr = G.get("trend") or {}
    sc = G.get("scorecard")
    if G.get("value_now") is not None:
        bits = ["%s/turn over %d turns" % ("%+.0f" % tr["per_turn_%d" % n], n) for n in (6, 24) if ("per_turn_%d" % n) in tr]
        out.append("- Value now %.1fk (cash + stock at home prices); %s." % (G["value_now"] / 1000, ", ".join(bits) or "no trend yet"))
    cv, pv = G.get("current_value"), G.get("plan_value")
    out.append("- Limits: cash flow >= %+.0f/turn, prestige >= %+.2f/turn (values are after %.0f tax a turn)." % (
        G["cash_min"], G["prestige_min"], G.get("fixed_cost") or 0))
    if cv is not None:
        br = G.get("current_breaks") or []
        out.append("- Today's settings: value %+.0f/turn, cash %+.0f/turn, prestige %+.2f/turn%s." % (
            cv, G.get("current_cashflow") or 0, G.get("current_prestige_rate") or 0,
            (" - breaks the %s" % " and ".join(br)) if br else ""))
    out.append("- Plan: value %+.0f/turn, cash %+.0f/turn, prestige %+.2f/turn%s." % (
        pv, G["plan_cashflow"], G["plan_prestige_rate"],
        (" - could not meet the %s" % " and ".join(G["relaxed"])) if G.get("relaxed") else ", inside both limits"))
    cc = G.get("cash_check") or {}
    if cc.get("ticks"):
        out.append("- Cash check (real vs predicted cash a tick, last %d): %s%s." % (
            len(cc["ticks"]), ", ".join("%+.0f vs %+.0f" % (x[2], x[1]) for x in cc["ticks"]),
            "" if cc.get("ok", True) else " - FAILED: the goal only cuts until a tick passes"))
    if G.get("route_proven") is not None:
        rp = G["route_proven"] or {}
        out.append("- Route sales counted at most (what the ships really sold, a turn): %s." % (
            ", ".join("%s %.1f" % kv for kv in sorted(rp.items())) or "none"))
    if G.get("changes"):
        out.append("- Changes, each priced on top of the one before (value/turn, limits aside):")
        for ch in G["changes"][:10]:
            g_ = "%+.0f/turn" % ch["gain"] if ch.get("gain") is not None else "not comparable"
            if ch.get("group"):
                out.append("  - together: %s: %s" % (", ".join("%s %.2f -> %.2f" % (x["name"], x["from"], x["to"])
                                                            for x in ch["group"]), g_))
            elif ch.get("kind") == "ship":
                out.append("  - ship %s: %s" % (ch["name"], g_))
            else:
                out.append("  - %s %.2f -> %.2f: %s" % (ch["name"], ch["from"], ch["to"], g_))
    else:
        out.append("- No building changes: today's rates are the plan's.")
    if G.get("promoted"):
        out.append("- HAND-OVER: %s." % G["promoted"])
    if sc:
        out.append("- Model check over the last %d turns: predicted %+.0f/turn for the settings we ran, real %+.0f/turn%s." % (
            sc["turns"], sc["predicted"], sc["real"],
            "" if abs(sc["predicted"] - sc["real"]) <= max(40.0, 0.5 * abs(sc["real"])) else " - OFF, trust the plan less"))
    else:
        out.append("- Model check: not enough runs yet (needs 6 turns of goal history).")
    sh = G.get("shadow") or {}
    if sh:
        out.append("- Worth of one more unit per turn: " + ", ".join(
            "%s %.2f" % (k.strip("_"), v) for k, v in sh.items()))
    go = G.get("goal_orders") or {}
    if go:
        diffs = []
        for item, d in sorted(go.items()):
            for side in ("buy", "sell"):
                k = side + "_volume"
                if k in d and d[k] != d.get("v2_" + k):
                    diffs.append("%s %s %s (v2 %s)" % (item, side, d[k], d.get("v2_" + k, "none")))
        if diffs:
            out.append("- Orders it would set%s: %s" % (
                "" if G.get("orders_live") else " (dry run)", "; ".join(diffs[:10])))
    sw = [b for b in (G.get("buildings") or {}).values() if b.get("recipe") != b.get("cur_recipe") and b.get("target", 0) > 0]
    for b in sw:
        out.append("- Recipe: %s %s -> %s at %.2f%s." % (b["name"], b.get("cur_recipe") or "(idle)", b["recipe"], b["target"],
                                                        (", worth %+.0f/turn" % b["switch_gain"]) if b.get("switch_gain") is not None else ""))
    for m in G.get("ships") or []:
        if m.get("town") != m.get("current"):
            out.append("- Ship %s: %s -> %s (%s/turn over staying)." % (
                m["name"], m.get("current_name") or "no route", m.get("town_name") or "no route",
                "%+.0f" % m["gain_over_current"] if m.get("gain_over_current") is not None else "?"))
        elif m.get("town"):
            out.append("- Ship %s: stays on %s (worth %+.0f/turn)." % (m["name"], m.get("town_name"), m.get("worth") or 0))
    if G.get("short"):
        out.append("- UNMET needs (no market or stock for them): %s." % ", ".join("%s %.1f" % kv for kv in G["short"].items()))
    mg = G.get("mgmt") or {}
    if mg.get("cap"):
        out.append("- Management: ~%.2f of %.0f used." % (mg.get("used") or 0, mg["cap"]))
    if G.get("investments"):
        out.append("- Investments:")
        for d in G["investments"][:6]:
            pb = (", payback %.0f turns" % d["payback"]) if d.get("payback") else ""
            out.append("  - %s for %s: %+.0f/turn%s%s%s" % (d["what"], d["cost"], d["gain"], pb,
                                                         "" if d.get("pays", True) else ", doesn't pay yet",
                                                         (" (%s)" % d["note"]) if d.get("note") else ""))
    for t in (G.get("trims") or [])[:4]:
        out.append("- Trim: %s: %+.0f/turn (tax %.0f saved)." % (t["what"], t["gain"], t["tax"]))
    return out


# ---------------------------------------------------------------- its own scorecard

def history_line(G):
    """One compact line per run for state/v2/goal_history.jsonl."""
    if not G or not G.get("ok"):
        return {"t": (G or {}).get("t"), "ok": False, "why": (G or {}).get("why")}
    return {"t": G.get("t"), "turn": G.get("turn"), "ok": True, "value_now": G.get("value_now"),
            "pred_today": G.get("current_value"), "pred_plan": G["plan_value"], "pred_book": G.get("current_book"), "cash_today": G.get("current_cashflow"), "cash_plan": G.get("plan_cashflow"),
            "levels": G.get("levels"), "live": G.get("live_jobs"),
            "check": None if not G.get("scorecard") else (abs(G["scorecard"]["predicted"] - G["scorecard"]["real"])
                                                         <= max(40.0, 0.5 * abs(G["scorecard"]["real"])))}


def scorecard(goal_hist, hist, perishable=(), min_turns=6):
    """Did the model's 'today's settings earn X/turn' match what really happened? Compares the mean prediction of
    the runs since a past turn with the real change in business value since that turn."""
    # book-value predictions only (Oct 23): what today's settings add to cash + stock at home prices, the same
    # measure as the real side; older rows predicted the model's own value (stock marked down) and don't compare
    rows = [r for r in goal_hist if r.get("ok") and r.get("pred_book") is not None and r.get("turn") is not None]
    if not rows or not hist:
        return None
    now = hist[-1]
    t_now = now.get("turn")
    by_turn = {r.get("turn"): r for r in hist}
    for back in (24, 12, min_turns):
        # the oldest run the history still holds: once goal history outgrew the 60-turn window (Oct 26) the oldest
        # run had no history row, every window was skipped and the check (and the brake on raises) went silent
        start = next((r for r in rows if t_now - r["turn"] >= back and r["turn"] in by_turn), None)
        if start is None:
            continue
        span = [r for r in rows if r["turn"] >= start["turn"]]
        pred = sum(r["pred_book"] for r in span) / len(span)
        real = (value_of(now, perishable)[0] - value_of(by_turn[start["turn"]], perishable)[0]) / (t_now - start["turn"])
        return {"turns": t_now - start["turn"], "predicted": pred, "real": real, "runs": len(span)}
    return None


# ---------------------------------------------------------------- orders (the 'buys' and 'sells' jobs)

def idle_piles(M, s, cfg, flows):
    """Stock over what we keep that the plan doesn't sell: {item: {excess, keep, last, ask}}. Offered as trials
    (apply_orders), never counted in the plan until it sells."""
    never = set((cfg or {}).get("never_drop") or [])
    mk = s.get("market") or {}
    out = {}
    for item, gd in (M.get("goods") or {}).items():
        if gd.get("perishable") or item in NOT_STOCK or item in never or (flows.get(item) or {}).get("sell"):
            continue
        keep = max(_n(gd.get("keep")), _n(gd.get("reserve")))
        excess = _n(gd.get("held")) - keep
        m = mk.get(item) or {}
        if excess >= 5 and _n(m.get("price")) > 0:
            out[item] = {"excess": round(excess, 1), "keep": round(keep, 1), "last": _n(m.get("price")),
                         "ask": _n(m.get("ask"))}
    return out


def apply_orders(G, plan, cfg, snap=None, prev_sells=()):
    """Put the goal planner's volumes into v2's planned orders for the jobs that are live; v2 keeps prices, tiers
    and the write/verify path (act.py). Returns ({item: volumes it wants vs v2's}, any job live).
    buys: perishables only (labour, porterage, fish, meat): bought to exactly what today's rates use, whole units up.
    sells: every item the plan sells at home: sell_volume raised to what the plan sells when that is more than v2
           offers (drawing a pile down faster); never cut, since a sell order only caps what buyers can take."""
    import math
    if not G or not G.get("ok"):
        return {}, False
    import goal_switch
    live = {j: goal_switch.owns(j, cfg) for j in ("buys", "sells")}
    orders = plan.setdefault("orders", {})
    now = G.get("orders_now") or {}
    per = set(cfg.get("perishable") or []) | {"labour"}
    out = {}
    for item in sorted(per):
        want = int(math.ceil(_n((now.get("buy") or {}).get(item)) - 1e-6))
        o = (orders.get(item) or {}).get("buy")
        d = out.setdefault(item, {})
        d["buy_volume"] = want
        d["v2_buy_volume"] = (o or {}).get("buy_volume")
        if live["buys"] and o is not None:
            o["buy_volume"] = want
            orders[item]["why"] = "goal planner: buys %d for today's rates (v2 had %s)" % (want, d["v2_buy_volume"])
    # every other input today's rates buy (Oct 23: the net maker made 0 for want of wax, which v1 never bought and
    # v2 didn't own): v2's buy is kept and only raised to what the rates use; with none, one is made at the home ask
    # (+2%, on the price grid), keeping up to 4 turns of use. Marked goal_buy: v2's actor owns the item and its
    # ceiling is that price, and every v1 writer stands aside (v2_owned).
    pxs = G.get("buy_px") or {}
    plan_buy = G.get("buy") or {}
    for item, v in sorted((now.get("buy") or {}).items()):
        # what today's rates need and the plan still wants (a rate on its way down doesn't stock up)
        v = min(_n(v), _n(plan_buy.get(item)))
        if item in per or v <= 0:
            continue
        want = int(math.ceil(v - 1e-6))
        reserve = max(_n(((cfg.get("goal") or {}).get("reserve") or {}).get(item)),
                      _n((cfg.get("stockpiles") or {}).get(item)))
        keep = max(want, int(math.ceil(4 * v - 1e-6)), int(math.ceil(reserve - 1e-6)))
        ent = orders.setdefault(item, {})
        o = ent.get("effective_buy") or ent.get("buy")
        d = out.setdefault(item, {})
        d["buy_volume"] = want
        d["v2_buy_volume"] = (o or {}).get("buy_volume")
        if not live["buys"]:
            continue
        cut_only = (G.get("cash_check") or {}).get("ok") is False   # failing cash check: buys may only shrink
        # ...except an input a building is stopped for right now (Oct 24, turn 13514: the net maker switched to nets 3
        # at 07:35, the cash check failed the next run, and varnish was never bought: production 0, limitation varnish).
        # Buying what today's rate already uses is not a raise.
        starving = any(b.get("limitation") == item and _n(b.get("target")) > 0
                       for b in ((snap or {}).get("buildings") or []))
        live_tiers_ = (((snap or {}).get("store") or {}).get("items") or {}).get(item, {}).get("orders") or []
        live_buy_ = any(_n(t.get("buy_volume")) > 0 for t in live_tiers_)
        if cut_only and starving and not live_buy_:
            px = _n(pxs.get(item))
            if px > 0:
                import planner as _pl
                o = ent["buy"] = {"buy_volume": want, "buy_price": "%g" % _pl.snap_price(px * 1.02, up=True),
                                  "max_holding": keep}
                ent.pop("effective_buy", None)
                ent.pop("buy_off", None)
                if any(_n(t.get("sell_volume")) > 0 for t in live_tiers_):
                    ent["sell"] = "off"          # a leftover sell would sell the input back (varnish 2 @ 15.8)
                ent["goal_buy"] = {"buy_price": o.get("buy_price"), "starving": True}
                ent["why"] = "goal planner: %s stops a building now - buys %s a turn, keeps up to %s (cuts only)" % (
                    item, want, keep)
            continue
        if cut_only and (not o or (want >= _n(o.get("buy_volume")) and (o.get("max_holding") is not None
                                                                        and keep >= _n(o.get("max_holding"))))):
            continue
        if not o:
            px = _n(pxs.get(item))
            if px <= 0:
                continue
            import planner as _pl
            o = ent["buy"] = {"buy_volume": want, "buy_price": "%g" % _pl.snap_price(px * 1.02, up=True),
                              "max_holding": keep}
            ent.pop("buy_off", None)
        else:
            # the plan's volume, and up to 4 turns of its use in stock (Oct 23: v2's runway rule bought grain 104 a
            # turn up to 260 held while the rates used 65)
            if cut_only:
                o["buy_volume"] = min(want, int(_n(o.get("buy_volume"))))
                o["max_holding"] = keep if o.get("max_holding") is None else min(keep, int(_n(o.get("max_holding"))))
            else:
                o["buy_volume"] = want
                o["max_holding"] = keep
        ent["goal_buy"] = {"buy_price": o.get("buy_price")}
        ent["why"] = "goal planner: buys %s a turn for today's rates, keeps up to %s (v2 had %s)" % (
            o["buy_volume"], o.get("max_holding"), d["v2_buy_volume"])
    # goods the plan sells at home that nobody offers (Oct 23, turn 13502: thread 15, flax fibres 6.6 a turn in the
    # plan, no sell order, 0 sold; ~110 coin a turn of plan that never happened): a sell at the plan's own lowest
    # price (on the grid, rounded down), keeping the plan's stock floor, ramping at most 2x+10 a run (v2's rule).
    # Marked goal_sell: v2's actor owns the item. Never for never-drop goods or goods with a live buy (no buying and
    # selling one good at once), nor goods someone else sells with success.
    store_items = ((snap or {}).get("store") or {}).get("items") or {}
    never = set(cfg.get("never_drop") or [])
    for item, v in sorted((now.get("sell") or {}).items()):
        ent = orders.setdefault(item, {})
        if ent.get("sell") is not None or _n(v) < 0.5 or item in never or not live["sells"]:
            continue
        b_ = ent.get("effective_buy") or ent.get("buy")
        tiers = (store_items.get(item) or {}).get("orders") or []
        held_ = _n((store_items.get(item) or {}).get("held"))
        live_buy = any(_n(t.get("buy_volume")) > 0 and (t.get("max_holding") is None or _n(t["max_holding"]) > held_)
                       for t in tiers)   # a buy capped under what we hold buys nothing (cloth: max 4, 45 held)
        if (b_ and _n(b_.get("buy_volume")) > 0) or live_buy:
            continue
        sold_last = _n(((store_items.get(item) or {}).get("flow") or {}).get("sale"))
        if any(_n(t.get("sell_volume")) > 0 for t in tiers) and item not in set(prev_sells or ()) and sold_last > 0:
            continue                 # someone else offers it and it sells (timber: v1 sells 20 a turn over its 350)
                                     # - an offer that sold nothing (garments 35 at 20.0 over a 19.5 town) is taken over
        px = _n((G.get("sell_px") or {}).get(item))
        if px <= 0:
            continue
        import planner as _pl
        keep = int(math.ceil(_n((G.get("sell_keep") or {}).get(item)) - 1e-6))
        live_sell = max([_n(t.get("sell_volume")) for t in ((store_items.get(item) or {}).get("orders") or [])] + [0])
        ent["sell"] = {"sell_volume": int(min(2 * live_sell + 10, math.ceil(_n(v) - 1e-6))),
                       "sell_price": "%g" % _pl.snap_price(px, up=False), "min_holding": keep}
        ent["goal_sell"] = {"sell_price": ent["sell"]["sell_price"]}
        if any(_n(t.get("buy_volume")) > 0 for t in tiers):
            ent["buy_off"] = "goal planner sells it: a dormant buy would buy back what it sells"
        ent["why"] = "goal planner: sells %s a turn at %s, keeps %d (no one offered it)" % (
            ent["sell"]["sell_volume"], ent["sell"]["sell_price"], keep)
        out.setdefault(item, {})["sell_volume"] = ent["sell"]["sell_volume"]
    # trials: idle piles the plan doesn't count (no sales yet) are offered just under the cheapest seller, over
    # trial_turns, keeping the plan's floor. They count in the plan once they sell (sales history).
    tt = max(1, int(_n(load_cfg(cfg).get("trial_turns", 12))))
    for item, d in sorted((G.get("idle") or {}).items()):
        if not live["sells"] or item in never:
            continue
        ent = orders.setdefault(item, {})
        tiers = (store_items.get(item) or {}).get("orders") or []
        held_ = _n((store_items.get(item) or {}).get("held"))
        b_ = ent.get("effective_buy") or ent.get("buy")
        if (b_ and _n(b_.get("buy_volume")) > 0) or any(
                _n(t.get("buy_volume")) > 0 and (t.get("max_holding") is None or _n(t["max_holding"]) > held_) for t in tiers):
            continue
        sold_last = _n(((store_items.get(item) or {}).get("flow") or {}).get("sale"))
        if sold_last > 0 and item not in set(prev_sells or ()):
            continue                                 # it sells already on someone's offer
        last, ask = _n(d.get("last")), _n(d.get("ask"))
        px = min(0.99 * ask, last) if ask else 0.97 * last
        import planner as _pl
        price = _pl.snap_price(px, up=False)
        cur = ent.get("sell")
        if cur and _n(cur.get("sell_price")) and _n(cur.get("sell_price")) <= price:
            continue                                 # v2's own offer is already as low
        live_sell = max([_n(t.get("sell_volume")) for t in tiers] + [0])
        vol = int(min(2 * live_sell + 10, max(1, math.ceil(_n(d.get("excess")) / tt))))
        ent["sell"] = {"sell_volume": vol, "sell_price": "%g" % price, "min_holding": int(math.ceil(_n(d.get("keep"))))}
        ent["goal_sell"] = {"sell_price": ent["sell"]["sell_price"], "trial": True}
        if any(_n(t.get("buy_volume")) > 0 for t in tiers):
            ent["buy_off"] = "goal planner offers its idle pile: a dormant buy would buy it back"
        ent["why"] = "goal planner: trial sale of an idle pile, %d a turn at %s, keeps %d (%.0f over)" % (
            vol, ent["sell"]["sell_price"], ent["sell"]["min_holding"], _n(d.get("excess")))
        out.setdefault(item, {})["sell_volume"] = vol
    for item, v in sorted((now.get("sell") or {}).items()):
        o = (orders.get(item) or {}).get("sell")
        if o is None or (orders.get(item) or {}).get("goal_sell"):
            continue
        want = max(int(math.ceil(_n(v) - 1e-6)), int(_n(o.get("sell_volume"))))
        d = out.setdefault(item, {})
        d["sell_volume"] = want
        d["v2_sell_volume"] = o.get("sell_volume")
        if live["sells"] and want != o.get("sell_volume"):
            o["sell_volume"] = want
            orders[item]["why"] = "goal planner: sells %d (v2 had %s)" % (want, d["v2_sell_volume"])
        # the plan's volume is priced at its lowest step (a live bid or the undercut): an ask over that sells less
        # than the plan counts (garments at 20.0 over a 19.5 town: 0 sold)
        px = _n((G.get("sell_px") or {}).get(item))
        if live["sells"] and px > 0 and px < 0.995 * _n(o.get("sell_price")):
            import planner as _pl
            newp = "%g" % _pl.snap_price(px, up=False)
            d["v2_sell_price"] = o.get("sell_price")
            o["sell_price"] = newp
            orders[item]["why"] = "goal planner: sells %d at %s (v2 had %s at %s)" % (
                want, newp, d["v2_sell_volume"], d["v2_sell_price"])
    return out, any(live.values())
