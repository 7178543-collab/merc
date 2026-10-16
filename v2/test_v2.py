#!/usr/bin/env python3
"""Bot v2 checks. Plain asserts, no dependencies:  python v2/test_v2.py

Runs the planner on a frozen snapshot (v2/fixtures/), so the hourly job overwriting state/v2 can't change the result.
Also guards the one rule that matters: shadow mode never writes to the game.
"""
import ast
import copy
import datetime
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
    cfg["diagnose"] = {"on": False}         # diagnose has its own tests (it would reach the order queue here)
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


def test_act_steps_big_volume_changes():
    live = [{"min_holding": 30, "sell_volume": 10, "sell_price": "22"}]
    new, notes = act.step_volumes(live, act.merge(live, None, {"sell_volume": 55, "sell_price": "22.0"}))
    assert new[0]["sell_volume"] == 30 and new[0]["min_holding"] == 30 and notes, (new, notes)
    assert not act.check("garments", live, new, CFG, 20000)
    same, notes = act.step_volumes(live, act.merge(live, None, {"sell_volume": 25, "sell_price": "22.0"}))
    assert same[0]["sell_volume"] == 25 and not notes


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
        assert [c[1] for c in calls] == ["/transports/1948883264/route/inventory/limestone",   # the clear goes first
                                         "/transports/1948883264/route/inventory/garments", "/transports/1948883264/operation"]
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
    assert p["crew"] == 0.2 and p["est_net"] > 200        # 64 cargo units / 483 a turn at full crew -> 0.2 (no round-trip minimum)
    shared = ships.plan_ship({"name": "s2", "id": "8", "route_to": "2"}, snap, world, sea, cfg, recipes=rec,
                             taken={"garments": 60})
    assert shared["orders"]["garments"]["sell_volume"] == 14            # 74 spare a turn, 60 already on another route
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


def test_export_first_home_sales():
    import shadow
    p = {"orders": {"garments": {"sell": {"sell_volume": 69, "sell_price": "22.0"}}, "beer": {"sell": {"sell_volume": 12}}},
         "ship_plans": {"plans": [{"orders": {"garments": {"sell_volume": 34}}}, {"orders": {"garments": {"sell_volume": 25},
                                                                                         "beer": {"sell_volume": 56}}}]}}
    shadow.export_first(p)
    assert p["orders"]["garments"]["sell"]["sell_volume"] == 10        # 69 - 59 abroad
    assert p["orders"]["beer"]["sell"]["sell_volume"] == 10            # never under the home minimum
    p = {"orders": {"garments": {"sell": {"sell_volume": 69}}},
         "ship_plans": {"plans": [{"orders": {"garments": {"sell_volume": 42}}}]}}
    snap = {"store": {"items": {"garments": {"held": 402, "orders": [{"min_holding": 30}]}}}}
    shadow.export_first(p, snap)
    assert p["orders"]["garments"]["sell"]["sell_volume"] == 69        # 372 spare covers 69 + 42: no cut
    snap["store"]["items"]["garments"]["held"] = 120
    shadow.export_first(p, snap)
    assert p["orders"]["garments"]["sell"]["sell_volume"] == 48        # 90 spare - 42 abroad


def test_ship_voyage_steps():
    d = tempfile.mkdtemp()
    calls = []

    def apply(e):
        calls.append(e)
        if e.get("route", {}).get("start"):
            return {"ok": True, "route": {"remote_town": "109102068"}}
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
        # an idle ship (its plan has no orders) waits only 2 turns; an earning one waits 12
        far = {"ship_plans": {"plans": [{"id": "9", "est_net": 0.0, "orders": {}}],
                              "best": [{"town": "Clairlond", "town_id": "88002195", "per_turn": 220}]}}
        assert act.ship_voyages(far, cfg, dict(snap, turn=5), sst, log, apply) == []
        assert "heading for Clairlond" in act.ship_voyages(far, cfg, dict(snap, turn=6), sst, log, apply)[0]
        sst["9"] = {"last_voyage_turn": 4}
        earning = {"ship_plans": dict(far["ship_plans"], plans=[{"id": "9", "est_net": 40.0, "orders": {"beer": {}}}])}
        assert act.ship_voyages(earning, cfg, dict(snap, turn=6), sst, log, apply) == []
        # at home, the target is re-checked: a better free town wins, and nothing paying ends the voyage at crew 0
        sst = {"9": {"voyage": {"target": "159601387", "name": "Kirchwerp", "step": "home", "turn": 7, "moves": 1072}}}
        calls.clear()
        home = {"turn": 7, "ships": [{"id": "9", "name": "s", "town": "152202387", "route_to": None}]}
        out = act.ship_voyages(plan, cfg, home, sst, log, apply)
        assert "re-targeted Kirchwerp -> Etallaen" in out[0] and calls[1]["travel"]["to_town"] == "109102068", (out, calls)
        sst = {"9": {"voyage": {"target": "159601387", "name": "Kirchwerp", "step": "home", "turn": 7, "moves": 1072}}}
        calls.clear()
        out = act.ship_voyages(dict(plan, ship_plans=dict(plan["ship_plans"], best=[])), cfg, home, sst, log, apply)
        assert "voyage ended" in out[0] and calls == [{"transport": "9", "operation_target": 0.0}] and sst["9"]["voyage"] is None
    finally:
        shutil.rmtree(d)


