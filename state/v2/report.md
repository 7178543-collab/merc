# v2 shadow report

Turn 13324, 2026-10-16 13:11. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,319, prestige 3,214 (544 free, -4.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 267 | 0 | 4 | 0 | 0 | min_holding 60, sell 39, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 34 | 0 | 2 | 0 | 0 | min_holding 30, sell 22, sell @ 22 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 286 | 286 | 727 | 0 | 9 | buy 286, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 47 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 36 |
| porterage | 21 | 21 | 13 | 0 | 8 | buy 21, buy @ 1.1 |

**1 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.2 turns (holds 8, next step uses 46/turn) -> v2: check the step that makes it

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.7 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 72
- **flax plants**: flax plants buffer thin: 1.8 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 187

## Notes

- labour: projection runs 73 over real use lately; planning 727, not 801

## Prestige spending, cheapest coin per prestige first

1077 turns left: prestige gained now converts 99.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 52.8 | 52.8 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 57.4 | 57.4 | thin at home: wine, cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 57.6 | 57.6 | thin at home: hop beer, cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 59.0 | 59.0 | thin at home: cured fish |
| hold banquet 4 (pies) | mansion | 18 | 60.2 | 60.2 | thin at home: pasties, hop beer, wine |
| hold feast 2 | townhouse | 2.6 | 57.8 | 60.3 | needs a townhouse (build cost 7,016); thin at home: wine |
| hold banquet 3 (meat) | mansion | 7.6 | 60.4 | 60.4 | thin at home: hop beer |
| hold banquet 3 (pies) | mansion | 8 | 60.5 | 60.5 | thin at home: pasties, hop beer, pies |
| hold banquet 2 (meat) | mansion | 6.8 | 60.6 | 60.6 | thin at home: wine |
| hold sermon 2 (candles) | church | 31 | 58.1 | 60.7 | needs a church (build cost 80,042); thin at home: jewellery, candles, furniture |
| hold prayer 2 | chapel | 13 | 58.5 | 60.9 | needs a chapel (build cost 31,440); thin at home: furniture |
| hold sermon 2 | church | 24 | 58.4 | 61.7 | needs a church (build cost 80,042); thin at home: jewellery, furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 74001604 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Brunnham: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn; best orders clear only -2 a turn after crew: ship stays at 0
- best towns now: Bordetes +15
- Bordetes would trade: nets sell 4 @ 42.8; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~106 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Rouhomme | 368 | 0.10 | 0.90 (95/turn) | bread 136 (2.52->3.48), beer 41 (2.92->3.69), stockfish 1 (90.3->107.35), timber 20 (6.3->8.36) | tools 4 (4.91->5.2) | +140 |
| Karlmoor | 787 | 0.22 | 0.10 (11/turn) | acid 1 (110.25->160.55), stockfish 1 (90.3->117.8), wool 1 (5.83->7.98) | honey 3 (8.14->8.41) | +70 |
| Hofkirchen | 991 | 0.33 | 0.20 (21/turn) | acid 1 (110.25->142.5), flax plants 14 (1.37->3.89), stockfish 1 (90.3->108.3), wool 1 (5.83->7.79) | - | +70 |
| Essenbrucke | 584 | 0.17 | 0.10 (11/turn) | acid 1 (110.25->160.55), garments 13 (20.48->21.47), ploughs 1 (75.08->78.85), lead ore 1 (5.72->7.41) | pasties 1 (9.55->13.3), cloth 8 (8.24->8.45), tar 1 (10.13->10.5) | +64 |
| Cobholme | 1564 | 0.66 | 0.20 (21/turn) | flour 3 (21.21->34.96), acid 1 (110.25->130.15), glassware 1 (65.62->76), medicine 1 (118.65->127.3) | tar 1 (8.93->10.5) | +64 |

**Best:** Rouhomme at about +140 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 39 @ min 3.7 | makes 28.0, uses 4.2, holds 267 (keeps 60): sells the surplus + 15/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 22 @ min 22.0 |  |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 277 @ 2.2, stop - |  | uses 727.2/turn (brewery 1, flax farm 1, household), makes 450.0, holds 286 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 11 @ min 36.0 | makes 9.0, uses 0.0, holds 47 (keeps 15): sells the surplus + 2/turn of the excess |
| porterage | 13 @ 1.1, stop - |  | uses 12.5/turn (observed), makes 0.0, holds 21 = 1.7 turns |
| rope |  | 6 @ min 77.5 | makes 4.5, uses 0.0, holds 17 (keeps 0): sells the surplus + 1/turn of the excess |
| tar | 2 @ 11.0, stop 5 |  | uses 1.0/turn (ropewalk 1), makes 0.0, holds 10 = 9.4 turns |
| timber |  | 36 @ min 8.5 | makes 12.0, uses 0.0, holds 654 (keeps 350): sells the surplus + 24/turn of the excess |
| tools | 5 @ 6.2, stop 37 |  | uses 4.6/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 43.6 turns |

## Chain sizing

Mode HOLD, garments sold 6.3/turn (+0.0 exported); plan makes 22.1 garments a turn.
Labour: own 450, everything else 385, chain may buy 350 -> chain allowance 415, chain plan 415 (+0 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.85 | 6.06 |
| ret | 3 | 1.04 | 1.08 |
| spin | 4 | 2.14 | 2.22 |
| weave | 3 | 0.92 | 0.87 |
| sew | 2 | 0.58 | 0.54 |

Buffers: flax fibres 64/91, thread 549/269, cloth 8/87
- chain plan needed 537 labour, budget left 415: cut to 415 (sewing capped at 0.54)

## Self-diagnosis

- R1: candles slot dry: 0.0 held, 1.5 a turn (luxury slot (+3 prestige)); our buy paused by the failsafe, home ask 80.0 (held back: paused by the failsafe at level 1: un-pause only at level 0)
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 4 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
