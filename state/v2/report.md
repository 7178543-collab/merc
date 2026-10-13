# v2 shadow report

Turn 13258, 2026-10-13 19:56. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, meat, nets, porterage; v1 runs everything else.
Cash 22,925, prestige 2,681 (11 free, +0.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 398 | 0 | 19 | 0 | 0 | min_holding 60, sell 74, sell @ 3.7 |
| cured fish | 21 | 6 | 6 | 0 | 0 | stop 22, buy 6, buy @ 26 |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 25 | 6 | 6 | 0 | 0 | stop 26, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 6 | 0 | 1 | stop 24, buy 7, buy @ 2.5 |
| garments | 299 | 0 | 2 | 0 | 0 | min_holding 30, sell 61, sell @ 22 |
| grain | 130 | 33 | 32 | 0 | 0 | stop 130, buy 33, buy @ 3.7 |
| meat | 7 | 7 | 6 | 0 | 1 | stop 24, buy 7, buy @ 3.02 |
| nets | 50 | 0 | 0 | 0 | 0 | min_holding 40, sell 6, sell @ 41 |
| porterage | 37 | 37 | 19 | 0 | 18 | buy 37, buy @ 0.8 |

**1 risks, 0 waste, 5 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **labour**: buying 522, short of ~664 needed -> v2: buy 664

## Tuning

- **cured fish**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **fish**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax plants**: flax plants buffer thin: 1.4 turns (target 4) -> v2: lift the maker's rate or hold back sales until it reaches 489
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **timber**: build materials for park 1 are in (468.1 held, 38 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 6% (EXPANSION), about 12 turns left; still to deliver: labour 245, limestone 57, timber 38; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 57 | 152.0 | 0 | off: covered |
| timber | 38 | 468.1 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 21

## Prestige spending, cheapest coin per prestige first

1143 turns left: prestige gained now converts 99.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 3 (pies) | mansion | 8 | 54.3 | 54.3 | thin at home: cheese, pies |
| hold banquet 2 (pies) | mansion | 7 | 54.9 | 54.9 | thin at home: cheese, pies |
| maintain 1 | park | 0.5 | 52.2 | 56.3 | running |
| hold banquet 4 (pies) | mansion | 18 | 57.8 | 57.8 | thin at home: cheese, pies |
| hold prayer 2 | chapel | 13 | 55.9 | 58.5 | needs a chapel (build cost 37,262); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 56.5 | 58.9 | needs a church (build cost 77,113); thin at home: jewellery, candles, furniture |
| hold banquet 3 (fish) | mansion | 7.6 | 59.1 | 59.1 | thin at home: cured fish, cheese |
| hold banquet 2 (fish) | mansion | 6.8 | 59.2 | 59.2 | thin at home: cured fish, cheese |
| hold sermon 2 | church | 24 | 57.1 | 60.1 | needs a church (build cost 77,113); thin at home: jewellery, furniture |
| hold banquet 1 (fish) | mansion | 4.2 | 60.2 | 60.2 | running; thin at home: cured fish |
| jousting 3 | arena | 230 | 61.2 | 61.3 | needs a arena (build cost 28,978); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| jousting 1 | arena | 170 | 61.3 | 61.4 | needs a arena (build cost 28,978); thin at home: protection, light armour, arms; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 117101560 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 108202735 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Darmwald: nothing pays; crew 0.0; est +0 a turn; best orders clear only 3 a turn after crew: ship stays at 0
- **linen snake** on Toqueque: nothing pays; crew 0.0; est +0 a turn

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~106 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Rouhomme | 368 | 0.10 | 0.50 (53/turn) | bread 135 (2.42->3.19), grain 10 (2.78->3.72), cured meat 2 (29.61->32.3), furniture 12 (12.5->13.3) | cloth 12 (7.46->8), thread 3 (3.53->4.92) | +97 |
| Pontmont | 341 | 0.10 | 0.90 (96/turn) | bread 135 (2.42->2.98), beer 79 (3.08->3.72), furniture 12 (12.5->13.49), timber 21 (6.2->7.98) | flax plants 1 (0.64->1.61), cloth 3 (7.88->8), garments 1 (21.84->22), wool 1 (8.66->9.07) | +93 |
| Birkeningen | 1006 | 0.35 | 0.70 (75/turn) | beer 79 (3.08->4.56), furniture 9 (12.5->15.48), yarn 5 (4.03->4.71), cured fish 1 (24.8->26.41) | steel ingots 1 (14.7->15.2) | +76 |
| Vauxvais | 204 | 0.06 | 0.30 (32/turn) | timber 28 (6.2->8.22), tools 16 (4.66->4.99), yarn 6 (4.03->4.54), bricks 1 (4.3->6.65) | limestone 2 (12.6->24.7), tiles 3 (2.56->4.54), beer 18 (3.49->3.7), hides 1 (10.92->12.82) | +69 |
| Cobholme | 1564 | 0.67 | 0.10 (11/turn) | blades 1 (17.75->19), wrought iron 1 (12.7->14.82), pies 1 (16.7->19), varnish 1 (20.16->21.09) | acid 1 (132.3->187.15), butter 1 (47.04->55.57), garments 1 (21->22) | +60 |

**Best:** Rouhomme at about +97 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 75 @ min 3.7 | makes 70.0, uses 18.6, holds 398 (keeps 60): sells the surplus + 24/turn of the excess |
| cured fish | 6 @ 26.0, stop 22 |  | uses 5.5/turn (mansion 1), makes 0.0, holds 21 = 3.9 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 26 |  | uses 6.4/turn (brewery 1, household upkeep), makes 0.0, holds 25 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 7 = 1.2 turns |
| garments |  | 63 @ min 22.0 | makes 46.3, uses 1.8, holds 299 (keeps 30): sells the surplus + 19/turn of the excess |
| grain | 33 @ 3.7, stop 130 |  | uses 32.5/turn (brewery 1), makes 0.0, holds 130 = 4.0 turns |
| labour | 664 @ 2.2, stop - |  | uses 1081.6/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 469 = 0.7 turns |
| limestone |  | 5 @ min 25.4 |  |
| meat | 7 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 7 = 1.2 turns |
| nets |  | 6 @ min 41.0 |  |
| porterage | 35 @ 0.8, stop - |  | uses 31.6/turn (observed), makes 0.0, holds 37 = 1.2 turns |
| timber |  | 32 @ min 8.5 | makes 24.0, uses 0.0, holds 468 (keeps 350): sells the surplus + 8/turn of the excess |
| tools | 8 @ 6.2, stop 62 |  | uses 7.7/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 25.8 turns |
