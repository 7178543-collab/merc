#!/usr/bin/env python3
"""Phone alerts for the Mercatorio business.

Runs merc_advisor.py --json, keeps the flags that need a human (running out,
a full storage bin, stock with no rule), and opens one GitHub issue per
problem. The GitHub app pushes new issues to the phone. Issues are deduped by
title against open issues labelled merc-alert, and an alert that has cleared
gets its issue closed automatically.

    python alerts.py          # dry run: print what would be opened/closed
    python alerts.py --live   # actually open/close issues (needs gh + GH_TOKEN)
"""
import json
import subprocess
import sys

LIVE = "--live" in sys.argv
LABEL = "merc-alert"

# flag kinds from merc_advisor.flag_item that mean "a human should look".
# stale_buy / stale_sell are left out on purpose: merc_actor.py fixes those.
ALERT_KINDS = {"low_stock", "no_order", "zero_volume"}


def gh(*args):
    return subprocess.run(["gh", *args], capture_output=True, text=True)


def wanted_alerts(data):
    wanted = {}
    for f in data.get("flags", []):
        kind = f.get("kind")
        text = f.get("text", "")
        # "capped" by space = the storage bin is full
        if kind in ALERT_KINDS or (kind == "capped" and "space" in text):
            title = "[merc] %s: %s" % (f.get("item"), kind)
            wanted[title] = "%s -- %s (%s)" % (f.get("item"), text, f.get("building"))
    return wanted


def main():
    out = subprocess.run([sys.executable, "merc_advisor.py", "--json"],
                         capture_output=True, text=True)
    if out.returncode != 0:
        print("advisor failed:", out.stderr[-800:])
        sys.exit(1)
    data = json.loads(out.stdout)
    wanted = wanted_alerts(data)
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
