# v2 shadow report

Turn 13565, 2026-10-26 14:27. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 135, prestige 3,551 (431 free, -0.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 41 | 0 | 4 | 0 | 0 | min_holding 60, sell 53, sell @ 2.98 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 0 | 0 | 0 | 0 | 0 | stop 52, buy 13, buy @ 1 |
| firewood | 0 | 0 | 0 | 4 | 0 | buy @ 2.4 |
| fish | 0 | 0 | 0 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 2, sell @ 17.9 |
| grain | 47 | 0 | 0 | 0 | 0 | stop 81, buy 21, buy @ 3.7 |
| labour | 0 | 0 | 282 | 0 | 218 | buy @ 2.2 |
| meat | 0 | 0 | 0 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 0 | 0 | 0 | 6 | 0 | buy 7, buy @ 1.1 |

**6 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: sewing shop 1 ran short of cloth (no buy order); labour need rises ~14/turn when they restart -> v2: add a cloth buy
- **cured meat**: mansion 1 ran short of cured meat (buy is live (1 @ 29), home ask 21.20 x10, yet 0 bought last turn); labour need rises ~5/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: brewery 1 ran short of firewood (buy is live (no volume cap @ 2.4), home ask 1.53 x11, yet 0 bought last turn); labour need rises ~57/turn when they restart -> v2: find out why the buy isn't filling
- **porterage**: flax farm 1, retting pit 1 ran short of porterage (buy is live (7 @ 1.1), home ask 0.34 x52, yet 0 bought last turn); labour need rises ~97/turn when they restart -> v2: find out why the buy isn't filling
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 9.75 x11, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling
- **varnish**: net maker152202386007001 ran short of varnish (buy is live (1 @ 20.6), home ask 18.00 x3, yet 0 bought last turn); labour need rises ~5/turn when they restart -> v2: find out why the buy isn't filling

## Tuning

- **candles**: home ask 78.00 is above our ceiling 70.00 and last turn bought 0 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 282, not 382

## Prestige spending, cheapest coin per prestige first

836 turns left: prestige gained now converts 98.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 44.7 | 44.7 | running |
| hold banquet 3 (pies) | mansion | 8 | 45.6 | 45.6 | thin at home: hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 46.3 | 46.3 | thin at home: hop beer, wine, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 48.6 | 48.6 | thin at home: hop beer, cured fish |
| hold banquet 2 (pies) | mansion | 7 | 48.9 | 48.9 | thin at home: wine, pies |
| hold banquet 4 | mansion | 17.5 | 49.4 | 49.4 | thin at home: wine, hop beer, ham, stockfish |
| hold banquet 3 (meat) | mansion | 7.6 | 49.6 | 49.6 | thin at home: hop beer |
| hold banquet 2 (fish) | mansion | 6.8 | 51.4 | 51.4 | thin at home: wine, cured fish |
| hold banquet 4 (premium) | mansion | 20 | 51.6 | 51.6 | thin at home: hop beer, wine, stockfish, premium cheese |
| hold banquet 2 (meat) | mansion | 6.8 | 52.5 | 52.5 | thin at home: wine |
| hold banquet 1 (fish) | mansion | 4.2 | 53.0 | 53.0 |  |
| jousting 3 | arena | 230 | 54.5 | 54.6 | needs a arena (build cost 23,815); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only -2 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only 1 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~95 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Calange | 218 | 0.06 | 0.10 (10/turn) | flax fibres 18 (6.4->9.69), steel ingots 2 (17.85->23.75), thread 28 (4.02->4.46), raw cloth 2 (5.3->5.98) | spinning wheels 1 (214.2->224.2), candles 1 (71.4->78), arms 4 (31.92->33.63), furniture 1 (13.65->14.5) | +101 |
| Darmwald | 1022 | 0.32 | 0.50 (48/turn) | charcoal 11 (1.88->7.46), cured fish 5 (22.68->27.74), yarn 19 (3.99->5.08), lead bars 2 (11.87->13.01) | arms 4 (30.66->33.63), cloth 6 (7.19->8.55), casks 1 (3.8->4.84), flax fibres 4 (5.88->6.6) | +89 |
| Nürnnieder | 520 | 0.13 | 0.10 (10/turn) | thread 57 (4.02->5.13), lead bars 2 (11.87->12.82), garments 1 (21->22.42), raw cloth 2 (5.3->5.94) | candles 1 (70.88->78), tools 23 (5.04->5.46), arms 4 (32.13->33.63), yarn 14 (3->3.44) | +83 |
| Hofkirchen | 991 | 0.30 | 0.20 (19/turn) | yarn 19 (3.99->5.08), lead bars 7 (11.87->12.82), iron ore 1 (5.57->7.6), raw cloth 3 (5.3->5.61) | arms 4 (27.3->33.63), tools 23 (4.54->5.46), medicine 2 (120.75->127.3), flax fibres 10 (5.25->6.6) | +78 |
| Kirchwerp | 1072 | 0.34 | 0.20 (19/turn) | glassware 2 (49.77->61.27), yarn 12 (3.99->5.08), garments 1 (21->21.66), grain 3 (2.42->3.17) | tools 23 (4.54->5.46), candles 1 (67.2->78), arms 4 (31.29->33.63), flax fibres 10 (5.25->6.6) | +68 |

**Best:** Calange at about +101 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 45 @ min 2.94 | goal planner: sells 45 a turn at 2.94, keeps 60 (no one offered it) |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 8 = 5.3 turns |
| cured meat | 2 @ 29.0, stop 4 |  | uses 0.9/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| firewood | 3 @ 2.4, stop 12 |  | goal planner: buys 3 a turn for today's rates, keeps up to 12 (v2 had 8) |
| flax fibres |  | 3 @ min 4.76 | goal planner: sells 3 a turn at 4.76, keeps 82 (no one offered it) |
| furniture | 2 @ 14.8, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| grain | 23 @ 3.7, stop 91 |  | goal planner: buys 23 a turn for today's rates, keeps up to 91 (v2 had 0) |
| labour | 0 @ 2.2, stop - |  | goal planner: buys 0 for today's rates (v2 had 0) |
| light armour | 1 @ 98.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 36.6) |
| porterage | 7 @ 1.1, stop - |  | goal planner: buys 7 for today's rates (v2 had 6) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 a turn at 69.5, keeps 1 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| thread |  | 25 @ min 4.02 | goal planner: sells 25 a turn at 4.02, keeps 180 (no one offered it) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 195 |
| varnish | 1 @ 18.9, stop 1 | off | a building is stalled on varnish: no sell until it runs again |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 17.5k (cash + stock at home prices); -17/turn over 6 turns, -43/turn over 24 turns.
- Limits: cash flow >= +161/turn, prestige >= -0.55/turn (values are after 200 tax a turn).
- Today's settings: value +103/turn, cash -49/turn, prestige +8.15/turn - breaks the cash floor.
- Plan: value +291/turn, cash +9/turn, prestige -0.50/turn - could not meet the cash floor.
- Cash check (real vs predicted cash a tick, last 3): +71 vs -7, -5 vs -46, +1 vs -32.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Pontmont: +5/turn
  - ship Flax Wyrm -> Bordetes: +0/turn
  - mansion 1 0.15 -> 0.00: +23/turn
  - net maker 0.23 -> 0.00: +5/turn
  - park 1 16.00 -> 0.00: +0/turn
  - weavery 1 0.13 -> 1.98: +9/turn
  - spinnery 1 1.59 -> 3.48: +179/turn
  - brewery 1 0.44 -> 0.35: +10/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.29: -22/turn
  - ropewalk 1 0.25 -> 0.00: +23/turn
