#!/usr/bin/env python3
"""Bot v2, shadow mode: read the game, plan, compare with what v1 has live, write the report.
Never writes to the game (api.allow_writes() is never called here).

    python v2/shadow.py                 # live read (needs credentials)
    python v2/shadow.py --from FILE     # replan a saved snapshot (offline testing)

Outputs (committed by the v2-shadow workflow):
  state/v2/snapshot.json   the full snapshot (latest)
  state/v2/plan.json       desired orders, flags, prestige sinks
  state/v2/report.md       the same in plain words
  state/v2/history.jsonl   one compact line per run (counts, cash, top flags) for the daily comparison
"""
import datetime
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import api        # noqa: E402
import planner    # noqa: E402
import snapshot   # noqa: E402

ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "state", "v2")


def report(p):
    L = ["# v2 shadow report", "",
         "Turn %s, %s. Mode: %s. v2 runs: %s; v1 runs everything else." % (
             p.get("turn"), (p.get("t") or "")[:16].replace("T", " "), p.get("mode"), ", ".join(p.get("live_items") or []) or "nothing (reads only)"),
         "Cash %s, prestige %s (%s free, %+.1f/turn)." % (
             "{:,.0f}".format(p.get("cash") or 0), "{:,.0f}".format(p.get("prestige") or 0),
             "{:,.0f}".format(p.get("prestige_free") or 0), p.get("prestige_rate") or 0), ""]
    live_items = p.get("live_items") or []
    if live_items and p.get("_items"):
        L += ["## Items v2 runs (last turn)", "", "| Item | Held | Bought | Used | Short | Expired | Live order |", "| --- | --- | --- | --- | --- | --- | --- |"]
        for item in live_items:
            it = p["_items"].get(item) or {}
            fl = it.get("flow") or {}
            o = "; ".join(", ".join("%s %s" % (k.replace("_volume", "").replace("_price", " @").replace("max_holding", "stop"), v)
                                    for k, v in tier.items()) for tier in it.get("orders") or []) or "none"
            L.append("| %s | %.0f | %.0f | %.0f | %.0f | %.0f | %s |" % (item, it.get("held", 0), fl.get("purchase", 0),
                                                                     fl.get("consumption", 0), fl.get("shortfall", 0), fl.get("expiration", 0), o))
        L.append("")
    c = p.get("counts") or {}
    L.append("**%d risks, %d waste, %d tuning** where v2 would act differently from v1." % (c.get("risk", 0), c.get("waste", 0), c.get("tune", 0)))
    L.append("")
    for sev, title in (("risk", "Risks (will stall or run out)"), ("waste", "Waste (money lost now)"), ("tune", "Tuning")):
        fs = [f for f in p.get("flags") or [] if f["severity"] == sev]
        if not fs:
            continue
        L += ["## " + title, ""]
        for f in fs:
            L.append("- **%s**: %s%s" % (f["item"], f["text"], (" -> v2: " + f["fix"]) if f.get("fix") else ""))
        L.append("")
    bp = p.get("builds")
    if bp:
        L += ["## Builds under construction", ""]
        for st in bp["sites"]:
            L.append("- **%s** %.0f%% (%s), about %s turns left; still to deliver: %s%s" % (
                st["building"], st["progress"], st.get("stage"), st.get("turns_left", "?"),
                ", ".join("%s %d" % kv for kv in st["remaining"].items()) or "nothing",
                "; ready for labour" if st.get("ready") else "; waiting on materials" if st["remaining"] else ""))
            for n_ in st.get("notes") or []:
                L.append("  - note: " + n_)
        L += ["", "| Material | Need | Held | Deficit | v2 action |", "| --- | --- | --- | --- | --- |"]
        for item, e in bp["buys"].items():
            act = {"buy": "buy %s @ %s, stop at %s" % (e.get("buy_volume"), e.get("buy_price"), e.get("max_holding")),
                   "off": "off: covered" + ("; switch v1's buy off" if e.get("switch_off") else ""),
                   "blocked": "blocked: %s" % e.get("why")}[e["action"]]
            L.append("| %s | %d | %s | %d | %s |" % (item, e["need"], e["held"], e["deficit"], act))
        if bp["drip"]:
            L.append("")
            L.append("Labour metered per turn while a site can progress: " + ", ".join("%s %d" % kv for kv in bp["drip"].items()))
        L.append("")
    if p.get("goals"):
        L += ["## Goals", "", "| Goal | Kind | Item | Status | Detail |", "| --- | --- | --- | --- | --- |"]
        for g in p["goals"]:
            L.append("| %s | %s | %s | %s | %s |" % (g["id"], g.get("kind"), g.get("item"), g["status"], g["detail"]))
        L.append("")
    if p.get("notes"):
        L += ["## Notes", ""] + ["- " + n_ for n_ in p["notes"]] + [""]
    pp = p.get("prestige_plan")
    if pp:
        L += ["## Prestige spending, cheapest coin per prestige first", ""]
        if pp.get("turns_left") is not None:
            L.append("%d turns left: prestige gained now converts %.1f%% of itself into legacy. Church contracts (best known rate, "
                     "16-38) are not in the snapshot, so they are not ranked here." % (pp["turns_left"], 100 * pp["legacy_factor"]))
            L.append("")
        for a in pp.get("agreed") or []:
            L.append("- agreed **%s** to level %s: %s - %s" % (a["sink"], a["to_level"], a["status"], a.get("detail", "")))
        L += ["", "| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |", "| --- | --- | --- | --- | --- | --- |"]
        for r in pp["ranked"][:12]:
            notes_ = []
            if r["running"]:
                notes_.append("running")
            elif not r["owned"]:
                notes_.append("needs a %s (build cost %s)" % (r["site"], "{:,}".format(r["capex"]) if r["capex"] else "unknown"))
            if r["thin"]:
                notes_.append("thin at home: " + ", ".join(r["thin"]))
            if r.get("class"):
                notes_.append("needs %s skill" % r["class"])
            L.append("| %s | %s | %s | %s | %s | %s |" % (r["sink"], r["site"], r["prestige_per_turn"], r["coin_per_prestige"],
                                                         r["effective"], "; ".join(notes_)))
        L.append("")
    elif p.get("sinks"):
        L += ["## Prestige sinks running now", "", "| Sink | Prestige/turn | Coin per prestige |", "| --- | --- | --- |"]
        for x in p["sinks"]:
            L.append("| %s | %.1f | %s |" % (x["sink"], x["prestige_per_turn"], x["coin_per_prestige"]))
        L.append("")
    if p.get("ships"):
        L += ["## Ships (last turn, real)", "", "| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |",
              "| --- | --- | --- | --- | --- | --- | --- | --- |"]
        for sh in p["ships"]:
            L.append("| %s | %s / %.2f | %.0f | %s | %s | %s | %s | %.0f |" % (
                sh["ship"], sh.get("crew_set"), sh.get("crew_last") or 0, sh["cost"], sh.get("route_to") or "-", sh.get("trips") or 0,
                ", ".join("%s %.0f" % kv for kv in sh["sold"].items()) or "-",
                ", ".join("%s %.0f" % kv for kv in sh["bought"].items()) or "-", sh["trade_value"]))
        L.append("")
    sp = p.get("ship_plans") or {}
    if sp.get("plans") or sp.get("best"):
        L += ["## Ship plans (this turn's world prices)", ""]
        for pl in sp.get("plans") or []:
            o = ", ".join("%s %s %s @ %s" % (k, "sell" if "sell_volume" in v else "buy", v.get("sell_volume") or v.get("buy_volume"),
                                              v.get("sell_price") or v.get("buy_price")) for k, v in pl["orders"].items()) or "nothing pays"
            L.append("- **%s** on %s: %s; crew %.1f; est %+.0f a turn%s" % (pl["ship"], pl["town"], o, pl["crew"], pl["est_net"],
                                                                         ("; " + "; ".join(pl["notes"])) if pl.get("notes") else ""))
        if sp.get("best"):
            L.append("- best towns now: " + ", ".join("%s %+.0f" % (r["town"], r["per_turn"]) for r in sp["best"][:5]))
            b0 = sp["best"][0]
            L.append("- %s would trade: %s; crew %.1f" % (b0["town"], ", ".join(
                "%s %s %s @ %s" % (k, "sell" if "sell_volume" in v else "buy", v.get("sell_volume") or v.get("buy_volume"),
                                   v.get("sell_price") or v.get("buy_price")) for k, v in (b0.get("orders") or {}).items()), b0["crew"]))
        L.append("")
    try:
        import routes
        L += routes.report_lines(p.get("routes"))
    except Exception:
        pass
    L += ["## v2 orders", "", "| Item | v2 buy | v2 sell | Why |", "| --- | --- | --- | --- |"]
    for item, o in sorted((p.get("orders") or {}).items()):
        b, s_ = o.get("buy"), o.get("sell")
        if not (b or s_):
            continue
        bt = ("%d @ %s, stop %s" % (b["buy_volume"], b.get("buy_price", "?"), b.get("max_holding", "-"))) if b else ""
        st = ("%d @ min %s" % (s_["sell_volume"], s_.get("sell_price"))) if s_ else ""
        L.append("| %s | %s | %s | %s |" % (item, bt, st, o.get("why", "")))
    return "\n".join(L) + "\n"


