# v2 shadow report

Turn 14086, 2026-11-17 07:00. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,977, prestige 3,638 (518 free, -2.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 17 | 4 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 5, buy @ 3.56 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 1, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 35 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 29 | 29 | 485 | 0 | 44 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.66 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.66 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 44 labour expired last turn (~80 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 485, not 584

## Prestige spending, cheapest coin per prestige first

315 turns left: prestige gained now converts 79.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 49.5 | 50.0 | needs a arena (build cost 29,393); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 54.3 | 54.3 | running |
| jousting 2 | arena | 210 | 54.2 | 54.8 | needs a arena (build cost 29,393); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 58.1 | 58.1 | thin at home: cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 61.4 | 61.4 | thin at home: wine, cured fish |
| hold banquet 1 (meat) | mansion | 4.2 | 62.0 | 62.0 |  |
| hold banquet 2 (meat) | mansion | 6.8 | 64.1 | 64.1 | thin at home: wine |
| hold banquet 4 (pies) | mansion | 18 | 64.7 | 64.7 | thin at home: hop beer, wine, stockfish |
| hold mass 2 (premium) | cathedral | 360 | 60.2 | 64.8 | needs a cathedral (build cost 324,420); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 2 (pies) | mansion | 7 | 64.9 | 64.9 | thin at home: wine |
| hold banquet 4 (premium) | mansion | 20 | 65.0 | 65.0 | thin at home: hop beer, wine, stockfish |
| hold banquet 3 (fish) | mansion | 7.6 | 67.9 | 67.9 | thin at home: hop beer, cured fish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: pasties buy 10 @ 16.0; crew 0.1; est +17 a turn; stock: pasties 10 @ 16.0 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 16.4 (keep 14); best orders clear only -9 a turn after crew: ship stays at 0
- best towns now: Amsdermund +696, Hofkirchen +486, Gotthafen +433, Bordees +381, Heidlowe +347
- Amsdermund would trade: furniture buy 64 @ 13.7; crew 1.0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~117 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.80 (93/turn) | timber 27 (8.4->12.35), firewood 35 (2.81->6.7), bread 161 (2.54->3.04), flour 2 (18.38->19.57) | dyed cloth 6 (16.38->17.48), garments 2 (27.09->29.4), glassware 1 (94.5->99.75), bricks 4 (11.13->13.11) | +255 |
| Kirchwerp | 1072 | 0.42 | 0.60 (70/turn) | honey 8 (8.77->11.69), thread 93 (5.1->5.7), leather 1 (23.1->32.3), lead ore 8 (7.82->10.45) | cloth 24 (7.98->11.4), flax fibres 23 (5.78->7.85), dyed cloth 7 (13.55->17.48), tools 15 (5.57->6.6) | +201 |
| Pontmont | 341 | 0.11 | 1.00 (117/turn) | firewood 26 (2.81->9.5), bread 84 (2.54->3.1), tiles 2 (3.89->9.59), honey 3 (8.77->11.4) | bricks 6 (9.35->13.11), cookware 3 (21->24.13), tools 7 (5.35->6.6), garments 1 (25.2->29.4) | +176 |
| Hofkirchen | 991 | 0.37 | 0.60 (70/turn) | leather 1 (23.1->26.79) | cloth 24 (8.66->11.4), flax fibres 23 (5.78->7.85), dyed cloth 7 (13.65->17.48), cookware 6 (20.79->24.13) | +158 |
| Amsdermund | 1111 | 0.44 | 0.30 (35/turn) | flour 2 (18.38->25.08), paper 6 (25.83->26.79), nets 3 (34.4->35.53) | cloth 24 (6.67->11.4), dyed cloth 7 (13.44->17.48), flax fibres 7 (5.78->7.85), garments 2 (27.09->29.4) | +158 |

**Best:** Grandgues at about +255 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 3.64, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 16, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 26.0) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 101, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.2) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 24.1k (cash + stock at home prices); -153/turn over 6 turns, -24/turn over 24 turns.
- Limits: cash flow >= -291/turn, prestige >= -0.91/turn (values are after 200 tax a turn).
- Today's settings: value +90/turn, cash +72/turn, prestige -2.80/turn - breaks the prestige floor.
- Plan: value +8/turn, cash +17/turn, prestige -0.91/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +164 vs +69, +101 vs +73, +160 vs +66.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Brunnham: +6/turn
  - ship Flax Wyrm -> Gosschweig: +0/turn
  - brewery 1 0.14 -> 0.08: +14/turn
  - spinnery 1 1.65 -> 1.39: +7/turn
  - net maker 0.00 -> 0.28: +1/turn
  - ropewalk 1 0.25 -> 0.32: -1/turn
  - flax farm 1 4.64 -> 4.32: -2/turn
  - sewing shop 1 0.30 -> 0.23: -20/turn
  - weavery 1 0.50 -> 0.37: -3/turn
  - mansion 1 0.00 -> 0.45: -82/turn
- Model check over the last 60 turns: predicted +52/turn for the settings we ran, real -3/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.38, garments 21.00, nets 32.95, beer 3.23, timber 3.51, prestige 63.34, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Brunnham (+6/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Gosschweig (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new leatherworks (make leather armour 1) for ~4364 coin: +6/turn, payback 764 turns, doesn't pay yet (materials thin at home: bricks, nails)

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

Buffers: flax fibres 85/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.66; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
