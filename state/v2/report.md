# v2 shadow report

Turn 13578, 2026-10-27 03:22. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 189, prestige 3,463 (343 free, -0.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 0 | 0 | 0 | 0 | 0 | min_holding 60, sell 25, sell @ 2.94 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 0 | 0 | 0 | 0 | 0 | none |
| firewood | 0 | 0 | 0 | 2 | 0 | buy @ 2.4 |
| fish | 0 | 0 | 0 | 0 | 0 | none |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 2, sell @ 17.9 |
| grain | 47 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 0 | 0 | 288 | 0 | 212 | buy @ 2.2 |
| meat | 0 | 0 | 0 | 0 | 0 | none |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 0 | 0 | 0 | 5 | 0 | buy 5, buy @ 1.1 |

**4 risks, 0 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: sewing shop 1 ran short of cloth (no buy order); labour need rises ~14/turn when they restart -> v2: add a cloth buy
- **firewood**: brewery 1 ran short of firewood (buy is live (no volume cap @ 2.4), home ask 1.87 x3, yet 0 bought last turn); labour need rises ~36/turn when they restart -> v2: find out why the buy isn't filling
- **porterage**: flax farm 1, retting pit 1 ran short of porterage (buy is live (5 @ 1.1), home ask 0.36 x3, yet 0 bought last turn); labour need rises ~71/turn when they restart -> v2: find out why the buy isn't filling
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 9.55 x9, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Notes

- labour: projection runs 102 over real use lately; planning 293, not 394

## Prestige spending, cheapest coin per prestige first

823 turns left: prestige gained now converts 98.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 45.9 | 45.9 | running |
| hold banquet 3 (pies) | mansion | 8 | 46.5 | 46.5 | thin at home: hop beer, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 49.0 | 49.0 | thin at home: hop beer |
| hold banquet 4 (pies) | mansion | 18 | 49.0 | 49.0 | thin at home: hop beer, wine, pies |
| hold banquet 3 (meat) | mansion | 7.6 | 50.4 | 50.4 | thin at home: hop beer |
| hold banquet 2 (pies) | mansion | 7 | 50.6 | 50.6 | thin at home: wine, pies |
| hold banquet 4 (premium) | mansion | 20 | 51.9 | 51.9 | thin at home: hop beer, wine, stockfish, premium cheese, premium ham |
| hold banquet 4 | mansion | 17.5 | 52.5 | 52.5 | thin at home: wine, hop beer, stockfish |
| hold banquet 2 (fish) | mansion | 6.8 | 52.6 | 52.6 | thin at home: wine |
| hold banquet 1 (fish) | mansion | 4.2 | 53.3 | 53.3 |  |
| hold banquet 2 (meat) | mansion | 6.8 | 54.2 | 54.2 | thin at home: wine |
| jousting 3 | arena | 230 | 55.4 | 55.5 | needs a arena (build cost 23,455); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |

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
| beer |  | 22 @ min 2.94 | goal planner: sells 22 a turn at 2.94, keeps 60 (no one offered it) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 5) |
| flax fibres |  | 17 @ min 4.76 | goal planner: trial sale of an idle pile, 17 a turn at 4.76, keeps 82 (204 over) |
| flax plants |  | 1 @ min 1.05 | goal planner: sells 1 a turn at 1.05, keeps 9 (no one offered it) |
| furniture | 2 @ 11.3, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| grain | 0 @ 3.7, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 47 |
| labour | 0 @ 2.2, stop - |  | goal planner: buys 0 for today's rates (v2 had 0) |
| light armour | 1 @ 91.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| thread |  | 29 @ min 3.96 | goal planner: sells 29 a turn at 3.96, keeps 169 (no one offered it) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 195 |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 14.4k (cash + stock at home prices); -135/turn over 6 turns, -161/turn over 24 turns.
- Limits: cash flow >= +159/turn, prestige >= -0.18/turn (values are after 200 tax a turn).
- Today's settings: value +32/turn, cash -85/turn, prestige +7.50/turn - breaks the cash floor.
- Plan: value +322/turn, cash +18/turn, prestige -0.18/turn - could not meet the cash floor.
- Cash check (real vs predicted cash a tick, last 3): +26 vs -12, +37 vs +14, +36 vs -60.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - retting pit 1 [retting 1] 0.00 -> 0.08: +12/turn
  - brewery 1 [brew mead 1] 0.00 -> 0.18: +5/turn
  - park 1 16.00 -> 0.64: +0/turn
  - weavery 1 0.13 -> 1.46: +13/turn
  - sewing shop 1 0.09 -> 0.91: +77/turn
  - spinnery 1 1.59 -> 2.48: +34/turn
  - brewery 1 0.28 -> 0.00: +9/turn
  - ropewalk 1 0.25 -> 0.00: -6/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.14: +14/turn
  - flax farm 1 5.88 -> 0.00: -40/turn
