# v2 shadow report

Turn 13559, 2026-10-26 08:02. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 419, prestige 3,553 (433 free, -2.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 7 | 0 | 0 | min_holding 60, sell 55, sell @ 2.98 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 6 | 0 | 6 | 1 | 0 | buy @ 2.4; sell 1, sell @ 1.74 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 2, sell @ 17.9 |
| grain | 36 | 21 | 22 | 0 | 0 | stop 81, buy 21, buy @ 3.7 |
| labour | 0 | 0 | 451 | 0 | 49 | buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 10, sell @ 33.6 |
| porterage | 14 | 14 | 13 | 0 | 1 | buy 14, buy @ 1.1 |

**3 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: sewing shop 1 ran short of cloth (no buy order); labour need rises ~14/turn when they restart -> v2: add a cloth buy
- **firewood**: brewery 1 ran short of firewood (buy is live (no volume cap @ 2.4), home ask 1.74 x4, yet 0 bought last turn); labour need rises ~57/turn when they restart -> v2: find out why the buy isn't filling
- **varnish**: net maker152202386007001 ran short of varnish (buy is live (1 @ 20.6), but the home ask 21.40 is above it); labour need rises ~5/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Tuning

- **flax plants**: flax plants buffer thin: 1.2 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 187

## Notes

- labour: projection runs 112 over real use lately; planning 451, not 557

## Prestige spending, cheapest coin per prestige first

842 turns left: prestige gained now converts 98.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 3 (pies) | mansion | 8 | 45.3 | 45.3 | thin at home: hop beer, pies |
| maintain 1 | park | 0.5 | 46.5 | 46.5 | running |
| hold banquet 4 (pies) | mansion | 18 | 47.1 | 47.1 | thin at home: hop beer, wine, pies |
| hold banquet 2 (pies) | mansion | 7 | 48.9 | 48.9 | thin at home: wine, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 49.8 | 49.8 | thin at home: hop beer |
| hold banquet 3 (meat) | mansion | 7.6 | 50.2 | 50.2 | thin at home: hop beer |
| hold banquet 4 | mansion | 17.5 | 50.5 | 50.5 | thin at home: wine, hop beer, ham, stockfish |
| hold banquet 2 (fish) | mansion | 6.8 | 52.9 | 52.9 | thin at home: wine |
| jousting 3 | arena | 230 | 52.9 | 53.1 | needs a arena (build cost 24,314); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 53.3 | 53.3 | thin at home: hop beer, wine, stockfish, premium cheese |
| hold banquet 2 (meat) | mansion | 6.8 | 53.4 | 53.4 | thin at home: wine |
| hold sermon 2 (candles) | church | 31 | 51.6 | 54.3 | needs a church (build cost 61,581); thin at home: candles, furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -8 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~97 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.31 | 0.20 (19/turn) | candles 2 (71.4->216.6), yarn 5 (3.99->5.08), iron ore 2 (5.25->7.6), cloth 9 (7.67->8.03) | medicine 2 (122.85->127.3), bellows 1 (252->254.6), blades 1 (11.76->13.01), tools 2 (4.2->4.82) | +306 |
| Neuborn | 780 | 0.20 | 0.30 (29/turn) | charcoal 11 (1.92->4.75), glassware 3 (50.82->52.72), thread 11 (4.4->4.8), cloth 7 (7.67->7.89) | grindstones 1 (208.95->226.1), cheese 13 (4.83->5.22), bellows 1 (252->254.6), canvas 2 (32.76->33.63) | +38 |
| Toqueque | 642 | 0.17 | 0.10 (10/turn) | scythes 1 (23.94->24.89) | looms 1 (499.8->541.5), candles 1 (66.15->68), chisels 1 (9.19->9.36) | +36 |
| Dedlowe | 1146 | 0.39 | 0.10 (10/turn) | wine 8 (6.41->9.31), rope 1 (71.5->84.08), wrought iron 2 (14.28->15.86), yarn 4 (3.99->4.8) | pasties 1 (11.13->12.3) | +34 |
| Angefont | 686 | 0.18 | 0.30 (29/turn) | limestone 1 (16.8->32.87), beer 40 (3.12->3.65), cookware 9 (22.26->23.18), hides 1 (14.8->15.77) | candles 1 (65.62->68), flax fibres 14 (4.62->5.15), gears 2 (55.65->57), premium cheese 1 (26.25->27.55) | +32 |

**Best:** Hofkirchen at about +306 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| cured meat | 1 @ 29.0, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 2) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 0 @ 2.4, stop 13 | off | a building is stalled on firewood: no sell until it runs again |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres |  | 2 @ min 4.76 | goal planner: sells 2 a turn at 4.76, keeps 82 (no one offered it) |
| grain | 29 @ 3.7, stop 88 |  | goal planner: buys 29 a turn for today's rates, keeps up to 88 (v2 had 44) |
| labour | 0 @ 2.2, stop - |  | goal planner: buys 0 for today's rates (v2 had 0) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 36.2) |
| pasties | 2 @ 14.5, stop 4 |  | uses 1.0/turn (household upkeep), makes 0.0, holds 0 = 0.0 turns |
| porterage | 14 @ 1.1, stop - |  | goal planner: buys 14 for today's rates (v2 had 13) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 (v2 had 1) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 1 = 3.0 turns |
| thread |  | 23 @ min 4.26 | goal planner: sells 23 a turn at 4.26, keeps 180 (no one offered it) |
| tools | 3 @ 6.2, stop 17 |  | uses 2.1/turn (retting pit 1), makes 0.0, holds 199 = 95.7 turns |
| varnish | 1 @ 22.4, stop 1 | off | a building is stalled on varnish: no sell until it runs again |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 18.1k (cash + stock at home prices); -22/turn over 6 turns, -32/turn over 24 turns.
- Limits: cash flow >= +149/turn, prestige >= -0.56/turn (values are after 220 tax a turn).
- Today's settings: value +89/turn, cash -0/turn, prestige -2.29/turn - breaks the prestige floor and cash floor.
- Plan: value +38/turn, cash +10/turn, prestige -0.56/turn - could not meet the cash floor.
- Cash check (real vs predicted cash a tick, last 3): -193 vs +18, -101 vs +1, -7 vs -13 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship Flax Wyrm -> Angefont: +1/turn
  - spinnery 1 1.59 -> 1.76: +10/turn
  - logging camp w/ tool 5.00 -> 4.93: -0/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.44: -2/turn
  - ropewalk 1 0.25 -> 0.00: +27/turn
  - net maker 0.23 -> 0.00: +8/turn
  - mansion 1 0.15 -> 0.57: -83/turn
  - retting pit 1 1.04 -> 0.00: -102/turn
  - flax farm 1 5.88 -> 0.00: -27/turn
  - flax farm 1 [make flax fibres 1] 0.00 -> 9.17: +108/turn
