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
  - failsafe at BRAKE or STOP: v2 stands down entirely (the failsafe owns the brakes); a buy the brake paused
    (state/failsafe.json "paused") is never raised again by v2 -- Taylor restores those by hand
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


def step_volumes(live, new):
    """Cap each side's volume at 2x+10 of the live one, so a big change walks there over a few runs instead of being
    refused forever (Oct 13: garments 10 -> 55 and beer 10 -> 56 were refused every run and sat at 10).
    Returns (new tiers, notes)."""
    out, notes = [dict(t) for t in new], []
    for has, key in ((_has_buy, "buy_volume"), (_has_sell, "sell_volume")):
        lt = next((t for t in live if has(t)), None)
        nt = next((t for t in out if has(t)), None)
        if lt is None or nt is None:
            continue
        lv, nv = _n(lt.get(key)), _n(nt.get(key))
        cap = int(2 * lv + 10)
        if nv > cap:
            nt[key] = cap
            notes.append("%s %d -> %d stepped to %d (2x+10 a run)" % (key.split("_")[0], lv, nv, cap))
    return out, notes


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
            e = r.get("entry") or {}
            if e.get("transport") or e.get("household"):
                continue                    # a ship route's or the household's order for the item, not the storehouse's
            if r.get("ok") and r.get("source", "queue") == "queue" and e.get("item") == item \
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
def decide(snap, plan, cfg, owned, live_tiers, failsafe_level=0, manual=recent_manual, paused=()):
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
        new, stepped = step_volumes(live, merge(live, buy, sell))
        row = {"item": item, "owned": is_owned, "live": live, "new": new, "same": _canon(new) == _canon(live)}
        if stepped:
            row["stepped"] = stepped
        if not row["same"]:
            row["refused"] = check(item, live, new, cfg, snap.get("cash"))
            if is_owned and manual(item):
                row["refused"].append("changed by hand through the order queue in the last 2 hours")
            if item in paused and _n((_side(new, _has_buy, BUY_KEYS) or {}).get("buy_volume")) > \
                    _n((_side(live, _has_buy, BUY_KEYS) or {}).get("buy_volume")):
                # Taylor's failsafe rule: a buy the brake paused is never restored automatically, only by hand
                row["refused"].append("paused by the failsafe brake (state/failsafe.json): restore it by hand")
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


SHIP_IDLE_TURNS = 3
MAX_ROUTE_WRITES = 6


def ship_auto(plan, cfg, snap, log_path, sst=None):
    """Ships in config live.ship_modes with "auto": set their route orders and crew to v2's ship plan (v2/ships.py),
    from this run's world prices. Returns a list of what was done."""
    modes = (cfg.get("live") or {}).get("ship_modes") or {}
    sp = (plan or {}).get("ship_plans") or {}
    if not sp.get("plans"):
        return []
    try:
        age = now() - datetime.datetime.fromisoformat(sp["t"])
        if age > datetime.timedelta(hours=2):
            return ["ship plans are %s old: no ship writes" % age]
    except (KeyError, ValueError, TypeError):
        return ["ship plans have no time: no ship writes"]
    live = {str(s.get("id")): s for s in (snap or {}).get("ships") or []}
    done = []
    for pl in sp["plans"]:
        sid = str(pl.get("id"))
        if modes.get(sid) != "auto" or sid not in live:
            continue
        gp = ((sst or {}).get(sid) or {}).get("guard_paused_turn")
        if gp is not None and (snap or {}).get("turn") is not None and (snap or {})["turn"] - gp < 6:
            done.append("%s held at crew 0 by the ship guard since turn %s" % (pl.get("ship"), gp))
            continue
        writes = 0
        # clears first: a route's orders reserve cargo room, so raising one before another is cleared can be refused
        # (Oct 13: beer 4 -> 65 got 409 "no capacity" while the old timber order still held 270 units)
        for item, managers in sorted((pl.get("diff") or {}).items(), key=lambda kv: bool(kv[1])):
            if writes >= MAX_ROUTE_WRITES:
                break
            ok, status, body = api.write("PATCH", "/transports/%s/route/inventory/%s" % (sid, api.q(item)), {"managers": managers})
            writes += 1
            rec = {"ts": now().isoformat(timespec="seconds"), "turn": (snap or {}).get("turn"), "ship": pl.get("ship"),
                   "route_item": item, "to": managers, "ok": bool(ok), "status": status,
                   "reply": None if ok else str(body)[:200]}
            with open(log_path, "a") as f:
                f.write(json.dumps(rec, default=str) + "\n")
            done.append("%s %s -> %s" % (pl.get("ship"), item, "ok" if ok else "FAILED %s" % status))
        cur = _n(live[sid].get("set_target"))
        want = min(1.0, max(0.0, _n(pl.get("crew"))))
        if abs(cur - want) >= 0.05:
            ok, status, body = api.write("PUT", "/transports/%s/operation" % sid, {"operation_target": "%.3f" % want})
            with open(log_path, "a") as f:
                f.write(json.dumps({"ts": now().isoformat(timespec="seconds"), "turn": (snap or {}).get("turn"),
                                    "ship": pl.get("ship"), "crew": [cur, want], "est_net": pl.get("est_net"),
                                    "ok": bool(ok), "status": status}, default=str) + "\n")
            done.append("%s crew %.2f -> %.2f %s" % (pl.get("ship"), cur, want, "ok" if ok else "FAILED"))
    return done


