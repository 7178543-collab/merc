# v2 shadow report

Turn 13862, 2026-11-07 23:41. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 8,483, prestige 3,503 (383 free, +148.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 15, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 4 | 4 | 4 | 0 | 0 | stop 13, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 21 | 8 | 9 | 0 | 0 | stop 7, buy 2, buy @ 3.7 |
| labour | 29 | 29 | 518 | 0 | 11 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 12.60 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Tuning

- **bread**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 12.60 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 99 over real use lately; planning 520, not 618

## Prestige spending, cheapest coin per prestige first

539 turns left: prestige gained now converts 93.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.5 | 49.5 | running |
| jousting 3 | arena | 230 | 54.3 | 54.5 | needs a arena (build cost 25,283); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 55.1 | 55.1 | thin at home: pasties, wine, ham, stockfish, cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 55.2 | 55.2 |  |
| hold banquet 1 (meat) | mansion | 4.2 | 56.8 | 56.8 |  |
| hold banquet 4 | mansion | 17.5 | 57.9 | 57.9 | thin at home: wine, ham, stockfish, cheese |
| hold banquet 4 (premium) | mansion | 20 | 58.4 | 58.4 | thin at home: wine, ham, stockfish, premium cheese |
| jousting 2 | arena | 210 | 59.4 | 59.7 | needs a arena (build cost 25,283); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 60.6 | 60.6 | thin at home: wine, cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 61.2 | 61.2 | thin at home: cheese |
| hold banquet 2 (meat) | mansion | 6.8 | 61.3 | 61.3 | thin at home: wine, cheese |
| hold banquet 3 (pies) | mansion | 8 | 61.3 | 61.3 | thin at home: pasties, cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 16.4 (keep 14); best orders clear only -1 a turn after crew: ship stays at 0
- best towns now: Kleinburgh +20
- Kleinburgh would trade: pasties buy 6 @ 13.9; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~105 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Neuborn | 780 | 0.22 | 0.30 (32/turn) | wine 12 (6.3->8.88), nets 5 (33.6->36.86), beer 15 (2.98->3.97), garments 10 (22.4->22.99) | cloth 19 (7.88->9.45), candles 1 (77.7->82.5), tallow 1 (21->22.99), tar 6 (10.71->11.4) | +98 |
| Pontmont | 341 | 0.10 | 0.30 (32/turn) | charcoal 19 (2.25->4.75), garments 10 (22.4->25.46), bricks 3 (7.14->10.54), beer 15 (2.98->3.32) | cloth 12 (8.66->9.45), gold ore 1 (142.8->151.05), cheese 5 (7.72->9.17), candles 1 (79.28->82.5) | +93 |
| Hanstein | 380 | 0.11 | 0.30 (32/turn) | charcoal 19 (2.25->3.31), canvas 1 (30.87->32.49), leather 1 (28.35->28.88), limestone 1 (15.86->20.52) | cloth 19 (7.93->9.45), flax fibres 17 (5.41->6.6), thread 44 (4.35->4.74), cheese 5 (6.77->9.17) | +84 |
| Kirchwerp | 1072 | 0.38 | 0.40 (42/turn) | thread 61 (4.66->5.7), wine 12 (6.3->7.6), hinges 1 (37.59->47.5), flour 1 (21->25.08) | cheese 5 (6.2->9.17), candles 1 (76.12->82.5), garments 2 (24.15->24.6) | +75 |
| Rouhomme | 368 | 0.10 | 0.30 (32/turn) | charcoal 19 (2.25->3.69), thread 16 (4.66->5.42), beer 15 (2.98->3.53), garments 10 (22.4->22.99) | tools 16 (4.51->5.37), cheese 5 (7.04->9.17), candles 1 (73.5->82.5), cloth 15 (8.87->9.45) | +72 |

**Best:** Neuborn at about +98 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 31.2, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 4.0 turns |
| beer |  | 15 @ min 3.38 |  |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 16 = 3.9 turns |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 4 @ 2.4, stop 13 |  | goal planner: buys 4 a turn for today's rates, keeps up to 13 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 21.8) |
| grain | 2 @ 3.7, stop 8 |  | goal planner: buys 2 a turn for today's rates, keeps up to 8 (v2 had 17) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 20) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 20.8k (cash + stock at home prices); -527/turn over 6 turns, -20/turn over 24 turns.
- Limits: cash flow >= -187/turn, prestige >= -0.35/turn (values are after 200 tax a turn).
- Today's settings: value +62/turn, cash +47/turn, prestige +148.07/turn.
- Plan: value +398/turn, cash +251/turn, prestige +140.07/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -1460 vs +63, -2439 vs +54, -6 vs +52 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Rouhomme: +6/turn
  - ship Flax Wyrm -> Chatgnan: +1/turn
  - park 1 16.00 -> 0.00: +48/turn
  - flax farm 1 4.64 -> 8.02: +29/turn
  - retting pit 1 0.91 -> 1.57: +32/turn
  - spinnery 1 1.65 -> 2.77: +64/turn
  - weavery 1 0.50 -> 1.32: +96/turn
  - net maker [make nets 1] 0.00 -> 0.38: +27/turn
  - sewing shop 1 0.30 -> 0.36: +12/turn
  - brewery 1 0.14 -> 0.03: +20/turn
- Model check over the last 61 turns: predicted +103/turn for the settings we ran, real +15/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.05, thread 2.64, cloth 4.21, flax fibres 3.14, garments 12.17, nets 19.73, beer 2.50, timber 3.29, prestige 0.00, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 4 (v2 8); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 2 (v2 17); labour buy 29 (v2 20); light armour buy 1 (v2 None); rope sell 2 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.31, worth +39/turn.
- Recipe: net maker make nets 3 -> make nets 1 at 0.38, worth +18/turn.
- Ship linen snake: Grandgues -> Rouhomme (+6/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Chatgnan (+1/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +52/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
- Trim: donate park 1: +96/turn (tax 96 saved).

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 436 (+147 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.92 |
| ret | 3 | 0.91 | 0.98 |
| spin | 4 | 1.65 | 1.73 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 553/228, cloth 72/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.6 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
- R5: tar buy not filling: bid 11 under the home ask 12.6 for 3 turns, bought 0.0 of 1, 0.0 held (0.0 turns); raise needs Taylor (ceiling 11.0)
