# v2 shadow report

Turn 13809, 2026-11-05 18:52. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,313, prestige 3,296 (176 free, -0.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 14 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.4 |
| grain | 33 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 525 | 0 | 4 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**1 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 525, not 618

## Prestige spending, cheapest coin per prestige first

592 turns left: prestige gained now converts 94.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.1 | 50.1 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 53.6 | 53.6 | thin at home: wine, cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 54.1 | 54.1 |  |
| jousting 3 | arena | 230 | 54.3 | 54.5 | needs a arena (build cost 26,388); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 54.8 | 54.8 | thin at home: hop beer, wine, ham, stockfish |
| hold banquet 2 (meat) | mansion | 6.8 | 55.7 | 55.7 | thin at home: wine, cheese |
| hold sermon 2 (candles) | church | 31 | 52.7 | 57.0 | needs a church (build cost 67,317); thin at home: jewellery, candles, furniture |
| hold prayer 2 | chapel | 13 | 52.6 | 57.1 | needs a chapel (build cost 31,560); thin at home: furniture |
| hold banquet 1 (meat) | mansion | 4.2 | 57.3 | 57.3 |  |
| hold banquet 4 | mansion | 17.5 | 57.3 | 57.3 | thin at home: wine, hop beer, ham, stockfish, cheese |
| hold banquet 2 (pies) | mansion | 7 | 57.4 | 57.4 | thin at home: wine, cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 58.4 | 58.4 | thin at home: hop beer, cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 16.1 (keep 14); best orders clear only -8 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 6 @ 15.4 (keep 14); best orders clear only 11 a turn after crew: ship stays at 0
- best towns now: Bedenis +90, Heilegg +60, Orlesailles +38, Fontaux +36, Fulkirch +33
- Bedenis would trade: pasties buy 14 @ 11.7; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~103 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.40 (41/turn) | charcoal 18 (2.16->6.98), timber 25 (6.93->9.97), cured fish 9 (22.68->24.51), limestone 4 (16.59->21.47) | cloth 5 (6.88->7.5), axes 1 (14.18->16.25), iron ore 1 (4.89->5.22) | +186 |
| Hanbrücken | 531 | 0.15 | 0.30 (31/turn) | garments 10 (19.9->22.04), charcoal 18 (2.16->3.84) | tapestries 1 (598.5->665), butter 1 (85.58->89.77), cloth 24 (7.3->7.5), potash 1 (14.6->15.67) | +102 |
| Angefont | 686 | 0.19 | 0.60 (62/turn) | charcoal 18 (2.16->4.6), limestone 4 (16.59->28.5), yarn 6 (4.22->6.27) | thread 62 (4.51->5.1), tapestries 1 (645.75->665), flax fibres 20 (4.83->5.5) | +94 |
| Pontmont | 341 | 0.09 | 0.30 (31/turn) | garments 10 (19.9->24.51), cured fish 9 (22.68->25.08), charcoal 18 (2.16->3.67), raw cloth 11 (7.09->7.69) | bricks 2 (5.25->7.6) | +90 |
| Essenbrucke | 584 | 0.16 | 0.10 (10/turn) | garments 10 (19.9->24.89), salt 6 (5.41->6.17), yarn 3 (4.22->5.27) | tar 3 (9.77->11.4), butter 1 (88.73->89.77), steel ingots 1 (18.06->19.38), wax 1 (22.47->23.75) | +60 |

**Best:** Grandgues at about +186 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.6, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 3.0 turns |
| beer |  | 16 @ min 3.06 | goal planner: sells 16 at 3.06 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| cloth |  | 2 @ min 7.05 | goal planner: sells 2 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 20.0) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 25) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 36.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 82.5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 21.0k (cash + stock at home prices); +189/turn over 6 turns, +143/turn over 24 turns.
- Limits: cash flow >= -263/turn, prestige >= +5.17/turn (values are after 200 tax a turn).
- Today's settings: value +94/turn, cash +96/turn, prestige -0.88/turn - breaks the prestige floor.
- Plan: value -132/turn, cash -128/turn, prestige +3.32/turn - could not meet the prestige floor.
- Cash check (real vs predicted cash a tick, last 3): +13 vs +101, +47 vs +108, -146 vs +105 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Bremcop: +0/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +3/turn
  - flax farm 1 4.64 -> 4.33: -0/turn
  - spinnery 1 1.65 -> 1.53: -1/turn
  - ropewalk 1 0.25 -> 0.00: -15/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.35: +17/turn
  - brewery 1 0.14 -> 0.27: -20/turn
  - mansion 1 0.00 -> 1.00: -213/turn
- Model check over the last 60 turns: predicted +97/turn for the settings we ran, real +71/turn.
- Worth of one more unit per turn: labour 1.67, thread 4.19, cloth 6.70, flax fibres 4.96, garments 19.38, nets 30.14, beer 2.88, timber 3.40, prestige 10000.00, cash 0.00
- Orders it would set: beer sell 16 (v2 15); cloth sell 2 (v2 none); firewood buy 4 (v2 5); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 29 (v2 25); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.35, worth +13/turn.
- Ship linen snake: Grandgues -> Bremcop (+5/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +84/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 486 (+197 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 6.02 |
| ret | 3 | 0.91 | 1.20 |
| spin | 4 | 1.65 | 2.13 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 319/228, cloth 73/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 5.5 for 3 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
