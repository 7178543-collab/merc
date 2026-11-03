# v2 shadow report

Turn 13749, 2026-11-03 06:03. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 6,160, prestige 3,187 (67 free, -0.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 14 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 10, sell @ 19.4 |
| grain | 33 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 525 | 0 | 4 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 14, buy @ 2.22 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**1 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **meat**: buying 14, need ~1 -> v2: buy 1

## Tuning

- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 525, not 625

## Prestige spending, cheapest coin per prestige first

652 turns left: prestige gained now converts 96.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.1 | 48.1 | running |
| hold banquet 4 (pies) | mansion | 18 | 50.2 | 50.2 | thin at home: hop beer, wine, stockfish, pies |
| hold banquet 4 (premium) | mansion | 20 | 52.8 | 52.8 | thin at home: hop beer, wine, stockfish, premium cheese |
| jousting 3 | arena | 230 | 53.0 | 53.1 | needs a arena (build cost 25,818); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 53.4 | 53.4 | thin at home: wine, hop beer, ham, stockfish |
| hold banquet 2 (pies) | mansion | 7 | 53.5 | 53.5 | thin at home: wine, pies |
| hold banquet 3 (pies) | mansion | 8 | 53.6 | 53.6 | thin at home: hop beer, pies |
| jousting 2 | arena | 210 | 58.0 | 58.2 | needs a arena (build cost 25,818); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold sermon 2 (candles) | church | 31 | 54.9 | 58.8 | needs a church (build cost 67,832); thin at home: candles, furniture |
| hold banquet 1 (meat) | mansion | 4.2 | 59.0 | 59.0 |  |
| hold banquet 2 (meat) | mansion | 6.8 | 59.0 | 59.0 | thin at home: wine |
| hold feast 2 | townhouse | 2.6 | 55.4 | 59.3 | needs a townhouse (build cost 6,330); thin at home: wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~94 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Chribruck | 1202 | 0.40 | 0.20 (19/turn) | tackles 2 (183.75->195.7), garments 1 (16.82->19.38), cloth 5 (7.88->8.55), honey 2 (7.67->8.46) | alembics 1 (348.6->456) | +129 |
| Heidlowe | 662 | 0.17 | 0.20 (19/turn) | thread 66 (3.96->4.24), garments 1 (16.82->18.71), wine 11 (5.67->5.98), lead ore 1 (6.93->9.21) | alembics 1 (348.6->456) | +119 |
| Rouhomme | 368 | 0.09 | 0.60 (56/turn) | bread 145 (2.31->2.93), charcoal 11 (1.87->3.52), thread 7 (3.96->5.18), flour 1 (16.91->19.95) | ploughs 4 (63->69.35) | +100 |
| Herschweig | 775 | 0.20 | 0.10 (9/turn) | flax fibres 13 (4.98->6.13), lead ore 1 (6.93->10.45), garments 1 (16.82->18.81), wine 4 (5.67->6.32) | alembics 1 (386.4->456), cloth 3 (6.88->7.5), tackles 1 (152.25->153.9) | +90 |
| Angefont | 686 | 0.17 | 0.20 (19/turn) | thread 29 (3.96->5.79), limestone 1 (13.12->28.31), premium cheese 1 (26.04->27.74), flour 1 (16.91->18.81) | garments 2 (21.21->21.8), honey 3 (6.3->6.84) | +63 |

**Best:** Chribruck at about +129 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 16 @ min 3.06 | goal planner: sells 16 at 3.06 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 80.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 6) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 15.1, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 10 @ min 19.4 | goal planner: sells 10 at 19.4 (v2 had 10 at 21.0) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 25) |
| light armour | 1 @ 89, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 35.2) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 75.5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 17.0k (cash + stock at home prices); -162/turn over 6 turns, +72/turn over 24 turns.
- Limits: cash flow >= -90/turn, prestige >= +9.70/turn (values are after 200 tax a turn).
- Today's settings: value +63/turn, cash +35/turn, prestige -0.34/turn - breaks the prestige floor.
- Plan: value -143/turn, cash -107/turn, prestige +3.86/turn - could not meet the prestige floor and cash floor.
- Cash check (real vs predicted cash a tick, last 3): -77 vs +60, -163 vs +45, +153 vs +42.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - sewing shop 1 0.30 -> 0.23: +6/turn
  - weavery 1 0.50 -> 0.36: +14/turn
  - net maker 0.00 -> 0.28: +9/turn
  - retting pit 1 0.91 -> 0.72: -14/turn
  - flax farm 1 4.64 -> 3.61: +5/turn
  - brewery 1 0.14 -> 0.27: -13/turn
  - spinnery 1 1.65 -> 1.27: -15/turn
  - mansion 1 0.00 -> 1.00: -199/turn
- Model check over the last 59 turns: predicted +86/turn for the settings we ran, real +102/turn.
- Worth of one more unit per turn: labour 163.62, thread 410.91, cloth 656.34, flax fibres 486.69, garments 1899.23, nets 2952.65, beer 280.46, timber 2.92, prestige 10000.00, cash 100.00
- Orders it would set: beer sell 16 (v2 15); candles buy 2 (v2 None); firewood buy 4 (v2 6); furniture buy 2 (v2 None); grain buy 9 (v2 11); labour buy 29 (v2 25); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +84/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new chandlery (make tallow candles 2) for ~3915 coin: +19/turn, payback 207 turns, doesn't pay yet (materials thin at home: nails)

## Chain sizing

Mode HOLD, garments sold 1.8/turn (+0.0 exported); plan makes 32.0 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 494 (+205 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 6.35 |
| ret | 3 | 0.91 | 1.27 |
| spin | 4 | 1.65 | 2.24 |
| weave | 3 | 0.50 | 1.25 |
| sew | 2 | 0.30 | 0.78 |

Buffers: flax fibres 27/76, thread 193/224, cloth 79/125

## Self-diagnosis

Nothing found this run.
