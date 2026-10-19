# v2 shadow report

Turn 13403, 2026-10-19 20:57. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 7,222, prestige 3,423 (753 free, -1.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 293 | 0 | 4 | 0 | 0 | min_holding 60, sell 43, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 17 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 166 | 0 | 2 | 0 | 0 | min_holding 30, sell 14, sell @ 20.8 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 41 | 0 | 450 | 116 | 0 | buy 41, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34.6 |
| porterage | 37 | 37 | 17 | 0 | 20 | buy 37, buy @ 1.1 |

**1 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **labour**: buying 41, short of ~116 needed -> v2: buy 116

## Tuning

- **limestone**: we make 13/turn more than we use but there is no sell order -> v2: sell 13

## Notes

- labour: projection runs 150 over real use lately; planning 566, not 630

## Prestige spending, cheapest coin per prestige first

998 turns left: prestige gained now converts 99.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 46.5 | 46.5 | running |
| hold banquet 2 (meat) | mansion | 6.8 | 55.1 | 55.1 | thin at home: wine |
| hold banquet 2 (fish) | mansion | 6.8 | 55.4 | 55.4 | thin at home: wine, cured fish |
| hold prayer 2 | chapel | 13 | 53.2 | 55.7 | needs a chapel (build cost 30,456); thin at home: furniture |
| hold banquet 3 (meat) | mansion | 7.6 | 56.2 | 56.2 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 56.4 | 56.4 | thin at home: cured fish |
| hold banquet 2 (pies) | mansion | 7 | 56.6 | 56.6 | thin at home: pasties, wine |
| hold banquet 3 (pies) | mansion | 8 | 56.8 | 56.8 | thin at home: pasties |
| jousting 1 | arena | 170 | 56.9 | 57.0 | needs a arena (build cost 24,074); thin at home: protection, light armour, arms; needs weaponry skill |
| hold feast 2 | townhouse | 2.6 | 54.6 | 57.4 | needs a townhouse (build cost 7,042); thin at home: wine |
| hold banquet 1 (fish) | mansion | 4.2 | 57.5 | 57.5 | thin at home: cured fish |
| hold banquet 1 (meat) | mansion | 4.2 | 57.9 | 57.9 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 120102307 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Rouhomme: beer sell 43 @ 3.52, furniture buy 1 @ 14.2; crew 0.1; est +24 a turn; stock: furniture 1 @ 14.2 (keep 145)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: furniture 1 @ 13.9 (keep 145); best orders clear only 3 a turn after crew: ship stays at 0
- best towns now: Briclives +52, Disscester +25, Chatgnan +24, Rouhomme +24, Etallaen +23
- Briclives would trade: beer sell 43 @ 4.58, furniture buy 1 @ 12.6; crew 0.3

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~94 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Neuborn | 780 | 0.20 | 1.00 (94/turn) | lead ore 2 (8.66->23.18), timber 23 (6.2->9.88), seeds 13 (1.81->3.32), beer 43 (2.73->3.13) | candles 1 (77.7->81.5), honey 3 (7.25->8.17), pasties 2 (12.71->14.3), flax fibres 3 (5.62->6.25) | +72 |
| Briclives | 1041 | 0.32 | 0.40 (38/turn) | beer 43 (2.73->4.71), canvas 1 (30.66->34.01), flax fibres 1 (4.51->5.61) | slaked lime 2 (7.35->9.69), tools 5 (4.35->4.82), nails 2 (4.79->5.27) | +61 |
| Hofkirchen | 991 | 0.30 | 0.10 (9/turn) | wrought iron 5 (12.71->17.67), flax fibres 4 (4.51->6.17) | candles 1 (71.4->81.5), medicine 1 (118.65->128.25), acid 1 (129.15->133), slaked lime 2 (7.35->9.69) | +52 |
| Fontaux | 411 | 0.10 | 0.50 (47/turn) | beer 43 (2.73->3.78), timber 16 (6.2->8.55), limestone 1 (15.4->21.66), cloth 1 (7.3->7.84) | candles 1 (74.55->81.5), pasties 2 (13.76->14.3) | +50 |
| Rouhomme | 368 | 0.09 | 0.20 (19/turn) | beer 43 (2.73->3.4), cheese 14 (5.62->5.84), thread 5 (4.66->5.13), firewood 1 (1.65->5.18) | candles 1 (72.45->81.5), lead bars 7 (12.08->12.82), flax fibres 3 (5.57->6.25), garments 2 (20.16->20.8) | +42 |

**Best:** Neuborn at about +72 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 26.2, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 41 @ min 3.38 | makes 28.0, uses 4.2, holds 293 (keeps 60): sells the surplus + 17/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 17 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 116 @ 2.2, stop - |  | uses 565.5/turn (brewery 1, flax farm 1, household), makes 450.0, holds 41 = 0.4 turns |
| limestone |  | 13 @ min 17.4 |  |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 34.4 |  |
| pasties | 3 @ 15.0, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 4.9 turns |
| porterage | 25 @ 1.1, stop - |  | uses 25.1/turn (observed), makes 0.0, holds 37 = 1.5 turns |
| rope |  | 3 @ min 75.0 |  |
| timber |  | 21 @ min 6.7 | makes 19.8, uses 0.0, holds 383 (keeps 350): sells the surplus + 1/turn of the excess |
| tools | 6 @ 6.2, stop 48 |  | uses 6.0/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 33.5 turns |

## Chain sizing

Mode HOLD, garments sold 1.6/turn (+0.0 exported); plan makes 1.2 garments a turn.
Labour: own 450, everything else 501, chain may buy 350 -> chain allowance 350, chain plan 122 (-4 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 2.58 | 2.52 |
| ret | 3 | 0.48 | 0.45 |
| spin | 4 | 0.98 | 0.98 |
| weave | 3 | 0.07 | 0.03 |
| sew | 2 | 0.04 | 0.03 |

Buffers: flax fibres 57/45, thread 318/131, cloth 13/4

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R4: ropewalk 1 projected 0: short of labour (~14 needed); acted on sewing shop 1 at turn 13402 (one action per 2 turns); acted on weavery 1 at turn 13402 (one action per 2 turns); labour itself is not raised here
