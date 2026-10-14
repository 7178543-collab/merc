# v2 shadow report

Turn 13274, 2026-10-14 11:57. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,993, prestige 2,815 (145 free, +3.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 315 | 0 | 19 | 0 | 0 | min_holding 60, sell 55, sell @ 3.7 |
| cured fish | 0 | 1 | 6 | 0 | 0 | stop 22, buy 11, buy @ 26 |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 24 | 3 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 8 | 8 | 7 | 0 | 1 | stop 24, buy 8, buy @ 2.5 |
| garments | 163 | 0 | 2 | 0 | 0 | min_holding 30, sell 53, sell @ 22 |
| grain | 103 | 0 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 646 | 580 | 1030 | 49 | 0 | buy 531, buy @ 2 |
| meat | 8 | 8 | 7 | 0 | 1 | stop 24, buy 8, buy @ 3.02 |
| nets | 57 | 0 | 0 | 0 | 0 | min_holding 40, sell 6, sell @ 42.4 |
| porterage | 37 | 37 | 25 | 0 | 12 | buy 37, buy @ 0.8 |

**1 risks, 2 waste, 5 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **labour**: buying 531, short of ~661 needed -> v2: buy 661

## Waste (money lost now)

- **Flax Wyrm**: Flax Wyrm cost 66 coin last turn (crew 0.61) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell
- **linen snake**: linen snake cost 54 coin last turn (crew 0.50) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell

## Tuning

- **cured fish**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax plants**: flax plants buffer thin: 1.4 turns (target 4) -> v2: lift the maker's rate or hold back sales until it reaches 496
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **timber**: build materials for park 1 are in (395.5 held, 10 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 75% (EXPANSION), about 3 turns left; still to deliver: labour 65, limestone 15, timber 10; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 15 | 145.5 | 0 | off: covered |
| timber | 10 | 395.5 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 22

## Prestige spending, cheapest coin per prestige first

1127 turns left: prestige gained now converts 99.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 2 (pies) | mansion | 7 | 52.9 | 52.9 | thin at home: wine, pies |
| hold feast 2 | townhouse | 2.6 | 52.6 | 55.1 | needs a townhouse (build cost 6,988); thin at home: wine |
| hold banquet 3 (pies) | mansion | 8 | 56.3 | 56.3 | thin at home: pies |
| maintain 1 | park | 0.5 | 53.7 | 57.4 | running |
| hold sermon 2 (candles) | church | 31 | 55.5 | 57.8 | needs a church (build cost 75,610); thin at home: jewellery, furniture |
| hold banquet 4 (pies) | mansion | 18 | 57.9 | 57.9 | thin at home: wine, pies |
| hold sermon 2 | church | 24 | 55.9 | 59.0 | needs a church (build cost 75,610); thin at home: jewellery, furniture |
| hold prayer 2 | chapel | 13 | 56.6 | 59.2 | needs a chapel (build cost 35,706); thin at home: furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 59.4 | 59.4 | thin at home: wine, cured fish, cheese |
| hold mass 2 (premium) | cathedral | 360 | 58.9 | 59.7 | needs a cathedral (build cost 298,200); thin at home: furniture, jewellery, glassware, candles, premium garments |
| jousting 1 | arena | 170 | 60.3 | 60.4 | needs a arena (build cost 28,728); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 60.5 | 60.5 | thin at home: wine, cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.61 / 0.61 | 66 | 108202735 | 0 | - | - | 0 |
| linen snake | 0.5 / 0.50 | 54 | - | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Toqueque: casks sell 1 @ 8.75, cheese sell 9 @ 11.3, salt sell 8 @ 7.1; crew 0.1; est +52 a turn
- best towns now: Toqueque +52, Heilegg +38, Vauxvais +28, Cobholme +25
- Toqueque would trade: casks sell 1 @ 8.75, cheese sell 9 @ 11.3, salt sell 8 @ 7.1; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~111 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Vauxvais | 204 | 0.06 | 0.40 (44/turn) | timber 27 (6.25->8.22), beer 58 (3.12->3.61), bricks 1 (4.42->9.79), thread 13 (4.66->4.99) | soap 1 (95.03->119.7), cloth 19 (7.88->8.6), tiles 3 (2.58->4.56), dye 1 (52.5->54.62) | +97 |
| Toqueque | 642 | 0.19 | 0.10 (11/turn) | cheese 9 (6.77->13.87), salt 8 (4.62->7.6), casks 1 (6.51->10.54), wheels 1 (23->25.27) | cloth 14 (7.88->8.6) | +95 |
| Chatgnan | 728 | 0.21 | 0.30 (33/turn) | beer 58 (3.12->4.94), nets 1 (39.8->40.85) | hides 1 (11.65->12.92), tar 2 (10.34->11.11) | +76 |
| Neuborn | 780 | 0.23 | 1.00 (111/turn) | timber 17 (6.25->11.4), beer 58 (3.12->3.84), candles 4 (79.8->81.7), tools 16 (4.76->5.27) | stockfish 1 (104.48->107.35), flax fibres 2 (5.67->6.7) | +64 |
| Hanstein | 380 | 0.11 | 0.20 (22/turn) | wine 6 (5.3->7.55), cloth 20 (7.4->7.98), timber 8 (6.25->8.93), light armour 1 (84.53->88.35) | flax fibres 28 (5.78->6.7), seeds 6 (1.87->2.32), tar 2 (10.5->11.11) | +59 |

**Best:** Vauxvais at about +97 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 55 @ min 3.7 | makes 56.0, uses 19.2, holds 315 (keeps 60): sells the surplus + 18/turn of the excess |
| cured fish | 11 @ 26.0, stop 22 |  | uses 5.5/turn (mansion 1), makes 0.0, holds 0 = 0.0 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 24 = 3.9 turns |
| fish | 8 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 8 = 1.1 turns |
| garments |  | 37 @ min 22.0 | makes 30.8, uses 2.1, holds 163 (keeps 30): sells the surplus + 9/turn of the excess |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 103 = 4.0 turns |
| labour | 661 @ 2.2, stop - |  | uses 1078.6/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 646 = 1.0 turns |
| limestone |  | 5 @ min 22.4 |  |
| meat | 8 @ 3.02, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 8 = 1.1 turns |
| nets |  | 7 @ min 38.8 |  |
| porterage | 33 @ 0.8, stop - |  | uses 29.6/turn (observed), makes 0.0, holds 37 = 1.3 turns |
| rope |  | 4 @ min 79.5 |  |
| timber |  | 26 @ min 8.5 | makes 24.0, uses 0.0, holds 396 (keeps 350): sells the surplus + 2/turn of the excess |
| tools | 8 @ 6.2, stop 63 |  | uses 7.8/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 25.7 turns |
