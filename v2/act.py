#!/usr/bin/env python3
"""Bot v2 actor: sends v2's planned store orders for the items v2 owns, and nothing else.

    python v2/act.py             # dry run: state/v2/act.json lists what v2 would send for EVERY planned item
    python v2/act.py --live      # sends only for owned items (v2/config.json "live" -> "items"), verifies each

Runs right after v2/shadow.py in the v2-shadow workflow (:25, mid-turn, clear of the tick), on the
snapshot and plan that run just wrote. v1's writers skip owned items (v2_owned.py), so nobody fights.

How a write is built (merge, never a blind replace):
  - the item's live order tiers are re-read just before the write;
  - buy side: the first buy tier gets v2's volume / price / stop-at; any other buy tiers lose their buy fields;
  - sell side: the first sell tier gets v2's volume / price; min_holding (stock kept back) is never touched;
  - nothing else in the tiers changes; tiers left empty are dropped.

Guards (any one refuses the item this run and says why):
  - failsafe at BRAKE or STOP: v2 stands down entirely (the failsafe owns the brakes)
  - snapshot or plan unusable, or the planner skipped a module this run
  - buy price above the config ceiling (an owned buy item needs a ceiling), sell price below the floor
  - price move over 50% or volume move over 2x+10 against the live order in one run
  - dropping a buy on a never_drop item; raising a buy while cash is under the reserve
  - the item was changed by hand through the order queue in the last 2 hours
  - more than MAX_WRITES writes in one run
Self-suspension: an owned item with a risk flag on 2 runs in a row, or 2 failed writes in a row, is written to
state/v2/suspended.json and goes straight back to v1. Delete its entry to hand it back.
"""
import datetime
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, ROOT)
import api          # noqa: E402

OUT = os.path.join(ROOT, "state", "v2")
QUEUE_DONE = os.path.join(ROOT, "state", "order_queue_done.jsonl")
FAILSAFE = os.path.join(ROOT, "state", "failsafe.json")

MAX_WRITES = 8
MAX_PRICE_MOVE = 0.5
SUSPEND_AFTER = 2
BUY_KEYS = ("buy_volume", "buy_price", "max_holding")
SELL_KEYS = ("sell_volume", "sell_price")


def _load(path, default):
    try:
        with open(path) as f:
            return json.load(f)
    except (OSError, ValueError):
        return default


def _save(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=1, default=str)
        f.write("\n")


