#!/usr/bin/env python3
"""Mercatorio actor -- dry-run by default, live only with --live.

Builds on merc_advisor.py's flags: for the flag kinds that are safe to fix
mechanically (a buy/sell order priced away from the market), it works out
the exact write call that would correct it. Without --live, that's all it
does -- the decision is logged, nothing is sent.

With --live, it PATCHes the real endpoint (confirmed against the open-source
pymerc library's implementation, not guessed):
  PATCH https://play.mercatorio.io/api/buildings/{id}/storage/inventory/{item}
using the same X-Merc-User / Bearer token auth merc_status4.py already uses.
Two safety rails stay on regardless: only stale_buy/stale_sell flags are ever
actionable (see ACTIONABLE_KINDS), and any proposed price more than
MAX_PRICE_JUMP away from the currently posted price is refused and logged,
never sent.

Needs merc_status4.py and merc_advisor.py in the same folder, and working
credentials already loaded by merc_status4.py (API_USER/API_TOKEN env vars
or ~/.merc_creds).

    python merc_actor.py              # one dry-run pass, prints + logs
    python merc_actor.py --live       # actually sends the proposed fixes
    python merc_actor.py --quiet      # log only, no console output (for cron/Task Scheduler)
    python merc_actor.py --json       # print the decisions as JSON instead of text
"""
import datetime
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

import merc_status4 as m
import merc_advisor as adv

# LIVE_MODE only turns on with an explicit --live flag on the command line --
# there is no way to flip this by editing a constant, on purpose.
LIVE_MODE = "--live" in sys.argv

QUIET = "--quiet" in sys.argv
AS_JSON = "--json" in sys.argv

# a proposed price more than this fraction away from the CURRENT posted price
# is refused and logged instead of sent -- catches a bad flag/bug turning into
# an absurd price change instead of just trusting the math blindly
MAX_PRICE_JUMP = 0.5  # 50%

# ---------------------------------------------------------------- OPERATING MODE THRESHOLDS
# Shared with merc-ops.user.js and chain_balancer.py (same numbers, no shared state file).
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
    "FILL_CASH_MIN": 8000,
    "OWN_LABOUR": 300,
    "CONSTRUCTION_PACE_STEADY": 25,
    "STOCK_TURNS_CHAIN": 4,
    "SALES_WINDOW": 12,
    "SALES_MARGIN": 1.05,
    "HOUSEHOLD_GARMENTS": 1.8,
    "MARKET_DEPTH_MULT": 3,
}

LOG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "merc_actions.log")

# only these flag kinds get an auto-proposed fix; everything else stays
# advisory-only because it takes a judgment call merc_advisor.py can't make
# safely on its own (start a new rule, change volumes, walk away from a
# building, etc.)
ACTIONABLE_KINDS = {"stale_buy", "stale_sell"}


def _current_price(d, field):
    """Pull the currently posted buy_price/sell_price out of the item's managers."""
    for mg in d["managers"]:
        v = mg.get(field)
        if v is not None:
            return m.num(v)
    return None


# Taylor's standing limits. Sells never go below the floor, buys never above
# the ceiling. Items with no limit here are never repriced (don't guess).
SELL_FLOORS = {
    "timber": 8.50,
    "flax fibres": 5.40,
    "flax plants": 1.27,
    "beer": 3.90,
    "cloth": 7.80,
    "thread": 4.50,
    "garments": 22.00,
}
BUY_CEILINGS = {"grain": 3.10, "labour": 1.80, "firewood": 2.25, "bread": 2.60, "tools": 5.75, "charcoal": 2.20, "furniture": 15.00, "fish": 2.50, "meat": 2.40, "timber": 7.00, "limestone": 18.00}


