# v2 shadow report

Turn 13783, 2026-11-04 16:43. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 7,408, prestige 3,321 (201 free, +99.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 15 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.4 |
| grain | 33 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 529 | 1 | 0 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**1 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 104 over real use lately; planning 530, not 630

## Prestige spending, cheapest coin per prestige first

618 turns left: prestige gained now converts 95.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.0 | 48.0 | running |
| hold banquet 4 (pies) | mansion | 18 | 52.2 | 52.2 | thin at home: pasties, hop beer, wine, stockfish, pies |
| hold banquet 1 (fish) | mansion | 4.2 | 53.5 | 53.5 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 54.4 | 54.4 | thin at home: wine, cheese |
| hold banquet 4 | mansion | 17.5 | 54.8 | 54.8 | thin at home: wine, hop beer, ham, stockfish, cheese |
| jousting 3 | arena | 230 | 54.7 | 54.9 | needs a arena (build cost 25,275); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 55.9 | 55.9 | thin at home: pasties, wine, cheese, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 56.4 | 56.4 | thin at home: hop beer, cheese |
| hold banquet 4 (premium) | mansion | 20 | 56.5 | 56.5 | thin at home: hop beer, wine, stockfish, premium cheese |
| hold banquet 3 (pies) | mansion | 8 | 56.7 | 56.7 | thin at home: pasties, hop beer, cheese, pies |
| hold banquet 2 (meat) | mansion | 6.8 | 59.8 | 59.8 | thin at home: wine, cheese |
| hold sermon 2 (candles) | church | 31 | 55.9 | 59.9 | needs a church (build cost 66,286); thin at home: candles, furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 10 | 151802239 | 0.052 | - | candles 2, pasties 3 | -202 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: candles 1 @ 78.0 (keep 12); stock: pasties 2 @ 14.1 (keep 14); best orders clear only 12 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: candles 1 @ 78.0 (keep 12); stock: pasties 2 @ 16.0 (keep 14); best orders clear only 8 a turn after crew: ship stays at 0
- best towns now: Clarfranche +19, Blanans +18, Boistot +16, Orlesailles +16, Gottweiler +16
- Clarfranche would trade: candles buy 1 @ 73.5, pasties buy 2 @ 12.5; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~98 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.40 (39/turn) | bread 152 (2.16->2.66), timber 25 (6.93->8.93), cured fish 7 (22.68->24.32), limestone 2 (16.59->21.47) | salt 4 (4.75->4.84) | +130 |
| Hanstein | 380 | 0.10 | 0.30 (30/turn) | timber 14 (6.93->10.54), grindstones 1 (243.6->252.7), garments 10 (18.31->18.9), firewood 1 (1.65->4.89) | thread 60 (4.14->5.05), premium cheese 6 (28.56->30.4), flax fibres 27 (5.3->5.75), beer 4 (2.94->3.34) | +109 |
| Kleinburgh | 1440 | 0.55 | 0.20 (20/turn) | premium ham 1 (252->281.2), dyed cloth 4 (10.82->14.34), gears 1 (54.08->56.05), nets 2 (34.8->35.91) | jewellery 3 (68.78->76.95), tapestries 1 (703.5->722), cookware 7 (19.11->21.85), furniture 1 (12.92->15.3) | +93 |
| Fontaux | 411 | 0.11 | 0.90 (89/turn) | timber 16 (6.93->10.45), wine 16 (5.83->7.74), bread 149 (2.16->2.58), firewood 1 (1.65->6.98) | thread 60 (4.73->5.05) | +92 |
| Dortgart | 1045 | 0.34 | 0.20 (20/turn) | grindstones 1 (243.6->290.7), garments 10 (18.31->20.33), nets 2 (34.8->35.72) | thread 20 (3.89->5.05), premium cheese 6 (29.4->30.4) | +75 |

**Best:** Grandgues at about +130 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 28.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 16 @ min 3.06 | goal planner: sells 16 at 3.06 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 76.0, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had 2) |
| cloth |  | 2 @ min 7.05 | goal planner: sells 2 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 1 @ min 1.27 | goal planner: sells 1 a turn at 1.27, keeps 219 (no one offered it) |
| furniture | 2 @ 15.7, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.4 | goal planner: sells 11 at 19.4 (v2 had 10 at 21.8) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 30) |
| light armour | 1 @ 92.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 79.0) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.3/turn (ropewalk 1), makes 0.0, holds 0 = 1.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 17.6k (cash + stock at home prices); -397/turn over 6 turns, -47/turn over 24 turns.
- Limits: cash flow >= -142/turn, prestige >= +4.13/turn (values are after 200 tax a turn).
- Today's settings: value +78/turn, cash +69/turn, prestige +98.99/turn.
- Plan: value +383/turn, cash +249/turn, prestige +90.99/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +202 vs +74, +72 vs +77, -117 vs +72.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Karlmoor: +7/turn
  - ship Flax Wyrm -> no route: +0/turn
  - park 1 16.00 -> 0.00: +46/turn
  - flax farm 1 4.64 -> 8.01: +20/turn
  - retting pit 1 0.91 -> 1.59: +29/turn
  - spinnery 1 1.65 -> 2.81: +85/turn
  - net maker [make nets 1] 0.00 -> 0.38: +32/turn
  - weavery 1 0.50 -> 0.68: +13/turn
  - sewing shop 1 0.30 -> 0.41: +41/turn
  - ropewalk 1 0.25 -> 0.00: -35/turn
- Model check over the last 60 turns: predicted +104/turn for the settings we ran, real +45/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 0.87, thread 2.19, cloth 3.49, flax fibres 2.61, garments 10.08, nets 16.35, beer 2.21, timber 2.99, prestige 0.00, cash 0.00
- Orders it would set: beer sell 16 (v2 15); cloth sell 2 (v2 none); firewood buy 4 (v2 5); flax plants sell 1 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 29 (v2 30); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 1.00, worth +38/turn.
- Recipe: net maker make nets 3 -> make nets 1 at 0.38, worth +23/turn.
- Ship linen snake: Grandgues -> Karlmoor (+7/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +43/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
- Trim: donate park 1: +96/turn (tax 96 saved).

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 478 (+189 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 5.86 |
| ret | 3 | 0.91 | 1.17 |
| spin | 4 | 1.65 | 2.07 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 355/228, cloth 73/128

## Self-diagnosis

Nothing found this run.
