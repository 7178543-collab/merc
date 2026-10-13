# v2 notes (running; newest learnings at the bottom of each section)

Season 8 is the testbed for season 9. Anything proven here goes into v2. Keep entries short and factual.

## Ships: how travel really works (Oct 12, from the game's own client code + live tests)
- Route a ship: `POST /transports/{id}/travel` with `{location: {x, y}, path: [{x, y, c}, ...], end_town_id}`.
  Ships must NOT send `use_ferry`: the server answers "ferry-path must start on land" (that flag is the land-cart branch).
- The server does no pathfinding. The browser runs A* (8 directions, step cost 1 / 1.414) and sends the whole tile path.
  `tools/seapath.py` does the same; it reproduces the Flax Wyrm's stored Blanans path exactly (244 tiles, cost 297.234).
- Navigable tile = `area` id even and > 0 (odd = land). Tile `type` (0 land, 1 river, 2 lake, 3 sea) is NOT the rule:
  Rouhomme's dock is a river-mouth tile (type 1) inside sea area 2.
- Dock tile = the town's `navigation_zones` keys with an even zone number, nearest to the town location.
  Key = x * 100000 + y. (Home: 152302387 -> (1523, 2387), zone 2.)
- Map data: `GET /map/section/position/X:Y`, X and Y multiples of 32, **gzip-compressed**. Returns
  `{map_size, section_corner, section_size, plots[1024]}`, row-major `plots[(y - cy) * 32 + (x - cx)]`,
  each plot `{alt, area, type?, region?, fertility?, forest?}`. 1,024 sections (1024 x 1024 tiles) pull in ~40 s
  with 6 parallel fetches and compress to ~3 KB per 512 x 512 grid (`state/seamap/*.json.gz`).
- Crew: `PUT /transports/{id}/operation {operation_target}` applies at the turn tick; a ship at 0 does not move.
  A paused ship keeps its position and costs nothing.
- Saved journeys exist (`/businesses/{id}/journeys`, `POST /transports/{id}` action `savejourney`); the list is empty here.
  Not needed now that paths can be computed.
- Test log: Oct 12 ~17:32 Toronto, Linen Snake sent home -> Grandgues (150 tiles, cost 152.7), crew 0.5. Server accepted (200).
  Arrived: docked at Grandgues by the next turn (150 tiles in one turn at crew 0.5). Level shows 0 after arrival.

## Queue and workflow constraints
- `order-queue` job: **5 minute timeout**, shares the `merc-actor` concurrency group with the bot. Long jobs block the bot.
  Keep each queue run short (parallel fetch, small bboxes: seamap max 600 x 600 per entry).
- Pattern for anything that moves things in the game: dry run by default, real send only with `"confirm": true`
  (donate, contract approval, travel). Every write is re-read and logged ok/failed in `state/order_queue_done.jsonl`.
- Read-only dumps (`{"dump": path}`) are the way to learn the API without a token or a browser; they now gunzip.
- IDs written in the handoff doc can be wrong (Linen Snake was listed as 1059744193; real id 1948883264). Read the id
  from `state/dump/api/transports_*.json` or the status file, never from prose.
- Claude can push to the repo via the GitHub app. One shallow clone, push to main, end commits with the session trailer.

## Phone app
- Ship card now has "Send to town" (Plan route = dry run, Send = crew + travel with confirm). The town list is
  baked in for the towns inside the sea grid; widen it when the grid grows.
- Service worker cache name must change with each app release (`merc-shell-vN`), or installed copies keep the old UI.

