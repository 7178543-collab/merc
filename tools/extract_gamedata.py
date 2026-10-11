#!/usr/bin/env python3
"""Extract recipe and building definitions from the game's saved main bundle (state/dump/js,
written by tools/probe.py --mainjs) into v2/data/recipes.json and v2/data/buildings.json.
Re-run after a game update (the bundle name changes):  python tools/extract_gamedata.py"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JS = os.path.join(HERE, "state", "dump", "js")
OUT = os.path.join(HERE, "v2", "data")


def objects(txt, pattern):
    """Yield each balanced {...} JSON object starting where pattern matches."""
    for m in re.finditer(pattern, txt):
        i, depth, j, instr, esc = m.start(), 0, m.start(), False, False
        while j < len(txt):
            c = txt[j]
            if instr:
                if esc:
                    esc = False
                elif c == "\\":
                    esc = True
                elif c == '"':
                    instr = False
            elif c == '"':
                instr = True
            elif c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        try:
            yield json.loads(txt[i:j + 1])
        except ValueError:
            continue


def main():
    files = [os.path.join(JS, f) for f in os.listdir(JS)] if os.path.isdir(JS) else []
    txt = "".join(open(f, encoding="utf-8", errors="ignore").read() for f in files)
    if not txt:
        sys.exit("no bundle in %s (run tools/probe.py --mainjs via the probe workflow)" % JS)
    recipes = {}
    for r in objects(txt, r'\{"name":"[^"]+","tier":\d'):
        if "site" in r and "inputs" in r:
            recipes.setdefault(r["name"], r)
    buildings = {}
    for b in objects(txt, r'\{"type":"[^"]+","(?:requires|supports_boost|prestige|capacity|tenants|construction)'):
        if "type" in b and ("construction" in b or "requires" in b):
            buildings.setdefault(b["type"], b)
    os.makedirs(OUT, exist_ok=True)
    for name, data in (("recipes.json", recipes), ("buildings.json", buildings)):
        with open(os.path.join(OUT, name), "w") as f:
            json.dump(data, f, indent=0, sort_keys=True)
    print("recipes %d, buildings %d -> %s" % (len(recipes), len(buildings), OUT))


if __name__ == "__main__":
    main()
