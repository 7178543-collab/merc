# v2 shadow report

Turn 13826, 2026-11-06 11:32. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,468, prestige 3,282 (162 free, -0.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 10 | 4 | 4 | 0 | 0 | stop 14, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 9 | 9 | 0 | 0 | stop 36, buy 11, buy @ 3.7 |
| labour | 29 | 29 | 518 | 0 | 11 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.50 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.50 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +1 crew for linen snake (crew 0.01, no projection from the game)
- labour: projection runs 100 over real use lately; planning 519, not 619

## Prestige spending, cheapest coin per prestige first

575 turns left: prestige gained now converts 94.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.5 | 49.5 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 54.2 | 54.2 |  |
| jousting 3 | arena | 230 | 54.2 | 54.4 | needs a arena (build cost 25,980); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 55.5 | 55.5 | thin at home: ham, stockfish, pies |
| hold banquet 1 (meat) | mansion | 4.2 | 58.2 | 58.2 |  |
| hold banquet 4 | mansion | 17.5 | 59.1 | 59.1 | thin at home: ham, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 59.1 | 59.1 | thin at home: ham, stockfish, premium cheese |
| jousting 2 | arena | 210 | 59.4 | 59.6 | needs a arena (build cost 25,980); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 59.7 | 59.7 | thin at home: pies |
| hold banquet 2 (fish) | mansion | 6.8 | 60.7 | 60.7 | thin at home: cured fish |
| hold sermon 2 (candles) | church | 31 | 56.4 | 60.7 | needs a church (build cost 65,806); thin at home: candles |
| hold banquet 2 (pies) | mansion | 7 | 60.8 | 60.8 | thin at home: pies |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: pasties buy 9 @ 15.5; crew 0.1; est +20 a turn; stock: pasties 9 @ 15.5 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 5 @ 15.1 (keep 14); best orders clear only 9 a turn after crew: ship stays at 0
- best towns now: Orlesailles +50, Angefont +40, Bordees +36, Fulkirch +34, Toqueque +28
- Orlesailles would trade: pasties buy 14 @ 13.8; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~104 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hanstein | 380 | 0.11 | 0.40 (42/turn) | timber 17 (7.35->11.59), bellows 1 (201.6->228), limestone 2 (18.27->32.68), nets 5 (34.6->36.29) | cheese 5 (6.14->9.17), flax plants 30 (1.26->1.88), thread 34 (4.77->5), candles 1 (82.42->85.5) | +134 |
| Fontaux | 411 | 0.11 | 0.60 (63/turn) | timber 26 (7.35->10.92), garments 10 (24->28.12), bellows 1 (201.6->220.4), furniture 15 (14.18->15.01) | casks 2 (5.67->6.65), cloth 4 (8.29->8.95), flax fibres 5 (5.35->5.9), candles 1 (84.53->85.5) | +117 |
| Grandgues | 152 | 0.04 | 0.20 (21/turn) | bellows 1 (201.6->243.2), timber 26 (7.35->9.17), flour 3 (18.38->22.04), logs 1 (3.95->7.79) | cheese 5 (6.51->9.17), candles 1 (81.38->85.5), cloth 4 (8.45->8.95), casks 2 (6.14->6.65) | +106 |
| Blanans | 297 | 0.08 | 0.50 (52/turn) | timber 26 (7.35->9.88), bellows 1 (201.6->214.7), medicine 2 (162.75->168.15), nets 4 (34.6->36.86) | cloth 9 (7.35->8.95), cheese 5 (7.3->9.17), candles 1 (79.8->85.5), flax plants 11 (1.4->1.88) | +105 |
| Bordetes | 831 | 0.24 | 0.20 (21/turn) | cured fish 4 (22.68->30.97), furniture 15 (14.18->16.05), gold ore 1 (154.35->165.3), hop beer 3 (10.82->11.3) | cheese 5 (6.2->9.17), garments 20 (21.84->22.8), cloth 13 (8.03->8.95), candles 1 (78.75->85.5) | +100 |

**Best:** Hanstein at about +134 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.2, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 4.0 turns |
| beer |  | 16 @ min 3.06 | goal planner: sells 16 at 3.06 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 16 = 3.9 turns |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 7) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.4) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 10) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 19) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 23.5k (cash + stock at home prices); +56/turn over 6 turns, +152/turn over 24 turns.
- Limits: cash flow >= -269/turn, prestige >= +5.77/turn (values are after 200 tax a turn).
- Today's settings: value +77/turn, cash +67/turn, prestige -0.81/turn - breaks the prestige floor.
- Plan: value -146/turn, cash -51/turn, prestige +3.39/turn - could not meet the prestige floor.
- Cash check (real vs predicted cash a tick, last 3): +132 vs +85, -239 vs +87, +37 vs +89 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Donaunieder: +9/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +7/turn
  - sewing shop 1 0.30 -> 0.36: -9/turn
  - weavery 1 0.50 -> 0.60: +11/turn
  - ropewalk 1 0.25 -> 0.00: -7/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.22: +13/turn
  - spinnery 1 1.65 -> 1.03: -17/turn
  - retting pit 1 0.91 -> 0.58: +2/turn
  - brewery 1 0.14 -> 0.27: -15/turn
- Model check over the last 62 turns: predicted +99/turn for the settings we ran, real +63/turn.
- Worth of one more unit per turn: labour 1.65, thread 4.14, cloth 6.62, flax fibres 4.91, garments 19.15, nets 29.88, beer 2.96, timber 3.15, prestige 10000.00, cash 0.00
- Orders it would set: beer sell 16 (v2 15); cloth sell 1 (v2 none); firewood buy 4 (v2 7); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 10); labour buy 29 (v2 19); light armour buy 1 (v2 None); rope sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.22, worth +11/turn.
- Ship linen snake: Grandgues -> Donaunieder (+9/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +82/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 456 (+167 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 5.37 |
| ret | 3 | 0.91 | 1.07 |
| spin | 4 | 1.65 | 1.89 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 457/228, cloth 73/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 5.9 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
