# v2 shadow report

Turn 13384, 2026-10-19 01:08. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 4,971, prestige 3,364 (694 free, -0.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 226 | 0 | 4 | 0 | 0 | min_holding 60, sell 38, sell @ 3.54 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 252 | 0 | 2 | 0 | 0 | min_holding 30, sell 22, sell @ 20.8 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 0 | 0 | 406 | 0 | 44 | buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 41 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 34 |
| porterage | 7 | 7 | 7 | 3 | 0 | buy 7, buy @ 1.1 |

**3 risks, 0 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **pasties**: needed (2.8/turn) but there is NO buy order, stock 4.8 -> v2: add buy 6
- **porterage**: quarry 1 ran short of porterage (buy is live (7 @ 1.1), 7 bought last turn); labour need rises ~28/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **porterage**: buying 7, short of ~13 needed -> v2: buy 13

## Notes

- labour: projection runs 75 over real use lately; planning 406, not 481

## Prestige spending, cheapest coin per prestige first

1017 turns left: prestige gained now converts 99.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 45.6 | 45.6 | running |
| hold prayer 2 | chapel | 13 | 52.8 | 55.4 | needs a chapel (build cost 32,496); thin at home: furniture |
| jousting 1 | arena | 170 | 55.4 | 55.5 | needs a arena (build cost 25,379); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 55.9 | 55.9 | thin at home: wine, cured fish |
| hold feast 2 | townhouse | 2.6 | 53.2 | 55.9 | needs a townhouse (build cost 7,008); thin at home: wine |
| hold sermon 2 | church | 24 | 53.4 | 57.0 | needs a church (build cost 80,753); thin at home: jewellery, furniture |
| hold banquet 3 (fish) | mansion | 7.6 | 57.4 | 57.4 | thin at home: cured fish |
| hold banquet 2 (meat) | mansion | 6.8 | 57.5 | 57.5 | thin at home: wine |
| hold sermon 2 (candles) | church | 31 | 54.9 | 57.7 | needs a church (build cost 80,753); thin at home: jewellery, candles, furniture |
| hold banquet 1 (fish) | mansion | 4.2 | 58.0 | 58.0 | thin at home: cured fish |
| hold banquet 2 (pies) | mansion | 7 | 58.1 | 58.1 | thin at home: pasties, wine, pies |
| hold banquet 3 (pies) | mansion | 8 | 58.6 | 58.6 | thin at home: pasties, pies |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 120102307 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: furniture buy 28 @ 14.2; crew 0.1; est +332 a turn; stock: furniture 28 @ 14.2 (keep 140)
- **Flax Wyrm** on Rouhomme: furniture buy 28 @ 14.2; crew 0.2; est +323 a turn; stock: furniture 28 @ 14.2 (keep 140)
- best towns now: Kleinburgh +378, Hofkirchen +367, Angefont +359, Blanans +332, Grandgues +332
- Kleinburgh would trade: furniture buy 30 @ 11.6; crew 0.7

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~94 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Karlmoor | 787 | 0.20 | 0.30 (28/turn) | garments 14 (20.02->25.27), resin 7 (2.31->4.1), yarn 7 (3.34->4.27), wrought iron 11 (10.71->11.3) | salt 10 (4.28->5.56), candles 1 (80.85->84.5), pasties 1 (12.6->16.2), tiles 1 (0.99->4.01) | +112 |
| Vauxvais | 204 | 0.05 | 0.30 (28/turn) | bread 152 (2.16->2.66), rope 1 (72->80.27), yarn 5 (3.34->4.69), wrought iron 3 (10.71->12.25) | pasties 2 (10.92->16.2), salt 10 (4.51->5.56), candles 1 (77.7->84.5), cloth 6 (7.88->8.65) | +106 |
| Neuborn | 780 | 0.20 | 0.10 (9/turn) | nets 9 (34.6->42.18), yarn 4 (3.34->4.62), grain 4 (2.52->3.27) | candles 1 (72.45->84.5), pasties 2 (12.71->16.2), cloth 2 (8.19->8.65), nails 2 (5.67->6.41) | +89 |
| Hanstein | 380 | 0.10 | 0.30 (28/turn) | bellows 1 (321.3->364.8), wrought iron 8 (10.71->12.35), timber 9 (6.25->8.26), yarn 3 (3.34->4.62) | pasties 2 (13.65->16.2), salt 5 (4.68->5.56), candles 1 (82.42->84.5), cloth 4 (8.29->8.65) | +74 |
| Orlesailles | 1178 | 0.39 | 0.60 (56/turn) | thread 21 (4.66->6.27), beer 37 (2.88->3.95), yarn 23 (3.34->3.95), tar 3 (10.08->11.02) | candles 1 (70.35->84.5), salt 5 (4.16->5.56), pasties 2 (13.02->16.2), nails 2 (5.72->6.41) | +67 |

**Best:** Karlmoor at about +112 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 36 @ min 3.54 | makes 28.0, uses 4.2, holds 226 (keeps 60): sells the surplus + 12/turn of the excess |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 12 = 7.7 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 20 @ min 20.8 | makes 3.3, uses 2.1, holds 252 (keeps 30): sells the surplus + 18/turn of the excess |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 0 @ 2.2, stop - |  | uses 406.2/turn (brewery 1, flax farm 1, household), makes 450.0, holds 0 |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 10 @ min 34.0 | makes 9.0, uses 0.0, holds 41 (keeps 15): sells the surplus + 1/turn of the excess |
| pasties | 6 @ 17.0, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 5 = 1.7 turns |
| porterage | 13 @ 1.1, stop - |  | uses 12.6/turn (observed), makes 0.0, holds 7 = 0.6 turns |
| rope |  | 7 @ min 70.0 | makes 2.2, uses 0.0, holds 60 (keeps 0): sells the surplus + 5/turn of the excess |
| timber |  | 9 @ min 6.7 |  |
| tools | 3 @ 6.2, stop 22 |  | uses 2.7/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 74.8 turns |

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 3.7 garments a turn.
Labour: own 450, everything else 389, chain may buy 350 -> chain allowance 411, chain plan 133 (-4 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 2.56 | 2.47 |
| ret | 3 | 0.46 | 0.44 |
| spin | 4 | 0.94 | 0.91 |
| weave | 3 | 0.12 | 0.13 |
| sew | 2 | 0.08 | 0.09 |

Buffers: flax fibres 57/48, thread 440/142, cloth 24/15

## Self-diagnosis

- R1: pasties slot dry: 4.8 held, 2.8 a turn (basic food slot (+1.3 prestige)); our buy none, home ask 16.2 (held back: failsafe level 1: reduce-only, would buy 6 @ 16.5 (ask 16.2, cap 27.9))
- R2: ropewalk 1 blocked by rope space: 60 held of 60 capacity, we make 2.2 a turn; no buy on it: add a sell order or more capacity for rope
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R4: quarry 1 projected 0 of 0.25 (limited by porterage)
