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
    assert abs(total - (G["plan_free"] - G["current_value"])) < 1.0, (total, G["plan_free"], G["current_value"])
    # duty never planned over the workers' own labour
    assert G["levels"]["household duty"] <= 2.0 + 1e-6
    assert any("Goal" in line for line in goal.report_lines(G))


def test_hand_over_one_job_at_a_time_and_back():
    import goal_switch
    import tempfile
    path = os.path.join(tempfile.mkdtemp(), "goal_live.json")
    cfg = {"goal": {"auto": True, "auto_promote": ["rates", "buys"], "hold_runs": 3, "drop_runs": 2,
                    "promote_gap_turns": 24}}
    good = {"turns": 24, "predicted": 50.0, "real": 60.0}
    bad = {"turns": 24, "predicted": 200.0, "real": 10.0}
    held = [{"check": True}] * 3
    assert "rates" in goal_switch.promote(cfg, held, good, 100, path=path)
    st = json.load(open(path))
    assert goal_switch.owns("rates", cfg, st) and not goal_switch.owns("buys", cfg, st)
    assert goal_switch.promote(cfg, held, good, 110, path=path) is None          # one job per 24 turns
    assert "buys" in goal_switch.promote(cfg, held, good, 124, path=path)
    msg = goal_switch.promote(cfg, held + [{"check": False}], bad, 130, path=path)
    assert msg and "buys" in msg and "back" in msg, msg                           # newest job handed back first
    st = json.load(open(path))
    assert goal_switch.owns("rates", cfg, st) and not goal_switch.owns("buys", cfg, st)
    # the kill switch beats everything; without auto nothing is live unless forced by hand
    assert not goal_switch.owns("rates", {"goal": {"auto": True, "off": True}}, st)
    assert not goal_switch.owns("rates", {"goal": {}}, st)
    assert goal_switch.owns("invest", {"goal": {"live": {"invest": True}}}, {})
    # no model check yet (under 24 turns of history): never hands anything over
    assert goal_switch.promote(cfg, held, {"turns": 6, "predicted": 1, "real": 1}, 500, path=path) is None


def test_rate_moves_step_and_respect_guards():
    import act
    snap = {"turn": 200, "buildings": [
        {"id": "7", "name": "spinnery 1", "recipe": "spin thread 1", "target": 2.0},
        {"id": "8", "name": "brewery 1", "recipe": "brew beer 1", "target": 0.4}]}
    G = {"ok": True, "changes": [{"name": "spinnery 1", "id": "7", "kind": "building", "from": 2.0, "to": 1.0, "gain": 20},
                                 {"name": "brewery 1", "id": "8", "kind": "building", "from": 0.4, "to": 1.0, "gain": 10}],
         "buildings": {"7": {"recipe": "spin thread 1", "target": 1.0}, "8": {"recipe": "brew beer 1", "target": 1.0}}}
    cfg = {"goal": {"step_share": 0.25, "step_min": 0.25, "min_gain": 3}}
    moves, why = act.goal_moves({"goal": G}, cfg, snap, 0, {})
    by = {m["name"]: m["to"] for m in moves}
    assert by == {"spinnery 1": 1.5, "brewery 1": 0.65}, by                        # steps, not jumps
    moves, _ = act.goal_moves({"goal": G}, cfg, snap, 3, {})                        # failsafe STOP: cuts only
    assert [m["name"] for m in moves] == ["spinnery 1"]
    moves, _ = act.goal_moves({"goal": G}, cfg, snap, 0, {"spinnery 1": 199})       # touched last turn: held
    assert [m["name"] for m in moves] == ["brewery 1"]
    G2 = dict(G, scorecard={"turns": 24, "predicted": 300.0, "real": 20.0})
    moves, why = act.goal_moves({"goal": G2}, cfg, snap, 0, {})
    assert moves == [] and "OFF" in why
    G3 = dict(G, changes=[dict(G["changes"][0], gain=1.0)], buildings=G["buildings"])
    assert act.goal_moves({"goal": G3}, cfg, snap, 0, {})[0] == []                  # not worth moving


def test_invest_waits_for_cash_and_builds():
    import act
    G = {"ok": True, "investments": [{"kind": "plot", "building": "9", "what": "+1 plot net maker", "cost": "~1400 coin",
                                      "coin": 1400, "gain": 20.0, "payback": 70, "pays": True}]}
    snap = {"turn": 300, "cash": 9000, "buildings": [{"id": "9", "name": "net maker", "type": "net maker"}]}
    cfg = {"goal": {"invest_hold_runs": 3}}
    st = {}
    for _ in range(2):
        assert act.invest_pick({"goal": G}, cfg, snap, st)[0] is None          # same pick 3 runs in a row first
    pick, why = act.invest_pick({"goal": G}, cfg, snap, st)
    assert pick and pick["plot"]["building"] == "9" and pick["confirm"], why
    st = {"want": {"key": "plot:9", "runs": 5}}
    pick, why = act.invest_pick({"goal": G}, cfg, dict(snap, cash=6000), st)
    assert pick is None and "cash" in why                                      # 6000 - 1400 < 4000 + 2000
    pick, why = act.invest_pick({"goal": G}, cfg, snap, {"last_invest_turn": 290, "want": {"key": "plot:9", "runs": 5}})
    assert pick is None and "cooldown" in why
    busy = dict(snap, buildings=snap["buildings"] + [{"id": "5", "construction": {"stage": "EXPANSION"}}])
    assert act.invest_pick({"goal": G}, cfg, busy, {"want": {"key": "plot:9", "runs": 5}})[0] is None
    # a new building goes through the order queue's site entry
    Gb = {"ok": True, "investments": [{"kind": "build", "type": "raghouse", "what": "new raghouse", "coin": 2000,
                                       "gain": 80.0, "payback": 25, "pays": True}]}
    pick, _ = act.invest_pick({"goal": Gb}, cfg, snap, {"want": {"key": "build:raghouse", "runs": 2}})
    assert pick == {"site": {"type": "raghouse"}, "confirm": True, "note": pick["note"]}


