# v2 shadow report

Turn 13306, 2026-10-15 19:06. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,757, prestige 3,111 (441 free, -1.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 323 | 0 | 4 | 0 | 0 | min_holding 60, sell 52, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 24 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 35 | 0 | 2 | 0 | 0 | min_holding 30, sell 2, sell @ 22 |
| grain | 103 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 210 | 210 | 612 | 0 | 48 | buy 210, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 46 | 0 | 0 | 0 | 0 | min_holding 15, sell 8, sell @ 39.6 |
| porterage | 26 | 26 | 15 | 0 | 11 | buy 26, buy @ 0.8 |

**0 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **labour**: 48 labour expired last turn (~78 coin): holding 210 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **candles**: home ask 78.50 is above our ceiling 70.00 and last turn bought 0 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **timber**: build materials for park 1 are in (707.0 held, 30 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 25% (EXPANSION), about 9 turns left; still to deliver: labour 195, limestone 45, timber 30; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 45 | 111.3 | 0 | off: covered |
| timber | 30 | 707.0 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 22

## Notes

- labour: projection runs 40 over real use lately; planning 612, not 564

## Prestige spending, cheapest coin per prestige first

1095 turns left: prestige gained now converts 99.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.2 | 52.1 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 57.0 | 57.0 | thin at home: cured fish |
| hold banquet 2 (pies) | mansion | 7 | 57.3 | 57.3 | thin at home: pies |
| hold banquet 4 (pies) | mansion | 18 | 58.0 | 58.0 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 58.3 | 58.3 | thin at home: cured fish |
| hold banquet 3 (pies) | mansion | 8 | 58.7 | 58.7 | thin at home: pies |
| hold sermon 2 (candles) | church | 31 | 57.4 | 59.6 | needs a church (build cost 67,749); thin at home: jewellery, candles, furniture |
| jousting 1 | arena | 170 | 59.6 | 59.8 | needs a arena (build cost 24,505); thin at home: protection, light armour, arms; needs weaponry skill |
| hold prayer 2 | chapel | 13 | 57.6 | 59.9 | needs a chapel (build cost 30,933); thin at home: furniture |
| jousting 3 | arena | 230 | 60.1 | 60.2 | needs a arena (build cost 24,505); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold mass 2 (premium) | cathedral | 360 | 59.9 | 60.6 | needs a cathedral (build cost 275,320); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold feast 2 | townhouse | 2.6 | 58.4 | 60.7 | needs a townhouse (build cost 6,479) |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 10 | 74001604 | 0.04 | - | hop beer 2, spinning wheels 1 | -255 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Heilegg: cheese buy 30 @ 6.35; crew 0.1; est +18 a turn
- **Flax Wyrm** on Brunnham: nothing pays; crew 0.0; est +0 a turn; best orders clear only -8 a turn after crew: ship stays at 0
- best towns now: Hanstein +65, Kirchwerp +53, Fulkirch +52, Hofkirchen +38, Magdeach +29
- Hanstein would trade: cheese buy 46 @ 6.1, steel ingots sell 1 @ 14.9, timber sell 19 @ 10.3; crew 0.3

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~102 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Rouhomme | 368 | 0.10 | 0.70 (71/turn) | bread 149 (2.27->3.21), lead ore 9 (7.56->11.88), beer 73 (3.32->3.8), charcoal 2 (2.18->4.75) | scythes 1 (28.14->30.02), wool 1 (5.46->7.27), dyed yarn 1 (6.46->7.98), flax plants 1 (1.39->1.72) | +160 |
| Hanstein | 380 | 0.10 | 0.40 (41/turn) | timber 19 (5.97->9.97), rope 1 (63.8->67.92), wine 14 (6.25->6.46), bricks 1 (4.34->6.98) | cheese 46 (6.25->7.31), thread 77 (5->5.5), flax plants 59 (1.34->1.72), flour 1 (21.21->25.46) | +145 |
| Heilegg | 826 | 0.23 | 0.10 (10/turn) | rope 5 (63.8->77.42) | cheese 30 (6.51->7.31), flour 1 (23.52->25.46) | +83 |
| Kirchwerp | 1072 | 0.37 | 0.20 (20/turn) | rope 2 (63.8->70.77), steel ingots 5 (14.18->15.86), butter 1 (70.35->76), grain 8 (2.52->3.44) | cheese 37 (6.2->7.31), gears 1 (70.35->75.05) | +57 |
| Clairas | 374 | 0.10 | 0.10 (10/turn) | rope 3 (63.8->76), blades 1 (16.38->17.48), firewood 1 (1.72->5.37), steel ingots 1 (14.18->15.11) | cheese 16 (6.83->7.31), flour 1 (21.63->25.46), yarn 6 (4.68->5.03), flax plants 1 (1.48->1.72) | +51 |

**Best:** Rouhomme at about +160 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 28.8, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 3 = 6.0 turns |
| beer |  | 69 @ min 3.7 | makes 56.0, uses 4.2, holds 323 (keeps 60): sells the surplus + 18/turn of the excess |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 5 = 3.3 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 24 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 103 = 4.0 turns |
| labour | 162 @ 2.2, stop - |  | uses 612.4/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 210 = 1.3 turns |
| limestone |  | 5 @ min 17.8 |  |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 8 @ min 38.4 | makes 6.0, uses 0.0, holds 46 (keeps 15): sells the surplus + 2/turn of the excess |
| porterage | 15 @ 1.1, stop - |  | uses 14.8/turn (observed), makes 0.0, holds 26 = 1.8 turns |
| rope |  | 5 @ min 79.0 |  |
| tar | 3 @ 11.0, stop 5 |  | uses 1.1/turn (ropewalk 1), makes 0.0, holds 1 = 1.0 turns |
| timber |  | 52 @ min 8.5 | makes 24.0, uses 0.0, holds 707 (keeps 350): sells the surplus + 28/turn of the excess |
| tools | 7 @ 6.2, stop 51 |  | uses 6.3/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 31.5 turns |

## Chain sizing

Mode FULL, garments sold 3.1/turn (+0.0 exported); plan makes 0.4 garments a turn.
Labour: own 450, everything else 468, chain may buy 350 -> chain allowance 350, chain plan 168 (+4 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 3.69 | 3.79 |
| ret | 3 | 0.66 | 0.67 |
| spin | 4 | 1.35 | 1.39 |
| weave | 3 | 0.00 | 0.00 |
| sew | 2 | 0.02 | 0.01 |

Buffers: flax fibres 63/54, thread 287/172, cloth 20/14
- thread beyond the household duty (55 a turn) is fed from weaving

## Self-diagnosis

- R1: prestige rate -0.96 a turn vs 12-turn median +3.25; likely: no slot, building or contract cause found: check the impacts
- R2: logging camp w/ tool blocked by timber space: 707 held of 711 capacity, we make 24.0 a turn; no buy on it: add a sell order or more capacity for timber
- R3: weavery 1 (weavery) finished but idle 6 turns (weave cloth 2 at 0); no planned recipe for a weavery: Taylor's call
- R3: mansion 1 (mansion) finished but idle 2 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
