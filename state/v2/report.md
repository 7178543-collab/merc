# v2 shadow report

Turn 13554, 2026-10-26 03:15. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 796, prestige 3,563 (443 free, -1.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 7 | 0 | 0 | min_holding 60, sell 55, sell @ 2.98 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 6 | 0 | 6 | 1 | 0 | buy @ 2.4; sell 1, sell @ 1.73 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 2, sell @ 17.9 |
| grain | 57 | 21 | 22 | 0 | 0 | stop 81, buy 21, buy @ 3.7 |
| labour | 0 | 0 | 451 | 0 | 49 | buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 15 | 0 | 0 | 0 | 0 | min_holding 15, sell 10, sell @ 33.6 |
| porterage | 14 | 14 | 13 | 0 | 1 | buy 14, buy @ 1.1 |

**2 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: sewing shop 1 ran short of cloth (no buy order); labour need rises ~14/turn when they restart -> v2: add a cloth buy
- **firewood**: brewery 1 ran short of firewood (buy is live (no volume cap @ 2.4), home ask 1.73 x4, yet 0 bought last turn); labour need rises ~57/turn when they restart -> v2: find out why the buy isn't filling

## Tuning

- **flax plants**: flax plants buffer thin: 1.2 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 187

## Notes

- labour: projection runs 112 over real use lately; planning 451, not 564

## Prestige spending, cheapest coin per prestige first

847 turns left: prestige gained now converts 98.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 46.2 | 46.2 | running |
| hold banquet 3 (pies) | mansion | 8 | 46.8 | 46.8 | thin at home: hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 47.9 | 47.9 | thin at home: hop beer, wine, pies |
| hold banquet 2 (pies) | mansion | 7 | 49.3 | 49.3 | thin at home: wine, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 50.0 | 50.0 | thin at home: hop beer |
| hold banquet 3 (meat) | mansion | 7.6 | 50.4 | 50.4 | thin at home: hop beer |
| hold banquet 4 | mansion | 17.5 | 51.2 | 51.2 | thin at home: wine, hop beer, stockfish |
| hold banquet 2 (fish) | mansion | 6.8 | 52.0 | 52.0 | thin at home: wine |
| hold banquet 2 (meat) | mansion | 6.8 | 52.4 | 52.4 | thin at home: wine |
| jousting 3 | arena | 230 | 52.7 | 52.8 | needs a arena (build cost 23,164); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 54.0 | 54.0 | thin at home: hop beer, wine, stockfish, premium cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 54.2 | 54.2 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -5 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~95 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Fontaux | 411 | 0.10 | 0.30 (29/turn) | thread 70 (4.46->5.65), charcoal 11 (1.93->3.8), cheese 11 (5.83->6.74), glass ingots 3 (58.8->61.27) | candles 1 (70.35->71.5), fleece 1 (5.99->7.5), flax plants 5 (1.07->1.36) | +100 |
| Kirchwerp | 1072 | 0.34 | 0.20 (19/turn) | glassware 3 (50.82->62.22), arms 5 (28.35->33.06), glass ingots 3 (58.8->61.75), wheels 2 (19.53->22.61) | jewellery 3 (91.35->95), candles 1 (68.25->71.5), premium cheese 1 (26.25->28.5), tools 2 (4.73->5.15) | +76 |
| Neuborn | 780 | 0.20 | 0.30 (29/turn) | glass ingots 3 (58.8->74.1), gold ore 1 (141.75->152.95), bricks 4 (4.98->9.5), seeds 12 (2.75->3.32) | canvas 3 (31.92->34.01), cheese 13 (4.83->5.22), candles 1 (69.83->71.5), flax fibres 12 (5.12->5.55) | +68 |
| Hofkirchen | 991 | 0.30 | 0.20 (19/turn) | flax plants 10 (1.19->3.89), arms 5 (28.35->32.87), yarn 5 (4.07->5.08), cloth 7 (7.72->8.5) | candles 1 (67.2->71.5), blades 2 (11.76->13.3), bellows 1 (252->254.6), premium cheese 1 (27.3->28.5) | +58 |
| Brebronn | 862 | 0.24 | 0.10 (10/turn) | spinning wheels 1 (262.5->277.4), glass ingots 3 (58.8->63.65), cloth 7 (7.72->8.46), leather 1 (31.71->32.3) | looms 1 (518.7->546.25), candles 1 (69.3->71.5), fleece 1 (6.93->7.5) | +56 |

**Best:** Fontaux at about +100 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 28.2, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 4.0 turns |
| cured meat | 1 @ 29.0, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 2) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 0 @ 2.4, stop 13 | off | a building is stalled on firewood: no sell until it runs again |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres |  | 1 @ min 4.82 | goal planner: sells 1 a turn at 4.82, keeps 82 (no one offered it) |
| grain | 29 @ 3.7, stop 88 |  | goal planner: buys 29 a turn for today's rates, keeps up to 88 (v2 had 38) |
| labour | 0 @ 2.2, stop - |  | goal planner: buys 0 for today's rates (v2 had 0) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 10 @ min 33.6 | goal planner: sells 10 at 33.6 (v2 had 10 at 36.0) |
| pasties | 2 @ 14.5, stop 8 |  | goal planner: buys 2 a turn for today's rates, keeps up to 8 (v2 had 4) |
| porterage | 14 @ 1.1, stop - |  | goal planner: buys 14 for today's rates (v2 had 13) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 (v2 had 1) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 1 = 4.0 turns |
| thread |  | 20 @ min 4.26 | goal planner: sells 20 a turn at 4.26, keeps 180 (no one offered it) |
| tools | 3 @ 6.2, stop 18 |  | uses 2.2/turn (net maker152202386007001, retting pit 1), makes 0.0, holds 199 = 89.7 turns |
| varnish | 1 @ 20.2, stop 1 |  | uses 0.1/turn (net maker152202386007001), makes 0.0, holds 0 = 3.2 turns |
| wax | 1 @ 23.0, stop 1 |  | uses 0.1/turn (net maker152202386007001), makes 0.0, holds 1 = 9.2 turns |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 18.3k (cash + stock at home prices); +8/turn over 6 turns, -7/turn over 24 turns.
- Limits: cash flow >= +134/turn, prestige >= -0.60/turn (values are after 220 tax a turn).
- Today's settings: value +85/turn, cash +18/turn, prestige -1.91/turn - breaks the prestige floor and cash floor.
- Plan: value +86/turn, cash +132/turn, prestige -0.60/turn - could not meet the cash floor.
- Cash check (real vs predicted cash a tick, last 3): -337 vs +55, -252 vs +27, -200 vs +41 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Hofkirchen: +5/turn
  - ship Flax Wyrm -> Angefont: +0/turn
  - ropewalk 1 0.25 -> 0.64: +36/turn
  - spinnery 1 1.59 -> 2.03: +25/turn
  - net maker 0.23 -> 0.00: +4/turn
  - weavery 1 0.13 -> 0.22: +5/turn
  - retting pit 1 1.04 -> 0.51: -32/turn
  - flax farm 1 5.88 -> 2.94: -1/turn
  - mansion 1 0.15 -> 0.47: -50/turn
