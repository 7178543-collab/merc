# v2 shadow report

Turn 13363, 2026-10-18 04:55. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 6,789, prestige 3,267 (597 free, -1.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 282 | 0 | 4 | 0 | 0 | min_holding 60, sell 34, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 17 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 260 | 0 | 2 | 0 | 0 | min_holding 30, sell 36, sell @ 22 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 261 | 261 | 687 | 0 | 24 | buy 261, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 38.6 |
| porterage | 11 | 11 | 10 | 0 | 1 | buy 11, buy @ 1.1 |

**1 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.7 turns (holds 35, next step uses 54/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **labour**: 24 labour expired last turn (~41 coin): holding 261 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax fibres**: flax fibres buffer thin: 1.8 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 64

## Notes

- labour: projection runs 75 over real use lately; planning 698, not 773

## Prestige spending, cheapest coin per prestige first

1038 turns left: prestige gained now converts 99.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.0 | 51.0 | running |
| hold sermon 2 (candles) | church | 31 | 52.8 | 55.6 | needs a church (build cost 81,986); thin at home: jewellery, candles, furniture |
| hold prayer 2 | chapel | 13 | 55.3 | 58.0 | needs a chapel (build cost 33,156); thin at home: furniture |
| hold banquet 3 (pies) | mansion | 8 | 58.3 | 58.3 | thin at home: pies, candles |
| jousting 1 | arena | 170 | 58.6 | 58.8 | needs a arena (build cost 26,249); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 59.2 | 59.2 | thin at home: wine, cured meat |
| hold banquet 2 (fish) | mansion | 6.8 | 59.4 | 59.4 | thin at home: wine, cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 59.5 | 59.5 | thin at home: cured fish |
| hold banquet 3 (meat) | mansion | 7.6 | 59.5 | 59.5 | thin at home: cured meat |
| hold banquet 3 (fish) | mansion | 7.6 | 59.8 | 59.8 | thin at home: cured fish |
| hold sermon 2 | church | 24 | 56.2 | 59.8 | needs a church (build cost 81,986); thin at home: jewellery, furniture |
| hold banquet 1 (meat) | mansion | 4.2 | 59.9 | 59.9 | thin at home: cured meat |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 64601365 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Disscester: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn
- best towns now: Briclives +84, Etallaen +76, Karlmoor +30, Cobholme +25, Birkeningen +23
- Briclives would trade: garments sell 34 @ 23.4; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~103 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Etallaen | 774 | 0.21 | 0.20 (21/turn) | garments 32 (20.17->24.51), glassware 1 (57.23->60.32), bricks 1 (7.25->13.68), cured meat 2 (22.4->23.56) | cloth 21 (7.35->8.85), thread 3 (3.65->5.1), flax fibres 3 (5.51->6.5), cheese 7 (6.14->6.55) | +173 |
| Karlmoor | 787 | 0.22 | 0.10 (10/turn) | garments 14 (20.17->24.7), tackles 1 (177.45->197.6), stockfish 1 (120.75->133), tools 10 (4.66->5.37) | cloth 11 (8.29->8.85), casks 1 (4.64->5.46), flax fibres 2 (6.04->6.5) | +100 |
| Briclives | 1041 | 0.35 | 0.20 (21/turn) | garments 34 (20.17->22.99), cured meat 2 (22.4->27.17), tackles 1 (177.45->181.45) | cloth 5 (8.19->8.85) | +93 |
| Hofkirchen | 991 | 0.32 | 0.30 (31/turn) | beer 42 (2.98->4.31), soap 2 (85.58->98.8), canvas 1 (33.39->34.58) | cloth 16 (7.77->8.85), cheese 23 (5.88->6.55), mouldboards 1 (36.54->40.66), jewellery 1 (78.75->81.22) | +84 |
| Gottweiler | 1135 | 0.40 | 0.30 (31/turn) | tools 16 (4.66->7.65) | cloth 31 (7.77->8.85), cheese 23 (5.72->6.55), paper 7 (19.95->20.71) | +74 |

**Best:** Etallaen at about +173 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 40 @ min 3.7 | makes 28.0, uses 4.2, holds 282 (keeps 60): sells the surplus + 17/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 17 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 42 @ min 22.0 | makes 27.5, uses 2.1, holds 260 (keeps 30): sells the surplus + 17/turn of the excess |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 248 @ 2.2, stop - |  | uses 697.6/turn (brewery 1, flax farm 1, household), makes 450.0, holds 261 = 1.1 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 38.2 |  |
| porterage | 10 @ 1.1, stop - |  | uses 9.9/turn (observed), makes 0.0, holds 11 = 1.1 turns |
| rope |  | 7 @ min 77.0 | makes 2.2, uses 0.0, holds 58 (keeps 0): sells the surplus + 5/turn of the excess |
| timber |  | 12 @ min 6.7 | makes 8.4, uses 0.0, holds 407 (keeps 350): sells the surplus + 4/turn of the excess |
| tools | 4 @ 6.2, stop 29 |  | uses 3.6/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 55.7 turns |

## Chain sizing

Mode HOLD, garments sold 6.7/turn (+4.9 exported); plan makes 26.2 garments a turn.
Labour: own 450, everything else 362, chain may buy 350 -> chain allowance 438, chain plan 394 (-19 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.19 | 4.97 |
| ret | 3 | 0.92 | 0.88 |
| spin | 4 | 1.90 | 1.82 |
| weave | 3 | 1.08 | 1.02 |
| sew | 2 | 0.67 | 0.64 |

Buffers: flax fibres 59/78, thread 511/229, cloth 35/102

## Self-diagnosis

- R2: ropewalk 1 blocked by rope space: 58 held of 60 capacity, we make 2.2 a turn; no buy on it: add a sell order or more capacity for rope
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
