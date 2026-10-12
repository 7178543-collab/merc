# v2 shadow report

Turn 13216, 2026-10-12 01:06. Mode: shadow (reads only; v1 runs the game).
Cash 24,966, prestige 2,476 (56 free, +3.8/turn).

**1 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.9 turns (holds 141, next step uses 160/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **labour**: 47 labour expired last turn (~78 coin): holding 928 against a ~70 buffer target -> v2: trim the buy until the stock is near 70

## Tuning

- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **timber**: build materials for ropewalk 1, quarry 1 are in (271.5 held, 177 needed) but a buy is still live -> v2: switch the timber buy off
- **wheels**: build materials for ropewalk 1, quarry 1 are in (13.0 held, 8 needed) but a buy is still live -> v2: switch the wheels buy off

## Builds under construction

- **ropewalk 1** 50% (INITIAL), about 12 turns left; still to deliver: labour 200, timber 130, tools 10, wheels 8; ready for labour
- **quarry 1** 61% (INITIAL), about 8 turns left; still to deliver: labour 312, timber 47, tools 8; ready for labour
  - note: game data lists a 20 discount on this build; not applied, so this buys slightly more than needed

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| timber | 177 | 271.5 | 0 | off: covered; switch v1's buy off |
| tools | 18 | 199.5 | 0 | off: covered |
| wheels | 8 | 13.0 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 56

## Prestige spending, cheapest coin per prestige first

1185 turns left: prestige gained now converts 99.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: waiting - level 2 costs 250, free 56: ~51 turns at +3.8/turn

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.1 | 50.1 | running |
| hold banquet 3 (pies) | mansion | 8 | 54.0 | 54.0 | thin at home: pasties, hop beer, cheese, pies, candles |
| hold sermon 2 (candles) | church | 31 | 53.6 | 55.6 | needs a church (build cost 68,869); thin at home: jewellery, candles |
| hold banquet 2 (pies) | mansion | 7 | 55.8 | 55.8 | thin at home: pasties, cheese, pies, candles |
| hold sermon 2 | church | 24 | 55.5 | 58.1 | needs a church (build cost 68,869); thin at home: jewellery |
| hold prayer 2 | chapel | 13 | 56.1 | 58.3 | needs a chapel (build cost 32,592) |
| hold mass 2 (premium) | cathedral | 360 | 58.2 | 58.9 | needs a cathedral (build cost 277,445); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 4 (pies) | mansion | 18 | 59.6 | 59.6 | thin at home: pasties, hop beer, cheese, pies, candles |
| hold banquet 3 (fish) | mansion | 7.6 | 60.2 | 60.2 | thin at home: hop beer, cured fish, cheese |
| jousting 1 | arena | 170 | 60.1 | 60.2 | needs a arena (build cost 26,030); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 60.9 | 60.9 | thin at home: cured fish, cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 61.0 | 61.0 | running |

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 51 @ min 3.9 |  |
| cured fish | 7 @ 25.2, stop 20 |  | uses 5.5/turn (mansion 1), makes 0.0, holds 20 = 3.6 turns |
| donations | 40 @ 1.02, stop 40 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 1.87, stop 26 |  | uses 6.4/turn (brewery 1, household upkeep), makes 0.0, holds 58 = 9.0 turns |
| fish | 12 @ 1.7, stop 24 |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| garments |  | 80 @ min 22.0 |  |
| grain | 46 @ 2.82, stop 130 |  | uses 32.5/turn (brewery 1), makes 0.0, holds 103 = 3.2 turns |
| labour | 987 @ 1.7, stop - |  | uses 1389.7/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 928 = 1.0 turns |
| meat | 12 @ ?, stop 24 |  | uses 6.0/turn (household upkeep), makes 0.0, holds 4 = 0.7 turns |
| nets |  | 6 @ min 36.0 |  |
| porterage | 26 @ 0.36, stop - |  | uses 23.4/turn (observed), makes 0.0, holds 24 = 1.0 turns |
| timber |  | 24 @ min 8.5 |  |
| tools | 12 @ 5.55, stop 96 |  | uses 12.0/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 16.7 turns |
