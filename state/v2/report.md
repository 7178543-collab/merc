# v2 shadow report

Turn 13611, 2026-10-28 12:48. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 1,369, prestige 3,243 (123 free, -4.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 0 | 0 | 4 | 12 | 0 | min_holding 60, sell 3, sell @ 2.94 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 0 | 0 | 0 | 0 | 0 | none |
| firewood | 3 | 3 | 3 | 1 | 0 | stop 12, buy 3, buy @ 2.4 |
| fish | 0 | 0 | 0 | 0 | 0 | none |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 2, sell @ 17.9 |
| grain | 45 | 0 | 2 | 0 | 0 | stop 21, buy 6, buy @ 3.7 |
| labour | 25 | 0 | 318 | 0 | 182 | buy 25, buy @ 2.2 |
| meat | 0 | 0 | 0 | 0 | 0 | none |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34.2 |
| porterage | 6 | 2 | 2 | 3 | 0 | buy 6, buy @ 1.1 |

**4 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **beer**: needed (15.0/turn) but there is NO buy order, stock 0.0 -> v2: add buy 30
- **firewood**: brewery 1 ran short of firewood (buy is live (3 @ 2.4), 3 bought last turn); knock-on: mansion 1 (no beer); labour need rises ~52/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **firewood**: only 0.8 turns of firewood left and buying 3 (need 8) -> v2: buy 8
- **porterage**: flax farm 1 ran short of porterage (buy is live (6 @ 1.1), 2 bought last turn); knock-on: retting pit 1 (no flax plants), spinnery 1 (no flax fibres); labour need rises ~238/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it

## Waste (money lost now)

- **labour**: 182 labour expired last turn (~296 coin): holding 25 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **candles**: home ask 71.00 is above our ceiling 70.00 and last turn bought 1 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 107 over real use lately; planning 399, not 506

## Prestige spending, cheapest coin per prestige first

790 turns left: prestige gained now converts 98.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.9 | 48.9 | running |
| hold banquet 4 (pies) | mansion | 18 | 49.7 | 49.7 | thin at home: hop beer, pies |
| hold banquet 2 (pies) | mansion | 7 | 50.5 | 50.5 | thin at home: pies |
| hold banquet 3 (pies) | mansion | 8 | 50.6 | 50.6 | thin at home: hop beer, pies |
| hold banquet 2 (fish) | mansion | 6.8 | 53.1 | 53.1 | thin at home: cured fish |
| hold banquet 4 | mansion | 17.5 | 53.1 | 53.1 | thin at home: hop beer, stockfish |
| hold banquet 3 (fish) | mansion | 7.6 | 54.1 | 54.1 | thin at home: hop beer, cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 54.4 | 54.4 |  |
| hold banquet 4 (premium) | mansion | 20 | 54.5 | 54.5 | thin at home: hop beer, stockfish, premium cheese |
| jousting 3 | arena | 230 | 54.5 | 54.6 | needs a arena (build cost 24,913); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 56.1 | 56.1 |  |
| hold banquet 3 (meat) | mansion | 7.6 | 56.8 | 56.8 | thin at home: hop beer |

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
| arms | 1 @ 27.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 30 @ 3.54, stop 60 | off | a building is stalled on beer: no sell until it runs again |
| candles | 1 @ 70.0, stop 61 |  | goal planner: buys 1 a turn for today's rates, keeps up to 61 (v2 had 2) |
| cured meat | 6 @ 23.8, stop 23 |  | goal planner: buys 6 a turn for today's rates, keeps up to 23 (v2 had None) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 8) |
| furniture | 2 @ 15.1, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 2 @ min 17.9 | goal planner: sells 2 at 17.9 (v2 had 2 at 22.4) |
| grain | 6 @ 3.7, stop 22 |  | goal planner: buys 6 a turn for today's rates, keeps up to 22 (v2 had 2) |
| labour | 38 @ 2.2, stop - |  | goal planner: buys 38 for today's rates (v2 had 0) |
| light armour | 1 @ 101, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| nets |  | 9 @ min 34.2 |  |
| pasties | 1 @ 14.5, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 2) |
| porterage | 6 @ 1.1, stop - |  | goal planner: buys 6 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 75.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| thread |  | 54 @ min 3.96 | goal planner: sells 54 a turn at 3.96, keeps 172 (no one offered it) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 200 |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 13.0k (cash + stock at home prices); -236/turn over 6 turns, -143/turn over 24 turns.
- Limits: cash flow >= +110/turn, prestige >= +7.38/turn (values are after 200 tax a turn).
- Today's settings: value -165/turn, cash -230/turn, prestige -1.60/turn - breaks the prestige floor and cash floor.
- Plan: value -151/turn, cash -95/turn, prestige -1.60/turn - could not meet the prestige floor and cash floor.
- Cash check (real vs predicted cash a tick, last 3): +67 vs -90, +76 vs -138, +267 vs -185.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - flax farm 1 5.88 -> 4.99: +8/turn
  - spinnery 1 1.86 -> 1.67: +2/turn
  - household duty 2.00 -> 0.00: +0/turn
- Model check over the last 59 turns: predicted +202/turn for the settings we ran, real -94/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 159.28, thread 399.96, cloth 638.87, flax fibres 473.63, garments 1848.71, nets 15.84, beer 294.43, timber 3.40, prestige 10000.00, cash 100.00
- Orders it would set: candles buy 1 (v2 2); cured meat buy 6 (v2 None); firewood buy 4 (v2 8); fish buy 0 (v2 None); furniture buy 2 (v2 None); grain buy 6 (v2 2); labour buy 38 (v2 0); light armour buy 1 (v2 None); meat buy 0 (v2 None); pasties buy 1 (v2 2)
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +78/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new chandlery (make candles 1) for ~4285 coin: +2/turn, payback 2190 turns, doesn't pay yet (materials thin at home: bricks, nails)
- Trim: donate park 1: +378/turn (tax 96 saved).
- Trim: donate mansion 1: +237/turn (tax 0 saved).

## Chain sizing

Mode HOLD, garments sold 1.7/turn (+0.0 exported); plan makes 2.9 garments a turn.
Labour: own 500, everything else 374, chain may buy 0 -> chain allowance 126, chain plan 126 (-137 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.88 | 2.47 |
| ret | 3 | 1.00 | 0.49 |
| spin | 4 | 1.86 | 0.87 |
| weave | 3 | 0.15 | 0.09 |
| sew | 2 | 0.09 | 0.07 |

Buffers: flax fibres 15/37, thread 241/110, cloth 18/11
- chain plan needed 495 labour, budget left 126: cut to 126 (sewing capped at 0.07)

## Self-diagnosis

- R1: beer slot dry: 0.0 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy none, home ask 3.38 (held back: failsafe level 3: reduce-only, would buy 19 @ 3.44 (ask 3.38, cap 14.4))
- R1: donations slot dry: 0.0 held, 40.0 a turn (luxury slot (+1 prestige)); our buy none, home ask 1.0 (held back: failsafe level 3: reduce-only, would buy 67 @ 1.02 (ask 1.0, cap 1.5))
- R1: fish slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask 1.77 (held back: failsafe level 3: reduce-only, would buy 14 @ 1.8 (ask 1.77, cap 2.6))
- R1: meat slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask 1.78 (held back: failsafe level 3: reduce-only, would buy 14 @ 1.81 (ask 1.78, cap 2.6))
