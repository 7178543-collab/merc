# v2 shadow report

Turn 13322, 2026-10-16 11:56. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,624, prestige 3,222 (552 free, -4.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 272 | 0 | 4 | 0 | 0 | min_holding 60, sell 40, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 5 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 35 | 0 | 2 | 0 | 0 | min_holding 30, sell 22, sell @ 22 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 286 | 286 | 727 | 0 | 9 | buy 286, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 51 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 36 |
| porterage | 21 | 21 | 13 | 0 | 8 | buy 21, buy @ 1.1 |

**1 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.2 turns (holds 9, next step uses 46/turn) -> v2: check the step that makes it

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.7 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 72
- **flax plants**: flax plants buffer thin: 1.8 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 187

## Notes

- labour: projection runs 73 over real use lately; planning 727, not 801

## Prestige spending, cheapest coin per prestige first

1079 turns left: prestige gained now converts 99.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 52.2 | 52.2 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 57.2 | 57.2 | thin at home: wine, cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 57.7 | 57.7 | thin at home: hop beer, cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 58.9 | 58.9 |  |
| hold banquet 2 (meat) | mansion | 6.8 | 60.1 | 60.1 | thin at home: wine |
| hold feast 2 | townhouse | 2.6 | 57.6 | 60.1 | needs a townhouse (build cost 6,746); thin at home: wine |
| hold banquet 3 (pies) | mansion | 8 | 60.2 | 60.2 | thin at home: pasties, hop beer, pies |
| hold banquet 3 (meat) | mansion | 7.6 | 60.3 | 60.3 | thin at home: hop beer |
| hold prayer 2 | chapel | 13 | 57.9 | 60.3 | needs a chapel (build cost 31,416); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 57.7 | 60.4 | needs a church (build cost 80,346); thin at home: jewellery, candles, furniture |
| hold banquet 2 (pies) | mansion | 7 | 61.1 | 61.1 | thin at home: pasties, wine, pies |
| hold sermon 2 | church | 24 | 57.9 | 61.3 | needs a church (build cost 80,346); thin at home: jewellery, furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 74001604 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Brunnham: nothing pays; crew 0.0; est +0 a turn; best orders clear only 1 a turn after crew: ship stays at 0
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn; best orders clear only 13 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~105 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Amsdermund | 1111 | 0.40 | 0.30 (31/turn) | garments 22 (20.3->23.94), canvas 2 (32.13->37.81), varnish 1 (19.01->23.56), nails 2 (4.48->6.17) | cloth 29 (7.77->8.65), cheese 17 (5.25->5.89), wrought iron 5 (10.82->11.97), cured meat 6 (22.05->23.37) | +120 |
| Kirchwerp | 1072 | 0.38 | 0.20 (21/turn) | tools 16 (4.76->5.7), butter 2 (71.4->76), grain 4 (2.26->3.34), wine 5 (6.56->7.17) | acid 1 (105->162.45), cloth 19 (8.03->8.65), gears 1 (70.35->73.15) | +82 |
| Darmwald | 1022 | 0.35 | 0.10 (10/turn) | garments 22 (20.3->20.9), wheels 1 (15.6->20.71), tallow 1 (29.61->33.06) | acid 1 (132.3->162.45), cloth 11 (7.77->8.65) | +49 |
| Grandgues | 152 | 0.04 | 0.10 (10/turn) | beer 41 (2.9->3.59), wheels 1 (15.6->20.71), garments 22 (20.3->20.52), scythes 1 (28.35->32.11) | slaked lime 2 (6.83->7.55), resin 1 (2.01->2.24) | +48 |
| Briclives | 1041 | 0.36 | 0.40 (42/turn) | beer 41 (2.9->3.76), garments 22 (20.3->20.9), thread 1 (4.66->5.03) | acid 1 (127.05->162.45), slaked lime 2 (6.04->7.55), steel ingots 1 (13.55->14.82) | +47 |

**Best:** Amsdermund at about +120 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 39 @ min 3.7 | makes 28.0, uses 4.2, holds 272 (keeps 60): sells the surplus + 16/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 22 @ min 22.0 |  |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 277 @ 2.2, stop - |  | uses 727.2/turn (brewery 1, flax farm 1, household), makes 450.0, holds 286 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 11 @ min 36.0 | makes 9.0, uses 0.0, holds 51 (keeps 15): sells the surplus + 2/turn of the excess |
| porterage | 13 @ 1.1, stop - |  | uses 12.5/turn (observed), makes 0.0, holds 21 = 1.7 turns |
| rope |  | 5 @ min 76.0 |  |
| tar | 2 @ 11.0, stop 5 |  | uses 1.0/turn (ropewalk 1), makes 0.0, holds 10 = 9.5 turns |
| timber |  | 37 @ min 8.5 | makes 12.0, uses 0.0, holds 667 (keeps 350): sells the surplus + 25/turn of the excess |
| tools | 5 @ 6.2, stop 37 |  | uses 4.6/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 43.7 turns |

## Chain sizing

Mode HOLD, garments sold 4.5/turn (+0.0 exported); plan makes 23.0 garments a turn.
Labour: own 450, everything else 385, chain may buy 350 -> chain allowance 415, chain plan 415 (+2 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.85 | 5.94 |
| ret | 3 | 1.04 | 1.06 |
| spin | 4 | 2.14 | 2.17 |
| weave | 3 | 0.92 | 0.90 |
| sew | 2 | 0.58 | 0.56 |

Buffers: flax fibres 64/92, thread 599/272, cloth 9/90
- chain plan needed 525 labour, budget left 415: cut to 415 (sewing capped at 0.56)

## Self-diagnosis

- R1: candles slot dry: 0.0 held, 1.5 a turn (luxury slot (+3 prestige)); our buy paused by the failsafe, home ask 80.0 (held back: paused by the failsafe at level 1: un-pause only at level 0)
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 3 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