def test_ship_trade_mode():
    import ships
    sea = {"1": {"name": "Home", "moves": 0.0}, "2": {"name": "Far", "moves": 774.0}}
    mk = lambda bid, ask, bv, av, tr=0: {"highest_bid": bid, "lowest_ask": ask, "bid_volume_10": bv, "ask_volume_10": av,
                                         "volume_ema_12": tr}
    world = [{"name": "Home", "markets": {"tallow": mk(20, 24.8, 5, 10, 10), "medicine": mk(120, 140, 3, 1, 4),
                                          "bread": mk(2.4, 2.44, 50, 200, 400), "salt": mk(1, 2, 5, 20, 20)}},
             {"name": "Far", "markets": {"tallow": mk(31.6, 0, 5, 0, 6), "medicine": mk(0, 60, 0, 2, 3),
                                         "bread": mk(3.4, 0, 137, 0, 400), "salt": mk(2.1, 0, 5, 0, 10)}}]
    snap = {"home_town": "1", "cash": 20000, "market": {"labour": {"price": 2.0}}, "store": {"items": {
        "bread": {"held": 60, "orders": [{"min_holding": 87, "sell_volume": 110, "sell_price": "2.24"}], "flow": {}}}}}
    cfg = {"chain": {"intermediates": []}, "never_drop": [], "ship_trade": {"on": True}}
    rec = {"snekkja 1": {"inputs": [{"amount": 50, "product": "labour"}]}}
    ship = {"name": "s", "id": "9", "route_to": "2"}
    p = ships.plan_ship(ship, snap, world, sea, cfg, recipes=rec)
    o, h = p["orders"], p["home_orders"]
    assert o["tallow"]["sell_volume"] == 5 and h["tallow"]["buy_volume"] == 5 and h["tallow"]["max_holding"] == 10, p
    assert o["medicine"]["buy_volume"] == 2 and h["medicine"]["sell_volume"] == 2 and o["medicine"]["max_holding"] == 4, p
    assert "bread" not in o                     # someone else's orders are on it: never traded
    assert "salt" not in o                      # 2.1 there vs 2.04 home buy: under the 6% margin
    assert all(not k.startswith("_") for t in list(o.values()) + list(h.values()) for k in t)
    # no cash: no home buys to ship out, but an import still runs (it costs nothing at home)
    p = ships.plan_ship(ship, dict(snap, cash=0), world, sea, cfg, recipes=rec)
    assert "tallow" not in p["orders"] and "medicine" in p["orders"], p
    # trade mode off: none of it
    p = ships.plan_ship(ship, snap, world, sea, dict(cfg, ship_trade={"on": False}), recipes=rec)
    assert not p["home_orders"] and "tallow" not in p["orders"]
    # the actor: writes the home side, owns the good, and hands it back once it is off every route and none is held
    d = tempfile.mkdtemp()
    try:
        calls = []
        w = lambda path, body: calls.append((path, body)) or (True, 200, None)
        plan = {"ship_plans": {"plans": [{"id": "9", "home_orders": {"tallow": {"buy_volume": 5, "buy_price": "25.4",
                                                                                 "max_holding": 10}}}]}}
        cfgl = {"live": {"ship_modes": {"9": "auto"}}}
        st = {}
        s2 = {"turn": 1, "store": {"items": {}}, "market": {}}
        act.trade_home(plan, cfgl, s2, st, "S", {"bread": [{"sell_volume": 1}]}, os.path.join(d, "a.jsonl"), w)
        assert calls[0][0].endswith("/tallow") and calls[0][1]["managers"][0]["buy_volume"] == 5 and calls[0][1]["capacity"] >= 10
        assert "tallow" in st["trade_items"]
        calls.clear()
        plan2 = {"ship_plans": {"plans": [{"id": "9", "home_orders": {"bread": {"buy_volume": 5, "buy_price": "2.5"}}}]}}
        s3 = {"turn": 2, "store": {"items": {"tallow": {"held": 4}}}, "market": {"tallow": {"bid": 20}}}
        out = act.trade_home(plan2, cfgl, s3, st, "S", {"tallow": [{"buy_volume": 5}], "bread": [{"sell_volume": 1}]},
                             os.path.join(d, "a.jsonl"), w)
        assert any("bread: skipped" in x for x in out)                         # never takes over someone else's good
        assert calls[0][1]["managers"][0]["sell_volume"] == 4 and "tallow" in st["trade_items"], calls  # sells the 4 left
        calls.clear()
        act.trade_home({"ship_plans": {"plans": []}}, cfgl, dict(s3, store={"items": {}}), st, "S",
                       {"tallow": [{"sell_volume": 4}]}, os.path.join(d, "a.jsonl"), w)
        assert calls[0][1] == {"managers": []} and "tallow" not in st["trade_items"]
    finally:
        shutil.rmtree(d)


