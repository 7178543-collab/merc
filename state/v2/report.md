# v2 shadow report

Turn 13406, 2026-10-19 23:53. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 8,281, prestige 3,420 (750 free, -1.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 209 | 0 | 4 | 0 | 0 | min_holding 60, sell 35, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 152 | 0 | 2 | 0 | 0 | min_holding 30, sell 14, sell @ 20.8 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 58 | 110 | 459 | 0 | 101 | buy 58, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 15 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34 |
| porterage | 37 | 37 | 16 | 0 | 21 | buy 37, buy @ 1.1 |

**0 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **labour**: 101 labour expired last turn (~160 coin): holding 58 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5

## Notes

- labour: projection runs 150 over real use lately; planning 459, not 534

## Prestige spending, cheapest coin per prestige first

995 turns left: prestige gained now converts 99.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.7 | 47.7 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 52.0 | 52.0 | thin at home: wine, cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 54.0 | 54.0 | thin at home: cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 54.5 | 54.5 | thin at home: cured fish |
| hold banquet 2 (meat) | mansion | 6.8 | 54.5 | 54.5 | thin at home: wine |
| hold feast 2 | townhouse | 2.6 | 52.6 | 55.5 | needs a townhouse (build cost 7,164); thin at home: wine |
| hold prayer 2 | chapel | 13 | 53.0 | 55.7 | needs a chapel (build cost 32,834); thin at home: furniture |
| hold banquet 3 (meat) | mansion | 7.6 | 56.3 | 56.3 |  |
| hold banquet 2 (pies) | mansion | 7 | 56.4 | 56.4 | thin at home: pasties, wine |
| jousting 1 | arena | 170 | 57.0 | 57.2 | needs a arena (build cost 27,055); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 57.4 | 57.4 | thin at home: pasties |
| hold sermon 2 | church | 24 | 53.8 | 57.7 | needs a church (build cost 85,570); thin at home: furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 120102307 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: furniture buy 3 @ 13.9; crew 0.1; est +28 a turn; stock: furniture 3 @ 13.9 (keep 145)
- **Flax Wyrm** on Rouhomme: furniture buy 3 @ 14.2; crew 0.1; est +27 a turn; stock: furniture 3 @ 14.2 (keep 145)
- best towns now: Briclives +46, Disscester +40, Dortdorf +37, Corstoft +34, Bordees +34
- Briclives would trade: beer sell 36 @ 4.66, furniture buy 3 @ 13.2; crew 0.3

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~96 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Rouhomme | 368 | 0.09 | 0.60 (57/turn) | bread 138 (2.18->2.81), beer 36 (2.74->3.42), firewood 1 (1.57->5.22), fleece 1 (5.46->6.93) | candles 1 (72.45->83), lead bars 5 (12.08->12.82), flax fibres 5 (5.57->6.2), tools 2 (4.62->4.74) | +77 |
| Grandgues | 152 | 0.04 | 0.30 (29/turn) | beer 36 (2.74->3.65), bread 138 (2.18->2.47), flax fibres 4 (4.53->5.46), wine 4 (5.51->6.08) | candles 1 (74.55->83), grain 13 (2.84->3.26), pasties 2 (13.97->14.5), hop beer 3 (8.4->8.55) | +67 |
| Vauxvais | 204 | 0.05 | 0.30 (29/turn) | bread 138 (2.18->2.62), beer 36 (2.74->3.15), cloth 1 (7.3->11.59), flax fibres 4 (4.53->5.42) | candles 1 (77.7->83), thread 9 (4.33->4.7), limestone 1 (12.6->14.91) | +65 |
| Dortgart | 1045 | 0.33 | 0.10 (10/turn) | nets 1 (35->37.24), fleece 1 (5.46->6.55) | bellows 1 (254.1->285), acid 1 (116.55->133.95), candles 1 (71.92->83) | +54 |
| Briclives | 1041 | 0.33 | 0.40 (38/turn) | beer 36 (2.74->4.67), jewellery 2 (88.73->91.67), flour 2 (18.48->21.66), cloth 1 (7.3->7.79) | candles 1 (80.85->83), tools 2 (4.37->4.74) | +47 |

**Best:** Rouhomme at about +77 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 34 @ min 3.38 | makes 28.0, uses 4.2, holds 209 (keeps 60): sells the surplus + 10/turn of the excess |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 12 = 7.7 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.1 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 9 @ 2.2, stop - |  | uses 459.2/turn (brewery 1, flax farm 1, household), makes 450.0, holds 58 = 6.3 turns |
| limestone |  | 5 @ min 17.0 |  |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 34.0 |  |
| pasties | 3 @ 15.2, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 13 = 4.7 turns |
| porterage | 16 @ 1.1, stop - |  | uses 15.9/turn (observed), makes 0.0, holds 37 = 2.3 turns |
| rope |  | 2 @ min 74.5 |  |
| timber |  | 10 @ min 6.7 | makes 8.4, uses 0.0, holds 380 (keeps 350): sells the surplus + 2/turn of the excess |
| tools | 3 @ 6.2, stop 22 |  | uses 2.7/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 73.8 turns |

## Chain sizing

Mode HOLD, garments sold 3.4/turn (+0.0 exported); plan makes 1.6 garments a turn.
Labour: own 450, everything else 406, chain may buy 350 -> chain allowance 394, chain plan 132 (+5 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 2.58 | 2.66 |
| ret | 3 | 0.48 | 0.47 |
| spin | 4 | 0.98 | 1.04 |
| weave | 3 | 0.07 | 0.05 |
| sew | 2 | 0.04 | 0.04 |

Buffers: flax fibres 58/45, thread 306/133, cloth 12/6

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
