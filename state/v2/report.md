# v2 shadow report

Turn 13512, 2026-10-24 09:42. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 971, prestige 3,583 (463 free, -0.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 72 | 0 | 7 | 0 | 0 | min_holding 60, sell 82, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 12 | 1 | 8 | 0 | 0 | stop 6, buy 2, buy @ 2.4; sell 1, sell @ 1.66 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 80 | 0 | 2 | 0 | 0 | min_holding 30, sell 2, sell @ 17.9 |
| grain | 90 | 37 | 41 | 0 | 0 | stop 158, buy 40, buy @ 3.7 |
| labour | 79 | 72 | 566 | 0 | 6 | buy 79, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 15 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 34 |
| porterage | 12 | 12 | 12 | 0 | 0 | buy 12, buy @ 1.1 |

**2 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **varnish**: net maker152202386007001 ran short of varnish (no buy order); labour need rises ~6/turn when they restart -> v2: add a varnish buy
- **varnish**: needed (0.1/turn) but there is NO buy order, stock 0.0 -> v2: add buy 1

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.5 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 57
- **tar**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 566, not 666

## Prestige spending, cheapest coin per prestige first

889 turns left: prestige gained now converts 98.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 45.0 | 45.0 | running |
| hold banquet 4 (pies) | mansion | 18 | 47.2 | 47.2 | thin at home: hop beer, wine, pies |
| hold banquet 3 (pies) | mansion | 8 | 49.6 | 49.6 | thin at home: hop beer, pies |
| hold banquet 4 | mansion | 17.5 | 49.8 | 49.8 | thin at home: wine, hop beer, ham, stockfish |
| hold banquet 2 (pies) | mansion | 7 | 51.1 | 51.1 | thin at home: wine, pies |
| jousting 3 | arena | 230 | 51.4 | 51.6 | needs a arena (build cost 24,166); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold prayer 2 | chapel | 13 | 49.5 | 52.3 | needs a chapel (build cost 30,717); thin at home: furniture |
| hold banquet 3 (fish) | mansion | 7.6 | 52.6 | 52.6 | thin at home: hop beer |
| hold banquet 2 (fish) | mansion | 6.8 | 53.1 | 53.1 | thin at home: wine |
| hold banquet 3 (meat) | mansion | 7.6 | 53.1 | 53.1 | thin at home: hop beer |
| hold sermon 2 (candles) | church | 31 | 50.6 | 53.2 | needs a church (build cost 64,382); thin at home: jewellery, furniture |
| hold banquet 2 (meat) | mansion | 6.8 | 53.6 | 53.6 | thin at home: wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only 13 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -7 a turn after crew: ship stays at 0
- best towns now: Bremcop +23
- Bremcop would trade: candles buy 1 @ 64.0, rope sell 3 @ 84.0; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~94 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Birkeningen | 1006 | 0.31 | 0.70 (66/turn) | beer 49 (3.06->4.89), garments 7 (17.9->22.99), charcoal 12 (1.85->6.08), thread 4 (3.35->4.46) | tar 5 (9.24->11.4), gears 2 (59.85->60.8), flax plants 2 (1.72->2.49) | +130 |
| Rouhomme | 368 | 0.09 | 1.00 (94/turn) | tackles 1 (182.7->201.4), firewood 24 (1.74->5.61), beer 63 (3.06->3.42), charcoal 9 (1.85->3.29) | candles 0 (50.4->67.5), lathes 0 (202.65->218.5), tar 3 (9.5->11.4), blades 0 (13.65->14.91) | +114 |
| Caillechâtel | 488 | 0.12 | 0.20 (19/turn) | beer 24 (3.06->6.17), thread 38 (3.35->3.86), acid 1 (136.5->143.45), nets 6 (35->35.91) | flax fibres 9 (4.81->5.4), flax plants 2 (1.25->2.49), furniture 1 (13.23->14.3), fleece 2 (6.77->6.93) | +99 |
| Nürnnieder | 520 | 0.13 | 0.10 (9/turn) | thread 48 (3.35->5.13), iron ore 2 (4.87->7.6), cloth 1 (7->7.46) | tar 2 (9.4->11.4), flax plants 2 (1.43->2.49), candles 1 (66.15->67.5) | +88 |
| Fontaux | 411 | 0.10 | 0.30 (28/turn) | thread 65 (3.35->4.41), charcoal 12 (1.85->4.26), casks 6 (5.25->6.13), flax fibres 3 (5.1->5.32) | tar 5 (10.08->11.4), flax plants 2 (1.54->2.49) | +84 |

**Best:** Birkeningen at about +130 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 82 @ min 3.06 | goal planner: sells 82 at 3.06 (v2 had 82 at 3.38) |
| cloth |  | 2 @ min 7 | goal planner: sells 2 a turn at 7, keeps 33 (no one offered it) |
| cured meat | 1 @ 29.0, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 2) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 2 @ 2.4, stop 6 | 1 @ min 1.67 | goal planner: buys 2 a turn for today's rates, keeps up to 6 (v2 had 2) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 15 @ min 17.9 | goal planner: sells 15 at 17.9 (v2 had 15 at 20.0) |
| grain | 38 @ 3.7, stop 149 |  | goal planner: buys 38 a turn for today's rates, keeps up to 149 (v2 had 79) |
| labour | 73 @ 2.2, stop - |  | goal planner: buys 73 for today's rates (v2 had 66) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 9 @ min 34.0 |  |
| pasties | 3 @ 14.5, stop 11 |  | goal planner: buys 3 a turn for today's rates, keeps up to 11 (v2 had 4) |
| porterage | 12 @ 1.1, stop - |  | goal planner: buys 12 for today's rates (v2 had 12) |
| rope |  | 5 @ min 71.0 | makes 2.9, uses 0.0, holds 25 (keeps 0): sells the surplus + 2/turn of the excess |
| tar | 2 @ 11.0, stop 3 |  | uses 0.6/turn (ropewalk 1), makes 0.0, holds 2 = 2.9 turns |
| thread |  | 6 @ min 4.34 | goal planner: sells 6 a turn at 4.34, keeps 225 (no one offered it) |
| tools | 2 @ 6.2, stop 13 |  | uses 1.5/turn (retting pit 1), makes 0.0, holds 199 = 130.8 turns |
| varnish | 1 @ 17.1, stop 1 |  | uses 0.1/turn (observed), makes 0.0, holds 0 = 0.0 turns |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 17.6k (cash + stock at home prices); +69/turn over 6 turns, +64/turn over 24 turns.
- Limits: cash flow >= +126/turn, prestige >= -0.68/turn (values are after 240 tax a turn).
- Today's settings: value +9/turn, cash -7/turn, prestige -0.67/turn - breaks the cash floor.
- Plan: value +63/turn, cash +126/turn, prestige -0.68/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -62 vs +118, -10 vs +142, -127 vs +35 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4, garments 0.5, nets 0.0, rope 0.1.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Rouhomme: +26/turn
  - ship Flax Wyrm -> Heidlowe: +1/turn
  - net maker 0.25 -> 0.60: +23/turn
  - brewery 1 0.63 -> 0.57: +10/turn
  - logging camp w/ tool [split timber 1] 0.00 -> 5.42: +6/turn
  - logging camp w/ tool 5.00 -> 0.00: +3/turn
  - flax farm 1 4.60 -> 5.40: +0/turn
  - spinnery 1 1.70 -> 1.53: -1/turn
  - weavery 1 0.23 -> 0.10: -7/turn
  - sewing shop 1 0.14 -> 0.04: +9/turn
