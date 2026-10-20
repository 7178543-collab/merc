# v2 shadow report

Turn 13426, 2026-10-20 19:56. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 6,400, prestige 3,397 (727 free, -0.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 52, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 56 | 0 | 2 | 0 | 0 | min_holding 30, sell 22, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 264 | 264 | 714 | 0 | 0 | buy 264, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 15 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 37.2 |
| porterage | 10 | 10 | 10 | 0 | 0 | buy 10, buy @ 1.1 |

**2 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.1 turns (holds 7, next step uses 46/turn) -> v2: check the step that makes it
- **flax plants**: flax plants buffer 1.0 turns (holds 80, next step uses 81/turn) -> v2: check the step that makes it

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.7 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 63
- **timber**: build materials for park 1, net maker152202386007001 are in (288.0 held, 116 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 33% (EXPANSION), about 9 turns left; still to deliver: labour 175, limestone 41, timber 27; ready for labour
- **net maker152202386007001** 41% (INITIAL), about 8 turns left; still to deliver: labour 119, timber 89, tools 12; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 41 | 80.7 | 0 | off: covered |
| timber | 116 | 288.0 | 0 | off: covered; switch v1's buy off |
| tools | 12 | 199.5 | 0 | off: covered |

Labour metered per turn while a site can progress: labour 35

## Notes

- labour: projection runs 75 over real use lately; planning 735, not 810

## Prestige spending, cheapest coin per prestige first

975 turns left: prestige gained now converts 99.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.8 | 53.8 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 55.1 | 55.1 |  |
| hold prayer 2 | chapel | 13 | 52.6 | 55.5 | needs a chapel (build cost 33,614); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 53.1 | 55.7 | needs a church (build cost 71,978); thin at home: candles, furniture |
| hold mass 2 (premium) | cathedral | 360 | 55.3 | 56.3 | needs a cathedral (build cost 287,070); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold sermon 2 | church | 24 | 52.9 | 56.3 | needs a church (build cost 71,978); thin at home: furniture |
| hold banquet 3 (pies) | mansion | 8 | 56.6 | 56.6 | thin at home: hop beer, pies |
| hold banquet 2 (fish) | mansion | 6.8 | 57.7 | 57.7 | thin at home: wine, cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 57.7 | 57.7 | thin at home: hop beer, cured fish |
| jousting 3 | arena | 230 | 57.7 | 57.9 | needs a arena (build cost 26,926); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 58.1 | 58.1 | thin at home: wine, pies |
| jousting 1 | arena | 170 | 58.4 | 58.5 | needs a arena (build cost 26,926); thin at home: protection, light armour, arms; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 120102307 | 0.1 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 185801747 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Rouhomme: furniture buy 5 @ 14.2, tools buy 5 @ 4.48; crew 0.1; est +55 a turn; stock: furniture 5 @ 14.2 (keep 145)
- **linen snake** on Neuborn: nothing pays; crew 0.0; est +0 a turn; best orders clear only -7 a turn after crew: ship stays at 0
- best towns now: Bremcop +82, Bedenis +77, Großaue +74, Toqueque +71, Etallaen +71
- Bremcop would trade: furniture buy 5 @ 12.5, rope sell 1 @ 99.0; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~102 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Caillechâtel | 488 | 0.13 | 0.20 (20/turn) | beer 43 (3.14->5.18), hides 2 (10.61->14.91), flax fibres 4 (4.75->5.46), copper ingots 1 (12.92->14.25) | spirits 1 (11.34->20.33), butter 1 (57.23->62.7), soap 1 (72.45->75.52), cheese 2 (6.67->7.12) | +110 |
| Heilegg | 826 | 0.23 | 0.40 (41/turn) | beer 51 (3.14->3.78), hinges 1 (32.55->41.99), acid 1 (115.5->122.55), gears 1 (61.43->67.92) | cheese 38 (6.09->7.12), candles 1 (74.55->76.5), tools 5 (4.75->5.3) | +82 |
| Amsdermund | 1111 | 0.39 | 0.30 (31/turn) | limestone 1 (20.68->47.31), acid 1 (115.5->125.4), hinges 1 (32.55->38.95), leather 1 (19.64->26.03) | cheese 30 (6.04->7.12), candles 1 (69.3->76.5), ploughs 1 (53.55->64.6), mouldboards 1 (36.12->39.9) | +79 |
| Hofkirchen | 991 | 0.32 | 0.20 (20/turn) | nets 3 (38.2->41.8), leather 1 (19.64->27.17), hinges 1 (32.55->39.33), acid 1 (115.5->120.65) | cheese 23 (6.3->7.12), candles 1 (71.4->76.5), mouldboards 1 (35.28->39.9), spirits 1 (15.75->20.33) | +68 |
| Etallaen | 774 | 0.21 | 0.30 (31/turn) | beer 51 (3.14->4.31), rope 1 (75->89.3), hinges 1 (32.55->36.1), grain 8 (2.78->3.44) | candles 1 (73.5->76.5), mouldboards 1 (37.38->39.9), tools 5 (4.94->5.3), resin 2 (1.68->2.2) | +61 |

**Best:** Caillechâtel at about +110 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 52 @ min 3.38 |  |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 22 @ min 20.0 | makes 23.4, uses 2.1, holds 56 (keeps 30): sells the surplus + 1/turn of the excess |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 285 @ 2.2, stop - |  | uses 735.1/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 264 = 0.9 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 37.2 |  |
| pasties | 3 @ 15.4, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 13 = 4.7 turns |
| porterage | 10 @ 1.1, stop - |  | uses 9.8/turn (observed), makes 0.0, holds 10 = 1.0 turns |
| rope |  | 4 @ min 73.0 | makes 2.2, uses 0.0, holds 18 (keeps 0): sells the surplus + 1/turn of the excess |
| timber |  | 8 @ min 6.5 |  |
| tools | 6 @ 6.2, stop 45 |  | uses 5.5/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 36.1 turns |

## Chain sizing

Mode HOLD, garments sold 15.2/turn (+0.0 exported); plan makes 23.0 garments a turn.
Labour: own 450, everything else 423, chain may buy 350 -> chain allowance 377, chain plan 377 (+0 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.08 | 5.08 |
| ret | 3 | 0.90 | 0.90 |
| spin | 4 | 1.86 | 1.86 |
| weave | 3 | 0.90 | 0.90 |
| sew | 2 | 0.57 | 0.56 |

Buffers: flax fibres 52/74, thread 400/217, cloth 7/90
- chain plan needed 488 labour, budget left 377: cut to 377 (sewing capped at 0.56)

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
