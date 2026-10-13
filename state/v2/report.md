# v2 shadow report

Turn 13250, 2026-10-13 11:44. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, meat, nets, porterage; v1 runs everything else.
Cash 23,007, prestige 2,603 (183 free, +4.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 298 | 0 | 19 | 0 | 0 | min_holding 60, sell 66, sell @ 3.7 |
| cured fish | 19 | 4 | 6 | 0 | 0 | stop 20, buy 8, buy @ 26 |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 25 | 7 | 6 | 0 | 0 | stop 26, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 6 | 0 | 1 | stop 24, buy 7, buy @ 2.5 |
| garments | 373 | 0 | 2 | 0 | 0 | min_holding 30, sell 66, sell @ 22 |
| grain | 130 | 33 | 32 | 0 | 0 | stop 130, buy 33, buy @ 3.7 |
| meat | 7 | 7 | 6 | 0 | 1 | stop 24, buy 7, buy @ 3.02 |
| nets | 48 | 0 | 0 | 0 | 0 | min_holding 40, sell 6, sell @ 41.6 |
| porterage | 37 | 37 | 27 | 0 | 10 | buy 37, buy @ 0.8 |

**0 risks, 1 waste, 5 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **labour**: 143 labour expired last turn (~248 coin): holding 479 against a ~48 buffer target -> v2: trim the buy until the stock is near 48

## Tuning

- **candles**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **cured fish**: home ask 26.40 is above our ceiling 26.00 and last turn bought 4 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **flax plants**: flax plants buffer thin: 1.9 turns (target 4) -> v2: lift the maker's rate or hold back sales until it reaches 378
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **timber**: build materials for park 1 are in (452.6 held, 16 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 62% (EXPANSION), about 5 turns left; still to deliver: labour 99, limestone 23, timber 16; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 23 | 153.0 | 0 | off: covered |
| timber | 16 | 452.6 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 20

## Prestige spending, cheapest coin per prestige first

1151 turns left: prestige gained now converts 99.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: waiting - level 2 costs 250, free 183: ~17 turns at +4.1/turn

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.9 | 54.9 | running |
| hold banquet 3 (pies) | mansion | 8 | 56.4 | 56.4 | thin at home: pasties, hop beer, cheese, pies, candles |
| hold banquet 4 (pies) | mansion | 18 | 57.3 | 57.3 | thin at home: pasties, hop beer, cheese, candles |
| hold sermon 2 (candles) | church | 31 | 55.4 | 57.5 | needs a church (build cost 68,799); thin at home: jewellery, candles, furniture |
| hold banquet 2 (pies) | mansion | 7 | 58.0 | 58.0 | thin at home: pasties, cheese, pies, candles |
| hold feast 2 | townhouse | 2.6 | 56.4 | 58.7 | needs a townhouse (build cost 6,831) |
| hold prayer 2 | chapel | 13 | 56.9 | 59.1 | needs a chapel (build cost 32,495) |
| hold sermon 2 | church | 24 | 57.0 | 59.7 | needs a church (build cost 68,799); thin at home: jewellery, furniture |
| jousting 1 | arena | 170 | 59.8 | 59.9 | needs a arena (build cost 25,392); thin at home: protection, light armour, arms; needs weaponry skill |
| hold mass 2 (premium) | cathedral | 360 | 59.6 | 60.3 | needs a cathedral (build cost 278,620); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 3 (fish) | mansion | 7.6 | 60.5 | 60.5 | thin at home: hop beer, cured fish, cheese |
| jousting 3 | arena | 230 | 60.5 | 60.6 | needs a arena (build cost 25,392); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 88002195 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 159601387 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Clairlond: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Kirchwerp: nothing pays; crew 0.0; est +0 a turn
- best towns now: Pontmont +58, Orlesailles +25
- Pontmont would trade: garments sell 55 @ 23.4; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~106 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Pontmont | 341 | 0.10 | 0.10 (11/turn) | garments 55 (21.8->26.41), cloth 3 (7.1->7.84), slaked lime 1 (6.77->8.93), grain 10 (2.8->3.12) | cheese 18 (7.72->7.93), flax plants 3 (1.28->2.06), yarn 2 (3.93->4.69) | +259 |
| Clarfranche | 1484 | 0.61 | 0.50 (53/turn) | garments 64 (21.8->24.89), tackles 1 (157.5->180.5), wheels 1 (18.7->20.9), varnish 1 (18.17->18.9) | cheese 18 (6.93->7.93), mouldboards 1 (37.38->41.61) | +191 |
| Blanans | 297 | 0.08 | 0.20 (21/turn) | garments 50 (21.8->24.51), beer 71 (3.04->3.32), cloth 6 (7.1->7.6), dyed cloth 6 (13.44->13.77) | cheese 9 (6.83->7.93), canvas 1 (33.81->34.77), pies 1 (17.75->18.52), flax plants 4 (1.83->2.06) | +155 |
| Boistot | 1230 | 0.47 | 0.40 (42/turn) | garments 46 (21.8->24.7), cloth 23 (7.1->8.74), dyed cloth 5 (13.44->15.01), slaked lime 1 (6.77->9.59) | cheese 12 (7.3->7.93), wax 3 (23.1->23.75) | +150 |
| Kirchwerp | 1072 | 0.38 | 0.40 (42/turn) | garments 64 (21.8->23.56), wine 21 (5.88->7.98), lead ore 1 (7.82->15.86), arms 4 (26.67->28.5) | cheese 18 (7.14->7.93), hop beer 2 (7.46->8.26) | +148 |

**Best:** Pontmont at about +259 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 67 @ min 3.7 | makes 70.0, uses 18.6, holds 298 (keeps 60): sells the surplus + 16/turn of the excess |
| candles | 3 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 2 = 1.0 turns |
| cured fish | 7 @ 26.0, stop 20 |  | uses 5.5/turn (mansion 1), makes 0.0, holds 19 = 3.5 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 26 |  | uses 6.4/turn (brewery 1, household upkeep), makes 0.0, holds 25 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 7 = 1.2 turns |
| garments |  | 62 @ min 22.0 | makes 38.1, uses 1.8, holds 373 (keeps 30): sells the surplus + 26/turn of the excess |
| grain | 33 @ 3.7, stop 130 |  | uses 32.5/turn (brewery 1), makes 0.0, holds 130 = 4.0 turns |
| labour | 531 @ 2.2, stop - |  | uses 955.3/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 479 = 0.9 turns |
| light armour | 1 @ 112, stop 1 |  | uses 0.2/turn (household upkeep), makes 0.0, holds 0 = 0.0 turns |
| limestone |  | 5 @ min 23.6 |  |
| meat | 7 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 7 = 1.2 turns |
| nets |  | 6 @ min 41.0 |  |
| porterage | 35 @ 0.8, stop - |  | uses 31.6/turn (observed), makes 0.0, holds 37 = 1.2 turns |
| timber |  | 31 @ min 8.5 | makes 24.0, uses 0.0, holds 453 (keeps 350): sells the surplus + 7/turn of the excess |
| tools | 8 @ 6.2, stop 57 |  | uses 7.1/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 28.1 turns |
