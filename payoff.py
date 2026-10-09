#!/usr/bin/env python3
"""Payoff check (Oct 9 2026): did each change actually pay?

The queue and the rules verify that a change LANDED in the game; this checks whether it HELPED.
For every applied change in state/order_queue_done.jsonl (queue, rules, manual) that is at least
WINDOW turns old, compare the WINDOW turns before it with the WINDOW turns after it:
  - profit per turn (whole business)
  - for the item it touched: sold, made, held at the end
  - prestige income per turn
Verdict: better / worse / flat (profit moved less than 10% or 50 coin a turn). Profit is noisy and
many things change at once, so treat a verdict as a flag to look at, not proof.

Writes state/payoff.json (all evaluated changes, newest first) and state/payoff_report.txt
(the last 10, plain text). No game calls: history files only.

    python payoff.py
"""
import datetime
import glob
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
DONE = os.path.join(HERE, "state", "order_queue_done.jsonl")
OUT = os.path.join(HERE, "state", "payoff.json")
REPORT = os.path.join(HERE, "state", "payoff_report.txt")
WINDOW = 6


def history():
    rows = {}
    for p in sorted(glob.glob(os.path.join(HERE, "history", "merc-*.jsonl"))):
        for line in open(p):
            try:
                d = json.loads(line)
            except ValueError:
                continue
            if "turn" in d and "items" in d and d.get("t"):
                rows[d["turn"]] = d      # last snapshot of each turn wins
    return rows


def ts(s):
    return datetime.datetime.fromisoformat(s.replace("Z", "+00:00"))


def turn_at(rows, when):
    """First turn whose snapshot is at or after the change time."""
    for t in sorted(rows):
        if ts(rows[t]["t"]) >= when:
            return t
    return None


def avg(xs):
    xs = [x for x in xs if x is not None]
    return sum(xs) / len(xs) if xs else None


def label(e):
    if e.get("producer"):
        p = e["producer"]
        return "building %s: %s x%s" % (e.get("building"), p.get("recipe") or "", p.get("target"))
    if e.get("prestige"):
        return "prestige buy: %s" % e["prestige"]
    if "operation_target" in e:
        return "ship %s operation %s" % (e.get("transport"), e["operation_target"])
    where = "ship %s " % e["transport"] if e.get("transport") else ""
    what = e.get("set") or ({"capacity": e["capacity"]} if e.get("capacity") is not None else {})
    return "%s%s %s" % (where, e.get("item"), json.dumps(what))


def main():
    rows = history()
    if not rows:
        return
    turns = sorted(rows)
    now = turns[-1]
    out = []
    try:
        lines = open(DONE).read().splitlines()
    except FileNotFoundError:
        lines = []
    for ln in lines:
        try:
            r = json.loads(ln)
        except ValueError:
            continue
        if not r.get("ok"):
            continue
        e = r.get("entry") or {}
        t0 = turn_at(rows, ts(r["ts"]))
        if t0 is None or now < t0 + WINDOW:
            continue
        before = [rows[t] for t in turns if t0 - WINDOW <= t < t0]
        after = [rows[t] for t in turns if t0 < t <= t0 + WINDOW]
        if len(before) < WINDOW // 2 or len(after) < WINDOW // 2:
            continue
        pb, pa = avg([x.get("profit") for x in before]), avg([x.get("profit") for x in after])
        rb, ra = avg([x.get("prestige_rate") for x in before]), avg([x.get("prestige_rate") for x in after])
        rec = dict(when=r["ts"], turn=t0, source=r.get("source", "queue"), change=label(e),
                   note=e.get("note"), profit_before=round(pb or 0), profit_after=round(pa or 0),
                   prestige_rate_before=round(rb or 0, 2), prestige_rate_after=round(ra or 0, 2))
        item = e.get("item")
        if item:
            def col(rs, i):
                return avg([(x["items"].get(item) or [None] * 7)[i] for x in rs])
            rec.update(item=item, sold_before=round(col(before, 3) or 0, 1), sold_after=round(col(after, 3) or 0, 1),
                       made_before=round(col(before, 1) or 0, 1), made_after=round(col(after, 1) or 0, 1),
                       held_end=round((after[-1]["items"].get(item) or [0])[0], 1))
        d = (pa or 0) - (pb or 0)
        rec["verdict"] = "flat" if abs(d) < max(50, 0.1 * abs(pb or 0)) else ("better" if d > 0 else "worse")
        out.append(rec)
    out.sort(key=lambda x: x["when"], reverse=True)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(out, f, indent=1)
    with open(REPORT, "w") as f:
        f.write("Payoff of applied changes (%d turns before vs after; profit is noisy, read as a flag)\n" % WINDOW)
        for x in out[:10]:
            f.write("- %s turn %s %s [%s]: profit %+d -> %+d/turn, prestige %+.2f -> %+.2f/turn%s\n" % (
                x["when"][:16], x["turn"], x["change"], x["verdict"], x["profit_before"], x["profit_after"],
                x["prestige_rate_before"], x["prestige_rate_after"],
                ("; %s sold %.1f -> %.1f, made %.1f -> %.1f, held %.0f" % (
                    x["item"], x["sold_before"], x["sold_after"], x["made_before"], x["made_after"], x["held_end"]))
                if x.get("item") else ""))
    print(open(REPORT).read())


if __name__ == "__main__":
    main()
