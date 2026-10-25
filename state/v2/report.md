# v2 shadow report

Turn 13544, 2026-10-25 17:10. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 2,999, prestige 3,580 (460 free, -0.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 54 | 0 | 7 | 0 | 0 | min_holding 60, sell 55, sell @ 2.98 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 8 | 0 | 0 | 4 | 0 | buy @ 2.4; sell 1, sell @ 1.77 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 2, sell @ 17.9 |
| grain | 93 | 27 | 0 | 0 | 0 | stop 107, buy 27, buy @ 3.7 |
| labour | 0 | 0 | 469 | 0 | 31 | buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 13, sell @ 33.6 |
| porterage | 14 | 14 | 13 | 0 | 1 | buy 14, buy @ 1.1 |

**3 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: sewing shop 1 ran short of cloth (no buy order); labour need rises ~14/turn when they restart -> v2: add a cloth buy
- **firewood**: brewery 1 ran short of firewood (buy is live (no volume cap @ 2.4), home ask 1.60 x5, yet 0 bought last turn); labour need rises ~57/turn when they restart -> v2: find out why the buy isn't filling
- **varnish**: net maker152202386007001 ran short of varnish (buy is live (1 @ 20.6), home ask 19.70 x2, yet 0 bought last turn); labour need rises ~17/turn when they restart -> v2: find out why the buy isn't filling

## Tuning

- **flax plants**: flax plants buffer thin: 1.3 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 201

## Notes

- labour: projection runs 103 over real use lately; planning 548, not 651
- labour expiry guard: 31 bought labour expired last turn, buy 0 (not 48) this turn

## Prestige spending, cheapest coin per prestige first

857 turns left: prestige gained now converts 98.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 46.2 | 46.2 | running |
| hold banquet 3 (pies) | mansion | 8 | 47.6 | 47.6 | thin at home: hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 48.1 | 48.1 | thin at home: hop beer, wine, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 50.5 | 50.5 | thin at home: hop beer |
| hold banquet 2 (pies) | mansion | 7 | 50.6 | 50.6 | thin at home: wine, pies |
| hold banquet 3 (meat) | mansion | 7.6 | 51.0 | 51.0 | thin at home: hop beer |
| hold banquet 4 (premium) | mansion | 20 | 51.3 | 51.3 | thin at home: hop beer, wine, stockfish, premium cheese |
| hold banquet 4 | mansion | 17.5 | 51.4 | 51.4 | thin at home: wine, hop beer, ham, stockfish |
| hold banquet 2 (fish) | mansion | 6.8 | 52.7 | 52.7 | thin at home: wine |
| hold banquet 2 (meat) | mansion | 6.8 | 53.2 | 53.2 | thin at home: wine |
| jousting 3 | arena | 230 | 53.1 | 53.2 | needs a arena (build cost 23,325); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold sermon 2 (candles) | church | 31 | 51.2 | 53.7 | needs a church (build cost 59,962); thin at home: jewellery, candles, furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only -8 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~96 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Birkeningen | 1006 | 0.31 | 0.20 (19/turn) | grindstones 1 (264.6->334.4), tackles 1 (163.8->175.75), silver ore 1 (31.92->36.48), thread 7 (4.26->4.89) | malt 1 (5.25->6.32) | +75 |
| Donaunieder | 985 | 0.30 | 0.10 (10/turn) | tackles 1 (163.8->172.9), hides 1 (14.49->18.34) | medicine 1 (119.7->146.3), lathes 1 (161.7->190), pasties 2 (12.71->14.3), tin ingots 1 (35.91->36.48) | +61 |
| Orlesailles | 1178 | 0.40 | 0.10 (10/turn) | thread 16 (4.26->6.27), jewellery 1 (94.5->96.9), ham 1 (71.92->74.1) | gears 2 (56.7->58.9), pasties 2 (12.6->14.3) | +33 |
| Angefont | 686 | 0.18 | 0.20 (19/turn) | thread 16 (4.26->5.03), limestone 1 (14.38->30.4), ham 1 (71.92->73.62), seeds 12 (2.73->3.19) | flax fibres 25 (4.62->5.35), gears 1 (56.7->58.9), garments 2 (19.64->20), tools 2 (4.26->4.58) | +33 |
| Cobholme | 1564 | 0.60 | 0.10 (10/turn) | glassware 1 (50.19->70.3), garments 1 (18->32.49), scythes 1 (24.36->25.84) | tin ingots 1 (31.5->36.48) | +31 |

**Best:** Birkeningen at about +75 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 27, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had None) |
| beer | 7 @ 3.66, stop 27 |  | uses 6.5/turn (household upkeep, mansion 1), makes 0.0, holds 54 = 8.3 turns |
| candles | 2 @ 68.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cured meat | 1 @ 29.0, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 1) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 0 @ 2.4, stop 8 | off | a building is stalled on firewood: no sell until it runs again |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres |  | 3 @ min 5.25 | goal planner: trial sale of an idle pile, 3 a turn at 5.25, keeps 82 (32 over) |
| furniture | 2 @ 13.2, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| grain | 28 @ 3.7, stop 111 |  | goal planner: buys 28 a turn for today's rates, keeps up to 111 (v2 had 21) |
| labour | 4 @ 2.2, stop - |  | goal planner: buys 4 for today's rates (v2 had 0) |
| light armour | 1 @ 90, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 10 @ min 33.6 | goal planner: sells 10 at 33.6 (v2 had 9 at 34.0) |
| pasties | 2 @ 14.5, stop 8 |  | goal planner: buys 2 a turn for today's rates, keeps up to 8 (v2 had 6) |
| porterage | 14 @ 1.1, stop - |  | goal planner: buys 14 for today's rates (v2 had 7) |
| rope |  | 1 @ min 73.5 |  |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| thread |  | 16 @ min 4.26 | goal planner: sells 16 a turn at 4.26, keeps 205 (no one offered it) |
| tools | 3 @ 6.2, stop 22 |  | uses 2.7/turn (retting pit 1), makes 0.0, holds 199 = 74.5 turns |
| varnish | 1 @ 20.6, stop 1 | off | a building is stalled on varnish: no sell until it runs again |
| wax | 1 @ 21.2, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 18.5k (cash + stock at home prices); -52/turn over 6 turns, +22/turn over 24 turns.
- Limits: cash flow >= +42/turn, prestige >= -0.67/turn (values are after 220 tax a turn).
- Today's settings: value +104/turn, cash +55/turn, prestige -0.85/turn - breaks the prestige floor.
- Plan: value +203/turn, cash +217/turn, prestige -0.67/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +472 vs +136, -243 vs -48, -44 vs +43.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4, rope 0.1.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Vauxvais: +5/turn
  - ship Flax Wyrm -> Bremcop: +1/turn
  - ropewalk 1 0.25 -> 0.85: +28/turn
  - net maker 0.73 -> 0.15: +42/turn
  - spinnery 1 1.59 -> 2.35: +10/turn
  - logging camp w/ tool 5.00 -> 2.87: +2/turn
  - weavery 1 0.13 -> 0.35: +1/turn
  - sewing shop 1 0.09 -> 0.19: +23/turn
  - flax farm 1 6.29 -> 6.49: -1/turn
