# v2 shadow report

Turn 13229, 2026-10-12 14:06. Mode: shadow (reads only; v1 runs the game).
Cash 18,765, prestige 2,529 (109 free, +4.0/turn).

**2 risks, 1 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.0 turns (holds 0, next step uses 155/turn) -> v2: check the step that makes it
- **flax plants**: retting pit 1 ran short of flax plants (buy is live (no volume cap @ 2.04), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~50/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 70 labour expired last turn (~117 coin): holding 916 against a ~65 buffer target -> v2: trim the buy until the stock is near 65

## Prestige spending, cheapest coin per prestige first

1172 turns left: prestige gained now converts 99.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: waiting - level 2 costs 250, free 109: ~36 turns at +4.0/turn

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.7 | 50.7 | running |
| hold banquet 3 (pies) | mansion | 8 | 52.7 | 52.7 | thin at home: pasties, hop beer, pies |
| hold banquet 2 (pies) | mansion | 7 | 55.6 | 55.6 | thin at home: pasties, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 56.5 | 56.5 | thin at home: hop beer |
| hold banquet 4 (pies) | mansion | 18 | 56.6 | 56.6 | thin at home: pasties, hop beer, pies |
| hold banquet 2 (fish) | mansion | 6.8 | 58.4 | 58.4 |  |
| hold sermon 2 (candles) | church | 31 | 56.3 | 58.4 | needs a church (build cost 70,904); thin at home: jewellery, candles, furniture |
| hold banquet 1 (fish) | mansion | 4.2 | 58.6 | 58.6 | running |
| hold prayer 2 | chapel | 13 | 56.8 | 59.2 | needs a chapel (build cost 33,483) |
| hold sermon 2 | church | 24 | 57.6 | 60.3 | needs a church (build cost 70,904); thin at home: jewellery, furniture |
| hold feast 2 | townhouse | 2.6 | 58.8 | 61.1 | needs a townhouse (build cost 6,935) |
| hold mass 2 (premium) | cathedral | 360 | 60.3 | 61.1 | needs a cathedral (build cost 285,780); thin at home: furniture, jewellery, glassware, candles, premium garments |

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 27.8, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 51 @ min 3.9 |  |
| bread | 4 @ 2.24, stop 15 |  | uses 3.6/turn (household upkeep), makes 0.0, holds 27 = 7.6 turns |
| cured fish | 7 @ 25.0, stop 20 |  | uses 5.5/turn (mansion 1), makes 0.0, holds 19 = 3.5 turns |
| donations | 40 @ 1.02, stop 40 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 1.69, stop 26 |  | uses 6.4/turn (brewery 1, household upkeep), makes 0.0, holds 58 = 9.0 turns |
| fish | 12 @ 1.71, stop 24 |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| garments |  | 78 @ min 22.0 |  |
| grain | 43 @ 2.82, stop 130 |  | uses 32.5/turn (brewery 1), makes 0.0, holds 110 = 3.4 turns |
| labour | 889 @ 1.72, stop - |  | uses 1296.5/turn (brewery 1, flax farm 1, household), makes 450.0, holds 916 = 1.1 turns |
| meat | 12 @ 1.81, stop 24 |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 6 @ min 36.0 |  |
| porterage | 26 @ 0.37, stop - |  | uses 23.4/turn (observed), makes 0.0, holds 24 = 1.0 turns |
| timber |  | 24 @ min 8.5 |  |
| tools | 7 @ 5.25, stop 56 |  | uses 6.9/turn (logging camp w/ tool), makes 0.0, holds 199 = 28.9 turns |
