# v2 shadow report

Turn 13421, 2026-10-20 14:04. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 8,036, prestige 3,402 (732 free, -3.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 57 | 0 | 4 | 0 | 0 | min_holding 60, sell 52, sell @ 3.4 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 24 | 3 | 3 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 71 | 0 | 2 | 0 | 0 | min_holding 30, sell 7, sell @ 20 |
| grain | 104 | 28 | 0 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 81 | 52 | 502 | 202 | 0 | buy 81, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 15 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 36 |
| porterage | 10 | 4 | 4 | 1 | 0 | buy 10, buy @ 1.1 |

**3 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.1 turns (holds 2, next step uses 44/turn) -> v2: check the step that makes it
- **labour**: buying 81, short of ~280 needed -> v2: buy 280
- **porterage**: flax farm 1 ran short of porterage (buy is live (10 @ 1.1), 4 bought last turn); labour need rises ~60/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.7 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 62
- **timber**: build materials for park 1, net maker152202386007001 are in (370.6 held, 190 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 0% (EXPANSION), about 12 turns left; still to deliver: labour 260, limestone 60, timber 40; ready for labour
- **net maker152202386007001** 0% (INITIAL), about 12 turns left; still to deliver: labour 200, timber 150, tools 20; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 60 | 105.7 | 0 | off: covered |
| timber | 190 | 370.6 | 0 | off: covered; switch v1's buy off |
| tools | 20 | 199.0 | 0 | off: covered |

Labour metered per turn while a site can progress: labour 39

## Notes

- labour: projection runs 75 over real use lately; planning 730, not 805

## Prestige spending, cheapest coin per prestige first

980 turns left: prestige gained now converts 99.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.7 | 51.1 | running |
| hold banquet 2 (pies) | mansion | 7 | 52.5 | 52.5 | thin at home: pasties, wine, pies, candles |
| hold prayer 2 | chapel | 13 | 51.8 | 54.3 | needs a chapel (build cost 30,357); thin at home: furniture |
| hold banquet 1 (fish) | mansion | 4.2 | 54.6 | 54.6 |  |
| hold banquet 3 (pies) | mansion | 8 | 55.0 | 55.0 | thin at home: pasties, pies, candles |
| hold banquet 2 (fish) | mansion | 6.8 | 55.4 | 55.4 | thin at home: wine, cured fish |
| hold sermon 2 (candles) | church | 31 | 53.2 | 55.7 | needs a church (build cost 68,824); thin at home: jewellery, candles, furniture |
| hold sermon 2 | church | 24 | 53.3 | 56.5 | needs a church (build cost 68,824); thin at home: jewellery, furniture |
| hold mass 2 (premium) | cathedral | 360 | 56.5 | 57.4 | needs a cathedral (build cost 277,320); thin at home: furniture, jewellery, glassware, candles, premium garments |
| jousting 1 | arena | 170 | 57.6 | 57.7 | needs a arena (build cost 24,599); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 57.8 | 57.8 | thin at home: wine, pies, candles |
| hold banquet 2 (meat) | mansion | 6.8 | 58.4 | 58.4 | thin at home: wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 120102307 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | - | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Rouhomme: furniture buy 6 @ 14.2, pasties buy 1 @ 14.9; crew 0.1; est +67 a turn; stock: furniture 6 @ 14.2 (keep 145); stock: pasties 1 @ 14.9 (keep 14)
- best towns now: Neuborn +136, Disscester +104, Dortgart +82, Großmühle +79, Friedwerp +78
- Neuborn would trade: furniture buy 6 @ 13.7, garments sell 23 @ 23.4; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~98 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Neuborn | 780 | 0.20 | 0.10 (10/turn) | garments 23 (20->25.08), flax fibres 4 (4.63->5.13), pasties 1 (16.2->16.91) | tallow 2 (18.59->20.14), hop beer 1 (8.14->9.12) | +113 |
| Hofkirchen | 991 | 0.31 | 0.10 (10/turn) | nails 4 (5.88->10.83), lead bars 9 (14.07->15.2), pies 1 (11.65->16.25) | acid 1 (130.2->140.6), medicine 2 (120.75->124.45), pasties 2 (15.02->19.2), candles 1 (71.4->77) | +60 |
| Etallaen | 774 | 0.20 | 0.10 (10/turn) | cured fish 4 (25.41->30.4), glassware 2 (63.53->69.35), dyed cloth 2 (13.76->15.86) | pasties 2 (13.76->19.2), cloth 18 (7.35->7.95), candles 1 (73.5->77), flax fibres 2 (4.73->5.95) | +56 |
| Friedwerp | 684 | 0.18 | 0.10 (10/turn) | tackles 1 (192.15->197.6), casks 3 (6.2->7.74), nets 4 (37->38), pies 1 (11.65->14.34) | pasties 2 (14.28->19.2), cheese 18 (5.72->6.13), mouldboards 1 (42->46.17), cloth 9 (7.67->7.95) | +34 |
| Amsdermund | 1111 | 0.38 | 0.10 (10/turn) | lead bars 9 (14.07->15.2), pies 1 (11.65->17.2), thread 10 (4.66->5.22) | bellows 1 (241.5->250.8), candles 1 (69.3->77), pasties 2 (15.54->19.2), acid 1 (138.6->140.6) | +34 |

**Best:** Neuborn at about +113 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 26.2, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 52 @ min 3.38 |  |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 24 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 26 @ min 20.0 | makes 22.6, uses 2.1, holds 71 (keeps 30): sells the surplus + 5/turn of the excess |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 280 @ 2.2, stop - |  | uses 729.7/turn (brewery 1, construction, household), makes 450.0, holds 81 = 0.3 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 36.0 |  |
| pasties | 3 @ 17.1, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 12 = 4.4 turns |
| porterage | 5 @ 1.1, stop - |  | uses 5.4/turn (observed), makes 0.0, holds 10 = 1.9 turns |
| rope |  | 3 @ min 74.5 |  |
| timber |  | 9 @ min 6.5 | makes 8.4, uses 0.0, holds 371 (keeps 350): sells the surplus + 1/turn of the excess |
| tools | 4 @ 6.2, stop 31 |  | uses 3.8/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 52.4 turns |

## Chain sizing

Mode HOLD, garments sold 5.0/turn (+0.0 exported); plan makes 23.0 garments a turn.
Labour: own 450, everything else 427, chain may buy 350 -> chain allowance 373, chain plan 374 (+0 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.04 | 5.00 |
| ret | 3 | 0.90 | 0.89 |
| spin | 4 | 1.84 | 1.83 |
| weave | 3 | 0.89 | 0.90 |
| sew | 2 | 0.55 | 0.56 |

Buffers: flax fibres 53/74, thread 419/217, cloth 2/90
- chain plan needed 461 labour, budget left 373: cut to 373 (sewing capped at 0.56)

## Self-diagnosis

- R1: prestige rate -3.43 a turn vs 12-turn median -0.97; likely: no slot, building or contract cause found: check the impacts
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 5 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
- R4: logging camp w/ tool, ropewalk 1 projected 0: short of labour (~36 needed); labour itself is not raised here
- R7 stale ask: rope ask 77 over the market for 3 turns: the town trades ~4 a turn at 76.5, we sold 0 with 11 over what we keep -> **sell price 77 -> 76.5 (last trade 76.5, floor 63.28)** (ok)
