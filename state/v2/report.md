# v2 shadow report

Turn 13456, 2026-10-22 01:08. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 5,921, prestige 3,579 (909 free, -1.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 151 | 0 | 4 | 0 | 0 | min_holding 60, sell 56, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 39 | 0 | 2 | 0 | 0 | min_holding 30, sell 19, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 274 | 274 | 724 | 2 | 0 | buy 274, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 37 |
| porterage | 10 | 10 | 10 | 0 | 0 | buy 10, buy @ 1.1 |

**1 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.0 turns (holds 1, next step uses 42/turn) -> v2: check the step that makes it

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.3 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 69
- **flax plants**: flax plants buffer thin: 1.0 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 176

## Notes

- labour: projection runs 87 over real use lately; planning 726, not 801

## Prestige spending, cheapest coin per prestige first

945 turns left: prestige gained now converts 99.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.7 | 47.7 | running |
| hold banquet 3 (pies) | mansion | 8 | 49.9 | 49.9 | thin at home: pasties, pies |
| hold banquet 4 (pies) | mansion | 18 | 50.0 | 50.0 | thin at home: wine |
| hold banquet 2 (pies) | mansion | 7 | 51.3 | 51.3 | thin at home: pasties, wine, pies |
| hold sermon 2 (candles) | church | 31 | 51.3 | 53.8 | needs a church (build cost 64,790); thin at home: candles, furniture |
| hold banquet 4 | mansion | 17.5 | 54.0 | 54.0 | thin at home: wine, ham |
| hold sermon 2 | church | 24 | 51.7 | 54.9 | needs a church (build cost 64,790); thin at home: furniture |
| hold prayer 2 | chapel | 13 | 52.3 | 55.1 | needs a chapel (build cost 33,000); thin at home: furniture |
| jousting 3 | arena | 230 | 55.7 | 55.8 | needs a arena (build cost 26,044); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| jousting 1 | arena | 170 | 55.8 | 55.9 | needs a arena (build cost 26,044); thin at home: protection, light armour, arms; needs weaponry skill |
| hold mass 1 | cathedral | 180 | 54.7 | 56.3 | needs a cathedral (build cost 240,290); thin at home: jewellery, glassware, candles |
| hold banquet 1 (fish) | mansion | 4.2 | 56.7 | 56.7 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 120102307 | 0 | - | - | 0 |
| linen snake | 0.2 / 0.20 | 19 | 185801747 | 0.336 | - | furniture 21 | -296 |

## Ship plans (this turn's world prices)

- **linen snake** on Neuborn: furniture buy 23 @ 13.9, garments sell 9 @ 21.8; crew 0.2; est +281 a turn; stock: furniture 23 @ 13.9 (keep 145)
- **Flax Wyrm** on Rouhomme: nothing pays; crew 0.0; est +0 a turn; best orders clear only -8 a turn after crew: ship stays at 0
- best towns now: Cobholme +481, Grandgues +422, Hofkirchen +412, Bordetes +394, Heilegg +376
- Cobholme would trade: beer sell 57 @ 5.7, furniture buy 35 @ 13.2; crew 0.9

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~99 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Kirchwerp | 1072 | 0.36 | 0.30 (30/turn) | plate armour 1 (1044.75->1301.5), lathes 1 (114.45->141.55), casks 10 (5.67->8.31), scythes 2 (20.79->23.37) | candles 1 (74.03->77) | +315 |
| Friedwerp | 684 | 0.18 | 0.30 (30/turn) | lathes 1 (114.45->157.7), beer 47 (3.2->3.86), tools 16 (4.78->5.65), casks 6 (5.67->7.74) | cheese 22 (6.2->7.08), lead ore 11 (9.61->11.78), hinges 1 (30.66->36.86), candles 1 (71.92->77) | +144 |
| Neuborn | 780 | 0.21 | 0.20 (20/turn) | garments 20 (18.98->23.56), tackles 1 (169.05->193.8), seeds 9 (1.78->3.32), wine 6 (6.09->6.98) | hinges 1 (30.24->36.86), chisels 2 (11.55->14.44), candles 1 (74.03->77), hop beer 5 (7.04->7.84) | +138 |
| Marmont | 638 | 0.17 | 0.30 (30/turn) | beer 59 (3.2->5.18), nets 8 (37.8->39.52), scythes 3 (20.79->23.37), fleece 1 (4.3->4.52) | candles 1 (72.45->77), rope 1 (76.65->77.42), tiles 2 (3->4.73), tools 3 (4.68->5) | +118 |
| Cobholme | 1564 | 0.62 | 0.80 (79/turn) | beer 57 (3.2->6.13), scythes 1 (20.79->32.87), fleece 1 (4.3->5.75), leather 1 (23.94->25.65) | lead ore 2 (6.51->11.78), copper ore 1 (14.6->20.33), canvas 2 (25.41->27.55) | +117 |

**Best:** Kirchwerp at about +315 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 55 @ min 3.38 | makes 56.0, uses 4.2, holds 151 (keeps 60): sells the surplus + 3/turn of the excess |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 12 = 7.7 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 10 @ min 20.0 | sell; ships offer 9 a turn abroad, so home sells 10 (was 20) |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 276 @ 2.2, stop - |  | uses 726.2/turn (brewery 1, flax farm 1, household), makes 450.0, holds 274 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 36.8 |  |
| pasties | 3 @ 14.9, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 13 = 4.7 turns |
| porterage | 10 @ 1.1, stop - |  | uses 10.3/turn (observed), makes 0.0, holds 10 = 1.0 turns |
| rope |  | 2 @ min 79.5 |  |
| timber |  | 8 @ min 6.5 |  |
| tools | 4 @ 6.2, stop 30 |  | uses 3.7/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 53.8 turns |

## Chain sizing

Mode HOLD, garments sold 20.0/turn (+0.0 exported); plan makes 22.6 garments a turn.
Labour: own 450, everything else 403, chain may buy 350 -> chain allowance 397, chain plan 398 (+7 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.54 | 5.63 |
| ret | 3 | 0.98 | 1.00 |
| spin | 4 | 2.03 | 2.06 |
| weave | 3 | 0.86 | 0.87 |
| sew | 2 | 0.53 | 0.55 |

Buffers: flax fibres 46/73, thread 266/214, cloth 1/87
- chain plan needed 533 labour, budget left 397: cut to 397 (sewing capped at 0.55)

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
