# v2 shadow report

Turn 13404, 2026-10-19 21:55. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 7,701, prestige 3,422 (752 free, -1.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 233 | 0 | 4 | 0 | 0 | min_holding 60, sell 41, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 158 | 0 | 2 | 0 | 0 | min_holding 30, sell 14, sell @ 20.8 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 116 | 41 | 491 | 69 | 0 | buy 116, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 15 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34.4 |
| porterage | 37 | 37 | 24 | 0 | 13 | buy 37, buy @ 1.1 |

**0 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Tuning

- **limestone**: we make 10/turn more than we use but there is no sell order -> v2: sell 10

## Notes

- labour: projection runs 150 over real use lately; planning 560, not 583

## Prestige spending, cheapest coin per prestige first

997 turns left: prestige gained now converts 99.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.7 | 47.7 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 52.8 | 52.8 | thin at home: wine, cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 54.5 | 54.5 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 54.8 | 54.8 | thin at home: cured fish |
| hold feast 2 | townhouse | 2.6 | 52.2 | 55.0 | needs a townhouse (build cost 6,984); thin at home: wine |
| hold banquet 2 (meat) | mansion | 6.8 | 55.4 | 55.4 | thin at home: wine |
| hold prayer 2 | chapel | 13 | 53.4 | 56.1 | needs a chapel (build cost 32,706); thin at home: furniture |
| hold banquet 2 (pies) | mansion | 7 | 56.9 | 56.9 | thin at home: pasties, wine |
| hold banquet 3 (meat) | mansion | 7.6 | 57.1 | 57.1 |  |
| hold banquet 3 (pies) | mansion | 8 | 57.7 | 57.7 | thin at home: pasties |
| hold banquet 1 (meat) | mansion | 4.2 | 58.2 | 58.2 |  |
| jousting 1 | arena | 170 | 58.2 | 58.4 | needs a arena (build cost 26,022); thin at home: protection, light armour, arms; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 9 | 120102307 | 0.344 | beer 43 | furniture 1 | 19 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: furniture buy 2 @ 14.0; crew 0.1; est +15 a turn; stock: furniture 2 @ 14.0 (keep 145)
- **Flax Wyrm** on Rouhomme: nothing pays; crew 0.0; est +0 a turn; stock: furniture 2 @ 14.2 (keep 145); best orders clear only 15 a turn after crew: ship stays at 0
- best towns now: Briclives +35, Chribruck +20, Toqueque +19, Bordees +18, Kleinburgh +18
- Briclives would trade: beer sell 38 @ 4.64, furniture buy 2 @ 12.5; crew 0.3

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~95 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Neuborn | 780 | 0.20 | 1.00 (95/turn) | timber 24 (6.2->9.88), garments 10 (19.65->21.28), seeds 12 (1.78->3.32), lead ore 1 (8.19->19.38) | cheese 62 (5.04->5.42), candles 1 (74.55->82.5), pies 1 (15.96->17.29), flax fibres 2 (5.78->6.3) | +78 |
| Briclives | 1041 | 0.33 | 0.30 (29/turn) | beer 38 (2.73->4.89), thread 6 (3.98->4.73), flax fibres 1 (4.51->5.61), honey 3 (8.87->9.36) | slaked lime 1 (7.35->10.73), tools 5 (4.37->4.82), candles 1 (81.9->82.5), nails 2 (4.81->5.27) | +63 |
| Fontaux | 411 | 0.10 | 0.40 (38/turn) | beer 38 (2.73->3.65), timber 15 (6.2->8.64), cookware 3 (22.26->25.27), limestone 1 (15.6->20.52) | candles 1 (74.55->82.5), grain 13 (2.92->3.28), hides 1 (10.82->12.82) | +63 |
| Clairas | 374 | 0.10 | 0.10 (10/turn) | thread 42 (3.98->4.45), nets 3 (35->38.38), flax fibres 4 (4.51->5.42), potash 1 (17.22->19.95) | candles 1 (70.88->82.5), grain 13 (2.46->3.28), yarn 4 (3.42->4.12), slaked lime 1 (9.24->10.73) | +54 |
| Arnsreuth | 921 | 0.27 | 0.30 (29/turn) | glassware 1 (60.9->87.88), beer 38 (2.73->3.88), wine 1 (5.46->6.22) | grain 13 (2.73->3.28) | +49 |

**Best:** Neuborn at about +78 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 36 @ min 3.38 | makes 28.0, uses 4.2, holds 233 (keeps 60): sells the surplus + 12/turn of the excess |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 12 = 7.7 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 110 @ 2.2, stop - |  | uses 559.7/turn (brewery 1, flax farm 1, household), makes 450.0, holds 116 = 1.1 turns |
| limestone |  | 10 @ min 17.2 |  |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 34.0 |  |
| pasties | 3 @ ?, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 4.9 turns |
| porterage | 25 @ 1.1, stop - |  | uses 24.6/turn (observed), makes 0.0, holds 37 = 1.5 turns |
| rope |  | 3 @ min 74.5 |  |
| timber |  | 12 @ min 6.7 | makes 8.4, uses 0.0, holds 403 (keeps 350): sells the surplus + 4/turn of the excess |
| tools | 6 @ 6.2, stop 41 |  | uses 5.1/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 39.2 turns |

## Chain sizing

Mode HOLD, garments sold 2.3/turn (+0.0 exported); plan makes 1.2 garments a turn.
Labour: own 450, everything else 450, chain may buy 350 -> chain allowance 350, chain plan 121 (-4 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 2.58 | 2.49 |
| ret | 3 | 0.48 | 0.44 |
| spin | 4 | 0.98 | 0.97 |
| weave | 3 | 0.07 | 0.04 |
| sew | 2 | 0.04 | 0.03 |

Buffers: flax fibres 58/45, thread 333/132, cloth 13/5

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
