# v2 shadow report

Turn 13560, 2026-10-26 09:22. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 352, prestige 3,551 (431 free, -2.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 7 | 0 | 0 | min_holding 60, sell 55, sell @ 2.98 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 8 | 0 | 6 | 1 | 0 | buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 2, sell @ 17.9 |
| grain | 35 | 21 | 22 | 0 | 0 | stop 81, buy 21, buy @ 3.7 |
| labour | 0 | 0 | 450 | 0 | 50 | buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 14 | 14 | 13 | 0 | 1 | buy 14, buy @ 1.1 |

**3 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: sewing shop 1 ran short of cloth (no buy order); labour need rises ~14/turn when they restart -> v2: add a cloth buy
- **firewood**: brewery 1 ran short of firewood (buy is live (no volume cap @ 2.4), home ask 1.58 x6, yet 0 bought last turn); labour need rises ~57/turn when they restart -> v2: find out why the buy isn't filling
- **varnish**: net maker152202386007001 ran short of varnish (buy is live (1 @ 20.6), but the home ask 21.00 is above it); labour need rises ~5/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Tuning

- **flax plants**: flax plants buffer thin: 1.2 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 187
- **tar**: home ask 11.70 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 112 over real use lately; planning 450, not 537

## Prestige spending, cheapest coin per prestige first

841 turns left: prestige gained now converts 98.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 3 (pies) | mansion | 8 | 45.1 | 45.1 | thin at home: hop beer, pies |
| maintain 1 | park | 0.5 | 46.2 | 46.2 | running |
| hold banquet 4 (pies) | mansion | 18 | 47.1 | 47.1 | thin at home: hop beer, wine, pies |
| hold banquet 2 (pies) | mansion | 7 | 48.8 | 48.8 | thin at home: wine, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 49.8 | 49.8 | thin at home: hop beer |
| hold banquet 3 (meat) | mansion | 7.6 | 50.2 | 50.2 | thin at home: hop beer |
| hold banquet 4 | mansion | 17.5 | 50.6 | 50.6 | thin at home: wine, hop beer, ham, stockfish |
| hold banquet 2 (fish) | mansion | 6.8 | 52.9 | 52.9 | thin at home: wine |
| jousting 3 | arena | 230 | 52.9 | 53.1 | needs a arena (build cost 24,540); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 53.4 | 53.4 | thin at home: wine |
| hold banquet 4 (premium) | mansion | 20 | 53.4 | 53.4 | thin at home: hop beer, wine, stockfish, premium cheese |
| hold sermon 2 (candles) | church | 31 | 51.8 | 54.4 | needs a church (build cost 61,754); thin at home: candles, furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~97 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Fontaux | 411 | 0.11 | 0.30 (29/turn) | charcoal 11 (1.64->4.26), thread 69 (4.08->4.46), malt 2 (4.75->5.75), garments 1 (19->19.76) | looms 1 (522.9->541.5), tin ingots 1 (31.08->36.1), premium cheese 1 (24.15->27.55) | +61 |
| Rouhomme | 368 | 0.10 | 0.70 (68/turn) | bread 144 (2.39->2.83), charcoal 11 (1.64->3.25), thread 7 (4.08->4.58), bricks 5 (3.32->5.61) | candles 1 (50.4->67.5), flax fibres 8 (4.94->5.4), cloth 6 (7.46->7.65), tools 2 (4.73->5.2) | +58 |
| Karlmoor | 787 | 0.20 | 0.10 (10/turn) | seeds 12 (2.79->4.8), premium cheese 1 (34.86->43.89), blades 2 (16.28->20.52), garments 1 (19->21.28) | arms 3 (28.35->30.4), furniture 1 (9.03->13.9), lead bars 1 (8.19->11.78) | +53 |
| Kirchwerp | 1072 | 0.35 | 0.20 (19/turn) | candles 2 (70.88->84.55), thread 50 (4.08->4.58), yarn 3 (4.03->5.08) | herbs 2 (33.6->38.57), harnesses 1 (48.3->52.25) | +48 |
| Vauxvais | 204 | 0.05 | 0.20 (19/turn) | bricks 6 (3.32->7.98), cloth 5 (8.03->11.59), limestone 2 (17.22->20.9), charcoal 11 (1.64->2.24) | candles 1 (66.15->67.5), flax fibres 5 (5.04->5.4), tools 2 (4.77->5.2), furniture 1 (13.65->13.9) | +47 |

**Best:** Fontaux at about +61 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| candles | 2 @ 69, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cured meat | 1 @ 29.0, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 2) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 0 @ 2.4, stop 13 |  | uses 6.3/turn (household upkeep), makes 6.5, holds 8 |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres |  | 2 @ min 4.76 | goal planner: sells 2 a turn at 4.76, keeps 82 (no one offered it) |
| furniture | 2 @ 14.2, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| grain | 29 @ 3.7, stop 115 |  | goal planner: buys 29 a turn for today's rates, keeps up to 115 (v2 had 58) |
| labour | 0 @ 2.2, stop - |  | goal planner: buys 0 for today's rates (v2 had 0) |
| light armour | 1 @ 94, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 36.2) |
| porterage | 14 @ 1.1, stop - |  | goal planner: buys 14 for today's rates (v2 had 13) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 (v2 had 1) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 0 = 2.0 turns |
| thread |  | 24 @ min 4.08 | goal planner: sells 24 a turn at 4.08, keeps 180 (no one offered it) |
| tools | 3 @ 6.2, stop 17 |  | uses 2.1/turn (retting pit 1), makes 0.0, holds 199 = 95.7 turns |
| varnish | 1 @ 22.0, stop 1 | off | a building is stalled on varnish: no sell until it runs again |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 17.6k (cash + stock at home prices); -105/turn over 6 turns, -47/turn over 24 turns.
- Limits: cash flow >= +152/turn, prestige >= -0.55/turn (values are after 220 tax a turn).
- Today's settings: value +87/turn, cash -7/turn, prestige -2.32/turn - breaks the prestige floor and cash floor.
- Plan: value +25/turn, cash -15/turn, prestige -0.55/turn - could not meet the cash floor.
- Cash check (real vs predicted cash a tick, last 3): -101 vs +1, -7 vs -13, -67 vs -0.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Angefont: +3/turn
  - ship Flax Wyrm -> Bordetes: +0/turn
  - spinnery 1 1.59 -> 1.71: +10/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.38: -4/turn
  - ropewalk 1 0.25 -> 0.00: +19/turn
  - net maker 0.23 -> 0.00: +3/turn
  - mansion 1 0.15 -> 0.58: -80/turn
  - retting pit 1 1.04 -> 0.00: -118/turn
  - flax farm 1 5.88 -> 0.00: -24/turn
  - flax farm 1 [make flax fibres 1] 0.00 -> 9.55: +116/turn
