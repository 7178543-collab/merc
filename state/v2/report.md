# v2 shadow report

Turn 13267, 2026-10-14 04:58. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, meat, nets, porterage; v1 runs everything else.
Cash 16,477, prestige 2,799 (129 free, +99.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 394 | 0 | 4 | 0 | 0 | min_holding 60, sell 63, sell @ 3.7 |
| cured fish | 22 | 6 | 0 | 0 | 0 | stop 22, buy 6, buy @ 26 |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 24 | 6 | 5 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 8 | 8 | 7 | 0 | 1 | stop 24, buy 8, buy @ 2.5 |
| garments | 221 | 0 | 2 | 0 | 0 | min_holding 30, sell 55, sell @ 22 |
| grain | 103 | 26 | 20 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| meat | 8 | 8 | 7 | 0 | 1 | stop 24, buy 8, buy @ 3.02 |
| nets | 54 | 0 | 0 | 0 | 0 | min_holding 40, sell 7, sell @ 41.2 |
| porterage | 37 | 37 | 7 | 0 | 30 | buy 37, buy @ 0.8 |

**0 risks, 0 waste, 6 tuning** where v2 would act differently from v1.

## Tuning

- **cured fish**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax plants**: flax plants buffer thin: 1.6 turns (target 4) -> v2: lift the maker's rate or hold back sales until it reaches 421
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **timber**: build materials for park 1 are in (415.9 held, 22 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 45% (EXPANSION), about 7 turns left; still to deliver: labour 143, limestone 33, timber 22; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 33 | 131.9 | 0 | off: covered |
| timber | 22 | 415.9 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 21

## Prestige spending, cheapest coin per prestige first

1134 turns left: prestige gained now converts 99.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 2 (pies) | mansion | 7 | 56.0 | 56.0 | thin at home: cheese, pies, candles |
| maintain 1 | park | 0.5 | 52.8 | 56.0 | running |
| hold banquet 3 (pies) | mansion | 8 | 57.4 | 57.4 | thin at home: hop beer, cheese, pies, candles |
| hold banquet 2 (fish) | mansion | 6.8 | 57.9 | 57.9 | thin at home: cured fish, cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 58.0 | 58.0 | running; thin at home: cured fish |
| hold sermon 2 (candles) | church | 31 | 56.8 | 59.0 | needs a church (build cost 71,180); thin at home: jewellery, candles, furniture |
| hold prayer 2 | chapel | 13 | 56.7 | 59.1 | needs a chapel (build cost 33,614) |
| hold sermon 2 | church | 24 | 56.3 | 59.1 | needs a church (build cost 71,180); thin at home: jewellery, furniture |
| hold banquet 4 (pies) | mansion | 18 | 59.9 | 59.9 | thin at home: hop beer, pies, candles |
| hold banquet 3 (fish) | mansion | 7.6 | 60.1 | 60.1 | thin at home: hop beer, cured fish, cheese |
| jousting 1 | arena | 170 | 59.9 | 60.1 | needs a arena (build cost 26,651); thin at home: protection, light armour, arms; needs weaponry skill |
| hold mass 2 (premium) | cathedral | 360 | 59.7 | 60.4 | needs a cathedral (build cost 285,000); thin at home: furniture, jewellery, glassware, candles, premium garments |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 55101678 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 95502502 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Kleinburgh: nothing pays; crew 0.0; est +0 a turn; best orders clear only -6 a turn after crew: ship stays at 0
- **linen snake** on Bordetes: nothing pays; crew 0.0; est +0 a turn; best orders clear only 11 a turn after crew: ship stays at 0
- best towns now: Toqueque +21, Clarfranche +19, Hofkirchen +17
- Toqueque would trade: cheese sell 11 @ 7.9, dyed cloth sell 4 @ 11.7, salt sell 11 @ 5.55, tallow sell 2 @ 27.2; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~109 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Calange | 218 | 0.06 | 0.10 (11/turn) | cloth 35 (7.15->9.69), cheese 12 (6.88->8.41), cured fish 1 (23->24.13), tar 2 (9.6->9.79) | nails 3 (5.99->6.46) | +100 |
| Rouhomme | 368 | 0.11 | 0.50 (55/turn) | bread 136 (2.46->3.29), cheese 9 (6.88->7.69), slaked lime 1 (12.08->15.96), charcoal 2 (2.18->4.01) | flax fibres 2 (5.99->6.25), tools 2 (5.02->5.15) | +77 |
| Hanstein | 380 | 0.11 | 0.10 (11/turn) | cloth 35 (7.15->8.64), tallow 2 (24.78->27.55), cured fish 1 (23->24.51), lead bars 2 (12.18->12.54) | flax fibres 27 (5.57->6.25), steel ingots 1 (13.44->15.2), seeds 5 (1.89->2.32) | +70 |
| Orlesailles | 1178 | 0.45 | 0.20 (22/turn) | garments 35 (20.8->22.61), dyed cloth 4 (10.45->13.68), tallow 1 (24.78->30.4), nets 2 (41.8->43.32) | nails 3 (5.78->6.46) | +67 |
| Hofkirchen | 991 | 0.34 | 0.60 (65/turn) | beer 65 (3.1->4.37), tallow 2 (24.78->31.16), thread 36 (4.66->5.22), dyed cloth 4 (10.45->11.4) | steel ingots 1 (9.08->15.2) | +63 |

**Best:** Calange at about +100 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 26.6, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 62 @ min 3.7 | makes 56.0, uses 19.2, holds 394 (keeps 60): sells the surplus + 25/turn of the excess |
| cured fish | 6 @ 26.0, stop 22 |  | uses 5.5/turn (mansion 1), makes 0.0, holds 22 = 4.0 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 24 = 4.0 turns |
| fish | 8 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 8 = 1.1 turns |
| garments |  | 55 @ min 22.0 | makes 44.3, uses 2.1, holds 221 (keeps 30): sells the surplus + 12/turn of the excess |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 103 = 4.0 turns |
| labour | 637 @ 2.2, stop - |  | uses 1056.4/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 534 = 0.9 turns |
| limestone |  | 5 @ min 23.2 |  |
| meat | 8 @ 3.02, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 8 = 1.1 turns |
| nets |  | 7 @ min 40.6 |  |
| porterage | 35 @ 0.8, stop - |  | uses 31.6/turn (observed), makes 0.0, holds 37 = 1.2 turns |
| rope |  | 4 @ min 85.0 |  |
| timber |  | 27 @ min 8.5 | makes 24.0, uses 0.0, holds 416 (keeps 350): sells the surplus + 3/turn of the excess |
| tools | 8 @ 6.2, stop 59 |  | uses 7.3/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 27.2 turns |
