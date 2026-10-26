# v2 shadow report

Turn 13563, 2026-10-26 12:04. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 140, prestige 3,561 (441 free, -3.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 49 | 0 | 5 | 0 | 0 | min_holding 60, sell 55, sell @ 2.98 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 13 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 4 | 0 | buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 2, sell @ 17.9 |
| grain | 47 | 21 | 0 | 0 | 0 | stop 81, buy 21, buy @ 3.7 |
| labour | 0 | 0 | 399 | 0 | 101 | buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 7 | 7 | 6 | 0 | 1 | buy 7, buy @ 1.1 |

**5 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: sewing shop 1 ran short of cloth (no buy order); labour need rises ~14/turn when they restart -> v2: add a cloth buy
- **cured meat**: mansion 1 ran short of cured meat (buy is live (1 @ 29), home ask 22.00 x2, yet 0 bought last turn); labour need rises ~5/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: brewery 1 ran short of firewood (buy is live (no volume cap @ 2.4), home ask 1.54 x15, yet 0 bought last turn); labour need rises ~57/turn when they restart -> v2: find out why the buy isn't filling
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 9.60 x9, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling
- **varnish**: net maker152202386007001 ran short of varnish (buy is live (1 @ 20.6), home ask 19.70 x1, yet 0 bought last turn); labour need rises ~5/turn when they restart -> v2: find out why the buy isn't filling

## Tuning

- **candles**: home ask 75.50 is above our ceiling 70.00 and last turn bought 0 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **flax plants**: flax plants buffer thin: 1.2 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 187

## Notes

- labour: projection runs 106 over real use lately; planning 399, not 478

## Prestige spending, cheapest coin per prestige first

838 turns left: prestige gained now converts 98.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 45.0 | 45.0 | running |
| hold banquet 3 (pies) | mansion | 8 | 45.5 | 45.5 | thin at home: hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 46.3 | 46.3 | thin at home: hop beer, pies |
| hold banquet 2 (pies) | mansion | 7 | 48.7 | 48.7 | thin at home: pies |
| hold banquet 4 | mansion | 17.5 | 49.4 | 49.4 | thin at home: hop beer, ham, stockfish |
| hold banquet 3 (fish) | mansion | 7.6 | 49.5 | 49.5 | thin at home: hop beer |
| hold banquet 3 (meat) | mansion | 7.6 | 50.0 | 50.0 | thin at home: hop beer, cured meat |
| hold banquet 2 (fish) | mansion | 6.8 | 52.3 | 52.3 |  |
| hold banquet 4 (premium) | mansion | 20 | 52.4 | 52.4 | thin at home: hop beer, stockfish, premium cheese |
| hold banquet 2 (meat) | mansion | 6.8 | 52.8 | 52.8 | thin at home: cured meat |
| jousting 3 | arena | 230 | 54.0 | 54.2 | needs a arena (build cost 24,430); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold feast 2 | townhouse | 2.6 | 51.5 | 54.3 | needs a townhouse (build cost 5,892) |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only -4 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -5 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~97 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Nürnnieder | 520 | 0.13 | 0.20 (19/turn) | flax fibres 22 (5.8->9.97), thread 57 (4.04->5.13), bricks 2 (3.15->6.17) | candles 1 (66.15->72), cloth 3 (8.29->8.55), flax plants 2 (1.54->1.99) | +147 |
| Fontaux | 411 | 0.11 | 0.30 (29/turn) | cheese 11 (5.88->9.79), casks 9 (5.3->9.5), thread 69 (4.04->4.48), charcoal 11 (1.94->4.48) | cloth 4 (8.14->8.55), flax plants 2 (1.46->1.99) | +125 |
| Darmwald | 1022 | 0.32 | 0.40 (39/turn) | charcoal 11 (1.94->7.17), thread 24 (4.04->4.89), scythes 1 (23.94->24.7) | cloth 6 (7.14->8.55), garments 2 (19.43->22.2), casks 1 (3.65->4.73) | +54 |
| Rouhomme | 368 | 0.10 | 1.00 (97/turn) | bread 96 (2.12->2.53), firewood 20 (1.63->4.71), charcoal 7 (1.94->3.27), iron ore 1 (5.35->8.46) | spinning wheels 1 (224.7->233.7), flax fibres 5 (4.94->6.05), cloth 4 (7.56->8.55), arms 2 (30.66->31.73) | +50 |
| Coburgbaum | 619 | 0.16 | 0.30 (29/turn) | tackles 1 (182.7->212.8), dyed cloth 2 (11.45->16.25), charcoal 11 (1.94->3.7), bricks 2 (3.15->6.79) | candles 1 (67.73->72), medicine 1 (126->127.3), flax plants 2 (1.56->1.99), salt 5 (3.59->3.78) | +46 |

**Best:** Nürnnieder at about +147 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 53 @ min 2.98 | goal planner: sells 53 a turn at 2.98, keeps 60 (no one offered it) |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 11 = 7.3 turns |
| cured meat | 1 @ 29.0, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 2) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 54) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres |  | 2 @ min 4.76 | goal planner: sells 2 a turn at 4.76, keeps 82 (no one offered it) |
| furniture | 2 @ 13.6, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| grain | 29 @ 3.7, stop 115 |  | goal planner: buys 29 a turn for today's rates, keeps up to 115 (v2 had 0) |
| labour | 0 @ 2.2, stop - |  | goal planner: buys 0 for today's rates (v2 had 0) |
| light armour | 1 @ 102, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 36.6) |
| porterage | 7 @ 1.1, stop - |  | goal planner: buys 7 for today's rates (v2 had 6) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| thread |  | 24 @ min 4.08 | goal planner: sells 24 a turn at 4.08, keeps 180 (no one offered it) |
| tools | 3 @ 6.2, stop 17 |  | uses 2.1/turn (retting pit 1), makes 0.0, holds 197 = 94.6 turns |
| varnish | 1 @ 20.6, stop 1 | off | a building is stalled on varnish: no sell until it runs again |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 18.2k (cash + stock at home prices); +85/turn over 6 turns, -27/turn over 24 turns.
- Limits: cash flow >= +161/turn, prestige >= -0.59/turn (values are after 200 tax a turn).
- Today's settings: value +74/turn, cash -46/turn, prestige -2.57/turn - breaks the prestige floor and cash floor.
- Plan: value +0/turn, cash -78/turn, prestige -0.59/turn - could not meet the cash floor.
- Cash check (real vs predicted cash a tick, last 3): -7 vs -13, -67 vs -0, +71 vs -7.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Brunnham: +4/turn
  - ship Flax Wyrm -> Bordetes: +0/turn
  - net maker 0.23 -> 0.00: +4/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.34: -10/turn
  - ropewalk 1 0.25 -> 0.00: +15/turn
  - mansion 1 0.15 -> 0.63: -81/turn
  - retting pit 1 1.04 -> 0.00: -119/turn
  - flax farm 1 5.88 -> 0.00: -36/turn
  - flax farm 1 [make flax fibres 1] 0.00 -> 11.00: +140/turn
