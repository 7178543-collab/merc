# v2 shadow report

Turn 13328, 2026-10-16 17:54. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,266, prestige 3,198 (528 free, -3.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 250 | 0 | 4 | 0 | 0 | min_holding 60, sell 38, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 17 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 32 | 0 | 2 | 0 | 0 | min_holding 30, sell 20, sell @ 22 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 286 | 286 | 728 | 0 | 8 | buy 286, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 63 | 0 | 0 | 0 | 0 | min_holding 15, sell 12, sell @ 36 |
| porterage | 21 | 21 | 13 | 0 | 8 | buy 21, buy @ 1.1 |

**1 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.1 turns (holds 6, next step uses 43/turn) -> v2: check the step that makes it

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax fibres**: flax fibres buffer thin: 1.6 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 76
- **flax plants**: flax plants buffer thin: 1.8 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 194

## Notes

- labour: projection runs 73 over real use lately; planning 728, not 801

## Prestige spending, cheapest coin per prestige first

1073 turns left: prestige gained now converts 99.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.0 | 51.0 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 56.5 | 56.5 | thin at home: wine, cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 56.7 | 56.7 | thin at home: hop beer, cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 58.0 | 58.0 | thin at home: cured fish |
| hold banquet 3 (meat) | mansion | 7.6 | 59.7 | 59.7 | thin at home: hop beer |
| hold banquet 2 (meat) | mansion | 6.8 | 59.9 | 59.9 | thin at home: wine |
| hold banquet 3 (pies) | mansion | 8 | 60.0 | 60.0 | thin at home: pasties, hop beer, pies |
| hold feast 2 | townhouse | 2.6 | 57.3 | 60.2 | needs a townhouse (build cost 7,980); thin at home: wine |
| hold banquet 2 (pies) | mansion | 7 | 61.2 | 61.2 | thin at home: pasties, wine, pies |
| hold sermon 2 (candles) | church | 31 | 58.7 | 61.5 | needs a church (build cost 82,963); thin at home: jewellery, candles, furniture |
| hold prayer 2 | chapel | 13 | 59.2 | 61.8 | needs a chapel (build cost 35,100); thin at home: furniture |
| hold sermon 2 | church | 24 | 58.9 | 62.4 | needs a church (build cost 82,963); thin at home: jewellery, furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 74001604 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Brunnham: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn
- best towns now: Gottweiler +15
- Gottweiler would trade: nets sell 5 @ 41.4; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~103 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hanbrücken | 531 | 0.15 | 0.10 (10/turn) | garments 20 (20.64->24.13), cloth 17 (8.77->11.69), glassware 1 (61.43->76.47), medicine 1 (120.75->123.5) | bellows 1 (235.2->273.6), flax fibres 4 (5.78->6.3) | +174 |
| Gottweiler | 1135 | 0.41 | 0.30 (31/turn) | garments 20 (20.64->22.8), nets 5 (35.8->40.09), cloth 17 (8.77->9.97), butter 1 (74.55->78.38) | bellows 1 (241.5->273.6), cured meat 5 (21.42->23.37), candles 2 (65.1->67.92), glassware 1 (54.08->54.62) | +112 |
| Friedwerp | 684 | 0.19 | 0.30 (31/turn) | beer 39 (2.97->4.52), garments 18 (20.64->21.09), nets 1 (35.8->39.52), arms 3 (27.72->28.5) | cloth 17 (7.77->8.35), pies 1 (16.59->17.95), hop beer 1 (7.61->8.36) | +60 |
| Fontaux | 411 | 0.11 | 0.20 (21/turn) | beer 39 (2.97->4.2), garments 18 (20.64->21.28), casks 3 (5.46->6.84), ploughs 1 (74.03->78.38) | flax fibres 14 (5.72->6.3) | +57 |
| Gosschweig | 1099 | 0.39 | 0.10 (10/turn) | mouldboards 1 (52.5->78.38), canvas 1 (39.9->60.32), tiles 1 (3.56->8.93), slaked lime 1 (5.62->7.55) | tools 4 (3.63->5.15), garments 2 (22.89->23.4) | +51 |

**Best:** Hanbrücken at about +174 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 38 @ min 3.7 | makes 28.0, uses 4.2, holds 250 (keeps 60): sells the surplus + 14/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 17 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 20 @ min 22.0 |  |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 278 @ 2.2, stop - |  | uses 728.0/turn (brewery 1, flax farm 1, household), makes 450.0, holds 286 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 12 @ min 36.0 | makes 9.0, uses 0.0, holds 63 (keeps 15): sells the surplus + 3/turn of the excess |
| porterage | 13 @ 1.1, stop - |  | uses 12.8/turn (observed), makes 0.0, holds 21 = 1.6 turns |
| rope |  | 5 @ min 78.0 |  |
| tar | 2 @ 11.0, stop 5 |  | uses 1.0/turn (ropewalk 1), makes 0.0, holds 10 = 9.4 turns |
| timber |  | 34 @ min 8.5 | makes 12.0, uses 0.0, holds 628 (keeps 350): sells the surplus + 22/turn of the excess |
| tools | 5 @ 6.2, stop 38 |  | uses 4.7/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 42.7 turns |

## Chain sizing

Mode HOLD, garments sold 15.2/turn (+0.0 exported); plan makes 20.9 garments a turn.
Labour: own 450, everything else 385, chain may buy 350 -> chain allowance 415, chain plan 414 (-2 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 6.16 | 6.24 |
| ret | 3 | 1.08 | 1.11 |
| spin | 4 | 2.25 | 2.28 |
| weave | 3 | 0.84 | 0.82 |
| sew | 2 | 0.54 | 0.51 |

Buffers: flax fibres 63/90, thread 480/264, cloth 6/82
- chain plan needed 564 labour, budget left 415: cut to 415 (sewing capped at 0.51)

## Self-diagnosis

- R1: candles slot dry: 0.0 held, 1.5 a turn (luxury slot (+3 prestige)); our buy paused by the failsafe, home ask 81.5 (held back: paused by the failsafe at level 1: un-pause only at level 0)
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
