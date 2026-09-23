#!/usr/bin/env python3
"""One-off tool: create a sell rule (min_holding reserve + sell_price +
sell_volume) for an item that currently has NO manager rules at all.
Shows the exact rule before sending; asks for confirmation.

    python create_sell_rule.py <building_id> "<item>" <min_holding> <sell_price> <sell_volume>
"""
import json
import sys
import urllib.error
import urllib.parse
import urllib.request

import merc_status4 as m

if len(sys.argv) != 6:
    sys.exit('usage: python create_sell_rule.py <building_id> "<item>" '
              '<min_holding> <sell_price> <sell_volume>')

building_id, item = sys.argv[1], sys.argv[2]
min_holding, sell_price, sell_volume = sys.argv[3], sys.argv[4], sys.argv[5]

b = m.get("/buildings/%s" % building_id)
inv = b.get("storage", {}).get("inventory", {})
holdings = inv.get("holdings", {})
entry = holdings.get(item)

if entry is None:
    sys.exit("NOT FOUND under holdings for item %r" % item)

managers = entry.get("managers", [])
non_empty = [mg for mg in managers if mg]
if non_empty:
    sys.exit("Item %r already has manager rule(s) set -- this tool is only "
              "for items with none. Refusing to overwrite an existing rule." % item)

new_rule = dict(
    min_holding=int(min_holding),
    sell_price=str(sell_price),
    sell_volume=int(sell_volume),
)

print("Building %s / item %r -- currently NO rule set" % (building_id, item))
print("Proposed new sell rule:")
print("  keep at least : %s" % new_rule["min_holding"])
print("  sell price    : %s" % new_rule["sell_price"])
print("  sell volume   : %s per turn" % new_rule["sell_volume"])
confirm = input("Send this rule? [y/N] ").strip().lower()
if confirm != "y":
    print("Cancelled -- nothing sent.")
    sys.exit(0)

url = "https://play.mercatorio.io/api/buildings/%s/storage/inventory/%s" % (
    building_id, urllib.parse.quote(item, safe=""))
payload = json.dumps({"managers": [new_rule]}, default=str).encode()
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
