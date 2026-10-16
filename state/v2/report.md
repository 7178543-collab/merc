# v2 shadow report

Turn 13312, 2026-10-16 01:56. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,294, prestige 3,097 (427 free, -3.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 412 | 0 | 4 | 0 | 0 | min_holding 60, sell 51, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 25 | 0 | 2 | 0 | 0 | min_holding 80, sell 2, sell @ 22 |
| grain | 103 | 26 | 13 | 0 | 0 | stop 52, buy 13, buy @ 3.7 |
| labour | 80 | 80 | 449 | 0 | 81 | buy 170, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 48 | 0 | 0 | 0 | 0 | min_holding 15, sell 8, sell @ 36.6 |
| porterage | 26 | 26 | 17 | 0 | 9 | buy 14, buy @ 1.1 |

**2 risks, 1 waste, 5 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.2 turns (holds 10, next step uses 42/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (no volume cap @ 9.6), but the home ask 10.70 is above it); labour need rises ~28/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 81 labour expired last turn (~136 coin): holding 80 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.8 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 69
- **flax plants**: flax plants buffer thin: 1.9 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 178
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **timber**: build materials for park 1 are in (705.0 held, 10 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 75% (EXPANSION), about 3 turns left; still to deliver: labour 65, limestone 15, timber 10; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 15 | 112.5 | 0 | off: covered |
| timber | 10 | 705.0 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 22

## Notes

- labour: projection runs 34 over real use lately; planning 744, not 779
- labour expiry guard: 81 bought labour expired last turn, buy 22 (not 294) this turn

## Prestige spending, cheapest coin per prestige first

1089 turns left: prestige gained now converts 99.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.4 | 53.9 | running |
| hold banquet 2 (pies) | mansion | 7 | 56.5 | 56.5 | thin at home: pasties, pies |
| hold banquet 2 (fish) | mansion | 6.8 | 57.9 | 57.9 |  |
| hold banquet 4 (pies) | mansion | 18 | 58.0 | 58.0 | thin at home: pasties, hop beer |
| hold banquet 1 (fish) | mansion | 4.2 | 58.4 | 58.4 |  |
| hold banquet 3 (pies) | mansion | 8 | 58.4 | 58.4 | thin at home: pasties, hop beer, pies |
| hold prayer 2 | chapel | 13 | 56.2 | 58.7 | needs a chapel (build cost 33,661); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 56.4 | 58.7 | needs a church (build cost 71,863); thin at home: jewellery, candles, furniture |
| hold sermon 2 | church | 24 | 57.0 | 60.0 | needs a church (build cost 71,863); thin at home: jewellery, furniture |
| hold feast 2 | townhouse | 2.6 | 57.9 | 60.4 | needs a townhouse (build cost 6,964) |
| hold mass 2 (premium) | cathedral | 360 | 60.0 | 60.8 | needs a cathedral (build cost 287,555); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 3 (fish) | mansion | 7.6 | 61.0 | 61.0 | thin at home: hop beer |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 74001604 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Brunnham: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~104 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hanstein | 380 | 0.11 | 0.30 (31/turn) | timber 14 (6.1->9.97), tackles 1 (173.25->195.7), charcoal 2 (1.8->3.59) | wrought iron 12 (13.86->15.77), butter 1 (74.55->78.85), seeds 9 (1.78->2.32), scythes 1 (28.77->30.59) | +84 |
| Etallaen | 774 | 0.22 | 0.10 (10/turn) | nets 6 (37.6->40.66), wine 6 (6.14->6.46) | wrought iron 13 (13.23->15.77), rope 1 (57.75->76.95), butter 1 (77.7->78.85), cloth 1 (7.35->8.1) | +66 |
| Amsdermund | 1111 | 0.40 | 0.30 (31/turn) | arms 6 (25.83->29.83), limestone 1 (21->45.22), wine 13 (6.14->6.84), lead bars 1 (12.4->14.34) | acid 2 (166.95->180.5), scythes 1 (29.19->30.59) | +60 |
| Chribruck | 1202 | 0.45 | 0.10 (10/turn) | - | acid 2 (157.5->180.5), butter 1 (71.92->78.85), wrought iron 1 (10.19->15.77), hides 1 (11.03->13.68) | +51 |
| Kleinburgh | 1440 | 0.58 | 0.10 (10/turn) | arms 2 (25.83->29.45), tallow 2 (30.45->33.25), varnish 1 (18.17->21.66) | wrought iron 13 (12.92->15.77), jewellery 1 (76.12->85.02), yarn 1 (3.3->4.62) | +50 |

**Best:** Hanstein at about +84 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 25.8, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 1 = 2.0 turns |
| beer |  | 51 @ min 3.7 | makes 28.0, uses 4.2, holds 412 (keeps 60): sells the surplus + 27/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 5.3 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 20 @ min 22.0 |  |
| grain | 13 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 103 = 7.9 turns |
| labour | 22 @ 2.2, stop - |  | uses 744.1/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 80 = 0.3 turns |
| limestone |  | 5 @ min 17.4 |  |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 8 @ min 36.6 | makes 6.0, uses 0.0, holds 48 (keeps 15): sells the surplus + 2/turn of the excess |
| porterage | 6 @ 1.1, stop - |  | uses 5.9/turn (observed), makes 0.0, holds 26 = 4.4 turns |
| tar | 3 @ 11.0, stop 5 |  | uses 1.1/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| timber |  | 41 @ min 8.5 | makes 12.0, uses 0.0, holds 705 (keeps 350): sells the surplus + 29/turn of the excess |
| tools | 5 @ 6.2, stop 36 |  | uses 4.5/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 44.5 turns |

## Chain sizing

Mode HOLD, garments sold 1.8/turn (+0.0 exported); plan makes 21.7 garments a turn.
Labour: own 450, everything else 411, chain may buy 350 -> chain allowance 389, chain plan 390 (+0 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.56 | 5.56 |
| ret | 3 | 0.99 | 0.99 |
| spin | 4 | 2.04 | 2.04 |
| weave | 3 | 0.84 | 0.84 |
| sew | 2 | 0.53 | 0.53 |

Buffers: flax fibres 63/82, thread 474/242, cloth 10/84
- chain plan needed 708 labour, budget left 389: cut to 389 (sewing capped at 0.53)

## Self-diagnosis

- R1: candles slot dry: 0.0 held, 1.5 a turn (luxury slot (+3 prestige)); our buy paused by the failsafe, home ask 79.0 (held back: paused by the failsafe at level 1: un-pause only at level 0)
- R1: prestige rate -3.90 a turn vs 12-turn median -0.95; likely: dry slot: candles
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R4: logging camp w/ tool, ropewalk 1, quarry 1 projected 0: short of labour (~103 needed); labour itself is not raised here