def test_two_ships_never_share_a_voyage_target():
    # Oct 13: Flax Wyrm and linen snake both picked Etallaen; the second must re-plan to the next free town
    d = tempfile.mkdtemp()
    try:
        cfg = {"live": {"ship_modes": {"1": "auto", "2": "auto"}}}
        plan = {"ship_plans": {"plans": [{"id": "1", "est_net": 0.0, "orders": {}}, {"id": "2", "est_net": 0.0, "orders": {}}],
                               "best": [{"town": "Etallaen", "town_id": "109102068", "per_turn": 217},
                                        {"town": "Rouhomme", "town_id": "111", "per_turn": 101}]}}
        sst = {"1": {"voyage": {"target": "109102068", "name": "Etallaen", "step": "home", "turn": 9}, "last_voyage_turn": 1},
               "2": {"voyage": {"target": "109102068", "name": "Etallaen", "step": "home", "turn": 9}, "last_voyage_turn": 1}}
        snap = {"turn": 9, "ships": [{"id": "1", "name": "a", "town": "5", "route_to": None},
                                     {"id": "2", "name": "b", "town": "6", "route_to": None}]}
        out = act.ship_voyages(plan, cfg, snap, sst, os.path.join(d, "a.jsonl"), lambda e: {"ok": True})
        assert sst["1"]["voyage"]["target"] == "109102068", sst
        assert sst["2"]["voyage"]["target"] == "111" and any("heading for Rouhomme" in o for o in out), (out, sst)
        # a ship back home re-checking its own reserved target keeps it (doesn't count itself as taken)
        sst = {"1": {"voyage": {"target": "109102068", "name": "Etallaen", "step": "home", "turn": 8, "moves": 774}}}
        calls = []
        home = {"turn": 9, "ships": [{"id": "1", "name": "a", "town": "152202387", "route_to": None}]}
        act.ship_voyages(plan, cfg, home, sst, os.path.join(d, "a.jsonl"), lambda e: calls.append(e) or {"ok": True, "route": {"remote_town": "109102068"}})
        assert any((c.get("travel") or {}).get("to_town") == "109102068" for c in calls), calls
    finally:
        shutil.rmtree(d)


