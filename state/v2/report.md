# v2 shadow report

Turn 13471, 2026-10-22 16:59. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 3,138, prestige 3,634 (514 free, +72.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 122 | 0 | 4 | 0 | 0 | min_holding 60, sell 53, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 16 | 0 | 1 | 0 | 0 | min_holding 30, sell 14, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 459 | 459 | 909 | 0 | 0 | buy 459, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 18 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 34.6 |
| porterage | 10 | 10 | 10 | 0 | 0 | buy 10, buy @ 1.1 |

**1 risks, 1 waste, 4 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.1 turns (holds 5, next step uses 32/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **linen snake**: linen snake cost 10 coin last turn (crew 0.10) and its route traded nothing (route limited by rope) -> v2: pause it (crew 0) until a route is proven to sell

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax fibres**: flax fibres buffer thin: 1.3 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 69
- **flax plants**: flax plants buffer thin: 1.1 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 180
- **timber**: build materials for farmstead 1 are in (282.8 held, 1 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **farmstead 1** 97% (EXPANSION), about 1 turns left; still to deliver: labour 4, timber 1; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| timber | 1 | 282.8 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 4

## Notes

- labour: projection runs 84 over real use lately; planning 909, not 787

## Prestige spending, cheapest coin per prestige first

930 turns left: prestige gained now converts 99.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 4 (pies) | mansion | 18 | 48.9 | 48.9 | thin at home: pasties, hop beer, wine |
| maintain 1 | park | 0.5 | 48.9 | 48.9 | running |
| hold banquet 2 (pies) | mansion | 7 | 49.6 | 49.6 | thin at home: pasties, wine, pies |
| hold banquet 3 (pies) | mansion | 8 | 49.7 | 49.7 | thin at home: pasties, hop beer, pies |
| jousting 3 | arena | 230 | 52.2 | 52.3 | needs a arena (build cost 25,546); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 52.5 | 52.5 | thin at home: wine, hop beer, ham |
| hold banquet 2 (fish) | mansion | 6.8 | 52.9 | 52.9 | thin at home: wine, cured fish |
| hold sermon 2 (candles) | church | 31 | 51.1 | 53.6 | needs a church (build cost 65,563); thin at home: candles, furniture |
| hold banquet 3 (fish) | mansion | 7.6 | 53.8 | 53.8 | thin at home: hop beer, cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 54.4 | 54.4 | thin at home: cured fish |
| hold prayer 2 | chapel | 13 | 51.7 | 54.6 | needs a chapel (build cost 32,734); thin at home: furniture |
| jousting 1 | arena | 170 | 54.6 | 54.7 | needs a arena (build cost 25,546); thin at home: protection, light armour, arms; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 10 | 151802239 | 0.04 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: beer sell 28 @ 4.5, candles buy 1 @ 73.5, pasties buy 1 @ 13.3; crew 0.1; est +17 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only 10 a turn after crew: ship stays at 0
- best towns now: Etallaen +30, Chribruck +25, Cobholme +20, Clarfranche +18, Bremcop +18
- Etallaen would trade: candles buy 1 @ 62.0, pasties buy 2 @ 13.2, rope sell 2 @ 82.0, tools buy 3 @ 4.44; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~100 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.10 (10/turn) | charcoal 13 (1.94->2.6), chisels 1 (12.6->14.82), timber 7 (6.45->7.36), thread 3 (4.11->4.39) | premium ham 1 (206.85->326.8), candles 1 (70.88->78), pasties 2 (12.29->15.8), medicine 1 (133.35->137.75) | +153 |
| Amsdermund | 1111 | 0.38 | 0.10 (10/turn) | paper 2 (16.17->19.19), axes 2 (16.07->17.57), lead ore 2 (9.77->11.88) | premium ham 1 (206.85->326.8), candles 1 (69.3->78), acid 1 (137.55->144.4), pasties 2 (12.71->15.8) | +145 |
| Dortgart | 1045 | 0.34 | 0.30 (30/turn) | windows 1 (512.4->555.75), paper 3 (16.17->20.71), ploughs 2 (75.08->81.7), pies 2 (16.38->18.71) | medicine 2 (117.6->137.75), bellows 1 (254.1->273.6), candles 1 (72.45->78), pasties 2 (12.92->15.8) | +132 |
| Bordetes | 831 | 0.23 | 0.20 (20/turn) | glass ingots 1 (57.23->120.65), lead ore 10 (9.77->13.3), paper 4 (16.17->21.47), rope 2 (73.5->76) | candles 1 (70.88->78), medicine 2 (136.5->137.75), tools 3 (4.43->5.3), coats 1 (56.7->57) | +131 |
| Magdeach | 667 | 0.18 | 0.10 (10/turn) | paper 2 (16.17->19), thread 6 (4.11->4.64), lead ore 1 (9.77->11.21), dyed yarn 1 (7.56->8.22) | premium ham 1 (231->326.8), candles 1 (72.98->78), cheese 12 (5.35->5.98), medicine 1 (134.4->137.75) | +113 |

**Best:** Grandgues at about +153 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 33 @ min 3.38 | sell; ships offer 28 a turn abroad, so home sells 33 (was 53) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 15 @ min 20.0 |  |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 459 @ 2.2, stop - |  | uses 909.0/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 459 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 11 @ min 34.6 |  |
| pasties | 3 @ 16.5, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 13 = 4.7 turns |
| porterage | 10 @ 1.1, stop - |  | uses 10.4/turn (observed), makes 0.0, holds 10 = 1.0 turns |
| rope |  | 2 @ min 71.5 |  |
| timber |  | 8 @ min 6.5 |  |
| tools | 4 @ 6.2, stop 30 |  | uses 3.8/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 53.2 turns |

## Chain sizing

Mode HOLD, garments sold 13.8/turn (+1.6 exported); plan makes 18.0 garments a turn.
Labour: own 450, everything else 419, chain may buy 350 -> chain allowance 381, chain plan 381 (+23 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.61 | 5.93 |
| ret | 3 | 1.00 | 1.05 |
| spin | 4 | 2.05 | 2.17 |
| weave | 3 | 0.67 | 0.70 |
| sew | 2 | 0.40 | 0.44 |

Buffers: flax fibres 44/74, thread 258/217, cloth 5/70
- chain plan needed 575 labour, budget left 381: cut to 381 (sewing capped at 0.44)

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
