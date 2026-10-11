"""Bot v2 prestige spending (shadow): every way of turning coin into prestige, ranked by coin per prestige,
plus the status of the agreed automatic purchases. Pure functions over the snapshot; never touches the game.

Ranking: each recipe in the game data that yields prestige (banquets, park upkeep, sermons, jousting ...), priced at
today's home market (last traded price, else ask, else our own unit cost). For a site we don't own yet the building's
construction materials are priced the same way and spread over the turns left after it is built, so a church that
costs 60k to build is compared fairly with a banquet that costs nothing to start.

Not modelled (not in the snapshot): church contracts, the best rate known (16-38 coin per prestige). The skill/unlock
needed for a higher tier is not checked either: a cheaper tier at a site we own is a candidate to look at, not an order.
"""
import datetime
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# Costs of the permanent purchases, as v1's prestige_rules.py has them (game tables). Buying level n costs:
#   tenants: 50 x (n - 3)  (v1: cost = 50 x (current level - 2) to go from level to level + 1)
#   prestige_management: PM_COSTS[n]     apprentices: APPRENTICE_COSTS[n - 1]
PM_COSTS = [0, 100, 250, 500, 1000, 2000, 3000, 5000, 10000]
APPRENTICE_COSTS = [50, 250, 1000, 2500, 5000, 7500, 10000]


def _buildings():
    with open(os.path.join(HERE, "data", "buildings.json")) as f:
        return json.load(f)


def turns_left(s, cfg):
    """Turns are hourly (checked against v1's history: 0.999 h/turn)."""
    try:
        end = datetime.datetime.fromisoformat(cfg["season_end"])
        now = datetime.datetime.fromisoformat((s.get("t") or "").replace("Z", "+00:00"))
        return max(0.0, (end - now).total_seconds() / 3600.0)
    except (KeyError, ValueError, TypeError):
        return None


def rank_sinks(s, cfg, recipes, items, market, make, data=None):
    data = data if data is not None else _buildings()
    R = turns_left(s, cfg)
    owned = {b.get("type") for b in s.get("buildings") or [] if not b.get("construction")}
    running = {}
    for b in s.get("buildings") or []:
        r = recipes.get(b.get("recipe") or "")
        if r and r.get("prestige") and (b.get("target") or 0) > 0:
            running[(b.get("type"), b.get("recipe"))] = b.get("name")

    def price(item):
        m = market.get(item) or {}
        return m.get("price") or m.get("ask") or m.get("bid") or (items.get(item) or {}).get("unit_cost") or None

    def cost(mats):
        total, missing = 0.0, []
        for item, n in mats.items():
            p = price(item)
            if p is None:
                missing.append(item)
            else:
                total += n * p
        return total, missing

    capex = {}
    rows = []
    for name, r in recipes.items():
        if not r.get("prestige") or not r.get("site"):
            continue
        site = r["site"]
        op, missing = cost({i["product"]: i["amount"] for i in r.get("inputs") or []})
        thin = [i["product"] for i in r.get("inputs") or []
                if i["product"] not in make and i["product"] != "labour"
                and (market.get(i["product"]) or {}).get("ask_vol", 0) < 0.5 * i["amount"]]
        row = {"sink": name, "site": site, "owned": site in owned, "running": (site, name) in running,
               "prestige_per_turn": r["prestige"], "coin_per_prestige": None, "effective": None,
               "capex": None, "class": r.get("class"), "missing": missing, "thin": thin}
        if not missing:
            row["coin_per_prestige"] = round(op / r["prestige"], 1)
            row["effective"] = row["coin_per_prestige"]
            if site not in owned:
                if site not in capex:
                    con = (data.get(site) or {}).get("construction") or {}
                    cc, cmiss = cost(con.get("materials") or {})
                    capex[site] = (None if (cmiss or not con.get("materials")) else cc, con.get("time") or 0)
                cc, build_time = capex[site]
                row["capex"] = None if cc is None else round(cc)
                T = (R - build_time) if R is not None else None
                if cc is not None and T and T > 0:
                    row["effective"] = round((op * T + cc) / (r["prestige"] * T), 1)
                else:
                    row["effective"] = None          # unknown capex, or too late for it to pay back
        rows.append(row)
    ranked = sorted((r for r in rows if r["effective"] is not None), key=lambda r: (r["effective"], r["sink"]))
    return {"turns_left": R, "legacy_factor": (1 - 0.995 ** R) if R is not None else None,
            "ranked": ranked, "unpriced": sorted((r["sink"] for r in rows if r["missing"]))}


def agreed_status(s, cfg):
    """Status of each agreed permanent purchase: done | ready | waiting (turns to afford at today's prestige income)."""
    hh = s.get("household") or {}
    levels, free, rate = hh.get("levels") or {}, hh.get("free") or 0.0, hh.get("rate") or 0.0
    out = []
    for a in (cfg.get("prestige") or {}).get("agreed") or []:
        track, to = a.get("sink"), a.get("to_level")
        cur = levels.get(track)
        e = {"sink": track, "to_level": to, "level": cur}
        if cur is None or to is None:
            e.update(status="unknown", detail="no level in the snapshot for %s" % track)
        elif cur >= to:
            e.update(status="done", detail="level %d (agreed %d)" % (cur, to))
        else:
            n = cur + 1
            try:       # look up only this track: the other tables are shorter and would run off their end
                cost = (50 * (n - 3) if track == "tenants" else PM_COSTS[n] if track == "prestige_management"
                        else APPRENTICE_COSTS[n - 1] if track == "apprentices" else None)
                if cost is None:
                    raise KeyError(track)
            except (KeyError, IndexError):
                e.update(status="unknown", detail="no cost table for %s level %d" % (track, n))
                out.append(e)
                continue
            e["cost"] = cost
            if free >= cost and rate > 0:
                e.update(status="ready", detail="level %d for %d prestige (free %.0f)" % (n, cost, free))
            elif rate > 0:
                e.update(status="waiting", detail="level %d costs %d, free %.0f: ~%d turns at %+.1f/turn" % (
                    n, cost, free, math.ceil((cost - free) / rate), rate))
            else:
                e.update(status="waiting", detail="level %d costs %d, free %.0f and prestige income is not positive" % (n, cost, free))
        out.append(e)
    return out
