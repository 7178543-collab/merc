# v2 shadow report

Turn 14250, 2026-11-24 03:32. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,430, prestige 3,697 (577 free, +1.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 40 | 0 | 19 | 0 | 0 | stop 116, buy 39, buy @ 3.82 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 12 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 7 | 7 | 7 | 2 | 0 | stop 25, buy 7, buy @ 3.7 |
| labour | 65 | 65 | 548 | 0 | 17 | buy 65, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **grain**: brewery 1 ran short of grain (buy is live (7 @ 3.7), 7 bought last turn); labour need rises ~18/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **grain**: only 0.8 turns of grain left and buying 7 (need 18) -> v2: buy 18

## Waste (money lost now)

- **labour**: 17 labour expired last turn (~29 coin): holding 65 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **cured meat**: home ask 31.20 is above our ceiling 29.00 and last turn bought 0 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **fish**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **hold banquet 2 (fish)**: hold banquet 2 (fish) costs 55.8 coin per prestige at mansion, vs 70.4 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch

## Notes

- labour: projection runs 115 over real use lately; planning 549, not 664

## Prestige spending, cheapest coin per prestige first

151 turns left: prestige gained now converts 53.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 47.7 | 48.8 | needs a arena (build cost 26,831); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 50.7 | 50.7 | running |
| jousting 2 | arena | 210 | 52.2 | 53.5 | needs a arena (build cost 26,831); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 55.8 | 55.8 |  |
| hold banquet 1 (fish) | mansion | 4.2 | 56.5 | 56.5 | thin at home: beer |
| hold banquet 2 (pies) | mansion | 7 | 60.5 | 60.5 |  |
| hold banquet 4 (pies) | mansion | 18 | 65.1 | 65.1 | thin at home: hop beer, stockfish |
| hold banquet 5 | mansion | 22 | 66.0 | 66.0 | thin at home: hop beer, stockfish, sculptures |
| hold banquet 2 (meat) | mansion | 6.8 | 66.7 | 66.7 |  |
| hold banquet 4 (premium) | mansion | 20 | 67.2 | 67.2 | thin at home: hop beer, stockfish, premium cheese |
| hold banquet 4 | mansion | 17.5 | 68.7 | 68.7 | thin at home: hop beer, stockfish |
| jousting 1 | arena | 170 | 67.1 | 68.7 | needs a arena (build cost 26,831); thin at home: protection, light armour, arms; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 10 | 151802239 | 0 | - | cured meat 6 | -142 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: beer sell 3 @ 4.9, cured meat buy 6 @ 25.0, pasties buy 3 @ 16.4; crew 0.1; est +37 a turn; stock: pasties 3 @ 16.4 (keep 14)
- **Flax Wyrm** on Caillechâtel: cured meat buy 3 @ 26.4, pasties buy 3 @ 13.8; crew 0.1; est +19 a turn; stock: pasties 3 @ 13.8 (keep 14)
- best towns now: Darmwald +57, Rotterburg +57, Donaunieder +54, Hofkirchen +42, Birkeningen +41
- Darmwald would trade: cured meat buy 6 @ 21.4, pasties buy 3 @ 16.1; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~107 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Rouhomme | 368 | 0.10 | 0.90 (96/turn) | nets 4 (15.43->35.91), grain 144 (2.94->3.69), garments 10 (29.8->35.91), bread 172 (2.6->3.23) | sculptures 1 (2394->2660), bricks 21 (5.41->9.88), cured meat 6 (26.25->31.2), tools 29 (5.93->6.89) | +717 |
| Pontmont | 341 | 0.10 | 0.70 (75/turn) | timber 40 (7.98->14.15), nets 4 (15.43->38.76), tiles 5 (3.19->7.69), furniture 8 (16.17->17.86) | tools 29 (5.78->6.89), bricks 12 (5.78->9.88), thread 35 (5.57->6.05), cured meat 6 (30.24->31.2) | +406 |
| Grandgues | 152 | 0.04 | 0.50 (54/turn) | nets 5 (15.43->41.42), bread 172 (2.6->3.21), garments 10 (29.8->33.63), charcoal 19 (2.33->3.72) | cured meat 6 (25.83->31.2), tools 10 (5.06->6.89), bricks 7 (7.4->9.88), casks 3 (4.87->5.84) | +390 |
| Kirchwerp | 1072 | 0.39 | 0.50 (54/turn) | nets 6 (15.43->37.81), canvas 6 (42->57), wine 23 (6.51->7.84), casks 10 (6.51->9.36) | cookware 5 (21->26.41), jewellery 3 (74.03->81.22), garments 2 (25.2->30), dyed cloth 2 (14.7->15.86) | +345 |
| Vauxvais | 204 | 0.06 | 0.40 (43/turn) | nets 6 (15.43->35.15), grain 99 (2.94->3.74), bread 157 (2.6->2.89), flour 1 (20.27->26.41) | tools 29 (5.46->6.89), cured meat 4 (23.73->31.2), bricks 5 (7.19->9.88), thread 15 (5.57->6.05) | +304 |

**Best:** Rouhomme at about +717 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 38 @ 4.3, stop 77 |  | uses 19.2/turn (household upkeep, mansion 1), makes 0.0, holds 40 = 2.1 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 89, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 9 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 19 = 3.2 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 6) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 15.8, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 30.0) |
| grain | 7 @ 3.7, stop 25 |  | goal planner: buys 7 a turn for today's rates, keeps up to 25 (v2 had 18) |
| labour | 65 @ 2.2, stop - |  | goal planner: buys 65 for today's rates (v2 had 49) |
| light armour | 1 @ 95, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.6) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 85.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 31.4k (cash + stock at home prices); -1/turn over 6 turns, +20/turn over 24 turns.
- Limits: cash flow >= -351/turn, prestige >= -1.15/turn (values are after 200 tax a turn).
- Today's settings: value -144/turn, cash -144/turn, prestige +1.32/turn.
- Plan: value +26/turn, cash +30/turn, prestige -1.15/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -369 vs -132, -243 vs -120, +24 vs -141.
- Route sales counted at most (what the ships really sold, a turn): beer 2.2, rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Rotterburg: +17/turn
  - ship Flax Wyrm -> Amsdermund: -0/turn
  - mansion 1 1.00 -> 0.41: +149/turn
  - spinnery 1 1.65 -> 1.42: -1/turn
  - retting pit 1 0.91 -> 0.83: +2/turn
  - flax farm 1 4.64 -> 4.17: +4/turn
  - sewing shop 1 0.30 -> 0.36: -9/turn
  - weavery 1 0.50 -> 0.60: +12/turn
- Model check over the last 58 turns: predicted -155/turn for the settings we ran, real +21/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.69, thread 4.24, cloth 6.78, flax fibres 5.03, garments 19.62, nets 16.98, beer 2.99, timber 3.42, prestige 62.20, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 6); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 7 (v2 18); labour buy 65 (v2 49); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Rotterburg (+5/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Amsdermund (+1/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +82/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new chandlery (make candles 2) for ~5281 coin: +16/turn, payback 337 turns, doesn't pay yet (materials thin at home: bricks, nails)

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 430 (+141 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.75 |
| ret | 3 | 0.91 | 0.95 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 87/77, thread 1050/228, cloth 72/128

## Self-diagnosis

- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
