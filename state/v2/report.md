# v2 shadow report

Turn 13370, 2026-10-18 11:48. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 5,325, prestige 3,258 (588 free, -1.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 449 | 0 | 4 | 0 | 0 | min_holding 60, sell 34, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 17 | 5 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 404 | 0 | 2 | 0 | 0 | min_holding 30, sell 36, sell @ 22 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 181 | 205 | 577 | 0 | 78 | buy 137, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 34 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 38.6 |
| porterage | 11 | 11 | 9 | 0 | 2 | buy 11, buy @ 1.1 |

**0 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **labour**: 78 labour expired last turn (~132 coin): holding 181 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **cloth**: cloth buffer thin: 1.1 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 62

## Notes

- labour: projection runs 73 over real use lately; planning 577, not 650
- labour expiry guard: 78 bought labour expired last turn, buy 127 (not 127) this turn

## Prestige spending, cheapest coin per prestige first

1031 turns left: prestige gained now converts 99.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.4 | 50.4 | running |
| hold sermon 2 (candles) | church | 31 | 53.7 | 56.5 | needs a church (build cost 80,920); thin at home: candles, furniture |
| hold prayer 2 | chapel | 13 | 54.8 | 57.4 | needs a chapel (build cost 33,044); thin at home: furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 57.5 | 57.5 | thin at home: wine, cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 58.4 | 58.4 | thin at home: hop beer, cured fish |
| hold banquet 2 (meat) | mansion | 6.8 | 58.8 | 58.8 | thin at home: wine |
| hold feast 2 | townhouse | 2.6 | 56.0 | 58.8 | needs a townhouse (build cost 7,414); thin at home: wine |
| hold banquet 1 (fish) | mansion | 4.2 | 59.3 | 59.3 | thin at home: cured fish |
| hold sermon 2 | church | 24 | 55.7 | 59.3 | needs a church (build cost 80,920); thin at home: furniture |
| hold banquet 3 (meat) | mansion | 7.6 | 59.6 | 59.6 | thin at home: hop beer |
| hold banquet 3 (pies) | mansion | 8 | 59.9 | 59.9 | thin at home: hop beer, pies |
| hold banquet 2 (pies) | mansion | 7 | 60.7 | 60.7 | thin at home: wine, pies |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 64601365 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Disscester: garments sell 19 @ 25.2; crew 0.2; est +72 a turn
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn
- best towns now: Bremcop +76, Disscester +72, Birkeningen +68, Calange +22, Coburgbaum +20
- Bremcop would trade: garments sell 39 @ 22.8; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~102 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Bremcop | 1326 | 0.50 | 0.30 (30/turn) | garments 39 (20.17->25.08), glassware 2 (59.33->60.32) | bronze ingots 1 (21.63->22.8) | +165 |
| Disscester | 1474 | 0.58 | 0.20 (20/turn) | garments 19 (20.17->27.74), cloth 2 (1.36->7.27), nets 2 (38.2->39.9) | ploughs 1 (53.03->62.22) | +148 |
| Birkeningen | 1006 | 0.33 | 0.40 (41/turn) | garments 18 (20.17->25.84), beer 47 (3->4.08), cloth 2 (1.36->7.46), rope 2 (79.5->84.55) | - | +135 |
| Vauxvais | 204 | 0.06 | 0.10 (10/turn) | butter 1 (68.78->86.45), cloth 2 (1.36->6.32), rope 2 (79.5->81.7), tar 2 (9.66->10.64) | cloth 31 (7.25->8.05), flax fibres 19 (5.46->6.25), thread 9 (4.28->4.8), honey 2 (7.25->7.89) | +76 |
| Hanstein | 380 | 0.10 | 0.20 (20/turn) | butter 1 (68.78->77.9), cloth 2 (1.36->4.8), tar 4 (9.66->11.11), flax fibres 5 (4.89->5.18) | flax plants 66 (1.29->2.02), cloth 11 (6.67->8.05) | +66 |

**Best:** Bremcop at about +165 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 54 @ min 3.7 | makes 28.0, uses 4.2, holds 449 (keeps 60): sells the surplus + 30/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 17 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| furniture | 2 @ 15.5, stop 6 |  | uses 1.4/turn (household upkeep), makes 0.0, holds 6 = 4.3 turns |
| garments |  | 44 @ min 22.0 | makes 16.0, uses 2.1, holds 404 (keeps 30): sells the surplus + 30/turn of the excess |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 127 @ 2.2, stop - |  | uses 576.7/turn (brewery 1, flax farm 1, household), makes 450.0, holds 181 = 1.4 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 10 @ min 37.2 |  |
| porterage | 9 @ 1.1, stop - |  | uses 8.8/turn (observed), makes 0.0, holds 11 = 1.2 turns |
| rope |  | 7 @ min 77.5 | makes 2.2, uses 0.0, holds 54 (keeps 0): sells the surplus + 4/turn of the excess |
| timber |  | 8 @ min 6.7 |  |
| tools | 4 @ 6.2, stop 26 |  | uses 3.2/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 61.9 turns |

## Chain sizing

Mode HOLD, garments sold 0.0/turn (+0.0 exported); plan makes 27.9 garments a turn.
Labour: own 450, everything else 362, chain may buy 350 -> chain allowance 438, chain plan 438 (+150 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.14 | 5.71 |
| ret | 3 | 0.74 | 1.02 |
| spin | 4 | 1.51 | 2.09 |
| weave | 3 | 0.62 | 1.09 |
| sew | 2 | 0.39 | 0.68 |

Buffers: flax fibres 58/80, thread 399/236, cloth 35/109
- chain plan needed 504 labour, budget left 438: cut to 438 (sewing capped at 0.68)

## Self-diagnosis

- R1: arms slot dry: 0.0 held, 0.5 a turn (gear slot (+0.4 prestige)); our buy paused by the failsafe, home ask 25.0 (held back: paused by the failsafe at level 3: un-pause only at level 0)
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
