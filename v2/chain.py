"""Chain sizing for bot v2: sets the textile chain's production targets every run.

A port of chain_balancer.py's pull model (sew what sells, each step upstream feeds the next, buffers held in turns of
the next step's use, glut drain, extra thread consumers such as the ropewalk fed from weaving), with two changes:

  1. LABOUR BUDGET (Oct 14, Taylor: improve the setup). Everything that is not the chain is funded first: the banquet,
     park, quarry, ropewalk, logging camp, brewery, the household duty and labour metered to build sites. The chain
     gets what is left of our own labour plus cfg chain.labour_buy_max of bought labour. If its plan needs more,
     sewing and weaving are cut first (garments are the thinnest margin), then the upstream steps, but never below
     the thread the ropewalk and the net duty need. This is the fix for this week's starvation loops (Oct 13 flax
     ramp, Oct 14 ropewalk loop), where the chain's labour bid crowded out the prestige buildings.
  2. SEASON-PROOF. Chain buildings are found by type, recipe amounts come from v2/data/recipes.json and the
     buildings' own recipes, and nothing is keyed to an id.

plan_chain(snap, cfg, recipes, ...) is pure (no API calls) so it runs offline and in tests. act.py applies it when
cfg live.chain is true; chain_balancer.py (v1) stands aside then.
"""
import glob
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

STEPS = ("flax", "ret", "spin", "weave", "sew")
TYPES = {"flax": "flax farm", "ret": "retting pit", "spin": "spinnery", "weave": "weavery", "sew": "sewing shop"}
# what each step makes and (for all but flax) eats; read from the building's recipe, these are the fallbacks
GOODS = {"flax": (None, "flax plants"), "ret": ("flax plants", "flax fibres"), "spin": ("flax fibres", "thread"),
         "weave": ("thread", "cloth"), "sew": ("cloth", "garments")}
BUFFERS = {"flax fibres": {"fill": 5, "drain": 10}, "thread": {"fill": 15, "drain": 30}, "cloth": {"fill": 10, "drain": 40}}

DEFAULTS = {
    "garment_sales_floor": 30,  # Oct 15: size sewing for at least this many sales a turn. Sizing on our OWN last sales was
                                # circular: v2 offered only the surplus, sales fell to what was offered, the chain made less,
                                # and garments sold went 62 -> 2 a turn (Oct 14-15) while home still trades ~51 a turn
    "garment_floor_pile_turns": 4,  # Oct 18: the floor is off while garments held > this x the floor (a pile to sell)
    "church_fill_turns": 4,     # Oct 15: an open church garments ask is built up to over this many turns
    "buffer_turns": 2,          # stockpile between steps, in turns of the next step's use (Oct 14: was 4)
    "drain_over": 1.2,          # drain a buffer once it is over 1.2x its target
    "drain_turns": 12,          # spread the excess over this many turns
    "garment_keep_turns": 2,    # finished garments: keep ~2 turns of sales
    "garment_drain_turns": 20,
    "garment_drain_max": 30,
    "low_fraction": 0.5,        # FILLING starts when a buffer is under half its target
    "fill_cash_min": 8000,      # below this cash: HOLD (make only what is used, no top-ups)
    "sos_cash": 2000,           # below this: run only what our own labour covers
    "sales_window": 12,
    "sales_margin": 1.05,
    "household_garments": 1.8,
    "extra_thread_min": 10,     # thread use beyond the household duty by more than this = another consumer (ropewalk)
    "labour_buy_max": 350,      # bought labour the chain may lean on, after everything else is funded
    "min_change": 0.02,         # ignore target moves smaller than this (x)
    "drift": 0.10,              # rewrite targets only when one is this far from plan, or the buffer mode flips
}


def _n(x, d=0.0):
    try:
        return float(x)
    except (TypeError, ValueError):
        return d


def _recipe_io(recipes, name):
    r = (recipes or {}).get(name or "") or {}
    ins = {i["product"]: _n(i["amount"]) for i in r.get("inputs") or []}
    outs = {o["product"]: _n(o["amount"]) for o in r.get("outputs") or []}
    return ins, outs


