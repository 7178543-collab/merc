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
import act        # noqa: E402
import api        # noqa: E402
import goals      # noqa: E402
import shutil     # noqa: E402
import tempfile   # noqa: E402
import planner    # noqa: E402

SNAP = json.load(open(os.path.join(HERE, "fixtures", "snapshot_2026-10-11.json")))
CFG = json.load(open(os.path.join(HERE, "config.json")))


def keys(p):
    return {"%s:%s" % (f["severity"], f["item"]) for f in p["flags"]}


def test_read_only():
    assert CFG["mode"] in ("shadow", "handover")
    for path in glob.glob(os.path.join(HERE, "*.py")):
        if os.path.basename(path) in ("api.py", "test_v2.py"):
            continue
        n = 0
        for node in ast.walk(ast.parse(open(path).read())):       # real calls only, not mentions in comments or docstrings
            if isinstance(node, ast.Call):
                fn = node.func
                n += getattr(fn, "attr", getattr(fn, "id", None)) == "allow_writes"
        # the actor is the one place writes can be enabled, once, behind --live + owned items (tested below)
        assert n == (1 if os.path.basename(path) == "act.py" else 0), "%s enables writes" % path
    ok, status, msg = api.write("PUT", "/anything", {})
    assert not ok and api.calls["write"] == 0, "api.write must refuse in shadow mode"


def _act_dir(cfg_live=(), failsafe_level=0, snap=None):
    d = tempfile.mkdtemp()
    s = snap or SNAP
    json.dump(s, open(os.path.join(d, "snapshot.json"), "w"))
    json.dump(planner.plan(s, CFG, goals=[]), open(os.path.join(d, "plan.json"), "w"), default=str)
    json.dump({"level": failsafe_level}, open(os.path.join(d, "failsafe.json"), "w"))
    cfg = copy.deepcopy(CFG)
    cfg["live"] = {"items": list(cfg_live)}
    return d, cfg


def test_act_merge():
    beer = [{"min_holding": 60, "max_holding": 8, "buy_volume": 4, "buy_price": "6", "sell_volume": 20, "sell_price": "4.1"},
            {"min_holding": 60, "sell_volume": 140, "sell_price": "3.7"}]
    new = act.merge(beer, None, {"sell_volume": 51, "sell_price": "3.9"})
    assert new == [{"min_holding": 60, "max_holding": 8, "buy_volume": 4, "buy_price": "6", "sell_volume": 51, "sell_price": "3.9"}]
    tools = [{"max_holding": 200, "buy_volume": 31, "buy_price": "6.2"}, {"max_holding": 200, "buy_volume": 10, "buy_price": "4.9"}]
    assert act.merge(tools, {"buy_volume": 8, "buy_price": "6.2", "max_holding": 60}, None) == \
        [{"max_holding": 60, "buy_volume": 8, "buy_price": "6.2"}]                     # one buy tier, the other's buy goes
    timber = [{"min_holding": 350, "sell_volume": 20, "sell_price": "7"}, {"buy_price": "8.6"}]
    assert act.merge(timber, None, {"sell_volume": 24, "sell_price": "8.5"})[0]["min_holding"] == 350   # kept-back stock untouched
    assert act.merge([], {"buy_volume": 5, "buy_price": "1"}, None) == [{"buy_volume": 5, "buy_price": "1"}]
    assert act._canon([{"sell_price": "22"}]) == act._canon([{"sell_price": 22.0}])


