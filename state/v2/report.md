# v2 shadow report

Turn 13219, 2026-10-12 04:01. Mode: shadow (reads only; v1 runs the game).
Cash 23,027, prestige 2,489 (69 free, +4.2/turn).

**2 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.7 turns (holds 106, next step uses 160/turn) -> v2: check the step that makes it
- **porterage**: home ask 1.10 is above our ceiling 0.80: the buy can't fill -> v2: raise the ceiling or find another source

## Tuning

- **timber**: build materials for ropewalk 1, quarry 1 are in (342.8 held, 127 needed) but a buy is still live -> v2: switch the timber buy off
- **wheels**: build materials for ropewalk 1, quarry 1 are in (13.0 held, 7 needed) but a buy is still live -> v2: switch the wheels buy off

## Builds under construction

- **ropewalk 1** 62% (INITIAL), about 10 turns left; still to deliver: labour 152, timber 99, tools 8, wheels 7; ready for labour
- **quarry 1** 77% (INITIAL), about 5 turns left; still to deliver: labour 184, timber 28, tools 5; ready for labour
  - note: game data lists a 20 discount on this build; not applied, so this buys slightly more than needed

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| timber | 127 | 342.8 | 0 | off: covered; switch v1's buy off |
| tools | 13 | 199.6 | 0 | off: covered |
| wheels | 7 | 13.0 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 53

## Prestige spending, cheapest coin per prestige first

1182 turns left: prestige gained now converts 99.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: waiting - level 2 costs 250, free 69: ~44 turns at +4.2/turn

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.4 | 50.4 | running |
| hold banquet 3 (pies) | mansion | 8 | 51.4 | 51.4 | thin at home: pasties, hop beer, cheese, pies, candles |
| hold banquet 3 (fish) | mansion | 7.6 | 54.7 | 54.7 | thin at home: hop beer, cured fish, cheese |
| hold sermon 2 (candles) | church | 31 | 53.1 | 55.2 | needs a church (build cost 70,332); thin at home: jewellery, candles, furniture |
| hold banquet 4 (pies) | mansion | 18 | 55.9 | 55.9 | thin at home: pasties, hop beer, pies, candles |
| hold banquet 2 (pies) | mansion | 7 | 56.0 | 56.0 | thin at home: pasties, cheese, pies, candles |
| hold banquet 1 (fish) | mansion | 4.2 | 56.6 | 56.6 | running; thin at home: cured fish |
| hold sermon 2 | church | 24 | 55.1 | 57.8 | needs a church (build cost 70,332); thin at home: jewellery, furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 58.0 | 58.0 | thin at home: cured fish, cheese |
| hold mass 2 (premium) | cathedral | 360 | 57.5 | 58.2 | needs a cathedral (build cost 284,040); thin at home: furniture, jewellery, glassware, candles, premium garments |
| jousting 1 | arena | 170 | 58.2 | 58.3 | needs a arena (build cost 26,096); thin at home: protection, light armour, arms; needs weaponry skill |
| hold prayer 2 | chapel | 13 | 56.2 | 58.5 | needs a chapel (build cost 33,752) |

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 26.4, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 5.0 turns |
| beer |  | 51 @ min 3.9 |  |
| cured fish | 7 @ 22.6, stop 20 |  | uses 5.5/turn (mansion 1), makes 0.0, holds 19 = 3.5 turns |
| donations | 40 @ 1.02, stop 40 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 1.8, stop 26 |  | uses 6.4/turn (brewery 1, household upkeep), makes 0.0, holds 58 = 9.0 turns |
| fish | 12 @ 1.71, stop 24 |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| garments |  | 80 @ min 22.0 |  |
| grain | 46 @ 2.76, stop 130 |  | uses 32.5/turn (brewery 1), makes 0.0, holds 104 = 3.2 turns |
| labour | 984 @ 1.71, stop - |  | uses 1386.7/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 891 = 1.0 turns |
| meat | 12 @ 2.34, stop 24 |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 6 @ min 36.0 |  |
| porterage | 26 @ 0.8, stop - |  | uses 23.4/turn (observed), makes 0.0, holds 24 = 1.0 turns |
| timber |  | 24 @ min 8.5 |  |
| tools | 10 @ 5.45, stop 80 |  | uses 10.0/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 20.0 turns |
