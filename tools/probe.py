"""Read-only probe (Claude, Oct 2026): dumps a transport and greps the game's web bundle for API paths. Never prints credentials."""
import json, re, sys, urllib.request, urllib.error
sys.path.insert(0, ".")
import merc_status4 as m

if sys.argv[1:2] == ["--status"]:
    pl = m.get("/player") or {}
    hh = pl.get("household") or {}
    biz = m.get("/businesses/%s" % hh["business_ids"][0]) or {}
    for b in biz.get("buildings", []):
        if b.get("type") in ("park", "farmstead") or "construction" in json.dumps(b)[:4000]:
            full = m.get("/buildings/%s" % b["id"]) or {}
            keep = {k: full.get(k) for k in full if k not in ("storage", "_embedded", "inventory")}
            print("BLD", b.get("type"), json.dumps(keep, default=str)[:2500])
    try:
        md = json.loads(urllib.request.urlopen("https://api.mercatorio-tools.tech/data/marketdata", timeout=60).read())
        txt = json.dumps(md)
        print("MD type", type(md).__name__, "len", len(txt))
        for good in sys.argv[2:]:
            for mt in list(re.finditer(r'.{0,200}"%s".{0,300}' % re.escape(good), txt))[:4]:
                print("MD", good, mt.group(0))
    except Exception as e:
        print("MDFAIL", e)
    sys.exit(0)
if sys.argv[1:2] == ["--route-test"]:
    tid, item, body = sys.argv[2], sys.argv[3], sys.argv[4]
    for shape in (json.loads(body), {"managers": json.loads(body)}):
        req = urllib.request.Request("https://play.mercatorio.io/api/transports/%s/route/inventory/%s" % (tid, item),
            data=json.dumps(shape).encode(), method="PATCH",
            headers={"X-Merc-User": m.USER, "Authorization": "Bearer " + m.TOKEN, "Content-Type": "application/json", "Accept": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                out = json.loads(r.read().decode())
                print("SHAPE", list(shape)[:3], r.status, "managers:", json.dumps(out.get("managers"))[:400], "keys:", sorted(out)[:30])
        except urllib.error.HTTPError as e:
            print("SHAPE", list(shape)[:3], e.code, e.read().decode()[:400])
        t = m.get("/transports/%s" % tid) or {}
        print("AFTER GET managers:", json.dumps((t.get("route") or {}).get("managers"))[:400])
        if ((t.get("route") or {}).get("managers") or {}).get(item):
            break
    sys.exit(0)
for tid in sys.argv[1:]:
    t = m.get("/transports/%s" % tid) or {}
    r = t.get("route") or {}
    slim = {k: t.get(k) for k in ("id", "name", "type", "town_id", "state", "capacity", "journey", "provider_id") if k in t}
    slim["route"] = {k: r.get(k) for k in ("id", "local_town", "remote_town", "distance", "capacity", "managers")}
    slim["keys"] = sorted(t.keys())
    j = dict(t.get("journey") or {}); j.pop("legs", None); slim["journey"] = j
    slim["route"]["managers"] = {k: v for k, v in (r.get("managers") or {}).items()}
    for k in ("location", "procedure", "previous_operation", "reference", "hometown_id"):
        slim[k] = t.get(k)
    print("TRANSPORT", tid, json.dumps(slim, default=str)[:3000])

print("ts", __import__("datetime").datetime.utcnow().isoformat())
import sys as _s; _s.exit(0)
html = urllib.request.urlopen("https://play.mercatorio.io/", timeout=30).read().decode("utf8", "ignore")
srcs = set(re.findall(r'(?:src|href)="([^"]+\.js)"', html))
seen = set()
for s in list(srcs):
    url = s if s.startswith("http") else "https://play.mercatorio.io" + ("" if s.startswith("/") else "/") + s
    try:
        js = urllib.request.urlopen(url, timeout=30).read().decode("utf8", "ignore")
    except Exception as e:
        print("JSFAIL", url, e); continue
    for more in re.findall(r'["\']([\w./-]+\.js)["\']', js):
        srcs.add(more)
    for mt in [] or re.finditer(r'.{0,250}[A-Za-z]+Resource\)?\(`/transports[^`]*`.{0,250}', js):
        frag = mt.group(0)
        if frag not in seen:
            seen.add(frag); print("JS", frag.replace("\n", " "))
print("bundles", len(srcs))