- Model check: not enough runs yet (needs 6 turns of goal history).
- Worth of one more unit per turn: labour 0.63, thread 2.90, cloth 3.85, flax fibres 5.76, garments 9.89, nets 16.92, beer 123.83, timber 2.83, prestige 0.00, cash 100.00
- Orders it would set: beer sell 45 (v2 none); firewood buy 3 (v2 8); fish buy 0 (v2 None); flax fibres sell 3 (v2 none); furniture buy 2 (v2 None); grain buy 23 (v2 0); light armour buy 1 (v2 None); meat buy 0 (v2 None); porterage buy 7 (v2 6); rope sell 2 (v2 none)
- Recipe: flax farm 1 grow flax 1 -> make flax fibres 1 at 11.00, worth +207/turn.
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.29, worth +34/turn.
- Ship linen snake: Grandgues -> Pontmont (+5/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Bordetes (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - new chandlery (make candles 1) for ~3984 coin: +30/turn, payback 131 turns, doesn't pay yet (materials thin at home: bricks, nails)
  - Tenants L13 for 500 prestige: +26/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot flax farm 1 for ~443 coin: +9/turn, payback 52 turns
- Trim: donate park 1: +96/turn (tax 96 saved).

## Chain sizing

Mode HOLD, garments sold 1.2/turn (+0.0 exported); plan makes 7.0 garments a turn.
Labour: own 500, everything else 390, chain may buy 0 -> chain allowance 110, chain plan 109 (-131 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.88 | 0.43 |
| ret | 3 | 1.04 | 0.08 |
| spin | 4 | 1.59 | 0.74 |
| weave | 3 | 0.13 | 0.27 |
| sew | 2 | 0.09 | 0.17 |

Buffers: flax fibres 489/46, thread 1060/134, cloth 0/27
- chain plan needed 393 labour, budget left 110: cut to 110 (sewing capped at 0.17)

## Self-diagnosis

- R1: arms slot dry: 0.0 held, 0.5 a turn (gear slot (+0.4 prestige)); our buy 1 @ 27, home ask 35.8; 5% of cash does not buy one at 36.4
- R1: cured meat slot dry: 0.0 held, 0.9 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 1 @ 29, home ask 21.2; our bid is already at/over the ask (sellers too thin)
- R1: donations slot dry: 0.0 held, 40.0 a turn (luxury slot (+1 prestige)); our buy none, home ask 1.0 (held back: failsafe level 3: reduce-only, would buy 6 @ 1.02 (ask 1.0, cap 1.5))
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy none, home ask 1.53 (held back: failsafe level 3: reduce-only, would buy 4 @ 1.56 (ask 1.53, cap 2.1))
- R1: fish slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask 1.68 (held back: failsafe level 3: reduce-only, would buy 3 @ 1.71 (ask 1.68, cap 2.6))
- R1: meat slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask 1.66 (held back: failsafe level 3: reduce-only, would buy 3 @ 1.69 (ask 1.66, cap 2.6))
- R1: pasties slot dry: 0.0 held, 2.8 a turn (basic food slot (+1.3 prestige)); our buy 2 @ 14.5, home ask 12.1; our bid is already at/over the ask (sellers too thin)
- R2: spinnery 1 blocked by thread space: 1060 held of 1084 capacity, we make 79.8 a turn; no buy on it: add a sell order or more capacity for thread
