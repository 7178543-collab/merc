# v2 shadow report

Turn 13788, 2026-11-04 21:11. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 8,122, prestige 3,315 (195 free, -1.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 14 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.4 |
| grain | 33 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 529 | 0 | 0 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 10.90 x4, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Notes

- labour: projection runs 100 over real use lately; planning 530, not 630

## Prestige spending, cheapest coin per prestige first

613 turns left: prestige gained now converts 95.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.4 | 47.4 | running |
| hold banquet 4 (pies) | mansion | 18 | 51.1 | 51.1 | thin at home: hop beer, stockfish, pies |
| hold banquet 2 (pies) | mansion | 7 | 52.1 | 52.1 | thin at home: pies |
| hold banquet 2 (fish) | mansion | 6.8 | 52.5 | 52.5 |  |
| hold banquet 1 (fish) | mansion | 4.2 | 53.4 | 53.4 |  |
| jousting 3 | arena | 230 | 53.5 | 53.7 | needs a arena (build cost 26,598); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 53.9 | 53.9 | thin at home: hop beer, ham, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 55.0 | 55.0 | thin at home: hop beer, pies |
| hold banquet 4 (premium) | mansion | 20 | 55.3 | 55.3 | thin at home: hop beer, stockfish |
| hold banquet 3 (fish) | mansion | 7.6 | 56.4 | 56.4 | thin at home: hop beer |
| hold banquet 2 (meat) | mansion | 6.8 | 56.6 | 56.6 |  |
| jousting 2 | arena | 210 | 58.5 | 58.8 | needs a arena (build cost 26,598); thin at home: swords, protection, coats, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 9 | 134102075 | 0.072 | - | pasties 1 | -14 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: pasties buy 6 @ 14.5; crew 0.1; est +17 a turn; stock: pasties 6 @ 14.5 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 5 @ 14.8 (keep 14); best orders clear only 11 a turn after crew: ship stays at 0
- best towns now: Hofkirchen +28, Clairlond +23, Orlesailles +23, Friedwerp +19, Angefont +18
- Hofkirchen would trade: pasties buy 6 @ 12.6; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~98 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.30 (29/turn) | bread 151 (2.39->3.23), cured meat 17 (24.99->27.36), nets 4 (34.8->36.67), cured fish 7 (22.68->23.37) | arms 4 (30.24->32.11), tools 4 (4.81->5.61) | +176 |
| Fontaux | 411 | 0.11 | 0.50 (49/turn) | salt 17 (4.6->7.79), timber 19 (7.93->10.83), nets 6 (34.8->38.38), cheese 10 (5.99->7.55) | tools 18 (5.12->5.61), garments 2 (20.27->23.4), candles 1 (82.42->85) | +127 |
| Hanstein | 380 | 0.10 | 0.30 (29/turn) | timber 14 (7.93->10.64), garments 10 (18.2->18.43), firewood 1 (1.67->4.69), leather 1 (21.84->22.04) | thread 59 (4.03->4.54), flax fibres 22 (4.37->5.3), arms 4 (29.4->32.11), flax plants 72 (1.14->1.44) | +83 |
| Heilegg | 826 | 0.22 | 1.00 (98/turn) | nets 5 (34.8->38), medicine 0 (145.95->161.5), bread 125 (2.39->3.12), cheese 8 (5.99->6.41) | arms 3 (26.46->32.11), tools 15 (4.83->5.61), candles 0 (77.7->85), garments 1 (20.48->23.4) | +74 |
| Pontmont | 341 | 0.09 | 0.10 (10/turn) | cured fish 10 (22.68->25.08), raw cloth 12 (6.98->7.69), slaked lime 2 (11.55->14.54), flour 1 (16.7->21.66) | arms 4 (30.03->32.11), candles 1 (77.7->85), garments 2 (20.68->23.4), tools 18 (5.25->5.61) | +70 |

**Best:** Grandgues at about +176 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 16 @ min 3.06 | goal planner: sells 16 at 3.06 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 15.7, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.4 | goal planner: sells 11 at 19.4 (v2 had 10 at 22.8) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 30) |
| light armour | 1 @ 89, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.3/turn (observed), makes 0.0, holds 1 = 3.3 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 18.2k (cash + stock at home prices); -377/turn over 6 turns, -50/turn over 24 turns.
- Limits: cash flow >= -172/turn, prestige >= +4.36/turn (values are after 200 tax a turn).
- Today's settings: value +107/turn, cash +137/turn, prestige -1.38/turn - breaks the prestige floor.
- Plan: value -120/turn, cash -59/turn, prestige +2.82/turn - could not meet the prestige floor.
- Cash check (real vs predicted cash a tick, last 3): -117 vs +72, +150 vs +69, +168 vs +100.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Marmont: +9/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +6/turn
  - sewing shop 1 0.30 -> 0.36: -3/turn
  - weavery 1 0.50 -> 0.62: +6/turn
  - flax farm 1 4.64 -> 3.84: -8/turn
  - retting pit 1 0.91 -> 0.75: +6/turn
  - spinnery 1 1.65 -> 1.33: +3/turn
  - ropewalk 1 0.25 -> 0.00: -14/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.30: +15/turn
- HAND-OVER: goal planner: model check failed 3 runs in a row, sells handed back to the old rules.
- Model check over the last 59 turns: predicted +96/turn for the settings we ran, real +41/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.58, thread 3.97, cloth 6.34, flax fibres 4.70, garments 18.34, nets 28.62, beer 2.80, timber 3.40, prestige 10000.00, cash 0.00
- Orders it would set: beer sell 16 (v2 15); firewood buy 4 (v2 5); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 29 (v2 30); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.30, worth +15/turn.
- Ship linen snake: Grandgues -> Marmont (+13/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +79/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 480 (+191 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 5.90 |
| ret | 3 | 0.91 | 1.18 |
| spin | 4 | 1.65 | 2.08 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 345/228, cloth 73/128

## Self-diagnosis

- R1: arms slot dry: 0.0 held, 0.5 a turn (gear slot (+0.4 prestige)); our buy 1 @ 33.8, home ask none (no sellers at home)
