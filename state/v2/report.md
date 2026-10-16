# v2 shadow report

Turn 13325, 2026-10-16 14:02. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,743, prestige 3,210 (540 free, -4.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 258 | 0 | 4 | 0 | 0 | min_holding 60, sell 39, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 17 | 5 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 32 | 0 | 2 | 0 | 0 | min_holding 30, sell 22, sell @ 22 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 286 | 286 | 727 | 0 | 9 | buy 286, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 46 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 36 |
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

1076 turns left: prestige gained now converts 99.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 53.1 | 53.1 | running |
| hold banquet 3 (fish) | mansion | 7.6 | 59.3 | 59.3 | thin at home: hop beer, cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 59.4 | 59.4 | thin at home: wine, cured fish |
| jousting 1 | arena | 170 | 59.4 | 59.5 | needs a arena (build cost 25,482); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 60.4 | 60.4 | thin at home: cured fish |
| hold feast 2 | townhouse | 2.6 | 57.8 | 60.6 | needs a townhouse (build cost 7,574); thin at home: wine |
| hold sermon 2 (candles) | church | 31 | 58.1 | 60.8 | needs a church (build cost 80,561); thin at home: jewellery, candles, furniture |
| hold banquet 3 (pies) | mansion | 8 | 60.9 | 60.9 | thin at home: pasties, hop beer, pies |
| hold prayer 2 | chapel | 13 | 58.5 | 61.0 | needs a chapel (build cost 32,332); thin at home: furniture |
| hold banquet 3 (meat) | mansion | 7.6 | 61.1 | 61.1 | thin at home: hop beer |
| hold banquet 2 (meat) | mansion | 6.8 | 61.5 | 61.5 | thin at home: wine |
| hold sermon 2 | church | 24 | 58.4 | 61.8 | needs a church (build cost 80,561); thin at home: jewellery, furniture |

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
| Rouhomme | 368 | 0.10 | 0.90 (95/turn) | bread 136 (2.52->3.48), beer 40 (2.93->3.69), stockfish 1 (90.3->107.35), timber 20 (6.3->8.36) | tools 4 (4.91->5.2) | +136 |
| Karlmoor | 787 | 0.22 | 0.10 (11/turn) | acid 1 (110.25->160.55), stockfish 1 (90.3->117.8), wool 1 (5.83->7.98) | honey 3 (8.14->8.41) | +70 |
| Hofkirchen | 991 | 0.34 | 0.20 (21/turn) | acid 1 (110.25->142.5), flax plants 14 (1.37->3.89), stockfish 1 (90.3->108.3), wool 1 (5.83->7.79) | - | +70 |
| Cobholme | 1564 | 0.66 | 0.20 (21/turn) | flour 3 (21.21->34.96), acid 1 (110.25->130.15), glassware 1 (65.62->76), medicine 1 (118.65->127.3) | tar 1 (8.93->10.5) | +64 |
| Essenbrucke | 584 | 0.17 | 0.10 (11/turn) | acid 1 (110.25->160.55), garments 13 (20.57->21.47), ploughs 1 (75.08->78.85), lead ore 1 (5.72->7.41) | pasties 1 (9.55->13.3), cloth 8 (8.24->8.45), tar 1 (10.13->10.5) | +64 |

**Best:** Rouhomme at about +136 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 38 @ min 3.7 | makes 28.0, uses 4.2, holds 258 (keeps 60): sells the surplus + 14/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 17 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 20 @ min 22.0 |  |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 277 @ 2.2, stop - |  | uses 726.8/turn (brewery 1, flax farm 1, household), makes 450.0, holds 286 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 11 @ min 36.0 | makes 9.0, uses 0.0, holds 46 (keeps 15): sells the surplus + 2/turn of the excess |
| porterage | 13 @ 1.1, stop - |  | uses 12.7/turn (observed), makes 0.0, holds 21 = 1.6 turns |
| rope |  | 6 @ min 77.5 | makes 4.5, uses 0.0, holds 18 (keeps 0): sells the surplus + 1/turn of the excess |
| tar | 2 @ 11.0, stop 5 |  | uses 1.0/turn (ropewalk 1), makes 0.0, holds 10 = 9.4 turns |
| timber |  | 36 @ min 8.5 | makes 12.0, uses 0.0, holds 646 (keeps 350): sells the surplus + 24/turn of the excess |
| tools | 5 @ 6.2, stop 38 |  | uses 4.7/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 42.7 turns |

## Chain sizing

Mode HOLD, garments sold 8.2/turn (+0.0 exported); plan makes 21.7 garments a turn.
Labour: own 450, everything else 385, chain may buy 350 -> chain allowance 415, chain plan 414 (+1 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 6.06 | 6.11 |
| ret | 3 | 1.08 | 1.09 |
| spin | 4 | 2.22 | 2.24 |
| weave | 3 | 0.87 | 0.85 |
| sew | 2 | 0.54 | 0.53 |

Buffers: flax fibres 64/91, thread 530/267, cloth 9/85
- chain plan needed 545 labour, budget left 415: cut to 415 (sewing capped at 0.53)

## Self-diagnosis

- R1: candles slot dry: 0.0 held, 1.5 a turn (luxury slot (+3 prestige)); our buy paused by the failsafe, home ask 80.0 (held back: paused by the failsafe at level 1: un-pause only at level 0)
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 5 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
