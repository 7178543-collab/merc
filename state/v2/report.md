# v2 shadow report

Turn 13579, 2026-10-27 04:42. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 199, prestige 3,455 (335 free, -0.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 0 | 0 | 0 | 0 | 0 | min_holding 60, sell 22, sell @ 2.94 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 0 | 0 | 0 | 0 | 0 | none |
| firewood | 0 | 0 | 0 | 2 | 0 | buy @ 2.4 |
| fish | 0 | 0 | 0 | 0 | 0 | none |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 2, sell @ 17.9 |
| grain | 47 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 0 | 0 | 294 | 0 | 206 | buy @ 2.2 |
| meat | 0 | 0 | 0 | 0 | 0 | none |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 0 | 0 | 0 | 5 | 0 | buy 5, buy @ 1.1 |

**4 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: sewing shop 1 ran short of cloth (no buy order); labour need rises ~14/turn when they restart -> v2: add a cloth buy
- **firewood**: brewery 1 ran short of firewood (buy is live (no volume cap @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~36/turn when they restart -> v2: find out why the buy isn't filling
- **porterage**: flax farm 1, retting pit 1 ran short of porterage (buy is live (5 @ 1.1), home ask 0.36 x12, yet 0 bought last turn); labour need rises ~71/turn when they restart -> v2: find out why the buy isn't filling
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 9.75 x4, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 102 over real use lately; planning 294, not 390

## Prestige spending, cheapest coin per prestige first

822 turns left: prestige gained now converts 98.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 45.9 | 45.9 | running |
| hold banquet 3 (pies) | mansion | 8 | 47.0 | 47.0 | thin at home: pasties, hop beer, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 49.0 | 49.0 | thin at home: hop beer |
| hold banquet 4 (pies) | mansion | 18 | 49.2 | 49.2 | thin at home: pasties, hop beer, wine, pies |
| hold banquet 3 (meat) | mansion | 7.6 | 50.4 | 50.4 | thin at home: hop beer, cured meat |
| hold banquet 2 (pies) | mansion | 7 | 51.6 | 51.6 | thin at home: pasties, wine, pies |
| hold banquet 4 | mansion | 17.5 | 52.6 | 52.6 | thin at home: wine, hop beer, stockfish |
| hold banquet 2 (fish) | mansion | 6.8 | 53.0 | 53.0 | thin at home: wine |
| hold banquet 1 (fish) | mansion | 4.2 | 53.8 | 53.8 | thin at home: beer |
| hold banquet 4 (premium) | mansion | 20 | 54.3 | 54.3 | thin at home: hop beer, wine, stockfish, premium cheese |
| hold banquet 2 (meat) | mansion | 6.8 | 54.6 | 54.6 | thin at home: wine, cured meat |
| jousting 3 | arena | 230 | 55.0 | 55.1 | needs a arena (build cost 22,762); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~94 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Chribruck | 1202 | 0.40 | 0.20 (19/turn) | tackles 2 (183.75->195.7), garments 1 (16.82->19.38), cloth 5 (7.88->8.55), honey 2 (7.67->8.46) | alembics 1 (348.6->456) | +129 |
| Heidlowe | 662 | 0.17 | 0.20 (19/turn) | thread 66 (3.96->4.24), garments 1 (16.82->18.71), wine 11 (5.67->5.98), lead ore 1 (6.93->9.21) | alembics 1 (348.6->456) | +119 |
| Rouhomme | 368 | 0.09 | 0.60 (56/turn) | bread 145 (2.31->2.93), charcoal 11 (1.87->3.52), thread 7 (3.96->5.18), flour 1 (16.91->19.95) | ploughs 4 (63->69.35) | +100 |
| Herschweig | 775 | 0.20 | 0.10 (9/turn) | flax fibres 13 (4.98->6.13), lead ore 1 (6.93->10.45), garments 1 (16.82->18.81), wine 4 (5.67->6.32) | alembics 1 (386.4->456), cloth 3 (6.88->7.5), tackles 1 (152.25->153.9) | +90 |
| Angefont | 686 | 0.17 | 0.20 (19/turn) | thread 29 (3.96->5.79), limestone 1 (13.12->28.31), premium cheese 1 (26.04->27.74), flour 1 (16.91->18.81) | garments 2 (21.21->21.8), honey 3 (6.3->6.84) | +63 |

**Best:** Chribruck at about +129 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 18 @ min 2.94 | goal planner: sells 18 a turn at 2.94, keeps 60 (no one offered it) |
| firewood | 1 @ 2.4, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 5) |
| flax fibres |  | 16 @ min 4.7 | goal planner: trial sale of an idle pile, 16 a turn at 4.7, keeps 82 (184 over) |
| flax plants |  | 1 @ min 1.05 | goal planner: sells 1 a turn at 1.05, keeps 9 (no one offered it) |
| furniture | 2 @ 13.3, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| grain | 9 @ 3.7, stop 33 |  | goal planner: buys 9 a turn for today's rates, keeps up to 33 (v2 had 0) |
| labour | 0 @ 2.2, stop - |  | goal planner: buys 0 for today's rates (v2 had 0) |
| light armour | 1 @ 95.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| nets |  | 9 @ min 33.4 | goal planner: sells 9 at 33.4 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| thread |  | 36 @ min 3.96 | goal planner: sells 36 a turn at 3.96, keeps 169 (no one offered it) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 195 |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 14.0k (cash + stock at home prices); -177/turn over 6 turns, -153/turn over 24 turns.
- Limits: cash flow >= +158/turn, prestige >= -0.15/turn (values are after 200 tax a turn).
- Today's settings: value +17/turn, cash -90/turn, prestige +7.50/turn - breaks the cash floor.
- Plan: value +303/turn, cash +26/turn, prestige -0.15/turn - could not meet the cash floor.
- Cash check (real vs predicted cash a tick, last 3): +37 vs +14, +36 vs -60, +9 vs -85.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - retting pit 1 [retting 1] 0.00 -> 0.08: +12/turn
  - park 1 16.00 -> 0.71: +0/turn
  - weavery 1 0.13 -> 1.56: +19/turn
  - sewing shop 1 0.09 -> 0.97: +78/turn
  - spinnery 1 1.59 -> 2.35: +35/turn
  - ropewalk 1 0.25 -> 0.00: +0/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.12: +10/turn
  - brewery 1 0.28 -> 0.12: -8/turn
  - flax farm 1 5.88 -> 0.00: -37/turn
  - flax farm 1 [make flax fibres 1] 0.00 -> 11.00: +177/turn
- Model check: not enough runs yet (needs 6 turns of goal history).
- Worth of one more unit per turn: labour 0.39, thread 3.74, cloth 4.32, flax fibres 9.31, garments 9.90, nets 15.03, beer 124.63, timber 2.90, prestige 11.60, cash 100.00
- Orders it would set: beer sell 18 (v2 none); firewood buy 1 (v2 5); fish buy 0 (v2 None); flax fibres sell 16 (v2 none); flax plants sell 1 (v2 none); furniture buy 2 (v2 None); grain buy 9 (v2 0); light armour buy 1 (v2 None); meat buy 0 (v2 None); thread sell 36 (v2 none)
- Recipe: flax farm 1 grow flax 1 -> make flax fibres 1 at 11.00, worth +316/turn.
- Recipe: retting pit 1 retting 2 -> retting 1 at 0.08, worth +14/turn.
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.12, worth +9/turn.
- Management: ~11.39 of 17 used.
- Investments:
  - +1 plot flax farm 1 for ~458 coin: +48/turn, payback 9 turns
  - Tenants L13 for 500 prestige: +19/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new carpentry (craft furniture 1) for ~1297 coin: +5/turn, payback 273 turns, doesn't pay yet
- Trim: donate park 1: +86/turn (tax 96 saved).

## Chain sizing

Mode HOLD, garments sold 1.1/turn (+0.0 exported); plan makes 10.7 garments a turn.
Labour: own 500, everything else 358, chain may buy 0 -> chain allowance 142, chain plan 142 (-73 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.88 | 0.61 |
| ret | 3 | 0.03 | 0.11 |
| spin | 4 | 1.59 | 0.81 |
| weave | 3 | 0.13 | 0.41 |
| sew | 2 | 0.09 | 0.26 |

Buffers: flax fibres 265/48, thread 1055/141, cloth 0/41
- chain plan needed 384 labour, budget left 142: cut to 142 (sewing capped at 0.26)

## Self-diagnosis

- R1: arms slot dry: 0.0 held, 0.5 a turn (gear slot (+0.4 prestige)); our buy 1 @ 27, home ask 29.4; 5% of cash does not buy one at 30
- R1: beer slot dry: 0.0 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy none, home ask 3.56 (held back: failsafe level 3: reduce-only, would buy 2 @ 3.62 (ask 3.56, cap 5.7))
- R1: candles slot dry: 0.0 held, 1.5 a turn (luxury slot (+3 prestige)); our buy 1 @ 70, home ask 69.0; our bid is already at/over the ask (sellers too thin)
- R1: donations slot dry: 0.0 held, 40.0 a turn (luxury slot (+1 prestige)); our buy none, home ask 1.0 (held back: failsafe level 3: reduce-only, would buy 9 @ 1.02 (ask 1.0, cap 1.5))
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy none, home ask none (no sellers at home)
- R1: fish slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask 1.7 (held back: failsafe level 3: reduce-only, would buy 5 @ 1.73 (ask 1.7, cap 2.6))
- R1: meat slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask 1.71 (held back: failsafe level 3: reduce-only, would buy 5 @ 1.74 (ask 1.71, cap 2.6))
- R1: pasties slot dry: 0.0 held, 2.8 a turn (basic food slot (+1.3 prestige)); our buy 2 @ 14.5, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1055 held of 1084 capacity, we make 79.8 a turn; no buy on it: add a sell order or more capacity for thread
