# v2 shadow report

Turn 13982, 2026-11-12 23:54. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,481, prestige 3,518 (398 free, -2.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 16 | 9 | 4 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 26, buy 9, buy @ 3.76 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 17, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 511 | 0 | 18 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **labour**: 18 labour expired last turn (~31 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 511, not 611

## Prestige spending, cheapest coin per prestige first

419 turns left: prestige gained now converts 87.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.9 | 51.9 | running |
| hold banquet 4 (pies) | mansion | 18 | 55.4 | 55.4 | thin at home: hop beer, ham, stockfish, candles |
| jousting 3 | arena | 230 | 55.2 | 55.6 | needs a arena (build cost 28,181); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 58.2 | 58.2 | thin at home: hop beer, ham, stockfish, candles |
| hold banquet 1 (fish) | mansion | 4.2 | 58.3 | 58.3 |  |
| hold banquet 4 (premium) | mansion | 20 | 58.8 | 58.8 | thin at home: hop beer, ham, stockfish, candles |
| hold banquet 3 (pies) | mansion | 8 | 60.0 | 60.0 | thin at home: hop beer, pies, candles |
| hold banquet 2 (fish) | mansion | 6.8 | 60.7 | 60.7 |  |
| jousting 2 | arena | 210 | 60.5 | 60.8 | needs a arena (build cost 28,181); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 60.9 | 60.9 | thin at home: pies, candles |
| hold banquet 3 (fish) | mansion | 7.6 | 61.7 | 61.7 | thin at home: hop beer |
| hold prayer 2 | chapel | 13 | 55.4 | 63.0 | needs a chapel (build cost 35,598) |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 14.3 (keep 14); best orders clear only -6 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 5 @ 16.0 (keep 14); best orders clear only 4 a turn after crew: ship stays at 0
- best towns now: Orlesailles +33, Brunnham +25, Großmühle +25, Boistot +24, Clairlond +24
- Orlesailles would trade: pasties buy 6 @ 11.6; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~107 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.90 (96/turn) | timber 40 (8.66->11.59), bread 154 (2.52->2.94), firewood 31 (4.05->6.65), rope 1 (60.97->85.02) | cloth 10 (6.88->8), cured meat 3 (24.36->27.36), flour 1 (21->26.22), flax fibres 8 (6.77->7.3) | +268 |
| Fontaux | 411 | 0.12 | 0.80 (85/turn) | looms 1 (588->655.5), thread 78 (4.98->5.65), rope 1 (60.97->78.38), timber 37 (8.66->10.83) | cured meat 3 (24.78->27.36), tools 16 (5.15->5.61), flour 1 (24.15->26.22) | +179 |
| Heilegg | 826 | 0.24 | 0.40 (43/turn) | looms 1 (588->636.5), casks 14 (6.41->9.17), candles 1 (65.62->81.22), rope 1 (60.97->75.52) | cloth 24 (7.35->8), cured meat 3 (23.94->27.36), belts 2 (28.56->32.11), garments 2 (21.63->23.8) | +172 |
| Hanstein | 380 | 0.11 | 0.30 (32/turn) | looms 1 (588->660.25), rope 1 (60.97->76.95), candles 1 (65.62->75.52), timber 12 (8.66->10.73) | flax fibres 11 (5.83->7.3), coats 1 (70.88->80.75), seeds 18 (1.78->2.51), dyed cloth 8 (12.5->13.39) | +166 |
| Pontmont | 341 | 0.10 | 0.10 (11/turn) | looms 1 (588->669.75), rope 1 (60.97->86.45), candles 1 (65.62->78.85), bricks 4 (6.88->11.69) | dyed cloth 8 (11.76->13.39), cloth 18 (7.56->8), tools 16 (5.25->5.61), flour 1 (23.31->26.22) | +161 |

**Best:** Grandgues at about +268 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 6) |
| candles | 2 @ 64, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.14 | goal planner: sells 2 a turn at 1.14, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 20.6) |
| grain | 0 @ 3.7, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 35 |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 11) |
| light armour | 1 @ 109, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 35.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 70.5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.3k (cash + stock at home prices); -2/turn over 6 turns, +74/turn over 24 turns.
- Limits: cash flow >= -395/turn, prestige >= -0.41/turn (values are after 200 tax a turn).
- Today's settings: value +63/turn, cash +38/turn, prestige -2.20/turn - breaks the prestige floor.
- Plan: value -12/turn, cash +2/turn, prestige -0.41/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +56 vs +63, -97 vs +55, +215 vs +33.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Essenbrucke: +2/turn
  - ship Flax Wyrm -> no route: +0/turn
  - brewery 1 0.14 -> 0.00: +19/turn
  - ropewalk 1 0.25 -> 0.14: +13/turn
  - net maker 0.00 -> 0.29: +9/turn
  - flax farm 1 4.64 -> 4.16: -0/turn
  - retting pit 1 0.91 -> 0.83: -2/turn
  - brewery 1 [brew beer 2] 0.00 -> 0.07: -4/turn
  - spinnery 1 1.65 -> 1.32: -11/turn
  - mansion 1 0.00 -> 0.43: -99/turn
- Model check over the last 61 turns: predicted +105/turn for the settings we ran, real -9/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.96, garments 19.30, nets 30.16, beer 2.81, timber 3.42, prestige 71.29, cash 0.00
- Orders it would set: bread buy 5 (v2 6); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax plants sell 2 (v2 none); garments sell 11 (v2 10); labour buy 29 (v2 11); light armour buy 1 (v2 None)
- Recipe: brewery 1 brew beer 1 -> brew beer 2 at 0.07, worth +9/turn.
- Ship linen snake: Grandgues -> Essenbrucke (+2/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +82/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~2004 coin: +5/turn, payback 425 turns, doesn't pay yet

## Chain sizing

Mode HOLD, garments sold 10.7/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 410 (+121 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 3.63 |
| ret | 3 | 0.91 | 0.73 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 159/77, thread 1050/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
