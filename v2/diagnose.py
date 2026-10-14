"""Bot v2 self-diagnosis: catch the quiet problems a human check used to find, propose a fix, apply it inside caps.

Built Oct 14 after a human check on Oct 13 found four problems the bot had not noticed:
  - the candle luxury slot ran dry for ~10 turns (our bid 70 under the home ask 80.50; prestige +4.1 -> +0.6 a turn),
    and the light armour gear slot sat paused by the failsafe since Oct 11;
  - the quarry made 0 for hours: "limestone space", a limestone buy (max_holding 153 = capacity) refilled the bin first;
  - the ropewalk finished construction and sat idle with no recipe;
  - starting the ropewalk ramped the textile chain and the extra labour starved the banquet, camp, quarry and ropewalk.

Rules (each: detect -> propose -> apply within caps -> log + report):
  R1 prestige slot dry   a good a prestige slot consumes (household sustenance slots from v2/data/sustenance.json,
                         inputs of running prestige recipes such as the banquet) held under 2 turns of use while its
                         buy did not fill last turn -> buy at the home ask +1.5% (snapped up to the price grid),
                         capped by coin_per_prestige_cap x the prestige a unit gives and 5% of cash a turn; un-pauses a
                         failsafe-paused buy only at failsafe level 0. Also: prestige rate > 2 a turn under its 12-turn
                         median -> a finding naming the likely cause (dry slot, prestige building at 0, contract penalty).
  R2 space-blocked       a building limited by "<item> space" while a store buy on that item exists -> lower the buy's
                         max_holding to capacity - 3 turns of our own output (never below 0); otherwise a finding.
  R3 finished idle       construction done, no recipe or target 0 for 2+ turns -> config planned_recipes[type] started
                         at 0.5 with the storehouse as provider (only for a building that never had a recipe, or one
                         nobody switched off on purpose in the last 12 hours); otherwise a finding.
  R4 priority starved    mansion/park/logging camp/quarry/ropewalk projected 0 with target > 0 and limited by labour ->
                         lower sewing, then weaving, by up to 25% (reduce only; labour is never raised here).
  R5 buy not filling     a buy whose bid sat under the home ask 3+ turns, under-filled last turn, with < 3 turns of
                         use held -> a finding; auto-raise only for an input of a running building, under its config
                         buy ceiling and 5% of cash. Labour is never raised.
Guards: failsafe level > 0 or quiet hours (23:00-07:00 Toronto) -> reduce-only; never prestige spends, contracts,
sell/donate/demolish, or the token; ship trade goods are never touched; v2-owned items are written directly (merge
into the live tiers, re-read, verify), v1 items only through the order queue's handler + spend guard + log
(source "v2-diagnose"); one action per item/building per 2 turns; at most MAX_ACTIONS a run.

diagnose() is pure (snapshot + context in, findings + actions out). run() applies them; v2/act.py calls it.
"""
import datetime
import json
import math
import os
import statistics

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

DRY_TURNS = 2              # R1: a slot with less than this many turns of use held is "dry"
RATE_DROP = 2.0            # R1b: prestige rate this far under its 12-turn median
RATE_WINDOW = 12
SPACE_TURNS = 3            # R2: room left in the bin for this many turns of our own output
IDLE_TURNS = 2             # R3
START_TARGET = 0.5         # R3
PRIORITY = ("mansion", "park", "logging camp", "quarry", "ropewalk")
TEXTILE_CUTS = ("sewing shop", "weavery")    # R4: lowered in this order
MAX_CUT = 0.25
R4_FLOOR = 0.5             # R4 never takes a textile step under half its target at the first cut
UNDER_ASK_TURNS = 3        # R5
LOW_TURNS = 3              # R5
CASH_SHARE = 0.05
BID_OVER_ASK = 1.015
COOLDOWN_TURNS = 2
MAX_ACTIONS = 4
QUIET = (23, 7)


