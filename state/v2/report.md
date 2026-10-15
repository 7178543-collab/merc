# v2 shadow report

Turn 13288, 2026-10-15 01:55. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,610, prestige 3,022 (352 free, +3.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 311 | 0 | 19 | 0 | 0 | min_holding 60, sell 55, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 24 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 69 | 0 | 2 | 0 | 0 | min_holding 30, sell 6, sell @ 22 |
| grain | 103 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 131 | 131 | 553 | 0 | 28 | buy 151, buy @ 2.2 |
| meat | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 3.02 |
| nets | 58 | 0 | 0 | 0 | 0 | min_holding 15, sell 7, sell @ 42.6 |
| porterage | 24 | 24 | 24 | 0 | 0 | buy 24, buy @ 0.8 |

**0 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **labour**: 28 labour expired last turn (~44 coin): holding 131 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **candles**: home ask 79.00 is above our ceiling 70.00 and last turn bought 1 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **timber**: build materials for park 1 are in (481.6 held, 4 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 91% (EXPANSION), about 2 turns left; still to deliver: labour 24, limestone 6, timber 4; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 6 | 115.2 | 0 | off: covered |
| timber | 4 | 481.6 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 12

## Prestige spending, cheapest coin per prestige first

1113 turns left: prestige gained now converts 99.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 46.8 | 49.9 | running |
| hold banquet 2 (pies) | mansion | 7 | 55.1 | 55.1 | thin at home: pies |
| hold banquet 3 (pies) | mansion | 8 | 55.6 | 55.6 | thin at home: hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 56.0 | 56.0 | thin at home: hop beer, pies |
| jousting 1 | arena | 170 | 56.4 | 56.6 | needs a arena (build cost 24,787); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 58.2 | 58.2 |  |
| hold sermon 2 (candles) | church | 31 | 56.0 | 58.2 | needs a church (build cost 68,852); thin at home: jewellery, candles, furniture |
| hold prayer 2 | chapel | 13 | 56.1 | 58.4 | needs a chapel (build cost 31,721); thin at home: furniture |
| hold sermon 2 | church | 24 | 56.3 | 59.1 | needs a church (build cost 68,852); thin at home: jewellery, furniture |
| hold banquet 1 (meat) | mansion | 4.2 | 59.2 | 59.2 | running |
| hold feast 2 | townhouse | 2.6 | 56.8 | 59.2 | needs a townhouse (build cost 6,860) |
| jousting 3 | arena | 230 | 59.2 | 59.3 | needs a arena (build cost 24,787); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 117101560 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Darmwald: nothing pays; crew 0.0; est +0 a turn; best orders clear only -8 a turn after crew: ship stays at 0
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn; best orders clear only -6 a turn after crew: ship stays at 0
- best towns now: Brunnham +41, Clarfranche +16
- Brunnham would trade: mouldboards buy 1 @ 38.0, soap buy 1 @ 75.0, varnish sell 1 @ 20.4; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~99 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Rouhomme | 368 | 0.10 | 1.00 (99/turn) | bread 143 (2.33->3.32), timber 34 (6.2->8.6), rope 2 (78.5->85.5), flour 1 (21->31.16) | garments 2 (22.89->23.4), mouldboards 1 (43.26->43.51) | +169 |
| Kirchwerp | 1072 | 0.36 | 1.00 (99/turn) | timber 16 (6.2->14.25), flax fibres 1 (5.45->9.26), furniture 5 (13.55->15.48), nails 0 (5.35->6.13) | cheese 18 (6.09->6.7), garments 0 (21.84->23.4) | +57 |
| Bordetes | 831 | 0.23 | 0.30 (30/turn) | furniture 12 (13.55->15.77), honey 3 (10.45->12.54), candles 2 (82.95->85.5), cured meat 2 (22.2->24.89) | garments 2 (21.63->23.4), cloth 8 (8.35->8.75), dyed yarn 1 (6.3->7.79), tools 5 (4.73->5.15) | +46 |
| Nürnnieder | 520 | 0.14 | 0.10 (10/turn) | cloth 12 (8.15->11.49), tools 10 (5.1->5.32), wool 3 (8.29->8.79), flax plants 1 (1.01->1.4) | thread 34 (5.19->5.45), hop beer 2 (7.88->9.36) | +45 |
| Hofkirchen | 991 | 0.31 | 0.40 (40/turn) | furniture 12 (13.55->15.77), fleece 2 (7.88->10.07), thread 29 (4.66->5.08), nails 2 (5.35->6.65) | cloth 9 (7.77->8.75), cheese 44 (6.3->6.7), garments 2 (21.84->23.4), hop beer 2 (7.67->9.36) | +39 |

**Best:** Rouhomme at about +169 coin a turn.

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
| nets |  | 9 @ min 42.6 | makes 6.0, uses 0.0, holds 58 (keeps 15): sells the surplus + 3/turn of the excess |
| porterage | 24 @ 0.8, stop - |  | uses 24.0/turn (observed), makes 0.0, holds 24 = 1.0 turns |
| rope |  | 5 @ min 76.5 |  |
| tar | 2 @ 11.0, stop 5 |  | uses 1.0/turn (ropewalk 1), makes 0.0, holds 8 = 7.4 turns |
| timber |  | 33 @ min 8.5 | makes 24.0, uses 0.0, holds 482 (keeps 350): sells the surplus + 9/turn of the excess |
| tools | 6 @ 6.2, stop 48 |  | uses 5.9/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 33.9 turns |

## Chain sizing

Mode FULL, garments sold 22.5/turn (+0.0 exported); plan makes 4.5 garments a turn.
Labour: own 450, everything else 463, chain may buy 350 -> chain allowance 350, chain plan 127 (-22 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 2.50 | 2.02 |
| ret | 3 | 0.44 | 0.36 |
| spin | 4 | 1.21 | 1.02 |
| weave | 3 | 0.00 | 0.00 |
| sew | 2 | 0.12 | 0.11 |

Buffers: flax fibres 105/49, thread 438/253, cloth 156/95
- thread beyond the household duty (55 a turn) is fed from weaving

## Self-diagnosis

Nothing found this run.
