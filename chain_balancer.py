#!/usr/bin/env python3
"""Keep the flax -> retting -> spinning -> weaving -> sewing chain in balance.

v2 (Sep 27): PULL model. Sewing is sized to what actually SELLS (average
garments sold over the last 24 turns, from history/), not to the plot count,
and each step upstream makes exactly what the next step uses, plus a small
top-up while its stockpile is below target. Stockpile targets are in TURNS of
use (STOCK_TURNS), so they grow with the chain. Filling only happens when cash
is above FILL_CASH_MIN; below that the mode is HOLD (make what's used, no
top-up), so a finished expansion can never again drain cash to fill stock.

Runs from the merc-actor workflow. It only ACTS when (a) a chain building's
plot count changed (an expansion finished) or (b) the mode flips
(FILLING / FULL / HOLD). Otherwise it never fights manual tweaks.

    python chain_balancer.py            # dry run: print the plan
    python chain_balancer.py --live     # apply it (only if sizes or mode changed)
    python chain_balancer.py --live --force   # apply even if nothing changed

State (last seen sizes + mode) lives in state/chain_sizes.json.
"""
import glob
import json
import os
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request

import merc_status4 as m

LIVE = "--live" in sys.argv
FORCE = "--force" in sys.argv
STORE = "152202386005001"
STATE = os.path.join("state", "chain_sizes.json")

# ---------------------------------------------------------------- OPERATING MODE THRESHOLDS
# Shared with merc-ops.user.js and merc_actor.py (same numbers, no shared state file).
# Hysteresis: leave SOS only when cash > SOS_EXIT_CASH and profit positive SOS_EXIT_PROFIT_TURNS;
# leave GROWTH when cash < GROWTH_EXIT_CASH.
MODE = {
    "SOS_CASH": 2000,
    "SOS_SOFT_CASH": 4000,
    "SOS_NEG_TURNS": 3,
    "SOS_EXIT_CASH": 4000,
    "SOS_EXIT_PROFIT_TURNS": 3,
    "STEADY_MAX": 15000,
    "GROWTH_CASH": 15000,
    "GROWTH_PROFIT_TURNS": 24,
    "GROWTH_EXIT_CASH": 10000,
    "FILL_CASH_MIN": 8000,          # STEADY: stockpile top-ups only above this cash
    "OWN_LABOUR": 300,              # SOS: run only what our own labour covers
    "CONSTRUCTION_PACE_STEADY": 25,
    "STOCK_TURNS_CHAIN": 2,        # Oct 14 (Taylor: cut the piles, cash falling): was 4
    "SALES_WINDOW": 12,             # was 24; Ops uses 12 — keep in step
    "SALES_MARGIN": 1.05,
    "HOUSEHOLD_GARMENTS": 1.8,
    "EXPORT_GARMENTS": 0,           # fixed extra; real route exports are read each run (garment_exports, Oct 13)
    "MARKET_DEPTH_MULT": 3,
}

# building id, recipe inputs/outputs per 1x (read from the game's production pages)
CHAIN = {
    "flax":  {"id": "151602400",       "labour": 12,  "tools": 0,   "out": 16},   # plants (grow flax 1; Oct 13: was 11/0.6/18, so the farm was sized 11% short and retting ran short ~14 plants a turn)
    "ret":   {"id": "151802398",       "labour": 25,  "tools": 2,   "in": 90, "out": 35},   # plants -> fibres
    "spin":  {"id": "152202388002007", "labour": 75,  "tools": 0,   "in": 17, "out": 50},   # fibres -> thread
    "weave": {"id": "152202388001005", "labour": 75,  "tools": 0,   "in": 50, "out": 50},   # thread -> cloth
    "sew":   {"id": "152202388000004", "labour": 155, "tools": 0,   "in": 80, "out": 41},   # cloth -> garments
}

