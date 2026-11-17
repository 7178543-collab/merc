# v2 shadow report

Turn 14098, 2026-11-17 19:58. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,109, prestige 3,604 (484 free, -2.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 17 | 5 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 9, buy @ 3.8 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 18, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 511 | 0 | 18 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **labour**: 18 labour expired last turn (~33 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 511, not 611

## Prestige spending, cheapest coin per prestige first

303 turns left: prestige gained now converts 78.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 52.0 | 52.5 | needs a arena (build cost 29,079); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 54.6 | 54.6 | running |
| jousting 2 | arena | 210 | 56.9 | 57.5 | needs a arena (build cost 29,079); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 58.0 | 58.0 | thin at home: hop beer |
| hold banquet 1 (fish) | mansion | 4.2 | 59.0 | 59.0 | thin at home: cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 59.5 | 59.5 | thin at home: hop beer, cured fish, cheese |
| hold banquet 2 (pies) | mansion | 7 | 60.8 | 60.8 | thin at home: cheese |
| hold banquet 2 (fish) | mansion | 6.8 | 60.9 | 60.9 | thin at home: cured fish, cheese |
| hold banquet 3 (meat) | mansion | 7.6 | 61.2 | 61.2 | thin at home: hop beer, cheese |
| hold banquet 4 (premium) | mansion | 20 | 61.6 | 61.6 | thin at home: hop beer, stockfish, premium cheese, premium ham |
| hold banquet 1 (meat) | mansion | 4.2 | 62.1 | 62.1 |  |
| hold banquet 4 (pies) | mansion | 18 | 62.3 | 62.3 | thin at home: hop beer, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 15.0 (keep 14); best orders clear only -0 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Amsdermund +695, Gotthafen +458, Fulkirch +311, Clairlond +291, Donaunieder +249
- Amsdermund would trade: furniture buy 64 @ 13.7; crew 1.0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~117 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 1.00 (117/turn) | timber 31 (7.98->12.73), bread 162 (2.52->3.13), firewood 33 (2.96->5.7), charcoal 19 (2.94->4.46) | bricks 4 (8.4->11.88), tools 4 (4.85->5.79), beer 4 (3.51->3.74), candles 1 (84->85.5) | +329 |
| Amsdermund | 1111 | 0.45 | 0.40 (47/turn) | looms 1 (588->646), chisels 3 (12.81->17.1), wine 9 (7.77->9.5), nets 3 (34.2->36.29) | cloth 24 (6.67->11.7), candles 1 (78.75->85.5), dyed cloth 9 (13.65->14.72), garments 2 (26.25->29.2) | +222 |
| Angefont | 686 | 0.21 | 0.30 (35/turn) | charcoal 19 (2.94->5.61), acid 1 (113.4->119.7), lead bars 4 (11.23->11.59), rope 1 (81.5->82.65) | plate armour 1 (1239->1339.5), flax fibres 28 (5.25->7.3), cloth 13 (10.92->11.7), garments 2 (27.72->29.2) | +181 |
| Kirchwerp | 1072 | 0.42 | 0.70 (82/turn) | honey 8 (8.98->12.82), looms 1 (588->612.75), thread 91 (5.15->5.7), lead bars 7 (11.23->13.01) | cloth 24 (9.29->11.7), flax fibres 28 (5.62->7.3), belts 6 (32.55->34.77), tools 18 (5.02->5.79) | +180 |
| Rotterburg | 1056 | 0.41 | 0.20 (23/turn) | windows 1 (829.5->869.25), looms 1 (588->612.75), lead bars 7 (11.23->13.01), dyed yarn 2 (5.88->6.89) | cloth 24 (6.93->11.7), candles 1 (82.95->85.5), leather 1 (28.98->30.02), salt 6 (4.33->4.8) | +177 |

**Best:** Grandgues at about +329 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 3.92, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 25.8) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 11) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 79.5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 25.7k (cash + stock at home prices); +103/turn over 6 turns, +84/turn over 24 turns.
- Limits: cash flow >= -296/turn, prestige >= -0.77/turn (values are after 200 tax a turn).
- Today's settings: value +81/turn, cash +61/turn, prestige -2.63/turn - breaks the prestige floor.
- Plan: value +6/turn, cash +14/turn, prestige -0.77/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +227 vs +67, +230 vs +82, +104 vs +70.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Amsdermund: +7/turn
  - ship Flax Wyrm -> Großmühle: +2/turn
  - brewery 1 0.14 -> 0.08: +15/turn
  - spinnery 1 1.65 -> 1.38: +5/turn
  - net maker 0.00 -> 0.28: +1/turn
  - retting pit 1 0.91 -> 0.83: +1/turn
  - flax farm 1 4.64 -> 4.14: +4/turn
  - sewing shop 1 0.30 -> 0.25: -23/turn
  - weavery 1 0.50 -> 0.40: -6/turn
  - mansion 1 0.00 -> 0.44: -74/turn
- Model check over the last 60 turns: predicted +123/turn for the settings we ran, real +29/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.80, thread 4.57, cloth 7.27, flax fibres 5.48, garments 21.00, nets 32.76, beer 3.37, timber 3.94, prestige 60.90, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 1 (v2 3); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 11); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Amsdermund (+11/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Großmühle (+2/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 430 (+141 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.75 |
| ret | 3 | 0.91 | 0.95 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 83/77, thread 1050/228, cloth 72/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
