#!/usr/bin/env python3
"""Contract scorer (Oct 9 2026): one score for every open offer in town, money deals and church
(prestige) deals alike. Replaces alerts.py's church-only check and covers what the Ops panel's
scoreContract() does (money only) plus prestige.

  church offer (they want goods, pay prestige):
      cost   = volume x cheapest way to get it (what we hold at its unit cost, else the cheapest
               world ask; home ask preferred when there is one)
      value  = coin per prestige = cost / bonus, against the mansion banquet's ~57 coin/prestige
      risk   = penalty (prestige) if we can't fill it in time: can we fill from stock now,
               from our own production in the timeframe, or only from thin markets?
  money offer (they buy or sell goods for coin):
      edge   = (their price - home bid) x volume when they buy from us,
               (home ask - their price) x volume when they sell to us
  verdict (church): GOOD = fillable now from stock and worth it (auto-filled); WAIT = worth it but not
           fillable now (stockpile, never sign); POOR / SKIP = not worth it
  verdict (money): GOOD / OK / POOR / SKIP on the edge vs home prices

Writes state/contracts_scored.json and returns the list; alerts.py puts GOOD/OK ones in the email.
RULE (Taylor, Oct 9): a prestige (church) contract is only ever signed if we can fill it IMMEDIATELY,
in full, from stock. That binds everyone: the bot, the daily check-in, Claude in chat. So no signing
an offer and then buying or shipping to fill it. Offers we can't fill yet are marked WAIT with what's
missing (a reason to stockpile, never to sign); auto-fill accepts and delivers in one call and checks
nothing is left open.
Auto-fill (Oct 9, Taylor: "let the game win itself"): `python contracts.py --fill` accepts and
delivers, in one call, a church offer that is GOOD and that we can cover ENTIRELY from stock right now
(so nothing is left open that could miss and cost the -100 penalty), keeping RESERVE units of items
we need for ourselves. Same call the game's Contracts > actions screen makes:
  POST /contracts/{contract id}/actions/{transaction id | 64}
       {participant_id: business, operation: "storage/<storehouse>", volume, asset, allow_alloc: true}
Every attempt is logged to state/order_queue_done.jsonl (source "contracts") and checked afterwards
(the offer must leave the open board or show as signed); a failure is flagged in the status email.

    python contracts.py          # print the board with scores
    python contracts.py --fill   # also auto-fill what qualifies
"""
import json
import os
import urllib.request

import endgame
import merc_status4 as m

HERE = os.path.dirname(os.path.abspath(__file__))
import ids as _ids                               # season-proof ids (state/v2/ids.json)
TOWN = _ids.get("home_town", "152202387")
STORE = _ids.get("store", "152202386005001")
BUSINESS = _ids.get("business", "39992")
OUT = os.path.join(HERE, "state", "contracts_scored.json")
BANQUET_COIN_PER_PRESTIGE = 57.0     # hold banquet 1 (fish), Oct 8 prices
RESERVE = {"limestone": 60,    # Oct 10 (Taylor): park plots first (60 each); Oct 14: one plot's worth (the quarry makes ~5/turn, the bin was full)
            "candles": 0,     # Oct 14 (Taylor: do it all): the 55-candle church ask may empty the slot for a turn or two (+125 prestige)
            "arms": 2, "light armour": 1, "cured fish": 10, "furniture": 10}   # keep for our own use
# Church readiness (Oct 9): what the church has asked for since Sep 27 and what we stockpile so an offer
# can be auto-filled the moment it appears (target = largest ask seen + RESERVE).
#   furniture 120-125 (+75) | limestone 40 (+50) | candles 50-55 (+100-125) | jewellery 40-45 (+100-125)
#   windows 6 (+150-175, Calange ~1/turn) | tapestries 6-7 (+150-175, Rouhomme): these two need a ship
CHURCH_STOCK = {"furniture": 135, "limestone": 100, "candles": 61, "jewellery": 45,
                "tapestries": 7, "windows": 6}    # Oct 14: ships stock these when v2 config ship_church.on
KEEP_AFTER_FILL = {"garments": 30}   # Oct 15: garments min_holding is raised to the ask while we build up for it
BUY_AFTER_FILL = {"furniture": {"buy_volume": 2, "max_holding": 20},   # Oct 16 (Taylor): recovery, no church restock after the fill;
                  "candles": {"buy_volume": 3, "max_holding": 12}}    # Oct 20 (Taylor: do what you can): buy 4 to 47 for the 45 ask, then slot upkeep
