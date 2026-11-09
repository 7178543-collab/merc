# v2 shadow report

Turn 13907, 2026-11-09 20:44. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,323, prestige 3,490 (370 free, -1.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 2 | 0 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 11 | 9 | 0 | 0 | stop 36, buy 10, buy @ 3.7 |
| labour | 29 | 29 | 518 | 0 | 11 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 518, not 600

## Prestige spending, cheapest coin per prestige first

494 turns left: prestige gained now converts 91.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.4 | 47.4 | running |
| hold banquet 4 (pies) | mansion | 18 | 54.4 | 54.4 | thin at home: pasties, hop beer, ham, stockfish |
| hold banquet 1 (fish) | mansion | 4.2 | 56.1 | 56.1 |  |
| hold banquet 4 | mansion | 17.5 | 56.7 | 56.7 | thin at home: hop beer, ham, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 57.0 | 57.0 | thin at home: hop beer, ham, stockfish |
| hold banquet 2 (fish) | mansion | 6.8 | 57.6 | 57.6 | thin at home: cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 57.8 | 57.8 | thin at home: hop beer, cheese |
| hold banquet 3 (pies) | mansion | 8 | 59.5 | 59.5 | thin at home: pasties, hop beer |
| jousting 3 | arena | 230 | 60.4 | 60.7 | needs a arena (build cost 25,740); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 60.9 | 60.9 | thin at home: pasties, cheese |
| hold banquet 3 (meat) | mansion | 7.6 | 64.4 | 64.4 | thin at home: hop beer, cheese |
| hold banquet 2 (meat) | mansion | 6.8 | 64.9 | 64.9 | thin at home: cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 16.0 (keep 14); best orders clear only 1 a turn after crew: ship stays at 0
- best towns now: Corstoft +48, Brebronn +46, Bremcop +37, Bedenis +36, Clarfranche +32
- Corstoft would trade: pasties buy 10 @ 12.0; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~102 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.60 (61/turn) | firewood 36 (2.67->7.41), cured fish 8 (22.68->30.02), charcoal 19 (2.44->4.94), mouldboards 1 (34.23->44.27) | coats 1 (92.92->100.7), tools 9 (4.94->5.46), candles 1 (81.9->82.5), tar 2 (10.61->11.4) | +263 |
| Rouhomme | 368 | 0.10 | 0.70 (72/turn) | bread 155 (2.27->3.25), charcoal 19 (2.44->6.32), cloth 1 (6.55->8.07), grain 2 (2.5->3.27) | tools 17 (4.85->5.46), coats 1 (94.5->100.7), cookware 4 (25.2->26.6), candles 1 (79.8->82.5) | +194 |
| Disscester | 1474 | 0.59 | 0.10 (10/turn) | garments 10 (24.8->34.58), cloth 1 (6.55->8.79), dyed cloth 3 (13.33->14.54), lead bars 1 (15.75->18.34) | coats 1 (87.15->100.7), candles 1 (79.28->82.5), salt 4 (4.56->5.56) | +117 |
| Hofkirchen | 991 | 0.32 | 0.20 (20/turn) | lead ore 5 (7.72->12.16), nails 4 (8.14->10.83), flax fibres 2 (6.1->10.16), glass ingots 1 (63->68.4) | cloth 18 (7.56->9.65), coats 1 (84.53->100.7), salt 16 (4.68->5.56), garments 2 (24.15->25.4) | +98 |
| Kleinburgh | 1440 | 0.57 | 0.20 (20/turn) | cured fish 8 (22.68->31.16), steel ingots 1 (15.12->17.48), cloth 1 (6.55->8.55) | coats 1 (78.75->100.7), salt 16 (4.43->5.56), cookware 4 (25.2->26.6) | +95 |

**Best:** Grandgues at about +263 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 16 @ min 3.26 | goal planner: sells 16 at 3.26 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 6.55 | goal planner: sells 1 a turn at 6.55, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 15.9, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 24.2) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 10) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 18) |
| light armour | 1 @ 105, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 37.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 27.3k (cash + stock at home prices); +391/turn over 6 turns, +226/turn over 24 turns.
- Limits: cash flow >= -305/turn, prestige >= -0.29/turn (values are after 200 tax a turn).
- Today's settings: value +95/turn, cash +87/turn, prestige -1.86/turn - breaks the prestige floor.
- Plan: value +14/turn, cash +17/turn, prestige -0.29/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +177 vs +92, +133 vs +95, +174 vs +106.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Corstoft: +3/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +9/turn
  - flax farm 1 4.64 -> 4.43: -1/turn
  - spinnery 1 1.65 -> 1.52: -1/turn
  - brewery 1 0.14 -> 0.20: -5/turn
  - ropewalk 1 0.25 -> 0.00: -7/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.24: +11/turn
  - weavery 1 0.50 -> 0.60: -10/turn
  - sewing shop 1 0.30 -> 0.36: +12/turn
- Model check over the last 59 turns: predicted +103/turn for the settings we ran, real +78/turn.
- Worth of one more unit per turn: labour 1.58, thread 3.97, cloth 6.34, flax fibres 4.71, garments 18.35, nets 28.67, beer 2.81, timber 3.38, prestige 63.49, cash 0.00
- Orders it would set: beer sell 16 (v2 15); cloth sell 1 (v2 none); firewood buy 4 (v2 8); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 10); labour buy 29 (v2 18); light armour buy 1 (v2 None); rope sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.24, worth +11/turn.
- Ship linen snake: Grandgues -> Corstoft (+7/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +79/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1695 coin: +2/turn, payback 829 turns, doesn't pay yet (materials thin at home: limestone)

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

Buffers: flax fibres 27/77, thread 920/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 2.2 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 4 @ 2.4, home ask none (no sellers at home)
- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.15 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
