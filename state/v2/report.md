# v2 shadow report

Turn 13533, 2026-10-25 06:25. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 3,446, prestige 3,568 (448 free, -0.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 7 | 0 | 0 | min_holding 60, sell 55, sell @ 2.98 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 8 | 0 | 6 | 0 | 0 | buy @ 2.4; sell 1, sell @ 1.75 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 7, sell @ 17.8 |
| grain | 30 | 28 | 29 | 0 | 0 | stop 108, buy 27, buy @ 3.7 |
| labour | 0 | 6 | 501 | 0 | 5 | buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 15 | 0 | 0 | 0 | 0 | min_holding 15, sell 12, sell @ 34 |
| porterage | 11 | 11 | 11 | 0 | 0 | buy 11, buy @ 1.1 |

**1 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: sewing shop 1 ran short of cloth (no buy order); labour need rises ~32/turn when they restart -> v2: add a cloth buy

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.6 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 43

## Notes

- labour: +0 crew for linen snake (crew 0.00, no projection from the game)
- labour: projection runs 100 over real use lately; planning 501, not 600

## Prestige spending, cheapest coin per prestige first

868 turns left: prestige gained now converts 98.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.1 | 47.1 | running |
| hold banquet 3 (pies) | mansion | 8 | 50.0 | 50.0 | thin at home: hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 50.2 | 50.2 | thin at home: hop beer, wine, pies |
| hold banquet 2 (pies) | mansion | 7 | 51.2 | 51.2 | thin at home: wine, pies |
| jousting 3 | arena | 230 | 52.6 | 52.7 | needs a arena (build cost 23,966); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 53.7 | 53.7 | thin at home: hop beer |
| hold banquet 4 | mansion | 17.5 | 53.7 | 53.7 | thin at home: wine, hop beer, stockfish |
| hold banquet 2 (fish) | mansion | 6.8 | 54.3 | 54.3 | thin at home: wine |
| hold banquet 3 (meat) | mansion | 7.6 | 54.3 | 54.3 | thin at home: hop beer |
| hold prayer 2 | chapel | 13 | 51.9 | 54.7 | needs a chapel (build cost 30,001); thin at home: furniture |
| hold banquet 2 (meat) | mansion | 6.8 | 55.0 | 55.0 | thin at home: wine |
| hold sermon 2 (candles) | church | 31 | 53.0 | 55.5 | needs a church (build cost 62,068); thin at home: candles, furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only 8 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only 3 a turn after crew: ship stays at 0
- best towns now: Etallaen +26, Marmont +19, Cobholme +18, Hanbrücken +18, Dortgart +17
- Etallaen would trade: candles buy 1 @ 62.0, rope sell 2 @ 79.0; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~97 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.50 (49/turn) | firewood 29 (1.84->4.31), charcoal 11 (1.97->4.29), wrought iron 3 (14.7->16.34), bricks 6 (4.49->5.84) | medicine 2 (143.85->157.7), candles 1 (69.3->78.5), mouldboards 2 (31.71->34.2), salt 3 (4.51->5.56) | +113 |
| Darmwald | 1022 | 0.32 | 0.30 (29/turn) | grindstones 1 (256.2->361), steel ingots 1 (13.44->14.63), tiles 2 (3.34->6.84), malt 1 (5.83->6.89) | medicine 1 (145.95->157.7), candles 1 (74.03->78.5), salt 5 (4.51->5.56), garments 2 (19.32->20) | +111 |
| Cobholme | 1564 | 0.61 | 0.10 (10/turn) | rope 2 (69.5->84.55), malt 1 (5.83->7.41) | medicine 1 (130.2->157.7), bellows 1 (260.4->285), candles 1 (66.67->78.5) | +86 |
| Neuborn | 780 | 0.20 | 0.30 (29/turn) | garments 3 (18.2->27.17), cookware 11 (23.52->25.46), charcoal 11 (1.97->4.75), seeds 12 (2.44->3.32) | flax fibres 9 (4.91->5.8), candles 1 (77.7->78.5), salt 2 (4.89->5.56), thread 9 (4.35->4.66) | +71 |
| Fontaux | 411 | 0.11 | 0.80 (78/turn) | cookware 6 (23.52->26.22), charcoal 11 (1.97->3.53), firewood 19 (1.84->5.32), cheese 10 (6.04->6.37) | medicine 1 (137.55->157.7), candles 1 (68.25->78.5), salt 5 (4.37->5.56), mouldboards 2 (33.81->34.2) | +67 |

**Best:** Grandgues at about +113 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 27.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 55 @ min 2.98 | goal planner: sells 55 at 2.98 (v2 had 55 at 3.38) |
| cured meat | 1 @ 29.0, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 2) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 0 @ 2.4, stop 13 | 1 @ min 1.75 | uses 6.3/turn (brewery 1, household upkeep), makes 6.5, holds 8 |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.4 | goal planner: sells 2 a turn at 1.4, keeps 167 (no one offered it) |
| furniture | 2 @ 13.8, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| grain | 28 @ 3.7, stop 109 |  | goal planner: buys 28 a turn for today's rates, keeps up to 109 (v2 had 58) |
| labour | 12 @ 2.2, stop - |  | goal planner: buys 12 for today's rates (v2 had 1) |
| light armour | 1 @ 87, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 12 @ min 34 | goal planner: sells 12 at 34 (v2 had 12 at 34.6) |
| pasties | 3 @ 14.5, stop 11 |  | goal planner: buys 3 a turn for today's rates, keeps up to 11 (v2 had 4) |
| porterage | 11 @ 1.1, stop - |  | goal planner: buys 11 for today's rates (v2 had 11) |
| rope |  | 3 @ min 67.5 | goal planner: sells 3 (v2 had 2) |
| thread |  | 12 @ min 4.5 | goal planner: sells 12 a turn at 4.5, keeps 206 (no one offered it) |
| tools | 2 @ 6.2, stop 13 |  | uses 1.5/turn (net maker152202386007001, retting pit 1), makes 0.0, holds 200 = 130.3 turns |
| varnish | 1 @ 20.4, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| wax | 1 @ 21.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 18.5k (cash + stock at home prices); +92/turn over 6 turns, +48/turn over 24 turns.
- Limits: cash flow >= +23/turn, prestige >= -0.62/turn (values are after 240 tax a turn).
- Today's settings: value +22/turn, cash +137/turn, prestige -0.59/turn.
- Plan: value +57/turn, cash +72/turn, prestige -0.62/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +514 vs -53, +351 vs +99, +552 vs +130.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4, nets 0.0, rope 0.1.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Bedenis: +2/turn
  - net maker 0.50 -> 0.69: +3/turn
  - sewing shop 1 0.21 -> 0.09: +5/turn
  - logging camp w/ tool 5.00 -> 4.71: -0/turn
  - flax farm 1 3.55 -> 5.48: -13/turn
  - retting pit 1 0.62 -> 0.96: -6/turn
  - spinnery 1 1.28 -> 1.98: +0/turn
  - ropewalk 1 0.50 -> 0.00: -99/turn
  - ropewalk 1 [make rope 2] 0.00 -> 0.76: +136/turn
