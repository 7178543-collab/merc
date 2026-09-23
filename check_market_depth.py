#!/usr/bin/env python3
"""One-off: full raw market entry for one item in your home town --
price, moving average, and volume over the last several turns, not just
the current snapshot. GET only."""
import json
import sys
import merc_status4 as m

if len(sys.argv) != 2:
    sys.exit('usage: python check_market_depth.py "<item>"')

item = sys.argv[1]
player = m.get("/player")
hh = player.get("household", {})
town_id = hh.get("town_id")

mkt = m.get("/towns/%s/marketdata" % town_id)
entry = mkt.get("markets", {}).get(item)

if entry is None:
    print("NOT FOUND -- available items:")
    print(json.dumps(sorted(mkt.get("markets", {}).keys()), indent=2))
else:
    print("town_id: %s" % town_id)
    print(json.dumps(entry, indent=2, default=str))
