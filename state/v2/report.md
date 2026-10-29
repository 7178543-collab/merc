# v2 shadow report

Turn 13626, 2026-10-29 03:59. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 1,300, prestige 3,291 (171 free, -1.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 5 | 0 | 19 | 0 | 0 | min_holding 60, sell 3, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 0 | 0 | 0 | 0 | 0 | none |
| firewood | 4 | 3 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 0 | 0 | 0 | 0 | 0 | none |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 2, sell @ 17.9 |
| grain | 14 | 0 | 8 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 16 | 4 | 504 | 4 | 0 | buy 16, buy @ 2.2 |
| meat | 0 | 0 | 0 | 0 | 0 | none |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34.2 |
| porterage | 6 | 6 | 5 | 0 | 1 | buy 6, buy @ 1.1 |

**2 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 0.9 turns (holds 30, next step uses 32/turn) -> v2: check the step that makes it
- **flax plants**: flax plants buffer 1.0 turns (holds 80, next step uses 80/turn) -> v2: check the step that makes it

## Tuning

- **candles**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **cloth**: cloth buffer thin: 1.2 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 14
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 508, not 608

## Prestige spending, cheapest coin per prestige first

775 turns left: prestige gained now converts 97.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.4 | 47.4 | running |
| hold banquet 3 (pies) | mansion | 8 | 48.6 | 48.6 | thin at home: hop beer, pies, candles |
| hold banquet 2 (pies) | mansion | 7 | 50.3 | 50.3 | thin at home: wine, pies, candles |
| hold banquet 4 (pies) | mansion | 18 | 50.5 | 50.5 | thin at home: hop beer, wine, stockfish, candles |
| hold banquet 3 (fish) | mansion | 7.6 | 52.4 | 52.4 | thin at home: hop beer |
| hold banquet 2 (fish) | mansion | 6.8 | 53.0 | 53.0 | thin at home: wine |
| jousting 3 | arena | 230 | 53.8 | 53.9 | needs a arena (build cost 24,232); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 54.4 | 54.4 |  |
| hold banquet 4 | mansion | 17.5 | 54.4 | 54.4 | thin at home: wine, hop beer, ham, stockfish, candles |
| hold banquet 3 (meat) | mansion | 7.6 | 55.1 | 55.1 | thin at home: hop beer, cured meat |
| hold feast 2 | townhouse | 2.6 | 51.8 | 55.1 | needs a townhouse (build cost 6,548); thin at home: wine |
| hold sermon 2 (candles) | church | 31 | 52.4 | 55.3 | needs a church (build cost 61,403); thin at home: jewellery, candles, furniture |

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
| arms | 1 @ 30.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had None) |
| beer | 3 @ 3.74, stop 39 |  | uses 19.2/turn (household upkeep, mansion 1), makes 17.9, holds 5 = 3.9 turns |
| candles | 1 @ 76.0, stop 61 |  | goal planner: buys 1 a turn for today's rates, keeps up to 61 (v2 had 2) |
| cured meat | 6 @ 29.0, stop 23 |  | goal planner: buys 6 a turn for today's rates, keeps up to 23 (v2 had 7) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| furniture | 2 @ 14.4, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 2 @ min 17.9 | goal planner: sells 2 at 17.9 (v2 had 2 at 20.4) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 17) |
| labour | 16 @ 2.2, stop - |  | goal planner: buys 16 for today's rates (v2 had 8) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| nets |  | 9 @ min 34.2 | goal planner: sells 9 at 34.2 (v2 had 9 at 35.8) |
| pasties | 1 @ 14.5, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 2) |
| porterage | 6 @ 1.1, stop - |  | goal planner: buys 6 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 74.0) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 1 = 2.5 turns |
| thread |  | 54 @ min 3.96 | goal planner: sells 54 a turn at 3.96, keeps 172 (no one offered it) |
| timber |  | 7 @ min 6.25 | goal planner: sells 7 a turn at 6.25, keeps 100 (no one offered it) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 200 |

## Goal: business value (live: rates, buys, sells, ships, invest)
- Value now 10.4k (cash + stock at home prices); -271/turn over 6 turns, -184/turn over 24 turns.
- Limits: cash flow >= +112/turn, prestige >= +5.38/turn (values are after 200 tax a turn).
- Today's settings: value -61/turn, cash -5/turn, prestige -1.32/turn - breaks the prestige floor and cash floor.
- Plan: value -33/turn, cash +45/turn, prestige -1.32/turn - could not meet the prestige floor and cash floor.
- Cash check (real vs predicted cash a tick, last 3): -128 vs +14, +68 vs +20, -39 vs -2.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - weavery 1 0.00 -> 0.10: +12/turn
  - net maker 0.00 -> 0.28: +7/turn
  - spinnery 1 1.86 -> 1.60: -3/turn
  - retting pit 1 1.00 -> 0.92: +2/turn
  - flax farm 1 4.99 -> 4.61: +3/turn
  - ropewalk 1 0.25 -> 0.00: -16/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.27: +16/turn
- Model check over the last 58 turns: predicted +126/turn for the settings we ran, real -100/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 159.26, thread 399.96, cloth 638.85, flax fibres 473.73, garments 1848.61, nets 2820.99, beer 286.97, timber 5.89, prestige 10000.00, cash 100.00
- Orders it would set: arms buy 1 (v2 None); candles buy 1 (v2 2); cured meat buy 6 (v2 7); firewood buy 4 (v2 8); fish buy 0 (v2 None); furniture buy 2 (v2 None); grain buy 9 (v2 17); labour buy 16 (v2 8); light armour buy 1 (v2 None); meat buy 0 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.27, worth +10/turn.
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +80/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
- Trim: donate weavery 1: +11/turn (tax 18 saved).

## Chain sizing

Mode HOLD, garments sold 1.7/turn (+0.0 exported); plan makes 1.6 garments a turn.
Labour: own 500, everything else 374, chain may buy 0 -> chain allowance 126, chain plan 126 (-115 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.99 | 2.62 |
| ret | 3 | 1.00 | 0.52 |
| spin | 4 | 1.86 | 0.93 |
| weave | 3 | 0.00 | 0.06 |
| sew | 2 | 0.09 | 0.04 |

Buffers: flax fibres 30/36, thread 184/106, cloth 9/6
- chain plan needed 676 labour, budget left 126: cut to 126 (sewing capped at 0.04)

## Self-diagnosis

- R1: beer slot dry: 5.0 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy none, home ask 3.58 (held back: failsafe level 3: reduce-only, would buy 17 @ 3.64 (ask 3.58, cap 14.4))
- R1: donations slot dry: 0.0 held, 40.0 a turn (luxury slot (+1 prestige)); our buy none, home ask 1.0 (held back: failsafe level 3: reduce-only, would buy 63 @ 1.02 (ask 1.0, cap 1.5))
- R1: fish slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask 1.77 (held back: failsafe level 3: reduce-only, would buy 14 @ 1.8 (ask 1.77, cap 2.6))
- R1: meat slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask 1.82 (held back: failsafe level 3: reduce-only, would buy 14 @ 1.85 (ask 1.82, cap 2.6))
