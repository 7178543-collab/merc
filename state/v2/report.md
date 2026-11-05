# v2 shadow report

Turn 13806, 2026-11-05 15:42. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,853, prestige 3,299 (179 free, -0.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 14 | 3 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.4 |
| grain | 33 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 525 | 0 | 4 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**1 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it

## Tuning

- **bread**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 525, not 625

## Prestige spending, cheapest coin per prestige first

595 turns left: prestige gained now converts 94.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.5 | 49.5 | running |
| jousting 3 | arena | 230 | 54.2 | 54.5 | needs a arena (build cost 27,684); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 55.1 | 55.1 | thin at home: wine, ham, stockfish, cheese, candles |
| hold prayer 2 | chapel | 13 | 51.4 | 56.2 | needs a chapel (build cost 33,198); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 52.2 | 56.7 | needs a church (build cost 70,333); thin at home: jewellery, candles, furniture |
| hold sermon 2 | church | 24 | 51.9 | 57.7 | needs a church (build cost 70,333); thin at home: jewellery, furniture |
| hold banquet 2 (pies) | mansion | 7 | 57.8 | 57.8 | thin at home: wine, cheese, candles |
| hold banquet 4 | mansion | 17.5 | 57.8 | 57.8 | thin at home: wine, ham, stockfish, cheese, candles |
| hold banquet 2 (meat) | mansion | 6.8 | 58.0 | 58.0 | thin at home: wine, cheese |
| hold banquet 1 (meat) | mansion | 4.2 | 58.2 | 58.2 |  |
| hold banquet 4 (premium) | mansion | 20 | 58.4 | 58.4 | thin at home: wine, ham, stockfish, candles, premium cheese |
| jousting 2 | arena | 210 | 59.4 | 59.6 | needs a arena (build cost 27,684); thin at home: swords, protection, coats, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 16.1 (keep 14); best orders clear only -7 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 5 @ 15.7 (keep 14); best orders clear only 6 a turn after crew: ship stays at 0
- best towns now: Disscester +33, Neuborn +30, Fulkirch +30, Friedwerp +29, Brunnham +27
- Disscester would trade: pasties buy 9 @ 13.0; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~101 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.50 (51/turn) | bread 153 (2.29->3.46), charcoal 18 (2.16->6.46), timber 24 (6.77->10.16), coats 1 (66.15->71.72) | malt 2 (6.51->7.08), salt 2 (5->5.56), slaked lime 1 (14.38->14.82), steel ingots 2 (19.11->19.38) | +305 |
| Blanans | 297 | 0.08 | 0.90 (91/turn) | looms 1 (630->665), timber 27 (6.77->8.74), coats 1 (66.15->73.62), rope 1 (83->88.35) | cured fish 5 (25.41->28.31), salt 3 (4.26->5.56), malt 2 (6.46->7.08), beer 4 (3.17->3.34) | +102 |
| Neuborn | 780 | 0.21 | 1.00 (101/turn) | timber 24 (6.77->10.83), arms 4 (32.76->37.62), furniture 10 (13.86->16.15), firewood 0 (1.66->8.31) | cured fish 4 (25.2->28.31), cloth 18 (7.04->7.5), cheese 3 (5.62->6.22), salt 3 (4.96->5.56) | +80 |
| Toqueque | 642 | 0.17 | 0.20 (20/turn) | looms 1 (630->684), coats 1 (66.15->77.42), casks 1 (5.46->5.84) | glass ingots 1 (56.7->59.38), salt 4 (5.19->5.56), bricks 5 (5.3->8.79), malt 2 (6.62->7.08) | +66 |
| Bedenis | 566 | 0.15 | 0.10 (10/turn) | coats 1 (66.15->73.62), nets 2 (37->40.28), rope 1 (83->85.97) | cured fish 5 (23.1->28.31), glass ingots 2 (47.88->59.38), salt 4 (4.98->5.56), canvas 1 (29.82->30.97) | +60 |

**Best:** Grandgues at about +305 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.6, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 4.0 turns |
| beer |  | 16 @ min 3.06 | goal planner: sells 16 at 3.06 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 16 = 3.9 turns |
| cloth |  | 2 @ min 7.05 | goal planner: sells 2 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.4 | goal planner: sells 11 at 19.4 (v2 had 10 at 20.0) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 25) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 36.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 81.0) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 1 = 3.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 20.7k (cash + stock at home prices); +146/turn over 6 turns, +141/turn over 24 turns.
- Limits: cash flow >= -244/turn, prestige >= +5.06/turn (values are after 200 tax a turn).
- Today's settings: value +96/turn, cash +100/turn, prestige -0.90/turn - breaks the prestige floor.
- Plan: value -136/turn, cash -127/turn, prestige +3.30/turn - could not meet the prestige floor.
- Cash check (real vs predicted cash a tick, last 3): +13 vs +101, +47 vs +108, -146 vs +105 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Dedlowe: +9/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +3/turn
  - ropewalk 1 0.25 -> 0.31: +2/turn
  - flax farm 1 4.64 -> 4.40: +0/turn
  - sewing shop 1 0.30 -> 0.36: -3/turn
  - weavery 1 0.50 -> 0.60: +5/turn
  - brewery 1 0.14 -> 0.27: -21/turn
  - mansion 1 0.00 -> 1.00: -219/turn
- Model check over the last 60 turns: predicted +97/turn for the settings we ran, real +67/turn.
- Worth of one more unit per turn: labour 1.65, thread 4.19, cloth 6.66, flax fibres 5.03, garments 19.24, nets 29.99, beer 2.92, timber 3.40, prestige 10000.00, cash 0.00
- Orders it would set: beer sell 16 (v2 15); candles buy 2 (v2 None); cloth sell 2 (v2 none); firewood buy 4 (v2 5); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 29 (v2 25); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Dedlowe (+9/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 484 (+195 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 5.98 |
| ret | 3 | 0.91 | 1.20 |
| spin | 4 | 1.65 | 2.11 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 327/228, cloth 73/128

## Self-diagnosis

Nothing found this run.
