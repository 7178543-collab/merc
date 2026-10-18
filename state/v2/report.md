# v2 shadow report

Turn 13366, 2026-10-18 07:04. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 6,887, prestige 3,264 (594 free, -1.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 353 | 0 | 4 | 0 | 0 | min_holding 60, sell 34, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 332 | 0 | 2 | 0 | 0 | min_holding 30, sell 36, sell @ 22 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 241 | 241 | 682 | 0 | 9 | buy 241, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 15 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 38.6 |
| porterage | 11 | 11 | 10 | 0 | 1 | buy 11, buy @ 1.1 |

**1 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.7 turns (holds 35, next step uses 51/turn) -> v2: check the step that makes it

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.9 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 61

## Notes

- labour: projection runs 75 over real use lately; planning 682, not 756

## Prestige spending, cheapest coin per prestige first

1035 turns left: prestige gained now converts 99.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.1 | 50.1 | running |
| jousting 1 | arena | 170 | 57.4 | 57.5 | needs a arena (build cost 27,640); thin at home: protection, light armour, arms; needs weaponry skill |
| hold prayer 2 | chapel | 13 | 54.8 | 57.6 | needs a chapel (build cost 35,744); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 54.7 | 57.6 | needs a church (build cost 84,465); thin at home: candles, furniture |
| hold banquet 3 (meat) | mansion | 7.6 | 58.2 | 58.2 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 58.4 | 58.4 | thin at home: cured fish |
| hold sermon 2 | church | 24 | 55.0 | 58.7 | needs a church (build cost 84,465); thin at home: furniture |
| hold banquet 1 (fish) | mansion | 4.2 | 59.2 | 59.2 | thin at home: cured fish |
| hold banquet 1 (meat) | mansion | 4.2 | 59.6 | 59.6 |  |
| hold banquet 3 (pies) | mansion | 8 | 59.9 | 59.9 | thin at home: pies, candles |
| hold banquet 2 (meat) | mansion | 6.8 | 60.9 | 60.9 | thin at home: wine |
| hold banquet 2 (fish) | mansion | 6.8 | 61.2 | 61.2 | thin at home: wine, cured fish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 64601365 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Disscester: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn
- best towns now: Kleinburgh +41, Caillechâtel +39, Calange +25, Fontaux +22, Rouhomme +20
- Kleinburgh would trade: garments sell 25 @ 22.8; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~101 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Fontaux | 411 | 0.11 | 0.40 (40/turn) | cheese 39 (5.83->9.79), beer 44 (3->4.29), timber 10 (6.3->8.55), cloth 1 (6->7.03) | pies 1 (15.54->16.81) | +198 |
| Hofkirchen | 991 | 0.32 | 0.20 (20/turn) | medicine 1 (143.85->239.4), flax plants 15 (1.82->3.89), cloth 2 (6->6.93) | slaked lime 1 (7.98->11.3), cloth 19 (7.77->8.15), wrought iron 4 (11.76->12.44), bronze ingots 1 (22.05->22.8) | +121 |
| Hanstein | 380 | 0.10 | 0.20 (20/turn) | salt 6 (4.24->5.27), cloth 2 (6->7.08), grain 4 (2.26->2.72) | flax fibres 30 (5.17->6.45), thread 95 (4.62->5), seeds 8 (1.74->2.32), flax plants 2 (1.31->1.73) | +70 |
| Caillechâtel | 488 | 0.13 | 0.10 (10/turn) | beer 25 (3->5.08), cloth 2 (6->7.93), salt 2 (4.24->4.99) | flax fibres 12 (5.62->6.45), grain 13 (2.5->2.84), seeds 8 (1.89->2.32), flax plants 2 (1.38->1.73) | +60 |
| Calange | 218 | 0.06 | 0.10 (10/turn) | beer 44 (3->3.97), cheese 14 (5.83->6.65), wine 4 (5.99->6.27), grain 4 (2.26->2.39) | slaked lime 1 (7.25->11.3), cloth 10 (7.88->8.15), flax fibres 4 (5.88->6.45), grain 13 (2.69->2.84) | +58 |

**Best:** Fontaux at about +198 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 27.6, stop 1 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 1 = 2.0 turns |
| beer |  | 46 @ min 3.7 | makes 28.0, uses 4.2, holds 353 (keeps 60): sells the surplus + 22/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.1 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| furniture | 2 @ 15.5, stop 6 |  | uses 1.4/turn (household upkeep), makes 0.0, holds 12 = 8.3 turns |
| garments |  | 47 @ min 22.0 | makes 26.2, uses 2.1, holds 332 (keeps 30): sells the surplus + 23/turn of the excess |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 232 @ 2.2, stop - |  | uses 682.1/turn (brewery 1, flax farm 1, household), makes 450.0, holds 241 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 38.0 |  |
| porterage | 10 @ 1.1, stop - |  | uses 9.7/turn (observed), makes 0.0, holds 11 = 1.1 turns |
| rope |  | 6 @ min 77.0 | makes 2.2, uses 0.0, holds 50 (keeps 0): sells the surplus + 4/turn of the excess |
| timber |  | 10 @ min 6.95 | makes 8.4, uses 0.0, holds 372 (keeps 350): sells the surplus + 1/turn of the excess |
| tools | 4 @ 6.2, stop 29 |  | uses 3.5/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 56.8 turns |

## Chain sizing

Mode HOLD, garments sold 5.2/turn (+4.9 exported); plan makes 22.1 garments a turn.
Labour: own 450, everything else 362, chain may buy 350 -> chain allowance 438, chain plan 356 (-38 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.97 | 4.72 |
| ret | 3 | 0.88 | 0.84 |
| spin | 4 | 1.82 | 1.73 |
| weave | 3 | 1.02 | 0.87 |
| sew | 2 | 0.64 | 0.54 |

Buffers: flax fibres 58/73, thread 458/214, cloth 35/87

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
