# v2 shadow report

Turn 13522, 2026-10-24 19:52. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 713, prestige 3,575 (455 free, -0.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 7 | 0 | 0 | min_holding 60, sell 82, sell @ 2.98 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 12 | 3 | 6 | 2 | 0 | stop 16, buy 2, buy @ 2.4; sell 4, sell @ 1.7 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 38 | 0 | 2 | 0 | 0 | min_holding 30, sell 8, sell @ 17.8 |
| grain | 109 | 10 | 22 | 0 | 0 | stop 145, buy 10, buy @ 3.7 |
| labour | 95 | 95 | 555 | 0 | 40 | buy 65, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 15 | 0 | 0 | 0 | 0 | min_holding 15, sell 12, sell @ 34 |
| porterage | 13 | 13 | 12 | 0 | 1 | buy 13, buy @ 1.1 |

**1 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), 3 bought last turn); labour need rises ~82/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it

## Waste (money lost now)

- **labour**: 40 labour expired last turn (~62 coin): holding 95 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **cloth**: cloth buffer thin: 1.1 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 33
- **flax fibres**: flax fibres buffer thin: 1.2 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 57

## Notes

- labour: projection runs 90 over real use lately; planning 604, not 694
- labour expiry guard: 40 bought labour expired last turn, buy 55 (not 104) this turn

## Prestige spending, cheapest coin per prestige first

879 turns left: prestige gained now converts 98.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 45.9 | 45.9 | running |
| hold banquet 4 (pies) | mansion | 18 | 49.2 | 49.2 | thin at home: hop beer, wine, pies |
| hold banquet 3 (pies) | mansion | 8 | 50.1 | 50.1 | thin at home: hop beer, pies |
| hold banquet 2 (pies) | mansion | 7 | 51.0 | 51.0 | thin at home: wine, pies |
| jousting 3 | arena | 230 | 52.0 | 52.1 | needs a arena (build cost 24,311); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 52.6 | 52.6 | thin at home: wine, hop beer, stockfish |
| hold prayer 2 | chapel | 13 | 50.2 | 53.2 | needs a chapel (build cost 31,452); thin at home: furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 53.5 | 53.5 | thin at home: wine |
| hold banquet 3 (fish) | mansion | 7.6 | 53.7 | 53.7 | thin at home: hop beer |
| hold sermon 2 (candles) | church | 31 | 51.0 | 53.7 | needs a church (build cost 66,029); thin at home: candles, furniture |
| hold banquet 2 (meat) | mansion | 6.8 | 54.4 | 54.4 | thin at home: wine |
| hold banquet 3 (meat) | mansion | 7.6 | 54.5 | 54.5 | thin at home: hop beer |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only -3 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~96 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.30 | 0.30 (29/turn) | rope 4 (53.98->68.4), yarn 16 (3.65->5.08), glass ingots 2 (59.33->68.4), lead ore 4 (8.09->11.49) | beer 6 (2.25->3.5), gears 2 (59.85->61.27), candles 1 (67.2->68.5), tar 3 (9.55->10.54) | +114 |
| Boistot | 1230 | 0.42 | 0.10 (10/turn) | rope 4 (53.98->69.35), thread 7 (4.1->5.32), yarn 5 (3.65->4.31) | lathes 1 (178.5->205.2), belts 2 (16.8->24.13), pasties 2 (8.45->13.3) | +107 |
| Bremcop | 1326 | 0.47 | 0.20 (19/turn) | rope 3 (53.98->74.58), gold ore 1 (156.45->165.3), cloth 1 (6.8->7.98), lead ore 2 (8.09->10.92) | lathes 1 (168->205.2), candles 1 (67.2->68.5), tar 3 (9.4->10.54), casks 3 (4.89->5.98) | +101 |
| Herschweig | 775 | 0.20 | 0.10 (10/turn) | rope 3 (53.98->72.67), tackles 1 (185.85->214.7), nets 2 (35.6->37.05), lead ore 1 (8.09->10.07) | tar 3 (9.29->10.54), candles 1 (67.2->68.5), cheese 8 (5.35->5.7), furniture 1 (11.65->13.4) | +96 |
| Pontmont | 341 | 0.09 | 0.20 (19/turn) | rope 4 (53.98->70.3), limestone 2 (18.17->28.5), beer 40 (2.98->3.38), lead ore 2 (8.09->9.59) | candles 1 (68.25->68.5), pasties 2 (13.02->13.3), tiles 1 (3.49->4.6) | +89 |

