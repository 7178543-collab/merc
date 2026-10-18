# v2 shadow report

Turn 13372, 2026-10-18 13:51. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 5,402, prestige 3,255 (585 free, -1.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 428 | 0 | 4 | 0 | 0 | min_holding 60, sell 34, sell @ 3.54 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 5 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 391 | 0 | 2 | 0 | 0 | min_holding 30, sell 36, sell @ 21.2 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 137 | 137 | 577 | 0 | 10 | buy 137, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 48 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 38.6 |
| porterage | 11 | 11 | 9 | 0 | 2 | buy 11, buy @ 1.1 |

**0 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Tuning

- **cloth**: cloth buffer thin: 1.1 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 62
- **furniture**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 73 over real use lately; planning 577, not 649

## Prestige spending, cheapest coin per prestige first

1029 turns left: prestige gained now converts 99.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.8 | 49.8 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 55.0 | 55.0 | thin at home: cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 55.8 | 55.8 | thin at home: cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 56.3 | 56.3 | thin at home: hop beer, cured fish |
| hold sermon 2 (candles) | church | 31 | 53.9 | 56.7 | needs a church (build cost 82,762); thin at home: jewellery, candles, furniture |
| jousting 1 | arena | 170 | 56.5 | 56.7 | needs a arena (build cost 26,265); thin at home: protection, light armour, arms; needs weaponry skill |
| hold prayer 2 | chapel | 13 | 54.3 | 57.0 | needs a chapel (build cost 34,152); thin at home: furniture |
| hold feast 2 | townhouse | 2.6 | 55.5 | 58.4 | needs a townhouse (build cost 7,576); thin at home: wine |
| hold banquet 2 (meat) | mansion | 6.8 | 59.0 | 59.0 |  |
| hold banquet 4 (pies) | mansion | 18 | 59.0 | 59.0 | thin at home: hop beer, stockfish, pies |
| hold sermon 2 | church | 24 | 55.6 | 59.2 | needs a church (build cost 82,762); thin at home: jewellery, furniture |
| hold banquet 3 (meat) | mansion | 7.6 | 59.9 | 59.9 | thin at home: hop beer |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 64601365 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Disscester: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn
- best towns now: Bremcop +27
- Bremcop would trade: garments sell 23 @ 23.4; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~100 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Bremcop | 1326 | 0.50 | 0.20 (20/turn) | garments 23 (20.16->24.7), soap 1 (89.78->118.75), thread 9 (4.66->5.22) | flour 1 (15.96->20.52) | +123 |
| Heidlowe | 662 | 0.18 | 0.40 (40/turn) | garments 16 (20.16->20.71), butter 1 (68.25->71.72) | thread 62 (4.7->5.7), cloth 5 (5.78->7.8), flax plants 66 (1.59->2.02), salt 7 (4.54->5.22) | +82 |
| Rouhomme | 368 | 0.10 | 0.60 (60/turn) | beer 54 (3->3.8), bread 145 (2.35->2.75), cured meat 2 (24->29.64), tallow 1 (22.26->23.56) | thread 20 (4.96->5.7), cookware 4 (21->22.23), blades 2 (14.7->15.11), flax fibres 3 (5.88->6.25) | +81 |
| Großmühle | 751 | 0.20 | 0.10 (10/turn) | garments 17 (20.16->24.13), butter 1 (68.25->71.25) | salt 8 (4.22->5.22), thread 6 (5.23->5.7), pies 1 (16.38->17.86), flax plants 6 (1.61->2.02) | +75 |
| Unterhufe | 595 | 0.16 | 0.10 (10/turn) | garments 13 (20.16->23.18), butter 1 (68.25->75.05), tools 8 (4.24->4.64) | salt 8 (4.22->5.22), pasties 1 (8.14->13.11), tar 1 (8.87->11.4), thread 5 (5.08->5.7) | +57 |

**Best:** Bremcop at about +123 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 52 @ min 3.54 | makes 28.0, uses 4.2, holds 428 (keeps 60): sells the surplus + 29/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| furniture | 3 @ 15.5, stop 6 |  | uses 1.4/turn (household upkeep), makes 0.0, holds 3 = 2.3 turns |
| garments |  | 43 @ min 21.2 | makes 16.0, uses 2.1, holds 391 (keeps 30): sells the surplus + 29/turn of the excess |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 127 @ 2.2, stop - |  | uses 576.7/turn (brewery 1, flax farm 1, household), makes 450.0, holds 137 = 1.1 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 11 @ min 37.4 | makes 9.0, uses 0.0, holds 48 (keeps 15): sells the surplus + 2/turn of the excess |
| porterage | 9 @ 1.1, stop - |  | uses 8.8/turn (observed), makes 0.0, holds 11 = 1.2 turns |
| rope |  | 7 @ min 77.5 | makes 2.2, uses 0.0, holds 58 (keeps 0): sells the surplus + 5/turn of the excess |
| timber |  | 8 @ min 6.7 |  |
| tools | 4 @ 6.2, stop 26 |  | uses 3.2/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 61.8 turns |

## Chain sizing

Mode HOLD, garments sold 1.6/turn (+0.0 exported); plan makes 13.1 garments a turn.
Labour: own 450, everything else 362, chain may buy 350 -> chain allowance 438, chain plan 263 (-26 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.14 | 3.98 |
| ret | 3 | 0.74 | 0.71 |
| spin | 4 | 1.51 | 1.46 |
| weave | 3 | 0.62 | 0.51 |
| sew | 2 | 0.39 | 0.32 |

Buffers: flax fibres 59/60, thread 371/178, cloth 34/51

## Self-diagnosis

- R1: arms slot dry: 0.0 held, 0.5 a turn (gear slot (+0.4 prestige)); our buy paused by the failsafe, home ask 25.0 (held back: paused by the failsafe at level 3: un-pause only at level 0)
- R2: ropewalk 1 blocked by rope space: 58 held of 60 capacity, we make 2.2 a turn; no buy on it: add a sell order or more capacity for rope
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
