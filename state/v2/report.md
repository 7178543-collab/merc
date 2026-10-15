# v2 shadow report

Turn 13295, 2026-10-15 08:00. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,350, prestige 3,065 (395 free, +3.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 245 | 0 | 19 | 0 | 0 | min_holding 60, sell 50, sell @ 3.86 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 24 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 52 | 0 | 2 | 0 | 0 | min_holding 30, sell 3, sell @ 22 |
| grain | 103 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 145 | 132 | 547 | 0 | 35 | buy 145, buy @ 2.2 |
| meat | 6 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 3.02 |
| nets | 48 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 39.8 |
| porterage | 23 | 23 | 23 | 0 | 0 | buy 23, buy @ 0.8 |

**0 risks, 2 waste, 3 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **Flax Wyrm**: Flax Wyrm cost 19 coin last turn (crew 0.20) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell
- **labour**: 35 labour expired last turn (~54 coin): holding 145 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **timber**: build materials for park 1 are in (597.2 held, 20 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 50% (EXPANSION), about 6 turns left; still to deliver: labour 130, limestone 30, timber 20; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 30 | 116.3 | 0 | off: covered |
| timber | 20 | 597.2 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 22

## Notes

- labour: projection runs 48 over real use lately; planning 547, not 586

## Prestige spending, cheapest coin per prestige first

1106 turns left: prestige gained now converts 99.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 45.9 | 48.8 | running |
| hold sermon 2 (candles) | church | 31 | 53.8 | 55.9 | needs a church (build cost 66,916); thin at home: jewellery, candles, furniture |
| hold banquet 2 (pies) | mansion | 7 | 56.0 | 56.0 | thin at home: pies |
| hold banquet 4 (pies) | mansion | 18 | 56.6 | 56.6 | thin at home: hop beer |
| hold banquet 3 (pies) | mansion | 8 | 57.4 | 57.4 | thin at home: hop beer, pies |
| hold prayer 2 | chapel | 13 | 55.2 | 57.4 | needs a chapel (build cost 30,094); thin at home: furniture |
| hold sermon 2 | church | 24 | 55.6 | 58.3 | needs a church (build cost 66,916); thin at home: jewellery, furniture |
| jousting 1 | arena | 170 | 58.6 | 58.7 | needs a arena (build cost 23,694); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 58.8 | 58.8 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 58.8 | 58.8 | thin at home: cured fish |
| hold feast 2 | townhouse | 2.6 | 56.8 | 58.9 | needs a townhouse (build cost 6,122) |
| hold mass 2 (premium) | cathedral | 360 | 58.8 | 59.5 | needs a cathedral (build cost 272,370); thin at home: furniture, jewellery, glassware, candles, premium garments |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.20 | 19 | 181601373 | 0.164 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | nets 2 | - | 48 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Gottweiler: butter buy 1 @ 59.5, cheese buy 26 @ 5.75, cured meat buy 6 @ 23.2; crew 0.2; est +26 a turn
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn; best orders clear only 2 a turn after crew: ship stays at 0
- best towns now: Clarfranche +59, Hofkirchen +53, Birkeningen +53, Donaunieder +32, Etallaen +28
- Clarfranche would trade: axes buy 3 @ 16.1, mouldboards buy 1 @ 37.0, tackles sell 1 @ 214; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~97 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.31 | 1.00 (97/turn) | bread 77 (2.29->4.35), beer 27 (3.96->5.18), thread 8 (4.66->5.32), grain 4 (2.26->3.17) | acid 0 (157.5->180.5), cured meat 3 (23.52->25.4), salt 5 (4.24->4.94), jewellery 0 (78.75->80.75) | +129 |
| Birkeningen | 1006 | 0.32 | 0.10 (10/turn) | tackles 1 (164.85->243.2), blades 1 (16.8->18.14), charcoal 2 (2.18->4.8), wheels 1 (20.2->20.9) | cloth 7 (7.93->8.55), cured meat 6 (24.36->25.4), salt 6 (4.3->4.94), resin 1 (1.89->2.62) | +84 |
| Fontaux | 411 | 0.11 | 0.20 (19/turn) | salt 18 (5.51->7.79), charcoal 2 (2.18->3.8), grain 8 (2.26->2.72), nets 2 (41->42.37) | cheese 40 (6.88->7.46), cloth 7 (7.98->8.55), flax plants 28 (1.4->1.72), cured meat 6 (24.99->25.4) | +73 |
| Kirchwerp | 1072 | 0.35 | 1.00 (97/turn) | timber 16 (6.3->14.25), wine 9 (6.14->7.69), grain 3 (2.26->3.04), flax plants 5 (1.01->1.71) | cheese 15 (6.2->7.46), acid 0 (178.5->180.5), cured meat 2 (24.36->25.4), jewellery 0 (78.75->80.75) | +72 |
| Amsdermund | 1111 | 0.37 | 0.30 (29/turn) | furniture 12 (13.65->17.95), garments 3 (21.2->25.84), thread 4 (4.66->5.7), paper 3 (24.36->25.08) | cured meat 6 (22.89->25.4), cloth 7 (7.77->8.55), cheese 24 (7.09->7.46) | +65 |

**Best:** Hofkirchen at about +129 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 26.0, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 49 @ min 3.94 | makes 56.0, uses 19.2, holds 245 (keeps 60): sells the surplus + 12/turn of the excess |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 8 = 5.0 turns |
| cured meat | 6 @ 26.6, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 24 = 4.0 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 24 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 3 @ min 22.0 | makes 3.7, uses 2.1, holds 52 (keeps 30): sells the surplus + 2/turn of the excess |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 103 = 4.0 turns |
| labour | 97 @ 2.2, stop - |  | uses 546.5/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 145 = 1.5 turns |
| limestone |  | 5 @ min 18.8 |  |
| meat | 7 @ 3.02, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 6 = 0.9 turns |
| nets |  | 8 @ min 42.6 | makes 6.0, uses 0.0, holds 48 (keeps 15): sells the surplus + 2/turn of the excess |
| porterage | 23 @ 0.8, stop - |  | uses 23.3/turn (observed), makes 0.0, holds 23 = 1.0 turns |
| rope |  | 6 @ min 76.5 | makes 4.5, uses 0.0, holds 22 (keeps 0): sells the surplus + 1/turn of the excess |
| tar | 2 @ 11.0, stop 5 |  | uses 1.1/turn (ropewalk 1), makes 0.0, holds 4 = 3.3 turns |
| timber |  | 43 @ min 8.5 | makes 24.0, uses 0.0, holds 597 (keeps 350): sells the surplus + 19/turn of the excess |
| tools | 6 @ 6.2, stop 46 |  | uses 5.7/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 35.2 turns |

## Chain sizing

Mode FULL, garments sold 10.4/turn (+0.0 exported); plan makes 2.9 garments a turn.
Labour: own 450, everything else 488, chain may buy 350 -> chain allowance 350, chain plan 101 (-8 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 1.84 | 1.68 |
| ret | 3 | 0.33 | 0.30 |
| spin | 4 | 0.90 | 0.83 |
| weave | 3 | 0.00 | 0.00 |
| sew | 2 | 0.09 | 0.07 |

Buffers: flax fibres 76/31, thread 199/202, cloth 93/44
- thread beyond the household duty (55 a turn) is fed from weaving

## Self-diagnosis

- R3: weavery 1 (weavery) finished but idle 6 turns (weave cloth 2 at 0); no planned recipe for a weavery: Taylor's call
