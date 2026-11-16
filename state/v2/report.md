# v2 shadow report

Turn 14072, 2026-11-16 17:21. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,467, prestige 3,626 (506 free, -2.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 14 | 9 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 26, buy 9, buy @ 3.9 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 18, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 508 | 0 | 21 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.70 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.70 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 10.30 x8, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 21 labour expired last turn (~39 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Notes

- labour: projection runs 100 over real use lately; planning 508, not 604

## Prestige spending, cheapest coin per prestige first

329 turns left: prestige gained now converts 80.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 49.7 | 50.1 | needs a arena (build cost 27,628); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| jousting 2 | arena | 210 | 54.4 | 54.9 | needs a arena (build cost 27,628); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 56.1 | 56.1 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 59.4 | 59.4 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 60.6 | 60.6 | thin at home: wine, cheese |
| hold banquet 2 (pies) | mansion | 7 | 61.7 | 61.7 | thin at home: wine, pies |
| hold banquet 2 (meat) | mansion | 6.8 | 63.0 | 63.0 | thin at home: wine, cheese |
| hold banquet 1 (meat) | mansion | 4.2 | 63.1 | 63.1 |  |
| hold banquet 4 (pies) | mansion | 18 | 64.5 | 64.5 | thin at home: hop beer, wine, stockfish |
| hold mass 2 (premium) | cathedral | 360 | 60.8 | 64.7 | needs a cathedral (build cost 298,390); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |
| hold banquet 4 (premium) | mansion | 20 | 65.0 | 65.0 | thin at home: hop beer, wine, stockfish, premium ham |
| hold banquet 3 (pies) | mansion | 8 | 66.1 | 66.1 | thin at home: hop beer, pies |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 13.2 (keep 14); best orders clear only -6 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 16.0 (keep 14); best orders clear only -1 a turn after crew: ship stays at 0
- best towns now: Brunnham +107, Gosschweig +95, Chribruck +93, Briclives +91, Bremcop +87
- Brunnham would trade: candles buy 8 @ 76.5, pasties buy 3 @ 15.1; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~115 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.80 (92/turn) | timber 33 (8.4->12.25), firewood 33 (2.84->6.51), charcoal 19 (3.21->5.22), limestone 3 (19.43->23.18) | garments 2 (24.99->30.6), cloth 4 (8.03->9.3), bricks 2 (7.56->10.64), dyed cloth 5 (14.91->15.58) | +246 |
| Pontmont | 341 | 0.10 | 1.00 (115/turn) | firewood 25 (2.84->9.5), bread 73 (2.62->3.25), jewellery 3 (101.33->107.35), charcoal 9 (3.21->4.64) | bellows 0 (279.3->285), garments 0 (28.98->30.6), candles 0 (81.9->84) | +150 |
| Amsdermund | 1111 | 0.44 | 0.40 (46/turn) | wine 4 (7.04->9.79), nets 3 (34.6->38), hides 1 (9.82->15.2), lead bars 3 (12.5->13.59) | cloth 24 (5.78->9.3), dyed cloth 7 (12.6->15.58), flax fibres 13 (5.78->7.65), tools 18 (4.83->5.75) | +150 |
| Vauxvais | 204 | 0.06 | 1.00 (115/turn) | firewood 49 (2.84->5.61), wax 10 (27.3->30.02), charcoal 17 (3.21->4.75), lead ore 3 (7.19->8.36) | dyed cloth 6 (13.76->15.58), garments 1 (25.2->30.6), flax fibres 5 (5.88->7.65), tools 16 (5.3->5.75) | +134 |
| Clairas | 374 | 0.12 | 0.70 (81/turn) | limestone 4 (19.43->31.73), tapestries 1 (771.75->793.25), timber 29 (8.4->10.26), lead bars 6 (12.5->13.11) | dyed cloth 7 (12.5->15.58), cloth 20 (8.51->9.3), garments 2 (23.52->30.6), flax fibres 5 (6.14->7.65) | +117 |

**Best:** Grandgues at about +246 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 6 @ 4.04, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 14 = 3.3 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 9) |
| candles | 2 @ 76.0, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had 3) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 15.8, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 29.2) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 8) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 34.0 |  |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 23.1k (cash + stock at home prices); +177/turn over 6 turns, -31/turn over 24 turns.
- Limits: cash flow >= -228/turn, prestige >= -0.86/turn (values are after 200 tax a turn).
- Today's settings: value +96/turn, cash +81/turn, prestige -2.74/turn - breaks the prestige floor.
- Plan: value +22/turn, cash +30/turn, prestige -0.86/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +266 vs +62, +416 vs +81, -2 vs +76.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Calange: +13/turn
  - ship Flax Wyrm -> Heidlowe: +0/turn
  - brewery 1 0.14 -> 0.08: +15/turn
  - spinnery 1 1.65 -> 1.37: +8/turn
  - net maker 0.00 -> 0.33: +3/turn
  - flax farm 1 4.64 -> 4.30: +0/turn
  - weavery 1 0.50 -> 0.38: -19/turn
  - sewing shop 1 0.30 -> 0.23: -8/turn
  - mansion 1 0.00 -> 0.45: -77/turn
- Model check over the last 60 turns: predicted -16/turn for the settings we ran, real -78/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.69, beer 3.36, timber 3.44, prestige 61.49, cash 0.00
- Orders it would set: bread buy 5 (v2 9); candles buy 2 (v2 3); cloth sell 1 (v2 none); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 8); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Calange (+13/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Heidlowe (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.6/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 423 (+134 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.35 |
| ret | 3 | 0.91 | 0.87 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 107/77, thread 1055/228, cloth 72/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.7; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1055 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
