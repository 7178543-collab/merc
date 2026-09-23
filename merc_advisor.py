#!/usr/bin/env python3
"""Mercatorio advisor (read-only). One comprehensive check: pulls every
storehouse you own, compares your posted auto-trade rules against the
current market, and flags anything that looks stale, mispriced, or stuck --
the kind of thing that otherwise only turns up by clicking through the game
by hand.

Needs merc_status4.py in the same folder (uses its saved login, get(), num(),
and SKIP -- same interface merc_watch.py and merc_scan.py already rely on).

    python merc_advisor.py            # flags only (short -- easy to copy)
    python merc_advisor.py --full     # also show the full per-item table
    python merc_advisor.py --json     # JSON instead of text (same scope as above;
                                       # add --full for the item table too)
    python merc_advisor.py --towns    # also cross-check flagged items against
                                       # every other town's market (slower)

Nothing in this script ever POSTs, PATCHes, or otherwise changes game state.
It only calls GET endpoints.
"""
import json
import sys
from concurrent.futures import ThreadPoolExecutor

import merc_status4 as m

AS_JSON = "--json" in sys.argv
FULL = "--full" in sys.argv
CROSS_TOWN = "--towns" in sys.argv

LOW_TURNS = 5             # flag when held / net_consumption is under this many turns
STALE_BUY_MARGIN = 0.0    # buy_price <= lowest_ask * (1+margin) still counts as competitive
STALE_SELL_MARGIN = 0.10  # sell_price above highest_bid by more than this looks stuck
MIN_VALUE = 20.0          # ignore dead-stock / no-order flags below this stock value

# result.limitations values that mean "this order isn't a pricing problem" --
# don't call it stale/mispriced when one of these is the real reason
NON_PRICE_LIMITS = {"space", "atmax", "stock"}


def safe_get(path):
    try:
        return m.get(path)
    except SystemExit as e:
        print("  (fetch failed: %s: %s)" % (path, e), file=sys.stderr)
        return None


def building_report(building_id, town_cache, default_town_id):
    b = safe_get("/buildings/%s" % building_id)
    if not b:
        return None
    # the /buildings response isn't documented to include a town id, so fall back
    # to the household's home town (what merc_status2.py relies on) if it's absent
    town_id = b.get("town_id") or b.get("owner_town_id") or default_town_id
    inv = b.get("storage", {}).get("inventory", {})
    assets = inv.get("account", {}).get("assets", {})
    holdings = inv.get("holdings", {})
    flows = inv.get("previous_flows") or {}

    if town_id and town_id not in town_cache:
        town_cache[town_id] = (safe_get("/towns/%s/marketdata" % town_id) or {}).get("markets", {})
    market = town_cache.get(town_id, {})

    items = {}
    for item, a in assets.items():
        if item in m.SKIP:
            continue
        held = m.num(a.get("balance"))
        mk = market.get(item, {})
        fl = flows.get(item, {})
        net = m.num(fl.get("production")) - m.num(fl.get("consumption"))
        managers = (holdings.get(item) or {}).get("managers") or []
        items[item] = dict(
            held=held,
            unit_cost=m.num(a.get("unit_cost")),
            net=net,
            highest_bid=m.num(mk.get("highest_bid")),
            lowest_ask=m.num(mk.get("lowest_ask")),
            last_price=m.num(mk.get("last_price")),
            volume=m.num(mk.get("volume")),
            managers=managers,
        )
    return dict(building_id=building_id, town_id=town_id, name=b.get("name"),
                type=b.get("type"), items=items)


def _is_buy(mg):
    return mg.get("buy_price") is not None or mg.get("buy_markup") is not None


def _is_sell(mg):
    return mg.get("sell_price") is not None or mg.get("sell_markup") is not None


