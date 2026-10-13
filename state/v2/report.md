# v2 shadow report

Turn 13251, 2026-10-13 12:54. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, meat, nets, porterage; v1 runs everything else.
Cash 23,103, prestige 2,607 (187 free, +3.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 311 | 0 | 19 | 0 | 0 | min_holding 60, sell 67, sell @ 3.7 |
| cured fish | 20 | 7 | 6 | 0 | 0 | stop 20, buy 7, buy @ 26 |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 26 | 6 | 6 | 0 | 0 | stop 26, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 6 | 0 | 1 | stop 24, buy 7, buy @ 2.5 |
| garments | 360 | 0 | 2 | 0 | 0 | min_holding 30, sell 62, sell @ 22 |
| grain | 130 | 32 | 32 | 0 | 0 | stop 130, buy 33, buy @ 3.7 |
| meat | 7 | 7 | 6 | 0 | 1 | stop 24, buy 7, buy @ 3.02 |
| nets | 48 | 0 | 0 | 0 | 0 | min_holding 40, sell 6, sell @ 41 |
| porterage | 37 | 37 | 27 | 0 | 10 | buy 37, buy @ 0.8 |

**0 risks, 0 waste, 4 tuning** where v2 would act differently from v1.

## Tuning

- **candles**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax plants**: flax plants buffer thin: 1.8 turns (target 4) -> v2: lift the maker's rate or hold back sales until it reaches 392
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **timber**: build materials for park 1 are in (472.6 held, 13 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 70% (EXPANSION), about 4 turns left; still to deliver: labour 79, limestone 19, timber 13; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 19 | 152.8 | 0 | off: covered |
| timber | 13 | 472.6 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 20

## Prestige spending, cheapest coin per prestige first

1150 turns left: prestige gained now converts 99.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: waiting - level 2 costs 250, free 187: ~18 turns at +3.6/turn

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.9 | 55.0 | running |
| hold sermon 2 (candles) | church | 31 | 54.6 | 56.7 | needs a church (build cost 69,218); thin at home: jewellery, candles |
| hold banquet 2 (pies) | mansion | 7 | 57.9 | 57.9 | thin at home: pasties, cheese, pies, candles |
| hold banquet 3 (pies) | mansion | 8 | 58.1 | 58.1 | thin at home: pasties, cheese, pies, candles |
| hold prayer 2 | chapel | 13 | 55.9 | 58.1 | needs a chapel (build cost 32,437) |
| hold banquet 4 (pies) | mansion | 18 | 58.2 | 58.2 | thin at home: pasties, cheese, candles |
| hold sermon 2 | church | 24 | 55.9 | 58.6 | needs a church (build cost 69,218); thin at home: jewellery |
| jousting 1 | arena | 170 | 58.7 | 58.9 | needs a arena (build cost 25,517); thin at home: protection, light armour, arms; needs weaponry skill |
| hold mass 2 (premium) | cathedral | 360 | 59.2 | 59.9 | needs a cathedral (build cost 279,830); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 2 (fish) | mansion | 6.8 | 60.2 | 60.2 | thin at home: cured fish, cheese |
| hold feast 2 | townhouse | 2.6 | 57.9 | 60.2 | needs a townhouse (build cost 6,691); thin at home: wine |
| jousting 3 | arena | 230 | 60.2 | 60.3 | needs a arena (build cost 25,517); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 88002195 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 159601387 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Clairlond: nothing pays; crew 0.0; est +0 a turn; best orders clear only 12 a turn after crew: ship stays at 0
- **linen snake** on Kirchwerp: nothing pays; crew 0.0; est +0 a turn; best orders clear only 14 a turn after crew: ship stays at 0
- best towns now: Pontmont +143, Clarfranche +110, Blanans +77, Boistot +64, Bordees +58
- Pontmont would trade: cured fish buy 5 @ 27.4, garments sell 65 @ 24.2; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~108 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Pontmont | 341 | 0.10 | 0.20 (22/turn) | garments 65 (21.8->28.69), furniture 14 (11.55->12.44), grain 10 (2.88->3.19), tar 1 (9.6->10.07) | cured fish 5 (28.35->31.4), flax plants 3 (1.27->2.06), cloth 8 (8.72->9), salt 2 (4.26->4.69) | +462 |
| Clarfranche | 1484 | 0.63 | 0.50 (54/turn) | garments 65 (21.8->27.17), wheels 1 (20.4->25.46), tallow 1 (32.97->35.15) | cured fish 5 (28.56->31.4), cloth 22 (8.09->9), mouldboards 1 (37.38->40.09), yarn 2 (4.03->4.84) | +329 |
| Blanans | 297 | 0.09 | 0.10 (11/turn) | garments 42 (21.8->26.79), furniture 13 (11.55->13.39), dyed cloth 5 (14.49->15.48), tar 2 (9.6->10.92) | cured fish 5 (27.09->31.4), cloth 9 (8.45->9), canvas 2 (33.6->35.15), pies 1 (17.75->18.62) | +262 |
| Boistot | 1230 | 0.48 | 0.20 (22/turn) | garments 33 (21.8->26.98), dyed cloth 4 (14.49->15.48) | cheese 11 (5.25->6.46), cured fish 5 (28.77->31.4) | +173 |
| Bordees | 1112 | 0.41 | 0.20 (22/turn) | garments 35 (21.8->26.98), tar 2 (9.6->10.64) | cured fish 5 (29.61->31.4) | +170 |

**Best:** Pontmont at about +462 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 28.6, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 68 @ min 3.7 | makes 70.0, uses 18.6, holds 311 (keeps 60): sells the surplus + 17/turn of the excess |
| candles | 3 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 0 = 0.0 turns |
| cured fish | 7 @ 26.0, stop 20 |  | uses 5.5/turn (mansion 1), makes 0.0, holds 20 = 3.6 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 26 |  | uses 6.4/turn (brewery 1, household upkeep), makes 0.0, holds 26 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 7 = 1.2 turns |
| garments |  | 63 @ min 22.0 | makes 40.2, uses 1.8, holds 360 (keeps 30): sells the surplus + 24/turn of the excess |
| grain | 33 @ 3.7, stop 130 |  | uses 32.5/turn (brewery 1), makes 0.0, holds 130 = 4.0 turns |
| labour | 557 @ 2.2, stop - |  | uses 980.3/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 467 = 0.9 turns |
| limestone |  | 5 @ min 23.4 |  |
| meat | 7 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 7 = 1.2 turns |
| nets |  | 6 @ min 41.0 |  |
| porterage | 35 @ 0.8, stop - |  | uses 31.6/turn (observed), makes 0.0, holds 37 = 1.2 turns |
| timber |  | 32 @ min 8.5 | makes 24.0, uses 0.0, holds 473 (keeps 350): sells the surplus + 8/turn of the excess |
| tools | 8 @ 6.2, stop 58 |  | uses 7.2/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 27.7 turns |