**Best:** Hofkirchen at about +114 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 25.6, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 4.0 turns |
| beer |  | 69 @ min 2.98 | goal planner: sells 69 a turn at 2.98, keeps 60 (no one offered it) |
| cured meat | 1 @ 29.0, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 2) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 2 @ 2.4, stop 16 | 4 @ min 1.72 | uses 7.9/turn (household upkeep), makes 6.5, holds 12 = 9.2 turns |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 8 @ min 17.8 | goal planner: sells 8 at 17.8 (v2 had 7 at 20.0) |
| grain | 36 @ 3.7, stop 141 |  | goal planner: buys 36 a turn for today's rates, keeps up to 141 (v2 had 69) |
| labour | 95 @ 2.2, stop - |  | goal planner: buys 95 for today's rates (v2 had 55) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 12 @ min 34 | goal planner: sells 12 at 34 (v2 had 12 at 34.6) |
| pasties | 3 @ 14.5, stop 11 |  | goal planner: buys 3 a turn for today's rates, keeps up to 11 (v2 had 4) |
| porterage | 13 @ 1.1, stop - |  | goal planner: buys 13 for today's rates (v2 had 12) |
| rope |  | 4 @ min 67.5 | makes 2.0, uses 0.2, holds 31 (keeps 0): sells the surplus + 2/turn of the excess |
| thread |  | 8 @ min 4.1 | goal planner: sells 8 a turn at 4.1, keeps 221 (no one offered it) |
| tools | 2 @ 6.2, stop 16 |  | uses 2.0/turn (net maker152202386007001, retting pit 1), makes 0.0, holds 199 = 101.4 turns |
| varnish | 1 @ 17.1, stop 1 |  | uses 0.1/turn (net maker152202386007001), makes 0.0, holds 1 = 5.2 turns |
| wax | 1 @ 20.6, stop 1 |  | uses 0.1/turn (net maker152202386007001), makes 0.0, holds 1 = 8.0 turns |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 18.0k (cash + stock at home prices); +24/turn over 6 turns, +78/turn over 24 turns.
- Limits: cash flow >= +137/turn, prestige >= -0.65/turn (values are after 240 tax a turn).
- Today's settings: value +14/turn, cash +6/turn, prestige -0.63/turn - breaks the cash floor.
- Plan: value +41/turn, cash +137/turn, prestige -0.65/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +1 vs +20, -167 vs +11, -144 vs +6 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4, garments 0.5, nets 0.0, rope 0.1.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Boistot: +9/turn
  - brewery 1 0.63 -> 0.54: +16/turn
  - logging camp w/ tool 5.00 -> 5.47: +0/turn
  - sewing shop 1 0.21 -> 0.13: -8/turn
  - weavery 1 0.33 -> 0.25: +4/turn
  - spinnery 1 1.70 -> 1.16: -9/turn
  - retting pit 1 0.83 -> 0.56: +9/turn
  - flax farm 1 4.60 -> 3.25: +11/turn
- Model check over the last 27 turns: predicted +128/turn for the settings we ran, real +65/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.64, thread 4.03, cloth 6.49, flax fibres 4.64, garments 18.84, nets 29.79, beer 2.89, timber 6.88, prestige 57.51, cash 0.06
- Orders it would set: beer sell 69 (v2 none); cured meat buy 1 (v2 2); furniture buy 2 (v2 None); garments sell 8 (v2 7); grain buy 36 (v2 69); labour buy 95 (v2 55); light armour buy 1 (v2 None); pasties buy 3 (v2 4); porterage buy 13 (v2 12); thread sell 8 (v2 none)
- Ship linen snake: Grandgues -> Boistot (+9/turn over staying).
- Ship Flax Wyrm: stays on Caillechâtel (worth +6/turn).
- Management: ~13.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +81/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
- Trim: donate quarry 1: +20/turn (tax 20 saved).
- Trim: donate logging camp w/ tool: +18/turn (tax 20 saved).

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

Buffers: flax fibres 35/47, thread 772/138, cloth 19/0
- chain plan needed 94 labour, budget left 66: cut to 94

## Self-diagnosis

Nothing found this run.
