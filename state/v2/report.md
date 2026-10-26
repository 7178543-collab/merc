# v2 shadow report

Turn 13564, 2026-10-26 13:25. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 134, prestige 3,556 (436 free, -0.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 45 | 0 | 4 | 0 | 0 | min_holding 60, sell 53, sell @ 2.98 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 0 | 13 | 13 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 4 | 0 | buy @ 2.4 |
| fish | 0 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 2, sell @ 17.9 |
| grain | 47 | 3 | 0 | 0 | 0 | stop 81, buy 21, buy @ 3.7 |
| labour | 0 | 0 | 378 | 0 | 122 | buy @ 2.2 |
| meat | 0 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 0 | 7 | 6 | 0 | 1 | buy 7, buy @ 1.1 |

**5 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: sewing shop 1 ran short of cloth (no buy order); labour need rises ~14/turn when they restart -> v2: add a cloth buy
- **cured meat**: mansion 1 ran short of cured meat (buy is live (1 @ 29), home ask 21.60 x7, yet 0 bought last turn); labour need rises ~5/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: brewery 1 ran short of firewood (buy is live (no volume cap @ 2.4), home ask 1.53 x15, yet 0 bought last turn); labour need rises ~57/turn when they restart -> v2: find out why the buy isn't filling
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 9.65 x9, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling
- **varnish**: net maker152202386007001 ran short of varnish (buy is live (1 @ 20.6), home ask 19.70 x1, yet 0 bought last turn); labour need rises ~5/turn when they restart -> v2: find out why the buy isn't filling

## Tuning

- **candles**: home ask 79.50 is above our ceiling 70.00 and last turn bought 0 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **flax plants**: flax plants buffer thin: 1.2 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 187

## Notes

- labour: projection runs 106 over real use lately; planning 378, not 382

## Prestige spending, cheapest coin per prestige first

837 turns left: prestige gained now converts 98.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 44.7 | 44.7 | running |
| hold banquet 3 (pies) | mansion | 8 | 45.6 | 45.6 | thin at home: hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 46.4 | 46.4 | thin at home: hop beer, wine, pies |
| hold banquet 2 (pies) | mansion | 7 | 48.6 | 48.6 | thin at home: wine, pies |
| hold banquet 4 | mansion | 17.5 | 49.5 | 49.5 | thin at home: wine, hop beer, ham, stockfish |
| hold banquet 3 (fish) | mansion | 7.6 | 49.7 | 49.7 | thin at home: hop beer |
| hold banquet 3 (meat) | mansion | 7.6 | 49.7 | 49.7 | thin at home: hop beer |
| hold banquet 2 (fish) | mansion | 6.8 | 52.3 | 52.3 | thin at home: wine |
| hold banquet 2 (meat) | mansion | 6.8 | 52.4 | 52.4 | thin at home: wine |
| hold banquet 4 (premium) | mansion | 20 | 52.4 | 52.4 | thin at home: hop beer, wine, stockfish, premium cheese |
| hold feast 2 | townhouse | 2.6 | 51.1 | 54.1 | needs a townhouse (build cost 6,334); thin at home: wine |
| hold banquet 1 (fish) | mansion | 4.2 | 54.6 | 54.6 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only -9 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -0 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~96 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Nürnnieder | 520 | 0.13 | 0.20 (19/turn) | thread 68 (4.02->5.13), flax fibres 4 (5.05->11.21), garments 1 (19.8->21.85), scythes 1 (23.73->24.32) | candles 1 (70.35->79.5), malt 1 (6.62->8.55) | +95 |
| Calange | 218 | 0.06 | 0.10 (10/turn) | flax fibres 15 (5.05->7.41), thread 50 (4.02->4.39), steel ingots 3 (17.75->22.61), tools 8 (5.3->5.7) | candles 1 (72.45->79.5), malt 2 (6.88->8.55), arms 5 (31.29->31.73), premium cheese 1 (27.3->27.55) | +77 |
| Darmwald | 1022 | 0.32 | 0.40 (38/turn) | charcoal 11 (1.9->7.74), cured fish 5 (25.2->26.6), yarn 3 (3.68->5.08), bellows 1 (281.4->285) | cloth 6 (7.19->8.6), candles 1 (74.55->79.5), garments 2 (19.43->20.8), malt 2 (7.09->8.55) | +61 |
| Grandgues | 152 | 0.04 | 0.50 (48/turn) | firewood 28 (1.61->3.29), charcoal 11 (1.9->2.72), limestone 2 (15.33->19), lead ore 2 (7.72->8.55) | arms 5 (27.3->31.73), candles 1 (73.5->79.5), malt 3 (7.04->8.55), premium cheese 1 (26.88->27.55) | +53 |
| Chribruck | 1202 | 0.41 | 0.20 (19/turn) | thread 5 (4.02->4.8), yarn 3 (3.68->4.64), lead ore 1 (7.72->10.16) | malt 16 (5.02->8.55), candles 1 (74.03->79.5) | +52 |

**Best:** Nürnnieder at about +95 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 53 @ min 2.98 | goal planner: sells 53 a turn at 2.98, keeps 60 (no one offered it) |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 10 = 6.3 turns |
| cured meat | 2 @ 29.0, stop 4 |  | uses 0.9/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| donations | 13 @ 1.0, stop 52 |  | goal planner: buys 13 a turn for today's rates, keeps up to 52 (v2 had 20) |
| firewood | 4 @ 2.4, stop 14 |  | goal planner: buys 4 a turn for today's rates, keeps up to 14 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres |  | 2 @ min 4.76 | goal planner: sells 2 a turn at 4.76, keeps 82 (no one offered it) |
| furniture | 2 @ 14.4, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| grain | 27 @ 3.7, stop 107 |  | goal planner: buys 27 a turn for today's rates, keeps up to 107 (v2 had 0) |
| labour | 0 @ 2.2, stop - |  | goal planner: buys 0 for today's rates (v2 had 0) |
| light armour | 1 @ 100, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 36.6) |
| porterage | 7 @ 1.1, stop - |  | goal planner: buys 7 for today's rates (v2 had 6) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 a turn at 69.5, keeps 1 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| thread |  | 24 @ min 4.02 | goal planner: sells 24 a turn at 4.02, keeps 180 (no one offered it) |
| tools | 3 @ 6.2, stop 17 |  | uses 2.1/turn (retting pit 1), makes 0.0, holds 195 = 93.6 turns |
| varnish | 1 @ 20.6, stop 1 | off | a building is stalled on varnish: no sell until it runs again |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 17.5k (cash + stock at home prices); -33/turn over 6 turns, -49/turn over 24 turns.
- Limits: cash flow >= +161/turn, prestige >= -0.57/turn (values are after 200 tax a turn).
- Today's settings: value +92/turn, cash -32/turn, prestige +8.15/turn - breaks the cash floor.
- Plan: value +305/turn, cash +30/turn, prestige -0.50/turn - could not meet the cash floor.
- Cash check (real vs predicted cash a tick, last 3): -67 vs -0, +71 vs -7, -5 vs -46.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Brunnham: +9/turn
  - ship Flax Wyrm -> Angefont: +0/turn
  - mansion 1 0.15 -> 0.00: +24/turn
  - net maker 0.23 -> 0.00: +5/turn
  - park 1 16.00 -> 0.00: +0/turn
  - weavery 1 0.13 -> 1.90: +10/turn
  - spinnery 1 1.59 -> 3.43: +198/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.34: -17/turn
  - ropewalk 1 0.25 -> 0.00: +25/turn
  - retting pit 1 1.04 -> 0.00: -229/turn
