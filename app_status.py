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
        "alerts": last.get("alerts") or [],
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
        done.append({"ts": d.get("ts"), "source": d.get("source"), "what": label, "note": what,
                     "ok": d.get("ok"), "error": (d.get("error") or "")[:120] if not d.get("ok") else None})
    s["recent"] = list(reversed(done))
    pend = _json("state/order_queue.json", []) or []
    s["queue_pending"] = len(pend) if isinstance(pend, list) else 0
    s["contracts"] = [{k: c.get(k) for k in ("id", "item", "volume", "kind", "bonus", "price", "held", "verdict", "why", "fill")}
                      for c in (_json("state/contracts_scored.json", []) or [])]

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
