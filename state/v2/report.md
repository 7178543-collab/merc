# v2 shadow report

Turn 13593, 2026-10-27 18:49. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 784, prestige 3,354 (234 free, -6.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 0 | 0 | 0 | 15 | 0 | min_holding 60, sell 3, sell @ 2.94 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 0 | 0 | 0 | 0 | 0 | none |
| firewood | 2 | 2 | 2 | 1 | 0 | stop 7, buy 2, buy @ 2.4 |
| fish | 0 | 0 | 0 | 0 | 0 | none |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 2, sell @ 17.9 |
| grain | 47 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 0 | 0 | 388 | 0 | 112 | buy @ 2.2 |
| meat | 0 | 0 | 0 | 0 | 0 | none |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34 |
| porterage | 2 | 2 | 2 | 0 | 0 | buy 2, buy @ 1.1 |

**5 risks, 0 waste, 4 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **beer**: needed (15.0/turn) but there is NO buy order, stock 0.0 -> v2: add buy 30
- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), 2 bought last turn); knock-on: mansion 1 (no beer); labour need rises ~52/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **firewood**: only 0.7 turns of firewood left and buying 2 (need 7) -> v2: buy 7
- **flax plants**: flax plants buffer 0.4 turns (holds 30, next step uses 80/turn) -> v2: check the step that makes it
- **pasties**: only 0.5 turns of pasties left and buying 1 (need 4) -> v2: buy 4

## Tuning

- **candles**: home ask 73.00 is above our ceiling 70.00 and last turn bought 1 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **pasties**: home ask 15.30 is above our ceiling 14.50 and last turn bought 2 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: home ask 12.60 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 108 over real use lately; planning 388, not 488

## Prestige spending, cheapest coin per prestige first

808 turns left: prestige gained now converts 98.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.0 | 48.0 | running |
| hold banquet 4 (pies) | mansion | 18 | 50.0 | 50.0 | thin at home: hop beer, wine, pies |
| hold banquet 3 (pies) | mansion | 8 | 50.4 | 50.4 | thin at home: hop beer, pies |
| hold banquet 2 (pies) | mansion | 7 | 51.2 | 51.2 | thin at home: wine, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 52.5 | 52.5 | thin at home: hop beer, cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 52.6 | 52.6 | thin at home: wine, cured fish |
| hold banquet 4 | mansion | 17.5 | 53.2 | 53.2 | thin at home: wine, hop beer, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 53.4 | 53.4 | thin at home: hop beer, wine, stockfish, premium cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 53.9 | 53.9 | thin at home: cured fish |
| jousting 3 | arena | 230 | 53.9 | 54.0 | needs a arena (build cost 24,693); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (meat) | mansion | 7.6 | 54.6 | 54.6 | thin at home: hop beer |
| hold banquet 2 (meat) | mansion | 6.8 | 54.9 | 54.9 | thin at home: wine |

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
| beer | 30 @ 3.6, stop 60 | off | a building is stalled on beer: no sell until it runs again |
| candles | 1 @ 70.0, stop 61 |  | goal planner: buys 1 a turn for today's rates, keeps up to 61 (v2 had 2) |
| cured meat | 6 @ 23, stop 24 |  | goal planner: buys 6 a turn for today's rates, keeps up to 24 (v2 had None) |
| firewood | 3 @ 2.4, stop 11 |  | goal planner: buys 3 a turn for today's rates, keeps up to 11 (v2 had 7) |
| furniture | 2 @ 14.7, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 2 @ min 17.9 | goal planner: sells 2 at 17.9 (v2 had 2 at 22.2) |
| grain | 0 @ 3.7, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 47 |
| labour | 0 @ 2.2, stop - |  | goal planner: buys 0 for today's rates (v2 had 0) |
| light armour | 1 @ 95.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| nets |  | 9 @ min 34.0 |  |
| pasties | 2 @ 14.5, stop 8 |  | goal planner: buys 2 a turn for today's rates, keeps up to 8 (v2 had 4) |
| porterage | 2 @ 1.1, stop - |  | goal planner: buys 2 for today's rates (v2 had 1) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 70.0) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 0 = 2.0 turns |
| thread |  | 45 @ min 3.96 | goal planner: sells 45 a turn at 3.96, keeps 172 (no one offered it) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 200 |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 16.0k (cash + stock at home prices); -83/turn over 6 turns, -5/turn over 24 turns.
- Limits: cash flow >= +134/turn, prestige >= +2.77/turn (values are after 200 tax a turn).
- Today's settings: value -306/turn, cash -196/turn, prestige -2.66/turn - breaks the prestige floor and cash floor.
- Plan: value -80/turn, cash -183/turn, prestige -2.66/turn - could not meet the prestige floor and cash floor.
- Cash check (real vs predicted cash a tick, last 3): -220 vs -267, -105 vs -196, +6 vs -168.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - flax farm 1 [grow flax 1] 0.00 -> 6.05: +210/turn
  - spinnery 1 1.86 -> 1.93: -1/turn
  - retting pit 1 1.00 -> 1.19: +2/turn
  - flax farm 1 2.75 -> 0.00: +14/turn
  - brewery 1 [brew mead 1] 0.00 -> 0.12: -22/turn
  - brewery 1 0.13 -> 0.00: +22/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.26: -27/turn
  - ropewalk 1 0.25 -> 0.00: +29/turn
