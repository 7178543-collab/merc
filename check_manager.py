#!/usr/bin/env python3
"""One-off read-only diagnostic: print the raw manager block for one item
in one building, exactly as the API returns it. GET only."""
import json
import sys
import merc_status4 as m

if len(sys.argv) != 3:
    sys.exit("usage: python check_manager.py <building_id> <item name>")

building_id, item = sys.argv[1], sys.argv[2]
b = m.get("/buildings/%s" % building_id)
inv = b.get("storage", {}).get("inventory", {})
holdings = inv.get("holdings", {})
entry = holdings.get(item)

if entry is None:
    print("NOT FOUND under holdings -- available keys:")
    print(json.dumps(sorted(holdings.keys()), indent=2))
else:
    print(json.dumps(entry, indent=2, default=str))
