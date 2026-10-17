# v2 shadow report

Turn 13336, 2026-10-17 01:54. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 15,278, prestige 3,241 (571 free, -4.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 212 | 0 | 4 | 0 | 0 | min_holding 60, sell 35, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 33 | 0 | 2 | 0 | 0 | min_holding 30, sell 19, sell @ 22 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 271 | 271 | 719 | 0 | 2 | buy 271, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 48 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 34 |
| porterage | 11 | 11 | 11 | 0 | 0 | buy 11, buy @ 1.1 |

**2 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.0 turns (holds 0, next step uses 42/turn) -> v2: check the step that makes it
- **labour**: buying 271, short of ~307 needed -> v2: buy 307

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax fibres**: flax fibres buffer thin: 1.4 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 80
- **flax plants**: flax plants buffer thin: 1.9 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 201

## Notes

- labour: projection runs 73 over real use lately; planning 757, not 830

## Prestige spending, cheapest coin per prestige first

1065 turns left: prestige gained now converts 99.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.9 | 48.9 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 55.0 | 55.0 | thin at home: cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 55.7 | 55.7 | thin at home: hop beer, cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 55.9 | 55.9 | thin at home: cured fish |
| hold banquet 2 (meat) | mansion | 6.8 | 57.8 | 57.8 |  |
| hold banquet 3 (meat) | mansion | 7.6 | 58.2 | 58.2 | thin at home: hop beer |
| hold prayer 2 | chapel | 13 | 57.3 | 59.6 | needs a chapel (build cost 30,210); thin at home: furniture |
| hold banquet 1 (meat) | mansion | 4.2 | 59.9 | 59.9 | running |
| hold sermon 2 (candles) | church | 31 | 57.5 | 60.1 | needs a church (build cost 76,674); thin at home: jewellery, candles, furniture |
| hold sermon 2 | church | 24 | 57.4 | 60.7 | needs a church (build cost 76,674); thin at home: jewellery, furniture |
| hold feast 2 | townhouse | 2.6 | 58.3 | 60.8 | needs a townhouse (build cost 6,826); thin at home: wine |
| hold banquet 4 (pies) | mansion | 18 | 61.4 | 61.4 | thin at home: hop beer |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 74001604 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Brunnham: nothing pays; crew 0.0; est +0 a turn; best orders clear only 12 a turn after crew: ship stays at 0
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn; best orders clear only 8 a turn after crew: ship stays at 0
- best towns now: Brebronn +18
- Brebronn would trade: beer sell 36 @ 5.05; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~99 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Rouhomme | 368 | 0.10 | 1.00 (99/turn) | bread 129 (2.29->3.12), thread 18 (4.66->6.08), charcoal 11 (1.77->4.31), timber 22 (6.35->8.55) | flax plants 2 (0.69->1.21), garments 1 (22.05->22.6), tools 2 (4.91->5.15) | +170 |
| Brebronn | 862 | 0.24 | 0.30 (30/turn) | beer 36 (2.96->5.65), wrought iron 13 (14.07->17.39), garments 15 (19.84->20.9), tools 13 (4.5->5.03) | wine 20 (5.25->5.61), wool 1 (8.87->9.21) | +139 |
| Orlesailles | 1178 | 0.41 | 0.20 (20/turn) | garments 18 (19.84->22.8), thread 22 (4.66->6.27), nets 1 (34.2->36.29) | cloth 6 (8.24->8.75), pies 2 (17.32->18.81) | +75 |
| Etallaen | 774 | 0.20 | 0.30 (30/turn) | flax fibres 4 (5.55->11.59), beer 36 (2.96->3.76), garments 18 (19.84->20.71), flax plants 9 (1.27->2.68) | - | +63 |
| Dortgart | 1045 | 0.34 | 0.30 (30/turn) | beer 32 (2.96->5.08), garments 13 (19.84->21.09) | cloth 2 (8.4->8.75) | +55 |

**Best:** Rouhomme at about +170 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 21 @ min 3.7 | makes 28.0, uses 19.2, holds 212 (keeps 60): sells the surplus + 12/turn of the excess |
| cured meat | 6 @ 24.2, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 24 = 4.0 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.1 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 19 @ min 22.0 |  |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 307 @ 2.2, stop - |  | uses 757.1/turn (brewery 1, flax farm 1, household), makes 450.0, holds 271 = 0.9 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 11 @ min 34.0 | makes 9.0, uses 0.0, holds 48 (keeps 15): sells the surplus + 2/turn of the excess |
| porterage | 10 @ 1.1, stop - |  | uses 10.1/turn (observed), makes 0.0, holds 11 = 1.1 turns |
| rope |  | 6 @ min 77.5 | makes 4.5, uses 0.0, holds 17 (keeps 0): sells the surplus + 1/turn of the excess |
| timber |  | 28 @ min 6.7 | makes 8.4, uses 0.0, holds 594 (keeps 350): sells the surplus + 20/turn of the excess |
| tools | 4 @ 6.2, stop 32 |  | uses 4.0/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 50.0 turns |

## Chain sizing

Mode HOLD, garments sold 19.8/turn (+0.0 exported); plan makes 17.6 garments a turn.
Labour: own 450, everything else 411, chain may buy 350 -> chain allowance 389, chain plan 390 (-33 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 6.44 | 6.18 |
| ret | 3 | 1.12 | 1.10 |
| spin | 4 | 2.36 | 2.26 |
| weave | 3 | 0.80 | 0.69 |
| sew | 2 | 0.52 | 0.43 |

Buffers: flax fibres 57/85, thread 397/251, cloth 0/69
- chain plan needed 582 labour, budget left 389: cut to 389 (sewing capped at 0.43)

## Self-diagnosis

- R1: candles slot dry: 0.0 held, 1.5 a turn (luxury slot (+3 prestige)); our buy paused by the failsafe, home ask 81.0 -> **un-pause and buy 3 @ 82.5 (ask 81.0, cap 120.0)** (ok)
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
- R4: ropewalk 1 projected 0: short of labour (~28 needed); labour itself is not raised here
