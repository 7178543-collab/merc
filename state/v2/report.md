# v2 shadow report

Turn 13228, 2026-10-12 13:19. Mode: shadow (reads only; v1 runs the game).
Cash 19,329, prestige 2,525 (105 free, +4.0/turn).

**2 risks, 0 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.0 turns (holds 7, next step uses 155/turn) -> v2: check the step that makes it
- **flax plants**: flax plants buffer 0.9 turns (holds 158, next step uses 178/turn) -> v2: check the step that makes it

## Prestige spending, cheapest coin per prestige first

1173 turns left: prestige gained now converts 99.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: waiting - level 2 costs 250, free 105: ~37 turns at +4.0/turn

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.4 | 50.4 | running |
| hold banquet 3 (pies) | mansion | 8 | 52.2 | 52.2 | thin at home: pasties, hop beer, pies |
| hold banquet 2 (pies) | mansion | 7 | 56.0 | 56.0 | thin at home: pasties, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 56.2 | 56.2 | thin at home: hop beer |
| hold banquet 4 (pies) | mansion | 18 | 56.4 | 56.4 | thin at home: pasties, hop beer, pies |
| hold sermon 2 (candles) | church | 31 | 55.6 | 57.7 | needs a church (build cost 69,853); thin at home: jewellery, candles |
| hold banquet 1 (fish) | mansion | 4.2 | 58.6 | 58.6 | running |
| hold prayer 2 | chapel | 13 | 56.6 | 58.8 | needs a chapel (build cost 32,564) |
| hold banquet 2 (fish) | mansion | 6.8 | 59.0 | 59.0 |  |
| jousting 1 | arena | 170 | 59.4 | 59.5 | needs a arena (build cost 25,474); thin at home: protection, light armour, arms; needs weaponry skill |
| hold sermon 2 | church | 24 | 57.5 | 60.2 | needs a church (build cost 69,853); thin at home: jewellery |
| hold mass 2 (premium) | cathedral | 360 | 60.1 | 60.8 | needs a cathedral (build cost 281,660); thin at home: furniture, jewellery, glassware, candles, premium garments |

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 51 @ min 3.9 |  |
| bread | 4 @ 2.24, stop 15 |  | uses 3.6/turn (household upkeep), makes 0.0, holds 26 = 7.2 turns |
| cured fish | 7 @ 25.2, stop 20 |  | uses 5.5/turn (mansion 1), makes 0.0, holds 20 = 3.6 turns |
| donations | 40 @ 1.02, stop 40 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 1.68, stop 26 |  | uses 6.4/turn (brewery 1, household upkeep), makes 0.0, holds 57 = 8.9 turns |
| fish | 12 @ 1.7, stop 24 |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| garments |  | 78 @ min 22.0 |  |
| grain | 43 @ 2.72, stop 130 |  | uses 32.5/turn (brewery 1), makes 0.0, holds 109 = 3.4 turns |
| labour | 919 @ 1.71, stop - |  | uses 1324.4/turn (brewery 1, flax farm 1, household), makes 450.0, holds 916 = 1.0 turns |
| meat | 12 @ 1.84, stop 24 |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 6 @ min 36.0 |  |
| porterage | 26 @ 0.37, stop - |  | uses 23.4/turn (observed), makes 0.0, holds 24 = 1.0 turns |
| timber |  | 24 @ min 8.5 |  |
| tools | 9 @ 5.4, stop 72 |  | uses 9.0/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 22.2 turns |
