# v2 shadow report

Turn 13585, 2026-10-27 10:35. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 399, prestige 3,410 (290 free, -7.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 0 | 0 | 0 | 0 | 0 | min_holding 60, sell 8, sell @ 2.94 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 0 | 0 | 0 | 0 | 0 | none |
| firewood | 0 | 0 | 0 | 2 | 0 | buy @ 2.4 |
| fish | 0 | 0 | 0 | 0 | 0 | none |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 2, sell @ 17.9 |
| grain | 47 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 0 | 0 | 395 | 0 | 105 | buy @ 2.2 |
| meat | 0 | 0 | 0 | 0 | 0 | none |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: sewing shop 1 ran short of cloth (no buy order); labour need rises ~14/turn when they restart -> v2: add a cloth buy
- **firewood**: brewery 1 ran short of firewood (buy is live (no volume cap @ 2.4), home ask 1.90 x1, yet 0 bought last turn); labour need rises ~36/turn when they restart -> v2: find out why the buy isn't filling

## Tuning

- **tar**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 106 over real use lately; planning 398, not 504

## Prestige spending, cheapest coin per prestige first

816 turns left: prestige gained now converts 98.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 3 (pies) | mansion | 8 | 45.1 | 45.1 | thin at home: hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 47.2 | 47.2 | thin at home: hop beer, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 47.7 | 47.7 | thin at home: hop beer |
| maintain 1 | park | 0.5 | 48.3 | 48.3 | running |
| hold banquet 3 (meat) | mansion | 7.6 | 49.1 | 49.1 | thin at home: hop beer |
| hold banquet 2 (pies) | mansion | 7 | 49.4 | 49.4 | thin at home: pies |
| hold banquet 4 | mansion | 17.5 | 50.4 | 50.4 | thin at home: hop beer, stockfish |
| hold banquet 2 (fish) | mansion | 6.8 | 51.5 | 51.5 |  |
| hold banquet 4 (premium) | mansion | 20 | 52.5 | 52.5 | thin at home: hop beer, stockfish, premium cheese |
| hold banquet 2 (meat) | mansion | 6.8 | 53.1 | 53.1 |  |
| hold feast 3 | townhouse | 3.7 | 51.3 | 53.5 | needs a townhouse (build cost 6,472); thin at home: hop beer |
| jousting 3 | arena | 230 | 53.7 | 53.9 | needs a arena (build cost 23,903); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |

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
| beer |  | 3 @ min 2.94 | goal planner: sells 3 a turn at 2.94, keeps 60 (no one offered it) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 5) |
| flax fibres |  | 3 @ min 4.56 | goal planner: trial sale of an idle pile, 3 a turn at 4.56, keeps 82 (32 over) |
| flax plants |  | 2 @ min 1.05 | goal planner: sells 2 a turn at 1.05, keeps 9 (no one offered it) |
| furniture | 2 @ 13.6, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 0) |
| labour | 0 @ 2.2, stop - |  | goal planner: buys 0 for today's rates (v2 had 0) |
| light armour | 1 @ 96.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| nets |  | 9 @ min 34.0 |  |
| pasties | 1 @ 14.5, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 2) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 70.0) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 0 = 1.0 turns |
| thread |  | 41 @ min 3.96 | goal planner: sells 41 a turn at 3.96, keeps 169 (no one offered it) |
| tools | 1 @ 6.2, stop 1 |  | uses 0.1/turn (retting pit 1), makes 0.0, holds 200 = 3123.1 turns |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 14.7k (cash + stock at home prices); +109/turn over 6 turns, -168/turn over 24 turns.
- Limits: cash flow >= +150/turn, prestige >= +0.42/turn (values are after 200 tax a turn).
- Today's settings: value -103/turn, cash -166/turn, prestige -7.25/turn - breaks the prestige floor and cash floor.
- Plan: value -32/turn, cash -142/turn, prestige -3.05/turn - could not meet the prestige floor and cash floor.
- Cash check (real vs predicted cash a tick, last 3): +9 vs -85, +4 vs -136, +56 vs -141.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - retting pit 1 [retting 1] 0.00 -> 0.36: +97/turn
  - ropewalk 1 0.25 -> 0.00: +16/turn
  - weavery 1 0.13 -> 0.23: +6/turn
  - spinnery 1 1.59 -> 1.82: +8/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.05: +9/turn
  - brewery 1 0.28 -> 0.13: -4/turn
  - flax farm 1 5.88 -> 0.00: -50/turn
  - flax farm 1 [make flax fibres 1] 0.00 -> 11.00: +141/turn
  - mansion 1 0.00 -> 1.00: -153/turn
