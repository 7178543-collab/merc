# v2 shadow report

Turn 13810, 2026-11-05 19:58. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,368, prestige 3,295 (175 free, -0.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 15 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 33 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 518 | 0 | 11 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 12.60 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 12.60 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 525, not 625

## Prestige spending, cheapest coin per prestige first

591 turns left: prestige gained now converts 94.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.8 | 49.8 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 53.8 | 53.8 | thin at home: wine, cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 54.0 | 54.0 |  |
| hold banquet 4 (pies) | mansion | 18 | 54.3 | 54.3 | thin at home: wine, ham, stockfish, cheese |
| jousting 3 | arena | 230 | 54.2 | 54.4 | needs a arena (build cost 26,382); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 56.1 | 56.1 | thin at home: wine, cheese |
| hold banquet 4 | mansion | 17.5 | 56.7 | 56.7 | thin at home: wine, ham, stockfish, cheese |
| hold sermon 2 (candles) | church | 31 | 52.9 | 57.2 | needs a church (build cost 67,236); thin at home: candles, furniture |
| hold prayer 2 | chapel | 13 | 52.9 | 57.4 | needs a chapel (build cost 31,544); thin at home: furniture |
| hold banquet 1 (meat) | mansion | 4.2 | 57.5 | 57.5 |  |
| hold banquet 2 (pies) | mansion | 7 | 57.6 | 57.6 | thin at home: wine, cheese |
| hold banquet 4 (premium) | mansion | 20 | 57.9 | 57.9 | thin at home: wine, ham, stockfish, premium cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 15.1 (keep 14); best orders clear only -3 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 6 @ 15.4 (keep 14); best orders clear only 11 a turn after crew: ship stays at 0
- best towns now: Bedenis +105, Heilegg +53, Donaunieder +41, Orlesailles +36, Fulkirch +34
- Bedenis would trade: pasties buy 14 @ 10.7; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~102 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.60 (61/turn) | charcoal 18 (2.23->7.17), timber 26 (6.93->9.26), limestone 5 (16.48->21.47), tackles 1 (208.95->220.4) | cloth 10 (6.88->7.6), bricks 2 (6.2->7.79), salt 5 (5.21->5.56), harnesses 1 (43.47->44.27) | +184 |
| Hanbrücken | 531 | 0.14 | 0.80 (82/turn) | garments 10 (19.7->23.56), charcoal 18 (2.23->3.82), timber 23 (6.93->9.4), mouldboards 1 (35.07->35.72) | salt 8 (4.14->5.56), cloth 24 (7.19->7.6), yarn 6 (3->4.08), harnesses 1 (42.84->44.27) | +74 |
| Pontmont | 341 | 0.09 | 0.20 (20/turn) | garments 10 (19.7->22.61), charcoal 18 (2.23->3.7), cured fish 7 (22.68->24.51), slaked lime 4 (14.18->16.72) | candles 1 (78.75->81), salt 7 (5.19->5.56), bricks 2 (5.25->7.79), tar 3 (10.82->11.4) | +68 |
| Vauxvais | 204 | 0.06 | 0.20 (20/turn) | charcoal 15 (2.23->3.34), beer 15 (3.3->3.93), wax 8 (26.46->27.17), limestone 1 (16.48->22.99) | thread 49 (4.73->5), salt 8 (4.54->5.56), bricks 2 (4.85->7.79), candles 1 (77.17->81) | +60 |
| Blanans | 297 | 0.08 | 0.60 (61/turn) | limestone 5 (16.48->23.75), timber 27 (6.93->8.84), firewood 1 (1.74->6.46), cheese 4 (6.14->6.51) | cloth 24 (7.35->7.6), salt 5 (4.75->5.56), candles 1 (78.23->81), harnesses 1 (43.47->44.27) | +54 |

**Best:** Grandgues at about +184 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.8, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 1 = 2.0 turns |
| beer |  | 16 @ min 3.06 | goal planner: sells 16 at 3.06 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| cloth |  | 2 @ min 7.05 | goal planner: sells 2 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 20.0) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 25) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 36.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 1 = 4.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 21.6k (cash + stock at home prices); +277/turn over 6 turns, +164/turn over 24 turns.
- Limits: cash flow >= -265/turn, prestige >= +5.21/turn (values are after 200 tax a turn).
- Today's settings: value +86/turn, cash +89/turn, prestige -0.88/turn - breaks the prestige floor.
- Plan: value -143/turn, cash -139/turn, prestige +3.32/turn - could not meet the prestige floor.
- Cash check (real vs predicted cash a tick, last 3): +47 vs +108, -146 vs +105, +55 vs +96 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Bremcop: +6/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +3/turn
  - retting pit 1 0.91 -> 0.72: -12/turn
  - flax farm 1 4.64 -> 3.61: +10/turn
  - spinnery 1 1.65 -> 1.27: -13/turn
  - brewery 1 0.14 -> 0.27: -2/turn
  - ropewalk 1 0.25 -> 0.00: -11/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.35: +11/turn
  - weavery 1 0.50 -> 0.24: -24/turn
- Model check over the last 61 turns: predicted +97/turn for the settings we ran, real +75/turn.
- Worth of one more unit per turn: labour 1.66, thread 4.20, cloth 6.68, flax fibres 5.05, garments 19.30, nets 30.07, beer 2.87, timber 3.40, prestige 10000.00, cash 0.00
- Orders it would set: beer sell 16 (v2 15); candles buy 2 (v2 None); cloth sell 2 (v2 none); firewood buy 4 (v2 5); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 29 (v2 25); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.35, worth +13/turn.
- Ship linen snake: Grandgues -> Bremcop (+6/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 483 (+194 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 5.97 |
| ret | 3 | 0.91 | 1.19 |
| spin | 4 | 1.65 | 2.11 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 330/228, cloth 73/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 5.55 for 4 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
