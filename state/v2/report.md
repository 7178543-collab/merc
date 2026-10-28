# v2 shadow report

Turn 13610, 2026-10-28 11:27. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 1,102, prestige 3,248 (128 free, -6.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 0 | 0 | 0 | 15 | 0 | min_holding 60, sell 3, sell @ 2.94 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 0 | 0 | 0 | 0 | 0 | none |
| firewood | 3 | 2 | 2 | 1 | 0 | stop 12, buy 3, buy @ 2.4 |
| fish | 0 | 0 | 0 | 0 | 0 | none |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 2, sell @ 17.9 |
| grain | 47 | 0 | 0 | 0 | 0 | stop 21, buy 6, buy @ 3.7 |
| labour | 0 | 0 | 308 | 0 | 192 | buy @ 2.2 |
| meat | 0 | 0 | 0 | 0 | 0 | none |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34.2 |
| porterage | 2 | 2 | 2 | 3 | 0 | buy 2, buy @ 1.1 |

**5 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **beer**: needed (15.0/turn) but there is NO buy order, stock 0.0 -> v2: add buy 30
- **firewood**: brewery 1 ran short of firewood (buy is live (3 @ 2.4), 2 bought last turn); knock-on: mansion 1 (no beer); labour need rises ~52/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **firewood**: only 1.0 turns of firewood left and buying 3 (need 7) -> v2: buy 7
- **porterage**: flax farm 1 ran short of porterage (buy is live (2 @ 1.1), 2 bought last turn); knock-on: retting pit 1 (no flax plants), spinnery 1 (no flax fibres); labour need rises ~238/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **porterage**: buying 2, short of ~5 needed -> v2: buy 5

## Tuning

- **candles**: home ask 71.00 is above our ceiling 70.00 and last turn bought 1 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 107 over real use lately; planning 308, not 393

## Prestige spending, cheapest coin per prestige first

791 turns left: prestige gained now converts 98.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.9 | 48.9 | running |
| hold banquet 4 (pies) | mansion | 18 | 49.7 | 49.7 | thin at home: hop beer |
| hold banquet 2 (pies) | mansion | 7 | 50.3 | 50.3 | thin at home: pies |
| hold banquet 3 (pies) | mansion | 8 | 50.4 | 50.4 | thin at home: hop beer, pies |
| hold banquet 2 (fish) | mansion | 6.8 | 52.9 | 52.9 | thin at home: cured fish |
| hold banquet 4 | mansion | 17.5 | 53.0 | 53.0 | thin at home: hop beer, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 53.6 | 53.6 | thin at home: hop beer, stockfish, premium cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 53.9 | 53.9 | thin at home: hop beer, cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 54.3 | 54.3 |  |
| jousting 3 | arena | 230 | 54.6 | 54.8 | needs a arena (build cost 23,730); thin at home: swords, protection, plate armour; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 56.4 | 56.4 |  |
| hold feast 2 | townhouse | 2.6 | 53.3 | 56.5 | needs a townhouse (build cost 6,362) |

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
| arms | 1 @ 27.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had None) |
| beer | 30 @ 3.5, stop 60 | off | a building is stalled on beer: no sell until it runs again |
| candles | 1 @ 70.0, stop 61 |  | goal planner: buys 1 a turn for today's rates, keeps up to 61 (v2 had 2) |
| cured meat | 6 @ 24.2, stop 22 |  | goal planner: buys 6 a turn for today's rates, keeps up to 22 (v2 had None) |
| firewood | 3 @ 2.4, stop 12 |  | goal planner: buys 3 a turn for today's rates, keeps up to 12 (v2 had 7) |
| flax fibres |  | off | a building is stalled on flax fibres: no sell until it runs again |
| furniture | 2 @ 14.9, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 2 @ min 17.9 | goal planner: sells 2 at 17.9 (v2 had 2 at 22.4) |
| grain | 6 @ 3.7, stop 21 |  | goal planner: buys 6 a turn for today's rates, keeps up to 21 (v2 had 2) |
| labour | 38 @ 2.2, stop - |  | goal planner: buys 38 for today's rates (v2 had 0) |
| light armour | 1 @ 97, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| nets |  | 9 @ min 34.2 |  |
| pasties | 1 @ 14.5, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 2) |
| porterage | 6 @ 1.1, stop - |  | goal planner: buys 6 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 75.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| thread |  | 63 @ min 3.96 | goal planner: sells 63 a turn at 3.96, keeps 172 (no one offered it) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 200 |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 12.7k (cash + stock at home prices); -289/turn over 6 turns, -156/turn over 24 turns.
- Limits: cash flow >= +121/turn, prestige >= +7.18/turn (values are after 200 tax a turn).
- Today's settings: value -162/turn, cash -185/turn, prestige -1.76/turn - breaks the prestige floor and cash floor.
- Plan: value -150/turn, cash -52/turn, prestige -1.76/turn - could not meet the prestige floor and cash floor.
- Cash check (real vs predicted cash a tick, last 3): -29 vs -122, +67 vs -90, +76 vs -138.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - flax farm 1 5.88 -> 4.79: +7/turn
  - household duty 2.00 -> 0.00: -0/turn
  - spinnery 1 1.86 -> 1.60: -2/turn
