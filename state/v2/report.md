# v2 shadow report

Turn 13909, 2026-11-09 22:36. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,460, prestige 3,486 (366 free, -2.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 52 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 14, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
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

492 turns left: prestige gained now converts 91.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.1 | 47.1 | running |
| hold banquet 4 (pies) | mansion | 18 | 54.6 | 54.6 | thin at home: hop beer, ham, stockfish, cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 55.2 | 55.2 | thin at home: beer |
| hold banquet 4 | mansion | 17.5 | 57.0 | 57.0 | thin at home: hop beer, ham, stockfish, cheese |
| hold banquet 4 (premium) | mansion | 20 | 57.0 | 57.0 | thin at home: hop beer, ham, stockfish |
| hold banquet 2 (fish) | mansion | 6.8 | 58.0 | 58.0 | thin at home: cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 58.8 | 58.8 | thin at home: hop beer, cheese |
| jousting 3 | arena | 230 | 59.5 | 59.7 | needs a arena (build cost 25,098); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 60.6 | 60.6 | thin at home: pasties, hop beer, cheese |
| hold banquet 2 (pies) | mansion | 7 | 61.9 | 61.9 | thin at home: pasties, cheese |
| hold banquet 1 (meat) | mansion | 4.2 | 63.9 | 63.9 | thin at home: beer |
| hold feast 2 | townhouse | 2.6 | 57.8 | 64.5 | needs a townhouse (build cost 8,100) |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: beer buy 4 @ 3.2, pasties buy 7 @ 13.6; crew 0.1; est +30 a turn; stock: pasties 7 @ 13.6 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 16.0 (keep 14); best orders clear only -1 a turn after crew: ship stays at 0
- best towns now: Corstoft +54, Bremcop +52, Toqueque +46, Clarfranche +34, Helmgreen +34
- Corstoft would trade: pasties buy 12 @ 11.9; crew 0.3

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~101 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.80 (81/turn) | firewood 34 (2.84->6.46), charcoal 19 (2.44->5.37), cured fish 7 (24.57->26.6), timber 24 (8.66->9.59) | tools 9 (4.89->5.75), candles 1 (80.33->86), flour 2 (21.84->24.13), cheese 4 (7.3->7.5) | +178 |
| Fontaux | 411 | 0.11 | 1.00 (101/turn) | thread 44 (5.5->7.27), timber 11 (8.66->12.54), charcoal 8 (2.44->5.56), salt 5 (6.25->7.79) | looms 0 (551.25->593.75), mouldboards 0 (35.49->45.03), candles 0 (80.85->86), seeds 2 (2.56->2.94) | +176 |
| Angefont | 686 | 0.18 | 0.40 (40/turn) | charcoal 18 (2.44->5.89), resin 7 (2.46->3.29), hinges 1 (48.93->50.82), cloth 1 (6.43->7.6) | flax fibres 27 (4.73->6.3), cloth 18 (8.61->9.25), tools 20 (5.17->5.75), seeds 8 (1.78->2.94) | +108 |
| Bedenis | 566 | 0.15 | 0.10 (10/turn) | lead ore 10 (7.4->10.73), glass ingots 1 (63->66.5), cloth 1 (6.43->8.55), copper ingots 1 (14.6->15.48) | looms 1 (530.25->593.75), mouldboards 1 (36.12->45.03), seeds 3 (1.94->2.94), candles 1 (84.53->86) | +108 |
| Brebronn | 862 | 0.25 | 0.20 (20/turn) | bellows 2 (268.8->285), garments 10 (23.4->24.7) | looms 1 (556.5->593.75), tools 20 (4.77->5.75), candles 1 (79.28->86), belts 4 (33.18->34.39) | +100 |

**Best:** Grandgues at about +178 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 16 @ min 3.26 | goal planner: sells 16 a turn at 3.26, keeps 60 (no one offered it) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 16.6, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 22.8) |
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
- Value now 27.9k (cash + stock at home prices); +326/turn over 6 turns, +223/turn over 24 turns.
- Limits: cash flow >= -311/turn, prestige >= -0.27/turn (values are after 200 tax a turn).
- Today's settings: value +92/turn, cash +76/turn, prestige -2.04/turn - breaks the prestige floor.
- Plan: value +7/turn, cash +10/turn, prestige -0.27/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +174 vs +106, -4 vs +87, +140 vs +76.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Gosschweig: +0/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +8/turn
  - flax farm 1 4.64 -> 5.43: -5/turn
  - retting pit 1 0.91 -> 1.06: -0/turn
  - spinnery 1 1.65 -> 1.87: +5/turn
  - brewery 1 0.14 -> 0.20: -7/turn
  - weavery 1 0.50 -> 0.60: -9/turn
  - sewing shop 1 0.30 -> 0.36: +14/turn
  - ropewalk 1 0.25 -> 0.00: -15/turn
- Model check over the last 59 turns: predicted +103/turn for the settings we ran, real +83/turn.
- Worth of one more unit per turn: labour 1.57, thread 3.94, cloth 6.30, flax fibres 4.68, garments 18.23, nets 28.60, beer 2.80, timber 3.38, prestige 61.66, cash 0.00
- Orders it would set: beer sell 16 (v2 none); cloth sell 1 (v2 none); firewood buy 2 (v2 3); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None); rope sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.19, worth +10/turn.
- Ship linen snake: Grandgues -> Gosschweig (+2/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +78/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1626 coin: +1/turn, payback 1272 turns, doesn't pay yet (materials thin at home: limestone)

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

Buffers: flax fibres 27/77, thread 942/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask none (no sellers at home)
- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.3 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