def test_trims_need_a_long_streak():
    import act
    G = {"ok": True, "trims": [{"building": "7", "what": "donate quarry", "gain": 15.0, "tax": 20}]}
    snap = {"turn": 400, "cash": 9000, "buildings": [{"id": "7", "type": "quarry"}]}
    cfg = {"goal": {"trim_hold_runs": 3}}
    st = {}
    assert act.invest_pick({"goal": G}, cfg, snap, st, trim_ok=True)[0] is None
    assert act.invest_pick({"goal": G}, cfg, snap, st, trim_ok=True)[0] is None
    pick, why = act.invest_pick({"goal": G}, cfg, snap, st, trim_ok=True)
    assert pick == {"donate": "7", "confirm": True, "note": pick["note"]} and why == "trim"
    # a run where it no longer pays resets the streak
    act.invest_pick({"goal": {"ok": True, "trims": []}}, cfg, snap, st, trim_ok=True)
    assert "7" not in st["trim"]
    # a refused donation is not retried for 48 turns
    st = {"trim": {"7": 10}, "trim_failed": {"7": 390}}
    assert act.invest_pick({"goal": G}, cfg, snap, st, trim_ok=True)[0] is None


def test_recipe_switch_and_ship_move_hold():
    import act
    snap = {"turn": 500, "buildings": [{"id": "3", "name": "net maker", "recipe": "make nets 1", "target": 0.5},
                                       {"id": "4", "name": "raghouse 1", "recipe": None, "target": 0.0}]}
    G = {"ok": True, "changes": [{"kind": "building", "gain": 30}],
         "buildings": {"3": {"recipe": "make nets 2", "target": 1.0, "switch_gain": 13.0},
                       "4": {"recipe": "make paper 1", "target": 1.0}}}
    cfg = {"goal": {"switch_hold_runs": 2, "switch_min": 10}}
    gst = {}
    moves, _ = act.goal_moves({"goal": G}, cfg, snap, 0, {}, gst)
    by = {m["id"]: m for m in moves}
    assert "3" not in by and by["4"]["switch"] and by["4"]["recipe"] == "make paper 1"   # idle: at once
    moves, _ = act.goal_moves({"goal": G}, cfg, snap, 0, {}, gst)
    by = {m["id"]: m for m in moves}
    assert by["3"]["switch"] and by["3"]["recipe"] == "make nets 2"                    # 2nd run in a row
    G2 = dict(G, buildings={"3": dict(G["buildings"]["3"], switch_gain=4.0)})
    assert act.goal_moves({"goal": G2}, cfg, snap, 0, {}, {})[0] == []                # not worth a switch
    # ships: a better town must win ship_hold_runs runs in a row before the pin moves
    Gs = {"ok": True, "ships": [{"ship": "1", "current": "A", "town": "B", "gain_over_current": 30.0}]}
    cfg = {"goal": {"ship_hold_runs": 2, "ship_switch_min": 20}, "live": {"ship_pins": {"1": "A"}}}
    gst = {}
    assert act.goal_pins({"goal": Gs}, cfg, gst)["1"] == "A"
    assert act.goal_pins({"goal": Gs}, cfg, gst)["1"] == "B"
    Gw = {"ok": True, "ships": [{"ship": "1", "current": "A", "town": "B", "gain_over_current": 5.0}]}
    assert act.goal_pins({"goal": Gw}, cfg, {})["1"] == "A"


def test_model_picks_one_recipe_and_ship_cargo_is_ours():
    """With ships modelled, cargo out is only what we make or hold, cargo back only what we use; a building runs
    one recipe."""
    rec = dict(RECIPES)
    rec["make gadgets"] = {"site": "workshop", "tier": 1, "class": "crafting",
                           "inputs": [{"product": "labour", "amount": 10}], "outputs": [{"product": "gadgets", "amount": 1}]}
    rec["make widgets"] = dict(RECIPES["make widgets"], site="workshop", tier=1, **{"class": "crafting"})
    s = snap()
    s["home_town"] = "H"
    s["market"]["gadgets"] = {"price": 25.0, "traded": 100}
    s["market"]["wine"] = {"price": 9.0, "ask": 9.0, "ask_vol": 100, "traded": 100}
    world = [{"name": "Far", "markets": {"widgets": {"highest_bid": "60", "bid_volume_10": 50, "volume_ema_12": 50},
                                         "wine": {"highest_bid": "30", "bid_volume_10": 50, "volume_ema_12": 50}}}]
    sea = {"T": {"name": "Far", "moves": 200}}
    prods = {"widgets": {"type": "commodity", "size": 1}, "wine": {"type": "commodity", "size": 1},
             "gadgets": {"type": "commodity", "size": 1}}
    s["ships"] = [{"id": "S1", "name": "boat", "route_to": None}]
    G = goal.plan_goal(s, CFG, rec, hist=hist_selling("widgets", 5), world=world, sea=sea, products=prods)
    assert G["ok"], G
    assert G["ships"][0]["town"] == "T", G["ships"]
    sp = G["ship_plan"]["S1"]
    assert "wine" not in (sp.get("exp") or {}), sp          # never bought at home to export
    assert sp["exp"]["widgets"] > 0
    lv = G["levels"]
    assert min(lv.get("workshop", 0), max([v for k, v in lv.items() if "[make gadgets]" in k] or [0])) < 1e-6, lv


if __name__ == "__main__":
    n = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            n += 1
            print("ok", name)
    print("%d checks passed" % n)
