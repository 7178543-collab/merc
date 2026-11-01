# v2 shadow report

Turn 13707, 2026-11-01 12:18. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 6,530, prestige 3,114 (-6 free, -1.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 62 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.18 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 0 | 0 | 0 | 0 | 0 | none |
| firewood | 15 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 0 | 0 | 0 | 0 | 0 | none |
| garments | 9 | 0 | 2 | 0 | 0 | min_holding 8, sell 11, sell @ 19.6 |
| grain | 27 | 9 | 9 | 0 | 0 | stop 36, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 525 | 0 | 4 | buy 29, buy @ 2.2 |
| meat | 0 | 0 | 0 | 0 | 0 | none |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**1 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it

## Tuning

- **cloth**: cloth buffer thin: 1.6 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 48
- **flax plants**: flax plants buffer thin: 1.9 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 145

## Notes

- labour: projection runs 100 over real use lately; planning 525, not 625

## Prestige spending, cheapest coin per prestige first

694 turns left: prestige gained now converts 96.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 2 (pies) | mansion | 7 | 46.8 | 46.8 | thin at home: pasties, pies |
| maintain 1 | park | 0.5 | 47.4 | 47.4 | running |
| hold banquet 3 (pies) | mansion | 8 | 49.6 | 49.6 | thin at home: pasties, hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 50.3 | 50.3 | thin at home: hop beer, ham, pies |
| hold banquet 2 (fish) | mansion | 6.8 | 52.4 | 52.4 | thin at home: cured fish |
| jousting 3 | arena | 230 | 52.6 | 52.8 | needs a arena (build cost 23,951); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 53.4 | 53.4 |  |
| hold banquet 4 | mansion | 17.5 | 54.3 | 54.3 | thin at home: hop beer, ham, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 54.3 | 54.3 | thin at home: hop beer, ham, stockfish, premium cheese, premium ham |
| hold banquet 1 (fish) | mansion | 4.2 | 54.4 | 54.4 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 55.5 | 55.5 | thin at home: hop beer, cured fish |
| hold banquet 1 (meat) | mansion | 4.2 | 56.2 | 56.2 |  |

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
| arms | 1 @ 27.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 16 @ min 3.18 | goal planner: sells 16 at 3.18 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 76.0, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had 2) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| furniture | 2 @ 14.7, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.6 | goal planner: sells 11 at 19.6 (v2 had 10 at 20.0) |
| grain | 9 @ 3.7, stop 36 |  | goal planner: buys 9 a turn for today's rates, keeps up to 36 (v2 had 14) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 25) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 80.5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| thread |  | 20 @ min 3.96 | goal planner: sells 20 a turn at 3.96, keeps 189 (no one offered it) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 14.2k (cash + stock at home prices); +174/turn over 6 turns, +113/turn over 24 turns.
- Limits: cash flow >= -105/turn, prestige >= +12.74/turn (values are after 200 tax a turn).
- Today's settings: value +159/turn, cash +160/turn, prestige -1.28/turn - breaks the prestige floor.
- Plan: value -59/turn, cash -57/turn, prestige +2.92/turn - could not meet the prestige floor.
- Cash check (real vs predicted cash a tick, last 3): +162 vs +154, +78 vs +156, +192 vs +165.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - net maker 0.00 -> 0.29: +4/turn
  - ropewalk 1 0.25 -> 0.31: +2/turn
  - flax farm 1 4.64 -> 4.57: +1/turn
  - sewing shop 1 0.30 -> 0.37: -3/turn
  - weavery 1 0.50 -> 0.60: +10/turn
  - brewery 1 0.14 -> 0.28: -16/turn
  - mansion 1 0.00 -> 1.00: -216/turn
- Model check over the last 59 turns: predicted +95/turn for the settings we ran, real +91/turn.
- Worth of one more unit per turn: labour 1.58, thread 3.97, cloth 6.34, flax fibres 4.70, garments 18.34, nets 28.42, beer 2.75, timber 2.97, prestige 10000.00, cash 0.00
- Orders it would set: beer sell 16 (v2 15); firewood buy 4 (v2 5); fish buy 0 (v2 None); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 14); labour buy 29 (v2 25); light armour buy 1 (v2 None); meat buy 0 (v2 None); rope sell 2 (v2 1)
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +79/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

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

Buffers: flax fibres 27/78, thread 189/230, cloth 38/130
- chain plan needed 511 labour, budget left 510: cut to 510 (sewing capped at 0.81)

## Self-diagnosis

- R1: donations slot dry: 0.0 held, 40.0 a turn (luxury slot (+1 prestige)); our buy none, home ask 1.0 (held back: failsafe level 1: reduce-only, would buy 80 @ 1.02 (ask 1.0, cap 1.5))
- R1: fish slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask 1.79 (held back: failsafe level 1: reduce-only, would buy 14 @ 1.82 (ask 1.79, cap 2.6))
- R1: meat slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask 2.02 (held back: failsafe level 1: reduce-only, would buy 14 @ 2.06 (ask 2.02, cap 2.6))