def test_act_guards():
    cfg = copy.deepcopy(CFG)
    live = [{"buy_volume": 40, "buy_price": "2.4"}]
    assert any("50%" in w for w in act.check("firewood", live, [{"buy_volume": 40, "buy_price": "1.0"}], cfg, 20000))
    assert any("ceiling" in w for w in act.check("firewood", live, [{"buy_volume": 40, "buy_price": "2.6"}], cfg, 20000))
    assert any("no buy ceiling" in w for w in act.check("bricks", [], [{"buy_volume": 40, "buy_price": "1"}], cfg, 20000))
    assert any("2x+10" in w for w in act.check("firewood", live, [{"buy_volume": 95, "buy_price": "2.4"}], cfg, 20000))
    assert any("reserve" in w for w in act.check("firewood", live, [{"buy_volume": 45, "buy_price": "2.4"}], cfg, 3000))
    assert any("floor" in w for w in act.check("garments", [{"sell_volume": 39, "sell_price": "22"}],
                                               [{"sell_volume": 39, "sell_price": "20"}], cfg, 20000))
    assert any("never_drop" in w for w in act.check("porterage", [{"buy_volume": 24, "buy_price": "0.6"}], [], cfg, 20000))
    assert act.check("firewood", live, [{"buy_volume": 30, "buy_price": "2.4", "max_holding": 60}], cfg, 20000) == []
    plan = planner.plan(SNAP, CFG, goals=[])
    live_t = {k: v.get("orders") or [] for k, v in SNAP["store"]["items"].items()}
    assert act.decide(SNAP, plan, cfg, {"grain"}, live_t, 2)[1].startswith("failsafe")          # BRAKE: v2 stands down
    rows, stand = act.decide(SNAP, plan, cfg, {"grain"}, live_t, 0, manual=lambda i: True)
    assert stand is None and any("by hand" in w for r in rows if r["item"] == "grain" for w in r["refused"])
    rows = {r["item"]: r for r in act.decide(SNAP, plan, cfg, {"grain"}, live_t, 0, manual=lambda i: False, paused={"grain"})[0]}
    assert any("paused by the failsafe" in w for w in rows["grain"]["refused"])           # brake-paused: never auto-restored
    bad = dict(plan, notes=["builds skipped: KeyError: x"])
    assert "skipped" in act.decide(SNAP, bad, cfg, {"grain"}, live_t, 0)[1]


def test_act_dry_run_never_writes():
    d, cfg = _act_dir(cfg_live=["grain"])
    try:
        before = api.calls["write"]
        res = act.main(argv=["act.py"], out=d, cfg=cfg, failsafe=os.path.join(d, "failsafe.json"))
        assert res["mode"] == "dry" and api.calls["write"] == before and not api._writes
        assert res["would_change"] > 0 and os.path.exists(os.path.join(d, "act.json"))
        cfg["live"]["items"] = []
        res = act.main(argv=["act.py", "--live"], out=d, cfg=cfg, failsafe=os.path.join(d, "failsafe.json"))
        assert not api._writes and api.calls["write"] == before                  # --live with nothing owned: still read-only
    finally:
        shutil.rmtree(d)


def test_act_live_sends_only_owned_and_suspends():
    d, cfg = _act_dir(cfg_live=["grain"])
    store = {k: {"managers": copy.deepcopy(v.get("orders") or [])} for k, v in SNAP["store"]["items"].items()}
    sent = []
    real = (api.get, api.write, api.allow_writes)

    def fake_get(path):
        return {"storage": {"inventory": {"holdings": copy.deepcopy(store)}}}

    def fake_write(method, path, body):
        item = path.rsplit("/", 1)[1].replace("%20", " ")
        sent.append((method, item, body))
        store[item]["managers"] = copy.deepcopy(body["managers"])
        return True, 200, {}
    api.get, api.write, api.allow_writes = fake_get, fake_write, lambda: None
    try:
        res = act.main(argv=["act.py", "--live"], out=d, cfg=cfg, failsafe=os.path.join(d, "failsafe.json"))
        assert [s[1] for s in sent] == ["grain"], sent                            # owned item only
        g = next(r for r in res["rows"] if r["item"] == "grain")
        assert g["verified"] and sent[0][2]["managers"][0]["buy_price"] == "3.7"  # bids at the ceiling (a limit)
        # second run: already set, nothing to send
        sent.clear()
        act.main(argv=["act.py", "--live"], out=d, cfg=cfg, failsafe=os.path.join(d, "failsafe.json"))
        assert sent == []
        # a risk flag on an owned item two runs in a row: suspended, back to v1
        p = json.load(open(os.path.join(d, "plan.json")))
        p["flags"].append({"severity": "risk", "item": "grain", "text": "test", "fix": None})
        json.dump(p, open(os.path.join(d, "plan.json"), "w"))
        act.main(argv=["act.py", "--live"], out=d, cfg=cfg, failsafe=os.path.join(d, "failsafe.json"))
        res = act.main(argv=["act.py", "--live"], out=d, cfg=cfg, failsafe=os.path.join(d, "failsafe.json"))
        assert "grain" in json.load(open(os.path.join(d, "suspended.json")))
        res = act.main(argv=["act.py", "--live"], out=d, cfg=cfg, failsafe=os.path.join(d, "failsafe.json"))
        assert res["owned"] == []
    finally:
        api.get, api.write, api.allow_writes = real
        shutil.rmtree(d)


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


