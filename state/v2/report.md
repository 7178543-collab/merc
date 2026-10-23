# v2 shadow report

Turn None, 2026-10-23 04:00. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 0, prestige 0 (0 free, +0.0/turn).

**0 risks, 0 waste, 0 tuning** where v2 would act differently from v1.

## Prestige spending, cheapest coin per prestige first

918 turns left: prestige gained now converts 99.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: unknown - no level in the snapshot for tenants
- agreed **prestige_management** to level 2: unknown - no level in the snapshot for prestige_management
- agreed **apprentices** to level 2: unknown - no level in the snapshot for apprentices

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~128 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Kleinburgh | 1440 | 0.71 | 0.00 (0/turn) | - | - | +0 |
| Cobholme | 1564 | 0.80 | 0.00 (0/turn) | - | - | +0 |
| Disscester | 1474 | 0.74 | 0.00 (0/turn) | - | - | +0 |
| Clarfranche | 1484 | 0.74 | 0.00 (0/turn) | - | - | +0 |
| Brunnham | 1281 | 0.60 | 0.00 (0/turn) | - | - | +0 |

**Best:** Kleinburgh at about +0 coin a turn (nothing pays at these prices).

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| firewood | 0 @ 2.4, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 0 |
| grain | 0 @ 3.7, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 0 |
| labour | 0 @ 2.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 0 |
| porterage | 0 @ 1.1, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 0 |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 0 |

## Goal: business value (shadow)
- no plan: goal plan failed: ValueError: Invalid input for linprog: A_eq must have exactly two dimensions, and the number of columns in A_eq must be equal to the size of c

## Chain sizing

Not planned: chain buildings or recipes missing: flax, ret, spin, weave, sew

