# v2 shadow report

Turn 13557, 2026-10-26 06:37. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 494, prestige 3,557 (437 free, -1.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 7 | 0 | 0 | min_holding 60, sell 55, sell @ 2.98 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 7 | 0 | 6 | 0 | 0 | buy @ 2.4; sell 1, sell @ 1.73 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 2, sell @ 17.9 |
| grain | 40 | 21 | 29 | 0 | 0 | stop 81, buy 21, buy @ 3.7 |
| labour | 0 | 0 | 468 | 0 | 32 | buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 10, sell @ 33.6 |
| porterage | 14 | 14 | 13 | 0 | 1 | buy 14, buy @ 1.1 |

**1 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: sewing shop 1 ran short of cloth (no buy order); labour need rises ~14/turn when they restart -> v2: add a cloth buy

## Tuning

- **flax plants**: flax plants buffer thin: 1.2 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 187

## Notes

- labour: projection runs 112 over real use lately; planning 468, not 568

## Prestige spending, cheapest coin per prestige first

844 turns left: prestige gained now converts 98.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 3 (pies) | mansion | 8 | 45.8 | 45.8 | thin at home: hop beer, pies |
| maintain 1 | park | 0.5 | 47.1 | 47.1 | running |
| hold banquet 4 (pies) | mansion | 18 | 47.7 | 47.7 | thin at home: hop beer, wine, pies |
| hold banquet 2 (pies) | mansion | 7 | 49.3 | 49.3 | thin at home: wine, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 49.6 | 49.6 | thin at home: hop beer |
| hold banquet 3 (meat) | mansion | 7.6 | 50.4 | 50.4 | thin at home: hop beer, cured meat |
| hold banquet 4 | mansion | 17.5 | 51.1 | 51.1 | thin at home: wine, hop beer, ham, stockfish |
| hold banquet 2 (fish) | mansion | 6.8 | 52.7 | 52.7 | thin at home: wine |
| jousting 3 | arena | 230 | 52.7 | 52.8 | needs a arena (build cost 23,633); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 53.6 | 53.6 | thin at home: wine, cured meat |
| hold banquet 4 (premium) | mansion | 20 | 53.7 | 53.7 | thin at home: hop beer, wine, stockfish, premium cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 54.7 | 54.7 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only -5 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -3 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~97 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Karlmoor | 787 | 0.20 | 0.20 (19/turn) | thread 16 (4.36->5.61), cloth 17 (7.61->8.6), flax fibres 3 (4.76->9.17), flax plants 7 (1.22->3.25) | furniture 1 (9.03->14.3), candles 1 (67.73->71) | +66 |
| Chatgnan | 728 | 0.19 | 0.30 (29/turn) | cured meat 4 (23.31->28.5), beer 54 (3.18->3.76), malt 5 (5.06->6.7), hop beer 1 (6.93->8.07) | harnesses 1 (42.42->62.22), furniture 1 (13.33->14.3) | +55 |
| Fontaux | 411 | 0.11 | 0.90 (87/turn) | cheese 12 (5.83->8.03), charcoal 11 (1.9->4.1), firewood 19 (1.82->5.22), scythes 1 (23.94->26.22) | candles 1 (65.62->71), harnesses 1 (57.75->62.22) | +53 |
| Bordetes | 831 | 0.22 | 0.10 (10/turn) | wrought iron 8 (14.18->16.15), tackles 1 (160.65->167.2), malt 6 (5.06->6.13), hop beer 1 (6.93->8.55) | looms 1 (522.9->541.5), candles 1 (67.73->71), chisels 1 (8.82->9.36), tools 2 (4.41->4.74) | +45 |
| Dedlowe | 1146 | 0.39 | 0.10 (10/turn) | wine 8 (6.25->9.17), rope 1 (71.5->84.08), wrought iron 4 (14.18->15.2), garments 1 (18.5->19.76) | herbs 1 (33.39->38.38), candles 1 (67.73->71), pasties 1 (11.13->12.4) | +43 |

**Best:** Karlmoor at about +66 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 31.2, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 0 = 1.0 turns |
| beer |  | 55 @ min 2.98 | goal planner: sells 55 at 2.98 (v2 had 55 at 3.38) |
| cured meat | 1 @ 29.0, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 2) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 0 @ 2.4, stop 13 | 1 @ min 1.74 | uses 6.3/turn (brewery 1, household upkeep), makes 6.5, holds 7 |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres |  | 2 @ min 4.76 | goal planner: sells 2 a turn at 4.76, keeps 82 (no one offered it) |
| grain | 29 @ 3.7, stop 115 |  | goal planner: buys 29 a turn for today's rates, keeps up to 115 (v2 had 58) |
| labour | 0 @ 2.2, stop - |  | goal planner: buys 0 for today's rates (v2 had 0) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 10 @ min 33.6 | goal planner: sells 10 at 33.6 (v2 had 10 at 36.0) |
| pasties | 2 @ 14.5, stop 4 |  | uses 1.0/turn (household upkeep), makes 0.0, holds 2 = 2.0 turns |
| porterage | 14 @ 1.1, stop - |  | goal planner: buys 14 for today's rates (v2 had 13) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 (v2 had 1) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 0 = 1.0 turns |
| thread |  | 22 @ min 4.26 | goal planner: sells 22 a turn at 4.26, keeps 180 (no one offered it) |
| tools | 3 @ 6.2, stop 18 |  | uses 2.2/turn (net maker152202386007001, retting pit 1), makes 0.0, holds 200 = 89.9 turns |
| varnish | 1 @ 21.0, stop 1 |  | uses 0.1/turn (net maker152202386007001), makes 0.0, holds 0 = 0.2 turns |
| wax | 1 @ 23.0, stop 1 |  | uses 0.1/turn (net maker152202386007001), makes 0.0, holds 0 = 6.2 turns |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 17.7k (cash + stock at home prices); -141/turn over 6 turns, -48/turn over 24 turns.
- Limits: cash flow >= +146/turn, prestige >= -0.57/turn (values are after 220 tax a turn).
- Today's settings: value +71/turn, cash -12/turn, prestige -1.91/turn - breaks the prestige floor and cash floor.
- Plan: value +41/turn, cash +30/turn, prestige -0.57/turn - could not meet the cash floor.
- Cash check (real vs predicted cash a tick, last 3): -193 vs +18, -101 vs +1, -7 vs -13 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Angefont: +9/turn
  - ship Flax Wyrm -> Hofkirchen: +0/turn
  - spinnery 1 1.59 -> 1.82: +3/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.51: +10/turn
  - ropewalk 1 0.25 -> 0.00: +27/turn
  - net maker 0.23 -> 0.00: +12/turn
  - logging camp w/ tool 5.00 -> 4.86: +0/turn
  - mansion 1 0.15 -> 0.47: -67/turn
  - retting pit 1 1.04 -> 0.00: -104/turn
  - flax farm 1 5.88 -> 0.00: -24/turn
