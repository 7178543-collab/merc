#!/usr/bin/env python3
"""Oversight bot: READ-ONLY information gathering for planning and oversight (Nov 1 2026, Taylor: "make an
information gathering bot ... use the API, get the most and best info you can").

It never changes anything in the game and never writes the token anywhere. Credentials come from ~/.merc_creds
(written by the workflow from the MERC_CREDS secret); with no creds the API section is skipped and the repo-state
sections still run.

Inputs : GET-only API calls (player, household, business, home town, church, contracts, scoreboards) + what the
         other bots already wrote (history/merc-YYYY-MM.jsonl, state/v2/goal_history.jsonl, state/failsafe.json,
         state/guardian.json, state/order_queue_done.jsonl, state/v2/diagnose.json, state/v2/report.md).
Outputs: state/oversight/latest.md    one-screen briefing (Claude and Taylor read this first)
         state/oversight/latest.json  the same numbers, machine readable
         state/oversight/log.jsonl    one compact line per run (the game log), trimmed to the last 600 runs
         state/oversight/changes.md   what the bots changed in the last 24 h (the change log)
Run    : python tools/oversight.py [--offline]
"""
import datetime
import glob
import gzip
import json
import os
import sys
import time
import urllib.request

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(HERE, "state", "oversight")
BASE = "https://play.mercatorio.io/api"
CREDS = os.path.expanduser("~/.merc_creds")
NAME = "Barthélemy de Gaillon"
HOME_TOWN = "152202387"
BUSINESS = "39992"
CASH_FLOOR = 1600           # guardian's current floor (state/guardian.json overrides if present)
FREE_TARGET = 15            # banquet rescue target (prestige_rules.BANQUET_FREE_KEEP)
TIME_BUDGET = 60            # seconds for all API calls together

NOW = datetime.datetime.now(datetime.timezone.utc)


# ------------------------------------------------------------------ helpers
def jload(path, default=None):
    try:
        with open(os.path.join(HERE, path)) as f:
            return json.load(f)
    except (OSError, ValueError):
        return default


def jlines(path, last=None):
    out = []
    try:
        with open(os.path.join(HERE, path)) as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        out.append(json.loads(line))
                    except ValueError:
                        pass
    except OSError:
        pass
    return out[-last:] if last else out


def num(x, d=0.0):
    try:
        return float(x)
    except (TypeError, ValueError):
        return d


def parse_t(s):
    try:
        return datetime.datetime.fromisoformat(s.replace("Z", "+00:00"))
    except (AttributeError, ValueError):
        return None


def slope(ys):
    """least-squares slope per step of a list of numbers (None for < 3 points)."""
    n = len(ys)
    if n < 3:
        return None
    xm, ym = (n - 1) / 2.0, sum(ys) / n
    den = sum((i - xm) ** 2 for i in range(n))
    return sum((i - xm) * (y - ym) for i, y in enumerate(ys)) / den if den else None


def r(x, nd=0):
    return None if x is None else round(x, nd)


def fmt(x, nd=0, sign=False):
    if x is None:
        return "n/a"
    s = ("%+." if sign else "%.") + str(nd) + "f"
    return s % x


