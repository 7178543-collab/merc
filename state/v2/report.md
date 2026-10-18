# v2 shadow report

Turn 13368, 2026-10-18 09:52. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 6,619, prestige 3,261 (591 free, -1.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 401 | 0 | 4 | 0 | 0 | min_holding 60, sell 34, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 17 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 372 | 0 | 2 | 0 | 0 | min_holding 30, sell 36, sell @ 22 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 205 | 241 | 645 | 0 | 46 | buy 205, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 19 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 38.6 |
| porterage | 11 | 11 | 9 | 0 | 2 | buy 11, buy @ 1.1 |

**1 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.8 turns (holds 35, next step uses 43/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **labour**: 46 labour expired last turn (~77 coin): holding 205 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax fibres**: flax fibres buffer thin: 2.0 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 58

## Notes

- labour: projection runs 74 over real use lately; planning 645, not 718
- labour expiry guard: 46 bought labour expired last turn, buy 195 (not 195) this turn

## Prestige spending, cheapest coin per prestige first

1033 turns left: prestige gained now converts 99.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.1 | 50.1 | running |
| hold sermon 2 (candles) | church | 31 | 54.3 | 57.1 | needs a church (build cost 81,910); thin at home: candles, furniture |
| hold prayer 2 | chapel | 13 | 54.8 | 57.5 | needs a chapel (build cost 34,044); thin at home: furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 57.8 | 57.8 | thin at home: cured fish |
| jousting 1 | arena | 170 | 57.6 | 57.8 | needs a arena (build cost 26,220); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 58.5 | 58.5 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 58.6 | 58.6 | thin at home: cured fish |
| hold sermon 2 | church | 24 | 55.4 | 59.0 | needs a church (build cost 81,910); thin at home: furniture |
| hold banquet 1 (fish) | mansion | 4.2 | 59.2 | 59.2 | thin at home: cured fish |
| hold banquet 3 (meat) | mansion | 7.6 | 59.2 | 59.2 |  |
| hold feast 2 | townhouse | 2.6 | 56.3 | 59.4 | needs a townhouse (build cost 8,026); thin at home: wine |
| hold banquet 3 (pies) | mansion | 8 | 59.9 | 59.9 | thin at home: pies, candles |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 64601365 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Disscester: garments sell 27 @ 24.2; crew 0.2; est +84 a turn
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn
- best towns now: Disscester +84, Birkeningen +46, Bremcop +43
- Disscester would trade: garments sell 27 @ 24.2; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~101 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Bremcop | 1326 | 0.50 | 0.30 (30/turn) | garments 44 (20.18->25.08), thread 5 (4.66->5.22) | - | +188 |
| Disscester | 1474 | 0.58 | 0.20 (20/turn) | garments 27 (20.18->26.03), wine 1 (5.93->8.31) | ploughs 1 (63.53->69.83) | +144 |
| Donaunieder | 985 | 0.32 | 0.10 (10/turn) | tackles 1 (174.3->186.2), cookware 7 (22.26->23.37) | candles 5 (62.48->70.77), cloth 8 (7.35->8.6), flax fibres 1 (5.15->6.1) | +62 |
| Birkeningen | 1006 | 0.33 | 0.20 (20/turn) | garments 17 (20.18->22.8), rope 2 (79->86.45), salt 6 (4.3->4.84), bricks 1 (8.82->15.67) | cloth 22 (8.24->8.6) | +55 |
| Angefont | 686 | 0.18 | 0.10 (10/turn) | tackles 1 (174.3->203.3), cloth 3 (6.3->6.6), tallow 2 (22.68->23.18) | cloth 12 (7.35->8.6), thread 33 (4.73->4.96), potash 1 (14.49->16.05), tools 3 (4.75->4.98) | +44 |

**Best:** Bremcop at about +188 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 27.0, stop 1 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 0 = 0.0 turns |
| beer |  | 50 @ min 3.7 | makes 28.0, uses 4.2, holds 401 (keeps 60): sells the surplus + 26/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 17 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| furniture | 2 @ 15.5, stop 6 |  | uses 1.4/turn (household upkeep), makes 0.0, holds 9 = 6.3 turns |
| garments |  | 47 @ min 22.0 | makes 22.1, uses 2.1, holds 372 (keeps 30): sells the surplus + 27/turn of the excess |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 195 @ 2.2, stop - |  | uses 644.6/turn (brewery 1, flax farm 1, household), makes 450.0, holds 205 = 1.1 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 37.0 |  |
| porterage | 9 @ 1.1, stop - |  | uses 9.4/turn (observed), makes 0.0, holds 11 = 1.2 turns |
| rope |  | 6 @ min 77.0 | makes 2.2, uses 0.0, holds 49 (keeps 0): sells the surplus + 4/turn of the excess |
| timber |  | 8 @ min 7.0 |  |
| tools | 4 @ 6.2, stop 28 |  | uses 3.4/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 58.2 turns |

## Chain sizing

Mode HOLD, garments sold 1.9/turn (+4.9 exported); plan makes 19.7 garments a turn.
Labour: own 450, everything else 362, chain may buy 350 -> chain allowance 438, chain plan 332 (-24 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.72 | 4.56 |
| ret | 3 | 0.84 | 0.81 |
| spin | 4 | 1.73 | 1.67 |
| weave | 3 | 0.87 | 0.77 |
| sew | 2 | 0.54 | 0.48 |

Buffers: flax fibres 58/69, thread 427/204, cloth 35/77

## Self-diagnosis

- R1: arms slot dry: 0.0 held, 0.5 a turn (gear slot (+0.4 prestige)); our buy paused by the failsafe, home ask 25.8 (held back: paused by the failsafe at level 2: un-pause only at level 0)
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
