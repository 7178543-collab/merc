# v2 shadow report

Turn 13586, 2026-10-27 11:56. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 1,966, prestige 3,403 (283 free, -7.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 0 | 0 | 0 | 0 | 0 | min_holding 60, sell 3, sell @ 2.94 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 0 | 0 | 0 | 0 | 0 | none |
| firewood | 0 | 0 | 0 | 1 | 0 | buy @ 2.4 |
| fish | 0 | 0 | 0 | 0 | 0 | none |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 2, sell @ 17.9 |
| grain | 47 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 0 | 0 | 397 | 0 | 103 | buy @ 2.2 |
| meat | 0 | 0 | 0 | 0 | 0 | none |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: sewing shop 1 ran short of cloth (no buy order); labour need rises ~14/turn when they restart -> v2: add a cloth buy
- **firewood**: brewery 1 ran short of firewood (buy is live (no volume cap @ 2.4), home ask 1.87 x3, yet 0 bought last turn); labour need rises ~17/turn when they restart -> v2: find out why the buy isn't filling
- **pasties**: only 0.5 turns of pasties left and buying 1 (need 4) -> v2: buy 4

## Tuning

- **tar**: home ask 12.60 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 108 over real use lately; planning 397, not 500

## Prestige spending, cheapest coin per prestige first

815 turns left: prestige gained now converts 98.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 3 (pies) | mansion | 8 | 45.2 | 45.2 | thin at home: hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 47.1 | 47.1 | thin at home: hop beer, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 47.9 | 47.9 | thin at home: hop beer, cured fish |
| maintain 1 | park | 0.5 | 48.3 | 48.3 | running |
| hold banquet 2 (pies) | mansion | 7 | 49.3 | 49.3 | thin at home: pies |
| hold banquet 3 (meat) | mansion | 7.6 | 50.2 | 50.2 | thin at home: hop beer, cured meat |
| hold banquet 4 | mansion | 17.5 | 50.3 | 50.3 | thin at home: hop beer, stockfish |
| hold banquet 2 (fish) | mansion | 6.8 | 51.4 | 51.4 | thin at home: cured fish |
| hold banquet 4 (premium) | mansion | 20 | 51.9 | 51.9 | thin at home: hop beer, stockfish, premium cheese |
| hold feast 3 | townhouse | 3.7 | 51.3 | 53.5 | needs a townhouse (build cost 6,514); thin at home: hop beer |
| jousting 3 | arena | 230 | 53.6 | 53.7 | needs a arena (build cost 24,061); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 54.0 | 54.0 |  |

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
| firewood | 1 @ 2.4, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 3) |
| flax fibres |  | 1 @ min 5 | goal planner: trial sale of an idle pile, 1 a turn at 5, keeps 82 (10 over) |
| flax plants |  | 2 @ min 1.05 | goal planner: sells 2 a turn at 1.05, keeps 9 (no one offered it) |
| furniture | 2 @ 13.6, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| grain | 6 @ 3.7, stop 21 |  | goal planner: buys 6 a turn for today's rates, keeps up to 21 (v2 had 0) |
| labour | 0 @ 2.2, stop - |  | goal planner: buys 0 for today's rates (v2 had 0) |
| light armour | 1 @ 96.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| nets |  | 9 @ min 34.0 |  |
| pasties | 2 @ 14.5, stop 8 |  | goal planner: buys 2 a turn for today's rates, keeps up to 8 (v2 had 4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 70.0) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 0 = 0.0 turns |
| thread |  | 42 @ min 3.96 | goal planner: sells 42 a turn at 3.96, keeps 169 (no one offered it) |
| tools | 1 @ 6.2, stop 1 |  | uses 0.1/turn (retting pit 1), makes 0.0, holds 200 = 3122.1 turns |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 16.4k (cash + stock at home prices); +425/turn over 6 turns, -73/turn over 24 turns.
- Limits: cash flow >= +85/turn, prestige >= +0.72/turn (values are after 200 tax a turn).
- Today's settings: value -152/turn, cash -145/turn, prestige -7.18/turn - breaks the prestige floor and cash floor.
- Plan: value -47/turn, cash -147/turn, prestige -2.98/turn - could not meet the prestige floor and cash floor.
- Cash check (real vs predicted cash a tick, last 3): +4 vs -136, +56 vs -141, +1566 vs -166.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - retting pit 1 [retting 1] 0.00 -> 0.45: +134/turn
  - spinnery 1 1.59 -> 1.86: +16/turn
  - weavery 1 0.13 -> 0.23: +6/turn
  - ropewalk 1 0.25 -> 0.00: +4/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.08: +13/turn
  - flax farm 1 5.88 -> 0.00: -59/turn
  - flax farm 1 [make flax fibres 1] 0.00 -> 11.00: +151/turn
  - mansion 1 0.00 -> 1.00: -162/turn
