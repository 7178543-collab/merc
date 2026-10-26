# v2 shadow report

Turn 13569, 2026-10-26 18:33. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 152, prestige 3,532 (412 free, -0.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 24 | 0 | 4 | 0 | 0 | min_holding 60, sell 42, sell @ 2.94 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 0 | 0 | 0 | 0 | 0 | none |
| firewood | 0 | 0 | 0 | 4 | 0 | buy @ 2.4 |
| fish | 0 | 0 | 0 | 0 | 0 | none |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 2, sell @ 17.9 |
| grain | 47 | 0 | 0 | 0 | 0 | stop 76, buy 19, buy @ 3.7 |
| labour | 0 | 0 | 285 | 0 | 215 | buy @ 2.2 |
| meat | 0 | 0 | 0 | 0 | 0 | none |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 0 | 0 | 0 | 5 | 0 | buy 6, buy @ 1.1 |

**4 risks, 0 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: sewing shop 1 ran short of cloth (no buy order); labour need rises ~14/turn when they restart -> v2: add a cloth buy
- **firewood**: brewery 1 ran short of firewood (buy is live (no volume cap @ 2.4), home ask 1.51 x6, yet 0 bought last turn); labour need rises ~57/turn when they restart -> v2: find out why the buy isn't filling
- **porterage**: flax farm 1, retting pit 1 ran short of porterage (buy is live (6 @ 1.1), home ask 0.33 x24, yet 0 bought last turn); labour need rises ~84/turn when they restart -> v2: find out why the buy isn't filling
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 9.40 x11, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Notes

- labour: projection runs 100 over real use lately; planning 287, not 387

## Prestige spending, cheapest coin per prestige first

832 turns left: prestige gained now converts 98.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 44.4 | 44.4 | running |
| hold banquet 3 (pies) | mansion | 8 | 47.2 | 47.2 | thin at home: hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 48.4 | 48.4 | thin at home: hop beer, wine, pies |
| hold banquet 2 (pies) | mansion | 7 | 49.4 | 49.4 | thin at home: wine, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 50.0 | 50.0 | thin at home: hop beer, cured fish |
| hold banquet 3 (meat) | mansion | 7.6 | 51.1 | 51.1 | thin at home: hop beer |
| hold banquet 2 (fish) | mansion | 6.8 | 51.6 | 51.6 | thin at home: wine, cured fish |
| hold banquet 4 | mansion | 17.5 | 51.8 | 51.8 | thin at home: wine, hop beer, stockfish |
| hold banquet 2 (meat) | mansion | 6.8 | 52.8 | 52.8 | thin at home: wine |
| hold banquet 1 (fish) | mansion | 4.2 | 52.9 | 52.9 |  |
| hold banquet 4 (premium) | mansion | 20 | 53.0 | 53.0 | thin at home: hop beer, wine, stockfish, premium cheese |
| jousting 3 | arena | 230 | 53.9 | 54.0 | needs a arena (build cost 23,228); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only -7 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~95 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Darmwald | 1022 | 0.31 | 0.70 (66/turn) | grindstones 1 (275.1->349.6), looms 1 (497.7->560.5), charcoal 11 (1.9->8.93), furniture 11 (13.65->15.39) | cloth 6 (7.88->8.65), steel ingots 1 (19.74->20.14), tin ingots 1 (35.7->36.48) | +194 |
| Angefont | 686 | 0.17 | 0.30 (28/turn) | looms 1 (497.7->617.5), limestone 2 (14.07->29.07), malt 6 (4.24->6.08), fleece 4 (7.61->9.07) | garments 2 (19.95->25), cloth 6 (8.14->8.65), axes 1 (18.27->19.76), flax fibres 10 (4.62->5.1) | +158 |
| Fontaux | 411 | 0.10 | 0.80 (76/turn) | looms 1 (497.7->555.75), cheese 14 (5.99->9.79), charcoal 11 (1.9->4.73), flax fibres 7 (4.96->6.46) | axes 1 (19.01->19.76) | +148 |
| Kirchwerp | 1072 | 0.34 | 0.40 (38/turn) | soap 2 (87.15->119.7), looms 1 (497.7->546.25), flax fibres 22 (4.96->6.17), tar 7 (9.87->11.4) | garments 2 (21->25), axes 1 (16.8->19.76), premium cheese 1 (24.36->27.93), steel ingots 1 (19.43->20.14) | +140 |
| Amsdermund | 1111 | 0.36 | 0.20 (19/turn) | looms 1 (497.7->570), thread 32 (4.02->5.22), tar 2 (9.87->11.4), yarn 4 (4.35->5.08) | medicine 2 (127.05->134.9), bellows 1 (252->260.3), axes 1 (18.27->19.76), garments 2 (24.36->25) | +124 |

**Best:** Darmwald at about +194 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer | 5 @ 3.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 24 = 5.8 turns |
| candles | 2 @ 70.0, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had 3) |
| firewood | 3 @ 2.4, stop 10 |  | goal planner: buys 3 a turn for today's rates, keeps up to 10 (v2 had 8) |
| flax fibres |  | 3 @ min 4.76 | goal planner: sells 3 a turn at 4.76, keeps 82 (no one offered it) |
| flax plants |  | 2 @ min 1.34 | goal planner: sells 2 a turn at 1.34, keeps 144 (no one offered it) |
| furniture | 2 @ 13.3, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| grain | 19 @ 3.7, stop 76 |  | goal planner: buys 19 a turn for today's rates, keeps up to 76 (v2 had 0) |
| labour | 0 @ 2.2, stop - |  | goal planner: buys 0 for today's rates (v2 had 0) |
| light armour | 1 @ 95, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 36.6) |
| porterage | 6 @ 1.1, stop - |  | goal planner: buys 6 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| thread |  | 28 @ min 4 | goal planner: sells 28 a turn at 4, keeps 169 (no one offered it) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 195 |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 15.8k (cash + stock at home prices); -294/turn over 6 turns, -112/turn over 24 turns.
- Limits: cash flow >= +160/turn, prestige >= -0.46/turn (values are after 200 tax a turn).
- Today's settings: value +71/turn, cash -65/turn, prestige +7.50/turn - breaks the cash floor.
- Plan: value +338/turn, cash -27/turn, prestige -0.46/turn - could not meet the cash floor.
- Cash check (real vs predicted cash a tick, last 3): +1 vs -32, +27 vs -49, +1 vs -61.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Pontmont: +1/turn
  - ship Flax Wyrm -> Angefont: +0/turn
  - park 1 16.00 -> 0.07: +0/turn
  - weavery 1 0.13 -> 1.29: +12/turn
  - spinnery 1 1.59 -> 2.79: +130/turn
  - sewing shop 1 0.09 -> 0.80: +102/turn
  - brewery 1 0.44 -> 0.29: +0/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.23: -11/turn
  - ropewalk 1 0.25 -> 0.00: +14/turn
  - retting pit 1 0.53 -> 0.00: -122/turn
