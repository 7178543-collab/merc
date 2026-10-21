# v2 shadow report

Turn 13436, 2026-10-21 05:57. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 3,282, prestige 3,530 (860 free, +18.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 52, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 50 | 0 | 2 | 0 | 0 | min_holding 30, sell 20, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 264 | 264 | 714 | 0 | 0 | buy 264, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 15 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 37.4 |
| porterage | 10 | 10 | 10 | 0 | 0 | buy 10, buy @ 1.1 |

**1 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.0 turns (holds 2, next step uses 42/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **linen snake**: linen snake cost 10 coin last turn (crew 0.10) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.5 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 65
- **flax plants**: flax plants buffer thin: 1.0 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 167
- **timber**: build materials for net maker152202386007001 are in (304.7 held, 56 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **net maker152202386007001** 63% (INITIAL), about 5 turns left; still to deliver: labour 74, timber 56, tools 8; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| timber | 56 | 304.7 | 0 | off: covered; switch v1's buy off |
| tools | 8 | 199.8 | 0 | off: covered |

Labour metered per turn while a site can progress: labour 15

## Notes

- labour: projection runs 96 over real use lately; planning 714, not 806

## Prestige spending, cheapest coin per prestige first

965 turns left: prestige gained now converts 99.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.0 | 51.0 | running |
| hold sermon 2 (candles) | church | 31 | 49.7 | 52.3 | needs a church (build cost 71,220); thin at home: jewellery, candles, furniture |
| hold banquet 3 (pies) | mansion | 8 | 53.2 | 53.2 | thin at home: pasties, hop beer, pies |
| hold prayer 2 | chapel | 13 | 50.9 | 53.7 | needs a chapel (build cost 33,406); thin at home: furniture |
| hold sermon 2 | church | 24 | 51.3 | 54.7 | needs a church (build cost 71,220); thin at home: jewellery, furniture |
| hold banquet 4 (pies) | mansion | 18 | 55.8 | 55.8 | thin at home: hop beer, wine |
| hold banquet 1 (fish) | mansion | 4.2 | 56.2 | 56.2 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 56.7 | 56.7 | thin at home: hop beer, cured fish |
| hold mass 1 | cathedral | 180 | 55.4 | 57.3 | needs a cathedral (build cost 285,040); thin at home: jewellery, glassware, candles |
| hold banquet 2 (pies) | mansion | 7 | 57.9 | 57.9 | thin at home: pasties, wine, pies |
| jousting 3 | arena | 230 | 58.5 | 58.6 | needs a arena (build cost 26,734); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (meat) | mansion | 7.6 | 59.7 | 59.7 | thin at home: hop beer |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 10 | 120102307 | 0.092 | - | furniture 2 | -28 |
| linen snake | 0.1 / 0.10 | 10 | 185801747 | 0.08 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Rouhomme: nothing pays; crew 0.0; est +0 a turn; best orders clear only -7 a turn after crew: ship stays at 0
- **linen snake** on Neuborn: nothing pays; crew 0.0; est +0 a turn
- best towns now: Karlmoor +21, Brunnham +19, Bedenis +16
- Karlmoor would trade: garments sell 14 @ 22.8; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~104 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Coburgbaum | 619 | 0.17 | 0.10 (10/turn) | bellows 1 (312.9->421.8), seeds 8 (1.84->3.32), belts 2 (24.99->26.6), cheese 7 (8.24->8.55) | wool 3 (9.92->11.4), spirits 1 (10.92->14.25), steel ingots 1 (12.71->15.39), butter 1 (66.15->67.92) | +130 |
| Chribruck | 1202 | 0.45 | 0.10 (10/turn) | soap 2 (92.4->152.95) | jewellery 1 (64.58->71.72), wool 5 (9.5->11.4), dyed cloth 2 (9.61->10.92) | +130 |
| Rouhomme | 368 | 0.10 | 0.10 (10/turn) | cloth 16 (7.93->11.02), raw cloth 1 (5.83->6.17), thread 6 (4.32->4.48) | ploughs 2 (55.65->69.83), wool 2 (9.29->11.4), dyed cloth 2 (9.29->10.92), lead ore 1 (9.61->10.64) | +79 |
| Karlmoor | 787 | 0.22 | 0.10 (10/turn) | garments 14 (19.2->22.8), salt 8 (4.81->5.65), dyed yarn 1 (7.98->8.74) | jewellery 1 (56.18->71.72), wool 5 (8.98->11.4), steel ingots 1 (12.92->15.39) | +77 |
| Gottweiler | 1135 | 0.41 | 0.20 (21/turn) | silver bars 1 (247.8->260.3), flour 2 (21->27.74), belts 2 (24.99->27.93), soap 2 (92.4->94.52) | bellows 2 (241.5->256.5), ploughs 1 (56.18->69.83), cheese 15 (6.51->7.41), wool 2 (8.4->11.4) | +76 |

**Best:** Coburgbaum at about +130 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 52 @ min 3.38 |  |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 12 = 7.7 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 20 @ min 20.0 |  |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 264 @ 2.2, stop - |  | uses 714.0/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 264 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 36.8 |  |
| pasties | 3 @ 14.0, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 13 = 4.7 turns |
| porterage | 10 @ 1.1, stop - |  | uses 10.0/turn (observed), makes 0.0, holds 10 = 1.0 turns |
| rope |  | 5 @ min 72.5 | makes 2.2, uses 0.0, holds 35 (keeps 0): sells the surplus + 3/turn of the excess |
| timber |  | 8 @ min 6.5 |  |
| tools | 4 @ 6.2, stop 29 |  | uses 3.6/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 55.3 turns |

## Chain sizing

Mode HOLD, garments sold 21.5/turn (+0.0 exported); plan makes 22.1 garments a turn.
Labour: own 450, everything else 418, chain may buy 350 -> chain allowance 382, chain plan 383 (+4 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.24 | 5.35 |
| ret | 3 | 0.93 | 0.95 |
| spin | 4 | 1.92 | 1.96 |
| weave | 3 | 0.85 | 0.86 |
| sew | 2 | 0.53 | 0.54 |

Buffers: flax fibres 50/72, thread 315/213, cloth 2/86
- chain plan needed 517 labour, budget left 382: cut to 382 (sewing capped at 0.54)

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