def test_no_false_cant_fill():
    s = copy.deepcopy(SNAP)
    it = s["store"]["items"]["porterage"]
    s["market"]["porterage"]["ask"] = 1.1
    it.setdefault("flow", {})["purchase"] = 40            # buy is filling at the bid side
    k = keys(planner.plan(s, CFG))
    assert "tune:porterage" not in k and "risk:porterage:cantfill" not in k
    assert not any("can't fill" in f["text"] for f in planner.plan(s, CFG)["flags"])
    it["flow"]["purchase"] = 0; it["held"] = 0             # really failing: flagged
    assert any("can't fill" in f["text"] for f in planner.plan(s, CFG)["flags"])


def test_act_takes_off_an_unneeded_buy():
    s = copy.deepcopy(SNAP)                                  # banquet switched off: the mansion no longer eats cured fish
    for b in s["buildings"]:
        if b["type"] == "mansion":
            b["target"], b["flows"] = 0.0, {}
    s["store"]["items"]["cured fish"]["flow"] = {}
    s["history_use"] = {k: v for k, v in (s.get("history_use") or {}).items() if k != "cured fish"}
    plan = planner.plan(s, CFG, goals=[])
    assert "buy_off" in plan["orders"]["cured fish"] and "buy" not in plan["orders"]["cured fish"]
    live = {k: v.get("orders") or [] for k, v in s["store"]["items"].items()}
    cfg = copy.deepcopy(CFG)
    rows = {r["item"]: r for r in act.decide(s, plan, cfg, {"cured fish"}, live, 0, manual=lambda i: False)[0]}
    assert rows["cured fish"]["new"] == [] and not rows["cured fish"]["refused"]           # owned: the buy comes off
    rows = {r["item"]: r for r in act.decide(s, plan, cfg, set(), live, 0, manual=lambda i: False)[0]}
    assert "cured fish" not in rows                                                        # not owned: v2 leaves v1's order alone
    assert all("buy_off" not in (plan["orders"].get(i) or {}) for i in CFG["never_drop"])  # never_drop items are never offered up


def test_ship_guard_pauses_an_idle_ship():
    d = tempfile.mkdtemp()
    calls = []
    real = api.write
    api.write = lambda m, p, b: (calls.append((m, p, b)) or (True, 200, {}))
    try:
        plan = {"ships": [{"ship": "Flax Wyrm", "id": "845668271", "cost": 72, "sold": {}, "bought": {}, "crew_set": 0.723},
                          {"ship": "Busy", "id": "2", "cost": 30, "sold": {"garments": 20}, "bought": {}, "crew_set": 0.3}]}
        st = {}
        log = os.path.join(d, "act.jsonl")
        for turn in (1, 1, 2):                          # the same turn twice counts once
            assert act.ship_guard(plan, {"845668271", "2"}, st, turn, log) == []
        assert act.ship_guard(plan, {"845668271", "2"}, st, 3, log) == ["Flax Wyrm"]     # 3rd idle turn: paused
        assert calls == [("PUT", "/transports/845668271/operation", {"operation_target": "0.000"})]
        assert st["2"]["idle"] == 0                      # a ship that trades is never touched
    finally:
        api.write = real
        shutil.rmtree(d)


def test_ship_auto_sets_route_and_crew():
    d = tempfile.mkdtemp()
    calls = []
    real = api.write
    api.write = lambda m, p, b: (calls.append((m, p, b)) or (True, 200, {}))
    try:
        t_ = act.now().isoformat()
        plan = {"ship_plans": {"t": t_, "plans": [
            {"ship": "linen snake", "id": "1948883264", "crew": 0.2, "est_net": 300,
             "diff": {"garments": [{"sell_volume": 59, "sell_price": "28.0", "min_holding": 30}], "limestone": []}},
            {"ship": "Flax Wyrm", "id": "845668271", "crew": 0.0, "diff": {"beer": []}}]}}
        snap = {"turn": 10, "ships": [{"id": "1948883264", "set_target": 0.0}, {"id": "845668271", "set_target": 0.25}]}
        cfg = {"live": {"ship_modes": {"1948883264": "auto"}}}                 # Flax Wyrm is not auto: untouched
        done = act.ship_auto(plan, cfg, snap, os.path.join(d, "a.jsonl"), {})
        assert [c[1] for c in calls] == ["/transports/1948883264/route/inventory/garments",
                                         "/transports/1948883264/route/inventory/limestone", "/transports/1948883264/operation"]
        assert calls[2][2] == {"operation_target": "0.200"} and len(done) == 3
        calls.clear()                                                          # held by the guard: no writes
        assert "guard" in act.ship_auto(plan, cfg, snap, os.path.join(d, "a.jsonl"), {"1948883264": {"guard_paused_turn": 8}})[0]
        old = dict(plan["ship_plans"], t="2026-01-01T00:00:00+00:00")          # stale prices: no writes
        act.ship_auto({"ship_plans": old}, cfg, snap, os.path.join(d, "a.jsonl"), {})
        assert calls == []
    finally:
        api.write = real
        shutil.rmtree(d)


