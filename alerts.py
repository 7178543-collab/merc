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
import os
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
    """List of dicts, one per ship: name, state, place, recipe + route/op/imp/exp/cargo."""
    try:
        player = m.get("/player")
        biz = m.get("/businesses/%s" % player["household"]["business_ids"][0])
        out = []
        for tid in biz.get("transport_ids", []):
            t = m.get("/transports/%s" % tid)
            j = t.get("journey") or {}
            end = j.get("end_town_id") or j.get("destination_town_id")
            prod = t.get("producer") or {}
            recipe = prod.get("recipe")
            if isinstance(recipe, dict):
                recipe = recipe.get("name") or recipe.get("reference") or str(recipe)
            loc = t.get("location") or {}
            town = t.get("town_id")
            if recipe and "fish" in str(recipe):
                state, place = "fishing", "at sea %s:%s" % (loc.get("x"), loc.get("y"))
            elif end and str(end) != str(town):
                state, place = "sailing", "to %s" % town_name(end)
            elif town:
                state, place = "docked", "at %s" % town_name(town)
            else:
                state, place = "anchored", "at sea %s:%s" % (loc.get("x"), loc.get("y"))
            entry = {"name": t.get("name"), "state": state, "place": place,
                     "recipe": recipe, "level": m.num(prod.get("target"))}
            # --- extended fields (never break the existing keys) ---
            try:
                route = t.get("route") or {}
                dest = route.get("remote_town") or end or route.get("local_town")
                entry["route"] = town_name(dest) if dest else None
                prev = prod.get("previous_operation") or {}
                tgt = m.num(prod.get("target") or prev.get("target"))
                entry["op"] = round(100.0 * tgt, 1) if tgt and tgt <= 1 else tgt
                imp, exp = {}, {}
                for item, mg in (route.get("managers") or {}).items():
                    if not isinstance(mg, dict):
                        continue
                    bv, sv = m.num(mg.get("buy_volume")), m.num(mg.get("sell_volume"))
                    if bv:
                        imp[item] = round(bv, 1)
                    if sv:
                        exp[item] = round(sv, 1)
                entry["imp"] = imp or None
                entry["exp"] = exp or None
                cargo = {}
                inv = (t.get("cargo") or {}).get("inventory") or t.get("inventory") or {}
                assets = (inv.get("account") or {}).get("assets") or inv.get("assets") or {}
                for item, a in assets.items():
                    q = m.num(a.get("balance") if isinstance(a, dict) else a)
                    if q:
                        cargo[item] = round(q, 1)
                entry["cargo"] = cargo or None
            except (SystemExit, Exception) as e:
                print("ship extras skipped:", type(e).__name__)
            out.append(entry)
        return out
    except (SystemExit, Exception) as e:
        return [{"name": "ship", "state": "unknown", "place": type(e).__name__}]


def ship_text(ships):
    return "; ".join("%s %s %s" % (s["name"], s["state"], s["place"]) for s in ships) or "no ships"


def status_text(wanted, hh, prev_cash, ships):
    # Taylor wants the email readable at a glance: "All good" or "Check Ops",
    # then one line of money: cash (change since last email), trading profit last turn, prestige.
    cash = m.num(hh.get("cash"))
    if not wanted:
        head = "\u2705 All good"
    else:
        head = "\u26a0\ufe0f Check Ops (%d issue%s)" % (len(wanted), "" if len(wanted) == 1 else "s")
    delta = "" if prev_cash is None else " (%+.0f)" % (cash - prev_cash)
    x = money_extra()
    money = "cash %s%s" % ("{:,.0f}".format(cash), delta)
    if "profit" in x:
        money += " \u00b7 profit %+.0f last turn" % x["profit"]
    if "prestige_free" in x:
        money += " \u00b7 prestige %.0f free (%+.1f/turn)" % (x["prestige_free"], x.get("prestige_rate", 0))
    return "%s\n%s" % (head, money)


_MONEY = {}


