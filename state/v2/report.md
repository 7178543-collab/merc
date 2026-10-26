# v2 shadow report

Turn 13555, 2026-10-26 04:35. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 603, prestige 3,561 (441 free, -1.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 7 | 0 | 0 | min_holding 60, sell 55, sell @ 2.98 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 6 | 0 | 6 | 1 | 0 | buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 2, sell @ 17.9 |
| grain | 56 | 21 | 22 | 0 | 0 | stop 81, buy 21, buy @ 3.7 |
| labour | 0 | 0 | 451 | 0 | 49 | buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 15 | 0 | 0 | 0 | 0 | min_holding 15, sell 10, sell @ 33.6 |
| porterage | 14 | 14 | 13 | 0 | 1 | buy 14, buy @ 1.1 |

**2 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: sewing shop 1 ran short of cloth (no buy order); labour need rises ~14/turn when they restart -> v2: add a cloth buy
- **firewood**: brewery 1 ran short of firewood (buy is live (no volume cap @ 2.4), home ask 1.77 x3, yet 0 bought last turn); labour need rises ~57/turn when they restart -> v2: find out why the buy isn't filling

## Tuning

- **flax plants**: flax plants buffer thin: 1.2 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 187

## Notes

- labour: projection runs 112 over real use lately; planning 466, not 579

## Prestige spending, cheapest coin per prestige first

846 turns left: prestige gained now converts 98.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 46.5 | 46.5 | running |
| hold banquet 3 (pies) | mansion | 8 | 46.6 | 46.6 | thin at home: hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 47.8 | 47.8 | thin at home: hop beer, wine, pies |
| hold banquet 2 (pies) | mansion | 7 | 49.1 | 49.1 | thin at home: wine, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 49.6 | 49.6 | thin at home: hop beer |
| hold banquet 3 (meat) | mansion | 7.6 | 51.1 | 51.1 | thin at home: hop beer, cured meat |
| hold banquet 4 | mansion | 17.5 | 51.3 | 51.3 | thin at home: wine, hop beer, stockfish |
| hold banquet 2 (fish) | mansion | 6.8 | 51.6 | 51.6 | thin at home: wine |
| jousting 3 | arena | 230 | 52.9 | 53.1 | needs a arena (build cost 23,128); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 53.3 | 53.3 | thin at home: wine, cured meat |
| hold banquet 1 (fish) | mansion | 4.2 | 53.8 | 53.8 |  |
| hold banquet 4 (premium) | mansion | 20 | 54.0 | 54.0 | thin at home: hop beer, wine, stockfish, premium cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only -4 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -1 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~96 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Neuborn | 780 | 0.20 | 0.50 (48/turn) | glass ingots 2 (61.43->85.97), furniture 12 (11.55->15.29), charcoal 12 (1.87->3.99), bricks 3 (4.24->9.5) | canvas 3 (32.76->34.01), flax fibres 13 (5.15->5.7), candles 1 (69.83->71.5), garments 2 (20.16->20.6) | +104 |
| Rouhomme | 368 | 0.09 | 0.80 (76/turn) | bread 145 (2.16->2.81), charcoal 12 (1.87->3.23), beer 40 (3.1->3.42), bricks 3 (4.24->6.65) | flax fibres 8 (4.94->5.7), chisels 1 (9.24->9.36) | +68 |
| Karlmoor | 787 | 0.20 | 0.20 (19/turn) | flax fibres 14 (5.3->8.5), thread 17 (4.4->5.03), nets 1 (37->41.23), lead ore 1 (9.55->10.64) | candles 1 (67.73->71.5), premium cheese 1 (26.46->28.5) | +48 |
| Dedlowe | 1146 | 0.38 | 0.10 (10/turn) | wine 9 (5.46->8.74), yarn 5 (4.03->5.42), tallow 1 (25.41->29.45), wrought iron 5 (14.18->15.01) | herbs 1 (33.39->38.38), candles 1 (67.73->71.5), pasties 2 (11.13->12.5) | +44 |
| Heilegg | 826 | 0.22 | 0.20 (19/turn) | malt 5 (5.41->9.36), furniture 12 (11.55->13.39), yarn 5 (4.03->5.08), hop beer 2 (6.62->7.6) | candles 1 (69.3->71.5) | +33 |

**Best:** Neuborn at about +104 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 29.8, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 3.0 turns |
| cured meat | 1 @ 29.0, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 2) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 0 @ 2.4, stop 13 |  | uses 6.3/turn (household upkeep), makes 6.5, holds 6 |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres |  | 2 @ min 4.82 | goal planner: sells 2 a turn at 4.82, keeps 82 (no one offered it) |
| grain | 29 @ 3.7, stop 115 |  | goal planner: buys 29 a turn for today's rates, keeps up to 115 (v2 had 58) |
| labour | 0 @ 2.2, stop - |  | goal planner: buys 0 for today's rates (v2 had 0) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 10 @ min 33.6 | goal planner: sells 10 at 33.6 (v2 had 10 at 36.0) |
| pasties | 4 @ 14.5, stop 8 |  | uses 2.0/turn (household upkeep), makes 0.0, holds 2 = 1.0 turns |
| porterage | 14 @ 1.1, stop - |  | goal planner: buys 14 for today's rates (v2 had 13) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 (v2 had 1) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 1 = 3.0 turns |
| thread |  | 21 @ min 4.26 | goal planner: sells 21 a turn at 4.26, keeps 180 (no one offered it) |
| tools | 3 @ 6.2, stop 18 |  | uses 2.2/turn (net maker152202386007001, retting pit 1), makes 0.0, holds 199 = 89.6 turns |
| varnish | 1 @ 20.4, stop 1 |  | uses 0.1/turn (net maker152202386007001), makes 0.0, holds 0 = 2.2 turns |
| wax | 1 @ 23.4, stop 1 |  | uses 0.1/turn (net maker152202386007001), makes 0.0, holds 0 = 8.2 turns |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 17.7k (cash + stock at home prices); -58/turn over 6 turns, -34/turn over 24 turns.
- Limits: cash flow >= +142/turn, prestige >= -0.59/turn (values are after 220 tax a turn).
- Today's settings: value +79/turn, cash +1/turn, prestige -1.90/turn - breaks the prestige floor and cash floor.
- Plan: value +53/turn, cash +76/turn, prestige -0.59/turn - could not meet the cash floor.
- Cash check (real vs predicted cash a tick, last 3): -252 vs +27, -200 vs +41, -193 vs +18 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Vauxvais: +5/turn
  - ship Flax Wyrm -> Rouhomme: +0/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.61: +7/turn
  - ropewalk 1 0.25 -> 0.00: +19/turn
  - spinnery 1 1.59 -> 1.91: +21/turn
  - net maker 0.23 -> 0.00: +11/turn
  - logging camp w/ tool 5.00 -> 4.91: +0/turn
  - mansion 1 0.15 -> 0.47: -67/turn
  - retting pit 1 1.04 -> 0.00: -106/turn
  - flax farm 1 5.88 -> 0.00: -27/turn
