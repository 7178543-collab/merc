# v2 shadow report

Turn 13721, 2026-11-02 02:09. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 4,915, prestige 3,143 (23 free, -0.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 15, sell @ 3.18 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 14 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 9 | 0 | 2 | 0 | 0 | min_holding 8, sell 11, sell @ 19.6 |
| grain | 27 | 9 | 9 | 0 | 0 | stop 36, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 525 | 0 | 39 | buy 64, buy @ 2.2 |
| meat | 0 | 0 | 0 | 0 | 0 | buy 7, buy @ 1.91 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**1 risks, 1 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **labour**: 39 labour expired last turn (~60 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Notes

- labour: projection runs 100 over real use lately; planning 525, not 625

## Prestige spending, cheapest coin per prestige first

680 turns left: prestige gained now converts 96.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 46.5 | 46.5 | running |
| hold banquet 2 (pies) | mansion | 7 | 48.3 | 48.3 | thin at home: cheese, pies |
| hold banquet 4 (pies) | mansion | 18 | 51.0 | 51.0 | thin at home: hop beer, cheese, pies |
| hold banquet 3 (pies) | mansion | 8 | 51.7 | 51.7 | thin at home: hop beer, cheese, pies |
| jousting 3 | arena | 230 | 52.6 | 52.8 | needs a arena (build cost 23,809); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 54.7 | 54.7 | thin at home: hop beer, stockfish, premium cheese, premium ham |
| hold banquet 1 (fish) | mansion | 4.2 | 55.2 | 55.2 |  |
| hold banquet 4 | mansion | 17.5 | 55.4 | 55.4 | thin at home: hop beer, ham, stockfish, cheese |
| hold banquet 2 (fish) | mansion | 6.8 | 56.0 | 56.0 | thin at home: cured fish, cheese |
| hold feast 2 | townhouse | 2.6 | 53.5 | 57.1 | needs a townhouse (build cost 6,276); thin at home: wine |
| hold sermon 2 (candles) | church | 31 | 54.3 | 57.8 | needs a church (build cost 64,292); thin at home: candles, furniture |
| jousting 2 | arena | 210 | 57.7 | 57.8 | needs a arena (build cost 23,809); thin at home: swords, protection, coats, plate armour; needs weaponry skill |

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
| arms | 1 @ 26.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 15 @ min 3.08 | goal planner: sells 15 at 3.08 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 76.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 15, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.6 | goal planner: sells 11 at 19.6 (v2 had 10 at 21.4) |
| grain | 9 @ 3.7, stop 36 |  | goal planner: buys 9 a turn for today's rates, keeps up to 36 (v2 had 14) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 25) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.6) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 81.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 14.5k (cash + stock at home prices); -99/turn over 6 turns, +92/turn over 24 turns.
- Limits: cash flow >= -38/turn, prestige >= +11.55/turn (values are after 200 tax a turn).
- Today's settings: value +106/turn, cash +100/turn, prestige -0.11/turn - breaks the prestige floor.
- Plan: value -115/turn, cash -55/turn, prestige +4.09/turn - could not meet the prestige floor and cash floor.
- Cash check (real vs predicted cash a tick, last 3): -198 vs -117, -110 vs -122, -118 vs -127.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - net maker 0.00 -> 0.28: +4/turn
  - sewing shop 1 0.30 -> 0.36: +2/turn
  - weavery 1 0.50 -> 0.58: +5/turn
  - flax farm 1 4.64 -> 5.39: -6/turn
  - retting pit 1 0.91 -> 1.08: +0/turn
  - spinnery 1 1.65 -> 1.90: +9/turn
  - brewery 1 0.14 -> 0.24: -17/turn
  - mansion 1 0.00 -> 1.00: -217/turn
- Model check over the last 59 turns: predicted +94/turn for the settings we ran, real +115/turn.
- Worth of one more unit per turn: labour 156.55, thread 393.07, cloth 627.90, flax fibres 465.42, garments 1817.00, nets 2830.69, beer 279.15, timber 2.86, prestige 10000.00, cash 100.00
- Orders it would set: candles buy 2 (v2 None); firewood buy 4 (v2 5); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 14); labour buy 29 (v2 25); light armour buy 1 (v2 None); meat buy 0 (v2 None); rope sell 2 (v2 1)
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +82/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new chandlery (make tallow candles 2) for ~4026 coin: +12/turn, payback 341 turns, doesn't pay yet (materials thin at home: nails)

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 33.2 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 510 (+221 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 6.50 |
| ret | 3 | 0.91 | 1.30 |
| spin | 4 | 1.65 | 2.30 |
| weave | 3 | 0.50 | 1.30 |
| sew | 2 | 0.30 | 0.81 |

Buffers: flax fibres 27/78, thread 192/230, cloth 52/130
- chain plan needed 511 labour, budget left 510: cut to 510 (sewing capped at 0.81)

## Self-diagnosis

- R1: meat slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask none (no sellers at home)
- R1: prestige rate -0.11 a turn vs 12-turn median +4.14; likely: dry slot: meat
