# v2 shadow report

Turn 13524, 2026-10-24 21:01. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 835, prestige 3,574 (454 free, -0.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 87 | 0 | 7 | 0 | 0 | min_holding 60, sell 69, sell @ 2.98 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 7 | 2 | 8 | 0 | 0 | stop 16, buy 2, buy @ 2.4; sell 4, sell @ 1.72 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 35 | 0 | 2 | 0 | 0 | min_holding 30, sell 8, sell @ 17.8 |
| grain | 47 | 10 | 41 | 0 | 0 | stop 145, buy 10, buy @ 3.7 |
| labour | 65 | 65 | 565 | 29 | 0 | buy 65, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 12, sell @ 34 |
| porterage | 13 | 13 | 9 | 0 | 4 | buy 13, buy @ 1.1 |

**2 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.7 turns (holds 12, next step uses 17/turn) -> v2: check the step that makes it
- **labour**: buying 65, short of ~94 needed -> v2: buy 94

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.2 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 57

## Notes

- labour: projection runs 112 over real use lately; planning 594, not 614

## Prestige spending, cheapest coin per prestige first

877 turns left: prestige gained now converts 98.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 46.8 | 46.8 | running |
| hold banquet 4 (pies) | mansion | 18 | 49.8 | 49.8 | thin at home: hop beer, wine, pies |
| hold banquet 3 (pies) | mansion | 8 | 50.2 | 50.2 | thin at home: hop beer, pies |
| hold banquet 2 (pies) | mansion | 7 | 51.3 | 51.3 | thin at home: wine, pies |
| jousting 3 | arena | 230 | 52.3 | 52.4 | needs a arena (build cost 24,680); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 52.5 | 52.5 | thin at home: wine |
| hold banquet 3 (fish) | mansion | 7.6 | 52.6 | 52.6 | thin at home: hop beer |
| hold prayer 2 | chapel | 13 | 49.7 | 52.7 | needs a chapel (build cost 31,101) |
| hold banquet 4 | mansion | 17.5 | 53.1 | 53.1 | thin at home: wine, hop beer, stockfish |
| hold banquet 1 (fish) | mansion | 4.2 | 53.8 | 53.8 |  |
| hold sermon 2 (candles) | church | 31 | 51.4 | 54.1 | needs a church (build cost 66,411); thin at home: jewellery, candles, furniture |
| hold banquet 3 (meat) | mansion | 7.6 | 54.6 | 54.6 | thin at home: hop beer |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only -4 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -9 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~97 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Darmwald | 1022 | 0.32 | 0.60 (58/turn) | grindstones 1 (283.5->475), charcoal 11 (1.92->7.12), thread 26 (4.14->4.54), rope 2 (69.5->70.77) | flax plants 1 (1.08->1.73) | +205 |
| Fontaux | 411 | 0.11 | 0.90 (87/turn) | garments 6 (17.7->22.99), thread 65 (4.14->4.5), steel ingots 2 (14.28->16.62), charcoal 11 (1.92->3.08) | casks 9 (5.02->5.51), cheese 7 (5.25->5.7), candles 1 (67.2->68) | +62 |
| Rouhomme | 368 | 0.10 | 1.00 (97/turn) | beer 70 (2.98->3.42), charcoal 9 (1.92->3.29), iron ore 1 (4.87->8.46), lead ore 1 (7.67->9.97) | grindstones 0 (204.75->224.2), casks 7 (5.1->5.51), lathes 0 (202.65->205.2), tiles 3 (4.07->5.56) | +59 |
| Clairlond | 1288 | 0.46 | 0.10 (10/turn) | garments 6 (17.7->25.27), acid 1 (138.6->152), yarn 2 (3.82->4.64) | cloth 4 (6.3->7.45), mouldboards 2 (30.66->31.16) | +57 |
| Hofkirchen | 991 | 0.31 | 0.30 (29/turn) | glass ingots 2 (59.33->68.4), lead ore 2 (7.67->10.83), thread 5 (4.14->5.13), yarn 3 (3.82->5.08) | lathes 1 (184.8->205.2), beer 6 (2.62->3.5), gears 2 (59.85->61.27), wrought iron 4 (11.87->12.35) | +52 |

**Best:** Darmwald at about +205 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 29.0, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 4.0 turns |
| beer |  | 82 @ min 2.98 | goal planner: sells 82 at 2.98 (v2 had 82 at 3.38) |
| cured meat | 1 @ 29.0, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 2) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 2 @ 2.4, stop 6 | 1 @ min 1.69 | goal planner: buys 2 a turn for today's rates, keeps up to 6 (v2 had 2) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 7 @ min 17.8 | goal planner: sells 7 at 17.8 (v2 had 6 at 20.0) |
| grain | 32 @ 3.7, stop 127 |  | goal planner: buys 32 a turn for today's rates, keeps up to 127 (v2 had 83) |
| labour | 95 @ 2.2, stop - |  | goal planner: buys 95 for today's rates (v2 had 94) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 12 @ min 34 | goal planner: sells 12 at 34 (v2 had 12 at 34.6) |
| pasties | 3 @ 14.5, stop 11 |  | goal planner: buys 3 a turn for today's rates, keeps up to 11 (v2 had 4) |
| porterage | 13 @ 1.1, stop - |  | goal planner: buys 13 for today's rates (v2 had 12) |
| rope |  | 4 @ min 67.5 | makes 2.0, uses 0.2, holds 32 (keeps 0): sells the surplus + 3/turn of the excess |
| thread |  | 9 @ min 4.1 | goal planner: sells 9 a turn at 4.1, keeps 221 (no one offered it) |
| tools | 2 @ 6.2, stop 16 |  | uses 2.0/turn (net maker152202386007001, retting pit 1), makes 0.0, holds 199 = 101.6 turns |
| varnish | 1 @ 19.0, stop 1 |  | uses 0.1/turn (net maker152202386007001), makes 0.0, holds 1 = 4.2 turns |
| wax | 1 @ 20.6, stop 1 |  | uses 0.1/turn (net maker152202386007001), makes 0.0, holds 1 = 7.0 turns |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 17.9k (cash + stock at home prices); +50/turn over 6 turns, +67/turn over 24 turns.
- Limits: cash flow >= +132/turn, prestige >= -0.64/turn (values are after 240 tax a turn).
- Today's settings: value -2/turn, cash -11/turn, prestige -0.63/turn - breaks the cash floor.
- Plan: value +41/turn, cash +132/turn, prestige -0.64/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +1 vs +20, -167 vs +11, -144 vs +6 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4, garments 0.5, nets 0.0, rope 0.1.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Boistot: +8/turn
  - brewery 1 0.63 -> 0.49: +25/turn
  - logging camp w/ tool 5.00 -> 0.00: +4/turn
  - logging camp w/ tool [split timber 1] 0.00 -> 2.71: +2/turn
  - sewing shop 1 0.21 -> 0.10: -12/turn
  - weavery 1 0.33 -> 0.22: +6/turn
  - spinnery 1 1.70 -> 1.21: -2/turn
  - retting pit 1 0.83 -> 0.59: +8/turn
  - flax farm 1 4.60 -> 3.38: +9/turn
