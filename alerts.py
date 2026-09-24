#!/usr/bin/env python3
"""Phone alerts for the Mercatorio business.

Opens one GitHub issue per problem that needs a human; the GitHub app pushes
new issues to the phone. Issues are deduped by title against open issues
labelled merc-alert, and an alert that has cleared gets its issue closed.

Sources:
  - merc_advisor.py --json --full flags: low_stock, no_order, zero_volume
    (stale_buy / stale_sell are left to merc_actor.py; "capped" by a full bin
    is normal for topped-up buys, so it is not alerted)
  - storehouse previous_flows: any shortfall (sustenance/input shortage) and
    labour expiration above EXPIRE_MIN (bought labour going to waste)

    python alerts.py          # dry run: print what would be opened/closed
    python alerts.py --live   # actually open/close issues (needs gh + GH_TOKEN)
"""
import json
import subprocess
import sys

import merc_status4 as m

LIVE = "--live" in sys.argv
LABEL = "merc-alert"
ALERT_KINDS = {"low_stock", "no_order", "zero_volume"}
EXPIRE_MIN = 5.0   # labour units wasted per turn before it is worth an alert


def gh(*args):
    return subprocess.run(["gh", *args], capture_output=True, text=True)


def flow_alerts(building_ids, wanted):
    for bid in building_ids:
        try:
            b = m.get("/buildings/%s" % bid)
        except SystemExit:
            continue
        flows = (b.get("storage", {}).get("inventory", {}).get("previous_flows")) or {}
        for item, fl in flows.items():
            short = m.num(fl.get("shortfall"))
            if short > 0:
                wanted["[merc] %s: shortage" % item] = (
                    "%s was %.1f short last turn -- household or production went without" % (item, short))
            if item == "labour" and m.num(fl.get("expiration")) > EXPIRE_MIN:
                wanted["[merc] labour: expiring"] = (
                    "%.1f bought labour expired unused last turn -- trim the labour buy" % m.num(fl.get("expiration")))


def main():
    out = subprocess.run([sys.executable, "merc_advisor.py", "--json", "--full"],
                         capture_output=True, text=True)
    if out.returncode != 0:
        print("advisor failed:", out.stderr[-800:])
        sys.exit(1)
    data = json.loads(out.stdout)

    wanted = {}
    for f in data.get("flags", []):
        if f.get("kind") in ALERT_KINDS:
            title = "[merc] %s: %s" % (f.get("item"), f.get("kind"))
            wanted[title] = "%s -- %s (%s)" % (f.get("item"), f.get("text", ""), f.get("building"))
    flow_alerts([r.get("building_id") for r in data.get("buildings", [])], wanted)

    hh = data.get("household", {})
    print("cash %s | prestige %s | %d alert(s)" % (hh.get("cash"), hh.get("prestige"), len(wanted)))
    for title, body in wanted.items():
        print("  ", title, "|", body)

    if not LIVE:
        print("(dry run -- no issues opened or closed)")
        return

    gh("label", "create", LABEL, "--color", "d93f0b", "--force")
    r = gh("issue", "list", "--label", LABEL, "--state", "open",
           "--limit", "100", "--json", "number,title")
    open_issues = {i["title"]: i["number"] for i in json.loads(r.stdout or "[]")}

    for title, body in wanted.items():
        if title not in open_issues:
            res = gh("issue", "create", "--title", title, "--body", body, "--label", LABEL)
            print("opened:" if res.returncode == 0 else "FAILED to open:", title, res.stderr.strip())

    for title, number in open_issues.items():
        if title not in wanted:
            gh("issue", "close", str(number), "--comment", "Cleared on the latest hourly check.")
            print("closed:", title)


if __name__ == "__main__":
    main()
