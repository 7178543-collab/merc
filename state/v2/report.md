# v2 shadow report

Turn 13273, 2026-10-14 10:58. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, meat, nets, porterage; v1 runs everything else.
Cash 14,296, prestige 2,811 (141 free, -0.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 316 | 0 | 4 | 0 | 0 | min_holding 60, sell 60, sell @ 3.7 |
| cured fish | 6 | 0 | 0 | 0 | 0 | stop 22, buy 11, buy @ 26 |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 24 | 5 | 3 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 8 | 8 | 7 | 0 | 1 | stop 24, buy 8, buy @ 2.5 |
| garments | 169 | 0 | 2 | 0 | 0 | min_holding 30, sell 56, sell @ 22 |
| grain | 103 | 21 | 0 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| meat | 8 | 8 | 7 | 0 | 1 | stop 24, buy 8, buy @ 3.02 |
| nets | 51 | 0 | 0 | 0 | 0 | min_holding 40, sell 6, sell @ 39.8 |
| porterage | 37 | 37 | 8 | 0 | 29 | buy 37, buy @ 0.8 |

**0 risks, 0 waste, 5 tuning** where v2 would act differently from v1.

## Tuning

- **cured fish**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax plants**: flax plants buffer thin: 1.6 turns (target 4) -> v2: lift the maker's rate or hold back sales until it reaches 442
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **timber**: build materials for park 1 are in (391.8 held, 10 needed) but a buy is still live -> v2: switch the timber buy off
- **tools**: home ask 6.45 is above our ceiling 6.20 and last turn bought 2 of ~7 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Builds under construction

- **park 1** 75% (EXPANSION), about 3 turns left; still to deliver: labour 65, limestone 15, timber 10; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 15 | 142.7 | 0 | off: covered |
| timber | 10 | 391.8 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 22

## Prestige spending, cheapest coin per prestige first

1128 turns left: prestige gained now converts 99.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 2 (pies) | mansion | 7 | 53.4 | 53.4 | thin at home: pies |
| hold banquet 3 (pies) | mansion | 8 | 55.7 | 55.7 | thin at home: pies |
| hold feast 2 | townhouse | 2.6 | 54.9 | 57.4 | needs a townhouse (build cost 7,093) |
| maintain 1 | park | 0.5 | 53.7 | 57.4 | running |
| hold banquet 4 (pies) | mansion | 18 | 57.6 | 57.6 | thin at home: pies |
| hold sermon 2 (candles) | church | 31 | 55.5 | 57.9 | needs a church (build cost 75,726); thin at home: jewellery, furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 59.2 | 59.2 | thin at home: cured fish, cheese |
| hold sermon 2 | church | 24 | 56.4 | 59.5 | needs a church (build cost 75,726); thin at home: jewellery, furniture |
| hold mass 2 (premium) | cathedral | 360 | 58.7 | 59.6 | needs a cathedral (build cost 298,530); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold prayer 2 | chapel | 13 | 57.2 | 59.7 | needs a chapel (build cost 35,760); thin at home: furniture |
| jousting 1 | arena | 170 | 59.7 | 59.8 | needs a arena (build cost 28,848); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 61.1 | 61.1 | thin at home: cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | - | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | - | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- best towns now: Toqueque +48, Vauxvais +28, Gotthafen +25, Nürnnieder +18
- Toqueque would trade: casks sell 1 @ 8.3, cheese sell 8 @ 10.7, salt sell 10 @ 6.95, tools buy 2 @ 5.3, yarn sell 2 @ 4.7; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~111 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Bordetes | 831 | 0.26 | 0.50 (56/turn) | garments 59 (21.4->23.37), furniture 13 (13.76->15.39), beer 21 (3.12->3.84), cloth 9 (7.3->7.6) | nails 2 (5.41->7.08), tools 2 (4.79->6.45), slaked lime 1 (11.76->12.73) | +110 |
| Toqueque | 642 | 0.19 | 0.10 (11/turn) | cheese 8 (6.83->13.11), salt 10 (4.6->7.65), casks 1 (6.51->9.4), wheels 1 (23->25.46) | cloth 21 (7.88->8.55), tools 2 (5.46->6.45), nails 2 (6.3->7.08), garments 2 (21.84->22.2) | +96 |
| Hanstein | 380 | 0.11 | 0.30 (33/turn) | light armour 3 (77.7->83.6), cloth 19 (7.3->8.07), wine 18 (5.62->6.13), timber 3 (6.25->8.79) | flax plants 71 (1.4->1.8), flax fibres 28 (6.46->6.8), tar 6 (10.82->11.4), tools 2 (5.21->6.45) | +65 |
| Cobholme | 1564 | 0.69 | 0.10 (11/turn) | rope 1 (94.5->127.3), light armour 1 (77.7->95), varnish 1 (18.17->22.04), pies 1 (16.7->19) | medicine 1 (164.85->168.15), nails 2 (5.88->7.08), tools 2 (5.25->6.45) | +53 |
| Vauxvais | 204 | 0.06 | 0.10 (11/turn) | beer 21 (3.12->3.61), bricks 1 (4.38->9.79), cloth 8 (7.3->7.69), timber 3 (6.25->8.22) | soap 1 (95.03->118.75), dye 1 (52.5->55.57), slaked lime 1 (10.92->12.73), tiles 2 (2.67->4.12) | +52 |

**Best:** Bordetes at about +110 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 26.6, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 55 @ min 3.7 | makes 56.0, uses 19.2, holds 316 (keeps 60): sells the surplus + 18/turn of the excess |
| cured fish | 11 @ 26.0, stop 22 |  | uses 5.5/turn (mansion 1), makes 0.0, holds 6 = 1.0 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 24 = 3.9 turns |
| fish | 8 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 8 = 1.1 turns |
| garments |  | 53 @ min 22.0 | makes 47.6, uses 2.1, holds 169 (keeps 30): sells the surplus + 8/turn of the excess |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 103 = 4.0 turns |
| labour | 693 @ 2.2, stop - |  | uses 1109.5/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 580 = 0.9 turns |
| limestone |  | 5 @ min 22.4 |  |
| meat | 8 @ 3.02, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 8 = 1.1 turns |
| nets |  | 6 @ min 42.4 |  |
| porterage | 33 @ 0.8, stop - |  | uses 29.4/turn (observed), makes 0.0, holds 37 = 1.3 turns |
| rope |  | 4 @ min 85.5 |  |
| timber |  | 25 @ min 8.5 | makes 24.0, uses 0.0, holds 392 (keeps 350): sells the surplus + 1/turn of the excess |
| tools | 8 @ 6.2, stop 60 |  | uses 7.5/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 26.8 turns |
