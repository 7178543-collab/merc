# v2 shadow report

Turn 13476, 2026-10-22 21:57. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 2,476, prestige 3,626 (506 free, -1.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 116 | 0 | 4 | 0 | 0 | min_holding 60, sell 53, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 55 | 0 | 2 | 0 | 0 | min_holding 30, sell 14, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 212 | 212 | 702 | 0 | 10 | buy 212, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 18 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 34.6 |
| porterage | 10 | 10 | 10 | 0 | 0 | buy 10, buy @ 1.1 |

**1 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.4 turns (holds 11, next step uses 32/turn) -> v2: check the step that makes it

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax fibres**: flax fibres buffer thin: 1.3 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 69
- **flax plants**: flax plants buffer thin: 1.1 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 180

## Notes

- labour: projection runs 75 over real use lately; planning 702, not 777

## Prestige spending, cheapest coin per prestige first

925 turns left: prestige gained now converts 99.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.9 | 48.9 | running |
| hold banquet 4 (pies) | mansion | 18 | 49.6 | 49.6 | thin at home: hop beer, wine |
| hold banquet 3 (pies) | mansion | 8 | 51.0 | 51.0 | thin at home: hop beer, pies |
| hold banquet 2 (pies) | mansion | 7 | 51.2 | 51.2 | thin at home: wine, pies |
| hold banquet 2 (fish) | mansion | 6.8 | 52.7 | 52.7 | thin at home: wine |
| jousting 3 | arena | 230 | 52.6 | 52.7 | needs a arena (build cost 25,750); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 52.8 | 52.8 | thin at home: wine, hop beer, ham |
| hold banquet 2 (meat) | mansion | 6.8 | 53.2 | 53.2 | thin at home: wine |
| hold banquet 3 (fish) | mansion | 7.6 | 53.4 | 53.4 | thin at home: hop beer |
| hold banquet 3 (meat) | mansion | 7.6 | 53.8 | 53.8 | thin at home: hop beer |
| hold sermon 2 (candles) | church | 31 | 51.3 | 53.8 | needs a church (build cost 65,064); thin at home: candles, furniture |
| hold prayer 2 | chapel | 13 | 51.4 | 54.3 | needs a chapel (build cost 32,716); thin at home: furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 10 | 151802239 | 0.04 | rope 1 | - | 18 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only 4 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -1 a turn after crew: ship stays at 0
- best towns now: Clairlond +25, Amsdermund +21, Cobholme +16
- Clairlond would trade: candles buy 1 @ 68.0, nets sell 2 @ 41.0, rope sell 2 @ 84.5; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~100 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Heilegg | 826 | 0.23 | 0.20 (20/turn) | grindstones 1 (281.4->347.7), lead ore 3 (8.77->14.34), rope 2 (71->77.9), lead bars 4 (13.02->14.91) | premium ham 1 (264.6->311.6), candles 1 (70.35->73.5), tools 3 (4.77->5.15) | +140 |
| Darmwald | 1022 | 0.33 | 0.10 (10/turn) | garments 16 (19.8->22.99), gold bars 1 (798->817), lead bars 1 (13.02->15.01), copper ingots 2 (15.54->16.25) | premium ham 1 (298.2->311.6), candles 1 (68.25->73.5), wrought iron 2 (8.4->11.11), steel ingots 1 (12.6->13.87) | +91 |
| Cobholme | 1564 | 0.62 | 0.30 (30/turn) | sails 1 (614.25->674.5), lead bars 3 (13.02->19), rope 2 (71->79.8), lead ore 2 (8.77->13.77) | candles 1 (70.88->73.5) | +90 |
| Großmühle | 751 | 0.20 | 0.10 (10/turn) | rope 2 (71->77.42), lead bars 2 (13.02->16.81), thread 4 (4.2->4.54), dyed yarn 1 (7.46->7.74) | looms 1 (535.5->608), candles 1 (70.88->73.5), salt 5 (4.12->4.48) | +88 |
| Clairas | 374 | 0.10 | 0.10 (10/turn) | sails 1 (614.25->674.5), gold bars 1 (798->817), lead bars 2 (13.02->14.54), thread 18 (4.2->4.35) | candles 1 (69.3->73.5), salt 5 (4.03->4.48), flax fibres 6 (5.67->5.9), tools 3 (5->5.15) | +83 |

**Best:** Heilegg at about +140 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 52 @ min 3.38 |  |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 12 = 7.7 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 17 @ min 20.0 | makes 16.4, uses 2.1, holds 55 (keeps 30): sells the surplus + 3/turn of the excess |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 202 @ 2.2, stop - |  | uses 701.7/turn (brewery 1, flax farm 1, household), makes 500.0, holds 212 = 1.1 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 11 @ min 34.6 |  |
| pasties | 3 @ 13.0, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 13 = 4.7 turns |
| porterage | 10 @ 1.1, stop - |  | uses 10.4/turn (observed), makes 0.0, holds 10 = 1.0 turns |
| rope |  | 2 @ min 69.0 |  |
| timber |  | 8 @ min 6.5 |  |
| tools | 4 @ 6.2, stop 30 |  | uses 3.8/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 53.2 turns |

## Chain sizing

Mode HOLD, garments sold 11.7/turn (+0.0 exported); plan makes 22.6 garments a turn.
Labour: own 500, everything else 415, chain may buy 350 -> chain allowance 435, chain plan 435 (+76 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.61 | 6.44 |
| ret | 3 | 1.00 | 1.14 |
| spin | 4 | 2.05 | 2.36 |
| weave | 3 | 0.67 | 0.89 |
| sew | 2 | 0.40 | 0.55 |

Buffers: flax fibres 45/80, thread 235/236, cloth 11/89
- chain plan needed 538 labour, budget left 435: cut to 435 (sewing capped at 0.55)

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
