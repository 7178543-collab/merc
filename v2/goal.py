"""Goal planner (shadow, Oct 23): one goal, one budget. See v2/GOAL.md.

Goal (Taylor, Oct 22): grow BUSINESS VALUE = cash + stock at market value.

Each run solves one linear program over a turn of steady flow: building rates, household duty, buys, sells, pile
draw-down and stock build, maximising value gained per turn, subject to item balances, own labour, building sizes,
home market depth, the free-prestige floor and the cash floor. Duals and re-solves price every change and investment.
Pure functions over the snapshot; never touches the game.
"""
import json
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


def _n(x, d=0.0):
    try:
        return float(x)
    except (TypeError, ValueError):
        return d


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


# ---------------------------------------------------------------- the model

def _coeffs(b, recipes):
    """Per unit of target: (inputs, outputs, prestige). Live flows when it produced (they carry the real porterage,
    tool wear and worker bonuses), else the recipe."""
    r = recipes.get(b.get("recipe") or "") or {}
    prod = _n(b.get("production"))
    ins, outs = {}, {}
    fl = b.get("flows") or {}
    if prod > 0 and fl:
        for item, f in fl.items():
            if _n(f.get("consumption")) > 0:
                ins[item] = _n(f["consumption"]) / prod
            if _n(f.get("production")) > 0:
                outs[item] = _n(f["production"]) / prod
    else:
        for i in r.get("inputs") or []:
            ins[i["product"]] = ins.get(i["product"], 0) + _n(i["amount"])
        for o in r.get("outputs") or []:
            outs[o["product"]] = outs.get(o["product"], 0) + _n(o["amount"])
    return ins, outs, _n(r.get("prestige"))


