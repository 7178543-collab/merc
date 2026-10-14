# v2 shadow report

Turn 13284, 2026-10-14 21:56. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,119, prestige 3,010 (340 free, +3.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 286 | 0 | 19 | 0 | 0 | min_holding 60, sell 52, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 24 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 8 | 8 | 7 | 0 | 1 | stop 24, buy 8, buy @ 2.5 |
| garments | 94 | 0 | 2 | 0 | 0 | min_holding 30, sell 15, sell @ 22 |
| grain | 103 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 237 | 273 | 652 | 0 | 71 | buy 237, buy @ 2.2 |
| meat | 8 | 8 | 7 | 0 | 1 | stop 24, buy 8, buy @ 3.02 |
| nets | 50 | 0 | 0 | 0 | 0 | min_holding 40, sell 6, sell @ 42.6 |
| porterage | 37 | 37 | 25 | 0 | 12 | buy 37, buy @ 0.8 |

**0 risks, 2 waste, 5 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **Flax Wyrm**: Flax Wyrm cost 49 coin last turn (crew 0.50) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell
- **labour**: 71 labour expired last turn (~115 coin): holding 237 against a ~34 buffer target -> v2: trim the buy until the stock is near 34

## Tuning

- **candles**: home ask 77.00 is above our ceiling 70.00 and last turn bought 1 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **timber**: build materials for park 1 are in (462.8 held, 17 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 58% (EXPANSION), about 6 turns left; still to deliver: labour 110, limestone 26, timber 17; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 26 | 114.4 | 0 | off: covered |
| timber | 17 | 462.8 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 19

## Prestige spending, cheapest coin per prestige first

1117 turns left: prestige gained now converts 99.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.3 | 51.5 | running |
| hold banquet 2 (pies) | mansion | 7 | 56.9 | 56.9 | thin at home: cheese, pies |
| hold banquet 3 (pies) | mansion | 8 | 57.2 | 57.2 | thin at home: pies |
| hold prayer 2 | chapel | 13 | 56.2 | 58.5 | needs a chapel (build cost 32,356); thin at home: furniture |
| jousting 1 | arena | 170 | 58.5 | 58.7 | needs a arena (build cost 25,452); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 59.2 | 59.2 | thin at home: pies |
| hold sermon 2 (candles) | church | 31 | 57.7 | 60.0 | needs a church (build cost 71,713); thin at home: jewellery, furniture |
| hold banquet 2 (meat) | mansion | 6.8 | 60.1 | 60.1 | thin at home: cheese |
| hold banquet 1 (meat) | mansion | 4.2 | 60.2 | 60.2 | running |
| jousting 3 | arena | 230 | 60.3 | 60.4 | needs a arena (build cost 25,452); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (meat) | mansion | 7.6 | 61.2 | 61.2 | thin at home: cheese |
| hold sermon 2 | church | 24 | 58.6 | 61.5 | needs a church (build cost 71,713); thin at home: jewellery, furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.5 / 0.50 | 50 | - | 0 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | nets 2 | - | 46 |

## Ship plans (this turn's world prices)

- **linen snake** on Heilegg: grindstones buy 1 @ 254, hop beer buy 2 @ 7.55; crew 0.1; est +31 a turn
- best towns now: Darmwald +105, Kirchwerp +98, Hofkirchen +66, Toqueque +49, Dortdorf +46
- Darmwald would trade: medicine buy 2 @ 141, tackles sell 1 @ 193; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~101 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.32 | 0.20 (20/turn) | flax plants 14 (1.42->3.89), rope 3 (69.01->78.38), tackles 1 (175.35->180.5), thread 23 (4.66->5.08) | medicine 2 (157.5->181.45), garments 20 (22.68->24.7), yarn 5 (3.95->5.61), steel ingots 4 (14.91->15.39) | +148 |
| Rouhomme | 368 | 0.10 | 0.60 (60/turn) | bread 137 (2.39->3.21), lead ore 2 (6.09->17), beer 55 (3.18->3.65), flour 2 (24.57->28.12) | garments 20 (22.89->24.7) | +147 |
| Darmwald | 1022 | 0.34 | 0.30 (30/turn) | spinning wheels 1 (281.4->300.2), tackles 1 (175.35->186.2), thread 40 (4.66->5.13), flax plants 14 (1.42->2.36) | medicine 2 (144.9->181.45), garments 20 (23.52->24.7), nails 2 (5->5.7), yarn 4 (5.23->5.61) | +132 |
| Toqueque | 642 | 0.17 | 0.10 (10/turn) | salt 4 (4.79->10.07), cheese 4 (6.62->10.73), ploughs 1 (75.6->80.27), cloth 6 (8->8.55) | garments 20 (21.84->24.7), yarn 10 (3.65->5.61), tar 1 (10.5->11.1) | +115 |
| Pontmont | 341 | 0.09 | 0.50 (50/turn) | rope 4 (69.01->84.08), bread 137 (2.39->2.75), ploughs 1 (75.6->78.85), bricks 1 (5.15->7.6) | garments 20 (22.47->24.7), slaked lime 1 (8.56->9.12) | +111 |

**Best:** Hofkirchen at about +148 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 53 @ min 3.7 | makes 56.0, uses 19.2, holds 286 (keeps 60): sells the surplus + 16/turn of the excess |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 8 = 5.3 turns |
| cured meat | 6 @ 24.8, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 24 = 4.0 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 24 = 3.9 turns |
| fish | 8 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 8 = 1.1 turns |
| garments |  | 11 @ min 22.0 | makes 8.6, uses 2.1, holds 94 (keeps 30): sells the surplus + 5/turn of the excess |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 103 = 4.0 turns |
| labour | 224 @ 2.2, stop - |  | uses 663.3/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 237 = 1.1 turns |
| limestone |  | 5 @ min 20.8 |  |
| meat | 8 @ 3.02, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 8 = 1.1 turns |
| nets |  | 6 @ min 43.4 |  |
| porterage | 33 @ 0.8, stop - |  | uses 29.6/turn (observed), makes 0.0, holds 37 = 1.3 turns |
| rope |  | 5 @ min 78.0 |  |
| timber |  | 31 @ min 8.5 | makes 24.0, uses 0.0, holds 463 (keeps 350): sells the surplus + 7/turn of the excess |
| tools | 7 @ 6.2, stop 49 |  | uses 6.1/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 32.7 turns |

## Self-diagnosis

Nothing found this run.
