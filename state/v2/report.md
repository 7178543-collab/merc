# v2 shadow report

Turn 13367, 2026-10-18 08:53. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 6,999, prestige 3,263 (593 free, -1.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 377 | 0 | 4 | 0 | 0 | min_holding 60, sell 34, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 5 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 352 | 0 | 2 | 0 | 0 | min_holding 30, sell 36, sell @ 22 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 241 | 241 | 645 | 0 | 46 | buy 205, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 38.6 |
| porterage | 11 | 11 | 9 | 0 | 2 | buy 11, buy @ 1.1 |

**1 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.8 turns (holds 35, next step uses 43/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **labour**: 46 labour expired last turn (~78 coin): holding 241 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **flax fibres**: flax fibres buffer thin: 2.0 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 58

## Notes

- labour: projection runs 74 over real use lately; planning 645, not 718
- labour expiry guard: 46 bought labour expired last turn, buy 195 (not 195) this turn

## Prestige spending, cheapest coin per prestige first

1034 turns left: prestige gained now converts 99.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.7 | 50.7 | running |
| hold sermon 2 (candles) | church | 31 | 54.4 | 57.2 | needs a church (build cost 81,919); thin at home: candles, furniture |
| hold prayer 2 | chapel | 13 | 54.8 | 57.5 | needs a chapel (build cost 34,152); thin at home: furniture |
| jousting 1 | arena | 170 | 57.8 | 58.0 | needs a arena (build cost 26,636); thin at home: protection, light armour, arms; needs weaponry skill |
| hold sermon 2 | church | 24 | 54.7 | 58.3 | needs a church (build cost 81,919); thin at home: furniture |
| hold banquet 3 (fish) | mansion | 7.6 | 58.6 | 58.6 | thin at home: cured fish |
| hold banquet 3 (meat) | mansion | 7.6 | 58.6 | 58.6 |  |
| hold banquet 1 (fish) | mansion | 4.2 | 59.4 | 59.4 | thin at home: cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 59.5 | 59.5 | thin at home: wine, cured fish |
| hold banquet 2 (meat) | mansion | 6.8 | 59.5 | 59.5 | thin at home: wine |
| hold banquet 1 (meat) | mansion | 4.2 | 60.1 | 60.1 |  |
| hold banquet 3 (pies) | mansion | 8 | 60.2 | 60.2 | thin at home: pies, candles |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 64601365 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Disscester: garments sell 28 @ 23.8; crew 0.2; est +77 a turn
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn
- best towns now: Disscester +77, Karlmoor +22
- Disscester would trade: garments sell 28 @ 23.8; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~101 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Disscester | 1474 | 0.58 | 0.20 (20/turn) | garments 28 (20.18->24.13) | - | +90 |
| Bremcop | 1326 | 0.50 | 0.20 (20/turn) | garments 33 (20.18->23.18), glassware 1 (50.19->54.62) | steel ingots 1 (13.65->15.67) | +85 |
| Karlmoor | 787 | 0.21 | 0.10 (10/turn) | rope 3 (79->96.9), tackles 1 (174.3->191.9), flax fibres 4 (4.93->7.93), stockfish 1 (123.9->133) | flax plants 1 (1.48->2), wine 2 (5.67->6.13), yarn 3 (3.59->3.93) | +84 |
| Hofkirchen | 991 | 0.32 | 0.20 (20/turn) | flax plants 15 (1.41->3.89), salt 6 (4.3->5.7), glassware 1 (50.19->52.25) | candles 7 (69.3->71.25), wrought iron 10 (11.55->12.92), cloth 12 (7.77->8.4), bronze ingots 1 (22.26->22.8) | +62 |
| Hanstein | 380 | 0.10 | 0.30 (30/turn) | salt 5 (4.3->5.42), glassware 1 (50.19->52.72), grain 4 (2.46->2.72), tools 9 (4.46->4.62) | flax plants 75 (1.29->2), cloth 12 (7.35->8.4), seeds 11 (1.77->2.32), cheese 27 (5.72->5.94) | +57 |

**Best:** Disscester at about +90 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 28.2, stop 1 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 0 = 1.0 turns |
| beer |  | 48 @ min 3.7 | makes 28.0, uses 4.2, holds 377 (keeps 60): sells the surplus + 24/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| furniture | 2 @ 15.5, stop 6 |  | uses 1.4/turn (household upkeep), makes 0.0, holds 10 = 7.3 turns |
| garments |  | 45 @ min 22.0 | makes 22.1, uses 2.1, holds 352 (keeps 30): sells the surplus + 25/turn of the excess |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 195 @ 2.2, stop - |  | uses 644.6/turn (brewery 1, flax farm 1, household), makes 450.0, holds 241 = 1.2 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 38.0 |  |
| porterage | 9 @ 1.1, stop - |  | uses 9.4/turn (observed), makes 0.0, holds 11 = 1.2 turns |
| rope |  | 6 @ min 77.0 | makes 2.2, uses 0.0, holds 47 (keeps 0): sells the surplus + 4/turn of the excess |
| timber |  | 9 @ min 7.0 |  |
| tools | 4 @ 6.2, stop 28 |  | uses 3.4/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 58.3 turns |

## Chain sizing

Mode HOLD, garments sold 3.2/turn (+4.9 exported); plan makes 20.9 garments a turn.
Labour: own 450, everything else 362, chain may buy 350 -> chain allowance 438, chain plan 344 (-12 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.72 | 4.63 |
| ret | 3 | 0.84 | 0.82 |
| spin | 4 | 1.73 | 1.70 |
| weave | 3 | 0.87 | 0.82 |
| sew | 2 | 0.54 | 0.51 |

Buffers: flax fibres 58/71, thread 443/209, cloth 35/82

## Self-diagnosis

- R1: arms slot dry: 0.5 held, 0.5 a turn (gear slot (+0.4 prestige)); our buy paused by the failsafe, home ask 27.0 (held back: paused by the failsafe at level 2: un-pause only at level 0)
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