def test_ships_plan():
    import ships
    sea = {"1": {"name": "Home", "moves": 0.0}, "2": {"name": "Far", "moves": 774.0}}
    mk = lambda bid, ask, bv, av, tr=0: {"highest_bid": bid, "lowest_ask": ask, "bid_volume_10": bv, "ask_volume_10": av,
                                         "volume_ema_12": tr}
    world = [{"name": "Home", "markets": {"garments": mk(22.4, 23.2, 12, 1, 64), "cured fish": mk(24.6, 26, 5, 5, 30)}},
             {"name": "Far", "markets": {"garments": mk(28.4, 0, 59, 0, 72), "cured fish": mk(0, 23, 0, 20, 10),
                                         "cloth": mk(0, 5, 0, 50, 20)}}]
    snap = {"home_town": "1", "market": {"labour": {"price": 2.0}}, "store": {"items": {
        "garments": {"held": 448, "unit_cost": 20.1, "orders": [{"min_holding": 30}],
                     "flow": {"production": 41, "consumption": 1.8, "sale": 49, "sale_value": 1078}},
        "cured fish": {"held": 19, "orders": [], "flow": {"consumption": 5.5}},
        "cloth": {"held": 80, "orders": [], "flow": {"production": 89, "consumption": 81}}}}}
    cfg = {"chain": {"intermediates": ["cloth"]}, "never_drop": []}
    rec = {"snekkja 1": {"inputs": [{"amount": 50, "product": "labour"}]}}
    p = ships.plan_ship({"name": "s", "id": "9", "route_to": "2", "route_orders": {"limestone": [{"buy_volume": 30}]}},
                        snap, world, sea, cfg, recipes=rec)
    g = p["orders"]["garments"]
    assert g["sell_volume"] == 59 and g["sell_price"] == "28.0" and g["min_holding"] == 30     # 98% of their 28.4 bid, grid-snapped
    assert p["orders"]["cured fish"]["buy_volume"] == 5 and "cloth" not in p["orders"]       # we use it / we make cloth
    assert p["crew"] == 0.2 and p["est_net"] > 250                                           # 64 units / 483 a turn -> 0.2
    diff = ships.route_diff({"route_orders": {"limestone": [{"buy_volume": 30}]}}, p)
    assert diff["limestone"] == [] and "garments" in diff
    world[1]["markets"]["garments"] = mk(23.0, 0, 59, 0, 72)                                 # bid gone below home value + margin
    p = ships.plan_ship({"name": "s", "id": "9", "route_to": "2"}, snap, world, sea, cfg, recipes=rec)
    assert "garments" not in p["orders"]


def test_ships_read_route_exports():
    s = copy.deepcopy(SNAP)
    s["ships"] = [{"id": "1", "name": "linen snake", "running_cost": 39.3, "production": 0.4, "set_target": 0.4,
                   "route_to": "109102068", "route_flows": {"garments": {"projection": {}, "realized": {
                       "export": 30, "export_value": 882, "export_cost": 601.658, "export_fare": 3.06}}}}]
    sh = planner.plan(s, CFG, goals=[])["ships"][0]
    assert sh["sold"] == {"garments": 30} and abs(sh["trade_value"] - 277.3) < 0.05
    assert not any(f["item"] == "linen snake" for f in planner.plan(s, CFG, goals=[])["flags"])   # it traded: no waste flag