# ------------------------------------------------------------------ API (GET only)
class Api:
    def __init__(self, offline=False):
        self.ok = False
        self.user = self.token = None
        self.calls = 0
        self.errors = []
        self.t0 = time.time()
        if offline:
            return
        try:
            with open(CREDS) as f:
                c = json.load(f)
            self.user, self.token = c["user"], c["token"]
            self.ok = True
        except (OSError, ValueError, KeyError):
            self.errors.append("no credentials: API section skipped")

    def get(self, path):
        if not self.ok or time.time() - self.t0 > TIME_BUDGET:
            return None
        req = urllib.request.Request(BASE + path, method="GET", headers={
            "X-Merc-User": self.user, "Authorization": "Bearer " + self.token, "Accept": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=25) as resp:
                raw = resp.read()
            if raw[:2] == b"\x1f\x8b":
                raw = gzip.decompress(raw)
            self.calls += 1
            return json.loads(raw.decode())
        except Exception as e:           # never print the request (headers hold the token)
            self.errors.append("%s: %s" % (path, type(e).__name__))
            return None


def api_section(api):
    """What only the live game knows: rank and gaps on the scoreboards, town size, church asks, open contracts."""
    res = {"available": api.ok}
    if not api.ok:
        return res
    pl = api.get("/player") or {}
    hid = (pl.get("household") or {}).get("id")
    res["household_id"] = hid
    hh = api.get("/households/%s" % hid) if hid else None
    if hh:
        pb = hh.get("prestige_board") or {}
        total = num(pb.get("prestige"), num(hh.get("prestige")))
        imp = pb.get("current_impacts") or pb.get("previous_impacts") or pb.get("prestige_impacts") or hh.get("prestige_impacts") or []
        if isinstance(imp, dict):
            rate = sum(num(v) for v in imp.values())
        else:
            rate = sum(num(x.get("impact")) if isinstance(x, dict) else num(x) for x in imp)
        res["prestige"] = {
            "total": r(total, 1), "allocated": r(num(pb.get("allocated")), 1), "free": r(total - num(pb.get("allocated")), 1),
            "rate": r(rate, 2), "legacy": r(num(pb.get("legacy")), 1), "ascent": r(num(pb.get("ascent")), 1),
            "levels": {k: v for k, v in pb.items() if k.endswith("_level")},
        }
        try:        # where prestige comes from and goes: the breakdown the rate is the sum of
            items = imp.items() if isinstance(imp, dict) else [(x.get("factor") or x.get("recipe") or x.get("name") or "?", x.get("impact")) for x in imp if isinstance(x, dict)]
            res["prestige"]["impacts"] = sorted(((str(k), r(num(v), 2)) for k, v in items), key=lambda kv: -abs(kv[1]))[:12]
        except Exception:
            pass
        res["workers"] = [{"name": w.get("name"), "assignment": w.get("assignment"),
                           "top": sorted(((k, r(num(v), 1)) for k, v in (w.get("skills") or {}).items()),
                                         key=lambda kv: -kv[1])[:2]} for w in hh.get("workers") or []]
    sc = api.get("/scoreboard/main") or {}
    glob_ = sc.get("global") or []
    if glob_:
        rows = sorted(glob_, key=lambda x: -num(x.get("legacy")))
        me = next((i for i, x in enumerate(rows) if x.get("name") == NAME), None)
        res["legacy"] = {
            "players": len(rows),
            "rank": None if me is None else me + 1,
            "ours": None if me is None else r(num(rows[me].get("legacy")), 1),
            "prestige": None if me is None else r(num(rows[me].get("prestige")), 1),
            "top5": [(x.get("name"), x.get("town_name"), r(num(x.get("legacy")), 0), r(num(x.get("prestige")), 0)) for x in rows[:5]],
            "neighbours": [] if me is None else [
                (x.get("name"), r(num(x.get("legacy")), 0)) for x in rows[max(0, me - 2): me + 3] if x.get("name") != NAME],
            "gap_to_next": None if not me else r(num(rows[me - 1].get("legacy")) - num(rows[me].get("legacy")), 1),
            "median": r(num(rows[len(rows) // 2].get("legacy")), 1),
        }
        # how many players have more prestige income than legacy drain would explain: our standing by prestige too
        byp = sorted(glob_, key=lambda x: -num(x.get("prestige")))
        mp = next((i for i, x in enumerate(byp) if x.get("name") == NAME), None)
        res["legacy"]["prestige_rank"] = None if mp is None else mp + 1
    prod = api.get("/scoreboard/production") or {}
    leaders = prod.get("production") or {}
    ours = []
    for item, lst in leaders.items():
        for i, x in enumerate(lst or []):
            if isinstance(x, dict) and x.get("name") == NAME:
                ours.append((item, i + 1))
    res["production_ranks"] = sorted(ours, key=lambda t: t[1])[:12]
    town = api.get("/towns/%s" % HOME_TOWN) or {}
    if town:
        cm = town.get("commoners") or {}
        res["town"] = {"commoners": cm.get("count"), "growth_progress": cm.get("growth_progress"),
                       "migration": cm.get("migration"), "households": len(town.get("household_ids") or [])}
    ch = api.get("/towns/%s/church" % HOME_TOWN) or {}
    res["church_contracts"] = len(ch.get("contract_ids") or [])
    cons = api.get("/businesses/%s/contracts" % BUSINESS) or {}
    lst = cons.get("contracts") or []
    states = {}
    for c in lst:
        states[c.get("state")] = states.get(c.get("state"), 0) + 1
    res["contracts"] = {"total": len(lst), "by_state": states}
    res["calls"] = api.calls
    if api.errors:
        res["errors"] = api.errors[:6]
    return res


# ------------------------------------------------------------------ repo-state analysis
def history_rows():
    files = sorted(glob.glob(os.path.join(HERE, "history", "merc-*.jsonl")))[-2:]
    rows = []
    for f in files:
        rows += jlines(os.path.relpath(f, HERE))
    return rows


def analyse(api_res):
    rows = history_rows()
    out = {"generated": NOW.isoformat(timespec="seconds")}
    flags = []

    def flag(sev, text):
        flags.append({"sev": sev, "text": text})

    if not rows:
        flag("HIGH", "no history file: the bot has written nothing")
        return out, flags
    cur = rows[-1]
    tcur = parse_t(cur.get("t"))
    age_h = (NOW - tcur).total_seconds() / 3600 if tcur else None
    out["turn"] = cur.get("turn")
    out["data_age_h"] = r(age_h, 1)
    if age_h is not None and age_h > 3:
        flag("HIGH", "bot data is %.1f h old: the GitHub clock or merc-actor may have stopped" % age_h)

    # one row per turn (several runs a turn) -> last 24 turns
    byturn = {}
    for x in rows:
        byturn[x.get("turn")] = x
    turns = sorted(k for k in byturn if k is not None)
    seq = [byturn[t] for t in turns][-25:]
    cash = [num(x.get("cash")) for x in seq]
    free = [num(x.get("prestige_free")) for x in seq]
    gaps = [b - a for a, b in zip(turns[-25:], turns[-24:]) if b - a > 1]
    if gaps:
        flag("MED", "history has %d skipped turn(s) in the last 24: the bots missed runs" % len(gaps))

    c = {"now": r(cash[-1]), "d6": r(cash[-1] - cash[-7]) if len(cash) > 6 else None,
         "d12": r(cash[-1] - cash[-13]) if len(cash) > 12 else None,
         "d24": r(cash[-1] - cash[0]) if len(cash) > 12 else None,
         "slope12": r(slope(cash[-13:]), 1), "slope24": r(slope(cash), 1)}
    sl = c["slope12"]
    for h in (12, 48, 120):
        c["in%d" % h] = None if sl is None else r(cash[-1] + sl * h)
    out["cash"] = c

    # prestige
    rate = num(cur.get("prestige_rate"))
    fr = free[-1]
    p = {"total": r(num(cur.get("prestige")), 1), "free": r(fr, 1), "rate": r(rate, 2),
         "free_slope12": r(slope(free[-13:]), 2),
         "turns_to_zero": r(-fr / rate, 1) if fr < 0 and rate > 0 else None,
         "turns_to_target": r((FREE_TARGET - fr) / rate, 1) if fr < FREE_TARGET and rate > 0 else None,
         "turns_to_tenants": r((800 - fr) / rate, 0) if rate > 0 and fr < 800 else None}
    out["prestige"] = p
    if fr < 0 and rate <= 0:
        flag("HIGH", "free prestige %.1f and still falling %.2f/turn: a random track level can drop" % (fr, rate))
    elif fr < 0:
        flag("MED", "free prestige %.1f, recovering at %+.2f/turn (about %s turns to zero)" % (fr, rate, p["turns_to_zero"]))
    mans = next((b for b in cur.get("bld") or [] if "mansion" in b[0]), None)
    if mans:
        out["banquet"] = {"recipe": mans[1], "rate": mans[2], "target": mans[3]}
        if fr < FREE_TARGET and num(mans[2]) < 0.5 * max(num(mans[3]), 0.01) and num(cur.get("cash")) > 4000:
            flag("MED", "banquet is at %.2f of target %.2f while free prestige is %.1f: its inputs may be short" % (num(mans[2]), num(mans[3]), fr))

    # cash health
    guard = jload("state/guardian.json", {}) or {}
    floor = num(guard.get("floor"), CASH_FLOOR) or CASH_FLOOR
    if cash[-1] < 2 * floor:
        flag("HIGH", "cash %.0f is under 2x the floor (%.0f)" % (cash[-1], floor))
    if sl is not None and sl < -50:
        flag("HIGH", "cash is falling %.0f/turn over the last 12 turns" % -sl)
    elif sl is not None and sl < 20:
        flag("MED", "cash growth is only %+.0f/turn: flat" % sl)
    fs = jload("state/failsafe.json", {}) or {}
    out["failsafe"] = {"level": fs.get("level"), "name": fs.get("name"), "burn": fs.get("burn"), "paused": sorted((fs.get("paused") or {}).keys())}
    if num(fs.get("level")) >= 2:
        flag("HIGH", "failsafe is at %s: discretionary buys are paused (%s)" % (fs.get("name"), ", ".join(sorted((fs.get("paused") or {}).keys())) or "none"))
    if guard.get("alert"):
        flag("HIGH", "guardian alert: %s" % str(guard.get("alert"))[:160])

    # value trend (cash + stock at market), from the goal planner's own log
    gh = jlines("state/v2/goal_history.jsonl", 80)
    vals = {}
    for x in gh:
        if x.get("turn") is not None and x.get("value_now") is not None:
            vals[x["turn"]] = num(x["value_now"])
    vt = sorted(vals)
    if len(vt) > 6:
        v = [vals[t] for t in vt[-25:]]
        out["value"] = {"now": r(v[-1]), "slope": r(slope(v), 1), "d24": r(v[-1] - v[0]), "turns": len(v)}
        if out["value"]["slope"] is not None and out["value"]["slope"] < 0:
            flag("HIGH", "business value is falling %.0f/turn" % -out["value"]["slope"])

    # profit / sales
    pr = [num(x.get("profit")) for x in seq]
    out["profit"] = {"last": r(pr[-1]), "avg12": r(sum(pr[-12:]) / max(1, len(pr[-12:])))}

    # stock: where is capital sitting, and what is wasted
    items = cur.get("items") or {}
    stock = []
    for k, v in items.items():
        try:
            held, made, used, sold, bought, expired, price = [num(z) for z in v]
        except (TypeError, ValueError):
            continue
        if held > 0 and price > 0:
            stock.append((k, r(held, 1), r(held * price), r(made, 1), r(used, 1), r(sold, 1)))
        if expired > 0 and price > 0 and expired * price > 20:
            flag("LOW", "%s expired %.1f last turn (~%.0f coin wasted)" % (k, expired, expired * price))
    stock.sort(key=lambda t: -t[2])
    out["stock_value"] = r(sum(t[2] for t in stock))
    out["stock_top"] = stock[:8]
    idle = [t for t in stock if t[3] == 0 and t[5] == 0 and t[2] > 150]
    out["dead_stock"] = [(t[0], t[1], t[2]) for t in idle[:6]]

    # alerts the bots raised themselves
    out["bot_alerts"] = cur.get("alerts") or []
    out["ships"] = [(s.get("name"), s.get("state"), s.get("level"), s.get("place")) for s in cur.get("ships") or []]
    out["buildings"] = [(b[0], b[1], b[2], b[3]) for b in cur.get("bld") or [] if b[1]]

    # queue health: refused entries (promotion retries are known noise)
    done = jlines("state/order_queue_done.jsonl", 400)
    cutoff = NOW - datetime.timedelta(hours=24)
    recent = [d for d in done if (parse_t(d.get("ts")) or NOW) > cutoff]
    bad = {}
    for d in recent:
        if d.get("ok") is False and "promote" not in json.dumps(d.get("entry") or {}):
            key = json.dumps({k: v for k, v in (d.get("entry") or {}).items() if k in ("item", "building", "transport", "contract", "money")}, sort_keys=True)
            bad[key] = bad.get(key, 0) + 1
    rep = [(k, n) for k, n in bad.items() if n >= 3]
    for k, n in rep[:4]:
        flag("MED", "the same queue entry failed %d times in 24 h: %s" % (n, k[:100]))
    out["queue_24h"] = {"entries": len(recent), "failed": sum(1 for d in recent if d.get("ok") is False and "promote" not in json.dumps(d.get("entry") or {}))}

    # horizon
    end = parse_t((jload("state/status.json", {}) or {}).get("season_end") or "2026-11-30T11:00:00+00:00")
    if end:
        out["season_turns_left"] = int((end - NOW).total_seconds() / 3600)

    # API-derived flags
    lg = (api_res or {}).get("legacy") or {}
    if lg.get("rank"):
        out["legacy"] = lg
    if (api_res or {}).get("available") and api_res.get("errors"):
        flag("LOW", "API read problems: %s" % "; ".join(api_res["errors"][:3]))
    return out, flags, recent


def changes_md(recent):
    lines = ["# Changes in the last 24 h (applied queue entries, newest first)", ""]
    for d in reversed(recent):
        e = d.get("entry") or {}
        if d.get("ok") is False:
            continue
        what = ", ".join("%s=%s" % (k, json.dumps(v)[:60]) for k, v in e.items() if k not in ("note", "tier"))
        lines.append("- %s [%s] %s%s" % ((d.get("ts") or "")[5:16], d.get("source"), what[:150],
                                          (" | " + str(e.get("note"))[:120]) if e.get("note") else ""))
        if len(lines) > 80:
            lines.append("- ... older entries trimmed")
            break
    return "\n".join(lines) + "\n"


def briefing(out, flags, api_res):
    L = ["# Oversight briefing", "", "Generated %s | turn %s | data %s h old | ~%s turns to season end" % (
        out["generated"][:16], out.get("turn"), out.get("data_age_h"), out.get("season_turns_left"))]
    L += ["", "## Flags"]
    order = {"HIGH": 0, "MED": 1, "LOW": 2}
    for f in sorted(flags, key=lambda f: order[f["sev"]]):
        L.append("- **%s** %s" % (f["sev"], f["text"]))
    if not flags:
        L.append("- none")
    c, p = out.get("cash") or {}, out.get("prestige") or {}
    L += ["", "## Cash", "- now %s | last 6 / 12 / 24 turns: %s / %s / %s | trend %s per turn" % (
        c.get("now"), fmt(c.get("d6"), 0, True), fmt(c.get("d12"), 0, True), fmt(c.get("d24"), 0, True), fmt(c.get("slope12"), 0, True)),
        "- if the 12-turn trend holds: +12 turns %s, +48 turns %s, +120 turns %s" % (c.get("in12"), c.get("in48"), c.get("in120"))]
    v = out.get("value")
    if v:
        L.append("- business value (cash + stock) %s, trend %s per turn over %d turns; stock at market %s" % (
            v["now"], fmt(v["slope"], 0, True), v["turns"], out.get("stock_value")))
    pf = out.get("profit") or {}
    L.append("- profit last turn %s, 12-turn average %s (before taxes)" % (pf.get("last"), pf.get("avg12")))
    L += ["", "## Prestige",
          "- total %s, free %s, rate %s per turn (free trend %s per turn)" % (p.get("total"), p.get("free"), p.get("rate"), p.get("free_slope12")),
          "- turns to free > 0: %s | to the banquet target (%d): %s | to 800 for Tenants L13: %s" % (
              p.get("turns_to_zero"), FREE_TARGET, p.get("turns_to_target"), p.get("turns_to_tenants"))]
    if out.get("banquet"):
        b = out["banquet"]
        L.append("- banquet: %s at %s of %s" % (b["recipe"], b["rate"], b["target"]))
    fs = out.get("failsafe") or {}
    L.append("- failsafe level %s (%s), paused: %s" % (fs.get("level"), fs.get("name"), ", ".join(fs.get("paused") or []) or "none"))
    lg = out.get("legacy")
    if lg:
        L += ["", "## Standing (live scoreboard)",
              "- legacy rank %s of %s (prestige rank %s): legacy %s, prestige %s; median legacy %s" % (
                  lg.get("rank"), lg.get("players"), lg.get("prestige_rank"), lg.get("ours"), lg.get("prestige"), lg.get("median")),
              "- gap to the next rank up: %s" % lg.get("gap_to_next"),
              "- top 5: " + "; ".join("%s (%s) %s" % (n, t, l) for n, t, l, _ in lg.get("top5", []))]
    if api_res and api_res.get("available"):
        t = api_res.get("town") or {}
        L += ["", "## Town and contracts",
              "- Strasclives: %s commoners, growth %s, migration %s, %s households" % (t.get("commoners"), t.get("growth_progress"), t.get("migration"), t.get("households")),
              "- church asks %s | contracts %s" % (api_res.get("church_contracts"), (api_res.get("contracts") or {}).get("by_state")),
              "- we rank in production of: " + (", ".join("%s #%d" % kv for kv in api_res.get("production_ranks") or []) or "nothing in the top lists"),
              "- workers: " + "; ".join("%s %s" % (w["name"], w["top"]) for w in api_res.get("workers") or [])]
    imp = ((api_res or {}).get("prestige") or {}).get("impacts")
    if imp:
        L += ["", "## Prestige sources and drains (per turn, live)", "- " + "; ".join("%s %+.2f" % kv for kv in imp)]
    L += ["", "## Capital and waste"]
    L.append("- biggest stock by value: " + ", ".join("%s %s (%s)" % (t[0], t[1], t[2]) for t in out.get("stock_top", [])[:6]))
    if out.get("dead_stock"):
        L.append("- held with no production or sales (some are deliberate church/household reserves): " + ", ".join("%s %s (%s)" % t for t in out["dead_stock"]))
    L += ["", "## Buildings (rate / target)"]
    L.append("- " + "; ".join("%s %s/%s" % (b[0], b[2], b[3]) for b in out.get("buildings", [])))
    L.append("- ships: " + "; ".join("%s %s crew %s" % (s[0], s[1], s[2]) for s in out.get("ships", [])))
    if out.get("bot_alerts"):
        L += ["", "## Alerts the bots raised", "- " + "\n- ".join(out["bot_alerts"][:10])]
    q = out.get("queue_24h") or {}
    L += ["", "## Queue (24 h)", "- %s entries, %s refused (promotion retries excluded)" % (q.get("entries"), q.get("failed"))]
    return "\n".join(L) + "\n"


def main():
    offline = "--offline" in sys.argv
    api = Api(offline=offline)
    api_res = api_section(api)
    res = analyse(api_res)
    out, flags = res[0], res[1]
    recent = res[2] if len(res) > 2 else []
    out["flags"] = flags
    out["api"] = api_res
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "latest.json"), "w") as f:
        json.dump(out, f, indent=1, default=str)
    with open(os.path.join(OUT, "latest.md"), "w") as f:
        f.write(briefing(out, flags, api_res))
    with open(os.path.join(OUT, "changes.md"), "w") as f:
        f.write(changes_md(recent))
    # the game log: one compact line per run
    lg = out.get("legacy") or {}
    line = {"t": out["generated"], "turn": out.get("turn"), "cash": (out.get("cash") or {}).get("now"),
            "slope12": (out.get("cash") or {}).get("slope12"), "free": (out.get("prestige") or {}).get("free"),
            "rate": (out.get("prestige") or {}).get("rate"), "value": (out.get("value") or {}).get("now"),
            "legacy": lg.get("ours"), "rank": lg.get("rank"), "high": sum(1 for x in flags if x["sev"] == "HIGH"),
            "med": sum(1 for x in flags if x["sev"] == "MED")}
    path = os.path.join(OUT, "log.jsonl")
    lines = []
    try:
        with open(path) as f:
            lines = f.read().splitlines()
    except OSError:
        pass
    lines.append(json.dumps(line))
    with open(path, "w") as f:
        f.write("\n".join(lines[-600:]) + "\n")
    print("oversight: %d flags (%d high), api %s" % (len(flags), line["high"], "on" if api.ok else "off"))


if __name__ == "__main__":
    main()
