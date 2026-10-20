# v2 shadow report

Turn 13409, 2026-10-20 02:58. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 8,108, prestige 3,417 (747 free, -1.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 180 | 0 | 4 | 0 | 0 | min_holding 60, sell 33, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 151 | 0 | 2 | 0 | 0 | min_holding 30, sell 14, sell @ 20.8 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 19 | 9 | 459 | 7 | 0 | buy 19, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 15 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34.8 |
| porterage | 37 | 37 | 16 | 0 | 21 | buy 37, buy @ 1.1 |

**0 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5

## Notes

- labour: projection runs 150 over real use lately; planning 466, not 541

## Prestige spending, cheapest coin per prestige first

992 turns left: prestige gained now converts 99.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.7 | 47.7 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 53.8 | 53.8 | thin at home: wine |
| hold banquet 1 (fish) | mansion | 4.2 | 54.8 | 54.8 |  |
| hold feast 2 | townhouse | 2.6 | 52.2 | 55.0 | needs a townhouse (build cost 7,034); thin at home: wine |
| hold prayer 2 | chapel | 13 | 52.6 | 55.3 | needs a chapel (build cost 32,758); thin at home: furniture |
| hold banquet 3 (fish) | mansion | 7.6 | 55.7 | 55.7 |  |
| hold banquet 2 (meat) | mansion | 6.8 | 56.4 | 56.4 | thin at home: wine |
| hold sermon 2 | church | 24 | 52.8 | 56.5 | needs a church (build cost 80,670); thin at home: jewellery, furniture |
| hold sermon 2 (candles) | church | 31 | 54.4 | 57.3 | needs a church (build cost 80,670); thin at home: jewellery, candles, furniture |
| hold banquet 2 (pies) | mansion | 7 | 57.9 | 57.9 | thin at home: pasties, wine |
| hold banquet 3 (meat) | mansion | 7.6 | 58.0 | 58.0 |  |
| jousting 1 | arena | 170 | 57.8 | 58.0 | needs a arena (build cost 25,487); thin at home: protection, light armour, arms; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 120102307 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: furniture buy 2 @ 13.9, tools buy 2 @ 4.44; crew 0.1; est +16 a turn; stock: furniture 2 @ 13.9 (keep 145)
- **Flax Wyrm** on Rouhomme: nothing pays; crew 0.0; est +0 a turn; stock: furniture 2 @ 14.2 (keep 145); best orders clear only 15 a turn after crew: ship stays at 0
- best towns now: Disscester +56, Großaue +22, Hofkirchen +19, Toqueque +19, Herschweig +19
- Disscester would trade: furniture buy 2 @ 13.1, garments sell 10 @ 23.6; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~96 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Cobholme | 1564 | 0.60 | 0.20 (19/turn) | cured fish 7 (23.31->30.59), cured meat 3 (24.15->28.88), nets 2 (35.8->40.09), rope 1 (81->86.45) | ploughs 1 (36.96->66.02) | +90 |
| Disscester | 1474 | 0.55 | 0.20 (19/turn) | garments 10 (19.59->23.18), slaked lime 1 (7.4->20.14), wrought iron 6 (12.6->14.25), nets 1 (35.8->39.9) | candles 1 (74.55->84), medicine 1 (126->131.1), wax 1 (21.63->23.75) | +64 |
| Karlmoor | 787 | 0.20 | 0.10 (10/turn) | nets 5 (35.8->43.51), cheese 5 (6.93->7.84), fleece 1 (5.99->6.6), seeds 3 (1.87->2.38) | candles 1 (77.7->84), pasties 1 (8.77->14.4), wrought iron 4 (10.34->10.64) | +48 |
| Friedwerp | 684 | 0.18 | 0.10 (10/turn) | casks 6 (5.67->7.74), slaked lime 1 (7.4->15.39), flax fibres 4 (4.57->4.99) | candles 1 (70.88->84), paper 5 (19.21->21.47), mouldboards 1 (41.79->47.12), cheese 13 (5.83->6.22) | +47 |
| Hofkirchen | 991 | 0.30 | 0.10 (10/turn) | nets 6 (35.8->38.19), tools 16 (4.66->5.03), yarn 2 (4.35->4.75) | candles 1 (71.4->84), medicine 1 (119.7->131.1), acid 1 (132.3->135.85), garments 2 (19.95->20.4) | +38 |

**Best:** Cobholme at about +90 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 26.2, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 32 @ min 3.38 | makes 28.0, uses 4.2, holds 180 (keeps 60): sells the surplus + 8/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 16 @ 2.2, stop - |  | uses 465.8/turn (brewery 1, flax farm 1, household), makes 450.0, holds 19 = 1.2 turns |
| limestone |  | 5 @ min 16.9 |  |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 34.8 |  |
| pasties | 3 @ 15.1, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 4.9 turns |
| porterage | 16 @ 1.1, stop - |  | uses 16.0/turn (observed), makes 0.0, holds 37 = 2.3 turns |
| rope |  | 2 @ min 79.0 |  |
| timber |  | 12 @ min 6.7 | makes 8.4, uses 0.0, holds 400 (keeps 350): sells the surplus + 3/turn of the excess |
| tools | 3 @ 6.2, stop 22 |  | uses 2.7/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 73.7 turns |

## Chain sizing

Mode HOLD, garments sold 3.2/turn (+0.0 exported); plan makes 1.6 garments a turn.
Labour: own 450, everything else 406, chain may buy 350 -> chain allowance 394, chain plan 132 (+0 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 2.69 | 2.68 |
| ret | 3 | 0.48 | 0.48 |
| spin | 4 | 1.05 | 1.04 |
| weave | 3 | 0.07 | 0.05 |
| sew | 2 | 0.04 | 0.04 |

Buffers: flax fibres 57/45, thread 304/133, cloth 11/6

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
