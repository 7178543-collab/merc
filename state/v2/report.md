# v2 shadow report

Turn 13316, 2026-10-16 05:55. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,150, prestige 3,196 (526 free, +96.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 312 | 0 | 4 | 0 | 0 | min_holding 60, sell 43, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 17 | 3 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 74 | 0 | 2 | 0 | 0 | min_holding 80, sell 10, sell @ 22 |
| grain | 90 | 0 | 13 | 0 | 0 | stop 52, buy 13, buy @ 3.7 |
| labour | 229 | 257 | 603 | 0 | 104 | buy 163, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 46 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 37.8 |
| porterage | 21 | 6 | 6 | 15 | 0 | buy 21, buy @ 1.1 |

**2 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.4 turns (holds 9, next step uses 24/turn) -> v2: check the step that makes it
- **porterage**: logging camp w/ tool, quarry 1 ran short of porterage (buy is live (21 @ 1.1), 6 bought last turn); labour need rises ~75/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it

## Waste (money lost now)

- **labour**: 104 labour expired last turn (~177 coin): holding 229 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.9 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 68
- **flax plants**: flax plants buffer thin: 1.9 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 174

## Notes

- labour: projection runs 86 over real use lately; planning 664, not 750
- labour expiry guard: 104 bought labour expired last turn, buy 153 (not 214) this turn

## Prestige spending, cheapest coin per prestige first

1085 turns left: prestige gained now converts 99.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.0 | 51.0 | running |
| hold banquet 4 (pies) | mansion | 18 | 58.0 | 58.0 | thin at home: hop beer |
| hold banquet 2 (pies) | mansion | 7 | 58.1 | 58.1 | thin at home: pasties, cheese, pies |
| hold banquet 2 (fish) | mansion | 6.8 | 58.2 | 58.2 | thin at home: cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 58.3 | 58.3 |  |
| hold banquet 3 (pies) | mansion | 8 | 58.4 | 58.4 | thin at home: pasties, hop beer, pies |
| hold sermon 2 (candles) | church | 31 | 56.9 | 59.2 | needs a church (build cost 70,894); thin at home: jewellery, candles, furniture |
| hold banquet 3 (fish) | mansion | 7.6 | 59.8 | 59.8 | thin at home: hop beer, cheese |
| hold mass 2 (premium) | cathedral | 360 | 59.3 | 60.1 | needs a cathedral (build cost 284,040); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold prayer 2 | chapel | 13 | 57.6 | 60.1 | needs a chapel (build cost 33,025); thin at home: furniture |
| hold sermon 2 | church | 24 | 57.8 | 60.8 | needs a church (build cost 70,894); thin at home: jewellery, furniture |
| jousting 3 | arena | 230 | 61.2 | 61.3 | needs a arena (build cost 26,291); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 74001604 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Brunnham: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~105 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Heidlowe | 662 | 0.18 | 0.10 (10/turn) | nets 10 (16.69->38.38), glassware 2 (61.95->63.65), varnish 1 (18.17->19.95) | pasties 2 (13.65->14.25), tools 2 (5.12->5.45) | +213 |
| Heilegg | 826 | 0.24 | 0.10 (10/turn) | nets 7 (16.69->39.33), varnish 1 (18.17->18.52) | cheese 24 (5.78->6.22), jewellery 1 (78.75->83.6), hop beer 1 (8.4->9.59), tools 2 (5.12->5.45) | +166 |
| Etallaen | 774 | 0.22 | 0.30 (31/turn) | nets 7 (16.69->39.14), beer 44 (3.28->3.74), flax plants 1 (1.31->1.77) | stockfish 1 (95.03->102.6), cloth 9 (7.35->8.1), hop beer 1 (8.09->9.59), jewellery 1 (82.42->83.6) | +166 |
| Caillechâtel | 488 | 0.14 | 0.10 (10/turn) | nets 7 (16.69->37.62), garments 10 (21.4->21.66), scythes 1 (28.14->28.69) | tools 2 (5.19->5.45) | +139 |
| Unterhufe | 595 | 0.17 | 0.10 (10/turn) | nets 6 (16.69->38.19), garments 10 (21.4->21.85), flax plants 3 (1.31->2.09) | jewellery 1 (81.38->83.6), wheels 2 (22.05->23.18), cloth 4 (7.77->8.1), beer 4 (3.34->3.7) | +133 |

**Best:** Heidlowe at about +213 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 43 @ min 3.7 | makes 28.0, uses 4.2, holds 312 (keeps 60): sells the surplus + 19/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 17 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 10 @ min 22.0 |  |
| grain | 13 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 90 = 6.9 turns |
| labour | 153 @ 2.2, stop - |  | uses 664.3/turn (brewery 1, flax farm 1, household), makes 450.0, holds 229 = 1.1 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 11 @ min 36.8 | makes 9.0, uses 0.0, holds 46 (keeps 15): sells the surplus + 2/turn of the excess |
| porterage | 21 @ 1.1, stop - |  | uses 20.8/turn (observed), makes 0.0, holds 21 = 1.0 turns |
| rope |  | 4 @ min 77.5 |  |
| tar | 2 @ 11.0, stop 5 |  | uses 1.0/turn (ropewalk 1), makes 0.0, holds 5 = 4.9 turns |
| tools | 5 @ 6.2, stop 36 |  | uses 4.4/turn (retting pit 1), makes 0.0, holds 199 = 44.9 turns |

## Chain sizing

Mode HOLD, garments sold 0.8/turn (+0.0 exported); plan makes 19.3 garments a turn.
Labour: own 450, everything else 429, chain may buy 350 -> chain allowance 371, chain plan 371 (+49 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.46 | 5.49 |
| ret | 3 | 0.97 | 0.98 |
| spin | 4 | 2.00 | 2.01 |
| weave | 3 | 0.47 | 0.76 |
| sew | 2 | 0.30 | 0.47 |

Buffers: flax fibres 64/88, thread 599/258, cloth 9/76
- chain plan needed 561 labour, budget left 371: cut to 371 (sewing capped at 0.47)

## Self-diagnosis

- R1: candles slot dry: 0.0 held, 1.5 a turn (luxury slot (+3 prestige)); our buy paused by the failsafe, home ask 76.0 (held back: paused by the failsafe at level 1: un-pause only at level 0)
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
