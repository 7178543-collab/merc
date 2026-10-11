# Bot v2

Built beside v1 and tested in **shadow mode**: every hour it reads the live game, plans every order from the
game's own recipes, and writes what it *would* do. It never writes to the game while `mode` is `shadow`
(`api.write()` refuses unless `allow_writes()` is called, and `shadow.py` never calls it). v1 keeps running the season.

| File | What it is |
| --- | --- |
| `config.json` | every rule in one place: ceilings, floors, runways, perishables, never-drop inputs, stockpiles, builds |
| `api.py` | the one API client: retries, never exits the process, read-only unless writes are allowed |
| `snapshot.py` | one full read per turn (cash, household, every building's recipe/rate/limit, store items with orders and flows, ships, home market) |
| `planner.py` | one model of the business: demand from recipes x rates, supply, per-item orders, ranked flags (risk / waste / tune), prestige sink costs |
| `shadow.py` | runs it and writes `state/v2/` (snapshot, plan, report.md, history.jsonl) |
| `data/` | recipes and buildings extracted from the game code (`python tools/extract_gamedata.py` after a game update) |

Offline: `python v2/shadow.py --from state/v2/snapshot.json` replans a saved snapshot.

Roadmap: (1) shadow + daily v1-vs-v2 diff [now] -> (2) build manager, goal queue, prestige spending by coin per prestige ->
(3) hand jobs over one at a time in November (pricing, chain sizing, prestige, contracts) -> (4) Season 9: v2 only.
