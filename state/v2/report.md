# v2 shadow report

Turn 13411, 2026-10-20 04:57. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 8,017, prestige 3,415 (745 free, -1.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 164 | 0 | 4 | 0 | 0 | min_holding 60, sell 31, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 151 | 0 | 2 | 0 | 0 | min_holding 30, sell 14, sell @ 20.8 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 21 | 16 | 422 | 0 | 44 | buy 21, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 15 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34.8 |
| porterage | 37 | 37 | 7 | 0 | 30 | buy 37, buy @ 1.1 |

**0 risks, 1 waste, 0 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **labour**: 44 labour expired last turn (~71 coin): holding 21 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Notes

- labour expiry guard: 44 bought labour expired last turn, buy 0 (not 47) this turn

## Prestige spending, cheapest coin per prestige first

990 turns left: prestige gained now converts 99.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.3 | 48.3 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 52.3 | 52.3 | thin at home: wine |
| hold banquet 3 (fish) | mansion | 7.6 | 54.0 | 54.0 |  |
| hold banquet 2 (meat) | mansion | 6.8 | 54.9 | 54.9 | thin at home: wine |
| hold banquet 1 (fish) | mansion | 4.2 | 55.0 | 55.0 |  |
| hold prayer 2 | chapel | 13 | 52.4 | 55.1 | needs a chapel (build cost 32,728); thin at home: furniture |
| hold banquet 2 (pies) | mansion | 7 | 55.7 | 55.7 | thin at home: wine |
| hold banquet 3 (meat) | mansion | 7.6 | 56.3 | 56.3 |  |
| hold feast 2 | townhouse | 2.6 | 53.5 | 56.3 | needs a townhouse (build cost 6,950); thin at home: wine |
| hold banquet 3 (pies) | mansion | 8 | 56.4 | 56.4 |  |
| hold sermon 2 (candles) | church | 31 | 53.8 | 56.7 | needs a church (build cost 80,603); thin at home: candles, furniture |
| hold sermon 2 | church | 24 | 53.3 | 57.1 | needs a church (build cost 80,603); thin at home: furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 120102307 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: furniture buy 3 @ 13.7; crew 0.1; est +28 a turn; stock: furniture 3 @ 13.7 (keep 145)
- **Flax Wyrm** on Rouhomme: furniture buy 3 @ 14.2; crew 0.1; est +27 a turn; stock: furniture 3 @ 14.2 (keep 145)
- best towns now: Amsdermund +40, Caillechâtel +36, Calange +36, Hofkirchen +34, Dortgart +34
- Amsdermund would trade: furniture buy 3 @ 14.0, garments sell 10 @ 21.0; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~97 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Cobholme | 1564 | 0.61 | 0.30 (29/turn) | cured fish 7 (23.31->34.39), tools 16 (4.32->5.42), cheese 6 (5.51->7.17), rope 1 (81->86.92) | candles 1 (74.55->77.5), wrought iron 1 (11.13->12.63) | +89 |
| Rouhomme | 368 | 0.10 | 0.10 (10/turn) | beer 32 (2.77->3.42), butter 1 (71.4->79.33), firewood 1 (1.6->5.46), flax fibres 2 (4.6->4.8) | bellows 1 (254.1->285), candles 1 (72.45->77.5), lead bars 5 (12.08->12.82), wax 1 (21->23.75) | +65 |
| Dedlowe | 1146 | 0.39 | 0.20 (19/turn) | cloth 18 (8.09->12.16), cured fish 2 (23.31->27.17), cheese 5 (5.51->6.13), thread 1 (4.03->4.56) | - | +64 |
| Vauxvais | 204 | 0.05 | 0.30 (29/turn) | bread 140 (2.18->2.64), beer 32 (2.77->3.12), flax fibres 4 (4.6->4.99), garments 10 (19.58->19.76) | glassware 1 (60.9->66.02), thread 38 (4.54->4.64), limestone 1 (12.6->15.29) | +60 |
| Fontaux | 411 | 0.11 | 0.30 (29/turn) | beer 32 (2.77->3.86), timber 13 (6.2->9.12), yarn 2 (4.35->6.89) | candles 1 (74.55->77.5), glassware 1 (64.05->66.02), wax 1 (21.84->23.75) | +56 |

**Best:** Cobholme at about +89 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 26.0, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 31 @ min 3.38 | makes 28.0, uses 4.2, holds 164 (keeps 60): sells the surplus + 7/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.1 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 0 @ 2.2, stop - |  | uses 496.8/turn (brewery 1, flax farm 1, household), makes 450.0, holds 21 = 0.4 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 34.8 |  |
| pasties | 3 @ 13.9, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 13 = 4.7 turns |
| porterage | 7 @ 1.1, stop - |  | uses 7.3/turn (observed), makes 0.0, holds 37 = 5.1 turns |
| rope |  | 2 @ min 79.0 |  |
| timber |  | 13 @ min 6.7 | makes 8.4, uses 0.0, holds 412 (keeps 350): sells the surplus + 5/turn of the excess |
| tools | 3 @ 6.2, stop 22 |  | uses 2.7/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 73.6 turns |

## Chain sizing

Mode HOLD, garments sold 2.8/turn (+0.0 exported); plan makes 1.6 garments a turn.
Labour: own 450, everything else 362, chain may buy 350 -> chain allowance 438, chain plan 135 (+1 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 2.69 | 2.76 |
| ret | 3 | 0.48 | 0.49 |
| spin | 4 | 1.05 | 1.06 |
| weave | 3 | 0.07 | 0.05 |
| sew | 2 | 0.04 | 0.04 |

Buffers: flax fibres 55/45, thread 288/133, cloth 10/6

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 2 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