def build_model(s, cfg, recipes, drip=None, hist=None):
    """Collect everything the LP needs into plain dicts (separate from solving, so tests can poke at it)."""
    g = load_cfg(cfg)
    perishable = set((cfg or {}).get("perishable") or []) | {"labour"}
    items = (s.get("store") or {}).get("items") or {}
    market = s.get("market") or {}
    ops = s.get("operations") or {}
    hh = s.get("household") or {}
    hist = hist if hist is not None else []
    sold = {}
    if hist:
        a12, a24 = sales_avg(hist, int(g["sales_window"])), sales_avg(hist, 2 * int(g["sales_window"]))
        sold = {k: max(a12.get(k, 0.0), a24.get(k, 0.0)) for k in set(a12) | set(a24)}
    reserves = dict((cfg or {}).get("stockpiles") or {})
    reserves.pop("_about", None)
    for k, v in (g.get("reserve") or {}).items():
        reserves[k] = max(_n(v), _n(reserves.get(k)))

    acts = []            # activities: {name, kind, ins, outs, prestige, lb, ub, cur}
    fixed_supply, fixed_demand = {}, {}
    notes = []

    for b in s.get("buildings") or []:
        if b.get("construction"):
            continue                          # a site: its materials are fixed demand (drip), not an activity
        r = recipes.get(b.get("recipe") or "")
        if not r:                             # e.g. the farmstead's 'service 1': its flows are fixed supply/demand
            for item, f in (b.get("flows") or {}).items():
                if _n(f.get("production")):
                    fixed_supply[item] = fixed_supply.get(item, 0) + _n(f["production"])
                if _n(f.get("consumption")):
                    fixed_demand[item] = fixed_demand.get(item, 0) + _n(f["consumption"])
            continue
        ins, outs, pr = _coeffs(b, recipes)
        if not outs and not pr:
            continue
        ub = _n(b.get("size")) or 1.0
        cap = (g.get("max_target") or {}).get(b.get("type"))
        if cap is not None:
            ub = min(ub, float(cap))
        ub = max(ub, _n(b.get("target")))     # never plan a building smaller than it already runs by hand
        nm = b.get("name") or b.get("type")
        if b.get("id") and str(b["id"]) in str(nm):
            nm = b.get("type") or nm        # the game names some buildings '<type><id>'
        acts.append({"name": nm, "kind": "building", "id": b.get("id"),
                     "type": b.get("type"), "recipe": b.get("recipe"), "ins": ins, "outs": outs, "prestige": pr,
                     "lb": 0.0, "ub": ub, "cur": _n(b.get("target")), "size": _n(b.get("size"))})

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

    names = set(fixed_supply) | set(fixed_demand) | set(items)
    for a in acts:
        names |= set(a["ins"]) | set(a["outs"])
    names.discard("money")

    use_now = {}
    for a in acts:
        for i, q in a["ins"].items():
            use_now[i] = use_now.get(i, 0) + q * a["cur"]
    for i, q in fixed_demand.items():
        use_now[i] = use_now.get(i, 0) + q

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
        # sell steps: what we really sold at our price, then an undercut step for town share
        steps = []
        avg = sold.get(item, 0.0)
        floor = _n(((cfg or {}).get("sell_floor") or {}).get(item))
        p1 = sell_px or last
        if avg > 0 and p1:
            steps.append((p1, avg))
        if bid and _n(m.get("bid_vol")) > 0 and (not floor or _n(bid) >= floor) and (not p1 or _n(bid) < p1):
            steps.append((_n(bid), _n(m.get("bid_vol"))))       # instant fill at the home bid
        p2 = g["undercut"] * last
        room = g["market_share"] * traded - avg - (_n(m.get("bid_vol")) if bid else 0.0)
        if p2 and room > 0.5 and (not floor or p2 >= floor):
            steps.append((p2, room))
        # stock: piles over max(reserve, buffer) may be drawn; free bin space may take output (at keep_value)
        draw_cap = stock_cap = 0.0
        if not perish and item not in NOT_STOCK:
            keep = max(reserve, g["buffer_turns"] * use_now.get(item, 0.0))
            draw_cap = max(0.0, held - keep) / g["drain_turns"]
            capy = _n(it.get("capacity"))
            stock_cap = max(0.0, capy - held) / g["drain_turns"] if capy else 0.0
        goods[item] = {"held": held, "cost": cost, "mark": mark, "buy_px": buy_px, "buy_cap": buy_cap,
                       "sell": steps, "draw_cap": draw_cap, "stock_cap": stock_cap, "perishable": perish,
                       "reserve": reserve, "last": last, "traded": traded}

    # prestige: impacts that no activity of ours explains are fixed (sustenance, legacy drain)
    imp = hh.get("impacts") or {}
    act_recipes = {a.get("recipe") for a in acts}
    fixed_pr = sum(_n(v) for k, v in imp.items() if k not in act_recipes)
    free = _n(hh.get("free"))
    if free >= g["prestige_floor"]:
        pr_min = -(free - g["prestige_floor"]) / g["prestige_horizon"]
    else:
        pr_min = (g["prestige_floor"] - free) / g["prestige_recover_turns"]

    cash = _n(s.get("cash"))
    fixed_cost = _n(g["building_tax"]) + sum(_n(sh.get("running_cost")) for sh in s.get("ships") or [])
    if cash < g["cash_floor"]:
        cash_min = (g["cash_floor"] - cash) / g["cash_recover_turns"]
    else:
        cash_min = -(cash - g["cash_floor"]) / g["cash_recover_turns"]

    return {"acts": acts, "goods": goods, "fixed_supply": fixed_supply, "fixed_demand": fixed_demand,
            "fixed_prestige": fixed_pr, "prestige_min": pr_min, "free_prestige": free,
            "cash": cash, "cash_min": cash_min, "fixed_cost": fixed_cost, "cfg": g, "notes": notes,
            "tenants_level": _n((hh.get("levels") or {}).get("tenants"))}