- Model check: not enough runs yet (needs 6 turns of goal history).
- Worth of one more unit per turn: labour 1.34, thread 3.64, cloth 5.65, flax fibres 4.82, garments 16.08, nets 16.74, beer 119.64, timber 2.85, prestige 3555.01, cash 100.00
- Orders it would set: candles buy 2 (v2 None); cured meat buy 1 (v2 2); flax fibres sell 2 (v2 none); furniture buy 2 (v2 None); grain buy 29 (v2 58); light armour buy 1 (v2 None); porterage buy 14 (v2 13); rope sell 2 (v2 1); thread sell 24 (v2 none)
- Recipe: flax farm 1 grow flax 1 -> make flax fibres 1 at 9.55, worth +108/turn.
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.38, worth +42/turn.
- Ship linen snake: Grandgues -> Angefont (+3/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Bordetes (+0/turn over staying).
- Management: ~12.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +40/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new chandlery (make candles 1) for ~3741 coin: +11/turn, payback 348 turns, doesn't pay yet (materials thin at home: bricks, nails)
- Trim: donate logging camp w/ tool: +17/turn (tax 20 saved).

## Chain sizing

Mode HOLD, garments sold 1.1/turn (+0.0 exported); plan makes 6.6 garments a turn.
Labour: own 500, everything else 394, chain may buy 0 -> chain allowance 106, chain plan 105 (-135 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.88 | 0.39 |
| ret | 3 | 1.04 | 0.07 |
| spin | 4 | 1.59 | 0.73 |
| weave | 3 | 0.13 | 0.26 |
| sew | 2 | 0.09 | 0.16 |

Buffers: flax fibres 410/45, thread 1070/133, cloth 0/26
- chain plan needed 393 labour, budget left 106: cut to 106 (sewing capped at 0.16)

## Self-diagnosis

- R1: arms slot dry: 0.0 held, 0.5 a turn (gear slot (+0.4 prestige)); our buy 1 @ 27, home ask 32.8; 5% of cash does not buy one at 33.4
- R1: pasties slot dry: 0.0 held, 2.8 a turn (basic food slot (+1.3 prestige)); our buy 2 @ 14.5, home ask 12.1; our bid is already at/over the ask (sellers too thin)
- R2: spinnery 1 blocked by thread space: 1070 held of 1084 capacity, we make 79.8 a turn; no buy on it: add a sell order or more capacity for thread