- Model check over the last 59 turns: predicted +111/turn for the settings we ran, real +34/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 0.44, thread 3.14, cloth 3.80, flax fibres 7.30, garments 9.09, nets 16.65, beer 121.59, timber 3.02, prestige 3496.78, cash 100.00
- Orders it would set: cured meat buy 1 (v2 2); flax fibres sell 1 (v2 none); furniture buy 2 (v2 None); grain buy 29 (v2 38); light armour buy 1 (v2 None); pasties buy 2 (v2 4); porterage buy 14 (v2 13); rope sell 2 (v2 1); thread sell 20 (v2 none)
- Ship linen snake: Grandgues -> Hofkirchen (+7/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Angefont (+0/turn over staying).
- Management: ~12.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +39/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new chandlery (make candles 1) for ~4002 coin: +23/turn, payback 175 turns, doesn't pay yet (materials thin at home: bricks, nails)
  - +1 plot park 1 for ~1472 coin: +8/turn, payback 187 turns, doesn't pay yet (materials thin at home: limestone)
  - new weaponsmith (forge arms 1) for ~2587 coin: +7/turn, payback 352 turns, doesn't pay yet (materials thin at home: bricks, wrought iron)
- Trim: donate logging camp w/ tool: +29/turn (tax 20 saved).
- Trim: donate net maker: +17/turn (tax 6 saved).

## Chain sizing

Mode HOLD, garments sold 1.1/turn (+0.0 exported); plan makes 6.6 garments a turn.
Labour: own 500, everything else 394, chain may buy 0 -> chain allowance 106, chain plan 105 (-135 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.88 | 0.39 |
| ret | 3 | 1.04 | 0.07 |
| spin | 4 | 1.59 | 0.73 |
| weave | 3 | 0.13 | 0.26 |
| sew | 2 | 0.09 | 0.16 |

Buffers: flax fibres 291/45, thread 1047/133, cloth 0/26
- chain plan needed 393 labour, budget left 106: cut to 106 (sewing capped at 0.16)

## Self-diagnosis

- R2: spinnery 1 blocked by thread space: 1047 held of 1084 capacity, we make 79.8 a turn; no buy on it: add a sell order or more capacity for thread
