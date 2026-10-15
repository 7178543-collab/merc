#!/usr/bin/env python3
"""Writes state/status.json for the phone app (docs/index.html). Called at the end of the bot's
runs (alerts.py after the history line, contracts.py after the queue/rules/contracts run).
Read-only: one GET of the storehouse (orders + last turn's flows/P&L) and one of the business
(ship ids). Never raises: a failure just leaves the previous status.json in place.
"""
import datetime
import glob
import json
import os
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "state", "status.json")
STORE = "152202386005001"
BUSINESS = "39992"
SEASON_END = "2026-11-30T11:00:00+00:00"      # 12:00 CET, Season 8
KEY_ITEMS = ["garments", "cloth", "thread", "flax fibres", "flax plants", "beer", "nets", "timber", "tools",
             "limestone", "wheels", "furniture", "candles", "jewellery", "light armour", "cured fish", "grain",
             "labour", "tar", "rope", "tiles", "nails"]


def _read(path, default=None):
    try:
        with open(os.path.join(HERE, path)) as f:
            return f.read()
    except Exception:
        return default


def _json(path, default=None):
    try:
        return json.loads(_read(path) or "")
    except Exception:
        return default


def _get(path):
    try:
        import merc_status4 as m
        if not (m.USER and m.TOKEN):
            return None
        req = urllib.request.Request("https://play.mercatorio.io/api" + path, method="GET",
                                     headers={"X-Merc-User": m.USER, "Authorization": "Bearer " + m.TOKEN,
                                              "Accept": "application/json"})
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read().decode())
    except Exception:
        return None


def _history():
    rows = []
    for path in sorted(glob.glob(os.path.join(HERE, "history", "merc-*.jsonl")))[-2:]:
        try:
            with open(path) as f:
                for line in f:
                    try:
                        rows.append(json.loads(line))
                    except ValueError:
                        pass
        except Exception:
            pass
    return rows


