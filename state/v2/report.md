# v2 shadow report

Turn 13357, 2026-10-17 22:46. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,651, prestige 3,275 (605 free, -1.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 158 | 0 | 4 | 0 | 0 | min_holding 60, sell 30, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 5 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 103 | 0 | 2 | 0 | 0 | min_holding 30, sell 28, sell @ 22 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 282 | 301 | 721 | 0 | 30 | buy 282, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 37.8 |
| porterage | 11 | 11 | 10 | 0 | 1 | buy 11, buy @ 1.1 |

**1 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.7 turns (holds 36, next step uses 54/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **labour**: 30 labour expired last turn (~51 coin): holding 282 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax fibres**: flax fibres buffer thin: 1.6 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 71

## Notes

- labour: projection runs 73 over real use lately; planning 723, not 797

## Prestige spending, cheapest coin per prestige first

1044 turns left: prestige gained now converts 99.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.3 | 51.3 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 56.0 | 56.0 | thin at home: wine, cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 56.5 | 56.5 | thin at home: cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 56.8 | 56.8 | thin at home: cured fish |
| hold banquet 2 (meat) | mansion | 6.8 | 57.2 | 57.2 | thin at home: wine |
| hold banquet 3 (pies) | mansion | 8 | 57.7 | 57.7 | thin at home: pies |
| hold banquet 3 (meat) | mansion | 7.6 | 57.8 | 57.8 |  |
| jousting 1 | arena | 170 | 58.0 | 58.1 | needs a arena (build cost 25,674); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 58.5 | 58.5 | thin at home: wine, pies |
| hold banquet 1 (meat) | mansion | 4.2 | 58.6 | 58.6 |  |
| hold prayer 2 | chapel | 13 | 56.3 | 58.9 | needs a chapel (build cost 32,764); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 57.1 | 59.8 | needs a church (build cost 81,057); thin at home: jewellery, candles, furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.20 | 20 | 64601365 | 0.116 | garments 29 | - | 493 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Disscester: candles buy 1 @ 72.5, garments sell 31 @ 30.0; crew 0.2; est +230 a turn
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn
- best towns now: Disscester +230
- Disscester would trade: candles buy 1 @ 72.5, garments sell 31 @ 30.0; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~103 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Disscester | 1474 | 0.59 | 0.20 (21/turn) | garments 31 (19.9->35.34), dyed cloth 2 (11.34->13.49) | jewellery 1 (92.92->127.3), candles 1 (75.08->78.5), ploughs 1 (61.95->70.77), wool 3 (8.98->10.54) | +506 |
| Rouhomme | 368 | 0.10 | 0.60 (62/turn) | beer 31 (2.93->3.76), bread 144 (2.44->2.83), lead ore 8 (7.72->9.88), flour 1 (18.79->28.88) | spinning wheels 2 (216.3->266), jewellery 1 (78.75->127.3), cookware 6 (21->23.18), bricks 1 (8.93->15.67) | +241 |
| Hofkirchen | 991 | 0.33 | 0.40 (41/turn) | flax plants 15 (1.26->3.89), flax fibres 5 (5.4->6.17) | jewellery 1 (78.75->127.3), spinning wheels 2 (256.2->266), cookware 6 (21->23.18), candles 1 (73.5->78.5) | +131 |
| Gottweiler | 1135 | 0.41 | 0.20 (21/turn) | garments 31 (19.9->22.42), paper 2 (23.73->25.08), salt 5 (4.16->4.94) | jewellery 1 (82.95->127.3), cheese 12 (5.25->6.41), cookware 6 (22.05->23.18), cloth 17 (7.77->8.35) | +130 |
| Grandgues | 152 | 0.04 | 0.10 (10/turn) | stockfish 1 (120.75->146.3), rope 2 (75.5->80.27), charcoal 10 (2.33->3.06), wine 3 (6.04->7.08) | jewellery 1 (88.73->127.3), cloth 23 (7.3->8.35), cookware 6 (22.05->23.18), bricks 1 (9.13->15.67) | +124 |

**Best:** Disscester at about +506 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 30 @ min 3.7 | makes 28.0, uses 4.2, holds 158 (keeps 60): sells the surplus + 6/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 30 @ min 22.0 | makes 27.9, uses 2.1, holds 103 (keeps 30): sells the surplus + 4/turn of the excess |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 273 @ 2.2, stop - |  | uses 723.4/turn (brewery 1, flax farm 1, household), makes 450.0, holds 282 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 37.4 |  |
| porterage | 10 @ 1.1, stop - |  | uses 10.5/turn (observed), makes 0.0, holds 11 = 1.0 turns |
| rope |  | 7 @ min 72.5 | makes 2.2, uses 0.0, holds 60 (keeps 0): sells the surplus + 5/turn of the excess |
| timber |  | 18 @ min 6.7 | makes 8.4, uses 0.0, holds 477 (keeps 350): sells the surplus + 10/turn of the excess |
| tools | 4 @ 6.2, stop 31 |  | uses 3.8/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 52.6 turns |

## Chain sizing

Mode HOLD, garments sold 11.5/turn (+2.5 exported); plan makes 28.3 garments a turn.
Labour: own 450, everything else 362, chain may buy 350 -> chain allowance 438, chain plan 438 (-1 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.71 | 5.66 |
| ret | 3 | 1.02 | 1.01 |
| spin | 4 | 2.09 | 2.07 |
| weave | 3 | 1.08 | 1.10 |
| sew | 2 | 0.68 | 0.69 |

Buffers: flax fibres 58/81, thread 418/237, cloth 36/110
- chain plan needed 484 labour, budget left 438: cut to 438 (sewing capped at 0.69)

## Self-diagnosis

- R1: prestige rate -1.28 a turn vs 12-turn median +2.91; likely: no slot, building or contract cause found: check the impacts
- R2: ropewalk 1 blocked by rope space: 60 held of 60 capacity, we make 2.2 a turn; no buy on it: add a sell order or more capacity for rope
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
