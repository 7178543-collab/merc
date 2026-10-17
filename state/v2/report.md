# v2 shadow report

Turn 13352, 2026-10-17 17:47. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,132, prestige 3,282 (612 free, -1.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 134 | 0 | 4 | 0 | 0 | min_holding 60, sell 28, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 5 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 104 | 0 | 2 | 0 | 0 | min_holding 30, sell 26, sell @ 22 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 311 | 281 | 724 | 0 | 7 | buy 311, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 36.4 |
| porterage | 10 | 10 | 10 | 1 | 0 | buy 10, buy @ 1.1 |

**2 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.4 turns (holds 24, next step uses 54/turn) -> v2: check the step that makes it
- **porterage**: logging camp w/ tool ran short of porterage (buy is live (10 @ 1.1), 10 bought last turn); labour need rises ~22/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.6 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 71

## Notes

- labour: projection runs 73 over real use lately; planning 724, not 797

## Prestige spending, cheapest coin per prestige first

1049 turns left: prestige gained now converts 99.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.0 | 51.0 | running |
| hold banquet 2 (meat) | mansion | 6.8 | 57.4 | 57.4 | thin at home: wine |
| hold banquet 3 (meat) | mansion | 7.6 | 58.0 | 58.0 |  |
| hold prayer 2 | chapel | 13 | 56.5 | 59.1 | needs a chapel (build cost 33,654); thin at home: furniture |
| hold banquet 1 (meat) | mansion | 4.2 | 60.2 | 60.2 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 60.6 | 60.6 | thin at home: wine, cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 60.8 | 60.8 | thin at home: cured fish |
| jousting 1 | arena | 170 | 60.8 | 61.0 | needs a arena (build cost 25,977); thin at home: protection, light armour, arms; needs weaponry skill |
| hold feast 2 | townhouse | 2.6 | 58.5 | 61.8 | needs a townhouse (build cost 8,950); thin at home: wine |
| hold banquet 4 (pies) | mansion | 18 | 63.1 | 63.1 | thin at home: wine, candles |
| hold banquet 1 (fish) | mansion | 4.2 | 63.3 | 63.3 | thin at home: cured fish |
| hold banquet 3 (pies) | mansion | 8 | 63.4 | 63.4 | thin at home: pies, candles |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 110801910 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | cured meat 5 | -109 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Karlmoor: nothing pays; crew 0.0; est +0 a turn; best orders clear only 12 a turn after crew: ship stays at 0
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn
- best towns now: Caillechâtel +71, Cobholme +52, Chatgnan +20, Coburgbaum +18
- Caillechâtel would trade: beer sell 29 @ 6.0; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~102 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Caillechâtel | 488 | 0.13 | 0.20 (20/turn) | beer 29 (2.9->7.36), light armour 1 (84->95.95), tools 8 (4.5->5.37), flax fibres 4 (5.05->6.22) | bricks 1 (5.51->12.16), cloth 13 (8.35->8.8), salt 2 (3.76->5.56) | +156 |
| Cobholme | 1564 | 0.64 | 0.50 (51/turn) | beer 29 (2.9->6.65), light armour 2 (84->95), cookware 4 (21.84->23.75), cheese 5 (6.14->7.12) | jewellery 1 (84.53->132.05), ploughs 1 (53.55->69.83), salt 3 (4.89->5.56) | +154 |
| Heilegg | 826 | 0.23 | 0.10 (10/turn) | tackles 2 (170.1->190), nets 4 (38->39.14), slaked lime 1 (6.35->9.5), thread 8 (4.66->5.13) | jewellery 1 (78.75->132.05), pies 2 (16.28->19.76), cloth 11 (8.14->8.8), salt 4 (4.05->5.56) | +115 |
| Arnsreuth | 921 | 0.28 | 0.30 (31/turn) | beer 29 (2.9->3.91), tools 16 (4.5->4.84) | jewellery 1 (77.7->132.05), cloth 53 (7.77->8.8), salt 4 (4.28->5.56), bricks 1 (4.62->12.16) | +115 |
| Darmwald | 1022 | 0.34 | 0.10 (10/turn) | bellows 1 (325.5->372.4), rope 1 (74->92.15), tackles 1 (170.1->172.9) | jewellery 1 (90.3->132.05), cloth 10 (7.77->8.8), salt 2 (4.77->5.56) | +110 |

**Best:** Caillechâtel at about +156 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 28 @ min 3.7 | makes 28.0, uses 4.2, holds 134 (keeps 60): sells the surplus + 4/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 29 @ min 22.0 | makes 27.5, uses 2.1, holds 104 (keeps 30): sells the surplus + 4/turn of the excess |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 274 @ 2.2, stop - |  | uses 723.7/turn (brewery 1, flax farm 1, household), makes 450.0, holds 311 = 1.1 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 37.0 |  |
| porterage | 11 @ 1.1, stop - |  | uses 10.5/turn (observed), makes 0.0, holds 10 = 0.9 turns |
| rope |  | 7 @ min 72.0 | makes 2.2, uses 0.0, holds 56 (keeps 0): sells the surplus + 4/turn of the excess |
| tools | 4 @ 6.2, stop 29 |  | uses 3.6/turn (retting pit 1), makes 0.0, holds 200 = 55.6 turns |

## Chain sizing

Mode HOLD, garments sold 12.6/turn (+0.0 exported); plan makes 27.5 garments a turn.
Labour: own 450, everything else 362, chain may buy 350 -> chain allowance 438, chain plan 438 (+0 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.77 | 5.79 |
| ret | 3 | 1.03 | 1.03 |
| spin | 4 | 2.11 | 2.12 |
| weave | 3 | 1.08 | 1.07 |
| sew | 2 | 0.67 | 0.67 |

Buffers: flax fibres 58/80, thread 368/234, cloth 24/107
- chain plan needed 460 labour, budget left 438: cut to 438 (sewing capped at 0.67)

## Self-diagnosis

- R1: prestige rate -1.31 a turn vs 12-turn median +2.98; likely: no slot, building or contract cause found: check the impacts
- R3: mansion 1 (mansion) finished but idle 2 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