# Stockpiles between chain steps, in TURNS of what the next step uses.
# fill = extra units per turn made while below target (and cash allows).
STOCK_TURNS = MODE['STOCK_TURNS_CHAIN']
BUFFERS = {
    "flax fibres": {"fill": 5,  "drain": 10},
    "thread":      {"fill": 15, "drain": 30},
    "cloth":       {"fill": 10, "drain": 40},
}
DRAIN_OVER = 1.2         # drain a buffer once it is over 1.2x its target (Oct 14: was 1.5)
DRAIN_TURNS = 12         # spread the excess over this many turns
GARMENT_KEEP_TURNS = 2    # finished garments: keep ~2 turns of sales on hand (Oct 12: 557 held vs ~65/turn sold)
GARMENT_DRAIN_TURNS = 20  # spread the excess over this many turns by sewing less than we sell
GARMENT_DRAIN_MAX = 30    # at most this many garments/turn of drain
DRIFT = 0.10             # also rebalance when any planned target is this far (x) from the current one
LOW_FRACTION = 0.5       # FILLING starts when a stock is under half its target
FILL_CASH_MIN = MODE['FILL_CASH_MIN']  # below this cash: HOLD (no top-ups, make only what's used)
SALES_WINDOW = MODE['SALES_WINDOW']   # turns of garment sales to average
SALES_MARGIN = MODE['SALES_MARGIN']   # sew 5% over average sales (garment stock covers the rest)
# Thread the household net duty uses (~24/turn). Measured use reads 0 when weaving
# stalled last turn, so never plan with less than this.
OTHER_THREAD_MIN = 24
ROPEWALK = "152202388001000"   # ropewalk building (make rope 2)
ROPE_THREAD = 55          # thread per ropewalk run
EXTRA_THREAD_MIN = 10    # thread use above the net duty by more than this = another consumer (ropewalk): fed from weaving
MIN_CHANGE = 0.02        # ignore target changes smaller than this (x)
EXPORTS = 0.0            # garments a turn sold abroad by ship routes (garment_exports(), set in main)


def gh(*args):
    try:
        return subprocess.run(["gh", *args], capture_output=True, text=True)
    except FileNotFoundError:
        return subprocess.CompletedProcess(args, 1, "", "no gh")


