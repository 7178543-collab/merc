#!/usr/bin/env python3
"""Mercatorio read-only status, phone-width (v2). Standard library only. GET only.

Uses credentials saved in ~/.merc_creds (asks on first run).
    python merc_status2.py         # compact table + flags
    python merc_status2.py --raw   # also print response keys
"""
import getpass
import json
import os
import stat
import sys
import urllib.error
import urllib.request

BASE = "https://play.mercatorio.io/api"
CREDS = os.path.expanduser("~/.merc_creds")
RAW = "--raw" in sys.argv
SKIP = {"money", "labour", "porterage", "handcart", "tumbrel", "cog", "snekkja"}
LOW_TURNS = 5      # flag items with fewer turns of supply than this
MIN_VALUE = 20.0   # ignore no-buyer flags for stock worth less than this


def load_creds():
    user, token = os.environ.get("API_USER"), os.environ.get("API_TOKEN")
    if user and token:
        return user, token
    if os.path.exists(CREDS):
        with open(CREDS) as f:
            d = json.load(f)
        return d["user"], d["token"]
    user = input("API user: ").strip()
    token = getpass.getpass("API token (hidden): ").strip()
    with open(CREDS, "w") as f:
        json.dump({"user": user, "token": token}, f)
    os.chmod(CREDS, stat.S_IRUSR | stat.S_IWUSR)
    return user, token


USER, TOKEN = load_creds()


def get(path):
    """GET only. This script never changes anything in the game."""
    req = urllib.request.Request(
        BASE + path,
        headers={"X-Merc-User": USER, "Authorization": "Bearer " + TOKEN,
                 "Accept": "application/json"},
        method="GET")
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            body = r.read().decode()
    except urllib.error.HTTPError as e:
        sys.exit("HTTP %s on %s: %s" % (e.code, path, e.read().decode()[:200]))
    except urllib.error.URLError as e:
        sys.exit("Network error on %s: %s" % (path, e.reason))
    if "preparing next game-turn" in body:
        sys.exit("Turn in progress. Try again in a few seconds.")
    data = json.loads(body)
    if RAW:
        keys = list(data.keys()) if isinstance(data, dict) else "list[%d]" % len(data)
        print("[raw] %s -> %s" % (path, keys))
    return data


def num(x, default=0.0):
    try:
        return float(x)
    except (TypeError, ValueError):
        return default


def main():
    player = get("/player")
    hh = player.get("household", {})
    biz = get("/businesses/%s" % hh["business_ids"][0])
    money = biz.get("account", {}).get("assets", {}).get("money", {})
    print("%s" % hh.get("name"))
    print("Cash %.0f | Prestige %.1f" % (num(money.get("balance")), num(hh.get("prestige"))))

    stores = [b for b in biz.get("buildings", [])
              if b.get("type") in ("storehouse", "warehouse")]
    if not stores:
        sys.exit("No warehouse found. Run with --raw.")
    sh = get("/buildings/%s" % stores[0]["id"])
    inv = sh.get("storage", {}).get("inventory", {})
    assets = inv.get("account", {}).get("assets", {})
    flows = inv.get("previous_flows") or {}
    holdings = inv.get("holdings") or {}
    market = get("/towns/%s/marketdata" % hh.get("town_id")).get("markets", {})

    sells, buys = [], []
    for item, h in holdings.items():
        for mg in (h.get("managers") or []):
            res = mg.get("result") or {}
            lim = res.get("limitations")
            if mg.get("sell_price") is not None:
                sells.append((item, num(mg["sell_price"]), mg.get("sell_volume"),
                              res.get("ask_volume"), lim))
            if mg.get("buy_price") is not None:
                buys.append((item, num(mg["buy_price"]), mg.get("buy_volume"),
                             res.get("bid_volume"), lim, mg.get("max_holding")))
    bought = {}   # posted buy volume per item
    for item, px, vol, posted, lim, mx in buys:
        bought[item] = bought.get(item, 0) + num(posted)

    rows = []
    for item, a in assets.items():
        if item in SKIP:
            continue
        held = num(a.get("balance"))
        m = market.get(item, {})
        price = num(m.get("price"))
        if held <= 0 or price <= 0:
            continue
        fl = flows.get(item, {})
        net = num(fl.get("production")) - num(fl.get("consumption"))
        rows.append(dict(item=item, held=held, price=price, cost=a.get("unit_cost"),
                         bid=num(m.get("highest_bid")), net=net,
                         eff=net + bought.get(item, 0), value=held * price))
    rows.sort(key=lambda r: r["value"], reverse=True)

    print("\n%-11s %6s %5s %5s %6s" % ("item", "held", "price", "bid", "net/t"))
    for r in rows:
        print("%-11s %6.1f %5.2f %5.2f %+6.1f" %
              (r["item"][:11], r["held"], r["price"], r["bid"], r["net"]))
    print("\nStock value: %.0f" % sum(r["value"] for r in rows))

    low = [r for r in rows if r["eff"] < 0 and r["held"] / -r["eff"] < LOW_TURNS]
    print("\nRUNNING LOW after buy orders:")
    if low:
        for r in sorted(low, key=lambda r: r["held"] / -r["eff"]):
            print("  %-11s %4.1f turns" % (r["item"][:11], r["held"] / -r["eff"]))
    else:
        print("  none")
    nobuy = [r for r in rows if r["bid"] == 0 and r["value"] >= MIN_VALUE]
    if nobuy:
        sold = set(x[0] for x in sells)
        print("\nNO LOCAL BID (value):")
        for r in nobuy:
            tag = " growing" if r["net"] > 0 else ""
            tag += "" if r["item"] in sold else " NO SELL ORDER"
            print("  %-11s %5.0f%s" % (r["item"][:11], r["value"], tag))

    print("\nSELL ORDERS (want/posted):")
    for item, px, vol, posted, lim in sells:
        print("  %-10s %6.2f x%s/%s%s" % (item[:10], px, vol, posted,
                                         " (%s)" % lim if lim else ""))
    if not sells:
        print("  none")

    print("\nBUY: limit vs market vs avg cost")
    byitem = dict((r["item"], r) for r in rows)
    seen = set()
    for item, px, vol, posted, lim, mx in buys:
        r = byitem.get(item)
        if item in seen or not r:
            continue
        seen.add(item)
        c = r["cost"]
        print("  %-9s %5.2f %5.2f %5s" % (item[:9], px, r["price"],
                                          "%.2f" % num(c) if c is not None else "-"))


if __name__ == "__main__":
    main()
