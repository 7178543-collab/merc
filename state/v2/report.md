# v2 shadow report

Turn 13358, 2026-10-17 23:43. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,062, prestige 3,274 (604 free, -1.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 163 | 0 | 4 | 0 | 0 | min_holding 60, sell 30, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 17 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 129 | 0 | 2 | 0 | 0 | min_holding 30, sell 30, sell @ 22 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 273 | 282 | 721 | 0 | 11 | buy 273, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 37.4 |
| porterage | 11 | 11 | 10 | 0 | 1 | buy 11, buy @ 1.1 |

**1 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.7 turns (holds 36, next step uses 54/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **Flax Wyrm**: Flax Wyrm cost 21 coin last turn (crew 0.20) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.6 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 71

## Notes

- labour: projection runs 73 over real use lately; planning 732, not 806

## Prestige spending, cheapest coin per prestige first

1043 turns left: prestige gained now converts 99.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.6 | 51.6 | running |
| hold banquet 2 (meat) | mansion | 6.8 | 56.3 | 56.3 | thin at home: wine |
| hold banquet 3 (meat) | mansion | 7.6 | 57.2 | 57.2 |  |
| hold banquet 3 (pies) | mansion | 8 | 57.9 | 57.9 | thin at home: pies |
| jousting 1 | arena | 170 | 57.8 | 58.0 | needs a arena (build cost 23,537); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 58.2 | 58.2 | thin at home: wine, cured fish |
| hold banquet 2 (pies) | mansion | 7 | 58.2 | 58.2 | thin at home: wine, pies |
| hold prayer 2 | chapel | 13 | 56.0 | 58.3 | needs a chapel (build cost 29,882); thin at home: furniture |
| hold banquet 1 (meat) | mansion | 4.2 | 58.4 | 58.4 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 58.9 | 58.9 | thin at home: cured fish |
| hold feast 2 | townhouse | 2.6 | 56.7 | 59.3 | needs a townhouse (build cost 6,944); thin at home: wine |
| hold sermon 2 (candles) | church | 31 | 57.1 | 59.7 | needs a church (build cost 76,776); thin at home: jewellery, candles, furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.20 | 21 | 64601365 | 0.124 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Disscester: nothing pays; crew 0.0; est +0 a turn; best orders clear only -6 a turn after crew: ship stays at 0
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn
- best towns now: Caillechâtel +47, Cobholme +22
- Caillechâtel would trade: beer sell 21 @ 6.2, grain buy 13 @ 2.44; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~104 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Rouhomme | 368 | 0.10 | 0.60 (62/turn) | bread 145 (2.37->2.83), beer 32 (2.94->3.76), lead ore 6 (7.25->9.97), limestone 1 (12.92->28.31) | spinning wheels 1 (216.3->266), jewellery 1 (78.75->126.35), cloth 24 (7.46->8.4), dyed yarn 1 (5.21->9.12) | +196 |
| Grandgues | 152 | 0.04 | 0.10 (10/turn) | stockfish 1 (121.8->176.7), rope 4 (77->80.27), beer 32 (2.94->3.27), charcoal 10 (2.35->3.17) | jewellery 1 (89.25->126.35), cloth 8 (7.3->8.4), grain 13 (3.04->3.58), garments 2 (21->21.8) | +143 |
| Cobholme | 1564 | 0.65 | 0.60 (62/turn) | beer 32 (2.94->5.56), cured fish 7 (26.04->30.78), light armour 1 (84.53->94.52) | jewellery 1 (93.45->126.35), ploughs 1 (56.7->71.25), candles 1 (74.55->79) | +116 |
| Blanans | 297 | 0.08 | 0.10 (10/turn) | cookware 4 (21.84->26.22), flax plants 3 (1.26->2.38), soap 1 (80.85->82.65), canvas 2 (32.97->33.25) | jewellery 1 (84.53->126.35), cloth 36 (7.82->8.4), grain 13 (2.84->3.58), candles 1 (78.23->79) | +87 |
| Disscester | 1474 | 0.59 | 0.10 (10/turn) | cookware 4 (21.84->22.8) | bellows 1 (183.75->233.7), jewellery 1 (92.92->126.35), ploughs 1 (63.53->71.25), candles 1 (78.23->79) | +83 |

**Best:** Rouhomme at about +196 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 30 @ min 3.7 | makes 28.0, uses 4.2, holds 163 (keeps 60): sells the surplus + 7/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 17 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 32 @ min 22.0 | makes 27.9, uses 2.1, holds 129 (keeps 30): sells the surplus + 6/turn of the excess |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 282 @ 2.2, stop - |  | uses 732.3/turn (brewery 1, flax farm 1, household), makes 450.0, holds 273 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 37.6 |  |
| porterage | 10 @ 1.1, stop - |  | uses 10.5/turn (observed), makes 0.0, holds 11 = 1.0 turns |
| rope |  | 7 @ min 75.0 | makes 2.2, uses 0.0, holds 60 (keeps 0): sells the surplus + 5/turn of the excess |
| timber |  | 17 @ min 6.7 | makes 8.4, uses 0.0, holds 465 (keeps 350): sells the surplus + 9/turn of the excess |
| tools | 4 @ 6.2, stop 31 |  | uses 3.8/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 52.6 turns |

## Chain sizing

Mode HOLD, garments sold 11.7/turn (+4.9 exported); plan makes 28.7 garments a turn.
Labour: own 450, everything else 362, chain may buy 350 -> chain allowance 438, chain plan 439 (-2 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.71 | 5.61 |
| ret | 3 | 1.02 | 1.00 |
| spin | 4 | 2.09 | 2.05 |
| weave | 3 | 1.08 | 1.12 |
| sew | 2 | 0.68 | 0.70 |

Buffers: flax fibres 58/81, thread 437/239, cloth 36/112
- chain plan needed 498 labour, budget left 438: cut to 438 (sewing capped at 0.70)

## Self-diagnosis

- R1: prestige rate -1.28 a turn vs 12-turn median +0.81; likely: no slot, building or contract cause found: check the impacts
- R2: ropewalk 1 blocked by rope space: 60 held of 60 capacity, we make 2.2 a turn; no buy on it: add a sell order or more capacity for rope
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
