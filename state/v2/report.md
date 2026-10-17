# v2 shadow report

Turn 13351, 2026-10-17 16:51. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,716, prestige 3,283 (613 free, +2.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 129 | 0 | 19 | 0 | 0 | min_holding 60, sell 13, sell @ 5.55 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 89 | 0 | 2 | 0 | 0 | min_holding 30, sell 25, sell @ 22 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 281 | 276 | 726 | 0 | 0 | buy 281, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 15 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 36.4 |
| porterage | 10 | 10 | 10 | 0 | 0 | buy 10, buy @ 1.1 |

**1 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.5 turns (holds 23, next step uses 50/turn) -> v2: check the step that makes it

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.7 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 65

## Notes

- labour: projection runs 73 over real use lately; planning 726, not 764

## Prestige spending, cheapest coin per prestige first

1050 turns left: prestige gained now converts 99.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.4 | 50.4 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 54.8 | 54.8 | thin at home: wine, cured fish |
| hold banquet 2 (meat) | mansion | 6.8 | 55.5 | 55.5 | thin at home: wine |
| hold banquet 3 (fish) | mansion | 7.6 | 55.7 | 55.7 | thin at home: cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 56.3 | 56.3 | thin at home: cured fish |
| hold banquet 3 (meat) | mansion | 7.6 | 56.3 | 56.3 |  |
| hold banquet 1 (meat) | mansion | 4.2 | 57.8 | 57.8 |  |
| hold prayer 2 | chapel | 13 | 56.4 | 59.0 | needs a chapel (build cost 33,546); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 57.7 | 60.5 | needs a church (build cost 81,482); thin at home: jewellery, candles, furniture |
| hold sermon 2 | church | 24 | 57.6 | 61.1 | needs a church (build cost 81,482); thin at home: jewellery, furniture |
| hold feast 2 | townhouse | 2.6 | 58.3 | 61.7 | needs a townhouse (build cost 8,936); thin at home: wine |
| jousting 1 | arena | 170 | 62.0 | 62.2 | needs a arena (build cost 25,854); thin at home: protection, light armour, arms; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 110801910 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | cured meat 5 | -108 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Karlmoor: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn
- best towns now: Amsdermund +38, Fulkirch +22
- Amsdermund would trade: candles buy 1 @ 71.0, rope sell 3 @ 86.5; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~101 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Caillechâtel | 488 | 0.13 | 0.10 (10/turn) | beer 14 (2.9->6.84), light armour 1 (84->95.95), tools 11 (4.5->5.37), garments 10 (19.64->20.14) | bricks 1 (5.51->12.16), potash 1 (14.18->16.05), furniture 1 (12.5->13.6), salt 2 (3.59->4.29) | +85 |
| Amsdermund | 1111 | 0.39 | 0.20 (20/turn) | rope 3 (74->85.5), thread 19 (4.66->5.22) | soap 1 (60.38->74.58), cloth 49 (7.67->8.25), candles 1 (73.5->81.5), jewellery 1 (86.1->88.35) | +69 |
| Bordees | 1112 | 0.39 | 0.10 (10/turn) | tackles 1 (169.05->218.5), cheese 5 (6.2->7.36), cured fish 3 (23.31->24.89), cured meat 1 (21.68->22.8) | acid 1 (116.55->125.4), candles 1 (80.33->81.5), dyed yarn 1 (8.66->9.31) | +63 |
| Toqueque | 642 | 0.17 | 0.20 (20/turn) | cheese 13 (6.2->8.41), salt 9 (4.89->7.22), medicine 1 (134.4->143.45), nets 2 (37.4->39.71) | bricks 1 (7.19->12.16), candles 1 (80.85->81.5) | +58 |
| Gosschweig | 1099 | 0.38 | 0.30 (30/turn) | tools 16 (4.5->6.98), varnish 2 (18.17->22.42), wrought iron 4 (13.86->15.2), garments 22 (19.64->20.14) | candles 1 (73.5->81.5), hop beer 2 (7.88->8.74) | +56 |

**Best:** Caillechâtel at about +85 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 28 @ min 3.7 | makes 28.0, uses 4.2, holds 129 (keeps 60): sells the surplus + 4/turn of the excess |
| cured meat | 9 @ 22.4, stop 24 |  | uses 6.0/turn (observed), makes 0.0, holds 18 = 3.0 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.1 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 26 @ min 22.0 | makes 25.4, uses 2.1, holds 89 (keeps 30): sells the surplus + 3/turn of the excess |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 276 @ 2.2, stop - |  | uses 726.1/turn (brewery 1, flax farm 1, household), makes 450.0, holds 281 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 36.4 |  |
| porterage | 10 @ 1.1, stop - |  | uses 10.0/turn (observed), makes 0.0, holds 10 = 1.0 turns |
| rope |  | 7 @ min 72.0 | makes 2.2, uses 0.0, holds 54 (keeps 0): sells the surplus + 4/turn of the excess |
| timber |  | 25 @ min 6.9 | makes 8.4, uses 0.0, holds 560 (keeps 350): sells the surplus + 17/turn of the excess |
| tools | 4 @ 6.2, stop 30 |  | uses 3.6/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 54.9 turns |

## Chain sizing

Mode HOLD, garments sold 13.1/turn (+0.0 exported); plan makes 27.5 garments a turn.
Labour: own 450, everything else 362, chain may buy 350 -> chain allowance 438, chain plan 438 (+35 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.30 | 5.77 |
| ret | 3 | 0.94 | 1.03 |
| spin | 4 | 1.94 | 2.11 |
| weave | 3 | 0.99 | 1.08 |
| sew | 2 | 0.62 | 0.67 |

Buffers: flax fibres 57/80, thread 375/235, cloth 23/108
- chain plan needed 469 labour, budget left 438: cut to 438 (sewing capped at 0.67)

## Self-diagnosis

- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
