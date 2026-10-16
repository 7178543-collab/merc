# v2 shadow report

Turn 13331, 2026-10-16 20:55. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,021, prestige 3,262 (592 free, +75.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 228 | 0 | 4 | 0 | 0 | min_holding 60, sell 37, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 33 | 0 | 2 | 0 | 0 | min_holding 30, sell 18, sell @ 22 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 286 | 286 | 726 | 0 | 10 | buy 286, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 70 | 0 | 0 | 0 | 0 | min_holding 15, sell 13, sell @ 36 |
| porterage | 13 | 21 | 13 | 0 | 8 | buy 13, buy @ 1.1 |

**1 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.1 turns (holds 4, next step uses 40/turn) -> v2: check the step that makes it

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax fibres**: flax fibres buffer thin: 1.6 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 78
- **flax plants**: flax plants buffer thin: 1.8 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 201

## Notes

- labour: projection runs 73 over real use lately; planning 726, not 790

## Prestige spending, cheapest coin per prestige first

1070 turns left: prestige gained now converts 99.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.5 | 49.5 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 55.8 | 55.8 | thin at home: wine, cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 56.4 | 56.4 | thin at home: hop beer, cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 57.3 | 57.3 | thin at home: cured fish |
| hold banquet 2 (meat) | mansion | 6.8 | 58.7 | 58.7 | thin at home: wine |
| hold banquet 3 (meat) | mansion | 7.6 | 59.0 | 59.0 | thin at home: hop beer |
| hold feast 2 | townhouse | 2.6 | 56.9 | 59.4 | needs a townhouse (build cost 6,872); thin at home: wine |
| hold banquet 4 (pies) | mansion | 18 | 60.0 | 60.0 | thin at home: hop beer, wine |
| hold banquet 3 (pies) | mansion | 8 | 60.1 | 60.1 | thin at home: pasties, hop beer, pies |
| hold banquet 2 (pies) | mansion | 7 | 60.9 | 60.9 | thin at home: pasties, wine, pies |
| hold banquet 1 (meat) | mansion | 4.2 | 61.5 | 61.5 |  |
| hold sermon 2 (candles) | church | 31 | 59.0 | 61.7 | needs a church (build cost 80,650); thin at home: jewellery, candles, furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 74001604 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Brunnham: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~100 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Rouhomme | 368 | 0.10 | 0.90 (90/turn) | bread 142 (2.39->3.12), tackles 1 (178.5->207.1), beer 37 (2.98->3.69), stockfish 1 (93.45->108.3) | flax plants 2 (0.98->2.34), tools 4 (4.91->5.15), tar 1 (9.71->10) | +159 |
| Hanbrücken | 531 | 0.14 | 0.10 (10/turn) | cloth 14 (8.98->15.2), garments 12 (23.6->24.89), medicine 1 (122.85->130.15), stockfish 1 (93.45->100.7) | fleece 4 (5.72->6.51), flax fibres 2 (5.57->6.7), wool 1 (8.4->10.54), flax plants 1 (1.83->2.34) | +121 |
| Karlmoor | 787 | 0.21 | 0.10 (10/turn) | tackles 1 (178.5->224.2), harnesses 1 (86.62->96.9), yarn 9 (3.57->4.27), resin 2 (2.46->3.55) | cloth 13 (8.29->8.55), garments 2 (23.1->23.8) | +59 |
| Hanstein | 380 | 0.10 | 0.10 (10/turn) | gears 1 (88.2->98.8), nets 2 (35.6->37.05), beer 37 (2.98->3.19) | flax fibres 32 (5.25->6.7), wool 1 (7.4->10.54), flax plants 3 (1.31->2.34), seeds 4 (1.85->2.32) | +58 |
| Brebronn | 862 | 0.25 | 0.30 (30/turn) | beer 37 (2.98->4.73), nets 1 (35.6->40.28), yarn 19 (3.57->4.05) | flax plants 1 (1.28->2.34), garments 2 (23.52->23.8) | +50 |

**Best:** Rouhomme at about +159 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 36 @ min 3.7 | makes 28.0, uses 4.2, holds 228 (keeps 60): sells the surplus + 12/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.1 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 18 @ min 22.0 |  |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 276 @ 2.2, stop - |  | uses 726.1/turn (brewery 1, flax farm 1, household), makes 450.0, holds 286 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 13 @ min 34.6 | makes 9.0, uses 0.0, holds 70 (keeps 15): sells the surplus + 4/turn of the excess |
| porterage | 11 @ 1.1, stop - |  | uses 11.1/turn (observed), makes 0.0, holds 13 = 1.2 turns |
| rope |  | 5 @ min 77.5 |  |
| tar | 2 @ 11.0, stop 5 |  | uses 1.0/turn (ropewalk 1), makes 0.0, holds 9 = 9.3 turns |
| timber |  | 32 @ min 6.7 | makes 8.4, uses 0.0, holds 639 (keeps 350): sells the surplus + 23/turn of the excess |
| tools | 5 @ 6.2, stop 38 |  | uses 4.7/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 42.0 turns |

## Chain sizing

Mode HOLD, garments sold 18.5/turn (+0.0 exported); plan makes 21.3 garments a turn.
Labour: own 450, everything else 376, chain may buy 350 -> chain allowance 424, chain plan 425 (+8 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 6.31 | 6.44 |
| ret | 3 | 1.12 | 1.14 |
| spin | 4 | 2.31 | 2.36 |
| weave | 3 | 0.80 | 0.82 |
| sew | 2 | 0.50 | 0.52 |

Buffers: flax fibres 62/90, thread 438/264, cloth 4/82
- chain plan needed 573 labour, budget left 424: cut to 424 (sewing capped at 0.52)

## Self-diagnosis

- R1: candles slot dry: 0.0 held, 1.5 a turn (luxury slot (+3 prestige)); our buy paused by the failsafe, home ask 81.5 (held back: paused by the failsafe at level 1: un-pause only at level 0)
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
