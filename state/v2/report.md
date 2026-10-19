# v2 shadow report

Turn 13400, 2026-10-19 17:54. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 6,528, prestige 3,426 (756 free, -1.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 265 | 0 | 4 | 0 | 0 | min_holding 60, sell 39, sell @ 3.54 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 17 | 5 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 185 | 0 | 2 | 0 | 0 | min_holding 30, sell 14, sell @ 20.8 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 0 | 0 | 423 | 0 | 27 | buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34.6 |
| porterage | 7 | 7 | 7 | 30 | 0 | buy 7, buy @ 1.1 |

**2 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **porterage**: logging camp w/ tool, quarry 1 ran short of porterage (buy is live (7 @ 1.1), 7 bought last turn); labour need rises ~172/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **porterage**: buying 7, short of ~37 needed -> v2: buy 37

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 144 over real use lately; planning 439, not 583

## Prestige spending, cheapest coin per prestige first

1001 turns left: prestige gained now converts 99.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 46.2 | 46.2 | running |
| hold prayer 2 | chapel | 13 | 52.8 | 55.6 | needs a chapel (build cost 34,318); thin at home: furniture |
| jousting 1 | arena | 170 | 56.1 | 56.2 | needs a arena (build cost 25,494); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 57.5 | 57.5 | thin at home: cured fish |
| hold banquet 3 (pies) | mansion | 8 | 57.6 | 57.6 | thin at home: pasties |
| hold sermon 2 (candles) | church | 31 | 54.8 | 57.7 | needs a church (build cost 81,335); thin at home: jewellery, candles, furniture |
| hold sermon 2 | church | 24 | 54.1 | 57.8 | needs a church (build cost 81,335); thin at home: jewellery, furniture |
| hold banquet 3 (fish) | mansion | 7.6 | 58.1 | 58.1 | thin at home: cured fish |
| hold banquet 3 (meat) | mansion | 7.6 | 58.2 | 58.2 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 58.3 | 58.3 | thin at home: wine, cured fish |
| hold banquet 1 (meat) | mansion | 4.2 | 58.4 | 58.4 |  |
| hold banquet 2 (meat) | mansion | 6.8 | 58.5 | 58.5 | thin at home: wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 120102307 | 0.392 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 9 | 151802239 | 0.496 | - | furniture 23 | -324 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Rouhomme: furniture buy 24 @ 14.2, tools buy 2 @ 4.48; crew 0.1; est +285 a turn; stock: furniture 24 @ 14.2 (keep 145)
- **linen snake** on Grandgues: furniture buy 24 @ 14.2, tools buy 2 @ 4.66; crew 0.1; est +284 a turn; stock: furniture 24 @ 14.2 (keep 145)
- best towns now: Dortgart +303, Angefont +294, Coburgbaum +286, Rouhomme +285, Grandgues +284
- Dortgart would trade: furniture buy 24 @ 12.2; crew 0.4

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~94 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Briclives | 1041 | 0.32 | 0.40 (38/turn) | beer 40 (2.73->5.03), slaked lime 1 (5.99->13.87), flour 1 (16.8->23.18), tar 3 (9.55->11.4) | nails 6 (4.77->5.27), tools 2 (4.37->5.15) | +80 |
| Hofkirchen | 991 | 0.30 | 0.20 (19/turn) | wrought iron 8 (12.6->17.39) | candles 1 (71.4->80), medicine 1 (119.7->127.3), salt 7 (4.45->5.42), acid 1 (129.15->131.1) | +58 |
| Neuborn | 780 | 0.20 | 0.40 (38/turn) | seeds 9 (1.95->3.32), thread 3 (4.66->6.37), timber 8 (6.7->9.88), cloth 1 (6.44->7.93) | wax 2 (19.43->23.75), candles 1 (72.45->80), cheese 22 (5.04->5.51), salt 7 (4.68->5.42) | +47 |
| Friedwerp | 684 | 0.17 | 0.20 (19/turn) | beer 40 (2.73->3.55), flax fibres 4 (4.5->5.08), cloth 1 (6.44->6.93), dyed yarn 1 (9.71->9.97) | candles 1 (68.78->80), mouldboards 1 (38.22->45.79), salt 5 (4.64->5.42), flax fibres 11 (6.2->6.75) | +45 |
| Essenbrucke | 584 | 0.15 | 0.20 (19/turn) | beer 35 (2.73->3.72), light armour 1 (84.53->91.2), cloth 1 (6.44->7.31), slaked lime 1 (5.99->7.65) | grain 13 (2.5->3.3), salt 7 (4.68->5.42), pasties 1 (11.34->14.6) | +44 |

**Best:** Briclives at about +80 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 39 @ min 3.54 | makes 28.0, uses 4.2, holds 265 (keeps 60): sells the surplus + 15/turn of the excess |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 12 = 7.7 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 17 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 0 @ 2.2, stop - |  | uses 439.0/turn (brewery 1, flax farm 1, household), makes 450.0, holds 0 |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 34.6 |  |
| pasties | 3 @ 15.3, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 5.0 turns |
| porterage | 37 @ 1.1, stop - |  | uses 37.2/turn (observed), makes 0.0, holds 7 = 0.2 turns |
| rope |  | 4 @ min 75.0 | makes 2.2, uses 0.0, holds 27 (keeps 0): sells the surplus + 2/turn of the excess |
| tools | 3 @ 6.2, stop 22 |  | uses 2.6/turn (retting pit 1), makes 0.0, holds 200 = 75.7 turns |

## Chain sizing

Mode HOLD, garments sold 3.0/turn (+0.0 exported); plan makes 1.6 garments a turn.
Labour: own 450, everything else 512, chain may buy 350 -> chain allowance 350, chain plan 124 (-5 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 2.58 | 2.53 |
| ret | 3 | 0.48 | 0.45 |
| spin | 4 | 0.98 | 0.98 |
| weave | 3 | 0.09 | 0.04 |
| sew | 2 | 0.06 | 0.04 |

Buffers: flax fibres 57/45, thread 332/133, cloth 15/6

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R4: quarry 1 projected 0 of 1 (limited by porterage)
