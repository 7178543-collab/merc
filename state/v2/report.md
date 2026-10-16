# v2 shadow report

Turn 13333, 2026-10-16 22:53. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,889, prestige 3,253 (583 free, -4.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 224 | 0 | 4 | 0 | 0 | min_holding 60, sell 36, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 17 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 34 | 0 | 2 | 0 | 0 | min_holding 30, sell 19, sell @ 22 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 286 | 286 | 724 | 0 | 12 | buy 286, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 61 | 0 | 0 | 0 | 0 | min_holding 15, sell 12, sell @ 34 |
| porterage | 11 | 11 | 11 | 0 | 0 | buy 11, buy @ 1.1 |

**1 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.0 turns (holds 1, next step uses 42/turn) -> v2: check the step that makes it

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.5 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 80
- **flax plants**: flax plants buffer thin: 1.8 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 201

## Notes

- labour: projection runs 73 over real use lately; planning 724, not 795

## Prestige spending, cheapest coin per prestige first

1068 turns left: prestige gained now converts 99.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.2 | 49.2 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 56.0 | 56.0 | thin at home: wine, cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 56.8 | 56.8 | thin at home: cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 57.5 | 57.5 | thin at home: cured fish |
| hold banquet 2 (meat) | mansion | 6.8 | 58.4 | 58.4 | thin at home: wine |
| hold banquet 3 (meat) | mansion | 7.6 | 59.0 | 59.0 |  |
| hold feast 2 | townhouse | 2.6 | 57.2 | 59.8 | needs a townhouse (build cost 7,054); thin at home: wine |
| jousting 1 | arena | 170 | 59.8 | 59.9 | needs a arena (build cost 25,252); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 60.6 | 60.6 | thin at home: pasties, wine |
| hold prayer 2 | chapel | 13 | 58.1 | 60.6 | needs a chapel (build cost 32,484); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 58.1 | 60.7 | needs a church (build cost 80,211); thin at home: jewellery, candles, furniture |
| hold banquet 3 (pies) | mansion | 8 | 60.9 | 60.9 | thin at home: pasties, pies |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 74001604 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Brunnham: nothing pays; crew 0.0; est +0 a turn; best orders clear only 4 a turn after crew: ship stays at 0
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn; best orders clear only 8 a turn after crew: ship stays at 0
- best towns now: Bremcop +23, Etallaen +18
- Bremcop would trade: nets sell 4 @ 43.2; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~100 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Rouhomme | 368 | 0.10 | 0.30 (30/turn) | charcoal 21 (1.78->4.24), thread 25 (4.66->6.08), axes 1 (17.12->36.67), beer 37 (2.97->3.67) | flax plants 2 (0.84->1.45), flax fibres 1 (5.67->6.1), tools 3 (4.91->5.15) | +131 |
| Donaunieder | 985 | 0.31 | 0.20 (20/turn) | garments 19 (20.09->23.94), tackles 1 (176.4->216.6), medicine 1 (123.9->129.2), wrought iron 3 (13.86->15.2) | candles 4 (65.1->69.35), flax fibres 1 (5.25->6.1) | +130 |
| Blanans | 297 | 0.08 | 0.40 (40/turn) | thread 15 (4.66->6.37), bread 142 (2.29->2.66), butter 1 (71.92->90.25), tackles 1 (176.4->190) | flax fibres 2 (5.21->6.1) | +107 |
| Orlesailles | 1178 | 0.41 | 0.30 (30/turn) | garments 19 (20.09->22.8), thread 35 (4.66->6.27), glassware 3 (54.6->57.47), nets 2 (34.2->38) | cloth 12 (7.88->8.7) | +106 |
| Fontaux | 411 | 0.11 | 0.20 (20/turn) | glassware 1 (54.6->82.65), salt 6 (4.41->7.79), beer 37 (2.97->3.7), spinning wheels 1 (310.8->323) | - | +88 |

**Best:** Rouhomme at about +131 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 35 @ min 3.7 | makes 28.0, uses 4.2, holds 224 (keeps 60): sells the surplus + 12/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 17 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 19 @ min 22.0 |  |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 274 @ 2.2, stop - |  | uses 724.1/turn (brewery 1, flax farm 1, household), makes 450.0, holds 286 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 12 @ min 34.0 | makes 9.0, uses 0.0, holds 61 (keeps 15): sells the surplus + 3/turn of the excess |
| porterage | 11 @ 1.1, stop - |  | uses 11.2/turn (observed), makes 0.0, holds 11 = 1.0 turns |
| rope |  | 5 @ min 77.5 |  |
| tar | 2 @ 11.0, stop 5 |  | uses 1.0/turn (ropewalk 1), makes 0.0, holds 9 = 9.3 turns |
| timber |  | 30 @ min 6.7 | makes 8.4, uses 0.0, holds 620 (keeps 350): sells the surplus + 22/turn of the excess |
| tools | 4 @ 6.2, stop 32 |  | uses 4.0/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 49.9 turns |

## Chain sizing

Mode HOLD, garments sold 20.1/turn (+0.0 exported); plan makes 20.9 garments a turn.
Labour: own 450, everything else 376, chain may buy 350 -> chain allowance 424, chain plan 424 (+1 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 6.44 | 6.48 |
| ret | 3 | 1.12 | 1.15 |
| spin | 4 | 2.36 | 2.37 |
| weave | 3 | 0.80 | 0.81 |
| sew | 2 | 0.52 | 0.51 |

Buffers: flax fibres 60/90, thread 422/263, cloth 1/81
- chain plan needed 577 labour, budget left 424: cut to 424 (sewing capped at 0.51)

## Self-diagnosis

- R1: candles slot dry: 0.0 held, 1.5 a turn (luxury slot (+3 prestige)); our buy paused by the failsafe, home ask 81.5 (held back: paused by the failsafe at level 1: un-pause only at level 0)
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