def find_chain(snap, recipes):
    """{step: {id, name, size, target, recipe, labour, in, in_good, out, out_good}} for the chain buildings we own."""
    found = {}
    for b in snap.get("buildings") or []:
        step = next((k for k, t in TYPES.items() if b.get("type") == t), None)
        if not step or step in found or b.get("construction") and not b.get("recipe"):
            continue
        ins, outs = _recipe_io(recipes, b.get("recipe"))
        in_good, out_good = GOODS[step]
        found[step] = {"id": str(b.get("id")), "name": b.get("name"), "size": _n(b.get("size")),
                       "target": _n(b.get("target")), "recipe": b.get("recipe"),
                       "labour": ins.get("labour", 0.0), "tools": ins.get("tools", 0.0),
                       "in": ins.get(in_good, 0.0) if in_good else 0.0, "in_good": in_good,
                       "out": outs.get(out_good, 0.0), "out_good": out_good}
    return found


def history_garments(window=12, root=ROOT):
    """(average garments sold a turn over the last `window` turns, average realized route exports a turn)."""
    sold = {}
    for path in sorted(glob.glob(os.path.join(root, "history", "merc-*.jsonl"))):
        with open(path) as f:
            for line in f:
                try:
                    r = json.loads(line)
                    sold[r["turn"]] = _n(r["items"]["garments"][3])
                except (ValueError, KeyError, IndexError, TypeError):
                    continue
    last = [sold[t] for t in sorted(sold)[-window:]]
    sales = sum(last) / len(last) if len(last) >= 6 else None
    exp = {}
    try:
        with open(os.path.join(root, "state", "v2", "history.jsonl")) as f:
            for line in f:
                try:
                    r = json.loads(line)
                except ValueError:
                    continue
                if r.get("turn") is not None:
                    exp.setdefault(r["turn"], 0.0)
                    if "exports" in r:
                        exp[r["turn"]] = max(exp[r["turn"]], _n((r.get("exports") or {}).get("garments")))
    except OSError:
        pass
    exports = 0.0
    if exp:
        t1 = max(exp)
        exports = sum(exp.get(t, 0.0) for t in range(t1 - 11, t1 + 1)) / 12.0
    return sales, exports


def other_labour(snap, recipes, chain, drip=0.0):
    """Labour everything outside the chain is set to use a turn: other buildings at their targets, the household duty,
    and labour metered to build sites. These are funded before the chain."""
    ids = {c["id"] for c in chain.values()}
    total, parts = 0.0, {}
    for b in snap.get("buildings") or []:
        if str(b.get("id")) in ids or _n(b.get("target")) <= 0:
            continue
        lab = _recipe_io(recipes, b.get("recipe"))[0].get("labour", 0.0) * _n(b.get("target"))
        if lab > 0:
            parts[b.get("name") or b.get("type")] = round(lab, 1)
            total += lab
    hd = snap.get("household_duty") or {}
    lab = _recipe_io(recipes, hd.get("recipe"))[0].get("labour", 0.0) * _n(hd.get("target"))
    if lab > 0:
        parts["household duty"] = round(lab, 1)
        total += lab
    if drip:
        parts["build sites"] = round(drip, 1)
        total += drip
    return total, parts


def other_thread(snap, recipes, chain):
    """(thread every non-weavery consumer is set to use, the household duty's part of it)."""
    weave_id = (chain.get("weave") or {}).get("id")
    total = 0.0
    for b in snap.get("buildings") or []:
        if str(b.get("id")) == weave_id or _n(b.get("target")) <= 0:
            continue
        total += _recipe_io(recipes, b.get("recipe"))[0].get("thread", 0.0) * _n(b.get("target"))
    hd = snap.get("household_duty") or {}
    duty = _recipe_io(recipes, hd.get("recipe"))[0].get("thread", 0.0) * _n(hd.get("target"))
    return total + duty, duty


