# v2 shadow report

Turn 13289, 2026-10-15 02:57. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,516, prestige 3,045 (375 free, +23.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 318 | 0 | 19 | 0 | 0 | min_holding 60, sell 55, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 24 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 66 | 0 | 2 | 0 | 0 | min_holding 30, sell 6, sell @ 22 |
| grain | 103 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 129 | 131 | 556 | 0 | 25 | buy 129, buy @ 2.2 |
| meat | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 3.02 |
| nets | 60 | 0 | 0 | 0 | 0 | min_holding 15, sell 7, sell @ 42.6 |
| porterage | 24 | 24 | 23 | 0 | 1 | buy 24, buy @ 0.8 |

**0 risks, 2 waste, 2 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **Flax Wyrm**: Flax Wyrm cost 48 coin last turn (crew 0.50) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell
- **labour**: 25 labour expired last turn (~39 coin): holding 129 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **timber**: build materials for park 1 are in (485.5 held, 40 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 0% (EXPANSION), about 12 turns left; still to deliver: labour 260, limestone 60, timber 40; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 60 | 115.4 | 0 | off: covered |
| timber | 40 | 485.5 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 22

## Notes

- labour: projection runs 48 over real use lately; planning 593, not 641

## Prestige spending, cheapest coin per prestige first

1112 turns left: prestige gained now converts 99.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 46.8 | 49.9 | running |
| hold banquet 2 (pies) | mansion | 7 | 55.2 | 55.2 | thin at home: pies |
| hold banquet 3 (pies) | mansion | 8 | 55.6 | 55.6 | thin at home: hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 56.5 | 56.5 | thin at home: hop beer, pies |
| jousting 1 | arena | 170 | 57.7 | 57.8 | needs a arena (build cost 24,842); thin at home: protection, light armour, arms; needs weaponry skill |
| hold sermon 2 (candles) | church | 31 | 56.5 | 58.6 | needs a church (build cost 68,396); thin at home: jewellery, furniture |
| jousting 3 | arena | 230 | 59.1 | 59.2 | needs a arena (build cost 24,842); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold feast 2 | townhouse | 2.6 | 57.0 | 59.4 | needs a townhouse (build cost 6,714) |
| hold mass 2 (premium) | cathedral | 360 | 58.7 | 59.5 | needs a cathedral (build cost 275,750); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold prayer 2 | chapel | 13 | 57.2 | 59.5 | needs a chapel (build cost 31,470); thin at home: furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 59.7 | 59.7 | thin at home: cured fish |
| hold banquet 2 (meat) | mansion | 6.8 | 59.7 | 59.7 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.5 / 0.50 | 48 | - | 0 | - | - | 0 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn; best orders clear only 5 a turn after crew: ship stays at 0
- best towns now: Gottweiler +66, Amsdermund +25, Etallaen +23, Bordetes +21
- Gottweiler would trade: cured meat buy 6 @ 22.6, grindstones buy 1 @ 226, hop beer buy 2 @ 7.65; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~99 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Rouhomme | 368 | 0.10 | 0.80 (79/turn) | timber 35 (6.18->9.17), beer 58 (3.12->3.65), rope 2 (79.5->87.4), grain 8 (2.6->3.61) | casks 2 (6.46->7.36), mouldboards 1 (43.26->43.51) | +108 |
| Bordetes | 831 | 0.23 | 0.60 (60/turn) | furniture 12 (12.39->16.43), beer 58 (3.12->3.93), cheese 16 (6.93->7.74), paper 2 (21.42->24.32) | cloth 10 (8.35->8.95), garments 2 (21.63->22.8) | +91 |
| Pontmont | 341 | 0.09 | 0.20 (20/turn) | furniture 12 (12.39->17.2), wrought iron 1 (12.5->16.62), beer 58 (3.12->3.32), flax plants 1 (0.86->1.58) | cloth 6 (8.09->8.95), garments 2 (21.84->22.8), slaked lime 1 (7.35->9.21) | +68 |
| Hofkirchen | 991 | 0.31 | 0.40 (40/turn) | furniture 12 (12.39->16.62), thread 34 (4.66->5.13), tools 16 (4.78->5.42), fleece 1 (7.77->11.3) | cured meat 6 (23.52->24.8), hop beer 2 (7.72->9.31), salt 4 (3.86->4.58), garments 2 (21.84->22.8) | +64 |
| Kirchwerp | 1072 | 0.36 | 1.00 (99/turn) | timber 13 (6.18->14.25), beer 22 (3.12->4.26), lead ore 3 (6.2->10.16), grain 3 (2.6->3.38) | cloth 3 (7.77->8.95), garments 0 (21.84->22.8), hop beer 0 (8.14->9.31) | +56 |

**Best:** Rouhomme at about +108 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 28.2, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 55 @ min 3.7 | makes 56.0, uses 19.2, holds 318 (keeps 60): sells the surplus + 18/turn of the excess |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 8 = 5.0 turns |
| cured meat | 6 @ 26.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 24 = 4.0 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 24 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 6 @ min 22.0 | makes 4.9, uses 2.1, holds 66 (keeps 30): sells the surplus + 3/turn of the excess |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 103 = 4.0 turns |
| labour | 143 @ 2.2, stop - |  | uses 592.8/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 129 = 0.9 turns |
| limestone |  | 5 @ min 19.7 |  |
| meat | 7 @ 3.02, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| nets |  | 9 @ min 40.8 | makes 6.0, uses 0.0, holds 60 (keeps 15): sells the surplus + 3/turn of the excess |
| porterage | 23 @ 0.8, stop - |  | uses 23.4/turn (observed), makes 0.0, holds 24 = 1.0 turns |
| rope |  | 6 @ min 77.5 | makes 4.5, uses 0.0, holds 17 (keeps 0): sells the surplus + 1/turn of the excess |
| tar | 2 @ 11.0, stop 6 |  | uses 1.3/turn (ropewalk 1), makes 0.0, holds 6 = 5.0 turns |
| timber |  | 33 @ min 8.5 | makes 24.0, uses 0.0, holds 485 (keeps 350): sells the surplus + 9/turn of the excess |
| tools | 6 @ 6.2, stop 46 |  | uses 5.7/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 34.9 turns |

## Chain sizing

Mode FULL, garments sold 20.3/turn (+0.0 exported); plan makes 4.5 garments a turn.
Labour: own 450, everything else 488, chain may buy 350 -> chain allowance 350, chain plan 120 (-7 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 2.02 | 1.88 |
| ret | 3 | 0.36 | 0.33 |
| spin | 4 | 1.02 | 0.96 |
| weave | 3 | 0.00 | 0.00 |
| sew | 2 | 0.12 | 0.11 |

Buffers: flax fibres 100/45, thread 410/244, cloth 145/86
- thread beyond the household duty (55 a turn) is fed from weaving

## Self-diagnosis

- R3: weavery 1 (weavery) finished but idle 2 turns (weave cloth 2 at 0); no planned recipe for a weavery: Taylor's call
