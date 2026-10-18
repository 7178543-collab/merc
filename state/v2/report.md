# v2 shadow report

Turn 13373, 2026-10-18 14:50. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 5,474, prestige 3,253 (583 free, -1.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 418 | 0 | 4 | 0 | 0 | min_holding 60, sell 34, sell @ 3.54 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 17 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 380 | 0 | 2 | 0 | 0 | min_holding 30, sell 36, sell @ 21.2 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 137 | 137 | 550 | 0 | 37 | buy 110, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 56 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 38.6 |
| porterage | 11 | 11 | 9 | 0 | 2 | buy 11, buy @ 1.1 |

**0 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **labour**: 37 labour expired last turn (~62 coin): holding 137 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **cloth**: cloth buffer thin: 1.3 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 51
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **furniture**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 73 over real use lately; planning 550, not 611
- labour expiry guard: 37 bought labour expired last turn, buy 100 (not 100) this turn

## Prestige spending, cheapest coin per prestige first

1028 turns left: prestige gained now converts 99.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.5 | 49.5 | running |
| hold sermon 2 (candles) | church | 31 | 53.9 | 56.7 | needs a church (build cost 81,940); thin at home: candles, furniture |
| hold prayer 2 | chapel | 13 | 54.2 | 56.8 | needs a chapel (build cost 32,792); thin at home: furniture |
| hold feast 2 | townhouse | 2.6 | 54.6 | 57.4 | needs a townhouse (build cost 7,258); thin at home: wine |
| hold banquet 2 (fish) | mansion | 6.8 | 57.6 | 57.6 | thin at home: cured fish |
| hold banquet 2 (meat) | mansion | 6.8 | 58.7 | 58.7 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 58.8 | 58.8 | thin at home: hop beer, cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 59.1 | 59.1 | thin at home: cured fish |
| hold sermon 2 | church | 24 | 55.6 | 59.2 | needs a church (build cost 81,940); thin at home: furniture |
| hold banquet 3 (meat) | mansion | 7.6 | 59.8 | 59.8 | thin at home: hop beer |
| hold banquet 3 (pies) | mansion | 8 | 60.3 | 60.3 | thin at home: hop beer, pies |
| hold banquet 2 (pies) | mansion | 7 | 61.0 | 61.0 | thin at home: pies |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 64601365 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Disscester: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~100 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Clarfranche | 1484 | 0.58 | 0.30 (30/turn) | slaked lime 1 (7.56->15.39) | plate armour 1 (1669.5->1957), cookware 7 (19.84->23.56), jewellery 1 (80.33->85.97), mouldboards 1 (36.54->41.8) | +317 |
| Bremcop | 1326 | 0.49 | 0.10 (10/turn) | soap 1 (90.3->160.55), stockfish 1 (97.12->101.65), thread 4 (4.66->5.18) | cookware 6 (22.26->23.56), tar 2 (9.03->11.4), casks 1 (3.32->5.27) | +82 |
| Karlmoor | 787 | 0.21 | 0.10 (10/turn) | stockfish 1 (97.12->133), tools 10 (4.24->5.42), nails 3 (6.25->9.59) | cookware 6 (22.05->23.56), flax fibres 7 (5.72->6.95), tar 4 (9.97->11.4), pasties 1 (9.71->13.11) | +76 |
| Birkeningen | 1006 | 0.33 | 0.40 (40/turn) | beer 49 (3->4.5), tools 16 (4.24->5.42), stockfish 1 (97.12->100.7), varnish 1 (18.17->18.52) | cookware 7 (21.84->23.56) | +69 |
| Rouhomme | 368 | 0.10 | 0.20 (20/turn) | beer 53 (3->3.76), stockfish 1 (97.12->105.45), cloth 2 (7.8->11.59), tallow 1 (22.26->22.8) | cookware 7 (21->23.56), jewellery 1 (78.75->85.97), flax fibres 3 (5.88->6.95), blades 2 (14.7->15.2) | +66 |

**Best:** Clarfranche at about +317 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 52 @ min 3.54 | makes 28.0, uses 4.2, holds 418 (keeps 60): sells the surplus + 28/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 17 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| furniture | 3 @ 15.5, stop 6 |  | uses 1.4/turn (household upkeep), makes 0.0, holds 2 = 1.3 turns |
| garments |  | 39 @ min 21.2 | makes 13.1, uses 2.1, holds 380 (keeps 30): sells the surplus + 28/turn of the excess |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 100 @ 2.2, stop - |  | uses 549.6/turn (brewery 1, flax farm 1, household), makes 450.0, holds 137 = 1.4 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 12 @ min 37.0 | makes 9.0, uses 0.0, holds 56 (keeps 15): sells the surplus + 3/turn of the excess |
| porterage | 9 @ 1.1, stop - |  | uses 8.6/turn (observed), makes 0.0, holds 11 = 1.3 turns |
| rope |  | 7 @ min 77.5 | makes 2.2, uses 0.0, holds 60 (keeps 0): sells the surplus + 5/turn of the excess |
| timber |  | 8 @ min 6.7 |  |
| tools | 4 @ 6.2, stop 26 |  | uses 3.2/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 62.9 turns |

## Chain sizing

Mode HOLD, garments sold 3.3/turn (+0.0 exported); plan makes 13.9 garments a turn.
Labour: own 450, everything else 362, chain may buy 350 -> chain allowance 438, chain plan 274 (+11 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 3.98 | 4.12 |
| ret | 3 | 0.71 | 0.73 |
| spin | 4 | 1.46 | 1.51 |
| weave | 3 | 0.51 | 0.54 |
| sew | 2 | 0.32 | 0.34 |

Buffers: flax fibres 59/62, thread 362/181, cloth 34/54

## Self-diagnosis

- R1: arms slot dry: 0.0 held, 0.5 a turn (gear slot (+0.4 prestige)); our buy paused by the failsafe, home ask 25.0 (held back: paused by the failsafe at level 3: un-pause only at level 0)
- R1: furniture slot dry: 1.8 held, 1.4 a turn (household slot (+0.4 prestige)); our buy paused by the failsafe, home ask none (no sellers at home)
- R2: ropewalk 1 blocked by rope space: 60 held of 60 capacity, we make 2.2 a turn; no buy on it: add a sell order or more capacity for rope
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
