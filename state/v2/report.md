# v2 shadow report

Turn 13462, 2026-10-22 07:17. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 5,094, prestige 3,572 (902 free, -1.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 134 | 0 | 4 | 0 | 0 | min_holding 60, sell 54, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 59 | 0 | 2 | 0 | 0 | min_holding 30, sell 10, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 284 | 284 | 734 | 12 | 0 | buy 284, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 22 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 35.6 |
| porterage | 11 | 11 | 11 | 0 | 0 | buy 11, buy @ 1.1 |

**1 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.0 turns (holds 0, next step uses 42/turn) -> v2: check the step that makes it

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.3 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 71
- **flax plants**: flax plants buffer thin: 1.0 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 183

## Notes

- labour: projection runs 75 over real use lately; planning 746, not 803

## Prestige spending, cheapest coin per prestige first

939 turns left: prestige gained now converts 99.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 46.8 | 46.8 | running |
| hold banquet 4 (pies) | mansion | 18 | 48.0 | 48.0 | thin at home: pasties, wine |
| hold banquet 3 (pies) | mansion | 8 | 49.7 | 49.7 | thin at home: pasties, pies |
| hold banquet 2 (pies) | mansion | 7 | 50.2 | 50.2 | thin at home: pasties, wine, pies |
| hold sermon 2 (candles) | church | 31 | 49.0 | 51.5 | needs a church (build cost 65,734); thin at home: candles, furniture |
| hold banquet 4 | mansion | 17.5 | 51.7 | 51.7 | thin at home: wine, ham |
| jousting 3 | arena | 230 | 52.3 | 52.4 | needs a arena (build cost 25,807); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 53.8 | 53.8 |  |
| hold feast 2 | townhouse | 2.6 | 51.2 | 54.0 | needs a townhouse (build cost 6,554); thin at home: wine |
| hold banquet 2 (fish) | mansion | 6.8 | 54.2 | 54.2 | thin at home: wine |
| hold sermon 2 | church | 24 | 51.4 | 54.6 | needs a church (build cost 65,734); thin at home: furniture |
| hold prayer 2 | chapel | 13 | 52.0 | 54.8 | needs a chapel (build cost 32,322) |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.20 | 19 | 120102307 | 0.148 | - | furniture 9 | -130 |
| linen snake | 0.2 / 0.20 | 19 | 185801747 | 0 | - | furniture 4 | -57 |

## Ship plans (this turn's world prices)

- **linen snake** on Neuborn: furniture buy 23 @ 14.0, garments sell 22 @ 23.2; crew 0.2; est +320 a turn; stock: furniture 23 @ 14.0 (keep 145)
- **Flax Wyrm** on Rouhomme: nothing pays; crew 0.0; est +0 a turn; best orders clear only -7 a turn after crew: ship stays at 0
- best towns now: Pontmont +328, Etallaen +327, Angefont +323, Grandgues +323, Clairlond +322
- Pontmont would trade: furniture buy 26 @ 13.8, nets sell 3 @ 39.2; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~97 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Bordetes | 831 | 0.22 | 0.10 (10/turn) | plate armour 1 (1044.75->1349), tackles 2 (168->172.9), candles 1 (59.85->66.02), nets 3 (35.2->37.24) | tallow 1 (15.44->16.62), garments 2 (19.95->20.4) | +322 |
| Fontaux | 411 | 0.11 | 0.30 (29/turn) | looms 1 (729.75->883.5), charcoal 13 (1.73->4.31), furniture 11 (11.87->13.39), garments 22 (19.02->19.57) | cloth 9 (7.25->7.55), hop beer 1 (7.25->7.6), pasties 2 (14.07->14.4) | +203 |
| Gosschweig | 1099 | 0.36 | 0.20 (19/turn) | windows 1 (593.25->698.25), lathes 1 (138.6->177.65), leather 1 (24.36->26.6), nets 3 (35.2->36.1) | stockfish 1 (100.8->106.4), canvas 1 (24.36->27.93), pasties 2 (11.76->14.4), garments 2 (19.64->20.4) | +151 |
| Hofkirchen | 991 | 0.31 | 0.20 (19/turn) | plate armour 1 (1044.75->1159), lathes 1 (138.6->152), candles 1 (59.85->68.88), tools 16 (4.52->4.99) | tin ingots 1 (27.3->31.92), flax fibres 16 (5.23->6), garments 2 (19.95->20.4) | +148 |
| Chatgnan | 728 | 0.19 | 0.10 (10/turn) | looms 1 (729.75->878.75), candles 1 (59.85->61.27), nets 2 (35.2->35.91), raw cloth 1 (6.04->6.51) | flax plants 2 (1.21->1.68), iron ore 1 (2.08->3.34) | +144 |

**Best:** Bordetes at about +322 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 54 @ min 3.38 | makes 56.0, uses 4.2, holds 134 (keeps 60): sells the surplus + 2/turn of the excess |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 12 = 7.7 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 10 @ min 20.0 | makes 21.7, uses 2.1, holds 59 (keeps 30): sells the surplus + 2/turn of the excess; ships offer 22 a turn abroad, so home sells 10 (was 22) |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 296 @ 2.2, stop - |  | uses 745.7/turn (brewery 1, flax farm 1, household), makes 450.0, holds 284 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 34.2 |  |
| pasties | 3 @ 15.1, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 13 = 4.8 turns |
| porterage | 11 @ 1.1, stop - |  | uses 10.5/turn (observed), makes 0.0, holds 11 = 1.0 turns |
| rope |  | 2 @ min 78.5 |  |
| timber |  | 8 @ min 6.5 |  |
| tools | 4 @ 6.2, stop 31 |  | uses 3.8/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 52.7 turns |

## Chain sizing

Mode HOLD, garments sold 16.5/turn (+2.3 exported); plan makes 23.0 garments a turn.
Labour: own 450, everything else 403, chain may buy 350 -> chain allowance 397, chain plan 398 (+0 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.76 | 5.54 |
| ret | 3 | 1.02 | 0.98 |
| spin | 4 | 2.11 | 2.03 |
| weave | 3 | 0.84 | 0.90 |
| sew | 2 | 0.53 | 0.56 |

Buffers: flax fibres 45/74, thread 301/217, cloth 0/90
- chain plan needed 548 labour, budget left 397: cut to 397 (sewing capped at 0.56)

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
- R3: net maker152202386007001 (net maker) finished but idle 5 turns (no recipe) (held back: failsafe level 1: reduce-only, would start make nets 1 at 0.5 (storehouse provider))