- Model check over the last 59 turns: predicted +207/turn for the settings we ran, real -99/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 155.75, thread 391.15, cloth 624.78, flax fibres 463.28, garments 1807.90, nets 15.84, beer 278.03, timber 2.95, prestige 10000.00, cash 100.00
- Orders it would set: arms buy 1 (v2 None); candles buy 1 (v2 2); cured meat buy 6 (v2 None); firewood buy 3 (v2 7); fish buy 0 (v2 None); furniture buy 2 (v2 None); grain buy 6 (v2 2); labour buy 38 (v2 0); light armour buy 1 (v2 None); meat buy 0 (v2 None)
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +79/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new chandlery (make candles 1) for ~4064 coin: +2/turn, payback 1730 turns, doesn't pay yet (materials thin at home: bricks, nails)
- Trim: donate park 1: +379/turn (tax 96 saved).
- Trim: donate mansion 1: +237/turn (tax 0 saved).

## Chain sizing

Mode HOLD, garments sold 1.7/turn (+0.0 exported); plan makes 4.5 garments a turn.
Labour: own 500, everything else 374, chain may buy 0 -> chain allowance 126, chain plan 127 (-139 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.88 | 2.20 |
| ret | 3 | 1.00 | 0.44 |
| spin | 4 | 1.86 | 0.78 |
| weave | 3 | 0.15 | 0.17 |
| sew | 2 | 0.09 | 0.11 |

Buffers: flax fibres 0/40, thread 349/117, cloth 18/17
- chain plan needed 469 labour, budget left 126: cut to 126 (sewing capped at 0.11)

## Self-diagnosis

- R1: beer slot dry: 0.0 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy none, home ask 3.34 (held back: failsafe level 3: reduce-only, would buy 16 @ 3.4 (ask 3.34, cap 14.4))
- R1: donations slot dry: 0.0 held, 40.0 a turn (luxury slot (+1 prestige)); our buy none, home ask 1.0 (held back: failsafe level 3: reduce-only, would buy 54 @ 1.02 (ask 1.0, cap 1.5))
- R1: firewood slot dry: 3.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 3 @ 2.4, home ask 1.99; our bid is already at/over the ask (sellers too thin)
- R1: fish slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask 1.77 (held back: failsafe level 3: reduce-only, would buy 14 @ 1.8 (ask 1.77, cap 2.6))
- R1: meat slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask 1.79 (held back: failsafe level 3: reduce-only, would buy 14 @ 1.82 (ask 1.79, cap 2.6))