- Model check: not enough runs yet (needs 6 turns of goal history).
- Worth of one more unit per turn: labour 0.49, thread 3.42, cloth 4.15, flax fibres 7.91, garments 9.95, nets 15.03, beer 138.03, timber 3.06, prestige 10000.00, cash 100.00
- Orders it would set: beer sell 3 (v2 none); firewood buy 2 (v2 5); fish buy 0 (v2 None); flax fibres sell 3 (v2 none); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); grain buy 9 (v2 0); light armour buy 1 (v2 None); meat buy 0 (v2 None); pasties buy 1 (v2 2)
- Recipe: flax farm 1 grow flax 1 -> make flax fibres 1 at 11.00, worth +297/turn.
- Recipe: retting pit 1 retting 2 -> retting 1 at 0.36, worth +65/turn.
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.05, worth +5/turn.
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +20/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot flax farm 1 for ~476 coin: +4/turn, payback 114 turns
  - new carpentry (craft furniture 2) for ~1353 coin: +3/turn, payback 389 turns, doesn't pay yet
- Trim: donate park 1: +176/turn (tax 96 saved).
- Trim: donate mansion 1: +170/turn (tax 0 saved).

## Chain sizing

Mode HOLD, garments sold 1.1/turn (+0.0 exported); plan makes 9.4 garments a turn.
Labour: own 500, everything else 358, chain may buy 0 -> chain allowance 142, chain plan 141 (-74 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.88 | 1.21 |
| ret | 3 | 0.03 | 0.22 |
| spin | 4 | 1.59 | 0.77 |
| weave | 3 | 0.13 | 0.37 |
| sew | 2 | 0.09 | 0.23 |

Buffers: flax fibres 113/47, thread 1031/137, cloth 0/37
- chain plan needed 403 labour, budget left 142: cut to 142 (sewing capped at 0.23)

## Self-diagnosis

- R1: arms slot dry: 0.0 held, 0.5 a turn (gear slot (+0.4 prestige)); our buy 1 @ 27, home ask 28.6; 5% of cash does not buy one at 29.2
- R1: beer slot dry: 0.0 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy none, home ask 3.44 (held back: failsafe level 3: reduce-only, would buy 5 @ 3.5 (ask 3.44, cap 5.7))
- R1: candles slot dry: 0.0 held, 1.5 a turn (luxury slot (+3 prestige)); our buy 1 @ 70, home ask 67.5; our bid is already at/over the ask (sellers too thin)
- R1: donations slot dry: 0.0 held, 40.0 a turn (luxury slot (+1 prestige)); our buy none, home ask 1.0 (held back: failsafe level 3: reduce-only, would buy 19 @ 1.02 (ask 1.0, cap 1.5))
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy none, home ask 1.9 (held back: failsafe level 3: reduce-only, would buy 6 @ 1.93 (ask 1.9, cap 2.1))
- R1: fish slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask 1.68 (held back: failsafe level 3: reduce-only, would buy 11 @ 1.71 (ask 1.68, cap 2.6))
- R1: meat slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask none (no sellers at home)
- R1: prestige rate -7.25 a turn vs 12-turn median -0.50; likely: dry slot: arms, beer, candles, donations, firewood, fish, meat
- R2: spinnery 1 blocked by thread space: 1031 held of 1084 capacity, we make 79.8 a turn; no buy on it: add a sell order or more capacity for thread