def test_ship_voyage_steps():
    d = tempfile.mkdtemp()
    calls = []

    def apply(e):
        calls.append(e)
        return {"ok": True}
    try:
        cfg = {"live": {"ship_modes": {"9": "auto"}}}
        plan = {"ship_plans": {"plans": [{"id": "9", "est_net": 0.0}],
                               "best": [{"town": "Etallaen", "town_id": "109102068", "per_turn": 300}]}}
        sst = {}
        log = os.path.join(d, "a.jsonl")
        snap = {"turn": 1, "ships": [{"id": "9", "name": "s", "town": "133002223", "route_to": "133002223"}]}
        out = act.ship_voyages(plan, cfg, snap, sst, log, apply)            # decides: heading for Etallaen
        assert "heading for Etallaen" in out[0] and calls == []
        snap["turn"] = 2
        act.ship_voyages(plan, cfg, snap, sst, log, apply)                  # stop the route, sail home
        assert calls[0]["route"]["stop"] and calls[-1]["travel"]["to_town"] == "152202387"
        calls.clear()
        snap = {"turn": 3, "ships": [{"id": "9", "name": "s", "town": "152202387", "route_to": None}]}
        act.ship_voyages(plan, cfg, snap, sst, log, apply)                  # home: sail out and start the route
        assert calls[1]["travel"]["to_town"] == "109102068" and calls[2]["route"]["start"]
        calls.clear()
        snap = {"turn": 4, "ships": [{"id": "9", "name": "s", "town": "109102068", "route_to": "109102068"}]}
        out = act.ship_voyages(plan, cfg, snap, sst, log, apply)            # route running: done
        assert "running" in out[0] and sst["9"]["voyage"] is None and calls == []
        assert act.ship_voyages(plan, cfg, dict(snap, turn=5), sst, log, apply) == []   # cooldown
    finally:
        shutil.rmtree(d)


def test_routes():
    import routes
    sea = {"1": {"name": "Home", "moves": 0.0}, "2": {"name": "Near", "moves": 300.0}, "3": {"name": "Far", "moves": 750.0},
           "4": {"name": "TooFar", "moves": 1700.0}}
    mk = lambda bid, ask, bv, av, tr=0: {"highest_bid": bid, "lowest_ask": ask, "bid_volume_10": bv, "ask_volume_10": av,
                                         "volume_ema_12": tr}
    world = [{"name": "Home", "markets": {"garments": mk(20, 21, 50, 50), "salt": mk(4, 5, 100, 100)}},
             {"name": "Near", "markets": {"garments": mk(40, 0, 10, 0, 100), "salt": mk(0, 1, 0, 300)}},
             {"name": "Far", "markets": {"garments": mk(40, 0, 10, 0, 100)}},
             {"name": "TooFar", "markets": {"garments": mk(90, 0, 100, 0)}}]
    snap = {"home_town": "1", "market": {}, "store": {"items": {
        "garments": {"held": 270, "orders": [{"min_holding": 30}], "flow": {"production": 40, "consumption": 0}},
        "salt": {"held": 0, "orders": [], "flow": {}}}}}
    recipes = {"snekkja 1": {"inputs": [{"amount": 50, "product": "labour"}]}}
    snap["market"]["labour"] = {"price": 2.0}                                      # 100 coin a turn at full crew
    rr = routes.rank(snap, world, sea, recipes=recipes)
    assert rr["assumptions"]["running_cost_full_crew"] == 100 and rr["out_of_range"] == 1   # 1700 moves > twice the 800 range
    near = next(r for r in rr["routes"] if r["town"] == "Near")
    assert near["trips_per_turn_full"] == 5.0 and abs(near["cost_per_unit"] - 0.08) < 1e-9   # 3000/(2x300); 100/(250x5)
    out = {x["item"]: x for x in near["out"]}
    assert out["garments"]["units"] == 30 and out["garments"]["buy"] == 20         # 30% of their 100/turn; valued at the home bid
    back = {x["item"]: x for x in near["back"]}
    assert back["salt"]["units"] == 100                                            # capped by what home buyers take
    assert near["crew"] == 0.1                                                     # 100 units a leg / 1,250 a turn -> 0.1 (client 0.1 steps)
    far = next(r for r in rr["routes"] if r["town"] == "Far")
    assert far["cost_per_unit"] > near["cost_per_unit"] and far["per_turn"] < near["per_turn"]
    assert "Best" in "\n".join(routes.report_lines(rr))


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