MAX_TRADE_WRITES = 6


def trade_home(plan, cfg, snap, st, store, live_tiers, log_path, write=None):
    """Home-side orders for ship trade goods (v2/ships.py trade mode): the buy that stocks an export, or the sell that
    clears an import. v2 owns these goods (act_state trade_items; v1 skips them via v2_owned). A good that drops off
    every route: its buy stops at once, stock left over is offered at home just under the bid, and once none is held
    the orders are cleared and the good is handed back. Never touches a good someone else has orders on."""
    write = write or (lambda path, body: api.write("PATCH", path, body))
    modes = (cfg.get("live") or {}).get("ship_modes") or {}
    turn = (snap or {}).get("turn")
    want = {}
    for pl in ((plan or {}).get("ship_plans") or {}).get("plans") or []:
        if modes.get(str(pl.get("id"))) != "auto":
            continue
        for item, t in (pl.get("home_orders") or {}).items():
            if item in want:            # two ships on one good: add the volumes
                for k in ("buy_volume", "sell_volume", "max_holding"):
                    if k in t:
                        want[item][k] = want[item].get(k, 0) + t[k]
            else:
                want[item] = dict(t)
    mine = st.setdefault("trade_items", {})
    items = ((snap or {}).get("store") or {}).get("items") or {}
    market = (snap or {}).get("market") or {}
    done, n = [], [0]

    def put(item, managers, capacity=None):
        body = {"managers": managers}
        if capacity is not None:
            body["capacity"] = int(capacity)
        ok, status, reply = write("/buildings/%s/storage/inventory/%s" % (store, api.q(item)), body)
        n[0] += 1
        with open(log_path, "a") as f:
            f.write(json.dumps({"ts": now().isoformat(timespec="seconds"), "turn": turn, "trade_item": item,
                                "to": body, "ok": bool(ok), "status": status,
                                "reply": None if ok else str(reply)[:200]}, default=str) + "\n")
        return bool(ok)

    for item, t in sorted(want.items()):
        if n[0] >= MAX_TRADE_WRITES:
            break
        live = [x for x in (live_tiers.get(item) or []) if x]
        if live and item not in mine:
            done.append("trade %s: skipped, other orders are on it" % item)
            continue
        if _canon(live) == _canon([t]):
            mine.setdefault(item, {"since": turn})
            continue
        it = items.get(item) or {}
        capn = max(_n(it.get("capacity")), _n(it.get("held")) + _n(t.get("max_holding")) + 2 * _n(t.get("sell_volume")), 10)
        ok = put(item, [t], capn)
        if ok:
            mine.setdefault(item, {"since": turn})
        done.append("trade %s -> %s %s" % (item, t, "ok" if ok else "FAILED"))
    for item in sorted(set(mine) - set(want)):
        if n[0] >= MAX_TRADE_WRITES:
            break
        held = _n((items.get(item) or {}).get("held"))
        live = [x for x in (live_tiers.get(item) or []) if x]
        if held >= 1:
            bid = _n((market.get(item) or {}).get("bid"))
            if bid > 0 and (not live or any(_n(x.get("buy_volume")) for x in live)):
                tier = [{"sell_volume": int(held), "sell_price": str(_snap_up(bid * 0.98)), "min_holding": 0}]
                if _canon(live) != _canon(tier):
                    put(item, tier)
                    done.append("trade %s: off route, selling the %d left at home" % (item, held))
            elif any(_n(x.get("buy_volume")) for x in live):
                put(item, [])
                done.append("trade %s: off route, buy stopped (no home bid for the %d left)" % (item, held))
            continue
        if live:
            put(item, [])
        del mine[item]
        done.append("trade %s: off every route, handed back" % item)
    return done


