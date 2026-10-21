# v2 shadow report

Turn 13435, 2026-10-21 04:58. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 3,277, prestige 3,512 (842 free, -1.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 52, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 50 | 0 | 2 | 0 | 0 | min_holding 30, sell 20, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 264 | 264 | 714 | 0 | 0 | buy 264, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 15 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 37.4 |
| porterage | 10 | 10 | 10 | 0 | 0 | buy 10, buy @ 1.1 |

**1 risks, 1 waste, 4 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.0 turns (holds 2, next step uses 42/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **linen snake**: linen snake cost 10 coin last turn (crew 0.10) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax fibres**: flax fibres buffer thin: 1.5 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 65
- **flax plants**: flax plants buffer thin: 1.0 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 167
- **timber**: build materials for park 1, net maker152202386007001 are in (296.3 held, 64 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 96% (EXPANSION), about 1 turns left; still to deliver: labour 11, limestone 3, timber 2; ready for labour
- **net maker152202386007001** 59% (INITIAL), about 5 turns left; still to deliver: labour 82, timber 62, tools 9; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 3 | 60.7 | 0 | off: covered |
| timber | 64 | 296.3 | 0 | off: covered; switch v1's buy off |
| tools | 9 | 199.4 | 0 | off: covered |

Labour metered per turn while a site can progress: labour 28

## Notes

- labour: projection runs 96 over real use lately; planning 714, not 798

## Prestige spending, cheapest coin per prestige first

966 turns left: prestige gained now converts 99.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 3 (pies) | mansion | 8 | 52.9 | 52.9 | thin at home: hop beer |
| hold sermon 2 (candles) | church | 31 | 51.6 | 54.2 | needs a church (build cost 70,888); thin at home: jewellery, candles, furniture |
| hold banquet 1 (fish) | mansion | 4.2 | 54.4 | 54.4 |  |
| maintain 1 | park | 0.5 | 50.7 | 54.7 | running |
| hold banquet 4 (pies) | mansion | 18 | 55.6 | 55.6 | thin at home: hop beer, wine |
| hold prayer 2 | chapel | 13 | 53.2 | 56.0 | needs a chapel (build cost 33,430); thin at home: furniture |
| hold banquet 3 (fish) | mansion | 7.6 | 56.1 | 56.1 | thin at home: hop beer, cured fish |
| hold sermon 2 | church | 24 | 52.9 | 56.3 | needs a church (build cost 70,888); thin at home: jewellery, furniture |
| hold mass 1 | cathedral | 180 | 56.2 | 58.0 | needs a cathedral (build cost 284,135); thin at home: jewellery, glassware, candles |
| hold banquet 2 (pies) | mansion | 7 | 58.1 | 58.1 | thin at home: wine |
| jousting 3 | arena | 230 | 58.4 | 58.5 | needs a arena (build cost 26,743); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (meat) | mansion | 7.6 | 59.0 | 59.0 | thin at home: hop beer |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 10 | 120102307 | 0.092 | - | furniture 1 | -14 |
| linen snake | 0.1 / 0.10 | 10 | 185801747 | 0.08 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Rouhomme: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Neuborn: nothing pays; crew 0.0; est +0 a turn

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~103 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Friedwerp | 684 | 0.19 | 0.10 (10/turn) | tools 16 (4.52->6.65), belts 1 (17.43->24.32), casks 5 (6.35->7.74), hides 1 (10.34->12.35) | tapestries 1 (522.9->798), cheese 26 (6.2->7.46), wool 4 (9.92->11.49), jewellery 1 (78.23->80.27) | +355 |
| Chatgnan | 728 | 0.20 | 0.10 (10/turn) | belts 1 (17.43->25.84), cured meat 3 (24.78->26.6), rope 3 (75->76.47), cheese 4 (8.29->8.79) | tapestries 1 (530.25->798), ploughs 2 (59.33->74.1), wool 2 (9.29->11.49), mouldboards 1 (24.99->28.69) | +318 |
| Essenbrucke | 584 | 0.16 | 0.10 (10/turn) | flax fibres 3 (4.93->5.42), malt 1 (5.51->5.84) | tapestries 1 (530.25->798), gears 1 (54.08->62.22), hinges 2 (28.14->32.49), ploughs 1 (64.05->74.1) | +306 |
| Angefont | 686 | 0.19 | 0.10 (10/turn) | belts 1 (17.43->28.5), raw cloth 1 (5.99->6.22) | tapestries 1 (522.9->798), wool 4 (9.29->11.49), thread 28 (4.41->4.72), jewellery 1 (78.23->80.27) | +302 |
| Calange | 218 | 0.06 | 0.10 (10/turn) | belts 1 (17.43->25.46), wrought iron 7 (13.02->13.87), cheese 10 (8.29->8.84), nets 1 (38.4->41.04) | tapestries 1 (556.5->798), wool 4 (8.72->11.49), grain 26 (2.42->2.68), jewellery 1 (76.65->80.27) | +298 |

**Best:** Friedwerp at about +355 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 28.8, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 52 @ min 3.38 |  |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 20 @ min 20.0 |  |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 264 @ 2.2, stop - |  | uses 714.0/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 264 = 1.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 37.4 |  |
| pasties | 3 @ 13.9, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 5.0 turns |
| porterage | 10 @ 1.1, stop - |  | uses 10.0/turn (observed), makes 0.0, holds 10 = 1.0 turns |
| rope |  | 5 @ min 73.0 | makes 2.2, uses 0.0, holds 36 (keeps 0): sells the surplus + 3/turn of the excess |
| timber |  | 8 @ min 6.5 |  |
| tools | 4 @ 6.2, stop 29 |  | uses 3.6/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 55.2 turns |

## Chain sizing

Mode HOLD, garments sold 21.4/turn (+0.0 exported); plan makes 22.1 garments a turn.
Labour: own 450, everything else 416, chain may buy 350 -> chain allowance 384, chain plan 384 (+6 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.24 | 5.36 |
| ret | 3 | 0.93 | 0.95 |
| spin | 4 | 1.92 | 1.96 |
| weave | 3 | 0.85 | 0.87 |
| sew | 2 | 0.53 | 0.54 |

Buffers: flax fibres 50/73, thread 320/214, cloth 2/87
- chain plan needed 515 labour, budget left 384: cut to 384 (sewing capped at 0.54)

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
- R7 stale ask: rope ask 75.5 over the market for 3 turns: the town trades ~3 a turn at 75, we sold 0 with 36 over what we keep -> **sell price 75.5 -> 75 (last trade 75, floor 64.81)** (ok)
