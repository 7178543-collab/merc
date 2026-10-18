# v2 shadow report

Turn 13360, 2026-10-18 01:06. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 7,785, prestige 3,271 (601 free, -1.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 211 | 0 | 4 | 0 | 0 | min_holding 60, sell 30, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 17 | 5 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 180 | 0 | 2 | 0 | 0 | min_holding 30, sell 32, sell @ 22 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 282 | 282 | 711 | 0 | 21 | buy 282, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 15 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 37.6 |
| porterage | 11 | 11 | 10 | 0 | 1 | buy 11, buy @ 1.1 |

**1 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.6 turns (holds 35, next step uses 54/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **labour**: 21 labour expired last turn (~36 coin): holding 282 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.7 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 71

## Notes

- labour: projection runs 73 over real use lately; planning 711, not 785

## Prestige spending, cheapest coin per prestige first

1041 turns left: prestige gained now converts 99.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 52.2 | 52.2 | running |
| jousting 1 | arena | 170 | 57.4 | 57.6 | needs a arena (build cost 25,816); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 57.7 | 57.7 | thin at home: wine |
| hold banquet 3 (meat) | mansion | 7.6 | 58.4 | 58.4 |  |
| hold prayer 2 | chapel | 13 | 56.0 | 58.5 | needs a chapel (build cost 32,718) |
| hold banquet 1 (meat) | mansion | 4.2 | 58.8 | 58.8 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 59.1 | 59.1 | thin at home: wine, cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 59.7 | 59.7 | thin at home: cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 59.8 | 59.8 | thin at home: cured fish |
| hold feast 2 | townhouse | 2.6 | 57.6 | 60.3 | needs a townhouse (build cost 7,206); thin at home: wine |
| hold sermon 2 (candles) | church | 31 | 57.5 | 60.3 | needs a church (build cost 81,554); thin at home: jewellery, candles |
| hold sermon 2 | church | 24 | 57.4 | 61.0 | needs a church (build cost 81,554); thin at home: jewellery |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 64601365 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Disscester: nothing pays; crew 0.0; est +0 a turn; best orders clear only -4 a turn after crew: ship stays at 0
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn
- best towns now: Briclives +55, Kleinburgh +48, Rouhomme +32, Etallaen +25, Chatgnan +18
- Briclives would trade: garments sell 35 @ 22.4; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~104 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Briclives | 1041 | 0.36 | 0.30 (31/turn) | garments 35 (20.07->22.8), grindstones 1 (443.1->536.75) | thread 1 (5.25->5.7) | +158 |
| Heidlowe | 662 | 0.18 | 0.30 (31/turn) | soap 1 (89.78->116.85), dyed cloth 1 (11.45->12.44), honey 1 (8.72->8.93) | thread 63 (4.83->5.7), flax fibres 27 (5.51->6.3), candles 1 (76.65->81), cloth 11 (7.56->8.15) | +91 |
| Rouhomme | 368 | 0.10 | 0.10 (10/turn) | beer 36 (2.96->4.56), lead ore 4 (8.45->10.26), paper 1 (23.31->24.7) | thread 32 (5.19->5.7), lead bars 21 (11.03->11.4), dyed yarn 1 (4.58->9.21), candles 1 (77.7->81) | +83 |
| Cobholme | 1564 | 0.65 | 0.20 (21/turn) | cured fish 7 (26.04->33.25), light armour 2 (83.48->95), glassware 1 (57.75->59.85) | ploughs 2 (63->71.25), wool 3 (9.13->10.92), candles 1 (79.28->81) | +68 |
| Kleinburgh | 1440 | 0.58 | 0.20 (21/turn) | garments 25 (20.07->22.23), nets 2 (39.6->41.61) | wool 3 (7.46->10.92), nails 3 (3.46->5.46), candles 1 (79.8->81), steel ingots 1 (13.76->15.11) | +56 |

**Best:** Briclives at about +158 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 34 @ min 3.7 | makes 28.0, uses 4.2, holds 211 (keeps 60): sells the surplus + 11/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 17 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 36 @ min 22.0 | makes 27.9, uses 2.1, holds 180 (keeps 30): sells the surplus + 10/turn of the excess |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 261 @ 2.2, stop - |  | uses 711.5/turn (brewery 1, flax farm 1, household), makes 450.0, holds 282 = 1.1 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 38.6 |  |
| porterage | 10 @ 1.1, stop - |  | uses 10.5/turn (observed), makes 0.0, holds 11 = 1.0 turns |
| rope |  | 7 @ min 77.0 | makes 2.2, uses 0.0, holds 60 (keeps 0): sells the surplus + 5/turn of the excess |
| timber |  | 15 @ min 6.7 | makes 8.4, uses 0.0, holds 442 (keeps 350): sells the surplus + 7/turn of the excess |
| tools | 4 @ 6.2, stop 31 |  | uses 3.8/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 52.8 turns |

## Chain sizing

Mode HOLD, garments sold 10.5/turn (+4.9 exported); plan makes 29.1 garments a turn.
Labour: own 450, everything else 362, chain may buy 350 -> chain allowance 438, chain plan 438 (+1 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.71 | 5.52 |
| ret | 3 | 1.02 | 0.98 |
| spin | 4 | 2.09 | 2.02 |
| weave | 3 | 1.08 | 1.14 |
| sew | 2 | 0.68 | 0.71 |

Buffers: flax fibres 59/82, thread 476/241, cloth 35/114
- chain plan needed 456 labour, budget left 438: cut to 438 (sewing capped at 0.71)

## Self-diagnosis

- R2: ropewalk 1 blocked by rope space: 60 held of 60 capacity, we make 2.2 a turn; no buy on it: add a sell order or more capacity for rope
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
