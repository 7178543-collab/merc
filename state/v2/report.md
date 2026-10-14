# v2 shadow report

Turn 13280, 2026-10-14 17:57. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,101, prestige 0 (-2,670 free, +0.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 298 | 0 | 19 | 0 | 0 | min_holding 60, sell 54, sell @ 3.72 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 24 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 8 | 8 | 7 | 0 | 1 | stop 24, buy 8, buy @ 2.5 |
| garments | 117 | 0 | 2 | 0 | 0 | min_holding 30, sell 25, sell @ 26.6 |
| grain | 103 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 356 | 585 | 712 | 0 | 323 | buy 327, buy @ 2.2 |
| meat | 8 | 8 | 7 | 0 | 1 | stop 24, buy 8, buy @ 3.02 |
| nets | 61 | 0 | 0 | 0 | 0 | min_holding 40, sell 7, sell @ 36 |
| porterage | 37 | 37 | 25 | 0 | 12 | buy 37, buy @ 0.8 |

**0 risks, 1 waste, 4 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **labour**: 323 labour expired last turn (~552 coin): holding 356 against a ~38 buffer target -> v2: trim the buy until the stock is near 38

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **rope**: floor 80.00 vs home bid 69.50: barely selling (0 of 4)
- **timber**: build materials for park 1 are in (438.0 held, 30 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 25% (EXPANSION), about 9 turns left; still to deliver: labour 195, limestone 45, timber 30; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 45 | 113.6 | 0 | off: covered |
| timber | 30 | 438.0 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 22

## Prestige spending, cheapest coin per prestige first

1121 turns left: prestige gained now converts 99.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.3 | 54.6 | running |
| hold banquet 2 (pies) | mansion | 7 | 56.3 | 56.3 | thin at home: pies, candles |
| hold banquet 3 (pies) | mansion | 8 | 56.4 | 56.4 | thin at home: pies, candles |
| hold banquet 4 (pies) | mansion | 18 | 58.8 | 58.8 | thin at home: pies, candles |
| hold mass 2 (premium) | cathedral | 360 | 58.5 | 59.3 | needs a cathedral (build cost 284,540); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 2 (meat) | mansion | 6.8 | 59.7 | 59.7 |  |
| hold banquet 3 (meat) | mansion | 7.6 | 60.4 | 60.4 |  |
| jousting 1 | arena | 170 | 60.5 | 60.6 | needs a arena (build cost 26,634); thin at home: protection, light armour, arms; needs weaponry skill |
| jousting 3 | arena | 230 | 60.9 | 61.0 | needs a arena (build cost 26,634); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (meat) | mansion | 4.2 | 61.3 | 61.3 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 62.4 | 62.4 | thin at home: cured fish |
| hold sermon 2 (candles) | church | 31 | 60.5 | 62.7 | needs a church (build cost 71,295); thin at home: jewellery, candles, furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 108202735 | 0.036 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | cured meat 2 | -46 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Toqueque: cheese sell 4 @ 11.1, salt sell 7 @ 8.2; crew 0.1; est +33 a turn
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn; best orders clear only -3 a turn after crew: ship stays at 0
- best towns now: Kirchwerp +81, Coburgbaum +80, Cobholme +78, Darmwald +72, Orlesailles +68
- Kirchwerp would trade: acid buy 1 @ 146, butter sell 1 @ 76.0, medicine buy 1 @ 174; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~105 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Rouhomme | 368 | 0.10 | 0.50 (53/turn) | cheese 14 (6.62->11.21), bread 134 (2.48->3.19), lead ore 6 (6.2->13.59), yarn 7 (5.35->8.69) | garments 20 (23.31->26.03) | +264 |
| Clairas | 374 | 0.10 | 0.20 (21/turn) | nets 5 (19.55->41.04), rope 3 (69.5->76.47), bricks 1 (4.4->8.69), cured meat 2 (22.8->23.75) | garments 20 (22.89->26.03), thread 26 (4.73->5.55), flax fibres 9 (5.67->6.55), beer 19 (3.36->3.84) | +214 |
| Bedenis | 566 | 0.16 | 0.10 (11/turn) | nets 5 (19.55->44.08), cured meat 2 (22.8->25.84), cheese 17 (6.62->7.03), wax 2 (24.78->26.03) | garments 20 (22.05->26.03), slaked lime 1 (11.13->12.16) | +208 |
| Etallaen | 774 | 0.22 | 0.10 (11/turn) | nets 5 (19.55->41.42), tools 16 (4.76->6.65), wax 2 (24.78->26.22) | garments 20 (22.89->26.03), wine 9 (5.25->5.94), furniture 1 (12.71->13.9), seeds 1 (1.84->2.32) | +198 |
| Fulkirch | 1576 | 0.66 | 0.30 (32/turn) | nets 5 (19.55->41.99), rope 2 (69.5->79.8), light armour 2 (86.1->91.67), varnish 1 (18.17->21.09) | garments 20 (22.47->26.03), canvas 1 (31.5->35.15), stockfish 1 (104.48->107.35), candles 1 (77.17->78.5) | +197 |

**Best:** Rouhomme at about +264 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 54 @ min 3.7 | makes 56.0, uses 19.2, holds 298 (keeps 60): sells the surplus + 17/turn of the excess |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 6 = 4.0 turns |
| cured meat | 6 @ 24.4, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 24 = 4.0 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 24 = 3.9 turns |
| fish | 8 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 8 = 1.1 turns |
| garments |  | 23 @ min 22.0 | makes 19.7, uses 2.1, holds 117 (keeps 30): sells the surplus + 6/turn of the excess |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 103 = 4.0 turns |
| labour | 313 @ 2.2, stop - |  | uses 747.5/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 356 = 1.2 turns |
| limestone |  | 5 @ min 21.6 |  |
| meat | 8 @ 3.02, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 8 = 1.1 turns |
| nets |  | 7 @ min 36.0 | makes 6.0, uses 0.0, holds 61 (keeps 40): sells the surplus + 1/turn of the excess |
| porterage | 33 @ 0.8, stop - |  | uses 29.6/turn (observed), makes 0.0, holds 37 = 1.3 turns |
| rope |  | 5 @ min 72.0 |  |
| timber |  | 29 @ min 8.5 | makes 24.0, uses 0.0, holds 438 (keeps 350): sells the surplus + 5/turn of the excess |
| tools | 7 @ 6.2, stop 51 |  | uses 6.3/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 31.8 turns |

## Self-diagnosis

Nothing found this run.
