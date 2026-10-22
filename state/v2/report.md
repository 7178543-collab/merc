# v2 shadow report

Turn 13468, 2026-10-22 13:14. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 5,185, prestige 3,564 (444 free, -1.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 125 | 0 | 4 | 0 | 0 | min_holding 60, sell 53, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 52 | 0 | 2 | 0 | 0 | min_holding 75, sell 19, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 452 | 285 | 735 | 0 | 0 | buy 452, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 18 | 0 | 0 | 0 | 0 | min_holding 15, sell 10, sell @ 34.6 |
| porterage | 11 | 11 | 11 | 0 | 0 | buy 11, buy @ 1.1 |

**1 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.1 turns (holds 2, next step uses 38/turn) -> v2: check the step that makes it

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.2 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 72
- **flax plants**: flax plants buffer thin: 1.0 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 185
- **timber**: build materials for farmstead 1 are in (324.9 held, 20 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **farmstead 1** 0% (EXPANSION), about 3 turns left; still to deliver: labour 100, timber 20; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| timber | 20 | 324.9 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 34

## Notes

- labour: projection runs 75 over real use lately; planning 902, not 977

## Prestige spending, cheapest coin per prestige first

933 turns left: prestige gained now converts 99.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.3 | 48.3 | running |
| hold banquet 2 (pies) | mansion | 7 | 48.5 | 48.5 | thin at home: pasties, wine, pies |
| hold banquet 3 (pies) | mansion | 8 | 48.7 | 48.7 | thin at home: pasties, hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 48.8 | 48.8 | thin at home: hop beer, wine, pies |
| hold banquet 4 | mansion | 17.5 | 52.6 | 52.6 | thin at home: wine, hop beer, ham |
| jousting 3 | arena | 230 | 52.5 | 52.7 | needs a arena (build cost 24,990); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 52.9 | 52.9 | thin at home: wine, cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 54.0 | 54.0 | thin at home: hop beer, cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 54.2 | 54.2 | thin at home: cured fish |
| hold feast 2 | townhouse | 2.6 | 51.6 | 54.5 | needs a townhouse (build cost 6,927); thin at home: wine |
| hold sermon 2 (candles) | church | 31 | 51.9 | 54.5 | needs a church (build cost 65,646); thin at home: jewellery, candles, furniture |
| hold prayer 2 | chapel | 13 | 51.8 | 54.6 | needs a chapel (build cost 31,992) |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 10 | 120102307 | 0.044 | - | furniture 2 | -28 |
| linen snake | 0.0 / 0.00 | 0 | - | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Rouhomme: nothing pays; crew 0.0; est +0 a turn; best orders clear only -7 a turn after crew: ship stays at 0
- best towns now: Caillechâtel +19
- Caillechâtel would trade: beer sell 31 @ 4.74; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~100 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hanstein | 380 | 0.10 | 0.40 (40/turn) | rope 2 (63.03->73.62), dye 1 (55.12->73.15), furniture 7 (11.76->13.68), lead bars 7 (14.38->15.67) | flax fibres 34 (5.15->6.55), flax plants 92 (1.25->1.72), cloth 7 (6.72->7.7), tools 3 (5.04->5.4) | +154 |
| Kleinburgh | 1440 | 0.55 | 0.20 (20/turn) | windows 2 (582.75->636.5), rope 2 (63.03->71.72), chisels 1 (12.92->15.58), lead bars 1 (14.38->16.43) | jewellery 1 (74.55->88.83), candles 1 (70.35->73), belts 1 (29.19->30.97) | +131 |
| Clairlond | 1288 | 0.47 | 0.10 (10/turn) | tackles 1 (166.95->260.3), rope 2 (63.03->75.52), lead bars 5 (14.38->16.62), hides 1 (12.18->17.39) | tools 3 (4.7->5.4), candles 1 (72.45->73), jewellery 1 (88.2->88.83) | +128 |
| Vauxvais | 204 | 0.05 | 0.20 (20/turn) | lathes 1 (210->254.6), beer 57 (3.18->3.86), rope 2 (63.03->70.3), tackles 1 (166.95->171.95) | cloth 37 (7.25->7.7), flax fibres 8 (5.83->6.55), malt 1 (4.85->6.65), tools 3 (4.77->5.4) | +124 |
| Caillechâtel | 488 | 0.13 | 0.20 (20/turn) | beer 31 (3.18->5.37), butter 1 (66.15->71.72), yarn 5 (3.51->4.33), chisels 1 (12.92->15.11) | flax fibres 10 (4.7->6.55), herbs 1 (24.78->31.73), flax plants 26 (1.22->1.72), jewellery 1 (84.53->88.83) | +108 |

**Best:** Hanstein at about +154 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 53 @ min 3.38 | makes 56.0, uses 4.2, holds 125 (keeps 60): sells the surplus + 1/turn of the excess |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 12 = 7.7 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 17 @ min 20.0 |  |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 452 @ 2.2, stop - |  | uses 902.0/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 452 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 11 @ min 34.6 |  |
| pasties | 3 @ 13.1, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 4.9 turns |
| porterage | 11 @ 1.1, stop - |  | uses 10.6/turn (observed), makes 0.0, holds 11 = 1.0 turns |
| rope |  | 2 @ min 73.0 |  |
| timber |  | 8 @ min 6.7 |  |
| tools | 4 @ 6.2, stop 31 |  | uses 3.8/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 52.4 turns |

## Chain sizing

Mode HOLD, garments sold 15.1/turn (+2.3 exported); plan makes 16.4 garments a turn.
Labour: own 450, everything else 449, chain may buy 350 -> chain allowance 351, chain plan 351 (-34 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.81 | 5.49 |
| ret | 3 | 1.03 | 0.98 |
| spin | 4 | 2.13 | 2.01 |
| weave | 3 | 0.76 | 0.64 |
| sew | 2 | 0.47 | 0.40 |

Buffers: flax fibres 44/72, thread 272/211, cloth 2/64
- chain plan needed 667 labour, budget left 351: cut to 351 (sewing capped at 0.40)

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
