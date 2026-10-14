# v2 shadow report

Turn 13280, 2026-10-14 17:00. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,052, prestige 0 (-2,670 free, +0.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 298 | 0 | 19 | 0 | 0 | min_holding 60, sell 51, sell @ 4.14 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 24 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 8 | 8 | 7 | 0 | 1 | stop 24, buy 8, buy @ 2.5 |
| garments | 117 | 0 | 2 | 0 | 0 | min_holding 30, sell 29, sell @ 26.2 |
| grain | 103 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 356 | 585 | 712 | 0 | 323 | buy 356, buy @ 2.2 |
| meat | 8 | 8 | 7 | 0 | 1 | stop 24, buy 8, buy @ 3.02 |
| nets | 61 | 0 | 0 | 0 | 0 | min_holding 40, sell 7, sell @ 41.4 |
| porterage | 37 | 37 | 25 | 0 | 12 | buy 37, buy @ 0.8 |

**0 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **labour**: 323 labour expired last turn (~552 coin): holding 356 against a ~39 buffer target -> v2: trim the buy until the stock is near 39

## Tuning

- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **rope**: floor 80.00 vs home bid 69.50: barely selling (0 of 4)
- **timber**: build materials for park 1 are in (444.0 held, 30 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 25% (EXPANSION), about 9 turns left; still to deliver: labour 195, limestone 45, timber 30; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 45 | 113.6 | 0 | off: covered |
| timber | 30 | 444.0 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 22

## Prestige spending, cheapest coin per prestige first

1121 turns left: prestige gained now converts 99.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.3 | 54.6 | running |
| hold banquet 2 (pies) | mansion | 7 | 56.6 | 56.6 | thin at home: pies |
| hold banquet 3 (pies) | mansion | 8 | 57.1 | 57.1 | thin at home: pies |
| hold banquet 4 (pies) | mansion | 18 | 59.2 | 59.2 | thin at home: pies |
| hold mass 2 (premium) | cathedral | 360 | 58.8 | 59.6 | needs a cathedral (build cost 284,380); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 2 (meat) | mansion | 6.8 | 59.7 | 59.7 |  |
| hold banquet 3 (meat) | mansion | 7.6 | 60.9 | 60.9 |  |
| jousting 1 | arena | 170 | 60.8 | 60.9 | needs a arena (build cost 26,594); thin at home: protection, light armour, arms; needs weaponry skill |
| jousting 3 | arena | 230 | 60.9 | 61.0 | needs a arena (build cost 26,594); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (meat) | mansion | 4.2 | 61.4 | 61.4 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 62.4 | 62.4 | thin at home: cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 63.3 | 63.3 | thin at home: cured fish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 108202735 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | cured meat 2 | -46 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Toqueque: cheese sell 5 @ 10.7, salt sell 4 @ 7.95, tar buy 1 @ 10.6; crew 0.1; est +24 a turn
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn; best orders clear only -2 a turn after crew: ship stays at 0
- best towns now: Hofkirchen +51, Rouhomme +43, Bordetes +38, Cobholme +37, Magdeach +27
- Hofkirchen would trade: rope sell 5 @ 84.5, soap buy 1 @ 112; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~105 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Rouhomme | 368 | 0.10 | 0.50 (53/turn) | bread 133 (2.5->3.25), cheese 15 (6.83->10.64), lead ore 6 (8.03->13.68), yarn 7 (5.15->8.26) | garments 20 (23.31->25.65), tiles 1 (3.38->5.32), tools 6 (4.94->5.15) | +226 |
| Hofkirchen | 991 | 0.33 | 0.30 (32/turn) | rope 5 (74->81.7), tools 16 (4.76->5.79), butter 1 (66.15->71.25), thread 32 (4.66->5.13) | garments 20 (22.68->25.65), beer 19 (3.07->4.42), soap 1 (114.45->118.75), slaked lime 1 (8.4->11.3) | +127 |
| Vauxvais | 204 | 0.06 | 0.10 (11/turn) | thread 23 (4.66->5.22), cured meat 2 (22.8->25.46), wax 2 (24.78->27.17), flax fibres 7 (5.65->6.27) | garments 20 (22.05->25.65), beer 19 (3.61->4.42), cloth 24 (7.88->8), hides 1 (11.03->12.92) | +118 |
| Toqueque | 642 | 0.18 | 0.10 (11/turn) | cheese 5 (6.83->10.36), salt 4 (4.45->8.74), thread 8 (4.66->5.27) | garments 20 (21.84->25.65), tar 1 (10.92->11.8) | +106 |
| Clairas | 374 | 0.10 | 0.20 (21/turn) | yarn 4 (5.15->7.41), rope 2 (74->77.9), wrought iron 1 (12.5->13.39), bricks 1 (4.6->6.79) | garments 20 (23.31->25.65), beer 19 (3.4->4.42), thread 26 (4.81->5.5), flax fibres 9 (5.41->6.9) | +98 |

**Best:** Rouhomme at about +226 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 54 @ min 3.72 | makes 56.0, uses 19.2, holds 298 (keeps 60): sells the surplus + 17/turn of the excess |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 6 = 4.0 turns |
| cured meat | 6 @ 24.4, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 24 = 4.0 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 24 = 3.9 turns |
| fish | 8 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 8 = 1.1 turns |
| garments |  | 25 @ min 26.6 | makes 21.7, uses 2.1, holds 117 (keeps 30): sells the surplus + 6/turn of the excess |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 103 = 4.0 turns |
| labour | 327 @ 2.2, stop - |  | uses 760.5/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 356 = 1.1 turns |
| limestone |  | 5 @ min 21.6 |  |
| meat | 8 @ 3.02, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 8 = 1.1 turns |
| nets |  | 7 @ min 36.0 | makes 6.0, uses 0.0, holds 61 (keeps 40): sells the surplus + 1/turn of the excess |
| porterage | 33 @ 0.8, stop - |  | uses 29.6/turn (observed), makes 0.0, holds 37 = 1.3 turns |
| rope |  | 5 @ min 72.0 |  |
| timber |  | 30 @ min 8.5 | makes 24.0, uses 0.0, holds 444 (keeps 350): sells the surplus + 6/turn of the excess |
| tools | 7 @ 6.2, stop 51 |  | uses 6.3/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 31.8 turns |

## Self-diagnosis

Nothing found this run.
