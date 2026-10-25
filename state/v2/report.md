# v2 shadow report

Turn 13546, 2026-10-25 19:51. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 2,464, prestige 3,578 (458 free, -0.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 53 | 0 | 7 | 0 | 0 | min_holding 60, sell 55, sell @ 2.98 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 6 | 0 | 2 | 4 | 0 | buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 2, sell @ 17.9 |
| grain | 107 | 28 | 0 | 0 | 0 | stop 107, buy 27, buy @ 3.7 |
| labour | 0 | 0 | 469 | 0 | 31 | buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 13, sell @ 33.6 |
| porterage | 14 | 14 | 13 | 0 | 1 | buy 14, buy @ 1.1 |

**4 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: sewing shop 1 ran short of cloth (no buy order); labour need rises ~14/turn when they restart -> v2: add a cloth buy
- **firewood**: brewery 1 ran short of firewood (buy is live (no volume cap @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~57/turn when they restart -> v2: find out why the buy isn't filling
- **rope**: needed (0.2/turn) but there is NO buy order, stock 0.3 -> v2: add buy 1
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 9.30 x7, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Tuning

- **flax plants**: flax plants buffer thin: 1.3 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 201

## Notes

- labour: projection runs 122 over real use lately; planning 516, not 638
- labour expiry guard: 31 bought labour expired last turn, buy 0 (not 16) this turn

## Prestige spending, cheapest coin per prestige first

855 turns left: prestige gained now converts 98.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 46.2 | 46.2 | running |
| hold banquet 3 (pies) | mansion | 8 | 47.5 | 47.5 | thin at home: hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 48.3 | 48.3 | thin at home: hop beer, wine, ham, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 49.8 | 49.8 | thin at home: hop beer |
| hold banquet 2 (pies) | mansion | 7 | 50.4 | 50.4 | thin at home: wine, pies |
| hold banquet 3 (meat) | mansion | 7.6 | 50.8 | 50.8 | thin at home: hop beer |
| hold banquet 2 (fish) | mansion | 6.8 | 51.7 | 51.7 | thin at home: wine |
| hold banquet 4 | mansion | 17.5 | 51.7 | 51.7 | thin at home: wine, hop beer, ham, stockfish |
| hold banquet 2 (meat) | mansion | 6.8 | 52.8 | 52.8 | thin at home: wine |
| jousting 3 | arena | 230 | 52.8 | 52.9 | needs a arena (build cost 24,290); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold sermon 2 (candles) | church | 31 | 50.6 | 53.2 | needs a church (build cost 61,800); thin at home: candles |
| hold banquet 1 (fish) | mansion | 4.2 | 53.6 | 53.6 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only -8 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -7 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~95 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Darmwald | 1022 | 0.32 | 0.30 (29/turn) | raw cloth 39 (7.25->10.54), looms 1 (520.8->546.25), garments 1 (19.8->25.08), nets 2 (34.6->36.67) | pasties 2 (12.81->14.3) | +141 |
| Angefont | 686 | 0.17 | 0.20 (19/turn) | looms 1 (520.8->617.5), limestone 2 (18.17->28.5), tackles 1 (162.75->165.3), seeds 2 (2.75->3.31) | flax fibres 18 (4.62->5.3), premium cheese 1 (28.56->31.35), cloth 6 (6.93->7.35), nails 2 (5.35->5.98) | +115 |
| Rotterburg | 1056 | 0.33 | 0.10 (10/turn) | looms 1 (520.8->608) | pasties 2 (13.02->14.3), yarn 1 (2.33->3.53) | +82 |
| Orlesailles | 1178 | 0.40 | 0.30 (29/turn) | looms 1 (520.8->570), furniture 12 (11.55->14.91), nets 2 (34.6->36.29) | gears 2 (56.7->58.42), pasties 2 (12.6->14.3) | +71 |
| Disscester | 1474 | 0.55 | 0.10 (10/turn) | spinning wheels 1 (254.1->319.2), looms 1 (520.8->532) | gears 1 (57.23->58.42) | +68 |

**Best:** Darmwald at about +141 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer | 7 @ 3.66, stop 27 |  | uses 6.5/turn (household upkeep, mansion 1), makes 0.0, holds 53 = 8.2 turns |
| cured meat | 1 @ 29.0, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 2) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 0 @ 2.4, stop 12 |  | uses 5.8/turn (household upkeep), makes 6.5, holds 6 |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| grain | 21 @ 3.7, stop 81 |  | uses 20.1/turn (observed), makes 0.0, holds 107 = 5.3 turns |
| labour | 0 @ 2.2, stop - |  | goal planner: buys 0 for today's rates (v2 had 0) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 11 @ min 33.6 | goal planner: sells 11 at 33.6 (v2 had 11 at 34.0) |
| pasties | 6 @ 14.5, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 3 = 1.1 turns |
| porterage | 14 @ 1.1, stop - |  | goal planner: buys 14 for today's rates (v2 had 7) |
| rope | 1 @ 83.0, stop 1 |  | uses 0.2/turn (net maker152202386007001), makes 0.0, holds 0 = 1.1 turns |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 1 = 4.0 turns |
| thread |  | 17 @ min 4.5 | goal planner: sells 17 a turn at 4.5, keeps 192 (no one offered it) |
| tools | 3 @ 6.2, stop 21 |  | uses 2.5/turn (net maker152202386007001, retting pit 1), makes 0.0, holds 200 = 79.2 turns |
| varnish | 1 @ 18.4, stop 1 |  | uses 0.1/turn (net maker152202386007001), makes 0.0, holds 1 = 5.8 turns |
| wax | 1 @ 21.0, stop 1 |  | uses 0.1/turn (net maker152202386007001), makes 0.0, holds 0 = 0.4 turns |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 18.2k (cash + stock at home prices); -44/turn over 6 turns, +16/turn over 24 turns.
- Limits: cash flow >= +64/turn, prestige >= -0.66/turn (values are after 220 tax a turn).
- Today's settings: value +115/turn, cash +67/turn, prestige -0.77/turn - breaks the prestige floor.
- Plan: value +200/turn, cash +214/turn, prestige -0.66/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -44 vs +43, -198 vs +55, -337 vs +55 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4, rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Cobholme: +5/turn
  - ship Flax Wyrm -> Vauxvais: +2/turn
  - ropewalk 1 0.25 -> 0.69: +24/turn
  - net maker 0.48 -> 0.00: +31/turn
  - spinnery 1 1.59 -> 2.10: +9/turn
  - retting pit 1 1.12 -> 1.03: +2/turn
  - flax farm 1 6.29 -> 5.86: +4/turn
  - weavery 1 0.13 -> 0.30: +2/turn
  - sewing shop 1 0.09 -> 0.17: +17/turn
  - logging camp w/ tool 5.00 -> 4.39: +0/turn
- Model check over the last 52 turns: predicted +102/turn for the settings we ran, real +38/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.54, thread 3.79, cloth 6.10, flax fibres 4.36, garments 17.73, nets 27.02, beer 2.80, timber 2.97, prestige 53.10, cash 0.00
- Orders it would set: arms buy 1 (v2 None); candles buy 2 (v2 None); cured meat buy 1 (v2 2); furniture buy 2 (v2 None); grain buy 27 (v2 21); light armour buy 1 (v2 None); porterage buy 14 (v2 7); thread sell 17 (v2 none)
- Ship linen snake: Grandgues -> Cobholme (+4/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Vauxvais (+2/turn over staying).
- Management: ~12.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +77/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
- Trim: donate logging camp w/ tool: +17/turn (tax 20 saved).

## Chain sizing

Mode HOLD, garments sold 1.3/turn (+0.0 exported); plan makes 32.0 garments a turn.
Labour: own 500, everything else 400, chain may buy 350 -> chain allowance 450, chain plan 419 (+172 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 6.29 | 4.21 |
| ret | 3 | 1.12 | 0.75 |
| spin | 4 | 1.59 | 1.80 |
| weave | 3 | 0.13 | 1.25 |
| sew | 2 | 0.09 | 0.78 |

Buffers: flax fibres 134/82, thread 975/240, cloth 0/125

## Self-diagnosis

Nothing found this run.