def money_extra():
    """Turn, trading profit and spendable prestige for the history line. Never fails the run."""
    if _MONEY:
        return dict(_MONEY)
    out = _MONEY
    try:
        f = ((m.get("/buildings/152202386005001").get("storage") or {}).get("inventory") or {}).get("previous_flows") or {}
        sale = sum(m.num(x.get("sale_value")) for x in f.values())
        buy = sum(m.num(x.get("purchase_cost")) for x in f.values())
        out.update(profit=round(sale - buy, 2), sales=round(sale, 2), buys=round(buy, 2))
    except (SystemExit, Exception):
        pass
    try:
        h = m.get("/households/21623")
        b = h.get("prestige_board") or {}
        out["prestige_free"] = round(m.num(h.get("prestige")) - m.num(b.get("allocated")), 2)
        out["prestige_rate"] = round(sum(m.num(x.get("impact")) for x in (h.get("prestige_impacts") or [])), 2)
    except (SystemExit, Exception):
        pass
    try:
        out["turn"] = int(m.num(m.get("/clock").get("turn")))
    except (SystemExit, Exception):
        pass
    return out


def data_line(wanted, hh, ships, snap, prices, held):
    items = {}
    for item in sorted(set(snap) | set(held)):
        f = snap.get(item, {})
        row = [round(held.get(item, 0), 1)] + [f.get(k, 0) for k in FLOW_KEYS] + [prices.get(item, 0)]
        if any(row):
            items[item] = row
    extra = money_extra()
    d = {
        "v": 2,
        "t": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        "cash": round(m.num(hh.get("cash")), 2),
        "prestige": round(m.num(hh.get("prestige")), 2),
        **extra,
        "alerts": [t.replace("[merc] ", "") for t in wanted],
        "ships": ships,
        "cols": ["held"] + FLOW_KEYS + ["price"],
        "items": items,
    }

    # 1. buildings
    try:
        player = m.get("/player")
        biz = m.get("/businesses/%s" % player["household"]["business_ids"][0])
        bld = []
        for bb in biz.get("buildings") or []:
            bid = bb.get("id") if isinstance(bb, dict) else bb
            if not bid:
                continue
            try:
                b = m.get("/buildings/%s" % bid)
            except SystemExit:
                continue
            name = b.get("name") or (bb.get("name") if isinstance(bb, dict) else None) or str(bid)
            prod = b.get("producer") or {}
            recipe = prod.get("recipe")
            if isinstance(recipe, dict):
                recipe = recipe.get("name") or recipe.get("reference") or str(recipe)
            prev = prod.get("previous_operation") or {}
            cur_rate = round(m.num(prev.get("production") or prev.get("volume")), 1)
            tgt_rate = round(m.num(prod.get("target") or prev.get("target")), 1)
            flags = []
            if not recipe:
                flags.append("idle")
            cons = b.get("construction")
            if cons:
                flags.append("%d%%" % int(m.num(cons.get("progress"))))
            if prod.get("limited"):
                flags.append("limited")
            mgr = prod.get("manager") if isinstance(prod.get("manager"), dict) else {}
            for src in (prod, b, mgr):
                if isinstance(src, dict) and (src.get("clearcut") or src.get("clear_cutting") or
                                              (isinstance(src.get("flags"), list) and "clearcut" in src["flags"])):
                    flags.append("clearcut")
                    break
            bld.append([name, recipe, cur_rate, tgt_rate, flags or None])
        d["bld"] = bld
    except (SystemExit, Exception) as e:
        print("bld skipped:", type(e).__name__)

    # 2. storehouse automated orders
    try:
        sh = m.get("/buildings/%s" % "152202386005001")
        inv = (sh.get("storage") or {}).get("inventory") or {}
        holdings = inv.get("holdings") or {}
        ord_ = {}
        for item, h in holdings.items():
            managers = h.get("managers", []) if isinstance(h, dict) else []
            buy_vol = buy_max = buy_high = sell_vol = sell_min = sell_low = None
            for mg in managers or []:
                if not isinstance(mg, dict):
                    continue
                if mg.get("buy_volume") is not None:
                    buy_vol = round(m.num(mg.get("buy_volume")), 1)
                    buy_max = round(m.num(mg.get("buy_price")), 2) if mg.get("buy_price") is not None else None
                    buy_high = round(m.num(mg.get("max_holding")), 1) if mg.get("max_holding") is not None else None
                if mg.get("sell_volume") is not None:
                    sell_vol = round(m.num(mg.get("sell_volume")), 1)
                    sell_min = round(m.num(mg.get("sell_price")), 2) if mg.get("sell_price") is not None else None
                    sell_low = round(m.num(mg.get("min_holding")), 1) if mg.get("min_holding") is not None else None
            if any(x is not None for x in (buy_vol, buy_max, buy_high, sell_vol, sell_min, sell_low)):
                ord_[item] = [buy_vol or 0, buy_max, buy_high, sell_vol or 0, sell_min, sell_low]
        d["ord"] = ord_
    except (SystemExit, Exception) as e:
        print("ord skipped:", type(e).__name__)

    return "merc-data: " + json.dumps(d, separators=(",", ":"), default=str)


