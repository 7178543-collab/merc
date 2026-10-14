#!/usr/bin/env python3
"""Season 9 turn-1 town test (handoff doc, "Season 9 plan" tab), as code.

Ranks every town using only what exists before anyone trades, so it works on turn 1 of a new map:

  Gates (a town that fails one is listed but not picked)
    mainland     the town's landmass (connected land on the sea grid) holds at least MAINLAND_MIN towns
    no rival     no other household runs RIVAL_MAX or more textile buildings in town (flax farm .. sewing shop);
                 on turn 1 nobody has built yet, so this gate matters at the ~48-turn re-check
    room         at least FREE_MIN unowned domain tiles to build on

  Score (higher is better; each part is shown in the report so the weights can be argued with)
    households   log(1 + households in town): players pick towns, and this season town size followed the number of
                 players (correlation 0.73), not geography (0.28)
    cluster      log(1 + towns on the same landmass within NEAR tiles): export buyers by road
    free land    share of the domain still unowned
    capital      a small bonus for a regional capital

Data:
  queue entry {"town_pick": {}}   the order-queue workflow GETs /towns and /towns/{id} for every town and writes the
                                  compact state/town_pick_data.json plus the ranking in state/town_pick.md
  python tools/town_pick.py       re-rank offline from state/town_pick_data.json (no API)
  python tools/town_pick.py --check   also compare with today's town sizes (commoners) to see how the test does

The landmass needs the sea grid in state/seamap (queue {"seamap": ...} entries). On a new map, refresh it first:
an old grid would put towns on the wrong landmass.
Read-only: never writes to the game.
"""
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, "state", "town_pick_data.json")
REPORT = os.path.join(ROOT, "state", "town_pick.md")

MAINLAND_MIN = 4       # towns on one landmass for it to count as mainland
NEAR = 200             # tiles: a neighbour for the cluster score
RIVAL_MAX = 3          # textile buildings (not plots) one other household runs in town = a rival (a full chain is 5)
FREE_MIN = 40          # unowned domain tiles needed to build a chain
TEXTILE = ("flax farm", "retting pit", "spinnery", "weavery", "sewing shop")
OUR_HOUSEHOLD_OWNER = None   # set to our owner id to leave our own buildings out of the rival count (not needed on turn 1)


# ---------------------------------------------------------------- collect (API, run by the order-queue workflow)
def collect(get):
    """GET /towns and /towns/{id} for every town; return the compact per-town rows (no domain tile lists)."""
    towns = get("/towns") or []
    rows = []
    for t in towns:
        tid = str(t.get("id"))
        d = get("/towns/%s" % tid) or {}
        dom = d.get("domain") or {}
        owners, structs, seen = {}, {}, set()
        free = resource = 0
        for tile in dom.values():
            o = tile.get("owner_id")
            if not o:
                free += 1
            if tile.get("resource"):
                resource += 1
            sd = tile.get("structure") or {}
            st, sid = sd.get("type"), sd.get("id")
            if st and o and sid not in seen:        # a building spans one tile per plot: count each building once
                seen.add(sid)
                structs[st] = structs.get(st, 0) + 1
                if st in TEXTILE:
                    owners[str(o)] = owners.get(str(o), 0) + 1
        loc = t.get("location") or d.get("location") or {}
        rows.append({
            "id": tid, "name": t.get("name") or d.get("name"), "x": loc.get("x"), "y": loc.get("y"),
            "region": t.get("region") or d.get("region"), "capital": bool(t.get("capital")),
            "commoners": t.get("commoners") if not isinstance(t.get("commoners"), dict) else (t["commoners"] or {}).get("count"),
            "population": ((d.get("state") or {}).get("population")),
            "households": len(d.get("household_ids") or []),
            "tiles": len(dom), "free": free, "resource_tiles": resource,
            "textile_by_owner": owners, "structures": structs,
            "centre_plots": len(d.get("center_ids") or []),
        })
    return rows


# ---------------------------------------------------------------- landmasses from the sea grid
def landmasses(grid):
    """Label connected land (4-neighbour) on a SeaGrid; returns a function (x, y) -> landmass id (None on sea).
    Works on runs of land per row with union-find, so it handles the whole map in pure Python."""
    parent = {}

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    runs_by_row = []
    nid = 0
    for j, row in enumerate(grid.rows):
        runs, i, w = [], 0, len(row)
        while i < w:
            if row[i] == "0":
                k = i
                while k < w and row[k] == "0":
                    k += 1
                parent[nid] = nid
                runs.append((i, k - 1, nid))
                nid += 1
                i = k
            else:
                i += 1
        if j:
            prev, a = runs_by_row[-1], 0
            for (s, e, r) in runs:
                while a < len(prev) and prev[a][1] < s:
                    a += 1
                b = a
                while b < len(prev) and prev[b][0] <= e:
                    union(prev[b][2], r)
                    b += 1
        runs_by_row.append(runs)

    def at(x, y):
        i, j = x - grid.x0, y - grid.y0
        if not (0 <= j < len(runs_by_row)):
            return None
        for s, e, r in runs_by_row[j]:
            if s <= i <= e:
                return find(r)
        return None
    return at


def town_landmass(at, x, y):
    """A town's tile can sit on the coast; look at the town tile, then its 8 neighbours, for land."""
    for dx, dy in ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)):
        lm = at(x + dx, y + dy)
        if lm is not None:
            return lm
    return None


