# v2 shadow report

Turn 13347, 2026-10-17 12:59. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,385, prestige 3,271 (601 free, +3.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 136 | 0 | 19 | 0 | 0 | min_holding 60, sell 15, sell @ 5.05 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 5 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 34 | 0 | 2 | 0 | 0 | min_holding 30, sell 16, sell @ 22 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 282 | 310 | 727 | 0 | 33 | buy 282, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 20 | 0 | 0 | 0 | 0 | min_holding 15, sell 10, sell @ 35.6 |
| porterage | 11 | 11 | 11 | 0 | 0 | buy 11, buy @ 1.1 |

**1 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.7 turns (holds 24, next step uses 36/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **labour**: 33 labour expired last turn (~54 coin): holding 282 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.5 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 75
- **flax plants**: flax plants buffer thin: 1.9 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 194

## Notes

- labour: projection runs 73 over real use lately; planning 727, not 787

## Prestige spending, cheapest coin per prestige first

1054 turns left: prestige gained now converts 99.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.8 | 49.8 | running |
| hold prayer 2 | chapel | 13 | 56.3 | 58.8 | needs a chapel (build cost 32,376); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 57.0 | 59.7 | needs a church (build cost 80,092); thin at home: jewellery, candles, furniture |
| hold sermon 2 | church | 24 | 56.7 | 60.2 | needs a church (build cost 80,092); thin at home: jewellery, furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 60.6 | 60.6 | thin at home: wine, cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 60.7 | 60.7 | thin at home: cured fish |
| hold feast 2 | townhouse | 2.6 | 58.2 | 61.2 | needs a townhouse (build cost 8,260); thin at home: wine |
| hold banquet 2 (meat) | mansion | 6.8 | 61.7 | 61.7 | thin at home: wine |
| hold banquet 3 (meat) | mansion | 7.6 | 61.7 | 61.7 |  |
| hold mass 2 (premium) | cathedral | 360 | 62.1 | 63.1 | needs a cathedral (build cost 354,401); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 4 (pies) | mansion | 18 | 63.6 | 63.6 | thin at home: wine |
| hold banquet 1 (fish) | mansion | 4.2 | 64.0 | 64.0 | thin at home: cured fish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 110801910 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | cured meat 5 | -107 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Karlmoor: cured meat buy 2 @ 21.4, nets sell 4 @ 48.4, rope sell 6 @ 83.5; crew 0.1; est +101 a turn
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn; best orders clear only -2 a turn after crew: ship stays at 0
- best towns now: Karlmoor +101, Clairas +36, Hofkirchen +20, Cobholme +18, Grandgues +17
- Karlmoor would trade: cured meat buy 2 @ 21.4, nets sell 4 @ 48.4, rope sell 6 @ 83.5; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~100 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Karlmoor | 787 | 0.21 | 0.30 (30/turn) | rope 6 (73->89.3), nets 7 (36.6->49.4), stockfish 1 (111.3->133), tackles 1 (169.05->185.25) | beer 46 (3.91->4.99), salt 7 (4.26->5.56), cured meat 2 (22.05->23.4) | +269 |
| Grandgues | 152 | 0.04 | 0.10 (10/turn) | rope 2 (73->80.27), garments 16 (19.4->19.95), wheels 2 (17.12->20.33), charcoal 13 (1.72->2.3) | beer 46 (3.99->4.99), arms 5 (28.35->32.49), flax fibres 7 (5.35->6.55), bricks 1 (7.35->11.88) | +123 |
| Hofkirchen | 991 | 0.31 | 0.40 (40/turn) | tackles 1 (169.05->185.25), wheels 2 (17.12->20.33), seeds 4 (2.52->3.59), flour 2 (19.01->22.04) | beer 46 (3.28->4.99), arms 5 (28.35->32.49), cured meat 6 (21->23.4), candles 1 (73.5->81.5) | +112 |
| Unterhufe | 595 | 0.16 | 0.20 (20/turn) | garments 14 (19.4->20.71), wheels 2 (17.12->20.9), tools 14 (4.5->4.73), cloth 2 (7.3->7.6) | beer 46 (3.07->4.99), candles 1 (76.65->81.5), bricks 1 (6.51->11.88), salt 1 (4.09->5.56) | +106 |
| Gottweiler | 1135 | 0.39 | 0.50 (50/turn) | garments 16 (19.4->21.09), hides 3 (15.75->16.91), slaked lime 1 (6.2->7.89) | beer 46 (3.07->4.99), arms 5 (28.35->32.49), salt 7 (4.05->5.56), cheese 13 (5.25->5.94) | +104 |

**Best:** Karlmoor at about +269 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ ?, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 5.0 turns |
| beer |  | 14 @ min 5.1 | makes 28.0, uses 19.2, holds 136 (keeps 60): sells the surplus + 6/turn of the excess |
| cured meat | 11 @ 24.4, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 15 = 2.5 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 16 @ min 22.0 |  |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 277 @ 2.2, stop - |  | uses 727.4/turn (brewery 1, flax farm 1, household), makes 450.0, holds 282 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 10 @ min 35.6 | sell; ships offer 4 a turn abroad, so home sells 10 (was 9) |
| porterage | 11 @ 1.1, stop - |  | uses 10.9/turn (observed), makes 0.0, holds 11 = 1.0 turns |
| rope |  | 6 @ min 71.0 | makes 2.2, uses 0.0, holds 50 (keeps 0): sells the surplus + 4/turn of the excess |
| tar | 2 @ 11.0, stop 5 |  | uses 1.0/turn (ropewalk 1), makes 0.0, holds 10 = 9.4 turns |
| timber |  | 29 @ min 6.7 | makes 8.4, uses 0.0, holds 607 (keeps 350): sells the surplus + 21/turn of the excess |
| tools | 4 @ 6.2, stop 32 |  | uses 3.9/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 51.1 turns |

## Chain sizing

Mode HOLD, garments sold 14.9/turn (+0.0 exported); plan makes 25.4 garments a turn.
Labour: own 450, everything else 397, chain may buy 350 -> chain allowance 403, chain plan 403 (+13 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 6.07 | 5.30 |
| ret | 3 | 1.08 | 0.94 |
| spin | 4 | 2.22 | 1.94 |
| weave | 3 | 0.72 | 0.99 |
| sew | 2 | 0.45 | 0.62 |

Buffers: flax fibres 58/77, thread 420/226, cloth 24/99
- chain plan needed 497 labour, budget left 403: cut to 403 (sewing capped at 0.62)

## Self-diagnosis

- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
