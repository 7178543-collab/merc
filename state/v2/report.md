# v2 shadow report

Turn 13261, 2026-10-13 22:52. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, meat, nets, porterage; v1 runs everything else.
Cash 21,075, prestige 2,683 (13 free, +0.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 423 | 0 | 19 | 0 | 0 | min_holding 60, sell 76, sell @ 3.7 |
| cured fish | 22 | 5 | 6 | 0 | 0 | stop 22, buy 6, buy @ 26 |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 28 | 9 | 7 | 0 | 0 | stop 28, buy 8, buy @ 2.4 |
| fish | 7 | 8 | 7 | 0 | 1 | stop 24, buy 8, buy @ 2.5 |
| garments | 290 | 0 | 2 | 0 | 0 | min_holding 30, sell 61, sell @ 22 |
| grain | 130 | 32 | 32 | 0 | 0 | stop 130, buy 33, buy @ 3.7 |
| meat | 8 | 8 | 7 | 0 | 1 | stop 24, buy 8, buy @ 3.02 |
| nets | 51 | 0 | 0 | 0 | 0 | min_holding 40, sell 6, sell @ 39.4 |
| porterage | 37 | 37 | 20 | 0 | 17 | buy 37, buy @ 0.8 |

**1 risks, 1 waste, 4 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax plants**: flax plants buffer 1.0 turns (holds 174, next step uses 180/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **labour**: 30 labour expired last turn (~54 coin): holding 543 against a ~63 buffer target -> v2: trim the buy until the stock is near 63

## Tuning

- **fish**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **timber**: build materials for park 1 are in (459.7 held, 30 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 25% (EXPANSION), about 9 turns left; still to deliver: labour 195, limestone 45, timber 30; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 45 | 148.0 | 0 | off: covered |
| timber | 30 | 459.7 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 22

## Prestige spending, cheapest coin per prestige first

1140 turns left: prestige gained now converts 99.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 3 (pies) | mansion | 8 | 54.9 | 54.9 | thin at home: cheese, pies, candles |
| hold banquet 2 (pies) | mansion | 7 | 56.0 | 56.0 | thin at home: wine, cheese, pies, candles |
| maintain 1 | park | 0.5 | 53.4 | 56.8 | running |
| hold banquet 4 (pies) | mansion | 18 | 58.0 | 58.0 | thin at home: wine, cheese, pies, candles |
| hold prayer 2 | chapel | 13 | 56.5 | 58.9 | needs a chapel (build cost 34,506) |
| hold banquet 3 (fish) | mansion | 7.6 | 59.2 | 59.2 | thin at home: cured fish, cheese |
| hold banquet 2 (fish) | mansion | 6.8 | 59.8 | 59.8 | thin at home: wine, cured fish, cheese |
| hold sermon 2 (candles) | church | 31 | 57.8 | 60.0 | needs a church (build cost 72,893); thin at home: jewellery, candles |
| hold banquet 1 (fish) | mansion | 4.2 | 60.3 | 60.3 | running; thin at home: cured fish |
| hold sermon 2 | church | 24 | 57.6 | 60.5 | needs a church (build cost 72,893); thin at home: jewellery |
| hold mass 2 (premium) | cathedral | 360 | 60.5 | 61.3 | needs a cathedral (build cost 291,240); thin at home: furniture, jewellery, glassware, candles, premium garments |
| jousting 3 | arena | 230 | 61.7 | 61.8 | needs a arena (build cost 26,918); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 117101560 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 108202735 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Darmwald: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Toqueque: nothing pays; crew 0.0; est +0 a turn
- best towns now: Etallaen +80
- Etallaen would trade: garments sell 34 @ 24.2, nets sell 6 @ 45.4; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~108 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Etallaen | 774 | 0.22 | 0.20 (22/turn) | garments 34 (21.4->26.98), nets 6 (41.6->44.27), rope 1 (78->89.3), tallow 1 (24.78->30.4) | jewellery 1 (82.95->88.35), hop beer 2 (7.72->9.45) | +214 |
| Rouhomme | 368 | 0.11 | 0.50 (54/turn) | bread 136 (2.39->3.38), grain 10 (2.26->4.37), cheese 8 (7.19->8.17), furniture 13 (12.5->13.3) | cloth 7 (7.46->7.85), tools 7 (5.04->5.15) | +127 |
| Herschweig | 775 | 0.22 | 0.20 (22/turn) | cloth 33 (7.8->9.79), garments 13 (21.4->22.23), tools 9 (4.66->5.18), arms 2 (26.67->28.31) | cheese 8 (5.99->6.46) | +71 |
| Bordetes | 831 | 0.25 | 0.50 (54/turn) | rope 1 (78->97.85), beer 81 (3.08->3.78), cheese 13 (7.19->8.55), grain 10 (2.26->3.1) | jewellery 1 (84->88.35), stockfish 1 (106.05->107.35), garments 2 (21.63->22) | +60 |
| Fontaux | 411 | 0.12 | 0.50 (54/turn) | timber 12 (6.25->10.07), beer 41 (3.08->3.69), tools 16 (4.66->5.7), furniture 8 (12.5->13.68) | candles 1 (77.7->77.9) | +59 |

**Best:** Etallaen at about +214 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 77 @ min 3.7 | makes 70.0, uses 19.2, holds 423 (keeps 60): sells the surplus + 26/turn of the excess |
| cured fish | 6 @ 26.0, stop 22 |  | uses 5.5/turn (mansion 1), makes 0.0, holds 22 = 4.0 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 28 |  | uses 6.8/turn (brewery 1, household upkeep), makes 0.0, holds 28 = 4.1 turns |
| fish | 8 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 61 @ min 22.0 | makes 44.7, uses 2.1, holds 290 (keeps 30): sells the surplus + 18/turn of the excess |
| grain | 33 @ 3.7, stop 130 |  | uses 32.5/turn (brewery 1), makes 0.0, holds 130 = 4.0 turns |
| labour | 845 @ 2.2, stop - |  | uses 1254.0/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 543 = 0.7 turns |
| limestone |  | 5 @ min 23.8 |  |
| meat | 8 @ 3.02, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 8 = 1.1 turns |
| nets |  | 6 @ min 40.4 |  |
| porterage | 35 @ 0.8, stop - |  | uses 31.6/turn (observed), makes 0.0, holds 37 = 1.2 turns |
| rope |  | 4 @ min 76.0 |  |
| timber |  | 31 @ min 8.5 | makes 24.0, uses 0.0, holds 460 (keeps 350): sells the surplus + 7/turn of the excess |
| tools | 9 @ 6.2, stop 72 |  | uses 9.0/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 22.2 turns |
