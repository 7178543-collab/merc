# v2 shadow report

Turn 13905, 2026-11-09 18:33. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,016, prestige 3,493 (373 free, -1.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 10 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 33 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 529 | 0 | 0 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **labour**: buying 29, short of ~123 needed -> v2: buy 123
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Tuning

- **tar**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: +5 crew for Flax Wyrm (crew 0.10, no projection from the game)

## Prestige spending, cheapest coin per prestige first

496 turns left: prestige gained now converts 91.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.6 | 48.6 | running |
| hold banquet 4 (pies) | mansion | 18 | 55.1 | 55.1 | thin at home: hop beer, ham, stockfish, cheese |
| hold banquet 4 | mansion | 17.5 | 57.6 | 57.6 | thin at home: hop beer, ham, stockfish, cheese |
| hold banquet 4 (premium) | mansion | 20 | 57.6 | 57.6 | thin at home: hop beer, ham, stockfish |
| hold banquet 1 (fish) | mansion | 4.2 | 57.7 | 57.7 | thin at home: cured fish |
| jousting 3 | arena | 230 | 58.7 | 59.0 | needs a arena (build cost 26,356); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 59.6 | 59.6 | thin at home: cured fish, cheese |
| hold banquet 3 (pies) | mansion | 8 | 60.6 | 60.6 | thin at home: hop beer, cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 60.7 | 60.7 | thin at home: hop beer, cured fish, cheese |
| hold banquet 2 (pies) | mansion | 7 | 61.2 | 61.2 | thin at home: cheese |
| jousting 2 | arena | 210 | 64.3 | 64.6 | needs a arena (build cost 26,356); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 65.3 | 65.3 | thin at home: cured meat, cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 10 | 134102075 | 0 | - | furniture 2, pasties 2 | -54 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: furniture 1 @ 13.8 (keep 145); stock: pasties 2 @ 13.4 (keep 14); best orders clear only 13 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 16.0 (keep 14); best orders clear only 1 a turn after crew: ship stays at 0
- best towns now: Bedenis +39, Corstoft +31, Brebronn +30, Clairlond +27, Bremcop +26
- Bedenis would trade: furniture buy 1 @ 14.3, pasties buy 8 @ 14.2; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~105 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 1.00 (105/turn) | bread 154 (2.27->3.61), firewood 38 (2.73->6.46), timber 34 (8.51->11.21), charcoal 18 (1.95->4.94) | tools 9 (4.96->5.61), candles 1 (81.9->83), flax plants 6 (1.44->1.69) | +472 |
| Rouhomme | 368 | 0.10 | 1.00 (105/turn) | bread 81 (2.27->3.31), charcoal 9 (1.95->5.84), furniture 5 (12.5->15.2), firewood 20 (2.73->5.94) | thread 25 (4.73->5.25), tools 8 (4.85->5.61), cookware 3 (24.36->25.65), candles 0 (79.8->83) | +141 |
| Kirchwerp | 1072 | 0.38 | 0.80 (84/turn) | thread 79 (4.66->5.7), lead bars 5 (13.02->16.91), furniture 11 (12.5->15.2), chisels 3 (10.82->11.78) | cured meat 6 (21->26.22), cheese 5 (5.1->7.12), cloth 24 (9.5->9.95), garments 2 (24.36->25.6) | +131 |
| Hanstein | 380 | 0.11 | 0.50 (52/turn) | charcoal 18 (1.95->4.48), thread 65 (4.66->5.13), furniture 7 (12.5->16.15), timber 12 (8.51->11.59) | flax plants 22 (1.19->1.69), cloth 15 (9.66->9.95), rope 2 (72.98->74.58), candles 1 (81.9->83) | +122 |
| Fontaux | 411 | 0.12 | 1.00 (105/turn) | thread 39 (4.66->5.65), charcoal 8 (1.95->5.65), timber 11 (8.51->12.35), furniture 5 (12.5->16.34) | salt 5 (5.15->5.56), candles 0 (81.9->83), cloth 4 (9.71->9.95) | +120 |

**Best:** Grandgues at about +472 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 16 @ min 3.26 | goal planner: sells 16 at 3.26 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 7) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 12.2, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 24.2) |
| grain | 11 @ 3.7, stop 36 |  | uses 9.0/turn (brewery 1), makes 0.0, holds 33 = 3.7 turns |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 123) |
| light armour | 1 @ 105, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 37.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 26.0k (cash + stock at home prices); +164/turn over 6 turns, +192/turn over 24 turns.
- Limits: cash flow >= -292/turn, prestige >= -0.31/turn (values are after 200 tax a turn).
- Today's settings: value +100/turn, cash +95/turn, prestige -1.88/turn - breaks the prestige floor.
- Plan: value +15/turn, cash +17/turn, prestige -0.31/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +292 vs +74, +144 vs +88, +177 vs +92.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Corstoft: +3/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +8/turn
  - spinnery 1 1.65 -> 1.55: -1/turn
  - flax farm 1 4.64 -> 4.42: -1/turn
  - brewery 1 0.14 -> 0.00: -9/turn
  - brewery 1 [brew beer 2] 0.00 -> 0.17: +11/turn
  - weavery 1 0.50 -> 0.61: -10/turn
  - sewing shop 1 0.30 -> 0.36: +12/turn
  - ropewalk 1 0.25 -> 0.00: -11/turn
- Model check over the last 59 turns: predicted +103/turn for the settings we ran, real +60/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.62, thread 4.07, cloth 6.50, flax fibres 4.82, garments 18.81, nets 29.37, beer 3.26, timber 3.38, prestige 65.14, cash 0.00
- Orders it would set: beer sell 16 (v2 15); cloth sell 1 (v2 none); firewood buy 4 (v2 7); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); labour buy 29 (v2 123); light armour buy 1 (v2 None)
- Recipe: brewery 1 brew beer 1 -> brew beer 2 at 0.17, worth +15/turn.
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.27, worth +11/turn.
- Ship linen snake: Grandgues -> Corstoft (+7/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +81/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1993 coin: +2/turn, payback 878 turns, doesn't pay yet (materials thin at home: limestone)

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

Buffers: flax fibres 27/77, thread 897/228, cloth 73/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 5.95 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
