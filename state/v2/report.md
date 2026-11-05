# v2 shadow report

Turn 13794, 2026-11-05 03:45. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 8,730, prestige 3,310 (190 free, -1.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 14 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.4 |
| grain | 34 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 525 | 0 | 4 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**1 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 525, not 625

## Prestige spending, cheapest coin per prestige first

607 turns left: prestige gained now converts 95.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.4 | 47.4 | running |
| jousting 3 | arena | 230 | 53.6 | 53.8 | needs a arena (build cost 26,298); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 54.8 | 54.8 | thin at home: hop beer, wine, ham, stockfish |
| hold banquet 2 (fish) | mansion | 6.8 | 55.1 | 55.1 | thin at home: wine, cheese |
| hold banquet 2 (pies) | mansion | 7 | 55.4 | 55.4 | thin at home: pasties, wine, cheese, pies |
| hold banquet 1 (fish) | mansion | 4.2 | 56.0 | 56.0 |  |
| hold sermon 2 (candles) | church | 31 | 52.8 | 57.0 | needs a church (build cost 66,979); thin at home: candles, furniture |
| hold banquet 4 | mansion | 17.5 | 57.4 | 57.4 | thin at home: wine, hop beer, ham, stockfish, cheese |
| hold feast 2 | townhouse | 2.6 | 52.9 | 57.8 | needs a townhouse (build cost 7,395); thin at home: wine |
| hold banquet 4 (premium) | mansion | 20 | 57.9 | 57.9 | thin at home: hop beer, wine, ham, stockfish |
| hold prayer 2 | chapel | 13 | 53.6 | 58.0 | needs a chapel (build cost 30,810); thin at home: furniture |
| hold banquet 2 (meat) | mansion | 6.8 | 58.3 | 58.3 | thin at home: wine, cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: pasties buy 6 @ 14.4; crew 0.1; est +17 a turn; stock: pasties 6 @ 14.4 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 15.8 (keep 14); best orders clear only 3 a turn after crew: ship stays at 0
- best towns now: Cobholme +44, Hofkirchen +34, Dortgart +31, Clairas +27, Boistot +24
- Cobholme would trade: pasties buy 7 @ 9.75; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~98 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Gottweiler | 1135 | 0.39 | 0.10 (10/turn) | tapestries 1 (619.5->864.5), nets 3 (34.8->36.29) | salt 3 (4.16->5.56), candles 1 (81.9->84) | +246 |
| Rouhomme | 368 | 0.10 | 0.80 (78/turn) | tapestries 1 (619.5->726.75), bread 150 (2.16->2.77), charcoal 19 (2.14->3.53), nets 6 (34.8->36.29) | tools 15 (4.73->5.98), candles 1 (79.8->84), salt 2 (5.23->5.56), seeds 5 (2.09->2.32) | +208 |
| Hofkirchen | 991 | 0.31 | 0.10 (10/turn) | tapestries 1 (619.5->793.25), nets 6 (34.8->36.29), wheels 1 (19.95->21.47) | tools 15 (5.21->5.98), garments 2 (19.53->20.8), salt 5 (4.79->5.56), jewellery 4 (76.12->76.47) | +189 |
| Neuborn | 780 | 0.20 | 0.50 (49/turn) | tapestries 1 (619.5->712.5), charcoal 19 (2.14->5.98), beer 15 (3.28->4.03), seeds 12 (2.71->3.32) | candles 1 (77.7->84), salt 4 (4.39->5.56), thread 26 (4.49->4.8), cloth 7 (7.3->7.6) | +159 |
| Fontaux | 411 | 0.11 | 1.00 (98/turn) | tapestries 0 (619.5->655.5), thread 26 (4.66->5.65), gold ore 0 (154.35->168.15), bread 135 (2.16->2.55) | tools 13 (5.06->5.98), candles 0 (77.17->84), slaked lime 1 (11.45->14.15), salt 4 (4.73->5.56) | +126 |

**Best:** Gottweiler at about +246 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 35.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 16 @ min 3.06 | goal planner: sells 16 at 3.06 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 15.7, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.4 | goal planner: sells 11 at 19.4 (v2 had 10 at 20.2) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 25) |
| light armour | 1 @ 92, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 81.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 19.2k (cash + stock at home prices); +133/turn over 6 turns, -52/turn over 24 turns.
- Limits: cash flow >= -197/turn, prestige >= +4.60/turn (values are after 200 tax a turn).
- Today's settings: value +91/turn, cash +97/turn, prestige -0.95/turn - breaks the prestige floor.
- Plan: value -145/turn, cash -141/turn, prestige +3.25/turn - could not meet the prestige floor.
- Cash check (real vs predicted cash a tick, last 3): +139 vs +122, +105 vs +112, +110 vs +112.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Angefont: +9/turn
  - ship Flax Wyrm -> Chatgnan: +1/turn
  - net maker 0.00 -> 0.29: +3/turn
  - ropewalk 1 0.25 -> 0.31: +2/turn
  - flax farm 1 4.64 -> 4.70: -1/turn
  - sewing shop 1 0.30 -> 0.36: -3/turn
  - weavery 1 0.50 -> 0.61: +6/turn
  - brewery 1 0.14 -> 0.27: -19/turn
  - mansion 1 0.00 -> 1.00: -227/turn
- Model check over the last 60 turns: predicted +96/turn for the settings we ran, real +40/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.58, thread 3.97, cloth 6.34, flax fibres 4.70, garments 18.34, nets 28.73, beer 2.84, timber 3.07, prestige 10000.00, cash 0.00
- Orders it would set: beer sell 16 (v2 15); firewood buy 4 (v2 5); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 29 (v2 25); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Angefont (+9/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Chatgnan (+1/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +79/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 481 (+192 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 5.94 |
| ret | 3 | 0.91 | 1.19 |
| spin | 4 | 1.65 | 2.09 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 338/228, cloth 72/128

## Self-diagnosis

Nothing found this run.
