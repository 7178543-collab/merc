# v2 shadow report

Turn 13260, 2026-10-13 21:54. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, meat, nets, porterage; v1 runs everything else.
Cash 22,267, prestige 2,682 (12 free, +0.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 415 | 0 | 19 | 0 | 0 | min_holding 60, sell 75, sell @ 3.7 |
| cured fish | 21 | 6 | 6 | 0 | 0 | stop 22, buy 6, buy @ 26 |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 28 | 7 | 7 | 0 | 0 | stop 28, buy 9, buy @ 2.4 |
| fish | 8 | 7 | 7 | 0 | 0 | stop 24, buy 8, buy @ 2.5 |
| garments | 298 | 0 | 2 | 0 | 0 | min_holding 30, sell 62, sell @ 22 |
| grain | 130 | 33 | 32 | 0 | 0 | stop 130, buy 33, buy @ 3.7 |
| meat | 8 | 7 | 7 | 0 | 0 | stop 24, buy 8, buy @ 3.02 |
| nets | 51 | 0 | 0 | 0 | 0 | min_holding 40, sell 6, sell @ 39.4 |
| porterage | 37 | 37 | 20 | 0 | 17 | buy 37, buy @ 0.8 |

**1 risks, 0 waste, 6 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **labour**: buying 543, short of ~648 needed -> v2: buy 648

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **fish**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax plants**: flax plants buffer thin: 1.7 turns (target 4) -> v2: lift the maker's rate or hold back sales until it reaches 421
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **timber**: build materials for park 1 are in (451.7 held, 34 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 16% (EXPANSION), about 11 turns left; still to deliver: labour 219, limestone 51, timber 34; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 51 | 153.0 | 0 | off: covered |
| timber | 34 | 451.7 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 20

## Prestige spending, cheapest coin per prestige first

1141 turns left: prestige gained now converts 99.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 2 (pies) | mansion | 7 | 55.4 | 55.4 | thin at home: cheese, pies |
| hold banquet 3 (pies) | mansion | 8 | 56.9 | 56.9 | thin at home: cheese, pies |
| hold prayer 2 | chapel | 13 | 55.4 | 58.1 | needs a chapel (build cost 37,636); thin at home: furniture |
| maintain 1 | park | 0.5 | 54.0 | 58.1 | running |
| hold sermon 2 (candles) | church | 31 | 56.3 | 58.7 | needs a church (build cost 77,494); thin at home: jewellery, candles, furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 59.0 | 59.0 | thin at home: cured fish, cheese |
| hold banquet 4 (pies) | mansion | 18 | 59.0 | 59.0 | thin at home: pies |
| hold banquet 1 (fish) | mansion | 4.2 | 59.9 | 59.9 | running; thin at home: cured fish |
| hold sermon 2 | church | 24 | 56.8 | 59.9 | needs a church (build cost 77,494); thin at home: jewellery, furniture |
| hold banquet 3 (fish) | mansion | 7.6 | 61.3 | 61.3 | thin at home: cured fish, cheese |
| jousting 3 | arena | 230 | 61.3 | 61.4 | needs a arena (build cost 29,411); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold mass 2 (premium) | cathedral | 360 | 60.9 | 61.7 | needs a cathedral (build cost 305,330); thin at home: furniture, jewellery, glassware, candles, premium garments |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 117101560 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 108202735 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Darmwald: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Toqueque: nothing pays; crew 0.0; est +0 a turn
- best towns now: Etallaen +46
- Etallaen would trade: garments sell 39 @ 23.6; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~109 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Etallaen | 774 | 0.23 | 0.20 (22/turn) | garments 39 (21.4->25.84), nets 5 (29.1->41.23), rope 1 (85.05->89.3), grain 10 (2.26->2.77) | hop beer 2 (7.72->9.45), cloth 7 (7.98->8.25) | +227 |
| Herschweig | 775 | 0.23 | 0.20 (22/turn) | cloth 32 (7.9->11.59), nets 4 (29.1->40.28), garments 13 (21.4->22.42), thread 9 (4.66->5.18) | cheese 8 (5.99->6.22) | +163 |
| Bordetes | 831 | 0.25 | 0.20 (22/turn) | nets 2 (29.1->43.13), cheese 14 (6.98->8.46), furniture 13 (12.5->14.63), rope 1 (85.05->92.62) | plate armour 1 (1459.5->1510.5), cloth 9 (7.67->8.25), stockfish 1 (103.43->107.35), garments 2 (21.63->22) | +124 |
| Rouhomme | 368 | 0.11 | 0.60 (66/turn) | bread 137 (2.46->3.38), grain 10 (2.26->4.14), cheese 8 (6.98->7.98), thread 4 (4.66->6.27) | - | +109 |
| Vauxvais | 204 | 0.06 | 0.30 (33/turn) | nets 4 (29.1->40.09), timber 28 (6.25->8.22), tools 16 (5.05->5.22), bricks 1 (4.12->6.65) | limestone 2 (12.6->24.7), tiles 3 (2.37->4.54), beer 19 (3.51->3.7), flax fibres 5 (5.72->5.9) | +102 |

**Best:** Etallaen at about +227 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 76 @ min 3.7 | makes 70.0, uses 19.2, holds 415 (keeps 60): sells the surplus + 25/turn of the excess |
| cured fish | 6 @ 26.0, stop 22 |  | uses 5.5/turn (mansion 1), makes 0.0, holds 21 = 3.9 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 8 @ 2.4, stop 28 |  | uses 6.8/turn (brewery 1, household upkeep), makes 0.0, holds 28 = 4.0 turns |
| fish | 8 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 8 = 1.1 turns |
| garments |  | 61 @ min 22.0 | makes 43.9, uses 2.1, holds 298 (keeps 30): sells the surplus + 19/turn of the excess |
| grain | 33 @ 3.7, stop 130 |  | uses 32.5/turn (brewery 1), makes 0.0, holds 130 = 4.0 turns |
| labour | 648 @ 2.2, stop - |  | uses 1066.8/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 555 = 0.9 turns |
| limestone |  | 5 @ min 23.8 |  |
| meat | 8 @ 3.02, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 8 = 1.1 turns |
| nets |  | 6 @ min 39.4 |  |
| porterage | 35 @ 0.8, stop - |  | uses 31.6/turn (observed), makes 0.0, holds 37 = 1.2 turns |
| rope |  | 4 @ min 73.0 |  |
| timber |  | 30 @ min 8.5 | makes 24.0, uses 0.0, holds 452 (keeps 350): sells the surplus + 6/turn of the excess |
| tools | 8 @ 6.2, stop 60 |  | uses 7.4/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 27.1 turns |
