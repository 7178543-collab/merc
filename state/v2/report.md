# v2 shadow report

Turn 13385, 2026-10-19 02:57. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 4,601, prestige 3,364 (694 free, -0.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 214 | 0 | 4 | 0 | 0 | min_holding 60, sell 36, sell @ 3.54 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 17 | 5 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 236 | 0 | 2 | 0 | 0 | min_holding 30, sell 20, sell @ 20.8 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 0 | 0 | 421 | 0 | 29 | buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 39 | 0 | 0 | 0 | 0 | min_holding 15, sell 10, sell @ 34 |
| porterage | 7 | 7 | 7 | 7 | 0 | buy 7, buy @ 1.1 |

**2 risks, 0 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **porterage**: quarry 1 ran short of porterage (buy is live (7 @ 1.1), 7 bought last turn); labour need rises ~50/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **porterage**: buying 7, short of ~17 needed -> v2: buy 17

## Notes

- labour: projection runs 75 over real use lately; planning 442, not 517

## Prestige spending, cheapest coin per prestige first

1016 turns left: prestige gained now converts 99.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 45.3 | 45.3 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 53.1 | 53.1 | thin at home: wine, cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 54.5 | 54.5 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 54.8 | 54.8 | thin at home: cured fish |
| hold prayer 2 | chapel | 13 | 52.8 | 55.2 | needs a chapel (build cost 30,516); thin at home: furniture |
| jousting 1 | arena | 170 | 55.5 | 55.6 | needs a arena (build cost 23,939); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 55.9 | 55.9 | thin at home: wine |
| hold feast 2 | townhouse | 2.6 | 53.2 | 55.9 | needs a townhouse (build cost 6,980); thin at home: wine |
| hold sermon 2 (candles) | church | 31 | 53.6 | 56.3 | needs a church (build cost 77,657); thin at home: candles, furniture |
| hold sermon 2 | church | 24 | 53.3 | 56.8 | needs a church (build cost 77,657); thin at home: furniture |
| hold banquet 3 (meat) | mansion | 7.6 | 57.3 | 57.3 |  |
| hold banquet 1 (meat) | mansion | 4.2 | 58.6 | 58.6 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.20 | 19 | 120102307 | 0.448 | - | furniture 23 | -331 |
| linen snake | 0.1 / 0.10 | 9 | 151802239 | 0.448 | - | furniture 28 | -394 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: furniture buy 24 @ 14.2, pasties buy 1 @ 15.0; crew 0.1; est +287 a turn; stock: furniture 24 @ 14.2 (keep 140); stock: pasties 1 @ 15.0 (keep 14)
- **Flax Wyrm** on Rouhomme: pasties buy 10 @ 15.8; crew 0.1; est +22 a turn; stock: pasties 10 @ 15.8 (keep 14)
- best towns now: Kleinburgh +350, Hofkirchen +344, Angefont +332, Blanans +296, Cobholme +291
- Kleinburgh would trade: furniture buy 28 @ 11.8, pasties buy 2 @ 15.6; crew 0.7

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~93 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Vauxvais | 204 | 0.05 | 0.30 (28/turn) | bread 150 (2.16->2.66), rope 1 (72->80.27), tools 16 (4.14->4.5), cheese 6 (6.35->6.46) | flax fibres 15 (5.88->7), pasties 2 (14.6->18.9), candles 1 (71.4->76.5), cloth 6 (7.88->8.45) | +98 |
| Bordetes | 831 | 0.21 | 0.10 (9/turn) | rope 3 (72->84.08), wrought iron 11 (13.12->16.15), salt 5 (4.49->6.74), tallow 1 (21->22.99) | pasties 2 (14.6->18.9), cloth 6 (7.77->8.45), candles 1 (74.55->76.5), tools 2 (4.51->4.8) | +91 |
| Heilegg | 826 | 0.21 | 0.20 (19/turn) | tools 16 (4.14->7.6), rope 2 (72->77.9), yarn 12 (3.34->4.31), nets 9 (35.2->36.29) | candles 1 (71.4->76.5), pasties 2 (16.38->18.9), cloth 6 (7.93->8.45), flax fibres 3 (5.83->7) | +87 |
| Gottweiler | 1135 | 0.37 | 0.10 (9/turn) | garments 18 (20.01->22.8), thread 2 (4.66->6.7), yarn 1 (3.34->4.14) | butter 1 (63->75.05), pasties 2 (13.65->18.9), cloth 6 (7.56->8.45) | +69 |
| Rouhomme | 368 | 0.09 | 0.60 (56/turn) | bread 150 (2.16->2.66), beer 36 (2.87->3.42), thread 6 (4.66->5.42), tallow 1 (21->22.99) | pasties 2 (16.28->18.9), candles 1 (72.45->76.5), flax fibres 3 (5.88->7), blades 2 (14.7->15.96) | +66 |

**Best:** Vauxvais at about +98 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 27.0, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 35 @ min 3.54 | makes 28.0, uses 4.2, holds 214 (keeps 60): sells the surplus + 11/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 17 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 18 @ min 20.8 | makes 3.3, uses 2.1, holds 236 (keeps 30): sells the surplus + 17/turn of the excess |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 0 @ 2.2, stop - |  | uses 441.8/turn (brewery 1, flax farm 1, household), makes 450.0, holds 0 |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 10 @ min 34.2 | makes 9.0, uses 0.0, holds 39 (keeps 15): sells the surplus + 1/turn of the excess |
| pasties | 6 @ 19.8, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 4 = 1.4 turns |
| porterage | 17 @ 1.1, stop - |  | uses 16.9/turn (observed), makes 0.0, holds 7 = 0.4 turns |
| rope |  | 7 @ min 70.0 | makes 2.2, uses 0.0, holds 60 (keeps 0): sells the surplus + 5/turn of the excess |
| timber |  | 9 @ min 6.7 |  |
| tools | 3 @ 6.2, stop 22 |  | uses 2.7/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 74.6 turns |

## Chain sizing

Mode HOLD, garments sold 9.7/turn (+0.0 exported); plan makes 3.7 garments a turn.
Labour: own 450, everything else 411, chain may buy 350 -> chain allowance 389, chain plan 129 (-7 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 2.56 | 2.41 |
| ret | 3 | 0.46 | 0.43 |
| spin | 4 | 0.94 | 0.88 |
| weave | 3 | 0.12 | 0.13 |
| sew | 2 | 0.08 | 0.09 |

Buffers: flax fibres 57/48, thread 449/141, cloth 23/14

## Self-diagnosis

- R1: pasties slot dry: 4.0 held, 2.8 a turn (basic food slot (+1.3 prestige)); our buy 6 @ 16.2, home ask 18.9 (held back: failsafe level 1: reduce-only, would buy 6 @ 19.2 (ask 18.9, cap 27.9))
- R2: ropewalk 1 blocked by rope space: 60 held of 60 capacity, we make 2.2 a turn; no buy on it: add a sell order or more capacity for rope
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R4: quarry 1 projected 0 of 0.45 (limited by porterage)
