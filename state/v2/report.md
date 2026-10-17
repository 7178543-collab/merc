# v2 shadow report

Turn 13349, 2026-10-17 14:49. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,883, prestige 3,277 (607 free, +2.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 126 | 0 | 19 | 0 | 0 | min_holding 60, sell 14, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 61 | 0 | 2 | 0 | 0 | min_holding 30, sell 23, sell @ 22 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 281 | 290 | 726 | 0 | 14 | buy 281, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 15 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 36.2 |
| porterage | 10 | 11 | 10 | 0 | 1 | buy 10, buy @ 1.1 |

**1 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.5 turns (holds 24, next step uses 50/turn) -> v2: check the step that makes it

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.7 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 65

## Notes

- labour: projection runs 73 over real use lately; planning 726, not 799

## Prestige spending, cheapest coin per prestige first

1052 turns left: prestige gained now converts 99.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.1 | 50.1 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 59.0 | 59.0 | thin at home: wine, cured fish |
| hold prayer 2 | chapel | 13 | 56.5 | 59.1 | needs a chapel (build cost 33,596); thin at home: furniture |
| hold banquet 3 (fish) | mansion | 7.6 | 59.3 | 59.3 | thin at home: cured fish |
| hold sermon 2 (candles) | church | 31 | 57.2 | 59.9 | needs a church (build cost 80,917); thin at home: jewellery, candles, furniture |
| hold banquet 2 (meat) | mansion | 6.8 | 60.3 | 60.3 | thin at home: wine |
| hold banquet 3 (meat) | mansion | 7.6 | 60.5 | 60.5 |  |
| hold sermon 2 | church | 24 | 57.0 | 60.5 | needs a church (build cost 80,917); thin at home: jewellery, furniture |
| hold feast 2 | townhouse | 2.6 | 58.2 | 61.6 | needs a townhouse (build cost 8,918); thin at home: wine |
| hold mass 2 (premium) | cathedral | 360 | 61.8 | 62.9 | needs a cathedral (build cost 356,171); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 4 (pies) | mansion | 18 | 63.4 | 63.4 | thin at home: wine |
| hold mass 1 | cathedral | 180 | 61.5 | 63.6 | needs a cathedral (build cost 356,171); thin at home: jewellery, glassware, candles |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 110801910 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | cured meat 5 | -108 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Karlmoor: candles buy 1 @ 72.5, cured meat buy 4 @ 21.2, rope sell 1 @ 84.5; crew 0.1; est +17 a turn
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn; best orders clear only -2 a turn after crew: ship stays at 0
- best towns now: Clairas +24, Neuborn +22, Hofkirchen +19, Karlmoor +17
- Clairas would trade: candles buy 1 @ 76.5, grain buy 13 @ 2.54, rope sell 2 @ 85.5; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~101 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Karlmoor | 787 | 0.21 | 0.20 (20/turn) | nets 3 (37.2->49.88), stockfish 1 (113.4->133), tackles 1 (169.05->186.2), rope 1 (75->84.08) | beer 19 (3.89->5.8), candles 1 (75.08->81.5), tar 3 (9.24->11.4), cheese 4 (6.04->7.12) | +126 |
| Heilegg | 826 | 0.23 | 0.20 (20/turn) | tackles 3 (169.05->190), beer 14 (2.89->3.88) | cheese 18 (5.46->7.12), beer 19 (4.3->5.8), candles 1 (76.65->81.5), acid 1 (131.25->134.9) | +123 |
| Hofkirchen | 991 | 0.32 | 0.50 (50/turn) | tackles 1 (169.05->185.25), thread 8 (4.66->5.13) | beer 19 (3.28->5.8), cheese 18 (5.72->7.12), cured meat 6 (21->23.2), candles 1 (73.5->81.5) | +104 |
| Birkeningen | 1006 | 0.33 | 0.20 (20/turn) | tackles 1 (169.05->190), garments 14 (19.52->20.71), rope 2 (75->79.33), slaked lime 1 (6.25->7.79) | beer 19 (3.4->5.8), cheese 15 (5.21->7.12), candles 1 (74.03->81.5) | +104 |
| Friedwerp | 684 | 0.18 | 0.20 (20/turn) | garments 15 (19.52->20.71), rope 1 (75->78.38) | beer 19 (3.7->5.8), cheese 18 (5.67->7.12), thread 9 (3.55->4.72), candles 1 (75.6->81.5) | +102 |

**Best:** Karlmoor at about +126 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 30.4, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 5.0 turns |
| beer |  | 14 @ min 3.7 | makes 28.0, uses 19.2, holds 126 (keeps 60): sells the surplus + 5/turn of the excess |
| cured meat | 11 @ 24.2, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 15 = 2.5 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 24 @ min 22.0 |  |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 276 @ 2.2, stop - |  | uses 726.2/turn (brewery 1, flax farm 1, household), makes 450.0, holds 281 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 36.2 |  |
| porterage | 10 @ 1.1, stop - |  | uses 10.0/turn (observed), makes 0.0, holds 10 = 1.0 turns |
| rope |  | 6 @ min 73.0 | makes 2.2, uses 0.0, holds 50 (keeps 0): sells the surplus + 4/turn of the excess |
| timber |  | 27 @ min 6.7 | makes 8.4, uses 0.0, holds 584 (keeps 350): sells the surplus + 19/turn of the excess |
| tools | 4 @ 6.2, stop 30 |  | uses 3.6/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 55.0 turns |

## Chain sizing

Mode HOLD, garments sold 13.9/turn (+0.0 exported); plan makes 25.0 garments a turn.
Labour: own 450, everything else 397, chain may buy 350 -> chain allowance 403, chain plan 403 (+2 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.30 | 5.36 |
| ret | 3 | 0.94 | 0.95 |
| spin | 4 | 1.94 | 1.96 |
| weave | 3 | 0.99 | 0.98 |
| sew | 2 | 0.62 | 0.61 |

Buffers: flax fibres 57/76, thread 397/225, cloth 24/98
- chain plan needed 483 labour, budget left 403: cut to 403 (sewing capped at 0.61)

## Self-diagnosis

- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