def test_goals():
    gs = [{"id": "f150", "kind": "keep", "item": "furniture", "units": 150},
          {"id": "t300", "kind": "keep", "item": "timber", "units": 300},
          {"id": "tcap", "kind": "cap", "item": "timber", "units": 200},
          {"id": "bcap", "kind": "cap", "item": "beer", "units": 40},
          {"id": "exp", "kind": "export", "item": "garments", "to": "Blanans"},
          {"id": "old", "kind": "keep", "item": "candles", "units": 99, "until": "2026-10-01"},
          {"id": "bad", "kind": "hoard", "item": "x"},
          {"id": "met", "kind": "keep", "item": "furniture", "units": 100}]
    p = planner.plan(SNAP, CFG, goals=gs)
    st = {g["id"]: g for g in p["goals"]}
    assert st["f150"]["status"] == "ordering" and st["f150"]["order"] == {"buy_volume": 1, "buy_price": "15.5", "max_holding": 150}
    assert st["t300"]["status"] == st["tcap"]["status"] == "conflict"
    assert st["bcap"]["status"] == "ordering" and st["bcap"]["order"]["min_holding"] == 40
    assert st["exp"]["status"] == "unsupported" and st["old"]["status"] == "expired"
    assert st["bad"]["status"] == "invalid" and st["met"]["status"] == "met"
    assert p["orders"]["furniture"]["effective_buy"]["max_holding"] == 150
    # a goal can't lift a safety rule: timber ask 9.15 is above the 8.60 ceiling, so a lone keep is blocked
    p = planner.plan(SNAP, CFG, goals=[{"id": "t", "kind": "keep", "item": "timber", "units": 300}])
    assert p["goals"][0]["status"] == "blocked" and "tune:timber" in keys(p)
    # the goals file that ships is valid and empty; a broken one is a note, not a crash
    assert goals.load() == ([], None)
    bad = os.path.join(HERE, "fixtures", "_broken_goals.json")
    open(bad, "w").write("{nope")
    try:
        assert goals.load(bad)[0] == [] and "unreadable" in goals.load(bad)[1]
    finally:
        os.remove(bad)


def test_prestige_ranking():
    pp = planner.plan(SNAP, CFG)["prestige_plan"]
    by = {r["sink"]: r for r in pp["ranked"]}
    assert 61 < by["jousting 1"]["coin_per_prestige"] < 62.5       # the doc's "~62 coin per prestige" for the arena
    assert by["maintain 1"]["running"] and by["hold banquet 1 (fish)"]["running"]
    assert [r["effective"] for r in pp["ranked"]] == sorted(r["effective"] for r in pp["ranked"])   # cheapest first
    ch = by["hold sermon 2"]                                       # a church isn't built: capex is spread over the turns left
    assert not ch["owned"] and ch["capex"] > 50000 and ch["effective"] > ch["coin_per_prestige"]
    assert 1189 < pp["turns_left"] < 1191 and pp["legacy_factor"] > 0.99
    late = copy.deepcopy(SNAP)
    late["t"] = "2026-11-29T00:00:00+00:00"                        # 35 turns left: a 90-turn build can't pay back
    assert "hold sermon 2" not in {r["sink"] for r in planner.plan(late, CFG)["prestige_plan"]["ranked"]}


def test_prestige_agreed():
    ag = {a["sink"]: a for a in planner.plan(SNAP, CFG)["prestige_plan"]["agreed"]}
    assert ag["tenants"]["status"] == "done" and ag["prestige_management"]["status"] == "done"
    assert ag["apprentices"]["status"] == "waiting" and ag["apprentices"]["cost"] == 250 and "51 turns" in ag["apprentices"]["detail"]
    s = copy.deepcopy(SNAP)
    s["household"]["free"] = 300
    assert {a["sink"]: a for a in planner.plan(s, CFG)["prestige_plan"]["agreed"]}["apprentices"]["status"] == "ready"
    s["household"]["levels"]["tenants"] = 10                       # v1's rule: 50 x (level - 2) from level 10 = 400
    s["household"]["free"] = 500
    a = {a["sink"]: a for a in planner.plan(s, CFG)["prestige_plan"]["agreed"]}["tenants"]
    assert a["cost"] == 400 and a["status"] == "ready"
    s["household"]["rate"] = 0                                     # no prestige income: never ready
    assert {a["sink"]: a for a in planner.plan(s, CFG)["prestige_plan"]["agreed"]}["tenants"]["status"] == "waiting"


def test_planner_survives_thin_snapshots():
    for snap in ({}, {"t": "2026-10-11T20:00:00+00:00"}, {"t": "2026-10-11T20:00:00+00:00", "buildings": [], "store": {"items": {}}, "market": {}},
                 dict(SNAP, market={}), dict(SNAP, buildings=[]), dict(SNAP, household={})):
        p = planner.plan(snap, CFG, goals=[])
        assert isinstance(p["flags"], list) and "skipped" not in " ".join(p["notes"]), p["notes"]


if __name__ == "__main__":
    n = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            n += 1
            print("ok", name)
    print("%d checks passed" % n)
