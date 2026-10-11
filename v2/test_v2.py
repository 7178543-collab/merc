#!/usr/bin/env python3
"""Bot v2 checks. Plain asserts, no dependencies:  python v2/test_v2.py

Runs the planner on a frozen snapshot (v2/fixtures/), so the hourly job overwriting state/v2 can't change the result.
Also guards the one rule that matters: shadow mode never writes to the game.
"""
import ast
import copy
import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import api        # noqa: E402
import planner    # noqa: E402

SNAP = json.load(open(os.path.join(HERE, "fixtures", "snapshot_2026-10-11.json")))
CFG = json.load(open(os.path.join(HERE, "config.json")))


def keys(p):
    return {"%s:%s" % (f["severity"], f["item"]) for f in p["flags"]}


def test_read_only():
    assert CFG["mode"] == "shadow"
    for path in glob.glob(os.path.join(HERE, "*.py")):
        if os.path.basename(path) in ("api.py", "test_v2.py"):
            continue
        for node in ast.walk(ast.parse(open(path).read())):       # real calls only, not mentions in comments or docstrings
            if isinstance(node, ast.Call):
                fn = node.func
                assert getattr(fn, "attr", getattr(fn, "id", None)) != "allow_writes", "%s enables writes" % path
    ok, status, msg = api.write("PUT", "/anything", {})
    assert not ok and api.calls["write"] == 0, "api.write must refuse in shadow mode"


def test_false_flags_cut():
    p = planner.plan(SNAP, CFG)
    k = keys(p)
    # one root cause, one flag: porterage stalls the farm, camp and pit, and the knock-on is folded into it
    assert [f["item"] for f in p["flags"] if f["severity"] == "risk"] == ["porterage"], k
    assert p["stalls"]["porterage"]["knock_on"] == ["spinnery 1"]
    # not flagged any more: arms has a standing price-only buy; buffers/labour/porterage-waste were knock-ons;
    # nets sell above realized cost and timber isn't selling; fish/meat/grain/donations/firewood/tar are in equilibrium
    for gone in ("risk:arms", "risk:flax fibres", "risk:thread", "risk:labour", "waste:nets", "waste:timber", "waste:porterage",
                 "tune:donations", "tune:firewood", "tune:fish", "tune:grain", "tune:meat", "tune:tar"):
        assert gone not in k, gone
    # still flagged because they are real: garments really sell below what they cost us
    assert "waste:garments" in k and "waste:labour" in k
    assert p["counts"]["risk"] + p["counts"]["waste"] + p["counts"]["tune"] <= 5


def test_orders_sane():
    o = planner.plan(SNAP, CFG)["orders"]
    assert o["donations"]["buy"]["buy_volume"] == 40          # a deep market needs no runway
    assert "tar" not in o                                     # 97 turns in stock: no order
    assert o["labour"]["buy"]["buy_volume"] < 500             # stalled buildings no longer counted as running


def test_builds_now():
    b = planner.plan(SNAP, CFG)["builds"]
    r = {st["building"]: st["remaining"] for st in b["sites"]}
    assert r["ropewalk 1"] == {"labour": 284, "timber": 185, "tools": 15, "wheels": 12}      # 71% of the full cost
    assert r["quarry 1"]["labour"] == 536 and "wheels" not in r["quarry 1"]
    assert b["buys"]["wheels"]["action"] == "off" and b["buys"]["wheels"]["switch_off"]       # 13 held vs 12 needed: buy off
    assert b["buys"]["timber"]["action"] == "blocked"                                         # ask 9.15 > ceiling 8.60
    assert b["drip"] == {} and b["ready"] == []                                              # no labour until materials are in


def test_builds_ready_meters_labour():
    s = copy.deepcopy(SNAP)
    s["store"]["items"]["timber"]["held"] = 600
    base = planner.plan(SNAP, CFG)["orders"]["labour"]["buy"]["buy_volume"]
    p = planner.plan(s, CFG)
    assert sorted(p["builds"]["ready"]) == ["quarry 1", "ropewalk 1"]
    assert p["builds"]["drip"] == {"labour": 16 + 42}                                        # 284/18 + 536/13, per turn, not 820 at once
    assert p["orders"]["labour"]["buy"]["buy_volume"] > base


def test_builds_cash_guard():
    s = copy.deepcopy(SNAP)
    s["cash"] = 4100                                                                          # 100 above the reserve
    s["market"]["timber"]["ask"] = 8.0
    e = planner.plan(s, CFG)["builds"]["buys"]["timber"]
    assert e["action"] == "buy" and 0 < e["buy_volume"] <= 12 < e["deficit"] and "cash guard" in e["why"]


if __name__ == "__main__":
    n = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            n += 1
            print("ok", name)
    print("%d checks passed" % n)
