# v2 shadow report

Turn 13340, 2026-10-17 05:52. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,507, prestige 3,250 (580 free, +3.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 185 | 0 | 19 | 0 | 0 | min_holding 60, sell 19, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 17 | 5 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 14, sell @ 22 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 271 | 272 | 721 | 0 | 1 | buy 271, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 37 | 0 | 0 | 0 | 0 | min_holding 15, sell 10, sell @ 34 |
| porterage | 11 | 11 | 11 | 0 | 0 | buy 11, buy @ 1.1 |

**1 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.4 turns (holds 14, next step uses 31/turn) -> v2: check the step that makes it

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.5 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 76
- **flax plants**: flax plants buffer thin: 1.9 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 198

## Notes

- labour: projection runs 74 over real use lately; planning 721, not 794

## Prestige spending, cheapest coin per prestige first

1061 turns left: prestige gained now converts 99.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.6 | 48.6 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 55.8 | 55.8 | thin at home: wine, cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 56.4 | 56.4 | thin at home: cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 56.8 | 56.8 | thin at home: cured fish |
| hold banquet 2 (meat) | mansion | 6.8 | 57.7 | 57.7 | thin at home: wine |
| hold banquet 3 (meat) | mansion | 7.6 | 58.2 | 58.2 |  |
| jousting 1 | arena | 170 | 58.4 | 58.5 | needs a arena (build cost 24,035); thin at home: protection, light armour, arms; needs weaponry skill |
| hold prayer 2 | chapel | 13 | 57.2 | 59.6 | needs a chapel (build cost 30,686); thin at home: furniture |
| hold banquet 1 (meat) | mansion | 4.2 | 59.9 | 59.9 | running |
| hold sermon 2 (candles) | church | 31 | 57.5 | 60.1 | needs a church (build cost 77,692); thin at home: jewellery, candles, furniture |
| hold sermon 2 | church | 24 | 57.4 | 60.7 | needs a church (build cost 77,692); thin at home: jewellery, furniture |
| hold feast 2 | townhouse | 2.6 | 58.2 | 60.9 | needs a townhouse (build cost 7,158); thin at home: wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 74001604 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | cured meat 5 | -109 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Brunnham: nothing pays; crew 0.0; est +0 a turn; best orders clear only -1 a turn after crew: ship stays at 0
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn; best orders clear only -2 a turn after crew: ship stays at 0
- best towns now: Karlmoor +38
- Karlmoor would trade: candles buy 1 @ 64.5, nets sell 5 @ 42.0; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~98 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Karlmoor | 787 | 0.21 | 0.10 (10/turn) | nets 5 (35.6->44.27), garments 13 (19.61->21.47), tools 9 (4.5->5.98) | candles 1 (66.67->81), pasties 1 (6.25->11.97), cloth 12 (8.29->8.65) | +95 |
| Friedwerp | 684 | 0.18 | 0.20 (20/turn) | tools 16 (4.5->6.65), garments 13 (19.61->21.09), beer 19 (2.94->3.72), thread 9 (4.66->4.94) | cloth 17 (8.14->8.65), candles 1 (76.65->81), pies 1 (16.59->19.19), hop beer 1 (7.67->8.74) | +72 |
| Rouhomme | 368 | 0.10 | 0.20 (20/turn) | thread 23 (4.66->6.22), soap 1 (86.1->99.75), beer 19 (2.94->3.65), garments 13 (19.61->20.14) | flax plants 3 (0.56->1.59), tools 3 (4.91->5.05) | +72 |
| Caillechâtel | 488 | 0.13 | 0.10 (10/turn) | beer 19 (2.94->4.89), garments 10 (19.61->21.47), nets 6 (35.6->37.24), tools 3 (4.5->5.13) | flax plants 23 (1.29->1.59), cured meat 3 (22.89->23.2) | +60 |
| Calange | 218 | 0.06 | 0.10 (10/turn) | beer 19 (2.94->4.6), soap 1 (86.1->99.75), rope 2 (79.5->82.65), cloth 4 (7.3->7.84) | garments 2 (21->22.6) | +50 |

**Best:** Karlmoor at about +95 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 18 @ min 3.7 | makes 28.0, uses 19.2, holds 185 (keeps 60): sells the surplus + 10/turn of the excess |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 8 = 5.0 turns |
| cured meat | 8 @ 24.2, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 20 = 3.3 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 17 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 14 @ min 22.0 |  |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 271 @ 2.2, stop - |  | uses 721.0/turn (brewery 1, flax farm 1, household), makes 450.0, holds 271 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 10 @ min 34.6 | makes 9.0, uses 0.0, holds 37 (keeps 15): sells the surplus + 1/turn of the excess |
| porterage | 11 @ 1.1, stop - |  | uses 11.0/turn (observed), makes 0.0, holds 11 = 1.0 turns |
| rope |  | 6 @ min 77.5 | makes 4.5, uses 0.0, holds 27 (keeps 0): sells the surplus + 2/turn of the excess |
| tar | 2 @ 11.0, stop 5 |  | uses 1.0/turn (ropewalk 1), makes 0.0, holds 9 = 9.2 turns |
| timber |  | 27 @ min 6.7 | makes 8.4, uses 0.0, holds 579 (keeps 350): sells the surplus + 18/turn of the excess |
| tools | 4 @ 6.2, stop 32 |  | uses 4.0/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 50.4 turns |

## Chain sizing

Mode HOLD, garments sold 18.0/turn (+0.0 exported); plan makes 17.2 garments a turn.
Labour: own 450, everything else 411, chain may buy 350 -> chain allowance 389, chain plan 390 (+6 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 6.18 | 6.26 |
| ret | 3 | 1.10 | 1.11 |
| spin | 4 | 2.26 | 2.29 |
| weave | 3 | 0.69 | 0.67 |
| sew | 2 | 0.39 | 0.42 |

Buffers: flax fibres 58/85, thread 365/249, cloth 14/67
- chain plan needed 598 labour, budget left 389: cut to 389 (sewing capped at 0.42)

## Self-diagnosis

- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
