# v2 shadow report

Turn 13387, 2026-10-19 04:03. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 4,654, prestige 3,362 (692 free, -0.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 191 | 0 | 4 | 0 | 0 | min_holding 60, sell 35, sell @ 3.54 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 5 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 207 | 0 | 2 | 0 | 0 | min_holding 30, sell 18, sell @ 20.8 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 0 | 0 | 410 | 0 | 40 | buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 35 | 0 | 0 | 0 | 0 | min_holding 15, sell 10, sell @ 34.2 |
| porterage | 7 | 7 | 7 | 10 | 0 | buy 7, buy @ 1.1 |

**2 risks, 1 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **porterage**: logging camp w/ tool, quarry 1 ran short of porterage (buy is live (7 @ 1.1), 7 bought last turn); labour need rises ~74/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **porterage**: buying 7, short of ~17 needed -> v2: buy 17

## Waste (money lost now)

- **Flax Wyrm**: Flax Wyrm cost 9 coin last turn (crew 0.10) and its route traded nothing (route limited by pasties space) -> v2: pause it (crew 0) until a route is proven to sell

## Notes

- labour: projection runs 75 over real use lately; planning 419, not 494

## Prestige spending, cheapest coin per prestige first

1014 turns left: prestige gained now converts 99.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 45.3 | 45.3 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 53.0 | 53.0 | thin at home: wine, cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 54.5 | 54.5 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 54.8 | 54.8 | thin at home: cured fish |
| hold banquet 2 (meat) | mansion | 6.8 | 55.5 | 55.5 | thin at home: wine |
| hold feast 2 | townhouse | 2.6 | 52.8 | 55.5 | needs a townhouse (build cost 6,982); thin at home: wine |
| jousting 1 | arena | 170 | 55.3 | 55.5 | needs a arena (build cost 24,757); thin at home: protection, light armour, arms; needs weaponry skill |
| hold prayer 2 | chapel | 13 | 53.2 | 55.8 | needs a chapel (build cost 31,902); thin at home: furniture |
| hold banquet 3 (meat) | mansion | 7.6 | 57.1 | 57.1 |  |
| hold banquet 2 (pies) | mansion | 7 | 57.6 | 57.6 | thin at home: pasties, wine |
| hold sermon 2 (candles) | church | 31 | 54.8 | 57.6 | needs a church (build cost 80,848); thin at home: jewellery, candles, furniture |
| hold banquet 3 (pies) | mansion | 8 | 58.0 | 58.0 | thin at home: pasties |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 9 | 120102307 | 0.12 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 9 | 151802239 | 0.396 | - | furniture 7 | -98 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Rouhomme: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 16.4 (keep 14); best orders clear only -2 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 14.9 (keep 14); best orders clear only -1 a turn after crew: ship stays at 0
- best towns now: Neuborn +19, Pontmont +18
- Neuborn would trade: nets sell 2 @ 39.8, pasties buy 3 @ 12.3; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~92 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Vauxvais | 204 | 0.05 | 0.30 (28/turn) | bread 151 (2.14->2.66), yarn 2 (3.53->4.16) | flax fibres 14 (5.88->6.6), pasties 2 (14.6->16.3), beer 4 (3.32->3.6), cloth 6 (7.88->8.05) | +69 |
| Karlmoor | 787 | 0.19 | 0.10 (9/turn) | garments 14 (19.97->21.28), resin 7 (2.29->4.33), yarn 5 (3.53->4.56) | butter 1 (48.93->63.17), candles 1 (70.88->78), pasties 1 (12.5->16.3), flax fibres 3 (5.78->6.6) | +58 |
| Heilegg | 826 | 0.21 | 0.20 (18/turn) | tools 16 (4.8->7.6), yarn 5 (3.53->4.31), flax plants 3 (1.36->2.36), nets 6 (35.2->35.91) | candles 1 (70.35->78), flax fibres 6 (5.78->6.6), salt 11 (4.03->4.41), cloth 6 (7.72->8.05) | +58 |
| Friedwerp | 684 | 0.17 | 0.10 (9/turn) | tools 16 (4.8->6.65), nets 6 (35.2->38.38), wrought iron 1 (13.44->18.52), yarn 5 (3.53->4.69) | wheels 1 (17.32->22.42), hop beer 1 (7.82->8.6), pasties 1 (15.33->16.3) | +57 |
| Rouhomme | 368 | 0.09 | 0.60 (56/turn) | bread 151 (2.14->2.66), beer 34 (3.12->3.42), thread 6 (4.66->5.42), tallow 1 (21->23.18) | candles 1 (72.45->78), blades 2 (14.7->16.05), flax fibres 3 (5.88->6.6), tools 2 (4.7->4.88) | +53 |

**Best:** Vauxvais at about +69 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 26.2, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 33 @ min 3.54 | makes 28.0, uses 4.2, holds 191 (keeps 60): sells the surplus + 9/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 16 @ min 20.8 | makes 3.3, uses 2.1, holds 207 (keeps 30): sells the surplus + 15/turn of the excess |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 0 @ 2.2, stop - |  | uses 419.3/turn (brewery 1, flax farm 1, household), makes 450.0, holds 0 |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 10 @ min 34.2 |  |
| pasties | 4 @ 17.1, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 10 = 3.7 turns |
| porterage | 17 @ 1.1, stop - |  | uses 17.4/turn (observed), makes 0.0, holds 7 = 0.4 turns |
| rope |  | 7 @ min 72.0 | makes 2.2, uses 0.0, holds 60 (keeps 0): sells the surplus + 5/turn of the excess |
| tools | 3 @ 6.2, stop 21 |  | uses 2.6/turn (retting pit 1), makes 0.0, holds 200 = 76.2 turns |

## Chain sizing

Mode HOLD, garments sold 9.2/turn (+0.0 exported); plan makes 3.3 garments a turn.
Labour: own 450, everything else 414, chain may buy 350 -> chain allowance 386, chain plan 123 (-4 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 2.41 | 2.33 |
| ret | 3 | 0.43 | 0.41 |
| spin | 4 | 0.88 | 0.85 |
| weave | 3 | 0.12 | 0.12 |
| sew | 2 | 0.08 | 0.08 |

Buffers: flax fibres 57/48, thread 463/140, cloth 22/13

## Self-diagnosis

- R2: ropewalk 1 blocked by rope space: 60 held of 60 capacity, we make 2.2 a turn; no buy on it: add a sell order or more capacity for rope
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R4: quarry 1 projected 0 of 0.45 (limited by porterage)
