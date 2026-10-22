# v2 shadow report

Turn 13460, 2026-10-22 05:57. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 6,278, prestige 3,574 (904 free, -1.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 139 | 0 | 4 | 0 | 0 | min_holding 60, sell 54, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 40 | 0 | 2 | 0 | 0 | min_holding 30, sell 10, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 271 | 276 | 721 | 0 | 5 | buy 279, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 18 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 35.6 |
| porterage | 10 | 10 | 10 | 0 | 0 | buy 10, buy @ 1.1 |

**1 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.1 turns (holds 3, next step uses 42/turn) -> v2: check the step that makes it

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax fibres**: flax fibres buffer thin: 1.3 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 71
- **flax plants**: flax plants buffer thin: 1.0 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 183

## Notes

- labour: projection runs 75 over real use lately; planning 734, not 809

## Prestige spending, cheapest coin per prestige first

941 turns left: prestige gained now converts 99.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.0 | 48.0 | running |
| hold banquet 4 (pies) | mansion | 18 | 50.1 | 50.1 | thin at home: pasties, wine |
| jousting 3 | arena | 230 | 51.6 | 51.7 | needs a arena (build cost 25,960); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 53.2 | 53.2 | thin at home: wine, ham |
| hold sermon 2 (candles) | church | 31 | 51.2 | 53.7 | needs a church (build cost 65,939); thin at home: jewellery, furniture |
| hold banquet 3 (pies) | mansion | 8 | 53.8 | 53.8 | thin at home: pasties, pies |
| hold banquet 1 (fish) | mansion | 4.2 | 54.1 | 54.1 |  |
| hold feast 2 | townhouse | 2.6 | 51.5 | 54.4 | needs a townhouse (build cost 6,834); thin at home: wine |
| hold banquet 2 (fish) | mansion | 6.8 | 54.6 | 54.6 | thin at home: wine |
| hold banquet 2 (pies) | mansion | 7 | 54.6 | 54.6 | thin at home: pasties, wine, pies |
| hold sermon 2 | church | 24 | 51.9 | 55.1 | needs a church (build cost 65,939); thin at home: jewellery, furniture |
| hold prayer 2 | chapel | 13 | 52.3 | 55.2 | needs a chapel (build cost 32,860); thin at home: furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 120102307 | 0 | - | - | 0 |
| linen snake | 0.2 / 0.10 | 10 | 185801747 | 0.384 | garments 9 | - | 69 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Rouhomme: furniture buy 35 @ 14.2, tools buy 3 @ 4.38; crew 0.2; est +409 a turn; stock: furniture 35 @ 14.2 (keep 145)
- **linen snake** on Neuborn: furniture buy 23 @ 14.2, garments sell 10 @ 23.8; crew 0.2; est +295 a turn; stock: furniture 23 @ 14.2 (keep 145)
- best towns now: Hofkirchen +463, Angefont +454, Grandgues +448, Bordetes +417, Rouhomme +409
- Hofkirchen would trade: furniture buy 38 @ 12.9; crew 0.5

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~100 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Rouhomme | 368 | 0.10 | 0.70 (70/turn) | plate armour 1 (1044.75->1567.5), bread 141 (2.18->2.64), nets 1 (16.3->37.43), beer 58 (3.2->3.59) | windows 1 (464.1->503.5), cheese 17 (6.88->7.31), hinges 1 (30.03->31.35), spirits 1 (17.22->18.24) | +634 |
| Chribruck | 1202 | 0.43 | 0.10 (10/turn) | plate armour 1 (1044.75->1330), nets 2 (16.3->38), leather 1 (24.36->28.69) | spinning wheels 1 (200.55->224.2), dye 1 (47.46->49.88), cheese 9 (6.83->7.31), spirits 1 (17.43->18.24) | +352 |
| Kirchwerp | 1072 | 0.36 | 0.40 (40/turn) | nets 8 (16.3->36.86), windows 1 (603.75->693.5), plate armour 1 (1044.75->1111.5), wine 7 (5.41->6.65) | - | +320 |
| Corstoft | 1496 | 0.58 | 0.30 (30/turn) | nets 9 (16.3->34.77) | windows 1 (392.7->503.5), flax fibres 8 (4.51->5.95), thread 21 (4.12->4.72) | +266 |
| Heilegg | 826 | 0.23 | 0.20 (20/turn) | nets 7 (16.3->36.86), plate armour 1 (1044.75->1149.5), grindstones 1 (279.3->296.4), lead ore 1 (13.55->16.91) | cheese 36 (7.09->7.31), flax plants 1 (0.99->1.68), tools 3 (4.75->5.1) | +259 |

**Best:** Rouhomme at about +634 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 54 @ min 3.38 | makes 56.0, uses 4.2, holds 139 (keeps 60): sells the surplus + 2/turn of the excess |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 12 = 7.7 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 10 @ min 20.0 | sell; ships offer 10 a turn abroad, so home sells 10 (was 20) |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 284 @ 2.2, stop - |  | uses 733.9/turn (brewery 1, flax farm 1, household), makes 450.0, holds 271 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 35.6 |  |
| pasties | 3 @ ?, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 5.0 turns |
| porterage | 11 @ 1.1, stop - |  | uses 10.5/turn (observed), makes 0.0, holds 10 = 1.0 turns |
| rope |  | 2 @ min 79.5 |  |
| timber |  | 8 @ min 6.5 |  |
| tools | 4 @ 6.2, stop 31 |  | uses 3.8/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 52.6 turns |

## Chain sizing

Mode HOLD, garments sold 17.3/turn (+2.3 exported); plan makes 21.3 garments a turn.
Labour: own 450, everything else 403, chain may buy 350 -> chain allowance 397, chain plan 396 (+0 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.76 | 5.76 |
| ret | 3 | 1.02 | 1.02 |
| spin | 4 | 2.11 | 2.11 |
| weave | 3 | 0.84 | 0.84 |
| sew | 2 | 0.53 | 0.52 |

Buffers: flax fibres 45/72, thread 250/211, cloth 3/84
- chain plan needed 560 labour, budget left 397: cut to 397 (sewing capped at 0.52)

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
- R3: net maker152202386007001 (net maker) finished but idle 4 turns (no recipe) (held back: failsafe level 1: reduce-only, would start make nets 1 at 0.5 (storehouse provider))
