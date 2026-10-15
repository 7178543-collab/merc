# v2 shadow report

Turn 13310, 2026-10-15 23:48. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,240, prestige 3,105 (435 free, -3.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 411 | 0 | 4 | 0 | 0 | min_holding 60, sell 75, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 24 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 28 | 0 | 2 | 0 | 0 | min_holding 30, sell 2, sell @ 22 |
| grain | 103 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 43 | 75 | 496 | 0 | 29 | buy 43, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 49 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 38.2 |
| porterage | 26 | 26 | 20 | 0 | 6 | buy 26, buy @ 0.8 |

**1 risks, 1 waste, 4 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **tar**: ropewalk 1 ran short of tar (buy is live (no volume cap @ 9.6), but the home ask 9.90 is above it); labour need rises ~28/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 29 labour expired last turn (~47 coin): holding 43 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **candles**: home ask 88.00 is above our ceiling 70.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **timber**: build materials for park 1 are in (702.0 held, 17 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 58% (EXPANSION), about 6 turns left; still to deliver: labour 110, limestone 26, timber 17; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 26 | 112.1 | 0 | off: covered |
| timber | 17 | 702.0 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 19

## Notes

- labour: projection runs 14 over real use lately; planning 538, not 552

## Prestige spending, cheapest coin per prestige first

1091 turns left: prestige gained now converts 99.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.9 | 52.4 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 57.7 | 57.7 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 58.4 | 58.4 |  |
| hold banquet 4 (pies) | mansion | 18 | 58.7 | 58.7 | thin at home: pasties, hop beer |
| hold banquet 2 (pies) | mansion | 7 | 58.8 | 58.8 | thin at home: pasties, pies |
| hold prayer 2 | chapel | 13 | 56.3 | 58.8 | needs a chapel (build cost 33,238); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 56.8 | 59.1 | needs a church (build cost 71,244); thin at home: jewellery, candles, furniture |
| hold banquet 3 (pies) | mansion | 8 | 59.5 | 59.5 | thin at home: pasties, hop beer, pies |
| hold sermon 2 | church | 24 | 56.9 | 59.8 | needs a church (build cost 71,244); thin at home: jewellery, furniture |
| hold banquet 3 (fish) | mansion | 7.6 | 60.3 | 60.3 | thin at home: hop beer |
| hold mass 2 (premium) | cathedral | 360 | 59.7 | 60.6 | needs a cathedral (build cost 284,900); thin at home: furniture, jewellery, glassware, candles, premium garments |
| jousting 3 | arena | 230 | 61.2 | 61.3 | needs a arena (build cost 26,512); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 74001604 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Brunnham: lead bars sell 8 @ 14.1, tallow sell 3 @ 32.2, varnish sell 1 @ 23.0; crew 0.1; est +15 a turn
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn; best orders clear only 14 a turn after crew: ship stays at 0
- best towns now: Hofkirchen +124, Fulkirch +54, Herschweig +30, Friedwerp +28, Karlmoor +28
- Hofkirchen would trade: acid buy 2 @ 153, nets sell 3 @ 42.2, steel ingots sell 2 @ 16.1, tackles sell 1 @ 214, tallow sell 3 @ 31.4; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~102 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.32 | 0.20 (20/turn) | tackles 1 (173.25->216.6), steel ingots 2 (13.86->16.81), tallow 3 (28.56->30.4), nets 3 (39.6->40.85) | acid 2 (157.5->180.5), wrought iron 4 (12.71->13.77), gears 1 (73.5->74.58), scythes 1 (29.4->30.4) | +95 |
| Grandgues | 152 | 0.04 | 0.30 (31/turn) | timber 21 (5.96->7.5), beer 68 (3.28->3.59), rope 3 (84->85.02), firewood 1 (1.71->5.37) | soap 1 (76.65->107.35), pasties 2 (13.12->14.06), pies 2 (17.12->17.86), cloth 1 (8.19->8.5) | +71 |
| Friedwerp | 684 | 0.19 | 0.20 (20/turn) | tackles 1 (173.25->197.6), beer 43 (3.28->4.1), nets 2 (39.6->42.18), flax fibres 5 (4.75->5.7) | pies 1 (17.12->17.86) | +54 |
| Rouhomme | 368 | 0.10 | 0.20 (20/turn) | beer 81 (3.28->3.8), rope 2 (84->85.5), hop beer 1 (11.03->11.59), pasties 1 (15.65->16.25) | soap 1 (87.67->107.35), scythes 1 (27.93->30.4), tools 4 (4.91->5.15), wheels 2 (21.42->22.04) | +51 |
| Toqueque | 642 | 0.17 | 0.10 (10/turn) | garments 15 (23.1->24.7), flax fibres 5 (4.75->5.46), nails 2 (5.4->5.94), resin 4 (2.42->3.04) | soap 1 (85.05->107.35) | +46 |

**Best:** Hofkirchen at about +95 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 30.4, stop 1 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 1 = 2.0 turns |
| beer |  | 77 @ min 3.7 | makes 56.0, uses 4.2, holds 411 (keeps 60): sells the surplus + 25/turn of the excess |
| candles | 1 @ 70.0, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 0 = 0.0 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 24 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 103 = 4.0 turns |
| labour | 88 @ 2.2, stop - |  | uses 537.9/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 43 = 0.5 turns |
| limestone |  | 5 @ min 17.5 |  |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 8 @ min 38.6 | makes 6.0, uses 0.0, holds 49 (keeps 15): sells the surplus + 2/turn of the excess |
| porterage | 17 @ 1.1, stop - |  | uses 17.1/turn (observed), makes 0.0, holds 26 = 1.5 turns |
| tar | 3 @ 11.0, stop 5 |  | uses 1.1/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| timber |  | 51 @ min 8.5 | makes 24.0, uses 0.0, holds 702 (keeps 350): sells the surplus + 27/turn of the excess |
| tools | 7 @ 6.2, stop 50 |  | uses 6.2/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 32.1 turns |

## Chain sizing

Mode FULL, garments sold 2.2/turn (+0.0 exported); plan makes 0.4 garments a turn.
Labour: own 450, everything else 465, chain may buy 350 -> chain allowance 350, chain plan 144 (-8 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 3.44 | 3.26 |
| ret | 3 | 0.61 | 0.58 |
| spin | 4 | 1.26 | 1.19 |
| weave | 3 | 0.00 | 0.00 |
| sew | 2 | 0.02 | 0.01 |

Buffers: flax fibres 63/54, thread 403/170, cloth 13/12
- thread beyond the household duty (55 a turn) is fed from weaving

## Self-diagnosis

- R1: candles slot dry: 0.0 held, 1.5 a turn (luxury slot (+3 prestige)); our buy paused by the failsafe, home ask 88.0 (held back: paused by the failsafe at level 1: un-pause only at level 0)
- R1: prestige rate -3.94 a turn vs 12-turn median +2.92; likely: dry slot: candles
- R2: logging camp w/ tool blocked by timber space: 702 held of 711 capacity, we make 24.0 a turn; no buy on it: add a sell order or more capacity for timber
- R3: weavery 1 (weavery) finished but idle 6 turns (weave cloth 2 at 0); no planned recipe for a weavery: Taylor's call
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R4: ropewalk 1 projected 0 of 1 (limited by tar)
