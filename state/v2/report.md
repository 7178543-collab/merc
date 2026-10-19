# v2 shadow report

Turn 13398, 2026-10-19 15:04. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 6,426, prestige 3,428 (758 free, +49.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 217 | 0 | 4 | 0 | 0 | min_holding 60, sell 36, sell @ 3.54 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 17 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 186 | 0 | 2 | 0 | 0 | min_holding 30, sell 14, sell @ 20.8 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 3 | 10 | 440 | 0 | 20 | buy 3, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 19 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34.6 |
| porterage | 7 | 7 | 7 | 30 | 0 | buy 7, buy @ 1.1 |

**2 risks, 1 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **porterage**: logging camp w/ tool, quarry 1 ran short of porterage (buy is live (7 @ 1.1), 7 bought last turn); labour need rises ~172/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **porterage**: buying 7, short of ~37 needed -> v2: buy 37

## Waste (money lost now)

- **labour**: 20 labour expired last turn (~32 coin): holding 3 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Notes

- labour: projection runs 140 over real use lately; planning 472, not 612

## Prestige spending, cheapest coin per prestige first

1003 turns left: prestige gained now converts 99.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 46.5 | 46.5 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 54.1 | 54.1 |  |
| jousting 1 | arena | 170 | 55.6 | 55.7 | needs a arena (build cost 25,241); thin at home: protection, light armour, arms; needs weaponry skill |
| hold prayer 2 | chapel | 13 | 53.2 | 55.8 | needs a chapel (build cost 32,442); thin at home: furniture |
| hold banquet 3 (fish) | mansion | 7.6 | 55.9 | 55.9 | thin at home: cured fish |
| hold sermon 2 | church | 24 | 53.8 | 57.5 | needs a church (build cost 81,330); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 54.7 | 57.6 | needs a church (build cost 81,330); thin at home: candles, furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 57.7 | 57.7 | thin at home: wine, cured fish |
| hold banquet 3 (pies) | mansion | 8 | 57.9 | 57.9 | thin at home: pasties |
| hold banquet 1 (meat) | mansion | 4.2 | 58.5 | 58.5 |  |
| hold banquet 3 (meat) | mansion | 7.6 | 58.6 | 58.6 |  |
| hold banquet 2 (meat) | mansion | 6.8 | 60.7 | 60.7 | thin at home: wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.20 | 19 | 120102307 | 0.512 | beer 38 | furniture 24 | -316 |
| linen snake | 0.1 / 0.10 | 9 | 151802239 | 0.608 | - | furniture 38 | -535 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: furniture buy 36 @ 14.2; crew 0.1; est +430 a turn; stock: furniture 36 @ 14.2 (keep 145)
- **Flax Wyrm** on Rouhomme: beer sell 36 @ 3.54, furniture buy 32 @ 14.2; crew 0.2; est +390 a turn; stock: furniture 32 @ 14.2 (keep 145)
- best towns now: Angefont +466, Hofkirchen +453, Grandgues +430, Etallaen +428, Heilegg +412
- Angefont would trade: furniture buy 38 @ 13.4; crew 0.3

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~94 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Karlmoor | 787 | 0.20 | 0.10 (9/turn) | butter 2 (89.25->133.95), flax fibres 4 (4.49->5.56), fleece 1 (6.51->7.79), thread 10 (4.66->4.89) | candles 1 (71.4->81), salt 9 (4.75->5.56), honey 3 (8.24->8.69), pasties 1 (13.55->15) | +109 |
| Briclives | 1041 | 0.32 | 0.40 (38/turn) | beer 36 (2.74->5.18), tackles 1 (212.1->231.8), nets 2 (35.6->41.99), tar 3 (10.03->11.3) | wrought iron 5 (10.82->12.73), salt 6 (4.68->5.56), steel ingots 1 (15.54->16.05), tools 2 (4.39->4.74) | +102 |
| Bordees | 1112 | 0.36 | 0.10 (9/turn) | cookware 7 (22.47->28.69), thread 7 (4.66->5.94), flax fibres 1 (4.49->6.03), nets 1 (35.6->37.24) | plate armour 1 (1470->1520), candles 1 (76.65->81), garments 2 (20.37->20.8), salt 2 (5.04->5.56) | +100 |
| Heilegg | 826 | 0.21 | 0.10 (9/turn) | flax fibres 4 (4.49->5.18) | plate armour 1 (1470->1520), salt 12 (4.43->5.56), candles 1 (71.92->81), flax fibres 5 (5.83->6.75) | +73 |
| Hofkirchen | 991 | 0.30 | 0.20 (19/turn) | seeds 9 (1.9->4.27), grain 4 (2.4->3.08) | salt 19 (4.26->5.56), flax fibres 16 (5.41->6.75), candles 1 (69.3->81), medicine 1 (120.75->126.35) | +66 |

**Best:** Karlmoor at about +109 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 35 @ min 3.54 | makes 28.0, uses 4.2, holds 217 (keeps 60): sells the surplus + 11/turn of the excess |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 12 = 7.7 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 17 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 14 @ min 20.8 | makes 3.3, uses 2.1, holds 186 (keeps 30): sells the surplus + 13/turn of the excess |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 22 @ 2.2, stop - |  | uses 471.7/turn (brewery 1, flax farm 1, household), makes 450.0, holds 3 = 0.1 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 34.6 |  |
| pasties | 3 @ 15.4, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 4.9 turns |
| porterage | 37 @ 1.1, stop - |  | uses 37.2/turn (observed), makes 0.0, holds 7 = 0.2 turns |
| rope |  | 5 @ min 75.0 | makes 2.2, uses 0.0, holds 34 (keeps 0): sells the surplus + 3/turn of the excess |
| tools | 3 @ 6.2, stop 21 |  | uses 2.6/turn (retting pit 1), makes 0.0, holds 200 = 76.9 turns |

## Chain sizing

Mode HOLD, garments sold 6.6/turn (+0.0 exported); plan makes 2.5 garments a turn.
Labour: own 450, everything else 512, chain may buy 350 -> chain allowance 350, chain plan 133 (-7 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 2.70 | 2.58 |
| ret | 3 | 0.48 | 0.46 |
| spin | 4 | 0.98 | 0.99 |
| weave | 3 | 0.12 | 0.09 |
| sew | 2 | 0.08 | 0.06 |

Buffers: flax fibres 57/47, thread 361/137, cloth 15/10

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R4: quarry 1 projected 0 of 1 (limited by porterage)
