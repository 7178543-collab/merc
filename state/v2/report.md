# v2 shadow report

Turn 13300, 2026-10-15 13:12. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,758, prestige 3,081 (411 free, +2.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 236 | 0 | 19 | 0 | 0 | min_holding 60, sell 48, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 24 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 47 | 0 | 2 | 0 | 0 | min_holding 30, sell 3, sell @ 22 |
| grain | 103 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 175 | 175 | 625 | 0 | 0 | buy 175, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 58 | 0 | 0 | 0 | 0 | min_holding 15, sell 8, sell @ 42.6 |
| porterage | 26 | 26 | 26 | 0 | 0 | buy 26, buy @ 0.8 |

**0 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Tuning

- **candles**: home ask 77.50 is above our ceiling 70.00 and last turn bought 1 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **timber**: build materials for park 1 are in (675.3 held, 4 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 91% (EXPANSION), about 2 turns left; still to deliver: labour 24, limestone 6, timber 4; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 6 | 110.5 | 0 | off: covered |
| timber | 4 | 675.3 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 12

## Notes

- labour: projection runs 40 over real use lately; planning 625, not 665

## Prestige spending, cheapest coin per prestige first

1101 turns left: prestige gained now converts 99.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.7 | 50.7 | running |
| hold banquet 2 (pies) | mansion | 7 | 57.0 | 57.0 | thin at home: wine, pies |
| hold banquet 3 (pies) | mansion | 8 | 58.0 | 58.0 | thin at home: hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 58.0 | 58.0 | thin at home: hop beer, wine |
| hold banquet 1 (fish) | mansion | 4.2 | 58.2 | 58.2 |  |
| jousting 1 | arena | 170 | 58.1 | 58.2 | needs a arena (build cost 24,368); thin at home: protection, light armour, arms; needs weaponry skill |
| hold prayer 2 | chapel | 13 | 56.4 | 58.7 | needs a chapel (build cost 30,954); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 56.6 | 58.8 | needs a church (build cost 68,482); thin at home: jewellery, candles, furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 59.2 | 59.2 | thin at home: wine |
| jousting 3 | arena | 230 | 59.7 | 59.8 | needs a arena (build cost 24,368); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold sermon 2 | church | 24 | 57.3 | 60.1 | needs a church (build cost 68,482); thin at home: jewellery, furniture |
| hold banquet 1 (meat) | mansion | 4.2 | 61.0 | 61.0 | running |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.16 | 16 | 181601373 | 0 | - | cheese 16 | -95 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Gottweiler: nothing pays; crew 0.0; est +0 a turn; best orders clear only 5 a turn after crew: ship stays at 0
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn; best orders clear only -2 a turn after crew: ship stays at 0
- best towns now: Toqueque +62, Bremcop +33, Brunnham +28, Donaunieder +23, Bordetes +23
- Toqueque would trade: cheese sell 6 @ 8.95, salt sell 5 @ 5.5, tackles sell 1 @ 218; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~100 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Rouhomme | 368 | 0.10 | 0.70 (70/turn) | bread 156 (2.27->2.96), beer 51 (3.28->3.65), rope 1 (80->85.5), charcoal 2 (1.84->3.86) | jewellery 2 (78.75->87.4), spinning wheels 1 (260.4->277.4), cloth 7 (7.88->8.85), garments 2 (22.68->24.2) | +127 |
| Fontaux | 411 | 0.11 | 0.10 (10/turn) | salt 18 (4.05->7.79), charcoal 2 (1.84->3.65), flax fibres 5 (5.5->5.89), grain 8 (2.26->2.6) | spinning wheels 1 (258.3->277.4), flax plants 31 (1.44->1.75), cloth 7 (8.45->8.85), yarn 5 (4.54->4.84) | +96 |
| Grandgues | 152 | 0.04 | 0.40 (40/turn) | timber 21 (5.99->7.5), beer 51 (3.28->3.59), wheels 1 (20.2->28.5), bread 156 (2.27->2.43) | cheese 13 (6.3->6.84), hop beer 2 (7.93->9.59), cured meat 6 (23.94->24.2), yarn 5 (4.7->4.84) | +71 |
| Toqueque | 642 | 0.17 | 0.10 (10/turn) | tackles 1 (164.85->222.3), salt 5 (4.05->5.32), wheels 1 (20.2->22.8), cheese 1 (7.2->8.64) | garments 2 (21.84->24.2), flax fibres 12 (6.09->6.5) | +68 |
| Boistot | 1230 | 0.45 | 0.10 (10/turn) | slaked lime 1 (8.87->12.54), wool 2 (6.88->7.65), yarn 1 (5.46->6.41) | jewellery 3 (78.75->87.4), spinning wheels 1 (260.4->277.4), garments 2 (21.84->24.2), hop beer 1 (8.03->9.59) | +47 |

**Best:** Rouhomme at about +127 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 48 @ min 3.7 | makes 56.0, uses 19.2, holds 236 (keeps 60): sells the surplus + 12/turn of the excess |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 8 = 5.3 turns |
| cured meat | 6 @ 25.4, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 24 = 4.0 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 24 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 3 @ min 22.0 | makes 3.7, uses 2.1, holds 47 (keeps 30): sells the surplus + 1/turn of the excess |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 103 = 4.0 turns |
| labour | 175 @ 2.2, stop - |  | uses 625.3/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 175 = 1.0 turns |
| limestone |  | 5 @ min 18.3 |  |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 39.4 | makes 6.0, uses 0.0, holds 58 (keeps 15): sells the surplus + 3/turn of the excess |
| porterage | 26 @ 1.1, stop - |  | uses 25.6/turn (observed), makes 0.0, holds 26 = 1.0 turns |
| rope |  | 6 @ min 78.0 | makes 4.5, uses 0.0, holds 23 (keeps 0): sells the surplus + 2/turn of the excess |
| tar | 2 @ 11.0, stop 5 |  | uses 1.1/turn (ropewalk 1), makes 0.0, holds 4 = 3.9 turns |
| timber |  | 49 @ min 8.5 | makes 24.0, uses 0.0, holds 675 (keeps 350): sells the surplus + 25/turn of the excess |
| tools | 7 @ 6.2, stop 52 |  | uses 6.4/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 30.9 turns |

## Chain sizing

Mode FULL, garments sold 5.2/turn (+0.0 exported); plan makes 2.1 garments a turn.
Labour: own 450, everything else 478, chain may buy 350 -> chain allowance 350, chain plan 187 (-12 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.07 | 3.99 |
| ret | 3 | 0.72 | 0.71 |
| spin | 4 | 1.58 | 1.52 |
| weave | 3 | 0.00 | 0.00 |
| sew | 2 | 0.09 | 0.05 |

Buffers: flax fibres 66/54, thread 216/179, cloth 56/21
- thread beyond the household duty (55 a turn) is fed from weaving

## Self-diagnosis

- R3: weavery 1 (weavery) finished but idle 6 turns (weave cloth 2 at 0); no planned recipe for a weavery: Taylor's call
