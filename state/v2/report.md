# v2 shadow report

Turn 14076, 2026-11-16 21:20. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,077, prestige 3,615 (495 free, -2.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 26 | 6 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 26, buy 9, buy @ 3.9 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 18, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 510 | 0 | 19 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.88 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.88 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 10.40 x6, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 19 labour expired last turn (~36 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Notes

- labour: projection runs 100 over real use lately; planning 510, not 608

## Prestige spending, cheapest coin per prestige first

325 turns left: prestige gained now converts 80.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 50.3 | 50.8 | needs a arena (build cost 28,522); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 55.5 | 55.5 | running |
| jousting 2 | arena | 210 | 55.1 | 55.6 | needs a arena (build cost 28,522); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 58.7 | 58.7 | thin at home: cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 60.0 | 60.0 | thin at home: cured fish |
| hold banquet 2 (pies) | mansion | 7 | 60.6 | 60.6 | thin at home: pies |
| hold banquet 1 (meat) | mansion | 4.2 | 62.3 | 62.3 |  |
| hold banquet 2 (meat) | mansion | 6.8 | 62.4 | 62.4 |  |
| hold mass 2 (premium) | cathedral | 360 | 61.4 | 65.7 | needs a cathedral (build cost 321,175); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 4 (premium) | mansion | 20 | 65.9 | 65.9 | thin at home: hop beer, stockfish |
| hold banquet 4 (pies) | mansion | 18 | 66.1 | 66.1 | thin at home: hop beer, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 68.2 | 68.2 | thin at home: hop beer, pies |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: candles buy 4 @ 78.0, pasties buy 3 @ 15.7; crew 0.1; est +46 a turn; stock: candles 4 @ 78.0 (keep 12); stock: pasties 3 @ 15.7 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 15.8 (keep 14); best orders clear only -8 a turn after crew: ship stays at 0
- best towns now: Brunnham +67, Orlesailles +63, Rotterburg +59, Fulkirch +58, Brebronn +58
- Brunnham would trade: candles buy 5 @ 76.5, pasties buy 3 @ 15.1; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~115 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.80 (92/turn) | timber 40 (8.35->12.35), firewood 32 (3.02->6.65), charcoal 19 (2.84->4.94), lead ore 2 (6.46->8.12) | dyed cloth 5 (14.7->17.95), bricks 1 (8.51->14.34), cloth 4 (9.19->9.85), beer 4 (3.36->3.54) | +254 |
| Amsdermund | 1111 | 0.44 | 0.30 (35/turn) | paper 7 (24.57->25.08) | cloth 24 (6.67->9.85), dyed cloth 10 (12.6->17.95), garments 2 (21.63->30), wax 4 (21.63->23.94) | +154 |
| Kirchwerp | 1072 | 0.41 | 0.30 (35/turn) | lead ore 9 (6.46->10.45), furniture 8 (16.91->19.95) | dyed cloth 10 (10.92->17.95), cloth 24 (7.98->9.85), ploughs 2 (73.5->83.12), garments 2 (27.3->30) | +151 |
| Pontmont | 341 | 0.10 | 1.00 (115/turn) | firewood 25 (3.02->9.5), bread 73 (2.69->3.27), charcoal 9 (2.84->4.16), raw cloth 0 (8.19->11.97) | cookware 1 (21->24.51), grindstones 0 (252->266), bricks 0 (8.98->14.34), thread 5 (5.35->5.6) | +129 |
| Vauxvais | 204 | 0.06 | 1.00 (115/turn) | firewood 49 (3.02->5.7), charcoal 17 (2.84->4.75), wax 10 (27.51->30.02), lead ore 3 (6.46->8.36) | dyed cloth 3 (15.44->17.95), garments 1 (26.46->30), spinning wheels 0 (218.4->224.2), flax fibres 5 (5.88->6.6) | +127 |

**Best:** Grandgues at about +254 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 31.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 3.7, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 26 = 6.2 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 9) |
| candles | 2 @ 76.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 7 = 4.7 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 16.5, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 28.4) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 10) |
| light armour | 1 @ 104, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 34.0 |  |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 24.1k (cash + stock at home prices); +214/turn over 6 turns, +21/turn over 24 turns.
- Limits: cash flow >= -253/turn, prestige >= -0.81/turn (values are after 200 tax a turn).
- Today's settings: value +96/turn, cash +85/turn, prestige -2.69/turn - breaks the prestige floor.
- Plan: value +21/turn, cash +29/turn, prestige -0.81/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -2 vs +76, +351 vs +81, +122 vs +84.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Hanbrücken: +12/turn
  - ship Flax Wyrm -> Unterhufe: +2/turn
  - brewery 1 0.14 -> 0.08: +15/turn
  - spinnery 1 1.65 -> 1.39: +7/turn
  - net maker 0.00 -> 0.28: +2/turn
  - flax farm 1 4.64 -> 4.37: -0/turn
  - ropewalk 1 0.25 -> 0.32: -1/turn
  - weavery 1 0.50 -> 0.37: -18/turn
  - sewing shop 1 0.30 -> 0.23: -5/turn
  - mansion 1 0.00 -> 0.45: -77/turn
- Model check over the last 60 turns: predicted +0/turn for the settings we ran, real -62/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.55, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.67, beer 3.38, timber 3.42, prestige 61.55, cash 0.00
- Orders it would set: bread buy 5 (v2 9); cloth sell 1 (v2 none); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 10); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Hanbrücken (+12/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Unterhufe (+2/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.4/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 425 (+136 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.48 |
| ret | 3 | 0.91 | 0.90 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 97/77, thread 1052/228, cloth 72/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.88; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1052 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