def _snap_up(p):
    sys.path.insert(0, HERE)
    import ships
    return ships.routes_snap(p, up=True)


VOYAGE_CREW = 0.5
VOYAGE_MIN_GAIN = 60           # a better town must promise this much a turn more before a ship sails
VOYAGE_COOLDOWN = 12           # turns between voyages per ship
VOYAGE_COOLDOWN_IDLE = 2       # ... when the ship's own town pays nothing
HOME_TOWN = "152202387"


def _queue_apply(entry):
    """The order queue's tested handlers (travel with the sea grid, route start/stop, crew), logged the same way."""
    sys.path.insert(0, ROOT)
    import order_queue
    r = order_queue.apply_entry(entry)
    order_queue.log(entry, r, source="v2-ships")
    return r


def ship_voyages(plan, cfg, snap, sst, log_path, apply=None):
    """Move an auto ship to a better town, one step per run (a ship moves at the turn tick):
      route that no longer pays (or no route) + a town promising VOYAGE_MIN_GAIN more -> stop the route, sail home;
      at home -> sail to the town and start the route there (the route runs on the home -> town journey);
      route on the target town -> done (ship_auto takes it from there).
    State per ship in act_state ships[id].voyage. At most one voyage per VOYAGE_COOLDOWN turns per ship."""
    apply = apply or _queue_apply
    modes = (cfg.get("live") or {}).get("ship_modes") or {}
    sp = (plan or {}).get("ship_plans") or {}
    turn = (snap or {}).get("turn") or 0
    plans = {str(p_.get("id")): p_ for p_ in sp.get("plans") or []}
    best = sp.get("best") or []
    taken = {str(s.get("route_to")) for s in (snap or {}).get("ships") or [] if s.get("route_to")}
    # Oct 13: reserve every in-progress voyage's target up front so two ships never head for the same town
    # (Flax Wyrm and linen snake both picked Etallaen an hour apart; the second would undercut the first's sales)
    voy_targets = {}
    for _s in (snap or {}).get("ships") or []:
        _sid = str(_s.get("id"))
        _v = (sst.get(_sid) or {}).get("voyage")
        if not _v:
            continue
        if str(_v["target"]) in voy_targets.values():
            sst[_sid]["voyage"] = None          # duplicate target: this ship re-plans below
            continue
        voy_targets[_sid] = str(_v["target"])
    taken |= set(voy_targets.values())
    out = []
    for sh in (snap or {}).get("ships") or []:
        sid = str(sh.get("id"))
        if modes.get(sid) != "auto":
            continue
        c = sst.setdefault(sid, {})
        v = c.get("voyage")
        if v:
            tgt = v["target"]
            if str(sh.get("route_to")) == tgt:
                c["voyage"] = None
                c["last_voyage_turn"] = turn
                out.append("%s: route on %s running" % (sh.get("name"), v.get("name")))
                continue
            at_home = str(sh.get("town")) == HOME_TOWN and not sh.get("route_to")
            if v.get("turn") == turn and not (at_home and v.get("step") == "home"):
                continue                        # one step per turn (the ship moves at the tick); sailing home is instant
            v["turn"] = turn
            if sh.get("route_to"):
                r = apply({"route": {"transport": sid, "stop": True}, "confirm": True})
                out.append("%s: stop route %s" % (sh.get("name"), "ok" if r.get("ok") else r.get("error") or r.get("status")))
                if not r.get("ok"):
                    continue
            if str(sh.get("town")) != HOME_TOWN and v["step"] == "home":
                apply({"transport": sid, "operation_target": VOYAGE_CREW})
                r = apply({"travel": {"transport": sid, "to_town": HOME_TOWN}, "confirm": True})
                out.append("%s: sail home %s" % (sh.get("name"), "ok" if r.get("ok") else r.get("error")))
                continue
            if str(sh.get("town")) == HOME_TOWN and v.get("step") == "home":
                # last look before sailing out: prices move, and a target picked on an over-full plan (Oct 13: Kirchwerp
                # scored +158 on cargo twice the ship's room) may no longer be the best. Take this run's best free town,
                # or end the voyage and wait at home at crew 0 if nothing pays.
                now_best = next((b for b in best if str(b.get("town_id")) not in taken or str(b.get("town_id")) == tgt), None)
                if not now_best:
                    apply({"transport": sid, "operation_target": 0.0})
                    c["voyage"] = None
                    c["last_voyage_turn"] = turn
                    out.append("%s: home; no town pays now, voyage ended, crew 0" % sh.get("name"))
                    continue
                if str(now_best["town_id"]) != tgt:
                    out.append("%s: re-targeted %s -> %s (%+.0f a turn)" % (sh.get("name"), v.get("name"), now_best["town"],
                                                                         now_best["per_turn"]))
                    v.update({"target": str(now_best["town_id"]), "name": now_best["town"], "expected": now_best["per_turn"],
                              "moves": now_best.get("moves")})
                    tgt = v["target"]
                taken.add(tgt)
            if str(sh.get("town")) == HOME_TOWN:
                # movement points per turn = 3,000 x crew, effective at once, and every move this turn (the instant hop
                # home included) spends them: Oct 13 a Brebronn trip (863) was refused with 794 left at crew 0.5
                moves = float(v.get("moves") or 800)
                apply({"transport": sid, "operation_target": round(min(1.0, max(VOYAGE_CREW, moves / 3000.0 + 0.4)), 2)})
                r = apply({"travel": {"transport": sid, "to_town": tgt}, "confirm": True})
                if not r.get("ok"):
                    out.append("%s: sail to %s refused (%s); retry next turn" % (sh.get("name"), v.get("name"),
                                                                                str(r.get("body") or r.get("error"))[:120]))
                    continue
                r2 = apply({"route": {"transport": sid, "start": True}, "confirm": True})
                if r2.get("ok") and str((r2.get("route") or {}).get("remote_town")) != tgt:
                    apply({"route": {"transport": sid, "stop": True}, "confirm": True})      # never keep a wrong route
                    r2 = {"ok": False, "error": "route came up on the wrong town; stopped"}
                v["step"] = "out"
                out.append("%s: sail to %s ok, route %s" % (sh.get("name"), v.get("name"),
                                                            "started" if r2.get("ok") else "not yet (%s)" % (r2.get("error") or r2.get("status"))))
                continue
            if v["step"] == "out" and str(sh.get("town")) == tgt:
                r2 = apply({"route": {"transport": sid, "start": True}, "confirm": True})
                out.append("%s: at %s, route %s" % (sh.get("name"), v.get("name"), "started" if r2.get("ok") else "FAILED %s" % (r2.get("error") or r2.get("status"))))
            continue
        cur = (plans.get(sid) or {}).get("est_net", 0.0) if sh.get("route_to") else 0.0
        # an idle ship (nothing pays where it is) waits only VOYAGE_COOLDOWN_IDLE turns: Oct 13 Flax Wyrm sat at crew 0
        # in Brebronn with Clairlond paying ~+220 a turn, held back by the 12-turn cooldown meant for earning ships
        idle = not (plans.get(sid) or {}).get("orders")
        if turn - (c.get("last_voyage_turn") or -999) < (VOYAGE_COOLDOWN_IDLE if idle else VOYAGE_COOLDOWN):
            continue
        cand = next((b for b in best if str(b.get("town_id")) not in taken and b["per_turn"] >= cur + VOYAGE_MIN_GAIN), None)
        if not cand:
            continue
        c["voyage"] = {"target": str(cand["town_id"]), "name": cand["town"], "step": "home", "turn": None, "from_turn": turn,
                       "expected": cand["per_turn"], "moves": cand.get("moves")}
        out.append("%s: heading for %s (est %+.0f a turn vs %+.0f now)" % (sh.get("name"), cand["town"], cand["per_turn"], cur))
        with open(log_path, "a") as f:
            f.write(json.dumps({"ts": now().isoformat(timespec="seconds"), "turn": turn, "ship": sh.get("name"),
                                "voyage_to": cand["town"], "expected": cand["per_turn"], "current": cur}, default=str) + "\n")
        taken.add(str(cand["town_id"]))
    return out


