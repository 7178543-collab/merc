# v2 shadow report

Turn 13282, 2026-10-14 19:05. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,877, prestige 0 (-2,670 free, +0.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 280 | 0 | 19 | 0 | 0 | min_holding 60, sell 54, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 24 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 8 | 8 | 7 | 0 | 1 | stop 24, buy 8, buy @ 2.5 |
| garments | 104 | 0 | 2 | 0 | 0 | min_holding 30, sell 23, sell @ 22 |
| grain | 103 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 313 | 313 | 685 | 0 | 78 | buy 313, buy @ 2.2 |
| meat | 8 | 8 | 7 | 0 | 1 | stop 24, buy 8, buy @ 3.02 |
| nets | 53 | 0 | 0 | 0 | 0 | min_holding 40, sell 7, sell @ 36 |
| porterage | 37 | 37 | 25 | 0 | 12 | buy 37, buy @ 0.8 |

**0 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **labour**: 78 labour expired last turn (~128 coin): holding 313 against a ~37 buffer target -> v2: trim the buy until the stock is near 37

## Tuning

- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **timber**: build materials for park 1 are in (460.0 held, 24 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 41% (EXPANSION), about 8 turns left; still to deliver: labour 154, limestone 36, timber 24; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 36 | 114.0 | 0 | off: covered |
| timber | 24 | 460.0 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 20

## Prestige spending, cheapest coin per prestige first

1119 turns left: prestige gained now converts 99.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.9 | 52.2 | running |
| hold banquet 2 (pies) | mansion | 7 | 56.2 | 56.2 | thin at home: wine, cheese, pies |
| hold banquet 3 (pies) | mansion | 8 | 57.2 | 57.2 | thin at home: pies |
| hold banquet 4 (pies) | mansion | 18 | 58.7 | 58.7 | thin at home: wine, pies |
| hold banquet 2 (meat) | mansion | 6.8 | 59.3 | 59.3 | thin at home: wine, cheese |
| hold banquet 1 (meat) | mansion | 4.2 | 60.2 | 60.2 | running |
| jousting 3 | arena | 230 | 60.8 | 60.9 | needs a arena (build cost 26,312); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (meat) | mansion | 7.6 | 61.3 | 61.3 | thin at home: cheese |
| hold feast 2 | townhouse | 2.6 | 59.1 | 61.5 | needs a townhouse (build cost 6,916); thin at home: wine |
| jousting 1 | arena | 170 | 61.8 | 62.0 | needs a arena (build cost 26,312); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 62.7 | 62.7 | thin at home: wine, cured fish, cheese |
| hold banquet 4 | mansion | 17.5 | 63.2 | 63.2 | thin at home: wine, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 10 | 108202735 | 0.044 | salt 3 | - | 11 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Toqueque: cheese sell 4 @ 8.7, nets sell 3 @ 46.2, salt sell 7 @ 8.45; crew 0.1; est +54 a turn
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn; best orders clear only 11 a turn after crew: ship stays at 0
- best towns now: Kirchwerp +90, Orlesailles +58, Amsdermund +54, Toqueque +54, Hofkirchen +52
- Kirchwerp would trade: acid buy 1 @ 146, medicine buy 1 @ 174, nets sell 4 @ 39.6, steel ingots buy 2 @ 13.8; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~102 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Clarfranche | 1484 | 0.59 | 0.20 (20/turn) | nets 5 (19.31->43.32), rope 5 (69->75.52), varnish 1 (18.17->20.71) | garments 20 (21.84->26.6), mouldboards 1 (37.59->43.32) | +231 |
| Kirchwerp | 1072 | 0.37 | 0.20 (20/turn) | nets 4 (19.31->38.38), salt 12 (4.68->5.7) | garments 20 (22.47->26.6), acid 1 (150.15->209), medicine 1 (178.5->181.45), yarn 5 (5.12->6.08) | +220 |
| Rouhomme | 368 | 0.10 | 0.60 (61/turn) | bread 134 (2.46->3.19), nets 2 (19.31->41.99), lead ore 3 (8.03->14.63), beer 55 (3.16->3.65) | garments 20 (23.31->26.6), tools 6 (4.91->5.15) | +217 |
| Clairas | 374 | 0.10 | 0.10 (10/turn) | nets 5 (19.31->41.04), rope 1 (69->86.92), tools 15 (4.76->5.08), cured meat 2 (22.8->23.94) | garments 20 (23.31->26.6), stockfish 1 (94.5->107.35), yarn 6 (4.75->6.08), pasties 1 (11.87->12.92) | +217 |
| Toqueque | 642 | 0.17 | 0.10 (10/turn) | nets 3 (19.31->44.65), salt 7 (4.68->9.17), cloth 16 (8->8.64), cheese 4 (6.72->8.41) | garments 20 (21.84->26.6), tar 1 (10.03->10.6), yarn 1 (5.51->6.08) | +211 |

**Best:** Clarfranche at about +231 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 52 @ min 3.7 | makes 56.0, uses 19.2, holds 280 (keeps 60): sells the surplus + 15/turn of the excess |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 8 = 5.3 turns |
| cured meat | 6 @ 24.4, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 24 = 4.0 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 24 = 3.9 turns |
| fish | 8 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 8 = 1.1 turns |
| garments |  | 20 @ min 26.8 | makes 17.6, uses 2.1, holds 104 (keeps 30): sells the surplus + 5/turn of the excess |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 103 = 4.0 turns |
| labour | 298 @ 2.2, stop - |  | uses 733.2/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 313 = 1.1 turns |
| limestone |  | 5 @ min 21.2 |  |
| meat | 8 @ 3.02, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 8 = 1.1 turns |
| nets |  | 7 @ min 42.6 |  |
| porterage | 33 @ 0.8, stop - |  | uses 29.6/turn (observed), makes 0.0, holds 37 = 1.3 turns |
| rope |  | 5 @ min 84.5 |  |
| timber |  | 31 @ min 8.5 | makes 24.0, uses 0.0, holds 460 (keeps 350): sells the surplus + 7/turn of the excess |
| tools | 7 @ 6.2, stop 50 |  | uses 6.2/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 32.1 turns |

## Self-diagnosis

Nothing found this run.
