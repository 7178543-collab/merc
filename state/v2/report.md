# v2 shadow report

Turn 13388, 2026-10-19 05:58. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 4,840, prestige 3,387 (717 free, +25.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 215 | 0 | 4 | 0 | 0 | min_holding 60, sell 35, sell @ 3.54 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 17 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 196 | 0 | 2 | 0 | 0 | min_holding 30, sell 15, sell @ 20.8 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 0 | 0 | 400 | 0 | 50 | buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 33 | 0 | 0 | 0 | 0 | min_holding 15, sell 10, sell @ 34.2 |
| porterage | 7 | 7 | 7 | 10 | 0 | buy 7, buy @ 1.1 |

**2 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **porterage**: quarry 1 ran short of porterage (buy is live (7 @ 1.1), 7 bought last turn); labour need rises ~77/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **porterage**: buying 7, short of ~22 needed -> v2: buy 22

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 75 over real use lately; planning 438, not 513

## Prestige spending, cheapest coin per prestige first

1013 turns left: prestige gained now converts 99.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 46.2 | 46.2 | running |
| jousting 1 | arena | 170 | 54.8 | 55.0 | needs a arena (build cost 25,139); thin at home: protection, light armour, arms; needs weaponry skill |
| hold prayer 2 | chapel | 13 | 53.0 | 55.7 | needs a chapel (build cost 33,016); thin at home: furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 55.9 | 55.9 | thin at home: wine, cured fish |
| hold feast 2 | townhouse | 2.6 | 53.0 | 55.9 | needs a townhouse (build cost 7,578); thin at home: wine |
| hold banquet 2 (meat) | mansion | 6.8 | 56.1 | 56.1 | thin at home: wine |
| hold sermon 2 (candles) | church | 31 | 54.1 | 56.9 | needs a church (build cost 80,553); thin at home: candles, furniture |
| hold sermon 2 | church | 24 | 53.4 | 57.0 | needs a church (build cost 80,553); thin at home: furniture |
| hold banquet 3 (fish) | mansion | 7.6 | 57.4 | 57.4 | thin at home: cured fish |
| hold banquet 3 (meat) | mansion | 7.6 | 57.6 | 57.6 |  |
| hold banquet 1 (fish) | mansion | 4.2 | 57.8 | 57.8 | thin at home: cured fish |
| hold banquet 2 (pies) | mansion | 7 | 57.8 | 57.8 | thin at home: pasties, wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 120102307 | 0.052 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0.04 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Rouhomme: nothing pays; crew 0.0; est +0 a turn; stock: furniture 1 @ 14.2 (keep 140); best orders clear only 3 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: furniture 1 @ 14.2 (keep 140); best orders clear only 3 a turn after crew: ship stays at 0
- best towns now: Corstoft +25, Clarfranche +18, Calange +15
- Corstoft would trade: furniture buy 1 @ 13.5, nets sell 7 @ 38.6; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~92 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Vauxvais | 204 | 0.05 | 0.40 (37/turn) | bread 151 (2.12->2.66), tools 16 (4.14->4.66), rope 1 (74->78.85), flax fibres 4 (4.54->5.08) | thread 19 (4.83->5.75), flax fibres 14 (5.88->6.35), pasties 2 (14.6->16.4), candles 1 (77.7->79) | +103 |
| Hanstein | 380 | 0.09 | 0.40 (37/turn) | tools 16 (4.14->4.73), charcoal 13 (1.69->2.83), timber 9 (6.25->8.07), nails 3 (5.51->6.22) | thread 37 (4.75->5.75), flax plants 38 (1.37->1.86), seeds 7 (1.89->2.94), pasties 2 (13.55->16.4) | +81 |
| Caillechâtel | 488 | 0.12 | 0.20 (18/turn) | rope 4 (74->77.42), light armour 1 (78.23->81.22), tools 6 (4.14->4.73), honey 1 (8.87->9.79) | thread 29 (4.43->5.75), flax plants 32 (1.33->1.86), flax fibres 11 (5.46->6.35), cloth 6 (7.35->8.05) | +77 |
| Rouhomme | 368 | 0.09 | 0.60 (55/turn) | bread 151 (2.12->2.68), beer 36 (2.82->3.42), tar 2 (9.71->11.4), tallow 1 (21.21->23.37) | candles 1 (72.45->79), blades 2 (14.7->15.86), lead bars 10 (12.08->12.35), pasties 2 (15.02->16.4) | +74 |
| Friedwerp | 684 | 0.17 | 0.10 (9/turn) | tools 16 (4.14->6.65), wrought iron 2 (13.33->22.61), nets 3 (35.2->38.38), wool 1 (7.3->8.41) | candles 1 (70.88->79), mouldboards 1 (38.85->43.7), casks 1 (4.87->5.32) | +74 |

**Best:** Vauxvais at about +103 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 35 @ min 3.54 | makes 28.0, uses 4.2, holds 215 (keeps 60): sells the surplus + 11/turn of the excess |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 12 = 7.7 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 17 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 15 @ min 20.8 | makes 3.3, uses 2.1, holds 196 (keeps 30): sells the surplus + 14/turn of the excess |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 0 @ 2.2, stop - |  | uses 438.2/turn (brewery 1, flax farm 1, household), makes 450.0, holds 0 |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 10 @ min 34.2 |  |
| pasties | 3 @ 17.2, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 4.9 turns |
| porterage | 22 @ 1.1, stop - |  | uses 22.4/turn (observed), makes 0.0, holds 7 = 0.3 turns |
| rope |  | 7 @ min 72.0 | makes 2.2, uses 0.0, holds 60 (keeps 0): sells the surplus + 5/turn of the excess |
| timber |  | 9 @ min 6.7 |  |
| tools | 3 @ 6.2, stop 22 |  | uses 2.7/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 73.9 turns |

## Chain sizing

Mode HOLD, garments sold 9.4/turn (+0.0 exported); plan makes 3.7 garments a turn.
Labour: own 450, everything else 440, chain may buy 350 -> chain allowance 360, chain plan 125 (+0 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 2.29 | 2.31 |
| ret | 3 | 0.41 | 0.41 |
| spin | 4 | 0.84 | 0.85 |
| weave | 3 | 0.12 | 0.13 |
| sew | 2 | 0.08 | 0.09 |

Buffers: flax fibres 57/48, thread 470/141, cloth 21/14

## Self-diagnosis

- R2: ropewalk 1 blocked by rope space: 60 held of 60 capacity, we make 2.2 a turn; no buy on it: add a sell order or more capacity for rope
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R4: quarry 1 projected 0 of 0.7 (limited by porterage)
