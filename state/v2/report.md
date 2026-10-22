# v2 shadow report

Turn 13465, 2026-10-22 10:59. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 4,919, prestige 3,568 (448 free, -1.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 129 | 0 | 4 | 0 | 0 | min_holding 60, sell 53, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 63 | 0 | 2 | 0 | 0 | min_holding 30, sell 10, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 290 | 285 | 732 | 0 | 3 | buy 282, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 18 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34.6 |
| porterage | 10 | 10 | 10 | 0 | 0 | buy 10, buy @ 1.1 |

**1 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.0 turns (holds 0, next step uses 45/turn) -> v2: check the step that makes it

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.3 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 69
- **flax plants**: flax plants buffer thin: 1.1 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 176

## Notes

- labour: projection runs 75 over real use lately; planning 741, not 816

## Prestige spending, cheapest coin per prestige first

936 turns left: prestige gained now converts 99.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.4 | 47.4 | running |
| hold banquet 4 (pies) | mansion | 18 | 47.9 | 47.9 | thin at home: wine, pies |
| hold banquet 3 (pies) | mansion | 8 | 48.2 | 48.2 | thin at home: pies |
| hold banquet 2 (pies) | mansion | 7 | 48.3 | 48.3 | thin at home: wine, pies |
| hold sermon 2 (candles) | church | 31 | 48.6 | 51.2 | needs a church (build cost 66,331); thin at home: jewellery, candles, furniture |
| hold banquet 4 | mansion | 17.5 | 51.8 | 51.8 | thin at home: wine, ham |
| jousting 3 | arena | 230 | 52.2 | 52.3 | needs a arena (build cost 26,238); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 53.4 | 53.4 | thin at home: wine |
| hold banquet 1 (fish) | mansion | 4.2 | 54.0 | 54.0 |  |
| hold sermon 2 | church | 24 | 50.8 | 54.0 | needs a church (build cost 66,331); thin at home: jewellery, furniture |
| hold prayer 2 | chapel | 13 | 51.1 | 54.1 | needs a chapel (build cost 33,518); thin at home: furniture |
| hold banquet 3 (fish) | mansion | 7.6 | 54.4 | 54.4 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.10 | 10 | 120102307 | 0 | nets 1, rope 1 | furniture 11 | -116 |
| linen snake | 0.1 / 0.06 | 6 | 185801747 | 0.092 | - | furniture 1 | -14 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Rouhomme: nothing pays; crew 0.0; est +0 a turn; best orders clear only -6 a turn after crew: ship stays at 0
- **linen snake** on Neuborn: nothing pays; crew 0.0; est +0 a turn
- best towns now: Marmont +16
- Marmont would trade: beer sell 51 @ 4.5; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~98 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Rotterburg | 1056 | 0.34 | 0.20 (20/turn) | windows 1 (588->698.25), nets 3 (35.6->38.95), leather 1 (24.57->27.93), butter 1 (59.85->63.17) | mouldboards 1 (23.73->26.6), pasties 1 (9.35->13), raw cloth 1 (5.88->6.93) | +124 |
| Rouhomme | 368 | 0.10 | 0.20 (20/turn) | stockfish 2 (123.9->149.15), furniture 12 (11.87->13.49), iron ore 2 (4.49->8.46), thread 10 (4.06->4.6) | spinning wheels 2 (222.6->231.8), coats 1 (53.03->63.17), steel ingots 2 (15.96->16.62), tools 3 (4.51->4.82) | +112 |
| Boistot | 1230 | 0.43 | 0.10 (10/turn) | medicine 1 (126->178.6), tackles 1 (176.4->216.6), varnish 1 (17.64->24.13), pies 1 (12.71->14.44) | steel ingots 2 (14.6->16.62), canvas 1 (25.2->28.12), mouldboards 1 (23.94->26.6), raw cloth 1 (5.35->6.93) | +101 |
| Caillechâtel | 488 | 0.13 | 0.20 (20/turn) | beer 44 (3.18->4.62), nets 9 (35.6->36.48), pies 1 (12.71->16.25), rope 2 (73.5->75.05) | glass ingots 1 (38.64->48.92), flax fibres 11 (4.85->5.85), flax plants 28 (1.24->1.69), raw cloth 1 (5.3->6.93) | +94 |
| Heilegg | 826 | 0.22 | 0.40 (39/turn) | casks 5 (5.72->9.17), grindstones 1 (277.2->296.4), lead ore 6 (10.19->12.73), furniture 12 (11.87->13.21) | gold bars 1 (782.25->817), steel ingots 4 (15.96->16.62), coats 1 (62.48->63.17), pasties 2 (12.18->13) | +87 |

**Best:** Rotterburg at about +124 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 53 @ min 3.38 | makes 56.0, uses 4.2, holds 129 (keeps 60): sells the surplus + 1/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 24 @ min 20.0 | makes 23.0, uses 2.1, holds 63 (keeps 30): sells the surplus + 3/turn of the excess |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 291 @ 2.2, stop - |  | uses 741.3/turn (brewery 1, flax farm 1, household), makes 450.0, holds 290 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 11 @ min 34.6 |  |
| pasties | 3 @ 13.6, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 5.0 turns |
| porterage | 10 @ 1.1, stop - |  | uses 10.3/turn (observed), makes 0.0, holds 10 = 1.0 turns |
| rope |  | 2 @ min 71.5 |  |
| timber |  | 8 @ min 6.5 |  |
| tools | 4 @ 6.2, stop 30 |  | uses 3.7/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 53.8 turns |

## Chain sizing

Mode HOLD, garments sold 14.5/turn (+2.3 exported); plan makes 19.3 garments a turn.
Labour: own 450, everything else 415, chain may buy 350 -> chain allowance 385, chain plan 385 (-12 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.54 | 5.81 |
| ret | 3 | 0.98 | 1.03 |
| spin | 4 | 2.03 | 2.13 |
| weave | 3 | 0.90 | 0.76 |
| sew | 2 | 0.56 | 0.47 |

Buffers: flax fibres 44/76, thread 282/223, cloth 0/76
- chain plan needed 636 labour, budget left 385: cut to 385 (sewing capped at 0.47)

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