def ship_guard(plan, ship_ids, st, turn, log_path):
    """A ship v2 watches (config live.ships) that costs crew for SHIP_IDLE_TURNS turns in a row while its route trades
    nothing is paused (crew 0). Oct 13: the Flax Wyrm ran ~2 days at 0.72 crew this way. Counts once per game turn."""
    out = []
    for sh in plan.get("ships") or []:
        sid = str(sh.get("id"))
        if sid not in ship_ids:
            continue
        c = st.setdefault(sid, {"idle": 0, "turn": None})
        c.setdefault("idle", 0)
        if c.get("voyage"):
            c["idle"] = 0
            continue                    # sailing to a new town costs crew without trading: expected
        if c.get("turn") == turn:
            continue
        c["turn"] = turn
        idle = (sh.get("cost") or 0) >= 5 and not sh.get("sold") and not sh.get("bought")
        c["idle"] = c["idle"] + 1 if idle else 0
        if c["idle"] >= SHIP_IDLE_TURNS and (sh.get("crew_set") or 0) > 0:
            ok, status, body = api.write("PUT", "/transports/%s/operation" % sid, {"operation_target": "0.000"})
            with open(log_path, "a") as f:
                f.write(json.dumps({"ts": now().isoformat(timespec="seconds"), "turn": turn, "ship": sh.get("ship"),
                                    "action": "pause (crew 0)", "why": "%d turns of crew cost with no route trade" % c["idle"],
                                    "ok": bool(ok), "status": status}, default=str) + "\n")
            out.append(sh.get("ship"))
            c["idle"] = 0
            c["guard_paused_turn"] = turn
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
    fs = _load(failsafe, {})
    fs_level = int(_n(fs.get("level")))
    paused = set((fs.get("paused") or {}).keys())
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

    rows, stand = decide(snap, plan, cfg, owned, live_tiers, fs_level, paused=paused)
    results, sent = {}, 0
    ship_ids = set(((cfg.get("live") or {}).get("ships")) or [])
    if live_mode and not stand and (owned or ship_ids):
        api.allow_writes()
    if live_mode and owned and not stand:
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
    paused_ships, ship_done = [], []
    if live_mode and ship_ids and not stand:
        paused_ships = ship_guard(plan or {}, ship_ids, st.setdefault("ships", {}), (snap or {}).get("turn"), LOG)
        ship_done = ship_auto(plan or {}, cfg, snap, LOG, st["ships"])
        if (cfg.get("ship_trade") or {}).get("on") and store:
            try:
                ship_done += trade_home(plan or {}, cfg, snap, st, store, live_tiers, LOG)
            except Exception as e:  # trade goods must never stop the rest
                ship_done.append("trade orders failed: %s: %s" % (type(e).__name__, e))
        try:
            ship_done += ship_voyages(plan or {}, cfg, snap, st["ships"], LOG)
        except Exception as e:      # a voyage step must never stop the store orders
            ship_done.append("voyages failed: %s: %s" % (type(e).__name__, e))
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
    if live_mode:       # one line per run: which items v2 would still change (handover candidates converge to "same")
        with open(os.path.join(out, "act_history.jsonl"), "a") as f:
            f.write(json.dumps({"t": res["t"], "turn": res["turn"], "owned": res["owned"], "stand_down": stand,
                                "differs": sorted(r["item"] for r in rows if not r["same"]),
                                "refused": {r["item"]: r["refused"] for r in rows if r.get("refused")},
                                "sent": sorted(r["item"] for r in rows if r.get("sent"))}, default=str) + "\n")
    print("v2 act (%s): owned %s; %d items differ from live; %d sent%s%s" % (
        res["mode"], ", ".join(sorted(owned)) or "none", res["would_change"], sent,
        ("; STAND DOWN: " + stand) if stand else "", ("; suspended " + ", ".join(newly)) if newly else "")
        + (("; paused ships " + ", ".join(paused_ships)) if paused_ships else ""))
    for d_ in ship_done:
        print("  ship: " + d_)
    for r in rows:
        if r["owned"] and not r["same"]:
            print("  %s: %s%s" % (r["item"], "refused: " + "; ".join(r["refused"]) if r.get("refused") else
                                  ("sent, verified" if r.get("verified") else "sent, NOT verified" if r.get("sent") else "would send"),
                                  ""))
    return res


if __name__ == "__main__":
    main()