- Model check: not enough runs yet (needs 6 turns of goal history).
- Worth of one more unit per turn: labour 0.86, thread 2.82, cloth 4.11, flax fibres 4.52, garments 11.25, nets 16.92, beer 122.05, timber 2.81, prestige 25.68, cash 100.00
- Orders it would set: candles buy 2 (v2 3); firewood buy 3 (v2 8); fish buy 0 (v2 None); flax fibres sell 3 (v2 none); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); grain buy 19 (v2 0); light armour buy 1 (v2 None); meat buy 0 (v2 None); porterage buy 6 (v2 5)
- Recipe: flax farm 1 grow flax 1 -> make flax fibres 1 at 11.00, worth +180/turn.
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.23, worth +28/turn.
- Ship linen snake: Grandgues -> Pontmont (+1/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Angefont (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +43/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new chandlery (make candles 1) for ~3907 coin: +19/turn, payback 209 turns, doesn't pay yet (materials thin at home: bricks, nails)
  - +1 plot flax farm 1 for ~428 coin: +4/turn, payback 119 turns
- Trim: donate park 1: +95/turn (tax 96 saved).

## Chain sizing

Mode HOLD, garments sold 1.2/turn (+0.0 exported); plan makes 8.6 garments a turn.
Labour: own 500, everything else 379, chain may buy 0 -> chain allowance 121, chain plan 120 (-107 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.88 | 0.41 |
| ret | 3 | 0.53 | 0.07 |
| spin | 4 | 1.59 | 0.74 |
| weave | 3 | 0.13 | 0.34 |
| sew | 2 | 0.09 | 0.21 |

Buffers: flax fibres 435/45, thread 1057/134, cloth 0/34
- chain plan needed 384 labour, budget left 121: cut to 121 (sewing capped at 0.21)

## Self-diagnosis

- R1: arms slot dry: 0.0 held, 0.5 a turn (gear slot (+0.4 prestige)); our buy 1 @ 27, home ask 33.0; 5% of cash does not buy one at 33.6
- R1: candles slot dry: 2.0 held, 1.5 a turn (luxury slot (+3 prestige)); our buy 2 @ 70, home ask 67.5; our bid is already at/over the ask (sellers too thin)
- R1: donations slot dry: 0.0 held, 40.0 a turn (luxury slot (+1 prestige)); our buy none, home ask 1.0 (held back: failsafe level 3: reduce-only, would buy 7 @ 1.02 (ask 1.0, cap 1.5))
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy none, home ask 1.51 (held back: failsafe level 3: reduce-only, would buy 4 @ 1.54 (ask 1.51, cap 2.1))
- R1: fish slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask 1.68 (held back: failsafe level 3: reduce-only, would buy 4 @ 1.71 (ask 1.68, cap 2.6))
- R1: meat slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask 1.48 (held back: failsafe level 3: reduce-only, would buy 5 @ 1.51 (ask 1.48, cap 2.6))
- R1: pasties slot dry: 0.0 held, 2.8 a turn (basic food slot (+1.3 prestige)); our buy 2 @ 14.5, home ask 12.7; our bid is already at/over the ask (sellers too thin)
- R2: spinnery 1 blocked by thread space: 1057 held of 1084 capacity, we make 79.8 a turn; no buy on it: add a sell order or more capacity for thread
