# v2 shadow report

Turn None, 2026-10-29 17:00. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 0, prestige 0 (0 free, +0.0/turn).

**0 risks, 0 waste, 0 tuning** where v2 would act differently from v1.

## Prestige spending, cheapest coin per prestige first

761 turns left: prestige gained now converts 97.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: unknown - no level in the snapshot for tenants
- agreed **prestige_management** to level 2: unknown - no level in the snapshot for prestige_management
- agreed **apprentices** to level 2: unknown - no level in the snapshot for apprentices

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~94 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Chribruck | 1202 | 0.40 | 0.20 (19/turn) | tackles 2 (183.75->195.7), garments 1 (16.82->19.38), cloth 5 (7.88->8.55), honey 2 (7.67->8.46) | alembics 1 (348.6->456) | +129 |
| Heidlowe | 662 | 0.17 | 0.20 (19/turn) | thread 66 (3.96->4.24), garments 1 (16.82->18.71), wine 11 (5.67->5.98), lead ore 1 (6.93->9.21) | alembics 1 (348.6->456) | +119 |
| Rouhomme | 368 | 0.09 | 0.60 (56/turn) | bread 145 (2.31->2.93), charcoal 11 (1.87->3.52), thread 7 (3.96->5.18), flour 1 (16.91->19.95) | ploughs 4 (63->69.35) | +100 |
| Herschweig | 775 | 0.20 | 0.10 (9/turn) | flax fibres 13 (4.98->6.13), lead ore 1 (6.93->10.45), garments 1 (16.82->18.81), wine 4 (5.67->6.32) | alembics 1 (386.4->456), cloth 3 (6.88->7.5), tackles 1 (152.25->153.9) | +90 |
| Angefont | 686 | 0.17 | 0.20 (19/turn) | thread 29 (3.96->5.79), limestone 1 (13.12->28.31), premium cheese 1 (26.04->27.74), flour 1 (16.91->18.81) | garments 2 (21.21->21.8), honey 3 (6.3->6.84) | +63 |

**Best:** Chribruck at about +129 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| firewood | 0 @ 2.4, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 0 |
| grain | 0 @ 3.7, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 0 |
| labour | 0 @ 2.2, stop - |  | goal planner: buys 0 for today's rates (v2 had 0) |
| porterage | 0 @ 1.1, stop - |  | goal planner: buys 0 for today's rates (v2 had 0) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 0 |

## Goal: business value (live: rates, buys, sells, ships, invest)
- Value now 9.6k (cash + stock at home prices); -20/turn over 6 turns, -116/turn over 24 turns.
- Limits: cash flow >= +167/turn, prestige >= +12.50/turn (values are after 226 tax a turn).
- Today's settings: value -226/turn, cash -226/turn, prestige +0.00/turn - breaks the prestige floor and cash floor.
- Plan: value -226/turn, cash -226/turn, prestige +0.00/turn - could not meet the prestige floor and cash floor.
- Cash check (real vs predicted cash a tick, last 3): +10 vs -18, +48 vs +17, -5 vs +16.
- Route sales counted at most (what the ships really sold, a turn): none.
- No building changes: today's rates are the plan's.
- Model check over the last 58 turns: predicted +49/turn for the settings we ran, real -72/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 100000.00, thread 100000.00, cloth 100000.00, flax fibres 100000.00, garments 100000.00, nets 100000.00, beer 100000.00, timber 100000.00, prestige 10000.00, cash 100.00
- Orders it would set: fish buy 0 (v2 None); meat buy 0 (v2 None)
- Investments:
  - Tenants L1 for -100 prestige: +0/turn, doesn't pay yet (waits until 200 free (keeps 300 after))

## Chain sizing

Not planned: chain buildings or recipes missing: flax, ret, spin, weave, sew

