# v2 shadow report

Turn 13678, 2026-10-31 07:15. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 2,519, prestige 3,182 (62 free, -4.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 93 | 0 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 3.3 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 0 | 0 | 0 | 0 | 0 | none |
| firewood | 15 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 0 | 0 | 0 | 0 | 0 | none |
| garments | 21 | 0 | 2 | 0 | 0 | min_holding 8, sell 11, sell @ 20 |
| grain | 30 | 8 | 9 | 0 | 0 | stop 31, buy 8, buy @ 3.7 |
| labour | 29 | 29 | 529 | 0 | 0 | buy 29, buy @ 2.2 |
| meat | 0 | 0 | 0 | 0 | 0 | none |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**1 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.4 turns (holds 9, next step uses 24/turn) -> v2: check the step that makes it

## Tuning

- **candles**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax fibres**: flax fibres buffer thin: 1.0 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 56
- **flax plants**: flax plants buffer thin: 1.3 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 145

## Notes

- labour: projection runs 100 over real use lately; planning 529, not 629

## Prestige spending, cheapest coin per prestige first

723 turns left: prestige gained now converts 97.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 3 (pies) | mansion | 8 | 46.7 | 46.7 | thin at home: hop beer, pies, candles |
| hold banquet 2 (pies) | mansion | 7 | 48.2 | 48.2 | thin at home: pies, candles |
| maintain 1 | park | 0.5 | 48.3 | 48.3 | running |
| hold banquet 4 (pies) | mansion | 18 | 49.8 | 49.8 | thin at home: hop beer, pies, candles |
| hold banquet 3 (fish) | mansion | 7.6 | 50.7 | 50.7 | thin at home: hop beer, cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 51.8 | 51.8 | thin at home: cured fish |
| hold banquet 3 (meat) | mansion | 7.6 | 52.9 | 52.9 | thin at home: hop beer |
| jousting 3 | arena | 230 | 53.3 | 53.4 | needs a arena (build cost 25,468); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 53.6 | 53.6 | thin at home: cured fish |
| hold banquet 4 | mansion | 17.5 | 53.8 | 53.8 | thin at home: hop beer, stockfish, candles |
| hold banquet 2 (meat) | mansion | 6.8 | 54.3 | 54.3 |  |
| hold banquet 4 (premium) | mansion | 20 | 54.9 | 54.9 | thin at home: hop beer, stockfish, candles, premium cheese |

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
| arms | 1 @ 31.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 3 @ min 3.3 | goal planner: trial sale of an idle pile, 3 a turn at 3.3, keeps 60 (33 over) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 1 @ 76.0, stop 61 |  | goal planner: buys 1 a turn for today's rates, keeps up to 61 (v2 had 2) |
| cured meat |  | 1 @ min 22 | goal planner: sells 1 a turn at 22, keeps 0 (no one offered it) |
| firewood | 4 @ 2.4, stop 14 |  | goal planner: buys 4 a turn for today's rates, keeps up to 14 (v2 had 5) |
| furniture | 2 @ 12.2, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 20 | goal planner: sells 11 at 20 (v2 had 11 at 20.4) |
| grain | 8 @ 3.7, stop 30 |  | goal planner: buys 8 a turn for today's rates, keeps up to 30 (v2 had 12) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 29) |
| light armour | 1 @ 82.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 81.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| thread |  | 20 @ min 3.96 | goal planner: sells 20 a turn at 3.96, keeps 189 (no one offered it) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 9.8k (cash + stock at home prices); +254/turn over 6 turns, +70/turn over 24 turns.
- Limits: cash flow >= +62/turn, prestige >= +9.93/turn (values are after 200 tax a turn).
- Today's settings: value +139/turn, cash +86/turn, prestige -4.63/turn - breaks the prestige floor.
- Plan: value -23/turn, cash +60/turn, prestige -0.43/turn - could not meet the prestige floor and cash floor.
- Cash check (real vs predicted cash a tick, last 3): +346 vs -11, +310 vs +39, +291 vs +83.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - sewing shop 1 0.30 -> 0.17: +8/turn
  - weavery 1 0.50 -> 0.27: +19/turn
  - net maker 0.00 -> 0.37: +18/turn
  - retting pit 1 0.91 -> 0.78: -16/turn
  - flax farm 1 4.64 -> 3.91: -9/turn
  - spinnery 1 1.65 -> 1.38: -25/turn
  - mansion 1 0.00 -> 1.00: -159/turn
- Model check over the last 59 turns: predicted -13/turn for the settings we ran, real -37/turn.
- Worth of one more unit per turn: labour 159.26, thread 399.96, cloth 638.85, flax fibres 473.73, garments 1848.62, nets 2890.91, beer 290.01, timber 674.93, prestige 10000.00, cash 100.00
- Orders it would set: beer sell 3 (v2 none); candles buy 1 (v2 2); cured meat sell 1 (v2 none); firewood buy 4 (v2 5); fish buy 0 (v2 None); furniture buy 2 (v2 None); grain buy 8 (v2 12); light armour buy 1 (v2 None); meat buy 0 (v2 None); rope sell 2 (v2 1)
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 4.7/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 504 (+215 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 6.44 |
| ret | 3 | 0.91 | 1.29 |
| spin | 4 | 1.65 | 2.27 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 29/77, thread 212/227, cloth 9/128

## Self-diagnosis

- R1: donations slot dry: 0.0 held, 40.0 a turn (luxury slot (+1 prestige)); our buy none, home ask 1.0 (held back: failsafe level 2: reduce-only, would buy 80 @ 1.02 (ask 1.0, cap 1.5))
- R1: fish slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask 1.8 (held back: failsafe level 2: reduce-only, would buy 14 @ 1.83 (ask 1.8, cap 2.6))
- R1: meat slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask 2.12 (held back: failsafe level 2: reduce-only, would buy 14 @ 2.16 (ask 2.12, cap 2.6))
