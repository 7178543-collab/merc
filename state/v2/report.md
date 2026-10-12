# v2 shadow report

Turn 13222, 2026-10-12 07:09. Mode: shadow (reads only; v1 runs the game).
Cash 21,055, prestige 2,501 (81 free, +4.1/turn).

**2 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.4 turns (holds 71, next step uses 160/turn) -> v2: check the step that makes it
- **porterage**: home ask 1.10 is above our ceiling 0.80: the buy can't fill -> v2: raise the ceiling or find another source

## Tuning

- **timber**: build materials for ropewalk 1, quarry 1 are in (395.1 held, 73 needed) but a buy is still live -> v2: switch the timber buy off
- **wheels**: build materials for ropewalk 1, quarry 1 are in (13.0 held, 4 needed) but a buy is still live -> v2: switch the wheels buy off

## Builds under construction

- **ropewalk 1** 75% (INITIAL), about 6 turns left; still to deliver: labour 100, timber 65, tools 5, wheels 4; ready for labour
- **quarry 1** 94% (INITIAL), about 2 turns left; still to deliver: labour 49, timber 8, tools 2; ready for labour
  - note: game data lists a 20 discount on this build; not applied, so this buys slightly more than needed

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| timber | 73 | 395.1 | 0 | off: covered; switch v1's buy off |
| tools | 7 | 199.7 | 0 | off: covered |
| wheels | 4 | 13.0 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 42

## Prestige spending, cheapest coin per prestige first

1179 turns left: prestige gained now converts 99.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: waiting - level 2 costs 250, free 81: ~42 turns at +4.1/turn

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.1 | 50.1 | running |
| hold banquet 3 (pies) | mansion | 8 | 57.6 | 57.6 | thin at home: pasties, hop beer, cheese, pies, candles |
| hold sermon 2 | church | 24 | 54.9 | 57.6 | needs a church (build cost 69,547); thin at home: jewellery, furniture |
| hold sermon 2 (candles) | church | 31 | 55.6 | 57.7 | needs a church (build cost 69,547); thin at home: jewellery, candles, furniture |
| hold banquet 2 (pies) | mansion | 7 | 58.0 | 58.0 | thin at home: pasties, cheese, pies, candles |
| hold banquet 1 (fish) | mansion | 4.2 | 58.1 | 58.1 | running |
| hold prayer 2 | chapel | 13 | 56.0 | 58.3 | needs a chapel (build cost 33,291); thin at home: furniture |
| hold banquet 4 (pies) | mansion | 18 | 58.9 | 58.9 | thin at home: pasties, hop beer, cheese, pies, candles |
| hold mass 2 (premium) | cathedral | 360 | 58.4 | 59.1 | needs a cathedral (build cost 281,580); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold feast 2 | townhouse | 2.6 | 58.0 | 60.2 | needs a townhouse (build cost 6,548); thin at home: wine |
| hold banquet 2 (fish) | mansion | 6.8 | 61.1 | 61.1 | thin at home: cheese |
| jousting 1 | arena | 170 | 61.1 | 61.2 | needs a arena (build cost 26,165); thin at home: protection, light armour, arms; needs weaponry skill |

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 51 @ min 3.9 |  |
| bread | 4 @ 2.18, stop 15 |  | uses 3.6/turn (household upkeep), makes 0.0, holds 18 = 4.9 turns |
| cured fish | 7 @ 25.0, stop 20 |  | uses 5.5/turn (mansion 1), makes 0.0, holds 20 = 3.6 turns |
| donations | 40 @ 1.02, stop 40 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 1.77, stop 26 |  | uses 6.4/turn (brewery 1, household upkeep), makes 0.0, holds 58 = 9.0 turns |
| fish | 12 @ 1.7, stop 24 |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| garments |  | 80 @ min 22.0 |  |
| grain | 45 @ 2.82, stop 130 |  | uses 32.5/turn (brewery 1), makes 0.0, holds 106 = 3.3 turns |
| labour | 972 @ 1.7, stop - |  | uses 1375.7/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 891 = 1.0 turns |
| meat | 12 @ 2.12, stop 24 |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 6 @ min 36.0 |  |
| porterage | 26 @ 0.8, stop - |  | uses 23.4/turn (observed), makes 0.0, holds 24 = 1.0 turns |
| timber |  | 24 @ min 8.5 |  |
| tools | 10 @ 5.4, stop 80 |  | uses 10.0/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 20.1 turns |