- Model check: not enough runs yet (needs 6 turns of goal history).
- Worth of one more unit per turn: labour 1.37, thread 3.78, cloth 5.83, flax fibres 5.08, garments 16.55, nets 16.92, beer 125.51, timber 2.83, prestige 3633.95, cash 100.00
- Orders it would set: beer sell 53 (v2 none); cured meat buy 1 (v2 2); donations buy 40 (v2 54); firewood buy 4 (v2 8); flax fibres sell 2 (v2 none); furniture buy 2 (v2 None); grain buy 29 (v2 0); light armour buy 1 (v2 None); porterage buy 7 (v2 6); thread sell 24 (v2 none)
- Recipe: flax farm 1 grow flax 1 -> make flax fibres 1 at 11.00, worth +85/turn.
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.34, worth +37/turn.
- Ship linen snake: Grandgues -> Brunnham (+4/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Bordetes (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +39/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new chandlery (make candles 1) for ~3623 coin: +17/turn, payback 213 turns, doesn't pay yet (materials thin at home: bricks, nails)

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

Buffers: flax fibres 477/46, thread 1061/134, cloth 0/27
- chain plan needed 393 labour, budget left 110: cut to 110 (sewing capped at 0.17)

## Self-diagnosis

- R1: arms slot dry: 0.0 held, 0.5 a turn (gear slot (+0.4 prestige)); our buy 1 @ 27, home ask 36.6; 5% of cash does not buy one at 37.2
- R1: cured meat slot dry: 0.0 held, 0.9 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 1 @ 29, home ask 22.0; our bid is already at/over the ask (sellers too thin)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy none, home ask 1.54 (held back: failsafe level 3: reduce-only, would buy 4 @ 1.57 (ask 1.54, cap 2.1))
- R1: pasties slot dry: 0.0 held, 2.8 a turn (basic food slot (+1.3 prestige)); our buy 2 @ 14.5, home ask 12.1; our bid is already at/over the ask (sellers too thin)
- R2: spinnery 1 blocked by thread space: 1061 held of 1084 capacity, we make 79.8 a turn; no buy on it: add a sell order or more capacity for thread