- Model check: not enough runs yet (needs 6 turns of goal history).
- Worth of one more unit per turn: labour 1.32, thread 3.61, cloth 5.60, flax fibres 4.77, garments 15.93, nets 16.65, beer 121.50, timber 2.94, prestige 3648.13, cash 100.00
- Orders it would set: cured meat buy 1 (v2 2); flax fibres sell 2 (v2 none); furniture buy 2 (v2 None); grain buy 29 (v2 58); light armour buy 1 (v2 None); porterage buy 14 (v2 13); rope sell 2 (v2 1); thread sell 21 (v2 none)
- Recipe: flax farm 1 grow flax 1 -> make flax fibres 1 at 7.60, worth +162/turn.
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.61, worth +64/turn.
- Ship linen snake: Grandgues -> Vauxvais (+5/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Rouhomme (+0/turn over staying).
- Management: ~12.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +53/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new chandlery (make candles 1) for ~4002 coin: +11/turn, payback 351 turns, doesn't pay yet (materials thin at home: bricks, nails)
- Trim: donate logging camp w/ tool: +16/turn (tax 20 saved).

## Chain sizing

Mode HOLD, garments sold 1.2/turn (+0.0 exported); plan makes 6.6 garments a turn.
Labour: own 500, everything else 394, chain may buy 0 -> chain allowance 106, chain plan 105 (-135 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.88 | 0.39 |
| ret | 3 | 1.04 | 0.07 |
| spin | 4 | 1.59 | 0.73 |
| weave | 3 | 0.13 | 0.26 |
| sew | 2 | 0.09 | 0.16 |

Buffers: flax fibres 312/45, thread 1046/133, cloth 0/26
- chain plan needed 393 labour, budget left 106: cut to 106 (sewing capped at 0.16)

## Self-diagnosis

- R2: spinnery 1 blocked by thread space: 1046 held of 1084 capacity, we make 79.8 a turn; no buy on it: add a sell order or more capacity for thread
