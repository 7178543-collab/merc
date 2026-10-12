# v2 shadow report

Turn 13230, 2026-10-12 15:04. Mode: shadow (reads only; v1 runs the game).
Cash 18,321, prestige 2,533 (113 free, +4.0/turn).

**2 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.0 turns (holds 0, next step uses 155/turn) -> v2: check the step that makes it
- **flax plants**: retting pit 1 ran short of flax plants (buy is live (no volume cap @ 2.04), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~50/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 117 labour expired last turn (~217 coin): holding 857 against a ~64 buffer target -> v2: trim the buy until the stock is near 64

## Tuning

- **bread**: home ask 2.68 is above our ceiling 2.60: the buy can't fill -> v2: raise the ceiling or find another source
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Prestige spending, cheapest coin per prestige first

1171 turns left: prestige gained now converts 99.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: waiting - level 2 costs 250, free 113: ~35 turns at +4.0/turn

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 3 (pies) | mansion | 8 | 55.5 | 55.5 | thin at home: pasties, hop beer, pies, candles |
| hold banquet 2 (pies) | mansion | 7 | 55.7 | 55.7 | thin at home: pasties, wine, pies, candles |
| maintain 1 | park | 0.5 | 55.8 | 55.8 | running |
| hold banquet 4 (pies) | mansion | 18 | 58.0 | 58.0 | thin at home: pasties, hop beer, wine, pies, candles |
| hold banquet 2 (fish) | mansion | 6.8 | 58.8 | 58.8 | thin at home: wine |
| hold sermon 2 (candles) | church | 31 | 56.9 | 59.0 | needs a church (build cost 70,832); thin at home: jewellery, candles |
| hold banquet 3 (fish) | mansion | 7.6 | 59.5 | 59.5 | thin at home: hop beer |
| hold prayer 2 | chapel | 13 | 57.8 | 60.1 | needs a chapel (build cost 33,646) |
| hold banquet 1 (fish) | mansion | 4.2 | 60.5 | 60.5 | running |
| jousting 1 | arena | 170 | 60.3 | 60.5 | needs a arena (build cost 26,420); thin at home: protection, light armour, arms; needs weaponry skill |
| hold mass 2 (premium) | cathedral | 360 | 60.1 | 60.9 | needs a cathedral (build cost 285,570); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold sermon 2 | church | 24 | 58.1 | 60.9 | needs a church (build cost 70,832); thin at home: jewellery |

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 51 @ min 3.9 |  |
| bread | 4 @ 2.6, stop 15 |  | uses 3.6/turn (household upkeep), makes 0.0, holds 29 = 8.0 turns |
| cured fish | 7 @ 25.2, stop 20 |  | uses 5.5/turn (mansion 1), makes 0.0, holds 20 = 3.6 turns |
| donations | 40 @ 1.02, stop 40 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 1.7, stop 26 |  | uses 6.4/turn (brewery 1, household upkeep), makes 0.0, holds 57 = 9.0 turns |
| fish | 12 @ 1.72, stop 24 |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| garments |  | 78 @ min 22.0 |  |
| grain | 43 @ 2.86, stop 130 |  | uses 32.5/turn (brewery 1), makes 0.0, holds 110 = 3.4 turns |
| labour | 867 @ 1.89, stop - |  | uses 1274.9/turn (brewery 1, flax farm 1, household), makes 450.0, holds 857 = 1.0 turns |
| meat | 12 @ ?, stop 24 |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 6 @ min 36.0 |  |
| porterage | 26 @ 0.36, stop - |  | uses 23.4/turn (observed), makes 0.0, holds 24 = 1.0 turns |
| timber |  | 24 @ min 8.5 |  |
| tools | 8 @ 5.25, stop 62 |  | uses 7.7/turn (logging camp w/ tool), makes 0.0, holds 199 = 25.9 turns |
