#!/usr/bin/env python3
"""One-off tool: raise (or change) an item's max_holding (its 'high stock
threshold' on the buy side) to a new value, preserving every other field on
that manager entry. Shows the exact change and asks for confirmation before
sending anything -- this is a real write, not a dry run.

    python set_max_holding.py <building_id> "<item>" <new_max_holding>
"""
import json
import sys
import urllib.error
import urllib.parse
import urllib.request

import merc_status4 as m

if len(sys.argv) != 4:
    sys.exit('usage: python set_max_holding.py <building_id> "<item>" <new_max_holding>')

building_id, item, new_max = sys.argv[1], sys.argv[2], sys.argv[3]

b = m.get("/buildings/%s" % building_id)
inv = b.get("storage", {}).get("inventory", {})
holdings = inv.get("holdings", {})
entry = holdings.get(item)

if entry is None:
    sys.exit("NOT FOUND under holdings for item %r" % item)

managers = entry.get("managers", [])
target = None
for mg in managers:
    if "max_holding" in mg:
        target = mg
        break

if target is None:
    sys.exit("No manager entry on %r has a max_holding field -- nothing to change." % item)

old_value = target["max_holding"]
print("Building %s / item %r" % (building_id, item))
print("  max_holding: %s -> %s" % (old_value, new_max))
print("  (all other fields on this manager entry stay unchanged)")
confirm = input("Send this change? [y/N] ").strip().lower()
if confirm != "y":
    print("Cancelled -- nothing sent.")
    sys.exit(0)

managers_patch = []
for mg in managers:
    clean = {k: v for k, v in mg.items() if k != "result"}
    if mg is target:
        clean["max_holding"] = int(new_max)
    managers_patch.append(clean)

url = "https://play.mercatorio.io/api/buildings/%s/storage/inventory/%s" % (
    building_id, urllib.parse.quote(item, safe=""))
payload = json.dumps({"managers": managers_patch}, default=str).encode()
req = urllib.request.Request(
    url, data=payload, method="PATCH",
    headers={
        "X-Merc-User": m.USER,
        "Authorization": "Bearer " + m.TOKEN,
        "Content-Type": "application/json",
        "Accept": "application/json",
    })
try:
    with urllib.request.urlopen(req, timeout=30) as r:
        print("OK -- status %s" % r.status)
except urllib.error.HTTPError as e:
    print("FAILED -- status %s: %s" % (e.code, e.read().decode()[:500]))
except urllib.error.URLError as e:
    print("FAILED -- network error: %s" % e.reason)