- Model check: not enough runs yet (needs 6 turns of goal history).
- Worth of one more unit per turn: labour 0.38, thread 3.73, cloth 4.29, flax fibres 9.29, garments 9.81, nets 15.21, beer 134.42, timber 2.94, prestige 11.35, cash 100.00
- Orders it would set: beer sell 22 (v2 none); firewood buy 2 (v2 5); fish buy 0 (v2 None); flax fibres sell 17 (v2 none); flax plants sell 1 (v2 none); furniture buy 2 (v2 None); light armour buy 1 (v2 None); meat buy 0 (v2 None); rope sell 1 (v2 none); thread sell 29 (v2 none)
- Recipe: flax farm 1 grow flax 1 -> make flax fibres 1 at 11.00, worth +295/turn.
- Recipe: retting pit 1 retting 2 -> retting 1 at 0.08, worth +14/turn.
- Recipe: brewery 1 brew beer 1 -> brew mead 1 at 0.18, worth +27/turn.
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.14, worth +12/turn.
- Management: ~11.39 of 17 used.
- Investments:
  - +1 plot flax farm 1 for ~459 coin: +32/turn, payback 15 turns
  - Tenants L13 for 500 prestige: +19/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new carpentry (craft furniture 1) for ~1301 coin: +2/turn, payback 649 turns, doesn't pay yet
- Trim: donate park 1: +87/turn (tax 96 saved).

## Chain sizing

Mode HOLD, garments sold 1.2/turn (+0.0 exported); plan makes 10.7 garments a turn.
Labour: own 500, everything else 358, chain may buy 0 -> chain allowance 142, chain plan 142 (-73 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.88 | 0.61 |
| ret | 3 | 0.03 | 0.11 |
| spin | 4 | 1.59 | 0.81 |
| weave | 3 | 0.13 | 0.41 |
| sew | 2 | 0.09 | 0.26 |

Buffers: flax fibres 285/48, thread 1052/141, cloth 0/41
- chain plan needed 384 labour, budget left 142: cut to 142 (sewing capped at 0.26)

## Self-diagnosis

- R1: arms slot dry: 0.0 held, 0.5 a turn (gear slot (+0.4 prestige)); our buy 1 @ 27, home ask 30.4; 5% of cash does not buy one at 31
- R1: beer slot dry: 0.0 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy none, home ask 3.44 (held back: failsafe level 3: reduce-only, would buy 2 @ 3.5 (ask 3.44, cap 5.7))
- R1: candles slot dry: 0.0 held, 1.5 a turn (luxury slot (+3 prestige)); our buy 1 @ 70, home ask 69.0; our bid is already at/over the ask (sellers too thin)
- R1: donations slot dry: 0.0 held, 40.0 a turn (luxury slot (+1 prestige)); our buy none, home ask 1.0 (held back: failsafe level 3: reduce-only, would buy 9 @ 1.02 (ask 1.0, cap 1.5))
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy none, home ask 1.87 (held back: failsafe level 3: reduce-only, would buy 4 @ 1.9 (ask 1.87, cap 2.1))
- R1: fish slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask 1.72 (held back: failsafe level 3: reduce-only, would buy 5 @ 1.75 (ask 1.72, cap 2.6))
- R1: meat slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask 1.71 (held back: failsafe level 3: reduce-only, would buy 5 @ 1.74 (ask 1.71, cap 2.6))
- R1: pasties slot dry: 0.0 held, 2.8 a turn (basic food slot (+1.3 prestige)); our buy 2 @ 14.5, home ask 12.7; our bid is already at/over the ask (sellers too thin)
- R2: spinnery 1 blocked by thread space: 1052 held of 1084 capacity, we make 79.8 a turn; no buy on it: add a sell order or more capacity for thread
