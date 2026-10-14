# v2 shadow report

Turn 13264, 2026-10-14 01:07. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, meat, nets, porterage; v1 runs everything else.
Cash 17,936, prestige 2,691 (21 free, +4.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 413 | 0 | 19 | 0 | 0 | min_holding 60, sell 63, sell @ 3.7 |
| cured fish | 22 | 5 | 6 | 0 | 0 | stop 22, buy 6, buy @ 26 |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 2 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 8 | 8 | 7 | 0 | 1 | stop 24, buy 8, buy @ 2.5 |
| garments | 268 | 0 | 2 | 0 | 0 | min_holding 30, sell 61, sell @ 22 |
| grain | 104 | 0 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| meat | 8 | 8 | 7 | 0 | 1 | stop 24, buy 8, buy @ 3.02 |
| nets | 56 | 0 | 0 | 0 | 0 | min_holding 40, sell 6, sell @ 40 |
| porterage | 37 | 37 | 28 | 0 | 9 | buy 37, buy @ 0.8 |

**0 risks, 3 waste, 6 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **Flax Wyrm**: Flax Wyrm cost 95 coin last turn (crew 0.88) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell
- **labour**: 117 labour expired last turn (~210 coin): holding 587 against a ~54 buffer target -> v2: trim the buy until the stock is near 54
- **linen snake**: linen snake cost 11 coin last turn (crew 0.10) and its route traded nothing (route limited by salt) -> v2: pause it (crew 0) until a route is proven to sell

## Tuning

- **cured fish**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **fish**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax plants**: flax plants buffer thin: 1.6 turns (target 4) -> v2: lift the maker's rate or hold back sales until it reaches 432
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **timber**: build materials for park 1 are in (446.3 held, 26 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 36% (EXPANSION), about 8 turns left; still to deliver: labour 167, limestone 39, timber 26; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 39 | 141.7 | 0 | off: covered |
| timber | 26 | 446.3 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 21

## Prestige spending, cheapest coin per prestige first

1137 turns left: prestige gained now converts 99.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 2 (pies) | mansion | 7 | 55.5 | 55.5 | thin at home: cheese, pies, candles |
| maintain 1 | park | 0.5 | 54.0 | 57.2 | running |
| hold banquet 3 (pies) | mansion | 8 | 57.4 | 57.4 | thin at home: pies, candles |
| hold prayer 2 | chapel | 13 | 56.7 | 59.1 | needs a chapel (build cost 33,190) |
| hold banquet 2 (fish) | mansion | 6.8 | 59.4 | 59.4 | thin at home: cured fish, cheese |
| hold sermon 2 (candles) | church | 31 | 57.2 | 59.4 | needs a church (build cost 71,402); thin at home: jewellery, candles, furniture |
| hold sermon 2 | church | 24 | 56.8 | 59.7 | needs a church (build cost 71,402); thin at home: jewellery, furniture |
| hold banquet 4 (pies) | mansion | 18 | 59.9 | 59.9 | thin at home: pies, candles, glassware |
| hold banquet 1 (fish) | mansion | 4.2 | 60.7 | 60.7 | running; thin at home: cured fish |
| hold mass 2 (premium) | cathedral | 360 | 60.6 | 61.4 | needs a cathedral (build cost 285,895); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 3 (fish) | mansion | 7.6 | 61.8 | 61.8 | thin at home: cured fish, cheese |
| jousting 3 | arena | 230 | 62.2 | 62.3 | needs a arena (build cost 26,535); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.88 / 0.88 | 95 | 55101678 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 11 | 108202735 | 0.084 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Kleinburgh: nothing pays; crew 0.0; est +0 a turn; best orders clear only -4 a turn after crew: ship stays at 0
- **linen snake** on Toqueque: nothing pays; crew 0.0; est +0 a turn; best orders clear only 4 a turn after crew: ship stays at 0
- best towns now: Etallaen +133, Essenbrucke +28, Orlesailles +19, Gotthafen +18, Kirchwerp +16
- Etallaen would trade: garments sell 28 @ 26.0, hop beer buy 2 @ 7.45, nets sell 7 @ 45.6, rope sell 1 @ 82.0; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~109 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Etallaen | 774 | 0.23 | 0.10 (11/turn) | garments 28 (21.4->27.93), nets 7 (25.06->44.08), rope 1 (78->89.3) | hop beer 2 (7.67->9.21), steel ingots 1 (16.59->17.86) | +321 |
| Vauxvais | 204 | 0.06 | 0.30 (33/turn) | nets 5 (25.06->40.09), lead bars 2 (12.39->13.3), timber 27 (6.95->7.93) | candles 4 (64.58->77.9), beer 19 (3.44->3.7), limestone 1 (12.6->17.7), hides 1 (10.5->13.11) | +142 |
| Gotthafen | 964 | 0.33 | 0.10 (11/turn) | nets 7 (25.06->44.27), seeds 1 (2.62->5.65), slaked lime 1 (11.13->13.68), varnish 1 (18.17->19.76) | salt 7 (4.43->4.89), steel ingots 1 (17.01->17.86), resin 1 (1.51->2.18) | +138 |
| Heilegg | 826 | 0.25 | 0.30 (33/turn) | nets 7 (25.06->41.04), rope 4 (78->81.22), thread 9 (4.66->5.08), garments 64 (21.4->21.66) | hop beer 3 (7.72->9.21), salt 7 (4.33->4.89), butter 1 (62.48->64.12), steel ingots 1 (16.17->17.86) | +125 |
| Neuborn | 780 | 0.23 | 0.90 (98/turn) | nets 6 (25.06->40.85), beer 66 (3.09->3.82), timber 14 (6.95->11.4), limestone 1 (18.59->28.5) | - | +119 |

**Best:** Etallaen at about +321 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 63 @ min 3.7 | makes 56.0, uses 19.2, holds 413 (keeps 60): sells the surplus + 26/turn of the excess |
| cured fish | 6 @ 26.0, stop 22 |  | uses 5.5/turn (mansion 1), makes 0.0, holds 22 = 4.0 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.8 turns |
| fish | 8 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 8 = 1.1 turns |
| garments |  | 60 @ min 22.0 | makes 46.3, uses 2.1, holds 268 (keeps 30): sells the surplus + 16/turn of the excess |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 655 @ 2.2, stop - |  | uses 1073.3/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 587 = 0.9 turns |
| limestone |  | 5 @ min 23.4 |  |
| meat | 8 @ 3.02, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 8 = 1.1 turns |
| nets |  | 7 @ min 38.8 |  |
| porterage | 35 @ 0.8, stop - |  | uses 31.6/turn (observed), makes 0.0, holds 37 = 1.2 turns |
| rope |  | 4 @ min 76.0 |  |
| timber |  | 30 @ min 8.5 | makes 24.0, uses 0.0, holds 446 (keeps 350): sells the surplus + 6/turn of the excess |
| tools | 8 @ 6.2, stop 60 |  | uses 7.4/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 27.0 turns |
