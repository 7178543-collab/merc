# v2 shadow report

Turn 13361, 2026-10-18 02:54. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 7,422, prestige 3,270 (600 free, -1.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 234 | 0 | 4 | 0 | 0 | min_holding 60, sell 34, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 207 | 0 | 2 | 0 | 0 | min_holding 30, sell 36, sell @ 22 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 261 | 282 | 712 | 0 | 20 | buy 261, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 15 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 38.6 |
| porterage | 11 | 11 | 10 | 0 | 1 | buy 11, buy @ 1.1 |

**1 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.6 turns (holds 35, next step uses 57/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **labour**: 20 labour expired last turn (~34 coin): holding 261 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax fibres**: flax fibres buffer thin: 1.7 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 68

## Notes

- labour: projection runs 74 over real use lately; planning 725, not 799

## Prestige spending, cheapest coin per prestige first

1040 turns left: prestige gained now converts 99.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.3 | 51.3 | running |
| hold sermon 2 (candles) | church | 31 | 52.9 | 55.7 | needs a church (build cost 81,515); thin at home: jewellery, candles |
| hold banquet 3 (pies) | mansion | 8 | 56.2 | 56.2 | thin at home: pies |
| hold banquet 2 (pies) | mansion | 7 | 58.3 | 58.3 | thin at home: wine, pies |
| hold prayer 2 | chapel | 13 | 55.8 | 58.5 | needs a chapel (build cost 33,738) |
| hold banquet 3 (fish) | mansion | 7.6 | 59.4 | 59.4 | thin at home: cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 59.6 | 59.6 | thin at home: cured fish |
| hold banquet 3 (meat) | mansion | 7.6 | 59.7 | 59.7 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 59.8 | 59.8 | thin at home: wine, cured fish |
| hold banquet 4 (pies) | mansion | 18 | 59.8 | 59.8 | thin at home: wine, pies, glassware |
| hold sermon 2 | church | 24 | 56.5 | 60.1 | needs a church (build cost 81,515); thin at home: jewellery |
| hold banquet 2 (meat) | mansion | 6.8 | 60.2 | 60.2 | thin at home: wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 64601365 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Disscester: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn
- best towns now: Briclives +65, Kleinburgh +40, Birkeningen +34, Rouhomme +30, Etallaen +29
- Briclives would trade: garments sell 34 @ 22.8; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~103 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Briclives | 1041 | 0.35 | 0.20 (21/turn) | garments 34 (20.12->23.94), candles 2 (59.85->74.58), salt 12 (4.24->4.99), cured meat 2 (22.4->24.51) | - | +153 |
| Rouhomme | 368 | 0.10 | 0.20 (21/turn) | beer 38 (2.97->4.6), candles 2 (59.85->66.97), salt 4 (4.24->5.37), lead ore 2 (8.56->10.64) | thread 32 (5.08->5.45), cloth 7 (7.46->8.2), dyed yarn 1 (4.37->9.5), flax plants 1 (1.43->1.84) | +91 |
| Birkeningen | 1006 | 0.34 | 0.20 (21/turn) | garments 21 (20.12->22.8), tackles 1 (178.5->199.5), rope 2 (79->84.08), salt 5 (4.24->5.42) | thread 10 (4.73->5.45), steel ingots 1 (14.18->15.2) | +88 |
| Caillechâtel | 488 | 0.13 | 0.20 (21/turn) | beer 23 (2.97->4.71), candles 2 (59.85->69.35), cloth 3 (8.15->9.07), canvas 2 (33.39->34.2) | thread 34 (4.81->5.45), flax plants 36 (1.42->1.84) | +79 |
| Karlmoor | 787 | 0.22 | 0.10 (10/turn) | garments 18 (20.12->22.42), tackles 1 (178.5->195.7), salt 14 (4.24->5.27) | flax fibres 2 (5.62->6.2), flour 1 (17.32->19.38) | +64 |

**Best:** Briclives at about +153 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 36 @ min 3.7 | makes 28.0, uses 4.2, holds 234 (keeps 60): sells the surplus + 13/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.1 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 40 @ min 22.0 | makes 29.1, uses 2.1, holds 207 (keeps 30): sells the surplus + 13/turn of the excess |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 275 @ 2.2, stop - |  | uses 725.0/turn (brewery 1, flax farm 1, household), makes 450.0, holds 261 = 0.9 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 38.4 |  |
| porterage | 10 @ 1.1, stop - |  | uses 10.3/turn (observed), makes 0.0, holds 11 = 1.1 turns |
| rope |  | 7 @ min 77.0 | makes 2.2, uses 0.0, holds 60 (keeps 0): sells the surplus + 5/turn of the excess |
| timber |  | 14 @ min 6.7 | makes 8.4, uses 0.0, holds 430 (keeps 350): sells the surplus + 6/turn of the excess |
| tools | 4 @ 6.2, stop 30 |  | uses 3.7/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 53.7 turns |

## Chain sizing

Mode HOLD, garments sold 8.3/turn (+4.9 exported); plan makes 29.1 garments a turn.
Labour: own 450, everything else 362, chain may buy 350 -> chain allowance 438, chain plan 434 (-3 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.52 | 5.44 |
| ret | 3 | 0.98 | 0.97 |
| spin | 4 | 2.02 | 1.99 |
| weave | 3 | 1.14 | 1.13 |
| sew | 2 | 0.71 | 0.71 |

Buffers: flax fibres 59/82, thread 489/240, cloth 35/113

## Self-diagnosis

- R2: ropewalk 1 blocked by rope space: 60 held of 60 capacity, we make 2.2 a turn; no buy on it: add a sell order or more capacity for rope
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
