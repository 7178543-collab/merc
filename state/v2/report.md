# v2 shadow report

Turn 13371, 2026-10-18 12:59. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 5,377, prestige 3,257 (587 free, -1.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 438 | 0 | 4 | 0 | 0 | min_holding 60, sell 34, sell @ 3.54 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 399 | 0 | 2 | 0 | 0 | min_holding 30, sell 36, sell @ 21.2 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 137 | 181 | 577 | 0 | 54 | buy 137, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 40 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 38.6 |
| porterage | 11 | 11 | 9 | 0 | 2 | buy 11, buy @ 1.1 |

**0 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **labour**: 54 labour expired last turn (~91 coin): holding 137 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **cloth**: cloth buffer thin: 1.1 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 62
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **furniture**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 73 over real use lately; planning 577, not 650
- labour expiry guard: 54 bought labour expired last turn, buy 127 (not 127) this turn

## Prestige spending, cheapest coin per prestige first

1030 turns left: prestige gained now converts 99.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.1 | 50.1 | running |
| hold sermon 2 (candles) | church | 31 | 53.5 | 56.3 | needs a church (build cost 81,708); thin at home: furniture |
| hold prayer 2 | chapel | 13 | 54.4 | 57.0 | needs a chapel (build cost 32,904); thin at home: furniture |
| jousting 1 | arena | 170 | 56.9 | 57.0 | needs a arena (build cost 25,787); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 58.5 | 58.5 | thin at home: hop beer, cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 58.9 | 58.9 | thin at home: wine, cured fish |
| hold sermon 2 | church | 24 | 55.3 | 59.0 | needs a church (build cost 81,708); thin at home: furniture |
| hold banquet 1 (fish) | mansion | 4.2 | 59.2 | 59.2 | thin at home: cured fish |
| hold banquet 3 (meat) | mansion | 7.6 | 59.9 | 59.9 | thin at home: hop beer |
| hold banquet 3 (pies) | mansion | 8 | 59.9 | 59.9 | thin at home: hop beer, pies |
| hold banquet 2 (meat) | mansion | 6.8 | 60.5 | 60.5 | thin at home: wine |
| hold banquet 1 (meat) | mansion | 4.2 | 61.9 | 61.9 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 64601365 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Disscester: garments sell 17 @ 25.6; crew 0.1; est +80 a turn
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn
- best towns now: Disscester +80, Bremcop +52, Fontaux +42, Calange +22, Birkeningen +16
- Disscester would trade: garments sell 17 @ 25.6; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~101 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Fontaux | 411 | 0.11 | 0.40 (40/turn) | beer 45 (3->4.37), cheese 16 (6.62->9.79), thread 32 (4.66->5.65), timber 8 (6.3->8.55) | salt 8 (4.7->5.03), cloth 6 (7.88->8.15) | +130 |
| Disscester | 1474 | 0.58 | 0.20 (20/turn) | garments 17 (20.16->28.12) | ploughs 2 (61.43->68.88), flax fibres 1 (5.08->6.25) | +128 |
| Bremcop | 1326 | 0.50 | 0.20 (20/turn) | garments 25 (20.16->25.08) | - | +102 |
| Hanbrücken | 531 | 0.14 | 0.30 (30/turn) | garments 7 (20.16->23.56), yarn 5 (5.57->7.12), wool 5 (9.45->10.83), beer 31 (3->3.31) | cloth 29 (6.46->8.15), salt 8 (4.18->5.03), grain 13 (2.31->2.72) | +90 |
| Rotterburg | 1056 | 0.35 | 0.20 (20/turn) | soap 2 (89.25->127.3), rope 2 (79.5->83.12), garments 33 (20.16->20.52) | beer 4 (2.44->3.6), salt 3 (4.33->5.03) | +82 |

**Best:** Fontaux at about +130 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 53 @ min 3.54 | makes 28.0, uses 4.2, holds 438 (keeps 60): sells the surplus + 30/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.1 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| furniture | 3 @ 15.5, stop 6 |  | uses 1.4/turn (household upkeep), makes 0.0, holds 5 = 3.3 turns |
| garments |  | 43 @ min 21.2 | makes 16.0, uses 2.1, holds 399 (keeps 30): sells the surplus + 30/turn of the excess |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 127 @ 2.2, stop - |  | uses 576.7/turn (brewery 1, flax farm 1, household), makes 450.0, holds 137 = 1.1 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 10 @ min 37.2 | makes 9.0, uses 0.0, holds 40 (keeps 15): sells the surplus + 1/turn of the excess |
| porterage | 9 @ 1.1, stop - |  | uses 8.8/turn (observed), makes 0.0, holds 11 = 1.2 turns |
| rope |  | 7 @ min 77.5 | makes 2.2, uses 0.0, holds 56 (keeps 0): sells the surplus + 4/turn of the excess |
| timber |  | 8 @ min 6.7 |  |
| tools | 4 @ 6.2, stop 26 |  | uses 3.2/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 61.8 turns |

## Chain sizing

Mode HOLD, garments sold 0.0/turn (+0.0 exported); plan makes 27.9 garments a turn.
Labour: own 450, everything else 362, chain may buy 350 -> chain allowance 438, chain plan 438 (+150 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.14 | 5.75 |
| ret | 3 | 0.74 | 1.02 |
| spin | 4 | 1.51 | 2.10 |
| weave | 3 | 0.62 | 1.08 |
| sew | 2 | 0.39 | 0.68 |

Buffers: flax fibres 59/80, thread 385/235, cloth 35/108
- chain plan needed 507 labour, budget left 438: cut to 438 (sewing capped at 0.68)

## Self-diagnosis

- R1: arms slot dry: 0.0 held, 0.5 a turn (gear slot (+0.4 prestige)); our buy paused by the failsafe, home ask 24.8 (held back: paused by the failsafe at level 3: un-pause only at level 0)
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
