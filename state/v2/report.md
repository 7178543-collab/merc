# v2 shadow report

Turn 13669, 2026-10-30 22:18. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 423, prestige 3,221 (101 free, -0.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 4 | 0 | 19 | 0 | 0 | min_holding 60, sell 1, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 0 | 0 | 0 | 0 | 0 | none |
| firewood | 13 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 0 | 0 | 0 | 0 | 0 | none |
| garments | 19 | 0 | 2 | 0 | 0 | min_holding 30, sell 10, sell @ 20 |
| grain | 32 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 4 | 50 | 494 | 0 | 56 | buy 4, buy @ 1.8 |
| meat | 0 | 0 | 0 | 0 | 0 | none |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**1 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.3 turns (holds 1, next step uses 4/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **labour**: 56 labour expired last turn (~90 coin): holding 4 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.3 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 56
- **flax plants**: flax plants buffer thin: 1.1 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 145

## Notes

- labour: projection runs 100 over real use lately; planning 494, not 587

## Prestige spending, cheapest coin per prestige first

732 turns left: prestige gained now converts 97.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.0 | 48.0 | running |
| hold banquet 3 (pies) | mansion | 8 | 48.2 | 48.2 | thin at home: hop beer, pies, candles |
| hold banquet 4 (pies) | mansion | 18 | 50.2 | 50.2 | thin at home: hop beer, pies, candles |
| hold banquet 2 (pies) | mansion | 7 | 50.3 | 50.3 | thin at home: pies, candles |
| hold banquet 3 (fish) | mansion | 7.6 | 51.6 | 51.6 | thin at home: hop beer |
| hold banquet 2 (fish) | mansion | 6.8 | 52.9 | 52.9 |  |
| jousting 3 | arena | 230 | 52.8 | 52.9 | needs a arena (build cost 23,931); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 3 (meat) | mansion | 7.6 | 53.7 | 53.7 | thin at home: hop beer, cured meat |
| hold banquet 4 | mansion | 17.5 | 53.9 | 53.9 | thin at home: hop beer, stockfish, candles |
| hold banquet 1 (fish) | mansion | 4.2 | 54.3 | 54.3 |  |
| hold sermon 2 (candles) | church | 31 | 51.7 | 54.7 | needs a church (build cost 61,149); thin at home: candles, furniture |
| hold banquet 2 (meat) | mansion | 6.8 | 55.3 | 55.3 | thin at home: cured meat |

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
| arms | 1 @ 26.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 6) |
| cured meat | 6 @ 29.0, stop 23 |  | goal planner: buys 6 a turn for today's rates, keeps up to 23 (v2 had 8) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 6) |
| furniture | 2 @ 12.2, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 0 @ 2.2, stop - |  | goal planner: buys 0 for today's rates (v2 had 0) |
| light armour | 1 @ 88.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 77.0) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 0 = 0.0 turns |
| thread |  | 43 @ min 3.96 | goal planner: sells 43 a turn at 3.96, keeps 189 (no one offered it) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 171 |

## Goal: business value (live: rates, buys, sells, ships)
- Value now 7.9k (cash + stock at home prices); +34/turn over 6 turns, -49/turn over 24 turns.
- Limits: cash flow >= +149/turn, prestige >= +8.28/turn (values are after 200 tax a turn).
- Today's settings: value +11/turn, cash +38/turn, prestige -0.61/turn - breaks the prestige floor and cash floor.
- Plan: value +28/turn, cash +74/turn, prestige -0.61/turn - could not meet the prestige floor and cash floor.
- Cash check (real vs predicted cash a tick, last 3): +37 vs -51, +43 vs -51, -16 vs -53.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - net maker 0.00 -> 0.44: +15/turn
  - spinnery 1 1.65 -> 1.60: +1/turn
  - flax farm 1 4.64 -> 4.53: -0/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.28: -15/turn
  - ropewalk 1 0.25 -> 0.00: +16/turn
- Model check over the last 59 turns: predicted -40/turn for the settings we ran, real -83/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 159.28, thread 399.96, cloth 638.89, flax fibres 473.62, garments 1848.79, nets 2828.60, beer 277.85, timber 654.93, prestige 10000.00, cash 100.00
- Orders it would set: bread buy 5 (v2 6); cured meat buy 6 (v2 8); firewood buy 4 (v2 6); fish buy 0 (v2 None); furniture buy 2 (v2 None); grain buy 9 (v2 11); light armour buy 1 (v2 None); meat buy 0 (v2 None); rope sell 2 (v2 1); thread sell 43 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.28, worth +11/turn.
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +80/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
- Trim: donate weavery 1: +13/turn (tax 18 saved).

## Chain sizing

Mode HOLD, garments sold 0.0/turn (+0.0 exported); plan makes 2.1 garments a turn.
Labour: own 500, everything else 375, chain may buy 0 -> chain allowance 125, chain plan 125 (-94 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 2.53 |
| ret | 3 | 0.91 | 0.51 |
| spin | 4 | 1.65 | 0.89 |
| weave | 3 | 0.08 | 0.08 |
| sew | 2 | 0.05 | 0.05 |

Buffers: flax fibres 36/36, thread 214/107, cloth 1/8
- chain plan needed 511 labour, budget left 125: cut to 125 (sewing capped at 0.05)

## Self-diagnosis

- R1: beer slot dry: 4.4 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy none, home ask 3.34 (held back: failsafe level 3: reduce-only, would buy 6 @ 3.4 (ask 3.34, cap 14.4))
- R1: candles slot dry: 0.0 held, 1.5 a turn (luxury slot (+3 prestige)); our buy 1 @ 76, home ask none (no sellers at home)
- R1: donations slot dry: 0.0 held, 40.0 a turn (luxury slot (+1 prestige)); our buy none, home ask 1.0 (held back: failsafe level 3: reduce-only, would buy 20 @ 1.02 (ask 1.0, cap 1.5))
- R1: fish slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask 1.67 (held back: failsafe level 3: reduce-only, would buy 12 @ 1.7 (ask 1.67, cap 2.6))
- R1: meat slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask 1.8 (held back: failsafe level 3: reduce-only, would buy 11 @ 1.83 (ask 1.8, cap 2.6))
