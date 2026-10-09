"""Read-only probe (Claude, Oct 2026): dumps a transport and greps the game's web bundle for API paths. Never prints credentials."""
import json, re, sys, urllib.request, urllib.error
sys.path.insert(0, ".")
import merc_status4 as m

if sys.argv[1:2] == ["--mainjs"]:
    import gzip, zlib, os
    os.makedirs("state/dump/js", exist_ok=True)
    for name in sys.argv[2:]:
        req = urllib.request.Request("https://play.mercatorio.io/static/js/" + name,
                                     headers={"Accept-Encoding": "identity", "User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=60) as r:
            raw, enc = r.read(), r.headers.get("Content-Encoding")
        if enc == "gzip" or raw[:2] == b"\x1f\x8b":
            raw = gzip.decompress(raw)
        elif enc == "deflate":
            raw = zlib.decompress(raw)
        elif enc == "br":
            import brotli
            raw = brotli.decompress(raw)
        open("state/dump/js/full_" + name, "wb").write(raw)
        print("saved", name, len(raw), "enc", enc)
    sys.exit(0)
if sys.argv[1:2] == ["--ship"]:
    for tid in sys.argv[2:]:
        t = m.get("/transports/%s" % tid) or {}
        inv = t.get("inventory") or {}
        r = t.get("route") or {}
        print("SHIP", t.get("name"), "town", t.get("town_id"), "loc", t.get("location"), "prev_op", t.get("previous_operation"))
        print("  inv prev_flows", json.dumps(inv.get("previous_flows"))[:500])
        print("  route trips", r.get("potential_trips"), r.get("actual_trips"), "res exp/imp", r.get("reserved_export"), r.get("reserved_import"))
        print("  route holdings", json.dumps({k: v.get("managers") for k, v in (r.get("holdings") or {}).items() if v.get("managers")})[:600])
        print("  route prev_flows", json.dumps(r.get("previous_flows"))[:500])
        print("  journey", json.dumps({k: v for k, v in (t.get("journey") or {}).items() if k != "legs"}))
    b = m.get("/buildings/152202386005001") or {}
    print("STORE labour flow", json.dumps(((b.get("storage") or {}).get("inventory") or {}).get("previous_flows", {}).get("labour")))
    sys.exit(0)
if sys.argv[1:2] == ["--link-test"]:
    bid, store = sys.argv[2], sys.argv[3]
    def prov():
        return ((m.get("/buildings/%s" % bid) or {}).get("producer") or {}).get("provider_id")
    R = "hold banquet 1 (fish)"
    cands = [("PATCH", "/buildings/%s/producer" % bid, {"target": "1", "provider_id": store}),
             ("PATCH", "/buildings/%s/producer" % bid, {"target": "1", "provider": store}),
             ("PUT", "/buildings/%s/producer" % bid, {"target": "1", "recipe": R, "provider_id": store, "manager": "static"}),
             ("PATCH", "/buildings/%s/producer" % bid, {"target": "1", "provider_id": int(store)}),
             ("PUT", "/buildings/%s/producer/provider" % bid, {"provider_id": store}),
             ("PATCH", "/buildings/%s" % bid, {"provider_id": store})]
    print("before", prov())
    for method, path, body in cands:
        req = urllib.request.Request("https://play.mercatorio.io/api" + path, data=json.dumps(body).encode(), method=method,
            headers={"X-Merc-User": m.USER, "Authorization": "Bearer " + m.TOKEN, "Content-Type": "application/json", "Accept": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                res = "%s %s" % (r.status, r.read().decode()[:150])
        except urllib.error.HTTPError as e:
            res = "%s %s" % (e.code, e.read().decode()[:200])
        now = prov()
        print("TRY", method, path, json.dumps(body), "->", res.replace("\n", " "), "| provider now:", now)
        if now:
            break
    sys.exit(0)
if sys.argv[1:2] == ["--dump"]:
    import os
    os.makedirs("state/dump/js", exist_ok=True)
    def save(name, obj):
        with open("state/dump/%s.json" % name, "w") as f:
            json.dump(obj, f, default=str)
    pl = m.get("/player") or {}
    hh = pl.get("household") or {}
    save("player", pl)
    save("household", m.get("/households/%s" % hh.get("id")) or {})
    biz = m.get("/businesses/%s" % hh["business_ids"][0]) or {}
    save("business", biz)
    for b in biz.get("buildings", []):
        save("bld_%s_%s" % (b.get("type"), b["id"]), m.get("/buildings/%s" % b["id"]) or {})
    for tid in biz.get("transport_ids", []):
        save("transport_%s" % tid, m.get("/transports/%s" % tid) or {})
    for path in ("/contracts/towns/152202387", "/towns/152202387"):
        try: save(path.strip("/").replace("/", "_"), m.get(path) or {})
        except SystemExit: pass
    html = urllib.request.urlopen("https://play.mercatorio.io/", timeout=30).read().decode("utf8", "ignore")
    srcs = set(re.findall(r'(?:src|href)="([^"]+\.js)"', html)); done = set()
    while srcs:
        s0 = srcs.pop()
        if s0 in done: continue
        done.add(s0)
        url = s0 if s0.startswith("http") else "https://play.mercatorio.io" + ("" if s0.startswith("/") else "/") + s0
        try: js = urllib.request.urlopen(url, timeout=30).read().decode("utf8", "ignore")
        except Exception: continue
        with open("state/dump/js/" + re.sub(r"[^\w.-]", "_", s0)[-80:], "w") as f: f.write(js)
        for more in re.findall(r'["\']([\w./-]+\.js)["\']', js):
            if more not in done: srcs.add(more)
    try:
        md = json.loads(urllib.request.urlopen("https://api.mercatorio-tools.tech/data/marketdata", timeout=90).read())
        save("marketdata", md)
    except Exception as e:
        print("MDFAIL", e)
    print("dumped", len(os.listdir("state/dump")), "files,", len(done), "js")
    sys.exit(0)
if sys.argv[1:2] == ["--site"]:
    site = sys.argv[2]
    pl = m.get("/player") or {}
    biz = m.get("/businesses/%s" % (pl.get("household") or {})["business_ids"][0]) or {}
    for b in biz.get("buildings", []):
        if b.get("type") == site:
            full = m.get("/buildings/%s" % b["id"]) or {}
            keep = {k: full.get(k) for k in full if k not in ("storage", "_embedded", "domain", "producer")}
            print("BLD", json.dumps(keep, default=str)[:2000])
            prod = full.get("producer") or {}
            print("PRODUCER", json.dumps({k: v for k, v in prod.items() if k != "inventory"}, default=str)[:2000])
    html = urllib.request.urlopen("https://play.mercatorio.io/", timeout=30).read().decode("utf8", "ignore")
    srcs = set(re.findall(r'(?:src|href)="([^"]+\.js)"', html)); done = set()
    while srcs:
        s0 = srcs.pop()
        if s0 in done: continue
        done.add(s0)
        url = s0 if s0.startswith("http") else "https://play.mercatorio.io" + ("" if s0.startswith("/") else "/") + s0
        try: js = urllib.request.urlopen(url, timeout=30).read().decode("utf8", "ignore")
        except Exception: continue
        for more in re.findall(r'["\']([\w./-]+\.js)["\']', js):
            if more not in done: srcs.add(more)
        for mt in re.finditer(r'\{"name":"[^"]*","tier":\d+,"site":"%s".{0,700}' % re.escape(site), js):
            print("RECIPE", mt.group(0))
        for mt in re.finditer(r'"%s":\{"text".{0,600}' % re.escape(site), js):
            print("TEXT", mt.group(0))
        for mt in re.finditer(r'.{0,200}"type":"%s".{0,600}' % re.escape(site), js):
            print("TYPE", mt.group(0)[:800])
    sys.exit(0)
if sys.argv[1:2] == ["--prestige"]:
    pl = m.get("/player") or {}
    hh = pl.get("household") or {}
    h = m.get("/households/%s" % hh.get("id")) or {}
    def walk(o, path=""):
        if isinstance(o, dict):
            for k, v in o.items():
                walk(v, path + "/" + str(k))
        elif isinstance(o, list):
            for i, v in enumerate(o[:40]):
                walk(v, path + "[%d]" % i)
        else:
            if re.search(r"prestige|legacy|sustenance|influence|reput|caps|donat|maint|bonus|upkeep|decay", path, re.I):
                print("H", path, o)
    walk(h); walk(pl, "/player")
    sys.exit(0)
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
