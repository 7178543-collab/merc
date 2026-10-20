# v2 shadow report

Turn 13424, 2026-10-20 17:55. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 6,906, prestige 3,398 (728 free, -0.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 52, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 61 | 0 | 2 | 0 | 0 | min_holding 30, sell 18, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 264 | 264 | 714 | 0 | 0 | buy 264, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 15 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 36.6 |
| porterage | 5 | 5 | 5 | 5 | 0 | buy 10, buy @ 1.1 |

**2 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.1 turns (holds 6, next step uses 46/turn) -> v2: check the step that makes it
- **porterage**: logging camp w/ tool ran short of porterage (buy is live (10 @ 1.1), 5 bought last turn); labour need rises ~22/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.7 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 61
- **flax plants**: flax plants buffer thin: 1.1 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 158
- **timber**: build materials for park 1, net maker152202386007001 are in (313.6 held, 147 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 16% (EXPANSION), about 11 turns left; still to deliver: labour 219, limestone 51, timber 34; ready for labour
- **net maker152202386007001** 25% (INITIAL), about 9 turns left; still to deliver: labour 150, timber 113, tools 15; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 51 | 90.7 | 0 | off: covered |
| timber | 147 | 313.6 | 0 | off: covered; switch v1's buy off |
| tools | 15 | 199.7 | 0 | off: covered |

Labour metered per turn while a site can progress: labour 37

## Notes

- labour: projection runs 75 over real use lately; planning 714, not 789

## Prestige spending, cheapest coin per prestige first

977 turns left: prestige gained now converts 99.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.2 | 53.2 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 55.0 | 55.0 |  |
| hold prayer 2 | chapel | 13 | 52.4 | 55.2 | needs a chapel (build cost 33,468); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 52.7 | 55.4 | needs a church (build cost 73,996); thin at home: candles, furniture |
| hold mass 2 (premium) | cathedral | 360 | 55.2 | 56.1 | needs a cathedral (build cost 292,110); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold sermon 2 | church | 24 | 52.7 | 56.2 | needs a church (build cost 73,996); thin at home: furniture |
| hold banquet 3 (pies) | mansion | 8 | 56.6 | 56.6 | thin at home: pasties |
| hold banquet 2 (fish) | mansion | 6.8 | 56.8 | 56.8 | thin at home: wine, cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 57.4 | 57.4 | thin at home: cured fish |
| hold banquet 2 (pies) | mansion | 7 | 57.6 | 57.6 | thin at home: pasties, wine |
| jousting 3 | arena | 230 | 58.2 | 58.3 | needs a arena (build cost 27,371); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 58.5 | 58.5 | thin at home: pasties, wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 120102307 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 185801747 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Rouhomme: nothing pays; crew 0.0; est +0 a turn; stock: furniture 2 @ 14.2 (keep 145); best orders clear only 14 a turn after crew: ship stays at 0
- **linen snake** on Neuborn: nothing pays; crew 0.0; est +0 a turn
- best towns now: Bedenis +35, Toqueque +28, Briclives +25, Grandgues +23, Calange +23
- Bedenis would trade: furniture buy 2 @ 13.7, rope sell 3 @ 82.0; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~101 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Dortdorf | 871 | 0.25 | 0.10 (10/turn) | plate armour 1 (1648.5->1957), lead bars 9 (14.91->15.96), copper ingots 1 (13.55->15.2), flax fibres 2 (4.68->5.42) | jewellery 1 (65.62->75.05), pasties 2 (14.38->18.1), hop beer 2 (8.66->9.88), cheese 3 (6.46->6.84) | +329 |
| Etallaen | 774 | 0.21 | 0.30 (30/turn) | beer 51 (3.14->4.18), grain 8 (2.64->3.53), hinges 1 (34.23->36.1) | plate armour 1 (1186.5->1301.5), mouldboards 1 (36.96->41.61), cloth 9 (7.35->7.85), pasties 1 (14.7->18.1) | +165 |
| Blanans | 297 | 0.08 | 0.10 (10/turn) | stockfish 1 (126->133), dyed yarn 1 (10.5->12.44), flax fibres 3 (4.68->5.51), lead ore 1 (7.88->8.98) | plate armour 1 (1228.5->1301.5), cloth 37 (7.46->7.85), mouldboards 1 (33.39->41.61), pasties 2 (15.33->18.1) | +108 |
| Fontaux | 411 | 0.11 | 0.30 (30/turn) | cheese 18 (7.61->9.79), beer 51 (3.14->3.72), charcoal 14 (2.12->3.42), flax fibres 4 (4.68->5.7) | pasties 2 (11.76->18.1), mouldboards 1 (35.49->41.61), cloth 6 (7.25->7.85), slaked lime 1 (8.03->11.49) | +91 |
| Heilegg | 826 | 0.23 | 0.40 (40/turn) | acid 1 (121.8->129.2), glass ingots 2 (54.6->58.42), hinges 1 (34.23->42.18), lead bars 9 (14.91->15.86) | cheese 37 (6.2->6.84), pasties 2 (14.7->18.1), candles 1 (74.55->76.5), hop beer 2 (8.4->9.88) | +73 |

**Best:** Dortdorf at about +329 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 52 @ min 3.38 |  |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 24 @ min 20.0 | makes 23.4, uses 2.1, holds 61 (keeps 30): sells the surplus + 2/turn of the excess |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 264 @ 2.2, stop - |  | uses 714.0/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 264 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 36.8 |  |
| pasties | 3 @ 19.0, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 4.9 turns |
| porterage | 10 @ 1.1, stop - |  | uses 9.7/turn (observed), makes 0.0, holds 5 = 0.5 turns |
| rope |  | 3 @ min 73.0 |  |
| tools | 4 @ 6.2, stop 31 |  | uses 3.8/turn (retting pit 1), makes 0.0, holds 200 = 53.1 turns |

## Chain sizing

Mode HOLD, garments sold 11.7/turn (+0.0 exported); plan makes 23.4 garments a turn.
Labour: own 450, everything else 425, chain may buy 350 -> chain allowance 375, chain plan 376 (+0 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.97 | 5.00 |
| ret | 3 | 0.88 | 0.89 |
| spin | 4 | 1.82 | 1.83 |
| weave | 3 | 0.92 | 0.91 |
| sew | 2 | 0.57 | 0.57 |

Buffers: flax fibres 53/74, thread 428/218, cloth 6/91
- chain plan needed 474 labour, budget left 375: cut to 375 (sewing capped at 0.57)

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
- R4: logging camp w/ tool projected 0 of 7 (limited by porterage)