def test_ships_fit_capacity():
    import ships
    # 1,072 moves -> 279 size units a turn at full crew: beer 63 (126) + timber 26 (390) can't both go
    sea = {"1": {"name": "Home", "moves": 0}, "2": {"name": "Kirch", "moves": 1072.24}}
    mk = lambda bid, ask, bv, av, tr=0: {"highest_bid": bid, "lowest_ask": ask, "bid_volume_10": bv, "ask_volume_10": av,
                                         "volume_ema_12": tr}
    world = [{"name": "Home", "markets": {"beer": mk(0, 3.7, 0, 99, 160), "timber": mk(6.6, 7.0, 8, 4, 60)}},
             {"name": "Kirch", "markets": {"beer": mk(4.82, 0, 63, 0, 210), "timber": mk(15.0, 0, 26, 0, 87)}}]
    snap = {"home_town": "1", "market": {"labour": {"price": 1.74}}, "store": {"items": {
        "beer": {"held": 202, "unit_cost": 2.98, "orders": [{"min_holding": 60}],
                 "flow": {"production": 70, "consumption": 18.6, "sale": 36, "sale_value": 133.2}},
        "timber": {"held": 422, "unit_cost": 6.53, "orders": [{"min_holding": 350}],
                   "flow": {"production": 24, "consumption": 4.2, "sale": 20, "sale_value": 140}}}}}
    rec = {"snekkja 1": {"inputs": [{"amount": 50, "product": "labour"}, {"amount": 1.6, "product": "cloth"}]}}
    prods = {"beer": {"size": 2, "type": "commodity"}, "timber": {"size": 15, "type": "commodity"}}
    p = ships.plan_ship({"name": "s", "id": "9", "route_to": "2"}, snap, world, sea, {}, recipes=rec, products=prods)
    space = sum(o.get("sell_volume", 0) * prods[k]["size"] for k, o in p["orders"].items())
    assert space <= p["capacity"] and p["crew"] <= 1.0, (p, space)
    assert all("_gain" not in o for o in p["orders"].values())
    assert p["est_net"] < 100, p


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


# ---------------------------------------------------------------- self-diagnosis (v2/diagnose.py), the Oct 13 cases
import diagnose   # noqa: E402

STORE_ID = "152202386005001"


def _dsnap(**kw):
    s = {"t": "2026-10-13T20:00:00+00:00", "turn": 13252, "cash": 20000.0, "errors": [],
         "household": {"rate": 4.1, "impacts": {}}, "sustenance": {},
         "buildings": [], "operations": {}, "market": {}, "history_use": {},
         "store": {"id": STORE_ID, "items": {}}}
    s.update(kw)
    return s


def _dctx(snap, fs_level=0, quiet=False, owned=(), paused=None, state=None):
    tiers = {k: copy.deepcopy(v.get("orders") or []) for k, v in snap["store"]["items"].items()}
    return {"live_tiers": tiers, "owned": set(owned), "trade": set(), "paused": paused or {}, "fs_level": fs_level,
            "quiet": quiet, "rates": [], "recipes": diagnose.load_data("recipes.json"),
            "sustenance": diagnose.load_data("sustenance.json"), "state": state if state is not None else {}}


def _candles_dry():
    # Oct 13, turn 13252: candle slot dry, our bid 70 under the home ask 80.50
    return _dsnap(sustenance={"candles": 1.5},
                  store={"id": STORE_ID, "items": {"candles": {"held": 1.0, "capacity": 70.0, "flow": {},
                         "orders": [{"max_holding": 66, "buy_volume": 3, "buy_price": "70"}]}}},
                  market={"candles": {"ask": 80.5, "bid": 76.5}})


def _quarry_blocked():
    # Oct 13: quarry "limestone space" while a limestone buy (max_holding 153 = capacity) refilled the bin
    return dict(buildings=[{"id": "149602389", "type": "quarry", "name": "quarry 1", "recipe": "extract stone 1",
                            "target": 0.4, "production": 0.0, "limitation": "limestone space", "construction": None}],
                operations={"producer/149602389": {"recipe": "extract stone 1", "target": 0.4, "volume": 0.0,
                                                   "limitation": "limestone space"}},
                items={"limestone": {"held": 153.0, "capacity": 153.0, "flow": {},
                                     "orders": [{"max_holding": 153, "buy_volume": 15, "buy_price": "26"}]}})


