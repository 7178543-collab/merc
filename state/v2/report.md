# v2 shadow report

Turn 13232, 2026-10-12 17:57. Mode: shadow (reads only; v1 runs the game).
Cash 19,793, prestige 2,541 (121 free, +3.6/turn).

**3 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.1 turns (holds 9, next step uses 118/turn) -> v2: check the step that makes it
- **flax plants**: flax plants buffer 0.9 turns (holds 141, next step uses 158/turn) -> v2: check the step that makes it
- **porterage**: home ask 1.10 is above our ceiling 0.80: the buy can't fill -> v2: raise the ceiling or find another source

## Waste (money lost now)

- **labour**: 128 labour expired last turn (~225 coin): holding 693 against a ~59 buffer target -> v2: trim the buy until the stock is near 59

## Tuning

- **meat**: home ask 2.70 is above our ceiling 2.40: the buy can't fill -> v2: raise the ceiling or find another source

## Prestige spending, cheapest coin per prestige first

1169 turns left: prestige gained now converts 99.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: waiting - level 2 costs 250, free 121: ~36 turns at +3.6/turn

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 52.8 | 52.8 | running |
| hold banquet 3 (pies) | mansion | 8 | 53.1 | 53.1 | thin at home: pasties, hop beer, cheese, pies, candles |
| hold banquet 2 (pies) | mansion | 7 | 56.2 | 56.2 | thin at home: pasties, cheese, pies, candles |
| hold banquet 4 (pies) | mansion | 18 | 56.7 | 56.7 | thin at home: pasties, hop beer, cheese, pies, candles |
| hold banquet 3 (fish) | mansion | 7.6 | 56.9 | 56.9 | thin at home: hop beer, cheese |
| hold sermon 2 (candles) | church | 31 | 56.0 | 58.1 | needs a church (build cost 71,305); thin at home: candles |
| jousting 1 | arena | 170 | 58.6 | 58.8 | needs a arena (build cost 26,358); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 59.2 | 59.2 | thin at home: cheese |
| hold prayer 2 | chapel | 13 | 57.3 | 59.7 | needs a chapel (build cost 33,838) |
| hold banquet 1 (fish) | mansion | 4.2 | 59.8 | 59.8 | running |
| hold sermon 2 | church | 24 | 57.4 | 60.2 | needs a church (build cost 71,305) |
| hold mass 2 (premium) | cathedral | 360 | 59.5 | 60.3 | needs a cathedral (build cost 286,515); thin at home: furniture, jewellery, glassware, candles, premium garments |

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 51 @ min 3.9 |  |
| cured fish | 7 @ 25.2, stop 20 |  | uses 5.5/turn (mansion 1), makes 0.0, holds 20 = 3.6 turns |
| donations | 40 @ 1.02, stop 40 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 1.78, stop 26 |  | uses 6.4/turn (brewery 1, household upkeep), makes 0.0, holds 58 = 9.0 turns |
| fish | 12 @ 1.76, stop 24 |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| garments |  | 58 @ min 22.0 |  |
| grain | 42 @ 2.78, stop 130 |  | uses 32.5/turn (brewery 1), makes 0.0, holds 111 = 3.4 turns |
| labour | 752 @ 1.79, stop - |  | uses 1165.5/turn (brewery 1, flax farm 1, household), makes 450.0, holds 693 = 1.0 turns |
| meat | 8 @ 2.4, stop 16 |  | uses 4.0/turn (household upkeep), makes 0.0, holds 6 = 1.5 turns |
| nets |  | 6 @ min 36.0 |  |
| porterage | 26 @ 0.8, stop - |  | uses 23.4/turn (observed), makes 0.0, holds 24 = 1.0 turns |
| timber |  | 24 @ min 8.5 |  |
| tools | 9 @ 5.4, stop 69 |  | uses 8.5/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 23.4 turns |
