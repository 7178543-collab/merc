# v2 shadow report

Turn 13279, 2026-10-14 16:03. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,151, prestige 0 (-2,670 free, +0.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 261 | 0 | 19 | 0 | 0 | min_holding 60, sell 53, sell @ 3.7 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 24 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 8 | 8 | 7 | 0 | 1 | stop 24, buy 8, buy @ 2.5 |
| garments | 126 | 0 | 2 | 0 | 0 | min_holding 30, sell 28, sell @ 22 |
| grain | 103 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 585 | 585 | 740 | 0 | 295 | buy 585, buy @ 2.2 |
| meat | 8 | 8 | 7 | 0 | 1 | stop 24, buy 8, buy @ 3.02 |
| nets | 55 | 0 | 0 | 0 | 0 | min_holding 40, sell 7, sell @ 43 |
| porterage | 37 | 37 | 25 | 0 | 12 | buy 37, buy @ 0.8 |

**0 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **labour**: 295 labour expired last turn (~516 coin): holding 585 against a ~40 buffer target -> v2: trim the buy until the stock is near 40

## Tuning

- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **timber**: build materials for park 1 are in (436.0 held, 34 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 16% (EXPANSION), about 11 turns left; still to deliver: labour 219, limestone 51, timber 34; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 51 | 113.4 | 0 | off: covered |
| timber | 34 | 436.0 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 20

## Prestige spending, cheapest coin per prestige first

1122 turns left: prestige gained now converts 99.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 2 (pies) | mansion | 7 | 56.2 | 56.2 | thin at home: pasties, cheese, pies |
| maintain 1 | park | 0.5 | 52.5 | 56.2 | running |
| hold banquet 3 (pies) | mansion | 8 | 56.4 | 56.4 | thin at home: pasties, cheese, pies |
| hold banquet 4 (pies) | mansion | 18 | 58.4 | 58.4 | thin at home: pies |
| hold banquet 2 (meat) | mansion | 6.8 | 59.0 | 59.0 | thin at home: cheese |
| hold mass 2 (premium) | cathedral | 360 | 58.6 | 59.5 | needs a cathedral (build cost 298,680); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 3 (meat) | mansion | 7.6 | 60.0 | 60.0 | thin at home: cheese |
| jousting 1 | arena | 170 | 60.0 | 60.2 | needs a arena (build cost 28,336); thin at home: protection, light armour, arms; needs weaponry skill |
| jousting 3 | arena | 230 | 60.7 | 60.8 | needs a arena (build cost 28,336); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 62.1 | 62.1 | thin at home: cured fish, cheese |
| hold feast 2 | townhouse | 2.6 | 60.2 | 62.6 | needs a townhouse (build cost 6,786) |
| hold banquet 3 (fish) | mansion | 7.6 | 62.8 | 62.8 | thin at home: cured fish, cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 11 | 108202735 | 0.052 | cheese 4, salt 4 | - | 38 |
| linen snake | 0.0 / 0.03 | 3 | 141901647 | 0 | nets 3 | cured meat 5 | -47 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Toqueque: nothing pays; crew 0.0; est +0 a turn; best orders clear only 1 a turn after crew: ship stays at 0
- **linen snake** on Heilegg: nothing pays; crew 0.0; est +0 a turn; best orders clear only -7 a turn after crew: ship stays at 0
- best towns now: Magdeach +59, Rouhomme +47, Cobholme +42, Hofkirchen +32, Boistot +27
- Magdeach would trade: cured meat buy 4 @ 21.2, rope sell 3 @ 98.5, varnish sell 1 @ 19.8; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~108 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Rouhomme | 368 | 0.11 | 0.50 (54/turn) | cheese 13 (6.51->9.88), bread 133 (2.54->3.13), lead ore 6 (6.09->11.97), yarn 7 (4.89->7.65) | garments 20 (22.68->24.89) | +197 |
| Magdeach | 667 | 0.19 | 0.10 (11/turn) | rope 3 (77.5->106.4), tools 13 (4.76->5.13), varnish 1 (18.17->20.33), tar 1 (9.6->11.11) | garments 15 (23.94->24.89), cured meat 4 (22.26->23) | +101 |
| Angefont | 686 | 0.20 | 0.10 (11/turn) | rope 4 (77.5->81.22), thread 20 (4.66->5.42), cheese 10 (6.51->7.03), cured meat 1 (22.8->25.08) | garments 20 (22.05->24.89), dye 1 (52.5->54.62) | +85 |
| Vauxvais | 204 | 0.06 | 0.10 (11/turn) | thread 18 (4.66->5.13), grain 8 (2.78->3.19), resin 2 (2.58->2.96), flax fibres 8 (6.15->6.27) | garments 20 (22.05->24.89), beer 19 (3.84->4.14), dye 1 (52.5->54.62), cloth 20 (7.88->8) | +72 |
| Hofkirchen | 991 | 0.34 | 0.20 (22/turn) | rope 3 (77.5->80.75), tools 16 (4.76->5.61), thread 30 (4.66->5.08), resin 1 (2.58->3.29) | garments 20 (22.68->24.89), soap 1 (114.45->120.65), pasties 6 (11.03->12.92), canvas 1 (31.71->35.15) | +70 |

**Best:** Rouhomme at about +197 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 26.6, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 51 @ min 4.14 | makes 56.0, uses 19.2, holds 261 (keeps 60): sells the surplus + 14/turn of the excess |
| candles | 3 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 4 = 3.0 turns |
| cured meat | 7 @ 24.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 22 = 3.7 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 24 = 3.9 turns |
| fish | 8 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 8 = 1.1 turns |
| garments |  | 29 @ min 26.2 | makes 24.6, uses 2.1, holds 126 (keeps 30): sells the surplus + 6/turn of the excess |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 103 = 4.0 turns |
| labour | 356 @ 2.2, stop - |  | uses 788.7/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 585 = 1.7 turns |
| limestone |  | 5 @ min 21.8 |  |
| meat | 8 @ 3.02, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 8 = 1.1 turns |
| nets |  | 7 @ min 41.4 |  |
| porterage | 33 @ 0.8, stop - |  | uses 29.6/turn (observed), makes 0.0, holds 37 = 1.3 turns |
| rope |  | 5 @ min 72.0 |  |
| timber |  | 29 @ min 8.5 | makes 24.0, uses 0.0, holds 436 (keeps 350): sells the surplus + 5/turn of the excess |
| tools | 7 @ 6.2, stop 51 |  | uses 6.3/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 31.6 turns |

## Self-diagnosis

- R1: prestige rate +0.00 a turn vs 12-turn median +3.54; likely: no slot, building or contract cause found: check the impacts
