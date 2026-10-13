# v2 shadow report

Turn 13254, 2026-10-13 15:46. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, meat, nets, porterage; v1 runs everything else.
Cash 23,244, prestige 2,608 (188 free, +0.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 353 | 0 | 19 | 0 | 0 | min_holding 60, sell 70, sell @ 3.7 |
| cured fish | 21 | 7 | 6 | 0 | 0 | stop 22, buy 7, buy @ 26 |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 26 | 6 | 6 | 0 | 0 | stop 26, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 6 | 0 | 1 | stop 24, buy 7, buy @ 2.5 |
| garments | 318 | 0 | 2 | 0 | 0 | min_holding 30, sell 64, sell @ 22 |
| grain | 130 | 33 | 32 | 0 | 0 | stop 130, buy 33, buy @ 3.7 |
| meat | 7 | 7 | 6 | 0 | 1 | stop 24, buy 7, buy @ 3.02 |
| nets | 48 | 0 | 0 | 0 | 0 | min_holding 40, sell 6, sell @ 40.2 |
| porterage | 37 | 37 | 10 | 0 | 27 | buy 37, buy @ 0.8 |

**0 risks, 3 waste, 5 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **Flax Wyrm**: Flax Wyrm cost 78 coin last turn (crew 0.74) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell
- **linen snake**: linen snake cost 64 coin last turn (crew 0.61) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell
- **porterage**: 27 porterage expired last turn (~30 coin): holding 37 against a ~4 buffer target -> v2: trim the buy until the stock is near 4

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax plants**: flax plants buffer thin: 1.5 turns (target 4) -> v2: lift the maker's rate or hold back sales until it reaches 482
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **timber**: build materials for park 1 are in (456.1 held, 9 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 79% (EXPANSION), about 3 turns left; still to deliver: labour 55, limestone 13, timber 9; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 13 | 152.2 | 0 | off: covered |
| timber | 9 | 456.1 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 19

## Prestige spending, cheapest coin per prestige first

1147 turns left: prestige gained now converts 99.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: waiting - level 2 costs 250, free 188: ~110 turns at +0.6/turn

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 2 (pies) | mansion | 7 | 53.1 | 53.1 | thin at home: pasties, cheese, pies, candles |
| hold banquet 3 (pies) | mansion | 8 | 54.5 | 54.5 | thin at home: pasties, cheese, pies, candles |
| maintain 1 | park | 0.5 | 53.1 | 56.5 | running |
| hold sermon 2 (candles) | church | 31 | 55.4 | 57.7 | needs a church (build cost 73,258); thin at home: jewellery, candles, furniture |
| hold banquet 4 (pies) | mansion | 18 | 58.0 | 58.0 | thin at home: pasties, cheese, pies, candles |
| hold prayer 2 | chapel | 13 | 56.4 | 58.9 | needs a chapel (build cost 34,984); thin at home: furniture |
| hold sermon 2 | church | 24 | 56.4 | 59.3 | needs a church (build cost 73,258); thin at home: jewellery, furniture |
| hold mass 2 (premium) | cathedral | 360 | 59.4 | 60.2 | needs a cathedral (build cost 291,135); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 2 (fish) | mansion | 6.8 | 60.6 | 60.6 | thin at home: cured fish, cheese |
| jousting 3 | arena | 230 | 61.2 | 61.4 | needs a arena (build cost 27,528); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 61.8 | 61.8 | running; thin at home: cured fish |
| jousting 1 | arena | 170 | 62.2 | 62.3 | needs a arena (build cost 27,528); thin at home: protection, light armour, arms; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.74 / 0.74 | 78 | 117101560 | 0 | - | - | 0 |
| linen snake | 0.61 / 0.61 | 64 | 108202735 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Darmwald: cured fish buy 5 @ 26.0, nets sell 4 @ 45.8; crew 0.1; est +30 a turn
- **linen snake** on Toqueque: nothing pays; crew 0.0; est +0 a turn; best orders clear only 6 a turn after crew: ship stays at 0
- best towns now: Clairlond +59, Karlmoor +41, Corstoft +34, Darmwald +30, Brebronn +26
- Clairlond would trade: cured fish buy 5 @ 25.8, garments sell 36 @ 23.6; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~109 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Clairlond | 1288 | 0.52 | 0.20 (22/turn) | garments 36 (21.8->24.89), glassware 1 (56.18->58.9) | cured fish 5 (26.67->31.4), cheese 8 (5.25->6.89), flax fibres 5 (6.09->8.45), wool 5 (9.66->10.36) | +130 |
| Hofkirchen | 991 | 0.34 | 0.50 (54/turn) | glassware 1 (56.18->69.35), thread 43 (4.66->5.13), salt 6 (4.43->5.22), wheels 1 (19.8->22.23) | flax fibres 22 (6.25->8.45), cured fish 5 (27.3->31.4), ploughs 1 (67.73->85.5), acid 1 (165.9->179.55) | +121 |
| Heidlowe | 662 | 0.19 | 0.30 (33/turn) | glassware 1 (56.18->66.97), cloth 15 (7.9->8.74), furniture 10 (12.39->14.15), beer 41 (3.06->3.63) | flax fibres 20 (5.93->8.45), cured fish 5 (27.3->31.4), wool 5 (9.61->10.36), cured meat 6 (26.67->27.17) | +107 |
| Rouhomme | 368 | 0.11 | 0.10 (11/turn) | lead ore 5 (6.09->18.9), furniture 10 (12.39->13.77), glassware 1 (56.18->65.55) | cured fish 5 (27.72->31.4), flax fibres 1 (7.14->8.45), flax plants 1 (1.25->2.01), wool 3 (10.08->10.36) | +98 |
| Kirchwerp | 1072 | 0.39 | 0.80 (87/turn) | timber 12 (6.15->14.25), wine 16 (6.35->7.6), glassware 1 (56.18->66.5), wheels 1 (19.8->21.28) | flax fibres 19 (6.09->8.45), cured fish 5 (27.72->31.4), rope 4 (88.2->89.3) | +97 |

**Best:** Clairlond at about +130 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 72 @ min 3.7 | makes 70.0, uses 18.6, holds 353 (keeps 60): sells the surplus + 20/turn of the excess |
| cured fish | 6 @ 26.0, stop 22 |  | uses 5.5/turn (mansion 1), makes 0.0, holds 21 = 3.9 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 26 |  | uses 6.4/turn (brewery 1, household upkeep), makes 0.0, holds 26 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 7 = 1.2 turns |
| garments |  | 64 @ min 22.0 | makes 45.5, uses 1.8, holds 318 (keeps 30): sells the surplus + 20/turn of the excess |
| grain | 33 @ 3.7, stop 130 |  | uses 32.5/turn (brewery 1), makes 0.0, holds 130 = 4.0 turns |
| labour | 634 @ 2.2, stop - |  | uses 1053.8/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 566 = 0.9 turns |
| limestone |  | 5 @ min 23.4 |  |
| meat | 7 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 7 = 1.2 turns |
| nets |  | 10 @ min 41.0 | sell; ships offer 4 a turn abroad, so home sells 10 (was 6) |
| porterage | 35 @ 0.8, stop - |  | uses 31.6/turn (observed), makes 0.0, holds 37 = 1.2 turns |
| timber |  | 31 @ min 8.5 | makes 24.0, uses 0.0, holds 456 (keeps 350): sells the surplus + 7/turn of the excess |
| tools | 8 @ 6.2, stop 62 |  | uses 7.7/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 26.0 turns |
