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
- **Building placement: SOLVED (Oct 12)** by probing the API with an impossible type (`probe_write`, type `zzz_probe`; the game
  can only reject it, and its error text names the next missing field). `POST /buildings` with
  `{type, owner_id: "39992", town_id: "152202387", location: "1522:2388", sublocation: {x, y}, construction: {stage: "INITIAL"}}`.
  Ids must be strings. Creates an empty site (stage INITIAL); materials and labour then go to the construction account.
  Queue entry `{"build": {...}}`: dry run unless `"confirm": true`. A "park plot" is simply another `park` building on a free
  centre tile (260 labour, 40 timber, 60 limestone, 12 turns). Building ids encode the tile: `1522 2388 | 002 004` = sub (2, 4).
  Still to do: choose a free tile automatically (centre grid is 8 x 8; occupied tiles from our dumps plus other players'),
  fund the construction account, app button.
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