# ---------------------------------------------------------------- rank
def rank(rows, at=None):
    lm = {}
    for r in rows:
        lm[r["id"]] = town_landmass(at, int(r["x"]), int(r["y"])) if at and r.get("x") is not None else None
    per_lm = {}
    for tid, k in lm.items():
        per_lm[k] = per_lm.get(k, 0) + 1
    out = []
    for r in rows:
        k = lm[r["id"]]
        mates = per_lm.get(k, 1) if k is not None else None
        near = sum(1 for o in rows if o["id"] != r["id"] and lm[o["id"]] == k and k is not None
                   and math.hypot(o["x"] - r["x"], o["y"] - r["y"]) <= NEAR)
        rival = max([n for o, n in (r.get("textile_by_owner") or {}).items() if o != OUR_HOUSEHOLD_OWNER] + [0])
        free_share = r["free"] / r["tiles"] if r.get("tiles") else 0.0
        parts = {"households": round(math.log1p(r.get("households") or 0), 2),
                 "cluster": round(0.6 * math.log1p(near), 2),
                 "free land": round(free_share, 2),
                 "capital": 0.2 if r.get("capital") else 0.0}
        fails = []
        if mates is not None and mates < MAINLAND_MIN:
            fails.append("island (%d town%s on its landmass)" % (mates, "" if mates == 1 else "s"))
        if mates is None:
            fails.append("landmass unknown (no sea grid)")
        if rival >= RIVAL_MAX:
            fails.append("textile rival (%d buildings)" % rival)
        if (r.get("free") or 0) < FREE_MIN:
            fails.append("little free land (%d tiles)" % (r.get("free") or 0))
        out.append(dict(r, landmass=k, landmass_towns=mates, near=near, rival=rival, parts=parts,
                        score=round(sum(parts.values()), 2), fails=fails))
    out.sort(key=lambda x: (bool(x["fails"]), -x["score"]))
    return out


def spearman(a, b):
    def ranks(v):
        order = sorted(range(len(v)), key=lambda i: v[i])
        r = [0.0] * len(v)
        i = 0
        while i < len(order):
            j = i
            while j + 1 < len(order) and v[order[j + 1]] == v[order[i]]:
                j += 1
            for k in range(i, j + 1):
                r[order[k]] = (i + j) / 2.0
            i = j + 1
        return r
    ra, rb = ranks(a), ranks(b)
    n = len(a)
    ma, mb = sum(ra) / n, sum(rb) / n
    cov = sum((x - ma) * (y - mb) for x, y in zip(ra, rb))
    va = math.sqrt(sum((x - ma) ** 2 for x in ra))
    vb = math.sqrt(sum((y - mb) ** 2 for y in rb))
    return cov / (va * vb) if va and vb else 0.0


def report(ranked, check=False):
    L = ["# Town pick", "",
         "Turn-1 town test (Season 9 plan). Gates: mainland (%d+ towns on the landmass), no textile rival (%d+ "
         "buildings by one household), %d+ free tiles. Score = households + cluster + free land + capital." % (
             MAINLAND_MIN, RIVAL_MAX, FREE_MIN), "",
         "| # | Town | Score | Households | Near towns | Free tiles | Landmass towns | Fails |",
         "| --- | --- | --- | --- | --- | --- | --- | --- |"]
    for i, r in enumerate(ranked[:25], 1):
        L.append("| %d | %s | %.2f | %s | %s | %s/%s | %s | %s |" % (
            i, r["name"], r["score"], r.get("households"), r["near"], r.get("free"), r.get("tiles"),
            r["landmass_towns"], "; ".join(r["fails"]) or "-"))
    if check:
        live = [r for r in ranked if r.get("commoners") is not None]
        if len(live) > 5:
            geo = [r["parts"]["cluster"] + r["parts"]["free land"] + r["parts"]["capital"] for r in live]
            full = [r["score"] for r in live]
            size = [float(r["commoners"]) for r in live]
            L += ["", "## Check against this season's town sizes (commoners now)", "",
                  "- Geography only (cluster + free land + capital), the part that is known on turn 1: Spearman %.2f" %
                  spearman(geo, size),
                  "- Full score with today's household counts: Spearman %.2f (households are counted at the END of "
                  "the season here, so this flatters the test; on turn 1 they are the early sign-ups)" % spearman(full, size)]
            top = sorted(live, key=lambda r: -float(r["commoners"]))[:5]
            pos = {r["id"]: i for i, r in enumerate(ranked, 1)}
            L.append("- Biggest towns now and where the test puts them: " + ", ".join(
                "%s #%d" % (r["name"], pos[r["id"]]) for r in top))
    return "\n".join(L) + "\n"


def grid_or_none():
    try:
        sys.path.insert(0, HERE)
        import seapath
        return seapath.SeaGrid.load()
    except (Exception, SystemExit):
        return None


def run(rows, check=False):
    g = grid_or_none()
    ranked = rank(rows, landmasses(g) if g else None)
    text = report(ranked, check)
    with open(REPORT, "w") as f:
        f.write(text)
    return ranked, text


if __name__ == "__main__":
    with open(DATA) as f:
        rows = json.load(f)
    _, text = run(rows, check="--check" in sys.argv)
    print(text)
