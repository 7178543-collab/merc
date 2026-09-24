#!/usr/bin/env python3
"""Phone alerts + hourly status for the Mercatorio business.

1. Problems: one GitHub issue per problem (label merc-alert), deduped by
   title; an alert that has cleared gets its issue closed.
   - merc_advisor.py --json --full flags: low_stock, no_order, zero_volume
     (stale_buy / stale_sell are left to merc_actor.py; "capped" by a full bin
     is normal for topped-up buys, so it is not alerted)
   - storehouse previous_flows: any shortfall, and labour expiration above
     EXPIRE_MIN (bought labour going to waste)
2. Good news: every run posts a comment on one standing issue
   "[merc] hourly status" (label merc-status): OK / alerts, cash and the cash
   change since the last check, prestige, and where the ship is. The last cash
   figure is kept in that issue's body so the change can be computed.
   Cash change includes construction and stock purchases -- it is cash flow,
   not accounting profit.

    python alerts.py          # dry run: print what would be posted
    python alerts.py --live   # actually open/close/comment (needs gh + GH_TOKEN)
"""
import json
import re
import subprocess
import sys

import merc_status4 as m

LIVE = "--live" in sys.argv
LABEL = "merc-alert"
STATUS_LABEL = "merc-status"
STATUS_TITLE = "[merc] hourly status"
ALERT_KINDS = {"low_stock", "no_order", "zero_volume"}
EXPIRE_MIN = 5.0   # labour units wasted per turn before it is worth an alert
TOWNS = {"152202387": "Strasclives", "133002223": "Blanans",
         "151802239": "Grandgues", "140502554": "Calange"}


def gh(*args):
    return subprocess.run(["gh", *args], capture_output=True, text=True)


def town_name(tid):
    return TOWNS.get(str(tid), "town %s" % tid)


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


def ship_status():
    try:
        player = m.get("/player")
        biz = m.get("/businesses/%s" % player["household"]["business_ids"][0])
        out = []
        for tid in biz.get("transport_ids", []):
            t = m.get("/transports/%s" % tid)
            j = t.get("journey") or {}
            end = j.get("end_town_id")
            if end and str(end) != str(t.get("town_id")):
                where = "sailing to %s" % town_name(end)
            else:
                where = "docked at %s" % town_name(t.get("town_id"))
            out.append("%s %s" % (t.get("name"), where))
        return "; ".join(out) or "no ships"
    except (SystemExit, Exception) as e:
        return "unavailable (%s)" % type(e).__name__


def status_text(wanted, hh, prev_cash):
    cash = m.num(hh.get("cash"))
    head = "OK - all clear" if not wanted else "ATTENTION - %d alert(s): %s" % (
        len(wanted), "; ".join(t.replace("[merc] ", "") for t in wanted))
    delta = "" if prev_cash is None else " (%+.0f since last check)" % (cash - prev_cash)
    return "%s\ncash %.0f%s | prestige %.1f\nship: %s" % (
        head, cash, delta, m.num(hh.get("prestige")), ship_status())


def post_status(wanted, hh):
    gh("label", "create", STATUS_LABEL, "--color", "0e8a16", "--force")
    r = gh("issue", "list", "--label", STATUS_LABEL, "--state", "open",
           "--limit", "5", "--json", "number,body")
    issues = json.loads(r.stdout or "[]")
    prev_cash = None
    if issues:
        num = str(issues[0]["number"])
        mm = re.search(r"last_cash: ([-\d.]+)", issues[0].get("body") or "")
        if mm:
            prev_cash = float(mm.group(1))
    else:
        res = gh("issue", "create", "--title", STATUS_TITLE, "--label", STATUS_LABEL,
                 "--body", "Hourly status from alerts.py. Keep this issue open.")
        num = res.stdout.strip().rsplit("/", 1)[-1]
    body = status_text(wanted, hh, prev_cash)
    gh("issue", "comment", num, "--body", body)
    gh("issue", "edit", num, "--body",
       "Hourly status from alerts.py. Keep this issue open.\n\nlast_cash: %.2f" % m.num(hh.get("cash")))
    print("status posted to #%s" % num)


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
    print(status_text(wanted, hh, None))
    for title, body in wanted.items():
        print("  ", title, "|", body)

    if not LIVE:
        print("(dry run -- no issues opened, closed or commented)")
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

    post_status(wanted, hh)


if __name__ == "__main__":
    main()
