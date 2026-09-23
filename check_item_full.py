#!/usr/bin/env python3
"""One-off: full picture for one item -- held stock, production/consumption,
market prices, and the raw manager rules. GET only."""
import json
import sys
import merc_status4 as m
import merc_advisor as adv

if len(sys.argv) != 3:
    sys.exit('usage: python check_item_full.py <building_id> "<item>"')

building_id, item = sys.argv[1], sys.argv[2]
player = adv.safe_get("/player")
hh = player.get("household", {})
home_town_id = hh.get("town_id")

r = adv.building_report(building_id, {}, home_town_id)
d = r["items"].get(item)
if d is None:
    sys.exit("Item %r not found in this building's inventory." % item)

print(json.dumps(d, indent=2, default=str))
