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
  * **Land claims**: `POST /towns/{id}/expand {claims: [{x, y, sub: {x, y}}], properties: []}` (omit `landing`; it is not a
    boolean). Replies 200 with the account embedded, **but settles at the next turn tick** (money stays reserved); the tile
    still reads `{ask_price: "24"}` until then. So claim, wait a tick, then expand. Queue entry `{"claim": {...}}`.
  * Town centre data: `GET /towns/{id}` `domain` holds one entry per sub-tile, key = centre * 1,000,000 + sx * 1000 + sy, value
    `{owner_id, structure?, ask_price?}`. No entry or an ask-price-only entry = unowned land. Centres are in `center_ids`; the
    main centre (town location) has reserved plaza/hall tiles, so skip it.
  * Mistake to avoid: my first `expand` claimed the tile of EVERY candidate it tried (5 small claims) before the expansion
    could start. Claim only the tile you will use. Fixed in intent: pass `"tiles": [...]` when the tile is known.
- **Deferred steps** (`{"later": {"after": ISO time, "entry": {...}}}`): parked in `state/deferred.json`, run on the first
  workflow run at or after that time (hourly at :20, or any queue push), same guards, logged with source `deferred`.
  Tested offline with a stubbed module (no network, no credentials). Use for anything that needs a turn tick in between.
- **Learning an API without docs**: a write endpoint can be mapped safely by posting a payload that can only fail validation.
  Status tells the story: 404 = no such route, 405 = wrong method, 401 = missing owner, 400 text = the next field. The public
  `pymerc` client (github.com/jmgilman/pymerc) has no building or travel calls, so don't look there.
  `tools/netlog.user.js` is no longer needed for this (kept in case another call hides).
- **Sea grid coverage**: only x 992-2015, y 1888-2911 (every town within ~500 tiles of home). Far towns need more
  sections. Idea: let the travel handler fetch missing sections itself, cached by bbox.
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