#   keep only the household upkeep buy (furniture is a sustenance slot, ~1.4/turn; tier 0 = the buy). Restore readiness by hand over 20k
MIN_BONUS = 20                         # don't bother below this much prestige
# Oct 22 (Taylor: "I want the bot to do more ... we are leaving money on the table"):
BUILDUP_MAX_CPP = 40      # a church ask our own output covers this cheaply (park ~47, banquet ~57) gets home sales held back
BUILDUP_STATE = os.path.join(HERE, "state", "church_buildup.json")
MIN_SALE_EDGE = 15        # a 'they buy' offer we fill now from stock is signed by itself when it beats home by this much
NO_AUTO_SALE = {"limestone", "jewellery", "furniture", "candles", "windows", "tapestries"}   # church stock: Taylor decides
# Oct 22 (Taylor: "Yes, above 8k cash"): buy the missing goods for a church ask at home when it's cheap prestige
CHURCH_BUY_MAX_CPP = 35        # coin per prestige, counting the whole ask at the price we bid
CHURCH_BUY_MIN_CASH = 8000     # cash left after the whole remaining buy
CHURCH_BUY_PER_TURN = 10       # bid volume per turn (thin markets: jewellery trades ~0.3/turn at home)
CHURCH_BUY_STATE = os.path.join(HERE, "state", "church_buy.json")
MARKET_URL = "https://api.mercatorio-tools.tech/data/marketdata"


