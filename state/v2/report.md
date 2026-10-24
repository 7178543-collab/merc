# v2 shadow report

Turn 13521, 2026-10-24 18:55. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 856, prestige 3,576 (456 free, -0.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 54 | 0 | 7 | 0 | 0 | min_holding 60, sell 82, sell @ 2.98 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 10 | 2 | 3 | 5 | 0 | stop 16, buy 3, buy @ 2.4; sell 4, sell @ 1.66 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 40 | 0 | 2 | 0 | 0 | min_holding 30, sell 8, sell @ 17.8 |
| grain | 121 | 0 | 0 | 0 | 0 | stop 145, buy 10, buy @ 3.7 |
| labour | 95 | 10 | 510 | 2 | 0 | buy 95, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 15 | 0 | 0 | 0 | 0 | min_holding 15, sell 12, sell @ 34 |
| porterage | 13 | 12 | 12 | 0 | 0 | buy 13, buy @ 1.1 |

**1 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (3 @ 2.4), 2 bought last turn); labour need rises ~82/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it

## Waste (money lost now)

- **labour**: buying 95, need ~55 -> v2: buy 55

## Tuning

- **cloth**: cloth buffer thin: 1.3 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 33
- **flax fibres**: flax fibres buffer thin: 1.2 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 57

## Notes

- labour: projection runs 100 over real use lately; planning 555, not 655

## Prestige spending, cheapest coin per prestige first

880 turns left: prestige gained now converts 98.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 45.9 | 45.9 | running |
| hold banquet 4 (pies) | mansion | 18 | 49.2 | 49.2 | thin at home: hop beer, pies |
| hold banquet 3 (pies) | mansion | 8 | 50.0 | 50.0 | thin at home: hop beer, pies |
| hold banquet 2 (pies) | mansion | 7 | 50.7 | 50.7 | thin at home: pies |
| jousting 3 | arena | 230 | 51.9 | 52.0 | needs a arena (build cost 24,467); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 52.5 | 52.5 | thin at home: hop beer, stockfish |
| hold prayer 2 | chapel | 13 | 50.2 | 53.1 | needs a chapel (build cost 31,272); thin at home: furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 53.3 | 53.3 |  |
| hold sermon 2 (candles) | church | 31 | 50.9 | 53.6 | needs a church (build cost 65,669); thin at home: candles, furniture |
| hold banquet 3 (fish) | mansion | 7.6 | 53.7 | 53.7 | thin at home: hop beer |
| hold banquet 2 (meat) | mansion | 6.8 | 54.2 | 54.2 |  |
| hold feast 2 | townhouse | 2.6 | 51.4 | 54.4 | needs a townhouse (build cost 6,776); thin at home: wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only -3 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -7 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~96 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.30 | 0.30 (29/turn) | rope 4 (53.92->68.88), glass ingots 2 (59.33->68.4), lead bars 6 (13.76->16.62), gold ore 1 (150.15->165.3) | beer 6 (2.62->3.5), gears 2 (59.85->61.27), wrought iron 5 (12.29->13.01), candles 1 (67.2->69) | +134 |
| Fontaux | 411 | 0.10 | 0.40 (38/turn) | cheese 10 (6.35->9.79), rope 2 (53.92->67.45), gold ore 1 (150.15->172.9), thread 65 (4.14->4.45) | candles 1 (67.73->69) | +112 |
| Grandgues | 152 | 0.04 | 0.30 (29/turn) | rope 4 (53.92->74.58), charcoal 12 (1.72->3.15), timber 26 (7.51->8.31), firewood 4 (1.57->3.13) | flax plants 1 (1.41->1.75) | +102 |
| Pontmont | 341 | 0.09 | 0.10 (10/turn) | rope 4 (53.92->70.3), limestone 2 (18.17->28.5), flax fibres 3 (4.42->4.75) | tallow 1 (20.37->23.94), candles 1 (68.25->69), wrought iron 2 (12.6->13.01), blades 1 (15.65->15.77) | +83 |
| Nürnnieder | 520 | 0.13 | 0.10 (10/turn) | thread 42 (4.14->5.13), rope 2 (53.92->71.25), garments 7 (17.9->18.52), wine 6 (5.46->5.7) | casks 7 (4.89->5.7), beer 6 (2.98->3.5), nails 1 (4.85->5.94), tallow 1 (22.89->23.94) | +82 |

