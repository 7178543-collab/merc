# v2 shadow report

Turn 13321, 2026-10-16 10:57. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,477, prestige 3,226 (556 free, -4.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 274 | 0 | 4 | 0 | 0 | min_holding 60, sell 40, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 35 | 0 | 2 | 0 | 0 | min_holding 30, sell 17, sell @ 22 |
| grain | 51 | 9 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 286 | 286 | 727 | 0 | 9 | buy 286, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 52 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 36 |
| porterage | 21 | 21 | 13 | 0 | 8 | buy 21, buy @ 1.1 |

**2 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.2 turns (holds 10, next step uses 46/turn) -> v2: check the step that makes it
- **labour**: buying 286, short of ~351 needed -> v2: buy 351

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax fibres**: flax fibres buffer thin: 1.7 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 72
- **flax plants**: flax plants buffer thin: 1.8 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 187

## Prestige spending, cheapest coin per prestige first

1080 turns left: prestige gained now converts 99.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 52.5 | 52.5 | running |
| hold sermon 2 (candles) | church | 31 | 57.8 | 60.5 | needs a church (build cost 83,043); thin at home: jewellery, candles, furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 60.9 | 60.9 | thin at home: cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 60.9 | 60.9 | thin at home: hop beer, cured fish |
| hold banquet 3 (pies) | mansion | 8 | 60.9 | 60.9 | thin at home: hop beer, pies, candles |
| hold feast 2 | townhouse | 2.6 | 58.5 | 61.0 | needs a townhouse (build cost 7,046); thin at home: wine |
| hold banquet 1 (fish) | mansion | 4.2 | 61.8 | 61.8 | thin at home: cured fish |
| hold banquet 3 (meat) | mansion | 7.6 | 62.0 | 62.0 | thin at home: hop beer |
| hold banquet 2 (meat) | mansion | 6.8 | 62.1 | 62.1 |  |
| hold prayer 2 | chapel | 13 | 59.9 | 62.4 | needs a chapel (build cost 33,148); thin at home: furniture |
| hold banquet 2 (pies) | mansion | 7 | 62.5 | 62.5 | thin at home: pies, candles |
| jousting 1 | arena | 170 | 62.4 | 62.5 | needs a arena (build cost 26,600); thin at home: protection, light armour, arms; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 74001604 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Brunnham: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn; best orders clear only 2 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~104 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Amsdermund | 1111 | 0.40 | 0.40 (42/turn) | glassware 2 (58.28->63.17), lead bars 3 (11.34->13.59), canvas 1 (32.13->37.81), nets 2 (35.8->38) | cheese 21 (5.25->6.6), medicine 2 (116.55->126.35), cloth 29 (7.77->8.7), cured meat 10 (21->23.18) | +112 |
| Hofkirchen | 991 | 0.33 | 0.20 (21/turn) | lead bars 11 (11.34->14.34), nets 2 (35.8->37.43), grain 4 (2.78->3.72), resin 3 (2.6->3.48) | bellows 1 (231->252.7), cheese 29 (5.67->6.6), wax 2 (16.17->20.52), garments 2 (22.05->23.8) | +83 |
| Bordetes | 831 | 0.24 | 0.30 (31/turn) | furniture 12 (13.02->14.91), ploughs 1 (77.17->85.97), bricks 1 (4.6->11.02), glassware 4 (58.28->58.9) | acid 1 (117.6->161.5), bellows 1 (237.3->252.7), tools 4 (5.02->5.3) | +80 |
| Kirchwerp | 1072 | 0.38 | 0.60 (63/turn) | thread 52 (4.66->5.37), lead bars 8 (11.34->13.3), wine 8 (6.14->7.98), tools 16 (5.16->5.7) | cloth 19 (7.77->8.7), cheese 29 (5.99->6.6), acid 1 (157.5->161.5), gears 1 (70.35->73.15) | +75 |
| Gottweiler | 1135 | 0.41 | 0.20 (21/turn) | nets 4 (35.8->40.28), lead bars 4 (11.34->13.39), wine 5 (6.14->6.65) | medicine 1 (113.4->126.35), bellows 1 (241.5->252.7), cheese 29 (5.88->6.6), pasties 3 (9.92->13.59) | +60 |

**Best:** Amsdermund at about +112 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 40 @ min 3.7 | makes 28.0, uses 4.2, holds 274 (keeps 60): sells the surplus + 16/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.1 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 22 @ min 22.0 |  |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 351 @ 2.2, stop - |  | uses 800.6/turn (brewery 1, flax farm 1, household), makes 450.0, holds 286 = 0.8 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 11 @ min 36.0 | makes 9.0, uses 0.0, holds 52 (keeps 15): sells the surplus + 2/turn of the excess |
| porterage | 13 @ 1.1, stop - |  | uses 12.5/turn (observed), makes 0.0, holds 21 = 1.7 turns |
| rope |  | 5 @ min 77.5 |  |
| tar | 2 @ 11.0, stop 5 |  | uses 1.0/turn (ropewalk 1), makes 0.0, holds 9 = 8.5 turns |
| timber |  | 38 @ min 8.5 | makes 12.0, uses 0.0, holds 668 (keeps 350): sells the surplus + 26/turn of the excess |
| tools | 5 @ 6.2, stop 37 |  | uses 4.6/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 43.6 turns |

## Chain sizing

Mode HOLD, garments sold 3.1/turn (+0.0 exported); plan makes 23.4 garments a turn.
Labour: own 450, everything else 385, chain may buy 350 -> chain allowance 415, chain plan 414 (+0 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.85 | 5.87 |
| ret | 3 | 1.04 | 1.04 |
| spin | 4 | 2.14 | 2.15 |
| weave | 3 | 0.92 | 0.91 |
| sew | 2 | 0.58 | 0.57 |

Buffers: flax fibres 64/93, thread 625/273, cloth 10/91
- chain plan needed 518 labour, budget left 415: cut to 415 (sewing capped at 0.57)

## Self-diagnosis

- R1: candles slot dry: 0.0 held, 1.5 a turn (luxury slot (+3 prestige)); our buy paused by the failsafe, home ask none (no sellers at home)
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 2 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
