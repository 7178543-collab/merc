# v2 shadow report

Turn 13475, 2026-10-22 20:58. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 2,386, prestige 3,628 (508 free, -1.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 117 | 0 | 4 | 0 | 0 | min_holding 60, sell 53, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 50 | 0 | 2 | 0 | 0 | min_holding 30, sell 14, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 212 | 212 | 702 | 0 | 10 | buy 212, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 18 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 34.6 |
| porterage | 10 | 10 | 10 | 0 | 0 | buy 10, buy @ 1.1 |

**1 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.3 turns (holds 10, next step uses 32/turn) -> v2: check the step that makes it

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax fibres**: flax fibres buffer thin: 1.3 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 69
- **flax plants**: flax plants buffer thin: 1.1 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 180

## Notes

- labour: projection runs 81 over real use lately; planning 702, not 777

## Prestige spending, cheapest coin per prestige first

926 turns left: prestige gained now converts 99.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.2 | 49.2 | running |
| hold banquet 4 (pies) | mansion | 18 | 49.8 | 49.8 | thin at home: hop beer, wine, pies |
| hold banquet 3 (pies) | mansion | 8 | 51.1 | 51.1 | thin at home: hop beer, pies |
| hold banquet 2 (pies) | mansion | 7 | 51.3 | 51.3 | thin at home: wine, pies |
| hold banquet 2 (fish) | mansion | 6.8 | 52.9 | 52.9 | thin at home: wine |
| hold banquet 2 (meat) | mansion | 6.8 | 53.0 | 53.0 | thin at home: wine, cured meat |
| hold banquet 4 | mansion | 17.5 | 53.1 | 53.1 | thin at home: wine, hop beer, ham |
| jousting 3 | arena | 230 | 53.3 | 53.4 | needs a arena (build cost 25,860); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 53.6 | 53.6 | thin at home: hop beer |
| hold banquet 3 (meat) | mansion | 7.6 | 53.7 | 53.7 | thin at home: hop beer, cured meat |
| hold sermon 2 (candles) | church | 31 | 51.4 | 53.9 | needs a church (build cost 65,413); thin at home: candles, furniture |
| hold prayer 2 | chapel | 13 | 51.6 | 54.5 | needs a chapel (build cost 33,004); thin at home: furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 10 | 151802239 | 0.04 | rope 1 | - | 15 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only 8 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only 1 a turn after crew: ship stays at 0
- best towns now: Clairlond +23, Amsdermund +22, Cobholme +17, Gosschweig +15
- Clairlond would trade: candles buy 1 @ 67.5, nets sell 2 @ 39.0, rope sell 2 @ 84.5; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~100 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.32 | 0.20 (20/turn) | herbs 1 (36.54->38.57), iron ore 1 (4.54->7.6), lead ore 2 (9.97->11.88), seeds 2 (1.78->2.87) | premium ham 1 (205.8->315.4), candles 1 (71.4->75.5), flax fibres 14 (4.98->5.7), blades 2 (12.29->12.63) | +119 |
| Dortdorf | 871 | 0.25 | 0.10 (10/turn) | lead ore 4 (9.97->14.91), rope 2 (71->74.1), herbs 1 (36.54->39.52), dyed yarn 1 (7.46->8.5) | premium ham 1 (235.2->315.4), candles 1 (68.25->75.5), ham 1 (58.8->63.65), fleece 2 (6.62->6.93) | +116 |
| Pontmont | 341 | 0.09 | 0.10 (10/turn) | tackles 1 (189->226.1), rope 2 (71->79.8), casks 1 (5.67->6.32), thread 5 (4.19->4.31) | candles 1 (69.3->75.5), coats 1 (52.5->57), canvas 2 (29.82->30.97), slaked lime 1 (6.83->7.6) | +59 |
| Rouhomme | 368 | 0.10 | 0.40 (40/turn) | charcoal 13 (2.01->3.42), paper 2 (23.52->27.74), honey 3 (8.24->10.07), beer 56 (3.18->3.42) | spinning wheels 2 (222.6->228), candles 1 (68.25->75.5), chisels 2 (9.35->13.11), gold ore 1 (157.5->161.5) | +53 |
| Brunnham | 1281 | 0.47 | 0.40 (40/turn) | nets 11 (35.6->38.57), lead ore 10 (9.97->13.59), leather 1 (25.41->29.45), varnish 3 (17.12->18.52) | candles 1 (67.2->75.5), tools 3 (4.62->5.2) | +51 |

**Best:** Hofkirchen at about +119 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 25.8, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 52 @ min 3.38 |  |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 16 @ min 20.0 | makes 16.4, uses 2.1, holds 50 (keeps 30): sells the surplus + 1/turn of the excess |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 202 @ 2.2, stop - |  | uses 701.7/turn (brewery 1, flax farm 1, household), makes 500.0, holds 212 = 1.1 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 11 @ min 34.6 |  |
| pasties | 3 @ 13.1, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 5.0 turns |
| porterage | 10 @ 1.1, stop - |  | uses 10.4/turn (observed), makes 0.0, holds 10 = 1.0 turns |
| rope |  | 2 @ min 69.0 |  |
| timber |  | 8 @ min 6.5 |  |
| tools | 4 @ 6.2, stop 30 |  | uses 3.8/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 53.1 turns |

## Chain sizing

Mode HOLD, garments sold 11.8/turn (+0.0 exported); plan makes 22.6 garments a turn.
Labour: own 500, everything else 415, chain may buy 350 -> chain allowance 435, chain plan 435 (+76 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.61 | 6.44 |
| ret | 3 | 1.00 | 1.14 |
| spin | 4 | 2.05 | 2.36 |
| weave | 3 | 0.67 | 0.89 |
| sew | 2 | 0.40 | 0.55 |

Buffers: flax fibres 45/80, thread 240/236, cloth 10/89
- chain plan needed 541 labour, budget left 435: cut to 435 (sewing capped at 0.55)

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
