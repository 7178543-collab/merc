#!/usr/bin/env python3
"""Sea path finder for ships (same rules as the game's own client: A*, 8 directions, step cost 1 / 1.414).

Reads a grid written by the queue's {"seamap": {...}} entry (state/seamap/*.json; '1' = sea, '0' = land)
and returns a path in the format POST /transports/{id}/travel expects:
    [{"x": 1523, "y": 2387, "c": "0"}, {"x": 1524, "y": 2386, "c": "1.414"}, ...]

Usage:
    python tools/seapath.py --validate            # re-derive the Flax Wyrm's stored Blanans path and compare cost
    python tools/seapath.py X0 Y0 X1 Y1           # path between two sea tiles, prints length and cost
Read-only: never talks to the game.
"""
import glob
import heapq
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SQRT2 = 1.414  # the game rounds the diagonal step to 3 places ("c": "1.414")


class SeaGrid:
    def __init__(self, x0, y0, rows):
        self.x0, self.y0, self.rows = x0, y0, rows
        self.h, self.w = len(rows), len(rows[0]) if rows else 0

    @classmethod
    def load(cls, pattern=None):
        """Merge every state/seamap/*.json into one grid (later files fill gaps; land if unknown)."""
        files = sorted(glob.glob(pattern or os.path.join(ROOT, "state", "seamap", "seamap_*.json")))
        if not files:
            raise SystemExit("no seamap files; queue a {\"seamap\": {...}} entry first")
        parts = [json.load(open(f)) for f in files]
        x0 = min(p["x0"] for p in parts)
        y0 = min(p["y0"] for p in parts)
        x1 = max(p["x0"] + p["w"] for p in parts)
        y1 = max(p["y0"] + p["h"] for p in parts)
        rows = [bytearray(b"0" * (x1 - x0)) for _ in range(y1 - y0)]
        for p in parts:
            for j, r in enumerate(p["rows"]):
                row = rows[p["y0"] - y0 + j]
                for i, ch in enumerate(r):
                    if ch == "1":
                        row[p["x0"] - x0 + i] = 49
        return cls(x0, y0, [bytes(r).decode() for r in rows])

    def sea(self, x, y):
        i, j = x - self.x0, y - self.y0
        return 0 <= i < self.w and 0 <= j < self.h and self.rows[j][i] == "1"


def find_path(grid, start, end):
    """Optimal sea path (octile-distance A*). Returns (path, cost) or (None, None)."""
    (sx, sy), (ex, ey) = start, end
    if not grid.sea(sx, sy) or not grid.sea(ex, ey):
        return None, None
    D, D2 = 1.0, SQRT2

    def h(x, y):
        dx, dy = abs(x - ex), abs(y - ey)
        return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)

    best = {(sx, sy): 0.0}
    prev = {}
    heap = [(h(sx, sy), 0.0, sx, sy)]
    while heap:
        _, g, x, y = heapq.heappop(heap)
        if (x, y) == (ex, ey):
            break
        if g > best.get((x, y), math.inf):
            continue
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if not grid.sea(nx, ny):
                    continue
                ng = g + (D2 if dx and dy else D)
                if ng < best.get((nx, ny), math.inf):
                    best[(nx, ny)] = ng
                    prev[(nx, ny)] = (x, y)
                    heapq.heappush(heap, (ng + h(nx, ny), ng, nx, ny))
    if (ex, ey) not in best:
        return None, None
    tiles = [(ex, ey)]
    while tiles[-1] != (sx, sy):
        tiles.append(prev[tiles[-1]])
    tiles.reverse()
    path, last = [], None
    for x, y in tiles:
        step = 0 if last is None else (SQRT2 if (x != last[0] and y != last[1]) else 1)
        path.append({"x": x, "y": y, "c": ("%g" % step)})
        last = (x, y)
    return path, best[(ex, ey)]


def path_cost(path):
    return sum(float(p["c"]) for p in path)


def validate():
    t = json.load(open(os.path.join(ROOT, "state", "dump", "api", "transports_845668271.json")))
    stored = t["journey"]["legs"][0]["path"]
    s, e = (stored[0]["x"], stored[0]["y"]), (stored[-1]["x"], stored[-1]["y"])
    grid = SeaGrid.load()
    bad = [(p["x"], p["y"]) for p in stored if not grid.sea(p["x"], p["y"])]
    print("stored path: %d tiles, cost %.3f, %s -> %s" % (len(stored), path_cost(stored), s, e))
    print("stored tiles that are NOT sea in my grid: %d %s" % (len(bad), bad[:5]))
    mine, cost = find_path(grid, s, e)
    if not mine:
        print("my A*: no path found")
        return 1
    print("my A*:       %d tiles, cost %.3f" % (len(mine), cost))
    diff = abs(cost - path_cost(stored))
    print("cost difference %.3f -> %s" % (diff, "MATCH" if diff < 0.01 and not bad else "CHECK"))
    return 0 if diff < 0.01 and not bad else 1


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "--validate":
        sys.exit(validate())
    if len(sys.argv) == 5:
        a = list(map(int, sys.argv[1:]))
        p, c = find_path(SeaGrid.load(), (a[0], a[1]), (a[2], a[3]))
        print("no path" if not p else "%d tiles, cost %.3f" % (len(p), c))
        sys.exit(0 if p else 1)
    print(__doc__)
