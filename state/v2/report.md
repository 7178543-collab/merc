# v2 shadow report

Turn 13296, 2026-10-15 09:01. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,279, prestige 3,068 (398 free, +3.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 233 | 0 | 19 | 0 | 0 | min_holding 60, sell 49, sell @ 3.94 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 24 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 52 | 0 | 2 | 0 | 0 | min_holding 30, sell 3, sell @ 22 |
| grain | 103 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 89 | 145 | 531 | 0 | 64 | buy 89, buy @ 2.2 |
| meat | 7 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 3.02 |
| nets | 49 | 0 | 0 | 0 | 0 | min_holding 15, sell 8, sell @ 42.6 |
| porterage | 23 | 23 | 23 | 0 | 0 | buy 23, buy @ 0.8 |

**0 risks, 2 waste, 3 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **Flax Wyrm**: Flax Wyrm cost 19 coin last turn (crew 0.20) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell
- **labour**: 64 labour expired last turn (~98 coin): holding 89 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **candles**: home ask 79.50 is above our ceiling 70.00 and last turn bought 1 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **timber**: build materials for park 1 are in (617.1 held, 17 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 58% (EXPANSION), about 6 turns left; still to deliver: labour 110, limestone 26, timber 17; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 26 | 116.5 | 0 | off: covered |
| timber | 17 | 617.1 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 19

## Notes

- labour: projection runs 48 over real use lately; planning 531, not 579

## Prestige spending, cheapest coin per prestige first

1105 turns left: prestige gained now converts 99.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 45.9 | 49.4 | running |
| hold banquet 2 (pies) | mansion | 7 | 57.4 | 57.4 | thin at home: wine, pies |
| hold prayer 2 | chapel | 13 | 55.1 | 57.6 | needs a chapel (build cost 32,792); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 55.6 | 57.9 | needs a church (build cost 70,920); thin at home: jewellery, candles, furniture |
| hold banquet 4 (pies) | mansion | 18 | 58.2 | 58.2 | thin at home: hop beer, wine |
| hold sermon 2 | church | 24 | 55.4 | 58.3 | needs a church (build cost 70,920); thin at home: jewellery, furniture |
| hold banquet 1 (fish) | mansion | 4.2 | 58.6 | 58.6 |  |
| hold banquet 3 (pies) | mansion | 8 | 58.6 | 58.6 | thin at home: hop beer, pies |
| hold banquet 2 (fish) | mansion | 6.8 | 59.0 | 59.0 | thin at home: wine |
| jousting 1 | arena | 170 | 59.1 | 59.2 | needs a arena (build cost 25,772); thin at home: protection, light armour, arms; needs weaponry skill |
| jousting 3 | arena | 230 | 59.9 | 60.0 | needs a arena (build cost 25,772); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold feast 2 | townhouse | 2.6 | 57.9 | 60.1 | needs a townhouse (build cost 6,251); thin at home: wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.20 | 19 | 181601373 | 0.164 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Gottweiler: cured meat buy 6 @ 21.4, salt buy 5 @ 4.12; crew 0.1; est +19 a turn
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn; best orders clear only 11 a turn after crew: ship stays at 0
- best towns now: Hofkirchen +112, Birkeningen +45, Etallaen +40, Kirchwerp +33, Amsdermund +30
- Hofkirchen would trade: acid buy 1 @ 159, axes buy 3 @ 17.4, cured meat buy 6 @ 22.8, grindstones buy 1 @ 222, lead bars sell 7 @ 12.9; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~96 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.30 | 1.00 (96/turn) | bread 75 (2.27->4.37), beer 25 (4.06->5.37), flax plants 7 (1.83->3.89), lead bars 3 (11.45->12.44) | grindstones 0 (226.8->286.9), cheese 22 (6.35->7.46), acid 0 (162.75->180.5), cured meat 3 (23.52->25.4) | +187 |
| Birkeningen | 1006 | 0.31 | 0.20 (19/turn) | tackles 1 (164.85->243.2), light armour 1 (77.7->82.17), charcoal 2 (2.18->4.94), tiles 1 (4.72->9.26) | cloth 7 (7.93->8.6), axes 1 (18.79->19.19), resin 1 (1.89->2.62) | +83 |
| Amsdermund | 1111 | 0.36 | 0.70 (67/turn) | furniture 12 (13.33->18.52), garments 3 (21.2->26.03), beer 51 (4.06->4.84), grain 8 (2.26->3.31) | cured meat 6 (23.1->25.4), acid 1 (177.45->180.5), cloth 7 (7.77->8.6), cheese 24 (7.09->7.46) | +82 |
| Magdeach | 667 | 0.17 | 0.60 (58/turn) | timber 19 (6.04->9.17), lead bars 7 (11.45->12.44), tools 13 (4.7->5.18), varnish 1 (18.17->20.52) | cheese 29 (6.51->7.46), cured meat 6 (23.73->25.4), flax fibres 3 (6.14->6.75) | +55 |
| Hanstein | 380 | 0.10 | 0.30 (29/turn) | timber 10 (6.04->9.97), tools 16 (4.7->5.08), furniture 6 (13.33->13.87), charcoal 2 (2.18->3.17) | flax fibres 14 (5.83->6.75), cloth 7 (7.98->8.6), beer 19 (3.78->4.08), scythes 1 (27.09->28.88) | +49 |

**Best:** Hofkirchen at about +187 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 48 @ min 3.96 | makes 56.0, uses 19.2, holds 233 (keeps 60): sells the surplus + 11/turn of the excess |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 8 = 5.3 turns |
| cured meat | 6 @ 26.2, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 24 = 4.0 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 24 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 3 @ min 22.0 | makes 3.7, uses 2.1, holds 52 (keeps 30): sells the surplus + 2/turn of the excess |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 103 = 4.0 turns |
| labour | 81 @ 2.2, stop - |  | uses 531.0/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 89 = 1.1 turns |
| limestone |  | 5 @ min 20.4 |  |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 7 = 1.2 turns |
| nets |  | 8 @ min 40.8 | makes 6.0, uses 0.0, holds 49 (keeps 15): sells the surplus + 2/turn of the excess |
| porterage | 23 @ 0.8, stop - |  | uses 23.1/turn (observed), makes 0.0, holds 23 = 1.0 turns |
| rope |  | 6 @ min 79.0 | makes 4.5, uses 0.0, holds 20 (keeps 0): sells the surplus + 1/turn of the excess |
| tar | 2 @ 11.0, stop 5 |  | uses 1.1/turn (ropewalk 1), makes 0.0, holds 5 = 4.1 turns |
| timber |  | 44 @ min 8.5 | makes 24.0, uses 0.0, holds 617 (keeps 350): sells the surplus + 20/turn of the excess |
| tools | 6 @ 6.2, stop 45 |  | uses 5.6/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 35.6 turns |

## Chain sizing

Mode FULL, garments sold 8.9/turn (+0.0 exported); plan makes 2.9 garments a turn.
Labour: own 450, everything else 485, chain may buy 350 -> chain allowance 350, chain plan 94 (-7 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 1.68 | 1.52 |
| ret | 3 | 0.30 | 0.27 |
| spin | 4 | 0.83 | 0.77 |
| weave | 3 | 0.00 | 0.00 |
| sew | 2 | 0.09 | 0.07 |

Buffers: flax fibres 72/29, thread 161/195, cloth 85/37
- thread beyond the household duty (55 a turn) is fed from weaving

## Self-diagnosis

- R3: weavery 1 (weavery) finished but idle 6 turns (weave cloth 2 at 0); no planned recipe for a weavery: Taylor's call
