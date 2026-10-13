# v2 shadow report

Turn 13257, 2026-10-13 18:53. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, meat, nets, porterage; v1 runs everything else.
Cash 23,034, prestige 2,680 (10 free, +70.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 387 | 0 | 19 | 0 | 0 | min_holding 60, sell 74, sell @ 3.7 |
| cured fish | 22 | 5 | 6 | 0 | 0 | stop 22, buy 6, buy @ 26 |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 26 | 7 | 6 | 0 | 0 | stop 26, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 6 | 0 | 1 | stop 24, buy 7, buy @ 2.5 |
| garments | 303 | 0 | 2 | 0 | 0 | min_holding 30, sell 63, sell @ 22 |
| grain | 130 | 32 | 32 | 0 | 0 | stop 130, buy 33, buy @ 3.7 |
| meat | 7 | 7 | 6 | 0 | 1 | stop 24, buy 7, buy @ 3.02 |
| nets | 50 | 0 | 0 | 0 | 0 | min_holding 40, sell 6, sell @ 41 |
| porterage | 37 | 37 | 19 | 0 | 18 | buy 37, buy @ 0.8 |

**0 risks, 1 waste, 6 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **labour**: 59 labour expired last turn (~103 coin): holding 481 against a ~52 buffer target -> v2: trim the buy until the stock is near 52

## Tuning

- **cured fish**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **fish**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax plants**: flax plants buffer thin: 1.7 turns (target 4) -> v2: lift the maker's rate or hold back sales until it reaches 413
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **timber**: build materials for park 1 are in (468.1 held, 40 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 0% (EXPANSION), about 12 turns left; still to deliver: labour 260, limestone 60, timber 40; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 60 | 153.0 | 0 | off: covered |
| timber | 40 | 468.1 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 22

## Prestige spending, cheapest coin per prestige first

1144 turns left: prestige gained now converts 99.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 3 (pies) | mansion | 8 | 52.2 | 52.2 | thin at home: pasties, pies |
| hold banquet 2 (pies) | mansion | 7 | 52.8 | 52.8 | thin at home: pasties, pies |
| maintain 1 | park | 0.5 | 52.2 | 55.4 | running |
| hold banquet 4 (pies) | mansion | 18 | 57.4 | 57.4 | thin at home: pasties, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 58.5 | 58.5 | thin at home: cured fish |
| hold prayer 2 | chapel | 13 | 56.3 | 58.6 | needs a chapel (build cost 33,722); thin at home: furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 58.8 | 58.8 | thin at home: cured fish |
| hold sermon 2 (candles) | church | 31 | 56.8 | 59.0 | needs a church (build cost 72,803); thin at home: jewellery, candles, furniture |
| jousting 1 | arena | 170 | 60.0 | 60.1 | needs a arena (build cost 26,489); thin at home: protection, light armour, arms; needs weaponry skill |
| hold sermon 2 | church | 24 | 57.4 | 60.2 | needs a church (build cost 72,803); thin at home: jewellery, furniture |
| hold banquet 1 (fish) | mansion | 4.2 | 60.7 | 60.7 | running; thin at home: cured fish |
| jousting 3 | arena | 230 | 61.3 | 61.4 | needs a arena (build cost 26,489); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 117101560 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 108202735 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Darmwald: nothing pays; crew 0.0; est +0 a turn; best orders clear only 6 a turn after crew: ship stays at 0
- **linen snake** on Toqueque: nothing pays; crew 0.0; est +0 a turn

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~107 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.34 | 0.30 (32/turn) | flax fibres 11 (5.6->10.16), lead bars 3 (12.39->14.34), thread 40 (4.66->5.13), wheels 1 (19.4->22.8) | acid 1 (168->185.25), jewellery 1 (78.75->87.88), steel ingots 1 (9.08->13.39), hop beer 2 (7.82->9.5) | +83 |
| Rouhomme | 368 | 0.10 | 0.60 (64/turn) | bread 134 (2.5->3.13), cheese 8 (6.25->8.36), grain 10 (2.26->3.5), furniture 12 (12.5->13.3) | rope 2 (86.1->89.3), cloth 12 (7.46->7.9) | +82 |
| Pontmont | 341 | 0.10 | 0.50 (53/turn) | bread 134 (2.5->2.93), cheese 14 (6.25->7.55), furniture 12 (12.5->13.59), grain 10 (2.26->3.27) | flax plants 1 (0.71->1.57), salt 3 (5.23->5.56) | +59 |
| Fontaux | 411 | 0.12 | 0.50 (53/turn) | timber 14 (7.3->10.07), tools 16 (4.66->5.51), beer 42 (3.08->3.53), furniture 8 (12.5->13.96) | rope 1 (84->89.3), salt 5 (5.3->5.56) | +55 |
| Clairlond | 1288 | 0.51 | 0.10 (11/turn) | wheels 1 (19.4->20.9) | acid 1 (132.3->185.25), salt 4 (4.28->5.56), rope 3 (87.67->89.3) | +53 |

**Best:** Hofkirchen at about +83 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 24.6, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 74 @ min 3.7 | makes 70.0, uses 18.6, holds 387 (keeps 60): sells the surplus + 23/turn of the excess |
| cured fish | 6 @ 26.0, stop 22 |  | uses 5.5/turn (mansion 1), makes 0.0, holds 22 = 4.0 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 26 |  | uses 6.4/turn (brewery 1, household upkeep), makes 0.0, holds 26 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 7 = 1.2 turns |
| garments |  | 61 @ min 22.0 | makes 43.1, uses 1.8, holds 303 (keeps 30): sells the surplus + 19/turn of the excess |
| grain | 33 @ 3.7, stop 130 |  | uses 32.5/turn (brewery 1), makes 0.0, holds 130 = 4.0 turns |
| labour | 609 @ 2.2, stop - |  | uses 1029.9/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 481 = 0.8 turns |
| limestone |  | 5 @ min 23.4 |  |
| meat | 7 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 7 = 1.2 turns |
| nets |  | 6 @ min 41.0 |  |
| porterage | 35 @ 0.8, stop - |  | uses 31.6/turn (observed), makes 0.0, holds 37 = 1.2 turns |
| timber |  | 32 @ min 8.5 | makes 24.0, uses 0.0, holds 468 (keeps 350): sells the surplus + 8/turn of the excess |
| tools | 8 @ 6.2, stop 59 |  | uses 7.3/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 27.3 turns |
