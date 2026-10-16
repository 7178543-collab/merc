# v2 shadow report

Turn 13319, 2026-10-16 08:59. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,035, prestige 3,234 (564 free, +45.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 279 | 0 | 4 | 0 | 0 | min_holding 60, sell 40, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 17, sell @ 24.6 |
| grain | 55 | 0 | 13 | 0 | 0 | stop 52, buy 13, buy @ 3.7 |
| labour | 286 | 255 | 705 | 21 | 0 | buy 286, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 37 | 0 | 0 | 0 | 0 | min_holding 15, sell 10, sell @ 38.2 |
| porterage | 21 | 21 | 21 | 0 | 0 | buy 21, buy @ 1.1 |

**2 risks, 0 waste, 4 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.3 turns (holds 10, next step uses 38/turn) -> v2: check the step that makes it
- **labour**: buying 286, short of ~349 needed -> v2: buy 349

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.9 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 68
- **flax plants**: flax plants buffer thin: 2.0 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 174
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **tar**: home ask 11.30 is above our ceiling 11.00 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Prestige spending, cheapest coin per prestige first

1082 turns left: prestige gained now converts 99.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 52.5 | 52.5 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 58.6 | 58.6 |  |
| hold banquet 2 (meat) | mansion | 6.8 | 58.8 | 58.8 |  |
| hold banquet 1 (fish) | mansion | 4.2 | 60.8 | 60.8 |  |
| hold feast 2 | townhouse | 2.6 | 58.8 | 61.3 | needs a townhouse (build cost 6,768); thin at home: wine |
| hold banquet 3 (fish) | mansion | 7.6 | 61.5 | 61.5 | thin at home: hop beer |
| hold banquet 2 (pies) | mansion | 7 | 61.7 | 61.7 | thin at home: pasties, pies |
| hold banquet 3 (meat) | mansion | 7.6 | 61.7 | 61.7 | thin at home: hop beer |
| hold banquet 1 (meat) | mansion | 4.2 | 61.8 | 61.8 |  |
| hold banquet 3 (pies) | mansion | 8 | 63.0 | 63.0 | thin at home: pasties, hop beer, pies |
| hold mass 2 (premium) | cathedral | 360 | 62.0 | 63.0 | needs a cathedral (build cost 358,201); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold sermon 2 (candles) | church | 31 | 60.9 | 63.6 | needs a church (build cost 81,490); thin at home: jewellery, candles, furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 74001604 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Brunnham: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~104 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Gosschweig | 1099 | 0.39 | 0.10 (10/turn) | thread 5 (4.4->5.32), varnish 2 (18.17->19.38), scythes 1 (28.14->29.64) | candles 4 (56.7->68.4), garments 2 (22.68->26.4), medicine 2 (120.75->123.5), soap 1 (105->107.35) | +62 |
| Grandgues | 152 | 0.04 | 0.30 (31/turn) | bread 140 (2.44->2.91), firewood 1 (1.7->5.79), logs 1 (3.24->6.7), bricks 1 (4.54->7.55) | pies 1 (17.22->17.39) | +49 |
| Bordees | 1112 | 0.39 | 0.10 (10/turn) | tackles 1 (176.4->207.1), rope 1 (76.5->81.7), cured meat 2 (23.2->25.46), salt 6 (4.16->4.66) | - | +35 |
| Hanstein | 380 | 0.10 | 0.10 (10/turn) | thread 69 (4.4->4.8), charcoal 2 (1.82->3.44) | garments 2 (23.31->26.4), gears 1 (69.83->73.62), flour 1 (17.01->18.43), resin 1 (0.99->2.17) | +34 |
| Hofkirchen | 991 | 0.33 | 0.20 (21/turn) | hop beer 3 (11.03->13.59), steel ingots 2 (14.18->16.43), tools 16 (5.1->5.56), varnish 1 (18.17->20.9) | garments 2 (22.05->26.4), cloth 13 (7.77->8.45), jewellery 1 (78.75->81.22), soap 1 (105->107.35) | +33 |

**Best:** Gosschweig at about +62 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 40 @ min 3.7 | makes 28.0, uses 4.2, holds 279 (keeps 60): sells the surplus + 16/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 17 @ min 22.4 |  |
| grain | 13 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 55 = 4.2 turns |
| labour | 349 @ 2.2, stop - |  | uses 799.0/turn (brewery 1, flax farm 1, household), makes 450.0, holds 286 = 0.8 turns |
| limestone |  | 5 @ min 17.4 |  |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 10 @ min 38.2 | makes 9.0, uses 0.0, holds 37 (keeps 15): sells the surplus + 1/turn of the excess |
| porterage | 21 @ 1.1, stop - |  | uses 20.8/turn (observed), makes 0.0, holds 21 = 1.0 turns |
| rope |  | 4 @ min 74.5 |  |
| tar | 1 @ 11.0, stop 4 |  | uses 1.0/turn (ropewalk 1), makes 0.0, holds 7 = 6.7 turns |
| timber |  | 37 @ min 8.5 | makes 12.0, uses 0.0, holds 667 (keeps 350): sells the surplus + 25/turn of the excess |
| tools | 5 @ 6.2, stop 36 |  | uses 4.4/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 45.0 turns |

## Chain sizing

Mode HOLD, garments sold 1.8/turn (+0.0 exported); plan makes 19.7 garments a turn.
Labour: own 450, everything else 429, chain may buy 350 -> chain allowance 371, chain plan 371 (-1 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.49 | 5.44 |
| ret | 3 | 0.97 | 0.97 |
| spin | 4 | 2.00 | 1.99 |
| weave | 3 | 0.76 | 0.77 |
| sew | 2 | 0.47 | 0.48 |

Buffers: flax fibres 64/88, thread 674/259, cloth 10/77
- chain plan needed 511 labour, budget left 371: cut to 371 (sewing capped at 0.48)

## Self-diagnosis

- R1: candles slot dry: 0.0 held, 1.5 a turn (luxury slot (+3 prestige)); our buy paused by the failsafe, home ask 73.0 (held back: paused by the failsafe at level 1: un-pause only at level 0)
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
