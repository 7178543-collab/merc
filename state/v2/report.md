# v2 shadow report

Turn 13339, 2026-10-17 04:54. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,946, prestige 3,247 (577 free, +3.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 191 | 0 | 19 | 0 | 0 | min_holding 60, sell 20, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 18 | 4 | 4 | 0 | 0 | stop 18, buy 5, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 14, sell @ 22 |
| grain | 51 | 13 | 13 | 0 | 0 | stop 52, buy 14, buy @ 3.7 |
| labour | 272 | 271 | 721 | 0 | 0 | buy 272, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 39 | 0 | 0 | 0 | 0 | min_holding 15, sell 10, sell @ 34 |
| porterage | 11 | 11 | 11 | 0 | 0 | buy 11, buy @ 1.1 |

**1 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.3 turns (holds 10, next step uses 31/turn) -> v2: check the step that makes it

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.5 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 76
- **flax plants**: flax plants buffer thin: 1.9 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 198

## Notes

- labour: projection runs 74 over real use lately; planning 721, not 794

## Prestige spending, cheapest coin per prestige first

1062 turns left: prestige gained now converts 99.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.9 | 48.9 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 55.9 | 55.9 | thin at home: wine, cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 56.5 | 56.5 | thin at home: cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 56.9 | 56.9 | thin at home: cured fish |
| hold banquet 2 (meat) | mansion | 6.8 | 57.5 | 57.5 | thin at home: wine |
| hold banquet 3 (meat) | mansion | 7.6 | 58.0 | 58.0 |  |
| jousting 1 | arena | 170 | 58.2 | 58.4 | needs a arena (build cost 24,015); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 1 (meat) | mansion | 4.2 | 59.7 | 59.7 | running |
| hold sermon 2 (candles) | church | 31 | 57.2 | 59.8 | needs a church (build cost 77,697); thin at home: jewellery, candles, furniture |
| hold prayer 2 | chapel | 13 | 57.7 | 60.0 | needs a chapel (build cost 30,696); thin at home: furniture |
| hold feast 2 | townhouse | 2.6 | 58.3 | 61.0 | needs a townhouse (build cost 7,156); thin at home: wine |
| hold sermon 2 | church | 24 | 57.7 | 61.0 | needs a church (build cost 77,697); thin at home: jewellery, furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 74001604 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | cured meat 5 | -110 |

## Ship plans (this turn's world prices)

- **linen snake** on Heilegg: candles buy 1 @ 74.0, nets sell 7 @ 41.6; crew 0.1; est +38 a turn
- **Flax Wyrm** on Brunnham: nothing pays; crew 0.0; est +0 a turn
- best towns now: Heilegg +38, Donaunieder +28, Karlmoor +26, Caillechâtel +17, Magdeach +16
- Heilegg would trade: candles buy 1 @ 74.0, nets sell 7 @ 41.6; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~99 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Rouhomme | 368 | 0.10 | 0.70 (69/turn) | bread 142 (2.29->3.08), charcoal 13 (1.81->4.89), thread 16 (4.66->6.08), soap 1 (85.58->99.75) | lead bars 1 (8.93->10.64), flax plants 3 (0.6->1.28), tools 3 (4.91->5.15) | +172 |
| Karlmoor | 787 | 0.21 | 0.20 (20/turn) | nets 6 (35->42.75), tools 16 (4.5->6.17), garments 13 (19.64->21.28), beer 19 (2.94->3.53) | cloth 12 (8.29->8.75), pasties 1 (8.51->11.88) | +95 |
| Caillechâtel | 488 | 0.13 | 0.10 (10/turn) | beer 19 (2.94->4.41), nets 7 (35->37.24), garments 10 (19.64->21.09), wine 2 (6.25->8.5) | thread 30 (4.43->5.05), seeds 8 (1.85->2.32), cloth 8 (8.56->8.75), rope 1 (74.03->75.52) | +73 |
| Friedwerp | 684 | 0.18 | 0.10 (10/turn) | tools 16 (4.5->6.65), garments 13 (19.64->21.09) | cloth 17 (8.14->8.75), pies 1 (16.59->19.19), thread 17 (4.73->5.05), hop beer 1 (7.67->8.74) | +60 |
| Heilegg | 826 | 0.23 | 0.20 (20/turn) | nets 7 (35->41.04), flax plants 9 (1.27->2.24), garments 13 (19.64->20.14), beer 19 (2.94->3.53) | pies 2 (18.06->19.19), candles 1 (77.17->77.5) | +52 |

**Best:** Rouhomme at about +172 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 19 @ min 3.7 | makes 28.0, uses 19.2, holds 191 (keeps 60): sells the surplus + 10/turn of the excess |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 6 = 4.0 turns |
| cured meat | 8 @ 24.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 21 = 3.5 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 5 @ 2.4, stop 18 |  | uses 4.4/turn (brewery 1, household upkeep), makes 0.0, holds 18 = 4.0 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 14 @ min 22.0 |  |
| grain | 14 @ 3.7, stop 52 |  | uses 13.0/turn (brewery 1), makes 0.0, holds 51 = 3.9 turns |
| labour | 271 @ 2.2, stop - |  | uses 721.0/turn (brewery 1, flax farm 1, household), makes 450.0, holds 272 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 10 @ min 34.0 | makes 9.0, uses 0.0, holds 39 (keeps 15): sells the surplus + 1/turn of the excess |
| porterage | 11 @ 1.1, stop - |  | uses 11.0/turn (observed), makes 0.0, holds 11 = 1.0 turns |
| rope |  | 6 @ min 77.5 | makes 4.5, uses 0.0, holds 22 (keeps 0): sells the surplus + 1/turn of the excess |
| tar | 2 @ 11.0, stop 5 |  | uses 1.0/turn (ropewalk 1), makes 0.0, holds 9 = 9.2 turns |
| timber |  | 27 @ min 6.7 | makes 8.4, uses 0.0, holds 578 (keeps 350): sells the surplus + 18/turn of the excess |
| tools | 4 @ 6.2, stop 32 |  | uses 4.0/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 50.4 turns |

## Chain sizing

Mode HOLD, garments sold 18.5/turn (+0.0 exported); plan makes 17.2 garments a turn.
Labour: own 450, everything else 411, chain may buy 350 -> chain allowance 389, chain plan 389 (+5 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 6.18 | 6.24 |
| ret | 3 | 1.10 | 1.11 |
| spin | 4 | 2.26 | 2.28 |
| weave | 3 | 0.69 | 0.67 |
| sew | 2 | 0.39 | 0.42 |

Buffers: flax fibres 58/85, thread 373/249, cloth 10/67
- chain plan needed 598 labour, budget left 389: cut to 389 (sewing capped at 0.42)

## Self-diagnosis

- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