## Still open (v2 candidates)
- **Building placement: SOLVED (Oct 12)**.
  * New building: `POST /buildings {type, owner_id: "39992", town_id: "152202387", location: "1522:2388", sublocation: {x, y},
    construction: {stage: "INITIAL"}}` (ids are strings). Queue entry `{"build": {...}}`, dry run unless `"confirm": true`.
  * **A park plot is NOT a new building: it is an EXPANSION of the existing park.**
    `PATCH /buildings/{id} {construction: {stage: "EXPANSION", domain: ["1522.6:2388.2"]}}`; domain tiles are strings `cx.sx:cy.sy`.
    Rules the game states: tile within `range` (8) sub-tiles of the building (8 sub-tiles per map tile), must own the land
    ("domain conflict: must own the land"), materials scale per plot (260 labour, 60 limestone, 40 timber, 12 turns).
    Queue entry `{"expand": {"building": id, "count": 1 | "tiles": [...]}, "confirm": true}`: reads the live town, skips
    structures and the fixed roads (grid column 4, row 3), prefers tiles we own then nearest, claims unowned land first, tries
    candidates nearest-first (a bad tile is refused harmlessly), verifies the building then shows an expansion.
  * **Buying a centre tile (CORRECTED Oct 13)**: a centre sub-tile nobody owns is a *property* the town sells (ask 24 by
    default), so `POST /towns/{id}/expand {claims: [], properties: [{location: "1522.3:2388.5"}]}`. It is ours at once (the
    expansion started in the same run). `claims` are for unowned *map* land outside the centres (domain growth, with a landing
    route). My Oct 12 "claims" of centre tiles returned 200 and did nothing (the tile stayed owner 0 after the tick; the money
    "reserved" in the reply was the normal order reserve, 1,570 before any claim). Source: the game client's town-expand
    dialog (`L('/towns/{id}', 'expand', {claims, properties: ue.map(e => ({location: v(xH(e.id))})), landing})`).
  * **Construction pace**: a new construction starts at `settings.pace = 0` and receives nothing, so it never progresses.
    `PUT /buildings/{id}/construction/settings {..., pace: 100}` (client slider: 0/25/50/100; per-turn delivery =
    ceil(capacity * pace / (100 * total_time)) from the provider storehouse). Queue `{"pace": {...}}`; `expand` now sets 100.
  * **Park plot 11 placed with no click, Oct 13 00:15 UTC** (turn 13239): queue `{"plot": {"building": park}, "confirm": true}`
    bought 1522.3:2388.5 and started the expansion; pace set to 100 at 00:18. prestige_rules `AUTO_PLOT = True`: the park
    rule now places the next plot itself when pool room + limestone 60 + timber 40 are there and no plot is building.
  * Town centre data: `GET /towns/{id}` `domain` holds one entry per sub-tile, key = centre * 1,000,000 + sx * 1000 + sy, value
    `{owner_id, structure?, ask_price?}`. No entry or an ask-price-only entry = unowned land. Centres are in `center_ids`; the
    main centre (town location) has reserved plaza/hall tiles, so skip it.
  * Mistake to avoid: my first `expand` "claimed" the tile of every candidate it tried. Buy only the tile you will use
    (`plot` does exactly one).
- **Deferred steps** (`{"later": {"after": ISO time, "entry": {...}}}`): parked in `state/deferred.json`, run on the first
  workflow run at or after that time (hourly at :20, or any queue push), same guards, logged with source `deferred`.
  Tested offline with a stubbed module (no network, no credentials). Use for anything that needs a turn tick in between.
- **Learning an API without docs**: a write endpoint can be mapped safely by posting a payload that can only fail validation.
  Status tells the story: 404 = no such route, 405 = wrong method, 401 = missing owner, 400 text = the next field. The public
  `pymerc` client (github.com/jmgilman/pymerc) has no building or travel calls, so don't look there.
  `tools/netlog.user.js` is no longer needed for this (kept in case another call hides).
- **Sea grid coverage**: whole map since Oct 13 (see "Ship routes").
- **Route economics** (v2 goal queue): a `route` goal = ship + destination + cargo + crew level; pick the destination
  from the world market data; return trip and arrival detection belong in the bot, not in clicks.
- **Next season**: the map may change. The area-parity rule and the dock rule are generic; regenerate `state/seamap`
  and `state/dump/api/towns.json` at season start. Don't assume ids or coordinates carry over.

