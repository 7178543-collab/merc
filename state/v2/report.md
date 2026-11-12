# v2 shadow report

Turn 13971, 2026-11-12 12:57. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,596, prestige 3,543 (423 free, -2.8/turn).

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
| labour | 29 | 29 | 516 | 0 | 13 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 516, not 612

## Prestige spending, cheapest coin per prestige first

430 turns left: prestige gained now converts 88.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.4 | 50.4 | running |
| hold banquet 4 (pies) | mansion | 18 | 54.1 | 54.1 | thin at home: pasties, ham, stockfish, candles |
| jousting 3 | arena | 230 | 54.7 | 55.0 | needs a arena (build cost 26,078); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 56.6 | 56.6 | thin at home: ham, stockfish, candles |
| hold banquet 1 (fish) | mansion | 4.2 | 57.9 | 57.9 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 57.9 | 57.9 |  |
| hold banquet 2 (pies) | mansion | 7 | 57.9 | 57.9 | thin at home: pasties, pies, candles |
| hold banquet 4 (premium) | mansion | 20 | 58.9 | 58.9 | thin at home: ham, stockfish, candles |
| hold banquet 3 (pies) | mansion | 8 | 59.2 | 59.2 | thin at home: pasties, pies, candles |
| hold banquet 3 (fish) | mansion | 7.6 | 60.2 | 60.2 |  |
| jousting 2 | arena | 210 | 59.9 | 60.3 | needs a arena (build cost 26,078); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| jousting 1 | arena | 170 | 65.5 | 65.9 | needs a arena (build cost 26,078); thin at home: protection, light armour, arms; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 10 | 134102075 | 0.044 | - | furniture 2, pasties 1 | -40 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: furniture buy 2 @ 14.6, pasties buy 1 @ 16.0; crew 0.1; est +16 a turn; stock: furniture 2 @ 14.6 (keep 145); stock: pasties 1 @ 16.0 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: furniture 2 @ 14.0 (keep 145); best orders clear only 14 a turn after crew: ship stays at 0
- best towns now: Clairlond +22, Disscester +21, Gotthafen +21, Helmgreen +20, Brebronn +20
- Clairlond would trade: furniture buy 2 @ 13.0, pasties buy 1 @ 13.8; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~104 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Darmwald | 1022 | 0.34 | 0.80 (83/turn) | beer 94 (3.89->6.13), malt 2 (7.14->13.21), garments 10 (18.8->19.57), lead ore 1 (10.03->14.54) | butter 1 (60.38->81.7), ploughs 1 (63->75.52), cured meat 3 (22.05->24.51), cloth 14 (7.35->7.8) | +202 |
| Großaue | 1136 | 0.41 | 0.10 (10/turn) | garments 10 (18.8->21.66), acid 1 (133.35->139.65), nets 2 (37.8->41.42), yarn 5 (3.99->4.75) | windows 1 (661.5->779), thread 13 (5.06->5.55) | +155 |
| Herschweig | 775 | 0.21 | 0.20 (21/turn) | tackles 1 (190.05->231.8), garments 10 (18.8->22.23), cloth 19 (8.19->8.98), wine 13 (6.56->7.55) | raw cloth 5 (5.17->7.17), ham 2 (83.48->87.88), thread 5 (4.41->5.55), cured meat 3 (23.1->24.51) | +116 |
| Großmühle | 751 | 0.21 | 0.10 (10/turn) | garments 10 (18.8->21.85), dyed cloth 9 (11.45->14.44), yarn 8 (3.99->4.99), flax plants 1 (1.95->2.47) | jewellery 1 (122.85->142.5), windows 1 (761.25->779), raw cloth 5 (5.99->7.17), cured meat 3 (23.52->24.51) | +105 |
| Gosschweig | 1099 | 0.39 | 0.20 (21/turn) | nets 6 (37.8->39.9), cured fish 5 (24.57->25.65), yarn 5 (3.99->4.73), hides 1 (12.6->13.68) | windows 1 (714->779), jewellery 1 (112.35->142.5), garments 2 (21.21->23) | +102 |

**Best:** Darmwald at about +202 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 87, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.14 | goal planner: sells 2 a turn at 1.14, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 22.4) |
| grain | 6 @ 3.7, stop 21 |  | goal planner: buys 6 a turn for today's rates, keeps up to 21 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 16) |
| light armour | 1 @ 108, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 36.8) |
| pasties |  | 2 @ min 12.5 | goal planner: trial sale of an idle pile, 2 a turn at 12.5, keeps 0 (13 over) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 81.5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.4k (cash + stock at home prices); +271/turn over 6 turns, -51/turn over 24 turns.
- Limits: cash flow >= -358/turn, prestige >= -0.51/turn (values are after 200 tax a turn).
- Today's settings: value +49/turn, cash +14/turn, prestige -2.83/turn - breaks the prestige floor.
- Plan: value -61/turn, cash -58/turn, prestige -0.51/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +366 vs -12, +161 vs -8, +150 vs +2.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Unterhufe: +0/turn
  - ship Flax Wyrm -> no route: +0/turn
  - ropewalk 1 0.25 -> 0.17: +8/turn
  - net maker 0.00 -> 0.29: +7/turn
  - spinnery 1 1.65 -> 1.31: -1/turn
  - retting pit 1 0.91 -> 0.80: +2/turn
  - weavery 1 0.50 -> 0.44: -0/turn
  - flax farm 1 4.64 -> 4.04: -8/turn
  - mansion 1 0.00 -> 0.55: -131/turn
- Model check over the last 61 turns: predicted +106/turn for the settings we ran, real +17/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.95, garments 19.30, nets 30.15, beer 3.04, timber 3.33, prestige 66.16, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax plants sell 2 (v2 none); garments sell 11 (v2 10); grain buy 6 (v2 0); labour buy 29 (v2 16); light armour buy 1 (v2 None); pasties sell 2 (v2 none)
- Ship linen snake: Grandgues -> Unterhufe (+1/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1903 coin: +2/turn, payback 889 turns, doesn't pay yet

## Chain sizing

Mode HOLD, garments sold 10.0/turn (+0.0 exported); plan makes 32.4 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 407 (+118 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 3.70 |
| ret | 3 | 0.91 | 0.74 |
| spin | 4 | 1.65 | 1.66 |
| weave | 3 | 0.50 | 1.27 |
| sew | 2 | 0.30 | 0.79 |

Buffers: flax fibres 150/77, thread 1050/226, cloth 72/127

## Self-diagnosis

- R1: beer slot dry: 0.0 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy none, home ask 3.7 -> **buy 9 @ 3.76 (ask 3.7, cap 5.7)** (ok)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
