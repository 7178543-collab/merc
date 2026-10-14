# v2 shadow report

Turn 13277, 2026-10-14 14:58. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,253, prestige 0 (-2,670 free, +0.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 294 | 0 | 19 | 0 | 0 | min_holding 60, sell 55, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 24 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 8 | 8 | 7 | 0 | 1 | stop 24, buy 8, buy @ 2.5 |
| garments | 139 | 0 | 2 | 0 | 0 | min_holding 30, sell 36, sell @ 22 |
| grain | 103 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 541 | 661 | 903 | 0 | 208 | buy 541, buy @ 2.2 |
| meat | 8 | 8 | 7 | 0 | 1 | stop 24, buy 8, buy @ 3.02 |
| nets | 59 | 0 | 0 | 0 | 0 | min_holding 40, sell 7, sell @ 37.8 |
| porterage | 37 | 37 | 21 | 0 | 16 | buy 37, buy @ 0.8 |

**0 risks, 1 waste, 4 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **labour**: 208 labour expired last turn (~373 coin): holding 541 against a ~51 buffer target -> v2: trim the buy until the stock is near 51

## Tuning

- **candles**: home ask 77.00 is above our ceiling 70.00 and last turn bought 1 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **timber**: build materials for park 1 are in (415.1 held, 40 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 0% (EXPANSION), about 12 turns left; still to deliver: labour 260, limestone 60, timber 40; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 60 | 113.0 | 0 | off: covered |
| timber | 40 | 415.1 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 22

## Prestige spending, cheapest coin per prestige first

1124 turns left: prestige gained now converts 99.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 2 (pies) | mansion | 7 | 55.9 | 55.9 | thin at home: pasties, pies |
| hold banquet 3 (pies) | mansion | 8 | 56.6 | 56.6 | thin at home: pasties, pies |
| hold sermon 2 (candles) | church | 31 | 55.0 | 57.3 | needs a church (build cost 75,084); thin at home: jewellery, furniture |
| maintain 1 | park | 0.5 | 53.7 | 57.5 | running |
| hold prayer 2 | chapel | 13 | 55.5 | 58.0 | needs a chapel (build cost 35,724); thin at home: furniture |
| hold sermon 2 | church | 24 | 55.1 | 58.1 | needs a church (build cost 75,084); thin at home: jewellery, furniture |
| hold banquet 4 (pies) | mansion | 18 | 58.6 | 58.6 | thin at home: pies |
| hold mass 2 (premium) | cathedral | 360 | 58.6 | 59.4 | needs a cathedral (build cost 295,070); thin at home: furniture, jewellery, glassware, candles, premium garments |
| jousting 1 | arena | 170 | 59.7 | 59.8 | needs a arena (build cost 28,688); thin at home: protection, light armour, arms; needs weaponry skill |
| hold mass 1 | cathedral | 180 | 59.8 | 61.4 | needs a cathedral (build cost 295,070); thin at home: jewellery, glassware, candles |
| jousting 3 | arena | 230 | 61.5 | 61.6 | needs a arena (build cost 28,688); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 61.9 | 61.9 | thin at home: cured fish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 108202735 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.10 | 11 | 141901647 | 0 | nets 4 | cured meat 6, hop beer 1 | -60 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Toqueque: casks sell 1 @ 7.85, cheese sell 7 @ 11.3, salt sell 4 @ 7.5; crew 0.1; est +36 a turn
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn; best orders clear only 9 a turn after crew: ship stays at 0
- best towns now: Gottweiler +80, Magdeach +49, Boistot +49, Kirchwerp +42, Hofkirchen +37
- Gottweiler would trade: cured meat buy 6 @ 21.8, grindstones buy 1 @ 226, steel ingots buy 2 @ 13.3; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~110 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.35 | 1.00 (110/turn) | bread 73 (2.81->5.27), beer 31 (3.14->4.84), tools 8 (4.76->5.42), thread 16 (4.66->5.08) | cured meat 3 (23.52->27.8), canvas 1 (24.99->32.68), garments 11 (22.68->23.56), pasties 2 (11.45->13.21) | +173 |
| Chatgnan | 728 | 0.21 | 0.30 (33/turn) | beer 56 (3.14->5.37), honey 2 (9.92->10.45), thread 2 (4.66->5.27), casks 1 (6.51->7.41) | garments 20 (21.84->23.56), hides 1 (11.65->13.01) | +132 |
| Rouhomme | 368 | 0.11 | 0.60 (66/turn) | cheese 12 (6.67->8.98), flour 2 (20.58->30.4), beer 56 (3.14->3.65), yarn 7 (4.77->6.79) | garments 20 (22.89->23.56), casks 2 (3.51->5.08), cured meat 6 (27.3->27.8), tools 7 (4.91->5.15) | +105 |
| Toqueque | 642 | 0.19 | 0.10 (11/turn) | cheese 7 (6.67->11.02), salt 4 (4.28->8.07), thread 16 (4.66->5.42), casks 1 (6.51->7.6) | garments 20 (21.84->23.56), rope 2 (79.8->80.75) | +84 |
| Grandgues | 152 | 0.04 | 0.20 (22/turn) | timber 29 (6.25->7.55), firewood 1 (2.16->5.08), resin 1 (2.58->3.32), flax plants 1 (1.41->1.86) | cured meat 5 (22.68->27.8), garments 20 (22.47->23.56), tar 1 (10.82->11.5), grain 26 (2.92->3.02) | +68 |

**Best:** Hofkirchen at about +173 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 53 @ min 3.7 | makes 56.0, uses 19.2, holds 294 (keeps 60): sells the surplus + 16/turn of the excess |
| candles | 3 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 0 = 0.0 turns |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 12 = 2.0 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 24 = 3.9 turns |
| fish | 8 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 8 = 1.1 turns |
| garments |  | 28 @ min 22.0 | makes 22.6, uses 2.1, holds 139 (keeps 30): sells the surplus + 7/turn of the excess |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 103 = 4.0 turns |
| labour | 585 @ 2.2, stop - |  | uses 1007.1/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 541 = 1.0 turns |
| limestone |  | 5 @ min 22.0 |  |
| meat | 8 @ 3.02, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 8 = 1.1 turns |
| nets |  | 7 @ min 43.0 | makes 6.0, uses 0.0, holds 59 (keeps 40): sells the surplus + 1/turn of the excess |
| porterage | 33 @ 0.8, stop - |  | uses 29.6/turn (observed), makes 0.0, holds 37 = 1.3 turns |
| rope |  | 4 @ min 82.5 |  |
| timber |  | 27 @ min 8.5 | makes 24.0, uses 0.0, holds 415 (keeps 350): sells the surplus + 3/turn of the excess |
| tools | 8 @ 6.2, stop 63 |  | uses 7.8/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 25.6 turns |

## Self-diagnosis

- R1: candles slot dry: 0.0 held, 1.5 a turn (luxury slot (+3 prestige)); our buy 3 @ 82, home ask 77.0; our bid is already at/over the ask (sellers too thin)
- R1: prestige rate +0.00 a turn vs 12-turn median +3.56; likely: dry slot: candles
- R2: quarry 1 blocked by limestone space: 113 held of 153 capacity, we make 5.2 a turn; buy already stops at 100: add a sell order or more capacity for limestone
