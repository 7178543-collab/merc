#!/usr/bin/env python3
"""Goal planner checks. Plain asserts:  python v2/test_goal.py   (needs scipy; goal.py installs it if missing)

Small made-up businesses pin down the rules that matter, then the frozen Oct 23 snapshot checks the real model runs.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import goal  # noqa: E402

RECIPES = {
    "make widgets": {"inputs": [{"product": "labour", "amount": 10}], "outputs": [{"product": "widgets", "amount": 1}]},
    "hold feast": {"inputs": [{"product": "labour", "amount": 20}], "prestige": 1.0},
}
CFG = {"perishable": ["labour"], "goal": {"building_tax": 0}}


def snap(**kw):
    s = {
        "turn": 100, "t": "2026-10-23T00:00:00Z", "cash": 20000,
        "household": {"free": 1000, "impacts": {"to legacy": -1.0, "sustenance": 1.0}, "levels": {"tenants": 12}},
        "household_duty": {},
        "sustenance": {},
        "buildings": [
            {"id": "1", "type": "farmstead", "name": "farmstead", "size": 50, "recipe": "service 1", "target": 50,
             "production": 50, "flows": {"labour": {"production": 500}}},
            {"id": "2", "type": "workshop", "name": "workshop", "size": 100, "recipe": "make widgets", "target": 5,
             "production": 0},
            {"id": "3", "type": "mansion", "name": "mansion", "size": 1, "recipe": "hold feast", "target": 0,
             "production": 0},
        ],
        "operations": {},
        "ships": [],
        "store": {"items": {
            "labour": {"held": 0, "unit_cost": 2.0, "orders": []},
            "widgets": {"held": 0, "unit_cost": 15, "capacity": 0, "orders": [{"sell_price": "30"}]},
        }},
        "market": {
            "labour": {"price": 2.0, "ask": 2.0, "ask_vol": 5000, "traded": 5000},
            "widgets": {"price": 30.0, "traded": 0},
        },
    }
    s.update(kw)
    return s


def hist_selling(item, per_turn, n=24):
    return [{"turn": i, "cash": 0, "items": {item: [0, 0, 0, per_turn, 0, 0, 30.0]}} for i in range(n)]


def test_labour_is_netted_against_own_labour_and_builds():
    """The Oct 22 overbuy: a build site's labour plus the chain must be netted against own labour, never added on top."""
    h = hist_selling("widgets", 20)
    G = goal.plan_goal(snap(), CFG, RECIPES, drip={"labour": 100}, hist=h)
    assert G["ok"], G
    # 20 widgets x 10 labour + 100 for the site = 300, all covered by 500 own labour: buy nothing
    assert G["levels"]["workshop"] == 20, G["levels"]
    assert G["buy"].get("labour", 0) == 0, G["buy"]
    G = goal.plan_goal(snap(), CFG, RECIPES, drip={"labour": 450}, hist=h)
    # 200 + 450 = 650 needed, 500 own: buy exactly 150 (widgets pay 30 for 20 of labour)
    assert abs(G["buy"]["labour"] - 150) < 1e-6, G["buy"]


def test_never_makes_what_does_not_sell():
    """Unsold output counts for nothing (no bin space here), so production stops at what the market takes."""
    G = goal.plan_goal(snap(), CFG, RECIPES, hist=hist_selling("widgets", 7))
    assert abs(G["levels"]["workshop"] - 7) < 1e-6, G["levels"]


def test_prestige_floor_buys_the_cheapest_prestige():
    """Free prestige under the floor: the plan must climb back, paying for it with the feast."""
    s = snap(household={"free": 250, "impacts": {"to legacy": -1.0}, "levels": {"tenants": 12}})
    s["buildings"][2]["size"] = 5
    G = goal.plan_goal(s, CFG, RECIPES, hist=hist_selling("widgets", 5))
    need = (300 - 250) / 24.0 + 1.0          # recover to the floor over 24 turns, on top of the legacy drain
    assert abs(G["levels"]["mansion"] - need) < 1e-3, (G["levels"], need)
    assert G["plan_prestige_rate"] >= G["prestige_min"] - 1e-9 and not G["relaxed"]
    # a floor it can't reach: it still gets as close as it can, and says so
    s["buildings"][2]["size"] = 1
    G = goal.plan_goal(s, CFG, RECIPES, hist=hist_selling("widgets", 5))
    assert G["levels"]["mansion"] == 1 and "prestige floor" in G["relaxed"], (G["levels"], G["relaxed"])


def test_cash_floor_forces_cash_back():
    """Under the cash floor the plan must earn cash back; impossible floors are reported, never ignored silently."""
    s = snap(cash=1000)
    s["buildings"] = s["buildings"][1:]       # no own labour to sell off
    G = goal.plan_goal(s, CFG, RECIPES, hist=hist_selling("widgets", 1))
    # needs (4000 - 1000) / 24 = 125/turn; one widget a turn can't do it
    assert "cash floor" in G["relaxed"], G["relaxed"]


def test_reserves_are_never_drawn():
    s = snap()
    s["store"]["items"]["tools"] = {"held": 130, "unit_cost": 5, "capacity": 200, "orders": []}
    s["market"]["tools"] = {"price": 5.0, "traded": 100}
    G = goal.plan_goal(s, CFG, RECIPES, hist=hist_selling("widgets", 5))
    # Taylor's tools stockpile: 100 kept, so at most 30 over 12 turns may be drawn
    drawn = (G["flows"].get("tools") or {}).get("draw", 0)
    assert drawn <= 30 / 12.0 + 1e-6, G["flows"].get("tools")


def test_real_snapshot_plans_and_explains():
    s = json.load(open(os.path.join(HERE, "fixtures", "snapshot_2026-10-23.json")))
    cfg = json.load(open(os.path.join(HERE, "config.json")))
    rec = json.load(open(os.path.join(HERE, "data", "recipes.json")))
    bd = json.load(open(os.path.join(HERE, "data", "buildings.json")))
    G = goal.plan_goal(s, cfg, rec, hist=[], buildings_data=bd)
    assert G["ok"], G
    assert G["plan_value"] is not None and G["current_value"] is not None
    # the gains of the changes add up to plan - today (limits aside), so every coin of the difference is explained
    total = sum(ch["gain"] for ch in G["changes"] if ch.get("gain") is not None)
    fixed = goal.solve(goal.build_model(s, cfg, rec, hist=[]), fix=G["levels"], prestige_min=-1e9, cash_min=None)
    assert abs(total - (fixed["value"] - G["current_value"])) < 1.0, (total, fixed["value"], G["current_value"])
    # duty never planned over the workers' own labour
    assert G["levels"]["household duty"] <= 2.0 + 1e-6
    assert any("Goal" in line for line in goal.report_lines(G))


if __name__ == "__main__":
    n = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            n += 1
            print("ok", name)
    print("%d checks passed" % n)
