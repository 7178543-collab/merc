// ==UserScript==
// @name         Merc Ops panel
// @namespace    strasclives
// @version      1.8
// @updateURL    https://raw.githubusercontent.com/7178543-collab/merc/main/merc-ops.user.js
// @downloadURL  https://raw.githubusercontent.com/7178543-collab/merc/main/merc-ops.user.js
// @description  30-second ops panel for Mercatorio: needs-you list, issues with one-tap fixes, production, orders, builds, boats, contracts, markets, money, charts with projections, plan, and an emergency self-sufficient mode.
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
  const VERSION = '1.8';
  const BUSINESS = '39992';
  const HOUSEHOLD = '21623';
  const STORE = '152202386005001';
  const TOWN = '152202387';
  const SKIP_ITEMS = new Set(['money', 'handcart', 'tumbrel', 'snekkja', 'cog', 'lodging']);
  // recipe to use when starting a building that has none (remembered after a Stop)
  const DEFAULT_RECIPES = { 'brewery': 'brew beer 1', 'logging camp': 'split timber 2', 'park': 'maintain 1' };
  const RIVAL = '15082';                 // Gaud de Noyon
  const RESERVE = 4000;                  // cash we keep
  const CARGO = 250;                     // snekkja cargo space (storage units)
  const TRIP_PER_TILE = 0.2;             // boat running cost per tile, one way (estimate)
  const SEA_DETOUR = 1.3;                // sea routes run longer than straight-line
  const GATE = { labour: 1.75, garments: 22, cash: 4000 };   // Phase 2 gate
  const KILL = { labour: 1.85, garments: 21.5 };             // stop adding if crossed
  const LABOUR_WARN = 1.70;              // labour guard kicks in at this price

  // The plan (Claude updates this text each version; live numbers are filled in by the panel)
  const PLAN = [
    { k: 'p1', t: 'Phase 1 (~7.1k)', d: '+1 plot each for weavery, spinnery and sewing shop → ~65 garments/turn. The chain balancer resets production as each one lands.' },
    { k: 'gate', t: 'Gate before Phase 2', d: 'Labour ≤ 1.75, garments still sell at ≥ 22, cash above the ~4k reserve.' },
    { k: 'p2', t: 'Phase 2 (~4.6k)', d: 'Weavery +1, spinnery +1 = full double (~82 garments). Needs an outlet for ~40 extra: ship runs (Calange bid ~23.2) or the second boat.' },
    { k: 'p3', t: 'Phase 3: Tenants → farmstead expansion (APPROVED)', d: 'Buy Tenants the moment 200 prestige is free (Claude has a check scheduled), then queue the farmstead expansion straight away: +5 plots, 500 labour + 100 timber (~1.6k), +50 own labour (~0.05 each vs ~1.65 bought, ~+80/turn). Beats a boardinghouse: that needs the same 5 tenants PLUS 1.0 management (another 100 prestige) and eats bread/beer/cloth for its labour.' },
    { k: 'p4', t: 'Phase 4: better recipes', d: 'Barthélemy to textile worker (sew garments 3) once a textile duty pays.' },
    { k: 'kill', t: 'Kill switch', d: 'Labour above ~1.85 or garments below ~21.5 for several turns: stop adding and trim weavery/sewing.' },
    { k: 'tools', t: 'Tools stockpile', d: 'Catch the dips, climb steadily to 100+.' },
    { k: 'boat', t: 'Second boat (Flax Wyrm)', d: 'Idle at home. Use: garment export runs (Calange), contract deliveries, beer backhaul from Clairas when a trip is happening anyway.' },
    { k: 'iron', t: 'Iron deposit (~1474,2419)', d: 'Outside the town domain. Iron mine = 1,000 labour + 240 timber, 18 turns. Open question: how a tile outside the domain becomes buildable. Next: try the tile in the build menu, or ask on Discord.' },
  ];
  const AUTOMATION = [
    ['Hourly GitHub actor', 'Reprices buy/sell orders within the floors and ceilings in merc_actor.py. Pause: add the merc-paused label on GitHub.'],
    ['Alerts + status', 'Posts problems and a status line to issue #1 each hour (GitHub emails you).'],
    ['Chain balancer', 'When a chain building gains a plot, sets all five chain targets, the labour/tools buys and the garments sell. Comments on issue #1 when it acts.'],
    ['History', 'Saves each hourly status line to history/ in the repo.'],
  ];
  // things waiting on Taylor (Claude adds these each version); Done/Later is remembered per device
  const NEEDS = [
    { id: 'iron-tile', text: 'Iron deposit near 1474,2419: open the build menu on that tile (iron mine) and see if it lets you claim it.', link: ['World map', '/worldmap'] },
    { id: 'flax-wyrm', text: 'Flax Wyrm is idle at home.', trip: 'best' },
    { id: 'update-1.8', text: 'v1.8 updates itself from GitHub from now on (Tampermonkey checks the repo). Nothing to paste next time.' },
  ];

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
  // game price grid (tested against the server, May 1069): max 2 decimals, 3 significant digits;
  // leading digit 1 -> any last digit, 2-4 -> last digit even, 5-9 -> last digit 0 or 5
  const snap = (p, dir = 0) => {
    p = num(p);
    if (p <= 0) return p;
    const e = Math.floor(Math.log10(p) + 1e-12) - 2;
    const lead = Math.floor(p / Math.pow(10, e + 2) + 1e-9);
    const step = Math.max(0.01, Math.pow(10, e) * (lead >= 5 ? 5 : lead >= 2 ? 2 : 1));
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
  const clamp = (x, a, b) => Math.max(a, Math.min(b, x));

  // ---------------------------------------------------------------- real time
  // turns are hourly; we learn when a turn started by watching the turn number change
  function noteTurn(turn, exact) {
    const t = store.get('turnAt', null);
    if (!turn) return t;
    if (!t || t.turn !== turn) { const v = { turn, at: Date.now(), exact: !!exact }; store.set('turnAt', v); return v; }
    return t;
  }
  function whenMs(n) {
    const t = store.get('turnAt', null), H = 3600e3;
    if (!t) return Date.now() + n * H;
    let ms = t.at + n * H;
    const cur = S && S.turn ? S.turn - t.turn : 0;      // turns since the anchor
    ms -= cur * H;
    return ms < Date.now() ? Date.now() + (n > 0 ? 60e3 : 0) : ms;
  }
  function clockText(ms, exact) {
    if (!exact) { const q = 15 * 60e3; ms = Math.round(ms / q) * q; }
    const d = new Date(ms), now = new Date();
    const dayDiff = Math.round((new Date(d.getFullYear(), d.getMonth(), d.getDate()) - new Date(now.getFullYear(), now.getMonth(), now.getDate())) / 864e5);
    const hm = d.toLocaleTimeString([], { hour: 'numeric', minute: '2-digit' }).replace(':00', '').toLowerCase().replace(/\s/g, ' ');
    if (dayDiff === 0) return hm;
    if (dayDiff === 1) return 'tomorrow ' + hm;
    if (dayDiff < 7) return d.toLocaleDateString([], { weekday: 'short' }) + ' ' + hm;
    return d.toLocaleDateString([], { month: 'short', day: 'numeric' });
  }
  // "~3 turns (about 9:15 pm)"
  const tt = n => { if (!isFinite(n)) return 'never at this rate'; const k = Math.max(0, Math.ceil(n)); return `~${k} turn${k === 1 ? '' : 's'} (about ${clockText(whenMs(k), (store.get('turnAt', {}) || {}).exact)})`; };

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
  #mo nav.more{top:88px;flex-wrap:wrap;background:#efe8d6}
  #mo nav.more button{flex:0 0 auto;font-weight:500}
  #mo .x{border:0;background:none;color:#999;font-size:16px;padding:0 4px;min-height:0;float:right}
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
  #mo small.h{display:block;font-weight:400;font-size:11px;opacity:.85;margin-top:3px;text-align:left;white-space:normal}
  #mo .expl{background:#fff7d6;border:1px solid #e6d28a;border-radius:6px;padding:6px 8px;margin:6px 0;font-size:12px}
  #mo .chip{display:inline-block;padding:1px 7px;border-radius:10px;font-size:12px;font-weight:600;color:#fff;background:#888}
  #mo .chip.g{background:#1f8a4c}#mo .chip.y{background:#c28a00}#mo .chip.r{background:#c0392b}
  #mo .opt{border:1px solid #ddd3bb;border-radius:6px;padding:7px 8px;margin:5px 0}
  #mo .opt.best{border:2px solid #1f8a4c}
  #mo select{padding:7px;font-size:14px;border:1px solid #b9ad8f;border-radius:5px;max-width:100%}
  #mo table.t{width:100%;border-collapse:collapse;font-size:13px}
  #mo table.t td{padding:3px 4px;border-top:1px solid #eee4cc}
  #mo-toast{position:fixed;left:10px;right:10px;bottom:62px;z-index:100000;background:#222;color:#fff;padding:10px 12px;border-radius:8px;
    font:14px system-ui;display:none}
  @media (prefers-color-scheme: dark){
    #mo{background:#1c1b18;color:#eee;--mo-good:#6fcf8f;--mo-bad:#ff7b6b}
    #mo nav{background:#2a2822}
    #mo nav.more{background:#24221d}
    #mo .card,#mo .kpi div{background:#26241f;border-color:#3a372f}
    #mo button.b{background:#26241f;color:#eee;border-color:#555}
    #mo input{background:#26241f;color:#eee;border-color:#555}
    #mo .muted{color:#aaa}
    #mo nav button{color:#bbb}
    #mo nav button.on{color:#7ed49b;border-bottom-color:#7ed49b}
    #mo .expl{background:#3a3420;border-color:#6b5d2a}
    #mo .opt{border-color:#3a372f}
    #mo select{background:#26241f;color:#eee;border-color:#555}
    #mo table.t td{border-color:#3a372f}
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
      const [blds, boats, myC, townC, towns, notes, rec] = await Promise.all([
        Promise.all(ids.map(id => api('/buildings/' + id).catch(() => null))),
        Promise.all((biz.transport_ids || []).map(id => api('/transports/' + id).catch(() => null))),
        api('/businesses/' + BUSINESS + '/contracts').catch(() => ({})),
        api('/contracts/towns/' + TOWN).catch(() => ({})),
        townNames(),
        api('/notifications').catch(() => []),
        gameData().catch(() => ({ r: [], sizes: {} })),
      ]);
      const inv = (sh.storage || {}).inventory || {};
      const prevS = S;
      S = {
        hh, rec,
        rival: prevS && prevS.rival,
        justActed: !!(prevS && prevS.justActed),
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
      noteTurn(S.turn, false);
      S.m = money(S.flows, S.cash, S.turn);
      S.issues = findIssues(S);
      try { const pq = await prestigeAuto(); if (pq) { S.hh = await api('/households/' + HOUSEHOLD); S.pr = prestigeInfo(S.hh); } } catch (e) { toast('Prestige auto-buy failed: ' + e.message, 8000); }
      trackChanges();
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
  const priceOf = p => p === 'labour' ? (num(mkt('labour').last_price) || 1.7) : (num(mkt(p).last_price) || num((S.assets[p] || {}).unit_cost) || 0);
  const sizeOf = p => num((S.rec && S.rec.sizes || {})[p]) || 1;
  const cargoable = p => { const t = ((S.rec && S.rec.types) || {})[p]; return t ? t === 'commodity' : !['porterage', 'labour', 'donations'].includes(p); };

  // recipes and item sizes, read once from the game's own script (cached until the game updates)
  async function gameData() {
    const el = document.querySelector('script[src*="/static/js/main."]');
    const src = el ? el.src : null;
    const c = store.get('gamedata', null);
    if (c && c.src === src && c.v === 2 && c.r && c.r.length) return c;
    if (!src) return c || { r: [], sizes: {} };
    const js = await fetch(src).then(r => r.text());
    const r = [], sizes = {};
    const re = /\{"name":"([^"]+)","tier":\d+,"site":"([^"]+)"[^{}]*?"inputs":(\[[^\]]*\]),"outputs":(\[[^\]]*\])/g;
    let m;
    while ((m = re.exec(js))) {
      try {
        const ins = {}, outs = {};
        JSON.parse(m[3]).forEach(x => ins[x.product] = x.amount);
        JSON.parse(m[4]).forEach(x => outs[x.product] = x.amount);
        r.push({ name: m[1], site: m[2], in: ins, out: outs });
      } catch (e) { }
    }
    const pr = /\{"name":"([^"]+)","type":"([a-z]+)","unit":"[^"]*"([^{}]*)/g, types = {};
    while ((m = pr.exec(js))) { types[m[1]] = m[2]; const s = /"size":([\d.]+)/.exec(m[3]); if (s) sizes[m[1]] = +s[1]; }
    const res = { src, r, sizes, types, v: 2 };
    if (r.length) store.set('gamedata', res);
    return res;
  }
  const recipeByName = n => ((S.rec && S.rec.r) || []).find(r => r.name === n);
  const labourPer1x = recipe => { const r = recipeByName(recipe); return r ? num(r.in.labour) : 0; };

  // ---------------------------------------------------------------- change tracking
  function ordSnap() {
    const o = {};
    for (const [i, h] of Object.entries(S.holdings)) {
      if (SKIP_ITEMS.has(i)) continue;
      const ms = (h.managers || []).map(m => ({ bv: num(m.buy_volume), bp: num(m.buy_price), sv: num(m.sell_volume), sp: num(m.sell_price), mx: m.max_holding ?? null, mn: m.min_holding ?? null }));
      if (ms.length) o[i] = ms;
    }
    return o;
  }
  function prodSnap() {
    const o = {};
    for (const b of S.buildings) if (b.type !== 'warehouse') o[b.id] = { n: b.name, r: (b.producer || {}).recipe || null, t: num((b.producer || {}).target), p: b.construction ? num(b.construction.progress) : null };
    return o;
  }
  function stockSnap() {
    const o = {};
    for (const [i, a] of Object.entries(S.assets)) if (!SKIP_ITEMS.has(i) && i !== 'labour') o[i] = +num(a.balance).toFixed(1);
    return o;
  }
  const OL = { bv: 'buy vol', bp: 'buy max', sv: 'sell vol', sp: 'sell floor', mx: 'stop at', mn: 'keep' };
  function ordDiff(a, b) {
    const out = [];
    for (const i of new Set([...Object.keys(a || {}), ...Object.keys(b || {})])) {
      const x = (a || {})[i] || [], y = (b || {})[i] || [];
      if (x.length !== y.length) { out.push(`${i}: ${x.length} → ${y.length} order tiers`); continue; }
      y.forEach((t, j) => { for (const k in OL) if (String(x[j][k]) !== String(t[k])) out.push(`${i}${y.length > 1 ? ' tier ' + (j + 1) : ''} ${OL[k]} ${x[j][k] ?? '–'} → ${t[k] ?? '–'}`); });
    }
    return out;
  }
  function prodDiff(a, b) {
    const out = [];
    for (const [id, y] of Object.entries(b || {})) {
      const x = (a || {})[id];
      if (!x) { out.push(`${y.n}: new building`); continue; }
      if (x.r !== y.r) out.push(`${y.n}: ${x.r || 'stopped'} → ${y.r || 'stopped'}`);
      else if (y.r && Math.abs(x.t - y.t) >= 0.01) out.push(`${y.n} target ${f2(x.t)}x → ${f2(y.t)}x`);
    }
    return out;
  }
  // orders/targets that changed outside this panel go into the automation log;
  // the "since you last looked" card compares against the last time you tapped Got it
  function trackChanges() {
    const now = { turn: S.turn, at: Date.now(), cash: S.cash, ord: ordSnap(), prod: prodSnap(), stock: stockSnap() };
    const base = store.get('logBase', null);
    if (base && !S.justActed) {
      const ch = [...ordDiff(base.ord, now.ord), ...prodDiff(base.prod, now.prod)];
      if (ch.length) {
        const log = store.get('autolog', []);
        log.unshift({ turn: S.turn, at: Date.now(), ch });
        store.set('autolog', log.slice(0, 30));
      }
    }
    store.set('logBase', { ord: now.ord, prod: now.prod });
    S.justActed = false;
    const seen = store.get('seen', null);
    if (!seen) { store.set('seen', now); S.since = null; return; }
    if (seen.turn === S.turn) { S.since = null; return; }
    const ds = Object.keys(now.stock).map(i => ({ i, d: now.stock[i] - (seen.stock[i] || 0) })).filter(x => Math.abs(x.d) >= 1)
      .sort((a, b) => Math.abs(b.d * priceOf(b.i)) - Math.abs(a.d * priceOf(a.i)));
    const builds = [];
    for (const [id, y] of Object.entries(now.prod)) {
      const x = seen.prod[id];
      if (x && x.p != null && y.p == null) builds.push(`${y.n} FINISHED`);
      else if (y.p != null) builds.push(`${y.n} ${x && x.p != null ? f1(x.p) + '→' : ''}${f1(y.p)}%`);
    }
    const log = store.get('autolog', []).filter(l => l.at > seen.at).flatMap(l => l.ch);
    const filled = Object.entries(S.flows).flatMap(([i, f]) => [num(f.purchase) ? `bought ${f1(f.purchase)} ${i}` : null, num(f.sale) ? `sold ${f1(f.sale)} ${i}` : null]).filter(Boolean);
    S.since = { turns: S.turn - seen.turn, cash: S.cash - seen.cash, stock: ds.slice(0, 8), builds, log, filled };
  }
  function markSeen() {
    store.set('seen', { turn: S.turn, at: Date.now(), cash: S.cash, ord: ordSnap(), prod: prodSnap(), stock: stockSnap() });
    S.since = null;
  }

  // ---------------------------------------------------------------- household
  // how long stock lasts: sales stop at the sell tier's keep, after that only real use drains it
  function runway(item) {
    const f = flowsOf(item), have = held(item), ms = (S.holdings[item] || {}).managers || [];
    const use = num(f.consumption) - num(f.production) - num(f.purchase);
    const net = use + num(f.sale);
    if (!(net > 0.5) || have <= 0) return null;
    const sells = ms.filter(m => num(m.sell_volume));
    const keep = sells.length ? Math.min(...sells.map(m => num(m.min_holding))) : 0;
    if (keep > 0 && have > keep && num(f.sale) > 0) {
      const toKeep = (have - keep) / net;
      const after = use > 0.05 ? keep / use : Infinity;
      return { turns: toKeep + after, text: `${f1(have)} left, sales stop at keep ${f1(keep)} ${tt(toKeep)}; then ${f1(use)}/turn of use runs it out ${isFinite(after) ? tt(toKeep + after) : 'never'}` };
    }
    return { turns: have / net, text: `${f1(have)} left, falling ${f1(net)}/turn → runs out ${tt(have / net)}` };
  }
  function household() {
    const pf = (((S.hh || {}).sustenance || {}).inventory || {}).previous_flows || {};
    return Object.entries(pf).filter(([i, f]) => i !== 'donations' && num(f.consumption) > 0).map(([i, f]) => {
      const hu = num(f.consumption), have = held(i), r = runway(i);
      return { i, hu, have, turns: r ? r.turns : Infinity, short: num(f.shortfall) + num(flowsOf(i).shortfall) };
    }).sort((a, b) => a.turns - b.turns);
  }

  // ---------------------------------------------------------------- make / buy / import / sell less
  function options(item) {
    const f = flowsOf(item), have = held(item), ms = (S.holdings[item] || {}).managers || [];
    const need = Math.max(1, Math.ceil(num(f.consumption) - num(f.production) - num(f.purchase)) || Math.ceil(num(f.consumption)) || 1);
    const out = [];
    // make it
    const allowed = b => { const cur = (b.producer || {}).recipe; if (cur) return [cur]; const last = store.get('recipe:' + b.id, null);
      const a = [last && last.recipe, DEFAULT_RECIPES[b.type]].filter(Boolean); return a.length ? a : null; };
    for (const r of ((S.rec && S.rec.r) || []).filter(r => r.out[item])) {
      const b = S.buildings.find(x => x.type === r.site && (allowed(x) ? allowed(x).includes(r.name) : / 1$/.test(r.name)));
      if (!b) continue;
      const cost1x = Object.entries(r.in).reduce((a, [p, amt]) => a + amt * priceOf(p), 0);
      const unit = cost1x / r.out[item];
      const cur = (b.producer || {}).recipe === r.name ? num(b.producer.target) : 0;
      const add = clamp(Math.ceil(need / r.out[item] * 20) / 20, 0.05, Math.max(0.05, num(b.size) - cur));
      const to = +(cur + add).toFixed(2);
      out.push({ kind: 'make', unit, title: `Make it: ${b.name} ${r.name}${cur ? ` ${f2(cur)}x → ${f2(to)}x` : ` at ${f2(to)}x`}`,
        detail: `+${f1(add * r.out[item])} ${item}/turn for +${f1(add * num(r.in.labour))} labour · inputs ${Object.entries(r.in).map(([p, a]) => `${f1(a * add)} ${p}`).join(', ')} · ~${Math.round(cost1x * add)}/turn at today's prices`,
        label: cur ? `Raise to ${f2(to)}x` : `Start at ${f2(to)}x`, lab: add * num(r.in.labour),
        run: () => cur ? setTarget(b, to) : startWith(b, r.name, to) });
    }
    // buy it
    const x = mkt(item), ask = num(x.lowest_ask) || num(x.last_price);
    if (ask) {
      const price = snap(ask * 1.02, 1), bi = ms.findIndex(m => num(m.buy_volume));
      out.push({ kind: 'buy', unit: price, title: `Buy it: ${need}/turn ≤ ${f2(price)}`,
        detail: `lowest ask ${f2(ask)}, ~${f1(x.volume_ema_60)}/turn traded here · ~${Math.round(need * price)}/turn`,
        label: bi >= 0 ? `Buy tier → ${num(ms[bi].buy_volume) + need}/turn` : `Add buy ${need}/turn`,
        run: () => bi >= 0 ? setTier(item, bi, { buy_volume: num(ms[bi].buy_volume) + need, buy_price: String(Math.max(price, num(ms[bi].buy_price))) }) : addTier(item, { buy_volume: need, buy_price: String(price) }) });
    }
    // import it
    const scan = store.get('scan', null);
    if (scan && cargoable(item)) {
      let best = null;
      for (const t of scan.near) { const y = (scan.data[t.id] || {})[item]; const p = y && num(y.lowest_ask); if (p && (!best || p < best.p)) best = { p, t }; }
      if (best) {
        const units = Math.floor(CARGO / sizeOf(item)), trip = tripCost(best.t.d);
        const landed = best.p + trip / units;
        out.push({ kind: 'import', unit: landed, title: `Import it: ${best.t.n} ask ${f2(best.p)}`,
          detail: `~${best.t.d} tiles · a boat carries ~${units} · trip ~${Math.round(trip)} → ~${f2(landed)} each landed (cheaper if the boat is going anyway)`,
          label: 'Plan the trip', run: () => { store.set('tripTown', best.t.id); tab = 'boat'; store.set('tab', tab); render(); return false; } });
      }
    }
    // sell less
    const si = ms.map((m, i) => i).filter(i => num(ms[i].sell_volume));
    if (si.length) {
      const floor = Math.min(...si.map(i => num(ms[i].sell_price)));
      const keep = Math.ceil(have);
      out.push({ kind: 'sell', unit: floor, title: `Sell less: pause sales (keep → ${keep})`,
        detail: `gives up ~${f2(floor)} per unit we'd have sold · stock then lasts ${tt(have / Math.max(0.1, num(f.consumption) - num(f.production) - num(f.purchase)))}`,
        label: `Keep ${keep}`, run: async () => { for (const i of si) await setTier(item, i, { min_holding: keep }); } });
    }
    const best = out.reduce((b, o) => (!b || o.unit < b.unit ? o : b), null);
    if (best) best.best = true;
    return { need, have, out };
  }

  // ---------------------------------------------------------------- trips and contracts
  const tripCost = d => 2 * d * SEA_DETOUR * TRIP_PER_TILE;
  function planTripTo(townId) {
    const scan = store.get('scan', null);
    if (!scan) return null;
    const t = scan.near.find(x => x.id === String(townId)); if (!t) return null;
    const there = scan.data[t.id] || {};
    const outs = [], backs = [];
    for (const [i, h] of Object.entries(S.holdings)) {
      if (SKIP_ITEMS.has(i) || i === 'labour' || !cargoable(i)) continue;
      const ms = h.managers || [], y = there[i]; if (!y) continue;
      const home = mkt(i), sz = sizeOf(i);
      const keep = Math.max(0, ...ms.map(m => num(m.min_holding)));
      const surplus = ms.some(m => num(m.sell_volume)) ? held(i) - keep : 0;
      const bid = num(y.highest_bid), homeBid = num(home.highest_bid) || num(home.last_price);
      if (surplus > 1 && bid && homeBid && bid > homeBid * 1.03) {
        const q = Math.floor(Math.min(surplus, CARGO / sz, Math.max(5, num(y.volume_ema_60) * 2)));
        if (q > 0) outs.push({ i, q, p: bid, home: homeBid, gain: (bid - homeBid) * q, space: q * sz });
      }
      const ask = num(y.lowest_ask), homeAsk = num(home.lowest_ask) || num(home.last_price);
      const f = flowsOf(i), wants = ms.some(m => num(m.buy_volume)) || num(f.consumption) > num(f.production) + 0.5;
      if (wants && ask && homeAsk && ask < homeAsk * 0.97) {
        const q = Math.floor(Math.min(CARGO / sz, Math.max(10, (num(f.consumption) || num(f.purchase)) * 15), Math.max(5, num(y.volume_ema_60) * 2)));
        if (q > 0) backs.push({ i, q, p: ask, home: homeAsk, gain: (homeAsk - ask) * q, space: q * sz });
      }
    }
    const fill = list => { list.sort((a, b) => b.gain / b.space - a.gain / a.space); let room = CARGO; const res = [];
      for (const x of list) { if (room <= 0) break; const q = Math.min(x.q, Math.floor(room / sizeOf(x.i))); if (q <= 0) continue; room -= q * sizeOf(x.i); res.push({ ...x, q, gain: x.gain / x.q * q }); } return res; };
    const o = fill(outs), b = fill(backs), cost = tripCost(t.d);
    const gain = o.reduce((a, x) => a + x.gain, 0) + b.reduce((a, x) => a + x.gain, 0);
    return { t, out: o, back: b, cost, net: gain - cost };
  }
  function scoreContract({ c, t, theyBuy, fit }) {
    const price = num(t.price), vol = num(t.initial_volume) || num(t.volume), home = theyBuy ? (num(mkt(t.asset).highest_bid) || num(mkt(t.asset).last_price)) : (num(mkt(t.asset).lowest_ask) || num(mkt(t.asset).last_price));
    const d = c.local || String(c.town_id) === TOWN ? 0 : (tdist(c.town_id) || 300);
    const trips = d ? Math.max(1, Math.ceil(vol * sizeOf(t.asset) / CARGO)) : 0;
    const trip = trips * tripCost(d);
    const edge = home ? (theyBuy ? price - home : home - price) : 0;
    const net = edge * vol - trip;
    const pct = home ? net / (home * Math.max(1, vol)) : 0;
    let s = 50 + clamp(pct * 250, -50, 35), why = [];
    why.push(`${net >= 0 ? '+' : '−'}${Math.round(Math.abs(net))} vs home${trip ? ` after ~${Math.round(trip)} boat cost` : ''}`);
    if (fit) { s += 10; why.push(theyBuy ? 'we make/hold it' : 'we use it'); }
    const turns = (t.timeframe && t.timeframe.length) || 10;
    if (theyBuy) {
      const f = flowsOf(t.asset), spare = held(t.asset) + Math.max(0, num(f.production) - num(f.consumption)) * turns;
      const cap = vol ? spare / vol : 1;
      if (cap < 1) { s -= 30 * (1 - cap); why.push(`we can only cover ~${Math.round(cap * 100)}%`); if (t.penalty) s -= 10; }
    } else {
      const pay = price * vol;
      if (pay > S.cash - RESERVE) { s -= 40; why.push('would dip below the cash reserve'); }
    }
    if (!home) why.push('no home price to compare');
    s = Math.round(clamp(s, 0, 100));
    return { s, label: s >= 75 ? 'great' : s >= 55 ? 'ok' : s >= 35 ? 'poor' : 'skip', cls: s >= 75 ? 'g' : s >= 55 ? 'y' : 'r', why: why.join(' · '), net };
  }

  // ---------------------------------------------------------------- needs you / gate
  function gate() {
    const lab = num(mkt('labour').last_price), gar = num(mkt('garments').last_price);
    return [
      { k: 'labour', ok: lab && lab <= GATE.labour, v: f2(lab), t: `≤ ${GATE.labour}`, kill: lab > KILL.labour },
      { k: 'garments', ok: gar >= GATE.garments, v: f2(gar), t: `≥ ${GATE.garments}`, kill: gar && gar < KILL.garments },
      { k: 'cash', ok: S.cash > GATE.cash, v: Math.round(S.cash / 100) / 10 + 'k', t: `> ${GATE.cash / 1000}k` },
    ];
  }
  function chainBuilding(b) { return Object.values(CHAIN).some(x => x.id === String(b.id)); }
  function needsYou() {
    const done = store.get('needsDone', {});
    const hide = id => done[id] && (done[id] === 'done' || done[id] > S.turn);
    const list = NEEDS.filter(n => !hide(n.id)).map(n => {
      if (n.trip !== 'best') return n;
      const scan = store.get('scan', null);
      if (!scan || scan.at < Date.now() - 60 * 60e3) { if (!S.scanning) { S.scanning = true; regionalScan(true).then(() => { S.scanning = false; if (tab === 'issues') render(); }).catch(() => { S.scanning = false; }); } return { ...n, text: n.text + ' Scanning nearby markets for the best trip…' }; }
      const best = scan.near.map(t => planTripTo(t.id)).filter(Boolean).sort((a, b) => b.net - a.net)[0];
      if (!best) return { ...n, text: n.text + ' No trip data.' };
      return { ...n, trip: best.t.id, text: `${n.text} Best round trip: ${best.t.n} (${best.t.d} tiles) ${best.net >= 0 ? '+' : '−'}${Math.round(Math.abs(best.net))} net${best.net > 50 ? ', worth a run' : best.net > 0 ? ', marginal' : ', not worth it on its own'}.` };
    });
    const free = S.pr.free;
    // prestige queue (auto-buys; see PQUEUE). After a Tenants buy the farmstead expansion is the follow-up.
    const pqd = store.get('pqDone', null);
    if (pqd && pqd.track === 'tenants' && !hide('pq' + pqd.turn)) list.unshift({ id: 'pq' + pqd.turn, text: `Tenants bought (+5, ${pqd.cost} prestige). Next: expand the farmstead +5 plots (buy the plots, then expand; 500 labour + 100 timber). Ops is learning the expand request from the game, then this becomes one tap.`, link: ['Farmstead build page', '/town/' + TOWN + '/building/151602398/construction'] });
    const pqn = pqNext();
    if (pqn && pqn.free >= pqn.cost && !store.get('pqAuto', true) && !hide('pqready' + S.turn)) list.unshift({ id: 'pqready' + S.turn, text: `${pqn.label} is affordable (${pqn.cost}); auto-buy is off.`, link: ['Prestige board', '/household/prestige'] });
    // unread game notices: one tap clears them
    const unread = (S.notes || []).filter(n => !n.acked).length;
    if (unread && !hide('notes' + S.turn)) list.push({ id: 'notes' + S.turn, text: `${unread} game notice${unread > 1 ? 's' : ''} (e.g. builds finished). Seen them in Upcoming?`, clearnotes: true });
    const g = gate(), p1busy = S.buildings.some(b => b.construction && chainBuilding(b));
    if (!p1busy && g.every(x => x.ok) && !hide('phase2')) list.unshift({ id: 'phase2', text: 'Phase 1 builds are done and the Phase 2 gate is green: queue weavery +1 and spinnery +1 (~4.6k)? Your call (Taylor: wait for Phase 1 sales data first).', link: ['Weavery build page', '/town/' + TOWN + '/building/152202388001005/construction'] });
    const kill = g.filter(x => x.kill);
    if (kill.length && !hide('kill' + S.turn)) list.unshift({ id: 'kill' + S.turn, text: `Kill switch: ${kill.map(x => x.k + ' ' + x.v).join(', ')}. Plan says stop adding and trim weavery/sewing if this lasts several turns.`, tab: 'prod' });
    try {
      const good = (S.townContracts || []).filter(c => !c.signed).map(c => { const t = (c.transactions || [])[0] || {}; const theyBuy = t.direction === 'bid'; return scoreContract({ c, t, theyBuy, fit: false }); }).filter(x => x.s >= 75);
      if (good.length && !hide('contracts' + S.turn)) list.push({ id: 'contracts' + S.turn, text: `${good.length} contract offer${good.length > 1 ? 's' : ''} scored great on the board.`, tab: 'deals' });
    } catch (e) { }
    return list;
  }
  // labour guard: ask before adding labour when the price is near the gate
  function labourOk(addLab) {
    const p = num(mkt('labour').last_price);
    if (!(addLab > 1) || p < LABOUR_WARN) return true;
    return confirm(`Labour is at ${f2(p)} (Phase 2 gate ${GATE.labour}, kill switch ${KILL.labour}).\nThis adds ~${Math.round(addLab)} labour/turn to our buy, which pushes the price up.\n\nGo ahead?`);
  }

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
  function chainState(sizeOverride) {
    const b = {}, size = {}, cur = {};
    for (const [k, c] of Object.entries(CHAIN)) {
      b[k] = S.buildings.find(x => String(x.id) === c.id);
      if (!b[k] || !b[k].producer || !b[k].producer.recipe) return null;
      size[k] = num(b[k].size); cur[k] = num(b[k].producer.target);
    }
    Object.assign(size, sizeOverride || {});
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
  // what the balancer will do as each chain expansion lands, in ETA order
  function chainNext() {
    const pend = [];
    for (const [k, c] of Object.entries(CHAIN)) {
      const b = S.buildings.find(x => String(x.id) === c.id);
      if (b && b.construction && b.construction.stage === 'EXPANSION') pend.push({ k, b, eta: buildEta(b) });
    }
    pend.sort((a, b) => a.eta.turns - b.eta.turns);
    const over = {}, steps = [];
    for (const p of pend) {
      over[p.k] = num(p.b.size) + 1;
      const c = chainState({ ...over });
      if (c) steps.push({ ...p, c });
    }
    return steps;
  }
  function buildEta(b) {
    const c = b.construction; if (!c || !c.inventory) return { turns: Infinity, limit: '' };
    const a = (c.inventory.account || {}).assets || {}, fl = c.inventory.previous_flows || {};
    let worst = 0, limit = '';
    for (const [k, v] of Object.entries(a)) {
      if (k === 'money') continue;
      const left = num(v.capacity) - num(v.balance); if (left <= 0.01) continue;
      const rate = num((fl[k] || {}).consumption);
      const t = rate > 0 ? left / rate : Infinity;
      if (t > worst) { worst = t; limit = k; }
    }
    return { turns: worst, limit };
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
    // v1.8: the chain uses all its fibres and plants: no sell orders on them
    for (const item of ['flax fibres', 'flax plants']) if (((S.holdings[item] || {}).managers || []).some(m => num(m.sell_volume))) await dropSide(item, 'sell');
  }

  // ---------------------------------------------------------------- issues
  function findIssues(S) {
    const out = [];
    const L = S.flows.labour || {};
    const exp = num(L.expiration), short = num(L.shortfall);
    const lm = (S.holdings.labour || {}).managers || [];
    if (exp > 5 && lm.length) out.push({ lvl: 'warn', item: 'labour', text: `Labour: ${f1(exp)} bought labour expired unused`,
      fixes: [{ safe: true, h: 'Lowers the labour buy by what expired, so we stop paying for labour nobody used', label: `Trim buy −${Math.round(exp)}`, run: () => setTier('labour', 0, { buy_volume: Math.max(0, num(lm[0].buy_volume) - Math.round(exp)) }) }] });

    for (const item of Object.keys(S.flows)) {
      const f = S.flows[item], sf = num(f.shortfall);
      if (sf > 0) {
        const ms = (S.holdings[item] || {}).managers || [];
        const bi = ms.findIndex(m => num(m.buy_volume));
        const fixes = [];
        if (bi >= 0) {
          fixes.push({ h: 'Raises the buy order by the shortfall', label: `Buy +${Math.ceil(sf)}/turn`, run: () => setTier(item, bi, { buy_volume: num(ms[bi].buy_volume) + Math.ceil(sf) }) });
          fixes.push({ h: 'Lets the buy order pay 5% more so it fills', label: 'Max price +5%', run: () => setTier(item, bi, { buy_price: String(snap(num(ms[bi].buy_price) * 1.05, 1)) }) });
        } else {
          const ask = num(mkt(item).lowest_ask) || num(mkt(item).last_price);
          if (ask) fixes.push({ h: 'Adds a buy order just above the lowest ask', label: `Add buy ${Math.ceil(sf)} ≤ ${f2(snap(ask * 1.05, 1))}`, run: () => addTier(item, { buy_volume: Math.ceil(sf), buy_price: String(snap(ask * 1.05, 1)) }) });
        }
        out.push({ lvl: 'bad', item, opt: item !== 'labour' && !!S.holdings[item], text: `${item}: ${f1(sf)} short last turn`, fixes });
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
        out.push({ lvl: 'bad', item, opt: true, text: `${item}: buy filled ${f1(bought)}/${f1(buyVol)}, ${f1(have)} left, dropping ${f1(net)}/turn, runs out ${tt(have / net)}. Max ${f2(cur)}${ask ? ', lowest ask ' + f2(ask) : ''}`,
          fixes: [{ h: 'Raises the buy max so the order can fill', label: `Max → ${f2(to)}`, run: () => setTier(item, bi, { buy_price: String(to) }) }] });
      }
      // sell not moving while stock piles up
      if (sellVol > 0 && sold < sellVol * 0.5 && have > keep + 2 * sellVol && net + sold <= 0) {
        const si = ms.reduce((best, m, i) => num(m.sell_volume) && (best < 0 || num(m.sell_price) < num(ms[best].sell_price)) ? i : best, -1);
        const cur = num(ms[si].sell_price);
        const bid = num(mkt(item).highest_bid);
        const to = snap(cur * 0.97, -1);
        out.push({ lvl: 'warn', item, text: `${item}: sold ${f1(sold)}/${f1(sellVol)}, ${f1(have)} held. Floor ${f2(cur)}${bid ? ', best bid ' + f2(bid) : ''}`,
          fixes: [{ h: 'Lowers the sell floor 3% so stock moves', label: `Floor → ${f2(to)}`, run: () => setTier(item, si, { sell_price: String(to) }) }] });
      }
      // using it, running low, nothing buying it
      if (!buyVol && net > 0 && have < net * 5) {
        const ask = num(mkt(item).lowest_ask) || num(mkt(item).last_price);
        out.push({ lvl: 'warn', item, opt: true, text: `${item}: ${f1(have)} left, dropping ${f1(net)}/turn, runs out ${tt(have / net)}, no buy order`,
          fixes: ask ? [{ h: 'Adds a buy order just above the lowest ask', label: `Add buy ${Math.ceil(net)} ≤ ${f2(snap(ask * 1.05, 1))}`, run: () => addTier(item, { buy_volume: Math.ceil(net), buy_price: String(snap(ask * 1.05, 1)) }) }] : [] });
      }
    }

    for (const b of S.buildings) {
      if (b.producer && b.producer.recipe && b.producer.provider_id == null && b.provider_id == null && b.type !== 'warehouse')
        out.push({ lvl: 'bad', item: b.name, text: `${b.name}: producing but not linked to the storehouse`, fixes: [{ h: 'Points the building at the storehouse for inputs and outputs', label: 'Link to storehouse', run: () => linkStore(b) }, { label: 'Open', run: () => go(b, 'production') }] });
      const c = b.construction;
      if (c && c.inventory) {
        const fl = c.inventory.previous_flows || {};
        const sh = Object.entries(fl).filter(([k, v]) => num(v.shortfall) > 0).map(([k, v]) => `${k} ${f1(v.shortfall)}`);
        if (sh.length) out.push({ lvl: 'warn', item: b.name, text: `${b.name} build short: ${sh.join(', ')}`, fixes: [{ label: 'Open', run: () => go(b, 'construction') }] });
      }
    }
    // stock going off
    for (const [item, f] of Object.entries(S.flows)) {
      const ex = num(f.expiration);
      if (item === 'labour' || ex < 1 || SKIP_ITEMS.has(item)) continue;
      const ms = (S.holdings[item] || {}).managers || [], x = mkt(item);
      const fixes = [];
      const bid = num(x.highest_bid) || num(x.last_price) * 0.95;
      if (!ms.some(m => num(m.sell_volume)) && bid) fixes.push({ h: 'Adds a sell order for the spare so it earns instead of spoiling (keeps 3 turns of our own use)', label: `Sell ${Math.ceil(ex)}/turn ≥ ${f2(snap(bid, -1))}`, run: () => addTier(item, { sell_volume: Math.ceil(ex), sell_price: String(snap(bid, -1)), min_holding: Math.ceil(num(f.consumption) * 3) }) });
      out.push({ lvl: 'warn', item, text: `${item}: ${f1(ex)} went off last turn (made/bought ${f1(num(f.production) + num(f.purchase))}, used ${f1(f.consumption)}, sold ${f1(f.sale)})`, fixes });
    }
    try {
      const c = chainState();
      if (c && c.moves.length && (Math.abs(c.dLab) >= 10 || Math.abs(c.gNew - c.gNow) >= 2))
        out.push({ lvl: 'warn', item: 'thread', text: `Textile chain out of balance: ${c.moves.map(x => `${x.k} ${f2(x.from)}→${f2(x.to)}x`).join(', ')} (garments ${f1(c.gNow)}→${f1(c.gNew)}/turn, labour ${c.dLab >= 0 ? '+' : ''}${Math.round(c.dLab)})`,
          fixes: [{ h: 'Sets all five chain steps to feed the most garments the plots allow, and adjusts labour/tools buys and the garments sell', label: 'Balance chain', lab: c.dLab, run: () => balanceChain(c) }] });
    } catch (e) { /* chain not readable */ }
    try { out.push(...extraIssues(S)); } catch (e) { }
    const order = { bad: 0, warn: 1 };
    return out.sort((a, b) => order[a.lvl] - order[b.lvl]);
  }

  function badge() {
    const n = S && S.issues ? visibleIssues().length : 0;
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
    // same request the game's "Link with warehouse" dialog sends
    await api('/buildings/' + b.id, 'PATCH', { provider_id: STORE, high_priority: false, bring_leftovers: false, autoset_inventory: false });
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
  async function startWith(b, recipe, target) {
    await api('/buildings/' + b.id + '/producer', 'PUT', {
      recipe, target: Math.min(target, num(b.size)).toFixed(3), manager: 'static',
      autoset_buying: false, autoset_selling: false, allow_fallback: false, allow_overprod: false, cargo_transfer: false,
    });
    try { await linkStore(b); } catch (e) { toast('Started, but relink failed: ' + e.message + ' (use Open)', 6000); }
  }
  function go(b, page) { location.href = `/town/${b.town_id || TOWN}/building/${b.id}/${page}`; }

  async function act(fn, label) {
    try { const r = await fn(); if (r === false) return; toast('Done: ' + label); } catch (e) { toast('Failed: ' + e.message, 6000); }
    if (S) S.justActed = true;
    setTimeout(load, 400);
  }

  // ---------------------------------------------------------------- render
  function render() {
    const L = S.flows.labour || {};
    const lIn = num(L.production) + num(L.purchase), lUse = num(L.consumption);
    const nNeeds = needsYou().length;
    const nIss = visibleIssues().length;
    const tabs = [['issues', `Issues${nIss + nNeeds ? ' (' + (nIss + nNeeds) + ')' : ''}`], ['plan', 'Plan']];
    const more = [['prod', 'Production'], ['orders', 'Orders'], ['build', 'Build'], ['boat', 'Boat'], ['deals', 'Contracts'], ['mkt', 'Markets'], ['money', 'Money'], ['charts', 'Charts'], ['shame', 'Wall of shame'], ['sos', store.get('emergency', null) ? 'EMERGENCY' : 'Emergency']];
    const moreOn = store.get('moreOpen', false) || more.some(([k]) => k === tab);
    const explain = store.get('explain', false);
    const toGo = 200 - S.pr.free;
    const g = gate();
    panel.innerHTML = `
      <header><b>Merc Ops <span style="font-weight:400;opacity:.75;font-size:12px">v${VERSION}</span></b><button data-x="sos" style="background:#c0392b;border-color:#fff8">SOS</button><button data-x="help" style="${explain ? 'background:#fff;color:#1f5130' : ''}">?</button><button data-x="refresh">Refresh</button><button data-x="close">Close</button></header>
      <nav>${tabs.map(([k, l]) => `<button data-tab="${k}" class="${tab === k ? 'on' : ''}">${l}</button>`).join('')}<button data-more="1" class="${moreOn ? 'on' : ''}">More ${moreOn ? '▴' : '▾'}</button></nav>
      ${moreOn ? `<nav class="more">${more.map(([k, l]) => `<button data-tab="${k}" class="${tab === k ? 'on' : ''}">${l}</button>`).join('')}</nav>` : ''}
      <section>
        ${explain ? '<div class="expl">Explain mode is on: every button shows what it does. Tap <b>?</b> again to hide. Header: Refresh reloads from the game, Close hides the panel. The chips under the numbers are the Phase 2 gate (green = passing).</div>' : ''}
        <div class="kpi">
          <div>Cash <b>${Math.round(S.cash).toLocaleString()}</b>
            · profit <b style="color:${S.m.profit >= 0 ? 'var(--mo-good)' : 'var(--mo-bad)'}">${sgn(S.m.profit)}</b>
            · <b style="color:${S.m.delta == null ? 'inherit' : S.m.delta >= 0 ? 'var(--mo-good)' : 'var(--mo-bad)'}">${S.m.delta == null ? '±?' : sgn(S.m.delta)}</b>${S.m.deltaTurns > 1 ? ` <span class="muted">(${S.m.deltaTurns} turns)</span>` : ''}</div>
          <div>Prestige <b>${f1(S.pr.free)}</b> spendable · <b>${S.pr.rate >= 0 ? '+' : '−'}${Math.abs(S.pr.rate).toFixed(1)}</b>/turn${toGo > 0 && S.pr.rate > 0 ? ` <span class="muted">· 200 ${tt(toGo / S.pr.rate)}</span>` : ''}</div>
          <div>Labour <b>${f1(lIn)}</b> in / <b>${f1(lUse)}</b> used${num(L.expiration) ? ` · <span style="color:#d68910">${f1(L.expiration)} expired</span>` : ''}${num(L.shortfall) ? ` · <span style="color:#c0392b">${f1(L.shortfall)} short</span>` : ''}</div>
          <div>Phase 2 gate ${g.map(x => `<span class="chip ${x.ok ? 'g' : 'r'}">${x.k} ${x.v}</span>`).join(' ')}</div>
        </div>
        ${store.get('emergency', null) ? '<div class="card bad"><b>Emergency mode is on.</b> Buys are off. <button class="b" data-x="sos">Open</button></div>' : ''}
        <div id="mo-body"></div>
      </section>`;
    const body = panel.querySelector('#mo-body');
    ({ issues: renderIssues, prod: renderProd, orders: renderOrders, build: renderBuild, boat: renderBoat, deals: renderDeals, mkt: renderMarkets, money: renderMoney, charts: renderCharts, plan: renderPlan, sos: renderSos, shame: renderShame }[tab] || renderIssues)(body);
    if (explain) panel.querySelectorAll('#mo-body button, #mo-body a.b').forEach(b => { const h = helpFor(b); if (h) b.insertAdjacentHTML('beforeend', `<small class="h">${esc(h)}</small>`); });
    wire();
  }

  // explain mode text for every button
  function helpFor(b) {
    const d = b.dataset;
    if (d.fix) { const [i, j] = d.fix.split(':').map(Number); const f = S.issues[i] && S.issues[i].fixes[j]; return f && f.h; }
    if (d.optrun) { const [item, k] = d.optrun.split('|'); const o = (options(item).out || [])[+k]; return o ? { make: 'Starts or raises the building that makes it', buy: 'Adds or raises a storehouse buy order at this price', import: 'Opens the trip planner for that town on the Boat tab', sell: 'Stops selling by setting keep to what we hold now' }[o.kind] : null; }
    if (d.tab) return null;
    if (d.x) return { sos: 'Opens the emergency page (nothing changes until you confirm there)', help: 'Turns these explanations on and off', refresh: 'Reloads everything from the game', close: 'Hides the panel (the Ops button brings it back)' }[d.x];
    if (d.t) return { '-': "Lowers the production target by 10% of the building's size", '+': "Raises the production target by 10% of the building's size", max: "Sets the target to the building's plot count (full output)" }[d.t.split(':')[1]];
    if (d.boat) return { '-': 'Fishing level −10%', '+': 'Fishing level +10%', stop: "Stops the boat's current operation", home: 'Sails the boat back to Strasclives' }[d.boat.split(':')[1]];
    if (d.needdone) return 'Hides this item for good on this device';
    if (d.needlater) return 'Hides this item for 12 turns';
    if (d.needgo) return 'Takes you where you can do it';
    const map = { stock: "Opens this item's orders", opt: 'Shows make / buy / import / sell-less choices with costs', stop: 'Halts production and remembers the recipe; Start in this panel relinks the storehouse',
      start: 'Starts production (asks recipe and target) and links it to the storehouse', open: "Opens the game's own page for this building", balance: 'Sets all five chain steps to feed the most garments the plots allow, and adjusts the labour/tools buys and garments sell',
      edit: 'Shows the buy/sell tiers for this item so you can change them', save: 'Saves these tiers to the storehouse (asks first)', addtier: 'Adds an empty tier', scan: 'Reads the markets of the 14 nearest towns (a few seconds)',
      seen: 'Clears this card until the next turn', sosgo: 'Saves every order, target and build pace, then turns off all buys and fits production to our own labour and stock (asks first)', sosundo: 'Restores everything saved when emergency mode started', sosreserve: 'Raises sell keeps / buy stop-ats so household goods cover 24 turns', more: 'Shows the other pages', dismiss: 'Clears this card for 12 turns (it comes back sooner if it gets worse)', clearall: 'Clears every card in this list for 12 turns', unclear: 'Shows cleared cards again', fixsafe: 'Applies every low-risk fix (marked ✓) after showing you the list', pqauto: 'Turns automatic prestige buying on or off (this device)', clearnotes: 'Marks all game notices as read', copyrec: 'Copies the recorded game requests so Claude can build one-tap actions from them', clearrec: 'Empties the recorded requests', rivalseen: 'Remembers the rival buildings as they are now, so only new changes get flagged', trip: 'Picks the destination for the trip plan', clearlog: 'Empties the change log on this device' };
    for (const k in map) if (d[k] != null) return map[k];
    if (b.tagName === 'A' && /actionid/.test(b.getAttribute('href') || '')) return "Opens the game's accept screen for this offer; you confirm there";
    return null;
  }

  function upcoming() {
    const out = [];
    for (const b of S.buildings) {
      const c = b.construction; if (!c || !c.inventory) continue;
      const { turns: worst, limit } = buildEta(b);
      const pct = f1(c.progress);
      const eta = worst === 0 ? 'materials all in, finishing' : isFinite(worst) ? `done ${tt(worst)}, ${limit} is the slowest` : `stalled: no ${limit} delivered last turn`;
      out.push({ lvl: isFinite(worst) ? (worst <= 3 ? 'soon' : 'later') : 'stuck', sort: isFinite(worst) ? worst : 999,
        text: `${b.name} ${c.stage === 'EXPANSION' ? 'expansion' : 'build'}: ${pct}% · ${eta}${chainBuilding(b) ? ' · the chain balancer rebalances production when it lands' : ''}` });
    }
    for (const [item, h] of Object.entries(S.holdings)) {
      if (SKIP_ITEMS.has(item) || item === 'labour') continue;
      const f = flowsOf(item), have = held(item);
      const r = runway(item);
      if (r && r.turns < 15) out.push({ item, lvl: r.turns <= 4 ? 'soon' : 'later', sort: r.turns, text: `${item}: ${r.text}` });
    }
    const toGo = 200 - S.pr.free;
    if (toGo > 0 && S.pr.rate > 0 && toGo / S.pr.rate < 48) out.push({ lvl: 'later', sort: toGo / S.pr.rate, text: `prestige: 200 spendable (Tenants) ${tt(toGo / S.pr.rate)}` });
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

  function optionsHtml(item) {
    const o = options(item);
    if (!o.out.length) return `<div class="muted">No options found for ${esc(item)} (no recipe we can run, no market here).</div>`;
    return `<div class="muted" style="margin:4px 0">Need ~${o.need}/turn · ${f1(o.have)} held. Cheapest per unit is outlined.</div>` + o.out.map((x, k) => `
      <div class="opt ${x.best ? 'best' : ''}"><b>${esc(x.title)}</b> <span class="muted">~${f2(x.unit)}/unit</span>
        <div class="muted">${esc(x.detail)}</div>
        <div class="row" style="margin-top:4px"><button class="${x.kind === 'sell' ? 'b' : 'a'}" data-optrun="${esc(item)}|${k}">${esc(x.label)}</button></div></div>`).join('');
  }

  function renderIssues(el) {
    const openOpt = store.get('optItem', null);
    const optBtn = item => `<button class="b" data-opt="${esc(item)}">${openOpt === item ? 'Hide options' : 'Options'}</button>`;
    const optBox = item => openOpt === item ? `<div style="margin-top:6px">${optionsHtml(item)}</div>` : '';
    // needs you
    const needs = needsYou();
    let h = needs.length ? `<h4 style="margin:6px 0">Needs you (${needs.length})</h4>` + needs.map(n => `
      <div class="card warn"><div>${esc(n.text)}</div>
        <div class="row" style="margin-top:6px">
          ${n.opt ? optBtn(n.opt) : ''}${n.link ? `<button class="a" data-needgo="link:${esc(n.link[1])}">${esc(n.link[0])}</button>` : ''}${n.trip ? `<button class="a" data-needgo="trip:${esc(n.trip)}">Plan a trip</button>` : ''}${n.tab ? `<button class="a" data-needgo="tab:${n.tab}">Go</button>` : ''}${n.clearnotes ? '<button class="a" data-clearnotes="1">Clear notices</button>' : ''}
          <button class="b" data-needdone="${esc(n.id)}">Done</button><button class="b" data-needlater="${esc(n.id)}">Later</button></div>
        ${n.opt ? optBox(n.opt) : ''}</div>`).join('') : '';
    // since you last looked
    const sn = S.since;
    if (sn) {
      h += `<div class="card ok"><b>Since you last looked</b> <span class="muted">(${sn.turns} turn${sn.turns === 1 ? '' : 's'})</span>
        <div>Cash <b style="color:${sn.cash >= 0 ? 'var(--mo-good)' : 'var(--mo-bad)'}">${sgn(sn.cash)}</b></div>
        ${sn.stock.length ? `<div class="muted">Stock: ${sn.stock.map(x => `${esc(x.i)} ${x.d >= 0 ? '+' : '−'}${f1(Math.abs(x.d))}`).join(' · ')}</div>` : ''}
        ${sn.filled.length ? `<div class="muted">Last turn's trades: ${esc(sn.filled.slice(0, 8).join(' · '))}</div>` : ''}
        ${sn.builds.length ? `<div class="muted">Builds: ${esc(sn.builds.join(' · '))}</div>` : ''}
        ${sn.log.length ? `<div class="muted">Changed outside this panel (bot, balancer or the game page): ${esc(sn.log.slice(0, 8).join(' · '))}${sn.log.length > 8 ? ` +${sn.log.length - 8} more (Plan tab)` : ''}</div>` : ''}
        <div class="row" style="margin-top:6px"><button class="b" data-seen="1">Got it</button></div></div>`;
    }
    // problems (v1.8: clear per card, clear all, fix all safe)
    const vis = visibleIssues();
    const safe = vis.filter(x => x.it.fixes.some(f => f.safe));
    const nHidden = S.issues.length - vis.length;
    h += `<div class="row" style="margin:12px 0 6px"><h4 class="grow" style="margin:0">Problems${vis.length ? ` (${vis.length})` : ''}</h4>
      ${safe.length ? `<button class="a" data-fixsafe="1">Fix all safe (${safe.length})</button>` : ''}${vis.length ? '<button class="b" data-clearall="i">Clear all</button>' : ''}</div>`;
    h += vis.length ? vis.map(({ it, i }) => `
      <div class="card ${it.lvl}"><button class="x" data-dismiss="i:${i}" title="Clear">✕</button><div>${esc(it.text)}</div>
        <div class="row" style="margin-top:6px">${it.fixes.map((f, j) => `<button class="a" data-fix="${i}:${j}">${esc(f.label)}${f.safe ? ' ✓' : ''}</button>`).join('')}
        ${it.opt ? optBtn(it.item) : ''}<button class="b" data-stock="${esc(it.item)}">Details</button></div>${it.opt ? optBox(it.item) : ''}</div>`).join('')
      : '<div class="card ok"><b>All clear.</b> <span class="muted">No shortages, waste, stuck orders or stalled builds last turn.</span></div>';
    if (nHidden) h += `<p class="muted">${nHidden} cleared (they come back in 12 turns, or sooner if they get worse). <button class="b" data-unclear="i">Show</button></p>`;
    // upcoming
    const upAll = upcoming(), up = upAll.map((u, k) => ({ u, k })).filter(x => !isHidden('u', x.u));
    h += `<div class="row" style="margin:14px 0 6px"><h4 class="grow" style="margin:0">Upcoming</h4>${up.length ? '<button class="b" data-clearall="u">Clear all</button>' : ''}</div>` + (up.length ? up.map(({ u, k }) => `<div class="card ${u.lvl === 'soon' ? 'warn' : u.lvl === 'stuck' ? 'bad' : ''}"><button class="x" data-dismiss="u:${k}" title="Clear">✕</button>${u.lvl === 'soon' ? '<b>Soon</b> · ' : ''}${esc(u.text)}
        ${u.item ? `<div class="row" style="margin-top:6px">${optBtn(u.item)}</div>${optBox(u.item)}` : ''}</div>`).join('') : '<p class="muted">Nothing finishing or running out soon.</p>');
    // household
    const hh = household();
    if (hh.length) h += `<h4 style="margin:14px 0 6px">Household</h4><div class="card"><table class="t">${hh.map(x => `<tr><td><b>${esc(x.i)}</b></td><td>${f1(x.have)} held</td><td>uses ${f1(x.hu)}/turn</td>
        <td style="color:${x.short ? 'var(--mo-bad)' : x.turns < 5 ? '#d68910' : 'inherit'}">${x.short ? `${f1(x.short)} SHORT` : isFinite(x.turns) ? (x.turns > 99 ? '99+ turns' : `${Math.floor(x.turns)} turns`) : 'steady'}</td></tr>`).join('')}</table>
        <div class="muted" style="margin-top:4px">What the household eats and wears, from the storehouse. Turns = how long stock lasts at last turn's rates (sales stop at their keep); steady = production or buys cover it.</div></div>`;
    el.innerHTML = h;
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
      .filter(i => q ? i.includes(q) : (S.holdings[i].managers || []).length).sort();
    const open = store.get('openItem', null);
    const side = i => { const ms = S.holdings[i].managers || []; const b = ms.some(m => num(m.buy_volume)), s2 = ms.some(m => num(m.sell_volume)); return b && s2 ? 'both' : b ? 'buy' : s2 ? 'sell' : 'none'; };
    const groups = [['buy', 'Buying'], ['sell', 'Selling'], ['both', 'Buying and selling'], ['none', 'No orders']];
    const line = item => {
      const f = flowsOf(item), ms = S.holdings[item].managers || [], m = mkt(item);
      const did = [num(f.purchase) ? `bought ${f1(f.purchase)}` : '', num(f.sale) ? `sold ${f1(f.sale)}` : '', num(f.shortfall) ? `<b style="color:var(--mo-bad)">short ${f1(f.shortfall)}</b>` : '', num(f.expiration) ? `<b style="color:#d68910">wasted ${f1(f.expiration)}</b>` : ''].filter(Boolean).join(' · ');
      const isOpen = open === item;
      return `<div class="card" style="padding:7px 9px"><div class="row" data-item="${esc(item)}"><div class="grow"><b>${esc(item)}</b> <span class="muted">${f1(held(item))} held${m.last_price ? ' · mkt ' + f2(m.last_price) : ''}</span>
          <br><span style="font-size:13px">${ms.map(tierLine).join(' | ') || 'no orders'}</span>${did ? `<br><span class="muted">${did}</span>` : ''}</div>
          <button class="b" data-edit="${esc(item)}">${isOpen ? 'Hide' : 'Edit'}</button></div>${isOpen ? editor(item, ms) : ''}</div>`;
    };
    el.innerHTML = `<input class="search" data-q placeholder="Search any item (e.g. porterage)" value="${esc(q)}">` +
      groups.map(([g, t]) => { const its = items.filter(i => side(i) === g); return its.length ? `<h4 style="margin:10px 0 4px">${t} <span class="muted">(${its.length})</span></h4>` + its.map(line).join('') : ''; }).join('') +
      (q ? '' : '<p class="muted">Only items with orders are listed. Search to find any other item and add an order.</p>');
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
          <div class="muted">${f1(c.progress)}% · ${(e => e.turns === 0 ? 'finishing' : isFinite(e.turns) ? 'done ' + tt(e.turns) : 'stalled')(buildEta(b))} · ${need}</div>
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
      const home = Math.hypot(loc.x - hx, loc.y - hy) <= 2 && !(j.legs || []).some(l => (l.path || []).length > 1);
      const fishing = p.recipe && /fish/.test(p.recipe);
      const state = fishing ? `fishing (${esc(p.recipe)}) at ${loc.x}:${loc.y}` : home ? 'docked at Strasclives' : `at sea ${loc.x}:${loc.y}`;
      const cargo = Object.entries(((t.cargo || {}).inventory || {}).account?.assets || {}).filter(([k, v]) => k !== 'money' && num(v.balance) > 0.01).map(([k, v]) => `${k} ${f1(v.balance)}`).join(', ');
      return `<div class="card ok"><b>${esc(t.name)}</b> <span class="muted">${esc(t.type)}</span>
        <div>${state}</div>
        <div class="muted">${p.recipe ? `level ${Math.round(num(p.target) * 100)}%` : 'no operation'}${t.fish_quantity != null ? ` · fish here: ${t.fish_quantity}` : ''} · cargo: ${cargo || 'empty'}${j.end_town_id && !home ? ` · heading to ${esc(tname(j.end_town_id))}` : ''}</div>
        <div class="ctl" style="grid-template-columns:repeat(4,1fr)">
          ${p.recipe ? `<button class="b" data-boat="${t.id}:-">− 10%</button><button class="b" data-boat="${t.id}:+">+ 10%</button><button class="r" data-boat="${t.id}:stop">Stop</button>` : `<button class="b" disabled style="grid-column:span 3">Start fishing from the boat page</button>`}
          <button class="b" data-boat="${t.id}:home" ${home ? 'disabled' : ''}>Home</button>
        </div>
        <div class="row" style="margin-top:6px"><a class="muted" href="/transport/${t.id}/operation">Boat page →</a> · <a class="muted" href="/transport/${t.id}/journey">Journey / send →</a></div></div>`;
    }).join('') + '<p class="muted">Fishing level steps 10% (10% = 5 fish/turn on fishing 2). Home sails back to Strasclives; Stop ends the current operation.</p>' + tripHtml();
  }

  function tripHtml() {
    const scan = store.get('scan', null);
    let h = '<h4 style="margin:14px 0 6px">Round-trip planner</h4>';
    if (!scan) return h + '<div class="card"><div class="muted">Needs a nearby market scan first.</div><div class="row" style="margin-top:6px"><button class="a" data-scan="1">Scan nearby towns</button></div></div>';
    let sel = store.get('tripTown', null);
    if (sel && !/^\d+$/.test(sel)) { const m = scan.near.find(t => t.n === sel); sel = m ? m.id : null; }
    const plans = scan.near.map(t => planTripTo(t.id)).filter(Boolean).sort((a, b) => b.net - a.net);
    if (!sel && plans.length) sel = plans[0].t.id;
    const p = planTripTo(sel);
    h += `<div class="card"><div class="row"><select data-trip="1">${plans.map(x => `<option value="${x.t.id}" ${x.t.id === sel ? 'selected' : ''}>${esc(x.t.n)} · ${x.t.d} tiles · ${x.net >= 0 ? '+' : '−'}${Math.round(Math.abs(x.net))}</option>`).join('')}</select></div>`;
    if (p) {
      const line = (x, out) => `<tr><td>${esc(x.i)}</td><td>${x.q}</td><td>${out ? 'sell' : 'buy'} ${f2(x.p)} vs home ${f2(x.home)}</td><td style="text-align:right"><b>+${Math.round(x.gain)}</b></td></tr>`;
      h += `<div style="margin-top:8px"><b>Carry out</b> <span class="muted">(our surplus that sells higher there)</span></div>
        ${p.out.length ? `<table class="t">${p.out.map(x => line(x, true)).join('')}</table>` : '<div class="muted">Nothing we hold sells meaningfully higher there.</div>'}
        <div style="margin-top:8px"><b>Bring back</b> <span class="muted">(things we use or buy that are cheaper there)</span></div>
        ${p.back.length ? `<table class="t">${p.back.map(x => line(x, false)).join('')}</table>` : '<div class="muted">Nothing we use is meaningfully cheaper there.</div>'}
        <div class="row" style="margin-top:8px"><div class="grow">Boat running cost (est.)</div><b>−${Math.round(p.cost)}</b></div>
        <div class="row"><div class="grow"><b>Net for the round trip</b></div><b style="color:${p.net >= 0 ? 'var(--mo-good)' : 'var(--mo-bad)'}">${sgn(p.net)}</b></div>
        <div class="muted" style="margin-top:4px">${p.net > 50 ? 'Worth a run.' : p.net > 0 ? 'Marginal: go only if the boat is heading there anyway.' : 'Not worth a trip on its own.'} Prices are standing bids/asks; depth is capped at ~2 turns of their trading, so big loads move the price. Trip cost = ${p.t.d} tiles × ${SEA_DETOUR} sea detour × 2 ways × ~${TRIP_PER_TILE}/tile.</div>`;
      const idle = S.boats.find(t => !(t.producer || {}).recipe);
      if (idle) h += `<div class="row" style="margin-top:6px"><a class="muted" href="/transport/${idle.id}/journey">Send ${esc(idle.name)} → (game journey page)</a></div>`;
    }
    return h + '</div>';
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
      const o = { c, t, theyBuy, fit }; o.sc = scoreContract(o); return o;
    }).sort((a, b) => b.sc.s - a.sc.s);
    const row = ({ c, t, theyBuy, fit, sc }) => {
      const home = num(mkt(t.asset).last_price), price = num(t.price), vol = num(t.initial_volume);
      const edge = home ? (theyBuy ? price - home : home - price) : null;
      const d = c.local || String(c.town_id) === TOWN ? 0 : tdist(c.town_id);
      const aid = (BigInt(c.id) | (BigInt(1) << BigInt(6))).toString();
      return `<div class="card ${sc.cls === 'g' ? 'ok' : sc.cls === 'y' ? 'warn' : 'bad'}">
        <div class="row"><span class="chip ${sc.cls}">${sc.s} ${sc.label}</span><span class="muted">${esc(sc.why)}</span></div>
        <div class="bar"><i style="width:${sc.s}%;background:${sc.cls === 'g' ? '#1f8a4c' : sc.cls === 'y' ? '#c28a00' : '#c0392b'}"></i></div>
        <div class="row" style="margin-top:4px"><div class="grow"><b>${theyBuy ? 'They buy' : 'They sell'} ${f1(vol)} ${esc(t.asset)}</b> @ ${f2(price)}${vol && price ? ` <span class="muted">(${Math.round(vol * price).toLocaleString()} total)</span>` : ''}
          <br><span class="muted">${d === 0 ? 'local, no boat needed' : `${esc(tname(c.town_id))} · ~${d ?? '?'} tiles away (boat)`}${t.timeframe ? ` · ${t.timeframe.length} turns` : ''}${t.penalty ? ` · penalty ${t.penalty}` : ''}</span>
          <br><span class="muted">${fit ? `<b>${theyBuy ? 'we make/hold this' : 'we use this'}</b> · ` : ''}${edge != null ? `vs home ${f2(home)}: <b style="color:${edge >= 0 ? 'var(--mo-good)' : 'var(--mo-bad)'}">${edge >= 0 ? '+' : '−'}${f2(Math.abs(edge))}/unit (${edge >= 0 ? '+' : '−'}${Math.round(Math.abs(edge * vol))})</b>` : 'no home price'}</span></div>
          <a class="b" style="text-decoration:none;display:inline-block;padding:9px 12px;border-radius:6px;font-weight:600" href="/contracts/actions#actionid=${aid}">Accept…</a></div></div>`;
    };
    el.innerHTML = `<h4 style="margin:6px 0">Our contracts</h4>` +
      (mine.length ? mine.map(c => { const t = tx(c); return `<div class="card warn"><b>${t.direction === 'bid' ? 'Selling' : 'Buying'} ${f1(t.initial_volume)} ${esc(t.asset)}</b> @ ${f2(t.price)} <span class="muted">· ${esc(t.stage || c.state)} · ${f1(t.volume)} left</span></div>`; }).join('') : '<p class="muted">None active.</p>') +
      `<h4 style="margin:12px 0 6px">Offers on the board (${offers.length})</h4>` +
      (offers.length ? offers.map(row).join('') : '<p class="muted">No open offers.</p>') +
      `<p class="muted">Score (0-100): margin vs our home price after estimated boat cost, +10 if we make/hold/use it, minus if we can't cover the volume in time or the payment would dip below the ${RESERVE / 1000}k reserve. 75+ great, 55+ ok, 35+ poor, below that skip. Accept… opens the game's own accept screen, where you confirm and pick a carrier.</p><div class="row"><a class="muted" href="/contracts">All contracts →</a></div>`;
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
      .map(([i, h]) => ({ i, sells: (h.managers || []).some(m => num(m.sell_volume)) }));
    const scan = store.get('scan', null);
    const best = (item, sells) => {
      if (!scan) return null; let b = null;
      for (const t of scan.near) { const x = (scan.data[t.id] || {})[item]; if (!x) continue;
        const p = sells ? num(x.highest_bid) || 0 : num(x.lowest_ask) || 0; if (!p) continue;
        if (!b || (sells ? p > b.p : p < b.p)) b = { p, t }; }
      return b;
    };
    const arrow = x => { const l = num(x.last_price), e = num(x.price_ema_60); if (!l || !e) return ''; const r = l / e - 1; return r > 0.03 ? '↑' : r < -0.03 ? '↓' : '→'; };
    const rows = items.sort((a, b) => a.i.localeCompare(b.i)).map(({ i, sells }) => {
      const x = mkt(i), b = best(i, sells), home = sells ? num(x.highest_bid) || num(x.last_price) : num(x.lowest_ask) || num(x.last_price);
      const better = b && home && (sells ? b.p > home * 1.05 : b.p < home * 0.95);
      return `<tr${better ? ' style="background:rgba(31,138,76,.08)"' : ''}><td><b>${esc(i)}</b><br><span class="muted">we ${sells ? 'sell' : 'buy'}</span></td><td>${f2(x.last_price)} ${arrow(x)}<br><span class="muted">avg ${f2(x.price_ema_60)}</span></td><td>${f2(x.highest_bid)} / ${f2(x.lowest_ask)}<br><span class="muted">~${f1(x.volume_ema_60)}/turn</span></td><td>${b ? `${f2(b.p)}<br><span class="muted">${esc(b.t.n)}</span>` : '<span class="muted">–</span>'}${better ? ' <span class="chip g">boat?</span>' : ''}</td></tr>`;
    }).join('');
    el.innerHTML = `<div class="row" style="justify-content:space-between"><span class="muted">${scan ? `Nearby scan ${Math.round((Date.now() - scan.at) / 60000)} min old` : 'No nearby scan yet'}</span><button class="b" data-scan="1">${scan ? 'Rescan' : 'Scan nearby'}</button></div>
      <div class="card" style="padding:4px 6px"><table class="t"><tr class="muted"><td>Item</td><td>Home last</td><td>Bid / ask</td><td>Best nearby</td></tr>${rows}</table></div>
      <p class="muted">↑ ↓ = last price vs the 60-turn average. 'boat?' = a nearby town beats home by 5%+, worth checking a boat run. Best nearby = best bid for what we sell, best ask for what we buy, in the 14 closest towns.</p>
      <h4 style="margin:14px 0 6px">Build watch</h4><div id="mo-bw"><p class="muted">Checking building-material markets…</p></div>`;
    buildWatch().then(bw => { const d = el.querySelector('#mo-bw'); if (d) d.innerHTML = bwHtml(bw); }).catch(e => { const d = el.querySelector('#mo-bw'); if (d) d.textContent = e.message; });
  }
  function bwHtml(bw) {
    return `<div class="card"><table class="t">${bw.res.map(r => `<tr><td><b>${esc(r.item)}</b></td><td>${f1(r.rv)}/turn now vs ${f1(r.bv)} normal</td><td>${f2(r.rp)} vs ${f2(r.bp)}</td><td>${r.hot ? '<span class="chip r">someone building</span>' : '<span class="chip g">normal</span>'}</td></tr>`).join('')}</table>
      <div class="muted" style="margin-top:4px">Other people's trading only: our own buys are taken out. Last 3 turns vs the 24 before. A jump in bricks, nails, tiles or limestone usually means a build is going up in town.</div></div>`;
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
      <div class="card"><b>Profit per building</b> <span class="muted">last turn, at market prices, bought labour at ${f2(priceOf('labour'))}</span>
        <table class="t" style="margin-top:4px">${buildingProfits().map(p => `<tr><td>${esc(p.b.name)} <span class="muted">${f2(p.x)}x</span></td><td class="muted">out ${Math.round(p.out)} · in ${Math.round(p.inn)} · lab ${Math.round(p.lab)}</td><td style="text-align:right;color:${p.net >= 0 ? 'var(--mo-good)' : 'var(--mo-bad)'}"><b>${sgn(p.net)}</b></td></tr>`).join('')}</table>
        <div class="muted" style="margin-top:4px">Chain steps value their output at market price (e.g. thread sold vs used), so a step can look negative while the chain as a whole earns. Our own labour (farmstead) is counted at the market price too.</div></div>
      <p class="muted">Market trades only. Wages for your own labour, land tax and household spending aren't in these numbers.</p>`;
  }

  // ---------------------------------------------------------------- plan
  async function rivalScan() {
    const t = await api('/towns/' + TOWN);
    const st = {};
    for (const v of Object.values(t.domain || {})) {
      if (String(v.owner_id) !== RIVAL || !v.structure) continue;
      const x = st[v.structure.id] || (st[v.structure.id] = { type: v.structure.type, plots: 0, building: (v.structure.tags || []).includes('C') });
      x.plots++;
    }
    return { turn: S.turn, st };
  }
  function rivalHtml() {
    const r = S.rival, seen = store.get('rivalSeen', null);
    if (!r) return '<div class="card muted">Loading rival…</div>';
    const rows = Object.entries(r.st).sort((a, b) => a[1].type.localeCompare(b[1].type)).map(([id, x]) => {
      const was = seen && seen.st[id];
      const tag = !seen ? '' : !was ? '<span class="chip r">NEW</span> ' : was.plots !== x.plots ? `<span class="chip y">${was.plots}→${x.plots} plots</span> ` : was.building && !x.building ? '<span class="chip y">finished</span> ' : '';
      return `<tr><td>${tag}${esc(x.type)}</td><td>${x.plots} plot${x.plots > 1 ? 's' : ''}</td><td class="muted">${x.building ? 'under construction' : ''}</td></tr>`;
    });
    const gone = seen ? Object.entries(seen.st).filter(([id]) => !r.st[id]).map(([id, x]) => `<tr><td><span class="chip g">GONE</span> ${esc(x.type)}</td><td>${x.plots} plots</td><td></td></tr>`) : [];
    return `<div class="card"><b>Rival: Gaud de Noyon</b> <span class="muted">${Object.keys(r.st).length} buildings in Strasclives${seen ? ` · compared with turn ${seen.turn}` : ''}</span>
      <table class="t" style="margin-top:4px">${rows.join('')}${gone.join('')}</table>
      <div class="row" style="margin-top:6px"><button class="b" data-rivalseen="1">Mark seen</button></div>
      <div class="muted" style="margin-top:4px">From the town's land register: what he owns and how big. His production and cash are hidden.</div></div>`;
  }
  function renderPlan(el) {
    const g = gate();
    const toGo = 200 - S.pr.free;
    const p1 = S.buildings.filter(b => b.construction && chainBuilding(b));
    const tools = held('tools');
    const live = {
      p1: p1.length ? `In progress: ${p1.map(b => { const e = buildEta(b); return `${b.name} ${f1(b.construction.progress)}% (${isFinite(e.turns) ? 'done ' + tt(e.turns) : 'stalled'})`; }).join(' · ')}` : 'Done: no chain expansion under construction.',
      gate: g.map(x => `<span class="chip ${x.ok ? 'g' : 'r'}">${x.k} ${x.v} ${x.ok ? '✓' : '✗'} (${x.t})</span>`).join(' '),
      p3: toGo > 0 ? `${f1(S.pr.free)}/200 spendable, +${f1(S.pr.rate)}/turn → Tenants ${S.pr.rate > 0 ? tt(toGo / S.pr.rate) : 'not rising'}` : `<b>${f1(S.pr.free)} spendable: Tenants is affordable (your call).</b>`,
      kill: g.some(x => x.kill) ? `<b style="color:var(--mo-bad)">Tripped now: ${g.filter(x => x.kill).map(x => x.k + ' ' + x.v).join(', ')}</b>` : 'Not tripped.',
      tools: `${f1(tools)} held${tools >= 100 ? ' ✓' : ` (${f1(100 - tools)} to go)`}`,
      boat: (S.boats || []).map(t => `${t.name}: ${(t.producer || {}).recipe || 'idle'}`).join(' · '),
    };
    const pqn = pqNext(), auto = store.get('pqAuto', true), pqd = store.get('pqDone', null);
    let h = `<h4 style="margin:6px 0">Prestige queue</h4><div class="card ${pqn && pqn.free >= pqn.cost ? 'ok' : ''}">
      ${pqn ? `<b>Next: ${esc(pqn.label)}</b> for ${pqn.cost} · ${f1(pqn.free)} free · ${pqn.free >= pqn.cost ? 'affordable now' : 'affordable ' + tt(pqn.eta)}<div class="muted">Then: ${esc(pqn.then)}</div>` : '<span class="muted">Queue empty.</span>'}
      ${pqd ? `<div class="muted" style="margin-top:4px">Last auto-buy: ${esc(pqd.track)} for ${pqd.cost} (${clockText(pqd.at, true)})</div>` : ''}
      <div class="row" style="margin-top:6px"><button class="${auto ? 'a' : 'b'}" data-pqauto="1">Auto-buy: ${auto ? 'ON' : 'OFF'}</button></div>
      <div class="muted" style="margin-top:4px">Agreed buys happen automatically the moment they're affordable, while Ops is open on any device (it also checks in the background every 10 min while the game tab is open). Tenants + farmstead always come first.</div></div>
      <h4 style="margin:14px 0 6px">The plan</h4>` + PLAN.map(x => `<div class="card ${x.k === 'kill' && g.some(y => y.kill) ? 'bad' : x.k === 'gate' ? (g.every(y => y.ok) ? 'ok' : 'warn') : ''}"><b>${esc(x.t)}</b><div class="muted">${esc(x.d)}</div>${live[x.k] ? `<div style="margin-top:3px">${live[x.k]}</div>` : ''}</div>`).join('');
    // next automatic actions
    const nx = chainNext();
    h += '<h4 style="margin:14px 0 6px">Next automatic actions</h4>' + (nx.length ? nx.map(x => `<div class="card"><b>When ${esc(x.b.name)} lands</b> <span class="muted">(${isFinite(x.eta.turns) ? tt(x.eta.turns) : 'stalled'})</span>
        <div class="muted">Chain balancer sets ${Object.keys(CHAIN).filter(k => Math.abs(x.c.plan[k] - x.c.cur[k]) >= 0.02).map(k => `${k} ${f2(x.c.cur[k])}→${f2(x.c.plan[k])}x`).join(', ') || 'no change'} · garments ${f1(x.c.gNow)}→${f1(x.c.gNew)}/turn · labour ${x.c.dLab >= 0 ? '+' : ''}${Math.round(x.c.dLab)}/turn</div></div>`).join('')
      : '<p class="muted">No chain expansion pending, so the balancer has nothing queued.</p>');
    h += '<p class="muted">Each step assumes the earlier ones have landed. Figures use today\'s thread use and stock.</p>';
    // Phase 2 gate on real sell-through (12 turns)
    h += '<h4 style="margin:14px 0 6px">Garment sell-through (Phase 2 gate)</h4><div class="card" id="mo-st"><span class="muted">Loading…</span></div>';
    h += '<h4 style="margin:14px 0 6px">Build watch</h4><div id="mo-bw2"><p class="muted">Checking…</p></div>';
    h += '<h4 style="margin:14px 0 6px">Recorded game actions</h4>' + recHtml();
    // running now
    h += '<h4 style="margin:14px 0 6px">Running now (GitHub, hourly)</h4>' + AUTOMATION.map(([t, d]) => `<div class="card"><b>${esc(t)}</b><div class="muted">${esc(d)}</div></div>`).join('') +
      '<p class="muted">The repo is private, so the panel can\'t read its logs. The change log below is what it can see from the game side.</p>';
    // change log
    const log = store.get('autolog', []);
    h += '<h4 style="margin:14px 0 6px">Changed outside this panel</h4>' + (log.length ? `<div class="card">${log.slice(0, 12).map(l => `<div><span class="muted">${clockText(l.at, true)} · turn ${l.turn}</span><br>${esc(l.ch.join(' · '))}</div>`).join('<hr style="border:0;border-top:1px solid #ddd3bb;margin:5px 0">')}
      <div class="row" style="margin-top:6px"><button class="b" data-clearlog="1">Clear log</button></div></div>` : '<p class="muted">Nothing yet. From now on, order or production changes made by the bot, the balancer or the game page get listed here (seen on this device each time the panel loads).</p>');
    // timeline
    const up = upcoming();
    h += '<h4 style="margin:14px 0 6px">Timeline</h4>' + (up.length ? `<div class="card">${up.map(u => `<div>${u.lvl === 'soon' ? '<b>Soon</b> · ' : ''}${esc(u.text)}</div>`).join('')}</div>` : '<p class="muted">Nothing scheduled.</p>');
    // rival
    h += '<h4 style="margin:14px 0 6px">Rival watch</h4>' + rivalHtml();
    el.innerHTML = h;
    loadHist().then(() => {
      const d = el.querySelector('#mo-st'); if (!d) return;
      const T = HIST.turns.slice(-12), st = HIST.st.slice(-12).map(x => (((x || {}).flows || {}).garments) || {});
      const made = st.reduce((a, f) => a + num(f.production), 0), sold = st.reduce((a, f) => a + num(f.sale), 0), used = st.reduce((a, f) => a + num(f.consumption), 0);
      const ratio = made - used > 0 ? sold / (made - used) : 0, price = num(mkt('garments').last_price);
      const ok = ratio >= 0.9 && price >= GATE.garments;
      d.className = 'card ' + (ok ? 'ok' : 'warn');
      d.innerHTML = `Last ${T.length} turns: made ${Math.round(made)}, sold ${Math.round(sold)} (${Math.round(ratio * 100)}% of what we didn't wear), price now ${f2(price)}. <b>${ok ? 'Passing: the extra garments are selling.' : 'Not yet: wait for sales to keep up at ≥ ' + GATE.garments + '.'}</b>`;
    }).catch(() => { });
    buildWatch().then(bw => { const d = el.querySelector('#mo-bw2'); if (d) d.innerHTML = bwHtml(bw); }).catch(() => { });
    if (!S.rival || S.rival.turn !== S.turn) rivalScan().then(r => { S.rival = r; if (!store.get('rivalSeen', null)) store.set('rivalSeen', r); if (tab === 'plan') render(); }).catch(() => { });
  }

  // ---------------------------------------------------------------- emergency (self-sufficient mode)
  // One button: stop every market buy, run only what our own labour and our stockpiles can carry,
  // keep selling, and keep the household fed so sustenance prestige doesn't drop. Undo puts it all back.
  const RESERVE_TURNS = 24;   // household reserve (Taylor: 24 turns)
  const STOCK_TURNS = 12;     // emergency: spread input stock over this many turns
  const KEEP_BUYING = new Set(['donations']);        // luxury slot: 40/turn buys +1 prestige/turn
  const PERISHABLE = new Set(['fish', 'meat']);      // go off every turn, can't be stockpiled
  function hhUseMap() { const m = {}; for (const x of household()) m[x.i] = x.hu; return m; }

  // standing reserve: sell keeps / buy stop-ats high enough that household goods last RESERVE_TURNS
  function reservePlan() {
    const use = hhUseMap(), out = [];
    for (const [item, u] of Object.entries(use)) {
      if (PERISHABLE.has(item) || KEEP_BUYING.has(item) || !(u > 0)) continue;
      const need = Math.ceil(u * RESERVE_TURNS);
      const ms = (S.holdings[item] || {}).managers || [];
      ms.forEach((m, i) => {
        if (num(m.sell_volume) && num(m.min_holding) < need) out.push({ item, i, ch: { min_holding: need }, text: `${item}: sell keep ${f1(m.min_holding)} → ${need}` });
        if (num(m.buy_volume) && m.max_holding != null && num(m.max_holding) < need) out.push({ item, i, ch: { max_holding: need }, text: `${item}: buy stop-at ${f1(m.max_holding)} → ${need}` });
      });
      if (held(item) < need) out.push({ item, info: true, text: `${item}: ${f1(held(item))} held, ${need} needed for ${RESERVE_TURNS} turns (${f1(u)}/turn)` });
    }
    return out;
  }

  function emergencyPlan() {
    const use = hhUseMap();
    const ownLab = num(flowsOf('labour').production);
    const boatLab = (S.boats || []).reduce((a, t) => { const p = t.producer || {}; return a + (p.recipe ? labourPer1x(p.recipe) * num(p.target) : 0); }, 0);
    let labLeft = ownLab - boatLab;
    // 1. orders: every buy off (except prestige luxuries and the household's perishables), keeps raised to the reserve
    const orders = [];
    for (const [item, h] of Object.entries(S.holdings)) {
      if (SKIP_ITEMS.has(item)) continue;
      const ms = (h.managers || []).map(clean);
      if (!ms.length) continue;
      let changed = false; const notes = [];
      const need = use[item] && !PERISHABLE.has(item) ? Math.ceil(use[item] * RESERVE_TURNS) : 0;
      const nm = ms.map(m => {
        const o = { ...m };
        if (num(o.buy_volume)) {
          if (KEEP_BUYING.has(item)) notes.push('buy kept (prestige)');
          else if (PERISHABLE.has(item) && use[item]) {
            const v = Math.max(0, Math.ceil(use[item] - num(flowsOf(item).production)));
            if (v !== num(o.buy_volume)) { changed = true; notes.push(v ? `buy ${v}/turn (household only; it can't be stored)` : 'buy off (we make enough)'); }
            else notes.push('household buy kept');
            if (v) o.buy_volume = v; else { delete o.buy_volume; delete o.buy_price; delete o.max_holding; }
          } else { delete o.buy_volume; delete o.buy_price; delete o.max_holding; changed = true; notes.push('buy off'); }
        }
        if (num(o.sell_volume) && need && num(o.min_holding) < need) { o.min_holding = need; changed = true; notes.push(`sell keep ${need}`); }
        return o;
      }).filter(o => num(o.buy_volume) || num(o.sell_volume));
      if (changed) orders.push({ item, managers: nm, text: `${item}: ${[...new Set(notes)].join(', ')}` });
    }
    // 2. production: fit the running buildings to our own labour and to inputs we hold or make
    const cands = S.buildings.filter(b => b.type !== 'warehouse' && b.producer && b.producer.recipe).map(b => {
      const r = recipeByName(b.producer.recipe); if (!r) return null;
      if (r.out.labour) return null;                                    // the farmstead makes our labour; never touched
      const lab = num(r.in.labour);
      const val = Object.entries(r.out).reduce((a, [p, x]) => a + x * priceOf(p), 0)
        - Object.entries(r.in).filter(([p]) => p !== 'labour').reduce((a, [p, x]) => a + x * priceOf(p), 0);
      const hhOut = Object.keys(r.out).find(p => use[p] && !KEEP_BUYING.has(p));
      const prio = b.type === 'park' ? 0 : hhOut ? 1 : 2;
      return { b, r, lab, val, prio, hhOut, cur: num(b.producer.target) };
    }).filter(Boolean);
    // the textile chain moves as one unit: scaling it together keeps each step fed by the one before
    const chainIds = new Set(Object.values(CHAIN).map(x => x.id));
    const members = cands.filter(c => chainIds.has(String(c.b.id)) && c.cur > 0);
    if (members.length > 1) {
      const agg = { in: {}, out: {} };
      for (const m of members) {
        for (const [p, x] of Object.entries(m.r.in)) agg.in[p] = (agg.in[p] || 0) + x * m.cur;
        for (const [p, x] of Object.entries(m.r.out)) agg.out[p] = (agg.out[p] || 0) + x * m.cur;
      }
      for (const p of Object.keys(agg.out)) if (agg.in[p]) { const n = agg.out[p] - agg.in[p]; if (n >= 0) { agg.out[p] = n; delete agg.in[p]; } else { agg.in[p] = -n; delete agg.out[p]; } }
      const hhOut = Object.keys(agg.out).find(p => use[p] && !KEEP_BUYING.has(p));
      const chain = { b: { name: 'textile chain', id: 'chain' }, members, r: agg, lab: num(agg.in.labour), prio: hhOut ? 1 : 2, hhOut, cur: 1 };
      cands.splice(0, cands.length, ...cands.filter(c => !members.includes(c)), chain);
    }
    // only count output we can use: sold by a sell order, eaten by the household, or fed to another running building
    // (e.g. timber with the builds paused and no sell order is just a pile, so the logging camp doesn't get labour)
    const fed = new Set(cands.flatMap(c => Object.keys(c.r.in)));
    // a sell order only counts if its floor is near the market (timber held back at 8.50 vs 7.60 won't sell)
    const sells = p => ((S.holdings[p] || {}).managers || []).some(m => num(m.sell_volume) && (m.markup_price || !priceOf(p) || num(m.sell_price) <= priceOf(p) * 1.05));
    for (const c of cands) {
      const useful = Object.keys(c.r.out).filter(p => sells(p) || use[p] || fed.has(p));
      c.useless = c.prio === 2 && !useful.length;
      c.val = Object.entries(c.r.out).filter(([p]) => useful.includes(p)).reduce((a, [p, x]) => a + x * priceOf(p), 0)
        - Object.entries(c.r.in).filter(([p]) => p !== 'labour').reduce((a, [p, x]) => a + x * priceOf(p), 0);
    }
    // what an input can supply per turn: our stock spread over the reserve window + what the plan makes of it
    const capOf = (c, made) => {
      let cap = c.cur, lim = null;
      for (const [p, x] of Object.entries(c.r.in)) {
        if (p === 'labour' || !(x > 0)) continue;
        const avail = held(p) / STOCK_TURNS + (made[p] || 0);
        if (avail / x < cap) { cap = avail / x; lim = p; }
      }
      return { cap: Math.max(0, cap), lim };
    };
    const allocate = made => {
      let left = labLeft; const alloc = new Map();
      const order = [...cands].sort((a, b) => a.prio - b.prio || (b.val / Math.max(1, b.lab)) - (a.val / Math.max(1, a.lab)));
      for (const c of order) {
        const { cap, lim } = capOf(c, made);
        let want = cap;
        if (c.prio === 1) want = Math.min(want, use[c.hhOut] * 1.5 / c.r.out[c.hhOut]);  // household first; surplus later
        if (c.prio === 2 && c.val <= 0) want = 0;
        const t = c.lab ? Math.max(0, Math.min(want, left / c.lab)) : want;
        alloc.set(c, { t, lim, dry: cap < 0.02, noLab: t < 0.02 && want >= 0.02 }); left -= t * c.lab;
      }
      for (const c of order.filter(c => c.prio === 1 && c.val > 0)) {             // spare labour: household makers can sell the rest
        const { cap } = capOf(c, made), a = alloc.get(c);
        const extra = c.lab ? Math.max(0, Math.min(cap - a.t, left / c.lab)) : 0;
        if (extra > 0.01) { a.t += extra; left -= extra * c.lab; }
      }
      return { alloc, left };
    };
    const madeBy = alloc => { const m = {}; for (const [c, a] of alloc) for (const [p, x] of Object.entries(c.r.out)) m[p] = (m[p] || 0) + x * a.t; return m; };
    const now = {}; for (const [p, f] of Object.entries(S.flows)) now[p] = num(f.production);
    let res = allocate(now);
    for (let k = 0; k < 3; k++) res = allocate(madeBy(res.alloc));               // settle the chain on the plan's own output
    const prod = [];
    for (const [c, a] of res.alloc) {
      if (c.members) {        // spread the chain's scale over its buildings
        const f = a.t;
        for (const m of c.members) {
          const to = Math.floor(m.cur * f * 100) / 100;
          if (to < 0.02) prod.push({ b: m.b, from: m.cur, to: 0, stop: true, text: `${m.b.name}: stop (textile chain ${a.noLab ? 'gets no labour' : 'runs out of ' + (a.lim || 'input')})` });
          else if (Math.abs(to - m.cur) >= 0.01) prod.push({ b: m.b, from: m.cur, to, text: `${m.b.name}: ${f2(m.cur)}x → ${f2(to)}x (textile chain at ${Math.round(f * 100)}%${a.lim && f < 0.999 ? ', limited by ' + a.lim : ''})` });
        }
        continue;
      }
      const to = Math.floor(a.t * 100) / 100;
      const why = c.prio === 0 ? 'prestige' : c.prio === 1 ? `household ${c.hhOut}` : `+${f2(c.val / Math.max(1, c.lab))}/labour`;
      if (to < 0.02) prod.push({ b: c.b, from: c.cur, to: 0, stop: true, text: `${c.b.name}: stop (${c.useless ? 'nothing uses or sells its output' : a.noLab ? 'no labour left' : a.dry && a.lim ? 'no ' + a.lim + ' without buying' : c.val <= 0 ? 'loses money at market prices' : 'no labour left'})` });
      else if (Math.abs(to - c.cur) >= 0.01) prod.push({ b: c.b, from: c.cur, to, text: `${c.b.name}: ${f2(c.cur)}x → ${f2(to)}x (${why}${a.lim ? ', limited by ' + a.lim : ''})` });
    }
    // 3. construction draws labour and timber too: pause it
    const cons = S.buildings.filter(b => b.construction && num((b.construction.settings || {}).pace) > 0)
      .map(b => ({ b, settings: b.construction.settings, text: `${b.name} ${b.construction.stage === 'EXPANSION' ? 'expansion' : 'build'}: pause (pace ${b.construction.settings.pace} → 0)` }));
    // projection: what emergency mode earns and costs per turn, and what it does to prestige
    const madeP = madeBy(res.alloc), usedP = {};
    for (const [c, a] of res.alloc) for (const [p, x] of Object.entries(c.r.in)) usedP[p] = (usedP[p] || 0) + x * a.t;
    let sales = 0;
    for (const [p, q] of Object.entries(madeP)) { if (p === 'labour' || !sells(p)) continue; const spare = q - (use[p] || 0) - (usedP[p] || 0); if (spare > 0) sales += spare * priceOf(p); }
    let keptBuys = 0;
    for (const [item, h] of Object.entries(S.holdings)) for (const m of (h.managers || [])) if (num(m.buy_volume)) {
      if (KEEP_BUYING.has(item)) keptBuys += num(m.buy_volume) * num(m.buy_price);
      else if (PERISHABLE.has(item) && use[item]) keptBuys += Math.max(0, Math.ceil(use[item] - num(flowsOf(item).production))) * num(m.buy_price);
    }
    const parkE = [...res.alloc].find(([c]) => c.b.type === 'park');
    const parkLoss = parkE ? 0.5 * Math.max(0, parkE[0].cur - parkE[1].t) : 0;
    const proj = { sales, keptBuys, prestigeDelta: -parkLoss };
    return { ownLab, boatLab, labLeft: res.left, orders, prod, cons, proj };
  }

  async function goEmergency(plan) {
    const snap = { at: Date.now(), turn: S.turn, orders: {}, prod: {}, cons: {} };
    for (const o of plan.orders) snap.orders[o.item] = ((S.holdings[o.item] || {}).managers || []).map(clean);
    for (const p of plan.prod) snap.prod[p.b.id] = { recipe: p.b.producer.recipe, target: num(p.b.producer.target) };
    for (const c of plan.cons) snap.cons[c.b.id] = c.settings;
    const prev = store.get('emergency', null);
    if (prev) { // already in emergency: keep the ORIGINAL settings for undo
      for (const k of ['orders', 'prod', 'cons']) snap[k] = { ...snap[k], ...prev[k] };
      snap.at = prev.at; snap.turn = prev.turn;
    }
    store.set('emergency', snap);
    const errs = [];
    for (const o of plan.orders) { try { await patchItem(o.item, o.managers); } catch (e) { errs.push(o.item + ': ' + e.message); } }
    for (const p of plan.prod) { try { if (p.stop) await stopBuilding(p.b); else await setTarget(p.b, p.to); } catch (e) { errs.push(p.b.name + ': ' + e.message); } }
    for (const c of plan.cons) { try { await api('/buildings/' + c.b.id + '/construction/settings', 'PUT', { ...c.settings, pace: 0 }); } catch (e) { errs.push(c.b.name + ' build: ' + e.message); } }
    if (errs.length) throw new Error(errs.length + ' step(s) failed: ' + errs.slice(0, 3).join('; '));
  }
  async function undoEmergency() {
    const snap = store.get('emergency', null);
    if (!snap) return false;
    const errs = [];
    for (const [item, ms] of Object.entries(snap.orders)) { try { await patchItem(item, ms); } catch (e) { errs.push(item + ': ' + e.message); } }
    for (const [id, p] of Object.entries(snap.prod)) {
      const b = S.buildings.find(x => String(x.id) === String(id)); if (!b) continue;
      try { if (b.producer && b.producer.recipe) await setTarget(b, p.target); else await startWith(b, p.recipe, p.target); } catch (e) { errs.push(b.name + ': ' + e.message); }
    }
    for (const [id, st] of Object.entries(snap.cons)) { try { await api('/buildings/' + id + '/construction/settings', 'PUT', st); } catch (e) { errs.push('build ' + id + ': ' + e.message); } }
    if (errs.length) throw new Error(errs.length + ' step(s) failed (emergency snapshot kept, try Undo again): ' + errs.slice(0, 3).join('; '));
    store.set('emergency', null);
  }
  // taxes per turn, from the business account statement (average of the last 10 turns)
  async function loadTax() {
    if (S.tax && S.tax.turn === S.turn) return S.tax;
    const biz = await api('/businesses/' + BUSINESS);
    const st = await api('/accounts/' + biz.account_id + '/assets/money/statement');
    const tx = st.transactions || [];
    const last = Math.max(0, ...tx.map(t => num(t.timestamp)));
    const recent = tx.filter(t => num(t.timestamp) > last - 10);
    const turns = Math.max(1, new Set(recent.map(t => t.timestamp)).size);
    const tax = -recent.filter(t => /tax/i.test(t.description || '')).reduce((a, t) => a + num(t.amount), 0) / turns;
    S.tax = { turn: S.turn, tax };
    return S.tax;
  }

  function renderSos(el) {
    const snap = store.get('emergency', null);
    const p = emergencyPlan(), rp = reservePlan();
    const tax = S.tax ? S.tax.tax : null;
    const hh = household();
    const lines = a => a.length ? a.map(x => `<div>• ${esc(x.text)}</div>`).join('') : '<div class="muted">nothing to change</div>';
    let h = snap ? `<div class="card bad"><b>EMERGENCY MODE is on</b> <span class="muted">since turn ${snap.turn}</span>
        <div class="muted">Buys are off and production runs on our own labour. Undo puts back every order, target and build pace saved when it started.</div>
        <div class="row" style="margin-top:6px"><button class="a" data-sosundo="1">Undo emergency</button><button class="b" data-sosgo="1">Re-apply</button></div></div>` : '';
    h += `<div class="card ${snap ? '' : 'warn'}"><b>Emergency: live on what we have</b>
      <div class="muted">For when cash runs low and production crashes. Stops every market buy, fits production to our own ${f1(p.ownLab)} labour and our stockpiles, keeps selling surplus, pauses builds, and keeps the household fed so sustenance prestige holds. Everything is saved first; Undo restores it.</div>
      <div style="margin-top:6px">Cash <b>${Math.round(S.cash).toLocaleString()}</b>${tax != null ? ` · taxes ~<b>${Math.round(tax)}</b>/turn → covers <b>${tax > 0 ? Math.floor(S.cash / tax) : '∞'}</b> turns with no income` : ' · taxes: loading…'}</div>
      <div class="muted">Own labour ${f1(p.ownLab)}${p.boatLab ? ` · boats ${f1(p.boatLab)}` : ''} · left unused after the plan ${f1(p.labLeft)}</div>
      ${tax != null ? (() => { const nowP = S.m.profit - tax, emP = p.proj.sales - p.proj.keptBuys - tax, nowR = S.pr.rate, emR = S.pr.rate + p.proj.prestigeDelta;
        return `<table class="t" style="margin-top:6px"><tr class="muted"><td></td><td>Now</td><td>Emergency</td></tr>
          <tr><td>Profit / turn</td><td>${sgn(nowP)}</td><td style="color:${emP >= 0 ? 'var(--mo-good)' : 'var(--mo-bad)'}"><b>${sgn(emP)}</b></td></tr>
          <tr><td>Prestige / turn</td><td>${nowR >= 0 ? '+' : ''}${f2(nowR)}</td><td><b>${emR >= 0 ? '+' : ''}${f2(emR)}</b></td></tr></table>
          <div class="muted">Emergency profit = what the plan makes and sells at today's prices (~${Math.round(p.proj.sales)}) − kept buys (donations, household meat/fish ~${Math.round(p.proj.keptBuys)}) − taxes (~${Math.round(tax)}). Now = last turn's trading profit − taxes. Prestige assumes the household stays fed (reserve below); a stopped park costs 0.5/turn. Stock already held sells down on top of this.</div>`; })() : ''}
      ${!snap ? `<div class="row" style="margin-top:8px"><button class="r" data-sosgo="1" style="font-size:15px;padding:10px 16px">Go to emergency mode</button></div>` : ''}</div>`;
    h += `<div class="card"><b>What it would change</b>
      <div style="margin-top:4px"><b>Orders</b></div>${lines(p.orders)}
      <div style="margin-top:6px"><b>Production</b></div>${lines(p.prod)}
      <div style="margin-top:6px"><b>Builds</b></div>${lines(p.cons)}
      <div class="muted" style="margin-top:6px">Kept on purpose: the farmstead (our labour), boats fishing (household fish), donations (prestige), and a household-only buy for goods that spoil (${[...PERISHABLE].join(', ')}). Inputs are spread over ${STOCK_TURNS} turns of stock plus what the plan itself makes.</div></div>`;
    h += `<h4 style="margin:14px 0 6px">${RESERVE_TURNS}-turn household reserve</h4>
      <div class="card ${rp.some(x => !x.info) ? 'warn' : 'ok'}">
      <table class="t">${hh.map(x => { const need = PERISHABLE.has(x.i) || KEEP_BUYING.has(x.i) ? null : Math.ceil(x.hu * RESERVE_TURNS);
        return `<tr><td><b>${esc(x.i)}</b></td><td>${f1(x.have)} held</td><td>${f1(x.hu)}/turn</td><td>${need == null ? '<span class="muted">' + (KEEP_BUYING.has(x.i) ? 'bought (prestige)' : 'spoils, can\'t store') + '</span>' : x.have >= need ? `<span style="color:var(--mo-good)">${Math.floor(x.have / x.hu)} turns ✓</span>` : `<span style="color:#d68910">${Math.floor(x.have / x.hu)} of ${RESERVE_TURNS} turns</span>`}</td></tr>`; }).join('')}</table>
      ${rp.filter(x => !x.info).length ? `<div style="margin-top:6px">${lines(rp.filter(x => !x.info))}</div><div class="row" style="margin-top:6px"><button class="a" data-sosreserve="1">Set ${RESERVE_TURNS}-turn keeps</button></div>` : `<div class="muted" style="margin-top:6px">Sell keeps already protect ${RESERVE_TURNS} turns of household use.</div>`}
      </div>`;
    el.innerHTML = h;
    if (!S.tax || S.tax.turn !== S.turn) loadTax().then(() => { if (tab === 'sos') render(); }).catch(() => { S.tax = { turn: S.turn, tax: null }; });
  }

  // ---------------------------------------------------------------- charts: history + projections
  let HIST = null;
  const PROJ = 24;           // turns to project ahead
  const FIT = 24;            // turns used for the trend
  async function loadHist() {
    if (HIST && HIST.turn === S.turn) return HIST;
    const [biz, hh, st] = await Promise.all([
      api('/businesses/' + BUSINESS + '/history'),
      api('/households/' + HOUSEHOLD + '/history').catch(() => []),
      api('/buildings/' + STORE + '/storage/history').catch(() => []),
    ]);
    const bh = (biz && biz.history) || [];
    const turns = bh.map(x => num(x.turn));
    // the household and storehouse histories carry no turn numbers; they end on the same turn as the business one
    const align = arr => { const a = Array.isArray(arr) ? arr : []; const off = turns.length - a.length; return turns.map((t, i) => a[i - off]); };
    HIST = { turn: S.turn, turns, biz: bh, hh: align(hh), st: align(st), mk: {} };
    return HIST;
  }
  async function marketHist(item) {
    if (HIST.mk[item]) return HIST.mk[item];
    const r = await api('/towns/' + TOWN + '/markets/' + encodeURIComponent(item) + '/history').catch(() => ({}));
    HIST.mk[item] = (r.history || []).map(x => ({ t: num(x.turn), p: num(x.avg) || num(x.last), v: num(x.vol) }));
    return HIST.mk[item];
  }
  function trend(pts) {           // least squares over the last FIT points -> {slope, at(t)}
    const q = pts.filter(p => isFinite(p[1])).slice(-FIT);
    if (q.length < 3) return null;
    const n = q.length, mx = q.reduce((a, p) => a + p[0], 0) / n, my = q.reduce((a, p) => a + p[1], 0) / n;
    let sxy = 0, sxx = 0; for (const [x, y] of q) { sxy += (x - mx) * (y - my); sxx += (x - mx) * (x - mx); }
    const slope = sxx ? sxy / sxx : 0;
    return { slope, at: t => my + slope * (t - mx) };
  }
  // small SVG line chart; series: [{name, color, pts:[[turn, value]], proj:true}]
  function lineChart(series, { h = 150, fmt = x => f1(x), hline = null, zero = false } = {}) {
    const W = 360, L = 46, R = 8, T = 8, B = 20;
    const now = S.turn;
    series.forEach(s => { if (s.proj) { const tr = trend(s.pts); if (tr && s.pts.length) { const lt = s.pts[s.pts.length - 1][0]; s.tr = tr; s.pp = [[lt, s.pts[s.pts.length - 1][1]], [lt + PROJ, tr.at(lt + PROJ)]]; } } });
    const xs = series.flatMap(s => s.pts.concat(s.pp || []).map(p => p[0]));
    const ys = series.flatMap(s => s.pts.concat(s.pp || []).map(p => p[1])).filter(isFinite).concat(hline ? [hline.v] : []).concat(zero ? [0] : []);
    if (!xs.length || !ys.length) return '<div class="muted">No history yet.</div>';
    const x0 = Math.min(...xs), x1 = Math.max(...xs, now + (series.some(s => s.pp) ? PROJ : 0));
    let y0 = Math.min(...ys), y1 = Math.max(...ys); if (y1 === y0) { y1 += 1; y0 -= 1; }
    const pad = (y1 - y0) * 0.08; y0 -= pad; y1 += pad;
    const X = t => L + (t - x0) / ((x1 - x0) || 1) * (W - L - R), Y = v => T + (1 - (v - y0) / (y1 - y0)) * (h - T - B);
    const path = pts => pts.filter(p => isFinite(p[1])).map((p, i) => (i ? 'L' : 'M') + X(p[0]).toFixed(1) + ' ' + Y(p[1]).toFixed(1)).join(' ');
    let g = '';
    for (let k = 0; k <= 3; k++) { const v = y0 + (y1 - y0) * k / 3; g += `<line x1="${L}" x2="${W - R}" y1="${Y(v)}" y2="${Y(v)}" stroke="currentColor" stroke-opacity=".12"/><text x="${L - 4}" y="${Y(v) + 3}" text-anchor="end" font-size="9" fill="currentColor" fill-opacity=".6">${esc(fmt(v))}</text>`; }
    const nowX = X(now);
    g += `<line x1="${nowX}" x2="${nowX}" y1="${T}" y2="${h - B}" stroke="currentColor" stroke-opacity=".3" stroke-dasharray="2 3"/>`;
    g += `<text x="${X(x0)}" y="${h - 6}" font-size="9" fill="currentColor" fill-opacity=".6">${x0 - now} turns</text><text x="${nowX}" y="${h - 6}" font-size="9" text-anchor="middle" fill="currentColor" fill-opacity=".6">now</text>`;
    if (x1 > now + 2) g += `<text x="${W - R}" y="${h - 6}" font-size="9" text-anchor="end" fill="currentColor" fill-opacity=".6">+${x1 - now}</text>`;
    if (hline) g += `<line x1="${L}" x2="${W - R}" y1="${Y(hline.v)}" y2="${Y(hline.v)}" stroke="${hline.color || '#c0392b'}" stroke-dasharray="4 3"/><text x="${L + 3}" y="${Y(hline.v) - 3}" font-size="9" fill="${hline.color || '#c0392b'}">${esc(hline.label)}</text>`;
    for (const s of series) {
      g += `<path d="${path(s.pts)}" fill="none" stroke="${s.color}" stroke-width="1.8" stroke-linejoin="round"/>`;
      if (s.pp) g += `<path d="${path(s.pp)}" fill="none" stroke="${s.color}" stroke-width="1.6" stroke-dasharray="4 3" opacity=".8"/>`;
    }
    const legend = series.length > 1 ? `<div class="muted" style="display:flex;gap:10px;flex-wrap:wrap">${series.map(s => `<span><span style="display:inline-block;width:10px;height:3px;background:${s.color};vertical-align:middle"></span> ${esc(s.name)}</span>`).join('')}</div>` : '';
    return `<svg viewBox="0 0 ${W} ${h}" style="width:100%;height:auto;display:block" role="img" aria-label="${esc(series.map(s => s.name).join(', '))}">${g}</svg>${legend}`;
  }
  const C = { a: '#2f7d4f', b: '#3b6fb0', c: '#c28a00', d: '#b0413e', e: '#7a5cb0' };
  const whenTurn = t => t - S.turn > 0 ? tt(t - S.turn) : 'already';

  function renderCharts(el) {
    if (!HIST || HIST.turn !== S.turn) {
      el.innerHTML = '<p class="muted">Loading the last 90 turns of history…</p>';
      loadHist().then(() => { if (tab === 'charts') render(); }).catch(e => { el.innerHTML = `<p class="muted">History failed to load: ${esc(e.message)}</p>`; });
      return;
    }
    const Hh = HIST, T = Hh.turns;
    const cash = T.map((t, i) => [t, num(Hh.biz[i].funds)]);
    const worth = T.map((t, i) => [t, num(Hh.biz[i].funds) + num(Hh.biz[i].inventory_cost) + num(Hh.biz[i].buildings_cost) + num(Hh.biz[i].transports_cost)]);
    const pres = T.map((t, i) => [t, Hh.hh[i] ? num(Hh.hh[i].prestige) : NaN]);
    const alloc = num(((S.hh || {}).prestige_board || {}).allocated);
    const profit = T.map((t, i) => { const fl = (Hh.st[i] || {}).flows || {}; let s = 0, b = 0; for (const f of Object.values(fl)) { s += num(f.sale_value); b += num(f.purchase_cost); } return [t, s - b]; });
    const ma = profit.map((p, i) => { const w = profit.slice(Math.max(0, i - 11), i + 1); return [p[0], w.reduce((a, x) => a + x[1], 0) / w.length]; });
    const trC = trend(cash), trW = trend(worth), trP = trend(pres);
    const tenantsAt = alloc + 200;
    const pNow = num(S.hh && S.hh.prestige);
    const tenEta = pNow >= tenantsAt ? 'now' : trP && trP.slope > 0 ? tt((tenantsAt - pNow) / trP.slope) : 'not rising';
    const k = x => Math.round(x).toLocaleString();
    let h = `<div class="kpi">
      <div>Cash trend <b>${trC ? sgn(trC.slope) : '?'}</b>/turn → <b>${trC ? k(S.cash + trC.slope * PROJ) : '?'}</b> in ${PROJ} turns</div>
      <div>Net worth <b>${k(worth[worth.length - 1] ? worth[worth.length - 1][1] : 0)}</b> · ${trW ? sgn(trW.slope) : '?'}/turn</div>
      <div>Prestige ${trP ? '+' + f2(trP.slope) : '?'}/turn · Tenants (200 free) <b>${tenEta}</b></div></div>
      <div class="muted">Solid = last ${T.length} turns from the game's own history · dashed = trend of the last ${FIT} turns carried ${PROJ} turns ahead.</div>`;
    h += `<div class="card"><b>Cash</b> <span class="muted">(builds and stock buys show up here)</span>${lineChart([{ name: 'cash', color: C.a, pts: cash, proj: true }], { fmt: v => Math.round(v / 100) / 10 + 'k' })}</div>`;
    h += `<div class="card"><b>Net worth</b> <span class="muted">cash + stock + buildings + boats, at cost</span>${lineChart([{ name: 'net worth', color: C.b, pts: worth, proj: true }], { fmt: v => Math.round(v / 1000) + 'k' })}</div>`;
    h += `<div class="card"><b>Prestige</b>${lineChart([{ name: 'prestige', color: C.e, pts: pres, proj: true }], { hline: { v: tenantsAt, label: 'Tenants (200 free)', color: '#c28a00' } })}</div>`;
    h += `<div class="card"><b>Trading profit per turn</b> <span class="muted">market sales − purchases (construction buys included)</span>${lineChart([{ name: 'per turn', color: C.c, pts: profit }, { name: '12-turn average', color: C.d, pts: ma }], { zero: true, fmt: v => Math.round(v) })}</div>`;
    // item picker
    const items = Object.keys(S.holdings).filter(i => !SKIP_ITEMS.has(i) && i !== 'labour' && ((S.holdings[i].managers || []).length || Object.keys(flowsOf(i)).length)).sort();
    const sel = store.get('chartItem', items.includes('garments') ? 'garments' : items[0]);
    h += `<div class="card"><div class="row"><b class="grow">Item</b><select data-chartitem="1">${items.map(i => `<option ${i === sel ? 'selected' : ''}>${esc(i)}</option>`).join('')}</select></div><div id="mo-itemchart"><div class="muted">Loading…</div></div></div>`;
    el.innerHTML = h;
    itemChart(sel).then(x => { const d = el.querySelector('#mo-itemchart'); if (d) d.innerHTML = x; }).catch(e => { const d = el.querySelector('#mo-itemchart'); if (d) d.innerHTML = `<div class="muted">${esc(e.message)}</div>`; });
  }
  async function itemChart(item) {
    const Hh = HIST, T = Hh.turns;
    const bal = x => x == null ? NaN : typeof x === 'object' ? num(x.balance) : num(x);
    const stock = T.map((t, i) => [t, bal(((Hh.st[i] || {}).assets || {})[item])]).filter(p => isFinite(p[1]));
    const fl = k => T.map((t, i) => [t, num((((Hh.st[i] || {}).flows || {})[item] || {})[k])]);
    const made = fl('production'), sold = fl('sale'), used = fl('consumption'), bought = fl('purchase');
    const mh = await marketHist(item);
    const price = mh.filter(x => x.t >= T[0]).map(x => [x.t, x.p]), vol = mh.filter(x => x.t >= T[0]).map(x => [x.t, x.v]);
    const tr = trend(stock);
    const have = held(item);
    let eta = '';
    if (tr && tr.slope < -0.05) eta = `stock falling ${f1(-tr.slope)}/turn → empty ${tt(have / -tr.slope)}`;
    else if (tr && tr.slope > 0.05) eta = `stock rising ${f1(tr.slope)}/turn`;
    else if (tr) eta = 'stock steady';
    const tp = trend(price);
    const any = a => a.some(p => p[1]);
    let h = `<div class="muted" style="margin:4px 0">${f1(have)} held · ${eta}${tp && price.length ? ` · price trend ${tp.slope >= 0 ? '+' : ''}${f2(tp.slope * 10)}/10 turns` : ''}</div>`;
    h += `<div style="margin-top:4px"><b>Stock</b></div>` + lineChart([{ name: 'held', color: C.b, pts: stock, proj: true }]);
    const fs = [['made', made, C.a], ['used', used, C.d], ['sold', sold, C.c], ['bought', bought, C.e]].filter(x => any(x[1])).map(([n, p, c]) => ({ name: n, color: c, pts: p }));
    if (fs.length) h += `<div style="margin-top:8px"><b>Per turn</b></div>` + lineChart(fs, { zero: true });
    if (price.length > 1) h += `<div style="margin-top:8px"><b>Home market price</b> <span class="muted">(turn average)</span></div>` + lineChart([{ name: 'price', color: C.a, pts: price, proj: true }], { fmt: v => f2(v) })
      + `<div style="margin-top:8px"><b>Traded in town per turn</b></div>` + lineChart([{ name: 'volume', color: C.c, pts: vol }], { zero: true, fmt: v => Math.round(v) });
    return h;
  }

  // ================================================================ v1.8
  // ---------------------------------------------------------------- request recorder
  // Records the game's own write requests (method, path, body) so new one-tap actions can copy them
  // exactly instead of guessing. Kept on this device only, last 25. No headers or cookies are stored.
  (function hookFetch() {
    if (window.__mercRec) return; window.__mercRec = true;
    const orig = window.fetch.bind(window);
    window.fetch = function (input, init) {
      try {
        const url = typeof input === 'string' ? input : (input && input.url) || '';
        const method = ((init && init.method) || (input && input.method) || 'GET').toUpperCase();
        if (method !== 'GET' && /\/api\//.test(url)) {
          const log = store.get('reqlog', []);
          log.unshift({ at: Date.now(), method, path: url.replace(/^https?:\/\/[^/]+/, ''), body: init && typeof init.body === 'string' ? init.body.slice(0, 2000) : null });
          store.set('reqlog', log.slice(0, 25));
        }
      } catch (e) { }
      return orig(input, init);
    };
    const XO = XMLHttpRequest.prototype.open, XS = XMLHttpRequest.prototype.send;
    XMLHttpRequest.prototype.open = function (m, u) { this.__mo = { m: String(m).toUpperCase(), u: String(u) }; return XO.apply(this, arguments); };
    XMLHttpRequest.prototype.send = function (body) {
      try {
        const x = this.__mo;
        if (x && x.m !== 'GET' && /\/api\//.test(x.u)) {
          const log = store.get('reqlog', []);
          log.unshift({ at: Date.now(), method: x.m, path: x.u.replace(/^https?:\/\/[^/]+/, ''), body: typeof body === 'string' ? body.slice(0, 2000) : null });
          store.set('reqlog', log.slice(0, 25));
        }
      } catch (e) { }
      return XS.apply(this, arguments);
    };
  })();

  // ---------------------------------------------------------------- prestige queue (auto-buy)
  // Taylor, Sep 26: agreed prestige buys happen automatically once affordable. Tenants (+ farmstead) never waits.
  const PQUEUE = [
    { track: 'tenants', repeat: true, label: 'Tenants (+5)', then: 'Expand the farmstead +5 plots (+50 own labour)' },
  ];
  // Tenants cost 50 per level above 2 (level 6 = 200, 7 = 250, 8 = 300: matches the game's own dialog)
  function trackCost(track, pb) {
    if (track === 'tenants') return 50 * (num(pb.tenants_level) - 2);
    return null;
  }
  function pqNext() {
    const pb = (S.hh && S.hh.prestige_board) || {};
    const q = PQUEUE[0]; if (!q) return null;
    const cost = trackCost(q.track, pb);
    return cost ? { ...q, cost, free: S.pr.free, eta: S.pr.rate > 0 ? Math.max(0, (cost - S.pr.free) / S.pr.rate) : Infinity } : null;
  }
  async function prestigeAuto() {
    if (!store.get('pqAuto', true) || !S || !S.hh || !S.hh.prestige_board) return null;
    const n = pqNext(); if (!n || n.free < n.cost) return null;
    const last = store.get('pqLast', null); if (last && last.turn === S.turn) return null;   // one try per turn
    store.set('pqLast', { turn: S.turn });
    await api('/households/' + HOUSEHOLD + '/prestige/allocate', 'POST', { track: n.track, cost: String(n.cost) });
    const done = { at: Date.now(), turn: S.turn, track: n.track, cost: n.cost, then: n.then };
    store.set('pqDone', done);
    toast(`Prestige: bought ${n.label} for ${n.cost}. Next: ${n.then}`, 8000);
    return done;
  }

  // ---------------------------------------------------------------- dismiss (clear) for issues / upcoming
  const cardKey = (kind, it) => kind + ':' + (it.item || '') + '|' + String(it.text || '').replace(/[\d.,:~+\-−]+/g, '#').slice(0, 70);
  const LVL = { later: 0, soon: 1, warn: 1, bad: 2, stuck: 2 };
  function isHidden(kind, it) {
    const d = store.get('dismiss', {}), x = d[cardKey(kind, it)];
    if (!x) return false;
    if (S.turn > x.until) return false;
    if ((LVL[it.lvl] || 0) > (LVL[x.lvl] || 0)) return false;          // got worse: show again
    return true;
  }
  function dismissCards(kind, list) {
    const d = store.get('dismiss', {});
    for (const k of Object.keys(d)) if (d[k].until < S.turn) delete d[k];
    for (const it of list) d[cardKey(kind, it)] = { until: S.turn + 12, lvl: it.lvl };
    store.set('dismiss', d);
  }
  const visibleIssues = () => (S.issues || []).map((it, i) => ({ it, i })).filter(x => !isHidden('i', x.it));

  // ---------------------------------------------------------------- inputs in use (guards 'drop buy' fixes)
  // porterage lesson (Sep 26): never drop a buy for something a running building, a build or the household uses
  function inputsInUse() {
    const s = new Set(['labour', 'donations']);
    for (const b of S.buildings || []) {
      const r = b.producer && b.producer.recipe && recipeByName(b.producer.recipe);
      if (r) Object.keys(r.in).forEach(p => s.add(p));
      const c = b.construction; if (c && c.inventory) Object.keys(((c.inventory.account || {}).assets) || {}).forEach(p => s.add(p));
    }
    for (const t of S.boats || []) { const r = t.producer && t.producer.recipe && recipeByName(t.producer.recipe); if (r) Object.keys(r.in).forEach(p => s.add(p)); }
    try { household().forEach(x => s.add(x.i)); } catch (e) { }
    return s;
  }
  async function dropSide(item, side) {
    const keys = side === 'buy' ? ['buy_volume', 'buy_price', 'max_holding'] : ['sell_volume', 'sell_price', 'min_holding'];
    const ms = ((S.holdings[item] || {}).managers || []).map(clean).map(m => { const o = { ...m }; keys.forEach(k => delete o[k]); return o; })
      .filter(m => num(m.buy_volume) || num(m.sell_volume));
    await patchItem(item, ms);
  }
  const CHAIN_ITEMS = ['flax plants', 'flax fibres', 'thread', 'cloth'];
  // extra issues v1.8: selling what the chain is short of; buying what nothing uses
  function extraIssues(S) {
    const out = [];
    for (const item of CHAIN_ITEMS) {
      const f = flowsOf(item), ms = (S.holdings[item] || {}).managers || [];
      if (num(f.shortfall) > 0 && ms.some(m => num(m.sell_volume)))
        out.push({ lvl: 'bad', item, text: `${item}: ${f1(f.shortfall)} short last turn while a sell order is on`,
          fixes: [{ safe: true, h: 'Drops the sell order: the chain needs all of it', label: 'Stop selling', run: () => dropSide(item, 'sell') }] });
    }
    if (S.rec && S.rec.r && S.rec.r.length) {
      const inUse = inputsInUse();
      for (const [item, h] of Object.entries(S.holdings)) {
        if (SKIP_ITEMS.has(item) || inUse.has(item)) continue;
        const ms = h.managers || [], f = flowsOf(item);
        if (!ms.some(m => num(m.buy_volume))) continue;
        if (num(f.consumption) > 0) continue;
        if (!(num(f.expiration) > 0 || held(item) >= Math.max(...ms.map(m => num(m.max_holding) || 0)))) continue;
        out.push({ lvl: 'warn', item, text: `${item}: we buy it but nothing uses it${num(f.expiration) ? ` (${f1(f.expiration)} went off)` : ''}`,
          fixes: [{ safe: true, h: 'Drops the buy order (no running building, build or the household uses it)', label: 'Stop buying', run: () => dropSide(item, 'buy') }] });
      }
    }
    return out;
  }

  // ---------------------------------------------------------------- profit per building (last turn, market prices)
  function buildingProfits() {
    const lp = priceOf('labour');
    return (S.buildings || []).filter(b => b.producer && b.producer.recipe).map(b => {
      const r = recipeByName(b.producer.recipe); if (!r) return null;
      const x = num((b.producer.previous_operation || {}).production);
      const out = Object.entries(r.out).reduce((a, [p, q]) => a + q * priceOf(p), 0) * x;
      const inn = Object.entries(r.in).filter(([p]) => p !== 'labour').reduce((a, [p, q]) => a + q * priceOf(p), 0) * x;
      const lab = num(r.in.labour) * x * lp;
      return { b, x, out, inn, lab, net: out - inn - lab };
    }).filter(Boolean).sort((a, b) => a.net - b.net);
  }

  // ---------------------------------------------------------------- build watch (someone is building)
  const BUILD_MATS = ['bricks', 'nails', 'tiles', 'limestone', 'timber', 'labour'];
  let BW = null;
  async function buildWatch() {
    if (BW && BW.turn === S.turn) return BW;
    await loadHist();
    const ours = item => { const m = {}; HIST.turns.forEach((t, i) => { m[t] = num((((HIST.st[i] || {}).flows || {})[item] || {}).purchase); }); return m; };
    const res = [];
    for (const item of BUILD_MATS) {
      const mh = await marketHist(item); if (mh.length < 10) continue;
      const o = ours(item);
      const other = mh.map(x => ({ t: x.t, v: Math.max(0, x.v - (o[x.t] || 0)), p: x.p }));
      const base = other.slice(-27, -3), recent = other.slice(-3);
      if (!base.length || !recent.length) continue;
      const bv = base.reduce((a, x) => a + x.v, 0) / base.length, rv = recent.reduce((a, x) => a + x.v, 0) / recent.length;
      const bp = base.reduce((a, x) => a + x.p, 0) / base.length, rp = recent.reduce((a, x) => a + x.p, 0) / recent.length;
      const k = item === 'labour' ? 1.15 : item === 'timber' ? 1.5 : 2.5;
      const hot = rv > Math.max(3, bv * k);
      res.push({ item, bv, rv, bp, rp, hot });
    }
    BW = { turn: S.turn, res };
    return BW;
  }

  // ---------------------------------------------------------------- wall of shame (money lost)
  async function shameData(turns = 24) {
    await loadHist();
    const T = HIST.turns.slice(-turns), st = HIST.st.slice(-turns);
    const per = {};   // key -> { what, item, value, qty }
    const add = (what, item, qty, value) => { if (!(value > 0.01)) return; const k = what + '|' + item; const x = per[k] || (per[k] = { what, item, qty: 0, value: 0 }); x.qty += qty; x.value += value; };
    st.forEach(s => {
      const fl = (s || {}).flows || {};
      for (const [item, f] of Object.entries(fl)) {
        const unit = num(f.purchase) ? num(f.purchase_cost) / num(f.purchase) : num(f.production) ? num(f.production_cost) / num(f.production) : priceOf(item);
        if (num(f.expiration)) add(item === 'labour' ? 'expired labour' : 'spoiled / expired', item, num(f.expiration), num(f.expiration) * unit);
        if (num(f.shortfall)) add('shortfall (lost production)', item, num(f.shortfall), num(f.shortfall) * priceOf(item));
      }
    });
    // right now: stock above keep sitting idle while there is a bid; sell orders priced above the best bid
    const now = [];
    for (const [item, h] of Object.entries(S.holdings)) {
      if (SKIP_ITEMS.has(item) || item === 'labour') continue;
      const ms = h.managers || [], f = flowsOf(item), bid = num(mkt(item).highest_bid);
      const sells = ms.filter(m => num(m.sell_volume));
      if (sells.length && bid) {
        const floor = Math.min(...sells.map(m => num(m.sell_price))), keep = Math.max(0, ...sells.map(m => num(m.min_holding)));
        const unsold = sells.reduce((a, m) => a + num(m.sell_volume), 0) - num(f.sale);
        if (unsold > 1 && floor > bid && held(item) > keep) now.push({ item, text: `${item}: floor ${f2(floor)} above best bid ${f2(bid)}, ${f1(unsold)} of the order didn't sell`, value: unsold * bid });
      }
    }
    const rows = Object.values(per).sort((a, b) => b.value - a.value);
    const total = rows.reduce((a, x) => a + x.value, 0);
    return { turns: T.length, rows, total, now };
  }
  function renderShame(el) {
    if (!HIST || HIST.turn !== S.turn) { el.innerHTML = '<p class="muted">Loading history…</p>'; shameData().then(() => { if (tab === 'shame') render(); }).catch(e => { el.innerHTML = `<p class="muted">${esc(e.message)}</p>`; }); return; }
    shameData().then(d => {
      if (tab !== 'shame') return;
      const k = x => Math.round(x).toLocaleString();
      let h = `<div class="card bad"><b>Wall of shame</b> <span class="muted">money lost in the last ${d.turns} turns</span>
        <div style="font-size:20px;margin-top:4px"><b>${k(d.total)}</b> <span class="muted" style="font-size:13px">≈ ${k(d.total / Math.max(1, d.turns))}/turn</span></div></div>`;
      h += d.rows.length ? `<div class="card"><table class="t">${d.rows.slice(0, 15).map(r => `<tr><td><b>${esc(r.item)}</b><br><span class="muted">${esc(r.what)}</span></td><td>${f1(r.qty)}</td><td style="text-align:right"><b>${k(r.value)}</b></td><td><button class="b" data-stock="${esc(r.item)}">Fix</button></td></tr>`).join('')}</table>
        <div class="muted" style="margin-top:4px">Expired and spoiled are valued at what we paid (or what it cost to make); shortfalls at market price as a stand-in for the output they cost.</div></div>` : '<div class="card ok">Nothing lost in this window.</div>';
      h += `<h4 style="margin:12px 0 6px">Right now</h4>` + (d.now.length ? d.now.map(x => `<div class="card warn">${esc(x.text)} <span class="muted">(~${k(x.value)} at the bid)</span><div class="row" style="margin-top:6px"><button class="b" data-stock="${esc(x.item)}">Orders</button></div></div>`).join('') : '<p class="muted">No stock stuck above the market.</p>');
      el.innerHTML = h; wire();
    });
  }

  // ---------------------------------------------------------------- recorded actions (Plan tab)
  function recHtml() {
    const log = store.get('reqlog', []);
    if (!log.length) return '<p class="muted">Nothing recorded yet. Game actions you take (build, expand, buy plots, prestige) are recorded here so Ops can learn to do them in one tap.</p>';
    return `<div class="card"><table class="t">${log.slice(0, 10).map(l => `<tr><td class="muted">${clockText(l.at, true)}</td><td><b>${esc(l.method)}</b> ${esc(l.path)}<br><span class="muted" style="word-break:break-all">${esc((l.body || '').slice(0, 300))}</span></td></tr>`).join('')}</table>
      <div class="row" style="margin-top:6px"><button class="b" data-copyrec="1">Copy all</button><button class="b" data-clearrec="1">Clear</button></div></div>`;
  }

  // ---------------------------------------------------------------- events
  function wire() {
    panel.onchange = ev => {
      const t = ev.target;
      if (t.matches && t.matches('select[data-trip]')) { store.set('tripTown', t.value); render(); }
      if (t.matches && t.matches('select[data-chartitem]')) { store.set('chartItem', t.value); render(); }
    };
    panel.onclick = async ev => {
      if (ev.target.closest('a')) return;
      const t = ev.target.closest('button'); if (!t) return;
      const d = t.dataset;
      if (d.x === 'close') { panel.classList.remove('open'); return; }
      if (d.x === 'refresh') return load();
      if (d.x === 'sos') { tab = 'sos'; store.set('tab', tab); return render(); }
      if (d.more) { store.set('moreOpen', !store.get('moreOpen', false)); return render(); }
      if (d.dismiss) { const [kind, idx] = d.dismiss.split(':'); const it = kind === 'i' ? S.issues[+idx] : upcoming()[+idx]; if (it) dismissCards(kind, [it]); badge(); return render(); }
      if (d.clearall) { if (d.clearall === 'i') dismissCards('i', visibleIssues().map(x => x.it)); else dismissCards('u', upcoming().filter(u => !isHidden('u', u))); badge(); return render(); }
      if (d.unclear) { const m = store.get('dismiss', {}); for (const k of Object.keys(m)) if (k.startsWith(d.unclear + ':')) delete m[k]; store.set('dismiss', m); badge(); return render(); }
      if (d.fixsafe) {
        const list = visibleIssues().map(x => ({ it: x.it, f: x.it.fixes.find(f => f.safe) })).filter(x => x.f);
        if (!confirm('Fix all safe:\n' + list.map(x => '• ' + x.it.text + ' → ' + x.f.label).join('\n'))) return;
        return act(async () => { const errs = []; for (const x of list) { try { await x.f.run(); } catch (e) { errs.push(x.it.item + ': ' + e.message); } } if (errs.length) throw new Error(errs.join('; ')); }, list.length + ' safe fixes applied');
      }
      if (d.pqauto) { store.set('pqAuto', !store.get('pqAuto', true)); return render(); }
      if (d.clearnotes) { return act(() => api('/notifications', 'DELETE'), 'game notices cleared'); }
      if (d.copyrec) { const t = JSON.stringify(store.get('reqlog', []), null, 1); try { await navigator.clipboard.writeText(t); toast('Copied ' + t.length + ' chars'); } catch (e) { prompt('Copy this:', t); } return; }
      if (d.clearrec) { store.set('reqlog', []); return render(); }
      if (d.sosgo) {
        const p = emergencyPlan();
        const msg = `EMERGENCY MODE\n\n${p.orders.length} order change(s): every buy off except donations and household perishables\n${p.prod.length} production change(s), ${p.cons.length} build(s) paused\n\nEverything is saved first; Undo emergency restores it. Go?`;
        if (!confirm(msg)) return;
        tab = 'sos'; store.set('tab', tab);
        return act(() => goEmergency(p), 'emergency mode on');
      }
      if (d.sosundo) { if (!confirm('Undo emergency mode?\nPuts back every saved order, production target and build pace.')) return; return act(() => undoEmergency(), 'emergency undone, settings restored'); }
      if (d.sosreserve) {
        const rp = reservePlan().filter(x => !x.info);
        if (!confirm('Set ' + RESERVE_TURNS + '-turn household keeps?\n' + rp.map(x => x.text).join('\n'))) return;
        return act(async () => { for (const x of rp) await setTier(x.item, x.i, x.ch); }, RESERVE_TURNS + '-turn keeps set');
      }
      if (d.x === 'help') { store.set('explain', !store.get('explain', false)); return render(); }
      if (d.needdone || d.needlater) { const m = store.get('needsDone', {}); if (d.needdone) m[d.needdone] = 'done'; else m[d.needlater] = S.turn + 12; store.set('needsDone', m); return render(); }
      if (d.needgo) {
        const [k, ...rest] = d.needgo.split(':'); const v = rest.join(':');
        if (k === 'link') { panel.classList.remove('open'); location.href = v; return; }
        if (k === 'trip') { store.set('tripTown', v); tab = 'boat'; store.set('tab', tab); return render(); }
        if (k === 'tab') { tab = v; store.set('tab', tab); return render(); }
      }
      if (d.opt) { store.set('optItem', store.get('optItem', null) === d.opt ? null : d.opt); return render(); }
      if (d.optrun) {
        const [item, k] = d.optrun.split('|'); const o = options(item).out[+k]; if (!o) return;
        if (o.kind === 'import') return o.run();
        if (o.lab && !labourOk(o.lab)) return;
        if (!confirm(`${o.title}\n${o.detail}\n\nDo it?`)) return;
        store.set('optItem', null);
        return act(o.run, o.title);
      }
      if (d.seen) { markSeen(); return render(); }
      if (d.rivalseen) { if (S.rival) store.set('rivalSeen', S.rival); return render(); }
      if (d.clearlog) { if (!confirm('Clear the change log on this device?')) return; store.set('autolog', []); return render(); }
      if (d.tab) { tab = d.tab; store.set('tab', tab); return render(); }
      if (d.fix) { const [i, j] = d.fix.split(':').map(Number); const f = S.issues[i].fixes[j]; if (f.lab && !labourOk(f.lab)) return; return act(f.run, f.label); }
      if (d.stock) { tab = 'orders'; store.set('openItem', d.stock); return render(); }
      if (d.open) { const [id, page] = d.open.split(':'); const b = S.buildings.find(x => x.id == id); panel.classList.remove('open'); return go(b, page); }
      if (d.t) {
        const [id, op] = d.t.split(':'); const b = S.buildings.find(x => x.id == id);
        const max = num(b.size) || 1, cur = num(b.producer.target), step = Math.max(0.1, +(max * 0.1).toFixed(2));
        let nt = op === 'max' ? max : op === '+' ? Math.min(max, cur + step) : Math.max(step, cur - step);
        nt = +nt.toFixed(2);
        if (nt === cur) return toast('Already at ' + (op === '-' ? 'minimum step' : 'max'));
        if (nt > cur && !labourOk((nt - cur) * labourPer1x(b.producer.recipe))) return;
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
        if (c.dLab > 0 && !labourOk(c.dLab)) return;
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
      const [biz, sh, clk, hh] = await Promise.all([api('/businesses/' + BUSINESS), api('/buildings/' + STORE), api('/clock').catch(() => ({})), api('/households/' + HOUSEHOLD).catch(() => null)]);
      const inv = (sh.storage || {}).inventory || {};
      const ids = (biz.building_ids || []).filter(id => id !== STORE);
      const blds = await Promise.all(ids.map(id => api('/buildings/' + id).catch(() => null)));
      S = Object.assign(S || {}, { cash: num(inv.account?.assets?.money?.balance), assets: inv.account?.assets || {}, flows: inv.previous_flows || {},
        holdings: inv.holdings || {}, buildings: blds.filter(Boolean), market: (S && S.market) || {} });
      S.turn = num(clk.turn); S.m = money(S.flows, S.cash, S.turn);
      if (hh) { S.hh = hh; S.pr = prestigeInfo(hh); }
      S.issues = findIssues(S); badge();
      if (hh) prestigeAuto().catch(() => { });
    } catch (e) { /* ignore */ } finally { busy = false; }
  }
  let lastTurn = null;
  setInterval(async () => {
    try {
      const c = await api('/clock');
      if (lastTurn != null && c.turn !== lastTurn) { noteTurn(num(c.turn), true); if (!panel.classList.contains('open')) setTimeout(quietCheck, 90e3); }
      lastTurn = c.turn;
    } catch (e) { }
  }, 120e3);
  setTimeout(quietCheck, 3000);
  setInterval(quietCheck, 600000);
})();
