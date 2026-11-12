# v2 shadow report

Turn 13981, 2026-11-12 22:28. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,266, prestige 3,520 (400 free, -2.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 11 | 0 | 4 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 26, buy 9, buy @ 3.76 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 17, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 496 | 0 | 33 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 3.86 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.86 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **labour**: 33 labour expired last turn (~58 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 516, not 616
- labour expiry guard: 33 bought labour expired last turn, buy 0 (not 16) this turn

## Prestige spending, cheapest coin per prestige first

420 turns left: prestige gained now converts 87.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.9 | 51.9 | running |
| jousting 3 | arena | 230 | 54.5 | 54.8 | needs a arena (build cost 27,233); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 56.6 | 56.6 | thin at home: hop beer, stockfish |
| hold banquet 1 (fish) | mansion | 4.2 | 58.3 | 58.3 |  |
| hold banquet 4 (premium) | mansion | 20 | 59.4 | 59.4 | thin at home: hop beer, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 59.6 | 59.6 | thin at home: hop beer, pies |
| hold banquet 4 | mansion | 17.5 | 59.7 | 59.7 | thin at home: hop beer, ham, stockfish |
| jousting 2 | arena | 210 | 59.7 | 60.0 | needs a arena (build cost 27,233); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 60.5 | 60.5 |  |
| hold banquet 2 (pies) | mansion | 7 | 60.5 | 60.5 | thin at home: pies |
| hold banquet 3 (fish) | mansion | 7.6 | 61.4 | 61.4 | thin at home: hop beer |
| hold mass 2 (premium) | cathedral | 360 | 59.9 | 62.6 | needs a cathedral (build cost 290,410); thin at home: furniture, jewellery, glassware, candles, premium garments |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 10 | 134102075 | 0.276 | - | furniture 12, pasties 3 | -206 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 5 @ 15.8 (keep 14); best orders clear only 5 a turn after crew: ship stays at 0
- best towns now: Orlesailles +26, Clarfranche +25, Brunnham +20, Boistot +19, Karlmoor +18
- Orlesailles would trade: pasties buy 5 @ 11.6; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~106 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.90 (95/turn) | timber 40 (8.61->11.4), bread 154 (2.54->2.98), furniture 17 (11.87->14.63), firewood 30 (4.05->6.65) | flour 2 (20.89->27.55), cured meat 3 (24.36->27.74), cloth 11 (6.88->7.65), cheese 3 (6.35->6.55) | +282 |
| Rouhomme | 368 | 0.10 | 0.20 (21/turn) | furniture 17 (11.87->15.67), rope 1 (60.77->81.7), limestone 2 (21.21->29.64), candles 1 (66.15->72.67) | thread 24 (4.94->5.6), tools 16 (4.85->5.46), flour 2 (24.78->27.55), cured meat 3 (26.88->27.74) | +123 |
| Fontaux | 411 | 0.12 | 0.20 (21/turn) | furniture 13 (11.87->17.29), rope 1 (60.77->77.42), candles 1 (66.15->75.05), arms 3 (33.6->35.34) | cured meat 3 (24.57->27.74), flour 2 (24.15->27.55), tools 16 (5.15->5.46) | +121 |
| Heilegg | 826 | 0.24 | 0.30 (32/turn) | furniture 17 (11.87->15.01), rope 1 (60.77->79.33), steel ingots 4 (20.79->25.65), candles 1 (66.15->79.8) | cured meat 3 (23.94->27.74), flour 2 (23.31->27.55), garments 2 (21.63->23.4), cheese 3 (6.09->6.55) | +118 |
| Briclives | 1041 | 0.36 | 0.40 (42/turn) | furniture 17 (11.87->17.2), garments 10 (22.2->25.46), candles 1 (66.15->71.72), tackles 1 (168->174.8) | steel ingots 8 (16.8->18.71), canvas 1 (35.7->38.38), leather 1 (28.98->30.78) | +114 |

**Best:** Grandgues at about +282 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 6) |
| candles | 2 @ 78.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 2 @ min 6.95 | goal planner: sells 2 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.14 | goal planner: sells 2 a turn at 1.14, keeps 219 (no one offered it) |
| furniture | 2 @ 11.6, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 21.6) |
| grain | 5 @ 3.7, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 37.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 73.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 27.9k (cash + stock at home prices); -154/turn over 6 turns, +62/turn over 24 turns.
- Limits: cash flow >= -386/turn, prestige >= -0.42/turn (values are after 200 tax a turn).
- Today's settings: value +59/turn, cash +39/turn, prestige -2.21/turn - breaks the prestige floor.
- Plan: value -20/turn, cash -9/turn, prestige -0.42/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +178 vs +70, +56 vs +63, -97 vs +55.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Marmont: +11/turn
  - ship Flax Wyrm -> no route: +0/turn
  - ropewalk 1 0.25 -> 0.12: +13/turn
  - brewery 1 0.14 -> 0.08: +12/turn
  - net maker 0.00 -> 0.29: +9/turn
  - flax farm 1 4.64 -> 4.11: -0/turn
  - retting pit 1 0.91 -> 0.82: -1/turn
  - spinnery 1 1.65 -> 1.29: -11/turn
  - mansion 1 0.00 -> 0.43: -103/turn
- Model check over the last 61 turns: predicted +105/turn for the settings we ran, real -17/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.96, garments 19.30, nets 30.26, beer 3.03, timber 3.40, prestige 72.66, cash 0.00
- Orders it would set: bread buy 5 (v2 6); candles buy 2 (v2 None); cloth sell 2 (v2 none); firewood buy 1 (v2 3); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Marmont (+11/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +82/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1990 coin: +5/turn, payback 369 turns, doesn't pay yet

## Chain sizing

Mode HOLD, garments sold 10.6/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 409 (+120 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 3.59 |
| ret | 3 | 0.91 | 0.72 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 161/77, thread 1050/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 3.86; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
