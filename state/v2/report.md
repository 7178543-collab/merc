# v2 shadow report

Turn 13391, 2026-10-19 08:10. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 4,651, prestige 3,384 (714 free, -0.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 246 | 0 | 4 | 0 | 0 | min_holding 60, sell 39, sell @ 3.54 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 185 | 0 | 2 | 0 | 0 | min_holding 30, sell 14, sell @ 20.8 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 0 | 0 | 412 | 0 | 38 | buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 27 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34.6 |
| porterage | 7 | 7 | 7 | 25 | 0 | buy 7, buy @ 1.1 |

**2 risks, 0 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **porterage**: logging camp w/ tool, quarry 1 ran short of porterage (buy is live (7 @ 1.1), 7 bought last turn); labour need rises ~158/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **porterage**: buying 7, short of ~34 needed -> v2: buy 34

## Notes

- labour: projection runs 94 over real use lately; planning 452, not 546
- labour expiry guard: 38 bought labour expired last turn, buy 0 (not 2) this turn

## Prestige spending, cheapest coin per prestige first

1010 turns left: prestige gained now converts 99.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 45.9 | 45.9 | running |
| hold banquet 2 (meat) | mansion | 6.8 | 55.3 | 55.3 | thin at home: wine |
| hold prayer 2 | chapel | 13 | 52.7 | 55.3 | needs a chapel (build cost 32,092); thin at home: furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 55.6 | 55.6 | thin at home: wine, cured fish |
| hold feast 2 | townhouse | 2.6 | 52.9 | 55.6 | needs a townhouse (build cost 6,946); thin at home: wine |
| hold banquet 3 (meat) | mansion | 7.6 | 56.9 | 56.9 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 57.2 | 57.2 | thin at home: cured fish |
| jousting 1 | arena | 170 | 57.3 | 57.5 | needs a arena (build cost 25,111); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 57.7 | 57.7 | thin at home: cured fish |
| hold sermon 2 | church | 24 | 54.3 | 58.0 | needs a church (build cost 81,524); thin at home: jewellery, furniture |
| hold banquet 1 (meat) | mansion | 4.2 | 58.1 | 58.1 |  |
| hold sermon 2 (candles) | church | 31 | 55.6 | 58.5 | needs a church (build cost 81,524); thin at home: jewellery, candles, furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 9 | 120102307 | 0.32 | beer 40 | furniture 2 | 8 |
| linen snake | 0.1 / 0.10 | 9 | 151802239 | 0.064 | - | furniture 4 | -56 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Rouhomme: nothing pays; crew 0.0; est +0 a turn; best orders clear only 8 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Karlmoor +17
- Karlmoor would trade: nets sell 8 @ 39.2; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~93 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Vauxvais | 204 | 0.05 | 0.30 (28/turn) | bread 151 (2.09->2.66), flax fibres 4 (4.52->4.99) | thread 19 (4.83->5.75), pasties 2 (14.6->18.8), candles 1 (77.7->84), flax fibres 13 (5.57->6.1) | +104 |
| Rouhomme | 368 | 0.09 | 0.60 (56/turn) | bread 151 (2.09->2.66), beer 39 (2.79->3.42), thread 6 (5.5->6.27), tar 2 (10.03->11.4) | candles 1 (72.98->84), pasties 2 (14.6->18.8), lead bars 9 (12.08->12.73), blades 2 (14.7->16.34) | +98 |
| Birkeningen | 1006 | 0.30 | 0.20 (19/turn) | cloth 1 (7.1->7.55) | rope 4 (57.75->73.15), candles 1 (71.4->84), thread 25 (5.25->5.75), pasties 1 (13.76->18.8) | +73 |
| Briclives | 1041 | 0.32 | 0.40 (37/turn) | tackles 1 (214.2->235.6), beer 39 (2.79->3.89), rope 1 (77->86.45), tar 1 (10.03->11.88) | pasties 2 (15.44->18.8), candles 1 (79.28->84), tools 2 (4.51->4.94), yarn 1 (3.8->4.31) | +51 |
| Nürnnieder | 520 | 0.13 | 0.10 (9/turn) | flax fibres 4 (4.52->5.13), cloth 1 (7.1->7.5) | thread 35 (4.58->5.75), candles 1 (74.03->84), wool 1 (6.83->7.55), beer 4 (3.15->3.5) | +47 |

**Best:** Vauxvais at about +104 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 26.2, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 37 @ min 3.54 | makes 28.0, uses 4.2, holds 246 (keeps 60): sells the surplus + 14/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.1 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 14 @ min 20.8 | makes 3.3, uses 2.1, holds 185 (keeps 30): sells the surplus + 13/turn of the excess |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 0 @ 2.2, stop - |  | uses 452.1/turn (brewery 1, flax farm 1, household), makes 450.0, holds 0 = 0.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 34.6 |  |
| pasties | 3 @ 19.7, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 13 = 4.7 turns |
| porterage | 34 @ 1.1, stop - |  | uses 34.0/turn (observed), makes 0.0, holds 7 = 0.2 turns |
| rope |  | 7 @ min 75.0 | makes 2.2, uses 0.0, holds 60 (keeps 0): sells the surplus + 5/turn of the excess |
| tools | 3 @ 6.2, stop 22 |  | uses 2.6/turn (retting pit 1), makes 0.0, holds 199 = 75.7 turns |

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 4.1 garments a turn.
Labour: own 450, everything else 498, chain may buy 350 -> chain allowance 350, chain plan 131 (+9 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 2.29 | 2.38 |
| ret | 3 | 0.41 | 0.42 |
| spin | 4 | 0.84 | 0.87 |
| weave | 3 | 0.12 | 0.15 |
| sew | 2 | 0.08 | 0.10 |

Buffers: flax fibres 57/49, thread 472/143, cloth 20/16

## Self-diagnosis

- R2: ropewalk 1 blocked by rope space: 60 held of 60 capacity, we make 2.2 a turn; no buy on it: add a sell order or more capacity for rope
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R4: quarry 1 projected 0 of 1 (limited by porterage)
