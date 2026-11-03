# v2 shadow report

Turn 13745, 2026-11-03 02:47. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 5,956, prestige 3,189 (69 free, -0.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 13 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 22 | 0 | 2 | 0 | 0 | min_holding 30, sell 12, sell @ 19.4 |
| grain | 33 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 525 | 0 | 4 | buy 29, buy @ 2.2 |
| meat | 0 | 0 | 0 | 0 | 0 | none |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**1 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it

## Tuning

- **tar**: home ask 12.40 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 525, not 618

## Prestige spending, cheapest coin per prestige first

656 turns left: prestige gained now converts 96.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.7 | 47.7 | running |
| hold banquet 4 (pies) | mansion | 18 | 51.1 | 51.1 | thin at home: hop beer, stockfish, cheese, pies |
| jousting 3 | arena | 230 | 52.9 | 53.1 | needs a arena (build cost 25,224); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 53.5 | 53.5 | thin at home: hop beer, stockfish, premium cheese |
| hold banquet 4 | mansion | 17.5 | 54.3 | 54.3 | thin at home: hop beer, ham, stockfish, cheese |
| hold banquet 3 (pies) | mansion | 8 | 54.8 | 54.8 | thin at home: hop beer, cheese, pies |
| hold banquet 2 (pies) | mansion | 7 | 54.9 | 54.9 | thin at home: cheese, pies |
| hold prayer 2 | chapel | 13 | 52.9 | 56.9 | needs a chapel (build cost 31,122); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 53.2 | 56.9 | needs a church (build cost 65,897); thin at home: candles, furniture |
| hold sermon 2 | church | 24 | 53.4 | 58.2 | needs a church (build cost 65,897); thin at home: furniture |
| jousting 2 | arena | 210 | 58.0 | 58.2 | needs a arena (build cost 25,224); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold mass 1 | cathedral | 180 | 57.5 | 60.2 | needs a cathedral (build cost 260,785); thin at home: jewellery, glassware, candles |

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
| arms | 1 @ 34.4, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 3.0 turns |
| beer |  | 16 @ min 3.06 | goal planner: sells 16 at 3.06 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 6) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 10 @ min 19.4 | goal planner: sells 10 at 19.4 (v2 had 10 at 20.0) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 25) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.6) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 75.5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 16.5k (cash + stock at home prices); -155/turn over 6 turns, +79/turn over 24 turns.
- Limits: cash flow >= -81/turn, prestige >= +9.65/turn (values are after 200 tax a turn).
- Today's settings: value +60/turn, cash +45/turn, prestige -0.34/turn - breaks the prestige floor.
- Plan: value -165/turn, cash -126/turn, prestige +3.86/turn - could not meet the prestige floor and cash floor.
- Cash check (real vs predicted cash a tick, last 3): -89 vs +87, -98 vs +84, -77 vs +60 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - net maker 0.00 -> 0.28: +3/turn
  - weavery 1 0.50 -> 0.41: -1/turn
  - spinnery 1 1.65 -> 1.32: -10/turn
  - retting pit 1 0.91 -> 0.75: +1/turn
  - flax farm 1 4.64 -> 3.73: -8/turn
  - brewery 1 0.14 -> 0.27: -0/turn
  - ropewalk 1 0.25 -> 0.00: -11/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.25: +11/turn
  - mansion 1 0.00 -> 1.00: -231/turn
- Model check over the last 59 turns: predicted +90/turn for the settings we ran, real +104/turn.
- Worth of one more unit per turn: labour 161.60, thread 410.21, cloth 652.61, flax fibres 493.55, garments 1884.31, nets 2938.26, beer 285.97, timber 3.10, prestige 10000.00, cash 100.00
- Orders it would set: beer sell 16 (v2 15); candles buy 2 (v2 None); firewood buy 4 (v2 6); furniture buy 2 (v2 None); grain buy 9 (v2 11); labour buy 29 (v2 25); light armour buy 1 (v2 None); meat buy 0 (v2 None); rope sell 2 (v2 1)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.25, worth +8/turn.
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new chandlery (make tallow candles 2) for ~4394 coin: +21/turn, payback 213 turns, doesn't pay yet (materials thin at home: nails)

## Chain sizing

Mode HOLD, garments sold 3.4/turn (+0.0 exported); plan makes 32.4 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 501 (+212 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 6.42 |
| ret | 3 | 0.91 | 1.28 |
| spin | 4 | 1.65 | 2.27 |
| weave | 3 | 0.50 | 1.27 |
| sew | 2 | 0.30 | 0.79 |

Buffers: flax fibres 27/77, thread 190/227, cloth 76/127

## Self-diagnosis

- R1: meat slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask none (no sellers at home)
