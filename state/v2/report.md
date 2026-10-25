# v2 shadow report

Turn 13545, 2026-10-25 18:30. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 2,801, prestige 3,579 (459 free, -1.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 55, sell @ 2.98 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 2 | 0 | 5 | 0 | 0 | buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 2, sell @ 17.9 |
| grain | 101 | 27 | 20 | 0 | 0 | stop 111, buy 28, buy @ 3.7 |
| labour | 0 | 0 | 500 | 27 | 0 | buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 15 | 0 | 0 | 0 | 0 | min_holding 15, sell 10, sell @ 33.6 |
| porterage | 14 | 14 | 7 | 0 | 7 | buy 14, buy @ 1.1 |

**1 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: sewing shop 1 ran short of cloth (no buy order); labour need rises ~14/turn when they restart -> v2: add a cloth buy

## Tuning

- **firewood**: we make 0/turn more than we use but there is no sell order -> v2: sell 0
- **flax plants**: flax plants buffer thin: 1.3 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 201

## Notes

- labour: projection runs 122 over real use lately; planning 527, not 606

## Prestige spending, cheapest coin per prestige first

856 turns left: prestige gained now converts 98.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 46.2 | 46.2 | running |
| hold banquet 3 (pies) | mansion | 8 | 47.6 | 47.6 | thin at home: hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 48.1 | 48.1 | thin at home: hop beer, wine, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 49.8 | 49.8 | thin at home: hop beer |
| hold banquet 2 (pies) | mansion | 7 | 50.6 | 50.6 | thin at home: wine, pies |
| hold banquet 3 (meat) | mansion | 7.6 | 50.9 | 50.9 | thin at home: hop beer |
| hold banquet 4 | mansion | 17.5 | 51.4 | 51.4 | thin at home: wine, hop beer, ham, stockfish |
| hold banquet 2 (fish) | mansion | 6.8 | 51.9 | 51.9 | thin at home: wine |
| hold banquet 4 (premium) | mansion | 20 | 52.2 | 52.2 | thin at home: hop beer, wine, stockfish, premium cheese |
| hold banquet 2 (meat) | mansion | 6.8 | 53.1 | 53.1 | thin at home: wine |
| jousting 3 | arena | 230 | 53.0 | 53.1 | needs a arena (build cost 24,018); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold sermon 2 (candles) | church | 31 | 50.7 | 53.3 | needs a church (build cost 61,360); thin at home: candles |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only -8 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~96 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Darmwald | 1022 | 0.32 | 0.40 (38/turn) | raw cloth 38 (7.25->10.16), furniture 12 (11.55->14.06), garments 1 (18.2->23.94), nets 3 (34->35.72) | - | +113 |
| Brunnham | 1281 | 0.45 | 0.10 (10/turn) | garments 1 (18.2->22.61), nets 3 (34->35.53), hides 1 (14.7->15.86), yarn 4 (4.14->4.69) | gold bars 1 (871.5->916.75), tin ingots 1 (26.25->36.48), lathes 1 (178.5->190), gears 1 (56.18->58.9) | +72 |
| Chribruck | 1202 | 0.41 | 0.10 (10/turn) | tools 13 (4.34->5.22), canvas 1 (36.54->38), garments 1 (18.2->18.71), iron ore 1 (5.23->7.6) | gold bars 1 (871.5->916.75) | +52 |
| Neuborn | 780 | 0.20 | 0.50 (48/turn) | furniture 12 (11.55->14.82), charcoal 11 (1.94->4.12), beer 39 (3.14->3.65), tools 16 (4.34->4.64) | pasties 2 (12.71->14.3), thread 7 (4.2->4.64), flax fibres 6 (4.91->5.45) | +47 |
| Hofkirchen | 991 | 0.30 | 0.20 (19/turn) | flax plants 11 (1.21->3.89), glass ingots 2 (59.33->68.4), tackles 1 (162.75->167.2), canvas 1 (36.54->38) | pasties 2 (13.02->14.3), cheese 12 (5.15->5.46), garments 2 (19.53->19.9) | +45 |

**Best:** Darmwald at about +113 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 27.4, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 3.0 turns |
| beer |  | 55 @ min 2.98 | goal planner: sells 55 at 2.98 (v2 had 55 at 3.38) |
| cured meat | 1 @ 29.0, stop 4 |  | uses 0.9/turn (mansion 1), makes 0.0, holds 4 = 4.3 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 0 @ 2.4, stop 13 | 0 @ min 1.75 | uses 6.3/turn (brewery 1, household upkeep), makes 6.5, holds 2 |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres |  | 4 @ min 5.35 | goal planner: trial sale of an idle pile, 4 a turn at 5.35, keeps 82 (41 over) |
| grain | 27 @ 3.7, stop 107 |  | goal planner: buys 27 a turn for today's rates, keeps up to 107 (v2 had 36) |
| labour | 4 @ 2.2, stop - |  | goal planner: buys 4 for today's rates (v2 had 27) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 13 @ min 33.6 | goal planner: sells 13 at 33.6 (v2 had 13 at 34.0) |
| pasties | 2 @ 14.5, stop 8 |  | goal planner: buys 2 a turn for today's rates, keeps up to 8 (v2 had 6) |
| porterage | 14 @ 1.1, stop - |  | goal planner: buys 14 for today's rates (v2 had 13) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 73.5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 0 = 0.6 turns |
| thread |  | 16 @ min 4.5 | goal planner: sells 16 a turn at 4.5, keeps 205 (no one offered it) |
| tools | 3 @ 6.2, stop 22 |  | uses 2.7/turn (net maker152202386007001, retting pit 1), makes 0.0, holds 199 = 74.6 turns |
| varnish | 1 @ 18.4, stop 1 |  | uses 0.2/turn (net maker152202386007001), makes 0.0, holds 1 = 4.5 turns |
| wax | 1 @ 21.0, stop 1 |  | uses 0.2/turn (net maker152202386007001), makes 0.0, holds 0 = 0.9 turns |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 18.5k (cash + stock at home prices); -58/turn over 6 turns, +11/turn over 24 turns.
- Limits: cash flow >= +50/turn, prestige >= -0.66/turn (values are after 220 tax a turn).
- Today's settings: value +105/turn, cash +55/turn, prestige -0.65/turn.
- Plan: value +209/turn, cash +223/turn, prestige -0.66/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -243 vs -48, -44 vs +43, -198 vs +55 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4, rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Vauxvais: +7/turn
  - ship Flax Wyrm -> Heilegg: +2/turn
  - ropewalk 1 0.25 -> 0.77: +21/turn
  - net maker 0.73 -> 0.11: +45/turn
  - spinnery 1 1.59 -> 2.24: +12/turn
  - logging camp w/ tool 5.00 -> 4.80: +0/turn
  - weavery 1 0.13 -> 0.33: +0/turn
  - sewing shop 1 0.09 -> 0.18: +21/turn
  - flax farm 1 6.29 -> 6.19: -0/turn
- Model check over the last 50 turns: predicted +100/turn for the settings we ran, real +45/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.54, thread 3.79, cloth 6.10, flax fibres 4.36, garments 17.73, nets 27.11, beer 2.78, timber 2.83, prestige 53.32, cash 0.00
- Orders it would set: candles buy 2 (v2 None); flax fibres sell 4 (v2 none); furniture buy 2 (v2 None); grain buy 27 (v2 36); labour buy 4 (v2 27); light armour buy 1 (v2 None); pasties buy 2 (v2 6); porterage buy 14 (v2 13); thread sell 16 (v2 none)
- Ship linen snake: Grandgues -> Vauxvais (+7/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Heilegg (+1/turn over staying).
- Management: ~12.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +77/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
- Trim: donate logging camp w/ tool: +17/turn (tax 20 saved).

## Chain sizing

Mode HOLD, garments sold 1.8/turn (+0.0 exported); plan makes 32.0 garments a turn.
Labour: own 500, everything else 406, chain may buy 350 -> chain allowance 444, chain plan 432 (+185 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 6.29 | 4.63 |
| ret | 3 | 1.12 | 0.82 |
| spin | 4 | 1.59 | 1.88 |
| weave | 3 | 0.13 | 1.25 |
| sew | 2 | 0.09 | 0.78 |

Buffers: flax fibres 122/84, thread 934/248, cloth 0/125

## Self-diagnosis

- R1: firewood slot dry: 2.2 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy none, home ask 1.84 (held back: failsafe level 2: reduce-only, would buy 6 @ 1.87 (ask 1.84, cap 2.1))
