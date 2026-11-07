# v2 shadow report

Turn 13843, 2026-11-07 04:21. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,651, prestige 3,383 (263 free, -1.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 16 | 9 | 4 | 0 | 0 | min_holding 60, sell 11, sell @ 3.06; stop 26, buy 9, buy @ 3.36 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 34 | 0 | 0 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 512 | 0 | 17 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **labour**: 17 labour expired last turn (~27 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 512, not 610

## Prestige spending, cheapest coin per prestige first

558 turns left: prestige gained now converts 93.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.2 | 49.2 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 53.3 | 53.3 |  |
| hold banquet 4 (pies) | mansion | 18 | 53.6 | 53.6 | thin at home: ham, stockfish |
| hold banquet 1 (fish) | mansion | 4.2 | 53.7 | 53.7 |  |
| jousting 3 | arena | 230 | 53.6 | 53.8 | needs a arena (build cost 25,873); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 54.4 | 54.4 | thin at home: pasties |
| hold banquet 2 (meat) | mansion | 6.8 | 55.9 | 55.9 |  |
| hold banquet 3 (pies) | mansion | 8 | 56.2 | 56.2 | thin at home: pasties |
| hold banquet 3 (fish) | mansion | 7.6 | 56.3 | 56.3 |  |
| hold banquet 4 | mansion | 17.5 | 56.7 | 56.7 | thin at home: ham, stockfish |
| hold banquet 1 (meat) | mansion | 4.2 | 57.5 | 57.5 |  |
| hold banquet 4 (premium) | mansion | 20 | 58.1 | 58.1 | thin at home: ham, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 10 | 134102075 | 0.096 | - | pasties 6 | -94 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 15.9 (keep 14); best orders clear only -1 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 15.5 (keep 14); best orders clear only -0 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~103 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Fontaux | 411 | 0.11 | 0.80 (82/turn) | timber 25 (7.19->11.4), garments 10 (18.8->23.18), thread 48 (4.66->5.65), furniture 12 (15.65->17.86) | lead bars 2 (15.96->16.53) | +183 |
| Hofkirchen | 991 | 0.32 | 1.00 (103/turn) | beer 105 (3.46->5.27), cloth 12 (8.82->10.16), blades 5 (15.12->17.1), garments 10 (18.8->19.76) | dyed cloth 11 (12.6->13.59), flax fibres 27 (5.17->5.95), candles 1 (79.8->83.5), bronze ingots 1 (20.37->21.66) | +176 |
| Grandgues | 152 | 0.04 | 0.30 (31/turn) | beer 105 (3.46->3.93), garments 10 (18.8->22.23), timber 29 (7.19->8.55), rope 1 (80->86.92) | candles 1 (77.7->83.5), bricks 6 (7.98->9.03), chisels 1 (7.4->8.22) | +116 |
| Etallaen | 774 | 0.21 | 0.50 (51/turn) | garments 10 (18.8->21.85), cured meat 3 (23.52->28.31), cured fish 7 (24.15->26.22), wine 6 (6.14->8.41) | candles 1 (78.75->83.5), flax fibres 6 (4.94->5.95), thread 16 (4.73->5.15), flax plants 2 (1.03->1.46) | +107 |
| Hanstein | 380 | 0.10 | 0.40 (41/turn) | garments 10 (18.8->22.61), tapestries 2 (661.5->669.75), timber 15 (7.19->9.26), cloth 12 (8.82->9.5) | seeds 12 (1.81->2.32), bricks 3 (5.99->9.03), candles 1 (80.33->83.5), yarn 4 (4.47->4.75) | +95 |

**Best:** Fontaux at about +183 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 30.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 3 @ min 1.21 | goal planner: sells 3 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 15.2, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 24.2) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 12) |
| light armour | 1 @ 94, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 78.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 22.3k (cash + stock at home prices); +185/turn over 6 turns, -14/turn over 24 turns.
- Limits: cash flow >= -277/turn, prestige >= +1.53/turn (values are after 200 tax a turn).
- Today's settings: value +67/turn, cash +46/turn, prestige -1.52/turn - breaks the prestige floor.
- Plan: value -71/turn, cash -58/turn, prestige +1.53/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -3 vs +16, +123 vs +29, +52 vs +53.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Fulkirch: +1/turn
  - ship Flax Wyrm -> no route: +0/turn
  - ropewalk 1 0.25 -> 0.15: +11/turn
  - net maker 0.00 -> 0.28: +9/turn
  - flax farm 1 4.64 -> 3.98: -1/turn
  - retting pit 1 0.91 -> 0.81: -1/turn
  - spinnery 1 1.65 -> 1.44: +6/turn
  - sewing shop 1 0.30 -> 0.36: -7/turn
  - weavery 1 0.50 -> 0.60: +9/turn
  - mansion 1 0.00 -> 0.73: -163/turn
- Model check over the last 61 turns: predicted +97/turn for the settings we ran, real +30/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.64, thread 4.16, cloth 6.62, flax fibres 5.00, garments 19.12, nets 29.63, beer 2.91, timber 3.08, prestige 56.06, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 2 (v2 3); flax plants sell 3 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 0); labour buy 29 (v2 12); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Fulkirch (+1/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +82/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 435 (+146 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.89 |
| ret | 3 | 0.91 | 0.98 |
| spin | 4 | 1.65 | 1.72 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 560/228, cloth 72/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask none (no sellers at home)
- R5: flax fibres buy not filling: bid 5.05 under the home ask 5.95 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