def send(method, path, body):
    req = urllib.request.Request(
        "https://play.mercatorio.io/api" + path, data=json.dumps(body).encode(), method=method,
        headers={"X-Merc-User": m.USER, "Authorization": "Bearer " + m.TOKEN,
                 "Content-Type": "application/json", "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return True, r.status
    except urllib.error.HTTPError as e:
        return False, "%s %s" % (e.code, e.read().decode()[:200])
    except urllib.error.URLError as e:
        return False, str(e.reason)


def garment_exports():
    """Garments a turn our ships' trade routes actually sold abroad, averaged over the last 12 game turns (v2 history
    `exports`; turns with no record count as 0). Realized sales only: no fallback to what the ship plans offer.
    Oct 13 lesson: counting offers and a 6-turn average of two lucky turns ramped the chain (flax 7.6 -> 11, sew 1.1 ->
    2, labour ~470 -> ~940 bought a turn) into a garment market that trades ~65 a turn at ~22 everywhere; the bids that
    made the first exports pay were one-off spikes. Cash fell ~2,600 over 4 turns before the balancer drained back."""
    per_turn = {}
    try:
        with open(os.path.join("state", "v2", "history.jsonl")) as f:
            for line in f:
                try:
                    r = json.loads(line)
                except ValueError:
                    continue
                if r.get("turn") is not None:
                    per_turn.setdefault(r["turn"], 0.0)
                    if "exports" in r:
                        per_turn[r["turn"]] = max(per_turn[r["turn"]], m.num((r.get("exports") or {}).get("garments")))
    except OSError:
        pass
    if not per_turn:
        return 0.0
    last = max(per_turn)
    return sum(per_turn.get(t, 0.0) for t in range(last - 11, last + 1)) / 12.0


def garment_sales():
    """Average garments sold per turn over the last SALES_WINDOW turns (None if no history)."""
    per_turn = {}
    for path in sorted(glob.glob("history/merc-*.jsonl")):
        with open(path) as f:
            for line in f:
                try:
                    r = json.loads(line)
                    per_turn[r["turn"]] = m.num(r["items"]["garments"][3])
                except (ValueError, KeyError, IndexError, TypeError):
                    continue
    last = [per_turn[t] for t in sorted(per_turn)[-SALES_WINDOW:]]
    return sum(last) / len(last) if len(last) >= 6 else None


def targets(t, other_thread):
    """Stockpile targets = STOCK_TURNS x what the next step uses per turn."""
    C = CHAIN
    return {
        "cloth": STOCK_TURNS * t["sew"] * C["sew"]["in"],
        "thread": STOCK_TURNS * (t["weave"] * C["weave"]["in"] + other_thread),
        "flax fibres": STOCK_TURNS * t["spin"] * C["spin"]["in"],
    }


def plan(sizes, other_thread, sales, stocks=None, mode="HOLD"):
    """Pull model: sew what sells, each step upstream feeds the next, plus a
    top-up per step while its stockpile is below target and mode is FILLING."""
    s, C = sizes, CHAIN
    stocks = stocks or {}
    want = sales + MODE['HOUSEHOLD_GARMENTS'] + MODE.get('EXPORT_GARMENTS', 0) + EXPORTS if sales else s["sew"] * C["sew"]["out"]
    have_g = stocks.get("garments", 0)
    outflow = (sales or 0) + EXPORTS
    if sales and have_g > GARMENT_KEEP_TURNS * outflow:
        # glut drain for the finished good (Oct 12): sell the pile down instead of sewing on top of it
        drain = min((have_g - GARMENT_KEEP_TURNS * outflow) / GARMENT_DRAIN_TURNS, GARMENT_DRAIN_MAX)
        want = max(want - drain, 0.3 * want)
    sew = min(s["sew"], want * SALES_MARGIN / C["sew"]["out"])
    # Oct 13 (Taylor: strive for profit): thread for consumers beyond the net duty (the ropewalk, 55/run)
    # is taken out of WEAVING, never by ramping flax/retting/spinning. Upstream is sized for weaving +
    # nets only. Rope earns ~18 a unit on thread vs ~1.5 a garment, and the Oct 13 ramp to feed rope
    # ate the labour the banquet/park/camp needed.
    fed_by_weaving = other_thread - OTHER_THREAD_MIN > EXTRA_THREAD_MIN
    other_up = OTHER_THREAD_MIN if fed_by_weaving else other_thread
    base = {"sew": sew, "weave": sew * C["sew"]["in"] / C["weave"]["out"]}
    base["spin"] = (base["weave"] * C["weave"]["in"] + other_up) / C["spin"]["out"]
    base["ret"] = base["spin"] * C["spin"]["in"] / C["ret"]["out"]
    tg = targets(base, other_thread)

    def top(item):
        have = stocks.get(item, 0)
        if mode == "FILLING" and have < tg[item]:
            return BUFFERS[item]["fill"]
        # glut drain (Oct 9): well over target, make less than is used so the pile shrinks
        # (excess spread over DRAIN_TURNS, capped per turn), freeing labour upstream
        if have > tg[item] * DRAIN_OVER:
            return -min((have - tg[item]) / DRAIN_TURNS, BUFFERS[item]["drain"])
        return 0
    weave = max(0, min(s["weave"], (sew * C["sew"]["in"] + top("cloth")) / C["weave"]["out"]))
    spin = max(0, min(s["spin"], (weave * C["weave"]["in"] + other_up + top("thread")) / C["spin"]["out"]))
    if fed_by_weaving:
        # weave only the thread spinning leaves after the other consumers (and the thread buffer's top-up)
        weave = max(0, min(weave, (spin * C["spin"]["out"] - other_thread - top("thread")) / C["weave"]["in"]))
        # sew only what weaving now makes plus a slice of the cloth pile above half its target,
        # so sewing labour isn't bought for cloth that won't be there
        cloth_slice = max(0.0, stocks.get("cloth", 0) - LOW_FRACTION * tg["cloth"]) / DRAIN_TURNS
        sew = min(sew, (weave * C["weave"]["out"] + cloth_slice) / C["sew"]["in"])
    ret =max(0, min(s["ret"], (spin * C["spin"]["in"] + top("flax fibres")) / C["ret"]["out"]))
    flax = min(s["flax"], ret * C["ret"]["in"] / C["flax"]["out"])
    # if plots cap a step upstream, the buffers cover the gap; the alert tells us
    t = {"sew": sew, "weave": weave, "spin": spin, "ret": ret, "flax": flax}
    return {k: round(v, 2) for k, v in t.items()}, tg


def profit_streak(sign, n):
    """True if the last n history turns all have trading profit with the given sign (+1/-1)."""
    per_turn = {}
    for path in sorted(glob.glob("history/merc-*.jsonl")):
        with open(path) as f:
            for line in f:
                try:
                    r = json.loads(line)
                    # items[*][3] is sale qty; we need value. Prefer explicit profit if present.
                    profit = r.get("profit")
                    if profit is None:
                        # approximate: sum sale_value - purchase_cost if present in flows-like fields
                        continue
                    per_turn[r["turn"]] = 1 if float(profit) >= 0 else -1
                except (ValueError, KeyError, TypeError):
                    continue
    last = [per_turn[t] for t in sorted(per_turn)[-n:]]
    return len(last) >= n and all(x == sign for x in last)


def operating_mode(cash, last_op=None):
    """SOS / STEADY / GROWTH from cash + profit (same thresholds as Ops). No shared state file."""
    last_op = last_op or "STEADY"
    if last_op == "SOS":
        if not (cash > MODE["SOS_EXIT_CASH"] and profit_streak(1, MODE["SOS_EXIT_PROFIT_TURNS"])):
            return "SOS"
    elif last_op == "GROWTH":
        if cash < MODE["GROWTH_EXIT_CASH"]:
            if cash < MODE["SOS_CASH"] or (cash < MODE["SOS_SOFT_CASH"] and profit_streak(-1, MODE["SOS_NEG_TURNS"])):
                return "SOS"
            return "STEADY"
        return "GROWTH"
    if cash < MODE["SOS_CASH"] or (cash < MODE["SOS_SOFT_CASH"] and profit_streak(-1, MODE["SOS_NEG_TURNS"])):
        return "SOS"
    if cash > MODE["GROWTH_CASH"] and profit_streak(1, MODE["GROWTH_PROFIT_TURNS"]):
        return "GROWTH"
    return "STEADY"


def buffer_mode(stocks, last_mode, tg, cash, op_mode="STEADY"):
    # Operating mode gates fill behaviour
    if op_mode == "SOS":
        return "HOLD"
    if op_mode == "STEADY" and cash < FILL_CASH_MIN:
        return "HOLD"
    # GROWTH (and STEADY above FILL_CASH_MIN) may fill
    low = any(stocks.get(i, 0) < tg[i] * LOW_FRACTION for i in BUFFERS)
    full = all(stocks.get(i, 0) >= tg[i] for i in BUFFERS)
    if low:
        return "FILLING"
    if full:
        return "FULL"
    if last_mode in (None, "HOLD"):
        return "FILLING"      # cash is back and stock is below target: top up
    return last_mode


def main():
    try:
        import v2_owned
        if v2_owned.chain_owned():
            print("chain sizing is v2's (v2/config.json live.chain; v2/chain.py): balancer stands aside")
            return
    except Exception as e:
        print("v2 chain check failed (%s): balancer runs as before" % e)
    blds = {k: m.get("/buildings/%s" % v["id"]) for k, v in CHAIN.items()}
    sizes = {k: int(m.num(b.get("size"))) for k, b in blds.items()}
    cur = {k: m.num((b.get("producer") or {}).get("target")) for k, b in blds.items()}
    recipes = {k: (b.get("producer") or {}).get("recipe") for k, b in blds.items()}

    store = m.get("/buildings/%s" % STORE)
    inv = (store.get("storage") or {}).get("inventory") or {}
    flows = inv.get("previous_flows") or {}
    holds = inv.get("holdings") or {}
    # thread used by anything other than the weavery (household net duty)
    other_thread = max(OTHER_THREAD_MIN, m.num((flows.get("thread") or {}).get("consumption")) - cur["weave"] * CHAIN["weave"]["in"])
    # Oct 14: count the ropewalk's PLANNED thread draw (target x 55), not just what it used last turn.
    # When labour starved the ropewalk to 0, measured use fell to the net duty, fed_by_weaving switched
    # off, weave/sew went back up and ate the labour rope needed: a loop (night checks Oct 14).
    try:
        rw = (m.get("/buildings/%s" % ROPEWALK) or {}).get("producer") or {}
        if "rope" in str(rw.get("recipe") or ""):
            other_thread = max(other_thread, OTHER_THREAD_MIN + m.num(rw.get("target")) * ROPE_THREAD)
    except (Exception, SystemExit) as e:
        print("ropewalk read failed (%s); using measured thread use" % e)

    try:
        with open(STATE) as f:
            saved = json.load(f)
    except (OSError, ValueError):
        saved = None
    # state file: {"sizes": {...}, "mode": "FILLING"|"FULL"}; older files held just the sizes
    if saved and "sizes" in saved:
        last, last_mode = saved["sizes"], saved.get("mode")
    else:
        last, last_mode = saved, None

    assets = (inv.get("account") or {}).get("assets") or {}
    stocks = {i: m.num((assets.get(i) or {}).get("balance")) for i in BUFFERS}
    stocks["garments"] = m.num((assets.get("garments") or {}).get("balance"))
    # cash is on the business account; /households has no cash field (read as 0 = SOS forever)
    _pl = m.get("/player") or {}
    _biz = m.get("/businesses/%s" % (_pl.get("household") or {})["business_ids"][0]) or {}
    cash = m.num(((_biz.get("account") or {}).get("assets") or {}).get("money", {}).get("balance"))
    sales = garment_sales()
    global EXPORTS
    try:
        EXPORTS = garment_exports()
    except Exception:
        EXPORTS = 0.0
    print("garment exports by ship routes: %.1f a turn" % EXPORTS)
    # operating mode (SOS/STEADY/GROWTH) from cash + profit; last op from state file if present
    last_op = None
    if saved and isinstance(saved, dict):
        last_op = saved.get("op_mode")
    op_mode = operating_mode(cash, last_op)
    _, tg = plan(sizes, other_thread, sales, stocks, "HOLD")
    mode = buffer_mode(stocks, last_mode, tg, cash, op_mode)
    new, tg = plan(sizes, other_thread, sales, stocks, mode)
    # SOS: cap chain to OWN_LABOUR, sewing first
    if op_mode == "SOS":
        left = MODE["OWN_LABOUR"]
        order = ["sew", "weave", "spin", "ret", "flax"]
        for k in order:
            max_x = left / CHAIN[k]["labour"] if CHAIN[k]["labour"] else new[k]
            new[k] = round(min(new[k], sizes[k], max(0, max_x)), 2)
            left -= new[k] * CHAIN[k]["labour"]
    changed = last is not None and last != sizes
    mode_changed = mode != last_mode
    print("sizes:", sizes, "(last seen: %s)" % last)
    print("cash: %.0f (fill only above %d) | garments sold/turn (avg %d turns): %s" % (
        cash, FILL_CASH_MIN, SALES_WINDOW, "%.1f" % sales if sales else "no history"))
    print("stocks:", {k: round(v) for k, v in stocks.items()}, "targets (%d turns):" % STOCK_TURNS,
          {k: round(v) for k, v in tg.items()})
    print("op_mode: %s | buffer mode: %s (last: %s)" % (op_mode, mode, last_mode))
    print("current targets:", cur)
    print("planned targets:", new, "| other thread use %.1f" % other_thread)
    print("garments/turn: %.1f -> %.1f" % (cur["sew"] * 41, new["sew"] * 41))

    def save():
        with open(STATE, "w") as f:
            json.dump({"sizes": sizes, "mode": mode, "op_mode": op_mode}, f)

    os.makedirs("state", exist_ok=True)
    if last is None:
        save()
        print("first run: saved sizes, no changes made")
        return
    drift = [k for k in CHAIN if abs(new[k] - cur[k]) >= DRIFT]
    if not (changed or mode_changed or FORCE or drift):
        print("no expansion finished, buffer mode unchanged, targets within %.2fx of plan: nothing to do" % DRIFT)
        return
    if any(not r for r in recipes.values()):
        print("a chain building is stopped (%s): not rebalancing" % recipes)
        return

    moves = [(k, cur[k], new[k]) for k in CHAIN if abs(new[k] - cur[k]) >= MIN_CHANGE]
    d_lab = sum((n - c) * CHAIN[k]["labour"] for k, c, n in moves)
    d_tools = sum((n - c) * CHAIN[k]["tools"] for k, c, n in moves)
    why = []
    if changed:
        why.append("expansion finished: " + ", ".join(
            "%s %s->%s plots" % (k, last.get(k), sizes[k]) for k in CHAIN if last.get(k) != sizes[k]))
    if mode_changed:
        why.append("mode %s -> %s (cash %.0f; %s)" % (last_mode, mode, cash, ", ".join(
            "%s %.0f/%.0f" % (i, stocks[i], tg[i]) for i in BUFFERS)))
    if drift and not (changed or mode_changed):
        why.append("sales/stock drift: " + ", ".join("%s %.2f->%.2f" % (k, cur[k], new[k]) for k in drift))
    lines = ["**Chain rebalanced** (%s)" % ("; ".join(why) or "forced")]
    lines += ["- %s %.2fx -> %.2fx" % (k, c, n) for k, c, n in moves] or ["- targets already right"]
    lines.append("- garments %.1f -> %.1f/turn, labour %+.0f/turn, tools %+.1f/turn" % (
        cur["sew"] * 41, new["sew"] * 41, d_lab, d_tools))

    if LIVE:
        errors = []
        for k, c, n in moves:
            ok, res = send("PUT", "/buildings/%s/producer" % CHAIN[k]["id"],
                           {"target": "%.3f" % n, "autoset_buying": False, "autoset_selling": False, "allow_overprod": False})
            if not ok:
                errors.append("%s target: %s" % (k, res))

        def bump(item, field, delta, idx=0):
            try:
                import v2_owned
                if v2_owned.owned(item):
                    lines.append("- %s %s left to v2 (v2 runs this item)" % (item, field))
                    return
            except Exception:
                pass
            ms = [{kk: vv for kk, vv in x.items() if kk != "result"} for x in (holds.get(item) or {}).get("managers") or []]
            if not ms or len(ms) <= idx:
                return
            ms[idx][field] = max(0, round(m.num(ms[idx].get(field)) + delta))
            ok, res = send("PATCH", "/buildings/%s/storage/inventory/%s" % (STORE, urllib.parse.quote(item, safe="")), {"managers": ms})
            if not ok:
                errors.append("%s order: %s" % (item, res))
            else:
                lines.append("- %s %s -> %s" % (item, field, ms[idx][field]))

        if abs(d_lab) >= 1 and op_mode != "SOS":
            bump("labour", "buy_volume", d_lab)
        elif abs(d_lab) >= 1 and op_mode == "SOS":
            lines.append("- labour buy skipped (SOS)")
        if abs(d_tools) >= 1:
            bump("tools", "buy_volume", d_tools)
        g_ms = (holds.get("garments") or {}).get("managers") or []
        si = next((i for i, x in enumerate(g_ms) if m.num(x.get("sell_volume"))), None)
        if si is not None:
            want = round(new["sew"] * 41 - MODE['HOUSEHOLD_GARMENTS'])
            bump("garments", "sell_volume", want - m.num(g_ms[si].get("sell_volume")), si)
        if errors:
            lines.append("- **errors:** " + "; ".join(errors))
        save()
        text = "\n".join(lines)
        print(text)
        r = gh("issue", "list", "--label", "merc-status", "--state", "open", "--limit", "1", "--json", "number")
        try:
            num = str(json.loads(r.stdout or "[]")[0]["number"])
        except (ValueError, IndexError, KeyError):
            num = "1"
        gh("issue", "comment", num, "--body", text)
    else:
        print("\n".join(lines))
        print("(dry run: nothing sent)")


if __name__ == "__main__":
    try:
        main()
    except SystemExit as e:          # merc_status4.get exits on API errors / turn in progress
        print("balancer skipped:", e)
