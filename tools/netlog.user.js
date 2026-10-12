// ==UserScript==
// @name         Merc netlog
// @namespace    merc
// @version      1.0
// @description  Records the game's write calls (POST/PUT/PATCH/DELETE: method, path, body, status) so one real action (e.g. placing a building) can be read. Never records headers, tokens, or /player and /auth calls.
// @match        https://play.mercatorio.io/*
// @run-at       document-start
// @grant        none
// ==/UserScript==
(function () {
  "use strict";
  const LOG = [], MAX = 60;
  const skip = /\/player\b|\/auth\b|\/keys\b/i;
  let btn = null;
  function badge() { if (btn) btn.textContent = "netlog (" + LOG.length + ")"; }
  function rec(method, url, body, status) {
    method = String(method || "GET").toUpperCase();
    url = String(url || "");
    if (method === "GET" || skip.test(url)) return;
    let b = "";
    try { b = typeof body === "string" ? body : ""; } catch (e) {}
    LOG.push({ t: new Date().toISOString().slice(11, 19), m: method, u: url.replace(location.origin, ""), b: b.slice(0, 1500), s: status });
    if (LOG.length > MAX) LOG.shift();
    badge();
  }
  const of = window.fetch;
  window.fetch = function (input, init) {
    const method = (init && init.method) || (input && input.method) || "GET";
    const url = typeof input === "string" ? input : (input && input.url);
    const body = init && init.body;
    return of.apply(this, arguments).then(
      (r) => { rec(method, url, body, r.status); return r; },
      (e) => { rec(method, url, body, "ERR"); throw e; });
  };
  const xo = XMLHttpRequest.prototype.open, xs = XMLHttpRequest.prototype.send;
  XMLHttpRequest.prototype.open = function (m, u) { this.__m = m; this.__u = u; return xo.apply(this, arguments); };
  XMLHttpRequest.prototype.send = function (body) {
    this.addEventListener("loadend", () => rec(this.__m, this.__u, body, this.status));
    return xs.apply(this, arguments);
  };
  function mount() {
    if (btn || !document.body) return;
    btn = document.createElement("button");
    btn.style.cssText = "position:fixed;left:8px;bottom:8px;z-index:99999;padding:6px 10px;font:12px sans-serif;opacity:.85";
    btn.onclick = () => {
      const text = JSON.stringify(LOG, null, 1);
      (navigator.clipboard ? navigator.clipboard.writeText(text) : Promise.reject()).then(
        () => alert("Copied " + LOG.length + " write calls. Paste them to Claude."),
        () => { window.prompt("Copy this:", text); });
    };
    document.body.appendChild(btn);
    badge();
  }
  document.addEventListener("DOMContentLoaded", mount);
  setInterval(mount, 2000);
})();
