# v2 shadow report

Turn 13240, 2026-10-13 01:01. Mode: handover. v2 runs: cured fish, donations, firewood, fish, grain, meat, nets, porterage; v1 runs everything else.
Cash 22,520, prestige 2,572 (152 free, +3.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| cured fish | 20 | 5 | 6 | 0 | 0 | stop 20, buy 7, buy @ 26 |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 44 | 0 | 6 | 0 | 0 | stop 26, buy 7, buy @ 2.4 |
| fish | 12 | 12 | 6 | 0 | 6 | stop 24, buy 12, buy @ 2.5 |
| grain | 127 | 41 | 32 | 0 | 0 | stop 130, buy 37, buy @ 3.7 |
| meat | 11 | 6 | 6 | 0 | 0 | stop 24, buy 12, buy @ 3.02 |
| nets | 41 | 0 | 0 | 0 | 0 | min_holding 40, sell 6, sell @ 36 |
| porterage | 26 | 24 | 19 | 0 | 5 | buy 26, buy @ 0.8 |

**2 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.9 turns (holds 75, next step uses 80/turn) -> v2: check the step that makes it
- **flax plants**: retting pit 1 ran short of flax plants (buy is live (no volume cap @ 2.04), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~31/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 34 labour expired last turn (~56 coin): holding 491 against a ~46 buffer target -> v2: trim the buy until the stock is near 46

## Tuning

- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **timber**: build materials for park 1 are in (432.7 held, 40 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 0% (EXPANSION), about 12 turns left; still to deliver: labour 260, limestone 60, timber 40; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 60 | 153.0 | 0 | off: covered |
| timber | 40 | 432.7 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 22

## Prestige spending, cheapest coin per prestige first

1161 turns left: prestige gained now converts 99.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: waiting - level 2 costs 250, free 152: ~27 turns at +3.8/turn

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.5 | 52.5 | running |
| hold banquet 2 (pies) | mansion | 7 | 57.2 | 57.2 | thin at home: pies, candles |
| hold sermon 2 (candles) | church | 31 | 55.1 | 57.2 | needs a church (build cost 70,166); thin at home: jewellery, candles, furniture |
| jousting 1 | arena | 170 | 57.7 | 57.9 | needs a arena (build cost 25,676); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 58.3 | 58.3 | thin at home: pies, candles |
| hold prayer 2 | chapel | 13 | 56.3 | 58.6 | needs a chapel (build cost 33,269) |
| hold banquet 4 (pies) | mansion | 18 | 58.8 | 58.8 | thin at home: candles |
| hold sermon 2 | church | 24 | 56.1 | 58.8 | needs a church (build cost 70,166); thin at home: jewellery, furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 59.2 | 59.2 | thin at home: cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 59.4 | 59.4 | running |
| jousting 3 | arena | 230 | 59.4 | 59.5 | needs a arena (build cost 25,676); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold mass 2 (premium) | cathedral | 360 | 59.0 | 59.8 | needs a cathedral (build cost 283,045); thin at home: furniture, jewellery, glassware, candles, premium garments |

## Ship routes at today's world prices (estimate, per turn)

28 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~103 coin a turn at full crew (crew is sized to the cargo, floor 0.23). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost/unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Fontaux | 411 | 0.11 | 0.23 (24/turn) | timber 23 (7.5->10.26), garments 18 (21.4->23.56), beer 45 (3.01->3.82), firewood 3 (1.67->4.07) | thread 79 (5.46->5.7), pies 1 (16.17->17.1) | +152 |
| Neuborn | 780 | 0.21 | 0.28 (28/turn) | timber 14 (7.5->11.4), lodging 30 (5.04->6.84), firewood 3 (1.67->6.41), limestone 1 (18.9->28.5) | flax fibres 5 (5.83->6.27), thread 8 (5.41->5.7), leather 1 (24.15->24.51) | +130 |
| Pontmont | 341 | 0.09 | 0.23 (24/turn) | beer 68 (3.01->3.69), bread 132 (2.42->2.7), protection 40 (3.97->4.69), cheese 12 (7.19->7.79) | thread 3 (5.57->5.7), yarn 4 (4.3->4.46) | +88 |
| Rouhomme | 368 | 0.10 | 0.23 (24/turn) | beer 68 (3.01->3.67), lead bars 1 (10.61->31.35), cured meat 2 (29.4->37.43), meat 4 (2.21->4.75) | thread 10 (5.02->5.7), cured fish 5 (26.04->26.4), flax plants 1 (1.67->2.02), tools 7 (5.04->5.15) | +79 |
| Etallaen | 774 | 0.21 | 0.26 (26/turn) | beer 50 (3.01->3.88), limestone 1 (18.9->35.34), lodging 30 (5.04->5.65), protection 23 (3.97->4.52) | hop beer 3 (7.72->9.69), flax fibres 1 (6.04->6.27) | +67 |

**Best:** Fontaux at about +152 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 65 @ min 3.7 | makes 70.0, uses 18.6, holds 271 (keeps 60): sells the surplus + 13/turn of the excess |
| cured fish | 7 @ 26.0, stop 20 |  | uses 5.5/turn (mansion 1), makes 0.0, holds 20 = 3.6 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 26 |  | uses 6.4/turn (brewery 1, household upkeep), makes 0.0, holds 44 = 6.9 turns |
| fish | 12 @ 2.5, stop 24 |  | uses 6.0/turn (household upkeep), makes 0.0, holds 12 = 2.0 turns |
| garments |  | 72 @ min 22.0 | makes 41.0, uses 1.8, holds 463 (keeps 30): sells the surplus + 33/turn of the excess |
| grain | 34 @ 3.7, stop 130 |  | uses 32.5/turn (brewery 1), makes 0.0, holds 127 = 3.9 turns |
| labour | 480 @ 2.2, stop - |  | uses 906.8/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 491 = 1.1 turns |
| meat | 12 @ 3.02, stop 24 |  | uses 6.0/turn (household upkeep), makes 0.0, holds 11 = 1.8 turns |
| nets |  | 6 @ min 36.0 |  |
| porterage | 26 @ 0.8, stop - |  | uses 23.4/turn (observed), makes 0.0, holds 26 = 1.1 turns |
| timber |  | 29 @ min 8.5 | makes 24.0, uses 0.0, holds 433 (keeps 350): sells the surplus + 5/turn of the excess |
| tools | 8 @ 6.2, stop 58 |  | uses 7.2/turn (logging camp w/ tool), makes 0.0, holds 200 = 27.6 turns |