- Model check: not enough runs yet (needs 6 turns of goal history).
- Worth of one more unit per turn: labour 1.25, thread 3.40, cloth 5.28, flax fibres 4.50, garments 15.03, nets 16.65, beer 121.43, timber 2.88, prestige 3647.24, cash 100.00
- Orders it would set: cured meat buy 1 (v2 2); flax fibres sell 2 (v2 none); furniture buy 2 (v2 None); grain buy 29 (v2 58); light armour buy 1 (v2 None); porterage buy 14 (v2 13); rope sell 2 (v2 1); thread sell 22 (v2 none)
- Recipe: flax farm 1 grow flax 1 -> make flax fibres 1 at 8.91, worth +148/turn.
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.51, worth +60/turn.
- Ship linen snake: Grandgues -> Angefont (+9/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Hofkirchen (+0/turn over staying).
- Management: ~12.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +43/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new chandlery (make candles 1) for ~3858 coin: +14/turn, payback 278 turns, doesn't pay yet (materials thin at home: bricks, nails)
  - +1 plot park 1 for ~1642 coin: +1/turn, payback 2773 turns, doesn't pay yet (materials thin at home: limestone)
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

Buffers: flax fibres 351/45, thread 1045/133, cloth 0/26
- chain plan needed 393 labour, budget left 106: cut to 106 (sewing capped at 0.16)

## Self-diagnosis

- R1: arms slot dry: 0.5 held, 0.5 a turn (gear slot (+0.4 prestige)); our buy 1 @ 27, home ask 29.8; 5% of cash does not buy one at 30.4
- R1: pasties slot dry: 2.0 held, 2.8 a turn (basic food slot (+1.3 prestige)); our buy 2 @ 14.5, home ask 12.4; our bid is already at/over the ask (sellers too thin)
- R2: spinnery 1 blocked by thread space: 1045 held of 1084 capacity, we make 79.8 a turn; no buy on it: add a sell order or more capacity for thread