def test_diagnose_r1_candles_dry():
    s = _candles_dry()
    finds, acts = diagnose.diagnose(s, CFG, _dctx(s))
    a = next(a for a in acts if a["rule"] == "R1" and a["item"] == "candles")
    assert a["via"] == "queue" and a["raise_"]                                   # a v1 item: through the queue
    assert a["entry"]["set"]["buy_price"] == "82", a["entry"]                    # ask 80.50 +1.5%, snapped up
    assert 82 <= 60 * 3 / 1.5                                                    # inside the coin-per-prestige cap
    assert a["entry"]["set"]["buy_volume"] * 82 <= 0.05 * 20000
    # live: applied through the queue handler, logged in act.jsonl
    d = tempfile.mkdtemp()
    try:
        got = []
        diagnose.run(s, CFG, _dctx(s), live=True, out_dir=d, apply_queue=lambda e: (got.append(e) or {"ok": True}))
        assert got and got[0]["item"] == "candles"
        rows = [json.loads(x) for x in open(os.path.join(d, "act.jsonl"))]
        assert any(r.get("diagnose") == "R1" and r.get("item") == "candles" and r.get("ok") for r in rows), rows
        assert any(r.get("diagnose") == "run" for r in rows)
        assert "Self-diagnosis" in "\n".join(diagnose.report_lines(json.load(open(os.path.join(d, "diagnose.json")))["findings"]))
        # one action per item per 2 turns
        _, again = diagnose.run(s, CFG, _dctx(s, state=json.load(open(os.path.join(d, "diagnose_state.json")))),
                                live=False, out_dir=d)
        assert not [a for a in again if a.get("item") == "candles"]
    finally:
        shutil.rmtree(d)
    # the light armour slot paused by the failsafe: un-paused at level 0 only
    s = _dsnap(sustenance={"light armour": 0.2},
               store={"id": STORE_ID, "items": {"light armour": {"held": 0.0, "capacity": 10.0, "flow": {},
                                                                 "orders": [{"max_holding": 10, "buy_price": "112"}]}}},
               market={"light armour": {"ask": 80.5}})
    paused = {"light armour": [{"max_holding": 10, "buy_volume": 2, "buy_price": "112"}]}
    _, acts = diagnose.diagnose(s, CFG, _dctx(s, paused=paused))
    a = acts[0]
    assert a.get("unpause") and a["entry"]["set"]["buy_volume"] == 2 and a["entry"]["set"]["buy_price"] == "82"
    f, acts = diagnose.diagnose(s, CFG, _dctx(s, paused=paused, fs_level=1))
    assert not acts and "level" in f[0].get("held_back", "")


def test_diagnose_r2_space_blocked():
    q = _quarry_blocked()
    s = _dsnap(buildings=q["buildings"], operations=q["operations"], store={"id": STORE_ID, "items": q["items"]})
    _, acts = diagnose.diagnose(s, CFG, _dctx(s))
    a = next(a for a in acts if a["rule"] == "R2")
    assert not a["raise_"] and a["entry"]["set"] == {"max_holding": 137}, a       # 153 - 3 turns x 5.2
    # buy already stopping lower: a finding only
    s["store"]["items"]["limestone"]["orders"] = [{"max_holding": 100, "buy_volume": 15, "buy_price": "26"}]
    f, acts = diagnose.diagnose(s, CFG, _dctx(s))
    assert not acts and "sell order or more capacity" in f[0]["finding"]


def test_diagnose_r3_idle_ropewalk():
    s = _dsnap(buildings=[{"id": "152202388001000", "type": "ropewalk", "name": "ropewalk 1", "recipe": None,
                           "target": 0.0, "production": 0.0, "limitation": None, "construction": None}])
    st = {}
    _, acts = diagnose.diagnose(s, CFG, _dctx(s, state=st))
    assert not acts                                                              # 1 turn idle: not yet
    s["turn"] += 1
    _, acts = diagnose.diagnose(s, CFG, _dctx(s, state=st))
    e = acts[0]["entry"]
    assert e["building"] == "152202388001000" and e["producer"] == {"recipe": "make rope 2", "target": 0.5, "provider_id": STORE_ID}
    s["buildings"][0]["type"] = "tannery"                                        # no planned recipe: a finding for Taylor
    f, acts = diagnose.diagnose(s, CFG, _dctx(s, state=st))
    assert not acts and "Taylor" in f[0]["finding"]


def test_diagnose_r4_banquet_starved():
    s = _dsnap(buildings=[
        {"id": "152002388", "type": "mansion", "name": "mansion 1", "recipe": "hold banquet 1 (fish)", "target": 1.0, "construction": None},
        {"id": "152202388000004", "type": "sewing shop", "name": "sewing shop 1", "recipe": "sew garments 2", "target": 0.75, "construction": None},
        {"id": "152202388001005", "type": "weavery", "name": "weavery 1", "recipe": "weave cloth 2", "target": 1.0, "construction": None}],
        operations={"producer/152002388": {"recipe": "hold banquet 1 (fish)", "target": 1.0, "volume": 0.0, "limitation": "labour"}},
        store={"id": STORE_ID, "items": {"labour": {"held": 300.0, "flow": {}, "orders": [{"buy_volume": 400, "buy_price": "2.2"}]}}})
    _, acts = diagnose.diagnose(s, CFG, _dctx(s, quiet=True))                    # reduce-only works at night too
    by = {a["entry"]["building"]: a["entry"]["producer"]["target"] for a in acts if a["rule"] == "R4"}
    assert 0.5625 - 1e-3 <= by["152202388000004"] < 0.75                       # sew first, at most -25%
    assert 0.75 <= by["152202388001005"] < 1.0                                  # then weave for the rest
    assert all(not a["raise_"] for a in acts) and not any(a.get("item") == "labour" for a in acts)