- Model check: not enough runs yet (needs 6 turns of goal history).
- Worth of one more unit per turn: labour 0.49, thread 3.42, cloth 4.16, flax fibres 7.89, garments 9.99, nets 15.03, beer 137.86, timber 3.10, prestige 10000.00, cash 100.00
- Orders it would set: firewood buy 1 (v2 3); fish buy 0 (v2 None); flax fibres sell 1 (v2 none); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); grain buy 6 (v2 0); light armour buy 1 (v2 None); meat buy 0 (v2 None); pasties buy 2 (v2 4); thread sell 42 (v2 none)
- Recipe: flax farm 1 grow flax 1 -> make flax fibres 1 at 11.00, worth +296/turn.
- Recipe: retting pit 1 retting 2 -> retting 1 at 0.45, worth +85/turn.
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.08, worth +7/turn.
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +20/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot flax farm 1 for ~477 coin: +3/turn, payback 155 turns
  - new carpentry (craft furniture 2) for ~1354 coin: +2/turn, payback 604 turns, doesn't pay yet
- Trim: donate park 1: +178/turn (tax 96 saved).
- Trim: donate mansion 1: +176/turn (tax 0 saved).

## Chain sizing

Mode HOLD, garments sold 1.2/turn (+0.0 exported); plan makes 10.7 garments a turn.
Labour: own 500, everything else 339, chain may buy 0 -> chain allowance 161, chain plan 160 (-54 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.88 | 1.66 |
| ret | 3 | 0.03 | 0.29 |
| spin | 4 | 1.59 | 0.82 |
| weave | 3 | 0.13 | 0.42 |
| sew | 2 | 0.09 | 0.26 |

Buffers: flax fibres 91/48, thread 1029/142, cloth 0/42
- chain plan needed 411 labour, budget left 161: cut to 161 (sewing capped at 0.26)

## Self-diagnosis

- R1: arms slot dry: 0.0 held, 0.5 a turn (gear slot (+0.4 prestige)); our buy 1 @ 27, home ask 28.6 (held back: failsafe level 3: reduce-only, would buy 1 @ 29.2 (ask 28.6, cap 48.0))
- R1: beer slot dry: 0.0 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy none, home ask 3.44 (held back: failsafe level 3: reduce-only, would buy 9 @ 3.5 (ask 3.44, cap 5.7))
- R1: candles slot dry: 0.0 held, 1.5 a turn (luxury slot (+3 prestige)); our buy 1 @ 70, home ask 68.5; our bid is already at/over the ask (sellers too thin)
- R1: donations slot dry: 0.0 held, 40.0 a turn (luxury slot (+1 prestige)); our buy none, home ask 1.0 (held back: failsafe level 3: reduce-only, would buy 80 @ 1.02 (ask 1.0, cap 1.5))
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 1.87; our bid is already at/over the ask (sellers too thin)
- R1: fish slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask 1.68 (held back: failsafe level 3: reduce-only, would buy 14 @ 1.71 (ask 1.68, cap 2.6))
- R1: meat slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask none (no sellers at home)
- R1: prestige rate -7.18 a turn vs 12-turn median -0.50; likely: dry slot: arms, beer, candles, donations, firewood, fish, meat
- R2: spinnery 1 blocked by thread space: 1029 held of 1084 capacity, we make 79.8 a turn; no buy on it: add a sell order or more capacity for thread
