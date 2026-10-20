# v2 shadow report

Turn 13423, 2026-10-20 16:59. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 7,201, prestige 3,399 (729 free, -0.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 52, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 2 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 58 | 0 | 2 | 0 | 0 | min_holding 30, sell 19, sell @ 20 |
| grain | 104 | 0 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 264 | 264 | 714 | 0 | 0 | buy 264, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 36.2 |
| porterage | 5 | 5 | 5 | 5 | 0 | buy 5, buy @ 1.1 |

**3 risks, 0 waste, 4 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.2 turns (holds 6, next step uses 33/turn) -> v2: check the step that makes it
- **porterage**: logging camp w/ tool ran short of porterage (buy is live (5 @ 1.1), 5 bought last turn); labour need rises ~22/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **porterage**: buying 5, short of ~10 needed -> v2: buy 10

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax fibres**: flax fibres buffer thin: 1.7 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 61
- **flax plants**: flax plants buffer thin: 1.1 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 158
- **timber**: build materials for park 1, net maker152202386007001 are in (330.6 held, 163 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 8% (EXPANSION), about 12 turns left; still to deliver: labour 240, limestone 56, timber 37; ready for labour
- **net maker152202386007001** 16% (INITIAL), about 11 turns left; still to deliver: labour 168, timber 126, tools 17; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 56 | 95.7 | 0 | off: covered |
| timber | 163 | 330.6 | 0 | off: covered; switch v1's buy off |
| tools | 17 | 199.5 | 0 | off: covered |

Labour metered per turn while a site can progress: labour 36

## Notes

- labour: projection runs 75 over real use lately; planning 714, not 789

## Prestige spending, cheapest coin per prestige first

978 turns left: prestige gained now converts 99.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.9 | 52.4 | running |
| hold prayer 2 | chapel | 13 | 52.1 | 54.7 | needs a chapel (build cost 31,352); thin at home: furniture |
| hold banquet 1 (fish) | mansion | 4.2 | 54.9 | 54.9 |  |
| hold sermon 2 (candles) | church | 31 | 52.3 | 54.9 | needs a church (build cost 70,952); thin at home: jewellery, candles, furniture |
| hold sermon 2 | church | 24 | 52.4 | 55.7 | needs a church (build cost 70,952); thin at home: jewellery, furniture |
| hold mass 2 (premium) | cathedral | 360 | 55.1 | 56.0 | needs a cathedral (build cost 282,680); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 3 (pies) | mansion | 8 | 56.1 | 56.1 | thin at home: pasties |
| jousting 1 | arena | 170 | 56.1 | 56.3 | needs a arena (build cost 25,904); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 56.5 | 56.5 | thin at home: wine, cured fish |
| hold banquet 2 (pies) | mansion | 7 | 56.9 | 56.9 | thin at home: pasties, wine |
| hold banquet 3 (fish) | mansion | 7.6 | 57.1 | 57.1 | thin at home: cured fish |
| hold banquet 4 (pies) | mansion | 18 | 57.7 | 57.7 | thin at home: wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 10 | 120102307 | 0.112 | - | furniture 7 | -99 |
| linen snake | 0.1 / 0.26 | 26 | 185801747 | 0.112 | - | furniture 1 | -14 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Rouhomme: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Neuborn: nothing pays; crew 0.0; est +0 a turn

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~101 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Fontaux | 411 | 0.11 | 0.20 (20/turn) | cheese 25 (7.56->9.79), casks 6 (5.99->9.5), charcoal 14 (2.18->3.32), flax fibres 3 (4.64->5.56) | mouldboards 1 (30.03->41.04), slaked lime 1 (8.24->15.96), pasties 2 (11.34->14.8), cloth 7 (7.25->7.9) | +109 |
| Etallaen | 774 | 0.21 | 1.00 (101/turn) | cured fish 4 (24.57->34.96), beer 42 (3.14->3.97), dyed cloth 1 (13.02->19.38), rope 0 (75.5->79.33) | cloth 15 (7.35->7.9), slaked lime 0 (10.4->15.96), mouldboards 0 (36.96->41.04), flax fibres 0 (4.64->5.95) | +90 |
| Vauxvais | 204 | 0.06 | 0.10 (10/turn) | wax 7 (21.63->27.17), medicine 1 (139.65->154.85), bricks 2 (7.04->9.5), flax fibres 4 (4.64->5.27) | limestone 2 (10.5->19.6), slaked lime 1 (10.82->15.96), spirits 1 (17.01->20.33), mouldboards 1 (39.27->41.04) | +81 |
| Großmühle | 751 | 0.20 | 0.10 (10/turn) | copper ingots 1 (13.86->16.25), flax fibres 2 (4.64->6.17), varnish 3 (17.64->18.05), cloth 1 (6.63->6.98) | bellows 1 (205.8->245.1), ploughs 1 (42.42->63.65), cheese 10 (5.88->6.74), pasties 1 (10.45->14.8) | +74 |
| Grandgues | 152 | 0.04 | 0.20 (20/turn) | beer 51 (3.14->3.55), charcoal 14 (2.18->3.42), butter 3 (73.5->74.58), hinges 1 (35.07->37.62) | cheese 19 (5.88->6.74), cloth 11 (7.19->7.9), mouldboards 1 (35.91->41.04), hop beer 1 (7.93->8.88) | +60 |

**Best:** Fontaux at about +109 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 26.0, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 52 @ min 3.38 |  |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 18 @ min 20.0 | makes 16.9, uses 2.1, holds 58 (keeps 30): sells the surplus + 3/turn of the excess |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 264 @ 2.2, stop - |  | uses 714.0/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 264 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 36.6 |  |
| pasties | 3 @ 15.5, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 4.9 turns |
| porterage | 10 @ 1.1, stop - |  | uses 9.7/turn (observed), makes 0.0, holds 5 = 0.5 turns |
| rope |  | 3 @ min 73.5 |  |
| tools | 4 @ 6.2, stop 31 |  | uses 3.8/turn (retting pit 1), makes 0.0, holds 199 = 53.1 turns |

## Chain sizing

Mode HOLD, garments sold 10.1/turn (+0.0 exported); plan makes 23.4 garments a turn.
Labour: own 450, everything else 424, chain may buy 350 -> chain allowance 376, chain plan 375 (+43 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.93 | 4.97 |
| ret | 3 | 0.88 | 0.88 |
| spin | 4 | 1.80 | 1.82 |
| weave | 3 | 0.70 | 0.92 |
| sew | 2 | 0.41 | 0.57 |

Buffers: flax fibres 53/74, thread 441/219, cloth 6/92
- chain plan needed 472 labour, budget left 376: cut to 376 (sewing capped at 0.57)

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
- R4: logging camp w/ tool projected 0 of 7 (limited by porterage)
- R7 stale ask: rope ask 76.5 over the market for 5 turns: the town trades ~3 a turn at 75.5, we sold 0 with 13 over what we keep -> **sell price 76.5 -> 75.5 (last trade 75.5, floor 63.35)** (ok)
