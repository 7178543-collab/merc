# v2 shadow report

Turn 13836, 2026-11-06 21:37. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,963, prestige 3,394 (274 free, -1.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 27 | 0 | 4 | 0 | 0 | min_holding 60, sell 15, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 34 | 0 | 0 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 517 | 0 | 12 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **Flax Wyrm**: Flax Wyrm cost 10 coin last turn (crew 0.10) and its route traded nothing (route limited by pasties space) -> v2: pause it (crew 0) until a route is proven to sell

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 517, not 617

## Prestige spending, cheapest coin per prestige first

565 turns left: prestige gained now converts 94.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.8 | 49.8 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 53.9 | 53.9 |  |
| jousting 3 | arena | 230 | 54.2 | 54.5 | needs a arena (build cost 26,509); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 55.1 | 55.1 | thin at home: hop beer, cheese |
| hold banquet 3 (pies) | mansion | 8 | 55.2 | 55.2 | thin at home: hop beer, cheese, pies |
| hold banquet 4 (pies) | mansion | 18 | 55.5 | 55.5 | thin at home: hop beer, wine, ham, stockfish, cheese |
| hold banquet 3 (meat) | mansion | 7.6 | 58.2 | 58.2 | thin at home: hop beer, cheese |
| hold banquet 4 | mansion | 17.5 | 58.6 | 58.6 | thin at home: wine, hop beer, ham, stockfish, cheese |
| hold banquet 1 (meat) | mansion | 4.2 | 58.8 | 58.8 |  |
| hold banquet 4 (premium) | mansion | 20 | 59.7 | 59.7 | thin at home: hop beer, wine, ham, stockfish, premium cheese |
| jousting 2 | arena | 210 | 59.4 | 59.7 | needs a arena (build cost 26,509); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 60.3 | 60.3 | thin at home: wine, cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 10 | 134102075 | 0.132 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 10 | 151802239 | 0.168 | - | pasties 3 | -45 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: pasties buy 11 @ 15.4; crew 0.1; est +28 a turn; stock: pasties 11 @ 15.4 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 5 @ 15.6 (keep 14); best orders clear only 6 a turn after crew: ship stays at 0
- best towns now: Rouhomme +52, Bordetes +40, Chatgnan +34, Orlesailles +33, Bedenis +31
- Rouhomme would trade: pasties buy 11 @ 13.2; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~106 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Etallaen | 774 | 0.22 | 0.40 (42/turn) | beer 70 (3.46->5.37), grain 2 (2.54->3.44), nets 4 (32.2->32.87), wool 1 (6.51->8.07) | dyed cloth 14 (15.12->19.38), cloth 24 (9.45->10.1), gears 1 (64.58->71.72), garments 2 (26.67->27.2) | +181 |
| Rotterburg | 1056 | 0.37 | 0.20 (21/turn) | nets 4 (32.2->34.58), paper 2 (20.06->21.66), rope 1 (81.5->84.55), wool 1 (6.51->7.74) | dyed cloth 14 (13.55->19.38), cloth 24 (7.19->10.1), coats 1 (74.03->89.3), garments 2 (24.36->27.2) | +171 |
| Fontaux | 411 | 0.12 | 0.50 (53/turn) | timber 25 (7.35->11.88), thread 48 (4.26->5.65), glass ingots 1 (56.18->57.95), grain 2 (2.54->2.91) | dyed cloth 2 (13.86->19.38), cloth 7 (8.51->10.1), wine 3 (6.72->8.22), coats 1 (86.1->89.3) | +166 |
| Kirchwerp | 1072 | 0.38 | 0.50 (53/turn) | thread 48 (4.26->4.8), rope 1 (81.5->85.02), wool 1 (6.51->8.74), pies 1 (18.06->19.95) | dyed cloth 14 (13.65->19.38), cloth 24 (7.56->10.1), coats 1 (81.38->89.3), garments 2 (23.1->27.2) | +163 |
| Heilegg | 826 | 0.24 | 0.20 (21/turn) | nets 6 (32.2->35.15), jewellery 3 (80.85->82.17), glass ingots 1 (56.18->58.42), wool 1 (6.51->8.88) | dyed cloth 14 (14.7->19.38), cloth 24 (7.93->10.1), coats 1 (79.28->89.3), tools 15 (4.91->5.51) | +150 |

**Best:** Etallaen at about +181 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 3.46, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 27 = 6.5 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 75.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 16.6, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 26.2) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 17) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 79.5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.3/turn (ropewalk 1), makes 0.0, holds 1 = 1.9 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 21.4k (cash + stock at home prices); -515/turn over 6 turns, -7/turn over 24 turns.
- Limits: cash flow >= -248/turn, prestige >= +1.08/turn (values are after 200 tax a turn).
- Today's settings: value +73/turn, cash +61/turn, prestige -1.58/turn - breaks the prestige floor.
- Plan: value -41/turn, cash +82/turn, prestige +1.08/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +3 vs +80, +64 vs +68, -13 vs +64.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Karlmoor: +8/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +8/turn
  - ropewalk 1 0.25 -> 0.00: +5/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.09: +13/turn
  - weavery 1 0.50 -> 0.60: -9/turn
  - sewing shop 1 0.30 -> 0.36: +11/turn
  - brewery 1 0.14 -> 0.19: -12/turn
  - spinnery 1 1.65 -> 1.00: -14/turn
  - retting pit 1 0.91 -> 0.57: +3/turn
- Model check over the last 62 turns: predicted +98/turn for the settings we ran, real +24/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.58, thread 3.96, cloth 6.33, flax fibres 4.69, garments 18.30, nets 28.51, beer 2.94, timber 3.15, prestige 56.77, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 2 (v2 3); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 0); labour buy 29 (v2 17); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.09, worth +6/turn.
- Ship linen snake: Grandgues -> Karlmoor (+8/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +78/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 436 (+147 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.90 |
| ret | 3 | 0.91 | 0.98 |
| spin | 4 | 1.65 | 1.73 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 556/228, cloth 72/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask none (no sellers at home)
- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.05 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
