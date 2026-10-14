# v2 shadow report

Turn 13265, 2026-10-14 02:55. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, meat, nets, porterage; v1 runs everything else.
Cash 16,633, prestige 2,695 (25 free, +4.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 411 | 0 | 19 | 0 | 0 | min_holding 60, sell 63, sell @ 3.7 |
| cured fish | 21 | 6 | 6 | 0 | 0 | stop 22, buy 6, buy @ 26 |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 8 | 8 | 7 | 0 | 1 | stop 24, buy 8, buy @ 2.5 |
| garments | 248 | 0 | 2 | 0 | 0 | min_holding 30, sell 23, sell @ 22 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| meat | 8 | 8 | 7 | 0 | 1 | stop 24, buy 8, buy @ 3.02 |
| nets | 56 | 0 | 0 | 0 | 0 | min_holding 40, sell 7, sell @ 38.8 |
| porterage | 37 | 37 | 29 | 0 | 8 | buy 37, buy @ 0.8 |

**0 risks, 2 waste, 5 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **labour**: 256 labour expired last turn (~459 coin): holding 486 against a ~53 buffer target -> v2: trim the buy until the stock is near 53
- **linen snake**: linen snake cost 54 coin last turn (crew 0.50) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell

## Tuning

- **flax plants**: flax plants buffer thin: 1.6 turns (target 4) -> v2: lift the maker's rate or hold back sales until it reaches 424
- **grain**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **timber**: build materials for park 1 are in (441.2 held, 22 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 45% (EXPANSION), about 7 turns left; still to deliver: labour 143, limestone 33, timber 22; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 33 | 141.9 | 0 | off: covered |
| timber | 22 | 441.2 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 21

## Prestige spending, cheapest coin per prestige first

1136 turns left: prestige gained now converts 99.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 2 (pies) | mansion | 7 | 56.2 | 56.2 | thin at home: cheese, pies, candles |
| maintain 1 | park | 0.5 | 53.7 | 56.9 | running |
| hold banquet 3 (pies) | mansion | 8 | 57.6 | 57.6 | thin at home: cheese, pies, candles |
| hold banquet 4 (pies) | mansion | 18 | 59.6 | 59.6 | thin at home: cheese, pies, candles |
| hold banquet 1 (fish) | mansion | 4.2 | 60.3 | 60.3 | running; thin at home: cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 60.3 | 60.3 | thin at home: cured fish, cheese |
| jousting 1 | arena | 170 | 60.2 | 60.4 | needs a arena (build cost 26,445); thin at home: protection, light armour, arms; needs weaponry skill |
| hold mass 2 (premium) | cathedral | 360 | 60.2 | 61.0 | needs a cathedral (build cost 285,085); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold sermon 2 (candles) | church | 31 | 58.8 | 61.0 | needs a church (build cost 71,230); thin at home: jewellery, candles, furniture |
| jousting 3 | arena | 230 | 61.7 | 61.8 | needs a arena (build cost 26,445); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold prayer 2 | chapel | 13 | 59.8 | 62.1 | needs a chapel (build cost 33,290); thin at home: furniture |
| hold sermon 2 | church | 24 | 59.3 | 62.1 | needs a church (build cost 71,230); thin at home: jewellery, furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 55101678 | 0 | - | - | 0 |
| linen snake | 0.5 / 0.50 | 54 | - | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Kleinburgh: nothing pays; crew 0.0; est +0 a turn; best orders clear only -1 a turn after crew: ship stays at 0
- best towns now: Bordetes +49, Coburgbaum +42, Nürnnieder +41, Marmont +38, Heilegg +34
- Bordetes would trade: dyed cloth sell 4 @ 11.5, rope sell 2 @ 86.0, soap buy 1 @ 100.0, steel ingots sell 1 @ 14.8, tallow sell 3 @ 28.0; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~110 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.35 | 0.80 (88/turn) | rope 4 (63->78.38), flax fibres 13 (5.45->10.16), beer 66 (3.1->4.35), tallow 3 (23.1->31.16) | garments 25 (22.68->23.75), cloth 11 (7.88->8.75), cheese 25 (6.3->6.84), hop beer 2 (7.72->9.59) | +214 |
| Bordetes | 831 | 0.25 | 0.40 (44/turn) | rope 3 (63->83.12), tallow 3 (23.1->26.98), beer 66 (3.1->3.72), ploughs 1 (79.8->85.5) | garments 25 (21.63->23.75), soap 1 (102.9->121.6), cloth 9 (7.67->8.75) | +156 |
| Vauxvais | 204 | 0.06 | 0.30 (33/turn) | rope 2 (63->73.62), nets 5 (38.4->40.09), cured meat 4 (25.41->26.6), steel ingots 1 (12.5->16.43) | candles 4 (64.58->77.9), garments 20 (22.26->23.75), cloth 11 (7.88->8.75), limestone 1 (12.6->22) | +141 |
| Cobholme | 1564 | 0.69 | 0.20 (22/turn) | rope 4 (63->82.65), tallow 1 (23.1->30.4), varnish 1 (18.17->21.66), pies 1 (16.7->19) | garments 25 (21->23.75) | +134 |
| Heilegg | 826 | 0.25 | 0.10 (11/turn) | rope 4 (63->82.17), nets 7 (38.4->42.75), dyed cloth 4 (10.45->11.49), glassware 1 (77.17->80.27) | cheese 25 (6.25->6.84), hop beer 2 (7.77->9.59), cloth 11 (8.45->8.75) | +122 |

**Best:** Hofkirchen at about +214 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 26.6, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 63 @ min 3.7 | makes 56.0, uses 19.2, holds 411 (keeps 60): sells the surplus + 26/turn of the excess |
| cured fish | 6 @ 26.0, stop 22 |  | uses 5.5/turn (mansion 1), makes 0.0, holds 21 = 3.9 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.8 turns |
| fish | 8 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 8 = 1.1 turns |
| garments |  | 57 @ min 22.0 | makes 44.7, uses 2.1, holds 248 (keeps 30): sells the surplus + 15/turn of the excess |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 628 @ 2.2, stop - |  | uses 1047.8/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 486 = 0.8 turns |
| limestone |  | 5 @ min 23.2 |  |
| meat | 8 @ 3.02, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 8 = 1.1 turns |
| nets |  | 7 @ min 37.4 |  |
| porterage | 35 @ 0.8, stop - |  | uses 31.6/turn (observed), makes 0.0, holds 37 = 1.2 turns |
| rope |  | 4 @ min 71.5 |  |
| timber |  | 30 @ min 8.5 | makes 24.0, uses 0.0, holds 441 (keeps 350): sells the surplus + 6/turn of the excess |
| tools | 8 @ 6.2, stop 62 |  | uses 7.7/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 26.0 turns |