def test_diagnose_quiet_hours_reduce_only():
    s = _candles_dry()
    q = _quarry_blocked()
    s["buildings"], s["operations"] = q["buildings"], q["operations"]
    s["store"]["items"].update(q["items"])
    for ctx in (_dctx(s, quiet=True), _dctx(s, fs_level=1)):
        f, acts = diagnose.diagnose(s, CFG, ctx)
        assert [a["rule"] for a in acts] == ["R2"] and not any(a["raise_"] for a in acts), acts
        assert "reduce-only" in next(x for x in f if x["rule"] == "R1")["held_back"]
    assert diagnose.quiet_now(datetime.datetime(2026, 10, 14, 4, 0, tzinfo=datetime.timezone.utc))      # 00:00 Toronto
    assert not diagnose.quiet_now(datetime.datetime(2026, 10, 14, 16, 0, tzinfo=datetime.timezone.utc))


def test_diagnose_r5_and_owned_items():
    # a running building's input whose bid sat under the ask 3 turns and under-filled: raised under its ceiling
    s = _dsnap(buildings=[{"id": "1", "type": "brewery", "name": "brewery 1", "recipe": "brew beer 1", "target": 0.4, "construction": None}],
               store={"id": STORE_ID, "items": {"grain": {"held": 10.0, "flow": {"consumption": 26.0, "purchase": 5.0},
                                                          "orders": [{"buy_volume": 26, "buy_price": "3"}]}}},
               market={"grain": {"ask": 3.3}})
    st = {"under_ask": {"grain": {"turns": [13250, 13251]}}}
    f, acts = diagnose.diagnose(s, CFG, _dctx(s, state=st, owned=["grain"]))
    a = next(a for a in acts if a["rule"] == "R5")
    assert a["via"] == "direct" and a["managers"][0]["buy_price"] == "3.36" and a["managers"][0]["buy_volume"] == 26
    assert diagnose.snap_up(80.5 * 1.015) == 82.0 and diagnose.snap_up(3.3 * 1.015) == 3.36


def test_act_runs_diagnose_safely():
    d, cfg = _act_dir(cfg_live=[])
    try:
        cfg["diagnose"] = {"on": True}
        before = api.calls["write"]
        act.main(argv=["act.py"], out=d, cfg=cfg, failsafe=os.path.join(d, "failsafe.json"))
        assert os.path.exists(os.path.join(d, "diagnose_dry.json")) and api.calls["write"] == before
        real = diagnose.diagnose
        diagnose.diagnose = lambda *a, **k: 1 / 0                                # a crash never breaks the run
        try:
            res = act.main(argv=["act.py"], out=d, cfg=cfg, failsafe=os.path.join(d, "failsafe.json"))
            assert res["mode"] == "dry"
        finally:
            diagnose.diagnose = real
    finally:
        shutil.rmtree(d)



