# v2 shadow report

Turn 13568, 2026-10-26 17:11. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 151, prestige 3,536 (416 free, -0.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 28 | 0 | 4 | 0 | 0 | min_holding 60, sell 42, sell @ 2.94 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 0 | 0 | 0 | 0 | 0 | none |
| firewood | 0 | 0 | 0 | 4 | 0 | buy @ 2.4 |
| fish | 0 | 0 | 0 | 0 | 0 | none |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 2, sell @ 17.9 |
| grain | 47 | 0 | 0 | 0 | 0 | stop 81, buy 21, buy @ 3.7 |
| labour | 0 | 0 | 285 | 0 | 215 | buy @ 2.2 |
| meat | 0 | 0 | 0 | 0 | 0 | none |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 0 | 0 | 0 | 6 | 0 | buy 6, buy @ 1.1 |

**4 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: sewing shop 1 ran short of cloth (no buy order); labour need rises ~14/turn when they restart -> v2: add a cloth buy
- **firewood**: brewery 1 ran short of firewood (buy is live (no volume cap @ 2.4), home ask 1.51 x4, yet 0 bought last turn); labour need rises ~57/turn when they restart -> v2: find out why the buy isn't filling
- **porterage**: flax farm 1, retting pit 1 ran short of porterage (buy is live (6 @ 1.1), home ask 0.33 x32, yet 0 bought last turn); labour need rises ~90/turn when they restart -> v2: find out why the buy isn't filling
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 9.50 x9, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Tuning

- **candles**: home ask 75.50 is above our ceiling 70.00 and last turn bought 0 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 285, not 385

## Prestige spending, cheapest coin per prestige first

833 turns left: prestige gained now converts 98.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 44.4 | 44.4 | running |
| hold banquet 3 (pies) | mansion | 8 | 47.5 | 47.5 | thin at home: hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 48.6 | 48.6 | thin at home: hop beer, wine, pies |
| hold banquet 2 (pies) | mansion | 7 | 49.8 | 49.8 | thin at home: wine, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 50.0 | 50.0 | thin at home: hop beer |
| hold banquet 3 (meat) | mansion | 7.6 | 51.0 | 51.0 | thin at home: hop beer |
| hold banquet 2 (fish) | mansion | 6.8 | 51.6 | 51.6 | thin at home: wine |
| hold banquet 4 | mansion | 17.5 | 52.0 | 52.0 | thin at home: wine, hop beer, ham, stockfish |
| hold banquet 2 (meat) | mansion | 6.8 | 52.7 | 52.7 | thin at home: wine |
| hold banquet 1 (fish) | mansion | 4.2 | 52.9 | 52.9 |  |
| hold banquet 4 (premium) | mansion | 20 | 52.9 | 52.9 | thin at home: hop beer, wine, stockfish, premium cheese |
| jousting 3 | arena | 230 | 54.1 | 54.2 | needs a arena (build cost 23,256); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only -8 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -4 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~95 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.60 (57/turn) | firewood 28 (1.6->3.42), charcoal 11 (1.87->3.06), timber 24 (6.67->7.5), malt 3 (4.51->5.79) | grindstones 1 (231->285), arms 2 (27.3->32.11), candles 1 (68.78->71.5), garments 2 (23.31->24) | +104 |
| Rouhomme | 368 | 0.09 | 0.60 (57/turn) | bread 144 (2.09->2.51), charcoal 11 (1.87->3.31), grain 3 (2.4->2.94), malt 1 (4.51->5.22) | grindstones 1 (231->285), spinning wheels 1 (216.3->226.1), garments 2 (21.42->24), candles 1 (69.83->71.5) | +95 |
| Chatgnan | 728 | 0.18 | 0.10 (10/turn) | cured meat 2 (22.68->28.12), malt 2 (4.51->7.79) | grindstones 1 (212.1->285), garments 2 (21->24), cloth 6 (8.35->8.7), wool 1 (7.98->8.26) | +89 |
| Angefont | 686 | 0.17 | 0.20 (19/turn) | premium ham 1 (273->285), limestone 1 (15.02->28.12), malt 5 (4.51->5.98), casks 7 (4.96->5.94) | grindstones 1 (231->285), candles 1 (68.78->71.5), flax fibres 10 (4.62->5.25), silver ore 1 (33.81->35.53) | +85 |
| Pontmont | 341 | 0.09 | 0.10 (10/turn) | malt 9 (4.51->6.55), garments 1 (23.2->28.88), limestone 1 (15.02->22.04), tiles 2 (3.32->4.69) | grindstones 1 (231->285), candles 1 (67.2->71.5), medicine 1 (126->127.3), beer 4 (3.26->3.44) | +84 |

**Best:** Grandgues at about +104 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer | 5 @ 3.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 28 = 6.8 turns |
| candles | 3 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 4 = 2.3 turns |
| firewood | 3 @ 2.4, stop 10 |  | goal planner: buys 3 a turn for today's rates, keeps up to 10 (v2 had 8) |
| flax fibres |  | 3 @ min 4.76 | goal planner: sells 3 a turn at 4.76, keeps 82 (no one offered it) |
| furniture | 2 @ 13.3, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| grain | 19 @ 3.7, stop 76 |  | goal planner: buys 19 a turn for today's rates, keeps up to 76 (v2 had 0) |
| labour | 0 @ 2.2, stop - |  | goal planner: buys 0 for today's rates (v2 had 0) |
| light armour | 1 @ 96.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 36.6) |
| porterage | 6 @ 1.1, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| thread |  | 27 @ min 4 | goal planner: sells 27 a turn at 4, keeps 169 (no one offered it) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 195 |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 16.2k (cash + stock at home prices); -333/turn over 6 turns, -96/turn over 24 turns.
- Limits: cash flow >= +160/turn, prestige >= -0.48/turn (values are after 200 tax a turn).
- Today's settings: value +98/turn, cash -61/turn, prestige +7.50/turn - breaks the cash floor.
- Plan: value +363/turn, cash -23/turn, prestige -0.48/turn - could not meet the cash floor.
- Cash check (real vs predicted cash a tick, last 3): -5 vs -46, +1 vs -32, +27 vs -49.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Pontmont: +3/turn
  - ship Flax Wyrm -> Bordetes: +0/turn
  - park 1 16.00 -> 0.03: +0/turn
  - weavery 1 0.13 -> 1.29: +15/turn
  - sewing shop 1 0.09 -> 0.80: +132/turn
  - spinnery 1 1.59 -> 2.79: +112/turn
  - brewery 1 0.44 -> 0.29: +9/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.25: -12/turn
  - ropewalk 1 0.25 -> 0.00: +14/turn
  - retting pit 1 0.78 -> 0.00: -143/turn
