# v2 shadow report

Turn 13561, 2026-10-26 10:43. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 423, prestige 3,567 (447 free, +15.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 7 | 0 | 0 | min_holding 60, sell 55, sell @ 2.98 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 1 | 0 | 6 | 0 | 0 | buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 2, sell @ 17.9 |
| grain | 23 | 21 | 29 | 0 | 0 | stop 81, buy 21, buy @ 3.7 |
| labour | 0 | 0 | 426 | 0 | 74 | buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 14 | 14 | 6 | 0 | 8 | buy 14, buy @ 1.1 |

**3 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: sewing shop 1 ran short of cloth (no buy order); labour need rises ~14/turn when they restart -> v2: add a cloth buy
- **grain**: only 0.8 turns of grain left and buying 21 (need 58) -> v2: buy 58
- **varnish**: net maker152202386007001 ran short of varnish (buy is live (1 @ 20.6), but the home ask 21.20 is above it); labour need rises ~5/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Tuning

- **flax plants**: flax plants buffer thin: 1.2 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 187
- **tar**: home ask 11.80 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 107 over real use lately; planning 426, not 512

## Prestige spending, cheapest coin per prestige first

840 turns left: prestige gained now converts 98.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 3 (pies) | mansion | 8 | 44.9 | 44.9 | thin at home: hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 45.9 | 45.9 | thin at home: hop beer, wine, pies |
| maintain 1 | park | 0.5 | 45.9 | 45.9 | running |
| hold banquet 2 (pies) | mansion | 7 | 48.6 | 48.6 | thin at home: wine, pies |
| hold banquet 4 | mansion | 17.5 | 49.0 | 49.0 | thin at home: wine, hop beer, stockfish |
| hold banquet 3 (fish) | mansion | 7.6 | 49.5 | 49.5 | thin at home: hop beer |
| hold banquet 3 (meat) | mansion | 7.6 | 50.4 | 50.4 | thin at home: hop beer, cured meat |
| hold banquet 4 (premium) | mansion | 20 | 52.0 | 52.0 | thin at home: hop beer, wine, stockfish, premium cheese |
| hold banquet 2 (fish) | mansion | 6.8 | 52.6 | 52.6 | thin at home: wine |
| jousting 3 | arena | 230 | 53.2 | 53.3 | needs a arena (build cost 24,634); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 53.6 | 53.6 | thin at home: wine, cured meat |
| hold banquet 1 (fish) | mansion | 4.2 | 54.4 | 54.4 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -9 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~98 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Rouhomme | 368 | 0.10 | 1.00 (98/turn) | premium ham 0 (270.9->305.9), charcoal 6 (1.63->3.27), bread 90 (2.14->2.49), firewood 19 (1.65->4.75) | candles 0 (50.4->67.5), flax fibres 2 (4.94->7.65), cloth 3 (7.56->8.25), garments 1 (20.68->22.2) | +73 |
| Vauxvais | 204 | 0.05 | 0.20 (20/turn) | bricks 5 (3.72->8.17), limestone 3 (16.59->20.9), charcoal 11 (1.63->2.2), malt 1 (4.49->5.37) | flax fibres 4 (5.25->7.65), cloth 6 (7.35->8.25), garments 2 (20.89->22.2), candles 1 (65.1->67.5) | +47 |
| Orlesailles | 1178 | 0.41 | 0.20 (20/turn) | thread 20 (4.18->6.27), harnesses 1 (49.14->50.82), malt 3 (4.49->5.42) | arms 6 (28.35->30.21), flax fibres 3 (5.51->7.65), garments 2 (21.63->22.2) | +45 |
| Darmwald | 1022 | 0.33 | 0.50 (49/turn) | charcoal 11 (1.63->6.89), premium cheese 1 (34.86->37.81), thread 25 (4.18->4.6), malt 2 (4.49->5.56) | cloth 6 (7.14->8.25), flax fibres 3 (5.99->7.65), casks 3 (3.49->4.73) | +45 |
| Fontaux | 411 | 0.11 | 0.30 (29/turn) | charcoal 11 (1.63->4.35), thread 69 (4.18->4.46), malt 2 (4.49->5.75), beer 53 (3.12->3.34) | flax fibres 4 (5.93->7.65) | +43 |

**Best:** Rouhomme at about +73 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 55 @ min 2.98 | goal planner: sells 55 at 2.98 (v2 had 55 at 3.38) |
| candles | 2 @ 69, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cured meat | 2 @ 29.0, stop 4 |  | uses 0.9/turn (mansion 1), makes 0.0, holds 1 = 1.2 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 7 @ 2.4, stop 25 |  | goal planner: buys 7 a turn for today's rates, keeps up to 25 (v2 had 13) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres |  | 2 @ min 4.76 | goal planner: sells 2 a turn at 4.76, keeps 82 (no one offered it) |
| grain | 27 @ 3.7, stop 107 |  | goal planner: buys 27 a turn for today's rates, keeps up to 107 (v2 had 58) |
| labour | 0 @ 2.2, stop - |  | goal planner: buys 0 for today's rates (v2 had 0) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 36.2) |
| porterage | 7 @ 1.1, stop - |  | goal planner: buys 7 for today's rates (v2 had 6) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 (v2 had 1) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 0 = 1.0 turns |
| thread |  | 23 @ min 4.08 | goal planner: sells 23 a turn at 4.08, keeps 180 (no one offered it) |
| tools | 3 @ 6.2, stop 17 |  | uses 2.1/turn (retting pit 1), makes 0.0, holds 197 = 94.7 turns |
| varnish | 1 @ 22.2, stop 1 | off | a building is stalled on varnish: no sell until it runs again |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 18.7k (cash + stock at home prices); +168/turn over 6 turns, -3/turn over 24 turns.
- Limits: cash flow >= +149/turn, prestige >= -0.61/turn (values are after 200 tax a turn).
- Today's settings: value +90/turn, cash -31/turn, prestige +15.60/turn - breaks the cash floor.
- Plan: value +248/turn, cash +34/turn, prestige +6.95/turn - could not meet the cash floor.
- Cash check (real vs predicted cash a tick, last 3): -7 vs -13, -67 vs -0, +71 vs -7.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Rouhomme: +26/turn
  - ship Flax Wyrm -> Bordetes: +0/turn
  - mansion 1 0.15 -> 0.00: +24/turn
  - net maker 0.23 -> 0.00: +3/turn
  - park 1 16.00 -> 0.00: +0/turn
  - weavery 1 0.13 -> 1.22: +4/turn
  - spinnery 1 1.59 -> 2.73: +96/turn
  - sewing shop 1 0.09 -> 0.76: +75/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.34: -20/turn
  - ropewalk 1 0.25 -> 0.00: +28/turn
- Model check: not enough runs yet (needs 6 turns of goal history).
- Worth of one more unit per turn: labour 0.54, thread 3.27, cloth 4.08, flax fibres 7.25, garments 9.99, nets 16.74, beer 125.86, timber 2.91, prestige 0.00, cash 100.00
- Orders it would set: candles buy 2 (v2 None); firewood buy 7 (v2 13); flax fibres sell 2 (v2 none); grain buy 27 (v2 58); light armour buy 1 (v2 None); porterage buy 7 (v2 6); rope sell 2 (v2 1); thread sell 23 (v2 none)
- Recipe: flax farm 1 grow flax 1 -> make flax fibres 1 at 11.00, worth +226/turn.
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.34, worth +34/turn.
- Ship linen snake: Grandgues -> Rouhomme (+26/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Bordetes (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - new chandlery (make candles 1) for ~3773 coin: +27/turn, payback 138 turns, doesn't pay yet (materials thin at home: bricks, nails)
  - Tenants L13 for 500 prestige: +27/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot flax farm 1 for ~448 coin: +13/turn, payback 35 turns
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

Buffers: flax fibres 438/46, thread 1046/134, cloth 0/27
- chain plan needed 393 labour, budget left 110: cut to 110 (sewing capped at 0.17)

## Self-diagnosis

- R1: arms slot dry: 0.0 held, 0.5 a turn (gear slot (+0.4 prestige)); our buy 1 @ 27, home ask 34.2; 5% of cash does not buy one at 34.8
- R1: cured meat slot dry: 1.1 held, 0.9 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 1 @ 29, home ask 22.6; our bid is already at/over the ask (sellers too thin)
- R1: firewood slot dry: 1.2 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy none, home ask 1.57 (held back: failsafe level 3: reduce-only, would buy 6 @ 1.6 (ask 1.57, cap 2.1))
- R1: pasties slot dry: 0.0 held, 2.8 a turn (basic food slot (+1.3 prestige)); our buy 2 @ 14.5, home ask 12.1; our bid is already at/over the ask (sellers too thin)
- R2: spinnery 1 blocked by thread space: 1046 held of 1084 capacity, we make 79.8 a turn; no buy on it: add a sell order or more capacity for thread
- R5: tar buy not filling: bid 11 under the home ask 11.8 for 3 turns, bought 0.0 of 1, 0.2 held (1.0 turns); raise needs Taylor (ceiling 11.0)
- R5: varnish buy not filling: bid 20.6 under the home ask 21.2 for 3 turns, bought 0.0 of 1, 0.0 held (0.0 turns); raise needs Taylor (ceiling None)
