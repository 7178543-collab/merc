# v2 shadow report

Turn 13469, 2026-10-22 14:03. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 4,463, prestige 3,563 (443 free, -1.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 124 | 0 | 4 | 0 | 0 | min_holding 60, sell 53, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 67 | 0 | 2 | 0 | 0 | min_holding 75, sell 17, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 418 | 452 | 902 | 0 | 0 | buy 418, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 18 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 34.6 |
| porterage | 11 | 11 | 10 | 0 | 1 | buy 11, buy @ 1.1 |

**1 risks, 2 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.1 turns (holds 3, next step uses 32/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **Flax Wyrm**: Flax Wyrm cost 49 coin last turn (crew 0.50) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell
- **linen snake**: linen snake cost 49 coin last turn (crew 0.50) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.3 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 68
- **flax plants**: flax plants buffer thin: 1.1 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 176
- **timber**: build materials for farmstead 1 are in (299.0 held, 14 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **farmstead 1** 33% (EXPANSION), about 3 turns left; still to deliver: labour 67, timber 14; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| timber | 14 | 299.0 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 23

## Notes

- labour: projection runs 84 over real use lately; planning 902, not 983

## Prestige spending, cheapest coin per prestige first

932 turns left: prestige gained now converts 99.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.6 | 48.6 | running |
| hold banquet 4 (pies) | mansion | 18 | 49.1 | 49.1 | thin at home: pasties, hop beer, wine, pies |
| hold banquet 3 (pies) | mansion | 8 | 49.7 | 49.7 | thin at home: pasties, hop beer, pies |
| hold banquet 2 (pies) | mansion | 7 | 49.8 | 49.8 | thin at home: pasties, wine, pies |
| jousting 3 | arena | 230 | 52.5 | 52.6 | needs a arena (build cost 24,986); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 52.7 | 52.7 | thin at home: wine, hop beer, ham |
| hold banquet 2 (fish) | mansion | 6.8 | 53.2 | 53.2 | thin at home: wine |
| hold sermon 2 (candles) | church | 31 | 51.5 | 53.9 | needs a church (build cost 64,921); thin at home: jewellery, candles |
| hold banquet 3 (fish) | mansion | 7.6 | 54.1 | 54.1 | thin at home: hop beer |
| hold banquet 1 (fish) | mansion | 4.2 | 54.3 | 54.3 |  |
| hold prayer 2 | chapel | 13 | 51.9 | 54.7 | needs a chapel (build cost 31,934) |
| hold feast 2 | townhouse | 2.6 | 52.5 | 55.4 | needs a townhouse (build cost 6,967); thin at home: wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.5 / 0.50 | 49 | - | 0 | - | - | 0 |
| linen snake | 0.5 / 0.50 | 49 | - | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- best towns now: Caillechâtel +19
- Caillechâtel would trade: beer sell 31 @ 4.74; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~100 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hanstein | 380 | 0.10 | 0.40 (40/turn) | rope 2 (63.34->73.62), dye 1 (55.12->73.15), furniture 7 (11.76->13.68), lead bars 7 (14.38->15.67) | flax fibres 34 (5.15->6.55), flax plants 88 (1.25->1.72), cloth 7 (6.72->7.7), tools 3 (5.04->5.4) | +152 |
| Kleinburgh | 1440 | 0.56 | 0.20 (20/turn) | windows 2 (582.75->636.5), rope 2 (63.34->71.72), chisels 1 (12.92->15.58), lead bars 1 (14.38->16.43) | jewellery 1 (74.55->88.83), candles 1 (70.35->73), belts 1 (29.19->30.97) | +131 |
| Clairlond | 1288 | 0.47 | 0.10 (10/turn) | tackles 1 (166.95->260.3), rope 2 (63.34->75.52), lead bars 5 (14.38->16.62), hides 1 (12.18->17.39) | tools 3 (4.7->5.4), candles 1 (72.45->73), jewellery 1 (88.2->88.83) | +126 |
| Vauxvais | 204 | 0.06 | 0.20 (20/turn) | lathes 1 (210->254.6), beer 57 (3.18->3.86), rope 2 (63.34->70.3), tackles 1 (166.95->171.95) | cloth 33 (7.25->7.7), flax fibres 8 (5.83->6.55), malt 1 (4.85->6.65), tools 3 (4.77->5.4) | +122 |
| Caillechâtel | 488 | 0.13 | 0.20 (20/turn) | beer 31 (3.18->5.37), butter 1 (66.15->71.72), yarn 5 (3.51->4.33), chisels 1 (12.92->15.11) | flax fibres 10 (4.7->6.55), herbs 1 (24.78->31.73), flax plants 26 (1.22->1.72), jewellery 1 (84.53->88.83) | +106 |

**Best:** Hanstein at about +152 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 53 @ min 3.38 | makes 56.0, uses 4.2, holds 124 (keeps 60): sells the surplus + 1/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 14 @ min 20.0 |  |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 452 @ 2.2, stop - |  | uses 902.0/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 418 = 0.9 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 11 @ min 34.6 |  |
| pasties | 3 @ 16.8, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 4.9 turns |
| porterage | 10 @ 1.1, stop - |  | uses 10.3/turn (observed), makes 0.0, holds 11 = 1.1 turns |
| rope |  | 2 @ min 65.0 |  |
| timber |  | 8 @ min 6.8 |  |
| tools | 4 @ 6.2, stop 30 |  | uses 3.7/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 53.9 turns |

## Chain sizing

Mode HOLD, garments sold 15.1/turn (+2.3 exported); plan makes 17.2 garments a turn.
Labour: own 450, everything else 438, chain may buy 350 -> chain allowance 362, chain plan 361 (+7 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.49 | 5.61 |
| ret | 3 | 0.98 | 1.00 |
| spin | 4 | 2.01 | 2.05 |
| weave | 3 | 0.64 | 0.67 |
| sew | 2 | 0.40 | 0.42 |

Buffers: flax fibres 44/73, thread 267/214, cloth 3/67
- chain plan needed 624 labour, budget left 362: cut to 362 (sewing capped at 0.42)

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
