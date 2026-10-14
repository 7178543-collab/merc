# v2 shadow report

Turn 13285, 2026-10-14 22:52. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,238, prestige 3,013 (343 free, +3.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 290 | 0 | 19 | 0 | 0 | min_holding 60, sell 53, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 24 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 8 | 8 | 7 | 0 | 1 | stop 24, buy 8, buy @ 2.5 |
| garments | 90 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 22 |
| grain | 103 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 224 | 237 | 627 | 0 | 60 | buy 224, buy @ 2.2 |
| meat | 8 | 8 | 7 | 0 | 1 | stop 24, buy 8, buy @ 3.02 |
| nets | 55 | 0 | 0 | 0 | 0 | min_holding 40, sell 6, sell @ 43.4 |
| porterage | 37 | 37 | 24 | 0 | 13 | buy 37, buy @ 0.8 |

**0 risks, 2 waste, 4 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **Flax Wyrm**: Flax Wyrm cost 73 coin last turn (crew 0.74) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell
- **labour**: 60 labour expired last turn (~96 coin): holding 224 against a ~35 buffer target -> v2: trim the buy until the stock is near 35

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **tar**: home ask 11.60 is above our ceiling 11.00 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **timber**: build materials for park 1 are in (462.6 held, 14 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 66% (EXPANSION), about 5 turns left; still to deliver: labour 89, limestone 21, timber 14; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 21 | 114.6 | 0 | off: covered |
| timber | 14 | 462.6 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 18

## Prestige spending, cheapest coin per prestige first

1116 turns left: prestige gained now converts 99.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.7 | 51.3 | running |
| hold banquet 2 (pies) | mansion | 7 | 55.9 | 55.9 | thin at home: cheese, pies |
| hold banquet 3 (pies) | mansion | 8 | 56.0 | 56.0 | thin at home: cheese, pies |
| jousting 1 | arena | 170 | 57.9 | 58.0 | needs a arena (build cost 26,709); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 58.2 | 58.2 | thin at home: pies |
| hold sermon 2 (candles) | church | 31 | 57.5 | 59.8 | needs a church (build cost 73,483); thin at home: jewellery, furniture |
| jousting 3 | arena | 230 | 59.7 | 59.8 | needs a arena (build cost 26,709); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 59.9 | 59.9 | thin at home: cheese |
| hold prayer 2 | chapel | 13 | 57.5 | 60.0 | needs a chapel (build cost 33,626); thin at home: furniture |
| hold banquet 1 (meat) | mansion | 4.2 | 60.3 | 60.3 | running |
| hold banquet 3 (meat) | mansion | 7.6 | 60.8 | 60.8 | thin at home: cheese |
| hold banquet 2 (fish) | mansion | 6.8 | 61.5 | 61.5 | thin at home: cured fish, cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.74 / 0.74 | 73 | 117101560 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | nets 1 | - | 23 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Darmwald: medicine buy 2 @ 140, tackles sell 1 @ 193, tar buy 1 @ 9.2; crew 0.1; est +110 a turn
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn; best orders clear only 7 a turn after crew: ship stays at 0
- best towns now: Kirchwerp +146, Großmühle +115, Darmwald +110, Brunnham +64, Dortdorf +48
- Kirchwerp would trade: acid buy 2 @ 147, canvas buy 1 @ 24.2, soap buy 1 @ 109; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~100 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Rouhomme | 368 | 0.10 | 1.00 (100/turn) | bread 138 (2.37->3.46), lead ore 1 (5.99->17.48), beer 55 (3.28->3.65), flour 2 (23.94->28.5) | garments 20 (21->24.32), tar 1 (11.23->11.6) | +209 |
| Hofkirchen | 991 | 0.32 | 0.30 (30/turn) | flax plants 14 (1.3->3.89), rope 3 (68.66->77.9), thread 38 (4.66->5.13), tackles 1 (174.3->180.5) | garments 20 (21.84->24.32), medicine 1 (157.5->181.45), stockfish 1 (106.05->107.35), beer 19 (3.07->3.7) | +134 |
| Darmwald | 1022 | 0.33 | 0.20 (20/turn) | flax plants 14 (1.3->3.1), rope 2 (68.66->76), tackles 1 (174.3->186.2) | medicine 2 (143.85->181.45), garments 20 (23.1->24.32), tar 1 (9.5->11.6) | +134 |
| Kirchwerp | 1072 | 0.36 | 1.00 (100/turn) | timber 13 (6.27->14.25), beer 26 (3.28->4.07), wine 7 (6.77->7.36), grain 3 (2.68->3.7) | acid 0 (151.2->209), garments 9 (22.47->24.32), canvas 0 (24.78->32.87), soap 0 (111.3->114) | +114 |
| Bordetes | 831 | 0.23 | 0.50 (50/turn) | cloth 9 (8->12.06), beer 55 (3.28->3.93), furniture 12 (13.65->14.82), pasties 5 (14.18->15.39) | garments 20 (21.63->24.32) | +103 |

**Best:** Rouhomme at about +209 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 28.6, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 53 @ min 3.7 | makes 56.0, uses 19.2, holds 290 (keeps 60): sells the surplus + 16/turn of the excess |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 8 = 5.0 turns |
| cured meat | 6 @ 25.2, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 24 = 4.0 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 24 = 3.9 turns |
| fish | 8 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 8 = 1.1 turns |
| garments |  | 11 @ min 22.4 | makes 8.6, uses 2.1, holds 90 (keeps 30): sells the surplus + 4/turn of the excess |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 103 = 4.0 turns |
| labour | 249 @ 2.2, stop - |  | uses 686.8/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 224 = 0.9 turns |
| limestone |  | 5 @ min 20.6 |  |
| meat | 8 @ 3.02, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 8 = 1.1 turns |
| nets |  | 7 @ min 40.8 |  |
| porterage | 33 @ 0.8, stop - |  | uses 29.6/turn (observed), makes 0.0, holds 37 = 1.3 turns |
| rope |  | 5 @ min 80.5 |  |
| tar | 2 @ 11.0, stop 6 |  | uses 1.4/turn (ropewalk 1), makes 0.0, holds 11 = 7.7 turns |
| timber |  | 31 @ min 8.5 | makes 24.0, uses 0.0, holds 463 (keeps 350): sells the surplus + 7/turn of the excess |
| tools | 7 @ 6.2, stop 49 |  | uses 6.1/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 32.8 turns |

## Chain sizing

Mode FULL, garments sold 31.8/turn (+0.0 exported); plan makes 8.6 garments a turn.
Labour: own 450, everything else 469, chain may buy 350 -> chain allowance 350, chain plan 195 (-2 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 3.04 | 2.97 |
| ret | 3 | 0.54 | 0.53 |
| spin | 4 | 1.40 | 1.38 |
| weave | 3 | 0.15 | 0.13 |
| sew | 2 | 0.21 | 0.21 |

Buffers: flax fibres 120/61, thread 492/290, cloth 184/132
- thread beyond the household duty (55 a turn) is fed from weaving

## Self-diagnosis

Nothing found this run.
