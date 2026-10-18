# v2 shadow report

Turn 13382, 2026-10-18 23:45. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 4,073, prestige 3,366 (696 free, +74.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 254 | 0 | 4 | 0 | 0 | min_holding 60, sell 39, sell @ 3.54 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 5 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 284 | 0 | 2 | 0 | 0 | min_holding 30, sell 22, sell @ 21.2 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 0 | 0 | 421 | 0 | 29 | buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 48 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 34 |
| porterage | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 1.1 |

**1 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **porterage**: buying 7, short of ~10 needed -> v2: buy 10

## Tuning

- **limestone**: we make 2/turn more than we use but there is no sell order -> v2: sell 1

## Notes

- labour: projection runs 75 over real use lately; planning 421, not 496

## Prestige spending, cheapest coin per prestige first

1019 turns left: prestige gained now converts 99.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 46.2 | 46.2 | running |
| jousting 1 | arena | 170 | 55.1 | 55.2 | needs a arena (build cost 23,935); thin at home: protection, light armour, arms; needs weaponry skill |
| hold prayer 2 | chapel | 13 | 53.3 | 55.8 | needs a chapel (build cost 30,364); thin at home: furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 56.0 | 56.0 | thin at home: wine |
| hold feast 2 | townhouse | 2.6 | 53.4 | 56.1 | needs a townhouse (build cost 6,994); thin at home: wine |
| hold sermon 2 (candles) | church | 31 | 53.8 | 56.6 | needs a church (build cost 78,520); thin at home: jewellery, candles, furniture |
| hold banquet 2 (pies) | mansion | 7 | 56.9 | 56.9 | thin at home: pasties, wine, pies |
| hold banquet 3 (pies) | mansion | 8 | 57.3 | 57.3 | thin at home: pasties, hop beer, pies |
| hold banquet 2 (meat) | mansion | 6.8 | 57.4 | 57.4 | thin at home: wine |
| hold banquet 3 (fish) | mansion | 7.6 | 57.7 | 57.7 | thin at home: hop beer |
| hold banquet 1 (fish) | mansion | 4.2 | 58.2 | 58.2 |  |
| hold sermon 2 | church | 24 | 55.1 | 58.6 | needs a church (build cost 78,520); thin at home: jewellery, furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.20 | 19 | 120102307 | 0.424 | - | furniture 26 | -369 |
| linen snake | 0.1 / 0.10 | 9 | 151802239 | 0.408 | nets 2 | furniture 24, pasties 2 | -324 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Rouhomme: nothing pays; crew 0.0; est +0 a turn; best orders clear only 14 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -8 a turn after crew: ship stays at 0
- best towns now: Karlmoor +28, Heilegg +26
- Karlmoor would trade: furniture buy 1 @ 8.75, garments sell 14 @ 22.6; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~94 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Vauxvais | 204 | 0.05 | 0.30 (28/turn) | bread 149 (2.18->2.66), rope 1 (71->80.75), nets 2 (33.6->37.05), tools 16 (4.24->4.6) | cloth 6 (7.88->12.9), pasties 2 (12.18->16.2), tiles 2 (3.57->6.08), flax fibres 15 (5.88->6.2) | +123 |
| Karlmoor | 787 | 0.20 | 0.20 (19/turn) | garments 14 (20.05->23.94), wool 1 (9.19->12.73) | cloth 6 (8.29->12.9), furniture 11 (9.03->11.49), nails 9 (6.2->6.74), casks 2 (5.72->6.65) | +105 |
| Pontmont | 341 | 0.09 | 0.10 (9/turn) | wrought iron 10 (13.76->19.19), rope 2 (71->79.8), nets 2 (33.6->34.96), thread 1 (4.66->4.84) | cloth 6 (8.29->12.9), pasties 2 (14.6->16.2), tiles 2 (3.74->6.08), casks 1 (5.46->6.65) | +104 |
| Rouhomme | 368 | 0.09 | 0.50 (47/turn) | bread 149 (2.18->2.7), cured meat 5 (25.62->27.17), thread 7 (4.66->5.46), cheese 16 (6.3->6.65) | candles 1 (50.4->69.5), cloth 5 (9.61->12.9), blades 2 (14.7->15.77), casks 2 (5.46->6.65) | +97 |
| Heilegg | 826 | 0.21 | 0.40 (38/turn) | nets 10 (33.6->36.48), rope 3 (71->76.47), yarn 17 (3.93->4.89), beer 39 (3.24->3.76) | cloth 6 (8.19->12.9), wax 1 (21->23.75), casks 2 (5.23->6.65), nails 9 (6.51->6.74) | +90 |

**Best:** Vauxvais at about +123 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 38 @ min 3.54 | makes 28.0, uses 4.2, holds 254 (keeps 60): sells the surplus + 14/turn of the excess |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 12 = 7.7 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 22 @ min 20.8 | makes 3.3, uses 2.1, holds 284 (keeps 30): sells the surplus + 21/turn of the excess |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 0 @ 2.2, stop - |  | uses 421.2/turn (brewery 1, flax farm 1, household), makes 450.0, holds 0 |
| limestone |  | 2 @ min 17.4 |  |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 11 @ min 34.0 | makes 9.0, uses 0.0, holds 48 (keeps 15): sells the surplus + 2/turn of the excess |
| pasties | 4 @ 17.0, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 10 = 3.7 turns |
| porterage | 10 @ 1.1, stop - |  | uses 10.4/turn (observed), makes 0.0, holds 7 = 0.7 turns |
| rope |  | 7 @ min 69.0 | makes 2.2, uses 0.0, holds 60 (keeps 0): sells the surplus + 5/turn of the excess |
| timber |  | 9 @ min 6.7 |  |
| tools | 3 @ 6.2, stop 22 |  | uses 2.7/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 74.9 turns |

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 3.7 garments a turn.
Labour: own 450, everything else 378, chain may buy 350 -> chain allowance 422, chain plan 136 (+0 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 2.56 | 2.56 |
| ret | 3 | 0.46 | 0.45 |
| spin | 4 | 0.94 | 0.94 |
| weave | 3 | 0.12 | 0.13 |
| sew | 2 | 0.08 | 0.09 |

Buffers: flax fibres 56/48, thread 420/142, cloth 25/15

## Self-diagnosis

- R2: ropewalk 1 blocked by rope space: 60 held of 60 capacity, we make 2.2 a turn; no buy on it: add a sell order or more capacity for rope
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R4: quarry 1 projected 0 of 0.15 (limited by porterage)
