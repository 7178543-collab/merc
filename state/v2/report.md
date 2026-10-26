# v2 shadow report

Turn 13571, 2026-10-26 20:39. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 153, prestige 3,519 (399 free, -0.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 16 | 0 | 4 | 0 | 0 | min_holding 60, sell 42, sell @ 2.94 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 0 | 0 | 0 | 0 | 0 | none |
| firewood | 0 | 0 | 0 | 4 | 0 | buy @ 2.4 |
| fish | 0 | 0 | 0 | 0 | 0 | none |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 2, sell @ 17.9 |
| grain | 47 | 0 | 0 | 0 | 0 | stop 72, buy 18, buy @ 3.7 |
| labour | 0 | 0 | 288 | 0 | 212 | buy @ 2.2 |
| meat | 0 | 0 | 0 | 0 | 0 | none |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 0 | 0 | 0 | 5 | 0 | buy 6, buy @ 1.1 |

**4 risks, 0 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: sewing shop 1 ran short of cloth (no buy order); labour need rises ~14/turn when they restart -> v2: add a cloth buy
- **firewood**: brewery 1 ran short of firewood (buy is live (no volume cap @ 2.4), home ask 1.73 x3, yet 0 bought last turn); labour need rises ~57/turn when they restart -> v2: find out why the buy isn't filling
- **porterage**: flax farm 1, retting pit 1 ran short of porterage (buy is live (6 @ 1.1), home ask 0.33 x26, yet 0 bought last turn); labour need rises ~78/turn when they restart -> v2: find out why the buy isn't filling
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 9.40 x10, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Notes

- labour: projection runs 100 over real use lately; planning 288, not 388

## Prestige spending, cheapest coin per prestige first

830 turns left: prestige gained now converts 98.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 44.4 | 44.4 | running |
| hold banquet 3 (pies) | mansion | 8 | 46.7 | 46.7 | thin at home: hop beer, pies |
| hold banquet 2 (pies) | mansion | 7 | 48.8 | 48.8 | thin at home: pies |
| hold banquet 4 (pies) | mansion | 18 | 50.1 | 50.1 | thin at home: hop beer, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 50.5 | 50.5 | thin at home: hop beer |
| hold banquet 3 (meat) | mansion | 7.6 | 51.6 | 51.6 | thin at home: hop beer, cured meat |
| hold banquet 2 (fish) | mansion | 6.8 | 52.0 | 52.0 |  |
| hold banquet 2 (meat) | mansion | 6.8 | 53.2 | 53.2 | thin at home: cured meat |
| jousting 3 | arena | 230 | 53.6 | 53.7 | needs a arena (build cost 23,200); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 54.0 | 54.0 |  |
| hold banquet 4 | mansion | 17.5 | 54.1 | 54.1 | thin at home: hop beer, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 54.3 | 54.3 | thin at home: hop beer, stockfish, premium cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~94 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Kirchwerp | 1072 | 0.34 | 0.20 (19/turn) | glassware 3 (51.03->67.92), flax fibres 11 (4.92->6.17), garments 1 (18.4->18.81), honey 2 (6.72->7.27) | alembics 1 (273->456), axes 1 (18.48->20.33), garments 2 (21->22.4), harnesses 1 (47.25->47.97) | +235 |
| Neuborn | 780 | 0.20 | 0.40 (38/turn) | charcoal 11 (1.9->4.75), thread 10 (3.98->4.89), furniture 12 (14.07->15.29), seeds 11 (2.75->3.32) | alembics 1 (367.5->456), canvas 4 (31.92->35.53), garments 2 (19.95->22.4), axes 1 (17.96->20.33) | +139 |
| Corstoft | 1496 | 0.55 | 0.80 (75/turn) | thread 91 (3.98->5.08), flax fibres 10 (4.92->7.93), dye 1 (57.75->60.8), garments 1 (18.4->19.57) | axes 1 (18.79->20.33) | +72 |
| Hanstein | 380 | 0.10 | 0.90 (84/turn) | thread 66 (3.98->4.39), wrought iron 3 (15.75->20.33), firewood 21 (1.82->4.94), garments 1 (18.4->21.28) | jewellery 1 (73.5->90.72), axes 1 (17.43->20.33), yarn 4 (4.73->5.27), fleece 2 (5.72->6.08) | +63 |
| Amsdermund | 1111 | 0.36 | 0.30 (28/turn) | thread 44 (3.98->5.22), wine 10 (5.57->6.84), honey 2 (6.72->8.36), garments 1 (18.4->20.9) | axes 1 (18.17->20.33), mouldboards 1 (30.66->32.3) | +53 |

**Best:** Kirchwerp at about +235 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer | 5 @ 3.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 16 = 3.8 turns |
| candles | 1 @ 70.0, stop 61 |  | goal planner: buys 1 a turn for today's rates, keeps up to 61 (v2 had 1) |
| firewood | 3 @ 2.4, stop 9 |  | goal planner: buys 3 a turn for today's rates, keeps up to 9 (v2 had 8) |
| flax fibres |  | 3 @ min 4.76 | goal planner: sells 3 a turn at 4.76, keeps 82 (no one offered it) |
| flax plants |  | 1 @ min 1.07 | goal planner: sells 1 a turn at 1.07, keeps 77 (no one offered it) |
| furniture | 2 @ 13.7, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| grain | 18 @ 3.7, stop 72 |  | goal planner: buys 18 a turn for today's rates, keeps up to 72 (v2 had 0) |
| labour | 0 @ 2.2, stop - |  | goal planner: buys 0 for today's rates (v2 had 0) |
| light armour | 1 @ 93.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 35.2) |
| porterage | 6 @ 1.1, stop - |  | goal planner: buys 6 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| thread |  | 29 @ min 3.98 | goal planner: sells 29 a turn at 3.98, keeps 169 (no one offered it) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 195 |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 15.2k (cash + stock at home prices); -387/turn over 6 turns, -126/turn over 24 turns.
- Limits: cash flow >= +160/turn, prestige >= -0.41/turn (values are after 200 tax a turn).
- Today's settings: value +85/turn, cash -12/turn, prestige +7.50/turn - breaks the cash floor.
- Plan: value +351/turn, cash +29/turn, prestige -0.41/turn - could not meet the cash floor.
- Cash check (real vs predicted cash a tick, last 3): +1 vs -61, +2 vs -65, -1 vs -80.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Bordetes: +0/turn
  - ship Flax Wyrm -> Pontmont: +0/turn
  - park 1 16.00 -> 0.18: +0/turn
  - weavery 1 0.13 -> 1.29: -1/turn
  - spinnery 1 1.59 -> 2.79: +122/turn
  - sewing shop 1 0.09 -> 0.80: +85/turn
  - brewery 1 0.44 -> 0.28: -8/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.22: -10/turn
  - ropewalk 1 0.25 -> 0.00: +13/turn
  - flax farm 1 5.88 -> 0.00: -83/turn
