# v2 shadow report

Turn 13422, 2026-10-20 15:59. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 7,668, prestige 3,400 (730 free, -2.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 52 | 0 | 4 | 0 | 0 | min_holding 60, sell 52, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 3 | 3 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 62 | 0 | 2 | 0 | 0 | min_holding 30, sell 19, sell @ 20 |
| grain | 104 | 0 | 0 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 251 | 81 | 531 | 158 | 0 | buy 264, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 36.2 |
| porterage | 5 | 10 | 5 | 0 | 5 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 4 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.1 turns (holds 4, next step uses 33/turn) -> v2: check the step that makes it
- **porterage**: buying 5, short of ~10 needed -> v2: buy 10

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax fibres**: flax fibres buffer thin: 1.7 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 61
- **flax plants**: flax plants buffer thin: 1.2 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 158
- **timber**: build materials for park 1, net maker152202386007001 are in (347.6 held, 190 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 0% (EXPANSION), about 12 turns left; still to deliver: labour 260, limestone 60, timber 40; ready for labour
- **net maker152202386007001** 0% (INITIAL), about 12 turns left; still to deliver: labour 200, timber 150, tools 20; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 60 | 100.7 | 0 | off: covered |
| timber | 190 | 347.6 | 0 | off: covered; switch v1's buy off |
| tools | 20 | 199.2 | 0 | off: covered |

Labour metered per turn while a site can progress: labour 39

## Notes

- labour: projection runs 75 over real use lately; planning 701, not 776

## Prestige spending, cheapest coin per prestige first

979 turns left: prestige gained now converts 99.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.6 | 52.0 | running |
| hold prayer 2 | chapel | 13 | 51.5 | 54.1 | needs a chapel (build cost 30,556); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 52.1 | 54.6 | needs a church (build cost 68,879); thin at home: candles, furniture |
| hold banquet 1 (fish) | mansion | 4.2 | 54.8 | 54.8 |  |
| hold sermon 2 | church | 24 | 52.0 | 55.3 | needs a church (build cost 68,879); thin at home: furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 55.6 | 55.6 | thin at home: wine, cured fish |
| hold mass 2 (premium) | cathedral | 360 | 55.1 | 56.0 | needs a cathedral (build cost 277,290); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 2 (pies) | mansion | 7 | 56.5 | 56.5 | thin at home: pasties, wine, pies |
| jousting 1 | arena | 170 | 57.8 | 58.0 | needs a arena (build cost 25,054); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 58.4 | 58.4 | thin at home: wine |
| hold banquet 3 (pies) | mansion | 8 | 58.4 | 58.4 | thin at home: pasties, pies |
| hold banquet 4 (pies) | mansion | 18 | 58.4 | 58.4 | thin at home: wine, pies |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 120102307 | 0.124 | - | - | 0 |
| linen snake | 0.66 / 0.00 | 0 | 185801747 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Neuborn: furniture buy 7 @ 13.7; crew 0.1; est +79 a turn; stock: furniture 7 @ 13.7 (keep 145)
- **Flax Wyrm** on Rouhomme: furniture buy 7 @ 14.2; crew 0.1; est +75 a turn; stock: furniture 7 @ 14.2 (keep 145)
- best towns now: Disscester +105, Birkeningen +98, Bedenis +93, Dortgart +89, Marmont +87
- Disscester would trade: furniture buy 7 @ 12.6, garments sell 17 @ 22.0; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~100 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Etallaen | 774 | 0.21 | 0.10 (10/turn) | cured fish 4 (24.57->33.63), dyed cloth 2 (13.12->18.43), grain 8 (2.52->3.31), nets 2 (37.2->38.19) | plate armour 1 (1249.5->1368), mouldboards 1 (36.33->41.42), pasties 2 (13.76->17), cloth 15 (7.35->7.8) | +184 |
| Blanans | 297 | 0.08 | 0.20 (20/turn) | flax fibres 3 (4.63->5.61), ploughs 1 (78.75->80.75), grain 8 (2.52->2.74) | plate armour 1 (1291.5->1368), cloth 33 (7.46->7.8), limestone 5 (15.23->19.7), jewellery 1 (79.28->84.55) | +102 |
| Fontaux | 411 | 0.11 | 0.10 (10/turn) | cheese 30 (7.3->9.79), leather 1 (20.89->23.94), butter 1 (73.5->76) | mouldboards 1 (30.03->41.42), pasties 2 (11.97->17), slaked lime 1 (8.45->11.21), flax fibres 7 (5.67->5.95) | +94 |
| Amsdermund | 1111 | 0.38 | 0.30 (30/turn) | glassware 3 (63->69.83), leather 1 (20.89->32.49), limestone 1 (20.68->44.46), lead bars 9 (14.07->15.2) | jewellery 2 (73.5->84.55), cheese 29 (5.93->6.55), candles 1 (69.3->74), mouldboards 1 (39.48->41.42) | +89 |
| Corstoft | 1496 | 0.59 | 0.20 (20/turn) | butter 3 (73.5->88.83), tools 14 (4.62->6.03) | stockfish 1 (95.55->102.6), pasties 2 (14.28->17), flax fibres 13 (4.73->5.95) | +62 |

**Best:** Etallaen at about +184 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 52 @ min 3.38 |  |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 19 @ min 20.0 | makes 16.9, uses 2.1, holds 62 (keeps 30): sells the surplus + 4/turn of the excess |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 251 @ 2.2, stop - |  | uses 701.0/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 251 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 36.2 |  |
| pasties | 3 @ 17.8, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 13 = 4.8 turns |
| porterage | 10 @ 1.1, stop - |  | uses 9.7/turn (observed), makes 0.0, holds 5 = 0.5 turns |
| rope |  | 3 @ min 73.5 |  |
| timber |  | 8 @ min 6.5 |  |
| tools | 4 @ 6.2, stop 31 |  | uses 3.8/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 52.4 turns |

## Chain sizing

Mode HOLD, garments sold 8.1/turn (+0.0 exported); plan makes 23.4 garments a turn.
Labour: own 450, everything else 427, chain may buy 350 -> chain allowance 373, chain plan 373 (+40 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.93 | 4.93 |
| ret | 3 | 0.88 | 0.88 |
| spin | 4 | 1.80 | 1.80 |
| weave | 3 | 0.70 | 0.91 |
| sew | 2 | 0.41 | 0.57 |

Buffers: flax fibres 53/74, thread 445/218, cloth 4/91
- chain plan needed 466 labour, budget left 373: cut to 373 (sewing capped at 0.57)

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
- R4: logging camp w/ tool projected 0 of 7 (limited by porterage)
- R7 stale ask: rope ask 76.5 over the market for 4 turns: the town trades ~4 a turn at 75.5, we sold 0 with 11 over what we keep (held back: acted on rope at turn 13421 (one action per 2 turns))
