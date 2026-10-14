# v2 shadow report

Turn 13286, 2026-10-14 23:48. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,942, prestige 3,016 (346 free, +3.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 296 | 0 | 19 | 0 | 0 | min_holding 60, sell 53, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 24 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 8 | 8 | 7 | 0 | 1 | stop 24, buy 8, buy @ 2.5 |
| garments | 85 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 22.4 |
| grain | 103 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 247 | 224 | 604 | 0 | 70 | buy 247, buy @ 2.2 |
| meat | 8 | 8 | 7 | 0 | 1 | stop 24, buy 8, buy @ 3.02 |
| nets | 60 | 0 | 0 | 0 | 0 | min_holding 40, sell 7, sell @ 40.8 |
| porterage | 37 | 37 | 24 | 0 | 13 | buy 37, buy @ 0.8 |

**0 risks, 2 waste, 4 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **Flax Wyrm**: Flax Wyrm cost 10 coin last turn (crew 0.10) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell
- **labour**: 70 labour expired last turn (~111 coin): holding 247 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **candles**: home ask 78.00 is above our ceiling 70.00 and last turn bought 1 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **timber**: build materials for park 1 are in (462.6 held, 10 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 75% (EXPANSION), about 3 turns left; still to deliver: labour 65, limestone 15, timber 10; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 15 | 114.8 | 0 | off: covered |
| timber | 10 | 462.6 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 22

## Notes

- labour expiry guard: 70 bought labour expired last turn, buy 177 (not 202) this turn

## Prestige spending, cheapest coin per prestige first

1115 turns left: prestige gained now converts 99.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.7 | 50.9 | running |
| hold banquet 2 (pies) | mansion | 7 | 54.9 | 54.9 | thin at home: cheese, pies |
| hold banquet 3 (pies) | mansion | 8 | 56.4 | 56.4 | thin at home: cheese, pies |
| hold prayer 2 | chapel | 13 | 54.3 | 56.7 | needs a chapel (build cost 31,940); thin at home: furniture |
| hold banquet 2 (meat) | mansion | 6.8 | 57.4 | 57.4 | thin at home: cheese |
| hold sermon 2 (candles) | church | 31 | 55.6 | 57.8 | needs a church (build cost 69,764); thin at home: jewellery, candles, furniture |
| hold banquet 4 (pies) | mansion | 18 | 58.0 | 58.0 | thin at home: pies |
| hold sermon 2 | church | 24 | 55.8 | 58.6 | needs a church (build cost 69,764); thin at home: jewellery, furniture |
| hold banquet 1 (meat) | mansion | 4.2 | 59.3 | 59.3 | running |
| jousting 1 | arena | 170 | 59.3 | 59.4 | needs a arena (build cost 25,641); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 3 (meat) | mansion | 7.6 | 59.6 | 59.6 | thin at home: cheese |
| jousting 3 | arena | 230 | 59.6 | 59.7 | needs a arena (build cost 25,641); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 10 | 117101560 | 0.016 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Darmwald: nothing pays; crew 0.0; est +0 a turn; best orders clear only 9 a turn after crew: ship stays at 0
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn; best orders clear only -6 a turn after crew: ship stays at 0
- best towns now: Hofkirchen +73, Kirchwerp +68, Großmühle +50, Disscester +36, Corstoft +29
- Hofkirchen would trade: medicine buy 1 @ 133, paper sell 1 @ 23.6, soap buy 1 @ 108, tackles sell 1 @ 185; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~99 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Rouhomme | 368 | 0.10 | 1.00 (99/turn) | bread 140 (2.35->3.53), timber 29 (6.25->8.55), nets 3 (40.4->42.56), flour 1 (24.99->29.64) | garments 2 (22.47->25), arms 3 (26.25->26.98) | +161 |
| Hofkirchen | 991 | 0.31 | 0.20 (20/turn) | flax fibres 9 (5.65->10.16), tackles 1 (173.25->180.5), thread 31 (4.66->5.13), paper 1 (21.42->22.8) | medicine 1 (136.5->181.45), garments 2 (21.84->25), arms 6 (25.83->26.98), soap 1 (110.25->114) | +106 |
| Bordees | 1112 | 0.38 | 0.20 (20/turn) | thread 14 (4.66->8.74), candles 1 (81.9->95.95), cheese 13 (6.62->7.27), cured meat 2 (22.2->24.7) | garments 2 (22.26->25) | +72 |
| Hanstein | 380 | 0.10 | 0.20 (20/turn) | timber 9 (6.25->9.03), tools 10 (4.76->5.18), charcoal 2 (1.96->3.23), grain 8 (2.62->2.96) | grindstones 1 (260.4->292.6), thread 73 (5.17->5.5), garments 2 (23.73->25), seeds 6 (1.84->2.32) | +66 |
| Kirchwerp | 1072 | 0.36 | 0.20 (20/turn) | grain 8 (2.62->3.69) | acid 1 (151.2->195.7), garments 2 (21.84->25), arms 6 (25.83->26.98), medicine 1 (178.5->181.45) | +60 |

**Best:** Rouhomme at about +161 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 53 @ min 3.7 | makes 56.0, uses 19.2, holds 296 (keeps 60): sells the surplus + 17/turn of the excess |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 8 = 5.3 turns |
| cured meat | 6 @ 24.2, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 24 = 4.0 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 24 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 8 = 1.1 turns |
| garments |  | 11 @ min 22.0 | makes 8.6, uses 2.1, holds 85 (keeps 30): sells the surplus + 4/turn of the excess |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 103 = 4.0 turns |
| labour | 177 @ 2.2, stop - |  | uses 652.4/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 247 = 1.2 turns |
| limestone |  | 5 @ min 20.4 |  |
| meat | 7 @ 3.02, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 8 = 1.1 turns |
| nets |  | 7 @ min 39.2 | makes 6.0, uses 0.0, holds 60 (keeps 40): sells the surplus + 1/turn of the excess |
| porterage | 24 @ 0.8, stop - |  | uses 24.5/turn (observed), makes 0.0, holds 37 = 1.5 turns |
| rope |  | 5 @ min 83.0 |  |
| tar | 2 @ 11.0, stop 5 |  | uses 1.1/turn (ropewalk 1), makes 0.0, holds 10 = 9.0 turns |
| timber |  | 31 @ min 8.5 | makes 24.0, uses 0.0, holds 463 (keeps 350): sells the surplus + 7/turn of the excess |
| tools | 7 @ 6.2, stop 49 |  | uses 6.1/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 32.8 turns |

## Chain sizing

Mode FULL, garments sold 28.0/turn (+0.0 exported); plan makes 4.9 garments a turn.
Labour: own 450, everything else 473, chain may buy 350 -> chain allowance 350, chain plan 150 (-46 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 2.97 | 2.50 |
| ret | 3 | 0.54 | 0.44 |
| spin | 4 | 1.38 | 1.21 |
| weave | 3 | 0.15 | 0.00 |
| sew | 2 | 0.21 | 0.12 |

Buffers: flax fibres 115/56, thread 475/274, cloth 175/116
- thread beyond the household duty (55 a turn) is fed from weaving

## Self-diagnosis

Nothing found this run.
