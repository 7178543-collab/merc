# v2 shadow report

Turn 13572, 2026-10-26 21:59. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 178, prestige 3,511 (391 free, -0.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 12 | 0 | 4 | 0 | 0 | min_holding 60, sell 42, sell @ 2.94 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 0 | 0 | 0 | 0 | 0 | none |
| firewood | 0 | 0 | 0 | 2 | 0 | buy @ 2.4 |
| fish | 0 | 0 | 0 | 0 | 0 | none |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 2, sell @ 17.9 |
| grain | 47 | 0 | 0 | 0 | 0 | stop 72, buy 18, buy @ 3.7 |
| labour | 0 | 0 | 288 | 0 | 212 | buy @ 2.2 |
| meat | 0 | 0 | 0 | 0 | 0 | none |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 0 | 0 | 0 | 5 | 0 | buy 6, buy @ 1.1 |

**4 risks, 0 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: sewing shop 1 ran short of cloth (no buy order); labour need rises ~14/turn when they restart -> v2: add a cloth buy
- **firewood**: brewery 1 ran short of firewood (buy is live (no volume cap @ 2.4), home ask 1.74 x3, yet 0 bought last turn); labour need rises ~36/turn when they restart -> v2: find out why the buy isn't filling
- **porterage**: flax farm 1, retting pit 1 ran short of porterage (buy is live (6 @ 1.1), home ask 0.33 x19, yet 0 bought last turn); labour need rises ~78/turn when they restart -> v2: find out why the buy isn't filling
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 9.75 x4, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Notes

- labour: projection runs 100 over real use lately; planning 290, not 390

## Prestige spending, cheapest coin per prestige first

829 turns left: prestige gained now converts 98.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 44.7 | 44.7 | running |
| hold banquet 3 (pies) | mansion | 8 | 46.8 | 46.8 | thin at home: hop beer, pies |
| hold banquet 2 (pies) | mansion | 7 | 48.8 | 48.8 | thin at home: pies |
| hold banquet 3 (fish) | mansion | 7.6 | 50.1 | 50.1 | thin at home: hop beer |
| hold banquet 4 (pies) | mansion | 18 | 50.2 | 50.2 | thin at home: hop beer, pies, glassware |
| hold banquet 3 (meat) | mansion | 7.6 | 51.3 | 51.3 | thin at home: hop beer, cured meat |
| hold banquet 2 (fish) | mansion | 6.8 | 51.5 | 51.5 |  |
| hold banquet 2 (meat) | mansion | 6.8 | 52.8 | 52.8 | thin at home: cured meat |
| hold banquet 1 (fish) | mansion | 4.2 | 53.5 | 53.5 |  |
| hold banquet 4 | mansion | 17.5 | 54.2 | 54.2 | thin at home: hop beer, stockfish, glassware |
| hold banquet 4 (premium) | mansion | 20 | 54.8 | 54.8 | thin at home: hop beer, stockfish, premium cheese, glassware |
| hold feast 2 | townhouse | 2.6 | 51.8 | 54.9 | needs a townhouse (build cost 6,458); thin at home: wine |

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
| Kirchwerp | 1072 | 0.34 | 0.20 (19/turn) | flax fibres 12 (5.05->6.17), honey 6 (7.61->8.6), iron ore 2 (5.51->8.55), garments 1 (16.89->18.81) | alembics 1 (338.1->456), garments 2 (21->21.8), harnesses 1 (47.25->48.45) | +130 |
| Vauxvais | 204 | 0.05 | 0.40 (38/turn) | bread 145 (2.07->2.28), limestone 1 (13.33->20.9), bricks 2 (5.99->8.26), garments 1 (16.89->20.33) | alembics 1 (417.9->456), tools 34 (4.77->4.84), seeds 1 (1.9->2.32) | +58 |
| Hanstein | 380 | 0.10 | 0.90 (85/turn) | thread 79 (3.96->4.41), firewood 22 (1.83->5.03), wrought iron 3 (15.75->17.67), garments 1 (16.89->21.47) | jewellery 1 (76.65->82.65), premium cheese 1 (26.04->26.98) | +57 |
| Grandgues | 152 | 0.04 | 0.50 (47/turn) | firewood 27 (1.83->3.7), charcoal 11 (1.87->3.86), iron ore 2 (5.51->8.55), cloth 13 (8.09->8.41) | - | +50 |
| Chribruck | 1202 | 0.40 | 0.20 (19/turn) | tackles 2 (183.75->193.8), thread 12 (3.96->5.27), garments 1 (16.89->22.04), leather 1 (31.08->34.77) | tin ingots 1 (27.93->33.63) | +43 |

**Best:** Kirchwerp at about +130 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer | 7 @ 3.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 12 = 2.8 turns |
| firewood | 3 @ 2.4, stop 9 |  | goal planner: buys 3 a turn for today's rates, keeps up to 9 (v2 had 5) |
| flax fibres |  | 4 @ min 4.76 | goal planner: sells 4 a turn at 4.76, keeps 82 (no one offered it) |
| flax plants |  | 1 @ min 1.05 | goal planner: sells 1 a turn at 1.05, keeps 77 (no one offered it) |
| furniture | 2 @ 13.6, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| grain | 18 @ 3.7, stop 69 |  | goal planner: buys 18 a turn for today's rates, keeps up to 69 (v2 had 0) |
| labour | 0 @ 2.2, stop - |  | goal planner: buys 0 for today's rates (v2 had 0) |
| light armour | 1 @ 90.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.4) |
| porterage | 6 @ 1.1, stop - |  | goal planner: buys 6 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| thread |  | 29 @ min 3.96 | goal planner: sells 29 a turn at 3.96, keeps 169 (no one offered it) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 195 |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 15.1k (cash + stock at home prices); -307/turn over 6 turns, -127/turn over 24 turns.
- Limits: cash flow >= +159/turn, prestige >= -0.38/turn (values are after 200 tax a turn).
- Today's settings: value +100/turn, cash +41/turn, prestige +7.50/turn - breaks the cash floor.
- Plan: value +376/turn, cash +56/turn, prestige -0.38/turn - could not meet the cash floor.
- Cash check (real vs predicted cash a tick, last 3): +2 vs -65, -1 vs -80, +26 vs -12.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Bordetes: +0/turn
  - park 1 16.00 -> 0.24: +0/turn
  - weavery 1 0.13 -> 1.29: -9/turn
  - spinnery 1 1.59 -> 2.80: +114/turn
  - sewing shop 1 0.09 -> 0.80: +89/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.21: -10/turn
  - ropewalk 1 0.25 -> 0.00: +13/turn
  - flax farm 1 5.88 -> 0.00: -74/turn
  - flax farm 1 [make flax fibres 1] 0.00 -> 11.00: +130/turn
  - retting pit 1 0.28 -> 0.00: +21/turn
