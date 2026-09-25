#!/usr/bin/env python3
"""Phone alerts + hourly status for the Mercatorio business.

1. Problems: one GitHub issue per problem (label merc-alert), deduped by
   title; an alert that has cleared gets its issue closed.
   - merc_advisor.py --json --full flags: low_stock, no_order, zero_volume
     (stale_buy / stale_sell are left to merc_actor.py; "capped" by a full bin
     is normal for topped-up buys, so it is not alerted)
   - storehouse previous_flows: any shortfall, and labour expiration above
     EXPIRE_MIN (bought labour going to waste)
   - order watch: a sell rule moving under half its volume with stock piling
     up ("not selling"), or a buy rule filling under half while stock is
     down to ~2 turns of use ("buy not filling")
2. Good news: every run posts a comment on one standing issue
   "[merc] hourly status" (label merc-status): OK / alerts, cash and the cash
   change since the last check, prestige, and where the ship is. The last cash
   figure is kept in that issue's body so the change can be computed.
   Cash change includes construction and stock purchases -- it is cash flow,
   not accounting profit.
3. Dashboard feed: the status comment ends with one line
   "merc-data: {json}" -- a compact snapshot (cash, prestige, ship, and per
   item: held, produced, consumed, sold, bought, expired, market price).
   The Merc dashboard page reads it from the GitHub notification emails.

    python alerts.py          # dry run: print what would be posted
    python alerts.py --live   # actually open/close/comment (needs gh + GH_TOKEN)
"""
import datetime
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
FLOW_KEYS = ["production", "consumption", "sale", "purchase", "expiration"]


def gh(*args):
    return subprocess.run(["gh", *args], capture_output=True, text=True)


def town_name(tid):
    return TOWNS.get(str(tid), "town %s" % tid)


def flow_alerts(building_ids, wanted, snap):
    """Alert on shortfalls / wasted labour, and collect flows into snap."""
    for bid in building_ids:
        try:
            b = m.get("/buildings/%s" % bid)
        except SystemExit:
            continue
        flows = (b.get("storage", {}).get("inventory", {}).get("previous_flows")) or {}
        for item, fl in flows.items():
            row = snap.setdefault(item, {})
            for k in FLOW_KEYS:
                v = m.num(fl.get(k))
                if v:
                    row[k] = round(row.get(k, 0) + v, 2)
            short = m.num(fl.get("shortfall"))
            if short > 0:
                wanted["[merc] %s: shortage" % item] = (
                    "%s was %.1f short last turn -- household or production went without" % (item, short))
            if item == "labour" and m.num(fl.get("expiration")) > EXPIRE_MIN:
                wanted["[merc] labour: expiring"] = (
                    "%.1f bought labour expired unused last turn -- trim the labour buy" % m.num(fl.get("expiration")))


def watch_alerts(buildings, snap, wanted):
    """Orders that aren't working, from last turn's flows vs the standing rules:
    - a sell rule that moved under half its volume while real stock sits
      above the keep level  -> "<item>: not selling" (price floor too high,
      or the market is full)
    - a buy rule that filled under half its volume while stock is down to
      about two turns of use -> "<item>: buy not filling" (max price too low,
      or nobody is selling)"""
    for r in buildings:
        for item, d in (r.get("items") or {}).items():
            held = m.num(d.get("held"))
            fl = snap.get(item, {})
            sold, bought = fl.get("sale", 0), fl.get("purchase", 0)
            used = fl.get("consumption", 0)
            for mg in d.get("managers") or []:
                sv, sp = m.num(mg.get("sell_volume")), m.num(mg.get("sell_price"))
                keep = m.num(mg.get("min_holding"))
                if sv > 0 and sold < 0.5 * sv and held > keep + 2 * sv:
                    wanted["[merc] %s: not selling" % item] = (
                        "%s sold %.0f of %.0f/turn at >= %.2f; %.0f in stock. Lower the floor "
                        "or cut production." % (item, sold, sv, sp, held))
                bv, bp = m.num(mg.get("buy_volume")), m.num(mg.get("buy_price"))
                if bv > 0 and bought < 0.5 * bv and used > 0 and held < 2 * used:
                    wanted["[merc] %s: buy not filling" % item] = (
                        "%s bought %.0f of %.0f/turn at <= %.2f; %.0f left, uses %.0f/turn. "
                        "Raise the max price or slow the buildings that use it."
                        % (item, bought, bv, bp, held, used))