- Model check over the last 38 turns: predicted +108/turn for the settings we ran, real +61/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.57, thread 3.87, cloth 6.22, flax fibres 4.45, garments 18.08, nets 28.71, beer 2.78, timber 2.88, prestige 55.01, cash 0.00
- Orders it would set: cured meat buy 1 (v2 2); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); grain buy 28 (v2 58); labour buy 12 (v2 1); light armour buy 1 (v2 None); pasties buy 3 (v2 4); rope sell 3 (v2 2); thread sell 12 (v2 none)
- Recipe: ropewalk 1 make rope 1 -> make rope 2 at 0.76, worth +32/turn.
- Ship linen snake: Grandgues -> Bedenis (+4/turn over staying).
- Ship Flax Wyrm: stays on Caillechâtel (worth +3/turn).
- Management: ~13.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +78/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
- Trim: donate quarry 1: +19/turn (tax 20 saved).
- Trim: donate logging camp w/ tool: +17/turn (tax 20 saved).
- Trim: donate weavery 1: +11/turn (tax 18 saved).

## Chain sizing

Mode HOLD, garments sold 7.0/turn (+0.0 exported); plan makes 30.3 garments a turn.
Labour: own 500, everything else 409, chain may buy 350 -> chain allowance 441, chain plan 440 (+238 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 3.55 | 5.39 |
| ret | 3 | 0.62 | 0.96 |
| spin | 4 | 1.28 | 1.97 |
| weave | 3 | 0.22 | 1.19 |
| sew | 2 | 0.21 | 0.74 |

Buffers: flax fibres 35/87, thread 791/257, cloth 0/119
- chain plan needed 465 labour, budget left 441: cut to 441 (sewing capped at 0.74)

## Self-diagnosis

Nothing found this run.
