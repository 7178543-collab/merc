# v2 shadow report

Turn 13309, 2026-10-15 22:51. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,231, prestige 3,109 (439 free, -0.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 395 | 0 | 4 | 0 | 0 | min_holding 60, sell 52, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 24 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 29 | 0 | 2 | 0 | 0 | min_holding 30, sell 2, sell @ 22 |
| grain | 103 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 75 | 75 | 481 | 0 | 44 | buy 75, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 52 | 0 | 0 | 0 | 0 | min_holding 15, sell 8, sell @ 39.6 |
| porterage | 26 | 26 | 15 | 0 | 11 | buy 26, buy @ 0.8 |

**1 risks, 1 waste, 4 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **tar**: ropewalk 1 ran short of tar (buy is live (no volume cap @ 9.6), but the home ask 10.90 is above it); labour need rises ~28/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 44 labour expired last turn (~71 coin): holding 75 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **candles**: home ask 87.50 is above our ceiling 70.00 and last turn bought 0 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **timber**: build materials for park 1 are in (697.0 held, 20 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 50% (EXPANSION), about 6 turns left; still to deliver: labour 130, limestone 30, timber 20; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 30 | 111.9 | 0 | off: covered |
| timber | 20 | 697.0 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 22

## Notes

- labour: projection runs 14 over real use lately; planning 554, not 568
- labour expiry guard: 44 bought labour expired last turn, buy 54 (not 104) this turn

## Prestige spending, cheapest coin per prestige first

1092 turns left: prestige gained now converts 99.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.2 | 52.7 | running |
| hold prayer 2 | chapel | 13 | 54.4 | 56.9 | needs a chapel (build cost 33,162); thin at home: furniture |
| hold banquet 1 (fish) | mansion | 4.2 | 57.5 | 57.5 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 58.0 | 58.0 | thin at home: cheese |
| hold sermon 2 | church | 24 | 55.1 | 58.1 | needs a church (build cost 70,971); thin at home: jewellery, furniture |
| hold sermon 2 (candles) | church | 31 | 55.8 | 58.1 | needs a church (build cost 70,971); thin at home: jewellery, candles, furniture |
| hold banquet 2 (pies) | mansion | 7 | 58.4 | 58.4 | thin at home: pasties, cheese, pies |
| hold banquet 4 (pies) | mansion | 18 | 58.8 | 58.8 | thin at home: pasties, hop beer |
| hold banquet 3 (pies) | mansion | 8 | 59.7 | 59.7 | thin at home: pasties, hop beer, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 60.5 | 60.5 | thin at home: hop beer, cheese |
| hold mass 2 (premium) | cathedral | 360 | 59.7 | 60.5 | needs a cathedral (build cost 284,090); thin at home: furniture, jewellery, glassware, candles, premium garments |
| jousting 3 | arena | 230 | 60.9 | 61.0 | needs a arena (build cost 26,522); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 74001604 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Brunnham: candles buy 1 @ 83.0, spinning wheels buy 1 @ 246, varnish sell 1 @ 22.0; crew 0.1; est +22 a turn
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn; best orders clear only -3 a turn after crew: ship stays at 0
- best towns now: Hofkirchen +107, Karlmoor +97, Kirchwerp +81, Fulkirch +52, Amsdermund +42
- Hofkirchen would trade: acid buy 2 @ 153, candles buy 1 @ 77.5, gears buy 1 @ 71.0, spinning wheels buy 1 @ 246, steel ingots sell 4 @ 15.7; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~102 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.32 | 0.20 (20/turn) | steel ingots 4 (14.07->16.81), salt 12 (4.22->4.99), nets 3 (39.2->40.85), flax fibres 5 (4.73->5.56) | acid 2 (157.5->180.5), spinning wheels 1 (252->277.4), candles 1 (79.8->87.5), gears 1 (72.98->74.58) | +96 |
| Karlmoor | 787 | 0.21 | 0.10 (10/turn) | tackles 1 (172.2->218.5), tallow 1 (30.45->32.68), flax fibres 4 (4.73->5.37), gears 1 (88.2->89.77) | ploughs 2 (61.95->77.9), candles 1 (81.9->87.5), wheels 2 (21.21->22.99), cloth 1 (7.93->8.45) | +84 |
| Kirchwerp | 1072 | 0.37 | 0.20 (20/turn) | steel ingots 4 (14.07->17.57), tackles 1 (172.2->180.5), flax fibres 5 (4.73->6.17), resin 2 (2.42->3.42) | spinning wheels 1 (252->277.4), acid 1 (172.2->180.5), candles 1 (82.42->87.5), gears 1 (70.88->74.58) | +69 |
| Hanstein | 380 | 0.10 | 0.30 (31/turn) | timber 13 (5.97->10.36), flax fibres 5 (4.73->5.32), yarn 4 (4.39->4.75), bricks 1 (4.6->7.12) | flax plants 59 (1.31->1.64), candles 1 (82.42->87.5), wheels 3 (22.05->22.99), seeds 4 (1.82->2.32) | +55 |
| Grandgues | 152 | 0.04 | 0.40 (41/turn) | timber 21 (5.97->7.5), beer 68 (3.28->3.59), bread 146 (2.29->2.43), firewood 1 (1.69->5.37) | wheels 4 (22.05->22.99), pies 2 (17.12->17.76), cloth 1 (8.19->8.45) | +50 |

**Best:** Hofkirchen at about +96 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 30.4, stop 1 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 3.0 turns |
| beer |  | 75 @ min 3.7 | makes 56.0, uses 4.2, holds 395 (keeps 60): sells the surplus + 24/turn of the excess |
| candles | 3 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 0 = 0.3 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 24 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 103 = 4.0 turns |
| labour | 54 @ 2.2, stop - |  | uses 553.7/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 75 = 0.7 turns |
| limestone |  | 5 @ min 17.6 |  |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 38.2 | makes 6.0, uses 0.0, holds 52 (keeps 15): sells the surplus + 3/turn of the excess |
| porterage | 20 @ 1.1, stop - |  | uses 20.0/turn (observed), makes 0.0, holds 26 = 1.3 turns |
| tar | 3 @ 11.0, stop 5 |  | uses 1.1/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| timber |  | 51 @ min 8.5 | makes 24.0, uses 0.0, holds 697 (keeps 350): sells the surplus + 27/turn of the excess |
| tools | 7 @ 6.2, stop 51 |  | uses 6.3/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 31.6 turns |

## Chain sizing

Mode FULL, garments sold 2.4/turn (+0.0 exported); plan makes 0.4 garments a turn.
Labour: own 450, everything else 468, chain may buy 350 -> chain allowance 350, chain plan 153 (-11 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 3.69 | 3.44 |
| ret | 3 | 0.66 | 0.61 |
| spin | 4 | 1.35 | 1.26 |
| weave | 3 | 0.00 | 0.00 |
| sew | 2 | 0.02 | 0.01 |

Buffers: flax fibres 63/54, thread 364/170, cloth 15/12
- thread beyond the household duty (55 a turn) is fed from weaving

## Self-diagnosis

- R1: candles slot dry: 0.5 held, 1.5 a turn (luxury slot (+3 prestige)); our buy paused by the failsafe, home ask 87.5 (held back: paused by the failsafe at level 1: un-pause only at level 0)
- R1: prestige rate -0.95 a turn vs 12-turn median +3.08; likely: dry slot: candles
- R2: logging camp w/ tool blocked by timber space: 697 held of 711 capacity, we make 24.0 a turn; no buy on it: add a sell order or more capacity for timber
- R3: weavery 1 (weavery) finished but idle 6 turns (weave cloth 2 at 0); no planned recipe for a weavery: Taylor's call
- R3: mansion 1 (mansion) finished but idle 5 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R4: ropewalk 1 projected 0 of 1 (limited by tar)
