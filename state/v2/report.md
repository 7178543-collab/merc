# v2 shadow report

Turn 13355, 2026-10-17 20:50. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 8,216, prestige 3,278 (608 free, -1.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 148 | 0 | 4 | 0 | 0 | min_holding 60, sell 29, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 17 | 5 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 138 | 0 | 2 | 0 | 0 | min_holding 30, sell 32, sell @ 22 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 301 | 274 | 724 | 33 | 0 | buy 301, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 15 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 37.8 |
| porterage | 11 | 11 | 7 | 0 | 4 | buy 11, buy @ 1.1 |

**1 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.6 turns (holds 30, next step uses 46/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **Flax Wyrm**: Flax Wyrm cost 90 coin last turn (crew 0.89) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.6 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 71
- **grain**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 73 over real use lately; planning 757, not 830

## Prestige spending, cheapest coin per prestige first

1046 turns left: prestige gained now converts 99.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.7 | 50.7 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 56.4 | 56.4 |  |
| hold sermon 2 (candles) | church | 31 | 54.4 | 57.0 | needs a church (build cost 76,721); thin at home: jewellery, candles, furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 57.4 | 57.4 | thin at home: wine, cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 57.8 | 57.8 | thin at home: cured fish |
| hold sermon 2 | church | 24 | 54.6 | 57.9 | needs a church (build cost 76,721); thin at home: jewellery, furniture |
| hold banquet 1 (meat) | mansion | 4.2 | 58.7 | 58.7 |  |
| hold banquet 2 (meat) | mansion | 6.8 | 58.8 | 58.8 | thin at home: wine |
| hold prayer 2 | chapel | 13 | 56.4 | 58.9 | needs a chapel (build cost 31,992); thin at home: furniture |
| hold banquet 3 (meat) | mansion | 7.6 | 59.1 | 59.1 |  |
| hold mass 1 | cathedral | 180 | 57.3 | 59.3 | needs a cathedral (build cost 343,520); thin at home: jewellery, glassware, candles |
| jousting 1 | arena | 170 | 59.7 | 59.8 | needs a arena (build cost 24,715); thin at home: protection, light armour, arms; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.89 / 0.89 | 90 | 64601365 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Disscester: garments sell 30 @ 27.0; crew 0.2; est +125 a turn
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn
- best towns now: Disscester +125, Caillechâtel +61
- Disscester would trade: garments sell 30 @ 27.0; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~102 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Disscester | 1474 | 0.59 | 0.30 (31/turn) | garments 30 (19.82->35.34), tools 16 (4.48->5.37), stockfish 1 (118.65->123.5), dyed cloth 2 (11.03->11.88) | cheese 5 (6.35->7.12) | +459 |
| Caillechâtel | 488 | 0.13 | 0.10 (10/turn) | beer 26 (2.91->7.5), garments 10 (19.82->20.14), tools 5 (4.48->4.84), dyed cloth 2 (11.03->11.4) | bricks 1 (5.41->14.82), cloth 15 (8.29->8.9), cheese 5 (6.14->7.12), nets 1 (34.44->36.86) | +139 |
| Neuborn | 780 | 0.21 | 0.20 (20/turn) | glassware 1 (58.28->61.75), charcoal 11 (2.33->4.1) | cheese 57 (5.25->7.12), bricks 1 (5.72->14.82), cloth 6 (8.14->8.9), salt 4 (4.54->5.51) | +110 |
| Rouhomme | 368 | 0.10 | 0.10 (10/turn) | beer 31 (2.91->3.8), rope 1 (75.5->85.5), cured meat 2 (21.68->26.03), nails 3 (5.78->7.31) | spinning wheels 1 (216.3->258.4), bricks 1 (5.15->14.82), lead ore 1 (1.84->7.31), dyed yarn 1 (8.4->9.45) | +99 |
| Kirchwerp | 1072 | 0.37 | 0.40 (41/turn) | lead ore 1 (8.29->23.94), flax fibres 5 (4.98->6.17) | cheese 41 (5.72->7.12), cloth 21 (7.77->8.9), acid 1 (121.8->131.1), bricks 1 (5.21->14.82) | +82 |

**Best:** Disscester at about +459 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 29 @ min 3.7 | makes 28.0, uses 4.2, holds 148 (keeps 60): sells the surplus + 5/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 17 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 29 @ min 22.0 | makes 23.8, uses 2.1, holds 138 (keeps 30): sells the surplus + 7/turn of the excess |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 307 @ 2.2, stop - |  | uses 757.0/turn (brewery 1, flax farm 1, household), makes 450.0, holds 301 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 37.8 |  |
| porterage | 11 @ 1.1, stop - |  | uses 10.5/turn (observed), makes 0.0, holds 11 = 1.0 turns |
| rope |  | 7 @ min 73.5 | makes 2.2, uses 0.0, holds 58 (keeps 0): sells the surplus + 5/turn of the excess |
| timber |  | 20 @ min 7.3 | makes 8.4, uses 0.0, holds 500 (keeps 350): sells the surplus + 12/turn of the excess |
| tools | 4 @ 6.2, stop 31 |  | uses 3.8/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 52.5 turns |

## Chain sizing

Mode HOLD, garments sold 11.8/turn (+0.0 exported); plan makes 27.5 garments a turn.
Labour: own 450, everything else 362, chain may buy 350 -> chain allowance 438, chain plan 431 (+8 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.77 | 5.63 |
| ret | 3 | 1.03 | 1.00 |
| spin | 4 | 2.11 | 2.06 |
| weave | 3 | 1.08 | 1.07 |
| sew | 2 | 0.58 | 0.67 |

Buffers: flax fibres 58/80, thread 401/234, cloth 30/107

## Self-diagnosis

- R1: prestige rate -1.29 a turn vs 12-turn median +2.94; likely: no slot, building or contract cause found: check the impacts
- R3: mansion 1 (mansion) finished but idle 5 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
