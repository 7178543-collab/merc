# v2 shadow report

Turn 13460, 2026-10-22 05:00. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
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
| labour | 271 | 276 | 721 | 0 | 5 | buy 271, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 18 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 36.6 |
| porterage | 10 | 10 | 10 | 0 | 0 | buy 10, buy @ 1.1 |

**1 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.1 turns (holds 3, next step uses 42/turn) -> v2: check the step that makes it

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.3 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 69
- **flax plants**: flax plants buffer thin: 1.1 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 176

## Notes

- labour: projection runs 75 over real use lately; planning 721, not 796

## Prestige spending, cheapest coin per prestige first

941 turns left: prestige gained now converts 99.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.0 | 48.0 | running |
| hold banquet 4 (pies) | mansion | 18 | 50.2 | 50.2 | thin at home: pasties, wine |
| jousting 3 | arena | 230 | 51.6 | 51.7 | needs a arena (build cost 25,960); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 53.3 | 53.3 | thin at home: wine, ham |
| hold sermon 2 (candles) | church | 31 | 51.0 | 53.5 | needs a church (build cost 66,219); thin at home: jewellery, furniture |
| hold banquet 3 (pies) | mansion | 8 | 53.8 | 53.8 | thin at home: pasties, pies |
| hold banquet 1 (fish) | mansion | 4.2 | 54.1 | 54.1 |  |
| hold feast 2 | townhouse | 2.6 | 51.5 | 54.4 | needs a townhouse (build cost 6,819); thin at home: wine |
| hold banquet 2 (fish) | mansion | 6.8 | 54.6 | 54.6 | thin at home: wine |
| hold banquet 2 (pies) | mansion | 7 | 54.6 | 54.6 | thin at home: pasties, wine, pies |
| hold sermon 2 | church | 24 | 51.6 | 54.8 | needs a church (build cost 66,219); thin at home: jewellery, furniture |
| hold prayer 2 | chapel | 13 | 52.1 | 54.9 | needs a chapel (build cost 32,770); thin at home: furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 120102307 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 10 | 185801747 | 0.036 | garments 9 | - | 69 |

## Ship plans (this turn's world prices)

- **linen snake** on Neuborn: furniture buy 24 @ 13.7, garments sell 10 @ 23.2; crew 0.2; est +313 a turn; stock: furniture 24 @ 13.7 (keep 145)
- **Flax Wyrm** on Rouhomme: nothing pays; crew 0.0; est +0 a turn; best orders clear only -8 a turn after crew: ship stays at 0
- best towns now: Cobholme +508, Hofkirchen +463, Grandgues +449, Brunnham +422, Bordetes +420
- Cobholme would trade: beer sell 56 @ 5.7, furniture buy 38 @ 13.2; crew 1.0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~100 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Boistot | 1230 | 0.44 | 0.20 (20/turn) | plate armour 1 (1044.75->1396.5), leather 1 (24.15->27.17), pies 1 (16.48->17.95) | looms 1 (501.9->698.25), pasties 2 (12.39->18.6), wrought iron 4 (10.82->12.16), fleece 3 (5.25->5.75) | +552 |
| Neuborn | 780 | 0.21 | 0.10 (10/turn) | garments 20 (19.02->23.94), tools 16 (4.72->5.32), wrought iron 4 (13.65->14.15) | looms 1 (474.6->698.25), pasties 2 (13.86->18.6), hop beer 4 (6.98->7.69) | +332 |
| Briclives | 1041 | 0.34 | 0.20 (20/turn) | plate armour 1 (1044.75->1263.5), rope 1 (81.5->129.2) | gold ore 1 (129.15->148.2), pasties 2 (14.49->18.6), butter 1 (49.56->54.15), tools 3 (4.18->5.05) | +287 |
| Clairas | 374 | 0.10 | 0.10 (10/turn) | gold bars 1 (782.25->817), nets 3 (37.6->39.9) | looms 1 (530.25->698.25), pasties 2 (12.29->18.6), cloth 16 (7.72->8.2), grain 26 (2.52->2.82) | +233 |
| Clairlond | 1288 | 0.47 | 0.20 (20/turn) | hides 2 (12.6->15.67), leather 1 (24.15->25.46) | looms 1 (510.3->698.25), gold ore 1 (135.45->148.2), pasties 2 (12.39->18.6), cheese 10 (6.09->7.17) | +213 |

**Best:** Boistot at about +552 coin a turn.

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
| labour | 271 @ 2.2, stop - |  | uses 721.2/turn (brewery 1, flax farm 1, household), makes 450.0, holds 271 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 35.6 |  |
| pasties | 3 @ ?, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 5.0 turns |
| porterage | 10 @ 1.1, stop - |  | uses 10.3/turn (observed), makes 0.0, holds 10 = 1.0 turns |
| rope |  | 2 @ min 79.5 |  |
| timber |  | 8 @ min 6.5 |  |
| tools | 4 @ 6.2, stop 30 |  | uses 3.7/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 53.7 turns |

## Chain sizing

Mode HOLD, garments sold 18.2/turn (+1.6 exported); plan makes 21.3 garments a turn.
Labour: own 450, everything else 403, chain may buy 350 -> chain allowance 397, chain plan 396 (+8 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.54 | 5.76 |
| ret | 3 | 0.98 | 1.02 |
| spin | 4 | 2.03 | 2.11 |
| weave | 3 | 0.86 | 0.84 |
| sew | 2 | 0.53 | 0.52 |

Buffers: flax fibres 45/72, thread 250/211, cloth 3/84
- chain plan needed 551 labour, budget left 397: cut to 397 (sewing capped at 0.52)

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
- R3: net maker152202386007001 (net maker) finished but idle 4 turns (no recipe) (held back: failsafe level 1: reduce-only, would start make nets 1 at 0.5 (storehouse provider))
