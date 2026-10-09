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
  verdict: GOOD (fill now from stock, or coin/prestige well under the banquet), OK, POOR, SKIP

Writes state/contracts_scored.json and returns the list; alerts.py puts GOOD/OK ones in the email.
Signing and delivering stay with Taylor (or a queue entry he approves) until the delivery call is
proven on a live contract: a church contract signed and not filled costs -100 prestige.

    python contracts.py      # print the board with scores
"""
import json
import os
import urllib.request

import merc_status4 as m

HERE = os.path.dirname(os.path.abspath(__file__))
TOWN = "152202387"
STORE = "152202386005001"
BUSINESS = "39992"
OUT = os.path.join(HERE, "state", "contracts_scored.json")
BANQUET_COIN_PER_PRESTIGE = 57.0     # hold banquet 1 (fish), Oct 8 prices
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
        if not market_px and held < vol:
            verdict = "SKIP"
        elif fill == "now" and (cpp or 0) <= BANQUET_COIN_PER_PRESTIGE * 2:
            verdict = "GOOD"
        elif fill in ("own", "buy") and cpp is not None and cpp <= BANQUET_COIN_PER_PRESTIGE * 0.8:
            verdict = "GOOD"
        elif fill in ("now", "own", "buy", "ship") and cpp is not None and cpp <= BANQUET_COIN_PER_PRESTIGE * 1.2:
            verdict = "OK"
        elif fill == "thin":
            verdict = "SKIP"
        else:
            verdict = "POOR"
        r.update(cost=round(cost), coin_per_prestige=round(cpp, 1) if cpp else None, fill=fill, verdict=verdict,
                 why="+%.0f prestige (%.0f if missed) for ~%.0f coin = %s coin/prestige (banquet ~%.0f); %s" % (
                     bonus, penalty, cost, ("%.0f" % cpp) if cpp else "?", BANQUET_COIN_PER_PRESTIGE, fill_txt))
        return r
    price = r["price"] or 0
    if theybuy:
        home = k.get("home_bid") or 0
        edge = (price - home) * vol
        can = held >= vol or held + max(0, net) * max(turns, 1) >= vol
        verdict = "GOOD" if edge > 0.05 * home * vol and can else ("OK" if edge > 0 and can else ("POOR" if can else "SKIP"))
        why = "they buy %.0f %s at %.2f vs home bid %.2f: %+.0f vs selling at home; we hold %.0f" % (vol, item, price, home, edge, held)
    else:
        home = k.get("home_ask") or 0
        edge = (home - price) * vol if home else 0
        verdict = "GOOD" if home and edge > 0.05 * home * vol else ("OK" if edge > 0 else "SKIP")
        why = "they sell %.0f %s at %.2f vs home ask %s: %+.0f vs buying at home" % (
            vol, item, price, ("%.2f" % home) if home else "none", edge)
    r.update(edge=round(edge), verdict=verdict, why=why)
    return r


def score_board():
    offers = open_offers()
    items = sorted({(c.get("transactions") or [{}])[0].get("asset") for c in offers} - {None})
    mk, st = world_market(items), stock()
    scored = [score(c, mk, st) for c in offers]
    order = {"GOOD": 0, "OK": 1, "POOR": 2, "SKIP": 3}
    scored.sort(key=lambda r: (order.get(r["verdict"], 9), -(r.get("bonus") or 0)))
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(scored, f, indent=1, default=str)
    return scored


if __name__ == "__main__":
    for r in score_board():
        print("%-4s %-9s %-12s %s" % (r["verdict"], r["kind"], r["item"], r["why"]))
