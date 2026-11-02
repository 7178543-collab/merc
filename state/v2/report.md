# v2 shadow report

Turn 13742, 2026-11-02 23:05. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 6,220, prestige 3,141 (21 free, -0.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.08 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 13 | 4 | 4 | 0 | 0 | stop 14, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 70 | 0 | 2 | 0 | 0 | min_holding 80, sell 11, sell @ 19.4 |
| grain | 35 | 9 | 9 | 0 | 0 | stop 36, buy 11, buy @ 3.7 |
| labour | 29 | 29 | 525 | 0 | 4 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 14, buy @ 1.97 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**1 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **meat**: buying 14, need ~1 -> v2: buy 1

## Tuning

- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 525, not 625

## Prestige spending, cheapest coin per prestige first

659 turns left: prestige gained now converts 96.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.1 | 47.1 | running |
| hold banquet 4 (pies) | mansion | 18 | 51.4 | 51.4 | thin at home: hop beer, stockfish, cheese, pies |
| jousting 3 | arena | 230 | 53.3 | 53.5 | needs a arena (build cost 24,811); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 53.6 | 53.6 | thin at home: hop beer, stockfish, premium cheese |
| hold banquet 4 | mansion | 17.5 | 54.8 | 54.8 | thin at home: hop beer, ham, stockfish, cheese |
| hold banquet 2 (pies) | mansion | 7 | 54.9 | 54.9 | thin at home: cheese, pies |
| hold banquet 3 (pies) | mansion | 8 | 55.1 | 55.1 | thin at home: hop beer, cheese, pies |
| hold prayer 2 | chapel | 13 | 51.6 | 55.6 | needs a chapel (build cost 30,751); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 52.9 | 56.5 | needs a church (build cost 64,972); thin at home: candles, furniture |
| hold sermon 2 | church | 24 | 52.5 | 57.2 | needs a church (build cost 64,972); thin at home: furniture |
| hold banquet 1 (fish) | mansion | 4.2 | 58.3 | 58.3 |  |
| hold banquet 1 (meat) | mansion | 4.2 | 58.4 | 58.4 |  |

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
| arms | 1 @ 33.6, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 4.0 turns |
| beer |  | 16 @ min 3.08 | goal planner: sells 16 at 3.08 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 16 = 3.9 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 6) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 19.4 | goal planner: sells 11 at 19.4 (v2 had 10 at 20.0) |
| grain | 10 @ 3.7, stop 36 |  | uses 9.0/turn (brewery 1), makes 0.0, holds 35 = 3.9 turns |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 25) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.6) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 75.5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 1 = 3.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 17.7k (cash + stock at home prices); +119/turn over 6 turns, +127/turn over 24 turns.
- Limits: cash flow >= -92/turn, prestige >= +11.64/turn (values are after 200 tax a turn).
- Today's settings: value +81/turn, cash +87/turn, prestige -0.10/turn - breaks the prestige floor.
- Plan: value -149/turn, cash -108/turn, prestige +4.10/turn - could not meet the prestige floor and cash floor.
- Cash check (real vs predicted cash a tick, last 3): -120 vs +105, -77 vs +96, -58 vs +95 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - net maker 0.00 -> 0.28: +3/turn
  - retting pit 1 0.91 -> 0.80: -6/turn
  - flax farm 1 4.64 -> 3.99: +6/turn
  - spinnery 1 1.65 -> 1.41: +1/turn
  - brewery 1 [brew beer 2] 0.00 -> 0.16: -18/turn
  - brewery 1 0.14 -> 0.00: +23/turn
  - mansion 1 0.00 -> 1.00: -242/turn
- Model check over the last 59 turns: predicted +94/turn for the settings we ran, real +111/turn.
- Worth of one more unit per turn: labour 161.60, thread 410.21, cloth 652.61, flax fibres 493.55, garments 1884.31, nets 2946.64, beer 311.08, timber 3.08, prestige 10000.00, cash 100.00
- Orders it would set: beer sell 16 (v2 15); candles buy 2 (v2 None); firewood buy 4 (v2 6); furniture buy 2 (v2 None); garments sell 11 (v2 10); labour buy 29 (v2 25); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Recipe: brewery 1 brew beer 1 -> brew beer 2 at 0.16, worth +19/turn.
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new chandlery (make tallow candles 1) for ~4107 coin: +28/turn, payback 147 turns, doesn't pay yet (materials thin at home: nails)

## Chain sizing

Mode HOLD, garments sold 6.8/turn (+0.0 exported); plan makes 33.2 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 510 (+221 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 6.50 |
| ret | 3 | 0.91 | 1.30 |
| spin | 4 | 1.65 | 2.30 |
| weave | 3 | 0.50 | 1.30 |
| sew | 2 | 0.30 | 0.81 |

Buffers: flax fibres 27/78, thread 189/230, cloth 73/130
- chain plan needed 557 labour, budget left 510: cut to 510 (sewing capped at 0.81)

## Self-diagnosis

- R1: meat slot dry: 1.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy 14 @ 1.97, home ask none (no sellers at home)
