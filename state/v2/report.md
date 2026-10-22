# v2 shadow report

Turn 13477, 2026-10-22 22:55. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 2,666, prestige 3,625 (505 free, -1.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 114 | 0 | 4 | 0 | 0 | min_holding 60, sell 53, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 60 | 0 | 2 | 0 | 0 | min_holding 30, sell 14, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 212 | 212 | 702 | 0 | 10 | buy 212, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 18 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 34.6 |
| porterage | 10 | 10 | 10 | 0 | 0 | buy 10, buy @ 1.1 |

**1 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.4 turns (holds 13, next step uses 32/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **linen snake**: linen snake cost 10 coin last turn (crew 0.10) and its route traded nothing (route limited by rope) -> v2: pause it (crew 0) until a route is proven to sell

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax fibres**: flax fibres buffer thin: 1.3 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 69
- **flax plants**: flax plants buffer thin: 1.0 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 180

## Notes

- labour: projection runs 75 over real use lately; planning 702, not 777

## Prestige spending, cheapest coin per prestige first

924 turns left: prestige gained now converts 99.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.6 | 48.6 | running |
| hold banquet 4 (pies) | mansion | 18 | 49.8 | 49.8 | thin at home: hop beer, wine |
| hold banquet 3 (pies) | mansion | 8 | 50.9 | 50.9 | thin at home: pasties, hop beer, pies |
| hold banquet 2 (pies) | mansion | 7 | 51.3 | 51.3 | thin at home: pasties, wine, pies |
| jousting 3 | arena | 230 | 52.1 | 52.2 | needs a arena (build cost 24,662); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 52.9 | 52.9 | thin at home: wine |
| hold banquet 4 | mansion | 17.5 | 53.0 | 53.0 | thin at home: wine, hop beer, ham |
| hold banquet 3 (fish) | mansion | 7.6 | 53.4 | 53.4 | thin at home: hop beer |
| hold sermon 2 (candles) | church | 31 | 51.4 | 53.8 | needs a church (build cost 62,859); thin at home: candles, furniture |
| hold banquet 2 (meat) | mansion | 6.8 | 54.1 | 54.1 | thin at home: wine |
| hold banquet 1 (fish) | mansion | 4.2 | 54.5 | 54.5 |  |
| hold banquet 3 (meat) | mansion | 7.6 | 54.5 | 54.5 | thin at home: hop beer |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 10 | 151802239 | 0.04 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only 4 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -1 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~99 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Heilegg | 826 | 0.23 | 0.20 (20/turn) | grindstones 1 (226.8->296.4), lead ore 6 (9.19->12.92), rope 2 (74->76), dyed yarn 1 (7.4->7.98) | premium ham 1 (249.9->317.3), candles 1 (70.35->73.5), canvas 8 (31.08->31.54), tools 3 (4.77->5) | +152 |
| Rotterburg | 1056 | 0.35 | 0.30 (30/turn) | sails 2 (645.75->698.25), lead bars 4 (12.71->14.91), lead ore 1 (9.19->18.34), grindstones 1 (226.8->239.4) | candles 1 (67.73->73.5), lathes 1 (185.85->191.9), resin 2 (1.04->1.78) | +120 |
| Hofkirchen | 991 | 0.31 | 0.20 (20/turn) | glass ingots 2 (56.18->68.4), jewellery 2 (92.4->99.75), lead bars 6 (12.71->14.91), lead ore 2 (9.19->11.69) | premium ham 1 (281.4->317.3), flax fibres 14 (4.73->5.7), candles 1 (71.4->73.5), blades 2 (11.97->12.63) | +96 |
| Kirchwerp | 1072 | 0.36 | 0.40 (40/turn) | lead bars 2 (12.71->18.34), wrought iron 9 (13.55->14.25), leather 1 (25.2->27.74), malt 3 (6.09->7.55) | premium ham 1 (262.5->317.3) | +69 |
| Chribruck | 1202 | 0.43 | 0.30 (30/turn) | grindstones 1 (226.8->279.3), lead ore 4 (9.19->18.62), iron ore 1 (4.6->7.6), lead bars 1 (12.71->14.63) | harnesses 1 (59.33->60.8) | +68 |

**Best:** Heilegg at about +152 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 24.4, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 52 @ min 3.38 |  |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 18 @ min 20.0 | makes 16.4, uses 2.1, holds 60 (keeps 30): sells the surplus + 4/turn of the excess |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 202 @ 2.2, stop - |  | uses 701.7/turn (brewery 1, flax farm 1, household), makes 500.0, holds 212 = 1.1 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 11 @ min 34.6 |  |
| pasties | 3 @ 13.0, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 13 = 4.8 turns |
| porterage | 10 @ 1.1, stop - |  | uses 10.4/turn (observed), makes 0.0, holds 10 = 1.0 turns |
| rope |  | 2 @ min 72.0 |  |
| timber |  | 8 @ min 6.5 |  |
| tools | 4 @ 6.2, stop 30 |  | uses 3.8/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 53.3 turns |

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 22.6 garments a turn.
Labour: own 500, everything else 415, chain may buy 350 -> chain allowance 435, chain plan 435 (+76 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.61 | 6.44 |
| ret | 3 | 1.00 | 1.14 |
| spin | 4 | 2.05 | 2.36 |
| weave | 3 | 0.67 | 0.89 |
| sew | 2 | 0.40 | 0.55 |

Buffers: flax fibres 45/80, thread 231/236, cloth 13/89
- chain plan needed 533 labour, budget left 435: cut to 435 (sewing capped at 0.55)

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
