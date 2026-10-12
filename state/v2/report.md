# v2 shadow report

Turn 13217, 2026-10-12 02:59. Mode: shadow (reads only; v1 runs the game).
Cash 24,451, prestige 2,480 (60 free, +3.9/turn).

**2 risks, 1 waste, 4 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.8 turns (holds 129, next step uses 160/turn) -> v2: check the step that makes it
- **porterage**: home ask 1.10 is above our ceiling 0.80: the buy can't fill -> v2: raise the ceiling or find another source

## Waste (money lost now)

- **labour**: 47 labour expired last turn (~78 coin): holding 891 against a ~70 buffer target -> v2: trim the buy until the stock is near 70

## Tuning

- **bread**: home ask 2.68 is above our ceiling 2.60: the buy can't fill -> v2: raise the ceiling or find another source
- **meat**: home ask 2.52 is above our ceiling 2.40: the buy can't fill -> v2: raise the ceiling or find another source
- **timber**: build materials for ropewalk 1, quarry 1 are in (295.3 held, 161 needed) but a buy is still live -> v2: switch the timber buy off
- **wheels**: build materials for ropewalk 1, quarry 1 are in (13.0 held, 8 needed) but a buy is still live -> v2: switch the wheels buy off

## Builds under construction

- **ropewalk 1** 54% (INITIAL), about 12 turns left; still to deliver: labour 184, timber 120, tools 10, wheels 8; ready for labour
- **quarry 1** 66% (INITIAL), about 7 turns left; still to deliver: labour 272, timber 41, tools 7; ready for labour
  - note: game data lists a 20 discount on this build; not applied, so this buys slightly more than needed

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| timber | 161 | 295.3 | 0 | off: covered; switch v1's buy off |
| tools | 17 | 199.5 | 0 | off: covered |
| wheels | 8 | 13.0 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 55

## Prestige spending, cheapest coin per prestige first

1184 turns left: prestige gained now converts 99.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: waiting - level 2 costs 250, free 60: ~49 turns at +3.9/turn

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.4 | 50.4 | running |
| hold sermon 2 (candles) | church | 31 | 53.0 | 55.1 | needs a church (build cost 73,411); thin at home: jewellery, candles |
| hold banquet 3 (pies) | mansion | 8 | 55.2 | 55.2 | thin at home: pasties, hop beer, cheese, pies, candles |
| hold banquet 2 (pies) | mansion | 7 | 56.2 | 56.2 | thin at home: pasties, wine, cheese, pies, candles |
| hold banquet 4 (pies) | mansion | 18 | 57.6 | 57.6 | thin at home: pasties, hop beer, wine, pies, candles |
| hold sermon 2 | church | 24 | 55.0 | 57.8 | needs a church (build cost 73,411); thin at home: jewellery |
| hold mass 2 (premium) | cathedral | 360 | 57.4 | 58.2 | needs a cathedral (build cost 291,300); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold prayer 2 | chapel | 13 | 55.9 | 58.3 | needs a chapel (build cost 35,622) |
| jousting 1 | arena | 170 | 59.9 | 60.0 | needs a arena (build cost 28,492); thin at home: protection, light armour, arms; needs weaponry skill |
| hold mass 1 | cathedral | 180 | 58.5 | 60.1 | needs a cathedral (build cost 291,300); thin at home: jewellery, glassware, candles |
| hold banquet 2 (fish) | mansion | 6.8 | 60.6 | 60.6 | thin at home: wine, cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 60.8 | 60.8 | running |

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 29.8, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 3.0 turns |
| beer |  | 51 @ min 3.9 |  |
| bread | 6 @ 2.6, stop 15 |  | uses 3.6/turn (household upkeep), makes 0.0, holds 11 = 2.9 turns |
| cured fish | 7 @ 24.8, stop 20 |  | uses 5.5/turn (mansion 1), makes 0.0, holds 19 = 3.5 turns |
| donations | 40 @ 1.02, stop 40 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 1.86, stop 26 |  | uses 6.4/turn (brewery 1, household upkeep), makes 0.0, holds 58 = 9.0 turns |
| fish | 12 @ 1.71, stop 24 |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| garments |  | 80 @ min 22.0 |  |
| grain | 46 @ 2.84, stop 130 |  | uses 32.5/turn (brewery 1), makes 0.0, holds 104 = 3.2 turns |
| labour | 986 @ 1.71, stop - |  | uses 1388.7/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 891 = 0.9 turns |
| meat | 8 @ 2.4, stop 16 |  | uses 4.0/turn (household upkeep), makes 0.0, holds 6 = 1.5 turns |
| nets |  | 6 @ min 36.0 |  |
| porterage | 26 @ 0.8, stop - |  | uses 23.4/turn (observed), makes 0.0, holds 24 = 1.0 turns |
| timber |  | 24 @ min 8.5 |  |
| tools | 10 @ 5.55, stop 80 |  | uses 10.0/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 20.0 turns |