- Model check: not enough runs yet (needs 6 turns of goal history).
- Worth of one more unit per turn: labour 0.94, thread 3.00, cloth 4.41, flax fibres 4.68, garments 12.15, nets 16.92, beer 122.13, timber 2.83, prestige 28.16, cash 100.00
- Orders it would set: firewood buy 3 (v2 8); fish buy 0 (v2 None); flax fibres sell 3 (v2 none); furniture buy 2 (v2 None); grain buy 19 (v2 0); light armour buy 1 (v2 None); meat buy 0 (v2 None); rope sell 1 (v2 none); thread sell 27 (v2 none)
- Recipe: flax farm 1 grow flax 1 -> make flax fibres 1 at 11.00, worth +146/turn.
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.25, worth +26/turn.
- Ship linen snake: Grandgues -> Pontmont (+3/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Bordetes (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +47/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new chandlery (make candles 1) for ~3992 coin: +21/turn, payback 193 turns, doesn't pay yet (materials thin at home: bricks, nails)
  - +1 plot flax farm 1 for ~444 coin: +3/turn, payback 134 turns
- Trim: donate park 1: +96/turn (tax 96 saved).

## Chain sizing

Mode HOLD, garments sold 1.2/turn (+0.0 exported); plan makes 8.6 garments a turn.
Labour: own 500, everything else 379, chain may buy 0 -> chain allowance 121, chain plan 120 (-113 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.88 | 0.41 |
| ret | 3 | 0.78 | 0.07 |
| spin | 4 | 1.59 | 0.74 |
| weave | 3 | 0.13 | 0.34 |
| sew | 2 | 0.09 | 0.21 |

Buffers: flax fibres 449/45, thread 1058/134, cloth 0/34
- chain plan needed 384 labour, budget left 121: cut to 121 (sewing capped at 0.21)

## Self-diagnosis

- R1: arms slot dry: 0.0 held, 0.5 a turn (gear slot (+0.4 prestige)); our buy 1 @ 27, home ask 33.8; 5% of cash does not buy one at 34.4
- R1: donations slot dry: 0.0 held, 40.0 a turn (luxury slot (+1 prestige)); our buy none, home ask 1.0 (held back: failsafe level 3: reduce-only, would buy 7 @ 1.02 (ask 1.0, cap 1.5))
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy none, home ask 1.51 (held back: failsafe level 3: reduce-only, would buy 4 @ 1.54 (ask 1.51, cap 2.1))
- R1: fish slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask 1.68 (held back: failsafe level 3: reduce-only, would buy 4 @ 1.71 (ask 1.68, cap 2.6))
- R1: meat slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask 1.51 (held back: failsafe level 3: reduce-only, would buy 4 @ 1.54 (ask 1.51, cap 2.6))
- R1: pasties slot dry: 0.0 held, 2.8 a turn (basic food slot (+1.3 prestige)); our buy 2 @ 14.5, home ask 13.1; our bid is already at/over the ask (sellers too thin)
- R2: spinnery 1 blocked by thread space: 1058 held of 1084 capacity, we make 79.8 a turn; no buy on it: add a sell order or more capacity for thread
- R5: candles buy not filling: bid 69 under the home ask 75.5 for 5 turns, bought 0.0 of 2, 3.5 held (2.3 turns)
