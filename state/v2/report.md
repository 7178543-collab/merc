# v2 shadow report

Turn 13908, 2026-11-09 21:50. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,320, prestige 3,488 (368 free, -2.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 57 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 2 | 1 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 9 | 0 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 500 | 0 | 29 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (4 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 29 labour expired last turn (~45 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 500, not 600

## Prestige spending, cheapest coin per prestige first

493 turns left: prestige gained now converts 91.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.1 | 47.1 | running |
| hold banquet 4 (pies) | mansion | 18 | 54.0 | 54.0 | thin at home: hop beer, ham, stockfish, cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 54.2 | 54.2 | thin at home: beer |
| hold banquet 2 (fish) | mansion | 6.8 | 55.9 | 55.9 | thin at home: cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 55.9 | 55.9 | thin at home: hop beer, cheese |
| hold banquet 4 | mansion | 17.5 | 55.9 | 55.9 | thin at home: hop beer, ham, stockfish, cheese |
| hold banquet 4 (premium) | mansion | 20 | 56.2 | 56.2 | thin at home: hop beer, ham, stockfish |
| jousting 3 | arena | 230 | 60.0 | 60.3 | needs a arena (build cost 25,232); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 60.8 | 60.8 | thin at home: hop beer, cheese |
| hold banquet 2 (pies) | mansion | 7 | 63.0 | 63.0 | thin at home: cheese |
| hold banquet 3 (meat) | mansion | 7.6 | 63.2 | 63.2 | thin at home: hop beer, cheese |
| hold banquet 2 (meat) | mansion | 6.8 | 64.2 | 64.2 | thin at home: cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 13.8 (keep 14); best orders clear only 10 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 7 @ 16.0 (keep 14); best orders clear only 10 a turn after crew: ship stays at 0
- best towns now: Clarfranche +39, Bedenis +36, Essenbrucke +33, Rotterburg +28, Brunnham +26
- Clarfranche would trade: pasties buy 11 @ 13.5; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~102 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Fontaux | 411 | 0.11 | 0.80 (81/turn) | thread 85 (5.5->7.27), charcoal 17 (2.54->5.65), bread 148 (2.25->2.83), salt 11 (6.2->7.79) | belts 2 (35.07->37.05), candles 1 (80.85->81.5) | +239 |
| Rouhomme | 368 | 0.10 | 0.70 (71/turn) | bread 155 (2.25->3.19), charcoal 19 (2.54->6.13), cloth 1 (6.46->7.89), grain 2 (2.5->3.29) | tools 17 (4.85->5.51), cloth 15 (9.08->9.65), candles 1 (79.8->81.5), casks 3 (6.09->6.65) | +176 |
| Darmwald | 1022 | 0.34 | 0.30 (31/turn) | garments 10 (24.6->32.87), dyed cloth 4 (13.02->14.91), cloth 1 (6.46->9.88), lead ore 1 (6.88->11.59) | salt 9 (4.28->5.56) | +94 |
| Etallaen | 774 | 0.21 | 1.00 (102/turn) | bread 110 (2.25->3.48), charcoal 13 (2.54->4.58), wine 5 (6.35->6.98), lead ore 0 (6.88->10.36) | canvas 0 (32.55->36.67), cloth 2 (8.56->9.65), thread 8 (4.73->5.22), candles 0 (79.8->81.5) | +84 |
| Neuborn | 780 | 0.21 | 1.00 (102/turn) | bread 110 (2.25->3.27), charcoal 13 (2.54->5.18), wine 9 (6.35->7.69), nets 3 (38.8->40.85) | tar 4 (10.45->11.4), cloth 4 (9.19->9.65), thread 6 (4.81->5.22), garments 1 (24.36->24.8) | +84 |

**Best:** Fontaux at about +239 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 14 |  | goal planner: buys 4 a turn for today's rates, keeps up to 14 (v2 had 7) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 15.9, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.0) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 110, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 37.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 27.6k (cash + stock at home prices); +361/turn over 6 turns, +213/turn over 24 turns.
- Limits: cash flow >= -305/turn, prestige >= -0.28/turn (values are after 200 tax a turn).
- Today's settings: value +88/turn, cash +76/turn, prestige -1.97/turn - breaks the prestige floor.
- Plan: value +3/turn, cash +7/turn, prestige -0.28/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +133 vs +95, +174 vs +106, -4 vs +87.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Corstoft: +3/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +9/turn
  - flax farm 1 4.64 -> 5.38: -5/turn
  - retting pit 1 0.91 -> 1.05: -0/turn
  - spinnery 1 1.65 -> 1.86: +3/turn
  - brewery 1 0.14 -> 0.21: -6/turn
  - weavery 1 0.50 -> 0.60: -6/turn
  - sewing shop 1 0.30 -> 0.36: +12/turn
  - ropewalk 1 0.25 -> 0.00: -20/turn
- Model check over the last 59 turns: predicted +103/turn for the settings we ran, real +81/turn.
- Worth of one more unit per turn: labour 1.57, thread 3.95, cloth 6.30, flax fibres 4.68, garments 18.23, nets 28.57, beer 2.79, timber 3.38, prestige 62.49, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 4 (v2 7); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None); rope sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.22, worth +11/turn.
- Ship linen snake: Grandgues -> Corstoft (+5/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +79/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1614 coin: +2/turn, payback 951 turns, doesn't pay yet (materials thin at home: limestone)

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

Buffers: flax fibres 27/77, thread 931/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 4 @ 2.4, home ask none (no sellers at home)
- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.2 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
