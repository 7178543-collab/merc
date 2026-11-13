# v2 shadow report

Turn 13985, 2026-11-13 02:06. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,757, prestige 3,511 (391 free, -2.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 3 | 0 | 4 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 2, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 29 | 29 | 508 | 0 | 21 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **beer**: needed (4.2/turn) but there is NO buy order, stock 3.0 -> v2: add buy 6
- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 4.02 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 4.02 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **labour**: 21 labour expired last turn (~37 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Notes

- labour: projection runs 100 over real use lately; planning 511, not 611

## Prestige spending, cheapest coin per prestige first

416 turns left: prestige gained now converts 87.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 52.5 | 52.5 | running |
| jousting 3 | arena | 230 | 55.2 | 55.5 | needs a arena (build cost 26,751); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 56.2 | 56.2 | thin at home: hop beer, wine, ham, stockfish, candles |
| hold banquet 1 (fish) | mansion | 4.2 | 56.9 | 56.9 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 58.8 | 58.8 | thin at home: wine |
| hold banquet 3 (fish) | mansion | 7.6 | 58.8 | 58.8 | thin at home: hop beer |
| hold banquet 3 (pies) | mansion | 8 | 58.8 | 58.8 | thin at home: hop beer, pies, candles |
| hold banquet 4 | mansion | 17.5 | 59.0 | 59.0 | thin at home: wine, hop beer, ham, stockfish, candles |
| hold banquet 4 (premium) | mansion | 20 | 59.6 | 59.6 | thin at home: hop beer, wine, ham, stockfish, candles |
| hold banquet 2 (pies) | mansion | 7 | 60.2 | 60.2 | thin at home: wine, pies, candles |
| jousting 2 | arena | 210 | 60.5 | 60.8 | needs a arena (build cost 26,751); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold mass 2 (premium) | cathedral | 360 | 62.7 | 65.4 | needs a cathedral (build cost 288,990); thin at home: furniture, jewellery, glassware, candles, premium garments |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: pasties buy 9 @ 15.0; crew 0.1; est +24 a turn; stock: pasties 9 @ 15.0 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 16.0 (keep 14); best orders clear only -2 a turn after crew: ship stays at 0
- best towns now: Etallaen +50, Clarfranche +46, Orlesailles +44, Großmühle +38, Boistot +35
- Etallaen would trade: pasties buy 9 @ 12.2; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~107 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.90 (97/turn) | timber 40 (7.88->11.97), firewood 30 (4.22->7.46), bread 157 (2.5->2.94), furniture 9 (12.08->14.34) | jewellery 2 (112.35->120.65), cloth 10 (6.88->7.85), tools 9 (4.87->5.56), flax fibres 8 (6.88->7.25) | +304 |
| Angefont | 686 | 0.20 | 0.90 (97/turn) | beer 118 (3.89->4.6), charcoal 19 (2.71->5.37), resin 8 (2.84->3.99), tackles 1 (168->173.85) | flax fibres 27 (5.25->7.25), looms 1 (666.75->693.5), dyed cloth 8 (11.45->13.77), tools 16 (4.91->5.56) | +175 |
| Disscester | 1474 | 0.62 | 0.20 (21/turn) | nets 4 (35.6->37.81), cheese 7 (6.3->7.41), tin ingots 1 (36.96->39.9), cloth 1 (7.75->8.55) | looms 1 (577.5->693.5), jewellery 2 (115.5->120.65), ploughs 1 (70.88->80.75) | +132 |
| Amsdermund | 1111 | 0.41 | 0.50 (54/turn) | cured fish 9 (24.57->28.88), chisels 10 (10.5->13.3), thread 42 (4.9->5.7), nets 6 (35.6->38) | dyed cloth 8 (10.71->13.77), jewellery 2 (110.25->120.65), cloth 24 (7.35->7.85), garments 2 (22.68->23.8) | +130 |
| Kirchwerp | 1072 | 0.39 | 0.70 (75/turn) | thread 89 (4.9->5.7), furniture 9 (12.08->17.1), chisels 10 (10.5->12.06), casks 10 (6.72->8.31) | dyed cloth 8 (10.71->13.77), tools 16 (5.02->5.56), garments 2 (22.68->23.8), jewellery 2 (119.7->120.65) | +125 |

**Best:** Grandgues at about +304 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 35.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 6 @ 3.88, stop 9 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 3 = 0.7 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 69.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 11.8, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 21.8) |
| grain | 5 @ 3.7, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 11) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 34.6) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 74.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.3k (cash + stock at home prices); -6/turn over 6 turns, +70/turn over 24 turns.
- Limits: cash flow >= -407/turn, prestige >= -0.38/turn (values are after 200 tax a turn).
- Today's settings: value +65/turn, cash +34/turn, prestige -2.17/turn - breaks the prestige floor.
- Plan: value -16/turn, cash -6/turn, prestige -0.38/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +56 vs +63, -97 vs +55, +215 vs +33.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Donaunieder: +5/turn
  - ship Flax Wyrm -> no route: +0/turn
  - brewery 1 0.14 -> 0.08: +14/turn
  - ropewalk 1 0.25 -> 0.16: +11/turn
  - net maker 0.00 -> 0.29: +7/turn
  - spinnery 1 1.65 -> 1.31: +5/turn
  - retting pit 1 0.91 -> 0.83: -3/turn
  - flax farm 1 4.64 -> 4.16: -6/turn
  - mansion 1 0.00 -> 0.42: -110/turn
- Model check over the last 61 turns: predicted +105/turn for the settings we ran, real -18/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.96, garments 19.30, nets 30.18, beer 3.21, timber 3.38, prestige 74.32, cash 0.00
- Orders it would set: candles buy 2 (v2 None); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 11); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Donaunieder (+5/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1808 coin: +6/turn, payback 290 turns, doesn't pay yet

## Chain sizing

Mode HOLD, garments sold 10.7/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 412 (+123 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 3.74 |
| ret | 3 | 0.91 | 0.75 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 151/78, thread 1050/228, cloth 73/128

## Self-diagnosis

- R1: beer slot dry: 3.0 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy none, home ask 3.7 -> **buy 9 @ 3.76 (ask 3.7, cap 5.7)** (ok)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 4.02; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
