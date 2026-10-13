# v2 shadow report

Turn 13243, 2026-10-13 04:42. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, meat, nets, porterage; v1 runs everything else.
Cash 25,187, prestige 2,583 (163 free, +4.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 211 | 0 | 19 | 0 | 0 | min_holding 60, stop 8, buy 4, buy @ 6, sell 20, sell @ 4.1; min_holding 60, sell 140, sell @ 3.7 |
| cured fish | 19 | 6 | 6 | 0 | 0 | stop 20, buy 7, buy @ 26 |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 25 | 0 | 6 | 0 | 0 | stop 26, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 6 | 0 | 1 | stop 24, buy 7, buy @ 2.5 |
| garments | 371 | 0 | 2 | 0 | 0 | min_holding 30, sell 45, sell @ 22; min_holding 30, sell 15, sell @ 21.6 |
| grain | 130 | 34 | 32 | 0 | 0 | stop 130, buy 33, buy @ 3.7 |
| meat | 7 | 7 | 6 | 0 | 1 | stop 24, buy 7, buy @ 3.02 |
| nets | 41 | 0 | 0 | 0 | 0 | min_holding 40, sell 6, sell @ 36 |
| porterage | 26 | 26 | 17 | 0 | 9 | buy 26, buy @ 0.8 |

**1 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax plants**: retting pit 1 ran short of flax plants (buy is live (no volume cap @ 2.04), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~34/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **Flax Wyrm**: Flax Wyrm cost 25 coin last turn (crew 0.25) and its route traded nothing (route limited by beer) -> v2: pause it (crew 0) until a route is proven to sell

## Tuning

- **cloth**: cloth buffer thin: 1.1 turns (target 4) -> v2: lift the maker's rate or hold back sales until it reaches 361
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **timber**: build materials for park 1 are in (443.4 held, 36 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 11% (EXPANSION), about 11 turns left; still to deliver: labour 232, limestone 54, timber 36; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 54 | 151.0 | 0 | off: covered |
| timber | 36 | 443.4 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 22

## Prestige spending, cheapest coin per prestige first

1158 turns left: prestige gained now converts 99.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: waiting - level 2 costs 250, free 163: ~21 turns at +4.2/turn

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.6 | 52.5 | running |
| hold banquet 2 (pies) | mansion | 7 | 56.5 | 56.5 | thin at home: pasties, pies, candles |
| hold banquet 3 (pies) | mansion | 8 | 56.7 | 56.7 | thin at home: pasties, hop beer, pies, candles |
| hold banquet 4 (pies) | mansion | 18 | 58.0 | 58.0 | thin at home: pasties, hop beer, candles |
| hold banquet 2 (fish) | mansion | 6.8 | 58.2 | 58.2 | thin at home: cured fish |
| hold sermon 2 (candles) | church | 31 | 56.1 | 58.4 | needs a church (build cost 76,282); thin at home: jewellery, candles, furniture |
| jousting 1 | arena | 170 | 58.3 | 58.4 | needs a arena (build cost 28,684); thin at home: protection, light armour, arms; needs weaponry skill |
| hold feast 2 | townhouse | 2.6 | 56.7 | 58.9 | needs a townhouse (build cost 6,608) |
| hold banquet 1 (fish) | mansion | 4.2 | 59.2 | 59.2 | running |
| hold prayer 2 | chapel | 13 | 56.7 | 59.3 | needs a chapel (build cost 36,446); thin at home: furniture |
| hold banquet 3 (fish) | mansion | 7.6 | 59.4 | 59.4 | thin at home: hop beer, cured fish |
| jousting 3 | arena | 230 | 59.3 | 59.4 | needs a arena (build cost 28,684); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.4 / 0.25 | 25 | 117401698 | 0.548 | - | - | 0 |
| linen snake | 0.1 / 0.40 | 39 | 109102068 | 0.136 | garments 48 | - | 444 |

## Ship plans (this turn's world prices)

- **linen snake** on Etallaen: garments sell 34 @ 28.6; crew 0.1; est +204 a turn
- **Flax Wyrm** on Brebronn: beer sell 56 @ 4.8, garments sell 25 @ 28.0; crew 0.4; est +163 a turn
- best towns now: Etallaen +204, Brebronn +163, Donaunieder +66, Orlesailles +60, Herschweig +56

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~102 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Brebronn | 862 | 0.25 | 0.40 (41/turn) | garments 25 (21.4->26.98), beer 56 (2.98->4.64), glassware 1 (74.03->92.62), nets 2 (44->45.41) | cloth 38 (8.4->9), soap 1 (103.43->114), thread 13 (4.83->5.75), salt 5 (5.17->6.74) | +259 |
| Etallaen | 774 | 0.21 | 0.20 (20/turn) | garments 34 (21.4->27.55), grindstones 1 (342.3->353.4) | flax fibres 1 (6.09->7.03), hop beer 6 (7.46->8.12), resin 1 (1.6->2.18) | +206 |
| Donaunieder | 985 | 0.32 | 0.60 (61/turn) | beer 63 (2.98->5.22), garments 21 (21.4->22.23), cloth 11 (7.4->8.17), tar 1 (9.65->12.54) | salt 4 (4.58->6.74), potash 1 (14.8->16.05), flax plants 1 (1.67->2.38) | +124 |
| Orlesailles | 1178 | 0.42 | 0.30 (31/turn) | garments 32 (21.4->23.94), cloth 17 (7.4->8.84), cheese 13 (7.14->8.74), varnish 1 (18.17->20.14) | salt 5 (4.6->6.74), wax 4 (20.58->22.23), flax fibres 2 (5.67->7.03), pies 1 (16.28->17.95) | +117 |
| Vauxvais | 204 | 0.06 | 0.30 (31/turn) | garments 20 (21.4->22.42), timber 21 (6.6->8.22), beer 57 (2.98->3.23), bricks 1 (3.64->9.79) | limestone 2 (12.6->24.7), thread 14 (4.73->5.75), cloth 12 (8.03->9), salt 2 (4.64->6.74) | +100 |

**Best:** Brebronn at about +259 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 27.6, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 10 @ min 3.7 | makes 70.0, uses 18.6, holds 211 (keeps 60): sells the surplus + 8/turn of the excess; ships offer 56 a turn abroad, so home sells 10 (was 60) |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 10 = 6.7 turns |
| cured fish | 7 @ 26.0, stop 20 |  | uses 5.5/turn (mansion 1), makes 0.0, holds 19 = 3.5 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 26 |  | uses 6.4/turn (brewery 1, household upkeep), makes 0.0, holds 25 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 7 = 1.2 turns |
| garments |  | 10 @ min 22.0 | makes 46.3, uses 1.8, holds 371 (keeps 30): sells the surplus + 25/turn of the excess; ships offer 59 a turn abroad, so home sells 10 (was 69) |
| grain | 33 @ 3.7, stop 130 |  | uses 32.5/turn (brewery 1), makes 0.0, holds 130 = 4.0 turns |
| labour | 610 @ 2.2, stop - |  | uses 1030.1/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 486 = 0.8 turns |
| light armour | 1 @ 112, stop 1 |  | uses 0.2/turn (household upkeep), makes 0.0, holds 1 = 7.0 turns |
| limestone |  | 5 @ min 25.0 |  |
| meat | 7 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 7 = 1.2 turns |
| nets |  | 6 @ min 36.0 |  |
| porterage | 26 @ 0.8, stop - |  | uses 23.4/turn (observed), makes 0.0, holds 26 = 1.1 turns |
| timber |  | 30 @ min 8.5 | makes 24.0, uses 0.0, holds 443 (keeps 350): sells the surplus + 6/turn of the excess |
| tools | 7 @ 6.2, stop 49 |  | uses 6.1/turn (logging camp w/ tool), makes 0.0, holds 199 = 32.8 turns |
