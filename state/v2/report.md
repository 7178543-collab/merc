# v2 shadow report

Turn 13226, 2026-10-12 11:02. Mode: shadow (reads only; v1 runs the game).
Cash 19,869, prestige 2,517 (97 free, +4.0/turn).

**1 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.2 turns (holds 25, next step uses 160/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **labour**: 53 labour expired last turn (~87 coin): holding 867 against a ~68 buffer target -> v2: trim the buy until the stock is near 68

## Tuning

- **timber**: build materials for ropewalk 1 are in (442.9 held, 24 needed) but a buy is still live -> v2: switch the timber buy off
- **wheels**: build materials for ropewalk 1 are in (13.0 held, 2 needed) but a buy is still live -> v2: switch the wheels buy off

## Builds under construction

- **ropewalk 1** 91% (INITIAL), about 3 turns left; still to deliver: labour 36, timber 24, tools 2, wheels 2; ready for labour

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| timber | 24 | 442.9 | 0 | off: covered; switch v1's buy off |
| tools | 2 | 199.4 | 0 | off: covered |
| wheels | 2 | 13.0 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 12

## Prestige spending, cheapest coin per prestige first

1175 turns left: prestige gained now converts 99.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: waiting - level 2 costs 250, free 97: ~38 turns at +4.0/turn

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.2 | 49.2 | running |
| hold banquet 3 (pies) | mansion | 8 | 54.6 | 54.6 | thin at home: pasties, hop beer, pies |
| hold sermon 2 (candles) | church | 31 | 53.6 | 55.6 | needs a church (build cost 67,996); thin at home: jewellery, candles, furniture |
| hold banquet 2 (pies) | mansion | 7 | 56.0 | 56.0 | thin at home: pasties, pies |
| hold banquet 4 (pies) | mansion | 18 | 56.9 | 56.9 | thin at home: pasties, hop beer, pies |
| hold sermon 2 | church | 24 | 54.9 | 57.5 | needs a church (build cost 67,996); thin at home: jewellery, furniture |
| hold prayer 2 | chapel | 13 | 56.0 | 58.2 | needs a chapel (build cost 32,392) |
| hold banquet 1 (fish) | mansion | 4.2 | 58.4 | 58.4 | running |
| hold mass 2 (premium) | cathedral | 360 | 57.7 | 58.5 | needs a cathedral (build cost 275,900); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 2 (fish) | mansion | 6.8 | 59.4 | 59.4 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 59.5 | 59.5 | thin at home: hop beer |
| hold feast 2 | townhouse | 2.6 | 57.6 | 59.8 | needs a townhouse (build cost 6,686) |

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 51 @ min 3.9 |  |
| bread | 4 @ 2.2, stop 15 |  | uses 3.6/turn (household upkeep), makes 0.0, holds 23 = 6.4 turns |
| cured fish | 7 @ 25.0, stop 20 |  | uses 5.5/turn (mansion 1), makes 0.0, holds 20 = 3.6 turns |
| donations | 40 @ 1.02, stop 40 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 1.7, stop 26 |  | uses 6.4/turn (brewery 1, household upkeep), makes 0.0, holds 58 = 9.0 turns |
| fish | 12 @ 1.69, stop 24 |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| garments |  | 80 @ min 22.0 |  |
| grain | 44 @ 3.36, stop 130 |  | uses 32.5/turn (brewery 1), makes 0.0, holds 108 = 3.3 turns |
| labour | 941 @ 1.67, stop - |  | uses 1345.7/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 867 = 1.0 turns |
| meat | 12 @ 1.92, stop 24 |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 6 @ min 36.0 |  |
| porterage | 26 @ 0.38, stop - |  | uses 23.4/turn (observed), makes 0.0, holds 24 = 1.0 turns |
| timber |  | 24 @ min 8.5 |  |
| tools | 9 @ 5.25, stop 72 |  | uses 9.0/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 22.2 turns |
