# v2 shadow report

Turn 13320, 2026-10-16 09:57. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,685, prestige 3,230 (560 free, -4.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 277 | 0 | 4 | 0 | 0 | min_holding 60, sell 40, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 17 | 5 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 17, sell @ 22.4 |
| grain | 51 | 0 | 13 | 0 | 0 | stop 52, buy 13, buy @ 3.7 |
| labour | 286 | 286 | 726 | 0 | 10 | buy 286, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 45 | 0 | 0 | 0 | 0 | min_holding 15, sell 10, sell @ 38.2 |
| porterage | 21 | 21 | 21 | 0 | 0 | buy 21, buy @ 1.1 |

**1 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.3 turns (holds 10, next step uses 38/turn) -> v2: check the step that makes it

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax fibres**: flax fibres buffer thin: 1.9 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 68
- **flax plants**: flax plants buffer thin: 2.0 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 174

## Prestige spending, cheapest coin per prestige first

1081 turns left: prestige gained now converts 99.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.9 | 51.9 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 58.4 | 58.4 | thin at home: cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 59.1 | 59.1 | thin at home: hop beer, cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 59.8 | 59.8 |  |
| hold banquet 2 (meat) | mansion | 6.8 | 60.4 | 60.4 |  |
| hold banquet 3 (meat) | mansion | 7.6 | 60.9 | 60.9 | thin at home: hop beer |
| hold feast 2 | townhouse | 2.6 | 59.5 | 61.9 | needs a townhouse (build cost 6,760) |
| hold prayer 2 | chapel | 13 | 59.5 | 62.1 | needs a chapel (build cost 33,622); thin at home: furniture |
| hold banquet 3 (pies) | mansion | 8 | 62.3 | 62.3 | thin at home: hop beer, pies |
| hold sermon 2 (candles) | church | 31 | 59.9 | 62.6 | needs a church (build cost 83,861); thin at home: jewellery, candles, furniture |
| hold sermon 2 | church | 24 | 59.2 | 62.7 | needs a church (build cost 83,861); thin at home: jewellery, furniture |
| hold banquet 2 (pies) | mansion | 7 | 62.9 | 62.9 | thin at home: pies |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 74001604 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Brunnham: nothing pays; crew 0.0; est +0 a turn; best orders clear only 8 a turn after crew: ship stays at 0
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~104 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Heidlowe | 662 | 0.18 | 0.30 (31/turn) | nets 10 (16.84->34.01), cloth 1 (7.9->11.88), varnish 2 (18.17->20.14), beer 41 (2.87->3.31) | cookware 3 (20.89->21.85), fleece 3 (7.82->8.6), dyed cloth 2 (12.92->13.11) | +179 |
| Corstoft | 1496 | 0.61 | 0.20 (21/turn) | nets 6 (16.84->39.33), garments 12 (22.2->24.32), soap 1 (72.98->90.25), varnish 1 (18.17->23.56) | fleece 3 (6.83->8.6) | +171 |
| Vauxvais | 204 | 0.06 | 0.10 (10/turn) | nets 5 (16.84->37.43), soap 1 (72.98->96.9), beer 41 (2.87->3.4), nails 2 (3.72->5.13) | candles 5 (64.58->69.35), garments 2 (22.05->23.6), fleece 1 (7.72->8.6), tools 4 (5.25->5.4) | +170 |
| Amsdermund | 1111 | 0.40 | 0.40 (42/turn) | nets 4 (16.84->37.05), soap 1 (72.98->94.52), arms 11 (28.35->30.02), spinning wheels 1 (264.6->273.6) | cloth 30 (7.77->8.75), medicine 1 (115.5->124.45), cheese 20 (5.25->5.84), cured meat 11 (22.05->22.99) | +158 |
| Brunnham | 1281 | 0.49 | 0.10 (10/turn) | nets 5 (16.84->42.18), soap 1 (72.98->99.75), wax 6 (22.68->23.75), nails 2 (3.72->5.27) | fleece 3 (7.04->8.6) | +156 |

**Best:** Heidlowe at about +179 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 40 @ min 3.7 | makes 28.0, uses 4.2, holds 277 (keeps 60): sells the surplus + 16/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 17 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 17 @ min 22.0 |  |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 305 @ 2.2, stop - |  | uses 755.0/turn (brewery 1, flax farm 1, household), makes 450.0, holds 286 = 0.9 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 11 @ min 36.0 | makes 9.0, uses 0.0, holds 45 (keeps 15): sells the surplus + 2/turn of the excess |
| porterage | 12 @ 1.1, stop - |  | uses 12.1/turn (observed), makes 0.0, holds 21 = 1.7 turns |
| rope |  | 5 @ min 76.0 |  |
| tar | 2 @ 11.0, stop 5 |  | uses 1.0/turn (ropewalk 1), makes 0.0, holds 8 = 7.5 turns |
| timber |  | 38 @ min 8.5 | makes 12.0, uses 0.0, holds 672 (keeps 350): sells the surplus + 26/turn of the excess |
| tools | 5 @ 6.2, stop 36 |  | uses 4.4/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 44.9 turns |

## Chain sizing

Mode HOLD, garments sold 1.7/turn (+0.0 exported); plan makes 23.8 garments a turn.
Labour: own 450, everything else 385, chain may buy 350 -> chain allowance 415, chain plan 416 (+46 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.49 | 5.85 |
| ret | 3 | 0.97 | 1.04 |
| spin | 4 | 2.00 | 2.14 |
| weave | 3 | 0.76 | 0.92 |
| sew | 2 | 0.47 | 0.58 |

Buffers: flax fibres 64/93, thread 650/274, cloth 10/92
- chain plan needed 514 labour, budget left 415: cut to 415 (sewing capped at 0.58)

## Self-diagnosis

- R1: candles slot dry: 0.0 held, 1.5 a turn (luxury slot (+3 prestige)); our buy paused by the failsafe, home ask 87.5 (held back: paused by the failsafe at level 1: un-pause only at level 0)
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
