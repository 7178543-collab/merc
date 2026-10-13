# v2 shadow report

Turn 13256, 2026-10-13 17:43. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, meat, nets, porterage; v1 runs everything else.
Cash 23,076, prestige 2,660 (240 free, +0.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 377 | 0 | 19 | 0 | 0 | min_holding 60, sell 73, sell @ 3.7 |
| cured fish | 21 | 6 | 6 | 0 | 0 | stop 22, buy 6, buy @ 26 |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 26 | 6 | 6 | 0 | 0 | stop 26, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 6 | 0 | 1 | stop 24, buy 7, buy @ 2.5 |
| garments | 307 | 0 | 2 | 0 | 0 | min_holding 30, sell 63, sell @ 22 |
| grain | 130 | 33 | 32 | 0 | 0 | stop 130, buy 33, buy @ 3.7 |
| meat | 7 | 7 | 6 | 0 | 1 | stop 24, buy 7, buy @ 3.02 |
| nets | 50 | 0 | 0 | 0 | 0 | min_holding 40, sell 6, sell @ 39.8 |
| porterage | 37 | 37 | 20 | 0 | 17 | buy 37, buy @ 0.8 |

**0 risks, 1 waste, 4 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **labour**: 85 labour expired last turn (~149 coin): holding 518 against a ~52 buffer target -> v2: trim the buy until the stock is near 52

## Tuning

- **cured fish**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax plants**: flax plants buffer thin: 1.6 turns (target 4) -> v2: lift the maker's rate or hold back sales until it reaches 428
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **timber**: build materials for park 1 are in (464.1 held, 2 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 96% (EXPANSION), about 1 turns left; still to deliver: labour 11, limestone 3, timber 2; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 3 | 153.0 | 0 | off: covered |
| timber | 2 | 464.1 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 11

## Prestige spending, cheapest coin per prestige first

1145 turns left: prestige gained now converts 99.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: waiting - level 2 costs 250, free 240: ~19 turns at +0.6/turn

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 2 (pies) | mansion | 7 | 52.5 | 52.5 | thin at home: pasties, pies |
| hold banquet 3 (pies) | mansion | 8 | 52.7 | 52.7 | thin at home: pasties, hop beer, pies |
| maintain 1 | park | 0.5 | 52.5 | 56.1 | running |
| hold banquet 4 (pies) | mansion | 18 | 57.7 | 57.7 | thin at home: pasties, hop beer, pies |
| hold banquet 2 (fish) | mansion | 6.8 | 58.6 | 58.6 | thin at home: cured fish |
| hold prayer 2 | chapel | 13 | 56.3 | 58.8 | needs a chapel (build cost 35,474) |
| hold banquet 3 (fish) | mansion | 7.6 | 58.9 | 58.9 | thin at home: hop beer, cured fish |
| hold sermon 2 (candles) | church | 31 | 56.8 | 59.1 | needs a church (build cost 75,522); thin at home: jewellery, candles, furniture |
| hold sermon 2 | church | 24 | 57.4 | 60.4 | needs a church (build cost 75,522); thin at home: jewellery, furniture |
| hold banquet 1 (fish) | mansion | 4.2 | 60.5 | 60.5 | running; thin at home: cured fish |
| jousting 1 | arena | 170 | 61.4 | 61.5 | needs a arena (build cost 28,060); thin at home: protection, light armour, arms; needs weaponry skill |
| jousting 3 | arena | 230 | 61.4 | 61.5 | needs a arena (build cost 28,060); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 117101560 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 108202735 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Darmwald: nothing pays; crew 0.0; est +0 a turn; best orders clear only 8 a turn after crew: ship stays at 0
- **linen snake** on Toqueque: nothing pays; crew 0.0; est +0 a turn
- best towns now: Clairlond +29
- Clairlond would trade: garments sell 35 @ 23.6; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~109 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hanstein | 380 | 0.11 | 0.40 (43/turn) | fleece 3 (7.46->8.07), charcoal 2 (2.18->3.32), lead bars 2 (12.5->12.92), paper 4 (21.42->21.85) | flax fibres 27 (6.04->7.2), thread 71 (5.04->5.5), jewellery 1 (79.8->88.35), cloth 13 (7.93->8.5) | +71 |
| Rouhomme | 368 | 0.11 | 0.50 (54/turn) | bread 134 (2.44->3), cheese 8 (6.25->7.6), furniture 12 (12.39->13.3), grain 10 (2.98->3.29) | cloth 16 (7.46->8.5), jewellery 1 (85.58->88.35), wool 1 (10.08->11.4) | +69 |
| Clairlond | 1288 | 0.52 | 0.20 (22/turn) | garments 35 (21.6->22.8), wheels 1 (19.4->20.9) | soap 1 (89.25->118.75), salt 11 (4.58->5.56), wool 1 (9.55->11.4) | +59 |
| Hofkirchen | 991 | 0.34 | 0.10 (11/turn) | flax fibres 10 (7.1->10.16), nets 2 (42.2->44.65), wheels 1 (19.4->22.8) | acid 1 (166.95->183.35), salt 13 (4.83->5.56), steel ingots 1 (9.08->14.63), wool 1 (8.93->11.4) | +59 |
| Heilegg | 826 | 0.25 | 0.60 (65/turn) | beer 77 (3.07->3.89), furniture 12 (12.39->13.68), wheels 1 (19.4->21.66), cheese 17 (6.25->6.55) | salt 13 (4.62->5.56), jewellery 1 (80.85->88.35), wool 1 (8.98->11.4), hop beer 4 (7.56->8.41) | +51 |

**Best:** Hanstein at about +71 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 74 @ min 3.7 | makes 70.0, uses 18.6, holds 377 (keeps 60): sells the surplus + 22/turn of the excess |
| cured fish | 6 @ 26.0, stop 22 |  | uses 5.5/turn (mansion 1), makes 0.0, holds 21 = 3.9 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 26 |  | uses 6.4/turn (brewery 1, household upkeep), makes 0.0, holds 26 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 7 = 1.2 turns |
| garments |  | 63 @ min 22.0 | makes 45.5, uses 1.8, holds 307 (keeps 30): sells the surplus + 19/turn of the excess |
| grain | 33 @ 3.7, stop 130 |  | uses 32.5/turn (brewery 1), makes 0.0, holds 130 = 4.0 turns |
| labour | 608 @ 2.2, stop - |  | uses 1028.8/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 518 = 0.9 turns |
| limestone |  | 5 @ min 23.4 |  |
| meat | 7 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 7 = 1.2 turns |
| nets |  | 6 @ min 41.0 |  |
| porterage | 35 @ 0.8, stop - |  | uses 31.6/turn (observed), makes 0.0, holds 37 = 1.2 turns |
| timber |  | 32 @ min 8.5 | makes 24.0, uses 0.0, holds 464 (keeps 350): sells the surplus + 8/turn of the excess |
| tools | 8 @ 6.2, stop 60 |  | uses 7.4/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 27.1 turns |