def _n(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return 0.0


def _diagnose_alerts(max_age_h=3):
    """bot v2's self-diagnosis findings (v2/diagnose.py, written each :25 run), first in the app's alert list."""
    d = _json("state/v2/diagnose.json") or {}
    try:
        age = datetime.datetime.now(datetime.timezone.utc) - datetime.datetime.fromisoformat(d["t"])
        if age > datetime.timedelta(hours=max_age_h):
            return []
    except (KeyError, ValueError, TypeError):
        return []
    return ["DIAGNOSE " + a for a in (d.get("alerts") or [])][:6]


CHAIN_GOODS = ("flax plants", "flax fibres", "thread", "cloth")


def _triage(alerts, rows, plan, snap):
    """Split alerts into (attention, expected). Attention = needs a decision; expected = a known state the bots are
    already handling (Oct 14, Taylor: the list showed six alerts and none needed him)."""
    chain = (plan or {}).get("chain") or {}
    bufs = chain.get("buffers") or {}
    mansion = next((b for b in (snap or {}).get("buildings") or [] if b.get("type") == "mansion"), {}) or {}
    recipe = str(mansion.get("recipe") or "")
    sold = {}
    for r in rows[-6:]:
        for k, v in (r.get("items") or {}).items():
            sold.setdefault(k, {})[r.get("turn")] = _n((v + [0] * 4)[3])
    att, exp = [], []
    for a in alerts:
        low = a.lower()
        why = None
        if a.startswith("DIAGNOSE") or "stop" in low and "failsafe" in low or "brake" in low:
            why = None
        elif low.startswith("failsafe watch"):
            why = "cash under 15k: the failsafe is watching, nothing paused"
        elif "running out" in low and ("cured fish" in low and "(meat)" in recipe or "cured meat" in low and "(fish)" in recipe):
            why = "the banquet runs on the other recipe"
        elif low.endswith(": no_order"):
            item = a.split(":")[0].strip()
            b = bufs.get(item)
            if item in CHAIN_GOODS and (b is None or _n(b.get("held")) >= _n(b.get("target"))):
                why = "chain pile above target: v2 makes less until it drains"
        elif low.endswith(": not selling"):
            item = a.split(":")[0].strip()
            last3 = [v for t, v in sorted((sold.get(item) or {}).items())][-3:]
            if any(x > 0 for x in last3):
                why = "sold in the last 3 turns: a one-turn gap"
        elif low.endswith(": expiring"):
            why = "shown in Wasted last turn"
        if why:
            exp.append({"text": a, "why": why})
        else:
            att.append(a)
    return att, exp


def _waste(snap):
    """What expired last turn and what it cost (expired x what we paid a unit), biggest first."""
    out = []
    for k, it in (((snap or {}).get("store") or {}).get("items") or {}).items():
        fl = it.get("flow") or {}
        e = _n(fl.get("expiration"))
        if e <= 0.05:
            continue
        unit = (_n(fl.get("purchase_cost")) / _n(fl.get("purchase"))) if _n(fl.get("purchase")) else _n(it.get("unit_cost"))
        out.append({"item": k, "expired": round(e, 1), "coin": round(e * unit, 1)})
    return sorted(out, key=lambda r: -r["coin"])


def _chain(plan, cfg):
    c = (plan or {}).get("chain") or {}
    if not c.get("ok"):
        return None
    return {"live": bool(((cfg or {}).get("live") or {}).get("chain")), "mode": c.get("mode"),
            "targets": c.get("targets"), "current": c.get("current"), "garments": c.get("garments_per_turn"),
            "sales": c.get("sales"), "labour": c.get("labour"), "buffers": c.get("buffers"), "notes": c.get("notes")}


# Prestige tracks for the app's one-tap options. Known costs (game tables in prestige_rules.py); the rest show a "Check
# price" button that sends a 1-prestige offer with max_cost 1: the game refuses it and names the real price, which the
# next status picks up from the queue log. Nothing is ever spent by a price check.
TRACKS = [
    ("prestige_management", "Prestige management", "+1 prestige pool: room for ~10 more park plots"),
    ("apprentices", "Apprentice slot", "+1 household worker"),
    ("management", "Regular management", "+1 management: room for more buildings"),
    ("tenants", "Tenants", "+5 tenants: farmstead plots, 10 free labour each"),
    ("luxuries", "Luxury slot", "+1 luxury slot (needs a luxury good with 2x supply at home)"),
    ("scale_luxuries", "Luxury boost", "+100% luxury use and its prestige"),
    ("transports", "Transport slot", "+1 ship"),
    ("cargo_slots", "Cargo slot", "+1 cargo slot"),
    ("contracts", "Contract slots", "more contracts at once"),
]
PM_COSTS = [0, 100, 250, 500, 1000, 2000, 3000, 5000, 10000]
APPRENTICE_COSTS = [50, 250, 1000, 2500, 5000, 7500, 10000]


def _prestige_options(snap, free):
    import re
    levels = ((snap or {}).get("household") or {}).get("levels") or {}
    learned = {}
    for line in (_read("state/order_queue_done.jsonl", "") or "").splitlines()[-400:]:
        try:
            d = json.loads(line)
        except ValueError:
            continue
        e = d.get("entry") or {}
        if e.get("prestige"):
            mm = re.search(r"expected (\d+)", str(d.get("body") or d.get("error") or ""))
            if mm:
                learned[e["prestige"]] = (int(mm.group(1)), d.get("before"))
            elif d.get("ok"):
                learned.pop(e["prestige"], None)
    out = []
    for track, label, gives in TRACKS:
        lv = int(_n(levels.get(track)))
        cost = None
        if track == "prestige_management" and lv + 1 < len(PM_COSTS):
            cost = PM_COSTS[lv + 1]
        elif track == "apprentices" and lv < len(APPRENTICE_COSTS):
            cost = APPRENTICE_COSTS[lv]
        lc = learned.get(track)
        if lc and (lc[1] is None or int(_n(lc[1])) == lv):
            cost = lc[0]             # the game's own answer beats the table
        out.append({"track": track, "label": label, "gives": gives, "level": lv, "cost": cost,
                    "affordable": cost is not None and cost <= free})
    return out


def _switches(ov, cfg):
    live = (cfg or {}).get("live") or {}
    return {
        "banquet": ov.get("banquet", "auto"),
        "chain": ov.get("chain") or ("v2" if live.get("chain") else "v1"),
        "ship_trade": ov.get("ship_trade") or ("on" if ((cfg or {}).get("ship_trade") or {}).get("on") else "off"),
        "church_imports": ov.get("church_imports") or ("on" if ((cfg or {}).get("ship_church") or {}).get("on") else "off"),
        "quarry": ov.get("quarry", "auto"),
    }


def build():
    rows = _history()
    last = rows[-1] if rows else {}
    by_turn = {}
    for r in rows:
        if r.get("turn") is not None and r.get("profit") is not None:
            by_turn[r["turn"]] = r["profit"]
    turns = sorted(by_turn)
    profit24 = sum(by_turn[t] for t in turns[-24:]) if turns else None

    s = {
        "t": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        "data_t": last.get("t"), "turn": last.get("turn"),
        "cash": last.get("cash"), "profit_last": last.get("profit"), "profit_24": profit24,
        "sales": last.get("sales"), "buys": last.get("buys"),
        "prestige": last.get("prestige"), "prestige_free": last.get("prestige_free"),
        "prestige_rate": last.get("prestige_rate"),
        "season_end": SEASON_END,
        "alerts": _diagnose_alerts() + (last.get("alerts") or []),
        "needs_you": (_json("state/needs_you.json") or {}).get("what"),
        "buildings": last.get("bld") or [],
        "ships": last.get("ships") or [],
        "stock": {k: (last.get("items") or {}).get(k) for k in KEY_ITEMS if (last.get("items") or {}).get(k)},
        "stock_cols": ["held", "made", "used", "sold", "bought", "expired", "price"],
        "rules": [l for l in (_read("state/prestige_rules_last.txt", "") or "").splitlines()[1:] if l.strip()],
        "overrides": _json("state/overrides.json", {}) or {},
    }
    # last 12 queue results, newest first, trimmed for the phone
    done = []
    for line in (_read("state/order_queue_done.jsonl", "") or "").splitlines()[-12:]:
        try:
            d = json.loads(line)
        except ValueError:
            continue
        e = d.get("entry") or {}
        what = (e.get("note") or "")[:90]
        label = e.get("item") or e.get("prestige") or e.get("donate") or e.get("dump") or e.get("contract") \
            or (("ship " + str(e.get("transport"))) if e.get("transport") else None) \
            or (("building " + str(e.get("building"))) if e.get("building") else None) \
            or ("override" if e.get("override") else None) or ("note for Claude" if e.get("message") else None) or "?"
        if "price check" in (e.get("note") or ""):      # a refused 1-prestige offer is the expected answer, not a failure
            import re
            mm = re.search(r"expected (\d+)", str(d.get("body") or ""))
            done.append({"ts": d.get("ts"), "source": d.get("source"), "what": label,
                         "note": ("price: %s prestige (nothing spent)" % mm.group(1)) if mm else "price check: no price given",
                         "ok": bool(mm), "error": None if mm else (str(d.get("body") or d.get("error") or ""))[:120]})
            continue
        done.append({"ts": d.get("ts"), "source": d.get("source"), "what": label, "note": what,
                     "ok": d.get("ok"), "error": (d.get("error") or "")[:120] if not d.get("ok") else None})
    s["recent"] = list(reversed(done))
    pend = _json("state/order_queue.json", []) or []
    s["queue_pending"] = len(pend) if isinstance(pend, list) else 0
    s["contracts"] = [{k: c.get(k) for k in ("id", "item", "volume", "kind", "bonus", "price", "held", "verdict", "why", "fill")}
                      for c in (_json("state/contracts_scored.json", []) or [])]
    v2 = _json("state/v2/plan.json") or {}
    snap = _json("state/v2/snapshot.json") or {}
    s["attention"], s["expected"] = _triage(s["alerts"], rows, v2, snap)
    s["waste"] = _waste(snap)
    s["waste_coin"] = round(sum(r["coin"] for r in s["waste"]), 1)
    s["waste_turn"] = snap.get("turn")
    s["chain"] = _chain(v2, _json("v2/config.json") or {})
    s["switches"] = _switches(s["overrides"], _json("v2/config.json") or {})
    s["prestige_options"] = _prestige_options(snap, _n(s.get("prestige_free")))
    if v2:
        s["v2"] = {"t": v2.get("t"), "turn": v2.get("turn"), "counts": v2.get("counts"),
                   "flags": [{k: f.get(k) for k in ("severity", "item", "text", "fix")} for f in (v2.get("flags") or [])[:12]],
                   "sinks": (v2.get("sinks") or [])[:5],
                   "live_items": v2.get("live_items") or [],
                   "suspended": sorted((_json("state/v2/suspended.json", {}) or {}).keys())}

    # live: every order tier + last turn's P&L from the storehouse flows
    w = _get("/buildings/%s" % STORE)
    if w:
        inv = ((w.get("storage") or {}).get("inventory") or {})
        holds = inv.get("holdings") or {}
        s["orders"] = {k: [{kk: vv for kk, vv in mg.items() if kk != "result"} for mg in (h.get("managers") or []) if mg]
                       for k, h in holds.items() if (h.get("managers") or [])}
        pf = inv.get("previous_flows") or {}
        pnl, buys = [], []
        for k, f in pf.items():
            sv, sc, pc, pq = _n(f.get("sale_value")), _n(f.get("sale_cost")), _n(f.get("purchase_cost")), _n(f.get("purchase"))
            if _n(f.get("sale")) > 0:
                pnl.append({"item": k, "sold": round(_n(f.get("sale")), 1), "value": round(sv), "margin": round(sv - sc)})
            if pq > 0:
                buys.append({"item": k, "qty": round(pq, 1), "cost": round(pc)})
        s["pnl"] = sorted(pnl, key=lambda r: -r["value"])
        s["purchases"] = sorted(buys, key=lambda r: -r["cost"])
    b = _get("/businesses/%s" % BUSINESS)
    if b:
        ships = []
        for tid in b.get("transport_ids") or []:
            t = _get("/transports/%s" % tid) or {}
            po = t.get("previous_operation") or {}
            ships.append({"id": str(tid), "name": t.get("name"), "target": po.get("target"),
                          "remote": ((t.get("route") or {}).get("remote_town"))})
        s["ship_ids"] = ships
    return s


def write():
    try:
        s = build()
        os.makedirs(os.path.dirname(OUT), exist_ok=True)
        tmp = OUT + ".tmp"
        with open(tmp, "w") as f:
            json.dump(s, f, separators=(",", ":"), default=str)
        os.replace(tmp, OUT)
        print("app status written (%d bytes)" % os.path.getsize(OUT))
    except Exception as e:
        print("app status skipped: %s: %s" % (type(e).__name__, e))


if __name__ == "__main__":
    write()
