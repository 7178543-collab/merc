# v2 shadow report

Turn 13377, 2026-10-18 18:54. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 5,588, prestige 3,296 (626 free, -1.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 347 | 0 | 4 | 0 | 0 | min_holding 60, sell 48, sell @ 3.54 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 5 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 294 | 0 | 2 | 0 | 0 | min_holding 30, sell 29, sell @ 21.2 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 45 | 206 | 457 | 0 | 199 | buy 45, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 59 | 0 | 0 | 0 | 0 | min_holding 15, sell 12, sell @ 34 |
| porterage | 9 | 4 | 4 | 3 | 0 | buy 9, buy @ 1.1 |

**1 risks, 2 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **porterage**: logging camp w/ tool ran short of porterage (buy is live (9 @ 1.1), 4 bought last turn); labour need rises ~22/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it

## Waste (money lost now)

- **Flax Wyrm**: Flax Wyrm cost 48 coin last turn (crew 0.50) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell
- **labour**: 199 labour expired last turn (~317 coin): holding 45 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **cloth**: cloth buffer thin: 1.7 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 38

## Notes

- labour: projection runs 73 over real use lately; planning 472, not 545
- labour expiry guard: 199 bought labour expired last turn, buy 7 (not 22) this turn

## Prestige spending, cheapest coin per prestige first

1024 turns left: prestige gained now converts 99.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.7 | 47.7 | running |
| hold sermon 2 (candles) | church | 31 | 52.3 | 55.0 | needs a church (build cost 80,000); thin at home: jewellery, candles, furniture |
| hold prayer 2 | chapel | 13 | 53.9 | 56.6 | needs a chapel (build cost 33,154); thin at home: furniture |
| hold feast 2 | townhouse | 2.6 | 54.2 | 57.0 | needs a townhouse (build cost 7,482); thin at home: wine |
| hold banquet 2 (fish) | mansion | 6.8 | 57.3 | 57.3 | thin at home: wine, cured fish |
| hold sermon 2 | church | 24 | 53.7 | 57.3 | needs a church (build cost 80,000); thin at home: jewellery, furniture |
| hold banquet 3 (pies) | mansion | 8 | 57.4 | 57.4 | thin at home: pasties, hop beer, pies, candles |
| hold banquet 2 (pies) | mansion | 7 | 57.6 | 57.6 | thin at home: pasties, wine, pies, candles |
| hold banquet 2 (meat) | mansion | 6.8 | 58.1 | 58.1 | thin at home: wine |
| jousting 1 | arena | 170 | 57.9 | 58.1 | needs a arena (build cost 25,368); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 58.5 | 58.5 | thin at home: hop beer, cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 58.6 | 58.6 | thin at home: cured fish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.5 / 0.50 | 48 | - | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 10 | 151802239 | 0.372 | nets 2 | furniture 21, pasties 3 | -297 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: furniture buy 21 @ 14.0, pasties buy 2 @ 15.3; crew 0.1; est +258 a turn; stock: furniture 21 @ 14.0 (keep 140); stock: pasties 2 @ 15.3 (keep 14)
- best towns now: Hofkirchen +387, Pontmont +387, Heilegg +352, Cobholme +351, Amsdermund +333
- Hofkirchen would trade: furniture buy 33 @ 13.2; crew 0.5

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~97 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Vauxvais | 204 | 0.05 | 0.40 (39/turn) | bread 146 (2.25->2.58), rope 3 (79->84.08), butter 2 (91.35->96.9), tools 16 (4.24->4.71) | flax fibres 14 (5.88->6.35), thread 39 (4.85->4.98), dyed cloth 2 (11.55->12.44), pasties 1 (12.81->13.01) | +77 |
| Bedenis | 566 | 0.15 | 0.10 (10/turn) | nets 5 (37.4->43.32), candles 1 (70.88->85.02), lead ore 2 (9.13->16.15), tools 16 (4.24->4.99) | wax 1 (23.1->23.75), flax fibres 1 (5.88->6.35), garments 2 (21->21.2) | +73 |
| Fontaux | 411 | 0.11 | 0.30 (29/turn) | beer 45 (2.97->4.2), charcoal 13 (1.81->3), hop beer 1 (9.61->13.68), arms 2 (25.62->27.17) | flax fibres 10 (5.99->6.35), cheese 15 (6.04->6.22), pies 2 (16.8->17.48) | +67 |
| Darmwald | 1022 | 0.32 | 0.10 (10/turn) | bellows 1 (312.9->383.8), tallow 1 (19.95->21.47), wine 1 (5.72->7.5), cloth 2 (6.6->7.03) | steel ingots 1 (13.02->15.2) | +67 |
| Rouhomme | 368 | 0.10 | 0.60 (58/turn) | beer 47 (2.97->3.76), bread 146 (2.25->2.68), tallow 1 (19.95->23.75), flax fibres 1 (4.8->5.03) | blades 2 (14.7->15.48), flax fibres 3 (5.88->6.35), wax 1 (23.1->23.75), dyed yarn 1 (9.5->9.88) | +50 |

**Best:** Vauxvais at about +77 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 25.6, stop 1 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 3.0 turns |
| beer |  | 46 @ min 3.54 | makes 28.0, uses 4.2, holds 347 (keeps 60): sells the surplus + 22/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 29 @ min 21.2 | makes 9.8, uses 2.1, holds 294 (keeps 30): sells the surplus + 21/turn of the excess |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 7 @ 2.2, stop - |  | uses 471.9/turn (brewery 1, flax farm 1, household), makes 450.0, holds 45 = 2.1 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 12 @ min 36.4 | makes 9.0, uses 0.0, holds 59 (keeps 15): sells the surplus + 3/turn of the excess |
| porterage | 7 @ 1.1, stop - |  | uses 6.8/turn (observed), makes 0.0, holds 9 = 1.3 turns |
| rope |  | 7 @ min 77.0 | makes 2.2, uses 0.0, holds 60 (keeps 0): sells the surplus + 5/turn of the excess |
| tools | 3 @ 6.2, stop 21 |  | uses 2.5/turn (retting pit 1), makes 0.0, holds 200 = 79.0 turns |

## Chain sizing

Mode HOLD, garments sold 8.3/turn (+0.0 exported); plan makes 3.3 garments a turn.
Labour: own 450, everything else 362, chain may buy 350 -> chain allowance 438, chain plan 124 (-44 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 2.22 | 2.30 |
| ret | 3 | 0.39 | 0.41 |
| spin | 4 | 0.87 | 0.89 |
| weave | 3 | 0.38 | 0.09 |
| sew | 2 | 0.24 | 0.08 |

Buffers: flax fibres 57/47, thread 422/139, cloth 32/12

## Self-diagnosis

- R2: ropewalk 1 blocked by rope space: 60 held of 60 capacity, we make 2.2 a turn; no buy on it: add a sell order or more capacity for rope
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
