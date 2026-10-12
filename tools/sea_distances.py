#!/usr/bin/env python3
"""Sea moves from our dock to every town's dock: one Dijkstra over the merged sea grid (state/seamap), same step costs
as the game (1 / 1.414). Writes state/v2/sea_routes.json for v2/routes.py. ~30 s for the whole map; rerun when the
map or the towns change (new season).

    python tools/sea_distances.py [HOME_X HOME_Y]      # default: Strasclives dock 1523 2387

A town's dock is the nearest sea tile reachable from home within 2 tiles of the town (the game's own dock is a
navigation_zones tile next to the town; checked: Blanans 296.8 vs the game's 297.2, Grandgues 151.7 vs 152.7).
"""
import heapq
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import seapath  # noqa: E402

NB = [(-1, -1, 1.414), (0, -1, 1), (1, -1, 1.414), (-1, 0, 1), (1, 0, 1), (-1, 1, 1.414), (0, 1, 1), (1, 1, 1.414)]


def main():
    hx, hy = (int(sys.argv[1]), int(sys.argv[2])) if len(sys.argv) == 3 else (1523, 2387)
    g = seapath.SeaGrid.load()
    W, H = g.w, g.h
    sea = bytearray(W * H)
    for j, r in enumerate(g.rows):
        b = r.encode()
        for i in range(W):
            if b[i] == 49:
                sea[j * W + i] = 1
    start = (hx - g.x0) + (hy - g.y0) * W
    dist = {start: 0.0}
    pq = [(0.0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist.get(u, 1e18):
            continue
        x, y = u % W, u // W
        for dx, dy, c in NB:
            nx, ny = x + dx, y + dy
            if 0 <= nx < W and 0 <= ny < H:
                v = ny * W + nx
                if sea[v] and d + c < dist.get(v, 1e18):
                    dist[v] = d + c
                    heapq.heappush(pq, (d + c, v))
    towns = json.load(open(os.path.join(ROOT, "state", "dump", "api", "towns.json")))
    out = {}
    for tw in towns:
        loc = tw["location"]
        if isinstance(loc, str):
            loc = json.loads(loc.replace("'", '"'))
        best = None
        for r in range(3):
            for dx in range(-r, r + 1):
                for dy in range(-r, r + 1):
                    if max(abs(dx), abs(dy)) != r:
                        continue
                    X, Y = loc["x"] + dx - g.x0, loc["y"] + dy - g.y0
                    v = Y * W + X
                    if 0 <= X < W and 0 <= Y < H and v in dist and (best is None or dist[v] < best[0]):
                        best = (dist[v], loc["x"] + dx, loc["y"] + dy)
            if best:
                break
        out[str(tw["id"])] = {"name": tw["name"], "loc": [loc["x"], loc["y"]], "dock": list(best[1:]) if best else None,
                              "moves": round(best[0], 3) if best else None}
    path = os.path.join(ROOT, "state", "v2", "sea_routes.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=0)
    print("%d of %d towns reachable by sea -> %s" % (sum(1 for v in out.values() if v["moves"] is not None), len(out), path))


if __name__ == "__main__":
    main()