- Model check: not enough runs yet (needs 6 turns of goal history).
- Worth of one more unit per turn: labour 1.25, thread 3.40, cloth 5.28, flax fibres 4.50, garments 15.03, nets 16.74, beer 120.49, timber 2.86, prestige 3557.32, cash 100.00
- Orders it would set: candles buy 2 (v2 None); cured meat buy 1 (v2 2); flax fibres sell 2 (v2 none); furniture buy 2 (v2 None); grain buy 29 (v2 44); light armour buy 1 (v2 None); porterage buy 14 (v2 13); rope sell 2 (v2 1); thread sell 23 (v2 none)
- Recipe: flax farm 1 grow flax 1 -> make flax fibres 1 at 9.17, worth +123/turn.
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.44, worth +52/turn.
- Ship linen snake: stays on Grandgues (worth +1/turn).
- Ship Flax Wyrm: Caillechâtel -> Angefont (+0/turn over staying).
- Management: ~12.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +42/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new chandlery (make candles 1) for ~3765 coin: +8/turn, payback 464 turns, doesn't pay yet (materials thin at home: bricks, nails)
- Trim: donate logging camp w/ tool: +16/turn (tax 20 saved).

## Chain sizing

Mode HOLD, garments sold 1.2/turn (+0.0 exported); plan makes 6.6 garments a turn.
Labour: own 500, everything else 394, chain may buy 0 -> chain allowance 106, chain plan 105 (-135 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.88 | 0.39 |
| ret | 3 | 1.04 | 0.07 |
| spin | 4 | 1.59 | 0.73 |
| weave | 3 | 0.13 | 0.26 |
| sew | 2 | 0.09 | 0.16 |

Buffers: flax fibres 390/45, thread 1048/133, cloth 0/26
- chain plan needed 394 labour, budget left 106: cut to 106 (sewing capped at 0.16)

## Self-diagnosis

- R1: arms slot dry: 0.0 held, 0.5 a turn (gear slot (+0.4 prestige)); our buy 1 @ 27, home ask 31.8; 5% of cash does not buy one at 32.4
- R1: pasties slot dry: 0.0 held, 2.8 a turn (basic food slot (+1.3 prestige)); our buy 2 @ 14.5, home ask 12.3; our bid is already at/over the ask (sellers too thin)
- R2: spinnery 1 blocked by thread space: 1048 held of 1084 capacity, we make 79.8 a turn; no buy on it: add a sell order or more capacity for thread