- Model check over the last 49 turns: predicted +99/turn for the settings we ran, real +46/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.54, thread 3.79, cloth 6.10, flax fibres 4.37, garments 17.73, nets 27.23, beer 2.78, timber 2.86, prestige 53.61, cash 0.00
- Orders it would set: arms buy 1 (v2 None); candles buy 2 (v2 None); flax fibres sell 3 (v2 none); furniture buy 2 (v2 None); grain buy 28 (v2 21); labour buy 4 (v2 0); light armour buy 1 (v2 None); nets sell 10 (v2 9); pasties buy 2 (v2 6); porterage buy 14 (v2 7)
- Ship linen snake: Grandgues -> Vauxvais (+5/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Bremcop (+1/turn over staying).
- Management: ~12.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +77/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
- Trim: donate logging camp w/ tool: +19/turn (tax 20 saved).
- Trim: donate weavery 1: +10/turn (tax 18 saved).

## Chain sizing

Mode HOLD, garments sold 2.0/turn (+0.0 exported); plan makes 32.0 garments a turn.
Labour: own 500, everything else 406, chain may buy 350 -> chain allowance 444, chain plan 434 (+187 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 6.29 | 4.76 |
| ret | 3 | 1.12 | 0.85 |
| spin | 4 | 1.59 | 1.88 |
| weave | 3 | 0.13 | 1.25 |
| sew | 2 | 0.09 | 0.78 |

Buffers: flax fibres 113/84, thread 900/248, cloth 0/125

## Self-diagnosis

Nothing found this run.
