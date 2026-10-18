# v2 shadow report

Turn 13364, 2026-10-18 05:52. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 6,909, prestige 3,266 (596 free, -1.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 306 | 0 | 4 | 0 | 0 | min_holding 60, sell 34, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 284 | 0 | 2 | 0 | 0 | min_holding 30, sell 36, sell @ 22 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 261 | 261 | 681 | 0 | 30 | buy 241, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 15 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 38.6 |
| porterage | 11 | 11 | 10 | 0 | 1 | buy 11, buy @ 1.1 |

**1 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.7 turns (holds 35, next step uses 51/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **labour**: 30 labour expired last turn (~51 coin): holding 261 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax fibres**: flax fibres buffer thin: 1.9 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 61

## Notes

- labour: projection runs 75 over real use lately; planning 681, not 756
- labour expiry guard: 30 bought labour expired last turn, buy 231 (not 231) this turn

## Prestige spending, cheapest coin per prestige first

1037 turns left: prestige gained now converts 99.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.7 | 50.7 | running |
| hold sermon 2 (candles) | church | 31 | 53.5 | 56.3 | needs a church (build cost 82,097); thin at home: candles, furniture |
| hold prayer 2 | chapel | 13 | 55.3 | 58.0 | needs a chapel (build cost 33,508); thin at home: furniture |
| jousting 1 | arena | 170 | 58.0 | 58.1 | needs a arena (build cost 26,489); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 58.9 | 58.9 | thin at home: wine, cured fish |
| hold banquet 3 (pies) | mansion | 8 | 59.0 | 59.0 | thin at home: pies, candles |
| hold banquet 2 (meat) | mansion | 6.8 | 59.1 | 59.1 | thin at home: wine, cured meat |
| hold sermon 2 | church | 24 | 55.5 | 59.1 | needs a church (build cost 82,097); thin at home: furniture |
| hold banquet 3 (fish) | mansion | 7.6 | 59.2 | 59.2 | thin at home: cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 59.4 | 59.4 | thin at home: cured fish |
| hold banquet 3 (meat) | mansion | 7.6 | 59.4 | 59.4 | thin at home: cured meat |
| hold feast 2 | townhouse | 2.6 | 57.2 | 59.9 | needs a townhouse (build cost 6,916); thin at home: wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 64601365 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Disscester: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn
- best towns now: Caillechâtel +34, Fontaux +18
- Caillechâtel would trade: beer sell 25 @ 5.05; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~102 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Fontaux | 411 | 0.11 | 0.40 (41/turn) | cheese 19 (7.25->9.79), beer 44 (2.99->3.89), timber 12 (6.35->8.55), casks 3 (6.25->6.84) | pies 1 (14.8->16.72), cloth 10 (8.09->8.2), dyed yarn 1 (9.4->9.59) | +83 |
| Caillechâtel | 488 | 0.13 | 0.20 (20/turn) | beer 25 (2.99->4.89), salt 2 (4.35->4.94) | cloth 19 (7.72->8.2), flax plants 35 (1.38->1.85), flax fibres 12 (5.78->6.4), tallow 2 (21->22.99) | +64 |
| Hanstein | 380 | 0.10 | 0.30 (31/turn) | salt 5 (4.35->5.46), timber 8 (6.35->8.17), grain 4 (2.26->2.7), tools 9 (4.66->4.8) | flax plants 79 (1.31->1.85), thread 97 (4.7->4.98), seeds 8 (1.75->2.32), cloth 12 (8.09->8.2) | +54 |
| Grandgues | 152 | 0.04 | 0.10 (10/turn) | beer 44 (2.99->3.42), salt 3 (4.35->5.22), firewood 1 (1.78->4.73), flax plants 3 (1.3->1.96) | cloth 25 (7.3->8.2), garments 2 (20.79->21.6), hop beer 1 (7.67->8.55), tallow 2 (22.26->22.99) | +50 |
| Heilegg | 826 | 0.23 | 0.30 (31/turn) | beer 44 (2.99->4.03), salt 5 (4.35->5.27), grain 4 (2.26->2.75) | cheese 20 (5.88->6.46), steel ingots 2 (14.18->15.39), cloth 7 (7.77->8.2), flax fibres 2 (5.62->6.4) | +41 |

**Best:** Fontaux at about +83 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 42 @ min 3.7 | makes 28.0, uses 4.2, holds 306 (keeps 60): sells the surplus + 18/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 43 @ min 22.0 | makes 26.2, uses 2.1, holds 284 (keeps 30): sells the surplus + 19/turn of the excess |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 231 @ 2.2, stop - |  | uses 680.6/turn (brewery 1, flax farm 1, household), makes 450.0, holds 261 = 1.1 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 38.8 |  |
| porterage | 10 @ 1.1, stop - |  | uses 9.7/turn (observed), makes 0.0, holds 11 = 1.1 turns |
| rope |  | 7 @ min 78.0 | makes 2.2, uses 0.0, holds 54 (keeps 0): sells the surplus + 4/turn of the excess |
| timber |  | 12 @ min 6.7 | makes 8.4, uses 0.0, holds 396 (keeps 350): sells the surplus + 3/turn of the excess |
| tools | 4 @ 6.2, stop 29 |  | uses 3.5/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 56.8 turns |

## Chain sizing

Mode HOLD, garments sold 6.0/turn (+4.9 exported); plan makes 24.6 garments a turn.
Labour: own 450, everything else 362, chain may buy 350 -> chain allowance 438, chain plan 380 (-14 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.97 | 4.88 |
| ret | 3 | 0.88 | 0.87 |
| spin | 4 | 1.82 | 1.78 |
| weave | 3 | 1.02 | 0.97 |
| sew | 2 | 0.64 | 0.60 |

Buffers: flax fibres 58/76, thread 496/224, cloth 35/97

## Self-diagnosis

- R2: ropewalk 1 blocked by rope space: 54 held of 60 capacity, we make 2.2 a turn; no buy on it: add a sell order or more capacity for rope
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