def snap_price(p, up):
    """Snap a price to the game's price grid (tested against the server,
    May 1069): at most 2 decimals and 3 significant digits; when the first
    digit is 1 any last digit is fine, 2-4 needs an even last digit
    (3.85 rejected, 3.84 ok), 5-9 needs a last digit of 0 or 5
    (5.46 rejected, 5.45 ok). up=True rounds up (a sell never drops below
    its target), False rounds down (a buy never goes above it)."""
    import math
    if not p or p <= 0:
        return p
    e = math.floor(math.log10(p) + 1e-12) - 2
    lead = int(p / 10 ** (e + 2) + 1e-9)
    step = 10 ** e * (5 if lead >= 5 else 2 if lead >= 2 else 1)
    step = max(step, 0.01)
    n = p / step
    n = math.ceil(n - 1e-9) if up else math.floor(n + 1e-9)
    return round(n * step, 6)


def propose_fix(building, building_id, item, kind, d):
    """Return the write call this flag implies, without sending it.

    The real API stores an item's buy/sell rules as a LIST under
    managers[] -- not a flat field on the item -- so the write payload has
    to be the whole (corrected) list, not a bare {field: value}. We rebuild
    that list here, changing only the one field that needs fixing and
    dropping each entry's server-computed "result" block (read-only,
    shouldn't be echoed back in a write)."""
    if kind == "stale_buy":
        field, new_price = "buy_price", d["lowest_ask"]
        reason = "match current lowest ask so the order can actually fill"
    elif kind == "stale_sell":
        field, new_price = "sell_price", d["highest_bid"]
        reason = "match current highest bid so the order can actually fill"
    else:
        return None

    if not new_price:
        return None
    old_price = _current_price(d, field)
    new_price = snap_price(new_price, up=(field == "sell_price"))
    if field == "sell_price":
        lim = SELL_FLOORS.get(item)
        if lim is None or new_price < lim:
            return None
    else:
        lim = BUY_CEILINGS.get(item)
        if lim is None or new_price > lim:
            return None

    managers_patch = []
    found = False
    for mg in d["managers"]:
        entry = {k: v for k, v in mg.items() if k != "result"}
        if not found and entry.get(field) is not None:
            entry[field] = str(new_price)
            found = True
        managers_patch.append(entry)

    if not found:
        return None  # couldn't locate which manager entry to patch -- don't guess

    p = dict(
        action="patch_manager",
        building=building, building_id=building_id, item=item,
        change="reprice %s order" % ("buy" if field == "buy_price" else "sell"),
        field=field,
        old_value=old_price,
        new_value=new_price,
        managers_patch=managers_patch,
        reason=reason,
    )

    if old_price and abs(p["new_value"] - old_price) / old_price > MAX_PRICE_JUMP:
        p["skipped"] = "price move >%.0f%% (%.2f -> %.2f) -- refused, needs a human look" % (
            MAX_PRICE_JUMP * 100, old_price, p["new_value"])

    return p


def chain_state(biz):
    """What our production buildings came up short on last turn, and whether
    any of them ran well under target for a reason other than labour. While
    the chain is stalled or restarting, last turn's usage is not normal usage:
    trimming labour or dropping a buy then breaks things (Sep 26: porterage
    outage stopped flax + retting, the 'unused' porterage buy was nearly
    dropped and the labour buy nearly trimmed just as they restarted)."""
    short_items, stalled = set(), []
    for bb in biz.get("buildings", []):
        if bb.get("type") in ("storehouse", "warehouse"):
            continue
        b = adv.safe_get("/buildings/%s" % bb["id"]) or {}
        p = b.get("producer") or {}
        flows = (p.get("inventory") or {}).get("previous_flows") or {}
        for item, f in flows.items():
            if m.num((f or {}).get("shortfall")) > 0:
                short_items.add(item)
        po = p.get("previous_operation") or {}
        tgt, prod = m.num(po.get("target")), m.num(po.get("production"))
        lim = po.get("limitation")
        # a full output bin ("... space") is a deliberate throttle, not a stall;
        # counting it blocked every labour trim while the timber bin sat full
        if tgt > 0 and prod < tgt * 0.9 and lim and lim != "labour" and "space" not in str(lim):
            stalled.append("%s (%s)" % (bb.get("name") or bb["id"], lim))
    return short_items, stalled


