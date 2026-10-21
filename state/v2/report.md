# v2 shadow report

Turn 13448, 2026-10-21 17:00. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 5,239, prestige 3,590 (920 free, -1.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 193 | 0 | 4 | 0 | 0 | min_holding 60, sell 57, sell @ 3.68 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 44 | 0 | 2 | 0 | 0 | min_holding 30, sell 20, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 264 | 264 | 714 | 0 | 0 | buy 264, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 36.8 |
| porterage | 10 | 10 | 10 | 0 | 0 | buy 10, buy @ 1.1 |

**2 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.0 turns (holds 0, next step uses 42/turn) -> v2: check the step that makes it
- **flax plants**: flax plants buffer 1.0 turns (holds 87, next step uses 87/turn) -> v2: check the step that makes it

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.4 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 68
- **timber**: build materials for net maker152202386007001 are in (350.6 held, 32 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **net maker152202386007001** 79% (INITIAL), about 3 turns left; still to deliver: labour 42, timber 32, tools 5; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| timber | 32 | 350.6 | 0 | off: covered; switch v1's buy off |
| tools | 5 | 199.5 | 0 | off: covered |

Labour metered per turn while a site can progress: labour 14

## Notes

- labour: projection runs 88 over real use lately; planning 714, not 801

## Prestige spending, cheapest coin per prestige first

953 turns left: prestige gained now converts 99.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.0 | 48.0 | running |
| hold banquet 3 (pies) | mansion | 8 | 53.3 | 53.3 | thin at home: pies |
| hold banquet 4 (pies) | mansion | 18 | 53.5 | 53.5 | thin at home: ham |
| hold sermon 2 (candles) | church | 31 | 51.5 | 53.9 | needs a church (build cost 64,535); thin at home: candles, furniture |
| hold sermon 2 | church | 24 | 52.6 | 55.7 | needs a church (build cost 64,535); thin at home: furniture |
| hold prayer 2 | chapel | 13 | 53.1 | 55.8 | needs a chapel (build cost 31,334); thin at home: furniture |
| jousting 3 | arena | 230 | 55.9 | 56.0 | needs a arena (build cost 25,408); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 56.5 | 56.5 | thin at home: pies |
| hold mass 1 | cathedral | 180 | 55.6 | 57.2 | needs a cathedral (build cost 251,710); thin at home: jewellery, glassware, candles |
| hold banquet 4 | mansion | 17.5 | 57.7 | 57.7 | thin at home: ham, stockfish |
| hold banquet 1 (fish) | mansion | 4.2 | 58.4 | 58.4 | thin at home: cured fish |
| jousting 1 | arena | 170 | 58.8 | 59.0 | needs a arena (build cost 25,408); thin at home: protection, light armour, arms; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 120102307 | 0 | - | - | 0 |
| linen snake | 0.3 / 0.00 | 0 | 185801747 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Neuborn: furniture buy 30 @ 13.7, tools buy 3 @ 4.84; crew 0.3; est +353 a turn; stock: furniture 30 @ 13.7 (keep 145)
- **Flax Wyrm** on Rouhomme: nothing pays; crew 0.0; est +0 a turn; best orders clear only -7 a turn after crew: ship stays at 0
- best towns now: Grandgues +407, Etallaen +395, Angefont +365, Bordetes +354, Neuborn +353
- Grandgues would trade: furniture buy 31 @ 13.5, rope sell 2 @ 82.5, tools buy 3 @ 4.68; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~100 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Bordetes | 831 | 0.23 | 0.20 (20/turn) | plate armour 1 (1134->1330), gold ore 1 (126->156.75), limestone 1 (20.89->52.25), cloth 4 (8.66->11.4) | windows 1 (445.2->565.25), candles 1 (73.5->82), stockfish 1 (123.9->129.2), tools 3 (4.47->5.5) | +401 |
| Hofkirchen | 991 | 0.32 | 0.20 (20/turn) | gold ore 2 (126->162.45), plate armour 1 (1134->1187.5), wine 10 (6.41->8.03), dye 1 (36.75->49.4) | windows 1 (466.2->565.25), stockfish 1 (114.45->129.2), candles 1 (73.5->82), spirits 1 (17.32->22.61) | +274 |
| Dortgart | 1045 | 0.34 | 0.20 (20/turn) | dye 1 (36.75->45.98), coats 2 (58.28->60.32), wine 2 (6.41->6.89) | sails 1 (535.5->646), windows 1 (480.9->565.25), stockfish 1 (109.2->129.2), canvas 3 (23.73->29.26) | +258 |
| Kleinburgh | 1440 | 0.56 | 0.40 (40/turn) | lead ore 12 (12.71->17), hinges 1 (31.08->36.1), rope 2 (75->77.9), thread 6 (4.18->5.03) | sails 1 (530.25->646), windows 1 (478.8->565.25), stockfish 1 (113.4->129.2), gears 2 (57.23->62.7) | +257 |
| Herschweig | 775 | 0.21 | 0.10 (10/turn) | coats 2 (58.28->65.08), dye 1 (36.75->47.5), pies 2 (12.6->14.91), wine 3 (6.41->7.22) | windows 1 (378->565.25), stockfish 1 (109.2->129.2), harnesses 3 (58.8->61.27), candles 1 (77.17->82) | +255 |

**Best:** Bordetes at about +401 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 59 @ min 3.38 | makes 56.0, uses 4.2, holds 193 (keeps 60): sells the surplus + 7/turn of the excess |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 12 = 7.7 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 20 @ min 20.0 |  |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 264 @ 2.2, stop - |  | uses 714.0/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 264 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 36.8 |  |
| pasties | 3 @ 15.8, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 4.9 turns |
| porterage | 10 @ 1.1, stop - |  | uses 10.2/turn (observed), makes 0.0, holds 10 = 1.0 turns |
| rope |  | 3 @ min 73.0 |  |
| timber |  | 8 @ min 6.5 |  |
| tools | 4 @ 6.2, stop 30 |  | uses 3.7/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 54.1 turns |

## Chain sizing

Mode HOLD, garments sold 20.0/turn (+0.0 exported); plan makes 21.3 garments a turn.
Labour: own 450, everything else 417, chain may buy 350 -> chain allowance 383, chain plan 383 (+0 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.45 | 5.47 |
| ret | 3 | 0.97 | 0.97 |
| spin | 4 | 2.00 | 2.00 |
| weave | 3 | 0.83 | 0.83 |
| sew | 2 | 0.53 | 0.52 |

Buffers: flax fibres 49/72, thread 273/210, cloth 0/83
- chain plan needed 530 labour, budget left 383: cut to 383 (sewing capped at 0.52)

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
