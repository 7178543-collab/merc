# v2 shadow report

Turn 13374, 2026-10-18 15:49. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 5,547, prestige 3,302 (632 free, +50.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 408 | 0 | 4 | 0 | 0 | min_holding 60, sell 34, sell @ 3.54 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 293 | 0 | 2 | 0 | 0 | min_holding 30, sell 36, sell @ 21.2 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 110 | 137 | 537 | 0 | 50 | buy 98, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 61 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 38.6 |
| porterage | 11 | 11 | 9 | 0 | 2 | buy 11, buy @ 1.1 |

**0 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **labour**: 50 labour expired last turn (~81 coin): holding 110 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **cloth**: cloth buffer thin: 1.3 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 51
- **furniture**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 73 over real use lately; planning 537, not 611

## Prestige spending, cheapest coin per prestige first

1027 turns left: prestige gained now converts 99.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.9 | 48.9 | running |
| hold prayer 2 | chapel | 13 | 54.2 | 56.6 | needs a chapel (build cost 30,614); thin at home: furniture |
| jousting 1 | arena | 170 | 56.5 | 56.7 | needs a arena (build cost 24,016); thin at home: protection, light armour, arms; needs weaponry skill |
| hold feast 2 | townhouse | 2.6 | 54.1 | 56.8 | needs a townhouse (build cost 7,204) |
| hold banquet 2 (fish) | mansion | 6.8 | 57.3 | 57.3 | thin at home: cured fish |
| hold sermon 2 (candles) | church | 31 | 54.7 | 57.4 | needs a church (build cost 78,585); thin at home: candles, furniture |
| hold banquet 3 (fish) | mansion | 7.6 | 58.7 | 58.7 | thin at home: hop beer, cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 58.9 | 58.9 | thin at home: cured fish |
| hold banquet 2 (meat) | mansion | 6.8 | 58.9 | 58.9 |  |
| hold sermon 2 | church | 24 | 55.5 | 59.0 | needs a church (build cost 78,585); thin at home: furniture |
| hold banquet 3 (meat) | mansion | 7.6 | 60.1 | 60.1 | thin at home: hop beer |
| hold banquet 3 (pies) | mansion | 8 | 60.5 | 60.5 | thin at home: hop beer, pies, candles |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 64601365 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Disscester: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~99 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Chribruck | 1202 | 0.42 | 0.20 (20/turn) | garments 23 (20.14->24.7), cheese 3 (6.88->8.26) | flax fibres 4 (5.57->6.45) | +93 |
| Chatgnan | 728 | 0.19 | 0.30 (30/turn) | beer 52 (2.99->4.56), nails 2 (5.67->9.12), rope 2 (79.5->83.6), cloth 2 (6.92->7.89) | flax fibres 2 (5.67->6.45) | +75 |
| Bremcop | 1326 | 0.49 | 0.20 (20/turn) | soap 1 (90.83->139.65), garments 23 (20.14->21.09) | casks 3 (3.32->5.27), butter 3 (73.5->75.52) | +62 |
| Rouhomme | 368 | 0.10 | 0.20 (20/turn) | beer 52 (2.99->3.8), cloth 2 (6.92->14.44), cheese 12 (6.88->7.22), tallow 1 (22.47->23.56) | jewellery 1 (78.75->85.97), cookware 3 (21->22.42), blades 2 (14.7->15.29), flax fibres 3 (5.88->6.45) | +59 |
| Fontaux | 411 | 0.11 | 0.20 (20/turn) | cheese 13 (6.88->9.59), tools 15 (4.24->4.75), timber 8 (6.3->8.55), flax fibres 4 (6.2->6.98) | - | +46 |

**Best:** Chribruck at about +93 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 51 @ min 3.54 | makes 28.0, uses 4.2, holds 408 (keeps 60): sells the surplus + 27/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| furniture | 3 @ 15.5, stop 6 |  | uses 1.4/turn (household upkeep), makes 0.0, holds 0 = 0.3 turns |
| garments |  | 32 @ min 21.2 | makes 13.1, uses 2.1, holds 293 (keeps 30): sells the surplus + 21/turn of the excess |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 87 @ 2.2, stop - |  | uses 537.2/turn (brewery 1, flax farm 1, household), makes 450.0, holds 110 = 1.3 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 12 @ min 37.2 | makes 9.0, uses 0.0, holds 61 (keeps 15): sells the surplus + 3/turn of the excess |
| porterage | 9 @ 1.1, stop - |  | uses 8.6/turn (observed), makes 0.0, holds 11 = 1.3 turns |
| rope |  | 7 @ min 77.5 | makes 2.2, uses 0.0, holds 60 (keeps 0): sells the surplus + 5/turn of the excess |
| timber |  | 8 @ min 6.7 |  |
| tools | 4 @ 6.2, stop 26 |  | uses 3.2/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 62.8 turns |

## Chain sizing

Mode HOLD, garments sold 5.2/turn (+0.0 exported); plan makes 18.4 garments a turn.
Labour: own 450, everything else 362, chain may buy 350 -> chain allowance 438, chain plan 328 (+65 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 3.98 | 4.63 |
| ret | 3 | 0.71 | 0.82 |
| spin | 4 | 1.46 | 1.70 |
| weave | 3 | 0.51 | 0.73 |
| sew | 2 | 0.32 | 0.45 |

Buffers: flax fibres 59/68, thread 379/200, cloth 34/73

## Self-diagnosis

- R1: arms slot dry: 0.0 held, 0.5 a turn (gear slot (+0.4 prestige)); our buy paused by the failsafe, home ask 24.8 (held back: paused by the failsafe at level 3: un-pause only at level 0)
- R1: furniture slot dry: 0.4 held, 1.4 a turn (household slot (+0.4 prestige)); our buy paused by the failsafe, home ask none (no sellers at home)
- R2: ropewalk 1 blocked by rope space: 60 held of 60 capacity, we make 2.2 a turn; no buy on it: add a sell order or more capacity for rope
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