def labour_proposal(building_id, building_name, stalled=()):
    """Labour auto-balance (Taylor, Sep 2026). Builds add labour to the buy and
    nothing takes it back when they finish, so bought labour expires. Each run:
    if last turn's bought labour expired, trim the buy by that (minus a small
    buffer); if we came up short, raise it by the shortfall plus the buffer.
    Moves under 5 are ignored and one move is capped at 25% of the buy."""
    b = adv.safe_get("/buildings/%s" % building_id)
    if not b:
        return None
    inv = (b.get("storage") or {}).get("inventory") or {}
    f = (inv.get("previous_flows") or {}).get("labour") or {}
    exp, short = m.num(f.get("expiration")), m.num(f.get("shortfall"))
    mgrs = ((inv.get("holdings") or {}).get("labour") or {}).get("managers") or []
    idx = next((i for i, mg in enumerate(mgrs) if m.num(mg.get("buy_volume"))), None)
    if idx is None:
        return None
    cur = m.num(mgrs[idx].get("buy_volume"))
    if exp <= LABOUR_BUFFER and short <= 0:
        return None
    # size the buy from what was actually used, not as a delta off the current
    # order: the current order may already have been changed by hand since that
    # turn, and a delta would then over-correct
    need = m.num(f.get("consumption")) + short - m.num(f.get("production")) + LABOUR_BUFFER
    new = need
    why = ("%.1f labour short last turn" % short) if short > 0 else ("%.1f bought labour expired last turn" % exp)
    if new < cur and stalled:
        print("labour trim skipped, chain stalled/restarting: %s" % ", ".join(stalled))
        return None
    # SOS: never raise the labour buy (trims still allowed)
    if new > cur and getattr(labour_proposal, "_op_mode", "STEADY") == "SOS":
        print("labour raise skipped (SOS)")
        return None
    new = max(cur * 0.75, min(cur * 1.25, new))
    new = int(round(max(0, new)))
    if abs(new - cur) < 5:
        return None
    patch = [{k: v for k, v in mg.items() if k != "result"} for mg in mgrs]
    patch[idx]["buy_volume"] = new
    return dict(action="patch_manager", building=building_name, building_id=building_id, item="labour",
                change="rebalance labour buy", field="buy_volume", old_value=cur, new_value=new,
                managers_patch=patch, reason=why, flag_text=why)


LABOUR_BUFFER = 10


def operating_mode(cash, last_op=None):
    """SOS / STEADY / GROWTH from cash (profit history is not loaded here; cash thresholds only).
    Full hysteresis with profit streaks lives in chain_balancer / Ops; actor uses cash gates
    so SOS never raises a labour buy."""
    last_op = last_op or "STEADY"
    if last_op == "SOS":
        if cash <= MODE["SOS_EXIT_CASH"]:
            return "SOS"
    elif last_op == "GROWTH":
        if cash < MODE["GROWTH_EXIT_CASH"]:
            return "SOS" if cash < MODE["SOS_CASH"] else "STEADY"
        return "GROWTH"
    if cash < MODE["SOS_CASH"]:
        return "SOS"
    if cash > MODE["GROWTH_CASH"]:
        return "GROWTH"
    return "STEADY"


CHAIN_INTERMEDIATES = {"flax plants", "flax fibres", "thread", "cloth"}


