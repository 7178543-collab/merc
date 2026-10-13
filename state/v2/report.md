# v2 shadow report

Turn 13248, 2026-10-13 09:14. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, meat, nets, porterage; v1 runs everything else.
Cash 22,472, prestige 2,595 (175 free, +4.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 269 | 0 | 19 | 0 | 0 | min_holding 60, sell 30, sell @ 3.7 |
| cured fish | 19 | 6 | 6 | 0 | 0 | stop 20, buy 7, buy @ 26 |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 25 | 6 | 6 | 0 | 0 | stop 26, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 6 | 0 | 1 | stop 24, buy 7, buy @ 2.5 |
| garments | 424 | 0 | 2 | 0 | 0 | min_holding 30, sell 68, sell @ 23.8 |
| grain | 130 | 33 | 32 | 0 | 0 | stop 130, buy 33, buy @ 3.7 |
| meat | 7 | 7 | 6 | 0 | 1 | stop 24, buy 7, buy @ 3.02 |
| nets | 48 | 0 | 0 | 0 | 0 | min_holding 40, sell 6, sell @ 41.6 |
| porterage | 37 | 37 | 29 | 0 | 8 | buy 37, buy @ 0.8 |

**0 risks, 3 waste, 5 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **Flax Wyrm**: Flax Wyrm cost 75 coin last turn (crew 0.72) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell
- **labour**: 154 labour expired last turn (~267 coin): holding 714 against a ~54 buffer target -> v2: trim the buy until the stock is near 54
- **linen snake**: linen snake cost 52 coin last turn (crew 0.50) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell

## Tuning

- **candles**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **cloth**: cloth buffer thin: 1.7 turns (target 4) -> v2: lift the maker's rate or hold back sales until it reaches 352
- **flax plants**: flax plants buffer thin: 1.4 turns (target 4) -> v2: lift the maker's rate or hold back sales until it reaches 489
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **timber**: build materials for park 1 are in (433.6 held, 22 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 45% (EXPANSION), about 7 turns left; still to deliver: labour 143, limestone 33, timber 22; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 33 | 152.7 | 0 | off: covered |
| timber | 22 | 433.6 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 21

## Prestige spending, cheapest coin per prestige first

1153 turns left: prestige gained now converts 99.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: waiting - level 2 costs 250, free 175: ~19 turns at +4.1/turn

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.9 | 55.0 | running |
| hold banquet 2 (pies) | mansion | 7 | 56.5 | 56.5 | thin at home: pasties, cheese, pies, candles |
| hold banquet 3 (pies) | mansion | 8 | 57.9 | 57.9 | thin at home: pasties, pies, candles |
| hold banquet 2 (fish) | mansion | 6.8 | 58.0 | 58.0 | thin at home: cured fish, cheese |
| hold banquet 4 (pies) | mansion | 18 | 58.3 | 58.3 | thin at home: pasties, candles |
| jousting 1 | arena | 170 | 58.7 | 58.9 | needs a arena (build cost 25,581); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 60.1 | 60.1 | running; thin at home: cured fish |
| jousting 3 | arena | 230 | 60.0 | 60.1 | needs a arena (build cost 25,581); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold mass 2 (premium) | cathedral | 360 | 59.4 | 60.2 | needs a cathedral (build cost 280,380); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold sermon 2 (candles) | church | 31 | 58.1 | 60.3 | needs a church (build cost 69,358); thin at home: jewellery, candles, furniture |
| hold banquet 3 (fish) | mansion | 7.6 | 60.5 | 60.5 | thin at home: cured fish, cheese |
| hold feast 2 | townhouse | 2.6 | 58.3 | 60.7 | needs a townhouse (build cost 6,909) |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.72 | 75 | 88002195 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.50 | 52 | 159601387 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Clairlond: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Kirchwerp: nothing pays; crew 0.0; est +0 a turn

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~106 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Rouhomme | 368 | 0.10 | 0.10 (11/turn) | thread 39 (4.86->6.27), lead ore 2 (5.78->22.8), lead bars 1 (12.39->31.35), cured meat 2 (31.5->39.9) | flax fibres 2 (4.83->5.7), tools 7 (5.04->5.2) | +130 |
| Hofkirchen | 991 | 0.33 | 0.20 (21/turn) | flax fibres 16 (5.01->10.16), tools 16 (5.43->6.65), yarn 5 (3.89->4.75), slaked lime 1 (8.03->9.12) | acid 1 (157.5->167.2), hop beer 2 (7.88->9.59), jewellery 1 (78.75->79.8), salt 13 (4.09->4.54) | +102 |
| Chatgnan | 728 | 0.20 | 0.30 (32/turn) | beer 52 (3.02->3.95), cheese 12 (6.3->8.79), varnish 2 (18.17->19.76), cured fish 1 (24.8->26.03) | garments 22 (21.84->23.18), hides 1 (11.23->12.35), salt 3 (4.24->4.54) | +84 |
| Hanstein | 380 | 0.11 | 0.40 (42/turn) | timber 8 (6.6->9.88), cloth 20 (7.01->7.6), nets 5 (42.8->43.89), beer 68 (3.02->3.25) | flax plants 68 (1.37->2.1), flax fibres 26 (5.35->5.7), pies 1 (17.32->18.34), seeds 3 (1.89->2.32) | +69 |
| Vauxvais | 204 | 0.06 | 0.40 (42/turn) | timber 26 (6.6->8.22), beer 57 (3.02->3.27), cheese 14 (6.3->6.79), bricks 1 (4.3->9.79) | thread 37 (4.73->5.25), limestone 2 (12.6->17.6), flax plants 6 (1.58->2.1), hides 1 (10.71->12.35) | +67 |

**Best:** Rouhomme at about +130 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 65 @ min 3.7 | makes 70.0, uses 18.6, holds 269 (keeps 60): sells the surplus + 13/turn of the excess |
| candles | 3 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 4 = 2.3 turns |
| cured fish | 7 @ 26.0, stop 20 |  | uses 5.5/turn (mansion 1), makes 0.0, holds 19 = 3.5 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 26 |  | uses 6.4/turn (brewery 1, household upkeep), makes 0.0, holds 25 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 7 = 1.2 turns |
| garments |  | 73 @ min 23.8 | makes 45.1, uses 1.8, holds 424 (keeps 30): sells the surplus + 29/turn of the excess |
| grain | 33 @ 3.7, stop 130 |  | uses 32.5/turn (brewery 1), makes 0.0, holds 130 = 4.0 turns |
| labour | 650 @ 2.2, stop - |  | uses 1068.9/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 714 = 1.2 turns |
| light armour | 1 @ 112, stop 1 |  | uses 0.2/turn (household upkeep), makes 0.0, holds 0 = 2.0 turns |
| limestone |  | 5 @ min 24.2 |  |
| meat | 7 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 7 = 1.2 turns |
| nets |  | 6 @ min 41.6 |  |
| porterage | 35 @ 0.8, stop - |  | uses 31.6/turn (observed), makes 0.0, holds 37 = 1.2 turns |
| timber |  | 29 @ min 8.5 | makes 24.0, uses 0.0, holds 434 (keeps 350): sells the surplus + 5/turn of the excess |
| tools | 8 @ 6.2, stop 62 |  | uses 7.7/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 25.9 turns |
