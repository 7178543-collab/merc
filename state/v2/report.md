# v2 shadow report

Turn 13346, 2026-10-17 11:48. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,839, prestige 3,268 (598 free, +3.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 142 | 0 | 19 | 0 | 0 | min_holding 60, sell 16, sell @ 4.56 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 33 | 0 | 2 | 0 | 0 | min_holding 30, sell 14, sell @ 22 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 310 | 299 | 732 | 0 | 17 | buy 310, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 22 | 0 | 0 | 0 | 0 | min_holding 15, sell 10, sell @ 35.6 |
| porterage | 11 | 11 | 11 | 0 | 0 | buy 11, buy @ 1.1 |

**1 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.7 turns (holds 24, next step uses 36/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **labour**: 17 labour expired last turn (~27 coin): holding 310 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.5 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 75
- **flax plants**: flax plants buffer thin: 1.9 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 194

## Notes

- labour: projection runs 73 over real use lately; planning 732, not 806

## Prestige spending, cheapest coin per prestige first

1055 turns left: prestige gained now converts 99.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.9 | 48.9 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 58.0 | 58.0 | thin at home: wine, cured fish |
| hold banquet 2 (meat) | mansion | 6.8 | 58.2 | 58.2 | thin at home: wine |
| hold banquet 3 (fish) | mansion | 7.6 | 58.3 | 58.3 | thin at home: cured fish |
| hold banquet 3 (meat) | mansion | 7.6 | 58.5 | 58.5 |  |
| hold prayer 2 | chapel | 13 | 56.5 | 58.7 | needs a chapel (build cost 27,921); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 57.1 | 59.5 | needs a church (build cost 73,317); thin at home: jewellery, candles, furniture |
| hold sermon 2 | church | 24 | 56.8 | 60.0 | needs a church (build cost 73,317); thin at home: jewellery, furniture |
| hold feast 2 | townhouse | 2.6 | 57.9 | 61.0 | needs a townhouse (build cost 8,196); thin at home: wine |
| hold banquet 4 (pies) | mansion | 18 | 62.5 | 62.5 | thin at home: wine |
| hold mass 2 (premium) | cathedral | 360 | 61.5 | 62.5 | needs a cathedral (build cost 333,781); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 3 (pies) | mansion | 8 | 63.0 | 63.0 | thin at home: pasties, pies |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 10 | 110801910 | 0.064 | nets 3 | - | 91 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | cured meat 5 | -103 |

## Ship plans (this turn's world prices)

- **linen snake** on Heilegg: candles buy 1 @ 74.0, nets sell 6 @ 41.6; crew 0.1; est +26 a turn
- **Flax Wyrm** on Karlmoor: nothing pays; crew 0.0; est +0 a turn
- best towns now: Clairas +41, Brunnham +30, Donaunieder +27, Heilegg +26, Bordetes +21
- Clairas would trade: candles buy 1 @ 77.5, grain buy 13 @ 2.54, nets sell 2 @ 38.6, rope sell 3 @ 85.5; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~98 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Fontaux | 411 | 0.11 | 0.50 (49/turn) | cheese 21 (6.62->9.79), salt 10 (4.07->7.79), garments 16 (19.39->20.71), tools 16 (4.5->5.37) | beer 48 (3.97->4.94), candles 1 (76.12->81), flax plants 7 (0.69->1.58), grain 13 (2.84->3.36) | +208 |
| Gosschweig | 1099 | 0.37 | 0.70 (69/turn) | soap 1 (80.85->153.9), thread 15 (4.66->5.22), wheels 1 (17.12->19.57), varnish 1 (19.84->21.66) | beer 90 (2.96->4.94), candles 1 (73.5->81) | +198 |
| Clairas | 374 | 0.10 | 0.20 (20/turn) | rope 3 (73->82.65), tools 16 (4.5->5.61), garments 16 (19.39->19.76), dyed cloth 1 (14.38->16.25) | beer 79 (3.3->4.94), grain 13 (2.62->3.36), candles 1 (80.85->81), flax plants 1 (1.02->1.58) | +176 |
| Toqueque | 642 | 0.17 | 0.40 (39/turn) | tackles 1 (169.05->237.5), nets 2 (36.6->41.04), medicine 1 (131.25->136.8), wheels 2 (17.12->20.14) | beer 90 (3.91->4.94), candles 1 (79.28->81), bricks 1 (7.4->11.69), grain 13 (2.92->3.36) | +166 |
| Grandgues | 152 | 0.04 | 0.20 (20/turn) | wheels 3 (17.12->22.04), rope 2 (73->80.27), salt 3 (4.07->7.41), garments 16 (19.39->19.95) | beer 90 (3.99->4.94), arms 6 (28.35->29.83), cloth 5 (7.3->8.45), grain 13 (2.88->3.36) | +162 |

**Best:** Fontaux at about +208 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ ?, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 3 = 6.0 turns |
| beer |  | 15 @ min 5.05 | makes 28.0, uses 19.2, holds 142 (keeps 60): sells the surplus + 6/turn of the excess |
| cured meat | 11 @ 24.4, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 15 = 2.5 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.1 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 16 @ min 22.0 |  |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 282 @ 2.2, stop - |  | uses 732.4/turn (brewery 1, flax farm 1, household), makes 450.0, holds 310 = 1.1 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 10 @ min 35.6 | sell; ships offer 6 a turn abroad, so home sells 10 (was 9) |
| porterage | 11 @ 1.1, stop - |  | uses 10.9/turn (observed), makes 0.0, holds 11 = 1.0 turns |
| rope |  | 8 @ min 71.0 | makes 4.5, uses 0.0, holds 45 (keeps 0): sells the surplus + 3/turn of the excess |
| tar | 2 @ 11.0, stop 5 |  | uses 1.1/turn (ropewalk 1), makes 0.0, holds 10 = 9.0 turns |
| timber |  | 29 @ min 6.7 | makes 8.4, uses 0.0, holds 610 (keeps 350): sells the surplus + 21/turn of the excess |
| tools | 4 @ 6.2, stop 32 |  | uses 3.9/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 51.1 turns |

## Chain sizing

Mode HOLD, garments sold 15.3/turn (+0.0 exported); plan makes 18.0 garments a turn.
Labour: own 450, everything else 411, chain may buy 350 -> chain allowance 389, chain plan 389 (+0 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 6.07 | 6.10 |
| ret | 3 | 1.08 | 1.08 |
| spin | 4 | 2.22 | 2.23 |
| weave | 3 | 0.72 | 0.71 |
| sew | 2 | 0.45 | 0.44 |

Buffers: flax fibres 58/86, thread 431/253, cloth 24/71
- chain plan needed 573 labour, budget left 389: cut to 389 (sewing capped at 0.44)

## Self-diagnosis

- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
