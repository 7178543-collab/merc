# v2 shadow report

Turn 14089, 2026-11-17 10:17. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,735, prestige 3,630 (510 free, -2.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 4 | 0 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 5, buy @ 3.56 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 35 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 29 | 29 | 496 | 0 | 33 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.70 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.70 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **labour**: 33 labour expired last turn (~59 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **arms**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 516, not 616
- labour expiry guard: 33 bought labour expired last turn, buy 0 (not 16) this turn

## Prestige spending, cheapest coin per prestige first

312 turns left: prestige gained now converts 79.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 50.2 | 50.7 | needs a arena (build cost 29,469); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 53.4 | 53.4 | running |
| jousting 2 | arena | 210 | 55.0 | 55.6 | needs a arena (build cost 29,469); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 58.8 | 58.8 | thin at home: cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 60.3 | 60.3 | thin at home: hop beer, cured fish |
| hold banquet 3 (pies) | mansion | 8 | 60.3 | 60.3 | thin at home: hop beer |
| hold banquet 1 (meat) | mansion | 4.2 | 62.0 | 62.0 |  |
| hold banquet 3 (meat) | mansion | 7.6 | 62.2 | 62.2 | thin at home: hop beer |
| hold mass 2 (premium) | cathedral | 360 | 59.8 | 64.5 | needs a cathedral (build cost 325,190); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |
| hold banquet 4 (premium) | mansion | 20 | 65.1 | 65.1 | thin at home: hop beer, wine, stockfish |
| hold banquet 4 (pies) | mansion | 18 | 65.7 | 65.7 | thin at home: hop beer, wine, stockfish |
| hold banquet 2 (fish) | mansion | 6.8 | 68.2 | 68.2 | thin at home: wine, cured fish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 11 | 151802239 | 0.132 | - | pasties 3 | -49 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 15.9 (keep 14); best orders clear only -2 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 8 @ 16.4 (keep 14); best orders clear only 9 a turn after crew: ship stays at 0
- best towns now: Amsdermund +674, Hofkirchen +525, Bordees +400, Chatgnan +369, Cobholme +304
- Amsdermund would trade: furniture buy 62 @ 13.7; crew 1.0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~114 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Fulkirch | 1576 | 0.71 | 0.40 (45/turn) | looms 1 (588->655.5), garments 10 (27.8->30.97), lathes 1 (192.15->218.5), nets 5 (34.8->36.48) | windows 1 (656.25->864.5), cloth 24 (9.13->11), candles 1 (81.38->89.5), dyed cloth 7 (13.97->15.58) | +359 |
| Hanstein | 380 | 0.12 | 0.60 (68/turn) | timber 35 (8.4->11.59), raw cloth 5 (11.55->12.54), dyed yarn 1 (5.1->5.84), tools 9 (6.88->7.12) | windows 1 (666.75->864.5), bricks 5 (7.56->12.82), cloth 24 (10.34->11), garments 2 (26.46->29.8) | +303 |
| Hofkirchen | 991 | 0.36 | 0.70 (80/turn) | lathes 1 (192.15->205.2) | cloth 24 (7.61->11), windows 1 (798->864.5), jewellery 7 (84->86.92), thread 20 (4.43->5.55) | +238 |
| Grandgues | 152 | 0.05 | 0.90 (102/turn) | firewood 35 (2.84->6.7), timber 23 (8.4->12.44), charcoal 19 (3.02->4.66), bread 160 (2.79->3.06) | candles 1 (84->89.5), wine 2 (7.25->9.5), beer 4 (3.36->3.72), medicine 1 (156.45->157.7) | +226 |
| Corstoft | 1496 | 0.66 | 0.20 (23/turn) | garments 10 (27.8->35.72) | windows 1 (771.75->864.5), medicine 1 (118.65->157.7), cloth 17 (9.5->11), candles 1 (86.1->89.5) | +222 |

**Best:** Fulkirch at about +359 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ ?, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 3.0 turns |
| beer | 9 @ 3.9, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 4 = 1.0 turns |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 15.5, stop 6 |  | uses 1.4/turn (household upkeep), makes 0.0, holds 11 = 7.7 turns |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 27.0) |
| grain | 0 @ 3.7, stop 18 |  | goal planner: buys 0 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 77.0) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.3/turn (ropewalk 1), makes 0.0, holds 1 = 2.3 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 24.5k (cash + stock at home prices); +149/turn over 6 turns, +130/turn over 24 turns.
- Limits: cash flow >= -281/turn, prestige >= -0.87/turn (values are after 200 tax a turn).
- Today's settings: value +92/turn, cash +74/turn, prestige -2.76/turn - breaks the prestige floor.
- Plan: value +14/turn, cash +20/turn, prestige -0.87/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -153 vs +72, -103 vs +79, +14 vs +89 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Amsdermund: +8/turn
  - ship Flax Wyrm -> Hofkirchen: +1/turn
  - brewery 1 0.14 -> 0.08: +13/turn
  - net maker 0.00 -> 0.28: +4/turn
  - spinnery 1 1.65 -> 1.57: +3/turn
  - flax farm 1 4.64 -> 4.79: -1/turn
  - weavery 1 0.50 -> 0.58: -7/turn
  - sewing shop 1 0.30 -> 0.36: +10/turn
  - mansion 1 0.00 -> 0.45: -104/turn
- Model check over the last 59 turns: predicted +78/turn for the settings we ran, real +12/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.78, thread 4.47, cloth 7.14, flax fibres 5.29, garments 20.66, nets 32.23, beer 3.18, timber 3.56, prestige 60.33, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 1 (v2 3); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Amsdermund (+9/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Hofkirchen (+1/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +89/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new leatherworks (make leather armour 1) for ~4310 coin: +6/turn, payback 690 turns, doesn't pay yet (materials thin at home: bricks, nails)

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

Buffers: flax fibres 90/77, thread 1050/228, cloth 73/128

## Self-diagnosis

- R1: beer slot dry: 4.4 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy 5 @ 3.56, home ask 3.72 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 9 @ 3.78 (ask 3.72, cap 5.7))
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.7; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
