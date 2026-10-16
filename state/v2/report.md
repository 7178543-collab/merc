# v2 shadow report

Turn 13330, 2026-10-16 19:51. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,755, prestige 3,190 (520 free, -3.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 237 | 0 | 4 | 0 | 0 | min_holding 60, sell 37, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 17 | 5 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 32 | 0 | 2 | 0 | 0 | min_holding 30, sell 20, sell @ 22 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 286 | 286 | 728 | 0 | 8 | buy 286, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 69 | 0 | 0 | 0 | 0 | min_holding 15, sell 13, sell @ 36 |
| porterage | 21 | 21 | 13 | 0 | 8 | buy 13, buy @ 1.1 |

**1 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.1 turns (holds 4, next step uses 40/turn) -> v2: check the step that makes it

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.6 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 78
- **flax plants**: flax plants buffer thin: 1.8 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 201

## Notes

- labour: projection runs 73 over real use lately; planning 728, not 799

## Prestige spending, cheapest coin per prestige first

1071 turns left: prestige gained now converts 99.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.8 | 49.8 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 57.7 | 57.7 | thin at home: wine, cured fish |
| hold banquet 4 (pies) | mansion | 18 | 57.8 | 57.8 | thin at home: hop beer, wine, stockfish |
| hold banquet 3 (fish) | mansion | 7.6 | 58.1 | 58.1 | thin at home: hop beer, cured fish |
| hold banquet 2 (meat) | mansion | 6.8 | 58.8 | 58.8 | thin at home: wine |
| hold banquet 3 (meat) | mansion | 7.6 | 59.1 | 59.1 | thin at home: hop beer |
| hold banquet 4 (premium) | mansion | 20 | 59.4 | 59.4 | thin at home: hop beer, wine, stockfish, premium cheese, premium ham |
| hold banquet 1 (fish) | mansion | 4.2 | 59.5 | 59.5 | thin at home: cured fish |
| hold feast 2 | townhouse | 2.6 | 57.0 | 59.5 | needs a townhouse (build cost 6,880); thin at home: wine |
| hold banquet 3 (pies) | mansion | 8 | 60.2 | 60.2 | thin at home: hop beer, pies |
| jousting 1 | arena | 170 | 60.6 | 60.7 | needs a arena (build cost 25,546); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 60.9 | 60.9 | thin at home: wine, hop beer, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 74001604 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Brunnham: nothing pays; crew 0.0; est +0 a turn; best orders clear only 0 a turn after crew: ship stays at 0
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn; best orders clear only 2 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~101 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hanbrücken | 531 | 0.14 | 0.10 (10/turn) | garments 20 (20.41->26.41), cloth 18 (8.82->15.11), medicine 1 (121.8->128.25), glassware 1 (58.8->64.12) | flax fibres 1 (5.57->8.84), yarn 5 (3.76->4.14) | +245 |
| Rouhomme | 368 | 0.10 | 0.60 (61/turn) | bread 141 (2.39->3.1), tackles 1 (179.55->207.1), soap 1 (80.85->100.7), beer 38 (2.98->3.67) | flax fibres 1 (6.56->8.84), tools 4 (4.91->5.15) | +181 |
| Vauxvais | 204 | 0.06 | 0.10 (10/turn) | medicine 1 (121.8->172.9), stockfish 1 (96.08->105.45), garments 20 (20.41->20.71), grain 4 (2.72->3.1) | thread 9 (4.47->5.2), flax fibres 1 (5.88->8.84), pies 1 (16.8->18.14) | +69 |
| Brebronn | 862 | 0.25 | 0.30 (30/turn) | beer 38 (2.98->4.71), cookware 5 (22.89->25.65), garments 16 (20.41->21.09) | flax fibres 1 (5.1->8.84), honey 2 (7.35->8.03) | +66 |
| Cobholme | 1564 | 0.63 | 0.20 (20/turn) | flour 2 (20.06->36.86), glassware 1 (58.8->76), light armour 2 (87.15->95), nets 4 (35.6->37.62) | flax fibres 1 (6.98->8.84) | +57 |

**Best:** Hanbrücken at about +245 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 37 @ min 3.7 | makes 28.0, uses 4.2, holds 237 (keeps 60): sells the surplus + 13/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 17 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 18 @ min 22.0 |  |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 278 @ 2.2, stop - |  | uses 728.0/turn (brewery 1, flax farm 1, household), makes 450.0, holds 286 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 13 @ min 36.0 | makes 9.0, uses 0.0, holds 69 (keeps 15): sells the surplus + 4/turn of the excess |
| porterage | 13 @ 1.1, stop - |  | uses 13.0/turn (observed), makes 0.0, holds 21 = 1.6 turns |
| rope |  | 5 @ min 77.5 |  |
| tar | 2 @ 11.0, stop 5 |  | uses 1.0/turn (ropewalk 1), makes 0.0, holds 9 = 9.3 turns |
| timber |  | 35 @ min 8.5 | makes 12.0, uses 0.0, holds 642 (keeps 350): sells the surplus + 23/turn of the excess |
| tools | 5 @ 6.2, stop 38 |  | uses 4.7/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 42.2 turns |

## Chain sizing

Mode HOLD, garments sold 17.7/turn (+0.0 exported); plan makes 20.5 garments a turn.
Labour: own 450, everything else 385, chain may buy 350 -> chain allowance 415, chain plan 414 (+0 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 6.31 | 6.31 |
| ret | 3 | 1.12 | 1.12 |
| spin | 4 | 2.31 | 2.31 |
| weave | 3 | 0.80 | 0.80 |
| sew | 2 | 0.50 | 0.50 |

Buffers: flax fibres 62/89, thread 449/262, cloth 4/80
- chain plan needed 571 labour, budget left 415: cut to 415 (sewing capped at 0.50)

## Self-diagnosis

- R1: candles slot dry: 0.0 held, 1.5 a turn (luxury slot (+3 prestige)); our buy paused by the failsafe, home ask 81.5 (held back: paused by the failsafe at level 1: un-pause only at level 0)
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
