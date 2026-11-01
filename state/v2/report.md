# v2 shadow report

Turn 13711, 2026-11-01 16:19. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 6,949, prestige 3,110 (-10 free, -0.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 6 | 0 | 0 | min_holding 60, sell 16, sell @ 3.18 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 0 | 0 | 0 | 0 | 0 | none |
| firewood | 14 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 0 | 0 | 0 | 0 | 0 | none |
| garments | 9 | 0 | 2 | 0 | 0 | min_holding 8, sell 11, sell @ 19.6 |
| grain | 27 | 9 | 9 | 0 | 0 | stop 36, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 529 | 0 | 0 | buy 29, buy @ 2.2 |
| meat | 0 | 0 | 0 | 0 | 0 | none |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (6 @ 29), home ask 22.60 x12, yet 0 bought last turn); labour need rises ~35/turn when they restart -> v2: find out why the buy isn't filling
- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **labour**: buying 29, short of ~60 needed -> v2: buy 60

## Tuning

- **cloth**: cloth buffer thin: 1.8 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 48
- **flax plants**: flax plants buffer thin: 2.0 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 145

## Notes

- labour: projection runs 100 over real use lately; planning 560, not 660

## Prestige spending, cheapest coin per prestige first

690 turns left: prestige gained now converts 96.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 45.3 | 45.3 | running |
| hold banquet 2 (pies) | mansion | 7 | 46.4 | 46.4 | thin at home: pies |
| hold banquet 3 (pies) | mansion | 8 | 50.1 | 50.1 | thin at home: hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 50.6 | 50.6 | thin at home: hop beer, pies |
| jousting 3 | arena | 230 | 52.5 | 52.7 | needs a arena (build cost 24,960); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 53.0 | 53.0 | thin at home: cured fish |
| hold banquet 2 (meat) | mansion | 6.8 | 53.7 | 53.7 |  |
| hold banquet 4 (premium) | mansion | 20 | 54.5 | 54.5 | thin at home: hop beer, stockfish, premium cheese, premium ham |
| hold banquet 4 | mansion | 17.5 | 54.6 | 54.6 | thin at home: hop beer, stockfish |
| hold banquet 1 (fish) | mansion | 4.2 | 54.9 | 54.9 | thin at home: cured fish |
| hold banquet 1 (meat) | mansion | 4.2 | 56.4 | 56.4 | running |
| hold feast 2 | townhouse | 2.6 | 53.0 | 56.6 | needs a townhouse (build cost 6,372) |

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
| arms | 1 @ 26.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 15 @ min 3.18 | goal planner: sells 15 at 3.18 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 72, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cured meat | 7 @ 29.0, stop 25 | off | goal planner: buys 7 a turn for today's rates, keeps up to 25 (v2 had 12) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| furniture | 2 @ 15, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.6 | goal planner: sells 11 at 19.6 (v2 had 10 at 20.0) |
| grain | 9 @ 3.7, stop 36 |  | goal planner: buys 9 a turn for today's rates, keeps up to 36 (v2 had 14) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 60) |
| light armour | 1 @ 94, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.6) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 79.5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 1 = 3.0 turns |
| thread |  | 20 @ min 3.96 | goal planner: sells 20 a turn at 3.96, keeps 189 (no one offered it) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 15.0k (cash + stock at home prices); +232/turn over 6 turns, +192/turn over 24 turns.
- Limits: cash flow >= -123/turn, prestige >= +12.94/turn (values are after 200 tax a turn).
- Today's settings: value -70/turn, cash -73/turn, prestige +2.95/turn - breaks the prestige floor.
- Plan: value -40/turn, cash -39/turn, prestige +2.95/turn - could not meet the prestige floor.
- Cash check (real vs predicted cash a tick, last 3): +192 vs +165, +168 vs +160, +166 vs +164.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - brewery 1 0.14 -> 0.28: +11/turn
  - net maker 0.00 -> 0.29: +4/turn
  - sewing shop 1 0.30 -> 0.37: +3/turn
  - weavery 1 0.50 -> 0.59: +5/turn
  - spinnery 1 1.65 -> 1.99: -8/turn
  - retting pit 1 0.91 -> 1.13: -6/turn
  - flax farm 1 4.64 -> 5.65: +11/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.35: -17/turn
  - ropewalk 1 0.25 -> 0.00: +26/turn
- Model check over the last 59 turns: predicted +110/turn for the settings we ran, real +113/turn.
- Worth of one more unit per turn: labour 1.51, thread 3.79, cloth 6.06, flax fibres 4.49, garments 17.53, nets 27.28, beer 2.65, timber 2.97, prestige 10000.00, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cured meat buy 7 (v2 12); firewood buy 4 (v2 5); fish buy 0 (v2 None); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 14); labour buy 64 (v2 60); light armour buy 1 (v2 None); meat buy 0 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.35, worth +18/turn.
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +75/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

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

Buffers: flax fibres 27/74, thread 190/218, cloth 42/118
- chain plan needed 511 labour, budget left 475: cut to 475 (sewing capped at 0.74)

## Self-diagnosis

- R1: cured meat slot dry: 6.0 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 7 @ 29, home ask 22.6; our bid is already at/over the ask (sellers too thin)
- R1: donations slot dry: 0.0 held, 40.0 a turn (luxury slot (+1 prestige)); our buy none, home ask 1.0 (held back: failsafe level 1: reduce-only, would buy 80 @ 1.02 (ask 1.0, cap 1.5))
- R1: fish slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask 1.73 (held back: failsafe level 1: reduce-only, would buy 14 @ 1.76 (ask 1.73, cap 2.6))
- R1: meat slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask 1.88 (held back: failsafe level 1: reduce-only, would buy 14 @ 1.91 (ask 1.88, cap 2.6))