def cleanup_proposals(building_id, building_name, short_items=()):
    """Safe order cleanups (Taylor, Sep 2026):
    - a chain intermediate (flax plants/fibres, thread, cloth) came up short
      last turn while a sell order was on: drop the sell order, the chain needs it
    - an item was bought, nothing used it last turn and some expired: drop the
      buy order (e.g. porterage after the logging camp stopped)"""
    b = adv.safe_get("/buildings/%s" % building_id)
    if not b:
        return []
    inv = (b.get("storage") or {}).get("inventory") or {}
    flows = inv.get("previous_flows") or {}
    out = []
    for item, h in (inv.get("holdings") or {}).items():
        if item in ("labour", "money"):
            continue
        mgrs = (h or {}).get("managers") or []
        if not mgrs:
            continue
        f = flows.get(item) or {}
        short, cons = m.num(f.get("shortfall")), m.num(f.get("consumption"))
        exp, bought = m.num(f.get("expiration")), m.num(f.get("purchase"))
        patch = [{k: v for k, v in mg.items() if k != "result"} for mg in mgrs]
        why = []
        if item in CHAIN_INTERMEDIATES and short > 0 and any(m.num(mg.get("sell_volume")) for mg in patch):
            for mg in patch:
                for k in ("sell_volume", "sell_price", "min_holding"):
                    mg.pop(k, None)
            why.append("%.1f short last turn while being sold; the chain needs it" % short)
        if item in short_items:
            print("keep %s buy: a building came up short on it last turn" % item)
        elif bought > 0 and cons == 0 and exp > 0 and any(m.num(mg.get("buy_volume")) for mg in patch):
            for mg in patch:
                for k in ("buy_volume", "buy_price", "max_holding"):
                    mg.pop(k, None)
            why.append("bought %.1f, nothing used it, %.1f went off" % (bought, exp))
        if not why:
            continue
        patch = [mg for mg in patch if m.num(mg.get("buy_volume")) or m.num(mg.get("sell_volume"))]
        out.append(dict(action="patch_manager", building=building_name, building_id=building_id, item=item,
                        change="drop order", field="orders", old_value=0, new_value=0,
                        managers_patch=patch, reason="; ".join(why), flag_text="; ".join(why)))
    return out


def send_live(proposal):
    """PATCH the real manager endpoint for one proposal. Returns a result dict
    for logging; never raises -- a failed send is a logged fact, not a crash."""
    url = "https://play.mercatorio.io/api/buildings/%s/storage/inventory/%s" % (
        proposal["building_id"], urllib.parse.quote(proposal["item"], safe=""))
    payload = json.dumps({"managers": proposal["managers_patch"]}, default=str).encode()
    req = urllib.request.Request(
        url, data=payload, method="PATCH",
        headers={
            "X-Merc-User": m.USER,
            "Authorization": "Bearer " + m.TOKEN,
            "Content-Type": "application/json",
            "Accept": "application/json",
        })
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return dict(sent=True, status=r.status, body=r.read().decode()[:800])
    except urllib.error.HTTPError as e:
        return dict(sent=False, status=e.code, body=e.read().decode()[:800])
    except urllib.error.URLError as e:
        return dict(sent=False, status=None, body=str(e.reason))
    except Exception as e:
        # anything else (bad URL chars, encoding issues, etc.) -- never let a
        # send crash the whole run; log it as a failed send instead
        return dict(sent=False, status=None, body="%s: %s" % (type(e).__name__, e))


def log_error(msg):
    record = dict(
        ts=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        mode="dry_run" if not LIVE_MODE else "live",
        error=msg,
    )
    with open(LOG_PATH, "a") as f:
        f.write(json.dumps(record, default=str) + "\n")


