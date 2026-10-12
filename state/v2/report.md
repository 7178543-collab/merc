# v2 shadow report

Turn 13235, 2026-10-12 20:59. Mode: shadow (reads only; v1 runs the game).
Cash 20,740, prestige 2,553 (133 free, +3.9/turn).

**2 risks, 0 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.5 turns (holds 35, next step uses 76/turn) -> v2: check the step that makes it
- **porterage**: home ask 1.10 is above our ceiling 0.80: the buy can't fill -> v2: raise the ceiling or find another source

## Prestige spending, cheapest coin per prestige first

1166 turns left: prestige gained now converts 99.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: waiting - level 2 costs 250, free 133: ~31 turns at +3.9/turn

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.7 | 50.7 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 56.4 | 56.4 | running; thin at home: cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 58.0 | 58.0 | thin at home: cured fish |
| hold banquet 2 (pies) | mansion | 7 | 58.3 | 58.3 | thin at home: pasties, pies, candles |
| hold sermon 2 (candles) | church | 31 | 56.6 | 58.8 | needs a church (build cost 73,203); thin at home: candles, furniture |
| hold banquet 4 (pies) | mansion | 18 | 59.1 | 59.1 | thin at home: pasties, hop beer, pies, candles |
| hold banquet 3 (pies) | mansion | 8 | 59.2 | 59.2 | thin at home: pasties, hop beer, pies, candles |
| jousting 1 | arena | 170 | 59.8 | 59.9 | needs a arena (build cost 27,392); thin at home: protection, light armour, arms; needs weaponry skill |
| jousting 3 | arena | 230 | 60.0 | 60.1 | needs a arena (build cost 27,392); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold mass 2 (premium) | cathedral | 360 | 59.5 | 60.3 | needs a cathedral (build cost 291,580); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 3 (fish) | mansion | 7.6 | 60.6 | 60.6 | thin at home: hop beer, cured fish |
| hold prayer 2 | chapel | 13 | 58.6 | 61.0 | needs a chapel (build cost 34,961) |

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 25.0, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 51 @ min 3.9 |  |
| cured fish | 7 @ 22.6, stop 20 |  | uses 5.5/turn (mansion 1), makes 0.0, holds 19 = 3.5 turns |
| donations | 40 @ 1.02, stop 40 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ ?, stop 26 |  | uses 6.4/turn (brewery 1, household upkeep), makes 0.0, holds 57 = 9.0 turns |
| fish | 12 @ 1.75, stop 24 |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| garments |  | 37 @ min 22.0 |  |
| grain | 42 @ 2.88, stop 130 |  | uses 32.5/turn (brewery 1), makes 0.0, holds 112 = 3.5 turns |
| labour | 451 @ 1.72, stop - |  | uses 879.2/turn (brewery 1, flax farm 1, household), makes 450.0, holds 410 = 1.0 turns |
| meat | 12 @ 2.4, stop 24 |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 6 @ min 36.0 |  |
| porterage | 26 @ 0.8, stop - |  | uses 23.4/turn (observed), makes 0.0, holds 24 = 1.0 turns |
| timber |  | 24 @ min 8.5 |  |
| tools | 8 @ 5.4, stop 58 |  | uses 7.1/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 27.9 turns |
