# Bot v2

Built beside v1 and tested in **shadow mode**: every hour it reads the live game, plans every order from the
game's own recipes, and writes what it *would* do. It never writes to the game while `mode` is `shadow`
(`api.write()` refuses unless `allow_writes()` is called, and nothing in v2 calls it; `test_v2.py` checks that).
v1 keeps running the season.

| File | What it is |
| --- | --- |
| `config.json` | every rule in one place: ceilings, floors, runways, perishables, never-drop inputs, stockpiles, builds, agreed prestige buys |
| `api.py` | the one API client: retries, never exits the process, read-only unless writes are allowed |
| `snapshot.py` | one full read per turn (cash, household, every building's recipe/rate/limit/construction, store items with orders and flows, ships, home market) |
| `planner.py` | one model of the business: demand from recipes x rates, supply, per-item orders, ranked flags (risk / waste / tune). Stalled buildings are grouped by root cause (one flag, knock-ons folded in) and don't count as running demand |
| `builds.py` | build manager: remaining materials of every site under construction; buys only the storable shortfall once (the order stops itself at `max_holding`), meters labour per turn once the rest is covered |
| `goals.py`, `goals.json` | goal queue: `keep N` / `cap N` (`export` is recognised, not supported yet) turned into orders inside the safety rules. **Not** `state/order_queue.json`: that file is v1's and is applied to the live game |
| `prestige.py` | every coin -> prestige sink ranked by coin per prestige at today's prices (unowned sites carry build cost spread over the turns left), and the status of the agreed permanent purchases |
| `diagnose.py` | self-diagnosis, run inside `act.py` (config `diagnose.on`): R1 prestige slot dry (+ prestige rate under its 12-turn median), R2 own producer blocked by "<item> space", R3 finished building idle, R4 priority building projected 0 for labour, R5 buy not filling. Detects, proposes, applies within caps (reduce-only at failsafe > 0 or 23:00-07:00 Toronto), logs `"diagnose"` lines in `state/v2/act.jsonl`, writes `state/v2/diagnose.json` (phone alerts) and the report's "Self-diagnosis" section |
| `shadow.py` | runs it and writes `state/v2/` (snapshot, plan, report.md, history.jsonl) |
| `test_v2.py`, `fixtures/` | `python v2/test_v2.py`: plain asserts on a frozen snapshot; includes the read-only guard |
| `data/` | recipes and buildings extracted from the game code (`python tools/extract_gamedata.py` after a game update) |

Offline: `python v2/shadow.py --from FILE [--out DIR]` replans a saved snapshot. A replay never appends to
`history.jsonl`; use `--out` to keep it away from `state/v2/` (the hourly job commits that folder).

Roadmap: (1) shadow + daily v1-vs-v2 diff [done] -> (2) build manager, goal queue, prestige spending by coin per
prestige [built, shadow] -> (3) hand jobs over one at a time in November (pricing, chain sizing, prestige,
contracts) -> (4) Season 9: v2 only.

## What to check as live runs accumulate

- **Flags that persist are real.** `history.jsonl` lines carry every flag as `severity:item`; a flag in every run is a
  finding, one that appears once is noise. The Oct 11 review cut 19 flags to 4 this way (see the commit message).
- **Build progress model.** `builds.py` assumes a site draws materials in proportion to progress
  (`remaining = full cost x (1 - progress/100)`). `history.jsonl` logs each site's `progress`; compare it with the stock
  actually drawn per turn. If they disagree, fix `scan_sites`.
- **Price-only buy orders** (arms, tar, timber: a price but no volume) are treated as standing buys. If the game reads
  them differently, change `standing` in `planner.py`.
- **Tier unlocks** for a cheaper banquet/sermon are not checked by `prestige.py`: a cheaper tier it shows at a site we
  own is a candidate to look at, not an order. Church contracts (best known rate, 16-38 coin per prestige) are not in
  the snapshot and not ranked.