- Model check: not enough runs yet (needs 6 turns of goal history).
- Worth of one more unit per turn: labour 0.71, thread 2.64, cloth 3.71, flax fibres 4.60, garments 9.95, nets 16.38, beer 122.25, timber 2.81, prestige 21.45, cash 100.00
- Orders it would set: firewood buy 3 (v2 8); fish buy 0 (v2 None); flax fibres sell 3 (v2 none); flax plants sell 1 (v2 none); furniture buy 2 (v2 None); grain buy 18 (v2 0); light armour buy 1 (v2 None); meat buy 0 (v2 None); porterage buy 6 (v2 5); rope sell 1 (v2 none)
- Recipe: flax farm 1 grow flax 1 -> make flax fibres 1 at 11.00, worth +227/turn.
- Recipe: retting pit 1 retting 2 -> retting 1 at 0.02, worth +1/turn.
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.22, worth +29/turn.
- Ship linen snake: Grandgues -> Bordetes (+0/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Pontmont (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +36/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot flax farm 1 for ~442 coin: +5/turn, payback 97 turns
  - new chandlery (make candles 1) for ~3972 coin: +1/turn, payback 2668 turns, doesn't pay yet (materials thin at home: bricks, nails)
- Trim: donate park 1: +94/turn (tax 96 saved).

## Chain sizing

Mode HOLD, garments sold 1.2/turn (+0.0 exported); plan makes 8.6 garments a turn.
Labour: own 500, everything else 379, chain may buy 0 -> chain allowance 121, chain plan 120 (-101 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.88 | 0.41 |
| ret | 3 | 0.28 | 0.07 |
| spin | 4 | 1.59 | 0.74 |
| weave | 3 | 0.13 | 0.34 |
| sew | 2 | 0.09 | 0.21 |

Buffers: flax fibres 406/45, thread 1056/134, cloth 0/34
- chain plan needed 384 labour, budget left 121: cut to 121 (sewing capped at 0.21)

## Self-diagnosis

- R1: arms slot dry: 0.0 held, 0.5 a turn (gear slot (+0.4 prestige)); our buy 1 @ 27, home ask 32.8; 5% of cash does not buy one at 33.4
- R1: candles slot dry: 0.0 held, 1.5 a turn (luxury slot (+3 prestige)); our buy 1 @ 70, home ask 65.5; our bid is already at/over the ask (sellers too thin)
- R1: donations slot dry: 0.0 held, 40.0 a turn (luxury slot (+1 prestige)); our buy none, home ask 1.0 (held back: failsafe level 3: reduce-only, would buy 7 @ 1.02 (ask 1.0, cap 1.5))
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy none, home ask 1.73 (held back: failsafe level 3: reduce-only, would buy 4 @ 1.76 (ask 1.73, cap 2.1))
- R1: fish slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask 1.64 (held back: failsafe level 3: reduce-only, would buy 4 @ 1.67 (ask 1.64, cap 2.6))
- R1: meat slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask none (no sellers at home)
- R1: pasties slot dry: 0.0 held, 2.8 a turn (basic food slot (+1.3 prestige)); our buy 2 @ 14.5, home ask 12.4; our bid is already at/over the ask (sellers too thin)
- R2: spinnery 1 blocked by thread space: 1056 held of 1084 capacity, we make 79.8 a turn; no buy on it: add a sell order or more capacity for thread
