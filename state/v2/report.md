# v2 shadow report

Turn 13428, 2026-10-20 21:56. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 5,686, prestige 3,395 (725 free, -0.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 52, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 54 | 0 | 2 | 0 | 0 | min_holding 30, sell 22, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 264 | 264 | 714 | 0 | 0 | buy 264, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 37.2 |
| porterage | 10 | 10 | 10 | 0 | 0 | buy 10, buy @ 1.1 |

**1 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.1 turns (holds 5, next step uses 46/turn) -> v2: check the step that makes it

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.6 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 63
- **flax plants**: flax plants buffer thin: 1.0 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 162
- **timber**: build materials for park 1, net maker152202386007001 are in (270.7 held, 85 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 48% (EXPANSION), about 7 turns left; still to deliver: labour 136, limestone 32, timber 21; ready for labour
- **net maker152202386007001** 58% (INITIAL), about 6 turns left; still to deliver: labour 85, timber 64, tools 9; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 32 | 70.7 | 0 | off: covered |
| timber | 85 | 270.7 | 0 | off: covered; switch v1's buy off |
| tools | 9 | 199.4 | 0 | off: covered |

Labour metered per turn while a site can progress: labour 35

## Notes

- labour: projection runs 88 over real use lately; planning 717, not 806

## Prestige spending, cheapest coin per prestige first

973 turns left: prestige gained now converts 99.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 3 (pies) | mansion | 8 | 53.8 | 53.8 | thin at home: pasties, hop beer, pies |
| maintain 1 | park | 0.5 | 49.8 | 53.9 | running |
| hold banquet 3 (fish) | mansion | 7.6 | 54.6 | 54.6 | thin at home: hop beer, cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 55.3 | 55.3 |  |
| hold sermon 2 (candles) | church | 31 | 52.8 | 55.4 | needs a church (build cost 71,886); thin at home: furniture |
| hold prayer 2 | chapel | 13 | 52.6 | 55.5 | needs a chapel (build cost 33,878); thin at home: furniture |
| hold sermon 2 | church | 24 | 52.9 | 56.3 | needs a church (build cost 71,886); thin at home: furniture |
| hold banquet 3 (meat) | mansion | 7.6 | 57.5 | 57.5 | thin at home: hop beer |
| jousting 3 | arena | 230 | 57.4 | 57.6 | needs a arena (build cost 26,887); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 57.7 | 57.7 | thin at home: wine, cured fish |
| jousting 1 | arena | 170 | 58.1 | 58.2 | needs a arena (build cost 26,887); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 58.3 | 58.3 | thin at home: pasties, wine, pies |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 120102307 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 185801747 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Rouhomme: furniture buy 2 @ 14.2, rope sell 2 @ 76.5; crew 0.1; est +21 a turn; stock: furniture 2 @ 14.2 (keep 145)
- **linen snake** on Neuborn: nothing pays; crew 0.0; est +0 a turn; stock: furniture 2 @ 14.6 (keep 145); best orders clear only 13 a turn after crew: ship stays at 0
- best towns now: Bordetes +49, Disscester +48, Bremcop +43, Bedenis +43, Clarfranche +41
- Bordetes would trade: furniture buy 2 @ 13.7, rope sell 3 @ 84.5; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~102 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Caillechâtel | 488 | 0.13 | 0.20 (20/turn) | beer 44 (3.14->5.84), spirits 1 (20.16->27.36) | lead ore 3 (7.56->11.02), flour 2 (13.23->15.11), cloth 16 (7.35->7.55), grain 26 (2.5->2.8) | +127 |
| Herschweig | 775 | 0.21 | 0.10 (10/turn) | tools 10 (4.72->5.08) | spinning wheels 1 (206.85->266), bellows 1 (210->229.9), stockfish 1 (112.35->122.55), cheese 5 (5.72->6.93) | +92 |
| Dortgart | 1045 | 0.35 | 0.10 (10/turn) | glass ingots 2 (49.98->55.1), dye 1 (44.94->48.92), rope 2 (73->75.52), axes 1 (15.12->16.53) | spinning wheels 1 (231->266), jewellery 2 (60.9->75.05), stockfish 1 (113.4->122.55), tackles 1 (161.7->165.3) | +89 |
| Fontaux | 411 | 0.11 | 0.20 (20/turn) | grindstones 1 (327.6->364.8), casks 3 (5.93->9.5), charcoal 12 (2.02->3.21), axes 1 (15.12->15.96) | spinning wheels 1 (224.7->266), slaked lime 1 (7.51->9.45) | +88 |
| Amsdermund | 1111 | 0.39 | 0.60 (61/turn) | beer 51 (3.14->4.39), dye 1 (44.94->52.72), limestone 1 (20.89->38.76), axes 1 (15.12->15.67) | spinning wheels 1 (231->266), ploughs 1 (55.12->65.08), cheese 12 (6.09->6.93), candles 1 (69.3->73) | +80 |

**Best:** Caillechâtel at about +127 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 52 @ min 3.38 |  |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 22 @ min 20.0 |  |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 267 @ 2.2, stop - |  | uses 717.3/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 264 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 37.2 |  |
| pasties | 3 @ 15.6, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 4.9 turns |
| porterage | 10 @ 1.1, stop - |  | uses 9.8/turn (observed), makes 0.0, holds 10 = 1.0 turns |
| rope |  | 4 @ min 71.0 | makes 2.2, uses 0.0, holds 22 (keeps 0): sells the surplus + 2/turn of the excess |
| timber |  | 8 @ min 6.7 |  |
| tools | 6 @ 6.2, stop 45 |  | uses 5.5/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 35.9 turns |

## Chain sizing

Mode HOLD, garments sold 19.0/turn (+0.0 exported); plan makes 22.6 garments a turn.
Labour: own 450, everything else 423, chain may buy 350 -> chain allowance 377, chain plan 377 (-1 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.08 | 5.14 |
| ret | 3 | 0.90 | 0.91 |
| spin | 4 | 1.86 | 1.88 |
| weave | 3 | 0.90 | 0.88 |
| sew | 2 | 0.57 | 0.55 |

Buffers: flax fibres 52/73, thread 379/215, cloth 5/88
- chain plan needed 498 labour, budget left 377: cut to 377 (sewing capped at 0.55)

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
