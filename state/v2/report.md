# v2 shadow report

Turn 13332, 2026-10-16 21:53. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,163, prestige 3,257 (587 free, +70.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 226 | 0 | 4 | 0 | 0 | min_holding 60, sell 36, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 5 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 34 | 0 | 2 | 0 | 0 | min_holding 30, sell 18, sell @ 22 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 286 | 286 | 725 | 0 | 11 | buy 286, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 65 | 0 | 0 | 0 | 0 | min_holding 15, sell 13, sell @ 34.6 |
| porterage | 11 | 13 | 11 | 0 | 2 | buy 11, buy @ 1.1 |

**1 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.1 turns (holds 2, next step uses 42/turn) -> v2: check the step that makes it

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.5 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 80
- **flax plants**: flax plants buffer thin: 1.8 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 201

## Notes

- labour: projection runs 73 over real use lately; planning 725, not 798

## Prestige spending, cheapest coin per prestige first

1069 turns left: prestige gained now converts 99.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.5 | 49.5 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 56.1 | 56.1 | thin at home: wine, cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 56.8 | 56.8 | thin at home: hop beer, cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 57.6 | 57.6 | thin at home: cured fish |
| hold banquet 2 (meat) | mansion | 6.8 | 58.0 | 58.0 | thin at home: wine |
| hold banquet 3 (meat) | mansion | 7.6 | 58.5 | 58.5 | thin at home: hop beer |
| hold feast 2 | townhouse | 2.6 | 57.3 | 59.9 | needs a townhouse (build cost 7,082); thin at home: wine |
| hold banquet 1 (meat) | mansion | 4.2 | 60.7 | 60.7 |  |
| hold prayer 2 | chapel | 13 | 58.2 | 60.7 | needs a chapel (build cost 33,050); thin at home: furniture |
| jousting 1 | arena | 170 | 60.5 | 60.7 | needs a arena (build cost 25,423); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 60.8 | 60.8 | thin at home: pasties, hop beer, pies |
| hold sermon 2 (candles) | church | 31 | 58.1 | 60.8 | needs a church (build cost 80,352); thin at home: jewellery, candles, furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 74001604 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Brunnham: nothing pays; crew 0.0; est +0 a turn; best orders clear only 0 a turn after crew: ship stays at 0
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~100 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Heidlowe | 662 | 0.18 | 0.30 (30/turn) | nets 11 (17.4->35.15), garments 17 (20.18->21.09), varnish 2 (18.17->21.28), slaked lime 2 (5.06->7.27) | wax 2 (22.05->23.75), flax fibres 22 (6.56->7), flax plants 58 (1.32->1.68) | +221 |
| Marmont | 638 | 0.17 | 0.10 (10/turn) | nets 9 (17.4->36.67), stockfish 1 (99.23->110.2), garments 16 (20.18->20.9), ploughs 1 (74.03->78.38) | flax fibres 4 (5.57->7), wool 1 (9.08->9.36) | +197 |
| Caillechâtel | 488 | 0.13 | 0.20 (20/turn) | nets 6 (17.4->36.29), beer 36 (2.98->3.5), stockfish 1 (99.23->107.35), canvas 1 (31.71->33.06) | flax fibres 10 (5.12->7), rope 1 (69.83->75.05), flax plants 26 (1.31->1.68), cloth 8 (8.35->8.7) | +157 |
| Rouhomme | 368 | 0.10 | 0.90 (90/turn) | bread 143 (2.39->3.12), beer 37 (2.98->3.72), thread 19 (5.2->6.08), garments 19 (20.18->20.9) | flax fibres 1 (5.67->7), flax plants 2 (0.92->1.68), tar 1 (9.61->9.9), tools 3 (4.91->5.15) | +135 |
| Donaunieder | 985 | 0.31 | 0.20 (20/turn) | tackles 2 (177.45->212.8), nets 2 (17.4->38.38), wrought iron 6 (13.55->16.72), medicine 1 (122.85->127.3) | flax fibres 1 (5.51->7) | +128 |

**Best:** Heidlowe at about +221 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 36 @ min 3.7 | makes 28.0, uses 4.2, holds 226 (keeps 60): sells the surplus + 12/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 19 @ min 22.0 |  |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 275 @ 2.2, stop - |  | uses 725.2/turn (brewery 1, flax farm 1, household), makes 450.0, holds 286 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 12 @ min 34.0 | makes 9.0, uses 0.0, holds 65 (keeps 15): sells the surplus + 3/turn of the excess |
| porterage | 11 @ 1.1, stop - |  | uses 11.2/turn (observed), makes 0.0, holds 11 = 1.0 turns |
| rope |  | 5 @ min 77.0 |  |
| tar | 2 @ 11.0, stop 5 |  | uses 1.0/turn (ropewalk 1), makes 0.0, holds 9 = 9.3 turns |
| timber |  | 31 @ min 6.7 | makes 8.4, uses 0.0, holds 628 (keeps 350): sells the surplus + 22/turn of the excess |
| tools | 4 @ 6.2, stop 32 |  | uses 4.0/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 49.9 turns |

## Chain sizing

Mode HOLD, garments sold 20.0/turn (+0.0 exported); plan makes 20.9 garments a turn.
Labour: own 450, everything else 376, chain may buy 350 -> chain allowance 424, chain plan 424 (+1 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 6.44 | 6.46 |
| ret | 3 | 1.12 | 1.15 |
| spin | 4 | 2.36 | 2.36 |
| weave | 3 | 0.80 | 0.82 |
| sew | 2 | 0.52 | 0.51 |

Buffers: flax fibres 61/90, thread 430/264, cloth 2/82
- chain plan needed 575 labour, budget left 424: cut to 424 (sewing capped at 0.51)

## Self-diagnosis

- R1: candles slot dry: 0.0 held, 1.5 a turn (luxury slot (+3 prestige)); our buy paused by the failsafe, home ask 81.5 (held back: paused by the failsafe at level 1: un-pause only at level 0)
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
