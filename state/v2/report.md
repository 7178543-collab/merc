# v2 shadow report

Turn 13379, 2026-10-18 20:50. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 5,494, prestige 3,293 (623 free, -1.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 305 | 0 | 4 | 0 | 0 | min_holding 60, sell 44, sell @ 3.54 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 285 | 0 | 2 | 0 | 0 | min_holding 30, sell 22, sell @ 21.2 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 3 | 0 | 423 | 0 | 27 | buy 3, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 51 | 0 | 0 | 0 | 0 | min_holding 15, sell 12, sell @ 36.2 |
| porterage | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 1.1 |

**0 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **labour**: 27 labour expired last turn (~43 coin): holding 3 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 73 over real use lately; planning 423, not 494

## Prestige spending, cheapest coin per prestige first

1022 turns left: prestige gained now converts 99.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 46.5 | 46.5 | running |
| jousting 1 | arena | 170 | 53.0 | 53.1 | needs a arena (build cost 25,128); thin at home: protection, light armour, arms; needs weaponry skill |
| hold sermon 2 (candles) | church | 31 | 53.0 | 55.8 | needs a church (build cost 80,466); thin at home: candles, furniture |
| hold prayer 2 | chapel | 13 | 53.7 | 56.3 | needs a chapel (build cost 32,202); thin at home: furniture |
| hold banquet 3 (pies) | mansion | 8 | 57.4 | 57.4 | thin at home: pasties, pies, candles |
| hold sermon 2 | church | 24 | 54.4 | 58.0 | needs a church (build cost 80,466); thin at home: furniture |
| hold banquet 1 (fish) | mansion | 4.2 | 58.2 | 58.2 | thin at home: cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 58.3 | 58.3 | thin at home: cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 58.5 | 58.5 | thin at home: wine, cured fish |
| hold banquet 2 (pies) | mansion | 7 | 59.0 | 59.0 | thin at home: pasties, wine, pies, candles |
| hold banquet 3 (meat) | mansion | 7.6 | 60.2 | 60.2 |  |
| hold banquet 2 (meat) | mansion | 6.8 | 60.6 | 60.6 | thin at home: wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 10 | 120102307 | 0.096 | - | pasties 6 | -92 |
| linen snake | 0.1 / 0.10 | 10 | 151802239 | 0.376 | - | furniture 22, pasties 2 | -333 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: furniture buy 23 @ 14.0; crew 0.1; est +276 a turn; stock: furniture 23 @ 14.0 (keep 140)
- **Flax Wyrm** on Rouhomme: nothing pays; crew 0.0; est +0 a turn; best orders clear only -9 a turn after crew: ship stays at 0
- best towns now: Hofkirchen +392, Cobholme +350, Angefont +345, Heilegg +338, Amsdermund +334
- Hofkirchen would trade: furniture buy 33 @ 13.1; crew 0.5

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~95 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Heilegg | 826 | 0.21 | 0.30 (28/turn) | nets 10 (17.19->37.43), rope 7 (67.5->76.47), beer 44 (2.95->3.72), glassware 2 (55.12->57.95) | yarn 13 (6.04->8.07), light armour 1 (76.65->86.92), casks 4 (5.35->6.65), garments 2 (20.58->21.2) | +316 |
| Heidlowe | 662 | 0.17 | 0.30 (28/turn) | nets 10 (17.19->34.39), rope 3 (67.5->76), beer 44 (2.95->3.5), tools 14 (4.24->4.99) | yarn 6 (4.68->8.07), cured meat 8 (22.89->23.56), dyed yarn 1 (8.09->9.88), cloth 5 (7.51->7.75) | +236 |
| Essenbrucke | 584 | 0.15 | 0.20 (19/turn) | nets 2 (17.19->44.84), beer 44 (2.95->3.84), rope 1 (67.5->69.83), cloth 2 (6.7->7.55) | yarn 23 (4.39->8.07), casks 4 (5.25->6.65), flax fibres 1 (5.93->6.35), nails 2 (6.2->6.37) | +170 |
| Angefont | 686 | 0.17 | 0.30 (28/turn) | nets 6 (17.19->38.76), flax fibres 4 (5.1->7.27), beer 44 (2.95->3.38), tallow 1 (20.37->21.85) | thread 41 (4.41->4.78), yarn 3 (5.67->8.07), casks 3 (6.3->6.65), garments 2 (20.79->21.2) | +154 |
| Clarfranche | 1484 | 0.55 | 0.30 (28/turn) | nets 4 (17.19->37.81), rope 5 (67.5->75.05), tools 16 (4.24->5.18), glassware 2 (55.12->56.05) | yarn 5 (4.16->8.07), light armour 1 (76.65->86.92), blades 2 (13.97->15.58), pies 2 (14.6->17.29) | +147 |

**Best:** Heilegg at about +316 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 42 @ min 3.54 | makes 28.0, uses 4.2, holds 305 (keeps 60): sells the surplus + 18/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 22 @ min 21.2 | makes 3.3, uses 2.1, holds 285 (keeps 30): sells the surplus + 21/turn of the excess |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 0 @ 2.2, stop - |  | uses 422.5/turn (brewery 1, flax farm 1, household), makes 450.0, holds 3 |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 11 @ min 34.0 | makes 9.0, uses 0.0, holds 51 (keeps 15): sells the surplus + 2/turn of the excess |
| porterage | 7 @ 1.1, stop - |  | uses 7.0/turn (observed), makes 0.0, holds 7 = 1.0 turns |
| rope |  | 7 @ min 67.5 | makes 2.2, uses 0.0, holds 58 (keeps 0): sells the surplus + 5/turn of the excess |
| timber |  | 8 @ min 6.7 |  |
| tools | 3 @ 6.2, stop 21 |  | uses 2.6/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 76.5 turns |

## Chain sizing

Mode HOLD, garments sold 9.6/turn (+0.0 exported); plan makes 3.7 garments a turn.
Labour: own 450, everything else 362, chain may buy 350 -> chain allowance 438, chain plan 136 (+8 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 2.43 | 2.56 |
| ret | 3 | 0.43 | 0.46 |
| spin | 4 | 0.89 | 0.94 |
| weave | 3 | 0.09 | 0.12 |
| sew | 2 | 0.08 | 0.09 |

Buffers: flax fibres 56/48, thread 412/141, cloth 27/14

## Self-diagnosis

- R2: ropewalk 1 blocked by rope space: 58 held of 60 capacity, we make 2.2 a turn; no buy on it: add a sell order or more capacity for rope
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
