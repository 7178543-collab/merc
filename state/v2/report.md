# v2 shadow report

Turn 13968, 2026-11-12 09:40. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,920, prestige 3,552 (432 free, -2.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 0 | 0 | 0 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 36 | 0 | 2 | 0 | 0 | min_holding 30, sell 10, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 21, buy 6, buy @ 3.7 |
| labour | 29 | 29 | 507 | 0 | 22 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 11.00 x20, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 22 labour expired last turn (~36 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 507, not 600

## Prestige spending, cheapest coin per prestige first

433 turns left: prestige gained now converts 88.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.9 | 48.9 | running |
| hold banquet 4 (pies) | mansion | 18 | 52.8 | 52.8 | thin at home: pasties, ham, stockfish |
| jousting 3 | arena | 230 | 55.3 | 55.6 | needs a arena (build cost 27,076); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 55.8 | 55.8 | thin at home: ham, stockfish |
| hold banquet 2 (pies) | mansion | 7 | 56.4 | 56.4 | thin at home: pasties |
| hold banquet 3 (pies) | mansion | 8 | 56.6 | 56.6 | thin at home: pasties |
| hold banquet 1 (fish) | mansion | 4.2 | 57.4 | 57.4 |  |
| hold banquet 4 (premium) | mansion | 20 | 58.4 | 58.4 | thin at home: ham, stockfish |
| hold banquet 2 (fish) | mansion | 6.8 | 59.5 | 59.5 | thin at home: cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 60.8 | 60.8 | thin at home: cured fish |
| jousting 2 | arena | 210 | 60.6 | 60.9 | needs a arena (build cost 27,076); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 66.6 | 66.6 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 5 @ 14.5 (keep 14); best orders clear only 12 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 5 @ 15.6 (keep 14); best orders clear only 6 a turn after crew: ship stays at 0
- best towns now: Orlesailles +29, Herschweig +24, Clarfranche +20, Magdeach +17, Fulkirch +15
- Orlesailles would trade: pasties buy 5 @ 11.0; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~104 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Darmwald | 1022 | 0.34 | 0.60 (62/turn) | beer 65 (3.89->6.03), cheese 5 (8.51->10.54), lead ore 2 (9.19->14.91), malt 1 (7.56->12.92) | cloth 9 (7.35->9.03), flax fibres 2 (7.3->11.49), butter 1 (76.65->81.22), cured meat 3 (22.05->23.94) | +146 |
| Neuborn | 780 | 0.22 | 1.00 (104/turn) | timber 29 (7.56->12.82), wine 11 (7.4->9.97), garments 7 (18.84->22.04), nets 2 (37.4->38.95) | flax fibres 2 (6.35->11.49), resin 0 (3.15->3.72) | +126 |
| Blanans | 297 | 0.08 | 0.60 (62/turn) | timber 37 (7.56->10.07), garments 10 (18.84->20.71), ploughs 2 (84.53->91.67), limestone 1 (19.11->31.35) | flax fibres 4 (6.04->11.49), cloth 9 (7.93->9.03), garments 2 (23.1->23.4) | +116 |
| Hanstein | 380 | 0.10 | 0.30 (31/turn) | garments 10 (18.84->21.09), steel ingots 4 (21.42->23.18), lead ore 1 (9.19->12.82), wax 3 (24.99->25.65) | thread 29 (4.68->5.6), flax fibres 4 (5.67->11.49), seeds 20 (1.85->2.51), cloth 9 (8.14->9.03) | +95 |
| Herschweig | 775 | 0.21 | 0.30 (31/turn) | beer 43 (3.89->4.84), garments 10 (18.84->20.9), nets 6 (37.4->39.71), flour 1 (18.38->22.99) | flax fibres 4 (6.46->11.49), spinning wheels 1 (197.4->205.2), ham 1 (85.58->87.88), spirits 1 (10.29->12.92) | +88 |

**Best:** Darmwald at about +146 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 36.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 88, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.14 | goal planner: sells 2 a turn at 1.14, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 22.8) |
| grain | 6 @ 3.7, stop 21 |  | goal planner: buys 6 a turn for today's rates, keeps up to 21 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 7) |
| light armour | 1 @ 108, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 36.4) |
| pasties |  | 1 @ min 13.1 | goal planner: trial sale of an idle pile, 1 a turn at 13.1, keeps 0 (9 over) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.5k (cash + stock at home prices); +304/turn over 6 turns, -10/turn over 24 turns.
- Limits: cash flow >= -330/turn, prestige >= -0.55/turn (values are after 200 tax a turn).
- Today's settings: value +30/turn, cash -12/turn, prestige -2.87/turn - breaks the prestige floor.
- Plan: value -39/turn, cash -271/turn, prestige -0.55/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +141 vs +79, +848 vs +86, +718 vs +41.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Calange: +7/turn
  - ship Flax Wyrm -> Hofkirchen: +1/turn
  - ropewalk 1 0.25 -> 0.10: +11/turn
  - net maker 0.00 -> 0.29: +14/turn
  - spinnery 1 1.65 -> 1.22: +7/turn
  - weavery 1 0.50 -> 0.43: -13/turn
  - flax farm 1 4.64 -> 11.00: -90/turn
  - retting pit 1 0.91 -> 2.20: +123/turn
  - mansion 1 0.00 -> 0.55: -138/turn
- Model check over the last 61 turns: predicted +107/turn for the settings we ran, real +20/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.63, thread 4.29, cloth 6.73, flax fibres 5.42, garments 19.30, nets 30.41, beer 3.05, timber 3.73, prestige 64.48, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax plants sell 2 (v2 none); garments sell 11 (v2 10); grain buy 6 (v2 0); labour buy 29 (v2 7); light armour buy 1 (v2 None); pasties sell 1 (v2 none)
- Ship linen snake: Grandgues -> Calange (+7/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Hofkirchen (+1/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +82/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1896 coin: +2/turn, payback 1059 turns, doesn't pay yet
  - +1 plot flax farm 1 for ~528 coin: +1/turn, payback 449 turns, doesn't pay yet

## Chain sizing

Mode HOLD, garments sold 10.0/turn (+0.0 exported); plan makes 32.4 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 407 (+117 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 3.63 |
| ret | 3 | 0.91 | 0.73 |
| spin | 4 | 1.65 | 1.67 |
| weave | 3 | 0.50 | 1.27 |
| sew | 2 | 0.30 | 0.79 |

Buffers: flax fibres 156/77, thread 1058/227, cloth 72/127

## Self-diagnosis

- R1: beer slot dry: 0.0 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy none, home ask 3.7 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 9 @ 3.76 (ask 3.7, cap 5.7))
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1058 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
