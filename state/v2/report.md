# v2 shadow report

Turn 13719, 2026-11-02 00:56. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 5,167, prestige 3,139 (19 free, +4.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 19 | 0 | 0 | min_holding 60, sell 15, sell @ 3.18 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 15 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 8 | 0 | 2 | 0 | 0 | min_holding 8, sell 11, sell @ 19.6 |
| grain | 27 | 9 | 9 | 0 | 0 | stop 36, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 560 | 0 | 4 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | buy 7, buy @ 1.91 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**1 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it

## Tuning

- **bread**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 560, not 660

## Prestige spending, cheapest coin per prestige first

682 turns left: prestige gained now converts 96.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 46.2 | 46.2 | running |
| hold banquet 2 (pies) | mansion | 7 | 46.9 | 46.9 | thin at home: cheese, pies |
| hold banquet 4 (pies) | mansion | 18 | 50.1 | 50.1 | thin at home: hop beer, cheese, pies |
| hold banquet 3 (pies) | mansion | 8 | 50.5 | 50.5 | thin at home: hop beer, cheese, pies |
| jousting 3 | arena | 230 | 52.6 | 52.8 | needs a arena (build cost 24,529); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 54.0 | 54.0 | thin at home: hop beer, stockfish, premium cheese, premium ham |
| hold banquet 4 | mansion | 17.5 | 54.4 | 54.4 | thin at home: hop beer, stockfish, cheese |
| hold sermon 2 (candles) | church | 31 | 51.2 | 54.8 | needs a church (build cost 65,629); thin at home: furniture |
| hold prayer 2 | chapel | 13 | 52.3 | 56.3 | needs a chapel (build cost 31,735); thin at home: furniture |
| hold banquet 1 (fish) | mansion | 4.2 | 56.4 | 56.4 | thin at home: cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 57.0 | 57.0 | thin at home: cured fish, cheese |
| hold sermon 2 | church | 24 | 53.0 | 57.7 | needs a church (build cost 65,629); thin at home: furniture |

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
| arms | 1 @ 26.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 73.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cured meat | 6 @ 29.0, stop 24 |  | goal planner: buys 6 a turn for today's rates, keeps up to 24 (v2 had 11) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 15, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.6 | goal planner: sells 11 at 19.6 (v2 had 10 at 20.0) |
| grain | 9 @ 3.7, stop 36 |  | goal planner: buys 9 a turn for today's rates, keeps up to 36 (v2 had 14) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 60) |
| light armour | 1 @ 87.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.6) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 79.5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 14.3k (cash + stock at home prices); -153/turn over 6 turns, +95/turn over 24 turns.
- Limits: cash flow >= -49/turn, prestige >= +11.71/turn (values are after 200 tax a turn).
- Today's settings: value -142/turn, cash -130/turn, prestige +4.13/turn - breaks the prestige floor and cash floor.
- Plan: value -121/turn, cash -97/turn, prestige +4.13/turn - could not meet the prestige floor and cash floor.
- Cash check (real vs predicted cash a tick, last 3): -198 vs -117, -110 vs -122, -118 vs -127.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - brewery 1 0.14 -> 0.24: +7/turn
  - net maker 0.00 -> 0.28: +3/turn
  - sewing shop 1 0.30 -> 0.36: +2/turn
  - weavery 1 0.50 -> 0.58: +5/turn
  - spinnery 1 1.65 -> 1.90: -4/turn
  - retting pit 1 0.91 -> 1.07: -2/turn
  - flax farm 1 4.64 -> 5.38: +10/turn
- Model check over the last 58 turns: predicted +99/turn for the settings we ran, real +113/turn.
- Worth of one more unit per turn: labour 155.54, thread 390.55, cloth 623.86, flax fibres 462.46, garments 1805.31, nets 2817.09, beer 269.90, timber 3.33, prestige 10000.00, cash 100.00
- Orders it would set: candles buy 2 (v2 None); cured meat buy 6 (v2 11); firewood buy 4 (v2 5); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 14); labour buy 64 (v2 60); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +81/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new chandlery (make tallow candles 2) for ~4313 coin: +7/turn, payback 647 turns, doesn't pay yet (materials thin at home: nails)

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 30.3 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 475 (+186 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 6.17 |
| ret | 3 | 0.91 | 1.23 |
| spin | 4 | 1.65 | 2.18 |
| weave | 3 | 0.50 | 1.18 |
| sew | 2 | 0.30 | 0.74 |

Buffers: flax fibres 27/74, thread 197/218, cloth 50/118
- chain plan needed 511 labour, budget left 475: cut to 475 (sewing capped at 0.74)

## Self-diagnosis

- R1: meat slot dry: 1.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy 7 @ 1.91, home ask none (no sellers at home)
