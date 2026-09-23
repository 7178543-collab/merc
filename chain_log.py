#!/usr/bin/env python3
"""Append one timestamped snapshot of the flax->thread->cloth->garments
chain (plus nets) to merc_chain_log.jsonl. Combines: your own held stock
and net production (from the storehouse, where you hold the item), and
town-wide market price/volume/trend and consumer demand (where it exists).
GET only. Meant to be run repeatedly over time -- each run adds one line;
the value comes from having many runs to compare, not any single one.

    python chain_log.py                      # logs the default chain items
    python chain_log.py "flax fibres" cloth   # logs just these
"""
import datetime
import json
import sys

import merc_status4 as m
import merc_advisor as adv

DEFAULT_ITEMS = ["flax plants", "flax fibres", "thread", "cloth", "garments", "nets"]
LOG_PATH = "merc_chain_log.jsonl"

items = sys.argv[1:] or DEFAULT_ITEMS

player = adv.safe_get("/player")
hh = player.get("household", {})
town_id = hh.get("town_id")
biz_id = hh["business_ids"][0]
biz = adv.safe_get("/businesses/%s" % biz_id)
stores = [b for b in biz.get("buildings", []) if b.get("type") in ("storehouse", "warehouse")]
building_id = stores[0]["id"] if stores else None

town = m.get("/towns/%s" % town_id)
mkt = m.get("/towns/%s/marketdata" % town_id).get("markets", {})

demand_lookup = {}
for cat in town.get("commoners", {}).get("spending", []):
    for p in cat.get("products", []):
        demand_lookup[p.get("product")] = dict(
            desire=p.get("desire"), request=p.get("request"),
            result=p.get("result"), category=cat.get("name"))

building_items = {}
if building_id:
    r = adv.building_report(building_id, {}, town_id)
    building_items = r["items"]

ts = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
snapshot = dict(ts=ts, items={})

for item in items:
    entry = {}
    bi = building_items.get(item)
    if bi:
        entry["held"] = bi.get("held")
        entry["net"] = bi.get("net")
        entry["unit_cost"] = bi.get("unit_cost")
    mk = mkt.get(item)
    if mk:
        entry["price"] = m.num(mk.get("price"))
        entry["highest_bid"] = m.num(mk.get("highest_bid"))
        entry["lowest_ask"] = m.num(mk.get("lowest_ask"))
        entry["volume"] = mk.get("volume")
        entry["volume_prev_12"] = mk.get("volume_prev_12")
        entry["moving_average"] = m.num(mk.get("moving_average"))
    dm = demand_lookup.get(item)
    if dm:
        entry["demand"] = dm
    snapshot["items"][item] = entry

with open(LOG_PATH, "a") as f:
    f.write(json.dumps(snapshot, default=str) + "\n")

print(json.dumps(snapshot, indent=2, default=str))
print("\n(appended to %s)" % LOG_PATH)
