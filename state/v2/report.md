# v2 shadow report

Turn 13241, 2026-10-13 02:44. Mode: handover. v2 runs: cured fish, donations, firewood, fish, grain, meat, nets, porterage; v1 runs everything else.
Cash 23,065, prestige 2,575 (155 free, +3.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| cured fish | 19 | 6 | 6 | 0 | 0 | stop 20, buy 7, buy @ 26 |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 38 | 0 | 6 | 0 | 0 | stop 26, buy 7, buy @ 2.4 |
| fish | 12 | 12 | 6 | 0 | 6 | stop 24, buy 12, buy @ 2.5 |
| grain | 128 | 37 | 32 | 0 | 0 | stop 130, buy 34, buy @ 3.7 |
| meat | 12 | 11 | 6 | 0 | 5 | stop 24, buy 12, buy @ 3.02 |
| nets | 41 | 0 | 0 | 0 | 0 | min_holding 40, sell 6, sell @ 36 |
| porterage | 26 | 26 | 19 | 0 | 7 | buy 26, buy @ 0.8 |

**1 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax plants**: retting pit 1 ran short of flax plants (buy is live (no volume cap @ 2.04), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~32/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 34 labour expired last turn (~56 coin): holding 467 against a ~46 buffer target -> v2: trim the buy until the stock is near 46

## Tuning

- **cloth**: cloth buffer thin: 1.0 turns (target 4) -> v2: lift the maker's rate or hold back sales until it reaches 329
- **timber**: build materials for park 1 are in (444.5 held, 40 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 0% (EXPANSION), about 12 turns left; still to deliver: labour 260, limestone 60, timber 40; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 60 | 153.0 | 0 | off: covered |
| timber | 40 | 444.5 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 22

## Prestige spending, cheapest coin per prestige first

1160 turns left: prestige gained now converts 99.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: waiting - level 2 costs 250, free 155: ~26 turns at +3.7/turn

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.2 | 52.3 | running |
| hold banquet 3 (pies) | mansion | 8 | 56.0 | 56.0 | thin at home: pasties, pies, candles |
| hold banquet 4 (pies) | mansion | 18 | 56.7 | 56.7 | thin at home: pasties, candles |
| hold banquet 2 (pies) | mansion | 7 | 56.9 | 56.9 | thin at home: pasties, pies, candles |
| hold sermon 2 (candles) | church | 31 | 55.3 | 57.4 | needs a church (build cost 70,109); thin at home: jewellery, candles, furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 58.8 | 58.8 | thin at home: cured fish |
| hold mass 2 (premium) | cathedral | 360 | 58.0 | 58.8 | needs a cathedral (build cost 282,720); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold prayer 2 | chapel | 13 | 56.5 | 58.8 | needs a chapel (build cost 33,210) |
| jousting 1 | arena | 170 | 58.7 | 58.8 | needs a arena (build cost 25,822); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 59.1 | 59.1 | thin at home: cured fish |
| hold sermon 2 | church | 24 | 56.4 | 59.1 | needs a church (build cost 70,109); thin at home: jewellery, furniture |
| hold banquet 1 (fish) | mansion | 4.2 | 59.5 | 59.5 | running; thin at home: cured fish |

## Ship routes at today's world prices (estimate, per turn)

28 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~103 coin a turn at full crew (crew is sized to the cargo, floor 0.23). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Fontaux | 411 | 0.11 | 0.55 (56/turn) | garments 18 (21.4->23.56), beer 45 (3.01->3.82), timber 23 (7.5->10.26), charcoal 2 (1.81->4.16) | thread 79 (5.46->5.7), pies 1 (16.17->17.1) | +107 |
| Rouhomme | 368 | 0.10 | 0.23 (24/turn) | beer 68 (3.01->3.67), lead bars 1 (10.61->31.35), cured meat 2 (29.4->37.43) | thread 10 (5.02->5.7), cured fish 5 (26.04->26.4), flax plants 1 (1.67->2.02), tools 7 (5.04->5.15) | +69 |
| Friedwerp | 684 | 0.19 | 0.23 (24/turn) | garments 15 (21.4->24.7), lead bars 5 (10.61->11.59), varnish 1 (18.17->20.52), dyed yarn 1 (8.56->10.07) | thread 10 (5.12->5.7), hop beer 1 (8.66->9.69), leather 1 (23.52->24.51), flax plants 1 (1.22->2.02) | +46 |
| Pontmont | 341 | 0.09 | 0.49 (51/turn) | beer 68 (3.01->3.69), cheese 12 (7.19->7.79), bread 132 (2.42->2.7) | thread 3 (5.57->5.7), yarn 4 (4.3->4.46) | +40 |
| Etallaen | 774 | 0.21 | 0.30 (31/turn) | beer 50 (3.01->3.88), limestone 1 (18.9->35.34), flax plants 2 (1.56->2.24) | hop beer 3 (7.72->9.69) | +36 |

**Best:** Fontaux at about +107 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 28.2, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 61 @ min 3.7 | makes 70.0, uses 18.6, holds 229 (keeps 60): sells the surplus + 10/turn of the excess |
| cured fish | 7 @ 26.0, stop 20 |  | uses 5.5/turn (mansion 1), makes 0.0, holds 19 = 3.5 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 26 |  | uses 6.4/turn (brewery 1, household upkeep), makes 0.0, holds 38 = 5.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 12 = 2.0 turns |
| garments |  | 72 @ min 22.0 | makes 42.2, uses 1.8, holds 448 (keeps 30): sells the surplus + 31/turn of the excess |
| grain | 34 @ 3.7, stop 130 |  | uses 32.5/turn (brewery 1), makes 0.0, holds 128 = 4.0 turns |
| labour | 493 @ 2.2, stop - |  | uses 918.6/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 467 = 1.0 turns |
| light armour | 1 @ 112, stop 1 |  | uses 0.2/turn (household upkeep), makes 0.0, holds 2 = 9.0 turns |
| meat | 7 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 12 = 2.0 turns |
| nets |  | 6 @ min 36.0 |  |
| porterage | 26 @ 0.8, stop - |  | uses 23.4/turn (observed), makes 0.0, holds 26 = 1.1 turns |
| timber |  | 30 @ min 8.5 | makes 24.0, uses 0.0, holds 444 (keeps 350): sells the surplus + 6/turn of the excess |
| tools | 8 @ 6.2, stop 58 |  | uses 7.2/turn (logging camp w/ tool), makes 0.0, holds 199 = 27.6 turns |
