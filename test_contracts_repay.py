"""Regression test: the loan repayment POST must send an integer volume (the API refuses 1600.0)."""
import json, os, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import types
# stub the game client (merc_status4 asks for live credentials at import); the repay path only needs num() and get()
stub = types.ModuleType("merc_status4")
stub.num = lambda x, default=0.0: float(x) if x not in (None, "") else default
stub.get = lambda *a, **k: {}
sys.modules["merc_status4"] = stub
import contracts
import order_queue as q

q.log = lambda *a, **k: None  # keep the real queue log untouched
contracts.LOAN_STATE = os.path.join(tempfile.mkdtemp(), "loan.json")
sent = []

def fake_get(path, *a, **k):
    if path == "/contracts/%s" % contracts.LOAN_ID:
        if sent:
            return {"transactions": [{"id": "1", "asset": "money", "stage": "done", "volume": 0}]}
        return {"transactions": [{"id": "1", "asset": "money", "stage": "open", "volume": 1600.0}]}
    return {}

def fake_post(path, body):
    sent.append(body)
    return True, 200, "{}"

st = contracts.repay_loan(cash=3572, turn=13682, post=fake_post, get=fake_get)
assert sent, "no repayment POST was made"
assert isinstance(sent[0]["volume"], int), sent[0]
assert sent[0]["volume"] == 1600, sent[0]
assert st.get("repaid"), st
print("ok: repay POST volume is int", sent[0]["volume"], "repaid", st.get("repaid"))
