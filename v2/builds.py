"""Bot v2 build manager (shadow): buy a building's materials once, then switch the buys off.

For every building under construction it works out what is still to be delivered, buys only the shortfall of
storable materials (once: the shortfall shrinks as stock arrives, and the buy stops itself at max_holding), and
meters out perishable ones (labour) per turn so they are bought in the turns the site can use them, not months early.

Assumption, stated because the snapshot can't prove it: a site draws its materials in proportion to progress, so
remaining = full cost x (1 - progress/100). shadow.py logs each site's progress in history.jsonl; if stock draw per
turn doesn't match the progress made, this is the line to fix.

Pure functions over the snapshot; never touches the game.
"""
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def _data():
    with open(os.path.join(HERE, "data", "buildings.json")) as f:
        return json.load(f)


def scan_sites(s, cfg, data=None):
    """Sites under construction and what each still needs: [{building, type, progress, turns_left, remaining{}, notes[]}].
    Material lists come from config 'builds' (an override per building type), else from the game data."""
    data = data if data is not None else _data()
    sites = []
    for b in s.get("buildings") or []:
        cons = b.get("construction")
        if not cons or (cons.get("progress") or 0) >= 100:
            continue
        spec = (data.get(b.get("type")) or {}).get("construction") or {}
        mats = (cfg.get("builds") or {}).get(b.get("type")) or spec.get("materials")
        site = {"building": b.get("name"), "type": b.get("type"), "progress": cons.get("progress") or 0.0,
                "stage": cons.get("stage"), "remaining": {}, "notes": []}
        if not mats:
            site["notes"].append("no material list for this building type")
            sites.append(site)
            continue
        left = max(0.0, 1.0 - site["progress"] / 100.0)
        site["turns_left"] = max(1, math.ceil((spec.get("time") or 0) * left))
        for item, total in mats.items():
            if math.ceil(total * left) > 0:
                site["remaining"][item] = math.ceil(total * left)
        if spec.get("discount"):
            site["notes"].append("game data lists a %s discount on this build; not applied, so this buys slightly more than needed"
                                 % spec["discount"])
        sites.append(site)
    return sites


def plan_builds(sites, s, cfg, items, market, use, snap_price):
    """Turn the sites into one-off buys of storable materials plus a per-turn drip of perishables.

    use = what the running business consumes per turn (so build stock sits on top of the chain's own runway).
    Returns {"sites", "buys": {item: {...}}, "drip": {item: per-turn}, "ready": [site names]}."""
    per = set(cfg.get("perishable") or [])
    runway = cfg.get("runway_turns") or {}
    ceil_ = cfg.get("buy_ceiling") or {}
    cash = s.get("cash") or 0
    budget = max(0.0, cash - (cfg.get("cash") or {}).get("reserve", 0))
    per_buy = (cfg.get("cash") or {}).get("max_single_buy_share", 0.2) * cash

    need = {}
    for site in sites:
        for item, n in site["remaining"].items():
            if item not in per:
                need[item] = need.get(item, 0) + n

    buys = {}
    for item, n_need in sorted(need.items()):
        it = items.get(item) or {}
        held = it.get("held", 0.0)
        used = max(use.get(item, 0), (it.get("flow") or {}).get("consumption", 0))     # recipes miss some real use (timber)
        keep = math.ceil(used * runway.get(item, runway.get("_default", 4)))
        spare = max(0.0, held - keep)
        deficit = max(0, math.ceil(n_need - spare))
        e = {"need": n_need, "held": round(held, 1), "keep_for_chain": keep, "deficit": deficit}
        m = market.get(item) or {}
        ask, cap = m.get("ask"), ceil_.get(item)
        if deficit == 0:
            e["action"] = "off"                  # covered: no build buy needed
        elif not ask:
            e.update(action="blocked", why="no sellers at home: import it")
        elif cap and ask > cap:
            e.update(action="blocked", why="home ask %.2f is above our ceiling %.2f" % (ask, cap))
        else:
            price = snap_price(cap if cap else ask * 1.05, up=False)   # a limit: trades clear at the market (planner.py)
            vol = min(deficit, int(min(per_buy, budget) // price)) if price else 0
            e.update(action="buy" if vol > 0 else "blocked", buy_volume=vol, buy_price=str(price),
                     max_holding=keep + n_need,   # the order stops itself here: bought once
                     cost=round(vol * price))
            if vol < deficit:
                e["why"] = "cash guard: %d of %d this turn (reserve and single-buy share)" % (vol, deficit)
            budget -= vol * price
        buys[item] = e

    # a site can only use labour once its storable materials are covered; before that, labour would just expire
    ready, drip = [], {}
    for site in sites:
        stor = [i for i in site["remaining"] if i not in per]
        site["ready"] = bool(site["remaining"]) and all((buys.get(i) or {}).get("deficit", 0) == 0 for i in stor)
        if site["ready"]:
            ready.append(site["building"])
            for item, n in site["remaining"].items():
                if item in per:
                    drip[item] = drip.get(item, 0) + math.ceil(n / site["turns_left"])
    return {"sites": sites, "buys": buys, "drip": drip, "ready": ready}


def annotate(bp, orders, items):
    """Once the planner's own orders exist: which build buys v1 has live that nothing needs any more."""
    for item, e in bp["buys"].items():
        live = any(o.get("buy_price") or o.get("buy_volume") for o in (items.get(item) or {}).get("orders") or [])
        wanted_elsewhere = bool((orders.get(item) or {}).get("buy"))
        e["v1_buy_live"] = live
        if e["action"] == "off" and live and not wanted_elsewhere:
            e["switch_off"] = True               # materials are in: v1's standing buy can go
    return bp
