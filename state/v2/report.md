# v2 shadow report

Turn 13237, 2026-10-12 22:58. Mode: shadow (reads only; v1 runs the game).
Cash 21,607, prestige 2,560 (140 free, +3.8/turn).

**3 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.6 turns (holds 52, next step uses 80/turn) -> v2: check the step that makes it
- **flax plants**: flax plants buffer 0.9 turns (holds 98, next step uses 112/turn) -> v2: check the step that makes it
- **porterage**: home ask 1.10 is above our ceiling 0.80: the buy can't fill -> v2: raise the ceiling or find another source

## Tuning

- **firewood**: home ask 2.50 is above our ceiling 2.40: the buy can't fill -> v2: raise the ceiling or find another source

## Prestige spending, cheapest coin per prestige first

1164 turns left: prestige gained now converts 99.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: waiting - level 2 costs 250, free 140: ~29 turns at +3.8/turn

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.9 | 48.9 | running |
| hold sermon 2 (candles) | church | 31 | 55.3 | 57.4 | needs a church (build cost 68,668); thin at home: candles, furniture |
| jousting 1 | arena | 170 | 58.2 | 58.4 | needs a arena (build cost 25,212); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 58.5 | 58.5 | thin at home: pasties, pies, candles |
| hold banquet 2 (pies) | mansion | 7 | 58.9 | 58.9 | thin at home: pasties, pies, candles |
| hold banquet 1 (fish) | mansion | 4.2 | 59.0 | 59.0 | running |
| hold banquet 4 (pies) | mansion | 18 | 59.1 | 59.1 | thin at home: pasties, pies, candles |
| hold prayer 2 | chapel | 13 | 56.8 | 59.1 | needs a chapel (build cost 31,983) |
| hold sermon 2 | church | 24 | 56.8 | 59.5 | needs a church (build cost 68,668); thin at home: furniture |
| hold mass 2 (premium) | cathedral | 360 | 59.4 | 60.2 | needs a cathedral (build cost 277,265); thin at home: furniture, jewellery, glassware, candles, premium garments |
| jousting 3 | arena | 230 | 61.6 | 61.7 | needs a arena (build cost 25,212); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 62.1 | 62.1 |  |

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 26.2, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 51 @ min 3.9 |  |
| cured fish | 7 @ 25.2, stop 20 |  | uses 5.5/turn (mansion 1), makes 0.0, holds 19 = 3.5 turns |
| donations | 40 @ 1.02, stop 40 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 26 |  | uses 6.4/turn (brewery 1, household upkeep), makes 0.0, holds 58 = 9.0 turns |
| fish | 12 @ 1.71, stop 24 |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| garments |  | 39 @ min 22.0 |  |
| grain | 41 @ 2.92, stop 130 |  | uses 32.5/turn (brewery 1), makes 0.0, holds 114 = 3.5 turns |
| labour | 490 @ 1.66, stop - |  | uses 915.7/turn (brewery 1, flax farm 1, household), makes 450.0, holds 451 = 1.0 turns |
| meat | 12 @ 2.26, stop 24 |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 6 @ min 36.0 |  |
| porterage | 26 @ 0.8, stop - |  | uses 23.4/turn (observed), makes 0.0, holds 24 = 1.0 turns |
| timber |  | 24 @ min 8.5 |  |
| tools | 8 @ 5.25, stop 60 |  | uses 7.5/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 26.6 turns |
