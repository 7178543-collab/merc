"""Tests for guardian.py (pure decision functions). python v2/test_guardian.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import guardian as g

C = dict(g.DEFAULTS, live=True, _live=True)
B = lambda i, name, rec, tgt: {"id": i, "name": name, "recipe": rec, "target": tgt}
GOOD = [B("1", "flax farm 1", "grow flax 1", 6.3), B("2", "retting pit 1", "retting 1", 1.1), B("3", "spinnery 1", "spin thread 1", 1.6)]
BAD = [B("1", "flax farm 1", "make flax fibres 1", 2.75), B("2", "retting pit 1", "retting 1", 1.0), B("3", "spinnery 1", "spin thread 1", 1.86)]


def hist(cashes, start=100, bld=None):
    return [{"turn": start + i, "cash": c, "bld": bld or []} for i, c in enumerate(cashes)]


def test_known_good_recorded_only_when_healthy():
    h = hist([4000] * 30)
    st, e, n = g.decide(129, 4000, 1000, 200, h, [], GOOD, {}, C)
    assert len(st["known_good"]) == 1 and e == []
    st2, _, _ = g.decide(131, 4000, 1000, 200, h, [], GOOD, st, C)      # under kg_gap_turns: no second record
    assert len(st2["known_good"]) == 1
    st3, _, _ = g.decide(129, 1500, 1000, 200, hist([1500] * 30), [], GOOD, {}, C)   # cash < 2 x floor: not healthy
    assert not st3.get("known_good")
    st4, _, _ = g.decide(129, 4000, 1000, 200, hist([6000] * 30), [], GOOD, {}, C)    # sliding (4000 < 0.9 x 6000)
    assert not st4.get("known_good")


def test_slide_with_goal_move_rolls_back_and_freezes():
    kg = {"turn": 100, "cash": 4000, "buildings": [dict(b) for b in GOOD]}
    h = hist([4000] * 12 + [3900, 3000, 1800, 1000, 900] + [900] * 20)
    moves = [{"turn": 120, "ok": True, "dry": False}]
    st, e, n = g.decide(135, 900, 1000, 200, h, moves, BAD, {"known_good": [kg]}, C)
    assert len(e) >= 1 and e[0]["building"] == "1" and e[0]["producer"]["recipe"] == "grow flax 1", e
    assert st["freeze_until_turn"] == 135 + 48 and "GUARDIAN ROLLBACK" in st["alert"]
    # cooldown: a second trigger within 48 turns does nothing
    st2, e2, _ = g.decide(140, 800, 1000, 200, h, moves, BAD, st, C)
    assert e2 == []


def test_slide_without_goal_move_does_not_roll_back():
    kg = {"turn": 100, "cash": 4000, "buildings": [dict(b) for b in GOOD]}
    h = hist([4000] * 12 + [900] * 23)
    st, e, _ = g.decide(134, 900, 1000, 200, h, [], BAD, {"known_good": [kg]}, C)
    assert e == []


def test_starvation_triggers():
    bld = [["retting pit 1", "retting 1", 0.0, 1.0, None], ["spinnery 1", "spin thread 1", 0.3, 1.9, None],
           ["flax farm 1", "grow flax 1", 5.0, 5.0, None]]
    h = hist([2500] * 30, bld=bld)
    assert g.starved_buildings(h, C) == ["retting pit 1", "spinnery 1"]
    kg = {"turn": 100, "cash": 4000, "buildings": [dict(b) for b in GOOD]}
    st, e, _ = g.decide(129, 2500, 1000, 200, h, [], BAD, {"known_good": [kg]}, C)
    assert len(e) >= 1 and st["freeze_until_turn"] > 129
    one = hist([2500] * 30, bld=bld[:1] + bld[2:])                       # only one starved building: no trigger
    assert g.starved_buildings(one, C) == ["retting pit 1"]
    st2, e2, _ = g.decide(129, 2500, 1000, 200, one, [], BAD, {"known_good": [kg]}, C)
    assert e2 == []


def test_no_known_good_alerts_without_sending():
    bld = [["retting pit 1", "retting 1", 0.0, 1.0, None], ["spinnery 1", "spin thread 1", 0.3, 1.9, None]]
    st, e, _ = g.decide(129, 2500, 1000, 200, hist([2500] * 30, bld=bld), [], BAD, {}, C)
    assert e == [] and "no known-good" in st["alert"] and not st.get("freeze_until_turn")


def test_floor_ratchets_up_only():
    h = hist([4000] * 30)
    st, _, _ = g.decide(129, 4000, 1000, 200, h, [], GOOD, {}, C)
    assert st["hard_floor"] == 1600.0
    st2, _, _ = g.decide(130, 1500, 1000, 200, hist([4000] * 29 + [1500]), [], GOOD, st, C)
    assert st2["hard_floor"] == 1600.0                                    # a lower cash never lowers it
    st3, _, _ = g.decide(129, 1700, 1000, 200, h, [], GOOD, {}, C)       # 1700 < 1600 + 500: no ratchet yet
    assert not st3.get("hard_floor")


def test_restore_skips_same_and_construction():
    kg = {"turn": 1, "cash": 1, "buildings": [dict(b) for b in GOOD]}
    snap = [B("1", "flax farm 1", "grow flax 1", 6.3), dict(B("2", "retting pit 1", "retting 1", 0.2), construction=True), BAD[2]]
    e = g.restore_entries(kg, snap)
    assert [x["building"] for x in e] == ["3"], e


def test_readers_ignore_state_when_not_live():
    old = g.cfg
    try:
        g.cfg = lambda: dict(g.DEFAULTS, live=False)
        assert g.frozen(10**9) is False and g.floor_override(1000) == 1000.0
    finally:
        g.cfg = old


def test_debt_is_not_a_cushion():
    h = hist([4000] * 30)
    st, _, _ = g.decide(129, 4000, 1000, 200, h, [], GOOD, {}, C, debt=3000)   # 4000 - 3000 < 2 x floor
    assert not st.get("known_good") and not st.get("hard_floor")
    assert st["debt"] == 3000 and st["free_cash"] == 1000
    st2, _, _ = g.decide(129, 4000, 1000, 200, h, [], GOOD, {}, C, debt=0)
    assert len(st2["known_good"]) == 1 and st2["hard_floor"] == 1600.0


def test_honest_burn_sees_stock_sales():
    h = hist([1000] * 30)                                                     # cash flat ...
    trend = {"per_turn_24": -150.0}                                           # ... value falling 150/turn
    st, _, n = g.decide(129, 1000, 1000, 200, h, [], GOOD, {}, C, trend=trend)
    assert st["burn"]["flattered"] is True and "HONEST BURN" in st["burn_alert"] and "stock" in st["burn_alert"]
    st2, _, _ = g.decide(129, 1000, 1000, 200, h, [], GOOD, st, C, trend={"per_turn_24": -20.0})
    assert "burn_alert" not in st2                                            # small burn: no alert, old alert cleared
    st3, _, _ = g.decide(129, 1000, 1000, 200, hist([1000 + 10 * i for i in range(30)]), [], GOOD, {}, C, trend={"per_turn_24": 5.0})
    assert st3["burn"]["alert"] is None


def test_honest_burn_cash_falling_is_not_flattered():
    b = g.honest_burn({"per_turn_24": -200.0}, -190.0, C)
    assert b["flattered"] is False and b["alert"].startswith("HONEST BURN")
    assert g.honest_burn({}, 5.0, C)["alert"] is None


if __name__ == "__main__":
    n = 0
    for k, v in sorted(globals().items()):
        if k.startswith("test_"):
            v(); n += 1
    print("guardian: %d tests ok" % n)