- Model check over the last 18 turns: predicted +152/turn for the settings we ran, real +74/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.50, thread 3.75, cloth 6.00, flax fibres 4.40, garments 17.37, nets 27.74, beer 2.70, timber 5.25, prestige 53.02, cash 0.00
- Orders it would set: arms buy 1 (v2 None); candles buy 2 (v2 None); cloth sell 2 (v2 none); cured meat buy 1 (v2 2); furniture buy 1 (v2 None); grain buy 38 (v2 79); labour buy 73 (v2 66); light armour buy 1 (v2 None); pasties buy 3 (v2 4); thread sell 6 (v2 none)
- Recipe: logging camp w/ tool cut firewood 1 -> split timber 1 at 5.42, worth +6/turn.
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.64, worth +27/turn.
- Ship linen snake: Grandgues -> Rouhomme (+26/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Heidlowe (+1/turn over staying).
- Management: ~13.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +75/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
- Trim: donate quarry 1: +19/turn (tax 20 saved).
- Trim: donate weavery 1: +16/turn (tax 18 saved).
- Trim: donate logging camp w/ tool: +14/turn (tax 20 saved).
- Trim: donate sewing shop 1: +11/turn (tax 12 saved).

## Chain sizing

Mode HOLD, garments sold 2.6/turn (+0.0 exported); plan makes 0.0 garments a turn.
Labour: own 500, everything else 432, chain may buy 0 -> chain allowance 68, chain plan 109 (-131 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.60 | 2.47 |
| ret | 3 | 0.76 | 0.44 |
| spin | 4 | 1.70 | 0.91 |
| weave | 3 | 0.23 | 0.00 |
| sew | 2 | 0.14 | 0.00 |

Buffers: flax fibres 43/51, thread 621/151, cloth 37/0
- chain plan needed 109 labour, budget left 68: cut to 109

## Self-diagnosis

Nothing found this run.
