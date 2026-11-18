# v2 shadow report

Turn 14120, 2026-11-18 17:30. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,159, prestige 3,596 (476 free, -2.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 17 | 4 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 9, buy @ 3.8 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 34 | 0 | 0 | 0 | 0 | stop 18, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 510 | 0 | 19 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.80 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.80 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 10.80 x20, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 19 labour expired last turn (~36 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **candles**: home ask 86.00 is above our ceiling 76.00 and last turn bought 0 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 510, not 601

## Prestige spending, cheapest coin per prestige first

281 turns left: prestige gained now converts 75.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 53.9 | 54.4 | needs a arena (build cost 27,042); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 58.2 | 58.2 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 58.9 | 58.9 |  |
| jousting 2 | arena | 210 | 59.0 | 59.6 | needs a arena (build cost 27,042); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold mass 2 (premium) | cathedral | 360 | 55.8 | 60.8 | needs a cathedral (build cost 293,600); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |
| hold banquet 2 (fish) | mansion | 6.8 | 62.7 | 62.7 | thin at home: cheese |
| hold banquet 1 (meat) | mansion | 4.2 | 63.0 | 63.0 |  |
| hold banquet 4 (premium) | mansion | 20 | 63.1 | 63.1 | thin at home: stockfish, premium ham |
| hold banquet 4 (pies) | mansion | 18 | 64.8 | 64.8 | thin at home: stockfish, cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 65.1 | 65.1 | thin at home: cheese |
| hold banquet 2 (meat) | mansion | 6.8 | 65.5 | 65.5 | thin at home: cheese |
| hold banquet 3 (pies) | mansion | 8 | 66.0 | 66.0 | thin at home: cheese, pies |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 12 | 151802239 | 0.04 | - | pasties 2 | -30 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: candles 1 @ 77.5 (keep 12); best orders clear only 0 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 16.0 (keep 14); best orders clear only -9 a turn after crew: ship stays at 0
- best towns now: Amsdermund +643, Hofkirchen +518, Gotthafen +443, Vauxvais +372, Chatgnan +281
- Amsdermund would trade: candles buy 5 @ 76.5, furniture buy 54 @ 13.7; crew 0.9

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~122 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Amsdermund | 1111 | 0.46 | 0.40 (49/turn) | jewellery 10 (96.6->104.5), tackles 3 (180.6->190), leather 1 (23.31->29.26), nets 3 (35.4->37.05) | cloth 24 (7.35->11), garments 2 (26.25->38), paper 6 (21->23.75), cheese 7 (6.62->8.74) | +267 |
| Grandgues | 152 | 0.05 | 0.70 (85/turn) | firewood 31 (2.94->6.89), timber 28 (8.66->11.97), charcoal 19 (2.48->5.46), jewellery 10 (96.6->98.8) | cloth 5 (10.24->11), candles 1 (85.05->86), premium ham 1 (285.6->286.9) | +257 |
| Hofkirchen | 991 | 0.38 | 0.40 (49/turn) | jewellery 10 (96.6->103.55), butter 2 (88.2->91.67), leather 1 (23.31->26.79), wine 1 (6.93->7.74) | cloth 24 (9.5->11), garments 2 (26.25->38), cheese 7 (5.78->8.74), flax fibres 28 (5.62->6.95) | +191 |
| Kirchwerp | 1072 | 0.44 | 0.30 (37/turn) | jewellery 10 (96.6->104.5), wine 26 (6.93->7.74), leather 1 (23.31->32.3), lead ore 2 (7.25->10.45) | garments 2 (28.14->38), cloth 17 (9.55->11), cheese 7 (6.2->8.74), cookware 3 (19.43->22.8) | +181 |
| Heilegg | 826 | 0.28 | 0.20 (24/turn) | jewellery 9 (96.6->102.6), nets 3 (35.4->39.33), wine 20 (6.93->7.5), leather 1 (23.31->27.55) | cloth 20 (8.56->11), garments 2 (28.77->38), cheese 7 (6.3->8.74), premium ham 1 (273->286.9) | +170 |

**Best:** Amsdermund at about +267 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 3.94, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 9) |
| candles | 2 @ 76.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 6 = 4.0 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 13.5, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 10 @ min 21 | goal planner: sells 10 at 21 (v2 had 10 at 36.8) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 10) |
| light armour | 1 @ 102, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 27.3k (cash + stock at home prices); +153/turn over 6 turns, +76/turn over 24 turns.
- Limits: cash flow >= -423/turn, prestige >= -0.73/turn (values are after 200 tax a turn).
- Today's settings: value +100/turn, cash +60/turn, prestige -2.59/turn - breaks the prestige floor.
- Plan: value +34/turn, cash +44/turn, prestige -0.73/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -0 vs +46, +447 vs +50, +183 vs +49.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Brunnham: +8/turn
  - ship Flax Wyrm -> no route: +0/turn
  - brewery 1 0.14 -> 0.08: +15/turn
  - spinnery 1 1.65 -> 1.42: +3/turn
  - retting pit 1 0.91 -> 0.80: +3/turn
  - net maker 0.00 -> 0.28: +2/turn
  - flax farm 1 4.64 -> 4.03: +6/turn
  - ropewalk 1 0.25 -> 0.32: -0/turn
  - sewing shop 1 0.30 -> 0.24: -19/turn
  - weavery 1 0.50 -> 0.39: -3/turn
- Model check over the last 60 turns: predicted +126/turn for the settings we ran, real +48/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.83, beer 3.37, timber 3.56, prestige 60.68, cash 0.00
- Orders it would set: bread buy 5 (v2 9); cloth sell 1 (v2 none); firewood buy 1 (v2 3); furniture buy 2 (v2 None); grain buy 5 (v2 0); labour buy 29 (v2 10); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Brunnham (+13/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +82/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 5.8/turn (+0.0 exported); plan makes 32.4 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 424 (+135 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.70 |
| ret | 3 | 0.91 | 0.94 |
| spin | 4 | 1.65 | 1.66 |
| weave | 3 | 0.50 | 1.26 |
| sew | 2 | 0.30 | 0.79 |

Buffers: flax fibres 72/77, thread 1061/226, cloth 72/126

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.8; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1061 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
- R7 stale ask: limestone ask 16.4 over the market for 6 turns: the town trades ~5 a turn at 14.7, we sold 0 with 46 over what we keep; floor 21.73 (config sell_floor / unit cost) is at or over the market: Taylor's call
