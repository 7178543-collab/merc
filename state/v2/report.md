# v2 shadow report

Turn 13342, 2026-10-17 07:05. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,532, prestige 3,256 (586 free, +3.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 174 | 0 | 19 | 0 | 0 | min_holding 60, sell 18, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 5 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 14, sell @ 22 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 271 | 271 | 721 | 0 | 0 | buy 271, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 33 | 0 | 0 | 0 | 0 | min_holding 15, sell 10, sell @ 34.6 |
| porterage | 11 | 11 | 11 | 0 | 0 | buy 11, buy @ 1.1 |

**1 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.7 turns (holds 21, next step uses 31/turn) -> v2: check the step that makes it

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.5 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 76
- **flax plants**: flax plants buffer thin: 1.9 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 198

## Notes

- labour: projection runs 74 over real use lately; planning 721, not 794

## Prestige spending, cheapest coin per prestige first

1059 turns left: prestige gained now converts 99.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.6 | 48.6 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 56.8 | 56.8 | thin at home: wine, cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 57.5 | 57.5 | thin at home: cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 57.9 | 57.9 | thin at home: cured fish |
| hold banquet 2 (meat) | mansion | 6.8 | 57.9 | 57.9 | thin at home: wine |
| hold banquet 3 (meat) | mansion | 7.6 | 58.4 | 58.4 |  |
| hold prayer 2 | chapel | 13 | 56.5 | 58.7 | needs a chapel (build cost 29,286); thin at home: furniture |
| jousting 1 | arena | 170 | 59.1 | 59.3 | needs a arena (build cost 23,018); thin at home: protection, light armour, arms; needs weaponry skill |
| hold sermon 2 (candles) | church | 31 | 57.1 | 59.6 | needs a church (build cost 75,472); thin at home: jewellery, candles, furniture |
| hold banquet 1 (meat) | mansion | 4.2 | 59.9 | 59.9 | running |
| hold sermon 2 | church | 24 | 56.8 | 60.0 | needs a church (build cost 75,472); thin at home: jewellery, furniture |
| hold feast 2 | townhouse | 2.6 | 58.2 | 60.8 | needs a townhouse (build cost 6,818); thin at home: wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 74001604 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | cured meat 5 | -108 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Brunnham: nothing pays; crew 0.0; est +0 a turn; best orders clear only 5 a turn after crew: ship stays at 0
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn; best orders clear only -2 a turn after crew: ship stays at 0
- best towns now: Karlmoor +60, Orlesailles +18
- Karlmoor would trade: candles buy 1 @ 72.5, nets sell 9 @ 43.0; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~98 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Karlmoor | 787 | 0.21 | 0.10 (10/turn) | nets 9 (36->45.41), garments 13 (19.5->21.47), tools 15 (4.5->5.98), fleece 1 (6.2->7.31) | candles 1 (75.08->81), pasties 1 (5.46->11.97) | +136 |
| Fontaux | 411 | 0.11 | 0.20 (20/turn) | garments 13 (19.5->20.9), gears 1 (88.2->92.15), tools 15 (4.5->4.73), lead bars 8 (11.87->12.06) | spinning wheels 1 (216.3->243.2), flax plants 13 (0.88->1.79), thread 65 (5.46->5.7), candles 1 (77.7->81) | +72 |
| Neuborn | 780 | 0.20 | 0.70 (69/turn) | garments 13 (19.5->22.42), timber 18 (6.35->9.88), nets 1 (36->42.56), tools 16 (4.5->4.99) | cured meat 6 (22.05->23.2), candles 1 (78.23->81), cheese 23 (5.51->5.79), flax plants 5 (1.28->1.79) | +67 |
| Friedwerp | 684 | 0.18 | 0.20 (20/turn) | beer 18 (2.92->4.31), garments 13 (19.5->21.09), tools 16 (4.5->5.37), tiles 1 (2.92->5.46) | thread 9 (4.58->5.7), candles 1 (76.65->81), pies 1 (16.48->19.38), wax 1 (21.42->23.75) | +63 |
| Caillechâtel | 488 | 0.13 | 0.10 (10/turn) | beer 18 (2.92->5.79), nets 5 (36->37.24), fleece 1 (6.2->7.41) | rope 1 (72.98->75.52), thread 31 (5.51->5.7), casks 1 (5.67->6.41), cured meat 1 (22.68->23.2) | +57 |

**Best:** Karlmoor at about +136 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 18 @ min 3.7 | makes 28.0, uses 19.2, holds 174 (keeps 60): sells the surplus + 9/turn of the excess |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 10 = 7.0 turns |
| cured meat | 9 @ 24.2, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 18 = 3.0 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 14 @ min 22.0 |  |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 271 @ 2.2, stop - |  | uses 721.0/turn (brewery 1, flax farm 1, household), makes 450.0, holds 271 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 10 @ min 35.6 |  |
| porterage | 11 @ 1.1, stop - |  | uses 11.0/turn (observed), makes 0.0, holds 11 = 1.0 turns |
| rope |  | 7 @ min 77.5 | makes 4.5, uses 0.0, holds 36 (keeps 0): sells the surplus + 3/turn of the excess |
| tar | 2 @ 11.0, stop 5 |  | uses 1.0/turn (ropewalk 1), makes 0.0, holds 9 = 9.2 turns |
| timber |  | 28 @ min 6.7 | makes 8.4, uses 0.0, holds 589 (keeps 350): sells the surplus + 19/turn of the excess |
| tools | 4 @ 6.2, stop 32 |  | uses 4.0/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 50.4 turns |

## Chain sizing

Mode HOLD, garments sold 17.5/turn (+0.0 exported); plan makes 16.8 garments a turn.
Labour: own 450, everything else 411, chain may buy 350 -> chain allowance 389, chain plan 390 (+3 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 6.18 | 6.30 |
| ret | 3 | 1.10 | 1.12 |
| spin | 4 | 2.26 | 2.31 |
| weave | 3 | 0.69 | 0.66 |
| sew | 2 | 0.39 | 0.41 |

Buffers: flax fibres 58/84, thread 349/248, cloth 21/66
- chain plan needed 598 labour, budget left 389: cut to 389 (sewing capped at 0.41)

## Self-diagnosis

- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