def run():
    try:
        player = adv.safe_get("/player")
    except Exception as e:
        log_error("fetch /player raised: %r" % e)
        if not QUIET:
            print("Run failed: %r (logged)" % e, file=sys.stderr)
        sys.exit(1)
    if not player:
        log_error("fetch /player returned nothing")
        if not QUIET:
            print("Run failed: no player data (logged)", file=sys.stderr)
        sys.exit(1)
    hh = player.get("household", {})

    op_mode = "STEADY"
    try:
        biz_id = hh["business_ids"][0]
        biz = adv.safe_get("/businesses/%s" % biz_id)
        if not biz:
            raise RuntimeError("fetch /businesses/%s returned nothing" % biz_id)
        home_town_id = hh.get("town_id")

        stores = [b for b in biz.get("buildings", []) if b.get("type") in ("storehouse", "warehouse")]
        town_cache = {}
        proposals = []
        all_flags = []

        for s in stores:
            r = adv.building_report(s["id"], town_cache, home_town_id)
            if not r:
                continue
            for item, d in r["items"].items():
                for kind, text in adv.flag_item(item, d):
                    all_flags.append(dict(building=r["name"], item=item, kind=kind, text=text))
                    if kind in ACTIONABLE_KINDS:
                        p = propose_fix(r["name"], r["building_id"], item, kind, d)
                        if p:
                            p["flag_text"] = text
                            proposals.append(p)
        # operating mode from household cash (same thresholds as Ops / chain_balancer)
        try:
            cash = m.num((adv.safe_get("/households/%s" % hh.get("id", "21623")) or {}).get("cash"))
        except Exception:
            cash = 0
        op_mode = operating_mode(cash)
        labour_proposal._op_mode = op_mode
        if not QUIET:
            print("op_mode=%s cash=%.0f" % (op_mode, cash))

        # labour auto-balance: trim what expired / top up a shortfall (see labour_proposal)
        short_items, stalled = chain_state(biz)
        for s in stores:
            lp = labour_proposal(s["id"], s.get("name") or "storehouse", stalled)
            if lp:
                proposals.append(lp)
            proposals.extend(cleanup_proposals(s["id"], s.get("name") or "storehouse", short_items))
    except Exception as e:
        log_error("run failed mid-pass: %r" % e)
        if not QUIET:
            print("Run failed partway: %r (logged)" % e, file=sys.stderr)
        sys.exit(1)

    record = dict(
        ts=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        mode="dry_run" if not LIVE_MODE else "live",
        op_mode=locals().get("op_mode"),
        household=hh.get("name"),
        flags_total=len(all_flags),
        proposals=proposals,
    )

    with open(LOG_PATH, "a") as f:
        f.write(json.dumps(record, default=str) + "\n")

    if LIVE_MODE:
        if not (m.USER and m.TOKEN):
            log_error("live mode requested but no credentials loaded (m.USER/m.TOKEN empty)")
        else:
            for p in proposals:
                if p.get("skipped"):
                    continue  # sanity-bound refusal -- never sent
                result = send_live(p)
                log_line = dict(
                    ts=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
                    mode="live_send",
                    building=p["building"], item=p["item"], field=p["field"],
                    old_value=p["old_value"], new_value=p["new_value"],
                    **result,
                )
                with open(LOG_PATH, "a") as f:
                    f.write(json.dumps(log_line, default=str) + "\n")
                if not QUIET:
                    status = "OK" if result["sent"] else "FAILED"
                    print("  [LIVE %s] %s / %s -> %s = %s" %
                          (status, p["building"], p["item"], p["field"], p["new_value"]))

    if QUIET:
        return

    if AS_JSON:
        print(json.dumps(record, indent=2, default=str))
        return

    tag = "LIVE" if LIVE_MODE else "DRY RUN"
    print("%s | %d flags | %d actionable | mode=%s" %
          (record["ts"], record["flags_total"], len(proposals), tag))
    if not proposals:
        print("  nothing this pass would have fixed")
    for p in proposals:
        if p.get("skipped"):
            print("  [SKIPPED] %s / %s: %s" % (p["building"], p["item"], p["skipped"]))
            continue
        print("  [%s] %s / %s: %s -> %s = %.2f  (%s)" %
              ("DRY RUN" if not LIVE_MODE else "SENDING", p["building"], p["item"],
               p["change"], p["field"], p["new_value"], p["reason"]))
    if not LIVE_MODE:
        print("\n(nothing was sent -- logged to %s)" % LOG_PATH)
    else:
        print("\n(live results logged to %s)" % LOG_PATH)


if __name__ == "__main__":
    run()