def save_history(dline):
    """Append this run's merc-data line to history/merc-YYYY-MM.jsonl; the
    workflow commits it. Never fails the run."""
    try:
        os.makedirs("history", exist_ok=True)
        path = os.path.join("history", "merc-%s.jsonl" % datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m"))
        with open(path, "a") as f:
            f.write(dline.split("merc-data: ", 1)[-1] + "\n")
    except Exception as e:
        print("history write failed:", e)


def post_status(wanted, hh, ships, dline):
    save_history(dline)
    # the late-in-turn run only emails when something needs a look (no second "All good" per hour)
    import datetime as _dt
    if _dt.datetime.utcnow().minute >= 30 and not wanted:
        print("late run, all good: no status comment")
        return
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
    # the data line stays in the comment for the Strasclives Ledger, hidden from the rendered email
    body = status_text(wanted, hh, prev_cash, ships) + "\n\n<!--\n" + dline + "\n-->"
    gh("issue", "comment", num, "--body", body)
    gh("issue", "edit", num, "--body",
       "Hourly status from alerts.py. Keep this issue open.\n\nlast_cash: %.2f" % m.num(hh.get("cash")))
    print("status posted to #%s" % num)


def contract_alerts(wanted, prices, held):
    """New church/NPC offers in our town that pay bonus prestige (Taylor, Sep 26:
    'keep a closer look for those contracts'). One issue per offer while it is
    open and unsigned; it closes itself once signed or gone. Shows what we hold,
    the rough cost at home prices and coin per prestige."""
    try:
        c = m.get("/contracts/towns/152202387")
    except SystemExit:
        print("contracts: town board not readable with this token")
        return
    for x in (c.get("contracts") if isinstance(c, dict) else c) or []:
        bonus = m.num(x.get("bonus"))
        if not bonus or x.get("signed"):
            continue
        for t in x.get("transactions") or []:
            if t.get("direction") != "bid":      # they want goods delivered
                continue
            item, vol = t.get("asset"), m.num(t.get("volume"))
            have = held.get(item, 0)
            price = prices.get(item, 0)
            cost = vol * price
            per = ("%.0f coin/prestige" % (cost / bonus)) if cost else "no home price"
            verdict = "WE HOLD ENOUGH: sign and deliver now" if have >= vol else "need %.0f more" % (vol - have)
            length = (t.get("timeframe") or {}).get("length")
            wanted["[merc] church contract: %s" % item] = (
                "Deliver %.0f %s for +%.0f prestige (penalty %s, %s turns). We hold %.0f. "
                "Cost about %.0f at home prices = %s. %s." % (
                    vol, item, bonus, t.get("penalty", "?"), length, have, cost, per, verdict))


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
    contract_alerts(wanted, prices, held)

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
