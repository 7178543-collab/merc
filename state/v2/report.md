# v2 shadow report

Turn 13308, 2026-10-15 21:55. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,953, prestige 3,110 (440 free, -1.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 373 | 0 | 4 | 0 | 0 | min_holding 60, sell 52, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 24 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 2, sell @ 22 |
| grain | 103 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 75 | 173 | 518 | 0 | 105 | buy 75, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 50 | 0 | 0 | 0 | 0 | min_holding 15, sell 8, sell @ 39.6 |
| porterage | 26 | 26 | 22 | 0 | 4 | buy 26, buy @ 0.8 |

**1 risks, 1 waste, 4 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **tar**: ropewalk 1 ran short of tar (buy is live (no volume cap @ 9.6), but the home ask 11.30 is above it); labour need rises ~28/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 105 labour expired last turn (~173 coin): holding 75 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **candles**: home ask 87.50 is above our ceiling 70.00 and last turn bought 0 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **tar**: home ask 11.30 is above our ceiling 11.00 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **timber**: build materials for park 1 are in (707.0 held, 24 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 41% (EXPANSION), about 8 turns left; still to deliver: labour 154, limestone 36, timber 24; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 36 | 111.7 | 0 | off: covered |
| timber | 24 | 707.0 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 20

## Notes

- labour: projection runs 9 over real use lately; planning 523, not 531

## Prestige spending, cheapest coin per prestige first

1093 turns left: prestige gained now converts 99.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.2 | 52.6 | running |
| hold banquet 2 (pies) | mansion | 7 | 56.5 | 56.5 | thin at home: pies |
| hold banquet 3 (pies) | mansion | 8 | 56.6 | 56.6 | thin at home: hop beer, pies |
| hold banquet 2 (fish) | mansion | 6.8 | 57.0 | 57.0 |  |
| hold banquet 4 (pies) | mansion | 18 | 57.3 | 57.3 | thin at home: hop beer |
| hold banquet 1 (fish) | mansion | 4.2 | 57.5 | 57.5 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 58.1 | 58.1 | thin at home: hop beer |
| hold prayer 2 | chapel | 13 | 56.6 | 59.1 | needs a chapel (build cost 32,908); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 56.9 | 59.2 | needs a church (build cost 70,629); thin at home: jewellery, candles, furniture |
| hold feast 2 | townhouse | 2.6 | 57.2 | 59.6 | needs a townhouse (build cost 6,634); thin at home: wine |
| hold sermon 2 | church | 24 | 56.8 | 59.8 | needs a church (build cost 70,629); thin at home: jewellery, furniture |
| jousting 1 | arena | 170 | 60.3 | 60.4 | needs a arena (build cost 26,146); thin at home: protection, light armour, arms; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 74001604 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Brunnham: nothing pays; crew 0.0; est +0 a turn; best orders clear only 15 a turn after crew: ship stays at 0
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn; best orders clear only 4 a turn after crew: ship stays at 0
- best towns now: Fulkirch +55, Karlmoor +46, Chribruck +40, Bedenis +37, Großaue +36
- Fulkirch would trade: acid buy 2 @ 161, bronze ingots buy 1 @ 21.0, candles buy 1 @ 80.5, lead bars sell 2 @ 13.4; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~102 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Rouhomme | 368 | 0.10 | 0.70 (72/turn) | bread 147 (2.29->3.5), beer 77 (3.28->3.7), lead ore 2 (6.98->14.63), grain 8 (2.54->3.46) | candles 1 (80.85->87.5), dyed yarn 1 (5.83->8.03), scythes 1 (28.14->30.21), wheels 3 (21.42->22.23) | +179 |
| Vauxvais | 204 | 0.06 | 0.30 (31/turn) | bread 144 (2.29->2.64), thread 10 (4.66->4.84), nails 2 (5.4->5.7), resin 2 (2.42->2.74) | soap 1 (85.05->109.25), limestone 1 (12.6->20), hides 1 (11.23->13.68), flour 1 (20.58->21.28) | +56 |
| Angefont | 686 | 0.19 | 0.10 (10/turn) | cookware 11 (23.94->27.55), blades 3 (16.38->17.48), thread 18 (4.66->4.89) | candles 1 (83.48->87.5), scythes 1 (28.14->30.21), garments 2 (21.84->22.4), slaked lime 1 (6.72->7.31) | +46 |
| Hanstein | 380 | 0.10 | 0.30 (31/turn) | timber 13 (6.95->10.45), bricks 1 (4.54->7.74), charcoal 2 (1.76->3.15), logs 1 (3.24->5.65) | candles 1 (80.85->87.5), flax plants 59 (1.34->1.66), seeds 7 (1.81->2.32), wrought iron 3 (12.18->13.11) | +44 |
| Blanans | 297 | 0.08 | 0.40 (41/turn) | bread 147 (2.29->2.6), cheese 9 (7.09->7.74), salt 2 (4.3->6.79), grain 8 (2.54->2.91) | pasties 2 (6.25->12.92), candles 1 (81.38->87.5), flax plants 2 (1.23->1.66), garments 2 (22.05->22.4) | +43 |

**Best:** Rouhomme at about +179 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 74 @ min 3.7 | makes 56.0, uses 4.2, holds 373 (keeps 60): sells the surplus + 22/turn of the excess |
| candles | 3 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 2 = 1.3 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 24 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 103 = 4.0 turns |
| labour | 73 @ 2.2, stop - |  | uses 522.9/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 75 = 1.0 turns |
| limestone |  | 5 @ min 17.6 |  |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 8 @ min 39.2 | makes 6.0, uses 0.0, holds 50 (keeps 15): sells the surplus + 2/turn of the excess |
| porterage | 15 @ 1.1, stop - |  | uses 14.8/turn (observed), makes 0.0, holds 26 = 1.8 turns |
| tar | 3 @ 11.0, stop 5 |  | uses 1.1/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| timber |  | 52 @ min 8.5 | makes 24.0, uses 0.0, holds 707 (keeps 350): sells the surplus + 28/turn of the excess |
| tools | 7 @ 6.2, stop 51 |  | uses 6.3/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 31.6 turns |

## Chain sizing

Mode FULL, garments sold 2.6/turn (+0.0 exported); plan makes 0.4 garments a turn.
Labour: own 450, everything else 466, chain may buy 350 -> chain allowance 350, chain plan 161 (-2 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 3.69 | 3.64 |
| ret | 3 | 0.66 | 0.65 |
| spin | 4 | 1.35 | 1.33 |
| weave | 3 | 0.00 | 0.00 |
| sew | 2 | 0.02 | 0.01 |

Buffers: flax fibres 63/54, thread 320/171, cloth 16/13
- thread beyond the household duty (55 a turn) is fed from weaving

## Self-diagnosis

- R1: candles slot dry: 2.0 held, 1.5 a turn (luxury slot (+3 prestige)); our buy paused by the failsafe, home ask 87.5 (held back: paused by the failsafe at level 2: un-pause only at level 0)
- R1: prestige rate -0.95 a turn vs 12-turn median +3.10; likely: dry slot: candles
- R2: logging camp w/ tool blocked by timber space: 707 held of 711 capacity, we make 24.0 a turn; no buy on it: add a sell order or more capacity for timber
- R3: weavery 1 (weavery) finished but idle 6 turns (weave cloth 2 at 0); no planned recipe for a weavery: Taylor's call
- R3: mansion 1 (mansion) finished but idle 4 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R4: ropewalk 1 projected 0 of 1 (limited by tar)
