# v2 shadow report

Turn 13420, 2026-10-20 13:13. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 8,516, prestige 3,406 (736 free, -0.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 55, sell @ 3.4 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 24 | 10 | 3 | 0 | 0 | stop 24, buy 10, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 58 | 0 | 2 | 0 | 0 | min_holding 30, sell 30, sell @ 20 |
| grain | 104 | 38 | 2 | 0 | 0 | stop 104, buy 38, buy @ 3.7 |
| labour | 52 | 0 | 450 | 85 | 0 | buy 52, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 15 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 36 |
| porterage | 4 | 4 | 4 | 2 | 0 | buy 4, buy @ 1.1 |

**4 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.7 turns (holds 2, next step uses 3/turn) -> v2: check the step that makes it
- **labour**: buying 52, short of ~120 needed -> v2: buy 120
- **porterage**: flax farm 1 ran short of porterage (buy is live (4 @ 1.1), 4 bought last turn); labour need rises ~67/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **porterage**: buying 4, short of ~10 needed -> v2: buy 10

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.5 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 69
- **timber**: build materials for park 1, net maker152202386007001 are in (387.6 held, 190 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 0% (EXPANSION), about 12 turns left; still to deliver: labour 260, limestone 60, timber 40; ready for labour
- **net maker152202386007001** 0% (INITIAL), about 12 turns left; still to deliver: labour 200, timber 150, tools 20; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 60 | 110.7 | 0 | off: covered |
| timber | 190 | 387.6 | 0 | off: covered; switch v1's buy off |
| tools | 20 | 199.8 | 0 | off: covered |

Labour metered per turn while a site can progress: labour 39

## Notes

- labour: projection runs 75 over real use lately; planning 570, not 645

## Prestige spending, cheapest coin per prestige first

981 turns left: prestige gained now converts 99.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.4 | 50.8 | running |
| hold banquet 2 (pies) | mansion | 7 | 53.5 | 53.5 | thin at home: pasties, wine, pies |
| hold banquet 2 (fish) | mansion | 6.8 | 53.8 | 53.8 | thin at home: wine, cured fish |
| hold prayer 2 | chapel | 13 | 51.7 | 54.2 | needs a chapel (build cost 30,294); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 51.9 | 54.3 | needs a church (build cost 67,212); thin at home: candles, furniture |
| hold banquet 1 (fish) | mansion | 4.2 | 54.7 | 54.7 |  |
| hold sermon 2 | church | 24 | 51.5 | 54.7 | needs a church (build cost 67,212); thin at home: furniture |
| hold feast 2 | townhouse | 2.6 | 52.9 | 55.5 | needs a townhouse (build cost 6,538); thin at home: wine |
| hold banquet 2 (meat) | mansion | 6.8 | 56.6 | 56.6 | thin at home: wine |
| hold mass 2 (premium) | cathedral | 360 | 56.1 | 57.0 | needs a cathedral (build cost 272,395); thin at home: furniture, jewellery, glassware, candles, premium garments |
| jousting 1 | arena | 170 | 57.3 | 57.5 | needs a arena (build cost 24,512); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 58.4 | 58.4 | thin at home: pasties, pies |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 120102307 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | - | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Rouhomme: furniture buy 4 @ 14.2, pasties buy 3 @ 14.9; crew 0.1; est +51 a turn; stock: furniture 4 @ 14.2 (keep 145); stock: pasties 3 @ 14.9 (keep 14)
- best towns now: Großmühle +64, Dortgart +62, Friedwerp +61, Donaunieder +59, Etallaen +59
- Großmühle would trade: furniture buy 4 @ 12.7, pasties buy 3 @ 12.5; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~98 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.31 | 0.10 (10/turn) | nails 4 (5.88->10.83), lead bars 9 (14.07->15.2), pies 1 (11.65->16.25) | acid 1 (130.2->140.6), medicine 2 (120.75->124.45), pasties 2 (15.02->19.2), candles 1 (71.4->77) | +60 |
| Etallaen | 774 | 0.20 | 0.10 (10/turn) | cured fish 4 (25.41->30.4), glassware 2 (63.53->69.35), dyed cloth 2 (13.76->15.86) | pasties 2 (13.76->19.2), candles 1 (73.5->77), flax fibres 2 (4.73->5.95), mouldboards 1 (44.1->46.17) | +46 |
| Amsdermund | 1111 | 0.38 | 0.10 (10/turn) | lead bars 9 (14.07->15.2), pies 1 (11.65->17.2), thread 10 (4.66->5.22) | bellows 1 (241.5->250.8), candles 1 (69.3->77), pasties 2 (15.54->19.2), acid 1 (138.6->140.6) | +34 |
| Friedwerp | 684 | 0.18 | 0.10 (10/turn) | tackles 1 (192.15->197.6), casks 3 (6.2->7.74), nets 4 (37->38), pies 1 (11.65->14.34) | pasties 2 (14.28->19.2), cheese 18 (5.72->6.13), mouldboards 1 (42->46.17), hop beer 1 (7.93->9.12) | +33 |
| Brunnham | 1281 | 0.47 | 0.10 (10/turn) | lead bars 9 (14.07->15.39), pies 1 (11.65->16.15), nets 4 (37->38.38) | candles 1 (69.3->77), mouldboards 1 (39.06->46.17), pasties 2 (15.86->19.2), cloth 2 (7.46->7.95) | +31 |

**Best:** Hofkirchen at about +60 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 52 @ min 3.4 |  |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 24 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 7 @ min 20.0 | makes 1.4, uses 2.1, holds 58 (keeps 30): sells the surplus + 7/turn of the excess |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 120 @ 2.2, stop - |  | uses 570.4/turn (brewery 1, construction, household), makes 450.0, holds 52 = 0.4 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 36.0 |  |
| pasties | 4 @ 20.0, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 11 = 3.9 turns |
| porterage | 10 @ 1.1, stop - |  | uses 10.3/turn (observed), makes 0.0, holds 4 = 0.4 turns |
| rope |  | 3 @ min 73.5 |  |
| timber |  | 11 @ min 6.5 | makes 8.4, uses 0.0, holds 388 (keeps 350): sells the surplus + 2/turn of the excess |
| tools | 4 @ 6.2, stop 32 |  | uses 4.0/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 50.2 turns |

## Chain sizing

Mode HOLD, garments sold 2.5/turn (+0.0 exported); plan makes 22.6 garments a turn.
Labour: own 450, everything else 427, chain may buy 350 -> chain allowance 373, chain plan 373 (+122 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.56 | 5.04 |
| ret | 3 | 0.99 | 0.90 |
| spin | 4 | 2.03 | 1.84 |
| weave | 3 | 0.03 | 0.89 |
| sew | 2 | 0.03 | 0.55 |

Buffers: flax fibres 52/73, thread 403/216, cloth 2/89
- chain plan needed 470 labour, budget left 373: cut to 373 (sewing capped at 0.55)

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 4 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
- R4: logging camp w/ tool projected 0 of 7 (limited by porterage)
