# v2 shadow report

Turn 13362, 2026-10-18 03:56. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 7,005, prestige 3,269 (599 free, -1.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 258 | 0 | 4 | 0 | 0 | min_holding 60, sell 34, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 5 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 234 | 0 | 2 | 0 | 0 | min_holding 30, sell 36, sell @ 22 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 261 | 261 | 711 | 1 | 0 | buy 261, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 38.6 |
| porterage | 11 | 11 | 10 | 0 | 1 | buy 11, buy @ 1.1 |

**1 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.6 turns (holds 35, next step uses 57/turn) -> v2: check the step that makes it

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax fibres**: flax fibres buffer thin: 1.7 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 68

## Notes

- labour: projection runs 75 over real use lately; planning 724, not 799

## Prestige spending, cheapest coin per prestige first

1039 turns left: prestige gained now converts 99.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.3 | 51.3 | running |
| hold sermon 2 (candles) | church | 31 | 52.6 | 55.4 | needs a church (build cost 81,391); thin at home: jewellery, candles, furniture |
| hold banquet 3 (pies) | mansion | 8 | 55.9 | 55.9 | thin at home: pies, candles |
| hold banquet 2 (meat) | mansion | 6.8 | 57.0 | 57.0 | thin at home: wine |
| hold banquet 2 (pies) | mansion | 7 | 57.1 | 57.1 | thin at home: wine, pies, candles |
| hold banquet 3 (meat) | mansion | 7.6 | 57.6 | 57.6 |  |
| hold prayer 2 | chapel | 13 | 55.4 | 58.0 | needs a chapel (build cost 32,886); thin at home: furniture |
| jousting 1 | arena | 170 | 58.1 | 58.3 | needs a arena (build cost 25,999); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 58.4 | 58.4 | thin at home: wine, cured fish |
| hold banquet 1 (meat) | mansion | 4.2 | 58.7 | 58.7 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 58.9 | 58.9 | thin at home: cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 59.7 | 59.7 | thin at home: cured fish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 64601365 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.01 | 1 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Disscester: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn
- best towns now: Etallaen +84, Briclives +78, Karlmoor +40, Caillechâtel +36
- Etallaen would trade: garments sell 41 @ 22.6; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~103 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Etallaen | 774 | 0.21 | 0.40 (41/turn) | garments 41 (20.15->23.37), beer 40 (2.97->3.61), cured meat 2 (21.68->23.75), bricks 1 (6.83->11.49) | cloth 21 (7.35->8.45), thread 7 (4.12->5.45), grain 13 (3.15->3.66), mouldboards 1 (39.48->40.47) | +165 |
| Bordetes | 831 | 0.24 | 0.10 (10/turn) | grindstones 1 (443.1->551), candles 1 (59.85->60.8), rope 1 (79->79.8) | mouldboards 1 (36.96->40.47), thread 24 (5.17->5.45), garments 2 (21.21->21.6), tools 3 (4.81->5.1) | +106 |
| Briclives | 1041 | 0.35 | 0.20 (21/turn) | garments 34 (20.15->23.18), salt 10 (4.22->5.03), tackles 1 (177.45->180.5), cured meat 2 (21.68->22.42) | - | +96 |
| Karlmoor | 787 | 0.22 | 0.10 (10/turn) | garments 17 (20.15->23.56), tackles 1 (177.45->195.7), tools 10 (4.24->5.22), glassware 1 (55.65->59.85) | grain 13 (2.62->3.66), flax fibres 2 (5.41->6.3) | +92 |
| Cobholme | 1564 | 0.65 | 0.70 (72/turn) | cured fish 6 (26.04->36.29), beer 40 (2.97->4.71), candles 1 (59.85->68.4), light armour 1 (83.48->92.15) | - | +84 |

**Best:** Etallaen at about +165 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 38 @ min 3.7 | makes 28.0, uses 4.2, holds 258 (keeps 60): sells the surplus + 15/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 42 @ min 22.0 | makes 29.1, uses 2.1, holds 234 (keeps 30): sells the surplus + 15/turn of the excess |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 274 @ 2.2, stop - |  | uses 723.8/turn (brewery 1, flax farm 1, household), makes 450.0, holds 261 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 38.0 |  |
| porterage | 10 @ 1.1, stop - |  | uses 10.3/turn (observed), makes 0.0, holds 11 = 1.1 turns |
| rope |  | 7 @ min 77.0 | makes 2.2, uses 0.0, holds 60 (keeps 0): sells the surplus + 5/turn of the excess |
| timber |  | 13 @ min 6.7 | makes 8.4, uses 0.0, holds 419 (keeps 350): sells the surplus + 5/turn of the excess |
| tools | 4 @ 6.2, stop 30 |  | uses 3.7/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 53.8 turns |

## Chain sizing

Mode HOLD, garments sold 7.6/turn (+4.9 exported); plan makes 27.5 garments a turn.
Labour: own 450, everything else 362, chain may buy 350 -> chain allowance 438, chain plan 413 (-25 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.52 | 5.19 |
| ret | 3 | 0.98 | 0.92 |
| spin | 4 | 2.02 | 1.90 |
| weave | 3 | 1.14 | 1.08 |
| sew | 2 | 0.71 | 0.67 |

Buffers: flax fibres 59/80, thread 502/235, cloth 35/108

## Self-diagnosis

- R2: ropewalk 1 blocked by rope space: 60 held of 60 capacity, we make 2.2 a turn; no buy on it: add a sell order or more capacity for rope
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
