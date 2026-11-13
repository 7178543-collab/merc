# v2 shadow report

Turn 13995, 2026-11-13 12:17. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 15,282, prestige 3,487 (367 free, -2.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 0 | 0 | 0 | 15 | 0 | min_holding 60, sell 8, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 21, buy 6, buy @ 3.7 |
| labour | 64 | 29 | 504 | 0 | 25 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **beer**: needed (15.0/turn) but there is NO buy order, stock 0.0 -> v2: add buy 30
- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.58 is above it); knock-on: mansion 1 (no beer); labour need rises ~53/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.58 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **labour**: 25 labour expired last turn (~46 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 99 over real use lately; planning 512, not 611

## Prestige spending, cheapest coin per prestige first

406 turns left: prestige gained now converts 87.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 54.6 | 54.6 | running |
| jousting 3 | arena | 230 | 56.3 | 56.7 | needs a arena (build cost 27,979); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 59.8 | 59.8 | thin at home: cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 60.0 | 60.0 | thin at home: cured fish |
| hold banquet 4 (pies) | mansion | 18 | 60.4 | 60.4 | thin at home: hop beer, ham, stockfish, pies, candles |
| hold banquet 4 (premium) | mansion | 20 | 60.6 | 60.6 | thin at home: hop beer, ham, stockfish, candles |
| hold banquet 2 (pies) | mansion | 7 | 60.9 | 60.9 | thin at home: pies, candles |
| hold banquet 3 (pies) | mansion | 8 | 61.9 | 61.9 | thin at home: hop beer, pies, candles |
| jousting 2 | arena | 210 | 61.7 | 62.1 | needs a arena (build cost 27,979); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 62.3 | 62.3 | thin at home: hop beer, cured fish |
| hold banquet 4 | mansion | 17.5 | 63.9 | 63.9 | thin at home: hop beer, ham, stockfish, candles |
| hold mass 2 (premium) | cathedral | 360 | 61.1 | 64.1 | needs a cathedral (build cost 313,130); thin at home: furniture, jewellery, glassware, candles, premium garments |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 15.0 (keep 14); best orders clear only -3 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 15.6 (keep 14); best orders clear only -5 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~113 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 1.00 (113/turn) | timber 37 (8.56->12.35), firewood 43 (2.71->6.65), bread 136 (2.73->2.94), nets 2 (37.6->38.57) | cured meat 1 (24.57->29.07), tar 3 (9.97->11.4), tools 8 (4.94->5.08) | +258 |
| Vauxvais | 204 | 0.06 | 1.00 (113/turn) | beer 58 (3.89->5.61), firewood 51 (2.71->5.7), charcoal 18 (2.35->4.29), premium cheese 1 (28.98->33.82) | cloth 13 (8.09->8.7), cured meat 2 (25.83->29.07), flax fibres 12 (6.25->6.75), seeds 6 (1.94->2.51) | +209 |
| Herschweig | 775 | 0.23 | 0.30 (34/turn) | beer 51 (3.89->5.94), tackles 2 (174.3->181.45), wine 2 (7.3->7.74) | cookware 9 (23.73->25.27), flax fibres 11 (5.25->6.75), cured meat 2 (26.25->29.07), tar 4 (9.82->11.4) | +128 |
| Hanstein | 380 | 0.11 | 0.50 (56/turn) | timber 18 (8.56->11.59), charcoal 17 (2.35->4.39), garments 10 (22->23.75), tools 16 (5.83->6.08) | grain 86 (2.5->2.85), cloth 11 (7.72->8.7), seeds 17 (1.77->2.51), cured meat 2 (24.78->29.07) | +121 |
| Clarfranche | 1484 | 0.66 | 0.20 (23/turn) | premium cheese 9 (28.98->32.87), acid 1 (115.5->124.45), tackles 2 (174.3->179.55), rope 1 (83->85.02) | cookware 9 (16.91->25.27), premium steel 2 (42.42->45.79), cloth 15 (7.93->8.7), cured meat 2 (27.09->29.07) | +120 |

**Best:** Grandgues at about +258 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 35.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 30 @ 3.88, stop 60 | off | a building is stalled on beer: no sell until it runs again |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 6) |
| candles | 2 @ 75.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cured meat | 4 @ 31.4, stop 13 |  | goal planner: buys 4 a turn for today's rates, keeps up to 13 (v2 had None) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 16.2, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 21.4) |
| grain | 6 @ 3.7, stop 21 |  | goal planner: buys 6 a turn for today's rates, keeps up to 21 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 12) |
| light armour | 1 @ 107, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 36.6) |
| pasties |  | 1 @ min 17.4 | goal planner: sells 1 a turn at 17.4, keeps 0 (no one offered it) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 81.0) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 1 = 3.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.6k (cash + stock at home prices); +223/turn over 6 turns, +110/turn over 24 turns.
- Limits: cash flow >= -470/turn, prestige >= -0.28/turn (values are after 200 tax a turn).
- Today's settings: value -244/turn, cash -144/turn, prestige +1.65/turn.
- Plan: value -50/turn, cash -34/turn, prestige -0.28/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +190 vs +52, +127 vs +51, +29 vs -126.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Vauxvais: +2/turn
  - ship Flax Wyrm -> no route: +0/turn
  - mansion 1 1.00 -> 0.54: +165/turn
  - brewery 1 0.14 -> 0.09: +11/turn
  - spinnery 1 1.65 -> 1.35: +6/turn
  - retting pit 1 0.91 -> 0.85: +1/turn
  - flax farm 1 4.64 -> 4.27: +3/turn
  - net maker 0.00 -> 0.29: +0/turn
  - weavery 1 0.50 -> 0.38: -7/turn
  - sewing shop 1 0.30 -> 0.22: +10/turn
- Model check over the last 60 turns: predicted +102/turn for the settings we ran, real -11/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.96, garments 19.30, nets 30.24, beer 3.15, timber 3.35, prestige 68.81, cash 0.00
- Orders it would set: bread buy 5 (v2 6); candles buy 2 (v2 None); cured meat buy 4 (v2 None); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 6 (v2 0); labour buy 64 (v2 12); light armour buy 1 (v2 None); pasties sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.30, worth +10/turn.
- Ship linen snake: Grandgues -> Vauxvais (+2/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1957 coin: +3/turn, payback 563 turns, doesn't pay yet (materials thin at home: limestone)

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 416 (+127 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 3.96 |
| ret | 3 | 0.91 | 0.79 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 134/77, thread 1050/228, cloth 72/128

## Self-diagnosis

- R1: beer slot dry: 0.0 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy none, home ask 3.7 -> **buy 39 @ 3.76 (ask 3.7, cap 14.4)** (ok)
- R1: cured meat slot dry: 3.2 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 4 @ 31.4, home ask none (no sellers at home)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.58; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
