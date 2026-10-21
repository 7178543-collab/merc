# v2 shadow report

Turn 13433, 2026-10-21 02:58. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 3,651, prestige 3,515 (845 free, +123.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 52, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 51 | 0 | 2 | 0 | 0 | min_holding 30, sell 20, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 264 | 264 | 714 | 0 | 0 | buy 264, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 37.4 |
| porterage | 10 | 10 | 10 | 0 | 0 | buy 10, buy @ 1.1 |

**1 risks, 0 waste, 4 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.1 turns (holds 3, next step uses 42/turn) -> v2: check the step that makes it

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax fibres**: flax fibres buffer thin: 1.6 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 65
- **flax plants**: flax plants buffer thin: 1.0 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 167
- **timber**: build materials for park 1, net maker152202386007001 are in (279.6 held, 69 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 85% (EXPANSION), about 2 turns left; still to deliver: labour 40, limestone 10, timber 7; ready for labour
- **net maker152202386007001** 59% (INITIAL), about 5 turns left; still to deliver: labour 82, timber 62, tools 9; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 10 | 60.7 | 0 | off: covered |
| timber | 69 | 279.6 | 0 | off: covered; switch v1's buy off |
| tools | 9 | 199.6 | 0 | off: covered |

Labour metered per turn while a site can progress: labour 37

## Notes

- labour: projection runs 96 over real use lately; planning 716, not 813

## Prestige spending, cheapest coin per prestige first

968 turns left: prestige gained now converts 99.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 3 (pies) | mansion | 8 | 52.6 | 52.6 | thin at home: hop beer |
| hold sermon 2 (candles) | church | 31 | 51.4 | 54.0 | needs a church (build cost 71,166); thin at home: furniture |
| hold banquet 1 (fish) | mansion | 4.2 | 54.3 | 54.3 |  |
| hold banquet 4 (pies) | mansion | 18 | 54.8 | 54.8 | thin at home: hop beer, wine |
| maintain 1 | park | 0.5 | 51.0 | 55.0 | running |
| hold banquet 3 (fish) | mansion | 7.6 | 55.5 | 55.5 | thin at home: hop beer, cured fish |
| hold prayer 2 | chapel | 13 | 52.8 | 55.7 | needs a chapel (build cost 34,214); thin at home: furniture |
| hold sermon 2 | church | 24 | 52.6 | 56.0 | needs a church (build cost 71,166); thin at home: furniture |
| hold banquet 2 (pies) | mansion | 7 | 57.9 | 57.9 | thin at home: wine |
| hold mass 1 | cathedral | 180 | 56.1 | 58.0 | needs a cathedral (build cost 284,740); thin at home: jewellery, glassware, candles |
| jousting 3 | arena | 230 | 57.9 | 58.0 | needs a arena (build cost 26,966); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (meat) | mansion | 7.6 | 58.8 | 58.8 | thin at home: hop beer |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 10 | 120102307 | 0.092 | - | candles 4, furniture 4 | -345 |
| linen snake | 0.1 / 0.10 | 10 | 185801747 | 0.08 | - | candles 4, furniture 1 | -300 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Rouhomme: nothing pays; crew 0.0; est +0 a turn; best orders clear only -9 a turn after crew: ship stays at 0
- **linen snake** on Neuborn: nothing pays; crew 0.0; est +0 a turn
- best towns now: Karlmoor +27, Bedenis +16
- Karlmoor would trade: garments sell 13 @ 22.2, rope sell 1 @ 89.0; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~104 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Caillechâtel | 488 | 0.14 | 0.20 (21/turn) | beer 34 (3.18->6.37), jewellery 1 (79.28->82.17), flax fibres 4 (4.92->5.27), malt 1 (5.83->6.27) | yarn 16 (4.85->6.27), butter 2 (52.08->60.32), spirits 1 (17.32->26.6), grain 26 (2.48->2.96) | +158 |
| Hanstein | 380 | 0.11 | 0.30 (31/turn) | windows 1 (540.75->608), glass ingots 1 (44.73->50.82), rope 2 (75->76.47), honey 4 (8.87->9.36) | jewellery 2 (53.55->71.25), yarn 15 (4.68->6.27), spirits 1 (20.27->26.6), canvas 2 (27.09->29.26) | +157 |
| Neuborn | 780 | 0.22 | 0.30 (31/turn) | coats 1 (54.08->67.92), beer 51 (3.18->3.84), seeds 8 (1.78->3.32), glass ingots 1 (44.73->49.88) | cured meat 19 (21.21->24.51), spirits 1 (18.69->26.6), yarn 3 (4.94->6.27), resin 1 (1.47->1.99) | +105 |
| Disscester | 1474 | 0.60 | 0.10 (10/turn) | soap 1 (92.4->151.05), rope 3 (75->78.85), coats 1 (54.08->60.32), nets 2 (38.4->41.99) | spirits 1 (23.1->26.6), yarn 3 (5.08->6.27) | +85 |
| Bordetes | 831 | 0.24 | 0.20 (21/turn) | cheese 40 (8.09->9.4), dye 1 (40.11->47.97), glass ingots 1 (44.73->48.45), leather 2 (24.36->26.22) | wine 16 (5.62->6.46), yarn 2 (5.12->6.27), nails 11 (5.02->5.37), tools 3 (4.47->5.15) | +79 |

**Best:** Caillechâtel at about +158 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 28.6, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 52 @ min 3.38 |  |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 11 = 7.3 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 20 @ min 20.0 |  |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 266 @ 2.2, stop - |  | uses 716.2/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 264 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 37.4 |  |
| pasties | 3 @ 13.8, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 4.9 turns |
| porterage | 10 @ 1.1, stop - |  | uses 10.0/turn (observed), makes 0.0, holds 10 = 1.0 turns |
| rope |  | 5 @ min 73.0 | makes 2.2, uses 0.0, holds 31 (keeps 0): sells the surplus + 2/turn of the excess |
| timber |  | 8 @ min 6.5 |  |
| tools | 4 @ 6.2, stop 29 |  | uses 3.6/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 55.3 turns |

## Chain sizing

Mode HOLD, garments sold 20.7/turn (+0.0 exported); plan makes 21.7 garments a turn.
Labour: own 450, everything else 425, chain may buy 350 -> chain allowance 375, chain plan 376 (+0 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.24 | 5.24 |
| ret | 3 | 0.93 | 0.93 |
| spin | 4 | 1.92 | 1.92 |
| weave | 3 | 0.85 | 0.85 |
| sew | 2 | 0.53 | 0.53 |

Buffers: flax fibres 51/72, thread 331/212, cloth 3/85
- chain plan needed 512 labour, budget left 375: cut to 375 (sewing capped at 0.53)

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
