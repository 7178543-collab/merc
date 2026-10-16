# v2 shadow report

Turn 13326, 2026-10-16 15:57. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,877, prestige 3,206 (536 free, -3.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 254 | 0 | 4 | 0 | 0 | min_holding 60, sell 38, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 32 | 0 | 2 | 0 | 0 | min_holding 30, sell 20, sell @ 22 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 286 | 286 | 727 | 0 | 9 | buy 286, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 50 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 36 |
| porterage | 21 | 21 | 13 | 0 | 8 | buy 21, buy @ 1.1 |

**1 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.2 turns (holds 9, next step uses 43/turn) -> v2: check the step that makes it

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.7 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 75
- **flax plants**: flax plants buffer thin: 1.8 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 194

## Notes

- labour: projection runs 73 over real use lately; planning 727, not 800

## Prestige spending, cheapest coin per prestige first

1075 turns left: prestige gained now converts 99.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 52.2 | 52.2 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 56.3 | 56.3 | thin at home: wine, cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 56.5 | 56.5 | thin at home: hop beer, cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 58.1 | 58.1 | thin at home: cured fish |
| hold banquet 3 (meat) | mansion | 7.6 | 60.0 | 60.0 | thin at home: hop beer |
| hold banquet 2 (meat) | mansion | 6.8 | 60.2 | 60.2 | thin at home: wine |
| hold feast 2 | townhouse | 2.6 | 57.6 | 60.2 | needs a townhouse (build cost 7,094); thin at home: wine |
| hold banquet 3 (pies) | mansion | 8 | 60.3 | 60.3 | thin at home: pasties, hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 60.9 | 60.9 | thin at home: pasties, hop beer, wine, stockfish |
| hold sermon 2 (candles) | church | 31 | 58.3 | 61.0 | needs a church (build cost 83,723); thin at home: jewellery, candles, furniture |
| hold prayer 2 | chapel | 13 | 58.8 | 61.4 | needs a chapel (build cost 33,570); thin at home: furniture |
| hold banquet 2 (pies) | mansion | 7 | 61.7 | 61.7 | thin at home: pasties, wine, pies |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 74001604 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Brunnham: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn; best orders clear only -4 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~105 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Rouhomme | 368 | 0.10 | 0.60 (63/turn) | bread 138 (2.52->3.31), beer 39 (2.95->3.72), tackles 1 (179.55->190), garments 20 (20.64->20.9) | flax plants 10 (1.08->1.5), tools 4 (4.91->5.2) | +100 |
| Toqueque | 642 | 0.18 | 0.10 (11/turn) | tackles 1 (179.55->228), acid 1 (122.85->140.6), hop beer 1 (9.29->14.91), nets 2 (35.8->37.81) | - | +68 |
| Clairas | 374 | 0.10 | 0.10 (11/turn) | acid 1 (122.85->158.65), tools 12 (4.46->5.03), nets 2 (35.8->36.48), wrought iron 1 (11.9->12.73) | bellows 1 (247.8->260.3), soap 1 (71.92->82.65) | +59 |
| Bordetes | 831 | 0.24 | 0.20 (21/turn) | cheese 25 (6.51->7.79), salt 2 (4.2->6.74), canvas 1 (32.55->34.58), bricks 1 (6.1->11.69) | bellows 1 (247.8->260.3), garments 2 (22.05->23.2) | +42 |
| Nürnnieder | 520 | 0.15 | 0.10 (11/turn) | acid 1 (122.85->153.9), garments 20 (20.64->21.28), bricks 1 (6.1->9.5), wrought iron 1 (11.9->12.16) | thread 24 (4.7->4.9) | +41 |

**Best:** Rouhomme at about +100 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 38 @ min 3.7 | makes 28.0, uses 4.2, holds 254 (keeps 60): sells the surplus + 14/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.1 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 20 @ min 22.0 |  |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 277 @ 2.2, stop - |  | uses 726.8/turn (brewery 1, flax farm 1, household), makes 450.0, holds 286 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 11 @ min 36.0 | makes 9.0, uses 0.0, holds 50 (keeps 15): sells the surplus + 2/turn of the excess |
| porterage | 13 @ 1.1, stop - |  | uses 12.7/turn (observed), makes 0.0, holds 21 = 1.6 turns |
| rope |  | 6 @ min 77.5 | makes 4.5, uses 0.0, holds 18 (keeps 0): sells the surplus + 1/turn of the excess |
| tar | 2 @ 11.0, stop 5 |  | uses 1.0/turn (ropewalk 1), makes 0.0, holds 10 = 9.4 turns |
| timber |  | 35 @ min 8.5 | makes 12.0, uses 0.0, holds 640 (keeps 350): sells the surplus + 23/turn of the excess |
| tools | 5 @ 6.2, stop 38 |  | uses 4.7/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 42.8 turns |

## Chain sizing

Mode HOLD, garments sold 11.8/turn (+0.0 exported); plan makes 21.7 garments a turn.
Labour: own 450, everything else 385, chain may buy 350 -> chain allowance 415, chain plan 415 (+1 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 6.06 | 6.16 |
| ret | 3 | 1.08 | 1.09 |
| spin | 4 | 2.22 | 2.25 |
| weave | 3 | 0.87 | 0.84 |
| sew | 2 | 0.54 | 0.53 |

Buffers: flax fibres 64/91, thread 512/266, cloth 9/84
- chain plan needed 553 labour, budget left 415: cut to 415 (sewing capped at 0.53)

## Self-diagnosis

- R1: candles slot dry: 0.0 held, 1.5 a turn (luxury slot (+3 prestige)); our buy paused by the failsafe, home ask 80.0 (held back: paused by the failsafe at level 1: un-pause only at level 0)
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
