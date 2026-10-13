# v2 shadow report

Turn 13259, 2026-10-13 20:58. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, meat, nets, porterage; v1 runs everything else.
Cash 22,593, prestige 2,681 (11 free, +0.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 407 | 0 | 19 | 0 | 0 | min_holding 60, sell 75, sell @ 3.7 |
| cured fish | 22 | 5 | 6 | 0 | 0 | stop 22, buy 6, buy @ 26 |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 25 | 6 | 7 | 0 | 0 | stop 26, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 300 | 0 | 2 | 0 | 0 | min_holding 30, sell 63, sell @ 22 |
| grain | 130 | 32 | 32 | 0 | 0 | stop 130, buy 33, buy @ 3.7 |
| meat | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 3.02 |
| nets | 51 | 0 | 0 | 0 | 0 | min_holding 40, sell 6, sell @ 41 |
| porterage | 37 | 37 | 11 | 0 | 26 | buy 37, buy @ 0.8 |

**0 risks, 0 waste, 5 tuning** where v2 would act differently from v1.

## Tuning

- **cured fish**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **fish**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax plants**: flax plants buffer thin: 1.6 turns (target 4) -> v2: lift the maker's rate or hold back sales until it reaches 428
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **timber**: build materials for park 1 are in (449.7 held, 38 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 6% (EXPANSION), about 12 turns left; still to deliver: labour 245, limestone 57, timber 38; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 57 | 153.0 | 0 | off: covered |
| timber | 38 | 449.7 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 21

## Prestige spending, cheapest coin per prestige first

1142 turns left: prestige gained now converts 99.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 3 (pies) | mansion | 8 | 54.1 | 54.1 | thin at home: cheese, pies |
| hold banquet 2 (pies) | mansion | 7 | 56.0 | 56.0 | thin at home: cheese, pies |
| maintain 1 | park | 0.5 | 52.2 | 56.3 | running |
| hold banquet 4 (pies) | mansion | 18 | 57.1 | 57.1 | thin at home: cheese, pies |
| hold prayer 2 | chapel | 13 | 55.1 | 57.8 | needs a chapel (build cost 38,204) |
| hold sermon 2 (candles) | church | 31 | 56.1 | 58.5 | needs a church (build cost 77,512); thin at home: jewellery, candles, furniture |
| hold sermon 2 | church | 24 | 56.5 | 59.6 | needs a church (build cost 77,512); thin at home: jewellery, furniture |
| hold banquet 3 (fish) | mansion | 7.6 | 59.8 | 59.8 | thin at home: cured fish, cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 60.5 | 60.5 | running; thin at home: cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 60.9 | 60.9 | thin at home: cured fish, cheese |
| hold mass 2 (premium) | cathedral | 360 | 60.1 | 60.9 | needs a cathedral (build cost 304,580); thin at home: furniture, jewellery, glassware, candles, premium garments |
| jousting 3 | arena | 230 | 60.9 | 61.0 | needs a arena (build cost 29,464); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 117101560 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 108202735 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Darmwald: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Toqueque: nothing pays; crew 0.0; est +0 a turn; best orders clear only 1 a turn after crew: ship stays at 0
- best towns now: Donaunieder +19
- Donaunieder would trade: nets sell 6 @ 47.4; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~106 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Etallaen | 774 | 0.22 | 0.50 (53/turn) | garments 42 (21.4->23.75), beer 46 (3.08->3.93), nets 6 (40.6->44.27), flax plants 13 (1.32->3.1) | arms 4 (24.57->26.41), cheese 18 (7.3->7.79), jewellery 1 (82.95->88.35), cloth 4 (7.98->8.75) | +169 |
| Fontaux | 411 | 0.12 | 0.40 (43/turn) | candles 1 (84.53->113.05), timber 9 (6.2->10.16), beer 41 (3.08->3.67), tools 16 (4.66->5.32) | cheese 34 (6.51->7.79), cloth 28 (8.29->8.75) | +125 |
| Rouhomme | 368 | 0.10 | 0.50 (53/turn) | bread 136 (2.44->3.27), grain 10 (2.26->3.89), furniture 12 (12.5->13.3), charcoal 2 (2.18->3.69) | cloth 32 (8.24->8.75), flax plants 1 (1.18->1.66) | +104 |
| Gottweiler | 1135 | 0.42 | 0.40 (43/turn) | wine 8 (6.41->7.27) | cheese 35 (6.04->7.79), cured meat 7 (22.47->27.55), cloth 37 (7.88->8.75), steel ingots 1 (13.12->15.11) | +99 |
| Pontmont | 341 | 0.10 | 0.80 (85/turn) | beer 79 (3.08->3.72), bread 136 (2.44->2.87), grain 10 (2.26->3.27), furniture 12 (12.5->13.49) | cheese 16 (6.72->7.79), cloth 10 (8.35->8.75), flax plants 1 (0.58->1.66), garments 2 (21.84->22) | +95 |

**Best:** Etallaen at about +169 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ ?, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 75 @ min 3.7 | makes 70.0, uses 19.2, holds 407 (keeps 60): sells the surplus + 25/turn of the excess |
| cured fish | 6 @ 26.0, stop 22 |  | uses 5.5/turn (mansion 1), makes 0.0, holds 22 = 4.0 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 9 @ 2.4, stop 28 |  | uses 6.8/turn (brewery 1, household upkeep), makes 0.0, holds 25 = 3.7 turns |
| fish | 8 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 62 @ min 22.0 | makes 45.1, uses 2.1, holds 300 (keeps 30): sells the surplus + 19/turn of the excess |
| grain | 33 @ 3.7, stop 130 |  | uses 32.5/turn (brewery 1), makes 0.0, holds 130 = 4.0 turns |
| labour | 633 @ 2.2, stop - |  | uses 1052.3/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 522 = 0.9 turns |
| limestone |  | 5 @ min 23.6 |  |
| meat | 8 @ 3.02, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| nets |  | 6 @ min 39.4 |  |
| porterage | 35 @ 0.8, stop - |  | uses 31.6/turn (observed), makes 0.0, holds 37 = 1.2 turns |
| timber |  | 30 @ min 8.5 | makes 24.0, uses 0.0, holds 450 (keeps 350): sells the surplus + 6/turn of the excess |
| tools | 8 @ 6.2, stop 60 |  | uses 7.4/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 27.0 turns |
