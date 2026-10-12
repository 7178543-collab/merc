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
    L += ["## v2 orders", "", "| Item | v2 buy | v2 sell | Why |", "| --- | --- | --- | --- |"]
    for item, o in sorted((p.get("orders") or {}).items()):
        b, s_ = o.get("buy"), o.get("sell")
        if not (b or s_):
            continue
        bt = ("%d @ %s, stop %s" % (b["buy_volume"], b.get("buy_price", "?"), b.get("max_holding", "-"))) if b else ""
        st = ("%d @ min %s" % (s_["sell_volume"], s_.get("sell_price"))) if s_ else ""
        L.append("| %s | %s | %s | %s |" % (item, bt, st, o.get("why", "")))
    return "\n".join(L) + "\n"


def main():
    if "--from" in sys.argv:
        with open(sys.argv[sys.argv.index("--from") + 1]) as f:
            snap = json.load(f)
    else:
        if not api.ready():
            print("v2 shadow: no credentials")
            return
        snap = snapshot.take()
    p = planner.plan(snap)
    replay = "--from" in sys.argv
    out = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else OUT
    os.makedirs(out, exist_ok=True)
    if not replay:
        with open(os.path.join(out, "snapshot.json"), "w") as f:
            json.dump(snap, f, separators=(",", ":"), default=str)
    with open(os.path.join(out, "plan.json"), "w") as f:
        json.dump(p, f, indent=1, default=str)
    with open(os.path.join(out, "report.md"), "w") as f:
        f.write(report(p))
    if not replay:      # a replay is not a new run: it must not add a line to the history
        line = {"t": p.get("t"), "turn": p.get("turn"), "cash": p.get("cash"), "counts": p.get("counts"),
                "top": [(f["severity"], f["item"], f["text"][:80]) for f in (p.get("flags") or [])[:5]],
                "keys": ["%s:%s" % (f["severity"], f["item"]) for f in (p.get("flags") or [])],   # persistence = real, one-offs = noise
                "builds": {st["building"]: st["progress"] for st in ((p.get("builds") or {}).get("sites") or [])},   # checks the progress model
                "api": (snap.get("api") or {}).get("calls")}
        with open(os.path.join(OUT, "history.jsonl"), "a") as f:
            f.write(json.dumps(line, default=str) + "\n")
    c = p["counts"]
    print("v2 shadow: turn %s, %d risks, %d waste, %d tuning; %d GETs, %d API errors" % (
        p.get("turn"), c["risk"], c["waste"], c["tune"], api.calls["GET"], len(api.errors)))
    for f in (p.get("flags") or [])[:8]:
        print("  [%s] %s: %s" % (f["severity"], f["item"], f["text"]))


if __name__ == "__main__":
    main()
