# v2 shadow report

Turn 13343, 2026-10-17 08:52. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,208, prestige 3,259 (589 free, +3.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 165 | 0 | 19 | 0 | 0 | min_holding 60, sell 18, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 17 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 14, sell @ 22 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 273 | 271 | 721 | 3 | 0 | buy 273, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 31 | 0 | 0 | 0 | 0 | min_holding 15, sell 10, sell @ 35.6 |
| porterage | 11 | 11 | 11 | 0 | 0 | buy 11, buy @ 1.1 |

**1 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.7 turns (holds 23, next step uses 31/turn) -> v2: check the step that makes it

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.5 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 78
- **flax plants**: flax plants buffer thin: 1.9 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 201

## Notes

- labour: projection runs 75 over real use lately; planning 724, not 797

## Prestige spending, cheapest coin per prestige first

1058 turns left: prestige gained now converts 99.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.3 | 48.3 | running |
| hold banquet 2 (meat) | mansion | 6.8 | 57.7 | 57.7 | thin at home: wine |
| hold banquet 2 (fish) | mansion | 6.8 | 57.8 | 57.8 | thin at home: wine, cured fish |
| hold banquet 3 (meat) | mansion | 7.6 | 58.2 | 58.2 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 58.3 | 58.3 | thin at home: cured fish |
| jousting 1 | arena | 170 | 59.0 | 59.2 | needs a arena (build cost 25,277); thin at home: protection, light armour, arms; needs weaponry skill |
| hold prayer 2 | chapel | 13 | 56.8 | 59.3 | needs a chapel (build cost 32,156); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 57.3 | 60.0 | needs a church (build cost 80,207); thin at home: jewellery, candles, furniture |
| hold banquet 1 (fish) | mansion | 4.2 | 60.5 | 60.5 | thin at home: cured fish |
| hold sermon 2 | church | 24 | 57.0 | 60.5 | needs a church (build cost 80,207); thin at home: jewellery, furniture |
| hold feast 2 | townhouse | 2.6 | 57.8 | 60.7 | needs a townhouse (build cost 7,760); thin at home: wine |
| hold banquet 1 (meat) | mansion | 4.2 | 61.1 | 61.1 | running |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 74001604 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Heilegg: candles buy 1 @ 74.5, cured meat buy 6 @ 21.4, nets sell 5 @ 41.2; crew 0.1; est +29 a turn
- **Flax Wyrm** on Brunnham: nothing pays; crew 0.0; est +0 a turn; best orders clear only 4 a turn after crew: ship stays at 0
- best towns now: Karlmoor +69, Amsdermund +32, Heilegg +29, Hofkirchen +17, Nürnnieder +17
- Karlmoor would trade: candles buy 1 @ 77.5, nets sell 9 @ 45.2; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~98 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Karlmoor | 787 | 0.20 | 0.10 (10/turn) | nets 9 (36.6->47.97), stockfish 1 (107.1->133), garments 13 (19.47->21.28), tackles 1 (169.05->181.45) | wool 3 (10.34->12.06), cured meat 5 (22.68->23.2) | +164 |
| Rouhomme | 368 | 0.10 | 0.20 (20/turn) | soap 2 (77.17->95.95), charcoal 13 (1.77->3.8), thread 10 (5.15->6.08), cheese 10 (6.51->7.08) | lead ore 1 (2.5->5.37), flax plants 3 (1.38->1.58), tools 3 (4.91->5.05) | +71 |
| Heilegg | 826 | 0.22 | 0.20 (20/turn) | tackles 1 (169.05->190), nets 5 (36.6->39.9), flax plants 7 (1.26->2.75), garments 13 (19.47->20.14) | acid 1 (114.45->123.5), wax 2 (21.21->23.75), candles 1 (77.17->81.5), wool 2 (9.61->12.06) | +71 |
| Neuborn | 780 | 0.20 | 0.90 (88/turn) | garments 13 (19.47->22.42), charcoal 13 (1.77->4.16), timber 17 (6.35->9.88), flax fibres 1 (4.73->5.7) | candles 1 (76.65->81.5), cured meat 6 (22.05->23.2), wool 1 (9.77->12.06) | +63 |
| Pontmont | 341 | 0.09 | 0.20 (20/turn) | soap 1 (77.17->112.1), garments 13 (19.47->19.76), tools 16 (4.5->4.71), cloth 3 (7.3->7.69) | beer 54 (3.42->3.88), candles 1 (79.8->81.5), wool 3 (11.45->12.06), garments 2 (22.05->22.4) | +62 |

**Best:** Karlmoor at about +164 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 29.4, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 17 @ min 3.96 | makes 28.0, uses 19.2, holds 165 (keeps 60): sells the surplus + 8/turn of the excess |
| cured meat | 12 @ 24.2, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 12 = 2.0 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 17 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 14 @ min 22.0 |  |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 274 @ 2.2, stop - |  | uses 723.6/turn (brewery 1, flax farm 1, household), makes 450.0, holds 273 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 10 @ min 35.6 |  |
| porterage | 11 @ 1.1, stop - |  | uses 11.1/turn (observed), makes 0.0, holds 11 = 1.0 turns |
| rope |  | 7 @ min 77.5 | makes 4.5, uses 0.0, holds 40 (keeps 0): sells the surplus + 3/turn of the excess |
| timber |  | 28 @ min 6.7 | makes 8.4, uses 0.0, holds 597 (keeps 350): sells the surplus + 20/turn of the excess |
| tools | 4 @ 6.2, stop 32 |  | uses 4.0/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 49.9 turns |

## Chain sizing

Mode HOLD, garments sold 16.5/turn (+0.0 exported); plan makes 16.8 garments a turn.
Labour: own 450, everything else 411, chain may buy 350 -> chain allowance 389, chain plan 389 (+0 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 6.30 | 6.31 |
| ret | 3 | 1.12 | 1.12 |
| spin | 4 | 2.31 | 2.31 |
| weave | 3 | 0.66 | 0.65 |
| sew | 2 | 0.39 | 0.41 |

Buffers: flax fibres 58/84, thread 348/247, cloth 23/65
- chain plan needed 598 labour, budget left 389: cut to 389 (sewing capped at 0.41)

## Self-diagnosis

- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
