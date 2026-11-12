# v2 shadow report

Turn 13970, 2026-11-12 11:51. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,447, prestige 3,546 (426 free, -2.8/turn).

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

**2 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.80 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 516, not 616

## Prestige spending, cheapest coin per prestige first

431 turns left: prestige gained now converts 88.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.8 | 49.8 | running |
| hold banquet 4 (pies) | mansion | 18 | 54.3 | 54.3 | thin at home: pasties, ham, stockfish |
| jousting 3 | arena | 230 | 54.6 | 54.9 | needs a arena (build cost 25,686); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 56.9 | 56.9 | thin at home: ham, stockfish |
| hold banquet 2 (fish) | mansion | 6.8 | 58.0 | 58.0 | thin at home: cheese |
| hold banquet 2 (pies) | mansion | 7 | 58.1 | 58.1 | thin at home: pasties, pies |
| hold banquet 1 (fish) | mansion | 4.2 | 58.2 | 58.2 | thin at home: beer |
| hold banquet 3 (pies) | mansion | 8 | 59.1 | 59.1 | thin at home: pasties, pies |
| hold banquet 4 (premium) | mansion | 20 | 59.3 | 59.3 | thin at home: ham, stockfish |
| hold banquet 3 (fish) | mansion | 7.6 | 59.9 | 59.9 | thin at home: cheese |
| jousting 2 | arena | 210 | 59.8 | 60.1 | needs a arena (build cost 25,686); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| jousting 1 | arena | 170 | 64.6 | 65.0 | needs a arena (build cost 25,686); thin at home: protection, light armour, arms; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 10 | 134102075 | 0.092 | - | furniture 1, pasties 3 | -56 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 2 @ 13.4, pasties buy 1 @ 16.1; crew 0.1; est +18 a turn; stock: furniture 2 @ 13.4 (keep 145); stock: pasties 1 @ 16.1 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 15.5 (keep 14); best orders clear only -4 a turn after crew: ship stays at 0
- best towns now: Etallaen +32, Clairlond +27, Helmgreen +25, Fulkirch +25, Disscester +24
- Etallaen would trade: furniture buy 2 @ 14.3, garments sell 6 @ 25.4, pasties buy 1 @ 12.2; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~104 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.90 (93/turn) | firewood 39 (4.28->7.65), garments 10 (18.79->20.52), limestone 9 (16.59->19), timber 28 (8.4->9.21) | jewellery 1 (114.45->145.35), furniture 7 (15.44->18.34), candles 1 (88.73->91.5), cured meat 3 (23.31->24.32) | +166 |
| Angefont | 686 | 0.19 | 0.30 (31/turn) | garments 10 (18.79->20.71), gold ore 1 (148.05->159.6), rope 1 (81.5->82.65), salt 4 (5.67->5.98) | flax fibres 28 (5.46->8.45), thread 62 (4.96->5.6), furniture 7 (16.17->18.34), seeds 7 (1.78->3.13) | +157 |
| Kirchwerp | 1072 | 0.37 | 0.50 (52/turn) | honey 7 (10.34->13.21), garments 10 (18.79->20.33), blades 4 (19.11->20.52), thread 91 (5->5.42) | flax fibres 28 (5.78->8.45), jewellery 1 (119.7->145.35), tools 15 (4.62->6.27), cloth 24 (7.56->8.1) | +143 |
| Darmwald | 1022 | 0.34 | 0.60 (62/turn) | beer 68 (3.89->5.61), malt 2 (7.19->13.11), garments 10 (18.79->19.57), salt 4 (5.67->6.22) | jewellery 1 (119.7->145.35), ploughs 2 (60.38->74.1), cloth 14 (7.35->8.1), cured meat 3 (22.05->24.32) | +142 |
| Hofkirchen | 991 | 0.33 | 0.50 (52/turn) | garments 10 (18.79->20.33), wine 3 (6.98->8.31), grain 2 (2.74->3.42) | flax fibres 28 (5.78->8.45), jewellery 1 (115.5->145.35), furniture 7 (15.02->18.34), cloth 24 (7.35->8.1) | +139 |

**Best:** Grandgues at about +166 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.14 | goal planner: sells 2 a turn at 1.14, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 22.6) |
| grain | 6 @ 3.7, stop 21 |  | goal planner: buys 6 a turn for today's rates, keeps up to 21 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 16) |
| light armour | 1 @ 98.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 36.8) |
| pasties |  | 1 @ min 12.7 | goal planner: trial sale of an idle pile, 1 a turn at 12.7, keeps 0 (12 over) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 79.5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.3/turn (ropewalk 1), makes 0.0, holds 0 = 1.5 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.5k (cash + stock at home prices); +303/turn over 6 turns, -10/turn over 24 turns.
- Limits: cash flow >= -352/turn, prestige >= -0.53/turn (values are after 200 tax a turn).
- Today's settings: value +41/turn, cash +2/turn, prestige -2.85/turn - breaks the prestige floor.
- Plan: value -66/turn, cash -62/turn, prestige -0.53/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +718 vs +41, +366 vs -12, +161 vs -8.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Hofkirchen: +4/turn
  - ship Flax Wyrm -> Marmont: +1/turn
  - net maker 0.00 -> 0.29: +7/turn
  - spinnery 1 1.65 -> 1.44: +3/turn
  - ropewalk 1 0.25 -> 0.00: +3/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.17: +9/turn
  - flax farm 1 4.64 -> 4.40: -2/turn
  - sewing shop 1 0.30 -> 0.36: -5/turn
  - weavery 1 0.50 -> 0.59: +7/turn
  - mansion 1 0.00 -> 0.55: -141/turn
- Model check over the last 61 turns: predicted +106/turn for the settings we ran, real +10/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.17, cloth 6.66, flax fibres 4.94, garments 19.27, nets 30.10, beer 3.07, timber 3.33, prestige 65.65, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax plants sell 2 (v2 none); garments sell 11 (v2 10); grain buy 6 (v2 0); labour buy 29 (v2 16); light armour buy 1 (v2 None); pasties sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.17, worth +6/turn.
- Ship linen snake: Grandgues -> Hofkirchen (+4/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Marmont (+1/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +82/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1718 coin: +2/turn, payback 891 turns, doesn't pay yet

## Chain sizing

Mode HOLD, garments sold 10.0/turn (+0.0 exported); plan makes 32.4 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 407 (+117 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 3.67 |
| ret | 3 | 0.91 | 0.73 |
| spin | 4 | 1.65 | 1.66 |
| weave | 3 | 0.50 | 1.27 |
| sew | 2 | 0.30 | 0.79 |

Buffers: flax fibres 153/77, thread 1050/226, cloth 72/127

## Self-diagnosis

- R1: beer slot dry: 0.0 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy none, home ask 4.02 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 9 @ 4.1 (ask 4.02, cap 5.7))
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
