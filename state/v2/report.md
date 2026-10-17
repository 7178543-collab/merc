# v2 shadow report

Turn 13353, 2026-10-17 18:53. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 8,706, prestige 3,280 (610 free, -1.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 138 | 0 | 4 | 0 | 0 | min_holding 60, sell 28, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 17 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 122 | 0 | 2 | 0 | 0 | min_holding 30, sell 29, sell @ 22 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 274 | 311 | 724 | 0 | 37 | buy 274, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 37 |
| porterage | 11 | 10 | 10 | 1 | 0 | buy 11, buy @ 1.1 |

**2 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.4 turns (holds 24, next step uses 54/turn) -> v2: check the step that makes it
- **porterage**: logging camp w/ tool ran short of porterage (buy is live (11 @ 1.1), 10 bought last turn); labour need rises ~22/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it

## Waste (money lost now)

- **labour**: 37 labour expired last turn (~63 coin): holding 274 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.6 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 71

## Notes

- labour: projection runs 73 over real use lately; planning 724, not 797
- labour expiry guard: 37 bought labour expired last turn, buy 274 (not 274) this turn

## Prestige spending, cheapest coin per prestige first

1048 turns left: prestige gained now converts 99.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.7 | 50.7 | running |
| hold banquet 2 (meat) | mansion | 6.8 | 57.6 | 57.6 | thin at home: wine |
| hold banquet 3 (meat) | mansion | 7.6 | 58.2 | 58.2 |  |
| hold sermon 2 (candles) | church | 31 | 56.0 | 58.7 | needs a church (build cost 79,365); thin at home: jewellery, candles, furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 58.8 | 58.8 | thin at home: wine, cured fish |
| hold prayer 2 | chapel | 13 | 56.4 | 58.9 | needs a chapel (build cost 32,634); thin at home: furniture |
| hold banquet 1 (meat) | mansion | 4.2 | 59.0 | 59.0 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 59.3 | 59.3 | thin at home: cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 59.8 | 59.8 |  |
| hold sermon 2 | church | 24 | 56.8 | 60.3 | needs a church (build cost 79,365); thin at home: jewellery, furniture |
| jousting 1 | arena | 170 | 60.2 | 60.3 | needs a arena (build cost 25,230); thin at home: protection, light armour, arms; needs weaponry skill |
| hold feast 2 | townhouse | 2.6 | 58.4 | 61.8 | needs a townhouse (build cost 8,962); thin at home: wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 110801910 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | cured meat 1 | -21 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Karlmoor: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn
- best towns now: Caillechâtel +59, Darmwald +35, Coburgbaum +19
- Caillechâtel would trade: beer sell 30 @ 6.3; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~102 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Disscester | 1474 | 0.59 | 0.20 (20/turn) | garments 25 (19.75->28.88) | steel ingots 2 (13.86->14.82) | +210 |
| Caillechâtel | 488 | 0.13 | 0.20 (20/turn) | beer 30 (2.91->7.6), light armour 1 (84->96.9), garments 10 (19.75->20.14), tools 4 (4.5->4.94) | cloth 13 (8.4->9.2), bricks 1 (5.46->12.25), cheese 8 (5.78->6.27), salt 2 (3.93->5.56) | +164 |
| Vauxvais | 204 | 0.06 | 0.10 (10/turn) | soap 1 (75.6->168.15), rope 3 (74->79.33), garments 22 (19.75->20.33), beer 30 (2.91->3.1) | pies 1 (18.79->19.76) | +119 |
| Darmwald | 1022 | 0.34 | 0.10 (10/turn) | rope 2 (74->104.5), bellows 1 (325.5->372.4), soap 1 (75.6->80.27), butter 1 (72.45->75.52) | cloth 8 (8.14->9.2) | +117 |
| Blanans | 297 | 0.08 | 0.10 (10/turn) | stockfish 1 (116.55->142.5), beer 30 (2.91->3.42), thread 8 (4.88->6.37), soap 1 (75.6->84.08) | cloth 34 (8.56->9.2), bricks 1 (7.4->12.25), hop beer 3 (8.4->8.74), pies 1 (18.59->19.76) | +85 |

**Best:** Disscester at about +210 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 28 @ min 3.7 | makes 28.0, uses 4.2, holds 138 (keeps 60): sells the surplus + 5/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 17 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 31 @ min 22.0 | makes 27.5, uses 2.1, holds 122 (keeps 30): sells the surplus + 6/turn of the excess |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 274 @ 2.2, stop - |  | uses 723.7/turn (brewery 1, flax farm 1, household), makes 450.0, holds 274 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 37.6 |  |
| porterage | 11 @ 1.1, stop - |  | uses 10.5/turn (observed), makes 0.0, holds 11 = 1.0 turns |
| rope |  | 7 @ min 72.0 | makes 2.2, uses 0.0, holds 58 (keeps 0): sells the surplus + 5/turn of the excess |
| tools | 4 @ 6.2, stop 31 |  | uses 3.8/turn (retting pit 1), makes 0.0, holds 199 = 52.3 turns |

## Chain sizing

Mode HOLD, garments sold 12.2/turn (+0.0 exported); plan makes 27.5 garments a turn.
Labour: own 450, everything else 362, chain may buy 350 -> chain allowance 438, chain plan 439 (+2 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.77 | 5.81 |
| ret | 3 | 1.03 | 1.03 |
| spin | 4 | 2.11 | 2.13 |
| weave | 3 | 1.08 | 1.07 |
| sew | 2 | 0.67 | 0.67 |

Buffers: flax fibres 58/79, thread 361/234, cloth 24/107
- chain plan needed 449 labour, budget left 438: cut to 438 (sewing capped at 0.67)

## Self-diagnosis

- R1: prestige rate -1.31 a turn vs 12-turn median +2.96; likely: no slot, building or contract cause found: check the impacts
- R2: ropewalk 1 blocked by rope space: 58 held of 60 capacity, we make 2.2 a turn; no buy on it: add a sell order or more capacity for rope
- R3: mansion 1 (mansion) finished but idle 3 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
