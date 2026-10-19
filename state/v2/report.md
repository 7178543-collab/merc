# v2 shadow report

Turn 13393, 2026-10-19 10:02. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 5,307, prestige 3,382 (712 free, -0.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 253 | 0 | 4 | 0 | 0 | min_holding 60, sell 39, sell @ 3.54 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 17 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 187 | 0 | 2 | 0 | 0 | min_holding 30, sell 14, sell @ 20.8 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 0 | 0 | 415 | 0 | 35 | buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 25 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34.6 |
| porterage | 7 | 7 | 7 | 30 | 0 | buy 7, buy @ 1.1 |

**2 risks, 0 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **porterage**: logging camp w/ tool, quarry 1 ran short of porterage (buy is live (7 @ 1.1), 7 bought last turn); labour need rises ~172/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **porterage**: buying 7, short of ~37 needed -> v2: buy 37

## Notes

- labour: projection runs 113 over real use lately; planning 437, not 550

## Prestige spending, cheapest coin per prestige first

1008 turns left: prestige gained now converts 99.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 45.9 | 45.9 | running |
| hold prayer 2 | chapel | 13 | 52.7 | 55.2 | needs a chapel (build cost 31,304); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 52.6 | 55.4 | needs a church (build cost 79,762); thin at home: candles, furniture |
| hold feast 2 | townhouse | 2.6 | 52.9 | 55.5 | needs a townhouse (build cost 6,556); thin at home: wine |
| hold banquet 2 (fish) | mansion | 6.8 | 55.8 | 55.8 | thin at home: wine, cured fish |
| hold banquet 2 (meat) | mansion | 6.8 | 56.2 | 56.2 | thin at home: wine |
| hold sermon 2 | church | 24 | 53.3 | 56.9 | needs a church (build cost 79,762); thin at home: furniture |
| hold banquet 3 (fish) | mansion | 7.6 | 57.3 | 57.3 | thin at home: cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 57.7 | 57.7 | thin at home: cured fish |
| hold banquet 3 (meat) | mansion | 7.6 | 57.7 | 57.7 |  |
| hold banquet 2 (pies) | mansion | 7 | 58.7 | 58.7 | thin at home: pasties, wine, candles |
| hold banquet 3 (pies) | mansion | 8 | 58.7 | 58.7 | thin at home: pasties, candles |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 9 | 120102307 | 0.328 | beer 41 | furniture 1 | 24 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Rouhomme: beer sell 39 @ 3.54, furniture buy 1 @ 14.2; crew 0.1; est +21 a turn; stock: furniture 1 @ 14.2 (keep 140)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: furniture 1 @ 14.2 (keep 140); best orders clear only 3 a turn after crew: ship stays at 0
- best towns now: Disscester +36, Chatgnan +26, Bordetes +24, Chribruck +24, Caillechâtel +23
- Disscester would trade: furniture buy 1 @ 13.7, garments sell 14 @ 21.8, rope sell 1 @ 85.0; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~93 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Rouhomme | 368 | 0.09 | 0.60 (56/turn) | bread 151 (2.09->2.81), beer 39 (2.78->3.42), thread 9 (5.5->6.27), tar 3 (9.82->11.4) | pasties 2 (14.6->18.8), lead bars 11 (12.08->12.82), blades 2 (14.7->16.34), bricks 1 (5.15->7.98) | +122 |
| Vauxvais | 204 | 0.05 | 0.30 (28/turn) | bread 151 (2.09->2.66), flax fibres 4 (4.51->4.99), grain 4 (2.38->2.83) | thread 18 (4.83->5.75), pasties 2 (14.6->18.8), flax fibres 14 (5.57->6.2), beer 4 (3.19->3.5) | +101 |
| Hanstein | 380 | 0.10 | 0.20 (19/turn) | beer 39 (2.78->3), flax fibres 4 (4.51->4.84), paper 2 (21.42->21.85), grain 4 (2.38->2.64) | thread 64 (4.77->5.75), pasties 2 (13.65->18.8), flax fibres 14 (5.46->6.2), flax plants 36 (1.4->1.81) | +87 |
| Heidlowe | 662 | 0.17 | 0.30 (28/turn) | seeds 8 (1.92->3.32), paper 1 (21.42->23.56), cloth 1 (7.1->8.17), flax fibres 4 (4.51->5.03) | thread 64 (4.68->5.75), pasties 2 (13.65->18.8), flax plants 36 (1.4->1.81), yarn 3 (4.96->5.37) | +84 |
| Heilegg | 826 | 0.21 | 0.10 (9/turn) | casks 13 (5.51->9.17), paper 3 (21.42->23.37), nets 7 (35.6->36.1), nails 1 (5.83->6.17) | pasties 2 (14.6->18.8), thread 19 (5.25->5.75), blades 2 (15.75->16.34), garments 2 (20.06->20.6) | +63 |

**Best:** Rouhomme at about +122 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 26.0, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 38 @ min 3.54 | makes 28.0, uses 4.2, holds 253 (keeps 60): sells the surplus + 14/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 17 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 14 @ min 20.8 | makes 3.3, uses 2.1, holds 187 (keeps 30): sells the surplus + 13/turn of the excess |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 0 @ 2.2, stop - |  | uses 436.9/turn (brewery 1, flax farm 1, household), makes 450.0, holds 0 |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 34.6 |  |
| pasties | 3 @ 19.7, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 4.9 turns |
| porterage | 37 @ 1.1, stop - |  | uses 36.8/turn (observed), makes 0.0, holds 7 = 0.2 turns |
| rope |  | 6 @ min 74.0 | makes 2.2, uses 0.0, holds 50 (keeps 0): sells the surplus + 4/turn of the excess |
| tools | 3 @ 6.2, stop 22 |  | uses 2.6/turn (retting pit 1), makes 0.0, holds 199 = 75.6 turns |

## Chain sizing

Mode HOLD, garments sold 9.6/turn (+0.0 exported); plan makes 3.7 garments a turn.
Labour: own 450, everything else 512, chain may buy 350 -> chain allowance 350, chain plan 129 (+5 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 2.29 | 2.40 |
| ret | 3 | 0.41 | 0.43 |
| spin | 4 | 0.84 | 0.88 |
| weave | 3 | 0.12 | 0.13 |
| sew | 2 | 0.08 | 0.09 |

Buffers: flax fibres 57/48, thread 454/141, cloth 19/14

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R4: quarry 1 projected 0 of 1 (limited by porterage)