def buffer_targets(C, t, other_th, turns):
    return {
        "cloth": turns * t["sew"] * C["sew"]["in"],
        "thread": turns * (t["weave"] * C["weave"]["in"] + other_th),
        "flax fibres": turns * t["spin"] * C["spin"]["in"],
    }


def size(C, stocks, sales, exports, other_th, duty_th, mode, p):
    """balancer's pull model on the chain's current plot counts: targets {step: x} and buffer targets."""
    caps = {k: C[k]["size"] for k in STEPS}
    have_g = stocks.get("garments", 0)
    floor = p.get("garment_sales_floor", 0)
    # Oct 18: the floor guards against the Oct 14 sell/make spiral, not against selling down a pile. With ~380 garments
    # held it kept sewing ~19 a turn into a market taking ~20: the pile never shrank and ~6k of finished goods sat
    # while bought labour made more. Over garment_floor_pile_turns x the floor held, size on real sales only.
    if floor and have_g > p.get("garment_floor_pile_turns", 4) * floor:
        floor = 0
    demand = max(sales, floor) if sales is not None else None
    want = demand + p["household_garments"] + exports if demand is not None else caps["sew"] * C["sew"]["out"]
    outflow = (sales or 0) + exports
    gfloor = p.get("garment_floor", 0)          # an open church garments ask (plan_chain reads it)
    if gfloor and have_g < gfloor:
        want += (gfloor - have_g) / p.get("church_fill_turns", 4)
    elif sales and have_g > p["garment_keep_turns"] * outflow:
        drain = min((have_g - p["garment_keep_turns"] * outflow) / p["garment_drain_turns"], p["garment_drain_max"])
        want = max(want - drain, 0.3 * want)
    sew = min(caps["sew"], want * p["sales_margin"] / C["sew"]["out"], p.get("sew_cap", float("inf")))
    fed_by_weaving = other_th - duty_th > p["extra_thread_min"]

    def thread_up(weave_runs):
        # Oct 15 fix: weaving can only hand the ropewalk the thread it would itself have drawn. Whatever it can't
        # cover (all of it while cloth drains and weaving sits at 0) has to come from spinning, or the ropewalk and
        # the net duty starve (Oct 15 night: spin 0.77 made ~40 thread vs 79 used, thread 456 -> 161 in 9 turns).
        if not fed_by_weaving:
            return other_th
        return max(duty_th, other_th - weave_runs * C["weave"]["in"])
    base = {"sew": sew, "weave": sew * C["sew"]["in"] / C["weave"]["out"]}
    base["spin"] = (base["weave"] * C["weave"]["in"] + thread_up(base["weave"])) / C["spin"]["out"]
    tg = buffer_targets(C, base, other_th, p["buffer_turns"])

    def top(item):
        have = stocks.get(item, 0)
        if mode == "FILLING" and have < tg[item]:
            return BUFFERS[item]["fill"]
        if have > tg[item] * p["drain_over"]:
            return -min((have - tg[item]) / p["drain_turns"], BUFFERS[item]["drain"])
        return 0
    weave = max(0, min(caps["weave"], (sew * C["sew"]["in"] + top("cloth")) / C["weave"]["out"]))
    spin = max(0, min(caps["spin"], (weave * C["weave"]["in"] + thread_up(weave) + top("thread")) / C["spin"]["out"]))
    if fed_by_weaving:
        weave = max(0, min(weave, (spin * C["spin"]["out"] - other_th - top("thread")) / C["weave"]["in"]))
        cloth_slice = max(0.0, stocks.get("cloth", 0) - p["low_fraction"] * tg["cloth"]) / p["drain_turns"]
        sew = min(sew, (weave * C["weave"]["out"] + cloth_slice) / C["sew"]["in"])
    ret = max(0, min(caps["ret"], (spin * C["spin"]["in"] + top("flax fibres")) / C["ret"]["out"]))
    flax = min(caps["flax"], ret * C["ret"]["in"] / C["flax"]["out"]) if C["flax"]["out"] else 0
    return {"sew": sew, "weave": weave, "spin": spin, "ret": ret, "flax": flax}, tg, fed_by_weaving


