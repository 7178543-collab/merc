# v2 shadow report

Turn 13430, 2026-10-20 23:50. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 5,211, prestige 3,393 (723 free, -0.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 52, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 53 | 0 | 2 | 0 | 0 | min_holding 30, sell 22, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 264 | 264 | 714 | 0 | 0 | buy 264, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 15 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 37.2 |
| porterage | 10 | 10 | 10 | 0 | 0 | buy 10, buy @ 1.1 |

**1 risks, 0 waste, 4 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.1 turns (holds 4, next step uses 46/turn) -> v2: check the step that makes it

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax fibres**: flax fibres buffer thin: 1.6 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 63
- **flax plants**: flax plants buffer thin: 1.0 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 162
- **timber**: build materials for park 1, net maker152202386007001 are in (261.5 held, 78 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 62% (EXPANSION), about 5 turns left; still to deliver: labour 99, limestone 23, timber 16; ready for labour
- **net maker152202386007001** 59% (INITIAL), about 5 turns left; still to deliver: labour 82, timber 62, tools 9; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 23 | 60.7 | 0 | off: covered |
| timber | 78 | 261.5 | 0 | off: covered; switch v1's buy off |
| tools | 9 | 199.3 | 0 | off: covered |

Labour metered per turn while a site can progress: labour 37

## Notes

- labour: projection runs 92 over real use lately; planning 719, not 811

## Prestige spending, cheapest coin per prestige first

971 turns left: prestige gained now converts 99.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 3 (pies) | mansion | 8 | 53.8 | 53.8 | thin at home: pasties, hop beer, pies |
| maintain 1 | park | 0.5 | 50.4 | 54.4 | running |
| hold banquet 3 (fish) | mansion | 7.6 | 54.9 | 54.9 | thin at home: hop beer, cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 55.0 | 55.0 |  |
| hold sermon 2 (candles) | church | 31 | 52.4 | 55.0 | needs a church (build cost 70,769); thin at home: candles, furniture |
| hold prayer 2 | chapel | 13 | 52.4 | 55.2 | needs a chapel (build cost 33,486); thin at home: furniture |
| hold sermon 2 | church | 24 | 52.7 | 56.0 | needs a church (build cost 70,769); thin at home: furniture |
| hold banquet 3 (meat) | mansion | 7.6 | 57.8 | 57.8 | thin at home: hop beer |
| jousting 3 | arena | 230 | 57.7 | 57.8 | needs a arena (build cost 26,566); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| jousting 1 | arena | 170 | 57.7 | 57.9 | needs a arena (build cost 26,566); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 58.2 | 58.2 | thin at home: hop beer, wine, stockfish |
| hold banquet 2 (fish) | mansion | 6.8 | 58.3 | 58.3 | thin at home: wine, cured fish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 120102307 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 10 | 185801747 | 0.032 | - | furniture 2 | -29 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Rouhomme: nothing pays; crew 0.0; est +0 a turn; stock: furniture 1 @ 14.2 (keep 145); best orders clear only 8 a turn after crew: ship stays at 0
- **linen snake** on Neuborn: nothing pays; crew 0.0; est +0 a turn; stock: furniture 1 @ 14.2 (keep 145); best orders clear only 2 a turn after crew: ship stays at 0
- best towns now: Bordetes +36, Bedenis +32, Clarfranche +31, Disscester +26, Cobholme +22
- Bordetes would trade: furniture buy 1 @ 13.7, rope sell 3 @ 84.5; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~103 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Dortgart | 1045 | 0.35 | 0.10 (10/turn) | plate armour 1 (1606.5->1957), dye 1 (42.84->48.92), glass ingots 2 (47.88->50.82), rope 2 (73->75.52) | jewellery 1 (57.75->74.58), stockfish 1 (113.4->130.15), cheese 11 (6.62->7.03), resin 1 (1.11->1.96) | +397 |
| Bremcop | 1326 | 0.51 | 0.20 (21/turn) | glass ingots 1 (47.88->57.95), nets 4 (38.2->40.85), rope 1 (73->76.95), axes 1 (14.49->15.29) | stockfish 4 (100.28->130.15), yarn 18 (2.31->3.57), gears 1 (57.23->66.5), garments 2 (20.06->20.6) | +156 |
| Kirchwerp | 1072 | 0.37 | 0.20 (21/turn) | tackles 2 (171.15->181.45), tallow 4 (19.43->21.85), dye 1 (42.84->47.31), butter 1 (66.67->69.83) | stockfish 4 (110.25->130.15), cheese 14 (6.2->7.03) | +115 |
| Gotthafen | 964 | 0.31 | 0.10 (10/turn) | glass ingots 2 (47.88->56.05), glassware 2 (62.48->65.55), soap 2 (92.4->95.95), belts 1 (27.09->29.26) | stockfish 3 (115.5->130.15), gears 1 (57.23->66.5), canvas 1 (25.83->30.02), casks 7 (4.94->5.61) | +88 |
| Vauxvais | 204 | 0.06 | 0.10 (10/turn) | medicine 1 (136.5->148.2), cheese 9 (7.88->8.88), cookware 6 (23.52->24.32), grain 8 (2.66->3.17) | limestone 3 (10.5->20), stockfish 1 (116.55->130.15), thread 9 (4.35->4.94), flax fibres 9 (6.04->6.3) | +71 |

**Best:** Dortgart at about +397 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 52 @ min 3.38 |  |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 22 @ min 20.0 |  |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 269 @ 2.2, stop - |  | uses 719.0/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 264 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 37.2 |  |
| pasties | 3 @ 15.3, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 5.0 turns |
| porterage | 10 @ 1.1, stop - |  | uses 9.8/turn (observed), makes 0.0, holds 10 = 1.0 turns |
| rope |  | 4 @ min 71.0 | makes 2.2, uses 0.0, holds 25 (keeps 0): sells the surplus + 2/turn of the excess |
| timber |  | 8 @ min 6.5 |  |
| tools | 4 @ 6.2, stop 29 |  | uses 3.5/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 56.1 turns |

## Chain sizing

Mode HOLD, garments sold 22.7/turn (+0.0 exported); plan makes 22.1 garments a turn.
Labour: own 450, everything else 425, chain may buy 350 -> chain allowance 375, chain plan 375 (-4 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.08 | 5.17 |
| ret | 3 | 0.90 | 0.92 |
| spin | 4 | 1.86 | 1.89 |
| weave | 3 | 0.90 | 0.86 |
| sew | 2 | 0.57 | 0.54 |

Buffers: flax fibres 51/73, thread 357/213, cloth 4/86
- chain plan needed 508 labour, budget left 375: cut to 375 (sewing capped at 0.54)

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
