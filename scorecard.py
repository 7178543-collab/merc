#!/usr/bin/env python3
"""Daily scorecard: is the business getting better or worse?

Reads the bot's own history (history/merc-YYYY-MM.jsonl, one line per run),
takes the last 24 turns, compares them with the 24 before, and posts one
comment on the hourly status issue at most once every 24 hours.

    python scorecard.py            # print only
    python scorecard.py --live     # also post (if 24h since the last post)

Numbers:
  garments/turn   made per turn (uptime of the chain = how close to the best turn)
  waste           coin/turn thrown away: expired goods x price (labour at market)
  profit          trading profit per turn (sales - purchases, from the status line)
  cash            change over the window (includes construction, so it's cash flow)
  prestige        change over the window
  labour/garment  labour bought per garment made (lower = cheaper garments)
"""
import glob
import json
import os
import subprocess
import sys
import time

LIVE = "--live" in sys.argv
STATE = os.path.join("state", "scorecard.json")
WINDOW = 24


def load_history():
    rows = {}
    for path in sorted(glob.glob("history/merc-*.jsonl")):
        with open(path) as f:
            for line in f:
                try:
                    r = json.loads(line)
                except ValueError:
                    continue
                t = r.get("turn")
                if t is not None:
                    rows[t] = r          # last reading of each turn wins
    return [rows[t] for t in sorted(rows)]


def labour_price():
    try:
        import merc_status4 as m
        md = m.get("/towns/152202387/marketdata")
        md = md.get("markets", md)
        return float((md.get("labour") or {}).get("last_price") or 1.65)
    except Exception:
        return 1.65


def stats(rows, lab_price):
    if not rows:
        return None
    col = lambda r, item, i: float(((r.get("items") or {}).get(item) or [0] * 7)[i] or 0)
    n = len(rows)
    made = [col(r, "garments", 1) for r in rows]
    waste = 0.0
    for r in rows:
        for item, v in (r.get("items") or {}).items():
            exp = float(v[5] or 0) if len(v) > 5 else 0
            if exp:
                price = lab_price if item == "labour" else float(v[6] or 0)
                waste += exp * price
    lab_bought = sum(col(r, "labour", 4) for r in rows)
    return {
        "turns": n,
        "garments": sum(made) / n,
        "uptime": (sum(made) / n) / max(made) if max(made) else 0,
        "zero_turns": sum(1 for x in made if x < 1),
        "waste": waste / n,
        "profit": sum(float(r.get("profit") or 0) for r in rows) / n,
        "cash": float(rows[-1].get("cash") or 0) - float(rows[0].get("cash") or 0),
        "prestige": float(rows[-1].get("prestige") or 0) - float(rows[0].get("prestige") or 0),
        "lab_per_garment": lab_bought / sum(made) if sum(made) else 0,
    }


def arrow(new, old, good_up=True):
    if old is None:
        return ""
    d = new - old
    if abs(d) < 1e-9:
        return " (=)"
    better = (d > 0) == good_up
    return " (%s %+.1f)" % ("better" if better else "worse", d)


def main():
    rows = load_history()
    if len(rows) < 2:
        print("not enough history yet")
        return
    lp = labour_price()
    cur = stats(rows[-WINDOW:], lp)
    prev = stats(rows[-2 * WINDOW:-WINDOW], lp) if len(rows) >= WINDOW + WINDOW // 2 else None
    g = lambda k: prev[k] if prev else None
    lines = [
        "**Scorecard, last %d turns** (turn %s)" % (cur["turns"], rows[-1].get("turn")),
        "- Garments: %.1f/turn, uptime %.0f%%, %d turn(s) with none%s" % (
            cur["garments"], cur["uptime"] * 100, cur["zero_turns"], arrow(cur["garments"], g("garments"))),
        "- Waste: %.0f coin/turn (expired goods + labour)%s" % (cur["waste"], arrow(cur["waste"], g("waste"), good_up=False)),
        "- Trading profit: %+.0f/turn%s" % (cur["profit"], arrow(cur["profit"], g("profit"))),
        "- Cash: %+.0f over the window (includes builds)%s" % (cur["cash"], arrow(cur["cash"], g("cash"))),
        "- Prestige: %+.1f%s" % (cur["prestige"], arrow(cur["prestige"], g("prestige"))),
        "- Labour bought per garment: %.1f%s" % (cur["lab_per_garment"], arrow(cur["lab_per_garment"], g("lab_per_garment"), good_up=False)),
    ]
    if not prev:
        lines.append("_(no earlier window yet to compare against)_")
    text = "\n".join(lines)
    print(text)

    if not LIVE:
        return
    try:
        with open(STATE) as f:
            last = json.load(f).get("posted", 0)
    except (OSError, ValueError):
        last = 0
    if time.time() - last < 23.5 * 3600:
        print("posted within the last 24h: not posting")
        return
    r = subprocess.run(["gh", "issue", "list", "--label", "merc-status", "--state", "open", "--limit", "1",
                        "--json", "number"], capture_output=True, text=True)
    try:
        num = str(json.loads(r.stdout or "[]")[0]["number"])
    except (ValueError, IndexError, KeyError):
        num = "1"
    subprocess.run(["gh", "issue", "comment", num, "--body", text])
    os.makedirs("state", exist_ok=True)
    with open(STATE, "w") as f:
        json.dump({"posted": time.time()}, f)


if __name__ == "__main__":
    main()
