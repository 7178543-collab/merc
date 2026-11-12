# v2 shadow report

Turn 13965, 2026-11-12 06:08. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,212, prestige 3,560 (440 free, -2.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 7 | 0 | 4 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 35 | 0 | 2 | 0 | 0 | min_holding 30, sell 10, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 18, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 506 | 0 | 23 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **beer**: needed (4.2/turn) but there is NO buy order, stock 6.8 -> v2: add buy 9
- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **labour**: 23 labour expired last turn (~38 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 526, not 626

## Prestige spending, cheapest coin per prestige first

436 turns left: prestige gained now converts 88.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.2 | 49.2 | running |
| jousting 3 | arena | 230 | 54.7 | 55.0 | needs a arena (build cost 26,014); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 56.5 | 56.5 | thin at home: wine, stockfish |
| hold banquet 1 (fish) | mansion | 4.2 | 57.2 | 57.2 |  |
| hold banquet 3 (pies) | mansion | 8 | 57.4 | 57.4 |  |
| jousting 2 | arena | 210 | 59.9 | 60.2 | needs a arena (build cost 26,014); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 60.5 | 60.5 | thin at home: wine, ham, stockfish |
| hold banquet 2 (pies) | mansion | 7 | 60.8 | 60.8 | thin at home: wine |
| hold banquet 4 (premium) | mansion | 20 | 60.9 | 60.9 | thin at home: wine, stockfish |
| hold banquet 3 (fish) | mansion | 7.6 | 62.3 | 62.3 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 64.4 | 64.4 | thin at home: wine |
| hold banquet 1 (meat) | mansion | 4.2 | 64.5 | 64.5 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.20 | 20 | 134102075 | 0.344 | - | furniture 20, pasties 2 | -302 |
| linen snake | 0.1 / 0.10 | 10 | 151802239 | 0.436 | - | furniture 1, pasties 7 | -120 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 16.4 (keep 14); best orders clear only -8 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 5 @ 15.4 (keep 14); best orders clear only 7 a turn after crew: ship stays at 0
- best towns now: Orlesailles +31, Clarfranche +18, Dortgart +16
- Orlesailles would trade: pasties buy 5 @ 10.5; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~106 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Amsdermund | 1111 | 0.40 | 0.30 (32/turn) | cured fish 9 (24.57->34.2), garments 10 (18.91->20.52), canvas 3 (42.21->45.03), nets 5 (36.2->38) | cloth 24 (7.56->10.3), bellows 1 (268.8->285), tools 14 (5.1->5.84), copper ingots 1 (17.96->19.76) | +189 |
| Kirchwerp | 1072 | 0.38 | 0.30 (32/turn) | honey 7 (9.82->13.21), canvas 3 (42.21->46.17), garments 10 (18.91->20.33), nets 6 (36.2->38.57) | cloth 24 (7.56->10.3), tools 14 (4.62->5.84), axes 3 (16.8->18.05), copper ingots 2 (18.27->19.76) | +136 |
| Darmwald | 1022 | 0.35 | 0.60 (64/turn) | beer 60 (3.78->5.65), tapestries 1 (740.25->760), lead ore 4 (9.55->14.25), malt 2 (7.09->13.11) | axes 1 (15.75->18.05), cured meat 3 (22.05->23.37), resin 1 (3->3.91) | +131 |
| Hanstein | 380 | 0.11 | 0.20 (21/turn) | dyed cloth 10 (11.55->13.96), garments 10 (18.91->21.09), timber 11 (8.24->10.26), nets 5 (36.2->37.05) | cloth 17 (8.35->10.3), thread 28 (4.68->5.55), seeds 22 (1.81->2.51), flax fibres 12 (5.67->6.55) | +126 |
| Brebronn | 862 | 0.26 | 0.20 (21/turn) | garments 10 (18.91->21.85), pies 2 (15.86->18.43) | cloth 24 (7.88->10.3), wine 15 (5.25->6.93), sails 1 (855.75->878.75), copper ingots 2 (17.43->19.76) | +124 |

**Best:** Amsdermund at about +189 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 36.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 9 @ 3.78, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 7 = 1.6 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 86.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres |  | 2 @ min 5.85 | goal planner: sells 2 a turn at 5.85, keeps 85 (no one offered it) |
| flax plants |  | 2 @ min 1.14 | goal planner: sells 2 a turn at 1.14, keeps 219 (no one offered it) |
| furniture | 2 @ 16.2, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.0) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 26) |
| light armour | 1 @ 104, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 35.2) |
| pasties |  | 1 @ min 13.7 | goal planner: trial sale of an idle pile, 1 a turn at 13.7, keeps 0 (9 over) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 80.5 |  |
| tar | 1 @ 11.0, stop 1 |  | uses 0.4/turn (ropewalk 1), makes 0.0, holds 1 = 1.5 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 26.7k (cash + stock at home prices); +43/turn over 6 turns, -99/turn over 24 turns.
- Limits: cash flow >= -259/turn, prestige >= -0.58/turn (values are after 200 tax a turn).
- Today's settings: value +38/turn, cash +79/turn, prestige -2.41/turn - breaks the prestige floor.
- Plan: value -18/turn, cash +77/turn, prestige -0.58/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +86 vs +114, +7 vs +83, +404 vs +105.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Clairas: +1/turn
  - ship Flax Wyrm -> no route: +0/turn
  - brewery 1 0.14 -> 0.08: +12/turn
  - net maker 0.00 -> 0.29: +7/turn
  - ropewalk 1 0.25 -> 0.00: +13/turn
  - weavery 1 0.50 -> 0.60: -0/turn
  - sewing shop 1 0.30 -> 0.36: +10/turn
  - flax farm 1 4.64 -> 4.02: -2/turn
  - retting pit 1 0.91 -> 0.80: +1/turn
  - spinnery 1 1.65 -> 1.31: +5/turn
- Model check over the last 61 turns: predicted +108/turn for the settings we ran, real +13/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.64, thread 4.12, cloth 6.58, flax fibres 4.88, garments 19.04, nets 29.72, beer 3.06, timber 3.17, prestige 62.60, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax fibres sell 2 (v2 none); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 26); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.04, worth +2/turn.
- Ship linen snake: Grandgues -> Clairas (+1/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +80/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1724 coin: +1/turn, payback 2467 turns, doesn't pay yet

## Chain sizing

Mode HOLD, garments sold 10.0/turn (+0.0 exported); plan makes 32.4 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 405 (+114 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 3.51 |
| ret | 3 | 0.91 | 0.70 |
| spin | 4 | 1.65 | 1.67 |
| weave | 3 | 0.50 | 1.27 |
| sew | 2 | 0.30 | 0.79 |

Buffers: flax fibres 164/77, thread 1050/227, cloth 72/127

## Self-diagnosis

- R1: beer slot dry: 6.8 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy none, home ask 3.6 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 9 @ 3.66 (ask 3.6, cap 5.7))
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
