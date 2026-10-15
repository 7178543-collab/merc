# v2 shadow report

Turn 13301, 2026-10-15 14:59. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,854, prestige 3,104 (434 free, +22.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 249 | 0 | 19 | 0 | 0 | min_holding 60, sell 49, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 24 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 46 | 0 | 2 | 0 | 0 | min_holding 30, sell 3, sell @ 22 |
| grain | 103 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 156 | 175 | 625 | 0 | 0 | buy 175, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 55 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 39 |
| porterage | 26 | 26 | 26 | 0 | 0 | buy 26, buy @ 0.8 |

**1 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **labour**: buying 175, short of ~218 needed -> v2: buy 218

## Waste (money lost now)

- **Flax Wyrm**: Flax Wyrm cost 16 coin last turn (crew 0.16) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell

## Tuning

- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **timber**: build materials for park 1 are in (680.2 held, 40 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 0% (EXPANSION), about 12 turns left; still to deliver: labour 260, limestone 60, timber 40; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 60 | 110.7 | 0 | off: covered |
| timber | 40 | 680.2 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 22

## Notes

- labour: projection runs 40 over real use lately; planning 668, not 708

## Prestige spending, cheapest coin per prestige first

1100 turns left: prestige gained now converts 99.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.7 | 50.4 | running |
| hold prayer 2 | chapel | 13 | 53.5 | 55.7 | needs a chapel (build cost 29,526); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 54.3 | 56.4 | needs a church (build cost 65,363); thin at home: jewellery, candles, furniture |
| hold sermon 2 | church | 24 | 54.5 | 57.2 | needs a church (build cost 65,363); thin at home: jewellery, furniture |
| hold banquet 2 (pies) | mansion | 7 | 57.3 | 57.3 | thin at home: wine, pies |
| hold banquet 4 (pies) | mansion | 18 | 57.9 | 57.9 | thin at home: hop beer, wine |
| hold banquet 1 (meat) | mansion | 4.2 | 58.0 | 58.0 | running |
| hold banquet 3 (pies) | mansion | 8 | 58.0 | 58.0 | thin at home: hop beer, pies |
| hold banquet 1 (fish) | mansion | 4.2 | 58.4 | 58.4 |  |
| hold banquet 2 (meat) | mansion | 6.8 | 58.9 | 58.9 | thin at home: wine |
| jousting 1 | arena | 170 | 59.3 | 59.4 | needs a arena (build cost 23,328); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 59.8 | 59.8 | thin at home: wine, cured fish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.5 / 0.16 | 16 | - | 0 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Heilegg: axes buy 3 @ 18.2, hop beer buy 2 @ 7.55, spinning wheels buy 1 @ 252, varnish sell 1 @ 19.2; crew 0.1; est +20 a turn
- best towns now: Brunnham +57, Kirchwerp +47, Hofkirchen +45, Toqueque +43, Dortgart +35
- Brunnham would trade: hop beer buy 2 @ 6.65, mouldboards buy 1 @ 38.2, nets sell 4 @ 45.8, spinning wheels buy 1 @ 242, varnish sell 1 @ 21.8; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~100 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.31 | 1.00 (100/turn) | bread 96 (2.44->3.88), flax fibres 3 (6.55->10.16), butter 0 (69.3->71.25), thread 10 (4.74->5.13) | acid 1 (174.3->180.5), spinning wheels 0 (268.8->277.4), axes 1 (17.85->19.38), gears 0 (74.03->75.52) | +75 |
| Kirchwerp | 1072 | 0.36 | 0.30 (30/turn) | furniture 12 (12.39->15.01), butter 1 (69.3->76), cured meat 2 (22->22.99), grain 8 (2.26->3.04) | spinning wheels 1 (256.2->277.4), gears 1 (66.67->75.52), axes 3 (17.85->19.38), cheese 16 (6.2->6.79) | +60 |
| Toqueque | 642 | 0.17 | 0.10 (10/turn) | tackles 1 (199.5->233.7), rope 2 (82.5->86.45), nets 4 (40.2->41.99), thread 5 (4.74->5.08) | flax fibres 11 (5.88->6.8), tar 1 (9.24->10.6), axes 2 (19.11->19.38) | +54 |
| Hanstein | 380 | 0.10 | 0.20 (20/turn) | timber 10 (5.99->9.79), logs 1 (3.24->5.65), nails 1 (5.5->5.79) | flax fibres 26 (5.72->6.8), cloth 7 (7.88->8.5), candles 1 (77.17->78.5), seeds 4 (1.84->2.32) | +52 |
| Brunnham | 1281 | 0.47 | 0.10 (10/turn) | nets 4 (40.2->44.46), varnish 1 (18.17->21.09) | spinning wheels 1 (247.8->277.4), hop beer 2 (6.83->9.59), mouldboards 1 (39.27->43.89), scythes 1 (28.14->29.45) | +50 |

**Best:** Hofkirchen at about +75 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 27.6, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 49 @ min 3.7 | makes 56.0, uses 19.2, holds 249 (keeps 60): sells the surplus + 13/turn of the excess |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 8 = 5.0 turns |
| cured meat | 6 @ 23.4, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 24 = 4.0 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 24 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 3 @ min 22.0 | makes 3.7, uses 2.1, holds 46 (keeps 30): sells the surplus + 1/turn of the excess |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 103 = 4.0 turns |
| labour | 218 @ 2.2, stop - |  | uses 668.4/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 156 = 0.7 turns |
| limestone |  | 5 @ min 18.2 |  |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 9 @ min 39.0 | makes 6.0, uses 0.0, holds 55 (keeps 15): sells the surplus + 3/turn of the excess |
| porterage | 25 @ 1.1, stop - |  | uses 25.2/turn (observed), makes 0.0, holds 26 = 1.0 turns |
| rope |  | 6 @ min 80.5 | makes 4.5, uses 0.0, holds 21 (keeps 0): sells the surplus + 1/turn of the excess |
| tar | 3 @ 11.0, stop 5 |  | uses 1.1/turn (ropewalk 1), makes 0.0, holds 3 = 2.8 turns |
| timber |  | 50 @ min 8.5 | makes 24.0, uses 0.0, holds 680 (keeps 350): sells the surplus + 26/turn of the excess |
| tools | 7 @ 6.2, stop 52 |  | uses 6.4/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 31.0 turns |

## Chain sizing

Mode FULL, garments sold 3.8/turn (+0.0 exported); plan makes 1.6 garments a turn.
Labour: own 450, everything else 503, chain may buy 350 -> chain allowance 350, chain plan 187 (-12 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.07 | 4.12 |
| ret | 3 | 0.72 | 0.73 |
| spin | 4 | 1.58 | 1.51 |
| weave | 3 | 0.00 | 0.00 |
| sew | 2 | 0.09 | 0.04 |

Buffers: flax fibres 64/54, thread 216/173, cloth 48/15
- thread beyond the household duty (55 a turn) is fed from weaving

## Self-diagnosis

- R3: weavery 1 (weavery) finished but idle 6 turns (weave cloth 2 at 0); no planned recipe for a weavery: Taylor's call
- R4: ropewalk 1 projected 0: short of labour (~28 needed); labour itself is not raised here
- R5: tar buy not filling: bid 9.6 under the home ask 10.6 for 6 turns, bought 2.0 of 4, 3.0 held (2.8 turns) (held back: failsafe level 1: reduce-only, would buy price 9.6 -> 10.8 (ask 10.6, ceiling 11.0))