def solve(M, fix=None, extra_supply=None, prestige_min=None, cash_min=None):
    """Solve the LP. fix: {activity name: level} pins those activities. Returns a result dict (ok False if infeasible
    even after relaxing the floors, with the reason)."""
    from scipy.optimize import linprog
    acts, goods = M["acts"], M["goods"]
    g = M["cfg"]
    fix = fix or {}
    sup = dict(M["fixed_supply"])
    for k, v in (extra_supply or {}).items():
        sup[k] = sup.get(k, 0) + v
    item_names = sorted(goods)
    idx = {k: i for i, k in enumerate(item_names)}

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

    n = len(cols)
    A_eq = [[0.0] * n for _ in item_names]
    b_eq = [0.0] * len(item_names)
    for k in item_names:
        b_eq[idx[k]] = M["fixed_demand"].get(k, 0.0) - sup.get(k, 0.0)
    pr_row = [0.0] * n
    cash_row = [0.0] * n
    for j, (kind, key, step) in enumerate(cols):
        if kind == "act":
            a = next(x for x in acts if x["name"] == key)
            for i, q in a["outs"].items():
                if i in idx:
                    A_eq[idx[i]][j] += q
            for i, q in a["ins"].items():
                if i in idx:
                    A_eq[idx[i]][j] -= q
            pr_row[j] = -a["prestige"]          # >= written as <=: -prestige * x <= fixed - min
        elif kind == "buy":
            A_eq[idx[key]][j] += 1.0
            cash_row[j] = goods[key]["buy_px"]  # -cashflow <= -cash_min
        elif kind == "sell":
            A_eq[idx[key]][j] -= 1.0
            cash_row[j] = -goods[key]["sell"][step][0]
        elif kind == "draw":
            A_eq[idx[key]][j] += 1.0
        elif kind in ("stock", "waste"):
            A_eq[idx[key]][j] -= 1.0

    pmin = M["prestige_min"] if prestige_min is None else prestige_min
    cmin = M["cash_min"] if cash_min is None else cash_min
    relaxed = []

    # The floors are soft: a slack column per floor, priced so high the plan only uses it when nothing else can meet
    # the floor. So an impossible floor still gets as close as it can (never "ignored"), and is reported.
    PEN_P, PEN_C = 10000.0, 100.0
    use_cash = cmin is not None
    cc = list(c) + [PEN_P] + ([PEN_C] if use_cash else [])
    bb = list(zip(lb, ub)) + [(0, None)] + ([(0, None)] if use_cash else [])
    ext = 1 + (1 if use_cash else 0)
    A_eq2 = [row + [0.0] * ext for row in A_eq]
    A_ub = [pr_row + [-1.0] + ([0.0] if use_cash else [])]       # -prestige - slack <= fixed - min
    b_ub = [M["fixed_prestige"] - pmin]
    if use_cash:
        A_ub.append(cash_row + [0.0, -1.0])                       # -cashflow - slack <= -(min + fixed)
        b_ub.append(-(cmin + M["fixed_cost"]))
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
    flows = {}
    for j, (kind, key, step) in enumerate(cols):
        if kind != "act" and x[j] > 1e-6:
            f = flows.setdefault(key, {})
            f[kind] = f.get(kind, 0.0) + x[j]
    value = -sum(c[j] * x[j] for j in range(n))
    cashflow = -sum(cash_row[j] * x[j] for j in range(n)) - M["fixed_cost"]
    prestige = M["fixed_prestige"] - sum(pr_row[j] * x[j] for j in range(n))
    shadow = {}
    try:
        for k in item_names:
            shadow[k] = res.eqlin.marginals[idx[k]]
        shadow["_prestige"] = -res.ineqlin.marginals[0]
        shadow["_cash"] = -res.ineqlin.marginals[1] if len(res.ineqlin.marginals) > 1 else 0.0
    except Exception:
        pass
    return {"ok": True, "value": value, "levels": levels, "flows": flows, "cashflow": cashflow,
            "prestige_rate": prestige, "shadow": shadow, "relaxed": relaxed}


# ---------------------------------------------------------------- the plan

def _margin(a, shadow):
    """Coin a unit of this activity makes at the plan's own item prices (shadow prices)."""
    out = sum(q * shadow.get(i, 0.0) for i, q in a["outs"].items())
    inn = sum(q * shadow.get(i, 0.0) for i, q in a["ins"].items())
    return out - inn + a["prestige"] * shadow.get("_prestige", 0.0)


