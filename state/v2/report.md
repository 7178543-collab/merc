# v2 shadow report

Turn 14064, 2026-11-16 09:21. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 7,989, prestige 3,650 (530 free, -3.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 0 | 0 | 0 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 35 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 29 | 29 | 518 | 0 | 11 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 0 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.92 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.92 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 10.90 x12, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Notes

- labour: projection runs 117 over real use lately; planning 518, not 614

## Prestige spending, cheapest coin per prestige first

337 turns left: prestige gained now converts 81.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 50.0 | 50.4 | needs a arena (build cost 27,606); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 51.3 | 51.3 | running |
| jousting 2 | arena | 210 | 54.7 | 55.2 | needs a arena (build cost 27,606); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 58.0 | 58.0 | thin at home: beer, cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 59.5 | 59.5 | thin at home: wine, cured fish |
| hold banquet 2 (pies) | mansion | 7 | 60.5 | 60.5 | thin at home: wine |
| hold banquet 1 (meat) | mansion | 4.2 | 61.7 | 61.7 | thin at home: beer |
| hold banquet 2 (meat) | mansion | 6.8 | 61.9 | 61.9 | thin at home: wine |
| hold banquet 4 (pies) | mansion | 18 | 63.1 | 63.1 | thin at home: hop beer, wine, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 63.5 | 63.5 | thin at home: hop beer, wine, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 63.6 | 63.6 | thin at home: hop beer |
| hold mass 2 (premium) | cathedral | 360 | 60.1 | 64.1 | needs a cathedral (build cost 310,710); thin at home: furniture, jewellery, glassware, candles, premium garments |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.20 | 20 | 134102075 | 0.348 | - | furniture 21, pasties 1 | -313 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: candles buy 3 @ 77.5, furniture buy 21 @ 14.5, pasties buy 1 @ 15.6; crew 0.2; est +269 a turn; stock: candles 3 @ 77.5 (keep 12); stock: furniture 21 @ 14.5 (keep 145); stock: pasties 1 @ 15.6 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 16.2 (keep 14); best orders clear only -8 a turn after crew: ship stays at 0
- best towns now: Caillechâtel +269, Vauxvais +267, Boistot +253, Clairas +252, Blanans +251
- Caillechâtel would trade: candles buy 3 @ 77.5, furniture buy 21 @ 14.5, pasties buy 1 @ 15.6; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~108 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.80 (86/turn) | timber 38 (8.09->12.54), firewood 35 (3.07->6.37), charcoal 19 (2.92->5.42), thread 11 (4.78->6.17) | cloth 7 (8.35->9.45), looms 1 (582.75->589), salt 7 (5.35->5.56), dyed cloth 3 (12.39->12.44) | +286 |
| Gotthafen | 964 | 0.33 | 0.20 (22/turn) | garments 10 (24.6->30.78), lead ore 3 (7.67->12.25), tiles 1 (3.02->10.45), wine 3 (6.51->7.6) | tapestries 1 (598.5->631.75), cloth 13 (7.61->9.45), jewellery 8 (84->86.45), salt 7 (4.7->5.56) | +152 |
| Heilegg | 826 | 0.24 | 0.60 (65/turn) | charcoal 19 (2.92->6.03), garments 10 (24.6->26.79), nets 6 (34.2->36.48), lead ore 7 (7.67->9.59) | cloth 24 (7.72->9.45), cheese 11 (6.3->7.08), tools 16 (5.51->5.89), candles 1 (81.38->82.5) | +114 |
| Kirchwerp | 1072 | 0.39 | 0.50 (54/turn) | lead ore 10 (7.67->10.45), wine 5 (6.51->7.5), acid 1 (115.5->116.85), tar 8 (11.45->12.35) | cloth 24 (7.56->9.45), jewellery 8 (84->86.45), lathes 1 (212.1->231.8), ploughs 2 (73.5->83.12) | +106 |
| Pontmont | 341 | 0.10 | 1.00 (108/turn) | firewood 33 (3.07->8.07), tiles 5 (3.02->6.6), acid 0 (115.5->127.3), rope 0 (79.8->84.08) | cloth 6 (8.93->9.45), logs 1 (4.2->7.22), ploughs 1 (81.9->83.12), resin 0 (3.19->3.42) | +100 |

**Best:** Grandgues at about +286 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.0, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 4.0 turns |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| candles | 2 @ 76.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 5 = 3.3 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 24.0) |
| grain | 0 @ 3.7, stop 22 |  | goal planner: buys 0 a turn for today's rates, keeps up to 22 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 18) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 34.0 |  |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.3/turn (observed), makes 0.0, holds 1 = 2.9 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 21.4k (cash + stock at home prices); -505/turn over 6 turns, -96/turn over 24 turns.
- Limits: cash flow >= -166/turn, prestige >= -0.96/turn (values are after 200 tax a turn).
- Today's settings: value +72/turn, cash +45/turn, prestige -3.37/turn - breaks the prestige floor.
- Plan: value -17/turn, cash -8/turn, prestige -0.96/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -22 vs +39, -268 vs +28, -160 vs +33 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Brunnham: +6/turn
  - ship Flax Wyrm -> Bordetes: +0/turn
  - ropewalk 1 0.25 -> 0.15: +12/turn
  - net maker 0.00 -> 0.29: +10/turn
  - spinnery 1 1.65 -> 1.49: +4/turn
  - sewing shop 1 0.30 -> 0.39: -12/turn
  - weavery 1 0.50 -> 0.64: +18/turn
  - mansion 1 0.00 -> 0.57: -132/turn
- HAND-OVER: goal planner: model check failed 3 runs in a row, buys handed back to the old rules.
- Model check over the last 59 turns: predicted -56/turn for the settings we ran, real -126/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.71, thread 4.30, cloth 6.86, flax fibres 5.10, garments 19.86, nets 30.99, beer 3.21, timber 3.31, prestige 60.72, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 6 (v2 0); labour buy 29 (v2 18); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Brunnham (+9/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Bordetes (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +85/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 11.0/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 419 (+130 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.09 |
| ret | 3 | 0.91 | 0.82 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.29 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 126/78, thread 1055/228, cloth 73/129

## Self-diagnosis

- R1: beer slot dry: 0.0 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy none, home ask 3.74 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 9 @ 3.8 (ask 3.74, cap 5.7))
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.92; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1055 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
