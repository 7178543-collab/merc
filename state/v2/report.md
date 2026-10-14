# v2 shadow report

Turn 13268, 2026-10-14 05:56. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, meat, nets, porterage; v1 runs everything else.
Cash 16,004, prestige 2,802 (132 free, +3.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 391 | 0 | 19 | 0 | 0 | min_holding 60, sell 62, sell @ 3.7 |
| cured fish | 20 | 0 | 6 | 0 | 0 | stop 22, buy 6, buy @ 26 |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 24 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 8 | 8 | 7 | 0 | 1 | stop 24, buy 8, buy @ 2.5 |
| garments | 213 | 0 | 2 | 0 | 0 | min_holding 30, sell 55, sell @ 22 |
| grain | 103 | 19 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| meat | 8 | 8 | 7 | 0 | 1 | stop 24, buy 8, buy @ 3.02 |
| nets | 53 | 0 | 0 | 0 | 0 | min_holding 40, sell 7, sell @ 40.6 |
| porterage | 37 | 37 | 28 | 0 | 9 | buy 37, buy @ 0.8 |

**1 risks, 0 waste, 4 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **labour**: buying 567, short of ~664 needed -> v2: buy 664

## Tuning

- **cured fish**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax plants**: flax plants buffer thin: 1.5 turns (target 4) -> v2: lift the maker's rate or hold back sales until it reaches 453
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **timber**: build materials for park 1 are in (419.9 held, 19 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 53% (EXPANSION), about 6 turns left; still to deliver: labour 123, limestone 29, timber 19; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 29 | 132.1 | 0 | off: covered |
| timber | 19 | 419.9 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 21

## Prestige spending, cheapest coin per prestige first

1133 turns left: prestige gained now converts 99.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 2 (pies) | mansion | 7 | 56.7 | 56.7 | thin at home: pies, candles |
| maintain 1 | park | 0.5 | 53.1 | 56.8 | running |
| hold banquet 3 (pies) | mansion | 8 | 57.0 | 57.0 | thin at home: pies, candles |
| hold sermon 2 (candles) | church | 31 | 57.0 | 59.3 | needs a church (build cost 74,505); thin at home: jewellery, candles, furniture |
| hold prayer 2 | chapel | 13 | 56.9 | 59.4 | needs a chapel (build cost 35,824) |
| hold banquet 4 (pies) | mansion | 18 | 59.5 | 59.5 | thin at home: pies, candles |
| hold sermon 2 | church | 24 | 56.5 | 59.5 | needs a church (build cost 74,505); thin at home: jewellery, furniture |
| jousting 1 | arena | 170 | 59.8 | 59.9 | needs a arena (build cost 28,409); thin at home: protection, light armour, arms; needs weaponry skill |
| hold mass 2 (premium) | cathedral | 360 | 59.7 | 60.5 | needs a cathedral (build cost 294,770); thin at home: furniture, jewellery, glassware, candles, premium garments |
| jousting 3 | arena | 230 | 61.0 | 61.1 | needs a arena (build cost 28,409); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 62.0 | 62.0 | running; thin at home: cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 62.3 | 62.3 | thin at home: cured fish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 55101678 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 95502502 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Kleinburgh: nothing pays; crew 0.0; est +0 a turn; best orders clear only -9 a turn after crew: ship stays at 0
- **linen snake** on Bordetes: nothing pays; crew 0.0; est +0 a turn; best orders clear only -1 a turn after crew: ship stays at 0
- best towns now: Etallaen +59, Calange +42, Orlesailles +32, Neuborn +26, Cobholme +25
- Etallaen would trade: dyed cloth sell 1 @ 11.9, garments sell 21 @ 25.2, hop beer buy 2 @ 7.5; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~109 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Neuborn | 780 | 0.23 | 0.80 (87/turn) | beer 64 (3.1->4.33), canvas 2 (30.87->36.86), timber 15 (7.55->11.4), dyed cloth 1 (10.5->11.49) | cheese 35 (6.3->6.93), paper 2 (21.63->23.18), wheels 2 (22.89->23.37) | +86 |
| Rouhomme | 368 | 0.11 | 0.50 (55/turn) | bread 136 (2.46->3.29), charcoal 2 (1.79->4.12), wrought iron 1 (12.2->15.11), cheese 8 (7.72->8.07) | nails 4 (6.25->6.46), tools 7 (5.02->5.15) | +71 |
| Hofkirchen | 991 | 0.34 | 1.00 (109/turn) | beer 33 (3.1->4.67), bread 71 (2.46->3.61), thread 22 (4.66->5.22), lead bars 2 (11.76->12.35) | cheese 18 (6.2->6.93), steel ingots 1 (9.08->13.3), cloth 6 (7.88->8.7), hop beer 1 (7.72->9.5) | +59 |
| Toqueque | 642 | 0.19 | 0.10 (11/turn) | salt 13 (4.62->6.79), cheese 8 (7.72->9.79), flax fibres 13 (5.35->6.08), dyed cloth 1 (10.5->11.4) | cloth 12 (8.19->8.7), nails 4 (5.46->6.46) | +55 |
| Etallaen | 774 | 0.23 | 0.10 (11/turn) | garments 21 (21.8->24.32), dyed cloth 1 (10.5->11.49) | cheese 10 (6.46->6.93), hop beer 2 (7.72->9.5), seeds 2 (1.8->2.32) | +53 |

**Best:** Neuborn at about +86 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 61 @ min 3.7 | makes 56.0, uses 19.2, holds 391 (keeps 60): sells the surplus + 25/turn of the excess |
| cured fish | 7 @ 26.0, stop 22 |  | uses 5.5/turn (mansion 1), makes 0.0, holds 20 = 3.7 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 24 = 4.0 turns |
| fish | 8 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 8 = 1.1 turns |
| garments |  | 54 @ min 22.0 | makes 44.3, uses 2.1, holds 213 (keeps 30): sells the surplus + 12/turn of the excess |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 103 = 4.0 turns |
| labour | 664 @ 2.2, stop - |  | uses 1081.6/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 546 = 0.9 turns |
| limestone |  | 5 @ min 23.0 |  |
| meat | 8 @ 3.02, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 8 = 1.1 turns |
| nets |  | 7 @ min 40.6 |  |
| porterage | 35 @ 0.8, stop - |  | uses 31.6/turn (observed), makes 0.0, holds 37 = 1.2 turns |
| rope |  | 4 @ min 82.5 |  |
| timber |  | 28 @ min 8.5 | makes 24.0, uses 0.0, holds 420 (keeps 350): sells the surplus + 4/turn of the excess |
| tools | 8 @ 6.2, stop 61 |  | uses 7.5/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 26.5 turns |
