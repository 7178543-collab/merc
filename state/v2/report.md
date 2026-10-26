# v2 shadow report

Turn 13551, 2026-10-26 00:30. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 1,392, prestige 3,569 (449 free, -1.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 7 | 0 | 0 | min_holding 60, sell 55, sell @ 2.98 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 7 | 0 | 6 | 0 | 0 | buy @ 2.4; sell 1, sell @ 1.74 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 2, sell @ 17.9 |
| grain | 64 | 21 | 29 | 0 | 0 | stop 81, buy 21, buy @ 3.7 |
| labour | 0 | 0 | 463 | 0 | 37 | buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 10, sell @ 33.6 |
| porterage | 14 | 14 | 13 | 0 | 1 | buy 14, buy @ 1.1 |

**1 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: sewing shop 1 ran short of cloth (no buy order); labour need rises ~14/turn when they restart -> v2: add a cloth buy

## Tuning

- **flax plants**: flax plants buffer thin: 1.2 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 187

## Notes

- labour: projection runs 124 over real use lately; planning 463, not 570

## Prestige spending, cheapest coin per prestige first

850 turns left: prestige gained now converts 98.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 45.9 | 45.9 | running |
| hold banquet 3 (pies) | mansion | 8 | 47.2 | 47.2 | thin at home: hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 49.0 | 49.0 | thin at home: hop beer, wine, ham, pies |
| hold banquet 2 (pies) | mansion | 7 | 49.7 | 49.7 | thin at home: wine, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 49.9 | 49.9 | thin at home: hop beer |
| hold banquet 3 (meat) | mansion | 7.6 | 50.5 | 50.5 | thin at home: hop beer |
| hold banquet 2 (fish) | mansion | 6.8 | 51.8 | 51.8 | thin at home: wine |
| hold banquet 2 (meat) | mansion | 6.8 | 52.5 | 52.5 | thin at home: wine |
| hold banquet 4 | mansion | 17.5 | 52.6 | 52.6 | thin at home: wine, hop beer, ham, stockfish |
| jousting 3 | arena | 230 | 52.8 | 52.9 | needs a arena (build cost 23,209); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold prayer 2 | chapel | 13 | 51.0 | 53.9 | needs a chapel (build cost 29,009) |
| hold banquet 1 (fish) | mansion | 4.2 | 54.2 | 54.2 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only -2 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only 4 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~94 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.50 (47/turn) | beer 55 (3.54->4.35), firewood 28 (1.83->3.21), charcoal 11 (1.96->2.77), logs 1 (3.72->6.98) | candles 1 (68.78->74.5), pasties 2 (11.13->13.4), fleece 1 (6.67->8.46), nails 2 (5.72->6.22) | +68 |
| Bordetes | 831 | 0.22 | 0.10 (9/turn) | gold ore 1 (152.25->181.45), tackles 1 (160.65->178.6), harnesses 1 (52.5->56.52), wrought iron 3 (14.6->16.15) | spinning wheels 1 (207.9->216.6), candles 1 (73.5->74.5), fleece 1 (6.98->8.46), tools 2 (4.45->5) | +65 |
| Helmgreen | 1354 | 0.48 | 0.10 (9/turn) | nets 1 (36.4->38.57), garments 1 (18.2->18.9) | looms 1 (508.2->551), candles 1 (64.58->74.5), fleece 5 (7.4->8.46), tin ingots 1 (33.18->36.48) | +54 |
| Briclives | 1041 | 0.32 | 0.10 (9/turn) | tackles 1 (160.65->209), harnesses 1 (52.5->55.1), honey 2 (7.82->8.88), slaked lime 2 (8.14->9.5) | candles 1 (71.92->74.5), tools 2 (4.26->5), mouldboards 2 (32.34->32.68) | +51 |
| Gotthafen | 964 | 0.28 | 0.10 (9/turn) | tackles 1 (160.65->203.3), dyed cloth 1 (11.34->13.59), flax fibres 3 (4.82->5.65) | candles 1 (70.88->74.5), premium cheese 1 (26.46->30.02), pasties 2 (11.45->13.4), fleece 2 (7.61->8.46) | +50 |

**Best:** Grandgues at about +68 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 27.4, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 3.0 turns |
| beer |  | 55 @ min 2.98 | goal planner: sells 55 at 2.98 (v2 had 55 at 3.44) |
| cured meat | 1 @ 29.0, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 2) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 0 @ 2.4, stop 13 | 1 @ min 1.73 | uses 6.3/turn (brewery 1, household upkeep), makes 6.5, holds 7 |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres |  | 1 @ min 4.82 | goal planner: sells 1 a turn at 4.82, keeps 82 (no one offered it) |
| grain | 29 @ 3.7, stop 114 |  | goal planner: buys 29 a turn for today's rates, keeps up to 114 (v2 had 55) |
| labour | 0 @ 2.2, stop - |  | goal planner: buys 0 for today's rates (v2 had 0) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 10 @ min 33.6 | goal planner: sells 10 at 33.6 (v2 had 10 at 35.4) |
| pasties | 4 @ 14.5, stop 8 |  | uses 2.0/turn (household upkeep), makes 0.0, holds 2 = 1.0 turns |
| porterage | 14 @ 1.1, stop - |  | goal planner: buys 14 for today's rates (v2 had 13) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 71.0) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 1 = 3.0 turns |
| thread |  | 18 @ min 4.26 | goal planner: sells 18 a turn at 4.26, keeps 180 (no one offered it) |
| tools | 3 @ 6.2, stop 18 |  | uses 2.2/turn (net maker152202386007001, retting pit 1), makes 0.0, holds 199 = 89.6 turns |
| varnish | 1 @ 20.4, stop 1 |  | uses 0.1/turn (net maker152202386007001), makes 0.0, holds 0 = 6.2 turns |
| wax | 1 @ 25.4, stop 1 |  | uses 0.1/turn (net maker152202386007001), makes 0.0, holds 1 = 12.2 turns |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 18.0k (cash + stock at home prices); -71/turn over 6 turns, +3/turn over 24 turns.
- Limits: cash flow >= +109/turn, prestige >= -0.62/turn (values are after 220 tax a turn).
- Today's settings: value +100/turn, cash +41/turn, prestige -1.93/turn - breaks the prestige floor and cash floor.
- Plan: value +127/turn, cash +117/turn, prestige -0.62/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -198 vs +55, -337 vs +55, -252 vs +27 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Vauxvais: +0/turn
  - ship Flax Wyrm -> Grandgues: +4/turn
  - ropewalk 1 0.25 -> 0.72: +47/turn
  - spinnery 1 1.59 -> 2.10: +23/turn
  - net maker 0.23 -> 0.00: +3/turn
  - weavery 1 0.13 -> 0.23: +7/turn
  - logging camp w/ tool 5.00 -> 4.84: +0/turn
  - mansion 1 0.15 -> 0.47: -64/turn
