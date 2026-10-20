# v2 shadow report

Turn 13414, 2026-10-20 07:13. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 7,784, prestige 3,412 (742 free, -1.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 145 | 0 | 4 | 0 | 0 | min_holding 60, sell 30, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 150 | 0 | 2 | 0 | 0 | min_holding 30, sell 14, sell @ 20.8 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 5 | 5 | 427 | 0 | 28 | buy 5, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 15 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34.8 |
| porterage | 37 | 37 | 8 | 0 | 29 | buy 37, buy @ 1.1 |

**0 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **labour**: 28 labour expired last turn (~45 coin): holding 5 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **limestone**: we make 1/turn more than we use but there is no sell order -> v2: sell 0

## Notes

- labour: projection runs 75 over real use lately; planning 434, not 509

## Prestige spending, cheapest coin per prestige first

987 turns left: prestige gained now converts 99.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.3 | 48.3 | running |
| hold feast 2 | townhouse | 2.6 | 51.6 | 54.4 | needs a townhouse (build cost 6,870); thin at home: wine |
| hold banquet 2 (meat) | mansion | 6.8 | 54.7 | 54.7 | thin at home: cheese |
| hold banquet 2 (fish) | mansion | 6.8 | 55.0 | 55.0 | thin at home: cured fish, cheese |
| hold prayer 2 | chapel | 13 | 52.4 | 55.1 | needs a chapel (build cost 32,666); thin at home: furniture |
| hold banquet 2 (pies) | mansion | 7 | 55.5 | 55.5 | thin at home: pasties, cheese, pies |
| hold banquet 3 (meat) | mansion | 7.6 | 56.7 | 56.7 | thin at home: cheese |
| hold banquet 3 (pies) | mansion | 8 | 56.7 | 56.7 | thin at home: pasties, cheese, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 57.0 | 57.0 | thin at home: cured fish, cheese |
| hold sermon 2 (candles) | church | 31 | 54.4 | 57.5 | needs a church (build cost 85,016); thin at home: candles, furniture |
| hold sermon 2 | church | 24 | 53.8 | 57.7 | needs a church (build cost 85,016); thin at home: furniture |
| hold banquet 1 (fish) | mansion | 4.2 | 58.4 | 58.4 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 120102307 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Rouhomme: furniture buy 3 @ 14.2, rope sell 2 @ 70.5; crew 0.1; est +41 a turn; stock: furniture 3 @ 14.2 (keep 145)
- **linen snake** on Grandgues: furniture buy 3 @ 13.5; crew 0.1; est +29 a turn; stock: furniture 3 @ 13.5 (keep 145)
- best towns now: Disscester +72, Pontmont +63, Dortgart +60, Kleinburgh +59, Hanstein +58
- Disscester would trade: furniture buy 3 @ 13.0, garments sell 10 @ 21.4, rope sell 1 @ 87.5; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~98 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Chatgnan | 728 | 0.19 | 0.10 (10/turn) | bellows 1 (325.5->461.7), rope 1 (63.05->66.97), fleece 2 (7.72->8.17), varnish 1 (17.64->18.71) | slaked lime 1 (6.46->14.44), candles 1 (76.12->79.5) | +145 |
| Fontaux | 411 | 0.11 | 0.40 (39/turn) | beer 30 (2.8->3.97), timber 14 (6.25->9.21), rope 2 (63.05->65.55), pasties 1 (13.3->16.53) | tackles 2 (176.4->189.05), candles 1 (74.55->79.5), fleece 1 (6.46->6.65) | +80 |
| Rotterburg | 1056 | 0.34 | 0.40 (39/turn) | beer 30 (2.8->4.69), wine 8 (5.35->7.27), rope 1 (63.05->74.1), thread 11 (4.06->4.8) | candles 1 (72.45->79.5), slaked lime 1 (6.35->14.44) | +72 |
| Rouhomme | 368 | 0.10 | 0.10 (10/turn) | glassware 2 (60.38->79.33), beer 30 (2.8->3.42), rope 2 (63.05->67.92), firewood 1 (1.58->5.65) | mouldboards 1 (39.69->46.93), candles 1 (77.7->79.5), flax fibres 4 (5.57->5.8), fleece 1 (6.35->6.65) | +70 |
| Amsdermund | 1111 | 0.37 | 0.30 (29/turn) | beer 30 (2.8->4.52), wine 8 (5.35->8.36), rope 1 (63.05->68.4), flax fibres 2 (4.64->5.42) | candles 1 (73.5->79.5), slaked lime 1 (8.4->14.44), acid 1 (137.55->138.7) | +68 |

**Best:** Chatgnan at about +145 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 29 @ min 3.38 | makes 28.0, uses 4.2, holds 145 (keeps 60): sells the surplus + 5/turn of the excess |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 12 = 7.7 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 0 @ 2.2, stop - |  | uses 434.2/turn (brewery 1, flax farm 1, household), makes 450.0, holds 5 |
| limestone |  | 1 @ min 16.8 |  |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 35.4 |  |
| pasties | 3 @ ?, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 4.9 turns |
| porterage | 9 @ 1.1, stop - |  | uses 8.9/turn (observed), makes 0.0, holds 37 = 4.1 turns |
| rope |  | 2 @ min 64.5 |  |
| timber |  | 14 @ min 6.7 | makes 9.0, uses 0.0, holds 418 (keeps 350): sells the surplus + 5/turn of the excess |
| tools | 3 @ 6.2, stop 24 |  | uses 2.9/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 68.3 turns |

## Chain sizing

Mode HOLD, garments sold 2.7/turn (+0.0 exported); plan makes 1.2 garments a turn.
Labour: own 450, everything else 369, chain may buy 350 -> chain allowance 431, chain plan 141 (+4 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 2.93 | 3.01 |
| ret | 3 | 0.52 | 0.54 |
| spin | 4 | 1.07 | 1.10 |
| weave | 3 | 0.07 | 0.05 |
| sew | 2 | 0.04 | 0.03 |

Buffers: flax fibres 54/45, thread 262/132, cloth 9/5

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