- Model check over the last 29 turns: predicted +126/turn for the settings we ran, real +58/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.60, thread 3.98, cloth 6.37, flax fibres 4.66, garments 18.47, nets 29.33, beer 2.82, timber 5.59, prestige 55.93, cash 0.03
- Orders it would set: cured meat buy 1 (v2 2); furniture buy 2 (v2 None); garments sell 7 (v2 6); grain buy 32 (v2 83); labour buy 95 (v2 94); light armour buy 1 (v2 None); pasties buy 3 (v2 4); porterage buy 13 (v2 12); thread sell 9 (v2 none)
- Recipe: logging camp w/ tool cut firewood 1 -> split timber 1 at 2.71, worth +3/turn.
- Ship linen snake: Grandgues -> Boistot (+8/turn over staying).
- Ship Flax Wyrm: stays on Caillechâtel (worth +7/turn).
- Management: ~13.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +79/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
- Trim: donate quarry 1: +20/turn (tax 20 saved).
- Trim: donate logging camp w/ tool: +18/turn (tax 20 saved).

## Chain sizing

Mode HOLD, garments sold 8.2/turn (+0.0 exported); plan makes 0.0 garments a turn.
Labour: own 500, everything else 434, chain may buy 0 -> chain allowance 66, chain plan 94 (-166 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.60 | 2.14 |
| ret | 3 | 0.83 | 0.38 |
| spin | 4 | 1.70 | 0.79 |
| weave | 3 | 0.33 | 0.00 |
| sew | 2 | 0.21 | 0.00 |

Buffers: flax fibres 35/47, thread 812/138, cloth 12/0
- chain plan needed 94 labour, budget left 66: cut to 94

## Self-diagnosis

Nothing found this run.