def fit_labour(C, t, allowance, thread_floor):
    """Cut the chain to `allowance` labour a turn: sewing and weaving first (together, as they are linked), then the
    upstream steps together, but never below the spinning that `thread_floor` needs. Returns (targets, cut note)."""
    lab = lambda x: sum(x[k] * C[k]["labour"] for k in STEPS)
    need = lab(t)
    if need <= allowance + 1e-6:
        return t, None
    t = dict(t)
    down = t["sew"] * C["sew"]["labour"] + t["weave"] * C["weave"]["labour"]
    over = need - allowance
    if down > 0:
        f = max(0.0, 1 - over / down)
        t["sew"] *= f
        t["weave"] *= f
    over = lab(t) - allowance
    if over > 1e-6:
        spin_floor = thread_floor / C["spin"]["out"] if C["spin"]["out"] else 0
        if t["spin"] > spin_floor:
            up = sum(t[k] * C[k]["labour"] for k in ("spin", "ret", "flax"))
            f = min(1.0, max(spin_floor / t["spin"], 1 - over / up if up else 1))
            for k in ("spin", "ret", "flax"):
                t[k] *= f
    return t, "chain plan needed %.0f labour, budget left %.0f: cut to %.0f" % (need, allowance, lab(t))


def buffer_mode(stocks, last_mode, tg, cash, p):
    if cash < p["fill_cash_min"]:
        return "HOLD"
    low = any(stocks.get(i, 0) < tg[i] * p["low_fraction"] for i in BUFFERS)
    full = all(stocks.get(i, 0) >= tg[i] for i in BUFFERS)
    if low:
        return "FILLING"
    if full:
        return "FULL"
    if last_mode in (None, "HOLD"):
        return "FILLING"
    return last_mode


def church_garment_floor(path=None):
    """Oct 15: garments to hold for an open church garments ask (volume + 5), from contracts.py's scoring; 0 if none."""
    path = path or os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "state", "contracts_scored.json")
    try:
        rows = json.load(open(path))
    except (OSError, ValueError):
        return 0
    asks = [_n(r.get("volume")) for r in rows or [] if r.get("kind") == "church" and r.get("item") == "garments"
            and r.get("verdict") in ("WAIT", "OK", "GOOD")]
    return max(asks) + 5 if asks else 0


