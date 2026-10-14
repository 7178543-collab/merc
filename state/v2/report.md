# v2 shadow report

Turn 13272, 2026-10-14 09:00. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, meat, nets, porterage; v1 runs everything else.
Cash 13,951, prestige 2,812 (142 free, -0.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 370 | 0 | 4 | 0 | 0 | min_holding 60, sell 60, sell @ 3.7 |
| cured fish | 5 | 0 | 0 | 0 | 0 | stop 22, buy 11, buy @ 26 |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 5 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 8 | 8 | 7 | 0 | 1 | stop 24, buy 8, buy @ 2.5 |
| garments | 177 | 0 | 2 | 0 | 0 | min_holding 30, sell 19, sell @ 22 |
| grain | 103 | 26 | 21 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| meat | 8 | 8 | 7 | 0 | 1 | stop 24, buy 8, buy @ 3.02 |
| nets | 51 | 0 | 0 | 0 | 0 | min_holding 40, sell 6, sell @ 40.6 |
| porterage | 37 | 37 | 8 | 0 | 29 | buy 37, buy @ 0.8 |

**1 risks, 2 waste, 4 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **labour**: buying 370, short of ~698 needed -> v2: buy 698

## Waste (money lost now)

- **Flax Wyrm**: Flax Wyrm cost 53 coin last turn (crew 0.48) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell
- **porterage**: 29 porterage expired last turn (~31 coin): holding 37 against a ~3 buffer target -> v2: trim the buy until the stock is near 3

## Tuning

- **cured fish**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax plants**: flax plants buffer thin: 1.4 turns (target 4) -> v2: lift the maker's rate or hold back sales until it reaches 507
- **limestone**: we make 5/turn more than we use but there is no sell order -> v2: sell 5
- **timber**: build materials for park 1 are in (411.8 held, 10 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 75% (EXPANSION), about 3 turns left; still to deliver: labour 65, limestone 15, timber 10; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 15 | 142.7 | 0 | off: covered |
| timber | 10 | 411.8 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 22

## Prestige spending, cheapest coin per prestige first

1129 turns left: prestige gained now converts 99.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 2 (pies) | mansion | 7 | 54.6 | 54.6 | thin at home: pies |
| hold banquet 3 (pies) | mansion | 8 | 56.8 | 56.8 | thin at home: pies |
| maintain 1 | park | 0.5 | 54.0 | 57.7 | running |
| hold banquet 4 (pies) | mansion | 18 | 58.9 | 58.9 | thin at home: pies |
| hold mass 2 (premium) | cathedral | 360 | 59.4 | 60.2 | needs a cathedral (build cost 297,190); thin at home: furniture, jewellery, glassware, candles, premium garments |
| jousting 1 | arena | 170 | 60.2 | 60.4 | needs a arena (build cost 28,474); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 60.5 | 60.5 | thin at home: cured fish |
| hold feast 2 | townhouse | 2.6 | 58.8 | 61.3 | needs a townhouse (build cost 6,919) |
| jousting 3 | arena | 230 | 61.4 | 61.5 | needs a arena (build cost 28,474); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold sermon 2 (candles) | church | 31 | 59.8 | 62.1 | needs a church (build cost 75,253); thin at home: jewellery, candles, furniture |
| hold banquet 1 (fish) | mansion | 4.2 | 62.8 | 62.8 | running; thin at home: cured fish |
| hold banquet 2 (meat) | mansion | 6.8 | 62.9 | 62.9 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.5 / 0.48 | 53 | - | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 95502502 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Bordetes: nothing pays; crew 0.0; est +0 a turn; best orders clear only -5 a turn after crew: ship stays at 0
- best towns now: Kirchwerp +75, Cobholme +65, Heilegg +42, Toqueque +31, Bedenis +21
- Kirchwerp would trade: acid buy 1 @ 144, cheese buy 16 @ 4.96; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~111 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Birkeningen | 1006 | 0.36 | 0.50 (56/turn) | beer 50 (3.12->4.84), furniture 9 (13.02->16.25), light armour 2 (84->93.1), nails 1 (6.15->8.98) | steel ingots 1 (13.44->14.15) | +85 |
| Kirchwerp | 1072 | 0.40 | 0.20 (22/turn) | flour 2 (21.63->28.31), resin 3 (2.6->3.42), tar 1 (9.9->11.02) | acid 1 (148.05->209), cloth 18 (7.88->8.7), cheese 16 (5.1->5.79) | +81 |
| Toqueque | 642 | 0.19 | 0.10 (11/turn) | cheese 8 (6.46->11.78), salt 9 (4.62->7.36), thread 10 (4.66->5.03), wheels 1 (24.4->25.84) | cloth 17 (7.88->8.7), nails 2 (5.57->5.84) | +77 |
| Cobholme | 1564 | 0.70 | 0.20 (22/turn) | varnish 1 (20.06->21.85), pies 1 (16.7->19) | medicine 1 (142.8->168.15), grindstones 1 (233.1->271.7) | +44 |
| Rouhomme | 368 | 0.11 | 0.50 (56/turn) | mouldboards 1 (60.9->75.52), cheese 9 (6.46->8.07), bread 135 (2.46->2.85), charcoal 2 (2.02->4.22) | tools 2 (5.02->5.15) | +43 |

**Best:** Birkeningen at about +85 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 60 @ min 3.7 | makes 56.0, uses 19.2, holds 370 (keeps 60): sells the surplus + 23/turn of the excess |
| cured fish | 11 @ 26.0, stop 22 |  | uses 5.5/turn (mansion 1), makes 0.0, holds 5 = 0.9 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 8 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 8 = 1.1 turns |
| garments |  | 56 @ min 24.6 | makes 50.0, uses 2.1, holds 177 (keeps 30): sells the surplus + 8/turn of the excess |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 103 = 4.0 turns |
| labour | 698 @ 2.2, stop - |  | uses 1114.2/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 370 = 0.6 turns |
| limestone |  | 5 @ min 22.4 |  |
| meat | 8 @ 3.02, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 8 = 1.1 turns |
| nets |  | 6 @ min 39.8 |  |
| porterage | 33 @ 0.8, stop - |  | uses 29.4/turn (observed), makes 0.0, holds 37 = 1.3 turns |
| rope |  | 4 @ min 85.5 |  |
| timber |  | 27 @ min 8.5 | makes 24.0, uses 0.0, holds 412 (keeps 350): sells the surplus + 3/turn of the excess |
| tools | 8 @ 6.2, stop 63 |  | uses 7.8/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 25.5 turns |
