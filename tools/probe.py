"""Read-only probe (Claude, Oct 2026): dumps a transport and greps the game's web bundle for API paths. Never prints credentials."""
import json, re, sys, urllib.request
sys.path.insert(0, ".")
import merc_status4 as m

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
    for mt in re.finditer(r'.{0,250}[A-Za-z]+Resource\)?\(`/transports[^`]*`.{0,250}', js):
        frag = mt.group(0)
        if frag not in seen:
            seen.add(frag); print("JS", frag.replace("\n", " "))
print("bundles", len(srcs))
