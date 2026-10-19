# v2 shadow report

Turn 13398, 2026-10-19 15:57. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 6,520, prestige 3,428 (758 free, +49.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 217 | 0 | 4 | 0 | 0 | min_holding 60, sell 35, sell @ 3.54 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 17 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 186 | 0 | 2 | 0 | 0 | min_holding 30, sell 14, sell @ 20.8 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 3 | 10 | 440 | 0 | 20 | buy 15, buy @ 2.2 |
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

- labour: projection runs 144 over real use lately; planning 448, not 592

## Prestige spending, cheapest coin per prestige first

1003 turns left: prestige gained now converts 99.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 46.5 | 46.5 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 54.1 | 54.1 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 55.6 | 55.6 | thin at home: wine, cured fish |
| jousting 1 | arena | 170 | 55.6 | 55.7 | needs a arena (build cost 25,745); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 55.9 | 55.9 | thin at home: cured fish |
| hold prayer 2 | chapel | 13 | 53.2 | 55.9 | needs a chapel (build cost 33,702); thin at home: furniture |
| hold sermon 2 | church | 24 | 53.8 | 57.6 | needs a church (build cost 82,170); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 54.7 | 57.6 | needs a church (build cost 82,170); thin at home: candles, furniture |
| hold banquet 3 (pies) | mansion | 8 | 57.9 | 57.9 | thin at home: pasties |
| hold banquet 1 (meat) | mansion | 4.2 | 58.5 | 58.5 |  |
| hold banquet 2 (meat) | mansion | 6.8 | 58.6 | 58.6 | thin at home: wine |
| hold banquet 3 (meat) | mansion | 7.6 | 58.6 | 58.6 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.20 | 19 | 120102307 | 0.512 | beer 38 | furniture 24 | -316 |
| linen snake | 0.1 / 0.10 | 9 | 151802239 | 0.576 | - | furniture 38 | -535 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: furniture buy 23 @ 14.2, grain buy 13 @ 2.64; crew 0.1; est +277 a turn; stock: furniture 23 @ 14.2 (keep 145)
- **Flax Wyrm** on Rouhomme: nothing pays; crew 0.0; est +0 a turn
- best towns now: Angefont +466, Hofkirchen +450, Heilegg +421, Etallaen +413, Bordetes +409
- Angefont would trade: furniture buy 38 @ 13.4; crew 0.3

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~94 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Bordees | 1112 | 0.36 | 0.20 (19/turn) | cookware 10 (22.68->29.26), rope 2 (77->83.12), flax fibres 1 (4.49->5.79), nets 1 (35.6->37.24) | plate armour 1 (1470->1539), thread 20 (4.83->5.4), candles 1 (77.17->81), garments 2 (20.37->20.8) | +148 |
| Hofkirchen | 991 | 0.30 | 0.30 (28/turn) | grain 4 (2.42->3.02) | plate armour 1 (1470->1539), salt 18 (4.26->5.56), flax fibres 16 (5.41->6.75), candles 1 (71.4->81) | +116 |
| Disscester | 1474 | 0.54 | 0.30 (28/turn) | grindstones 1 (443.1->536.75), garments 14 (19.73->22.42), rope 1 (77->83.6) | cloth 6 (7.25->7.9), salt 3 (4.83->5.56) | +115 |
| Heilegg | 826 | 0.21 | 0.20 (19/turn) | beer 36 (2.74->3.48) | plate armour 1 (1470->1539), salt 12 (4.43->5.56), candles 1 (71.92->81), honey 5 (7.56->8.22) | +102 |
| Amsdermund | 1111 | 0.36 | 0.10 (9/turn) | tackles 1 (212.1->220.4), garments 14 (19.73->20.14) | plate armour 1 (1470->1539), candles 1 (69.3->81), salt 8 (4.28->5.56), pasties 2 (13.12->14.7) | +93 |

**Best:** Bordees at about +148 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 35 @ min 3.54 | makes 28.0, uses 4.2, holds 217 (keeps 60): sells the surplus + 11/turn of the excess |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 12 = 7.7 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 17 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 0 @ 2.2, stop - |  | uses 448.2/turn (brewery 1, flax farm 1, household), makes 450.0, holds 3 |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 34.6 |  |
| pasties | 3 @ 15.4, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 4.9 turns |
| porterage | 37 @ 1.1, stop - |  | uses 37.2/turn (observed), makes 0.0, holds 7 = 0.2 turns |
| rope |  | 5 @ min 75.0 | makes 2.2, uses 0.0, holds 34 (keeps 0): sells the surplus + 3/turn of the excess |
| tools | 3 @ 6.2, stop 22 |  | uses 2.6/turn (retting pit 1), makes 0.0, holds 200 = 75.8 turns |

## Chain sizing

Mode HOLD, garments sold 5.5/turn (+0.0 exported); plan makes 2.5 garments a turn.
Labour: own 450, everything else 512, chain may buy 350 -> chain allowance 350, chain plan 130 (-1 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 2.58 | 2.52 |
| ret | 3 | 0.48 | 0.45 |
| spin | 4 | 0.98 | 0.97 |
| weave | 3 | 0.09 | 0.08 |
| sew | 2 | 0.06 | 0.06 |

Buffers: flax fibres 57/46, thread 361/136, cloth 15/9

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R4: quarry 1 projected 0 of 1 (limited by porterage)