def flag_item(item, d):
    flags = []
    held, net = d["held"], d["net"]
    value = held * (d["last_price"] or d["unit_cost"] or 0)
    # actual pending/posted buy volume (from the live order), not just the configured
    # target -- matches how merc_watch.py computes "effective" incoming supply
    bought_vol = sum(m.num((mg.get("result") or {}).get("bid_volume"))
                      for mg in d["managers"] if _is_buy(mg))
    eff = net + bought_vol

    if eff < 0 and held > 0 and (held / -eff) < LOW_TURNS:
        flags.append(("low_stock", "%.1f turns of supply left" % (held / -eff)))

    have_buy = have_sell = False
    for mg in d["managers"]:
        limits = (mg.get("result") or {}).get("limitations")
        non_price_reason = limits if limits in NON_PRICE_LIMITS else None

        if _is_buy(mg):
            have_buy = True
            bp = mg.get("buy_price")
            if bp is not None and not non_price_reason:
                bp = m.num(bp)
                if d["lowest_ask"] and bp < d["lowest_ask"] * (1 + STALE_BUY_MARGIN):
                    flags.append(("stale_buy",
                        "auto-buy at %.2f but lowest ask is %.2f -- won't fill" % (bp, d["lowest_ask"])))
            # NOTE: buy_markup (the buy-side equivalent of sell_markup) isn't
            # evaluated for staleness yet -- we haven't seen a live example of
            # it, and guessing its sign/direction (discount off cost? above
            # market?) risks a wrong, misleading flag. Confirm its real shape
            # via check_manager.py against a buy_markup item before adding this.
            if non_price_reason:
                flags.append(("capped", "buy order limited by '%s', not price" % non_price_reason))
            elif mg.get("buy_volume") is not None and m.num(mg.get("buy_volume")) <= 0:
                flags.append(("zero_volume", "auto-buy rule has 0 volume/turn"))

        if _is_sell(mg):
            have_sell = True
            sp = mg.get("sell_price")
            if sp is not None and not non_price_reason:
                sp = m.num(sp)
                if d["highest_bid"] and sp > d["highest_bid"] * (1 + STALE_SELL_MARGIN):
                    flags.append(("stale_sell",
                        "auto-sell at %.2f but highest bid is %.2f -- likely stuck" % (sp, d["highest_bid"])))
            smk = mg.get("sell_markup")
            if smk is not None and not non_price_reason:
                smk = m.num(smk)
                implied = d["unit_cost"] * (1 + smk) if d["unit_cost"] else None
                if implied and d["highest_bid"] and implied > d["highest_bid"] * (1 + STALE_SELL_MARGIN):
                    flags.append(("stale_sell_markup",
                        "sell markup +%.0f%% on cost implies ~%.2f but highest bid is %.2f -- likely stuck "
                        "(implied price is an estimate from unit_cost, not exact)" %
                        (smk * 100, implied, d["highest_bid"])))
            if non_price_reason and non_price_reason != "space":
                flags.append(("capped", "sell order limited by '%s'" % non_price_reason))

    if not have_buy and not have_sell and value >= MIN_VALUE and net != 0:
        flags.append(("no_order", "worth %.0f, producing/consuming but no buy or sell rule set" % value))

    # only call it dead stock if nothing traded last turn either -- a snapshot taken
    # between turns can show an empty order book even for something that just sold
    # fine, since this game clears trades in a start-of-turn auction
    if have_sell and d["highest_bid"] == 0 and d["volume"] == 0 and value >= MIN_VALUE:
        flags.append(("no_local_bid", "no buyer and no trades last turn either (value %.0f)" % value))

    return flags


def cross_town_bids(item, home_town_id, all_towns):
    rows = []
    def fetch(t):
        mk = (safe_get("/towns/%s/marketdata" % t["id"]) or {}).get("markets", {})
        return t, mk.get(item, {})
    with ThreadPoolExecutor(max_workers=6) as ex:
        for t, it in ex.map(fetch, all_towns):
            bid = m.num(it.get("highest_bid"))
            if bid > 0:
                rows.append((bid, t["name"], t.get("region")))
    rows.sort(reverse=True)
    return rows[:5]


def main():
    player = safe_get("/player")
    if not player:
        sys.exit(1)
    hh = player.get("household", {})
    header = {"household": hh.get("name"), "prestige": m.num(hh.get("prestige"))}

    biz_id = hh["business_ids"][0]
    biz = safe_get("/businesses/%s" % biz_id)
    money = m.num(biz.get("account", {}).get("assets", {}).get("money", {}).get("balance"))
    header["cash"] = money

    stores = [b for b in biz.get("buildings", []) if b.get("type") in ("storehouse", "warehouse")]
    town_cache = {}
    reports = []
    all_flags = []
    home_town_id = hh.get("town_id")
    for s in stores:
        r = building_report(s["id"], town_cache, home_town_id)
        if not r:
            continue
        reports.append(r)
        for item, d in r["items"].items():
            for kind, text in flag_item(item, d):
                all_flags.append(dict(building=r["name"], item=item, kind=kind, text=text))

    if CROSS_TOWN:
        towns = safe_get("/towns") or []
        for f in all_flags:
            if f["kind"] in ("no_local_bid", "low_stock"):
                f["other_towns"] = cross_town_bids(f["item"], home_town_id, towns)

    result = {"household": header, "flags": all_flags}
    if FULL:
        result["buildings"] = reports

    if AS_JSON:
        print(json.dumps(result, indent=2, default=str))
        return

    print("%s | cash %.0f | prestige %.1f" % (hh.get("name"), money, m.num(hh.get("prestige"))))

    if FULL:
        for r in reports:
            print("\n== %s (%s) ==" % (r["name"], r["type"]))
            for item, d in sorted(r["items"].items(), key=lambda kv: -kv[1]["held"] * (kv[1]["last_price"] or 1)):
                if d["held"] <= 0 and d["net"] == 0:
                    continue
                print("  %-14s held %8.1f  net/t %+7.1f  bid %6.2f  ask %6.2f" %
                      (item, d["held"], d["net"], d["highest_bid"], d["lowest_ask"]))

    print("\n==== FLAGS (%d) ====" % len(all_flags))
    if not all_flags:
        print("  nothing flagged")
    for f in all_flags:
        print("  [%s] %s: %s" % (f["kind"], f["item"], f["text"]))
        for bid, name, region in f.get("other_towns", []):
            print("      -> %-12s bid %6.2f (%s)" % (name, bid, region))


if __name__ == "__main__":
    main()
