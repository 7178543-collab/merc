# v2 shadow report

Turn 13452, 2026-10-21 21:58. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 6,423, prestige 3,585 (915 free, -1.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 168 | 0 | 4 | 0 | 0 | min_holding 60, sell 57, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 40 | 0 | 2 | 0 | 0 | min_holding 30, sell 20, sell @ 20.2 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 275 | 264 | 714 | 0 | 0 | buy 275, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 37.2 |
| porterage | 10 | 10 | 10 | 0 | 0 | buy 10, buy @ 1.1 |

**2 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.0 turns (holds 0, next step uses 42/turn) -> v2: check the step that makes it
- **flax plants**: flax plants buffer 1.0 turns (holds 87, next step uses 87/turn) -> v2: check the step that makes it

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax fibres**: flax fibres buffer thin: 1.4 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 68
- **timber**: build materials for net maker152202386007001 are in (350.7 held, 17 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **net maker152202386007001** 89% (INITIAL), about 2 turns left; still to deliver: labour 22, timber 17, tools 3; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| timber | 17 | 350.7 | 0 | off: covered; switch v1's buy off |
| tools | 3 | 199.0 | 0 | off: covered |

Labour metered per turn while a site can progress: labour 11

## Notes

- labour: projection runs 87 over real use lately; planning 714, not 801

## Prestige spending, cheapest coin per prestige first

949 turns left: prestige gained now converts 99.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.1 | 47.1 | running |
| hold banquet 4 (pies) | mansion | 18 | 49.5 | 49.5 | thin at home: pasties, pies |
| hold banquet 3 (pies) | mansion | 8 | 49.9 | 49.9 | thin at home: pasties, pies |
| hold banquet 2 (pies) | mansion | 7 | 51.5 | 51.5 | thin at home: pasties, pies |
| hold banquet 4 | mansion | 17.5 | 53.4 | 53.4 | thin at home: ham |
| hold sermon 2 (candles) | church | 31 | 52.3 | 54.6 | needs a church (build cost 62,650); thin at home: candles, furniture |
| hold prayer 2 | chapel | 13 | 52.2 | 55.0 | needs a chapel (build cost 31,722); thin at home: furniture |
| hold sermon 2 | church | 24 | 52.9 | 56.0 | needs a church (build cost 62,650); thin at home: furniture |
| hold banquet 1 (fish) | mansion | 4.2 | 57.0 | 57.0 |  |
| jousting 3 | arena | 230 | 57.2 | 57.3 | needs a arena (build cost 25,100); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 58.2 | 58.2 |  |
| hold banquet 1 (meat) | mansion | 4.2 | 58.4 | 58.4 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 120102307 | 0 | - | - | 0 |
| linen snake | 0.2 / 0.00 | 0 | 185801747 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Neuborn: furniture buy 20 @ 13.7; crew 0.2; est +234 a turn; stock: furniture 20 @ 13.7 (keep 145)
- **Flax Wyrm** on Rouhomme: nothing pays; crew 0.0; est +0 a turn
- best towns now: Grandgues +484, Etallaen +462, Fulkirch +432, Bordetes +430, Hofkirchen +426
- Grandgues would trade: furniture buy 38 @ 13.4; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~99 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Briclives | 1041 | 0.34 | 0.20 (20/turn) | tapestries 2 (619.5->1197), gold ore 1 (129.15->138.7), cheese 9 (8.24->9.26), pasties 1 (12.1->14.72) | candles 1 (77.17->85.5), fleece 2 (5.1->5.65) | +1171 |
| Hofkirchen | 991 | 0.31 | 0.20 (20/turn) | plate armour 1 (1044.75->1187.5), gold ore 1 (129.15->157.7), ham 1 (57.75->67.45), wine 5 (6.3->7.46) | medicine 2 (126->141.55), candles 1 (74.55->85.5), cloth 8 (7.98->8.5), hinges 2 (29.4->30.78) | +227 |
| Marmont | 638 | 0.17 | 0.30 (30/turn) | beer 60 (3.22->4.5), gold ore 1 (129.15->186.2), yarn 6 (4.56->6.65), malt 2 (7.4->12.73) | medicine 1 (116.55->141.55), copper ore 3 (18.59->22.61), candles 1 (76.12->85.5), herbs 1 (24.99->32.3) | +190 |
| Chribruck | 1202 | 0.42 | 0.10 (10/turn) | windows 1 (506.1->608), wine 11 (6.3->7.12) | medicine 1 (98.7->141.55), candles 1 (71.92->85.5), cloth 13 (7.88->8.5) | +162 |
| Corstoft | 1496 | 0.58 | 0.20 (20/turn) | lathes 1 (127.05->182.4), rope 2 (77.5->102.6), gold ore 1 (129.15->173.85), pies 1 (11.97->13.96) | medicine 1 (119.7->141.55), pasties 2 (11.55->13.3) | +161 |

**Best:** Briclives at about +1171 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 57 @ min 3.38 | makes 56.0, uses 4.2, holds 168 (keeps 60): sells the surplus + 5/turn of the excess |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 12 = 7.7 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 20 @ min 20.0 |  |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 264 @ 2.2, stop - |  | uses 714.0/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 275 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 37.0 |  |
| pasties | 3 @ 13.9, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 13 = 4.8 turns |
| porterage | 10 @ 1.1, stop - |  | uses 10.2/turn (observed), makes 0.0, holds 10 = 1.0 turns |
| rope |  | 2 @ min 75.5 |  |
| timber |  | 8 @ min 6.9 |  |
| tools | 4 @ 6.2, stop 30 |  | uses 3.7/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 53.9 turns |

## Chain sizing

Mode HOLD, garments sold 20.0/turn (+0.0 exported); plan makes 21.3 garments a turn.
Labour: own 450, everything else 414, chain may buy 350 -> chain allowance 386, chain plan 386 (+4 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.45 | 5.55 |
| ret | 3 | 0.97 | 0.99 |
| spin | 4 | 2.00 | 2.03 |
| weave | 3 | 0.83 | 0.83 |
| sew | 2 | 0.53 | 0.52 |

Buffers: flax fibres 48/71, thread 253/210, cloth 0/83
- chain plan needed 532 labour, budget left 386: cut to 386 (sewing capped at 0.52)

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
