# v2 shadow report

Turn 13211, 2026-10-11 20:54. Mode: shadow (reads only; v1 runs the game).
Cash 25,355, prestige 2,475 (55 free, +3.8/turn).

**8 risks, 4 waste, 7 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **arms**: needed (0.5/turn) but there is NO buy order, stock 0 -> v2: add buy 1
- **flax fibres**: spinnery 1 ran 0.0 of 3.8: short of flax fibres -> v2: keep a flax fibres buy (or stock) that covers it
- **flax fibres**: flax fibres buffer 0.0 turns (holds 0, next step uses 64/turn) -> v2: check the step that makes it
- **labour**: buying 356, short of ~928 needed -> v2: buy 928
- **porterage**: logging camp w/ tool ran 0.0 of 20.0: short of porterage -> v2: keep a porterage buy (or stock) that covers it
- **porterage**: flax farm 1 ran 0.0 of 9.9: short of porterage -> v2: keep a porterage buy (or stock) that covers it
- **porterage**: retting pit 1 ran 0.0 of 2.0: short of porterage -> v2: keep a porterage buy (or stock) that covers it
- **thread**: thread buffer 0.0 turns (holds 0, next step uses 174/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **garments**: it costs us 23.46 to make, the floor sells at 22.00 -> v2: cut its cost (labour price) or export it; a higher floor would just stop home sales
- **nets**: it costs us 36.85 to make, the floor sells at 36.00 -> v2: cut its cost (labour price) or export it; a higher floor would just stop home sales
- **porterage**: buying 40, need ~26 -> v2: buy 26
- **timber**: it costs us 8.01 to make, the floor sells at 7.00 -> v2: cut its cost (labour price) or export it; a higher floor would just stop home sales

## Tuning

- **donations**: buy 40 vs v2 80
- **firewood**: buy 40 vs v2 7
- **fish**: buy 6 vs v2 12
- **grain**: buy 33 vs v2 65
- **meat**: buy 6 vs v2 12
- **tar**: no sellers at home right now -> v2: stock covers it, or import
- **tools**: buy 31 vs v2 9

## Prestige sinks running now

| Sink | Prestige/turn | Coin per prestige |
| --- | --- | --- |
| maintain 1 (park 1) | 4.5 | 50.7 |
| hold banquet 1 (fish) (mansion 1) | 4.2 | 60.9 |

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 27.8, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 0 = 1.0 turns |
| beer |  | 51 @ min 3.9 |  |
| candles | 2 @ 69.5, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 55 = 36.7 turns |
| cured fish | 7 @ 24.8, stop 20 |  | uses 5.5/turn (mansion 1), makes 0.0, holds 20 = 3.6 turns |
| donations | 80 @ 1.02, stop 160 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.08, stop 26 |  | uses 6.4/turn (brewery 1, household upkeep), makes 0.0, holds 58 = 9.0 turns |
| fish | 12 @ 1.86, stop 24 |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| furniture | 2 @ 15.4, stop 5 |  | uses 1.2/turn (household upkeep), makes 0.0, holds 141 = 117.7 turns |
| garments |  | 80 @ min 22.0 |  |
| grain | 65 @ 3.26, stop 130 |  | uses 32.5/turn (brewery 1), makes 0.0, holds 36 = 1.1 turns |
| labour | 928 @ 1.72, stop - |  | uses 1333.7/turn (brewery 1, flax farm 1, household), makes 450.0, holds 378 = 0.4 turns |
| light armour | 1 @ 87.0, stop 1 |  | uses 0.2/turn (household upkeep), makes 0.0, holds 8 = 39.0 turns |
| meat | 12 @ 2.06, stop 24 |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 6 @ min 36.0 |  |
| porterage | 26 @ 0.39, stop - |  | uses 23.4/turn (observed), makes 0.0, holds 24 = 1.0 turns |
| tar | 1 @ ?, stop 2 |  | uses 0.5/turn (observed), makes 0.0, holds 47 = 97.7 turns |
| timber |  | 24 @ min 8.5 |  |
| tools | 9 @ 5.95, stop 72 |  | uses 9.0/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 182 = 20.3 turns |