def _f(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def world_market(items):
    """{item: {"home_ask","home_bid","home_vol","best_ask","best_town","world_vol"}} from the public market data."""
    try:
        req = urllib.request.Request(MARKET_URL, headers={"User-Agent": "merc-bot"})
        md = json.loads(urllib.request.urlopen(req, timeout=60).read())
    except Exception as e:
        print("contracts: market data unavailable (%s)" % e)
        return {}
    out = {}
    for item in items:
        best, best_town, wv, home = None, None, 0.0, {}
        for t in md:
            mk = (t.get("markets") or {}).get(item)
            if not mk:
                continue
            ask, vol = _f(mk.get("lowest_ask")), _f(mk.get("volume_ema_12")) or 0
            wv += vol
            if ask and (best is None or ask < best):
                best, best_town = ask, t.get("name")
            if t.get("name") == "Strasclives":
                home = mk
        out[item] = {"home_ask": _f(home.get("lowest_ask")), "home_bid": _f(home.get("highest_bid")),
                     "home_vol": _f(home.get("volume_ema_12")) or 0, "best_ask": best,
                     "best_town": best_town, "world_vol": round(wv, 1)}
    return out


def stock():
    """{item: (held, unit_cost, net_production_per_turn)} from the storehouse."""
    b = m.get("/buildings/%s" % STORE) or {}
    inv = (b.get("storage") or {}).get("inventory") or {}
    assets = (inv.get("account") or {}).get("assets") or {}
    flows = inv.get("previous_flows") or {}
    out = {}
    for item, a in assets.items():
        f = flows.get(item) or {}
        net = m.num(f.get("production")) - m.num(f.get("consumption"))
        out[item] = (m.num(a.get("balance")), _f(a.get("unit_cost")), net)
    return out


def open_offers():
    """Unsigned offers on the town board plus the church's list (which the board can miss)."""
    seen, offers = set(), []
    board = m.get("/contracts/towns/%s" % TOWN) or {}
    for c in (board.get("contracts") if isinstance(board, dict) else board) or []:
        seen.add(str(c.get("id")))
        offers.append(c)
    try:
        church = m.get("/towns/%s/church" % TOWN) or {}
        for cid in church.get("contract_ids") or []:
            if str(cid) not in seen:
                c = m.get("/contracts/%s" % cid)
                if c:
                    offers.append(c)
    except SystemExit:
        pass
    return [c for c in offers if not c.get("signed") and str(c.get("initiator")) != BUSINESS]


def score(c, mk, st):
    t = (c.get("transactions") or [{}])[0]
    item = t.get("asset")
    vol = m.num(t.get("initial_volume")) or m.num(t.get("volume"))
    turns = int(m.num((t.get("timeframe") or {}).get("length")) or 0)
    bonus = m.num(c.get("bonus"))
    penalty = m.num(t.get("penalty"))
    theybuy = t.get("direction") == "bid"
    k = mk.get(item) or {}
    held, ucost, net = st.get(item, (0.0, None, 0.0))
    r = dict(id=str(c.get("id")), item=item, volume=vol, turns=turns, bonus=bonus, penalty=penalty,
             kind="church" if bonus and theybuy else ("they buy" if theybuy else "they sell"),
             price=_f(t.get("price")), held=round(held, 1))
    if bonus and theybuy:
        # cost to fill: own stock at unit cost first, the rest at the best market ask
        from_stock = min(held, vol)
        market_px = k.get("home_ask") or k.get("best_ask")
        cost = from_stock * (ucost or market_px or 0) + (vol - from_stock) * (market_px or 0)
        own_over_time = max(0.0, net) * turns
        supply = held + own_over_time + (k.get("world_vol") or 0) * turns * 0.25   # assume we can win ~25% of world trade
        cpp = cost / bonus if bonus else None
        if held >= vol:
            fill, fill_txt = "now", "we hold %.0f of %.0f: fill now" % (held, vol)
        elif held + own_over_time >= vol:
            fill, fill_txt = "own", "own production covers it in %d turns" % turns
        elif supply >= vol and market_px and k.get("home_ask"):
            fill, fill_txt = "buy", "buy ~%.0f at home (ask %.2f; cheapest %.2f at %s)" % (
                vol - held, k["home_ask"], k.get("best_ask") or 0, k.get("best_town") or "?")
        elif supply >= vol and market_px:
            fill, fill_txt = "ship", "not sold here: a ship run for ~%.0f (cheapest %.2f at %s, ~%.0f/turn traded worldwide)" % (
                vol - held, k.get("best_ask") or 0, k.get("best_town") or "?", k.get("world_vol") or 0)
        else:
            fill, fill_txt = "thin", "thin market: ~%.1f/turn traded worldwide" % (k.get("world_vol") or 0)
        # Taylor's rule: only an offer we can fill immediately is ever signable
        if fill == "now" and cpp is not None and cpp <= BANQUET_COIN_PER_PRESTIGE * 2:
            verdict = "GOOD"
        elif fill == "now":
            verdict = "POOR"
        elif cpp is not None and cpp <= BANQUET_COIN_PER_PRESTIGE * 1.2 and fill != "thin":
            verdict = "WAIT"        # worth it, but not fillable now: stockpile, don't sign
        else:
            verdict = "SKIP"
        r.update(cost=round(cost), coin_per_prestige=round(cpp, 1) if cpp else None, fill=fill, verdict=verdict,
                 why="+%.0f prestige (%.0f if missed) for ~%.0f coin = %s coin/prestige (banquet ~%.0f); %s" % (
                     bonus, penalty, cost, ("%.0f" % cpp) if cpp else "?", BANQUET_COIN_PER_PRESTIGE, fill_txt))
        return r
    price = r["price"] or 0
    r["town_id"] = str(c.get("town_id") or TOWN)
    away = r["town_id"] != TOWN
    if theybuy:
        home = k.get("home_bid") or 0
        edge = (price - home) * vol
        can = (held >= vol or held + max(0, net) * max(turns, 1) >= vol) and not away
        verdict = "GOOD" if edge > 0.05 * home * vol and can else ("OK" if edge > 0 and can else ("POOR" if can else "SKIP"))
        why = "they buy %.0f %s at %.2f vs home bid %.2f: %+.0f vs selling at home; we hold %.0f" % (vol, item, price, home, edge, held)
        # Oct 22: contracts are regional. A buyer in another town takes delivery there, so our storehouse can't fill it
        # (the beer 60 @3.50 was signed and refused: 'storage/... not present in town 105202565')
        r["fill"] = "ship" if away else ("now" if held >= vol else "later")     # the phone app can approve a fill-now delivery
        if away:
            why += "; delivery in town %s, not here: needs a ship" % r["town_id"]
    else:
        home = k.get("home_ask") or 0
        edge = (home - price) * vol if home else 0
        verdict = "GOOD" if home and edge > 0.05 * home * vol else ("OK" if edge > 0 else "SKIP")
        why = "they sell %.0f %s at %.2f vs home ask %s: %+.0f vs buying at home" % (
            vol, item, price, ("%.2f" % home) if home else "none", edge)
        if net >= 0:
            # Oct 20: a cheap offer for a good we don't use is no saving (100 wool showed as GOOD in the app's
            # Attention list every run); only goods we consume more of than we make can be a good buy
            verdict, why = "SKIP", why + "; we don't use %s" % item
    r.update(edge=round(edge), verdict=verdict, why=why)
    return r


def score_board():
    offers = open_offers()
    items = sorted({(c.get("transactions") or [{}])[0].get("asset") for c in offers} - {None})
    mk, st = world_market(items), stock()
    scored = [score(c, mk, st) for c in offers]
    order = {"GOOD": 0, "OK": 1, "WAIT": 2, "POOR": 3, "SKIP": 4}
    scored.sort(key=lambda r: (order.get(r["verdict"], 9), -(r.get("bonus") or 0)))
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(scored, f, indent=1, default=str)
    return scored


def _post(path, body):
    import urllib.error
    req = urllib.request.Request(
        "https://play.mercatorio.io/api" + path, data=json.dumps(body).encode(), method="POST",
        headers={"X-Merc-User": m.USER, "Authorization": "Bearer " + m.TOKEN,
                 "Content-Type": "application/json", "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return True, r.status, r.read().decode()[:300]
    except urllib.error.HTTPError as e:
        return False, e.code, e.read().decode()[:300]
    except Exception as e:
        return False, None, "%s: %s" % (type(e).__name__, e)


def approvals():
    """Contract ids Taylor approved from the phone app (state/contract_approvals.json)."""
    try:
        with open(os.path.join(HERE, "state", "contract_approvals.json")) as f:
            return {str(x.get("id")) for x in json.load(f)}
    except (FileNotFoundError, ValueError):
        return set()


def _load_buildup():
    try:
        with open(BUILDUP_STATE) as f:
            return json.load(f) or {}
    except (OSError, ValueError):
        return {}


def _auto_sale(r, building_up):
    """Oct 22: a 'they buy' offer is signed and delivered by itself when it beats selling at home by MIN_SALE_EDGE,
    we hold the full volume now, it isn't church stock (NO_AUTO_SALE) and we aren't holding that item for a church ask."""
    return (r["kind"] == "they buy" and r["verdict"] == "GOOD" and r.get("fill") == "now"
            and str(r.get("town_id") or TOWN) == TOWN
            and (r.get("edge") or 0) >= MIN_SALE_EDGE and r["item"] not in NO_AUTO_SALE and r["item"] not in building_up)


def auto_fill(scored):
    import order_queue as q
    done = []
    ok_ids = approvals()
    building_up = _load_buildup()
    for r in scored:
        approved = str(r["id"]) in ok_ids and r["kind"] in ("church", "they buy") and r.get("fill") == "now"
        church_ok = r["kind"] == "church" and r["verdict"] == "GOOD" and r.get("fill") == "now" and r["bonus"] >= MIN_BONUS
        if not approved and not church_ok and not _auto_sale(r, building_up):
            continue
        if r["held"] - r["volume"] < RESERVE.get(r["item"], 0):
            print("contracts: %s offer skipped, would dip under our reserve of %s" % (r["item"], RESERVE.get(r["item"])))
            continue
        c = m.get("/contracts/%s" % r["id"]) or {}
        t = (c.get("transactions") or [{}])[0]
        if c.get("signed") or t.get("stage") != "ready":
            continue
        # An open offer is "idle"; delivering to it gives 409 "contract not active". Sign first (same call
        # as the game's Contracts > manage > sign), then deliver in the same run. Stock was checked above.
        sok, sstatus, sresp = _post("/contracts/%s/sign" % r["id"], {"participant_id": BUSINESS})
        if not sok:
            q.log({"contract": r["id"], "item": r["item"], "volume": r["volume"], "bonus": r["bonus"], "note": "auto-fill: sign step"},
                  dict(ok=False, status=sstatus, body=sresp[:200]), source="contracts")
            print("contracts: sign %s FAILED %s %s" % (r["item"], sstatus, sresp[:150]))
            continue
        c = m.get("/contracts/%s" % r["id"]) or c
        t = (c.get("transactions") or [t])[0]
        aid = str(int(t["id"]) | 64)
        body = {"participant_id": BUSINESS, "operation": "storage/%s" % STORE,
                "volume": int(r["volume"]), "asset": r["item"], "allow_alloc": True}
        ok, status, resp = _post("/contracts/%s/actions/%s" % (r["id"], aid), body)
        after = m.get("/contracts/%s" % r["id"]) or {}
        at = (after.get("transactions") or [{}])[0]
        remaining = m.num(at.get("volume"))
        good = ok and (at.get("stage") == "done" or remaining <= 0.001)   # fully delivered, nothing left open
        what = ("church offer from stock" if r["kind"] == "church" else
                "sale %s @ %s (+%s vs home)" % (r["item"], r.get("price"), r.get("edge")))
        q.log({"contract": r["id"], "item": r["item"], "volume": r["volume"], "bonus": r["bonus"], "note": "auto-fill " + what},
              dict(ok=bool(good), status=status, body=resp[:200], after_stage=at.get("stage"), after_signed=after.get("signed"),
                   remaining=remaining),
              source="contracts")
        print("contracts: auto-fill %s %s (%s) -> %s" % (r["volume"], r["item"], what, "OK" if good else "FAILED %s %s" % (status, resp[:150])))
        if r["kind"] != "church":
            done.append(dict(r, filled=bool(good)))
            continue
        if good and r["item"] in KEEP_AFTER_FILL:
            e = {"item": r["item"], "tier": 0, "set": {"min_holding": KEEP_AFTER_FILL[r["item"]]},
                 "note": "church %s ask filled: sell reserve back to normal" % r["item"]}
            try:
                q.log(e, q.apply_entry(e), source="contracts")
            except Exception as ex:
                print("contracts: reserve reset failed: %s" % ex)
        if good and r["item"] in BUY_AFTER_FILL and not endgame.active():   # endgame: keep stocking for the next ask
            e = {"item": r["item"], "tier": 0, "set": BUY_AFTER_FILL[r["item"]],
                 "note": "church %s ask filled: readiness buy back to household upkeep only (Taylor Oct 16, recovery; restore over 20k cash)" % r["item"]}
            try:
                q.log(e, q.apply_entry(e), source="contracts")
            except Exception as ex:
                print("contracts: buy off after fill failed: %s" % ex)
        done.append(dict(r, filled=bool(good)))
    return done


def church_buildup(scored, apply=None, failsafe_level=None):
    """Oct 22 (Taylor: "I want the bot to do more ... we are leaving money on the table"). A church ask our own production
    covers ('own') at <= BUILDUP_MAX_CPP coin per prestige gets the item's home sell reserve (tier 0 min_holding) raised
    to the ask's volume, so home sales stop eating the pile (Oct 22: garments 75 for +75 = ~20 coin/prestige sat WAIT
    for days while 23 a turn sold at home). auto_fill signs and delivers the moment stock covers it (Taylor's rule
    holds: nothing is signed before it can be filled in full) and KEEP_AFTER_FILL puts the reserve back. When the ask
    leaves the board unfilled (expired, or another player took it), or the failsafe brakes, the reserve goes back too.
    Only items in KEEP_AFTER_FILL (we sell them and know the normal reserve). v2 never touches min_holding."""
    if apply is None:
        import order_queue as q

        def apply(e):
            r = q.apply_entry(e)
            q.log(e, r, source="contracts")
            return r
    if failsafe_level is None:
        try:
            failsafe_level = int(m.num(json.load(open(os.path.join(HERE, "state", "failsafe.json"))).get("level")))
        except (OSError, ValueError):
            failsafe_level = 0
    st = _load_buildup()
    open_ids = {str(r["id"]) for r in scored}
    want = {}
    if failsafe_level < 2:
        for r in scored:
            if (r["kind"] == "church" and r["item"] in KEEP_AFTER_FILL and r.get("fill") in ("own", "now")
                    and r["verdict"] in ("WAIT", "GOOD") and (r.get("bonus") or 0) >= MIN_BONUS
                    and r.get("coin_per_prestige") is not None and r["coin_per_prestige"] <= BUILDUP_MAX_CPP):
                best = want.get(r["item"])
                if best is None or r["coin_per_prestige"] < best["coin_per_prestige"]:
                    want[r["item"]] = r
    out = []
    for item, cur in list(st.items()):
        w = want.get(item)
        if w and str(w["id"]) == str(cur.get("contract")):
            continue
        why = ("failsafe level %s" % failsafe_level if failsafe_level >= 2 else
               "ask %s left the board" % cur.get("contract") if str(cur.get("contract")) not in open_ids else
               "ask no longer worth holding for")
        if w:
            continue        # a better ask for the same item replaces it below
        e = {"item": item, "tier": 0, "set": {"min_holding": KEEP_AFTER_FILL[item]},
             "note": "church build-up over (%s): %s sell reserve back to %s" % (why, item, KEEP_AFTER_FILL[item])}
        apply(e)
        del st[item]
        out.append(("release", item, why))
    for item, r in want.items():
        if str((st.get(item) or {}).get("contract")) == str(r["id"]):
            continue
        target = int(r["volume"] + 0.999)
        e = {"item": item, "tier": 0, "set": {"min_holding": target},
             "note": "church build-up: hold %s home sales until %d held for the church ask (+%.0f prestige, %.0f coin/prestige); "
                     "auto-fill delivers it, then the reserve goes back to %s" % (
                         item, target, r["bonus"], r["coin_per_prestige"], KEEP_AFTER_FILL[item])}
        res = apply(e)
        if res.get("ok"):
            st[item] = {"contract": str(r["id"]), "volume": r["volume"], "bonus": r["bonus"]}
        out.append(("hold", item, target, bool(res.get("ok"))))
    with open(BUILDUP_STATE, "w") as f:
        json.dump(st, f, indent=1)
    for o in out:
        print("contracts: build-up", o)
    return out


def _snap_up(p):
    """The game's price grid: 3 significant digits; lead 1 any, 2-4 even last digit, 5-9 last digit 0 or 5. Rounds up."""
    import math
    if not p or p <= 0:
        return p
    e = math.floor(math.log10(p) + 1e-12) - 2
    lead = int(p / 10 ** (e + 2) + 1e-9)
    step = max(10 ** e * (5 if lead >= 5 else 2 if lead >= 2 else 1), 0.01)
    return round(math.ceil(p / step - 1e-9) * step, 6)


def _snap_down(p):
    import math
    if not p or p <= 0:
        return p
    e = math.floor(math.log10(p) + 1e-12) - 2
    lead = int(p / 10 ** (e + 2) + 1e-9)
    step = max(10 ** e * (5 if lead >= 5 else 2 if lead >= 2 else 1), 0.01)
    return round(math.floor(p / step + 1e-9) * step, 6)


def _cash():
    b = m.get("/businesses/%s" % BUSINESS) or {}
    mon = ((b.get("account") or {}).get("assets") or {}).get("money") or {}
    return m.num(mon.get("balance")) - m.num(mon.get("reserved"))


def church_buy(scored, cash=None, apply=None, failsafe_level=None, mk=None):
    """Oct 22 (Taylor: "Yes, above 8k cash"). A church ask we can't cover from stock or own output ('buy': sold at home)
    gets a home buy order for what's missing when the whole ask costs <= CHURCH_BUY_MAX_CPP coin per prestige at our
    bid and cash stays >= CHURCH_BUY_MIN_CASH after the whole remaining buy. Bid = the cheaper of the prestige value
    (CHURCH_BUY_MAX_CPP x bonus / volume) and home ask + 10%, CHURCH_BUY_PER_TURN a turn, stop at the ask + RESERVE.
    Taylor's Oct 9 rule still holds: nothing is signed until stock covers the ask in full; auto_fill then fills it and
    BUY_AFTER_FILL puts the order back. The buy is switched off when cash drops under the line, the failsafe brakes,
    or the ask leaves the board. Tier 0 is the item's buy tier (household slot for candles/furniture)."""
    if apply is None:
        import order_queue as q

        def apply(e):
            r = q.apply_entry(e)
            q.log(e, r, source="contracts")
            return r
    if failsafe_level is None:
        try:
            failsafe_level = int(m.num(json.load(open(os.path.join(HERE, "state", "failsafe.json"))).get("level")))
        except (OSError, ValueError):
            failsafe_level = 0
    try:
        with open(CHURCH_BUY_STATE) as f:
            st = json.load(f) or {}
    except (OSError, ValueError):
        st = {}
    if cash is None:
        cash = _cash()
    if mk is None:
        mk = world_market(sorted({r["item"] for r in scored if r["kind"] == "church"}))
    open_ids = {str(r["id"]) for r in scored}
    plans = {}
    for r in scored:
        if not (r["kind"] == "church" and r["verdict"] == "WAIT" and r.get("fill") == "buy"
                and (r.get("bonus") or 0) >= MIN_BONUS and r["item"] not in KEEP_AFTER_FILL):
            continue
        ask = (mk.get(r["item"]) or {}).get("home_ask")
        if not ask:
            continue
        target = r["volume"] + RESERVE.get(r["item"], 0)
        need = target - r["held"]
        if need <= 0:
            continue
        bid = _snap_down(min(CHURCH_BUY_MAX_CPP * r["bonus"] / r["volume"], ask * 1.10))
        if bid < ask * 0.9:
            continue                # can't buy it cheaply enough at home now
        cpp = (r["volume"] * bid) / r["bonus"]
        best = plans.get(r["item"])
        if cpp <= CHURCH_BUY_MAX_CPP and (best is None or cpp < best["cpp"]):
            plans[r["item"]] = dict(contract=str(r["id"]), need=need, bid=bid, target=int(target + 0.999), cpp=round(cpp, 1),
                                    cost=round(need * bid), bonus=r["bonus"])
    out = []
    for item, cur in list(st.items()):
        p = plans.get(item)
        if p and p["contract"] == cur.get("contract"):
            continue
        if p:
            continue                # replaced below
        why = "ask left the board" if cur.get("contract") not in open_ids else "no longer cheap enough"
        if cur.get("on"):
            apply({"item": item, "tier": 0, "set": BUY_AFTER_FILL.get(item, {"buy_volume": 0}),
                   "note": "church buy over (%s): %s buy back to normal" % (why, item)})
        del st[item]
        out.append(("stop", item, why))
    for item, p in plans.items():
        ok_cash = cash - p["cost"] >= CHURCH_BUY_MIN_CASH and failsafe_level < 2
        cur = st.get(item) or {}
        on = bool(cur.get("on"))
        if ok_cash and (not on or cur.get("contract") != p["contract"] or cur.get("bid") != p["bid"]):
            e = {"item": item, "tier": 0,
                 "set": {"buy_volume": int(min(p["need"], CHURCH_BUY_PER_TURN) + 0.999), "buy_price": "%g" % p["bid"],
                         "max_holding": p["target"]},
                 "note": "church buy: %s for the church ask (+%.0f prestige, %.1f coin/prestige at bid %g); need %.0f "
                         "(~%d coin), cash %.0f stays over %d; auto-fill delivers once %d held" % (
                             item, p["bonus"], p["cpp"], p["bid"], p["need"], p["cost"], cash, CHURCH_BUY_MIN_CASH, p["target"])}
            r = apply(e)
            st[item] = dict(p, on=bool(r.get("ok")))
            out.append(("buy", item, p["need"], p["bid"], bool(r.get("ok"))))
        elif not ok_cash and on:
            apply({"item": item, "tier": 0, "set": BUY_AFTER_FILL.get(item, {"buy_volume": 0}),
                   "note": "church buy paused: cash %.0f - %d to buy < %d (or failsafe %s)" % (
                       cash, p["cost"], CHURCH_BUY_MIN_CASH, failsafe_level)})
            st[item] = dict(p, on=False)
            out.append(("pause", item, round(cash), p["cost"]))
        elif not ok_cash:
            st[item] = dict(p, on=False)
            out.append(("wait", item, round(cash), p["cost"]))
    with open(CHURCH_BUY_STATE, "w") as f:
        json.dump(st, f, indent=1)
    for o in out:
        print("contracts: church buy", o)
    return out


if __name__ == "__main__":
    import sys
    board = score_board()
    for r in board:
        print("%-4s %-9s %-12s %s" % (r["verdict"], r["kind"], r["item"], r["why"]))
    if "--fill" in sys.argv and m.USER and m.TOKEN:
        auto_fill(board)
        try:
            board2 = score_board()              # re-read: a fill this run takes its ask off the board
            church_buildup(board2)
            church_buy(board2)
        except Exception as ex:
            print("contracts: build-up / church buy failed: %s: %s" % (type(ex).__name__, ex))
    try:
        import app_status
        app_status.write()      # phone app overview, after queue + rules + contracts in this workflow run
    except Exception as ex:
        print("app status failed:", ex)