_WORLD = {}          # this run's world market (ship_routes fetches it; the goal planner reuses it)


def ship_routes(snap, out, replay):
    """World prices -> (route ranking, per-ship route plans). Fetched every run (ships need this turn's bids; one public
    download). A replay uses --world FILE (marketdata list or the queue's compact world.json.gz) if given, else the last
    ranking with no ship plans. Never fails the run."""
    import routes
    import ships
    path = os.path.join(out, "routes.json")
    last = None
    try:
        with open(path) as f:
            last = json.load(f)
    except (OSError, ValueError):
        pass
    try:
        if replay:
            if "--world" not in sys.argv:
                return last, None
            wp = sys.argv[sys.argv.index("--world") + 1]
            if wp.endswith(".gz"):
                import gzip
                world = routes.world_from_compact(json.load(gzip.open(wp, "rt")))
            else:
                with open(wp) as f:
                    world = json.load(f)
        else:
            world = routes.fetch_world()
        _WORLD["w"] = world
        cfg = planner.load_json("config.json")
        try:        # goods ship trade mode already runs (act.trade_home), so the planner keeps them in play
            with open(os.path.join(out, "act_state.json")) as f:
                cfg["_trade_owned"] = sorted((json.load(f).get("trade_items") or {}))
        except (OSError, ValueError, AttributeError):
            cfg["_trade_owned"] = []
        sea = routes.load_sea()
        rr = routes.rank(snap, world, sea, cfg=cfg)
        rr["t"] = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
        with open(path, "w") as f:
            json.dump(rr, f, indent=1)
        # ships share one storehouse: plan the best-paying route first and give the next ships what is left
        prelim = []
        for sh in snap.get("ships") or []:
            pl = ships.plan_ship(sh, snap, world, sea, cfg)
            if pl:
                prelim.append((pl["est_net"], sh))
        plans, taken = [], {}
        for _, sh in sorted(prelim, key=lambda x: -x[0]):
            pl = ships.plan_ship(sh, snap, world, sea, cfg, taken=taken)
            for item, o in pl["orders"].items():
                if "sell_volume" in o:
                    taken[item] = taken.get(item, 0) + o["sell_volume"]
            pl["diff"] = ships.route_diff(sh, pl)
            plans.append(pl)
        return rr, {"t": rr["t"], "plans": plans, "best": ships.best_towns(snap, world, sea, cfg)}
    except Exception as e:
        print("routes skipped: %s: %s" % (type(e).__name__, e))
        return last, None


