# v2 shadow report

Turn 13459, 2026-10-22 04:01. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 6,213, prestige 3,575 (905 free, -1.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 141 | 0 | 4 | 0 | 0 | min_holding 60, sell 55, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 39 | 0 | 2 | 0 | 0 | min_holding 30, sell 10, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 276 | 276 | 721 | 0 | 5 | buy 276, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 36.8 |
| porterage | 10 | 10 | 10 | 0 | 0 | buy 10, buy @ 1.1 |

**1 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.0 turns (holds 2, next step uses 42/turn) -> v2: check the step that makes it

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.3 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 69
- **flax plants**: flax plants buffer thin: 1.1 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 176

## Notes

- labour: projection runs 87 over real use lately; planning 721, not 796

## Prestige spending, cheapest coin per prestige first

942 turns left: prestige gained now converts 99.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.0 | 48.0 | running |
| hold banquet 4 (pies) | mansion | 18 | 50.4 | 50.4 | thin at home: pasties, pies |
| jousting 3 | arena | 230 | 51.9 | 52.0 | needs a arena (build cost 26,024); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 53.3 | 53.3 | thin at home: ham |
| hold sermon 2 (candles) | church | 31 | 51.3 | 53.9 | needs a church (build cost 66,545); thin at home: jewellery, candles, furniture |
| hold feast 2 | townhouse | 2.6 | 51.5 | 54.4 | needs a townhouse (build cost 6,847); thin at home: wine |
| hold banquet 3 (pies) | mansion | 8 | 54.9 | 54.9 | thin at home: pasties, pies |
| hold sermon 2 | church | 24 | 51.8 | 55.1 | needs a church (build cost 66,545); thin at home: jewellery, furniture |
| hold prayer 2 | chapel | 13 | 52.3 | 55.2 | needs a chapel (build cost 32,782); thin at home: furniture |
| hold banquet 2 (pies) | mansion | 7 | 55.7 | 55.7 | thin at home: pasties, pies |
| hold banquet 1 (fish) | mansion | 4.2 | 56.2 | 56.2 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 56.2 | 56.2 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 120102307 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 10 | 185801747 | 0.04 | garments 10 | - | 61 |

## Ship plans (this turn's world prices)

- **linen snake** on Neuborn: garments sell 9 @ 22.8, pasties buy 3 @ 13.7; crew 0.1; est +28 a turn; stock: pasties 3 @ 13.7 (keep 14)
- **Flax Wyrm** on Rouhomme: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 14.1 (keep 14); best orders clear only 4 a turn after crew: ship stays at 0
- best towns now: Hofkirchen +467, Grandgues +447, Bordetes +417, Heilegg +397, Cobholme +388
- Hofkirchen would trade: furniture buy 38 @ 12.8; crew 0.5

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~100 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Bedenis | 566 | 0.15 | 0.10 (10/turn) | plate armour 1 (1044.75->1605.5), rope 2 (81.5->82.65) | windows 1 (472.5->522.5), lead bars 4 (13.97->15.67), pasties 2 (15.54->18.3), coats 1 (59.33->63.65) | +627 |
| Fontaux | 411 | 0.11 | 0.40 (40/turn) | grindstones 1 (281.4->457.9), charcoal 14 (1.74->3.61), lathes 1 (108.15->119.7), garments 20 (18.99->19.38) | windows 1 (428.4->522.5), cheese 11 (6.2->6.89), pasties 1 (15.23->18.3) | +310 |
| Hofkirchen | 991 | 0.32 | 0.20 (20/turn) | plate armour 1 (1044.75->1320.5), wine 7 (5.41->6.65), gears 1 (53.55->56.05), thread 14 (4.66->5.13) | pasties 2 (13.55->18.3), windows 1 (516.6->522.5), tar 3 (10.29->11.02) | +296 |
| Neuborn | 780 | 0.21 | 0.20 (20/turn) | garments 20 (18.99->23.56), lathes 1 (108.15->116.85), wrought iron 4 (13.02->14.15), flax fibres 1 (5.05->7.31) | windows 1 (468.3->522.5), gold ore 1 (128.1->147.25), pasties 2 (14.18->18.3), coats 1 (57.23->63.65) | +185 |
| Arnsreuth | 921 | 0.28 | 0.30 (30/turn) | tapestries 1 (908.25->1007), lathes 1 (108.15->150.1), yarn 2 (3.7->4.71), wine 1 (5.41->6.03) | windows 1 (504->522.5), coats 1 (52.08->63.65), cloth 36 (7.67->8.2), pasties 2 (14.07->18.3) | +179 |

**Best:** Bedenis at about +627 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 54 @ min 3.38 | makes 56.0, uses 4.2, holds 141 (keeps 60): sells the surplus + 2/turn of the excess |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 10 @ min 20.0 | sell; ships offer 9 a turn abroad, so home sells 10 (was 20) |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 271 @ 2.2, stop - |  | uses 721.2/turn (brewery 1, flax farm 1, household), makes 450.0, holds 276 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 36.6 |  |
| pasties | 4 @ 19.5, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 11 = 3.9 turns |
| porterage | 10 @ 1.1, stop - |  | uses 10.3/turn (observed), makes 0.0, holds 10 = 1.0 turns |
| rope |  | 2 @ min 79.5 |  |
| timber |  | 8 @ min 6.5 |  |
| tools | 4 @ 6.2, stop 30 |  | uses 3.7/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 53.9 turns |

## Chain sizing

Mode HOLD, garments sold 19.0/turn (+0.8 exported); plan makes 21.7 garments a turn.
Labour: own 450, everything else 403, chain may buy 350 -> chain allowance 397, chain plan 393 (+3 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.54 | 5.61 |
| ret | 3 | 0.98 | 1.00 |
| spin | 4 | 2.03 | 2.05 |
| weave | 3 | 0.86 | 0.86 |
| sew | 2 | 0.53 | 0.53 |

Buffers: flax fibres 45/72, thread 255/213, cloth 2/86
- chain plan needed 542 labour, budget left 397: cut to 393 (sewing capped at 0.53)

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
- R3: net maker152202386007001 (net maker) finished but idle 3 turns (no recipe) (held back: failsafe level 1: reduce-only, would start make nets 1 at 0.5 (storehouse provider))
