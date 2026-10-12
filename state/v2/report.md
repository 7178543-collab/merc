# v2 shadow report

Turn 13220, 2026-10-12 05:58. Mode: shadow (reads only; v1 runs the game).
Cash 22,359, prestige 2,493 (73 free, +4.2/turn).

**2 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.6 turns (holds 94, next step uses 160/turn) -> v2: check the step that makes it
- **porterage**: home ask 1.10 is above our ceiling 0.80: the buy can't fill -> v2: raise the ceiling or find another source

## Tuning

- **timber**: build materials for ropewalk 1, quarry 1 are in (366.6 held, 110 needed) but a buy is still live -> v2: switch the timber buy off
- **wheels**: build materials for ropewalk 1, quarry 1 are in (13.0 held, 6 needed) but a buy is still live -> v2: switch the wheels buy off

## Builds under construction

- **ropewalk 1** 66% (INITIAL), about 9 turns left; still to deliver: labour 136, timber 89, tools 7, wheels 6; ready for labour
- **quarry 1** 83% (INITIAL), about 4 turns left; still to deliver: labour 137, timber 21, tools 4; ready for labour
  - note: game data lists a 20 discount on this build; not applied, so this buys slightly more than needed

| Material | Need | Held | Deficit | v2 action |
| --- | --- | --- | --- | --- |
| timber | 110 | 366.6 | 0 | off: covered; switch v1's buy off |
| tools | 11 | 199.7 | 0 | off: covered |
| wheels | 6 | 13.0 | 0 | off: covered; switch v1's buy off |

Labour metered per turn while a site can progress: labour 51

## Prestige spending, cheapest coin per prestige first

1181 turns left: prestige gained now converts 99.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 11 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: waiting - level 2 costs 250, free 73: ~43 turns at +4.2/turn

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.1 | 50.1 | running |
| hold banquet 3 (pies) | mansion | 8 | 51.4 | 51.4 | thin at home: pasties, hop beer, cheese, pies, candles |
| hold banquet 2 (pies) | mansion | 7 | 54.7 | 54.7 | thin at home: pasties, cheese, pies, candles |
| hold banquet 3 (fish) | mansion | 7.6 | 55.2 | 55.2 | thin at home: hop beer, cheese |
| hold sermon 2 (candles) | church | 31 | 53.4 | 55.4 | needs a church (build cost 68,075); thin at home: jewellery, candles, furniture |
| hold banquet 4 (pies) | mansion | 18 | 56.2 | 56.2 | thin at home: pasties, hop beer, candles |
| hold banquet 1 (fish) | mansion | 4.2 | 57.6 | 57.6 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 57.6 | 57.6 | thin at home: cheese |
| hold sermon 2 | church | 24 | 55.1 | 57.7 | needs a church (build cost 68,075); thin at home: jewellery, furniture |
| hold prayer 2 | chapel | 13 | 56.1 | 58.4 | needs a chapel (build cost 32,127); thin at home: furniture |
| hold mass 2 (premium) | cathedral | 360 | 57.7 | 58.5 | needs a cathedral (build cost 275,700); thin at home: furniture, jewellery, glassware, candles, premium garments |
| jousting 1 | arena | 170 | 58.7 | 58.9 | needs a arena (build cost 25,593); thin at home: protection, light armour, arms; needs weaponry skill |

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 28.2, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 3 = 6.0 turns |
| beer |  | 51 @ min 3.9 |  |
| bread | 4 @ 2.42, stop 15 |  | uses 3.6/turn (household upkeep), makes 0.0, holds 15 = 4.1 turns |
| cured fish | 7 @ 24.8, stop 20 |  | uses 5.5/turn (mansion 1), makes 0.0, holds 20 = 3.6 turns |
| donations | 40 @ 1.02, stop 40 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 1.81, stop 26 |  | uses 6.4/turn (brewery 1, household upkeep), makes 0.0, holds 57 = 9.0 turns |
| fish | 12 @ 1.71, stop 24 |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| garments |  | 80 @ min 22.0 |  |
| grain | 45 @ 2.74, stop 130 |  | uses 32.5/turn (brewery 1), makes 0.0, holds 105 = 3.2 turns |
| labour | 982 @ 1.7, stop - |  | uses 1384.7/turn (brewery 1, construction, flax farm 1), makes 450.0, holds 891 = 1.0 turns |
| meat | 12 @ 2.26, stop 24 |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 6 @ min 36.0 |  |
| porterage | 26 @ 0.8, stop - |  | uses 23.4/turn (observed), makes 0.0, holds 24 = 1.0 turns |
| timber |  | 24 @ min 8.5 |  |
| tools | 10 @ 5.45, stop 80 |  | uses 10.0/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 200 = 20.0 turns |
