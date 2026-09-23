#!/usr/bin/env python3
"""One-off: dump the raw /towns/{id} response's top-level shape so we can
see the real field names instead of guessing. GET only."""
import json
import merc_status4 as m

player = m.get("/player")
hh = player.get("household", {})
town_id = hh.get("town_id")

town = m.get("/towns/%s" % town_id)
print("top-level keys:", sorted(town.keys()))
print()
if "commoners" in town:
    print("commoners keys:", sorted(town["commoners"].keys()))
    print(json.dumps(town["commoners"], indent=2, default=str)[:1500])
else:
    print("no 'commoners' key -- full dump (trimmed):")
    print(json.dumps(town, indent=2, default=str)[:2000])
