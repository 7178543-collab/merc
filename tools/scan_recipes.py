# Season 9 recipe scan (Oct 28 2026): python tools/scan_recipes.py <max tier>; run from the repo root. Writes JSON to /home/claude/scratch (edit the path).
import json,gzip,statistics as st,sys
R=json.load(open('v2/data/recipes.json')); B=json.load(open('v2/data/buildings.json'))
W=json.load(gzip.open('state/dump/world.json.gz'))['towns']
def f(x):
    try:return float(x)
    except:return None
price={};depth={};ntown={}
items=set()
for t in W.values(): items|=set(t)
for it in items:
    ps=[];ds=[]
    for t in W.values():
        e=t.get(it)
        if e and e[5]:
            p=f(e[5]);d=f(e[4]) or 0
            ps.append(p)
            if d>0: ds.append(d)
    if ps:
        price[it]=st.median(ps); ntown[it]=len(ps)
        depth[it]=st.median(ds) if ds else 0
LAB=1.8; SPREAD=0.06; CAP=0.30
def cost_of(mat):
    return sum(price.get(k,0)*v for k,v in mat.items() if k!='labour')+mat.get('labour',0)*LAB
rows=[]
for n,r in R.items():
    if 'outputs' not in r or 'inputs' not in r: continue
    if r.get('tier',9)>int(sys.argv[1] if len(sys.argv)>1 else 1): continue
    ins=r['inputs'];outs=r['outputs']
    lab=sum(i['amount'] for i in ins if i['product']=='labour')
    if lab<=0: continue
    ok=True;cin=0;lim=1e9
    for i in ins:
        if i['product']=='labour': continue
        p=price.get(i['product'])
        if not p or ntown.get(i['product'],0)<20: ok=False;break
        cin+=p*(1+SPREAD)*i['amount']
        lim=min(lim,CAP*depth.get(i['product'],0)/i['amount'])
    if not ok: continue
    val=0
    for o in outs:
        p=price.get(o['product'])
        if not p or ntown.get(o['product'],0)<20 or depth.get(o['product'],0)<=0: ok=False;break
        val+=p*(1-SPREAD)*o['amount']
        lim=min(lim,CAP*depth[o['product']]/o['amount'])
    if not ok: continue
    marg=val-cin-lab*LAB
    site=r['site']; b=B.get(site,{})
    con=b.get('construction',{}).get('materials',{})
    cap=cost_of(con) if con else None
    vol=lim; prof=marg*vol-6
    rows.append(dict(recipe=n,tier=r.get('tier'),site=site,lab_per_vol=lab,margin_per_vol=round(marg,1),m_per_lab=round(marg/lab,2),
        vol=round(vol,2),labour_turn=round(lab*vol),profit_turn=round(prof),build_cost=None if cap is None else round(cap),
        payback=None if (cap is None or prof<=0) else round(cap/prof),out=outs[0]['product'],typ_depth=round(depth[outs[0]['product']],1),price=round(price[outs[0]['product']],2)))
rows.sort(key=lambda x:-x['profit_turn'])
json.dump(rows,open('state/scan_t%s.json'%(sys.argv[1] if len(sys.argv)>1 else 1),'w'),indent=1)
print(len(rows))
for x in rows[:25]:
    print(f"{x['profit_turn']:5} /turn  {x['recipe']:22}T{x['tier']} {x['site']:15} m/lab {x['m_per_lab']:5} vol {x['vol']:6} lab/turn {x['labour_turn']:5} build {x['build_cost']} payback {x['payback']} out {x['out']} px {x['price']} depth {x['typ_depth']}")
