# v2 shadow report

Turn 13231, 2026-10-12 16:57. Mode: shadow (reads only; v1 runs the game).
Cash 18,381, prestige 2,537 (117 free, +3.9/turn).

**2 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.0 turns (holds 0, next step uses 114/turn) -> v2: check the step that makes it
- **porterage**: home ask 1.10 is above our ceiling 0.80: the buy can't fill -> v2: raise the ceiling or find another source

## Waste (money lost now)

- **labour**: 64 labour expired last turn (~112 coin): holding 810 against a ~63 buffer target -> v2: trim the buy until the stock is near 63

## Tuning

- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Prestige spending, cheapest coin per prestige first

1170 turns left: prestige gained now converts 99.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: waiting - level 2 costs 250, free 117: ~34 turns at +3.9/turn

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 52.8 | 52.8 | running |
| hold banquet 3 (pies) | mansion | 8 | 56.5 | 56.5 | thin at home: pasties, hop beer, cheese, pies |
| hold banquet 2 (pies) | mansion | 7 | 57.4 | 57.4 | thin at home: pasties, wine, cheese, pies |
| hold banquet 4 (pies) | mansion | 18 | 58.1 | 58.1 | thin at home: pasties, hop beer, wine, cheese, pies |
| hold sermon 2 (candles) | church | 31 | 56.0 | 58.2 | needs a church (build cost 74,565); thin at home: candles |
| hold prayer 2 | chapel | 13 | 57.2 | 59.7 | needs a chapel (build cost 36,340) |
| jousting 1 | arena | 170 | 59.7 | 59.8 | needs a arena (build cost 27,942); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 59.9 | 59.9 | running |
| hold sermon 2 | church | 24 | 57.3 | 60.2 | needs a church (build cost 74,565) |
| hold mass 2 (premium) | cathedral | 360 | 59.6 | 60.4 | needs a cathedral (build cost 295,620); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 2 (fish) | mansion | 6.8 | 60.8 | 60.8 | thin at home: wine, cured fish, cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 61.2 | 61.2 | thin at home: hop beer, cured fish, cheese |

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 24.6, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 51 @ min 3.9 |  |
| cured fish | 7 @ 25.2, stop 20 |  | uses 5.5/turn (mansion 1), makes 0.0, holds 19 = 3.5 turns |
| donations | 40 @ 1.02, stop 40 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ ?, stop 26 |  | uses 6.4/turn (brewery 1, household upkeep), makes 0.0, holds 58 = 9.0 turns |
| fish | 12 @ 1.76, stop 24 |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| garments |  | 56 @ min 22.0 |  |
| grain | 43 @ 3.08, stop 130 |  | uses 32.5/turn (brewery 1), makes 0.0, holds 110 = 3.4 turns |
| labour | 833 @ 1.79, stop - |  | uses 1243.3/turn (brewery 1, flax farm 1, household), makes 450.0, holds 810 = 1.0 turns |
| meat | 12 @ ?, stop 24 |  | uses 6.0/turn (household upkeep), makes 0.0, holds 4 = 0.7 turns |
| nets |  | 6 @ min 36.0 |  |
| porterage | 26 @ 0.8, stop - |  | uses 23.4/turn (observed), makes 0.0, holds 24 = 1.0 turns |
| timber |  | 24 @ min 8.5 |  |
| tools | 9 @ 5.4, stop 68 |  | uses 8.5/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 23.5 turns |
