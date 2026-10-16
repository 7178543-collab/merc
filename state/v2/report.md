# v2 shadow report

Turn 13313, 2026-10-16 02:57. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,406, prestige 3,092 (422 free, -5.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 379 | 0 | 4 | 0 | 0 | min_holding 60, sell 51, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 20 | 4 | 3 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 39 | 0 | 2 | 0 | 0 | min_holding 80, sell 2, sell @ 22 |
| grain | 103 | 13 | 0 | 0 | 0 | stop 52, buy 13, buy @ 3.7 |
| labour | 22 | 80 | 530 | 162 | 0 | buy 22, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 46 | 0 | 0 | 0 | 0 | min_holding 15, sell 8, sell @ 36.6 |
| porterage | 6 | 26 | 6 | 0 | 20 | buy 6, buy @ 1.1 |

**3 risks, 0 waste, 6 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.3 turns (holds 9, next step uses 32/turn) -> v2: check the step that makes it
- **labour**: buying 22, short of ~264 needed -> v2: buy 264
- **porterage**: buying 6, short of ~21 needed -> v2: buy 21

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.8 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 69
- **flax plants**: flax plants buffer thin: 1.9 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 178
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.30 is above our ceiling 11.00 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **timber**: build materials for park 1 are in (698.0 held, 7 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 83% (EXPANSION), about 3 turns left; still to deliver: labour 45, limestone 11, timber 7; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 11 | 107.5 | 0 | off: covered |
| timber | 7 | 698.0 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 15

## Notes

- labour: projection runs 54 over real use lately; planning 714, not 767

## Prestige spending, cheapest coin per prestige first

1088 turns left: prestige gained now converts 99.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.2 | 53.5 | running |
| hold banquet 2 (pies) | mansion | 7 | 57.4 | 57.4 | thin at home: pasties, pies, candles |
| hold banquet 4 (pies) | mansion | 18 | 58.0 | 58.0 | thin at home: pasties, hop beer, candles |
| hold banquet 1 (fish) | mansion | 4.2 | 58.1 | 58.1 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 58.1 | 58.1 |  |
| hold banquet 3 (pies) | mansion | 8 | 58.8 | 58.8 | thin at home: pasties, hop beer, pies, candles |
| hold sermon 2 (candles) | church | 31 | 57.0 | 59.3 | needs a church (build cost 70,326); thin at home: jewellery, candles, furniture |
| hold prayer 2 | chapel | 13 | 57.3 | 59.7 | needs a chapel (build cost 32,738); thin at home: furniture |
| hold mass 2 (premium) | cathedral | 360 | 59.6 | 60.4 | needs a cathedral (build cost 282,980); thin at home: furniture, jewellery, glassware, candles, premium garments |
| jousting 3 | arena | 230 | 60.5 | 60.6 | needs a arena (build cost 25,719); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 60.7 | 60.7 | thin at home: hop beer |
| hold sermon 2 | church | 24 | 57.8 | 60.7 | needs a church (build cost 70,326); thin at home: jewellery, furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 74001604 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Brunnham: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn; best orders clear only -10 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~104 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hanstein | 380 | 0.11 | 0.30 (31/turn) | timber 15 (6.4->10.54), tackles 1 (174.3->195.7), charcoal 2 (1.81->3.52), flax fibres 5 (4.79->5.37) | wrought iron 8 (13.65->15.39), butter 1 (67.2->78.85), seeds 9 (1.8->2.32), thread 55 (4.79->4.94) | +95 |
| Neuborn | 780 | 0.22 | 0.20 (21/turn) | steel ingots 2 (14.18->17.48), limestone 1 (18.06->28.5), grain 8 (2.64->3.17), charcoal 2 (1.81->3.63) | cheese 85 (5.51->6.46), wrought iron 5 (14.28->15.39), wheels 2 (22.26->23.18) | +76 |
| Kleinburgh | 1440 | 0.58 | 0.10 (10/turn) | tallow 2 (28.77->33.25), varnish 2 (18.17->21.85), glassware 4 (63->64.12) | jewellery 2 (75.6->84.55), gears 1 (59.33->74.1), wrought iron 8 (13.02->15.39) | +60 |
| Brunnham | 1281 | 0.49 | 0.10 (10/turn) | tallow 3 (28.77->31.16), lead bars 1 (12.35->13.59) | wrought iron 8 (13.02->15.39), jewellery 2 (78.75->84.55), butter 1 (68.25->78.85) | +39 |
| Cobholme | 1564 | 0.65 | 0.10 (10/turn) | varnish 1 (18.17->23.75), blades 2 (16.38->19), lead bars 1 (12.35->13.59), tallow 1 (28.77->30.4) | butter 1 (56.7->78.85), jewellery 1 (78.75->84.55), wrought iron 4 (13.86->15.39) | +38 |

**Best:** Hanstein at about +95 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 28.2, stop 1 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 3.0 turns |
| beer |  | 48 @ min 3.7 | makes 28.0, uses 4.2, holds 379 (keeps 60): sells the surplus + 25/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 20 = 4.7 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 14 @ min 22.0 |  |
| grain | 13 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 103 = 7.9 turns |
| labour | 264 @ 2.2, stop - |  | uses 713.8/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 22 = 0.1 turns |
| limestone |  | 5 @ min 17.4 |  |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 11 @ min 40.4 | makes 9.0, uses 0.0, holds 46 (keeps 15): sells the surplus + 2/turn of the excess |
| porterage | 21 @ 1.1, stop - |  | uses 20.8/turn (observed), makes 0.0, holds 6 = 0.3 turns |
| rope |  | 4 @ min 79.0 |  |
| tar | 2 @ 11.0, stop 4 |  | uses 1.0/turn (ropewalk 1), makes 0.0, holds 0 = 0.0 turns |
| timber |  | 40 @ min 8.5 | makes 12.0, uses 0.0, holds 698 (keeps 350): sells the surplus + 28/turn of the excess |
| tools | 5 @ 6.2, stop 36 |  | uses 4.5/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 44.5 turns |

## Chain sizing

Mode HOLD, garments sold 1.5/turn (+0.0 exported); plan makes 18.0 garments a turn.
Labour: own 450, everything else 429, chain may buy 350 -> chain allowance 371, chain plan 371 (+18 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.56 | 5.69 |
| ret | 3 | 0.99 | 1.01 |
| spin | 4 | 2.04 | 2.08 |
| weave | 3 | 0.63 | 0.71 |
| sew | 2 | 0.40 | 0.44 |

Buffers: flax fibres 63/86, thread 520/253, cloth 9/71
- chain plan needed 687 labour, budget left 371: cut to 371 (sewing capped at 0.44)

## Self-diagnosis

- R1: candles slot dry: 0.0 held, 1.5 a turn (luxury slot (+3 prestige)); our buy paused by the failsafe, home ask none (no sellers at home)
- R1: prestige rate -5.00 a turn vs 12-turn median -0.95; likely: dry slot: candles
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R4: logging camp w/ tool, ropewalk 1, quarry 1 projected 0: short of labour (~103 needed); acted on sewing shop 1 at turn 13312 (one action per 2 turns); acted on weavery 1 at turn 13312 (one action per 2 turns); labour itself is not raised here
