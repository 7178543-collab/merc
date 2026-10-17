# v2 shadow report

Turn 13356, 2026-10-17 21:48. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 8,781, prestige 3,276 (606 free, -1.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 153 | 0 | 4 | 0 | 0 | min_holding 60, sell 29, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 122 | 0 | 2 | 0 | 0 | min_holding 30, sell 29, sell @ 22 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 301 | 301 | 713 | 0 | 38 | buy 301, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 15 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 37.8 |
| porterage | 11 | 11 | 10 | 0 | 1 | buy 11, buy @ 1.1 |

**1 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.8 turns (holds 37, next step uses 46/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **labour**: 38 labour expired last turn (~66 coin): holding 301 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.7 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 70
- **grain**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 73 over real use lately; planning 713, not 776
- labour expiry guard: 38 bought labour expired last turn, buy 263 (not 263) this turn

## Prestige spending, cheapest coin per prestige first

1045 turns left: prestige gained now converts 99.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.3 | 51.3 | running |
| hold banquet 2 (meat) | mansion | 6.8 | 57.8 | 57.8 | thin at home: wine |
| hold banquet 3 (meat) | mansion | 7.6 | 58.1 | 58.1 |  |
| hold banquet 1 (meat) | mansion | 4.2 | 58.6 | 58.6 |  |
| hold prayer 2 | chapel | 13 | 56.4 | 58.9 | needs a chapel (build cost 32,076); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 56.4 | 59.1 | needs a church (build cost 78,913); thin at home: jewellery, candles, furniture |
| jousting 1 | arena | 170 | 58.9 | 59.1 | needs a arena (build cost 24,838); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 59.5 | 59.5 | thin at home: wine, cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 59.6 | 59.6 | thin at home: cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 59.9 | 59.9 |  |
| hold sermon 2 | church | 24 | 57.1 | 60.6 | needs a church (build cost 78,913); thin at home: jewellery, furniture |
| hold feast 2 | townhouse | 2.6 | 58.5 | 61.5 | needs a townhouse (build cost 7,950); thin at home: wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.20 | 20 | 64601365 | 0.12 | garments 30 | - | 524 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Disscester: garments sell 29 @ 28.6; crew 0.2; est +167 a turn
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn
- best towns now: Disscester +167, Caillechâtel +43, Cobholme +22, Coburgbaum +16
- Disscester would trade: garments sell 29 @ 28.6; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~102 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Disscester | 1474 | 0.59 | 0.30 (31/turn) | garments 29 (19.85->35.72), cloth 5 (7.4->9.03), stockfish 2 (119.7->123.5) | ploughs 1 (43.05->70.77) | +472 |
| Rouhomme | 368 | 0.10 | 0.20 (20/turn) | beer 31 (2.92->3.8), limestone 1 (15.33->28.31), salt 7 (4.18->5.37), wheels 2 (17.12->20.33) | spinning wheels 1 (216.3->266), jewellery 2 (78.75->85.5), bricks 1 (8.51->14.82), dyed yarn 1 (6.35->9.45) | +124 |
| Caillechâtel | 488 | 0.13 | 0.30 (31/turn) | beer 18 (2.92->7.6), tools 10 (4.5->5.13), garments 10 (19.85->20.14) | bricks 1 (5.35->14.82), spinning wheels 1 (264.6->266), grain 79 (2.52->2.79) | +94 |
| Hanstein | 380 | 0.10 | 0.40 (41/turn) | tar 4 (9.97->11.11), paper 1 (21.42->22.42) | thread 95 (4.68->5.45), mouldboards 1 (30.03->39.71), bricks 1 (4.91->14.82), seeds 10 (1.8->2.32) | +86 |
| Friedwerp | 684 | 0.19 | 0.20 (20/turn) | beer 31 (2.92->4.2), salt 6 (4.18->5.89), casks 5 (5.93->7.74), rope 1 (75.5->79.33) | cheese 14 (5.67->6.6), bricks 1 (6.25->14.82), cloth 16 (7.77->8.3), mouldboards 1 (37.59->39.71) | +73 |

**Best:** Disscester at about +472 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 30 @ min 3.7 | makes 28.0, uses 4.2, holds 153 (keeps 60): sells the surplus + 6/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.1 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 28 @ min 22.0 | makes 23.8, uses 2.1, holds 122 (keeps 30): sells the surplus + 6/turn of the excess |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 263 @ 2.2, stop - |  | uses 712.6/turn (brewery 1, flax farm 1, household), makes 450.0, holds 301 = 1.1 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 37.8 |  |
| porterage | 10 @ 1.1, stop - |  | uses 10.4/turn (observed), makes 0.0, holds 11 = 1.1 turns |
| rope |  | 7 @ min 73.5 | makes 2.2, uses 0.0, holds 60 (keeps 0): sells the surplus + 5/turn of the excess |
| timber |  | 19 @ min 7.3 | makes 8.4, uses 0.0, holds 489 (keeps 350): sells the surplus + 11/turn of the excess |
| tools | 4 @ 6.2, stop 30 |  | uses 3.8/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 53.1 turns |

## Chain sizing

Mode HOLD, garments sold 12.1/turn (+0.0 exported); plan makes 27.9 garments a turn.
Labour: own 450, everything else 362, chain may buy 350 -> chain allowance 438, chain plan 438 (+19 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.63 | 5.71 |
| ret | 3 | 1.00 | 1.02 |
| spin | 4 | 2.06 | 2.09 |
| weave | 3 | 1.08 | 1.09 |
| sew | 2 | 0.58 | 0.68 |

Buffers: flax fibres 58/80, thread 399/236, cloth 37/109
- chain plan needed 442 labour, budget left 438: cut to 438 (sewing capped at 0.68)

## Self-diagnosis

- R1: prestige rate -1.29 a turn vs 12-turn median +2.92; likely: no slot, building or contract cause found: check the impacts
- R2: ropewalk 1 blocked by rope space: 60 held of 60 capacity, we make 2.2 a turn; no buy on it: add a sell order or more capacity for rope
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
