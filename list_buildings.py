#!/usr/bin/env python3
"""One-off: list every building on the household's main business, with type,
name, and whatever status/construction fields the API returns. GET only."""
import json
import sys
import merc_status4 as m

player = m.get("/player")
hh = player.get("household", {})
biz_id = hh["business_ids"][0]
biz = m.get("/businesses/%s" % biz_id)

for b in biz.get("buildings", []):
    # print the whole thing minus storage/inventory (too big, not relevant here)
    slim = {k: v for k, v in b.items() if k != "storage"}
    print(json.dumps(slim, indent=2, default=str))
    print("---")