- Model check: not enough runs yet (needs 6 turns of goal history).
- Worth of one more unit per turn: labour 0.70, thread 2.61, cloth 3.66, flax fibres 4.57, garments 9.81, nets 16.20, beer 122.30, timber 2.97, prestige 21.11, cash 100.00
- Orders it would set: firewood buy 3 (v2 5); fish buy 0 (v2 None); flax fibres sell 4 (v2 none); flax plants sell 1 (v2 none); furniture buy 2 (v2 None); grain buy 18 (v2 0); light armour buy 1 (v2 None); meat buy 0 (v2 None); porterage buy 6 (v2 5); rope sell 1 (v2 none)
- Recipe: flax farm 1 grow flax 1 -> make flax fibres 1 at 11.00, worth +242/turn.
- Recipe: retting pit 1 retting 2 -> retting 1 at 0.02, worth +1/turn.
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.21, worth +28/turn.
- Ship linen snake: Grandgues -> Bordetes (+0/turn over staying).
- Ship Flax Wyrm: stays on Caillechâtel (worth +0/turn).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +35/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot flax farm 1 for ~461 coin: +5/turn, payback 100 turns
  - new carpentry (craft furniture 1) for ~1301 coin: +3/turn, payback 462 turns, doesn't pay yet
- Trim: donate park 1: +93/turn (tax 96 saved).

## Chain sizing

Mode HOLD, garments sold 1.1/turn (+0.0 exported); plan makes 10.7 garments a turn.
Labour: own 500, everything else 358, chain may buy 0 -> chain allowance 142, chain plan 142 (-79 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.88 | 0.61 |
| ret | 3 | 0.28 | 0.11 |
| spin | 4 | 1.59 | 0.81 |
| weave | 3 | 0.13 | 0.41 |
| sew | 2 | 0.09 | 0.26 |

Buffers: flax fibres 391/48, thread 1055/141, cloth 0/41
- chain plan needed 385 labour, budget left 142: cut to 142 (sewing capped at 0.26)

## Self-diagnosis

- R1: arms slot dry: 0.0 held, 0.5 a turn (gear slot (+0.4 prestige)); our buy 1 @ 27, home ask 32.8; 5% of cash does not buy one at 33.4
- R1: candles slot dry: 0.0 held, 1.5 a turn (luxury slot (+3 prestige)); our buy 1 @ 70, home ask 65.0; our bid is already at/over the ask (sellers too thin)
- R1: donations slot dry: 0.0 held, 40.0 a turn (luxury slot (+1 prestige)); our buy none, home ask 1.0 (held back: failsafe level 3: reduce-only, would buy 8 @ 1.02 (ask 1.0, cap 1.5))
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy none, home ask 1.74 (held back: failsafe level 3: reduce-only, would buy 5 @ 1.77 (ask 1.74, cap 2.1))
- R1: fish slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask 1.62 (held back: failsafe level 3: reduce-only, would buy 5 @ 1.65 (ask 1.62, cap 2.6))
- R1: meat slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask none (no sellers at home)
- R1: pasties slot dry: 0.0 held, 2.8 a turn (basic food slot (+1.3 prestige)); our buy 2 @ 14.5, home ask 12.5; our bid is already at/over the ask (sellers too thin)
- R2: spinnery 1 blocked by thread space: 1055 held of 1084 capacity, we make 79.8 a turn; no buy on it: add a sell order or more capacity for thread
