# v2 shadow report

Turn 13234, 2026-10-12 19:57. Mode: shadow (reads only; v1 runs the game).
Cash 20,284, prestige 2,549 (129 free, +3.9/turn).

**2 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.3 turns (holds 26, next step uses 76/turn) -> v2: check the step that makes it
- **porterage**: home ask 1.10 is above our ceiling 0.80: the buy can't fill -> v2: raise the ceiling or find another source

## Waste (money lost now)

- **labour**: 293 labour expired last turn (~505 coin): holding 403 against a ~44 buffer target -> v2: trim the buy until the stock is near 44

## Tuning

- **meat**: home ask 2.44 is above our ceiling 2.40: the buy can't fill -> v2: raise the ceiling or find another source

## Prestige spending, cheapest coin per prestige first

1167 turns left: prestige gained now converts 99.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: waiting - level 2 costs 250, free 129: ~32 turns at +3.9/turn

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.6 | 51.6 | running |
| hold banquet 3 (pies) | mansion | 8 | 54.7 | 54.7 | thin at home: pasties, hop beer, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 56.6 | 56.6 | thin at home: hop beer, cheese |
| hold banquet 4 (pies) | mansion | 18 | 56.9 | 56.9 | thin at home: pasties, hop beer, pies |
| hold banquet 2 (pies) | mansion | 7 | 57.5 | 57.5 | thin at home: pasties, cheese, pies |
| hold sermon 2 (candles) | church | 31 | 55.7 | 57.8 | needs a church (build cost 71,094); thin at home: candles |
| hold banquet 2 (fish) | mansion | 6.8 | 58.2 | 58.2 | thin at home: cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 59.0 | 59.0 | running |
| hold prayer 2 | chapel | 13 | 57.3 | 59.6 | needs a chapel (build cost 33,728) |
| hold sermon 2 | church | 24 | 57.3 | 60.1 | needs a church (build cost 71,094) |
| hold mass 2 (premium) | cathedral | 360 | 59.5 | 60.3 | needs a cathedral (build cost 285,775); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 4 | mansion | 17.5 | 60.9 | 60.9 | thin at home: hop beer, stockfish |

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 51 @ min 3.9 |  |
| cured fish | 7 @ 25.2, stop 20 |  | uses 5.5/turn (mansion 1), makes 0.0, holds 20 = 3.6 turns |
| donations | 40 @ 1.02, stop 40 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ ?, stop 26 |  | uses 6.4/turn (brewery 1, household upkeep), makes 0.0, holds 58 = 9.0 turns |
| fish | 12 @ 1.76, stop 24 |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| garments |  | 37 @ min 22.0 |  |
| grain | 42 @ 3.14, stop 130 |  | uses 32.5/turn (brewery 1), makes 0.0, holds 112 = 3.4 turns |
| labour | 451 @ 1.75, stop - |  | uses 879.2/turn (brewery 1, flax farm 1, household), makes 450.0, holds 403 = 0.9 turns |
| meat | 12 @ 2.4, stop 24 |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 6 @ min 36.0 |  |
| porterage | 26 @ 0.8, stop - |  | uses 23.4/turn (observed), makes 0.0, holds 24 = 1.0 turns |
| timber |  | 24 @ min 8.5 |  |
| tools | 8 @ 5.3, stop 58 |  | uses 7.1/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 27.9 turns |