def plan_chain(snap, cfg=None, recipes=None, last_mode=None, sales=None, exports=0.0, drip=0.0):
    """The chain's targets for this turn. Returns a dict: targets, current, moves, labour, buffers, mode, notes."""
    p = dict(DEFAULTS)
    p.update({k: v for k, v in ((cfg or {}).get("chain") or {}).items() if k in DEFAULTS})
    p["garment_floor"] = church_garment_floor()
    C = find_chain(snap, recipes)
    missing = [k for k in STEPS if k not in C or not C[k]["labour"] or not C[k]["out"]]
    if missing:
        return {"ok": False, "why": "chain buildings or recipes missing: %s" % ", ".join(missing)}
    items = (snap.get("store") or {}).get("items") or {}
    stocks = {i: _n((items.get(i) or {}).get("held")) for i in list(BUFFERS) + ["garments"]}
    cash = _n(snap.get("cash"))
    other_th, duty_th = other_thread(snap, recipes, C)
    _, tg0, _ = size(C, stocks, sales, exports, other_th, duty_th, "HOLD", p)
    mode = buffer_mode(stocks, last_mode, tg0, cash, p)
    t, tg, fed = size(C, stocks, sales, exports, other_th, duty_th, mode, p)

    own = _n(((items.get("labour") or {}).get("flow") or {}).get("production"))
    others, parts = other_labour(snap, recipes, C, drip)
    buy_max = 0 if cash < p["sos_cash"] else p["labour_buy_max"]
    allowance = max(0.0, own - others) + buy_max
    # the labour cut never takes spinning under what the ropewalk and the net duty draw (both earn more per thread
    # than garments); it never raises spinning either
    # Oct 15: over budget -> lower SEWING and re-derive the whole chain from it (search on a sewing cap), so weaving,
    # spinning, retting and flax shrink with it. fit_labour alone cut sewing/weaving but left the upstream sized for
    # the uncut chain: spin 2.5 / flax 7.7 feeding 5 garments a turn while 400 thread sat in store.
    lab = lambda x: sum(x[k] * C[k]["labour"] for k in STEPS)
    search_note = None
    if lab(t) > allowance + 1e-6:
        need0 = lab(t)
        lo, hi = 0.0, t["sew"]
        for _ in range(30):
            mid = (lo + hi) / 2
            if lab(size(C, stocks, sales, exports, other_th, duty_th, mode, dict(p, sew_cap=mid))[0]) <= allowance:
                lo = mid
            else:
                hi = mid
        t, tg, fed = size(C, stocks, sales, exports, other_th, duty_th, mode, dict(p, sew_cap=lo))
        search_note = "chain plan needed %.0f labour, budget left %.0f: cut to %.0f (sewing capped at %.2f)" % (
            need0, allowance, lab(t), lo)
    t, cut = fit_labour(C, t, allowance, other_th)
    cut = cut or search_note
    t = {k: round(v, 2) for k, v in t.items()}
    cur = {k: C[k]["target"] for k in STEPS}
    moves = [(k, cur[k], t[k]) for k in STEPS if abs(t[k] - cur[k]) >= p["min_change"]]
    chain_lab = sum(t[k] * C[k]["labour"] for k in STEPS)
    notes = []
    if cut:
        notes.append(cut)
    if fed:
        notes.append("thread beyond the household duty (%.0f a turn) is fed from weaving" % (other_th - duty_th))
    return {
        "ok": True, "mode": mode, "cash": round(cash), "sales": None if sales is None else round(sales, 1),
        "exports": round(exports, 1), "targets": t, "current": cur, "moves": moves,
        "drift": [k for k in STEPS if abs(t[k] - cur[k]) >= p["drift"]],
        "buildings": {k: {"id": C[k]["id"], "name": C[k]["name"], "size": C[k]["size"]} for k in STEPS},
        "buffers": {i: {"held": round(stocks.get(i, 0)), "target": round(tg[i])} for i in BUFFERS},
        "garments_per_turn": round(t["sew"] * C["sew"]["out"], 1),
        "labour": {"own": round(own), "others": round(others), "others_by": parts, "buy_max": buy_max,
                   "allowance": round(allowance), "chain": round(chain_lab),
                   "delta": round(sum((n - c) * C[k]["labour"] for k, c, n in moves))},
        "thread": {"other": round(other_th, 1), "duty": round(duty_th, 1), "fed_by_weaving": fed},
        "notes": notes,
    }


def report_lines(pc):
    if not pc or not pc.get("ok"):
        return ["## Chain sizing", "", "Not planned: %s" % (pc or {}).get("why", "no plan"), ""]
    L = ["## Chain sizing", "",
         "Mode %s, garments sold %s/turn (+%s exported); plan makes %s garments a turn." % (
             pc["mode"], pc["sales"], pc["exports"], pc["garments_per_turn"]),
         "Labour: own %(own)s, everything else %(others)s, chain may buy %(buy_max)s -> chain allowance %(allowance)s, "
         "chain plan %(chain)s (%(delta)+d vs now)." % pc["labour"], "",
         "| Step | Plots | Now | Plan |", "| --- | --- | --- | --- |"]
    for k in STEPS:
        L.append("| %s | %g | %.2f | %.2f |" % (k, pc["buildings"][k]["size"], pc["current"][k], pc["targets"][k]))
    L.append("")
    L.append("Buffers: " + ", ".join("%s %s/%s" % (i, v["held"], v["target"]) for i, v in pc["buffers"].items()))
    for n in pc["notes"]:
        L.append("- " + n)
    return L + [""]
