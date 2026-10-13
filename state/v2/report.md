# v2 shadow report

Turn 13239, 2026-10-13 00:36. Mode: handover. v2 runs: cured fish, donations, firewood, fish, grain, meat, nets, porterage; v1 runs everything else.
Cash 22,167, prestige 2,568 (148 free, +3.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| cured fish | 19 | 6 | 6 | 0 | 0 | stop 20, buy 7, buy @ 26 |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 51 | 6 | 6 | 0 | 0 | stop 26, buy 7, buy @ 2.4 |
| fish | 12 | 6 | 6 | 0 | 0 | stop 24, buy 12, buy @ 2.5 |
| grain | 122 | 33 | 32 | 0 | 0 | stop 130, buy 37, buy @ 3.7 |
| meat | 6 | 6 | 6 | 0 | 0 | buy 6, buy @ 3.02 |
| nets | 41 | 0 | 0 | 0 | 0 | min_holding 40, sell 6, sell @ 36 |
| porterage | 24 | 24 | 19 | 0 | 5 | buy 26, buy @ 0.8 |

**2 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.8 turns (holds 67, next step uses 80/turn) -> v2: check the step that makes it
- **flax plants**: retting pit 1 ran short of flax plants (buy is live (no volume cap @ 2.04), home ask 2.02 x1, yet 0 bought last turn); labour need rises ~31/turn when they restart -> v2: find out why the buy isn't filling

## Tuning

- **timber**: build materials for park 1 are in (429.0 held, 40 needed) but a buy is still live -> v2: switch the timber buy off

## Builds under construction

- **park 1** 0% (EXPANSION), about 12 turns left; still to deliver: labour 260, limestone 60, timber 40; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| limestone | 60 | 153.0 | 0 | off: covered |
| timber | 40 | 429.0 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 22

## Prestige spending, cheapest coin per prestige first

1162 turns left: prestige gained now converts 99.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: waiting - level 2 costs 250, free 148: ~28 turns at +3.8/turn

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.5 | 52.6 | running |
| hold banquet 2 (pies) | mansion | 7 | 56.7 | 56.7 | thin at home: pies, candles |
| hold sermon 2 (candles) | church | 31 | 54.9 | 57.0 | needs a church (build cost 69,552); thin at home: jewellery, candles, furniture |
| jousting 1 | arena | 170 | 57.4 | 57.6 | needs a arena (build cost 25,824); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 58.2 | 58.2 | thin at home: pies, candles |
| hold banquet 4 (pies) | mansion | 18 | 58.6 | 58.6 | thin at home: candles |
| hold prayer 2 | chapel | 13 | 56.3 | 58.6 | needs a chapel (build cost 33,016) |
| hold sermon 2 | church | 24 | 56.1 | 58.8 | needs a church (build cost 69,552); thin at home: jewellery, furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 59.2 | 59.2 | thin at home: cured fish |
| jousting 3 | arena | 230 | 59.1 | 59.3 | needs a arena (build cost 25,824); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 59.7 | 59.7 | running; thin at home: cured fish |
| hold mass 2 (premium) | cathedral | 360 | 59.1 | 59.8 | needs a cathedral (build cost 279,575); thin at home: furniture, jewellery, glassware, candles, premium garments |

## Ship routes at today's world prices (estimate)

91 towns by sea; one ship, 250 units each way, 150 moves/turn at crew 0.5, crew ~266 coin/turn, 5% slippage. Only what each market can take right now is counted.

| Town | Trip turns | Out (sell there) | Back (buy there) | Gross | Crew | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Fontaux | 8 | timber 23 (7.5->10.26), firewood 4 (1.67->4.07), charcoal 5 (1.81->4.16), garments 18 (21.4->23.56) | pies 1 (16.17->17.1), thread 79 (5.46->5.7) | 164 | 2128 | -246 |
| Neuborn | 14 | limestone 1 (18.9->28.5), bricks 9 (4.48->9.5), firewood 21 (1.67->6.41), timber 14 (7.5->11.4) | flax fibres 5 (5.83->6.27), leather 1 (24.15->24.51), thread 8 (5.41->5.7), fleece 1 (6.46->6.55) | 248 | 3724 | -248 |
| Kirchwerp | 18 | lead ore 1 (7.98->13.87), timber 4 (7.5->11.88), firewood 16 (1.67->5.7), lead bars 5 (10.61->13.3) | hop beer 3 (9.19->9.69), flax fibres 5 (6.09->6.27), flax plants 2 (1.99->2.02), beer 12 (3.7->3.7) | 247 | 4788 | -252 |
| Angefont | 12 | tackles 1 (158.55->165.3), arms 3 (23.2->27.17), bricks 3 (4.48->6.84), firewood 44 (1.67->3.8) | yarn 2 (3.57->4.46), thread 18 (5.51->5.7), flax plants 1 (1.91->2.02), honey 2 (7.88->7.89) | 149 | 3192 | -254 |
| Heilegg | 14 | firewood 10 (1.67->3.38), varnish 1 (18.17->19.76), charcoal 34 (1.81->3.31), logs 1 (3.24->4.64) | hop beer 3 (7.67->9.69), tallow 1 (24.78->25.46), flax fibres 5 (5.83->6.27), wax 4 (23.31->23.75) | 157 | 3724 | -255 |

**Verdict:** no route pays at these prices; keep the ships parked (crew costs more than the trade margin).

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 26.2, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 65 @ min 3.7 | makes 70.0, uses 18.6, holds 278 (keeps 60): sells the surplus + 14/turn of the excess |
| cured fish | 7 @ 26.0, stop 20 |  | uses 5.5/turn (mansion 1), makes 0.0, holds 19 = 3.5 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 26 |  | uses 6.4/turn (brewery 1, household upkeep), makes 0.0, holds 51 = 7.9 turns |
| fish | 12 @ 2.5, stop 24 |  | uses 6.0/turn (household upkeep), makes 0.0, holds 12 = 2.0 turns |
| garments |  | 73 @ min 22.0 | makes 41.0, uses 1.8, holds 478 (keeps 30): sells the surplus + 34/turn of the excess |
| grain | 37 @ 3.7, stop 130 |  | uses 32.5/turn (brewery 1), makes 0.0, holds 122 = 3.8 turns |
| labour | 480 @ 2.2, stop - |  | uses 906.8/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 491 = 1.1 turns |
| meat | 12 @ 3.02, stop 24 |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 6 @ min 36.0 |  |
| porterage | 26 @ 0.8, stop - |  | uses 23.4/turn (observed), makes 0.0, holds 24 = 1.0 turns |
| timber |  | 29 @ min 8.5 | makes 24.0, uses 0.0, holds 429 (keeps 350): sells the surplus + 5/turn of the excess |
| tools | 8 @ 6.2, stop 58 |  | uses 7.2/turn (logging camp w/ tool), makes 0.0, holds 200 = 27.7 turns |