## v2 shadow review (Oct 12, turn 13237)
- Running hourly, read-only, 10 checks pass. Latest: 3 risks, 1 tuning item; it plans orders but sends none.
- **Bug (false alarm)**: the "buy can't fill" flag compares our ceiling to the market's lowest ask. Porterage showed
  "ask 1.10 above ceiling 0.80" while our buy of 24 filled at 0.424 (the clearing price; the 1.10 ask is a deep placeholder
  offer). Flag it only when the last turn's buy actually under-filled, or the clearing price is above the ceiling.
- **Real finding**: intermediate buffers are thin (cloth 0.6 turns, flax plants 0.9), against the multi-turn stockpile goal.
  Production is slightly ahead of use, so nothing stalls today, but one upstream hiccup would. Candidate v2 rule: hold N turns
  of each chain stage, and size the downstream throttle to protect it.
- Porterage over-buys by ~9/turn (expires unused, ~4 coin/turn). Harmless; do NOT trim it (Oct 11 outage: porterage must
  never be dropped).

## v2 fixes + takeover plan (Oct 12)
- Fixed: "home ask above ceiling: can't fill" now fires only if last turn's purchases < 80% of need or stock is under runway (porterage fills on the bid side). Test added (11 checks).
- Added: tune flag when a chain buffer is under 2 turns (risk flag still <1 turn).
- Sea grid: batch 1 of 8 chunks queued Oct 12; remaining ~24 chunks in 8s after it lands (whole map x0-3039, y640-3103). Unreached tiles are treated as land, so travel dry-runs stay safe.
- "Perfect" is not provable; staged takeover is the safe path. Gates, one job at a time, each only after >=48 turns of shadow with no flag v1 handled better:
  1. Pricing/ceilings (buy/sell orders)  2. chain buffers  3. prestige agreed buys  4. build manager  5. travel/expand via goals.
  Each handover = flip a per-job switch in config.json, turn that job off in v1 in the same commit, watch 6 turns, auto-revert on any risk flag. Not yet coded: the per-job switches.

## Handover machinery + first live items (Oct 12-13)
- **Per-item, not per-job.** v2 owns an item when it is in `v2/config.json` `live.items` and not in `state/v2/suspended.json`.
  `v2_owned.py` (repo root) is the one shared answer; merc_actor, chain_balancer, failsafe (below BRAKE) and prestige_rules all
  skip owned items. At failsafe BRAKE/STOP v2 stands down and the failsafe acts on everything.
- **v2/act.py** runs after shadow.py in the v2-shadow workflow, now at **:25** (mid-turn; :50 runs started ~:57, right on the
  tick). It re-reads the store, merges v2's buy/sell into the live tiers (keeps min_holding and non-buy fields, folds extra
  buy tiers into one), checks guards (ceiling/floor, 50% price move, 2x+10 volume, cash reserve, never_drop, 2h manual window,
  8 writes/run), PATCHes, re-reads and verifies. Log: `state/v2/act.jsonl`; last run: `state/v2/act.json` (dry rows for every
  item too, so the next candidates can be judged).
- **Self-suspension**: risk flag on an owned item 2 runs in a row, or 2 failed writes in a row -> `state/v2/suspended.json`,
  item goes straight back to v1. Delete the entry to hand it back.
- **v2 owns the whole buy**: the planner marks `buy_off` when nothing needs a live buy (made at home, stocked 2x the runway,
  nothing used it); act takes it off for owned items only; never_drop items never get one.
- **First live run, turn 13238 (Oct 12 23:56 UTC)**: donations, cured fish, fish, grain, firewood -- 5 PATCHes, all verified.
  Chosen because each is a single-tier household/brewery buy within a few units of v1's order, with a ceiling set.
