# v2 shadow report

Turn 13288, 2026-10-15 01:05. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,470, prestige 3,022 (352 free, +3.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 311 | 0 | 19 | 0 | 0 | min_holding 60, sell 53, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 24 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 69 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 22 |
| grain | 103 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 131 | 131 | 553 | 0 | 28 | buy 131, buy @ 2.2 |
| meat | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 3.02 |
| nets | 58 | 0 | 0 | 0 | 0 | min_holding 40, sell 7, sell @ 39.2 |
| porterage | 24 | 24 | 24 | 0 | 0 | buy 24, buy @ 0.8 |

**0 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **labour**: 28 labour expired last turn (~44 coin): holding 131 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **candles**: home ask 79.00 is above our ceiling 70.00 and last turn bought 1 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **timber**: build materials for park 1 are in (501.6 held, 4 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 91% (EXPANSION), about 2 turns left; still to deliver: labour 24, limestone 6, timber 4; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 6 | 115.2 | 0 | off: covered |
| timber | 4 | 501.6 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 12

## Prestige spending, cheapest coin per prestige first

1113 turns left: prestige gained now converts 99.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 46.8 | 49.9 | running |
| hold banquet 2 (pies) | mansion | 7 | 55.6 | 55.6 | thin at home: pies |
| jousting 1 | arena | 170 | 56.7 | 56.8 | needs a arena (build cost 24,591); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 57.6 | 57.6 | thin at home: hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 57.6 | 57.6 | thin at home: hop beer, pies |
| hold banquet 2 (meat) | mansion | 6.8 | 58.8 | 58.8 |  |
| hold feast 2 | townhouse | 2.6 | 56.8 | 59.1 | needs a townhouse (build cost 6,574) |
| hold sermon 2 (candles) | church | 31 | 57.1 | 59.3 | needs a church (build cost 68,444); thin at home: jewellery, candles, furniture |
| jousting 3 | arena | 230 | 59.2 | 59.3 | needs a arena (build cost 24,591); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (meat) | mansion | 4.2 | 59.6 | 59.6 | running |
| hold mass 2 (premium) | cathedral | 360 | 59.5 | 60.3 | needs a cathedral (build cost 276,400); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold prayer 2 | chapel | 13 | 58.1 | 60.3 | needs a chapel (build cost 31,145); thin at home: furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 117101560 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Darmwald: nothing pays; crew 0.0; est +0 a turn; best orders clear only 11 a turn after crew: ship stays at 0
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn; best orders clear only -6 a turn after crew: ship stays at 0
- best towns now: Kirchwerp +124, Corstoft +41, Arnsreuth +40, Hofkirchen +34, Fulkirch +33
- Kirchwerp would trade: acid buy 2 @ 146, medicine buy 1 @ 170; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~99 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Rouhomme | 368 | 0.10 | 1.00 (99/turn) | bread 118 (2.35->3.53), timber 30 (6.2->8.55), beer 47 (3.1->3.65), flour 1 (23.52->31.73) | garments 1 (22.68->24.2) | +187 |
| Hofkirchen | 991 | 0.31 | 0.30 (30/turn) | flax fibres 8 (5.75->10.16), furniture 12 (13.23->14.82), paper 2 (21.42->22.8), wheels 1 (21.4->22.99) | medicine 1 (157.5->181.45), cheese 38 (6.09->6.79), cloth 9 (7.77->8.5), garments 2 (21.84->24.2) | +87 |
| Kirchwerp | 1072 | 0.35 | 1.00 (99/turn) | timber 12 (6.2->12.44), beer 20 (3.1->4.12), furniture 4 (13.23->15.11), grain 2 (2.64->3.69) | acid 0 (150.15->197.6), cheese 13 (6.2->6.79), medicine 0 (174.3->181.45), garments 0 (21.84->24.2) | +64 |
| Fontaux | 411 | 0.11 | 0.30 (30/turn) | salt 15 (5.67->7.79), timber 10 (6.2->8.98), furniture 10 (13.23->14.06), charcoal 2 (2.06->3.82) | cheese 30 (6.56->6.79), cloth 9 (7.98->8.5), garments 2 (23.31->24.2), pies 1 (15.65->16.53) | +58 |
| Pontmont | 341 | 0.09 | 0.20 (20/turn) | furniture 12 (13.23->16.15), flour 2 (23.52->29.64), cured meat 2 (22.2->25.27), beer 57 (3.1->3.32) | garments 2 (21.84->24.2), tar 1 (9.87->10.6) | +57 |

**Best:** Rouhomme at about +187 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 55 @ min 3.7 | makes 56.0, uses 19.2, holds 311 (keeps 60): sells the surplus + 18/turn of the excess |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 8 = 5.3 turns |
| cured meat | 6 @ 24.6, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 24 = 4.0 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 24 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 6 @ min 22.0 | makes 4.9, uses 2.1, holds 69 (keeps 30): sells the surplus + 3/turn of the excess |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 103 = 4.0 turns |
| labour | 151 @ 2.2, stop - |  | uses 601.4/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 131 = 0.9 turns |
| limestone |  | 5 @ min 19.9 |  |
| meat | 7 @ 3.02, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| nets |  | 7 @ min 42.6 |  |
| porterage | 24 @ 0.8, stop - |  | uses 24.0/turn (observed), makes 0.0, holds 24 = 1.0 turns |
| rope |  | 5 @ min 76.5 |  |
| tar | 2 @ 11.0, stop 5 |  | uses 1.0/turn (ropewalk 1), makes 0.0, holds 8 = 7.4 turns |
| timber |  | 35 @ min 8.5 | makes 24.0, uses 0.0, holds 502 (keeps 350): sells the surplus + 11/turn of the excess |
| tools | 6 @ 6.2, stop 48 |  | uses 5.9/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 33.9 turns |

## Chain sizing

Mode FULL, garments sold 24.7/turn (+0.0 exported); plan makes 4.5 garments a turn.
Labour: own 450, everything else 463, chain may buy 350 -> chain allowance 350, chain plan 143 (-5 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 2.50 | 2.42 |
| ret | 3 | 0.44 | 0.43 |
| spin | 4 | 1.21 | 1.15 |
| weave | 3 | 0.00 | 0.00 |
| sew | 2 | 0.12 | 0.11 |

Buffers: flax fibres 105/52, thread 438/262, cloth 156/104
- thread beyond the household duty (55 a turn) is fed from weaving

## Self-diagnosis

Nothing found this run.
