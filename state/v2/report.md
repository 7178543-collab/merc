# v2 shadow report

Turn 13684, 2026-10-31 13:45. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 2,488, prestige 3,157 (37 free, -1.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 95 | 0 | 4 | 0 | 0 | min_holding 60, sell 17, sell @ 3.18 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 0 | 0 | 0 | 0 | 0 | none |
| firewood | 14 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 0 | 0 | 0 | 0 | 0 | none |
| garments | 16 | 0 | 2 | 0 | 0 | min_holding 8, sell 11, sell @ 19.6 |
| grain | 26 | 9 | 9 | 0 | 0 | stop 36, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 525 | 0 | 4 | buy 29, buy @ 2.2 |
| meat | 0 | 0 | 0 | 0 | 0 | none |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 4 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.6 turns (holds 15, next step uses 24/turn) -> v2: check the step that makes it
- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it

## Tuning

- **candles**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax plants**: flax plants buffer thin: 1.4 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 145
- **tar**: home ask 11.20 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 525, not 625

## Prestige spending, cheapest coin per prestige first

717 turns left: prestige gained now converts 97.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.1 | 47.1 | running |
| hold banquet 3 (pies) | mansion | 8 | 47.2 | 47.2 | thin at home: hop beer, pies, candles |
| hold banquet 2 (pies) | mansion | 7 | 49.0 | 49.0 | thin at home: wine, pies, candles |
| hold banquet 4 (pies) | mansion | 18 | 50.2 | 50.2 | thin at home: hop beer, wine, pies, candles |
| hold banquet 3 (meat) | mansion | 7.6 | 52.2 | 52.2 | thin at home: hop beer |
| hold banquet 3 (fish) | mansion | 7.6 | 52.6 | 52.6 | thin at home: hop beer, cured fish |
| jousting 3 | arena | 230 | 53.5 | 53.6 | needs a arena (build cost 25,590); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 53.7 | 53.7 | thin at home: wine |
| hold banquet 2 (fish) | mansion | 6.8 | 54.1 | 54.1 | thin at home: wine, cured fish |
| hold banquet 4 | mansion | 17.5 | 54.1 | 54.1 | thin at home: wine, hop beer, stockfish, candles |
| hold banquet 4 (premium) | mansion | 20 | 54.8 | 54.8 | thin at home: hop beer, wine, stockfish, candles, premium cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 55.7 | 55.7 |  |

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
| arms | 1 @ ?, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 4.0 turns |
| beer |  | 17 @ min 3.18 | goal planner: sells 17 at 3.18 (v2 had 17 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| candles | 2 @ 76.0, stop 6 |  | goal planner: buys 2 a turn for today's rates, keeps up to 6 (v2 had 3) |
| cured meat |  | 2 @ min 21.2 | goal planner: sells 2 a turn at 21.2, keeps 0 (no one offered it) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| garments |  | 11 @ min 19.6 | goal planner: sells 11 at 19.6 (v2 had 10 at 20.0) |
| grain | 9 @ 3.7, stop 36 |  | goal planner: buys 9 a turn for today's rates, keeps up to 36 (v2 had 14) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 25) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 80.5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 0 = 1.0 turns |
| thread |  | 20 @ min 3.96 | goal planner: sells 20 a turn at 3.96, keeps 189 (no one offered it) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 10.0k (cash + stock at home prices); -6/turn over 6 turns, +93/turn over 24 turns.
- Limits: cash flow >= +63/turn, prestige >= +10.94/turn (values are after 200 tax a turn).
- Today's settings: value +151/turn, cash +172/turn, prestige -1.49/turn - breaks the prestige floor.
- Plan: value -55/turn, cash +12/turn, prestige +2.71/turn - could not meet the prestige floor and cash floor.
- Cash check (real vs predicted cash a tick, last 3): +270 vs +132, -1379 vs +149, +295 vs +198 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - net maker 0.00 -> 0.28: +3/turn
  - sewing shop 1 0.30 -> 0.36: -2/turn
  - weavery 1 0.50 -> 0.57: +8/turn
  - flax farm 1 4.64 -> 6.17: -11/turn
  - retting pit 1 0.91 -> 1.23: +0/turn
  - spinnery 1 1.65 -> 2.18: +14/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.31: -21/turn
  - ropewalk 1 0.25 -> 0.00: +22/turn
  - mansion 1 0.00 -> 1.00: -221/turn
- HAND-OVER: goal planner: model check held 12 runs, it now runs 'rates' live.
- Model check over the last 59 turns: predicted +12/turn for the settings we ran, real -6/turn.
- Worth of one more unit per turn: labour 158.57, thread 398.18, cloth 636.03, flax fibres 471.53, garments 1840.51, nets 2878.65, beer 292.64, timber 686.80, prestige 10000.00, cash 100.00
- Orders it would set: candles buy 2 (v2 3); cured meat sell 2 (v2 none); firewood buy 4 (v2 5); fish buy 0 (v2 None); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 14); labour buy 29 (v2 25); light armour buy 1 (v2 None); meat buy 0 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.31, worth +15/turn.
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +82/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.7/turn (+0.0 exported); plan makes 33.2 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 510 (+221 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 6.50 |
| ret | 3 | 0.91 | 1.30 |
| spin | 4 | 1.65 | 2.30 |
| weave | 3 | 0.50 | 1.30 |
| sew | 2 | 0.30 | 0.81 |

Buffers: flax fibres 27/78, thread 215/230, cloth 15/130
- chain plan needed 511 labour, budget left 510: cut to 510 (sewing capped at 0.81)

## Self-diagnosis

- R1: donations slot dry: 0.0 held, 40.0 a turn (luxury slot (+1 prestige)); our buy none, home ask 1.0 (held back: failsafe level 2: reduce-only, would buy 80 @ 1.02 (ask 1.0, cap 1.5))
- R1: fish slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask 1.76 (held back: failsafe level 2: reduce-only, would buy 14 @ 1.79 (ask 1.76, cap 2.6))
- R1: meat slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask 1.96 (held back: failsafe level 2: reduce-only, would buy 14 @ 1.99 (ask 1.96, cap 2.6))