- Model check: not enough runs yet (needs 6 turns of goal history).
- Worth of one more unit per turn: labour 0.70, thread 2.82, cloth 3.87, flax fibres 5.22, garments 10.19, nets 16.92, beer 123.90, timber 2.83, prestige 0.00, cash 100.00
- Orders it would set: beer sell 53 (v2 none); donations buy 13 (v2 20); firewood buy 4 (v2 8); flax fibres sell 2 (v2 none); furniture buy 2 (v2 None); grain buy 27 (v2 0); light armour buy 1 (v2 None); porterage buy 7 (v2 6); rope sell 2 (v2 none); thread sell 24 (v2 none)
- Recipe: flax farm 1 grow flax 1 -> make flax fibres 1 at 11.00, worth +204/turn.
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.34, worth +41/turn.
- Ship linen snake: Grandgues -> Brunnham (+9/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Angefont (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - new chandlery (make candles 1) for ~3883 coin: +34/turn, payback 114 turns, doesn't pay yet (materials thin at home: bricks, nails)
  - Tenants L13 for 500 prestige: +28/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot flax farm 1 for ~431 coin: +7/turn, payback 65 turns
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

Buffers: flax fibres 501/46, thread 1060/134, cloth 0/27
- chain plan needed 393 labour, budget left 110: cut to 110 (sewing capped at 0.17)

## Self-diagnosis

- R1: arms slot dry: 0.0 held, 0.5 a turn (gear slot (+0.4 prestige)); our buy 1 @ 27, home ask 35.6; 5% of cash does not buy one at 36.2
- R1: cured meat slot dry: 0.0 held, 0.9 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 1 @ 29, home ask 21.6; our bid is already at/over the ask (sellers too thin)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy none, home ask 1.53 (held back: failsafe level 3: reduce-only, would buy 4 @ 1.56 (ask 1.53, cap 2.1))
- R1: pasties slot dry: 0.0 held, 2.8 a turn (basic food slot (+1.3 prestige)); our buy 2 @ 14.5, home ask 12.1; our bid is already at/over the ask (sellers too thin)
- R2: spinnery 1 blocked by thread space: 1060 held of 1084 capacity, we make 79.8 a turn; no buy on it: add a sell order or more capacity for thread
