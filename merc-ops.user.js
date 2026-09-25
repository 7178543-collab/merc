// ==UserScript==
// @name         Merc Ops panel
// @namespace    strasclives
// @version      1.5
// @description  30-second ops panel for Mercatorio: issues with one-tap fixes, production start/stop/+/- and chain balancing, orders, builds, boat, contracts.
// @match        https://play.mercatorio.io/*
// @grant        none
// @run-at       document-idle
// ==/UserScript==
//
// Runs inside the game page and uses your normal logged-in game session
// (same requests the game's own buttons send). No API token, no server.
// Everything it changes is a tap you make; Stop asks to confirm first.

(function () {
  'use strict';
  if (window.__mercOps) return;
  window.__mercOps = true;

  // ---------------------------------------------------------------- config
  const VERSION = '1.5';
  const BUSINESS = '39992';
  const HOUSEHOLD = '21623';
  const STORE = '152202386005001';
  const TOWN = '152202387';
  const SKIP_ITEMS = new Set(['money', 'handcart', 'tumbrel', 'snekkja', 'cog', 'lodging']);
  // recipe to use when starting a building that has none (remembered after a Stop)
  const DEFAULT_RECIPES = { 'brewery': 'brew beer 1', 'logging camp': 'split timber 2', 'park': 'maintain 1' };

  // ---------------------------------------------------------------- helpers
  const api = async (path, method = 'GET', body) => {
    const r = await fetch('/api' + path, {
      method, credentials: 'same-origin',
      headers: body ? { 'Content-Type': 'application/json', 'Accept': 'application/json' } : { 'Accept': 'application/json' },
      body: body ? JSON.stringify(body) : undefined,
    });
    const txt = await r.text();
    if (!r.ok) throw new Error(method + ' ' + path + ' -> ' + r.status + ' ' + txt.slice(0, 160));
    try { return JSON.parse(txt); } catch (e) { return txt; }
  };
  const num = x => { const n = parseFloat(x); return isNaN(n) ? 0 : n; };
  const f1 = x => { const n = num(x); return Math.abs(n) >= 100 ? n.toFixed(0) : (+n.toFixed(1)).toString(); };
  const f2 = x => (+num(x).toFixed(2)).toString();
  // game price grid: 3 significant digits; above 2 the last digit must be even
  const snap = (p, dir = 0) => {
    if (p <= 0) return p;
    const e = Math.floor(Math.log10(p)) - 2;
    const lead = Math.floor(p / Math.pow(10, e + 2) + 1e-9);
    const step = Math.pow(10, e) * (lead > 2 ? 2 : 1);
    const n = p / step;
    const k = dir > 0 ? Math.ceil(n - 1e-9) : dir < 0 ? Math.floor(n + 1e-9) : Math.round(n);
    return +(k * step).toFixed(6);
  };
  const sgn = x => (x >= 0 ? '+' : '−') + Math.round(Math.abs(x)).toLocaleString();
  const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const store = {
    get(k, d) { try { const v = localStorage.getItem('mercops:' + k); return v == null ? d : JSON.parse(v); } catch (e) { return d; } },
    set(k, v) { try { localStorage.setItem('mercops:' + k, JSON.stringify(v)); } catch (e) {} },
  };

  // ---------------------------------------------------------------- styles
  const css = `
  #mo-btn{position:fixed;right:10px;bottom:10px;z-index:99999;background:#1f5130;color:#fff;border:0;border-radius:22px;
    padding:10px 14px;font:600 15px system-ui,sans-serif;box-shadow:0 2px 8px rgba(0,0,0,.35)}
  #mo-btn .dot{display:inline-block;min-width:18px;margin-left:6px;padding:0 5px;border-radius:9px;background:#c0392b;font-size:12px}
  #mo{--mo-good:#1f8a4c;--mo-bad:#c0392b;position:fixed;inset:0;z-index:99998;background:#f6f1e4;color:#222;overflow:auto;font:14px/1.35 system-ui,sans-serif;display:none}
  #mo.open{display:block}
  #mo *,#mo-btn,#mo-toast{box-sizing:border-box;text-shadow:none;letter-spacing:normal;text-transform:none}
  #mo div,#mo span,#mo b,#mo p,#mo h4{color:inherit;font-family:system-ui,sans-serif}
  #mo button{width:auto;height:auto;margin:0;min-height:0;line-height:1.2;font-family:system-ui,sans-serif}
  #mo nav button{color:#555}
  #mo input{height:auto;margin:0}
  #mo header{position:sticky;top:0;background:#1f5130;color:#fff;padding:10px 12px;display:flex;gap:8px;align-items:center;z-index:2}
  #mo header b{flex:1;font-size:15px}
  #mo header button{background:#fff2;color:#fff;border:1px solid #fff5;border-radius:6px;padding:6px 10px;font-size:14px}
  #mo nav{display:flex;position:sticky;top:44px;background:#e9e1cc;z-index:2}
  #mo nav{overflow-x:auto}
  #mo nav button{flex:1 0 auto;border:0;background:none;padding:10px 8px;font:600 13px system-ui;color:#555;border-bottom:3px solid transparent}
  #mo nav button.on{color:#1f5130;border-bottom-color:#1f5130}
  #mo section{padding:8px 10px 80px}
  #mo .card{background:#fff;border:1px solid #ddd3bb;border-radius:8px;padding:9px 10px;margin:7px 0}
  #mo .row{display:flex;align-items:center;gap:6px;flex-wrap:wrap}
  #mo .grow{flex:1;min-width:120px}
  #mo .muted{color:#777;font-size:12px}
  #mo .bad{border-left:4px solid #c0392b}
  #mo .warn{border-left:4px solid #d68910}
  #mo .ok{border-left:4px solid #1f8a4c}
  #mo button.a,#mo button.b,#mo button.r{min-height:40px}
  #mo .ctl{display:grid;grid-template-columns:repeat(5,1fr);gap:6px;margin-top:8px}
  #mo .ctl button{width:100%}
  #mo .search{width:100%;padding:9px;margin:4px 0 2px;font-size:15px}
  #mo button.a{border:1px solid #1f5130;background:#1f5130;color:#fff;border-radius:6px;padding:7px 10px;font:600 13px system-ui}
  #mo button.b{border:1px solid #b9ad8f;background:#fff;color:#333;border-radius:6px;padding:7px 10px;font:600 13px system-ui;min-width:38px}
  #mo button.r{border:1px solid #c0392b;background:#fff;color:#c0392b;border-radius:6px;padding:7px 10px;font:600 13px system-ui}
  #mo input{width:64px;padding:6px;border:1px solid #b9ad8f;border-radius:5px;font-size:14px}
  #mo .kpi{display:flex;gap:6px;flex-wrap:wrap;margin:6px 0}
  #mo .kpi div{background:#fff;border:1px solid #ddd3bb;border-radius:8px;padding:6px 9px;font-size:13px}
  #mo .bar{height:6px;background:#eee;border-radius:3px;overflow:hidden;margin-top:4px}
  #mo .bar i{display:block;height:100%;background:#1f8a4c}
  #mo-toast{position:fixed;left:10px;right:10px;bottom:62px;z-index:100000;background:#222;color:#fff;padding:10px 12px;border-radius:8px;
    font:14px system-ui;display:none}
  @media (prefers-color-scheme: dark){
    #mo{background:#1c1b18;color:#eee;--mo-good:#6fcf8f;--mo-bad:#ff7b6b}
    #mo nav{background:#2a2822}
    #mo .card,#mo .kpi div{background:#26241f;border-color:#3a372f}
    #mo button.b{background:#26241f;color:#eee;border-color:#555}
    #mo input{background:#26241f;color:#eee;border-color:#555}
    #mo .muted{color:#aaa}
    #mo nav button{color:#bbb}
    #mo nav button.on{color:#7ed49b;border-bottom-color:#7ed49b}
  }`;
  const st = document.createElement('style'); st.textContent = css; document.head.appendChild(st);

  const btn = document.createElement('button'); btn.id = 'mo-btn'; btn.textContent = 'Ops';
  const panel = document.createElement('div'); panel.id = 'mo';
  const toastEl = document.createElement('div'); toastEl.id = 'mo-toast';
  document.body.append(btn, panel, toastEl);
  let toastT;
  const toast = (msg, ms = 2600) => { toastEl.textContent = msg; toastEl.style.display = 'block'; clearTimeout(toastT); toastT = setTimeout(() => toastEl.style.display = 'none', ms); };

  let tab = store.get('tab', 'issues');
  let S = null;             // last loaded state
  let busy = false;

  btn.onclick = () => { panel.classList.add('open'); load(); };

  // ---------------------------------------------------------------- data
  // cash per turn, first value seen in each turn (kept for ~2 days of turns)
  function money(flows, cash, turn) {
    let sale = 0, buy = 0;
    for (const v of Object.values(flows || {})) { sale += num(v.sale_value); buy += num(v.purchase_cost); }
    const hist = store.get('cash', {});
    if (turn && hist[turn] == null) { hist[turn] = cash; const ks = Object.keys(hist).map(Number).sort((a, b) => a - b); while (ks.length > 48) delete hist[ks.shift()]; store.set('cash', hist); }
    const ks = Object.keys(hist).map(Number).filter(k => k < turn).sort((a, b) => b - a);
    const prev = ks.length ? ks[0] : null;
    return { profit: sale - buy, sales: sale, buys: buy, delta: prev != null ? cash - hist[prev] : null, deltaTurns: prev != null ? turn - prev : 0 };
  }
  function prestigeInfo(hh) {
    const board = hh.prestige_board || {};
    const total = num(hh.prestige);
    const rate = (hh.prestige_impacts || board.prestige_impacts || []).reduce((a, x) => a + num(x.impact), 0);
    return { free: total - num(board.allocated), rate, total };
  }

  async function load() {
    if (busy) return; busy = true;
    panel.innerHTML = '<header><b>Merc Ops</b><button data-x="close">Close</button></header><section>Loading…</section>';
    wire();
    try {
      const [biz, sh, hh, md, clk] = await Promise.all([
        api('/businesses/' + BUSINESS), api('/buildings/' + STORE),
        api('/households/' + HOUSEHOLD).catch(() => ({})),
        api('/towns/' + TOWN + '/marketdata').catch(() => ({})),
        api('/clock').catch(() => ({})),
      ]);
      const ids = (biz.building_ids || []).filter(id => id !== STORE);
      const [blds, boats, myC, townC, towns, notes] = await Promise.all([
        Promise.all(ids.map(id => api('/buildings/' + id).catch(() => null))),
        Promise.all((biz.transport_ids || []).map(id => api('/transports/' + id).catch(() => null))),
        api('/businesses/' + BUSINESS + '/contracts').catch(() => ({})),
        api('/contracts/towns/' + TOWN).catch(() => ({})),
        townNames(),
        api('/notifications').catch(() => []),
      ]);
      const inv = (sh.storage || {}).inventory || {};
      S = {
        boats: boats.filter(Boolean),
        myContracts: (myC.contracts || []),
        townContracts: (townC.contracts || []),
        towns,
        notes: Array.isArray(notes) ? notes : [],
        cash: num(((inv.account || {}).assets || {}).money?.balance),
        pr: prestigeInfo(hh),
        turn: num(clk.turn),
        assets: (inv.account || {}).assets || {},
        flows: inv.previous_flows || {},
        holdings: inv.holdings || {},
        market: md.markets || md || {},
        buildings: blds.filter(Boolean),
      };
      S.m = money(S.flows, S.cash, S.turn);
      S.issues = findIssues(S);
      badge();
      render();
    } catch (e) {
      panel.querySelector('section').textContent = 'Load failed: ' + e.message + ' (turn in progress? try Refresh in a few seconds)';
    } finally { busy = false; }
  }

  function flowsOf(item) { return S.flows[item] || {}; }
  function held(item) { return num((S.assets[item] || {}).balance); }
  function use(item) { const f = flowsOf(item); return num(f.consumption); }
  function mkt(item) { return S.market[item] || {}; }

  async function townNames() {
    const c = store.get('towns2', null);
    if (c && c.at > Date.now() - 7 * 864e5) return c.t;
    try {
      const list = await api('/towns');
      const t = {};
      (Array.isArray(list) ? list : list.towns || []).forEach(x => { if (x && x.id) t[x.id] = { n: x.name, x: x.location && x.location.x, y: x.location && x.location.y }; });
      store.set('towns2', { at: Date.now(), t });
      return t;
    } catch (e) { return (c && c.t) || {}; }
  }
  const HX = +TOWN.slice(0, 4), HY = +TOWN.slice(4);
  const tdist = id => { const t = S.towns && S.towns[id]; return t && t.x != null ? Math.round(Math.hypot(t.x - HX, t.y - HY)) : null; };
  const tname = id => (S.towns && S.towns[id] && S.towns[id].n) || (String(id) === TOWN ? 'Strasclives' : 'town ' + id);

  // ---------------------------------------------------------------- textile chain
  // per 1x of each recipe (from the game's production pages)
  const CHAIN = {
    flax:  { id: '151602400',       labour: 11,  tools: 0.6, out: 18 },
    ret:   { id: '151802398',       labour: 25,  tools: 2,   in: 90, out: 35 },
    spin:  { id: '152202388002007', labour: 75,  tools: 0,   in: 17, out: 50 },
    weave: { id: '152202388001005', labour: 75,  tools: 0,   in: 50, out: 50 },
    sew:   { id: '152202388000004', labour: 155, tools: 0,   in: 80, out: 41 },
  };
  function chainState() {
    const b = {}, size = {}, cur = {};
    for (const [k, c] of Object.entries(CHAIN)) {
      b[k] = S.buildings.find(x => String(x.id) === c.id);
      if (!b[k] || !b[k].producer || !b[k].producer.recipe) return null;
      size[k] = num(b[k].size); cur[k] = num(b[k].producer.target);
    }
    const other = Math.max(0, num(flowsOf('thread').consumption) - cur.weave * CHAIN.weave.in);
    const retCap = Math.min(size.ret, size.flax * CHAIN.flax.out / CHAIN.ret.in);
    const spinCap = Math.min(size.spin, retCap * CHAIN.ret.out / CHAIN.spin.in);
    const buffer = held('thread') / 40;   // let thread stock cover a small deficit (~40 turns)
    const clothCap = Math.min(size.weave * CHAIN.weave.out, spinCap * CHAIN.spin.out + buffer - other);
    const sew = Math.min(size.sew, Math.max(0, clothCap) / CHAIN.sew.in);
    const weave = sew * CHAIN.sew.in / CHAIN.weave.out;
    const spin = Math.min(size.spin, (weave * CHAIN.weave.in + other) / CHAIN.spin.out);
    const ret = Math.min(size.ret, spin * CHAIN.spin.in / CHAIN.ret.out);
    const flax = Math.min(size.flax, ret * CHAIN.ret.in / CHAIN.flax.out);
    const plan = { flax, ret, spin, weave, sew };
    for (const k in plan) plan[k] = +plan[k].toFixed(2);
    const moves = Object.keys(CHAIN).filter(k => Math.abs(plan[k] - cur[k]) >= 0.02).map(k => ({ k, from: cur[k], to: plan[k], b: b[k] }));
    const dLab = moves.reduce((a, x) => a + (x.to - x.from) * CHAIN[x.k].labour, 0);
    const dTools = moves.reduce((a, x) => a + (x.to - x.from) * CHAIN[x.k].tools, 0);
    return { size, cur, plan, moves, dLab, dTools, other, gNow: cur.sew * 41, gNew: plan.sew * 41 };
  }
  async function balanceChain(c) {
    for (const x of c.moves) await setTarget(x.b, x.to);
    const bumpFirst = async (item, field, delta, pick) => {
      const ms = (S.holdings[item] || {}).managers || [];
      const i = pick ? ms.findIndex(pick) : 0;
      if (i < 0 || !ms[i]) return;
      await setTier(item, i, { [field]: Math.max(0, Math.round(num(ms[i][field]) + delta)) });
    };
    if (Math.abs(c.dLab) >= 1) await bumpFirst('labour', 'buy_volume', c.dLab);
    if (Math.abs(c.dTools) >= 1) await bumpFirst('tools', 'buy_volume', c.dTools, m => num(m.buy_volume));
    const gm = (S.holdings.garments || {}).managers || [];
    const gi = gm.findIndex(m => num(m.sell_volume));
    if (gi >= 0) await setTier('garments', gi, { sell_volume: Math.max(0, Math.round(c.gNew - 1.8)) });
  }

  // ---------------------------------------------------------------- issues
  function findIssues(S) {
    const out = [];
    const L = S.flows.labour || {};
    const exp = num(L.expiration), short = num(L.shortfall);
    const lm = (S.holdings.labour || {}).managers || [];
    if (exp > 5 && lm.length) out.push({ lvl: 'warn', item: 'labour', text: `Labour: ${f1(exp)} bought labour expired unused`,
      fixes: [{ label: `Trim buy −${Math.round(exp)}`, run: () => setTier('labour', 0, { buy_volume: Math.max(0, num(lm[0].buy_volume) - Math.round(exp)) }) }] });

    for (const item of Object.keys(S.flows)) {
      const f = S.flows[item], sf = num(f.shortfall);
      if (sf > 0) {
        const ms = (S.holdings[item] || {}).managers || [];
        const bi = ms.findIndex(m => num(m.buy_volume));
        const fixes = [];
        if (bi >= 0) {
          fixes.push({ label: `Buy +${Math.ceil(sf)}/turn`, run: () => setTier(item, bi, { buy_volume: num(ms[bi].buy_volume) + Math.ceil(sf) }) });
          fixes.push({ label: 'Max price +5%', run: () => setTier(item, bi, { buy_price: String(snap(num(ms[bi].buy_price) * 1.05, 1)) }) });
        } else {
          const ask = num(mkt(item).lowest_ask) || num(mkt(item).last_price);
          if (ask) fixes.push({ label: `Add buy ${Math.ceil(sf)} ≤ ${f2(snap(ask * 1.05, 1))}`, run: () => addTier(item, { buy_volume: Math.ceil(sf), buy_price: String(snap(ask * 1.05, 1)) }) });
        }
        out.push({ lvl: 'bad', item, text: `${item}: ${f1(sf)} short last turn`, fixes });
      }
    }

    for (const [item, h] of Object.entries(S.holdings)) {
      if (SKIP_ITEMS.has(item) || item === 'labour') continue;
      const ms = h.managers || [], f = flowsOf(item), have = held(item), u = use(item);
      const buyVol = ms.reduce((a, m) => a + num(m.buy_volume), 0);
      const sellVol = ms.reduce((a, m) => a + num(m.sell_volume), 0);
      const keep = Math.max(0, ...ms.map(m => num(m.min_holding)));
      const bought = num(f.purchase), sold = num(f.sale);
      const net = u - num(f.production) - bought;          // stock lost per turn
      // buy not filling while stock runs low
      if (buyVol > 0 && bought < buyVol * 0.5 && net > 0 && have < net * 5) {
        const bi = ms.findIndex(m => num(m.buy_volume));
        const ask = num(mkt(item).lowest_ask);
        const cur = num(ms[bi].buy_price);
        const to = snap(ask && ask <= cur * 1.12 ? ask : cur * 1.05, 1);
        out.push({ lvl: 'bad', item, text: `${item}: buy filled ${f1(bought)}/${f1(buyVol)}, ${f1(have)} left, dropping ${f1(net)}/turn (~${f1(have / net)} turns). Max ${f2(cur)}${ask ? ', lowest ask ' + f2(ask) : ''}`,
          fixes: [{ label: `Max → ${f2(to)}`, run: () => setTier(item, bi, { buy_price: String(to) }) }] });
      }
      // sell not moving while stock piles up
      if (sellVol > 0 && sold < sellVol * 0.5 && have > keep + 2 * sellVol && net + sold <= 0) {
        const si = ms.reduce((best, m, i) => num(m.sell_volume) && (best < 0 || num(m.sell_price) < num(ms[best].sell_price)) ? i : best, -1);
        const cur = num(ms[si].sell_price);
        const bid = num(mkt(item).highest_bid);
        const to = snap(cur * 0.97, -1);
        out.push({ lvl: 'warn', item, text: `${item}: sold ${f1(sold)}/${f1(sellVol)}, ${f1(have)} held. Floor ${f2(cur)}${bid ? ', best bid ' + f2(bid) : ''}`,
          fixes: [{ label: `Floor → ${f2(to)}`, run: () => setTier(item, si, { sell_price: String(to) }) }] });
      }
      // using it, running low, nothing buying it
      if (!buyVol && net > 0 && have < net * 5) {
        const ask = num(mkt(item).lowest_ask) || num(mkt(item).last_price);
        out.push({ lvl: 'warn', item, text: `${item}: ${f1(have)} left, dropping ${f1(net)}/turn (~${f1(have / net)} turns), no buy order`,
          fixes: ask ? [{ label: `Add buy ${Math.ceil(net)} ≤ ${f2(snap(ask * 1.05, 1))}`, run: () => addTier(item, { buy_volume: Math.ceil(net), buy_price: String(snap(ask * 1.05, 1)) }) }] : [] });
      }
    }

    for (const b of S.buildings) {
      if (b.producer && b.producer.recipe && b.producer.provider_id == null && b.provider_id == null && b.type !== 'warehouse')
        out.push({ lvl: 'bad', item: b.name, text: `${b.name}: producing but not linked to the storehouse`, fixes: [{ label: 'Link to storehouse', run: () => linkStore(b) }, { label: 'Open', run: () => go(b, 'production') }] });
      const c = b.construction;
      if (c && c.inventory) {
        const fl = c.inventory.previous_flows || {};
        const sh = Object.entries(fl).filter(([k, v]) => num(v.shortfall) > 0).map(([k, v]) => `${k} ${f1(v.shortfall)}`);
        if (sh.length) out.push({ lvl: 'warn', item: b.name, text: `${b.name} build short: ${sh.join(', ')}`, fixes: [{ label: 'Open', run: () => go(b, 'construction') }] });
      }
    }
    try {
      const c = chainState();
      if (c && c.moves.length && (Math.abs(c.dLab) >= 10 || Math.abs(c.gNew - c.gNow) >= 2))
        out.push({ lvl: 'warn', item: 'thread', text: `Textile chain out of balance: ${c.moves.map(x => `${x.k} ${f2(x.from)}→${f2(x.to)}x`).join(', ')} (garments ${f1(c.gNow)}→${f1(c.gNew)}/turn, labour ${c.dLab >= 0 ? '+' : ''}${Math.round(c.dLab)})`,
          fixes: [{ label: 'Balance chain', run: () => balanceChain(c) }] });
    } catch (e) { /* chain not readable */ }
    const order = { bad: 0, warn: 1 };
    return out.sort((a, b) => order[a.lvl] - order[b.lvl]);
  }

  function badge() {
    const n = S ? S.issues.length : 0;
    btn.innerHTML = 'Ops' + (n ? `<span class="dot">${n}</span>` : '');
  }

  // ---------------------------------------------------------------- actions
  async function patchItem(item, managers) {
    await api('/buildings/' + STORE + '/storage/inventory/' + encodeURIComponent(item), 'PATCH', { managers });
  }
  const clean = m => { const o = { ...m }; delete o.result; return o; };
  async function setTier(item, idx, changes) {
    const ms = ((S.holdings[item] || {}).managers || []).map(clean);
    if (!ms[idx]) ms[idx] = {};
    Object.assign(ms[idx], changes);
    for (const k of Object.keys(ms[idx])) if (ms[idx][k] === null) delete ms[idx][k];
    await patchItem(item, ms.filter(m => Object.keys(m).length));
  }
  async function addTier(item, tier) {
    const ms = ((S.holdings[item] || {}).managers || []).map(clean);
    ms.push(tier);
    await patchItem(item, ms);
  }
  async function setTarget(b, target) {
    await api('/buildings/' + b.id + '/producer', 'PUT', { target: target.toFixed(3), autoset_buying: false, autoset_selling: false, allow_overprod: false });
  }
  async function linkStore(b) {
    await api('/buildings/' + b.id + '/operation', 'PATCH', { provider_id: STORE, high_priority: false, bring_leftovers: false, autoset_inventory: false });
  }
  async function stopBuilding(b) {
    store.set('recipe:' + b.id, { recipe: b.producer.recipe, target: b.producer.target });
    await api('/buildings/' + b.id + '/producer', 'DELETE');
  }
  async function startBuilding(b) {
    const last = store.get('recipe:' + b.id, null);
    const recipe = prompt(`Recipe for ${b.name}?`, (last && last.recipe) || DEFAULT_RECIPES[b.type] || '');
    if (!recipe) return false;
    const t = parseFloat(prompt(`Target (x, max ${b.size})?`, (last && last.target) || '1'));
    if (!(t > 0)) return false;
    await api('/buildings/' + b.id + '/producer', 'PUT', {
      recipe, target: Math.min(t, num(b.size)).toFixed(3), manager: 'static',
      autoset_buying: false, autoset_selling: false, allow_fallback: false, allow_overprod: false, cargo_transfer: false,
    });
    try { await linkStore(b); } catch (e) { toast('Started, but relink failed: ' + e.message + ' (use Open)', 6000); }
    return true;
  }
  function go(b, page) { location.href = `/town/${b.town_id || TOWN}/building/${b.id}/${page}`; }

  async function act(fn, label) {
    try { const r = await fn(); if (r === false) return; toast('Done: ' + label); } catch (e) { toast('Failed: ' + e.message, 6000); }
    setTimeout(load, 400);
  }

  // ---------------------------------------------------------------- render
  function render() {
    const L = S.flows.labour || {};
    const lIn = num(L.production) + num(L.purchase), lUse = num(L.consumption);
    const tabs = [['issues', `Issues${S.issues.length ? ' (' + S.issues.length + ')' : ''}`], ['prod', 'Production'], ['orders', 'Orders'], ['build', 'Build'], ['boat', 'Boat'], ['deals', 'Contracts'], ['mkt', 'Markets'], ['money', 'Money']];
    panel.innerHTML = `
      <header><b>Merc Ops <span style="font-weight:400;opacity:.75;font-size:12px">v${VERSION}</span></b><button data-x="refresh">Refresh</button><button data-x="close">Close</button></header>
      <nav>${tabs.map(([k, l]) => `<button data-tab="${k}" class="${tab === k ? 'on' : ''}">${l}</button>`).join('')}</nav>
      <section>
        <div class="kpi">
          <div>Cash <b>${Math.round(S.cash).toLocaleString()}</b>
            · profit <b style="color:${S.m.profit >= 0 ? 'var(--mo-good)' : 'var(--mo-bad)'}">${sgn(S.m.profit)}</b>
            · <b style="color:${S.m.delta == null ? 'inherit' : S.m.delta >= 0 ? 'var(--mo-good)' : 'var(--mo-bad)'}">${S.m.delta == null ? '±?' : sgn(S.m.delta)}</b>${S.m.deltaTurns > 1 ? ` <span class="muted">(${S.m.deltaTurns} turns)</span>` : ''}</div>
          <div>Prestige <b>${f1(S.pr.free)}</b> spendable · <b>${S.pr.rate >= 0 ? '+' : '−'}${Math.abs(S.pr.rate).toFixed(1)}</b>/turn</div>
          <div>Labour <b>${f1(lIn)}</b> in / <b>${f1(lUse)}</b> used${num(L.expiration) ? ` · <span style="color:#d68910">${f1(L.expiration)} expired</span>` : ''}${num(L.shortfall) ? ` · <span style="color:#c0392b">${f1(L.shortfall)} short</span>` : ''}</div>
        </div>
        <div id="mo-body"></div>
      </section>`;
    const body = panel.querySelector('#mo-body');
    ({ issues: renderIssues, prod: renderProd, orders: renderOrders, build: renderBuild, boat: renderBoat, deals: renderDeals, mkt: renderMarkets, money: renderMoney }[tab] || renderIssues)(body);
    wire();
  }

  function upcoming() {
    const out = [];
    for (const b of S.buildings) {
      const c = b.construction; if (!c || !c.inventory) continue;
      const a = (c.inventory.account || {}).assets || {}, fl = c.inventory.previous_flows || {};
      let worst = 0, limit = '';
      for (const [k, v] of Object.entries(a)) {
        if (k === 'money') continue;
        const left = num(v.capacity) - num(v.balance); if (left <= 0.01) continue;
        const rate = num((fl[k] || {}).consumption);
        const t = rate > 0 ? left / rate : Infinity;
        if (t > worst) { worst = t; limit = k; }
      }
      const pct = f1(c.progress);
      const eta = worst === 0 ? 'materials all in, finishing' : isFinite(worst) ? `~${Math.ceil(worst)} turn${Math.ceil(worst) === 1 ? '' : 's'} (${limit} is the slowest)` : `stalled: no ${limit} delivered last turn`;
      const chain = Object.values(CHAIN).some(x => x.id === String(b.id));
      out.push({ lvl: isFinite(worst) ? (worst <= 3 ? 'soon' : 'later') : 'stuck', sort: isFinite(worst) ? worst : 999,
        text: `${b.name} ${c.stage === 'EXPANSION' ? 'expansion' : 'build'}: ${pct}% · ${eta}${chain ? ' · the chain balancer rebalances production when it lands' : ''}` });
    }
    for (const [item, h] of Object.entries(S.holdings)) {
      if (SKIP_ITEMS.has(item) || item === 'labour') continue;
      const f = flowsOf(item), have = held(item);
      const net = num(f.consumption) + num(f.sale) - num(f.production) - num(f.purchase);
      if (net > 0.5 && have > 0 && have / net < 15) out.push({ lvl: have / net <= 4 ? 'soon' : 'later', sort: have / net,
        text: `${item}: ${f1(have)} left, falling ${f1(net)}/turn → runs out in ~${Math.ceil(have / net)} turns` });
    }
    for (const c of S.myContracts || []) {
      if (c.state === 'done') continue; const t = (c.transactions || [])[0] || {};
      out.push({ lvl: 'later', sort: 50, text: `contract: ${t.direction === 'bid' ? 'selling' : 'buying'} ${f1(t.volume)} ${t.asset} @ ${f2(t.price)} (${t.stage || c.state})` });
    }
    for (const n of (S.notes || []).filter(n => !n.acked).slice(0, 8)) {
      const b = S.buildings.find(x => String(x.id) === String(n.subject));
      out.push({ lvl: 'soon', sort: -1, text: `game notice: ${n.name || (b && b.name) || 'item ' + n.subject}${n.type === 10 ? ' (construction finished)' : ''}` });
    }
    return out.sort((a, b) => a.sort - b.sort);
  }

  function renderIssues(el) {
    const up = upcoming();
    const upHtml = `<h4 style="margin:14px 0 6px">Upcoming</h4>` + (up.length ? up.map(u => `<div class="card ${u.lvl === 'soon' ? 'warn' : u.lvl === 'stuck' ? 'bad' : ''}">${u.lvl === 'soon' ? '<b>Soon</b> · ' : ''}${esc(u.text)}</div>`).join('') : '<p class="muted">Nothing finishing or running out soon.</p>');
    if (!S.issues.length) { el.innerHTML = '<div class="card ok"><b>All clear.</b> <span class="muted">No shortages, waste, stuck orders or stalled builds last turn.</span></div>' + upHtml; return; }
    el.innerHTML = S.issues.map((it, i) => `
      <div class="card ${it.lvl}"><div>${esc(it.text)}</div>
        <div class="row" style="margin-top:6px">${it.fixes.map((f, j) => `<button class="a" data-fix="${i}:${j}">${esc(f.label)}</button>`).join('')}
        <button class="b" data-stock="${esc(it.item)}">Details</button></div></div>`).join('') + upHtml;
  }

  function renderProd(el) {
    const bl = S.buildings.filter(b => b.type !== 'warehouse').sort((a, b) => a.name.localeCompare(b.name));
    let chainHtml = '';
    try {
      const c = chainState();
      if (c) chainHtml = `<div class="card ${c.moves.length ? 'warn' : 'ok'}"><b>Textile chain</b> <span class="muted">flax → retting → spinning → weaving → sewing</span>
        <div class="muted">${Object.keys(CHAIN).map(k => `${k} ${f2(c.cur[k])}x/${c.size[k]}`).join(' · ')}</div>
        ${c.moves.length ? `<div style="margin-top:6px">Balanced: ${c.moves.map(x => `${x.k} → ${f2(x.to)}x`).join(', ')}<br><span class="muted">garments ${f1(c.gNow)} → ${f1(c.gNew)}/turn · labour ${c.dLab >= 0 ? '+' : ''}${Math.round(c.dLab)} · tools ${c.dTools >= 0 ? '+' : ''}${f1(c.dTools)}</span></div>
          <div class="row" style="margin-top:6px"><button class="a" data-balance="1">Balance chain</button></div>` : '<div class="muted" style="margin-top:4px">Balanced: every step feeds the next.</div>'}</div>`;
    } catch (e) { chainHtml = ''; }
    el.innerHTML = chainHtml + bl.map(b => {
      const p = b.producer || {};
      const on = !!p.recipe;
      const t = num(p.target), max = num(b.size) || 1;
      const po = p.previous_operation || {};
      const ran = num(po.production), tgt = num(po.target);
      const lag = on && tgt && ran < tgt * 0.95;
      return `<div class="card ${on ? (lag ? 'warn' : 'ok') : ''}">
        <div class="row"><div class="grow"><b>${esc(b.name)}</b> <span class="muted">${esc(p.recipe || 'stopped')}</span><br>
          <span class="muted">${on ? `target ${f2(t)}x of ${max}x${lag ? ` · ran ${f2(ran)}x last turn` : ''}` : (b.construction ? 'under construction' : 'no production')}</span></div>
        </div>
        <div class="ctl">${on ? `<button class="b" data-t="${b.id}:-">−</button><button class="b" data-t="${b.id}:+">+</button><button class="b" data-t="${b.id}:max">max</button><button class="r" data-stop="${b.id}">Stop</button>`
               : `<button class="a" data-start="${b.id}" style="grid-column:span 4">Start</button>`}
          <button class="b" data-open="${b.id}:production">Open</button></div></div>`;
    }).join('') + '<p class="muted">− / + step 10% of the building\'s max. Changes don\'t touch your storehouse orders; check Issues after the next turn for labour balance.</p>';
  }

  function tierLine(m) {
    const p = [];
    if (num(m.buy_volume)) p.push(`buy ${f1(m.buy_volume)} ≤ ${f2(m.buy_price)}${m.max_holding != null ? ' stop ' + f1(m.max_holding) : ''}`);
    if (num(m.sell_volume)) p.push(`sell ${f1(m.sell_volume)} ≥ ${f2(m.sell_price)}${m.min_holding != null ? ' keep ' + f1(m.min_holding) : ''}`);
    return p.join(' · ') || 'empty';
  }

  function renderOrders(el) {
    const q = (store.get('q', '') || '').toLowerCase();
    const items = Object.keys(S.holdings).filter(i => !SKIP_ITEMS.has(i))
      .filter(i => q ? i.includes(q) : ((S.holdings[i].managers || []).length || Object.keys(flowsOf(i)).length))
      .sort();
    const open = store.get('openItem', null);
    el.innerHTML = `<input class="search" data-q placeholder="Filter items (e.g. beer)" value="${esc(q)}">` + items.map(item => {
      const f = flowsOf(item), ms = S.holdings[item].managers || [], m = mkt(item);
      const move = [['production', 'made'], ['consumption', 'used'], ['purchase', 'bought'], ['sale', 'sold'], ['expiration', 'wasted'], ['shortfall', 'SHORT']]
        .filter(([k]) => num(f[k])).map(([k, l]) => `${l} ${f1(f[k])}`).join(', ');
      const isOpen = open === item;
      return `<div class="card"><div class="row" data-item="${esc(item)}"><div class="grow"><b>${esc(item)}</b> ${f1(held(item))} held
          <br><span class="muted">${move || 'no movement'}${m.last_price ? ` · mkt ${f2(m.last_price)} (bid ${f2(m.highest_bid)} / ask ${f2(m.lowest_ask)})` : ''}</span>
          <br><span class="muted">${ms.map(tierLine).join(' | ') || 'no orders'}</span></div><button class="b" data-edit="${esc(item)}">${isOpen ? 'Hide' : 'Edit'}</button></div>
        ${isOpen ? editor(item, ms) : ''}</div>`;
    }).join('');
    const qi = el.querySelector('[data-q]');
    qi.oninput = () => { store.set('q', qi.value.trim()); const pos = qi.selectionStart; renderOrders(el); const n = el.querySelector('[data-q]'); n.focus(); n.setSelectionRange(pos, pos); };
  }

  function editor(item, ms) {
    const rows = ms.map((m, i) => `
      <div class="card" data-tier="${i}"><div class="muted">Tier ${i + 1}</div>
        <div class="row">Buy <input data-k="buy_volume" value="${m.buy_volume ?? ''}" inputmode="decimal"> ≤ <input data-k="buy_price" value="${m.buy_price ?? ''}" inputmode="decimal"> stop at <input data-k="max_holding" value="${m.max_holding ?? ''}" inputmode="decimal"></div>
        <div class="row" style="margin-top:4px">Sell <input data-k="sell_volume" value="${m.sell_volume ?? ''}" inputmode="decimal"> ≥ <input data-k="sell_price" value="${m.sell_price ?? ''}" inputmode="decimal"> keep <input data-k="min_holding" value="${m.min_holding ?? ''}" inputmode="decimal"></div>
      </div>`).join('');
    return `<div data-editor="${esc(item)}">${rows}
      <div class="row"><button class="a" data-save="${esc(item)}">Save</button><button class="b" data-addtier="${esc(item)}">+ tier</button>
      <span class="muted">Blank = off. Prices snap to the game grid.</span></div></div>`;
  }

  function renderBuild(el) {
    const bl = S.buildings.filter(b => b.type !== 'warehouse');
    const cons = bl.filter(b => b.construction);
    el.innerHTML = (cons.length ? '<h4 style="margin:6px 0">Under construction</h4>' : '<p class="muted">Nothing under construction.</p>') +
      cons.map(b => {
        const c = b.construction, a = (c.inventory && c.inventory.account && c.inventory.account.assets) || {};
        const need = Object.entries(a).filter(([k]) => k !== 'money').map(([k, v]) => `${k} ${f1(v.balance)}/${f1(v.capacity)}`).join(' · ');
        return `<div class="card"><b>${esc(b.name)}</b> <span class="muted">${esc(c.stage || '')}, pace ${c.settings ? c.settings.pace : '?'}</span>
          <div class="bar"><i style="width:${Math.min(100, num(c.progress))}%"></i></div>
          <div class="muted">${f1(c.progress)}% · ${need}</div>
          <div class="row" style="margin-top:6px"><button class="b" data-open="${b.id}:construction">Open</button></div></div>`;
      }).join('') +
      '<h4 style="margin:12px 0 6px">Expand a building</h4><p class="muted">Opens the building\'s construction page; tap “expand or modify”, pick the plot, confirm, then link it to the storehouse.</p>' +
      bl.sort((a, b) => a.name.localeCompare(b.name)).map(b => `<div class="card row"><div class="grow"><b>${esc(b.name)}</b> <span class="muted">${b.size} plot${b.size > 1 ? 's' : ''}</span></div><button class="b" data-open="${b.id}:construction">Expand…</button></div>`).join('');
  }

  function renderBoat(el) {
    if (!S.boats || !S.boats.length) { el.innerHTML = '<p class="muted">No boats.</p>'; return; }
    const hx = +TOWN.slice(0, 4), hy = +TOWN.slice(4);
    el.innerHTML = S.boats.map(t => {
      const p = t.producer || {}, loc = t.location || {}, j = t.journey || {};
      const legs = j.legs || [];
      const home = loc.x === hx && loc.y === hy;
      const fishing = p.recipe && /fish/.test(p.recipe);
      const state = fishing ? `fishing (${esc(p.recipe)}) at ${loc.x}:${loc.y}` : home ? 'docked at Strasclives' : `at sea ${loc.x}:${loc.y}`;
      const cargo = Object.entries(((t.cargo || {}).inventory || {}).account?.assets || {}).filter(([k, v]) => k !== 'money' && num(v.balance) > 0.01).map(([k, v]) => `${k} ${f1(v.balance)}`).join(', ');
      return `<div class="card ok"><b>${esc(t.name)}</b> <span class="muted">${esc(t.type)}</span>
        <div>${state}</div>
        <div class="muted">${p.recipe ? `level ${Math.round(num(p.target) * 100)}%` : 'no operation'}${t.fish_quantity != null ? ` · fish here: ${t.fish_quantity}` : ''} · cargo: ${cargo || 'empty'}${j.end_town_id ? ` · heading to ${esc(tname(j.end_town_id))}` : ''}</div>
        <div class="ctl" style="grid-template-columns:repeat(4,1fr)">
          ${p.recipe ? `<button class="b" data-boat="${t.id}:-">− 10%</button><button class="b" data-boat="${t.id}:+">+ 10%</button><button class="r" data-boat="${t.id}:stop">Stop</button>` : `<button class="b" disabled style="grid-column:span 3">Start fishing from the boat page</button>`}
          <button class="b" data-boat="${t.id}:home" ${home ? 'disabled' : ''}>Home</button>
        </div>
        <div class="row" style="margin-top:6px"><a class="muted" href="/transport/${t.id}/operation">Boat page →</a> · <a class="muted" href="/transport/${t.id}/journey">Journey / send →</a></div></div>`;
    }).join('') + '<p class="muted">Fishing level steps 10% (10% = 5 fish/turn on fishing 2). Home sails back to Strasclives; Stop ends the current operation.</p>';
  }

  function renderDeals(el) {
    const makes = new Set(Object.entries(S.flows).filter(([k, f]) => num(f.production) > 0).map(([k]) => k));
    const uses = new Set(Object.entries(S.flows).filter(([k, f]) => num(f.consumption) > 0).map(([k]) => k));
    const tx = c => (c.transactions || [])[0] || {};
    const mine = S.myContracts.filter(c => c.state !== 'done');
    const offers = S.townContracts.filter(c => !c.signed).map(c => {
      const t = tx(c);
      const theyBuy = t.direction === 'bid';
      const fit = theyBuy ? makes.has(t.asset) || held(t.asset) >= num(t.initial_volume) : uses.has(t.asset);
      return { c, t, theyBuy, fit };
    }).sort((a, b) => (b.fit - a.fit) || (b.c.local ? 1 : 0) - (a.c.local ? 1 : 0));
    const row = ({ c, t, theyBuy, fit }) => {
      const home = num(mkt(t.asset).last_price), price = num(t.price), vol = num(t.initial_volume);
      const edge = home ? (theyBuy ? price - home : home - price) : null;
      const d = c.local || String(c.town_id) === TOWN ? 0 : tdist(c.town_id);
      const aid = (BigInt(c.id) | (BigInt(1) << BigInt(6))).toString();
      return `<div class="card ${fit ? 'ok' : ''}">
        <div class="row"><div class="grow"><b>${theyBuy ? 'They buy' : 'They sell'} ${f1(vol)} ${esc(t.asset)}</b> @ ${f2(price)}${vol && price ? ` <span class="muted">(${Math.round(vol * price).toLocaleString()} total)</span>` : ''}
          <br><span class="muted">${d === 0 ? 'local, no boat needed' : `${esc(tname(c.town_id))} · ~${d ?? '?'} tiles away (boat)`}${t.timeframe ? ` · ${t.timeframe.length} turns` : ''}${t.penalty ? ` · penalty ${t.penalty}` : ''}</span>
          <br><span class="muted">${fit ? `<b>${theyBuy ? 'we make/hold this' : 'we use this'}</b> · ` : ''}${edge != null ? `vs home ${f2(home)}: <b style="color:${edge >= 0 ? 'var(--mo-good)' : 'var(--mo-bad)'}">${edge >= 0 ? '+' : '−'}${f2(Math.abs(edge))}/unit (${edge >= 0 ? '+' : '−'}${Math.round(Math.abs(edge * vol))})</b>` : 'no home price'}</span></div>
          <a class="b" style="text-decoration:none;display:inline-block;padding:9px 12px;border-radius:6px;font-weight:600" href="/contracts/actions#actionid=${aid}">Accept…</a></div></div>`;
    };
    el.innerHTML = `<h4 style="margin:6px 0">Our contracts</h4>` +
      (mine.length ? mine.map(c => { const t = tx(c); return `<div class="card warn"><b>${t.direction === 'bid' ? 'Selling' : 'Buying'} ${f1(t.initial_volume)} ${esc(t.asset)}</b> @ ${f2(t.price)} <span class="muted">· ${esc(t.stage || c.state)} · ${f1(t.volume)} left</span></div>`; }).join('') : '<p class="muted">None active.</p>') +
      `<h4 style="margin:12px 0 6px">Offers on the board (${offers.length})</h4>` +
      (offers.length ? offers.map(row).join('') : '<p class="muted">No open offers.</p>') +
      `<p class="muted">Accept… opens the game's own accept screen for that offer, where you confirm and pick a carrier. Distances are straight-line; sea routes run longer.</p><div class="row"><a class="muted" href="/contracts">All contracts →</a></div>`;
  }

  async function regionalScan(force) {
    const c = store.get('scan', null);
    if (!force && c && c.at > Date.now() - 30 * 60e3) return c;
    const near = Object.entries(S.towns || {}).filter(([id, t]) => t.x != null && id !== TOWN)
      .map(([id, t]) => ({ id, n: t.n, d: Math.round(Math.hypot(t.x - HX, t.y - HY)) })).sort((a, b) => a.d - b.d).slice(0, 14);
    const data = {};
    await Promise.all(near.map(async t => {
      try { const md = await api('/towns/' + t.id + '/marketdata'); data[t.id] = md.markets || md; } catch (e) { }
    }));
    const res = { at: Date.now(), near, data };
    store.set('scan', res);
    return res;
  }

  function renderMarkets(el) {
    const items = Object.entries(S.holdings).filter(([i, h]) => !SKIP_ITEMS.has(i) && i !== 'labour' && (h.managers || []).length)
      .map(([i, h]) => ({ i, sells: (h.managers || []).some(m => num(m.sell_volume)), buys: (h.managers || []).some(m => num(m.buy_volume)) }));
    const scan = store.get('scan', null);
    const best = (item, sells) => {
      if (!scan) return null; let b = null;
      for (const t of scan.near) { const x = (scan.data[t.id] || {})[item]; if (!x) continue;
        const p = sells ? num(x.highest_bid) || 0 : num(x.lowest_ask) || 0; if (!p) continue;
        if (!b || (sells ? p > b.p : p < b.p)) b = { p, t, vol: x.volume_ema_60 }; }
      return b;
    };
    const arrow = x => { const l = num(x.last_price), e = num(x.price_ema_60); if (!l || !e) return ''; const r = l / e - 1; return r > 0.03 ? ' ↑' : r < -0.03 ? ' ↓' : ' →'; };
    el.innerHTML = `<div class="row" style="justify-content:space-between"><span class="muted">${scan ? `Nearby scan: ${Math.round((Date.now() - scan.at) / 60000)} min old (${scan.near.length} towns)` : 'No nearby scan yet'}</span><button class="b" data-scan="1">${scan ? 'Rescan' : 'Scan nearby towns'}</button></div>` +
      items.sort((a, b) => a.i.localeCompare(b.i)).map(({ i, sells, buys }) => {
        const x = mkt(i); const side = sells ? 'sell' : 'buy'; const b = best(i, sells);
        const home = sells ? num(x.highest_bid) || num(x.last_price) : num(x.lowest_ask) || num(x.last_price);
        const better = b && home && (sells ? b.p > home * 1.05 : b.p < home * 0.95);
        return `<div class="card ${better ? 'ok' : ''}"><b>${esc(i)}</b> <span class="muted">(we ${side})</span>
          <div class="muted">home: last ${f2(x.last_price)}${arrow(x)} · bid ${f2(x.highest_bid)} · ask ${f2(x.lowest_ask)} · avg ${f2(x.price_ema_60)} · ~${f1(x.volume_ema_60)}/turn traded</div>
          ${b ? `<div class="muted">best nearby ${sells ? 'bid' : 'ask'}: <b>${f2(b.p)}</b> at ${esc(b.t.n)} (~${b.t.d} tiles)${better ? ' · <b>worth a boat run?</b>' : ''}</div>` : ''}</div>`;
      }).join('') + '<p class="muted">↑ ↓ = last price vs the 60-turn average. "Best nearby" is the best standing bid (for things we sell) or ask (for things we buy) in the 14 closest towns.</p>';
  }

  function renderMoney(el) {
    const rows = Object.entries(S.flows).map(([i, f]) => ({ i, sale: num(f.sale_value), buy: num(f.purchase_cost), sv: num(f.sale), bv: num(f.purchase) }));
    const earn = rows.filter(r => r.sale > 0).sort((a, b) => b.sale - a.sale);
    const cost = rows.filter(r => r.buy > 0).sort((a, b) => b.buy - a.buy);
    const tot = (a, k) => a.reduce((s, r) => s + r[k], 0);
    const line = (r, k, v) => `<div class="row"><div class="grow">${esc(r.i)} <span class="muted">${f1(r[v])} @ ${f2(r[k] / (r[v] || 1))}</span></div><b>${Math.round(r[k]).toLocaleString()}</b></div>`;
    const cs = [];
    for (const b of S.buildings) { const c = b.construction; if (!c || !c.inventory) continue; const fl = c.inventory.previous_flows || {}; const v = Object.values(fl).reduce((s, x) => s + num(x.consumption_cost), 0); if (v) cs.push({ n: b.name, v }); }
    el.innerHTML = `<div class="card"><b>Last turn</b><div class="row" style="margin-top:4px"><div class="grow">Market sales</div><b style="color:var(--mo-good)">+${Math.round(tot(earn, 'sale')).toLocaleString()}</b></div>
        <div class="row"><div class="grow">Market purchases</div><b style="color:var(--mo-bad)">−${Math.round(tot(cost, 'buy')).toLocaleString()}</b></div>
        <div class="row"><div class="grow"><b>Trading profit</b></div><b>${sgn(S.m.profit)}</b></div>
        ${cs.length ? `<div class="muted" style="margin-top:4px">Goods fed into construction (from stock): ${cs.map(c => `${esc(c.n)} ${Math.round(c.v)}`).join(' · ')}</div>` : ''}</div>
      <div class="card"><b>What earns</b>${earn.slice(0, 8).map(r => line(r, 'sale', 'sv')).join('') || '<div class="muted">No sales</div>'}</div>
      <div class="card"><b>What costs</b>${cost.slice(0, 8).map(r => line(r, 'buy', 'bv')).join('') || '<div class="muted">No purchases</div>'}</div>
      <p class="muted">Market trades only. Wages for your own labour, land tax and household spending aren't in these numbers.</p>`;
  }

  // ---------------------------------------------------------------- events
  function wire() {
    panel.onclick = async ev => {
      const t = ev.target.closest('button'); if (!t) return;
      const d = t.dataset;
      if (d.x === 'close') { panel.classList.remove('open'); return; }
      if (d.x === 'refresh') return load();
      if (d.tab) { tab = d.tab; store.set('tab', tab); return render(); }
      if (d.fix) { const [i, j] = d.fix.split(':').map(Number); const f = S.issues[i].fixes[j]; return act(f.run, f.label); }
      if (d.stock) { tab = 'orders'; store.set('openItem', d.stock); return render(); }
      if (d.open) { const [id, page] = d.open.split(':'); const b = S.buildings.find(x => x.id == id); panel.classList.remove('open'); return go(b, page); }
      if (d.t) {
        const [id, op] = d.t.split(':'); const b = S.buildings.find(x => x.id == id);
        const max = num(b.size) || 1, cur = num(b.producer.target), step = Math.max(0.1, +(max * 0.1).toFixed(2));
        let nt = op === 'max' ? max : op === '+' ? Math.min(max, cur + step) : Math.max(step, cur - step);
        nt = +nt.toFixed(2);
        if (nt === cur) return toast('Already at ' + (op === '-' ? 'minimum step' : 'max'));
        return act(() => setTarget(b, nt), `${b.name} ${f2(cur)}x → ${f2(nt)}x`);
      }
      if (d.stop) {
        const b = S.buildings.find(x => x.id == d.stop);
        if (!confirm(`Stop ${b.name} (${b.producer.recipe})?\nStart (in this panel) remembers the recipe and relinks the storehouse.`)) return;
        return act(() => stopBuilding(b), `${b.name} stopped`);
      }
      if (d.start) { const b = S.buildings.find(x => x.id == d.start); return act(() => startBuilding(b), `${b.name} started + linked`); }
      if (d.scan) { toast('Scanning nearby markets…', 4000); try { await regionalScan(true); } catch (e) { toast('Scan failed: ' + e.message, 5000); } return render(); }
      if (d.balance) {
        const c = chainState(); if (!c || !c.moves.length) return toast('Chain already balanced');
        if (!confirm('Balance the textile chain?\n' + c.moves.map(x => `${x.k}: ${f2(x.from)}x → ${f2(x.to)}x`).join('\n') + `\n\nlabour buy ${c.dLab >= 0 ? '+' : ''}${Math.round(c.dLab)}, tools ${c.dTools >= 0 ? '+' : ''}${f1(c.dTools)}, garments sell → ${Math.round(c.gNew - 1.8)}`)) return;
        return act(() => balanceChain(c), 'chain balanced');
      }
      if (d.boat) {
        const [id, op] = d.boat.split(':'); const t = S.boats.find(x => String(x.id) === id); const p = t.producer || {};
        if (op === 'home') { if (!confirm(`Sail ${t.name} home to Strasclives?`)) return; return act(() => api('/transports/' + id + '/return', 'POST'), `${t.name} heading home`); }
        if (op === 'stop') { if (!confirm(`Stop ${t.name}'s ${p.recipe}?`)) return; return act(() => api('/transports/' + id + '/producer', 'DELETE'), `${t.name} stopped`); }
        const nt = Math.max(0.1, Math.min(1, +(num(p.target) + (op === '+' ? 0.1 : -0.1)).toFixed(2)));
        if (nt === num(p.target)) return toast('Already at ' + (op === '+' ? 'max' : 'min'));
        return act(() => api('/transports/' + id + '/producer', 'PUT', { recipe: p.recipe, target: nt.toFixed(3), autoset_buying: false, autoset_inventory: false, allow_fallback: false, cargo_transfer: false }), `${t.name} ${Math.round(num(p.target) * 100)}% → ${Math.round(nt * 100)}%`);
      }
      if (d.edit) { store.set('openItem', store.get('openItem') === d.edit ? null : d.edit); return render(); }
      if (d.addtier) {
        const ed = panel.querySelector(`[data-editor="${CSS.escape(d.addtier)}"]`);
        const n = ed.querySelectorAll('[data-tier]').length;
        ed.insertAdjacentHTML('afterbegin', editor(d.addtier, [{}]).replace('data-tier="0"', `data-tier="${n}"`).replace('Tier 1', 'New tier').replace(/<div class="row"><button class="a" data-save[\s\S]*$/, ''));
        return;
      }
      if (d.save) {
        const item = d.save;
        const ed = panel.querySelector(`[data-editor="${CSS.escape(item)}"]`);
        const tiers = [...ed.querySelectorAll('[data-tier]')].sort((a, b) => a.dataset.tier - b.dataset.tier).map(tr => {
          const m = {};
          tr.querySelectorAll('input').forEach(inp => {
            const v = inp.value.trim(); if (v === '') return;
            const n = parseFloat(v); if (isNaN(n)) return;
            if (/price/.test(inp.dataset.k)) m[inp.dataset.k] = String(snap(n)); else m[inp.dataset.k] = n;
          });
          if (!m.buy_volume) { delete m.buy_price; delete m.max_holding; }
          if (!m.sell_volume) { delete m.sell_price; delete m.min_holding; }
          if (m.buy_volume && !m.buy_price) throw new Error('buy price missing');
          if (m.sell_volume && !m.sell_price) throw new Error('sell price missing');
          return m;
        }).filter(m => Object.keys(m).length);
        const summary = tiers.map(tierLine).join('\n') || '(no orders)';
        if (!confirm(`Save ${item}:\n${summary}`)) return;
        return act(() => patchItem(item, tiers), `${item} orders saved`);
      }
    };
  }

  // quiet background check every 10 min so the badge shows problems without opening the panel
  async function quietCheck() {
    if (panel.classList.contains('open') || busy) return;
    try {
      busy = true;
      const [biz, sh, clk] = await Promise.all([api('/businesses/' + BUSINESS), api('/buildings/' + STORE), api('/clock').catch(() => ({}))]);
      const inv = (sh.storage || {}).inventory || {};
      const ids = (biz.building_ids || []).filter(id => id !== STORE);
      const blds = await Promise.all(ids.map(id => api('/buildings/' + id).catch(() => null)));
      S = Object.assign(S || {}, { cash: num(inv.account?.assets?.money?.balance), assets: inv.account?.assets || {}, flows: inv.previous_flows || {},
        holdings: inv.holdings || {}, buildings: blds.filter(Boolean), market: (S && S.market) || {} });
      S.turn = num(clk.turn); S.m = money(S.flows, S.cash, S.turn);
      S.issues = findIssues(S); badge();
    } catch (e) { /* ignore */ } finally { busy = false; }
  }
  let lastTurn = null;
  setInterval(async () => {
    try { const c = await api('/clock'); if (lastTurn != null && c.turn !== lastTurn && !panel.classList.contains('open')) setTimeout(quietCheck, 90e3); lastTurn = c.turn; } catch (e) { }
  }, 120e3);
  setTimeout(quietCheck, 3000);
  setInterval(quietCheck, 600000);
})();
