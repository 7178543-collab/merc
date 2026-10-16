# v2 shadow report

Turn 13327, 2026-10-16 16:58. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,041, prestige 3,202 (532 free, -3.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 252 | 0 | 4 | 0 | 0 | min_holding 60, sell 38, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 5 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 32 | 0 | 2 | 0 | 0 | min_holding 30, sell 20, sell @ 22 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 286 | 286 | 728 | 0 | 8 | buy 286, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 56 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 36 |
| porterage | 21 | 21 | 13 | 0 | 8 | buy 21, buy @ 1.1 |

**1 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.2 turns (holds 8, next step uses 43/turn) -> v2: check the step that makes it

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax fibres**: flax fibres buffer thin: 1.7 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 76
- **flax plants**: flax plants buffer thin: 1.8 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 194

## Notes

- labour: projection runs 73 over real use lately; planning 728, not 801

## Prestige spending, cheapest coin per prestige first

1074 turns left: prestige gained now converts 99.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.9 | 51.9 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 56.2 | 56.2 | thin at home: wine, cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 56.4 | 56.4 | thin at home: hop beer, cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 58.0 | 58.0 | thin at home: cured fish |
| hold banquet 3 (meat) | mansion | 7.6 | 59.6 | 59.6 | thin at home: hop beer |
| hold banquet 2 (meat) | mansion | 6.8 | 59.8 | 59.8 | thin at home: wine |
| hold feast 2 | townhouse | 2.6 | 57.5 | 60.1 | needs a townhouse (build cost 7,040); thin at home: wine |
| hold banquet 3 (pies) | mansion | 8 | 60.2 | 60.2 | thin at home: pasties, hop beer, pies |
| hold sermon 2 (candles) | church | 31 | 58.3 | 61.1 | needs a church (build cost 83,502); thin at home: jewellery, candles, furniture |
| hold prayer 2 | chapel | 13 | 58.9 | 61.4 | needs a chapel (build cost 33,458); thin at home: furniture |
| hold banquet 2 (pies) | mansion | 7 | 61.5 | 61.5 | thin at home: pasties, wine, pies |
| hold mass 2 (premium) | cathedral | 360 | 60.9 | 62.0 | needs a cathedral (build cost 364,081); thin at home: furniture, jewellery, glassware, candles, premium garments |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 74001604 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Heilegg: nets sell 6 @ 41.0; crew 0.1; est +18 a turn
- **Flax Wyrm** on Brunnham: nothing pays; crew 0.0; est +0 a turn
- best towns now: Heilegg +18
- Heilegg would trade: nets sell 6 @ 41.0; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~105 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Rouhomme | 368 | 0.10 | 1.00 (105/turn) | bread 126 (2.48->3.38), timber 30 (6.35->8.55), beer 35 (2.96->3.65), rope 2 (79.5->85.5) | flax plants 5 (1.04->1.5), tools 3 (4.91->5.2), flax fibres 0 (5.72->6.3) | +136 |
| Bedenis | 566 | 0.16 | 0.20 (21/turn) | garments 20 (20.65->21.47), tools 14 (4.46->4.89), beer 39 (2.96->3.31) | stockfish 1 (97.12->134.9), butter 2 (62.48->64.6), soap 1 (76.65->77.9), flax fibres 2 (5.88->6.3) | +58 |
| Angefont | 686 | 0.19 | 0.20 (21/turn) | ploughs 1 (76.65->85.5), beer 39 (2.96->3.42) | stockfish 1 (87.67->134.9), flax fibres 5 (5.72->6.3), garments 2 (22.89->23.2), tar 1 (9.66->10.3) | +57 |
| Clairlond | 1288 | 0.50 | 0.10 (10/turn) | nets 1 (35.8->42.75) | stockfish 1 (94.5->134.9), bellows 1 (252->260.3), flax fibres 5 (5->6.3) | +52 |
| Karlmoor | 787 | 0.22 | 0.10 (10/turn) | axes 1 (26.04->53.67), pies 1 (26.25->30.59), bricks 1 (6->13.77), nets 3 (35.8->36.48) | stockfish 1 (123.9->134.9), soap 1 (74.03->77.9), tar 1 (8.4->10.3), flax fibres 2 (5.83->6.3) | +52 |

**Best:** Rouhomme at about +136 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 38 @ min 3.7 | makes 28.0, uses 4.2, holds 252 (keeps 60): sells the surplus + 14/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 20 @ min 22.0 |  |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 278 @ 2.2, stop - |  | uses 728.0/turn (brewery 1, flax farm 1, household), makes 450.0, holds 286 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 12 @ min 36.0 | makes 9.0, uses 0.0, holds 56 (keeps 15): sells the surplus + 3/turn of the excess |
| porterage | 13 @ 1.1, stop - |  | uses 12.8/turn (observed), makes 0.0, holds 21 = 1.6 turns |
| rope |  | 6 @ min 77.5 | makes 4.5, uses 0.0, holds 17 (keeps 0): sells the surplus + 1/turn of the excess |
| tar | 2 @ 11.0, stop 5 |  | uses 1.0/turn (ropewalk 1), makes 0.0, holds 10 = 9.4 turns |
| timber |  | 35 @ min 8.5 | makes 12.0, uses 0.0, holds 636 (keeps 350): sells the surplus + 23/turn of the excess |
| tools | 5 @ 6.2, stop 38 |  | uses 4.7/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 42.9 turns |

## Chain sizing

Mode HOLD, garments sold 13.5/turn (+0.0 exported); plan makes 21.3 garments a turn.
Labour: own 450, everything else 385, chain may buy 350 -> chain allowance 415, chain plan 415 (-1 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 6.16 | 6.20 |
| ret | 3 | 1.08 | 1.10 |
| spin | 4 | 2.25 | 2.27 |
| weave | 3 | 0.84 | 0.83 |
| sew | 2 | 0.54 | 0.52 |

Buffers: flax fibres 63/90, thread 496/265, cloth 8/83
- chain plan needed 558 labour, budget left 415: cut to 415 (sewing capped at 0.52)

## Self-diagnosis

- R1: candles slot dry: 0.0 held, 1.5 a turn (luxury slot (+3 prestige)); our buy paused by the failsafe, home ask 80.0 (held back: paused by the failsafe at level 1: un-pause only at level 0)
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
