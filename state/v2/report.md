# v2 shadow report

Turn 13570, 2026-10-26 19:54. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 153, prestige 3,527 (407 free, -0.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 20 | 0 | 4 | 0 | 0 | min_holding 60, sell 42, sell @ 2.94 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 0 | 0 | 0 | 0 | 0 | none |
| firewood | 0 | 0 | 0 | 4 | 0 | buy @ 2.4 |
| fish | 0 | 0 | 0 | 0 | 0 | none |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 2, sell @ 17.9 |
| grain | 47 | 0 | 0 | 0 | 0 | stop 76, buy 19, buy @ 3.7 |
| labour | 0 | 0 | 287 | 0 | 213 | buy @ 2.2 |
| meat | 0 | 0 | 0 | 0 | 0 | none |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 0 | 0 | 0 | 5 | 0 | buy 6, buy @ 1.1 |

**4 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: sewing shop 1 ran short of cloth (no buy order); labour need rises ~14/turn when they restart -> v2: add a cloth buy
- **firewood**: brewery 1 ran short of firewood (buy is live (no volume cap @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~57/turn when they restart -> v2: find out why the buy isn't filling
- **porterage**: flax farm 1, retting pit 1 ran short of porterage (buy is live (6 @ 1.1), home ask 0.33 x24, yet 0 bought last turn); labour need rises ~84/turn when they restart -> v2: find out why the buy isn't filling
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 9.40 x10, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 288, not 388

## Prestige spending, cheapest coin per prestige first

831 turns left: prestige gained now converts 98.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 44.1 | 44.1 | running |
| hold banquet 3 (pies) | mansion | 8 | 46.9 | 46.9 | thin at home: hop beer, pies |
| hold banquet 2 (pies) | mansion | 7 | 49.0 | 49.0 | thin at home: wine, pies |
| hold banquet 4 (pies) | mansion | 18 | 50.2 | 50.2 | thin at home: hop beer, wine, stockfish, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 50.5 | 50.5 | thin at home: hop beer |
| hold banquet 3 (meat) | mansion | 7.6 | 51.1 | 51.1 | thin at home: hop beer |
| hold banquet 2 (fish) | mansion | 6.8 | 52.1 | 52.1 | thin at home: wine |
| hold prayer 2 | chapel | 13 | 49.6 | 52.5 | needs a chapel (build cost 28,920) |
| hold banquet 2 (meat) | mansion | 6.8 | 52.8 | 52.8 | thin at home: wine |
| hold sermon 2 (candles) | church | 31 | 51.2 | 53.8 | needs a church (build cost 60,006); thin at home: furniture |
| jousting 3 | arena | 230 | 53.6 | 53.8 | needs a arena (build cost 23,574); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 53.9 | 53.9 |  |

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
| Hofkirchen | 991 | 0.30 | 0.10 (9/turn) | lead ore 2 (7.3->9.69), iron ore 1 (5.51->7.6) | alembics 1 (300.3->456), medicine 2 (123.9->134.9), bellows 1 (252->262.2), arms 2 (27.3->29.83) | +200 |
| Angefont | 686 | 0.17 | 0.20 (19/turn) | limestone 2 (13.97->33.25), fleece 2 (6.77->8.17), lead ore 4 (7.3->8.22) | alembics 1 (354.9->456), yarn 4 (3.72->6.08), garments 2 (19.95->22.6), cloth 6 (7.82->8.35) | +146 |
| Amsdermund | 1111 | 0.36 | 0.30 (28/turn) | thread 43 (4.02->5.22), tar 3 (9.87->11.59), garments 1 (20.2->20.9), pies 1 (16.91->18.05) | premium ham 1 (216.3->247), medicine 2 (127.05->134.9), bellows 1 (252->262.2), mouldboards 1 (31.29->32.11) | +86 |
| Darmwald | 1022 | 0.31 | 0.60 (57/turn) | charcoal 11 (1.9->9.26), thread 25 (4.02->4.8), furniture 11 (13.65->15.39), lead ore 1 (7.3->9.07) | spinning wheels 1 (202.65->216.6), garments 2 (21->22.6), cloth 6 (7.88->8.35), tin ingots 1 (35.7->36.48) | +86 |
| Fontaux | 411 | 0.10 | 0.80 (76/turn) | cheese 11 (5.72->9.79), charcoal 11 (1.9->4.89), firewood 19 (1.59->5.22), flax fibres 7 (4.92->5.27) | yarn 2 (5.04->6.08), stockfish 1 (97.65->98.8) | +80 |

**Best:** Hofkirchen at about +200 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer | 5 @ 3.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 20 = 4.8 turns |
| candles | 2 @ 70.0, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had 3) |
| firewood | 3 @ 2.4, stop 9 |  | goal planner: buys 3 a turn for today's rates, keeps up to 9 (v2 had 8) |
| flax fibres |  | 3 @ min 4.76 | goal planner: sells 3 a turn at 4.76, keeps 82 (no one offered it) |
| flax plants |  | 2 @ min 1.17 | goal planner: sells 2 a turn at 1.17, keeps 144 (no one offered it) |
| furniture | 2 @ 13.3, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| grain | 18 @ 3.7, stop 72 |  | goal planner: buys 18 a turn for today's rates, keeps up to 72 (v2 had 0) |
| labour | 0 @ 2.2, stop - |  | goal planner: buys 0 for today's rates (v2 had 0) |
| light armour | 1 @ 92.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 36.2) |
| porterage | 6 @ 1.1, stop - |  | goal planner: buys 6 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| thread |  | 28 @ min 3.98 | goal planner: sells 28 a turn at 3.98, keeps 169 (no one offered it) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 195 |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 15.6k (cash + stock at home prices); -332/turn over 6 turns, -110/turn over 24 turns.
- Limits: cash flow >= +160/turn, prestige >= -0.44/turn (values are after 200 tax a turn).
- Today's settings: value +57/turn, cash -80/turn, prestige +7.50/turn - breaks the cash floor.
- Plan: value +272/turn, cash -37/turn, prestige -0.44/turn - could not meet the cash floor.
- Cash check (real vs predicted cash a tick, last 3): +27 vs -49, +1 vs -61, +2 vs -65.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Angefont: +1/turn
  - ship Flax Wyrm -> Bordetes: +0/turn
  - park 1 16.00 -> 0.11: +0/turn
  - weavery 1 0.13 -> 1.61: +6/turn
  - spinnery 1 1.59 -> 3.12: +165/turn
  - sewing shop 1 0.09 -> 0.50: +13/turn
  - brewery 1 0.44 -> 0.28: +6/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.23: -11/turn
  - ropewalk 1 0.25 -> 0.00: +13/turn
  - flax farm 1 5.88 -> 0.00: -144/turn
- Model check: not enough runs yet (needs 6 turns of goal history).
- Worth of one more unit per turn: labour 0.36, thread 3.22, cloth 3.76, flax fibres 7.89, garments 8.69, nets 16.74, beer 137.87, timber 3.19, prestige 10.73, cash 100.00
- Orders it would set: candles buy 2 (v2 3); firewood buy 3 (v2 8); fish buy 0 (v2 None); flax fibres sell 3 (v2 none); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); grain buy 18 (v2 0); light armour buy 1 (v2 None); meat buy 0 (v2 None); porterage buy 6 (v2 5)
- Recipe: flax farm 1 grow flax 1 -> make flax fibres 1 at 11.00, worth +270/turn.
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.23, worth +26/turn.
- Ship linen snake: Grandgues -> Angefont (+0/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Bordetes (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - new chandlery (make candles 1) for ~4098 coin: +23/turn, payback 178 turns, doesn't pay yet (materials thin at home: bricks, nails)
  - Tenants L13 for 500 prestige: +18/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot flax farm 1 for ~464 coin: +16/turn, payback 29 turns
- Trim: donate park 1: +94/turn (tax 96 saved).

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

Buffers: flax fibres 421/45, thread 1056/134, cloth 0/34
- chain plan needed 384 labour, budget left 121: cut to 121 (sewing capped at 0.21)

## Self-diagnosis

- R1: arms slot dry: 0.0 held, 0.5 a turn (gear slot (+0.4 prestige)); our buy 1 @ 27, home ask 33.0; 5% of cash does not buy one at 33.6
- R1: candles slot dry: 0.5 held, 1.5 a turn (luxury slot (+3 prestige)); our buy 2 @ 70, home ask 64.5; our bid is already at/over the ask (sellers too thin)
- R1: donations slot dry: 0.0 held, 40.0 a turn (luxury slot (+1 prestige)); our buy none, home ask 1.0 (held back: failsafe level 3: reduce-only, would buy 7 @ 1.02 (ask 1.0, cap 1.5))
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy none, home ask none (no sellers at home)
- R1: fish slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask 1.66 (held back: failsafe level 3: reduce-only, would buy 4 @ 1.69 (ask 1.66, cap 2.6))
- R1: meat slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask 1.48 (held back: failsafe level 3: reduce-only, would buy 5 @ 1.51 (ask 1.48, cap 2.6))
- R1: pasties slot dry: 0.0 held, 2.8 a turn (basic food slot (+1.3 prestige)); our buy 2 @ 14.5, home ask 12.7; our bid is already at/over the ask (sellers too thin)
- R2: spinnery 1 blocked by thread space: 1056 held of 1084 capacity, we make 79.8 a turn; no buy on it: add a sell order or more capacity for thread
