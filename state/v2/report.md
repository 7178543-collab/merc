# v2 shadow report

Turn 13236, 2026-10-12 21:56. Mode: shadow (reads only; v1 runs the game).
Cash 21,182, prestige 2,556 (136 free, +3.8/turn).

**2 risks, 0 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.6 turns (holds 44, next step uses 78/turn) -> v2: check the step that makes it
- **porterage**: home ask 1.10 is above our ceiling 0.80: the buy can't fill -> v2: raise the ceiling or find another source

## Prestige spending, cheapest coin per prestige first

1165 turns left: prestige gained now converts 99.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: waiting - level 2 costs 250, free 136: ~30 turns at +3.8/turn

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.8 | 49.8 | running |
| hold banquet 3 (pies) | mansion | 8 | 56.9 | 56.9 | thin at home: pasties, hop beer, pies |
| hold sermon 2 (candles) | church | 31 | 56.0 | 58.0 | needs a church (build cost 69,632); thin at home: candles, furniture |
| jousting 1 | arena | 170 | 57.9 | 58.0 | needs a arena (build cost 25,582); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 58.7 | 58.7 | thin at home: hop beer, pies |
| jousting 3 | arena | 230 | 59.3 | 59.4 | needs a arena (build cost 25,582); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 59.5 | 59.5 | running; thin at home: cured fish |
| hold banquet 2 (pies) | mansion | 7 | 59.5 | 59.5 | thin at home: pasties, pies |
| hold prayer 2 | chapel | 13 | 57.9 | 60.2 | needs a chapel (build cost 32,599) |
| hold mass 2 (premium) | cathedral | 360 | 59.6 | 60.3 | needs a cathedral (build cost 280,375); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold sermon 2 | church | 24 | 57.7 | 60.4 | needs a church (build cost 69,632); thin at home: furniture |
| hold banquet 3 (fish) | mansion | 7.6 | 62.0 | 62.0 | thin at home: hop beer, cured fish |

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 51 @ min 3.9 |  |
| cured fish | 7 @ 25.8, stop 20 |  | uses 5.5/turn (mansion 1), makes 0.0, holds 20 = 3.6 turns |
| donations | 40 @ 1.02, stop 40 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 1.81, stop 26 |  | uses 6.4/turn (brewery 1, household upkeep), makes 0.0, holds 58 = 9.0 turns |
| fish | 12 @ 1.73, stop 24 |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| garments |  | 38 @ min 22.0 |  |
| grain | 41 @ 2.82, stop 130 |  | uses 32.5/turn (brewery 1), makes 0.0, holds 113 = 3.5 turns |
| labour | 466 @ 1.69, stop - |  | uses 893.0/turn (brewery 1, flax farm 1, household), makes 450.0, holds 434 = 1.0 turns |
| meat | 12 @ 2.32, stop 24 |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 6 @ min 36.0 |  |
| porterage | 26 @ 0.8, stop - |  | uses 23.4/turn (observed), makes 0.0, holds 24 = 1.0 turns |
| timber |  | 24 @ min 8.5 |  |
| tools | 8 @ 5.25, stop 58 |  | uses 7.2/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 27.8 turns |
