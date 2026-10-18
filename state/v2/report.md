# v2 shadow report

Turn 13380, 2026-10-18 21:49. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 5,168, prestige 3,292 (622 free, -1.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 287 | 0 | 4 | 0 | 0 | min_holding 60, sell 42, sell @ 3.54 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 17 | 5 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 282 | 0 | 2 | 0 | 0 | min_holding 30, sell 22, sell @ 21.2 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 8 | 3 | 422 | 0 | 31 | buy 8, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 54 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 34 |
| porterage | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 1.1 |

**0 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **labour**: 31 labour expired last turn (~48 coin): holding 8 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 73 over real use lately; planning 422, not 486

## Prestige spending, cheapest coin per prestige first

1021 turns left: prestige gained now converts 99.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 46.5 | 46.5 | running |
| jousting 1 | arena | 170 | 55.5 | 55.6 | needs a arena (build cost 25,908); thin at home: protection, light armour, arms; needs weaponry skill |
| hold sermon 2 (candles) | church | 31 | 53.1 | 56.0 | needs a church (build cost 81,992); thin at home: candles, furniture |
| hold feast 2 | townhouse | 2.6 | 53.5 | 56.3 | needs a townhouse (build cost 7,360); thin at home: wine |
| hold prayer 2 | chapel | 13 | 53.7 | 56.5 | needs a chapel (build cost 34,000); thin at home: furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 56.9 | 56.9 | thin at home: wine, cured fish |
| hold banquet 2 (pies) | mansion | 7 | 57.6 | 57.6 | thin at home: pasties, wine, pies |
| hold banquet 3 (pies) | mansion | 8 | 57.6 | 57.6 | thin at home: pasties, pies |
| hold sermon 2 | church | 24 | 54.4 | 58.0 | needs a church (build cost 81,992); thin at home: furniture |
| hold banquet 1 (fish) | mansion | 4.2 | 58.2 | 58.2 | thin at home: cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 58.5 | 58.5 | thin at home: cured fish |
| hold banquet 2 (meat) | mansion | 6.8 | 59.0 | 59.0 | thin at home: wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 120102307 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 10 | 151802239 | 0.368 | - | furniture 23 | -324 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: furniture buy 23 @ 14.2, nets sell 4 @ 38.8; crew 0.1; est +280 a turn; stock: furniture 23 @ 14.2 (keep 140)
- **Flax Wyrm** on Rouhomme: nothing pays; crew 0.0; est +0 a turn; best orders clear only -9 a turn after crew: ship stays at 0
- best towns now: Hofkirchen +340, Angefont +339, Heilegg +337, Blanans +326, Kirchwerp +314
- Hofkirchen would trade: furniture buy 27 @ 13.0, rope sell 3 @ 76.5; crew 0.4

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~95 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Heidlowe | 662 | 0.17 | 0.20 (19/turn) | nets 11 (17.16->34.39), rope 3 (71->76), beer 42 (2.94->3.55) | yarn 4 (5.02->7.55), salt 5 (4.3->5.56), cured meat 8 (22.89->23.56), cloth 5 (7.61->7.85) | +229 |
| Marmont | 638 | 0.16 | 0.10 (9/turn) | nets 7 (17.16->37.81), arms 1 (26.04->26.6), flax fibres 1 (4.73->5.18) | yarn 8 (5.35->7.55), beer 4 (3.23->3.6), lead bars 1 (11.65->12.16), salt 1 (5->5.56) | +154 |
| Heilegg | 826 | 0.21 | 0.30 (28/turn) | nets 5 (17.16->34.01), rope 5 (71->76), beer 42 (2.94->3.78), flax fibres 1 (4.73->5.46) | yarn 11 (5.83->7.55), casks 6 (5.25->6.65), salt 5 (4.07->5.56), garments 2 (20.68->21.2) | +152 |
| Grandgues | 152 | 0.04 | 0.30 (28/turn) | nets 4 (17.16->38.76), beer 42 (2.94->3.61), bread 147 (2.21->2.43), timber 8 (6.3->7.27) | yarn 4 (5.21->7.55), salt 5 (4.14->5.56), casks 2 (5.3->6.65), tiles 2 (4.03->4.8) | +152 |
| Corstoft | 1496 | 0.55 | 0.20 (19/turn) | nets 6 (17.16->36.67), rope 1 (71->77.42) | yarn 6 (4.77->7.55), dyed yarn 1 (8.03->9.97), salt 5 (4.81->5.56), butter 1 (78.23->80.27) | +129 |

**Best:** Heidlowe at about +229 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 26.0, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 3 = 6.0 turns |
| beer |  | 41 @ min 3.54 | makes 28.0, uses 4.2, holds 287 (keeps 60): sells the surplus + 17/turn of the excess |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 12 = 7.7 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 17 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 22 @ min 21.2 | makes 3.3, uses 2.1, holds 282 (keeps 30): sells the surplus + 21/turn of the excess |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 0 @ 2.2, stop - |  | uses 422.0/turn (brewery 1, flax farm 1, household), makes 450.0, holds 8 |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 12 @ min 34.0 | makes 9.0, uses 0.0, holds 54 (keeps 15): sells the surplus + 3/turn of the excess |
| porterage | 7 @ 1.1, stop - |  | uses 7.1/turn (observed), makes 0.0, holds 7 = 1.0 turns |
| rope |  | 7 @ min 69.0 | makes 2.2, uses 0.0, holds 60 (keeps 0): sells the surplus + 5/turn of the excess |
| timber |  | 8 @ min 6.7 |  |
| tools | 3 @ 6.2, stop 22 |  | uses 2.7/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 74.6 turns |

## Chain sizing

Mode HOLD, garments sold 9.8/turn (+0.0 exported); plan makes 3.7 garments a turn.
Labour: own 450, everything else 362, chain may buy 350 -> chain allowance 438, chain plan 138 (+2 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 2.56 | 2.62 |
| ret | 3 | 0.46 | 0.47 |
| spin | 4 | 0.94 | 0.96 |
| weave | 3 | 0.12 | 0.12 |
| sew | 2 | 0.08 | 0.09 |

Buffers: flax fibres 56/48, thread 400/141, cloth 26/14

## Self-diagnosis

- R2: ropewalk 1 blocked by rope space: 60 held of 60 capacity, we make 2.2 a turn; no buy on it: add a sell order or more capacity for rope
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