def ship_info():
    """List of dicts, one per ship: name, state, place, recipe."""
    try:
        player = m.get("/player")
        biz = m.get("/businesses/%s" % player["household"]["business_ids"][0])
        out = []
        for tid in biz.get("transport_ids", []):
            t = m.get("/transports/%s" % tid)
            j = t.get("journey") or {}
            end = j.get("end_town_id")
            prod = t.get("producer") or {}
            recipe = prod.get("recipe")
            loc = t.get("location") or {}
            town = t.get("town_id")
            if recipe and "fish" in recipe:
                state, place = "fishing", "at sea %s:%s" % (loc.get("x"), loc.get("y"))
            elif end and str(end) != str(town):
                state, place = "sailing", "to %s" % town_name(end)
            elif town:
                state, place = "docked", "at %s" % town_name(town)
            else:
                state, place = "anchored", "at sea %s:%s" % (loc.get("x"), loc.get("y"))
            out.append({"name": t.get("name"), "state": state, "place": place,
                        "recipe": recipe, "level": m.num(prod.get("target"))})
        return out
    except (SystemExit, Exception) as e:
        return [{"name": "ship", "state": "unknown", "place": type(e).__name__}]


def ship_text(ships):
    return "; ".join("%s %s %s" % (s["name"], s["state"], s["place"]) for s in ships) or "no ships"


def status_text(wanted, hh, prev_cash, ships):
    cash = m.num(hh.get("cash"))
    head = "OK - all clear" if not wanted else "ATTENTION - %d alert(s): %s" % (
        len(wanted), "; ".join(t.replace("[merc] ", "") for t in wanted))
    delta = "" if prev_cash is None else " (%+.0f since last check)" % (cash - prev_cash)
    return "%s\ncash %.0f%s | prestige %.1f\nship: %s" % (
        head, cash, delta, m.num(hh.get("prestige")), ship_text(ships))


def data_line(wanted, hh, ships, snap, prices, held):
    items = {}
    for item in sorted(set(snap) | set(held)):
        f = snap.get(item, {})
        row = [round(held.get(item, 0), 1)] + [f.get(k, 0) for k in FLOW_KEYS] + [prices.get(item, 0)]
        if any(row):
            items[item] = row
    d = {
        "v": 1,
        "t": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        "cash": round(m.num(hh.get("cash")), 2),
        "prestige": round(m.num(hh.get("prestige")), 2),
        "alerts": [t.replace("[merc] ", "") for t in wanted],
        "ships": ships,
        "cols": ["held"] + FLOW_KEYS + ["price"],
        "items": items,
    }
    return "merc-data: " + json.dumps(d, separators=(",", ":"), default=str)


def post_status(wanted, hh, ships, dline):
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
    body = status_text(wanted, hh, prev_cash, ships) + "\n\n" + dline
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

    prices, held = {}, {}
    for r in data.get("buildings", []):
        for item, d in (r.get("items") or {}).items():
            held[item] = held.get(item, 0) + m.num(d.get("held"))
            if m.num(d.get("last_price")):
                prices[item] = m.num(d.get("last_price"))
    snap = {}
    flow_alerts([r.get("building_id") for r in data.get("buildings", [])], wanted, snap)
    watch_alerts(data.get("buildings", []), snap, wanted)

    hh = data.get("household", {})
    ships = ship_info()
    dline = data_line(wanted, hh, ships, snap, prices, held)
    print(status_text(wanted, hh, None, ships))
    print(dline[:300] + ("..." if len(dline) > 300 else ""), "(%d chars)" % len(dline))
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

    post_status(wanted, hh, ships, dline)


if __name__ == "__main__":
    main()
