# v2 shadow report

Turn 13292, 2026-10-15 05:55. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,967, prestige 3,055 (385 free, +3.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 291 | 0 | 19 | 0 | 0 | min_holding 60, sell 54, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 24 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 59 | 0 | 2 | 0 | 0 | min_holding 30, sell 5, sell @ 22 |
| grain | 103 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 142 | 140 | 590 | 2 | 0 | buy 142, buy @ 2.2 |
| meat | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 3.02 |
| nets | 59 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 40.2 |
| porterage | 23 | 23 | 23 | 0 | 0 | buy 23, buy @ 0.8 |

**0 risks, 0 waste, 4 tuning** where v2 would act differently from v1.

## Tuning

- **candles**: home ask 77.00 is above our ceiling 70.00 and last turn bought 1 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **timber**: build materials for park 1 are in (537.3 held, 30 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 25% (EXPANSION), about 9 turns left; still to deliver: labour 195, limestone 45, timber 30; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 45 | 115.9 | 0 | off: covered |
| timber | 30 | 537.3 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 22

## Notes

- labour: projection runs 48 over real use lately; planning 594, not 642

## Prestige spending, cheapest coin per prestige first

1109 turns left: prestige gained now converts 99.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 46.5 | 49.6 | running |
| hold banquet 2 (pies) | mansion | 7 | 55.2 | 55.2 | thin at home: cheese, pies |
| hold banquet 2 (fish) | mansion | 6.8 | 56.9 | 56.9 | thin at home: cheese |
| hold banquet 3 (pies) | mansion | 8 | 57.4 | 57.4 | thin at home: hop beer, cheese, pies |
| hold prayer 2 | chapel | 13 | 55.2 | 57.4 | needs a chapel (build cost 30,296); thin at home: furniture |
| jousting 1 | arena | 170 | 57.4 | 57.5 | needs a arena (build cost 24,199); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 57.6 | 57.6 |  |
| hold sermon 2 (candles) | church | 31 | 55.5 | 57.6 | needs a church (build cost 67,617); thin at home: jewellery, candles, furniture |
| hold banquet 4 (pies) | mansion | 18 | 57.7 | 57.7 | thin at home: hop beer, pies |
| hold sermon 2 | church | 24 | 55.6 | 58.4 | needs a church (build cost 67,617); thin at home: jewellery, furniture |
| hold feast 2 | townhouse | 2.6 | 57.3 | 59.5 | needs a townhouse (build cost 6,304) |
| jousting 3 | arena | 230 | 59.5 | 59.6 | needs a arena (build cost 24,199); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 181601373 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Gottweiler: butter buy 1 @ 45.0, cured meat buy 6 @ 22.6, salt buy 5 @ 4.12, steel ingots sell 1 @ 13.8; crew 0.1; est +32 a turn
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn; best orders clear only -2 a turn after crew: ship stays at 0
- best towns now: Hofkirchen +61, Etallaen +47, Dedlowe +35, Birkeningen +32, Gottweiler +32
- Hofkirchen would trade: acid buy 1 @ 153, cured meat buy 6 @ 22.8, paper sell 1 @ 23.6, steel ingots sell 1 @ 12.5; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~97 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.31 | 1.00 (97/turn) | bread 72 (2.25->4.08), beer 28 (3.08->4.5), furniture 6 (13.33->17.57), thread 12 (4.66->5.32) | acid 0 (157.5->199.5), cured meat 3 (23.52->25), jewellery 0 (78.75->79.8), cloth 4 (7.77->8.1) | +134 |
| Rouhomme | 368 | 0.10 | 0.70 (68/turn) | timber 35 (6.11->9.17), beer 56 (3.08->3.65), grain 8 (2.26->3.31), nets 4 (40.8->42.56) | flax fibres 2 (5.72->6.4), jewellery 1 (78.75->79.8), mouldboards 1 (43.26->43.89), scythes 1 (28.14->28.5) | +108 |
| Birkeningen | 1006 | 0.32 | 0.40 (39/turn) | tackles 1 (166.95->243.2), candles 1 (80.85->95.95), beer 51 (3.08->3.74), wheels 1 (20.4->23.18) | cured meat 6 (23.1->25), resin 1 (1.89->2.62), salt 6 (4.58->4.94) | +103 |
| Pontmont | 341 | 0.09 | 0.50 (49/turn) | furniture 12 (13.33->18.62), cheese 19 (7.14->7.74), beer 56 (3.08->3.32), steel ingots 1 (10.82->12.63) | soap 1 (97.65->111.15), garments 2 (21.84->22) | +83 |
| Amsdermund | 1111 | 0.37 | 0.70 (68/turn) | furniture 12 (13.33->17.57), beer 56 (3.08->4.18), arms 3 (26.04->27.74), paper 1 (21.42->25.08) | cured meat 6 (22.05->25) | +72 |

**Best:** Hofkirchen at about +134 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 53 @ min 3.7 | makes 56.0, uses 19.2, holds 291 (keeps 60): sells the surplus + 16/turn of the excess |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 8 = 5.3 turns |
| cured meat | 6 @ 26.2, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 24 = 4.0 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 24 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 5 @ min 22.0 | makes 4.9, uses 2.1, holds 59 (keeps 30): sells the surplus + 2/turn of the excess |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 103 = 4.0 turns |
| labour | 144 @ 2.2, stop - |  | uses 593.5/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 142 = 1.0 turns |
| limestone |  | 5 @ min 19.2 |  |
| meat | 7 @ 3.02, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| nets |  | 9 @ min 39.6 | makes 6.0, uses 0.0, holds 59 (keeps 15): sells the surplus + 3/turn of the excess |
| porterage | 23 @ 0.8, stop - |  | uses 23.1/turn (observed), makes 0.0, holds 23 = 1.0 turns |
| rope |  | 6 @ min 77.5 | makes 4.5, uses 0.0, holds 21 (keeps 0): sells the surplus + 1/turn of the excess |
| tar | 2 @ 11.0, stop 4 |  | uses 1.0/turn (ropewalk 1), makes 0.0, holds 3 = 2.9 turns |
| timber |  | 38 @ min 8.5 | makes 24.0, uses 0.0, holds 537 (keeps 350): sells the surplus + 14/turn of the excess |
| tools | 6 @ 6.2, stop 45 |  | uses 5.6/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 35.7 turns |

## Chain sizing

Mode FULL, garments sold 14.0/turn (+0.0 exported); plan makes 3.7 garments a turn.
Labour: own 450, everything else 488, chain may buy 350 -> chain allowance 350, chain plan 100 (-12 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 1.70 | 1.55 |
| ret | 3 | 0.30 | 0.28 |
| spin | 4 | 0.89 | 0.81 |
| weave | 3 | 0.00 | 0.00 |
| sew | 2 | 0.12 | 0.09 |

Buffers: flax fibres 86/36, thread 310/216, cloth 115/58
- thread beyond the household duty (55 a turn) is fed from weaving

## Self-diagnosis

- R3: weavery 1 (weavery) finished but idle 5 turns (weave cloth 2 at 0); no planned recipe for a weavery: Taylor's call
- R5: tar buy not filling: bid 9.6 under the home ask 11.0 for 6 turns, bought 0.0 of 4, 2.9 held (2.9 turns); raise needs Taylor (ceiling 11.0)
