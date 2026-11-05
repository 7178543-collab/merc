# v2 shadow report

Turn 13795, 2026-11-05 04:51. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 8,901, prestige 3,309 (189 free, -0.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 14 | 3 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.4 |
| grain | 34 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 529 | 1 | 0 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**1 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **Flax Wyrm**: Flax Wyrm cost 10 coin last turn (crew 0.10) and its route traded nothing (route limited by pasties space) -> v2: pause it (crew 0) until a route is proven to sell

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 530, not 630

## Prestige spending, cheapest coin per prestige first

606 turns left: prestige gained now converts 95.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.4 | 47.4 | running |
| hold banquet 2 (pies) | mansion | 7 | 53.1 | 53.1 | thin at home: wine, cheese, candles |
| jousting 3 | arena | 230 | 52.9 | 53.1 | needs a arena (build cost 28,242); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 53.9 | 53.9 | thin at home: wine, cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 54.6 | 54.6 |  |
| hold banquet 4 (pies) | mansion | 18 | 54.9 | 54.9 | thin at home: wine, ham, stockfish, cheese, candles |
| hold sermon 2 (candles) | church | 31 | 51.8 | 56.3 | needs a church (build cost 70,669); thin at home: jewellery, candles, furniture |
| hold prayer 2 | chapel | 13 | 51.7 | 56.5 | needs a chapel (build cost 33,950); thin at home: furniture |
| hold banquet 2 (meat) | mansion | 6.8 | 57.1 | 57.1 | thin at home: wine, cheese |
| hold banquet 4 | mansion | 17.5 | 58.1 | 58.1 | thin at home: wine, ham, stockfish, cheese, candles |
| hold sermon 2 | church | 24 | 52.4 | 58.1 | needs a church (build cost 70,669); thin at home: jewellery, furniture |
| hold banquet 4 (premium) | mansion | 20 | 58.2 | 58.2 | thin at home: wine, ham, stockfish, candles |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 10 | 134102075 | 0.072 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 14.9 (keep 14); best orders clear only 6 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 15.9 (keep 14); best orders clear only -1 a turn after crew: ship stays at 0
- best towns now: Cobholme +46, Heilegg +44, Hofkirchen +41, Donaunieder +38, Clairas +33
- Cobholme would trade: pasties buy 8 @ 10.7; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~98 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Fontaux | 411 | 0.11 | 0.60 (59/turn) | thread 32 (4.66->7.27), charcoal 18 (2.14->4.14), timber 19 (7.98->10.54), flax plants 4 (1.31->1.98) | yarn 5 (4.62->6.46), salt 4 (4.41->5.56), garments 2 (21.42->23.2), tools 15 (5.19->5.37) | +138 |
| Neuborn | 780 | 0.20 | 0.40 (39/turn) | charcoal 19 (2.14->6.46), gears 1 (69.83->92.62), beer 15 (3.28->3.91), grain 2 (2.42->3.93) | thread 20 (4.45->5.05), yarn 5 (4.56->6.46), garments 2 (20.27->23.2), cloth 7 (7.3->7.6) | +101 |
| Essenbrucke | 584 | 0.15 | 0.10 (10/turn) | tapestries 1 (813.75->878.75) | slaked lime 3 (8.51->15.67), yarn 5 (4.28->6.46), garments 2 (21.42->23.2), salt 4 (4.91->5.56) | +97 |
| Vauxvais | 204 | 0.05 | 0.20 (20/turn) | charcoal 19 (2.14->4.1), wax 2 (25.62->27.17), firewood 1 (1.65->3.8), tiles 1 (2.46->3.12) | thread 38 (4.45->5.05), tools 15 (4.77->5.37), yarn 3 (3.97->6.46), garments 2 (20.27->23.2) | +77 |
| Rouhomme | 368 | 0.10 | 0.70 (69/turn) | bread 149 (2.39->2.79), charcoal 19 (2.14->3.53), nets 5 (34.8->36.86), beer 15 (3.28->3.7) | thread 49 (4.73->5.05), tools 15 (4.73->5.37), yarn 2 (3.99->6.46), garments 2 (21->23.2) | +75 |

**Best:** Fontaux at about +138 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 36.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 16 @ min 3.06 | goal planner: sells 16 at 3.06 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 71.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 15.7, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.4 | goal planner: sells 11 at 19.4 (v2 had 10 at 20.0) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 30) |
| light armour | 1 @ 92, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 81.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 19.3k (cash + stock at home prices); +116/turn over 6 turns, +19/turn over 24 turns.
- Limits: cash flow >= -204/turn, prestige >= +4.64/turn (values are after 200 tax a turn).
- Today's settings: value +104/turn, cash +115/turn, prestige -0.95/turn - breaks the prestige floor.
- Plan: value -129/turn, cash -119/turn, prestige +3.25/turn - could not meet the prestige floor.
- Cash check (real vs predicted cash a tick, last 3): +105 vs +112, +110 vs +112, +170 vs +97.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Karlmoor: +2/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +3/turn
  - ropewalk 1 0.25 -> 0.31: +2/turn
  - flax farm 1 4.64 -> 4.69: -0/turn
  - sewing shop 1 0.30 -> 0.36: -3/turn
  - weavery 1 0.50 -> 0.61: +6/turn
  - brewery 1 0.14 -> 0.27: -17/turn
  - mansion 1 0.00 -> 1.00: -225/turn
- Model check over the last 60 turns: predicted +96/turn for the settings we ran, real +39/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.58, thread 3.97, cloth 6.34, flax fibres 4.70, garments 18.34, nets 28.77, beer 2.73, timber 3.67, prestige 10000.00, cash 0.00
- Orders it would set: beer sell 16 (v2 15); candles buy 2 (v2 None); firewood buy 4 (v2 5); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 29 (v2 30); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Karlmoor (+2/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +79/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 481 (+192 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 5.93 |
| ret | 3 | 0.91 | 1.19 |
| spin | 4 | 1.65 | 2.09 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 338/228, cloth 72/128

## Self-diagnosis

Nothing found this run.
