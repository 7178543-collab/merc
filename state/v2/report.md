# v2 shadow report

Turn 13255, 2026-10-13 16:45. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, meat, nets, porterage; v1 runs everything else.
Cash 23,069, prestige 2,609 (189 free, +0.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 366 | 0 | 19 | 0 | 0 | min_holding 60, sell 72, sell @ 3.7 |
| cured fish | 22 | 6 | 6 | 0 | 0 | stop 22, buy 6, buy @ 26 |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 25 | 7 | 6 | 0 | 0 | stop 26, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 6 | 0 | 1 | stop 24, buy 7, buy @ 2.5 |
| garments | 311 | 0 | 2 | 0 | 0 | min_holding 30, sell 64, sell @ 22 |
| grain | 130 | 32 | 32 | 0 | 0 | stop 130, buy 33, buy @ 3.7 |
| meat | 7 | 7 | 6 | 0 | 1 | stop 24, buy 7, buy @ 3.02 |
| nets | 50 | 0 | 0 | 0 | 0 | min_holding 40, sell 10, sell @ 41 |
| porterage | 37 | 37 | 21 | 0 | 16 | buy 37, buy @ 0.8 |

**0 risks, 2 waste, 4 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **Flax Wyrm**: Flax Wyrm cost 11 coin last turn (crew 0.10) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell
- **labour**: 58 labour expired last turn (~104 coin): holding 581 against a ~52 buffer target -> v2: trim the buy until the stock is near 52

## Tuning

- **flax plants**: flax plants buffer thin: 1.6 turns (target 4) -> v2: lift the maker's rate or hold back sales until it reaches 428
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **timber**: build materials for park 1 are in (460.1 held, 6 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 87% (EXPANSION), about 2 turns left; still to deliver: labour 34, limestone 8, timber 6; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 8 | 153.0 | 0 | off: covered |
| timber | 6 | 460.1 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 17

## Prestige spending, cheapest coin per prestige first

1146 turns left: prestige gained now converts 99.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: waiting - level 2 costs 250, free 189: ~110 turns at +0.6/turn

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 2 (pies) | mansion | 7 | 53.3 | 53.3 | thin at home: pasties, cheese, pies, candles |
| hold banquet 3 (pies) | mansion | 8 | 55.1 | 55.1 | thin at home: pasties, cheese, pies, candles |
| maintain 1 | park | 0.5 | 53.4 | 56.6 | running |
| hold sermon 2 (candles) | church | 31 | 55.5 | 57.6 | needs a church (build cost 71,236); thin at home: jewellery, candles, furniture |
| hold banquet 4 (pies) | mansion | 18 | 57.7 | 57.7 | thin at home: pasties, cheese, pies, candles, glassware |
| hold banquet 2 (fish) | mansion | 6.8 | 58.5 | 58.5 | thin at home: cured fish, cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 58.6 | 58.6 | running; thin at home: cured fish |
| hold prayer 2 | chapel | 13 | 56.5 | 58.8 | needs a chapel (build cost 33,262); thin at home: furniture |
| hold sermon 2 | church | 24 | 56.5 | 59.3 | needs a church (build cost 71,236); thin at home: jewellery, furniture |
| hold feast 2 | townhouse | 2.6 | 57.2 | 59.5 | needs a townhouse (build cost 6,763) |
| hold mass 2 (premium) | cathedral | 360 | 59.3 | 60.1 | needs a cathedral (build cost 285,705); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 3 (fish) | mansion | 7.6 | 61.3 | 61.3 | thin at home: cured fish, cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 11 | 117101560 | 0.04 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 108202735 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Darmwald: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Toqueque: nothing pays; crew 0.0; est +0 a turn
- best towns now: Clairlond +30
- Clairlond would trade: garments sell 36 @ 23.6; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~110 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Clairlond | 1288 | 0.52 | 0.20 (22/turn) | garments 36 (21.4->23.94), nets 1 (31.77->39.52) | cheese 8 (5.25->7.93), salt 9 (4.49->5.56), wool 2 (9.66->12.06), flax fibres 6 (6.2->7.65) | +108 |
| Fontaux | 411 | 0.12 | 0.40 (44/turn) | timber 15 (6.2->10.07), nets 3 (31.77->41.23), blades 1 (16.8->18.43), charcoal 2 (1.87->3.97) | cheese 13 (6.72->7.93), flax fibres 14 (6.56->7.65), salt 9 (4.35->5.56), wool 2 (8.98->12.06) | +103 |
| Vauxvais | 204 | 0.06 | 0.30 (33/turn) | nets 5 (31.77->40.85), timber 28 (6.2->8.22), thread 16 (4.66->4.94), cloth 9 (8.05->8.31) | flax fibres 5 (6.25->7.65), wool 2 (8.87->12.06), salt 4 (4.83->5.56), tiles 3 (3.34->4.54) | +102 |
| Heidlowe | 662 | 0.19 | 0.20 (22/turn) | nets 6 (31.77->38.38), cloth 9 (8.05->9.59), beer 41 (3.06->3.67), tar 2 (9.2->10.07) | flax fibres 20 (5.83->7.65), wool 2 (9.55->12.06), salt 5 (5.15->5.56), stockfish 1 (106.05->107.35) | +96 |
| Heilegg | 826 | 0.25 | 0.50 (55/turn) | nets 6 (31.77->38.38), beer 76 (3.06->3.88), tallow 1 (32.97->35.15), tar 2 (9.2->9.97) | cheese 13 (6.83->7.93), salt 9 (4.62->5.56), wool 2 (8.98->12.06), flax fibres 7 (6.72->7.65) | +94 |

**Best:** Clairlond at about +108 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 29.8, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 73 @ min 3.7 | makes 70.0, uses 18.6, holds 366 (keeps 60): sells the surplus + 21/turn of the excess |
| cured fish | 6 @ 26.0, stop 22 |  | uses 5.5/turn (mansion 1), makes 0.0, holds 22 = 4.0 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 26 |  | uses 6.4/turn (brewery 1, household upkeep), makes 0.0, holds 25 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 7 = 1.2 turns |
| garments |  | 63 @ min 22.0 | makes 45.5, uses 1.8, holds 311 (keeps 30): sells the surplus + 20/turn of the excess |
| grain | 33 @ 3.7, stop 130 |  | uses 32.5/turn (brewery 1), makes 0.0, holds 130 = 4.0 turns |
| labour | 615 @ 2.2, stop - |  | uses 1034.8/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 581 = 1.0 turns |
| limestone |  | 5 @ min 23.4 |  |
| meat | 7 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 7 = 1.2 turns |
| nets |  | 6 @ min 39.8 |  |
| porterage | 35 @ 0.8, stop - |  | uses 31.6/turn (observed), makes 0.0, holds 37 = 1.2 turns |
| timber |  | 31 @ min 8.5 | makes 24.0, uses 0.0, holds 460 (keeps 350): sells the surplus + 7/turn of the excess |
| tools | 8 @ 6.2, stop 60 |  | uses 7.4/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 27.0 turns |
