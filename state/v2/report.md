# v2 shadow report

Turn 13814, 2026-11-05 23:15. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,823, prestige 3,292 (172 free, -0.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 15 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 33 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 525 | 0 | 4 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**1 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it

## Tuning

- **tar**: home ask 11.80 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 525, not 618

## Prestige spending, cheapest coin per prestige first

587 turns left: prestige gained now converts 94.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.1 | 50.1 | running |
| jousting 3 | arena | 230 | 53.8 | 54.0 | needs a arena (build cost 25,465); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 54.1 | 54.1 |  |
| hold banquet 4 (pies) | mansion | 18 | 54.5 | 54.5 | thin at home: hop beer, wine, ham, stockfish, cheese |
| hold banquet 2 (fish) | mansion | 6.8 | 56.2 | 56.2 | thin at home: wine, cheese |
| hold banquet 2 (pies) | mansion | 7 | 56.4 | 56.4 | thin at home: wine, cheese |
| hold banquet 4 | mansion | 17.5 | 57.8 | 57.8 | thin at home: wine, hop beer, ham, stockfish, cheese |
| hold banquet 4 (premium) | mansion | 20 | 58.3 | 58.3 | thin at home: hop beer, wine, ham, stockfish, premium cheese |
| jousting 2 | arena | 210 | 58.9 | 59.1 | needs a arena (build cost 25,465); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 1 (meat) | mansion | 4.2 | 59.8 | 59.8 |  |
| hold feast 2 | townhouse | 2.6 | 54.8 | 59.9 | needs a townhouse (build cost 7,530); thin at home: wine |
| hold banquet 2 (meat) | mansion | 6.8 | 60.4 | 60.4 | thin at home: wine, cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 14.6 (keep 14); best orders clear only 2 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 16.1 (keep 14); best orders clear only -2 a turn after crew: ship stays at 0
- best towns now: Donaunieder +39, Orlesailles +36, Bordetes +35, Brunnham +28, Rouhomme +28
- Donaunieder would trade: pasties buy 12 @ 13.9; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~104 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Bedenis | 566 | 0.16 | 0.80 (83/turn) | bread 160 (2.25->3.23), gears 1 (54.08->58.9), mouldboards 1 (35.07->36.48) | garments 18 (22.05->23.18), cloth 20 (7.35->8.25), candles 1 (77.7->84), cheese 4 (6.83->7.6) | +130 |
| Grandgues | 152 | 0.04 | 0.50 (52/turn) | timber 24 (7.04->10.07), limestone 7 (16.07->21.47), bread 160 (2.25->2.47), mouldboards 1 (35.07->42.94) | candles 1 (80.85->84), cheese 4 (7.04->7.6), bricks 1 (7.51->9.21), lead ore 2 (11.13->11.97) | +124 |
| Blanans | 297 | 0.08 | 0.70 (73/turn) | limestone 7 (16.07->23.75), timber 26 (7.04->8.74), medicine 1 (149.1->154.85), furniture 12 (14.18->14.72) | cloth 24 (7.35->8.25), garments 18 (22.05->23.18), candles 1 (78.75->84), cheese 4 (6.88->7.6) | +105 |
| Heilegg | 826 | 0.24 | 0.30 (31/turn) | gears 1 (54.08->61.75), mouldboards 1 (35.07->37.62) | garments 18 (20.48->23.18), thread 62 (4.47->5.1), cloth 24 (7.04->8.25), cheese 4 (6.3->7.6) | +101 |
| Neuborn | 780 | 0.22 | 1.00 (104/turn) | timber 23 (7.04->11.59), limestone 2 (16.07->25.65), grain 1 (2.6->3.61), wine 4 (5.78->6.13) | garments 16 (21->23.18), cloth 16 (7.04->8.25), candles 0 (80.85->84), wax 1 (23.1->23.75) | +88 |

**Best:** Bedenis at about +130 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 31.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 16 @ min 3.06 | goal planner: sells 16 at 3.06 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 13.8, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.8) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 25) |
| light armour | 1 @ 93.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 36.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 83.0) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 21.8k (cash + stock at home prices); +183/turn over 6 turns, +148/turn over 24 turns.
- Limits: cash flow >= -284/turn, prestige >= +5.35/turn (values are after 200 tax a turn).
- Today's settings: value +105/turn, cash +110/turn, prestige -0.86/turn - breaks the prestige floor.
- Plan: value -133/turn, cash -127/turn, prestige +3.34/turn - could not meet the prestige floor.
- Cash check (real vs predicted cash a tick, last 3): +55 vs +96, +82 vs +102, +263 vs +109.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Etallaen: +1/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +3/turn
  - retting pit 1 0.91 -> 0.72: -11/turn
  - flax farm 1 4.64 -> 3.65: +8/turn
  - spinnery 1 1.65 -> 1.28: -10/turn
  - brewery 1 0.14 -> 0.27: -6/turn
  - ropewalk 1 0.25 -> 0.00: -14/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.38: +15/turn
  - weavery 1 0.50 -> 0.23: -33/turn
- Model check over the last 62 turns: predicted +97/turn for the settings we ran, real +68/turn.
- Worth of one more unit per turn: labour 1.66, thread 4.17, cloth 6.67, flax fibres 4.94, garments 19.30, nets 30.05, beer 2.95, timber 3.02, prestige 10000.00, cash 0.00
- Orders it would set: beer sell 16 (v2 15); cloth sell 1 (v2 none); firewood buy 4 (v2 5); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 29 (v2 25); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.38, worth +15/turn.
- Ship linen snake: Grandgues -> Etallaen (+5/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.1/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 485 (+196 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 6.00 |
| ret | 3 | 0.91 | 1.20 |
| spin | 4 | 1.65 | 2.12 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 323/228, cloth 73/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 5.45 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
- R5: tar buy not filling: bid 11 under the home ask 11.8 for 4 turns, bought 0.0 of 1, 0.0 held (0.0 turns); raise needs Taylor (ceiling 11.0)