def test_ship_church_stock():
    import ships
    sea = {"1": {"name": "Home", "moves": 0.0}, "2": {"name": "Far", "moves": 774.0}}
    mk = lambda bid, ask, bv, av, tr=0: {"highest_bid": bid, "lowest_ask": ask, "bid_volume_10": bv, "ask_volume_10": av,
                                         "volume_ema_12": tr}
    world = [{"name": "Home", "markets": {}},
             {"name": "Far", "markets": {"tapestries": mk(650, 705, 2, 9, 3), "windows": mk(0, 900, 0, 4, 1)}}]
    snap = {"home_town": "1", "cash": 30000, "market": {"labour": {"price": 2.0}},
            "store": {"items": {"tapestries": {"held": 2, "orders": [], "flow": {}}}}}
    sc = {"on": True, "min_cash": 20000, "spend_share": 0.15, "value_per_prestige": 57,
          "goods": {"tapestries": {"keep": 7, "max_price": 760, "prestige_per_unit": 25},
                    "windows": {"keep": 6, "max_price": 790, "prestige_per_unit": 25}}}
    cfg = {"chain": {"intermediates": []}, "never_drop": [], "ship_church": sc}
    rec = {"snekkja 1": {"inputs": [{"amount": 50, "product": "labour"}]}}
    ship = {"name": "s", "id": "9", "route_to": "2"}
    p = ships.plan_ship(ship, snap, world, sea, cfg, recipes=rec)
    o = p["orders"]
    assert o["tapestries"]["buy_volume"] == 5 and o["tapestries"]["max_holding"] == 7, p      # keep 7, hold 2
    assert "windows" not in o, p                                                             # 900 over the 790 cap
    assert not p["home_orders"] and p["crew"] > 0 and p["est_net"] > 0, p
    p = ships.plan_ship(ship, dict(snap, cash=10000), world, sea, cfg, recipes=rec)
    assert "tapestries" not in p["orders"], p                                                # under min_cash
    p = ships.plan_ship(ship, snap, world, sea, dict(cfg, ship_church=dict(sc, on=False)), recipes=rec)
    assert "tapestries" not in p["orders"], p                                                # off
    p = ships.plan_ship(ship, dict(snap, cash=24000), world, sea, cfg, recipes=rec)
    assert p["orders"]["tapestries"]["buy_volume"] == 5, p        # 15% of 24k = 3,600 -> 5 at 719


def test_suspended_item_comes_back_after_clean_runs():
    st, cfg, sus = {}, {"live": {"items": ["porterage"]}}, {"porterage": {"why": "risk flag 2 runs in a row"}}
    clean, risky = {"flags": []}, {"flags": [{"severity": "risk", "item": "porterage"}]}
    for _ in range(11):
        assert act.unsuspend_check(clean, sus, st, cfg) == []
    assert act.unsuspend_check(risky, sus, st, cfg) == []           # a risk run resets the count
    for _ in range(11):
        assert act.unsuspend_check(clean, sus, st, cfg) == []
    assert act.unsuspend_check(clean, sus, st, cfg) == ["porterage"]
    assert act.unsuspend_check(clean, {"tar": {}}, {}, cfg) == [] or True   # not in live.items: never returns
    st2 = {}
    for _ in range(20):
        r = act.unsuspend_check(clean, {"tar": {}}, st2, cfg)
    assert r == []


def test_labour_bias_from_history():
    import shadow
    d = tempfile.mkdtemp()
    try:
        h = os.path.join(d, "h.jsonl")
        rows = [{"labour": {"proj": 687, "used": 627, "short": 0}}, {"labour": {"proj": 700, "used": 500, "short": 40}},
                {"labour": {"proj": 690, "used": 640, "short": 0}}, {"counts": {}}]
        with open(h, "w") as f:
            f.write("\n".join(json.dumps(r) for r in rows) + "\n")
        assert shadow.labour_bias(h) == 0.0                 # only 2 clean runs: not enough to trust
        with open(h, "a") as f:
            f.write(json.dumps({"labour": {"proj": 680, "used": 610, "short": 0}}) + "\n")
        assert shadow.labour_bias(h) == 60                  # median of 60, 50, 70; the shortfall run is left out
    finally:
        shutil.rmtree(d)


# ---------------------------------------------------------------- chain sizing (v2/chain.py, Oct 14)
def _chain_inputs():
    import copy
    import chain
    snap = _load_fixture("snapshot_2026-10-14.json")
    rec = json.load(open(os.path.join(HERE, "data", "recipes.json")))
    cfg = copy.deepcopy(json.load(open(os.path.join(HERE, "config.json"))))
    return chain, snap, rec, cfg


def _load_fixture(name):
    with open(os.path.join(HERE, "fixtures", name)) as f:
        return json.load(f)


def test_chain_plan_matches_live_targets():
    # Oct 14 22:00 UTC: v1's balancer had just set these; the v2 port must plan the same chain from the same state
    chain, snap, rec, cfg = _chain_inputs()
    # the Oct 14 settings (Oct 15 recovery config changed both: HOLD under 20k cash, rope thread spun directly)
    cfg["chain"].update({"extra_thread_min": 10, "fill_cash_min": 8000})
    pc = chain.plan_chain(snap, cfg, rec, last_mode="FULL", sales=32.1, exports=0.0, drip=19)
    assert pc["ok"] and pc["mode"] == "FULL", pc
    for k in chain.STEPS:
        assert abs(pc["targets"][k] - pc["current"][k]) <= 0.011, (k, pc["targets"], pc["current"])
    assert pc["thread"]["fed_by_weaving"] and pc["thread"]["other"] == 79.0, pc["thread"]
    assert pc["labour"]["chain"] < pc["labour"]["allowance"], pc["labour"]