ROUTES_EVERY_H = 6
HOME_SELL_MIN = 10      # always keep a little on the home market, in case the ships' buyers vanish for a turn


def _route_exports(snap):
    out = {}
    for sh in snap.get("ships") or []:
        for item, f in (sh.get("route_flows") or {}).items():
            n = ((f or {}).get("realized") or {}).get("export") or 0
            if n:
                out[item] = round(out.get(item, 0) + n, 1)
    return out


EXPORT_TRIAL_RUNS = 12  # a route gets this many runs of home-sell cuts to prove it ships; then the cut follows real exports


def _export_history(n=EXPORT_TRIAL_RUNS):
    try:
        lines = open(os.path.join(OUT, "history.jsonl")).read().splitlines()[-n:]
    except OSError:
        return []
    out = []
    for line in lines:
        try:
            out.append(json.loads(line))
        except ValueError:
            pass
    return out


def export_first(p, snap=None, hist=None):
    """When stock is short, the routes only get what the home sell orders leave, so home sells give way to the ship
    plans' offers (never under HOME_SELL_MIN). When stock covers both (garments 400 held, beer 280), nothing is cut:
    Oct 13 the cut left home garments at 30 and beer at 10 for two turns while the routes sold nothing.
    Oct 22: Linen Snake on Neuborn was offered 23 garments a turn for 40 turns and shipped 0, while home sells sat at
    10 (was 24) and the pile grew. Each run's offers now go to the history; after EXPORT_TRIAL_RUNS runs of an offer,
    if the ships really shipped under a quarter of it, the cut is held to what they really shipped."""
    sp = p.get("ship_plans") or {}
    items = ((snap or {}).get("store") or {}).get("items") or {}
    ex = {}
    for pl in sp.get("plans") or []:
        for item, o in (pl.get("orders") or {}).items():
            if "sell_volume" in o:
                ex[item] = ex.get(item, 0) + int(o["sell_volume"])
    p["export_offers"] = dict(ex)
    hist = _export_history() if hist is None else hist
    for item, n in ex.items():
        s = (p.get("orders") or {}).get(item, {}).get("sell")
        if not s:
            continue
        offered = [h for h in hist if ((h.get("offers") or {}).get(item) or 0) > 0]
        held_to = ""
        if len(offered) >= EXPORT_TRIAL_RUNS:
            real = sum(((h.get("exports") or {}).get(item) or 0) for h in offered)
            if real < 0.25 * sum(h["offers"][item] for h in offered):
                n_real = int(-(-real // len(offered)))      # ceil: the turn average they really shipped
                held_to = " (ships shipped %.0f in %d turns, so the cut is held to %d)" % (real, len(offered), n_real)
                n = n_real
        if n <= 0:
            p["orders"][item]["why"] = "%s; ships offered abroad but shipped none in %d turns: no home cut" % (
                p["orders"][item].get("why") or "sell", len(offered))
            continue
        before = int(s.get("sell_volume") or 0)
        it = items.get(item)
        if it is not None:
            keep = max([float(o.get("min_holding") or 0) for o in it.get("orders") or []] + [0.0])
            room = float(it.get("held") or 0) - keep
            if room >= before + n:
                continue            # enough stock for home and abroad: no cut
            s["sell_volume"] = max(HOME_SELL_MIN, min(before, int(room - n)))
        else:
            s["sell_volume"] = max(HOME_SELL_MIN, before - n)
        p["orders"][item]["why"] = "%s; ships offer %d a turn abroad%s, so home sells %d (was %d)" % (
            p["orders"][item].get("why") or "sell", n, held_to, s["sell_volume"], before)


def labour_numbers(snap):
    """(labour the operations project for next turn, labour really used last turn, last turn's shortfall)."""
    proj = 0.0
    for k, op in (snap.get("operations") or {}).items():
        if k.startswith(("producer/", "construction/", "transport/", "knight/")):
            pj = (((op.get("flows") or {}).get("labour") or {}).get("projection") or {})
            proj += (pj.get("consumption", 0) or 0) + (pj.get("shortfall", 0) or 0)
    fl = ((((snap.get("store") or {}).get("items") or {}).get("labour") or {}).get("flow")) or {}
    short = fl.get("shortfall", 0) or 0
    return round(proj, 1), round((fl.get("consumption", 0) or 0) + short, 1), round(short, 1)


def labour_bias(path, runs=8, need=3, cap=150.0):
    """Median of (projected - really used) over the last runs with no labour shortfall (state/v2/history.jsonl)."""
    gaps = []
    try:
        with open(path) as f:
            lines = f.readlines()[-runs:]
    except OSError:
        return 0.0
    for line in lines:
        try:
            lab = json.loads(line).get("labour") or {}
        except ValueError:
            continue
        if lab.get("proj") and lab.get("short", 0) <= 1:
            gaps.append(lab["proj"] - lab.get("used", 0))
    if len(gaps) < need:
        return 0.0
    gaps.sort()
    return max(0.0, min(cap, gaps[len(gaps) // 2]))


def main():
    if "--from" in sys.argv:
        with open(sys.argv[sys.argv.index("--from") + 1]) as f:
            snap = json.load(f)
    else:
        if not api.ready():
            print("v2 shadow: no credentials")
            return
        snap = snapshot.take()
    snap["labour_bias"] = labour_bias(os.path.join(OUT, "history.jsonl"))
    if "--from" not in sys.argv:
        try:            # season-proof ids for every script (state/ids.json)
            sys.path.insert(0, ROOT)
            import ids
            ids.save(snap)
        except Exception as e:
            print("ids not saved: %s" % e)
    p = planner.plan(snap)
    replay = "--from" in sys.argv
    out = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else OUT
    os.makedirs(out, exist_ok=True)
    p["routes"], p["ship_plans"] = ship_routes(snap, out, replay)
    export_first(p, snap)
    try:        # chain sizing (v2/chain.py): planned every run, applied by act.py when live.chain is on
        import chain as chain_mod
        cst = {}
        try:
            with open(os.path.join(out, "chain_state.json")) as f:
                cst = json.load(f)
        except (OSError, ValueError):
            pass
        sales, exports = chain_mod.history_garments(((planner.load_json("config.json").get("chain") or {}).get("sales_window")) or 12)
        drip = (((p.get("builds") or {}).get("drip")) or {}).get("labour", 0)
        p["chain"] = chain_mod.plan_chain(snap, planner.load_json("config.json"), planner.load_json("data/recipes.json"),
                                          last_mode=cst.get("mode"), sales=sales, exports=exports, drip=drip)
    except Exception as e:
        p["chain"] = {"ok": False, "why": "chain plan failed: %s: %s" % (type(e).__name__, e)}
    try:        # goal planner (v2/goal.py, Oct 23): business value, one LP; shadow only until goal.live
        import goal as goal_mod
        cfg_all = planner.load_json("config.json")
        ghist = goal_mod.read_history()
        import routes as routes_mod
        world = _WORLD.get("w")
        sea = None
        try:
            sea = routes_mod.load_sea()
        except Exception:
            pass
        rec_all = planner.load_json("data/recipes.json")
        mem_path = os.path.join(out, "goal_coef.json")
        try:
            with open(mem_path) as f:
                mem = json.load(f)
        except (OSError, ValueError):
            mem = {}
        mem = goal_mod.coef_memory(snap, rec_all, mem)
        if not replay:
            with open(mem_path, "w") as f:
                json.dump(mem, f, indent=1)
        G = goal_mod.plan_goal(snap, cfg_all, rec_all,
                               drip=((p.get("builds") or {}).get("drip")) or {}, hist=ghist,
                               buildings_data=planner.load_json("data/buildings.json"), world=world, sea=sea,
                               memory=mem)
        import goal_switch
        gh_path = os.path.join(out, "goal_history.jsonl")
        gh = []
        try:
            with open(gh_path) as f:
                gh = [json.loads(x) for x in f if x.strip()]
        except (OSError, ValueError):
            pass
        G["scorecard"] = goal_mod.scorecard(gh, ghist, set(cfg_all.get("perishable") or []))
        if not replay:
            G["promoted"] = goal_switch.promote(cfg_all, gh, G["scorecard"], snap.get("turn"))
        G["live_jobs"] = {j: goal_switch.owns(j, cfg_all) for j in goal_switch.JOBS}
        G["goal_orders"], G["orders_live"] = goal_mod.apply_orders(G, p, cfg_all)
        p["goal"] = G
        with open(os.path.join(out, "goal.json"), "w") as f:
            json.dump(G, f, indent=1, default=float)
        if not replay:
            with open(gh_path, "a") as f:
                f.write(json.dumps(goal_mod.history_line(G), default=float) + "\n")
    except Exception as e:
        import traceback
        tb = traceback.format_exc().strip().splitlines()
        p["goal"] = {"ok": False, "why": "goal plan failed: %s: %s" % (type(e).__name__, e), "trace": tb[-6:]}
        try:            # a failed run still says so in goal.json (it used to keep the last good plan and look fine)
            with open(os.path.join(out, "goal.json"), "w") as f:
                json.dump(p["goal"], f, indent=1)
        except OSError:
            pass
    if not replay:
        with open(os.path.join(out, "snapshot.json"), "w") as f:
            json.dump(snap, f, separators=(",", ":"), default=str)
    with open(os.path.join(out, "plan.json"), "w") as f:
        json.dump(p, f, indent=1, default=str)
    p["_items"] = {k: v for k, v in ((snap.get("store") or {}).get("items") or {}).items() if k in (p.get("live_items") or [])}
    with open(os.path.join(out, "report.md"), "w") as f:
        f.write(report(p))
        try:
            import goal as goal_mod
            f.write("\n" + "\n".join(goal_mod.report_lines(p.get("goal"))) + "\n")
        except Exception:
            pass
        try:
            import chain as chain_mod
            f.write("\n" + "\n".join(chain_mod.report_lines(p.get("chain"))) + "\n")
        except Exception:
            pass
    if not replay:      # a replay is not a new run: it must not add a line to the history
        line = {"t": p.get("t"), "turn": p.get("turn"), "cash": p.get("cash"), "counts": p.get("counts"),
                "top": [(f["severity"], f["item"], f["text"][:80]) for f in (p.get("flags") or [])[:5]],
                "keys": ["%s:%s" % (f["severity"], f["item"]) for f in (p.get("flags") or [])],   # persistence = real, one-offs = noise
                "builds": {st["building"]: st["progress"] for st in ((p.get("builds") or {}).get("sites") or [])},   # checks the progress model
                "api": (snap.get("api") or {}).get("calls"),
                # what the ships' routes really sold abroad last turn (chain_balancer averages this for sewing)
                "exports": _route_exports(snap),
                # what the ship plans offered abroad this run (export_first holds the home cut to real exports)
                "offers": p.get("export_offers") or {},
                # projected vs really used labour (labour_bias trims the buy by the median gap)
                "labour": dict(zip(("proj", "used", "short"), labour_numbers(snap)))}
        with open(os.path.join(OUT, "history.jsonl"), "a") as f:
            f.write(json.dumps(line, default=str) + "\n")
    c = p["counts"]
    print("v2 shadow: turn %s, %d risks, %d waste, %d tuning; %d GETs, %d API errors" % (
        p.get("turn"), c["risk"], c["waste"], c["tune"], api.calls["GET"], len(api.errors)))
    for f in (p.get("flags") or [])[:8]:
        print("  [%s] %s: %s" % (f["severity"], f["item"], f["text"]))


if __name__ == "__main__":
    main()
