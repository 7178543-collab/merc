# v2 shadow report

Turn 13846, 2026-11-07 07:38. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,919, prestige 3,379 (259 free, -1.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 3 | 0 | 4 | 0 | 0 | min_holding 60, sell 8, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 34 | 0 | 0 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 507 | 0 | 22 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **beer**: needed (4.2/turn) but there is NO buy order, stock 3.4 -> v2: add buy 6
- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **labour**: 22 labour expired last turn (~35 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 507, not 607

## Prestige spending, cheapest coin per prestige first

555 turns left: prestige gained now converts 93.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.2 | 49.2 | running |
| hold banquet 4 (pies) | mansion | 18 | 53.2 | 53.2 | thin at home: wine, ham, stockfish, cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 53.7 | 53.7 |  |
| jousting 3 | arena | 230 | 53.8 | 54.0 | needs a arena (build cost 26,959); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 56.2 | 56.2 | thin at home: pasties, cheese |
| hold banquet 4 | mansion | 17.5 | 56.6 | 56.6 | thin at home: wine, ham, stockfish, cheese |
| hold banquet 4 (premium) | mansion | 20 | 57.3 | 57.3 | thin at home: wine, ham, stockfish |
| hold banquet 2 (fish) | mansion | 6.8 | 57.4 | 57.4 | thin at home: wine, cheese |
| hold banquet 2 (pies) | mansion | 7 | 57.4 | 57.4 | thin at home: pasties, wine, cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 58.1 | 58.1 | thin at home: cheese |
| hold banquet 1 (meat) | mansion | 4.2 | 59.2 | 59.2 |  |
| jousting 2 | arena | 210 | 58.9 | 59.2 | needs a arena (build cost 26,959); thin at home: swords, protection, coats, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 6 @ 15.9 (keep 14); best orders clear only 8 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 6 @ 15.7 (keep 14); best orders clear only 9 a turn after crew: ship stays at 0
- best towns now: Bedenis +21, Rouhomme +20, Bremcop +18, Boistot +17, Kleinburgh +17
- Bedenis would trade: pasties buy 6 @ 13.7; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~103 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.33 | 0.80 (82/turn) | beer 101 (3.46->5.37), bellows 1 (273->340.1), lead bars 9 (19.53->20.71), wine 5 (6.04->7.27) | cheese 9 (5.78->8.12), thread 29 (4.83->5.35), slaked lime 2 (7.25->10.83), flax fibres 27 (5.17->5.95) | +246 |
| Grandgues | 152 | 0.04 | 0.30 (31/turn) | beer 101 (3.46->4.52), cured fish 10 (24.15->26.98), timber 28 (7.14->8.5), nets 2 (33.2->35.72) | cheese 9 (6.67->8.12), dyed cloth 9 (10.08->10.83), candles 1 (81.9->83.5), thread 16 (5.17->5.35) | +182 |
| Kirchwerp | 1072 | 0.37 | 0.30 (31/turn) | garments 10 (24.2->28.88), thread 47 (4.66->5.7), casks 6 (6.56->8.31), lead bars 5 (19.53->20.9) | cheese 9 (6.2->8.12), ham 1 (108.15->114), blades 1 (13.76->14.63), flax fibres 27 (5.17->5.95) | +110 |
| Fontaux | 411 | 0.11 | 0.70 (72/turn) | timber 27 (7.14->11.59), beer 55 (3.46->3.84), flax fibres 2 (5.3->7.17), cloth 1 (8.65->9.4) | cheese 9 (7.35->8.12), candles 1 (78.75->83.5), lead bars 1 (16.28->16.43) | +90 |
| Etallaen | 774 | 0.21 | 0.40 (41/turn) | cured fish 10 (24.15->26.6), cured meat 4 (24.78->28.5), grain 2 (2.56->3.8), fleece 1 (8.19->9.03) | bellows 1 (178.5->214.7), candles 1 (78.75->83.5), thread 13 (4.73->5.35), cheese 9 (7.61->8.12) | +90 |

**Best:** Hofkirchen at about +246 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 29.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 6 @ 3.46, stop 9 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 3 = 0.8 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 12.8, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.6) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 7) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 78.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 22.3k (cash + stock at home prices); +97/turn over 6 turns, -41/turn over 24 turns.
- Limits: cash flow >= -288/turn, prestige >= +1.72/turn (values are after 200 tax a turn).
- Today's settings: value +79/turn, cash +70/turn, prestige -1.50/turn - breaks the prestige floor.
- Plan: value -81/turn, cash -68/turn, prestige +1.72/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +100 vs +46, +150 vs +60, +19 vs +56.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Bremcop: +2/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +8/turn
  - flax farm 1 4.64 -> 4.35: -0/turn
  - spinnery 1 1.65 -> 1.55: -1/turn
  - sewing shop 1 0.30 -> 0.36: -9/turn
  - weavery 1 0.50 -> 0.60: +11/turn
  - mansion 1 0.00 -> 0.77: -173/turn
- Model check over the last 61 turns: predicted +97/turn for the settings we ran, real +73/turn.
- Worth of one more unit per turn: labour 1.64, thread 4.16, cloth 6.62, flax fibres 5.00, garments 19.12, nets 29.77, beer 2.90, timber 3.06, prestige 57.73, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 2 (v2 3); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 0); labour buy 29 (v2 7); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Bremcop (+6/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +82/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 436 (+147 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.91 |
| ret | 3 | 0.91 | 0.98 |
| spin | 4 | 1.65 | 1.73 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 555/228, cloth 72/128

## Self-diagnosis

- R1: beer slot dry: 3.4 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy none, home ask 3.3 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 9 @ 3.36 (ask 3.3, cap 5.7))
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask none (no sellers at home)
- R5: flax fibres buy not filling: bid 5.05 under the home ask 5.95 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