def _n(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return 0.0


def snap_up(p):
    """The game's price grid: 3 significant digits, 2-4 leading -> even last digit, 5-9 -> 0 or 5. Rounds up."""
    if not p or p <= 0:
        return 0.0
    e = math.floor(math.log10(p) + 1e-12) - 2
    lead = int(p / 10 ** (e + 2) + 1e-9)
    step = max(10 ** e * (5 if lead >= 5 else 2 if lead >= 2 else 1), 0.01)
    return round(math.ceil(p / step - 1e-9) * step, 6)


def price_str(p):
    s = ("%.2f" % p).rstrip("0").rstrip(".")
    return s


def quiet_now(now=None):
    from zoneinfo import ZoneInfo
    h = (now or datetime.datetime.now(datetime.timezone.utc)).astimezone(ZoneInfo("America/Toronto")).hour
    return h >= QUIET[0] or h < QUIET[1]


def load_data(name):
    try:
        with open(os.path.join(HERE, "data", name)) as f:
            return json.load(f)
    except (OSError, ValueError):
        return {} if name != "sustenance.json" else []


# ---------------------------------------------------------------- helpers over the snapshot
def _buy_tier(tiers):
    for i, t in enumerate(tiers or []):
        if _n(t.get("buy_volume")) > 0 or t.get("buy_price") not in (None, "", "0"):
            return i, t
    return None, None


def _use(snap, item):
    """Units a turn: the store's consumption last turn, or the median of the last 6 turns of observed use."""
    it = ((snap.get("store") or {}).get("items") or {}).get(item) or {}
    last = _n((it.get("flow") or {}).get("consumption"))
    hist = [x for x in ((snap.get("history_use") or {}).get(item) or [])[-6:] if x]
    return max(last, statistics.median(hist) if hist else 0.0)


def prestige_slots(snap, sustenance, recipes):
    """{item: {"prestige": per turn, "use": units per turn, "why": text}} for every good a prestige slot consumes."""
    out = {}

    def add(item, prestige, use, why):
        o = out.setdefault(item, {"prestige": 0.0, "use": 0.0, "why": []})
        o["prestige"] += prestige
        o["use"] += use
        o["why"].append(why)
    eaten = snap.get("sustenance") or {}
    slots = set(snap.get("sustenance_slots") or [])
    hist = snap.get("history_use") or {}
    # apprentices add 20% each to the household's use, except gear and luxuries (game client)
    mult = 1 + 0.2 * max(0, len((snap.get("household") or {}).get("workers") or []) - 1)
    for grp in sustenance or []:
        cat = grp.get("category")
        for p in grp.get("products") or []:
            item = p.get("product")
            if _n(p.get("score")) <= 0:
                continue
            # a slot that ran dry eats nothing, so it drops out of last turn's consumption: also take the household's
            # slot list, or (older snapshots) a gear/luxury good the store fed in the last 12 turns
            in_slot = _n(eaten.get(item)) > 0 or item in slots or \
                (not snap.get("sustenance_slots") and cat in ("gear", "luxury") and any(_n(x) > 0 for x in (hist.get(item) or [])[-12:]))
            if not in_slot:
                continue
            use = max(_n(eaten.get(item)), _n(p.get("volume")) * (1 if cat in ("gear", "luxury") else mult))
            add(item, _n(p["score"]), use, "%s slot (+%s prestige)" % (cat, p["score"]))
    for b in snap.get("buildings") or []:
        r = recipes.get(b.get("recipe") or "") or {}
        if not r.get("prestige") or _n(b.get("target")) <= 0 or b.get("construction"):
            continue
        for i in r.get("inputs") or []:
            if i.get("product") in ("labour",):
                continue
            add(i["product"], _n(r["prestige"]) * _n(b["target"]), _n(i["amount"]) * _n(b["target"]),
                "%s %s (+%s prestige)" % (b.get("name"), b.get("recipe"), r["prestige"]))
    return out


def _running_inputs(snap, recipes):
    used = set()
    for b in snap.get("buildings") or []:
        if _n(b.get("target")) > 0 and not b.get("construction"):
            for i in (recipes.get(b.get("recipe") or "") or {}).get("inputs") or []:
                used.add(i.get("product"))
    return used


def _output(snap, recipes, item):
    tot = 0.0
    for b in snap.get("buildings") or []:
        for o in (recipes.get(b.get("recipe") or "") or {}).get("outputs") or []:
            if o.get("product") == item:
                tot += _n(o.get("amount")) * _n(b.get("target"))
    return tot


# ---------------------------------------------------------------- the rules (pure)
def diagnose(snap, cfg, ctx):
    """ctx: live_tiers {item: tiers}, owned set, trade set, paused {item: tiers}, fs_level, quiet, rates [(turn, rate)],
    state (diagnose_state, mutated: counters), recipes, sustenance, manual(item)->bool, building_touched(id)->bool.
    Returns (findings, actions). A finding: {rule, item|building, finding}; an action is a finding plus "action"
    (text), "raise" (bool), "via" ("direct" | "queue"), and "entry" (queue entry) or "managers" (direct store write)."""
    dcfg = (cfg or {}).get("diagnose") or {}
    cpp = _n(dcfg.get("coin_per_prestige_cap") or 60)
    planned = (cfg or {}).get("planned_recipes") or {}
    priority = tuple(dcfg.get("priority_buildings") or PRIORITY)
    recipes, sust = ctx.get("recipes") or {}, ctx.get("sustenance") or []
    live = ctx.get("live_tiers") or {}
    st = ctx.setdefault("state", {})
    turn = snap.get("turn") or 0
    cash = _n(snap.get("cash"))
    items = (snap.get("store") or {}).get("items") or {}
    market = snap.get("market") or {}
    store = (snap.get("store") or {}).get("id")
    ops = snap.get("operations") or {}
    owned, trade = set(ctx.get("owned") or ()), set(ctx.get("trade") or ())
    paused = ctx.get("paused") or {}
    fs_level = int(_n(ctx.get("fs_level")))
    reduce_only = fs_level > 0 or bool(ctx.get("quiet"))
    why_reduce = "failsafe level %d" % fs_level if fs_level > 0 else "quiet hours (23:00-07:00 Toronto)"
    manual = ctx.get("manual") or (lambda item: False)
    touched = ctx.get("building_touched") or (lambda bid: False)
    last_act = st.setdefault("last_action", {})
    findings, actions = [], []

    def note(rule, key, kind, text):
        f = {"rule": rule, kind: key, "finding": text}
        findings.append(f)
        return f

    def propose(f, action, raise_, via, entry=None, managers=None):
        key = f.get("item") or f.get("building")
        if raise_ and reduce_only:
            f["held_back"] = "%s: reduce-only, would %s" % (why_reduce, action)
            return
        if raise_ and key == "labour":
            f["held_back"] = "labour is never raised by diagnose"
            return
        if turn - last_act.get(key, -99) < COOLDOWN_TURNS:
            f["held_back"] = "acted on %s at turn %s (one action per 2 turns)" % (key, last_act[key])
            return
        if f.get("item") and manual(key):
            f["held_back"] = "changed by hand through the queue in the last 2 hours"
            return
        f.update(action=action, raise_=raise_, via=via)
        if entry is not None:
            f["entry"] = entry
        if managers is not None:
            f["managers"] = managers
        actions.append(f)

    def store_fix(f, item, tier_idx, sets, text, raise_):
        """A store order change: direct for v2-owned items, the queue for v1's, never for ship trade goods."""
        if item in trade:
            f["held_back"] = "ship trade good (v2 ships own it): finding only"
            return
        cur = [dict(t) for t in live.get(item) or []]
        if item in owned:
            if tier_idx is None or tier_idx >= len(cur):
                cur.append({})
                tier_idx = len(cur) - 1
            cur[tier_idx].update(sets)
            propose(f, text, raise_, "direct", managers=cur)
        else:
            e = {"item": item, "tier": len(cur) if tier_idx is None else tier_idx, "set": sets,
                 "note": "v2 diagnose %s: %s" % (f["rule"], text)}
            if store:
                e["building"] = store
            propose(f, text, raise_, "queue", entry=e)

    # ---- R1: prestige slots running dry
    slots = prestige_slots(snap, sust, recipes)
    dry = []
    for item, s in sorted(slots.items()):
        use = max(s["use"], 1e-9)
        it = items.get(item) or {}
        held = _n(it.get("held"))
        if held >= DRY_TURNS * use:
            continue
        i, tier = _buy_tier(live.get(item))
        vol = _n((tier or {}).get("buy_volume"))
        bought = _n((it.get("flow") or {}).get("purchase"))
        if vol > 0 and bought >= 0.8 * min(vol, use):
            continue                                    # it filled: stock is on its way
        dry.append(item)
        ask = (market.get(item) or {}).get("ask")
        cap_unit = cpp * s["prestige"] / use
        bid_now = _n((tier or {}).get("buy_price"))
        is_paused = item in paused and vol <= 0
        f = note("R1", item, "item", "%s slot dry: %.1f held, %.1f a turn (%s); our buy %s, home ask %s" % (
            item, held, use, "; ".join(s["why"]), ("%g @ %s" % (vol, (tier or {}).get("buy_price"))) if vol else
            ("paused by the failsafe" if is_paused else "none"), ask if ask else "none (no sellers at home)"))
        if not ask:
            continue
        bid = snap_up(max(_n(ask) * BID_OVER_ASK, _n(ask) + 0.01))
        if vol > 0 and bid_now >= _n(ask):
            f["finding"] += "; our bid is already at/over the ask (sellers too thin)"
            continue
        if bid > cap_unit:
            f["finding"] += "; ask over the cap %.1f (%g coin per prestige)" % (cap_unit, cpp)
            continue
        if is_paused and fs_level != 0:
            f["held_back"] = "paused by the failsafe at level %d: un-pause only at level 0" % fs_level
            continue
        base = dict(tier or {})
        if is_paused:
            pt = _buy_tier(paused.get(item))[1] or {}
            base = {k: pt[k] for k in ("buy_volume", "max_holding") if k in pt}
        want_vol = int(max(_n(base.get("buy_volume")), math.ceil(DRY_TURNS * use)))
        want_vol = min(want_vol, int(CASH_SHARE * cash / bid)) if bid else 0
        if want_vol < 1:
            f["finding"] += "; 5%% of cash does not buy one at %s" % price_str(bid)
            continue
        sets = {"buy_volume": want_vol, "buy_price": price_str(bid)}
        if not base.get("max_holding"):
            cap_room = _n(it.get("capacity")) or 1e9
            sets["max_holding"] = int(min(cap_room, math.ceil(4 * use + want_vol)))
        text = "%sbuy %d @ %s (ask %s, cap %.1f)" % ("un-pause and " if is_paused else "", want_vol, price_str(bid), ask, cap_unit)
        store_fix(f, item, i, sets, text, True)
        if is_paused:
            f["unpause"] = True

    # R1b: prestige rate well under its 12-turn median
    rate = (snap.get("household") or {}).get("rate")
    by_turn = {}
    for t, r in ctx.get("rates") or []:
        if t is not None and t < turn:
            by_turn[t] = r
    hist = [by_turn[t] for t in sorted(by_turn)[-RATE_WINDOW:]]
    if rate is not None and len(hist) >= 6:
        med = statistics.median(hist)
        if _n(rate) < med - RATE_DROP:
            causes = ["dry slot: %s" % ", ".join(dry)] if dry else []
            for b in snap.get("buildings") or []:
                r = recipes.get(b.get("recipe") or "") or {}
                op = ops.get("producer/%s" % b.get("id")) or {}
                if r.get("prestige") and _n(b.get("target")) > 0 and op and _n(op.get("volume")) <= 1e-6:
                    causes.append("%s projected 0 (%s)" % (b.get("name"), op.get("limitation") or "no reason given"))
            for k, v in ((snap.get("household") or {}).get("impacts") or {}).items():
                if "contract" in k and _n(v) < 0:
                    causes.append("contract penalty %s" % v)
            note("R1", "prestige", "item", "prestige rate %+.2f a turn vs 12-turn median %+.2f; likely: %s" % (
                _n(rate), med, "; ".join(causes) or "no slot, building or contract cause found: check the impacts"))

    # ---- R2: own producer blocked by a full bin
    for b in snap.get("buildings") or []:
        op = ops.get("producer/%s" % b.get("id")) or {}
        lim = op.get("limitation") or b.get("limitation") or ""
        if not lim.endswith(" space") or _n(b.get("target")) <= 0:
            continue
        item = lim[:-len(" space")]
        it = items.get(item) or {}
        capn, held = _n(it.get("capacity")), _n(it.get("held"))
        out = _output(snap, recipes, item)
        want_mh = max(0, int(capn - SPACE_TURNS * out))
        i, tier = _buy_tier(live.get(item))
        f = note("R2", b.get("name"), "building", "%s blocked by %s: %.0f held of %.0f capacity, we make %.1f a turn" % (
            b.get("name"), lim, held, capn, out))
        f["item"] = item
        if tier and _n(tier.get("buy_volume")) > 0 and (tier.get("max_holding") is None or _n(tier["max_holding"]) > want_mh):
            text = "%s buy max_holding %s -> %d (capacity %.0f - 3 turns of our %.1f)" % (
                item, tier.get("max_holding"), want_mh, capn, out)
            store_fix(f, item, i, {"max_holding": want_mh}, text, False)
        else:
            f["finding"] += "; %s: add a sell order or more capacity for %s" % (
                ("buy already stops at %s" % tier.get("max_holding")) if tier and _n(tier.get("buy_volume")) > 0 else "no buy on it",
                item)

    # ---- R3: finished building left idle
    idle = st.setdefault("idle", {})
    seen = set()
    for b in snap.get("buildings") or []:
        bid = str(b.get("id"))
        if b.get("construction") or (b.get("recipe") and _n(b.get("target")) > 0):
            continue
        seen.add(bid)
        c = idle.setdefault(bid, {"first": turn, "turns": []})
        if turn not in c["turns"]:
            c["turns"] = (c["turns"] + [turn])[-6:]
        if len(c["turns"]) < IDLE_TURNS:
            continue
        rec = planned.get(b.get("type"))
        f = note("R3", b.get("name"), "building", "%s (%s) finished but idle %d turns (%s)" % (
            b.get("name"), b.get("type"), len(c["turns"]), "no recipe" if not b.get("recipe") else "%s at 0" % b["recipe"]))
        f["building_id"] = bid
        if not rec:
            f["finding"] += "; no planned recipe for a %s: Taylor's call" % b.get("type")
            continue
        if b.get("recipe") and touched(bid):
            f["finding"] += "; switched off on purpose in the last 12 hours: left alone"
            continue
        e = {"building": bid, "producer": {"recipe": rec, "target": START_TARGET, "provider_id": store},
             "note": "v2 diagnose R3: finished building idle, start %s at %s" % (rec, START_TARGET)}
        propose(f, "start %s at %s (storehouse provider)" % (rec, START_TARGET), True, "queue", entry=e)
    for bid in list(idle):
        if bid not in seen:
            del idle[bid]

    # ---- R4: a priority building projected at 0
    starved, labour_need = [], 0.0
    for b in snap.get("buildings") or []:
        if b.get("type") not in priority:
            continue
        op = ops.get("producer/%s" % b.get("id")) or {}
        tgt = _n(op.get("target") if op else b.get("target"))
        if not op or tgt <= 0 or _n(op.get("volume")) > 1e-6:
            continue
        lim = op.get("limitation") or "no reason given"
        if lim == "labour":
            starved.append(b.get("name"))
            r = recipes.get(op.get("recipe") or b.get("recipe") or "") or {}
            labour_need += sum(_n(i["amount"]) for i in r.get("inputs") or [] if i.get("product") == "labour") * tgt
        elif not lim.endswith(" space"):            # space is R2's; a missing input is R1/R5's
            note("R4", b.get("name"), "building", "%s projected 0 of %g (limited by %s)" % (b.get("name"), tgt, lim))
    r4_base = st.setdefault("r4_base", {})
    if not starved:
        r4_base.clear()
    if starved:
        f = note("R4", ", ".join(starved), "building", "%s projected 0: short of labour (~%.0f needed)" % (
            ", ".join(starved), labour_need))
        left = labour_need
        for site in TEXTILE_CUTS:
            if left <= 0:
                break
            for b in snap.get("buildings") or []:
                if b.get("type") != site or _n(b.get("target")) <= 0 or left <= 0:
                    continue
                r = recipes.get(b.get("recipe") or "") or {}
                per = sum(_n(i["amount"]) for i in r.get("inputs") or [] if i.get("product") == "labour")
                if per <= 0:
                    continue
                base = r4_base.setdefault(str(b.get("id")), _n(b["target"]))
                # never under half of where it stood at the first cut: repeated cuts while the balancer leaves it alone
                # would otherwise walk the chain toward 0
                cut = min(MAX_CUT * _n(b["target"]), left / per, max(0.0, _n(b["target"]) - R4_FLOOR * base))
                new = round(_n(b["target"]) - cut, 3)
                if cut < 0.01:
                    continue
                left -= cut * per
                g = {"rule": "R4", "building": b.get("name"), "building_id": str(b.get("id")),
                     "finding": "lower %s to free labour for %s" % (b.get("name"), ", ".join(starved))}
                e = {"building": str(b.get("id")), "producer": {"recipe": b.get("recipe"), "target": new},
                     "note": "v2 diagnose R4: %s projected 0 (labour); %s %.3f -> %.3f" % (", ".join(starved), b.get("name"), _n(b["target"]), new)}
                propose(g, "%s %s %.3f -> %.3f (frees ~%.0f labour)" % (b.get("name"), b.get("recipe"), _n(b["target"]), new, cut * per),
                        False, "queue", entry=e)
                if g.get("held_back"):
                    f["finding"] += "; %s" % g["held_back"]
        f["finding"] += "; labour itself is not raised here"

    # ---- R5: a buy that sits under the ask and does not fill
    under = st.setdefault("under_ask", {})
    inputs_running = _running_inputs(snap, recipes)
    household = set(snap.get("sustenance") or {})
    perishable = set((cfg or {}).get("perishable") or [])
    ceilings = (cfg or {}).get("buy_ceiling") or {}
    for item, tiers in sorted(live.items()):
        i, tier = _buy_tier(tiers)
        if tier is None or _n(tier.get("buy_volume")) <= 0 or item in dry:
            under.pop(item, None)
            continue
        ask, bidp = (market.get(item) or {}).get("ask"), _n(tier.get("buy_price"))
        c = under.setdefault(item, {"turns": []})
        if ask and bidp < _n(ask):
            if turn not in c["turns"]:
                c["turns"] = (c["turns"] + [turn])[-6:]
        else:
            under.pop(item, None)
            continue
        if len(c["turns"]) < UNDER_ASK_TURNS or not (item in inputs_running or item in household):
            continue
        it = items.get(item) or {}
        use = _use(snap, item)
        held, vol = _n(it.get("held")), _n(tier.get("buy_volume"))
        bought = _n((it.get("flow") or {}).get("purchase"))
        if use <= 0 or held >= LOW_TURNS * use or bought >= 0.8 * vol:
            continue
        f = note("R5", item, "item", "%s buy not filling: bid %s under the home ask %s for %d turns, bought %.1f of %g, %.1f held (%.1f turns)" % (
            item, tier.get("buy_price"), ask, len(c["turns"]), bought, vol, held, held / use))
        if item not in inputs_running or item in perishable:
            continue
        bid = snap_up(_n(ask) * BID_OVER_ASK)
        ceil_ = ceilings.get(item)
        if ceil_ is None or bid > _n(ceil_):
            f["finding"] += "; raise needs Taylor (ceiling %s)" % ceil_
            continue
        if bid * vol > CASH_SHARE * cash:
            f["finding"] += "; %g @ %s is over 5%% of cash" % (vol, price_str(bid))
            continue
        store_fix(f, item, i, {"buy_price": price_str(bid)}, "buy price %s -> %s (ask %s, ceiling %s)" % (
            tier.get("buy_price"), price_str(bid), ask, ceil_), True)

    acts = actions[:MAX_ACTIONS]
    for a in actions[MAX_ACTIONS:]:
        a["held_back"] = "action cap %d reached this run" % MAX_ACTIONS
        for k in ("action", "via", "entry", "managers"):
            a.pop(k, None)
    return findings, acts


# ---------------------------------------------------------------- applying (side effects)
def _canon(tiers):
    def v(x):
        try:
            return round(float(x), 4)
        except (TypeError, ValueError):
            return str(x)
    return json.dumps([{k: v(x) for k, x in sorted(t.items())} for t in tiers or []], sort_keys=True)


def _queue_apply(entry):
    import sys
    sys.path.insert(0, ROOT)
    import order_queue
    refuse = order_queue._spend_guard(entry, None) if entry.get("item") else None
    r = dict(ok=False, error=refuse) if refuse else order_queue.apply_entry(entry)
    order_queue.log(entry, r, source="v2-diagnose")
    return r


def _direct_store(store, item, managers):
    import api
    path = "/buildings/%s/storage/inventory/%s" % (store, api.q(item))
    ok, status, body = api.write("PATCH", path, {"managers": managers})
    b = api.get("/buildings/%s" % store) or {}
    got = (((((b.get("storage") or {}).get("inventory") or {}).get("holdings")) or {}).get(item) or {}).get("managers") or []
    got = [{k: v for k, v in t.items() if k != "result"} for t in got if t]
    good = bool(ok) and _canon(got) == _canon(managers)
    return {"ok": good, "status": status, "error": None if good else str(body)[:200]}


def report_lines(findings):
    if not findings:
        return ["## Self-diagnosis", "", "Nothing found this run.", ""]
    out = ["## Self-diagnosis", ""]
    for f in findings:
        tail = (" -> **%s** (%s)" % (f["action"], "ok" if f.get("ok") else "FAILED: %s" % f.get("error"))) if f.get("action") and "ok" in f \
            else (" -> would %s" % f["action"]) if f.get("action") else (" (held back: %s)" % f["held_back"]) if f.get("held_back") else ""
        out.append("- %s: %s%s" % (f["rule"], f["finding"], tail))
    return out + [""]


def alert_lines(findings):
    out = []
    for f in findings:
        s = "%s: %s" % (f["rule"], f["finding"])
        if f.get("action") and "ok" in f:
            s += " -> %s %s" % (f["action"], "ok" if f.get("ok") else "FAILED")
        out.append(s[:220])
    return out


def run(snap, cfg, ctx, live=False, out_dir=None, log_path=None, apply_queue=None, direct=None, now=None):
    """Diagnose, apply the actions (live only), log, and write state/v2/diagnose.json + the report section.
    Never raises (the caller wraps it too). Returns (findings, actions)."""
    out_dir = out_dir or os.path.join(ROOT, "state", "v2")
    log_path = log_path or os.path.join(out_dir, "act.jsonl")
    apply_queue = apply_queue or _queue_apply
    direct = direct or _direct_store
    now = now or datetime.datetime.now(datetime.timezone.utc)
    ts = now.isoformat(timespec="seconds")
    turn = (snap or {}).get("turn")
    st_path = os.path.join(out_dir, "diagnose_state.json")
    try:
        st = json.load(open(st_path))
    except (OSError, ValueError):
        st = {}
    ctx["state"] = st
    findings, actions = diagnose(snap or {}, cfg or {}, ctx)
    store = ((snap or {}).get("store") or {}).get("id")
    for a in actions:
        key = a.get("item") or a.get("building_id") or a.get("building")
        if not live:
            continue
        try:
            if a["via"] == "direct":
                r = direct(store, a["item"], a["managers"])
            else:
                r = apply_queue(a["entry"])
        except Exception as e:      # one failed action never stops the others
            r = {"ok": False, "error": "%s: %s" % (type(e).__name__, e)}
        a["ok"], a["error"] = bool(r.get("ok")), (None if r.get("ok") else str(r.get("error") or r.get("body") or r.get("status"))[:200])
        st.setdefault("last_action", {})[a.get("item") or a.get("building")] = turn
        if a.get("unpause") and a["ok"]:
            st.setdefault("unpaused", {})[a["item"]] = ts
    prev = set(st.get("open") or [])
    cur = ["%s|%s" % (f["rule"], f.get("item") or f.get("building")) for f in findings]
    if live:
        with open(log_path, "a") as fh:
            for f in findings:
                k = "%s|%s" % (f["rule"], f.get("item") or f.get("building"))
                if "ok" not in f and k in prev:
                    continue                    # an open finding is logged once, when it first appears
                fh.write(json.dumps({"ts": ts, "turn": turn, "diagnose": f["rule"],
                                     ("item" if f.get("item") else "building"): f.get("item") or f.get("building"),
                                     "building": f.get("building"), "finding": f["finding"],
                                     "action": f.get("action") or (("held back: " + f["held_back"]) if f.get("held_back") else None),
                                     "ok": f.get("ok")}, default=str) + "\n")
            fh.write(json.dumps({"ts": ts, "turn": turn, "diagnose": "run", "findings": len(findings),
                                 "actions": sum(1 for a in actions if "ok" in a),
                                 "ok": all(a.get("ok") for a in actions if "ok" in a)}, default=str) + "\n")
        st["open"] = cur
        st["t"] = ts
        with open(st_path, "w") as fh:
            json.dump(st, fh, indent=1, default=str)
            fh.write("\n")
    res = {"t": ts, "turn": turn, "mode": "live" if live else "dry", "reduce_only": ctx.get("fs_level", 0) > 0 or bool(ctx.get("quiet")),
           "findings": [{k: v for k, v in f.items() if k not in ("managers",)} for f in findings],
           "alerts": alert_lines(findings)}
    name = "diagnose.json" if live else "diagnose_dry.json"
    with open(os.path.join(out_dir, name), "w") as fh:
        json.dump(res, fh, indent=1, default=str)
        fh.write("\n")
    if live:
        rp = os.path.join(out_dir, "report.md")
        try:
            txt = open(rp).read()
            cut = txt.find("## Self-diagnosis")
            if cut >= 0:
                nxt = txt.find("\n## ", cut + 5)
                txt = txt[:cut] + (txt[nxt + 1:] if nxt >= 0 else "")
            with open(rp, "w") as fh:
                fh.write(txt.rstrip("\n") + "\n\n" + "\n".join(report_lines(findings)))
        except OSError:
            pass
    return findings, actions


def context(snap, cfg, live_tiers, owned, fs, history_glob=None, act_state=None, manual=None, now=None):
    """Build ctx from the repo files (history rates, failsafe paused, trade goods, done log)."""
    import glob
    rates = []
    for path in sorted(glob.glob(history_glob or os.path.join(ROOT, "history", "merc-*.jsonl")))[-1:]:
        try:
            with open(path, "rb") as f:
                f.seek(0, 2)
                f.seek(max(0, f.tell() - 400000))
                lines = f.read().decode(errors="ignore").splitlines()[1:]
            for ln in lines[-80:]:
                try:
                    r = json.loads(ln)
                    rates.append((r.get("turn"), _n(r.get("prestige_rate"))))
                except ValueError:
                    continue
        except OSError:
            pass
    trade = set(((act_state or {}).get("trade_items") or {}).keys())
    st_unp = {}
    try:
        st_unp = (json.load(open(os.path.join(ROOT, "state", "v2", "diagnose_state.json"))).get("unpaused") or {})
    except (OSError, ValueError):
        pass
    since = str((fs or {}).get("since") or "")
    paused = {k: v for k, v in ((fs or {}).get("paused") or {}).items() if not (k in st_unp and str(st_unp[k]) >= since)}

    def touched(bid, hours=12):
        try:
            lines = open(os.path.join(ROOT, "state", "order_queue_done.jsonl")).read().splitlines()[-300:]
        except OSError:
            return False
        cutoff = (now or datetime.datetime.now(datetime.timezone.utc)) - datetime.timedelta(hours=hours)
        for ln in lines:
            try:
                r = json.loads(ln)
                e = r.get("entry") or {}
                if str(e.get("building")) == str(bid) and e.get("producer") and r.get("ok") \
                        and datetime.datetime.fromisoformat(r["ts"]) >= cutoff:
                    return True
            except (ValueError, KeyError, TypeError):
                continue
        return False
    return {"live_tiers": live_tiers, "owned": set(owned), "trade": trade, "paused": paused,
            "fs_level": int(_n((fs or {}).get("level"))), "quiet": quiet_now(now), "rates": rates,
            "recipes": load_data("recipes.json"), "sustenance": load_data("sustenance.json"),
            "manual": manual, "building_touched": touched}
