# v2 shadow report

Turn 13369, 2026-10-18 10:50. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 5,951, prestige 3,260 (590 free, -1.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 425 | 0 | 4 | 0 | 0 | min_holding 60, sell 34, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 390 | 0 | 2 | 0 | 0 | min_holding 30, sell 36, sell @ 22 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 205 | 205 | 621 | 0 | 34 | buy 181, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 26 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 38.6 |
| porterage | 11 | 11 | 9 | 0 | 2 | buy 11, buy @ 1.1 |

**1 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.9 turns (holds 35, next step uses 38/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **labour**: 34 labour expired last turn (~57 coin): holding 205 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 73 over real use lately; planning 621, not 694
- labour expiry guard: 34 bought labour expired last turn, buy 171 (not 171) this turn

## Prestige spending, cheapest coin per prestige first

1032 turns left: prestige gained now converts 99.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.1 | 50.1 | running |
| hold prayer 2 | chapel | 13 | 54.8 | 57.5 | needs a chapel (build cost 34,084); thin at home: furniture |
| jousting 1 | arena | 170 | 58.2 | 58.3 | needs a arena (build cost 26,294); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 58.5 | 58.5 | thin at home: cured fish |
| hold feast 2 | townhouse | 2.6 | 55.5 | 58.6 | needs a townhouse (build cost 8,026) |
| hold sermon 2 (candles) | church | 31 | 56.0 | 58.9 | needs a church (build cost 82,539); thin at home: candles, furniture |
| hold banquet 1 (fish) | mansion | 4.2 | 59.2 | 59.2 | thin at home: cured fish |
| hold sermon 2 | church | 24 | 55.6 | 59.3 | needs a church (build cost 82,539); thin at home: furniture |
| hold banquet 2 (meat) | mansion | 6.8 | 59.4 | 59.4 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 59.4 | 59.4 | thin at home: cured fish |
| hold banquet 3 (meat) | mansion | 7.6 | 60.2 | 60.2 |  |
| hold banquet 1 (meat) | mansion | 4.2 | 61.1 | 61.1 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 64601365 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Disscester: candles buy 1 @ 75.0, garments sell 22 @ 24.6; crew 0.2; est +80 a turn
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn; best orders clear only -5 a turn after crew: ship stays at 0
- best towns now: Disscester +80, Birkeningen +72, Bremcop +69, Brunnham +24
- Disscester would trade: candles buy 1 @ 75.0, garments sell 22 @ 24.6; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~101 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Bremcop | 1326 | 0.50 | 0.30 (30/turn) | garments 38 (20.17->24.89), thread 3 (4.66->5.22) | candles 1 (73.5->80.5), bronze ingots 1 (21.63->22.8) | +158 |
| Disscester | 1474 | 0.58 | 0.20 (20/turn) | garments 22 (20.17->26.98) | candles 1 (77.7->80.5), flax fibres 4 (4.89->6.2) | +138 |
| Birkeningen | 1006 | 0.33 | 0.20 (20/turn) | garments 18 (20.17->24.13), rope 2 (79->85.97), bricks 1 (8.82->15.67) | candles 1 (72.98->80.5) | +79 |
| Karlmoor | 787 | 0.21 | 0.10 (10/turn) | tackles 1 (174.3->193.8), butter 1 (68.78->71.25), flax plants 2 (1.47->2.05) | furniture 11 (9.03->11.4), candles 1 (74.03->80.5), garments 2 (20.79->21.4) | +45 |
| Hofkirchen | 991 | 0.32 | 0.10 (10/turn) | flax plants 15 (1.47->3.89) | candles 1 (69.3->80.5), wrought iron 4 (11.23->12.44), bronze ingots 1 (22.47->22.8) | +42 |

**Best:** Bremcop at about +158 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 52 @ min 3.7 | makes 28.0, uses 4.2, holds 425 (keeps 60): sells the surplus + 28/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| furniture | 2 @ 15.5, stop 6 |  | uses 1.4/turn (household upkeep), makes 0.0, holds 7 = 5.3 turns |
| garments |  | 46 @ min 22.0 | makes 19.7, uses 2.1, holds 390 (keeps 30): sells the surplus + 29/turn of the excess |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 171 @ 2.2, stop - |  | uses 620.7/turn (brewery 1, flax farm 1, household), makes 450.0, holds 205 = 1.2 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 37.2 |  |
| porterage | 9 @ 1.1, stop - |  | uses 9.3/turn (observed), makes 0.0, holds 11 = 1.2 turns |
| rope |  | 6 @ min 77.0 | makes 2.2, uses 0.0, holds 51 (keeps 0): sells the surplus + 4/turn of the excess |
| timber |  | 8 @ min 6.7 |  |
| tools | 4 @ 6.2, stop 27 |  | uses 3.4/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 59.1 turns |

## Chain sizing

Mode HOLD, garments sold 1.3/turn (+2.4 exported); plan makes 16.0 garments a turn.
Labour: own 450, everything else 362, chain may buy 350 -> chain allowance 438, chain plan 288 (-44 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.56 | 4.14 |
| ret | 3 | 0.81 | 0.74 |
| spin | 4 | 1.67 | 1.51 |
| weave | 3 | 0.77 | 0.62 |
| sew | 2 | 0.48 | 0.39 |

Buffers: flax fibres 58/64, thread 413/189, cloth 35/62

## Self-diagnosis

- R1: arms slot dry: 0.0 held, 0.5 a turn (gear slot (+0.4 prestige)); our buy paused by the failsafe, home ask 25.0 (held back: paused by the failsafe at level 3: un-pause only at level 0)
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
