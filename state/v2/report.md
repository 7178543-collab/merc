# v2 shadow report

Turn 13625, 2026-10-29 02:39. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 1,339, prestige 3,292 (172 free, -2.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 6 | 0 | 15 | 0 | 0 | min_holding 60, sell 3, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 0 | 0 | 0 | 0 | 0 | none |
| firewood | 4 | 3 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 0 | 0 | 0 | 0 | 0 | none |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 2, sell @ 17.9 |
| grain | 14 | 0 | 8 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 4 | 4 | 504 | 15 | 0 | buy 16, buy @ 2.2 |
| meat | 0 | 0 | 0 | 0 | 0 | none |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34.2 |
| porterage | 6 | 6 | 5 | 0 | 1 | buy 6, buy @ 1.1 |

**3 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 0.9 turns (holds 30, next step uses 32/turn) -> v2: check the step that makes it
- **flax plants**: flax plants buffer 1.0 turns (holds 80, next step uses 80/turn) -> v2: check the step that makes it
- **labour**: buying 16, short of ~19 needed -> v2: buy 19

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 519, not 608

## Prestige spending, cheapest coin per prestige first

776 turns left: prestige gained now converts 98.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.7 | 47.7 | running |
| hold banquet 3 (pies) | mansion | 8 | 48.6 | 48.6 | thin at home: hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 48.6 | 48.6 | thin at home: hop beer, wine, stockfish, pies |
| hold banquet 2 (pies) | mansion | 7 | 50.1 | 50.1 | thin at home: wine, pies |
| hold banquet 4 | mansion | 17.5 | 51.9 | 51.9 | thin at home: wine, hop beer, ham, stockfish |
| hold banquet 3 (fish) | mansion | 7.6 | 52.5 | 52.5 | thin at home: hop beer, cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 52.9 | 52.9 | thin at home: wine, cured fish |
| hold banquet 4 (premium) | mansion | 20 | 53.6 | 53.6 | thin at home: hop beer, wine, stockfish, premium cheese |
| jousting 3 | arena | 230 | 53.6 | 53.7 | needs a arena (build cost 25,162); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 3 (meat) | mansion | 7.6 | 53.8 | 53.8 | thin at home: hop beer |
| hold banquet 1 (fish) | mansion | 4.2 | 54.1 | 54.1 | thin at home: cured fish |
| hold banquet 2 (meat) | mansion | 6.8 | 54.4 | 54.4 | thin at home: wine |

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
| arms | 1 @ 31.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| candles | 1 @ 76.0, stop 61 |  | goal planner: buys 1 a turn for today's rates, keeps up to 61 (v2 had 2) |
| cured meat | 6 @ 29.0, stop 23 |  | goal planner: buys 6 a turn for today's rates, keeps up to 23 (v2 had 7) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| furniture | 2 @ 13.9, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 2 @ min 17.9 | goal planner: sells 2 at 17.9 (v2 had 2 at 20.6) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 17) |
| labour | 16 @ 2.2, stop - |  | goal planner: buys 16 for today's rates (v2 had 19) |
| light armour | 1 @ 94.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| nets |  | 9 @ min 34.2 | goal planner: sells 9 at 34.2 (v2 had 9 at 35.8) |
| pasties | 1 @ 14.5, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 2) |
| porterage | 6 @ 1.1, stop - |  | goal planner: buys 6 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 74.5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| thread |  | 55 @ min 3.96 | goal planner: sells 55 a turn at 3.96, keeps 172 (no one offered it) |
| timber |  | 6 @ min 6.25 | goal planner: sells 6 a turn at 6.25, keeps 100 (no one offered it) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 200 |

## Goal: business value (live: rates, buys, sells, ships, invest)
- Value now 10.4k (cash + stock at home prices); -272/turn over 6 turns, -196/turn over 24 turns.
- Limits: cash flow >= +111/turn, prestige >= +5.32/turn (values are after 200 tax a turn).
- Today's settings: value -57/turn, cash -2/turn, prestige -1.77/turn - breaks the prestige floor and cash floor.
- Plan: value -33/turn, cash +45/turn, prestige -1.77/turn - could not meet the prestige floor and cash floor.
- Cash check (real vs predicted cash a tick, last 3): +57 vs -13, -128 vs +14, +68 vs +20.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - weavery 1 0.00 -> 0.10: +10/turn
  - net maker 0.00 -> 0.28: +7/turn
  - spinnery 1 1.86 -> 1.62: -2/turn
  - retting pit 1 1.00 -> 0.93: +3/turn
  - flax farm 1 4.99 -> 4.67: +2/turn
- Model check over the last 59 turns: predicted +134/turn for the settings we ran, real -112/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 159.26, thread 399.96, cloth 638.85, flax fibres 473.73, garments 1848.61, nets 2832.88, beer 286.92, timber 6.71, prestige 10000.00, cash 100.00
- Orders it would set: candles buy 1 (v2 2); cured meat buy 6 (v2 7); firewood buy 4 (v2 8); fish buy 0 (v2 None); furniture buy 2 (v2 None); grain buy 9 (v2 17); labour buy 16 (v2 19); light armour buy 1 (v2 None); meat buy 0 (v2 None); pasties buy 1 (v2 2)
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +81/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
- Trim: donate weavery 1: +11/turn (tax 18 saved).

## Chain sizing

Mode HOLD, garments sold 1.8/turn (+0.0 exported); plan makes 1.6 garments a turn.
Labour: own 500, everything else 374, chain may buy 0 -> chain allowance 126, chain plan 126 (-116 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.99 | 2.62 |
| ret | 3 | 1.00 | 0.52 |
| spin | 4 | 1.86 | 0.93 |
| weave | 3 | 0.00 | 0.05 |
| sew | 2 | 0.09 | 0.04 |

Buffers: flax fibres 30/36, thread 181/106, cloth 16/7
- chain plan needed 675 labour, budget left 126: cut to 126 (sewing capped at 0.04)

## Self-diagnosis

- R1: beer slot dry: 6.3 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy none, home ask 3.4 (held back: failsafe level 3: reduce-only, would buy 19 @ 3.46 (ask 3.4, cap 14.4))
- R1: donations slot dry: 0.0 held, 40.0 a turn (luxury slot (+1 prestige)); our buy none, home ask 1.0 (held back: failsafe level 3: reduce-only, would buy 65 @ 1.02 (ask 1.0, cap 1.5))
- R1: fish slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask 1.76 (held back: failsafe level 3: reduce-only, would buy 14 @ 1.79 (ask 1.76, cap 2.6))
- R1: meat slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask 1.83 (held back: failsafe level 3: reduce-only, would buy 14 @ 1.86 (ask 1.83, cap 2.6))