**Best:** Hofkirchen at about +134 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 28.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| cured meat | 1 @ 29.0, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 2) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 16 | 4 @ min 1.7 | uses 7.8/turn (household upkeep), makes 6.5, holds 10 = 7.3 turns |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 13.8, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 8 @ min 17.8 | goal planner: sells 8 at 17.8 (v2 had 7 at 20.0) |
| grain | 36 @ 3.7, stop 141 |  | goal planner: buys 36 a turn for today's rates, keeps up to 141 (v2 had 22) |
| labour | 95 @ 2.2, stop - |  | goal planner: buys 95 for today's rates (v2 had 55) |
| light armour | 1 @ 84.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 12 @ min 34 | goal planner: sells 12 at 34 (v2 had 12 at 34.6) |
| pasties | 3 @ 14.5, stop 11 |  | goal planner: buys 3 a turn for today's rates, keeps up to 11 (v2 had 4) |
| porterage | 13 @ 1.1, stop - |  | goal planner: buys 13 for today's rates (v2 had 12) |
| rope |  | 4 @ min 72.0 | makes 2.0, uses 0.2, holds 29 (keeps 0): sells the surplus + 2/turn of the excess |
| thread |  | 8 @ min 4.12 | goal planner: sells 8 a turn at 4.12, keeps 221 (no one offered it) |
| tools | 2 @ 6.2, stop 16 |  | uses 2.0/turn (net maker152202386007001, retting pit 1), makes 0.0, holds 199 = 101.4 turns |
| varnish | 1 @ 17.1, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| wax | 1 @ 21.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 18.0k (cash + stock at home prices); +24/turn over 6 turns, +78/turn over 24 turns.
- Limits: cash flow >= +131/turn, prestige >= -0.65/turn (values are after 240 tax a turn).
- Today's settings: value +14/turn, cash +6/turn, prestige -0.74/turn - breaks the prestige floor and cash floor.
- Plan: value +35/turn, cash +131/turn, prestige -0.65/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +139 vs +63, +1 vs +20, -167 vs +11.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4, garments 0.5, nets 0.0, rope 0.1.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Boistot: +6/turn
  - brewery 1 0.63 -> 0.54: +15/turn
  - logging camp w/ tool 5.00 -> 5.44: +0/turn
  - weavery 1 0.33 -> 0.48: -4/turn
  - sewing shop 1 0.21 -> 0.27: +13/turn
  - retting pit 1 0.83 -> 0.68: -10/turn
  - flax farm 1 4.60 -> 3.88: +5/turn
  - spinnery 1 1.70 -> 1.39: +3/turn
- Model check over the last 27 turns: predicted +130/turn for the settings we ran, real +65/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.64, thread 4.03, cloth 6.49, flax fibres 4.64, garments 18.85, nets 29.83, beer 2.90, timber 7.22, prestige 57.93, cash 0.07
- Orders it would set: cured meat buy 1 (v2 2); furniture buy 2 (v2 None); garments sell 8 (v2 7); grain buy 36 (v2 22); labour buy 95 (v2 55); light armour buy 1 (v2 None); pasties buy 3 (v2 4); porterage buy 13 (v2 12); thread sell 8 (v2 none)
- Ship linen snake: Grandgues -> Boistot (+6/turn over staying).
- Ship Flax Wyrm: stays on Caillechâtel (worth +7/turn).
- Management: ~13.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +81/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
- Trim: donate quarry 1: +21/turn (tax 20 saved).
- Trim: donate logging camp w/ tool: +19/turn (tax 20 saved).

## Chain sizing

Mode HOLD, garments sold 7.3/turn (+0.0 exported); plan makes 0.0 garments a turn.
Labour: own 500, everything else 434, chain may buy 0 -> chain allowance 66, chain plan 94 (-166 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.60 | 2.14 |
| ret | 3 | 0.83 | 0.38 |
| spin | 4 | 1.70 | 0.79 |
| weave | 3 | 0.33 | 0.00 |
| sew | 2 | 0.21 | 0.00 |

Buffers: flax fibres 34/47, thread 768/138, cloth 22/0
- chain plan needed 94 labour, budget left 66: cut to 94

## Self-diagnosis

Nothing found this run.
