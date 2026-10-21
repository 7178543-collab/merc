# v2 shadow report

Turn 13440, 2026-10-21 09:03. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 3,325, prestige 3,601 (931 free, +73.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 52, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 48 | 0 | 2 | 0 | 0 | min_holding 30, sell 20, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 264 | 264 | 714 | 0 | 0 | buy 264, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 15 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 37.4 |
| porterage | 10 | 10 | 10 | 0 | 0 | buy 10, buy @ 1.1 |

**1 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.0 turns (holds 1, next step uses 42/turn) -> v2: check the step that makes it

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.5 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 65
- **flax plants**: flax plants buffer thin: 1.0 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 167
- **timber**: build materials for net maker152202386007001 are in (338.1 held, 54 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **net maker152202386007001** 64% (INITIAL), about 5 turns left; still to deliver: labour 72, timber 54, tools 8; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| timber | 54 | 338.1 | 0 | off: covered; switch v1's buy off |
| tools | 8 | 199.3 | 0 | off: covered |

Labour metered per turn while a site can progress: labour 15

## Notes

- labour: projection runs 92 over real use lately; planning 714, not 806

## Prestige spending, cheapest coin per prestige first

961 turns left: prestige gained now converts 99.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.1 | 50.1 | running |
| hold sermon 2 (candles) | church | 31 | 50.9 | 53.5 | needs a church (build cost 70,636); thin at home: candles |
| hold banquet 3 (pies) | mansion | 8 | 54.4 | 54.4 | thin at home: pasties, hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 55.1 | 55.1 | thin at home: hop beer, wine, pies |
| hold banquet 1 (fish) | mansion | 4.2 | 55.7 | 55.7 |  |
| hold prayer 2 | chapel | 13 | 53.1 | 55.9 | needs a chapel (build cost 32,623) |
| hold sermon 2 | church | 24 | 52.7 | 56.1 | needs a church (build cost 70,636) |
| hold banquet 2 (pies) | mansion | 7 | 57.8 | 57.8 | thin at home: pasties, wine, pies |
| hold mass 1 | cathedral | 180 | 55.9 | 57.8 | needs a cathedral (build cost 282,300); thin at home: jewellery, glassware, candles |
| jousting 3 | arena | 230 | 58.0 | 58.1 | needs a arena (build cost 26,669); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| jousting 1 | arena | 170 | 58.4 | 58.6 | needs a arena (build cost 26,669); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 58.9 | 58.9 | thin at home: hop beer, cured fish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 10 | 120102307 | 0.092 | - | furniture 4 | -57 |
| linen snake | 0.1 / 0.10 | 10 | 185801747 | 0.08 | - | furniture 1 | -14 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Rouhomme: nothing pays; crew 0.0; est +0 a turn; best orders clear only -7 a turn after crew: ship stays at 0
- **linen snake** on Neuborn: nothing pays; crew 0.0; est +0 a turn; best orders clear only -6 a turn after crew: ship stays at 0
- best towns now: Etallaen +44, Karlmoor +38, Orlesailles +32, Bedenis +23, Essenbrucke +23
- Etallaen would trade: garments sell 18 @ 22.6, pasties buy 2 @ 14.4, rope sell 2 @ 82.5; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~103 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Etallaen | 774 | 0.21 | 0.20 (21/turn) | garments 21 (20.2->26.22), rope 2 (74->79.8), light armour 1 (84->92.15), grain 8 (2.62->3.36) | - | +138 |
| Kirchwerp | 1072 | 0.37 | 0.30 (31/turn) | gold ore 1 (129.15->143.45), lathes 1 (168->179.55), wine 8 (7.35->8.5), wrought iron 11 (12.81->13.68) | cheese 39 (6.35->7.98), slaked lime 2 (8.4->11.69), garments 2 (19.32->20.4) | +97 |
| Arnsreuth | 921 | 0.29 | 0.10 (10/turn) | silver bars 1 (201.6->247), gold ore 1 (129.15->165.3), hinges 1 (31.71->38.95), dye 1 (44.1->46.55) | canvas 2 (26.67->29.07), cheese 3 (7.4->7.98) | +96 |
| Caillechâtel | 488 | 0.13 | 0.20 (21/turn) | beer 31 (3.16->5.98), flax fibres 4 (4.87->5.27), malt 1 (5.02->6.17), nets 4 (37.8->38.38) | lead ore 2 (6.14->11.3), canvas 1 (25.83->29.07), axes 1 (14.28->16.05), cloth 14 (7.4->7.6) | +95 |
| Gottweiler | 1135 | 0.40 | 0.20 (21/turn) | silver bars 1 (201.6->281.2), coats 1 (61.43->68.4), nails 10 (5.78->6.55), tools 16 (4.32->4.73) | cheese 19 (7.51->7.98) | +91 |

**Best:** Etallaen at about +138 coin a turn.

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
| pasties | 3 @ 15.8, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 5.0 turns |
| porterage | 10 @ 1.1, stop - |  | uses 10.0/turn (observed), makes 0.0, holds 10 = 1.0 turns |
| rope |  | 5 @ min 72.0 | makes 2.2, uses 0.0, holds 34 (keeps 0): sells the surplus + 3/turn of the excess |
| timber |  | 8 @ min 6.5 |  |
| tools | 4 @ 6.2, stop 29 |  | uses 3.6/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 55.2 turns |

## Chain sizing

Mode HOLD, garments sold 21.0/turn (+0.0 exported); plan makes 21.7 garments a turn.
Labour: own 450, everything else 418, chain may buy 350 -> chain allowance 382, chain plan 382 (+7 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.24 | 5.40 |
| ret | 3 | 0.93 | 0.96 |
| spin | 4 | 1.92 | 1.98 |
| weave | 3 | 0.85 | 0.84 |
| sew | 2 | 0.53 | 0.53 |

Buffers: flax fibres 50/72, thread 294/211, cloth 1/84
- chain plan needed 529 labour, budget left 382: cut to 382 (sewing capped at 0.53)

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
