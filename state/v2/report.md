# v2 shadow report

Turn 13312, 2026-10-16 01:04. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,273, prestige 3,097 (427 free, -3.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 412 | 0 | 4 | 0 | 0 | min_holding 60, sell 77, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 4 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 25 | 0 | 2 | 0 | 0 | min_holding 80, sell 2, sell @ 22 |
| grain | 103 | 26 | 13 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 80 | 80 | 449 | 0 | 81 | buy 80, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 48 | 0 | 0 | 0 | 0 | min_holding 15, sell 8, sell @ 38.6 |
| porterage | 26 | 26 | 17 | 0 | 9 | buy 26, buy @ 0.8 |

**1 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **tar**: ropewalk 1 ran short of tar (buy is live (no volume cap @ 9.6), but the home ask 10.70 is above it); labour need rises ~28/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 81 labour expired last turn (~136 coin): holding 80 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **timber**: build materials for park 1 are in (708.0 held, 10 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 75% (EXPANSION), about 3 turns left; still to deliver: labour 65, limestone 15, timber 10; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 15 | 112.5 | 0 | off: covered |
| timber | 10 | 708.0 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 22

## Notes

- labour: projection runs 54 over real use lately; planning 449, not 484

## Prestige spending, cheapest coin per prestige first

1089 turns left: prestige gained now converts 99.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.4 | 53.9 | running |
| hold banquet 2 (pies) | mansion | 7 | 56.5 | 56.5 | thin at home: pasties, pies |
| hold banquet 2 (fish) | mansion | 6.8 | 57.9 | 57.9 |  |
| hold banquet 4 (pies) | mansion | 18 | 58.0 | 58.0 | thin at home: pasties, hop beer |
| hold banquet 1 (fish) | mansion | 4.2 | 58.4 | 58.4 |  |
| hold banquet 3 (pies) | mansion | 8 | 58.4 | 58.4 | thin at home: pasties, hop beer, pies |
| hold sermon 2 (candles) | church | 31 | 56.8 | 59.2 | needs a church (build cost 71,863); thin at home: jewellery, candles, furniture |
| hold prayer 2 | chapel | 13 | 56.9 | 59.4 | needs a chapel (build cost 33,661); thin at home: furniture |
| hold feast 2 | townhouse | 2.6 | 57.9 | 60.3 | needs a townhouse (build cost 6,718) |
| hold sermon 2 | church | 24 | 57.6 | 60.6 | needs a church (build cost 71,863); thin at home: jewellery, furniture |
| hold mass 2 (premium) | cathedral | 360 | 60.0 | 60.8 | needs a cathedral (build cost 287,555); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 3 (fish) | mansion | 7.6 | 61.0 | 61.0 | thin at home: hop beer |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 74001604 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Brunnham: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn; best orders clear only 10 a turn after crew: ship stays at 0
- best towns now: Angefont +21, Hanstein +18, Darmwald +17
- Angefont would trade: blades sell 1 @ 17.5, cookware sell 10 @ 25.4; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~104 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hanstein | 380 | 0.11 | 0.30 (31/turn) | timber 14 (5.96->10.45), tackles 1 (173.25->195.7), charcoal 2 (1.79->3.5), tools 9 (5.13->5.32) | seeds 9 (1.81->2.32), scythes 1 (28.77->30.59), beer 4 (3.3->3.7) | +73 |
| Angefont | 686 | 0.19 | 0.10 (10/turn) | cookware 10 (22.68->28.12), blades 1 (16.38->17) | scythes 1 (28.14->30.59), cloth 1 (7.35->8.1) | +47 |
| Etallaen | 774 | 0.22 | 0.30 (31/turn) | beer 53 (3.28->4.18), glassware 1 (64.05->80.75), nails 2 (5.4->5.65) | cloth 1 (7.35->8.1), flax fibres 1 (5.23->6.25), wrought iron 3 (13.23->13.87) | +38 |
| Arnsreuth | 921 | 0.29 | 0.10 (10/turn) | thread 31 (4.66->5.27) | jewellery 2 (77.7->83.6), stockfish 1 (90.3->99.75), flax fibres 10 (5.19->6.25), cloth 1 (7.77->8.1) | +35 |
| Grandgues | 152 | 0.04 | 0.40 (42/turn) | beer 53 (3.28->3.59), rope 2 (85.05->88.83), timber 16 (5.96->6.98), bread 146 (2.29->2.43) | pies 2 (17.12->17.95), flax fibres 2 (6.04->6.25) | +31 |

**Best:** Hanstein at about +73 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 25.8, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 1 = 2.0 turns |
| beer |  | 51 @ min 3.7 | makes 28.0, uses 4.2, holds 412 (keeps 60): sells the surplus + 27/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 5.3 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| grain | 13 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 103 = 7.9 turns |
| labour | 0 @ 2.2, stop - |  | uses 449.2/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 80 |
| limestone |  | 5 @ min 17.4 |  |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 8 @ min 36.6 | makes 6.0, uses 0.0, holds 48 (keeps 15): sells the surplus + 2/turn of the excess |
| porterage | 14 @ 1.1, stop - |  | uses 13.8/turn (observed), makes 0.0, holds 26 = 1.9 turns |
| tar | 3 @ 11.0, stop 5 |  | uses 1.1/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| timber |  | 41 @ min 8.5 | makes 12.0, uses 0.0, holds 708 (keeps 350): sells the surplus + 29/turn of the excess |
| tools | 4 @ 6.2, stop 30 |  | uses 3.7/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 54.5 turns |

## Chain sizing

Mode HOLD, garments sold 2.0/turn (+0.0 exported); plan makes 21.7 garments a turn.
Labour: own 450, everything else 411, chain may buy 350 -> chain allowance 389, chain plan 390 (+244 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 3.26 | 5.56 |
| ret | 3 | 0.58 | 0.99 |
| spin | 4 | 1.19 | 2.04 |
| weave | 3 | 0.00 | 0.84 |
| sew | 2 | 0.02 | 0.53 |

Buffers: flax fibres 63/82, thread 474/242, cloth 10/84
- chain plan needed 708 labour, budget left 389: cut to 389 (sewing capped at 0.53)

## Self-diagnosis

- R1: candles slot dry: 0.0 held, 1.5 a turn (luxury slot (+3 prestige)); our buy paused by the failsafe, home ask 79.0 (held back: paused by the failsafe at level 1: un-pause only at level 0)
- R1: prestige rate -3.90 a turn vs 12-turn median -0.95; likely: dry slot: candles
- R2: logging camp w/ tool blocked by timber space: 708 held of 711 capacity, we make 12.0 a turn; no buy on it: add a sell order or more capacity for timber
- R3: weavery 1 (weavery) finished but idle 6 turns (weave cloth 2 at 0); no planned recipe for a weavery: Taylor's call
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R4: ropewalk 1 projected 0 of 1 (limited by tar)