- **Verified**: v1's 00:25 run left all five untouched (live orders still v2's), and v2's 00:33 run re-sized grain 41 -> 37.
- **Handover 2 (00:35 UTC)**: porterage (bids at the 0.80 ceiling, so a price tick above v1's 0.60 can't starve the outlying
  buildings again; sized on the 24-turn peak; never_drop) and nets (first sell: 6/turn at the 36 floor, min_holding 40 kept).
  **Handover 3 (00:36)**: meat, ceiling 2.40 -> 3.02 to match the live bid (home ask is often 2.44-2.70). All verified.
- **Not handed over yet, and why**: labour (~800 coin/turn; v1 has 3 writers on it and the Oct 11 loss was labour: wants
  Taylor's OK), tools (v2 holds 8 turns, the failsafe's tool guard holds ~25: Taylor's policy), garments/beer/timber sells
  (garments interact with chain_balancer's pile drain; beer and timber floors vs live prices need Taylor's word), arms and
  beer buys (no ceiling set).
- Also: a buy the failsafe brake paused is never raised by v2 (restore by hand, Taylor's rule); v2 stands down at BRAKE/STOP.

## Finding: our bid is a limit, not the price we pay (Oct 12, turn 13237)
- Bought at well under our bids: labour bid 2.00 paid 1.66 avg, fish 2.50/1.70, meat 3.02/2.28, tools 6.20/5.14, cured fish
  26/24.8, grain 3.70/2.78, porterage 0.60/0.41. Sells likewise received the market (nets floor 36, got 41.4).
- So v2 now bids at the ceiling (planner, goals, builds). Bidding just over the lowest ask only under-fills deep needs
  (labour wanted 490, 430 offered near the ask). The ceiling is the real risk control.

## Ship routes (Oct 13, corrected after Taylor questioned the cost)
- Whole map pulled (36 chunks, x 0-3039, y 640-3103, 5M sea tiles). `tools/sea_distances.py`: one Dijkstra (~20 s) ->
  `state/v2/sea_routes.json`, 92 of 101 towns reachable. Matches the game within ~1 move (Blanans 296.8 vs 297.2).
- **First model was wrong** (said "no route pays"): it assumed 150 moves/turn (the Linen Snake test only showed *at least*
  150) and ~266 coin/turn crew, i.e. ~6 coin per unit shipped. Taylor: "you are calculating maximum price from ship".
- **Real numbers (game client + Flax Wyrm's own route data)**: movement per turn = type moves x crew (snekkja 3,000 at crew
  1.0; client `ze()`); route trips per turn = 3,000 x crew / (2 x distance) -> Blanans 5.03 = the route's `potential_trips`
  5.033 and `capacity` 1,258 = 250 x 5.03. Running cost = recipe "snekkja 1" x crew: 50 labour + 1.6 cloth + 0.5 tar +
  0.25 timber per turn at crew 1.0 (Flax Wyrm ran 0.953 of it for 122.5 coin; ~100 at Oct 13 prices). Per cargo slot that is
  ~0.08-0.2 coin (Blanans `capacity_cost` 0.103). Cargo space is each product's `size` (garments 1, beer 2, bread 3, timber 15,
  limestone 40), services (labour, porterage, lodging, protection, meat, fish, milk, ox power, donations) can't ship.
  Product table saved to `v2/data/products.json`. Snekkja: capacity 250, moves 3000, range 800.
- **So the limit is the markets, not the ship.** `v2/routes.py` sizes crew to the cargo (floor 0.23, as the game held the
  Flax Wyrm), takes at most max(10% depth, 30% of a town's per-turn trade), 5% slippage. Oct 12 21:00 prices: Blanans about
  +100 coin/turn (garments ~21/turn at ~25 vs 21.8 home), Rouhomme ~+75 (garments 68 at 23.6), Coburgbaum ~+150 but mostly
  bread bought at home (shakier). Not modelled: fees, prices moving as we sell, the one-off trip to set a route up.
- Phone app ship list = all 91 sea-reachable towns, by sea distance.
