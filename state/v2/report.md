# v2 shadow report

Turn 13623, 2026-10-29 00:43. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 1,149, prestige 3,297 (177 free, +73.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 3 | 0 | 18 | 0 | 0 | min_holding 60, sell 3, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 0 | 0 | 0 | 0 | 0 | none |
| firewood | 6 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 0 | 0 | 0 | 0 | 0 | none |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 2, sell @ 17.9 |
| grain | 30 | 8 | 8 | 0 | 0 | stop 32, buy 8, buy @ 3.7 |
| labour | 27 | 27 | 519 | 0 | 8 | buy 27, buy @ 2.2 |
| meat | 0 | 0 | 0 | 0 | 0 | none |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34.2 |
| porterage | 6 | 6 | 5 | 0 | 1 | buy 6, buy @ 1.1 |

**2 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 0.9 turns (holds 30, next step uses 32/turn) -> v2: check the step that makes it
- **flax plants**: flax plants buffer 1.0 turns (holds 80, next step uses 80/turn) -> v2: check the step that makes it

## Tuning

- **candles**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 519, not 619

## Prestige spending, cheapest coin per prestige first

778 turns left: prestige gained now converts 98.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.0 | 48.0 | running |
| hold banquet 3 (pies) | mansion | 8 | 48.7 | 48.7 | thin at home: hop beer, pies, candles |
| hold banquet 4 (pies) | mansion | 18 | 48.9 | 48.9 | thin at home: hop beer, stockfish, pies, candles |
| hold banquet 2 (pies) | mansion | 7 | 50.1 | 50.1 | thin at home: pies, candles |
| hold banquet 4 | mansion | 17.5 | 52.4 | 52.4 | thin at home: hop beer, stockfish, candles |
| hold banquet 3 (fish) | mansion | 7.6 | 53.2 | 53.2 | thin at home: hop beer, cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 53.7 | 53.7 | thin at home: cured fish |
| hold banquet 4 (premium) | mansion | 20 | 53.8 | 53.8 | thin at home: hop beer, stockfish, candles, premium cheese |
| jousting 3 | arena | 230 | 53.8 | 54.0 | needs a arena (build cost 23,939); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold feast 2 | townhouse | 2.6 | 51.2 | 54.5 | needs a townhouse (build cost 6,556) |
| hold banquet 3 (meat) | mansion | 7.6 | 54.6 | 54.6 | thin at home: hop beer |
| hold banquet 1 (fish) | mansion | 4.2 | 54.9 | 54.9 | thin at home: cured fish |

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
| arms | 1 @ 30.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| candles | 1 @ 76.0, stop 61 |  | goal planner: buys 1 a turn for today's rates, keeps up to 61 (v2 had 2) |
| cured meat | 7 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 22 = 3.7 turns |
| firewood | 3 @ 2.4, stop 12 |  | goal planner: buys 3 a turn for today's rates, keeps up to 12 (v2 had 8) |
| furniture | 2 @ 14.7, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 2 @ min 17.9 | goal planner: sells 2 at 17.9 (v2 had 2 at 21.0) |
| grain | 1 @ 3.7, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 11) |
| labour | 27 @ 2.2, stop - |  | goal planner: buys 27 for today's rates (v2 had 19) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| nets |  | 9 @ min 34.2 | goal planner: sells 9 at 34.2 (v2 had 9 at 35.8) |
| pasties | 1 @ 14.5, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 2) |
| porterage | 6 @ 1.1, stop - |  | goal planner: buys 6 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 76.0) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 1 = 4.0 turns |
| thread |  | 48 @ min 3.96 | goal planner: sells 48 a turn at 3.96, keeps 172 (no one offered it) |
| timber |  | 5 @ min 6.25 | goal planner: sells 5 a turn at 6.25, keeps 100 (no one offered it) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 200 |

## Goal: business value (live: rates, buys, sells, ships, invest)
- Value now 10.4k (cash + stock at home prices); -278/turn over 6 turns, -207/turn over 24 turns.
- Limits: cash flow >= +119/turn, prestige >= +5.14/turn (values are after 200 tax a turn).
- Today's settings: value -35/turn, cash +13/turn, prestige +73.21/turn - breaks the cash floor.
- Plan: value +476/turn, cash +335/turn, prestige +61.01/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +57 vs -13, -128 vs +14, +68 vs +20.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - mansion 1 1.00 -> 0.00: +202/turn
  - net maker [make nets 1] 0.00 -> 0.38: +21/turn
  - park 1 16.00 -> 0.00: +1/turn
  - spinnery 1 1.86 -> 3.14: +51/turn
  - weavery 1 0.15 -> 0.94: +69/turn
  - flax farm 1 4.99 -> 11.00: +36/turn
  - retting pit 1 1.00 -> 1.80: +105/turn
  - brewery 1 0.13 -> 0.02: +15/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.31: -19/turn
  - ropewalk 1 0.25 -> 0.00: +26/turn
- Model check over the last 59 turns: predicted +147/turn for the settings we ran, real -121/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 0.91, thread 2.37, cloth 3.73, flax fibres 2.95, garments 10.73, nets 17.54, beer 2.22, timber 5.94, prestige 0.00, cash 0.00
- Orders it would set: candles buy 1 (v2 2); firewood buy 3 (v2 8); fish buy 0 (v2 None); furniture buy 2 (v2 None); grain buy 1 (v2 11); labour buy 27 (v2 19); light armour buy 1 (v2 None); meat buy 0 (v2 None); pasties buy 1 (v2 2); porterage buy 6 (v2 5)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.31, worth +42/turn.
- Recipe: net maker make nets 3 -> make nets 1 at 0.38, worth +25/turn.
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +46/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new chandlery (make candles 1) for ~4125 coin: +3/turn, payback 1395 turns, doesn't pay yet (materials thin at home: bricks, nails)
  - +1 plot flax farm 1 for ~456 coin: +1/turn, payback 833 turns, doesn't pay yet
- Trim: donate park 1: +96/turn (tax 96 saved).

## Chain sizing

Mode HOLD, garments sold 1.7/turn (+0.0 exported); plan makes 1.6 garments a turn.
Labour: own 500, everything else 374, chain may buy 0 -> chain allowance 126, chain plan 126 (-126 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.99 | 2.64 |
| ret | 3 | 1.00 | 0.53 |
| spin | 4 | 1.86 | 0.93 |
| weave | 3 | 0.15 | 0.05 |
| sew | 2 | 0.09 | 0.04 |

Buffers: flax fibres 30/36, thread 172/106, cloth 17/7
- chain plan needed 676 labour, budget left 126: cut to 126 (sewing capped at 0.04)

## Self-diagnosis

- R1: beer slot dry: 2.9 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy none, home ask 3.36 (held back: failsafe level 3: reduce-only, would buy 16 @ 3.42 (ask 3.36, cap 14.4))
- R1: donations slot dry: 0.0 held, 40.0 a turn (luxury slot (+1 prestige)); our buy none, home ask 1.0 (held back: failsafe level 3: reduce-only, would buy 56 @ 1.02 (ask 1.0, cap 1.5))
- R1: fish slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask 1.74 (held back: failsafe level 3: reduce-only, would buy 14 @ 1.77 (ask 1.74, cap 2.6))
- R1: meat slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask none (no sellers at home)