- Model check over the last 56 turns: predicted +108/turn for the settings we ran, real +32/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.53, thread 3.78, cloth 6.07, flax fibres 4.36, garments 17.63, nets 16.38, beer 2.69, timber 2.86, prestige 52.66, cash 0.00
- Orders it would set: cured meat buy 1 (v2 2); flax fibres sell 1 (v2 none); furniture buy 2 (v2 None); grain buy 29 (v2 55); light armour buy 1 (v2 None); porterage buy 14 (v2 13); rope sell 2 (v2 1); thread sell 18 (v2 none)
- Ship linen snake: Grandgues -> Vauxvais (+0/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Grandgues (+4/turn over staying).
- Management: ~12.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +76/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new chandlery (make candles 2) for ~3978 coin: +3/turn, payback 1577 turns, doesn't pay yet (materials thin at home: bricks, nails)
- Trim: donate logging camp w/ tool: +17/turn (tax 20 saved).

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

Buffers: flax fibres 228/45, thread 1048/133, cloth 0/26
- chain plan needed 393 labour, budget left 106: cut to 106 (sewing capped at 0.16)

## Self-diagnosis

- R2: spinnery 1 blocked by thread space: 1048 held of 1084 capacity, we make 79.8 a turn; no buy on it: add a sell order or more capacity for thread
