"""Spare own labour (Oct 18, Taylor: "why aren't we making and using maxing free labor").

The farmstead's tenants give ~450 labour a turn for ~0.05 coin each. Whatever nothing draws expires at the end of the
turn. Since the Oct 18 garment-pile fix cut sewing, ~30-40 of it expired every turn. This puts that spare on storable
output instead, in order:
  1. the quarry (limestone, Taylor keeps the quarry for limestone; it pays its 20 tax a turn either way), until the
     limestone bin is within one run of full;
  2. the logging camp (timber, "we will always need timber"), from Taylor's base rate up to CAMP_MAX, while timber held
     is under TIMBER_STOP.
It is sized on the last turns' REAL use (made - used, adding back what this rule itself had added), minus a margin, so it
never makes us buy labour; when the chain needs its labour back the extra comes off by itself.

Pure functions here (no game calls); prestige_rules.spare_labour_rule() does the reads and writes.
"""
import math

MARGIN = 10            # labour left unassigned a turn (noise in use)
TURNS = 3              # spare = the smallest of the last TURNS turns
LABOUR_PER_RUN = {"quarry": 110.0, "camp": 3.1}     # extract stone 1: 110 labour -> 13 limestone; split timber 2: 3.1 -> 1.2
LIMESTONE_PER_RUN = 13.0
QUARRY_MAX = 1.0       # the quarry is one plot
CAMP_BASE = 7.0        # Taylor, Oct 16: camp 10 -> 7 to match timber sales
CAMP_MAX = 20.0
TIMBER_STOP = 650      # bin is 711


def spare_from_history(rows, extra_by_turn, turns=TURNS):
    """rows: history lines (dicts with 'turn' and items.labour = [held, made, used, sold, bought, expired, price]),
    one per game turn, oldest first. extra_by_turn: {turn: labour this rule had added for that turn}.
    Returns the smallest 'made - (used - extra)' over the last `turns` turns, or None without enough data."""
    vals = []
    for r in rows[-turns:]:
        lab = ((r.get("items") or {}).get("labour")) or []
        if len(lab) < 3:
            continue
        made, used = float(lab[1] or 0), float(lab[2] or 0)
        vals.append(made - (used - float(extra_by_turn.get(str(r.get("turn")), 0) or 0)))
    if len(vals) < turns:
        return None
    return min(vals)


def allocate(spare, lime_held, lime_cap, timber_held, quarry_floor=0.0, camp_slowed=False, margin=MARGIN):
    """Targets for the quarry and the camp from `spare` own labour a turn.
    quarry_floor: what the quarry rule wants anyway (its labour is not spare-funded). Returns a dict with the quarry
    target, the camp target, the spare-funded labour and a reason."""
    avail = max(0.0, (spare or 0.0) - margin)
    q_extra, why = 0.0, []
    room = (lime_cap - lime_held) if lime_cap else 0.0
    if avail > 0 and room > LIMESTONE_PER_RUN:
        q_extra = min(QUARRY_MAX - quarry_floor, avail / LABOUR_PER_RUN["quarry"])
        q_extra = max(0.0, math.floor(q_extra * 20) / 20.0)          # 0.05 steps
        avail -= q_extra * LABOUR_PER_RUN["quarry"]
        if q_extra:
            why.append("quarry +%.2f (limestone %.0f of %.0f)" % (q_extra, lime_held, lime_cap))
    elif room <= LIMESTONE_PER_RUN:
        why.append("limestone bin full (%.0f of %.0f)" % (lime_held, lime_cap))
    c_extra = 0.0
    if avail > 0 and not camp_slowed and timber_held < TIMBER_STOP:
        c_extra = min(CAMP_MAX - CAMP_BASE, avail / LABOUR_PER_RUN["camp"])
        c_extra = max(0.0, math.floor(c_extra * 2) / 2.0)             # 0.5 steps
        avail -= c_extra * LABOUR_PER_RUN["camp"]
        if c_extra:
            why.append("camp +%.1f (timber %.0f, stop %d)" % (c_extra, timber_held, TIMBER_STOP))
    elif camp_slowed:
        why.append("camp held by the tool guard")
    elif timber_held >= TIMBER_STOP:
        why.append("timber %.0f at its stop %d" % (timber_held, TIMBER_STOP))
    used = q_extra * LABOUR_PER_RUN["quarry"] + c_extra * LABOUR_PER_RUN["camp"]
    return {"quarry": round(quarry_floor + q_extra, 2), "quarry_extra": q_extra, "camp": CAMP_BASE + c_extra,
            "camp_extra": c_extra, "labour": round(used, 1),
            "why": "spare own labour %.0f (margin %d): %s" % (spare or 0.0, margin, "; ".join(why) or "nothing to add")}