def _n(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return 0.0


def now():
    return datetime.datetime.now(datetime.timezone.utc)


# ---------------------------------------------------------------- what v2 wants for one item
def desired(item, o):
    """v2's wanted buy and sell for one item from the plan. buy/sell: dict, or "off", or None (not v2's call)."""
    buy = o.get("effective_buy") or o.get("buy")
    bb = o.get("build_buy")
    if bb:
        if buy:
            buy = {"buy_volume": int(buy.get("buy_volume", 0)) + int(bb.get("buy_volume", 0)),
                   "buy_price": str(max(_n(buy.get("buy_price")), _n(bb.get("buy_price")))),
                   "max_holding": max(int(buy.get("max_holding") or 0), int(bb.get("max_holding") or 0)) or None}
            if buy["max_holding"] is None:
                buy.pop("max_holding")
        else:
            buy = dict(bb)
    if buy is None and o.get("buy_off"):
        buy = "off"             # the planner says nothing needs this buy (an owned item only: decide() checks)
    sell = o.get("sell")
    return buy, sell


# ---------------------------------------------------------------- merge into the live tiers
def _has_buy(t):
    return _n(t.get("buy_volume")) > 0 or t.get("buy_price") not in (None, "", "0")


def _has_sell(t):
    return _n(t.get("sell_volume")) > 0


def _empty(t):
    return not (_has_buy(t) or _has_sell(t))


def merge(live, buy, sell):
    """New tier list: v2's buy/sell folded into the live tiers (see the module docstring)."""
    ms = [dict(t) for t in live]
    if buy is not None:
        idx = [i for i, t in enumerate(ms) if _has_buy(t)]
        if buy == "off":
            for i in idx:
                for k in BUY_KEYS:
                    ms[i].pop(k, None)
        else:
            if idx:
                first, others = idx[0], idx[1:]
            else:
                ms.append({})
                first, others = len(ms) - 1, []
            ms[first]["buy_volume"] = int(buy["buy_volume"])
            if buy.get("buy_price"):
                ms[first]["buy_price"] = str(buy["buy_price"])
            if buy.get("max_holding"):
                ms[first]["max_holding"] = int(buy["max_holding"])
            for i in others:
                for k in BUY_KEYS:
                    ms[i].pop(k, None)
    if sell is not None:
        idx = [i for i, t in enumerate(ms) if _has_sell(t)]
        if sell == "off":
            for i in idx:
                for k in SELL_KEYS:
                    ms[i].pop(k, None)
        else:
            if idx:
                first, others = idx[0], idx[1:]
            else:
                ms.append({})
                first, others = len(ms) - 1, []
            ms[first]["sell_volume"] = int(sell["sell_volume"])
            if sell.get("sell_price"):
                ms[first]["sell_price"] = str(sell["sell_price"])
            for i in others:
                for k in SELL_KEYS:
                    ms[i].pop(k, None)
    return [t for t in ms if not _empty(t)]


def _side(tiers, has, keys):
    t = next((t for t in tiers if has(t)), None)
    return {k: t.get(k) for k in keys if t.get(k) is not None} if t else None


def _canon(tiers):
    """Order tiers in a form that compares equal however the game formats the numbers ("22" == 22.0)."""
    def v(x):
        try:
            return round(float(x), 4)
        except (TypeError, ValueError):
            return str(x)
    return json.dumps([{k: v(x) for k, x in sorted(t.items())} for t in tiers], sort_keys=True)


# ---------------------------------------------------------------- guards
def recent_manual(item, hours=2, path=QUEUE_DONE):
    try:
        lines = open(path).read().splitlines()[-200:]
    except OSError:
        return False
    cutoff = now() - datetime.timedelta(hours=hours)
    for ln in lines:
        try:
            r = json.loads(ln)
            if r.get("ok") and r.get("source", "queue") == "queue" and (r.get("entry") or {}).get("item") == item \
                    and datetime.datetime.fromisoformat(r["ts"]) >= cutoff:
                return True
        except (ValueError, KeyError, TypeError):
            continue
    return False


def check(item, live, new, cfg, cash):
    """Reasons to refuse this write (empty list = fine)."""
    why = []
    lb, nb = _side(live, _has_buy, BUY_KEYS), _side(new, _has_buy, BUY_KEYS)
    ls, ns = _side(live, _has_sell, SELL_KEYS), _side(new, _has_sell, SELL_KEYS)
    ceil_ = (cfg.get("buy_ceiling") or {}).get(item)
    floor_ = (cfg.get("sell_floor") or {}).get(item)
    if nb:
        p = _n(nb.get("buy_price"))
        if ceil_ is None and p:
            why.append("no buy ceiling in config for %s" % item)
        elif p and p > ceil_ + 1e-9:
            why.append("buy price %.2f above ceiling %.2f" % (p, ceil_))
        if lb and _n(lb.get("buy_price")) and p and abs(p - _n(lb["buy_price"])) / _n(lb["buy_price"]) > MAX_PRICE_MOVE:
            why.append("buy price %.2f -> %.2f is over a %d%% move" % (_n(lb["buy_price"]), p, MAX_PRICE_MOVE * 100))
        lv, nv = _n((lb or {}).get("buy_volume")), _n(nb.get("buy_volume"))
        if nv > 2 * lv + 10:
            why.append("buy volume %d -> %d is over 2x+10 in one run" % (lv, nv))
        if nv > lv and cash is not None and cash < (cfg.get("cash") or {}).get("reserve", 0):
            why.append("cash %.0f under the reserve: no buy raises" % cash)
    elif lb and item in set(cfg.get("never_drop") or []):
        why.append("%s is never_drop: v2 will not take its buy off" % item)
    if ns:
        p = _n(ns.get("sell_price"))
        if floor_ is not None and p and p < floor_ - 1e-9:
            why.append("sell price %.2f below floor %.2f" % (p, floor_))
        if ls and _n(ls.get("sell_price")) and p and abs(p - _n(ls["sell_price"])) / _n(ls["sell_price"]) > MAX_PRICE_MOVE:
            why.append("sell price %.2f -> %.2f is over a %d%% move" % (_n(ls["sell_price"]), p, MAX_PRICE_MOVE * 100))
        lv, nv = _n((ls or {}).get("sell_volume")), _n(ns.get("sell_volume"))
        if nv > 2 * lv + 10:
            why.append("sell volume %d -> %d is over 2x+10 in one run" % (lv, nv))
    return why


# ---------------------------------------------------------------- one run
def decide(snap, plan, cfg, owned, live_tiers, failsafe_level=0, manual=recent_manual):
    """Pure: what to send. live_tiers: {item: [tier, ...]} read just now. Returns (rows, standdown_reason)."""
    if failsafe_level >= 2:
        return [], "failsafe at level %d: v2 stands down" % failsafe_level
    if not snap or not plan or snap.get("errors"):
        return [], "snapshot unusable: %s" % ((snap or {}).get("errors") or "missing")
    skipped = [n for n in plan.get("notes") or [] if "skipped" in n]
    if skipped:
        return [], "planner skipped a module this run: %s" % "; ".join(skipped)
    rows = []
    for item, o in sorted((plan.get("orders") or {}).items()):
        buy, sell = desired(item, o)
        is_owned = item in owned
        if buy == "off" and not is_owned:
            buy = None          # v2 takes a buy off only for items it owns; a side it plans nothing for is left as it is
        if buy is None and sell is None:
            continue
        live = live_tiers.get(item, [])
        new = merge(live, buy, sell)
        row = {"item": item, "owned": is_owned, "live": live, "new": new, "same": _canon(new) == _canon(live)}
        if not row["same"]:
            row["refused"] = check(item, live, new, cfg, snap.get("cash"))
            if is_owned and manual(item):
                row["refused"].append("changed by hand through the order queue in the last 2 hours")
        rows.append(row)
    return rows, None


def suspend_check(plan, owned, st, results):
    """Count consecutive risk runs / failed writes per owned item; returns {item: reason} to suspend."""
    risky = {f["item"] for f in plan.get("flags") or [] if f["severity"] == "risk"}
    out = {}
    for item in owned:
        c = st.setdefault(item, {"risk": 0, "fail": 0})
        c["risk"] = c["risk"] + 1 if item in risky else 0
        r = results.get(item)
        if r is not None:
            c["fail"] = 0 if r else c["fail"] + 1
        if c["risk"] >= SUSPEND_AFTER:
            out[item] = "risk flag %d runs in a row" % c["risk"]
        elif c["fail"] >= SUSPEND_AFTER:
            out[item] = "write failed %d runs in a row" % c["fail"]
    return out


def main(argv=None, out=OUT, cfg=None, failsafe=FAILSAFE):
    argv = sys.argv if argv is None else argv
    live_mode = "--live" in argv
    STATE, SUSPENDED, LOG = (os.path.join(out, n) for n in ("act_state.json", "suspended.json", "act.jsonl"))
    cfg = cfg if cfg is not None else _load(os.path.join(HERE, "config.json"), {})
    snap = _load(os.path.join(out, "snapshot.json"), None)
    plan = _load(os.path.join(out, "plan.json"), None)
    sus = _load(SUSPENDED, {})
    owned = set(((cfg.get("live") or {}).get("items")) or []) - set(sus)
    fs_level = int(_n(_load(failsafe, {}).get("level")))
    store = ((snap or {}).get("store") or {}).get("id")

    live_tiers = {}
    if live_mode and owned and store:
        b = api.get("/buildings/%s" % store) or {}     # re-read just before writing: the snapshot is minutes old
        holds = (((b.get("storage") or {}).get("inventory") or {}).get("holdings")) or {}
        for k, h in holds.items():
            live_tiers[k] = [{kk: vv for kk, vv in t.items() if kk != "result"} for t in (h or {}).get("managers") or [] if t]
        if not holds:
            print("v2 act: could not re-read the store; nothing sent")
            owned = set()
    if not live_tiers:
        live_tiers = {k: v.get("orders") or [] for k, v in (((snap or {}).get("store") or {}).get("items") or {}).items()}

    rows, stand = decide(snap, plan, cfg, owned, live_tiers, fs_level)
    results, sent = {}, 0
    if live_mode and owned and not stand:
        api.allow_writes()
        for r in rows:
            if not r["owned"] or r["same"] or r.get("refused"):
                continue
            if sent >= MAX_WRITES:
                r["refused"] = ["write cap %d reached this run" % MAX_WRITES]
                continue
            ok, status, body = api.write("PATCH", "/buildings/%s/storage/inventory/%s" % (store, api.q(r["item"])),
                                         {"managers": r["new"]})
            sent += 1
            check_ = api.get("/buildings/%s" % store) or {}
            got = (((((check_.get("storage") or {}).get("inventory") or {}).get("holdings")) or {}).get(r["item"]) or {}).get("managers") or []
            got = [{k: v for k, v in t.items() if k != "result"} for t in got if t]
            verified = bool(ok) and _canon(got) == _canon(r["new"])
            r.update(sent=True, ok=bool(ok), status=status, verified=verified, reply=str(body)[:200] if not ok else None)
            results[r["item"]] = verified
            with open(LOG, "a") as f:
                f.write(json.dumps({"ts": now().isoformat(timespec="seconds"), "turn": (snap or {}).get("turn"),
                                    "item": r["item"], "from": r["live"], "to": r["new"], "ok": bool(ok),
                                    "verified": verified, "status": status}, default=str) + "\n")

    st = _load(STATE, {})
    newly = suspend_check(plan or {}, owned, st.setdefault("counters", {}), results) if live_mode else {}
    if newly:
        for item, why in newly.items():
            sus[item] = {"since": now().isoformat(timespec="seconds"), "why": why}
        _save(SUSPENDED, sus)
    if live_mode:
        st["last"] = now().isoformat(timespec="seconds")
        _save(STATE, st)

    res = {"t": now().isoformat(timespec="seconds"), "turn": (snap or {}).get("turn"), "mode": "live" if live_mode else "dry",
           "owned": sorted(owned), "suspended": sus, "stand_down": stand, "failsafe_level": fs_level,
           "would_change": sum(1 for r in rows if not r["same"]),
           "rows": rows}
    _save(os.path.join(out, "act.json"), res)
    print("v2 act (%s): owned %s; %d items differ from live; %d sent%s%s" % (
        res["mode"], ", ".join(sorted(owned)) or "none", res["would_change"], sent,
        ("; STAND DOWN: " + stand) if stand else "", ("; suspended " + ", ".join(newly)) if newly else ""))
    for r in rows:
        if r["owned"] and not r["same"]:
            print("  %s: %s%s" % (r["item"], "refused: " + "; ".join(r["refused"]) if r.get("refused") else
                                  ("sent, verified" if r.get("verified") else "sent, NOT verified" if r.get("sent") else "would send"),
                                  ""))
    return res


if __name__ == "__main__":
    main()
