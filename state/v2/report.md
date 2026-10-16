# v2 shadow report

Turn 13314, 2026-10-16 03:15. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,552, prestige 3,085 (415 free, -7.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 346 | 0 | 4 | 0 | 0 | min_holding 60, sell 48, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 0 | 3 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 54 | 0 | 2 | 0 | 0 | min_holding 80, sell 2, sell @ 22 |
| grain | 103 | 0 | 0 | 0 | 0 | stop 52, buy 13, buy @ 3.7 |
| labour | 54 | 22 | 472 | 225 | 0 | buy 54, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 42 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 40.4 |
| porterage | 21 | 6 | 6 | 0 | 0 | buy 21, buy @ 1.1 |

**2 risks, 0 waste, 5 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.3 turns (holds 9, next step uses 32/turn) -> v2: check the step that makes it
- **labour**: buying 54, short of ~269 needed -> v2: buy 269

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.8 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 70
- **flax plants**: flax plants buffer thin: 1.9 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 181
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **timber**: build materials for park 1 are in (692.0 held, 4 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 91% (EXPANSION), about 2 turns left; still to deliver: labour 24, limestone 6, timber 4; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 6 | 107.5 | 0 | off: covered |
| timber | 4 | 692.0 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 12

## Notes

- labour: projection runs 54 over real use lately; planning 719, not 772

## Prestige spending, cheapest coin per prestige first

1087 turns left: prestige gained now converts 99.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.8 | 53.3 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 58.0 | 58.0 |  |
| hold banquet 4 (pies) | mansion | 18 | 58.6 | 58.6 | thin at home: pasties, hop beer |
| hold sermon 2 (candles) | church | 31 | 56.4 | 58.7 | needs a church (build cost 71,421); thin at home: jewellery, candles, furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 58.9 | 58.9 |  |
| hold banquet 2 (pies) | mansion | 7 | 59.3 | 59.3 | thin at home: pasties, pies |
| hold prayer 2 | chapel | 13 | 57.1 | 59.6 | needs a chapel (build cost 33,407); thin at home: furniture |
| hold banquet 3 (pies) | mansion | 8 | 59.7 | 59.7 | thin at home: pasties, hop beer, pies |
| hold mass 2 (premium) | cathedral | 360 | 59.5 | 60.3 | needs a cathedral (build cost 285,980); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold sermon 2 | church | 24 | 57.4 | 60.3 | needs a church (build cost 71,421); thin at home: jewellery, furniture |
| hold banquet 3 (fish) | mansion | 7.6 | 60.7 | 60.7 | thin at home: hop beer |
| jousting 3 | arena | 230 | 60.6 | 60.7 | needs a arena (build cost 26,357); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 74001604 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Brunnham: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~103 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hanstein | 380 | 0.10 | 0.30 (31/turn) | timber 15 (6.15->10.45), soap 1 (98.17->102.6), charcoal 2 (1.82->3.5), yarn 3 (4.16->5.08) | cheese 39 (5.88->6.46), seeds 9 (1.81->2.32) | +71 |
| Hofkirchen | 991 | 0.33 | 0.20 (21/turn) | hop beer 5 (11.03->19.38), tallow 3 (28.77->31.16), grain 8 (2.66->3.65), steel ingots 8 (14.18->14.82) | acid 2 (165.9->172.9), jewellery 2 (82.42->84.08), garments 2 (22.05->22.6) | +65 |
| Angefont | 686 | 0.19 | 0.10 (10/turn) | cookware 10 (24.57->28.31), garments 14 (21.6->22.99), yarn 6 (4.16->4.89), blades 3 (16.28->16.62) | cloth 12 (7.35->8.1), thread 18 (4.73->4.96) | +64 |
| Gosschweig | 1099 | 0.39 | 0.10 (10/turn) | - | candles 4 (56.7->70.77), medicine 1 (147->151.05) | +51 |
| Calange | 218 | 0.06 | 0.10 (10/turn) | garments 14 (21.6->23.94), soap 1 (98.17->110.2), yarn 6 (4.16->5.22), cured meat 2 (25->25.84) | cloth 6 (7.88->8.1) | +47 |

**Best:** Hanstein at about +71 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 46 @ min 3.7 | makes 28.0, uses 4.2, holds 346 (keeps 60): sells the surplus + 22/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 14 @ min 22.0 |  |
| grain | 13 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 103 = 7.9 turns |
| labour | 269 @ 2.2, stop - |  | uses 718.9/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 54 = 0.2 turns |
| limestone |  | 5 @ min 17.4 |  |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 11 @ min 39.8 | makes 9.0, uses 0.0, holds 42 (keeps 15): sells the surplus + 2/turn of the excess |
| porterage | 6 @ 1.1, stop - |  | uses 6.1/turn (observed), makes 0.0, holds 21 = 3.5 turns |
| rope |  | 4 @ min 74.0 |  |
| tar | 2 @ 11.0, stop 4 |  | uses 1.0/turn (ropewalk 1), makes 0.0, holds 2 = 2.0 turns |
| timber |  | 40 @ min 8.5 | makes 12.0, uses 0.0, holds 692 (keeps 350): sells the surplus + 28/turn of the excess |
| tools | 5 @ 6.2, stop 37 |  | uses 4.5/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 44.1 turns |

## Chain sizing

Mode HOLD, garments sold 1.2/turn (+0.0 exported); plan makes 18.9 garments a turn.
Labour: own 450, everything else 426, chain may buy 350 -> chain allowance 374, chain plan 373 (+15 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.69 | 5.61 |
| ret | 3 | 1.01 | 1.00 |
| spin | 4 | 2.08 | 2.05 |
| weave | 3 | 0.63 | 0.74 |
| sew | 2 | 0.40 | 0.46 |

Buffers: flax fibres 63/87, thread 561/256, cloth 9/74
- chain plan needed 633 labour, budget left 374: cut to 374 (sewing capped at 0.46)

## Self-diagnosis

- R1: candles slot dry: 0.0 held, 1.5 a turn (luxury slot (+3 prestige)); our buy paused by the failsafe, home ask 77.0 (held back: paused by the failsafe at level 1: un-pause only at level 0)
- R1: prestige rate -7.05 a turn vs 12-turn median -0.96; likely: dry slot: candles
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R4: logging camp w/ tool, ropewalk 1, quarry 1 projected 0: short of labour (~103 needed); labour itself is not raised here
