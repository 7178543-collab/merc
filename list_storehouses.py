#!/usr/bin/env python3
"""One-off: for every business your household owns, list its storehouse/
warehouse buildings and home town. Shows whether you have one storage pool
or several separate ones. GET only."""
import json
import merc_status4 as m

player = m.get("/player")
hh = player.get("household", {})
biz_ids = hh.get("business_ids", [])
print("household: %s" % hh.get("name"))
print("business_ids: %s" % biz_ids)
print()

for biz_id in biz_ids:
    biz = m.get("/businesses/%s" % biz_id)
    print("== business %s ==" % biz_id)
    stores = [b for b in biz.get("buildings", []) if b.get("type") in ("storehouse", "warehouse")]
    if not stores:
        print("  no storehouse/warehouse in this business")
    for s in stores:
        print("  %s  id=%s  town_id=%s" % (s.get("type"), s.get("id"), s.get("town_id")))
    print()