- Model check: not enough runs yet (needs 6 turns of goal history).
- Worth of one more unit per turn: labour 1.33, thread 3.88, cloth 5.88, flax fibres 5.54, garments 16.49, nets 15.57, beer 138.53, timber 3.38, prestige 10000.00, cash 100.00
- Orders it would set: candles buy 1 (v2 2); cured meat buy 6 (v2 None); firewood buy 3 (v2 7); fish buy 0 (v2 None); furniture buy 2 (v2 None); light armour buy 1 (v2 None); meat buy 0 (v2 None); pasties buy 2 (v2 4); porterage buy 2 (v2 1); rope sell 2 (v2 1)
- Recipe: flax farm 1 make flax fibres 1 -> grow flax 1 at 6.05, worth +380/turn.
- Recipe: brewery 1 brew beer 1 -> brew mead 1 at 0.12, worth +5/turn.
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.26, worth +22/turn.
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +59/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new chandlery (make candles 1) for ~4194 coin: +5/turn, payback 780 turns, doesn't pay yet (materials thin at home: nails)
- Trim: donate park 1: +344/turn (tax 96 saved).
- Trim: donate mansion 1: +216/turn (tax 0 saved).

## Chain sizing

Not planned: chain buildings or recipes missing: flax

## Self-diagnosis

- R1: arms slot dry: 0.0 held, 0.5 a turn (gear slot (+0.4 prestige)); our buy 1 @ 27, home ask 27.4 (held back: failsafe level 3: reduce-only, would buy 1 @ 28 (ask 27.4, cap 48.0))
- R1: beer slot dry: 0.0 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy none, home ask 3.44 (held back: failsafe level 3: reduce-only, would buy 11 @ 3.5 (ask 3.44, cap 14.4))
- R1: donations slot dry: 0.0 held, 40.0 a turn (luxury slot (+1 prestige)); our buy none, home ask 1.0 (held back: failsafe level 3: reduce-only, would buy 38 @ 1.02 (ask 1.0, cap 1.5))
- R1: fish slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask 1.7 (held back: failsafe level 3: reduce-only, would buy 14 @ 1.73 (ask 1.7, cap 2.6))
- R1: meat slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask 1.97 (held back: failsafe level 3: reduce-only, would buy 14 @ 2 (ask 1.97, cap 2.6))
- R2: spinnery 1 blocked by thread space: 1021 held of 1084 capacity, we make 92.8 a turn; no buy on it: add a sell order or more capacity for thread