def _plot_cost(btype, buildings_data, goods):
    """Coin for one more plot of a building type: one plot takes the building's full construction materials (park
    plots: 260 labour, 60 limestone, 40 timber, as the game charged), priced at home asks."""
    b = buildings_data.get(btype) or {}
    mats = (b.get("construction") or {}).get("materials") or {}
    cost = 0.0
    for item, q in mats.items():
        gd = goods.get(item) or {}
        px = gd.get("buy_px") or gd.get("last") or gd.get("cost") or 0.0
        cost += _n(q) * px
    return cost


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


def plan_goal(s, cfg, recipes, drip=None, hist=None, buildings_data=None):
    if not _ensure_scipy():
        return {"ok": False, "why": "scipy not installed and pip install failed"}
    M = build_model(s, cfg, recipes, drip=drip, hist=hist)
    g = M["cfg"]
    opt = solve(M)
    if not opt["ok"]:
        return {"ok": False, "why": "no feasible plan: %s" % opt.get("why")}
    cur_fix = {a["name"]: a["cur"] for a in M["acts"]}

    def free(fix):          # value with the levels pinned and the limits set aside: like-for-like comparisons
        return solve(M, fix=fix, prestige_min=-1e9, cash_min=None)

    def same(r):
        return bool(r.get("ok"))

    cur = free(cur_fix)                     # what today's settings earn
    cur_lim = solve(M, fix=cur_fix)         # ... and which limits they break
    breaks = cur_lim.get("relaxed") if cur_lim.get("ok") else ["no feasible flow"]
    now_flows = (cur_lim if cur_lim.get("ok") else cur).get("flows") or {}

    # changes, priced one at a time on top of each other (best first), so the gains add up to plan - today.
    # Moves that only work together (a chain stage and its feeder) are priced as one group.
    changes = []
    pending = [a for a in M["acts"] if abs(opt["levels"].get(a["name"], 0.0) - a["cur"]) >= g["change_min"]]
    applied, base = dict(cur_fix), cur
    while pending and same(base):
        best = None
        for a in pending:
            trial = dict(applied)
            trial[a["name"]] = opt["levels"][a["name"]]
            r = free(trial)
            if same(r) and (best is None or r["value"] - base["value"] > best[2]):
                best = (a, r, r["value"] - base["value"])
        if best is None:
            trial = dict(applied)
            for a in pending:
                trial[a["name"]] = opt["levels"][a["name"]]
            r = free(trial)
            changes.append({"name": " + ".join(a["name"] for a in pending), "group": [
                {"name": a["name"], "id": a.get("id"), "kind": a["kind"], "recipe": a.get("recipe"),
                 "from": round(a["cur"], 3), "to": round(opt["levels"][a["name"]], 3)} for a in pending],
                "gain": (r["value"] - base["value"]) if same(r) else None})
            break
        a, r, gain = best
        applied[a["name"]] = opt["levels"][a["name"]]
        base = r
        pending.remove(a)
        changes.append({"name": a["name"], "id": a.get("id"), "kind": a["kind"], "recipe": a.get("recipe"),
                        "from": round(a["cur"], 3), "to": round(opt["levels"][a["name"]], 3), "gain": gain})
    if pending and not same(cur):
        for a in pending:
            changes.append({"name": a["name"], "id": a.get("id"), "kind": a["kind"], "recipe": a.get("recipe"),
                            "from": round(a["cur"], 3), "to": round(opt["levels"][a["name"]], 3), "gain": None})

    # investments, each priced by re-solving with the extra capacity under the same limits
    inv = []
    lvl = int(M["tenants_level"]) + 1
    t_cost = 50 * (lvl - 3)          # 450 for L12, 500 for L13 (game prices seen Oct 22)
    left = M["free_prestige"] - t_cost
    M_t = dict(M)
    M_t["prestige_min"] = -(left - g["prestige_floor"]) / g["prestige_horizon"] if left >= g["prestige_floor"] else M["prestige_min"]
    tl = solve(M_t, extra_supply={"labour": g["tenants_labour"]})
    if tl.get("ok") and tl.get("relaxed") == opt.get("relaxed"):
        inv.append({"what": "Tenants L%d" % lvl, "cost": "%d prestige" % t_cost, "gain": tl["value"] - opt["value"],
                    "pays": left >= g["prestige_floor"],
                    "note": ("free after %.0f" % left) if left >= g["prestige_floor"] else
                            "waits until %.0f free (keeps %d after)" % (t_cost + g["prestige_floor"], g["prestige_floor"])})
    bdata = buildings_data or {}
    for a in M["acts"]:
        if a["kind"] != "building" or opt["levels"].get(a["name"], 0) < a["ub"] - 1e-6:
            continue
        if a["type"] in (g.get("max_target") or {}):
            continue
        most = _n(((bdata.get(a["type"]) or {}).get("construction") or {}).get("size"))
        if most and a["size"] >= most:
            continue                  # already at the most plots the building type allows
        M2 = dict(M)
        M2["acts"] = [dict(x, ub=x["ub"] + 1) if x["name"] == a["name"] else x for x in M["acts"]]
        r = solve(M2)
        if not (r.get("ok") and r.get("relaxed") == opt.get("relaxed")):
            continue
        gain = r["value"] - opt["value"] - g["urban_plot_tax"]
        if gain <= 0.5:
            continue
        cost = _plot_cost(a["type"], bdata, M["goods"])
        inv.append({"what": "+1 plot %s" % a["name"], "cost": "~%.0f coin" % cost, "gain": gain,
                    "payback": cost / gain, "pays": cost / gain <= g["invest_horizon"]})
    inv.sort(key=lambda d: -(d["gain"] or 0))

    hist = hist or []
    trend = value_trend(hist, set((cfg or {}).get("perishable") or [])) if hist else {}
    sh = opt["shadow"]
    keys = ["labour", "thread", "cloth", "flax fibres", "garments", "nets", "beer", "timber"]
    return {
        "ok": True, "goal": "business value", "turn": s.get("turn"), "t": s.get("t"),
        "value_now": trend.get("now"), "trend": trend,
        "plan_value": opt["value"], "current_value": cur.get("value") if cur.get("ok") else None,
        "current_breaks": breaks,
        "plan_cashflow": opt["cashflow"], "current_cashflow": cur.get("cashflow"),
        "buy": {k: round(v.get("buy", 0), 2) for k, v in opt["flows"].items() if v.get("buy")},
        # buys and sells for the rates that run today (the 'buys'/'sells' jobs use these: rates move in steps,
        # so orders follow the real targets, not the plan's end state)
        "orders_now": {"buy": {k: round(v.get("buy", 0), 2) for k, v in now_flows.items() if v.get("buy")},
                       "sell": {k: round(v.get("sell", 0), 2) for k, v in now_flows.items() if v.get("sell")}},
        "sell": {k: round(v.get("sell", 0), 2) for k, v in opt["flows"].items() if v.get("sell")},
        "plan_prestige_rate": opt["prestige_rate"], "current_prestige_rate": cur.get("prestige_rate"),
        "prestige_min": M["prestige_min"], "cash_min": M["cash_min"], "fixed_cost": M["fixed_cost"],
        "relaxed": opt["relaxed"], "levels": {k: round(v, 3) for k, v in opt["levels"].items()},
        "changes": changes, "investments": inv,
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
    out.append("- Limits: cash flow >= %+.0f/turn, prestige >= %+.2f/turn (after %.0f tax and crew)." % (
        G["cash_min"], G["prestige_min"], G["fixed_cost"]))
    if cv is not None:
        br = G.get("current_breaks") or []
        out.append("- Today's settings: value %+.0f/turn, cash %+.0f/turn, prestige %+.2f/turn%s." % (
            cv - G["fixed_cost"], G.get("current_cashflow") or 0, G.get("current_prestige_rate") or 0,
            (" - breaks the %s" % " and ".join(br)) if br else ""))
    out.append("- Plan: value %+.0f/turn, cash %+.0f/turn, prestige %+.2f/turn%s." % (
        pv - G["fixed_cost"], G["plan_cashflow"], G["plan_prestige_rate"],
        (" - could not meet the %s" % " and ".join(G["relaxed"])) if G.get("relaxed") else ", inside both limits"))
    if G.get("changes"):
        out.append("- Changes, each priced on top of the one before (value/turn, limits aside):")
        for ch in G["changes"][:10]:
            g_ = "%+.0f/turn" % ch["gain"] if ch.get("gain") is not None else "not comparable"
            if ch.get("group"):
                out.append("  - together: %s: %s" % (", ".join("%s %.2f -> %.2f" % (x["name"], x["from"], x["to"])
                                                            for x in ch["group"]), g_))
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
    if G.get("investments"):
        out.append("- Investments:")
        for d in G["investments"][:5]:
            pb = (", payback %.0f turns" % d["payback"]) if d.get("payback") else ""
            out.append("  - %s for %s: %+.0f/turn%s%s" % (d["what"], d["cost"], d["gain"], pb,
                                                       (" (%s)" % d["note"]) if d.get("note") else ""))
    return out


# ---------------------------------------------------------------- its own scorecard

def history_line(G):
    """One compact line per run for state/v2/goal_history.jsonl."""
    if not G or not G.get("ok"):
        return {"t": (G or {}).get("t"), "ok": False, "why": (G or {}).get("why")}
    fc = G.get("fixed_cost") or 0.0
    return {"t": G.get("t"), "turn": G.get("turn"), "ok": True, "value_now": G.get("value_now"),
            "pred_today": (G["current_value"] - fc) if G.get("current_value") is not None else None,
            "pred_plan": G["plan_value"] - fc, "cash_today": G.get("current_cashflow"), "cash_plan": G.get("plan_cashflow"),
            "levels": G.get("levels"), "live": G.get("live_jobs"),
            "check": None if not G.get("scorecard") else (abs(G["scorecard"]["predicted"] - G["scorecard"]["real"])
                                                         <= max(40.0, 0.5 * abs(G["scorecard"]["real"])))}


def scorecard(goal_hist, hist, perishable=(), min_turns=6):
    """Did the model's 'today's settings earn X/turn' match what really happened? Compares the mean prediction of
    the runs since a past turn with the real change in business value since that turn."""
    rows = [r for r in goal_hist if r.get("ok") and r.get("pred_today") is not None and r.get("turn") is not None]
    if not rows or not hist:
        return None
    now = hist[-1]
    t_now = now.get("turn")
    by_turn = {r.get("turn"): r for r in hist}
    for back in (24, 12, min_turns):
        start = next((r for r in rows if t_now - r["turn"] >= back), None)
        if start is None or start["turn"] not in by_turn:
            continue
        span = [r for r in rows if r["turn"] >= start["turn"]]
        pred = sum(r["pred_today"] for r in span) / len(span)
        real = (value_of(now, perishable)[0] - value_of(by_turn[start["turn"]], perishable)[0]) / (t_now - start["turn"])
        return {"turns": t_now - start["turn"], "predicted": pred, "real": real, "runs": len(span)}
    return None


# ---------------------------------------------------------------- orders (the 'buys' and 'sells' jobs)

def apply_orders(G, plan, cfg):
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
    for item, v in sorted((now.get("sell") or {}).items()):
        o = (orders.get(item) or {}).get("sell")
        if o is None:
            continue
        want = max(int(math.ceil(_n(v) - 1e-6)), int(_n(o.get("sell_volume"))))
        d = out.setdefault(item, {})
        d["sell_volume"] = want
        d["v2_sell_volume"] = o.get("sell_volume")
        if live["sells"] and want != o.get("sell_volume"):
            o["sell_volume"] = want
            orders[item]["why"] = "goal planner: sells %d (v2 had %s)" % (want, d["v2_sell_volume"])
    return out, any(live.values())