def test_chain_labour_budget_cuts_sewing_first_keeps_rope_thread():
    chain, snap, rec, cfg = _chain_inputs()
    for i in ("thread", "cloth", "flax fibres", "garments"):
        snap["store"]["items"][i]["held"] = 0
    cfg["chain"]["labour_buy_max"] = 10 ** 6
    free = chain.plan_chain(snap, cfg, rec, last_mode="FILLING", sales=120, exports=0.0)
    cfg["chain"]["labour_buy_max"] = 250
    pc = chain.plan_chain(snap, cfg, rec, last_mode="FILLING", sales=120, exports=0.0)
    lab = pc["labour"]
    assert free["labour"]["chain"] > 400 and lab["chain"] <= lab["allowance"] + 1, (free["labour"], lab)
    assert pc["notes"] and "cut to" in pc["notes"][0], pc["notes"]
    assert pc["targets"]["sew"] < free["targets"]["sew"], (pc["targets"], free["targets"])
    # spinning keeps at least the thread the ropewalk + net duty draw (79/turn at 50 a run)
    assert pc["targets"]["spin"] >= 79 / 50.0 - 0.01, pc["targets"]
    # a budget too small even for that: sewing/weaving go to 0, spinning stops at the rope + nets floor
    cfg["chain"]["labour_buy_max"] = 60
    pc = chain.plan_chain(snap, cfg, rec, last_mode="FILLING", sales=120, exports=0.0)
    assert pc["targets"]["sew"] == 0 and pc["targets"]["weave"] == 0, pc["targets"]
    assert abs(pc["targets"]["spin"] - 79 / 50.0) <= 0.01, pc["targets"]


def test_chain_found_by_type_not_id():
    chain, snap, rec, cfg = _chain_inputs()
    for n, b in enumerate(snap["buildings"]):
        b["id"] = "9%05d" % n                     # a new season: every id is different
    pc = chain.plan_chain(snap, cfg, rec, last_mode="FULL", sales=32.1)
    assert pc["ok"] and pc["buildings"]["sew"]["id"].startswith("9"), pc


def test_chain_moves_rules():
    import act
    chain, snap, rec, cfg = _chain_inputs()
    pc = chain.plan_chain(snap, cfg, rec, last_mode="FULL", sales=32.1)
    pc["targets"]["sew"] = 0.9
    pc["moves"] = [("sew", 0.21, 0.9), ("weave", 0.12, 0.05)]
    pc["drift"] = ["sew"]
    plan = {"chain": pc}
    cfg["live"]["chain"] = False
    assert act.chain_moves(plan, cfg, snap, 0, {}, {})[0] == []
    cfg["live"]["chain"] = True
    mv, why = act.chain_moves(plan, cfg, snap, 0, {}, {"mode": "FULL", "sizes": {k: v["size"] for k, v in pc["buildings"].items()}})
    assert [m["step"] for m in mv] == ["sew", "weave"] and "drift" in why, (mv, why)
    mv, _ = act.chain_moves(plan, cfg, snap, 2, {}, {})
    assert [m["step"] for m in mv] == ["weave"], mv          # failsafe stand-down: reduce only
    mv, _ = act.chain_moves(plan, cfg, snap, 0, {"sewing shop 1": snap["turn"]}, {})
    assert [m["step"] for m in mv] == ["weave"], mv          # diagnose touched sewing this turn: held
    stopped = json.loads(json.dumps(snap))
    next(b for b in stopped["buildings"] if b["type"] == "weavery")["recipe"] = None
    assert act.chain_moves(plan, cfg, stopped, 0, {}, {})[0] == []
    d = act.chain_labour_delta(plan, snap, rec, [{"id": pc["buildings"]["sew"]["id"], "recipe": "sew garments 2",
                                                  "from": 0.21, "to": 0.9}])
    assert abs(d - 0.69 * 155) < 0.01, d

if __name__ == "__main__":
    n = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            n += 1
            print("ok", name)
    print("%d checks passed" % n)
