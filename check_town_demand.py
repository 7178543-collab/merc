#!/usr/bin/env python3
"""One-off: town-wide consumer demand for specific items (desire/request/
result from the commoners' sustenance categories). GET only."""
import json
import sys
import merc_status4 as m

player = m.get("/player")
hh = player.get("household", {})
town_id = hh.get("town_id")

town = m.get("/towns/%s" % town_id)
categories = town.get("commoners", {}).get("spending", [])

targets = set(a.lower() for a in sys.argv[1:]) if len(sys.argv) > 1 else None

for cat in categories:
    for p in cat.get("products", []):
        name = p.get("product", "")
        if targets and name.lower() not in targets:
            continue
        print("%-12s desire=%s request=%s result=%s  (category: %s)" % (
            name, p.get("desire"), p.get("request"), p.get("result"), cat.get("name")))
