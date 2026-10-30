# v2 shadow report

Turn 13670, 2026-10-30 23:38. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 518, prestige 3,221 (101 free, -0.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 5 | 0 | 19 | 0 | 0 | min_holding 60, sell 1, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 0 | 0 | 0 | 0 | 0 | none |
| firewood | 13 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 0 | 0 | 0 | 0 | 0 | none |
| garments | 19 | 0 | 2 | 0 | 0 | min_holding 30, sell 10, sell @ 20 |
| grain | 32 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 0 | 4 | 487 | 0 | 17 | buy @ 2.2 |
| meat | 0 | 0 | 0 | 0 | 0 | none |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.3 turns (holds 1, next step uses 4/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.20 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.2 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 56
- **flax plants**: flax plants buffer thin: 1.1 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 145
- **tar**: home ask 11.20 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 487, not 587

## Prestige spending, cheapest coin per prestige first

731 turns left: prestige gained now converts 97.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.7 | 47.7 | running |
| hold banquet 3 (pies) | mansion | 8 | 48.0 | 48.0 | thin at home: hop beer, pies, candles |
| hold banquet 2 (pies) | mansion | 7 | 50.1 | 50.1 | thin at home: wine, pies, candles |
| hold banquet 4 (pies) | mansion | 18 | 50.3 | 50.3 | thin at home: hop beer, wine, pies, candles |
| hold banquet 3 (fish) | mansion | 7.6 | 51.2 | 51.2 | thin at home: hop beer |
| hold banquet 3 (meat) | mansion | 7.6 | 52.0 | 52.0 | thin at home: hop beer |
| hold banquet 2 (fish) | mansion | 6.8 | 52.7 | 52.7 | thin at home: wine |
| jousting 3 | arena | 230 | 52.9 | 53.0 | needs a arena (build cost 24,967); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 53.6 | 53.6 | thin at home: wine |
| hold banquet 4 | mansion | 17.5 | 53.9 | 53.9 | thin at home: wine, hop beer, stockfish, candles |
| hold banquet 1 (fish) | mansion | 4.2 | 54.2 | 54.2 |  |
| hold banquet 4 (premium) | mansion | 20 | 55.4 | 55.4 | thin at home: hop beer, wine, stockfish, candles, premium cheese |

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
| arms | 1 @ 29.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had None) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 6) |
| cured meat | 6 @ 29.0, stop 24 |  | goal planner: buys 6 a turn for today's rates, keeps up to 24 (v2 had 9) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 6) |
| furniture | 2 @ 12.2, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 0 @ 2.2, stop - |  | goal planner: buys 0 for today's rates (v2 had 0) |
| light armour | 1 @ 88, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| thread |  | 44 @ min 3.96 | goal planner: sells 44 a turn at 3.96, keeps 189 (no one offered it) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 171 |

## Goal: business value (live: rates, buys, sells, ships)
- Value now 8.0k (cash + stock at home prices); +31/turn over 6 turns, -45/turn over 24 turns.
- Limits: cash flow >= +145/turn, prestige >= +8.30/turn (values are after 200 tax a turn).
- Today's settings: value +10/turn, cash +37/turn, prestige -0.61/turn - breaks the prestige floor and cash floor.
- Plan: value +26/turn, cash +66/turn, prestige -0.61/turn - could not meet the prestige floor and cash floor.
- Cash check (real vs predicted cash a tick, last 3): +43 vs -51, -16 vs -53, +95 vs +38.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - net maker 0.00 -> 0.32: +13/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.28: -18/turn
  - ropewalk 1 0.25 -> 0.00: +18/turn
- Model check over the last 59 turns: predicted -42/turn for the settings we ran, real -82/turn.
- Worth of one more unit per turn: labour 159.28, thread 399.96, cloth 638.89, flax fibres 473.62, garments 1848.79, nets 2813.70, beer 278.08, timber 679.93, prestige 10000.00, cash 100.00
- Orders it would set: arms buy 1 (v2 None); bread buy 5 (v2 6); cured meat buy 6 (v2 9); firewood buy 4 (v2 6); fish buy 0 (v2 None); furniture buy 2 (v2 None); grain buy 9 (v2 11); light armour buy 1 (v2 None); meat buy 0 (v2 None); thread sell 44 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.28, worth +14/turn.
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +82/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
- Trim: donate weavery 1: +12/turn (tax 18 saved).

## Chain sizing

Mode HOLD, garments sold 0.0/turn (+0.0 exported); plan makes 2.1 garments a turn.
Labour: own 500, everything else 375, chain may buy 0 -> chain allowance 125, chain plan 125 (-95 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 2.51 |
| ret | 3 | 0.91 | 0.50 |
| spin | 4 | 1.65 | 0.88 |
| weave | 3 | 0.08 | 0.09 |
| sew | 2 | 0.05 | 0.05 |

Buffers: flax fibres 35/37, thread 225/108, cloth 1/9
- chain plan needed 511 labour, budget left 125: cut to 125 (sewing capped at 0.05)

## Self-diagnosis

- R1: beer slot dry: 4.6 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy none, home ask 3.34 (held back: failsafe level 3: reduce-only, would buy 7 @ 3.4 (ask 3.34, cap 14.4))
- R1: candles slot dry: 0.0 held, 1.5 a turn (luxury slot (+3 prestige)); our buy 1 @ 76, home ask none (no sellers at home)
- R1: donations slot dry: 0.0 held, 40.0 a turn (luxury slot (+1 prestige)); our buy none, home ask 1.0 (held back: failsafe level 3: reduce-only, would buy 25 @ 1.02 (ask 1.0, cap 1.5))
- R1: fish slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask 1.67 (held back: failsafe level 3: reduce-only, would buy 14 @ 1.7 (ask 1.67, cap 2.6))
- R1: meat slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask 1.8 (held back: failsafe level 3: reduce-only, would buy 14 @ 1.83 (ask 1.8, cap 2.6))
