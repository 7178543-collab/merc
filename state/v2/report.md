# v2 shadow report

Turn 13307, 2026-10-15 20:56. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,307, prestige 3,111 (441 free, -1.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 347 | 0 | 4 | 0 | 0 | min_holding 60, sell 52, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 24 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 32 | 0 | 2 | 0 | 0 | min_holding 30, sell 2, sell @ 22 |
| grain | 103 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 173 | 210 | 514 | 0 | 146 | buy 75, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 52 | 0 | 0 | 0 | 0 | min_holding 15, sell 8, sell @ 39.6 |
| porterage | 26 | 26 | 15 | 0 | 11 | buy 26, buy @ 0.8 |

**0 risks, 1 waste, 4 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **labour**: 146 labour expired last turn (~244 coin): holding 173 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **candles**: home ask 78.50 is above our ceiling 70.00 and last turn bought 0 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **timber**: build materials for park 1 are in (693.0 held, 27 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 33% (EXPANSION), about 9 turns left; still to deliver: labour 175, limestone 41, timber 27; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 41 | 111.5 | 0 | off: covered |
| timber | 27 | 693.0 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 20

## Notes

- labour: projection runs 9 over real use lately; planning 559, not 568
- labour expiry guard: 146 bought labour expired last turn, buy 85 (not 109) this turn

## Prestige spending, cheapest coin per prestige first

1094 turns left: prestige gained now converts 99.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.1 | 53.6 | running |
| hold banquet 2 (pies) | mansion | 7 | 56.0 | 56.0 | thin at home: pies |
| hold banquet 2 (fish) | mansion | 6.8 | 56.6 | 56.6 |  |
| hold banquet 1 (fish) | mansion | 4.2 | 57.2 | 57.2 |  |
| hold banquet 4 (pies) | mansion | 18 | 57.7 | 57.7 |  |
| hold banquet 3 (pies) | mansion | 8 | 58.2 | 58.2 | thin at home: pies |
| jousting 1 | arena | 170 | 58.0 | 58.2 | needs a arena (build cost 26,538); thin at home: protection, light armour, arms; needs weaponry skill |
| hold sermon 2 (candles) | church | 31 | 57.0 | 59.3 | needs a church (build cost 72,462); thin at home: jewellery, candles, furniture |
| hold feast 2 | townhouse | 2.6 | 57.1 | 59.6 | needs a townhouse (build cost 6,936) |
| hold prayer 2 | chapel | 13 | 57.3 | 59.8 | needs a chapel (build cost 34,184); thin at home: furniture |
| hold banquet 3 (fish) | mansion | 7.6 | 60.1 | 60.1 |  |
| jousting 3 | arena | 230 | 60.2 | 60.3 | needs a arena (build cost 26,538); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 10 | 74001604 | 0 | varnish 1 | mouldboards 1 | -32 |
| linen snake | 0.0 / 0.00 | 0 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Brunnham: nothing pays; crew 0.0; est +0 a turn; best orders clear only 4 a turn after crew: ship stays at 0
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn; best orders clear only -2 a turn after crew: ship stays at 0
- best towns now: Fulkirch +55, Hofkirchen +45, Bedenis +39, Kirchwerp +36, Herschweig +36
- Fulkirch would trade: acid buy 2 @ 161, bronze ingots buy 1 @ 21.0, mouldboards sell 1 @ 36.6, wax sell 3 @ 23.8; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~104 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Caillechâtel | 488 | 0.14 | 0.10 (10/turn) | nets 9 (16.74->40.85), light armour 1 (77.7->79.33), flax fibres 5 (5.35->5.65) | cloth 1 (6.62->8.1), yarn 3 (4.85->5.22) | +212 |
| Heilegg | 826 | 0.23 | 0.10 (10/turn) | nets 9 (16.74->39.9), wax 3 (21.63->22.61) | scythes 1 (28.14->30.21), hop beer 1 (7.67->9.5) | +204 |
| Heidlowe | 662 | 0.18 | 0.10 (10/turn) | nets 9 (16.74->37.81), mouldboards 1 (33.39->40.47) | ploughs 1 (66.67->77.9), flour 2 (20.27->22.04), yarn 3 (4.6->5.22) | +202 |
| Rouhomme | 368 | 0.10 | 0.70 (73/turn) | bread 147 (2.29->3.53), lead ore 8 (7.19->10.92), beer 75 (3.28->3.8), grain 8 (2.48->3.13) | scythes 1 (28.14->30.21), wool 1 (5.72->7.69), dyed yarn 1 (6.77->8.03), flax plants 1 (1.42->1.69) | +198 |
| Marmont | 638 | 0.18 | 0.10 (10/turn) | nets 8 (16.74->40.28), yarn 3 (5.83->7.55), light armour 1 (77.7->80.75), butter 1 (68.78->70.77) | soap 1 (102.38->109.25) | +196 |

**Best:** Caillechâtel at about +212 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 26.0, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 5.0 turns |
| beer |  | 71 @ min 3.7 | makes 56.0, uses 4.2, holds 347 (keeps 60): sells the surplus + 20/turn of the excess |
| candles | 3 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 4 = 2.3 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 24 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 103 = 4.0 turns |
| labour | 85 @ 2.2, stop - |  | uses 559.0/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 173 = 1.6 turns |
| limestone |  | 5 @ min 19.4 |  |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 37.8 | makes 6.0, uses 0.0, holds 52 (keeps 15): sells the surplus + 3/turn of the excess |
| porterage | 22 @ 1.1, stop - |  | uses 22.1/turn (observed), makes 0.0, holds 26 = 1.2 turns |
| rope |  | 6 @ min 77.0 | makes 4.5, uses 0.0, holds 20 (keeps 0): sells the surplus + 1/turn of the excess |
| tar | 3 @ 11.0, stop 5 |  | uses 1.1/turn (ropewalk 1), makes 0.0, holds 0 = 0.0 turns |
| timber |  | 51 @ min 8.5 | makes 24.0, uses 0.0, holds 693 (keeps 350): sells the surplus + 27/turn of the excess |
| tools | 7 @ 6.2, stop 51 |  | uses 6.3/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 31.6 turns |

## Chain sizing

Mode FULL, garments sold 2.7/turn (+0.0 exported); plan makes 0.4 garments a turn.
Labour: own 450, everything else 466, chain may buy 350 -> chain allowance 350, chain plan 170 (+6 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 3.69 | 3.84 |
| ret | 3 | 0.66 | 0.68 |
| spin | 4 | 1.35 | 1.40 |
| weave | 3 | 0.00 | 0.00 |
| sew | 2 | 0.02 | 0.01 |

Buffers: flax fibres 63/54, thread 277/171, cloth 18/13
- thread beyond the household duty (55 a turn) is fed from weaving

## Self-diagnosis

- R1: prestige rate -0.96 a turn vs 12-turn median +3.24; likely: no slot, building or contract cause found: check the impacts
- R2: logging camp w/ tool blocked by timber space: 693 held of 711 capacity, we make 24.0 a turn; no buy on it: add a sell order or more capacity for timber
- R3: weavery 1 (weavery) finished but idle 6 turns (weave cloth 2 at 0); no planned recipe for a weavery: Taylor's call
- R3: mansion 1 (mansion) finished but idle 3 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R4: ropewalk 1 projected 0 of 1 (limited by tar)
