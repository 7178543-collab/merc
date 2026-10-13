# v2 shadow report

Turn 13262, 2026-10-13 23:49. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, meat, nets, porterage; v1 runs everything else.
Cash 20,350, prestige 2,683 (13 free, -0.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 416 | 0 | 4 | 0 | 0 | min_holding 60, sell 77, sell @ 3.7 |
| cured fish | 22 | 6 | 0 | 0 | 0 | stop 22, buy 6, buy @ 26 |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 27 | 7 | 6 | 0 | 0 | stop 28, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 8, buy @ 2.5 |
| garments | 282 | 0 | 2 | 0 | 0 | min_holding 30, sell 61, sell @ 22 |
| grain | 130 | 33 | 23 | 0 | 0 | stop 130, buy 33, buy @ 3.7 |
| meat | 8 | 8 | 7 | 0 | 1 | stop 24, buy 8, buy @ 3.02 |
| nets | 51 | 0 | 0 | 0 | 0 | min_holding 40, sell 6, sell @ 40.4 |
| porterage | 37 | 37 | 12 | 0 | 25 | buy 37, buy @ 0.8 |

**1 risks, 0 waste, 5 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **labour**: buying 639, short of ~767 needed -> v2: buy 767

## Tuning

- **fish**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax plants**: flax plants buffer thin: 1.6 turns (target 4) -> v2: lift the maker's rate or hold back sales until it reaches 432
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **timber**: build materials for park 1 are in (435.7 held, 29 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 28% (EXPANSION), about 9 turns left; still to deliver: labour 188, limestone 44, timber 29; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 44 | 143.0 | 0 | off: covered |
| timber | 29 | 435.7 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 21

## Prestige spending, cheapest coin per prestige first

1139 turns left: prestige gained now converts 99.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 2 (pies) | mansion | 7 | 55.4 | 55.4 | thin at home: wine, cheese, pies, candles |
| hold banquet 3 (pies) | mansion | 8 | 56.5 | 56.5 | thin at home: hop beer, cheese, pies, candles |
| maintain 1 | park | 0.5 | 53.7 | 56.9 | running |
| hold prayer 2 | chapel | 13 | 56.6 | 58.9 | needs a chapel (build cost 33,338); thin at home: furniture |
| hold banquet 4 (pies) | mansion | 18 | 59.0 | 59.0 | thin at home: hop beer, wine, cheese, pies, candles |
| hold sermon 2 (candles) | church | 31 | 57.1 | 59.2 | needs a church (build cost 71,174); thin at home: jewellery, candles, furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 59.4 | 59.4 | thin at home: wine, cured fish, cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 60.3 | 60.3 | running; thin at home: cured fish |
| hold sermon 2 | church | 24 | 57.7 | 60.5 | needs a church (build cost 71,174); thin at home: jewellery, furniture |
| hold banquet 3 (fish) | mansion | 7.6 | 61.3 | 61.3 | thin at home: hop beer, cured fish, cheese |
| hold mass 2 (premium) | cathedral | 360 | 61.0 | 61.8 | needs a cathedral (build cost 285,850); thin at home: furniture, jewellery, glassware, candles, premium garments |
| jousting 3 | arena | 230 | 61.8 | 61.9 | needs a arena (build cost 26,171); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 117101560 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 108202735 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Darmwald: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Toqueque: nothing pays; crew 0.0; est +0 a turn
- best towns now: Etallaen +74
- Etallaen would trade: garments sell 32 @ 24.8; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~109 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Etallaen | 774 | 0.23 | 0.10 (11/turn) | garments 32 (21.4->27.93), tallow 1 (24.78->30.4) | candles 5 (75.6->77.9), hop beer 1 (7.72->9.69) | +217 |
| Rouhomme | 368 | 0.11 | 0.60 (65/turn) | bread 137 (2.44->3.25), grain 10 (2.8->4.16), limestone 1 (18.9->30.59), furniture 13 (12.6->13.3) | cloth 16 (7.46->8) | +101 |
| Pontmont | 341 | 0.10 | 0.70 (76/turn) | beer 75 (3.08->3.72), bread 137 (2.44->2.85), furniture 13 (12.6->13.49), grain 10 (2.8->3.34) | rope 2 (78.23->80.27), cloth 5 (7.88->8) | +63 |
| Birkeningen | 1006 | 0.35 | 0.20 (22/turn) | furniture 9 (12.6->16.34), wrought iron 1 (12.7->13.11) | soap 1 (79.28->120.65), candles 4 (76.65->77.9) | +59 |
| Hofkirchen | 991 | 0.34 | 0.40 (44/turn) | flax plants 16 (1.33->3.89), tallow 2 (24.78->31.16), cloth 11 (7.8->8.79), thread 41 (4.66->5.13) | stockfish 1 (105->107.35), hop beer 1 (7.72->9.69), cheese 27 (6.2->6.55) | +58 |

**Best:** Etallaen at about +217 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 63 @ min 3.7 | makes 56.0, uses 19.2, holds 416 (keeps 60): sells the surplus + 27/turn of the excess |
| cured fish | 6 @ 26.0, stop 22 |  | uses 5.5/turn (mansion 1), makes 0.0, holds 22 = 4.0 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 6 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 27 = 4.5 turns |
| fish | 8 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 62 @ min 22.0 | makes 46.3, uses 2.1, holds 282 (keeps 30): sells the surplus + 17/turn of the excess |
| grain | 26 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 130 = 5.0 turns |
| labour | 767 @ 2.2, stop - |  | uses 1180.4/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 535 = 0.7 turns |
| limestone |  | 5 @ min 23.8 |  |
| meat | 8 @ 3.02, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 8 = 1.1 turns |
| nets |  | 6 @ min 41.0 |  |
| porterage | 35 @ 0.8, stop - |  | uses 31.6/turn (observed), makes 0.0, holds 37 = 1.2 turns |
| rope |  | 4 @ min 82.0 |  |
| timber |  | 29 @ min 8.5 | makes 24.0, uses 0.0, holds 436 (keeps 350): sells the surplus + 5/turn of the excess |
| tools | 8 @ 6.2, stop 60 |  | uses 7.4/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 27.0 turns |
