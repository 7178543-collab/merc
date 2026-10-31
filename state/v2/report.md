# v2 shadow report

Turn 13673, 2026-10-31 02:19. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 992, prestige 3,205 (85 free, -5.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 19 | 0 | 0 | 0 | 0 | min_holding 60, sell 12, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 0 | 0 | 0 | 0 | 0 | none |
| firewood | 14 | 3 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 0 | 0 | 0 | 0 | 0 | none |
| garments | 32 | 0 | 2 | 0 | 0 | min_holding 8, sell 12, sell @ 21.4 |
| grain | 33 | 0 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 529 | 0 | 0 | buy 29, buy @ 2 |
| meat | 0 | 0 | 0 | 0 | 0 | none |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**1 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.2 turns (holds 4, next step uses 24/turn) -> v2: check the step that makes it

## Tuning

- **candles**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax fibres**: flax fibres buffer thin: 1.2 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 56
- **flax plants**: flax plants buffer thin: 1.2 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 145

## Notes

- labour: projection runs 100 over real use lately; planning 529, not 629

## Prestige spending, cheapest coin per prestige first

728 turns left: prestige gained now converts 97.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 3 (pies) | mansion | 8 | 46.7 | 46.7 | thin at home: hop beer, pies, candles |
| maintain 1 | park | 0.5 | 47.7 | 47.7 | running |
| hold banquet 2 (pies) | mansion | 7 | 48.8 | 48.8 | thin at home: wine, pies, candles |
| hold banquet 4 (pies) | mansion | 18 | 50.0 | 50.0 | thin at home: hop beer, wine, pies, candles |
| hold banquet 3 (meat) | mansion | 7.6 | 52.3 | 52.3 | thin at home: hop beer |
| hold banquet 3 (fish) | mansion | 7.6 | 53.4 | 53.4 | thin at home: hop beer, cured fish |
| jousting 3 | arena | 230 | 53.4 | 53.6 | needs a arena (build cost 24,298); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 54.0 | 54.0 | thin at home: wine, hop beer, ham, stockfish, candles |
| hold banquet 2 (meat) | mansion | 6.8 | 54.1 | 54.1 | thin at home: wine |
| hold banquet 2 (fish) | mansion | 6.8 | 55.2 | 55.2 | thin at home: wine, cured fish |
| hold banquet 4 (premium) | mansion | 20 | 55.8 | 55.8 | thin at home: hop beer, wine, stockfish, candles, premium cheese, premium ham |
| hold sermon 2 (candles) | church | 31 | 52.6 | 55.8 | needs a church (build cost 61,878); thin at home: candles, furniture |

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
| arms | 1 @ 29.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 19 @ min 3.38 |  |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 1 @ 76.0, stop 61 |  | goal planner: buys 1 a turn for today's rates, keeps up to 61 (v2 had 2) |
| cured meat |  | 2 @ min 21.2 | goal planner: trial sale of an idle pile, 2 a turn at 21.2, keeps 0 (24 over) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| furniture | 2 @ 12.2, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 14 @ min 20.8 | makes 12.3, uses 2.1, holds 32 (keeps 8): sells the surplus + 3/turn of the excess |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 29) |
| light armour | 1 @ 91.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 80.0) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 1 = 3.0 turns |
| thread |  | 23 @ min 3.96 | goal planner: sells 23 a turn at 3.96, keeps 189 (no one offered it) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 150 |

## Goal: business value (live: buys, sells, ships)
- Value now 8.4k (cash + stock at home prices); +94/turn over 6 turns, -18/turn over 24 turns.
- Limits: cash flow >= +125/turn, prestige >= +8.95/turn (values are after 200 tax a turn).
- Today's settings: value +84/turn, cash -11/turn, prestige -5.25/turn - breaks the prestige floor and cash floor.
- Plan: value -28/turn, cash +75/turn, prestige -1.05/turn - could not meet the prestige floor and cash floor.
- Cash check (real vs predicted cash a tick, last 3): -16 vs -53, +95 vs +38, +174 vs +38.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - net maker 0.00 -> 0.28: +3/turn
  - sewing shop 1 0.30 -> 0.02: +4/turn
  - weavery 1 0.50 -> 0.03: +12/turn
  - flax farm 1 4.64 -> 4.81: +2/turn
  - retting pit 1 0.91 -> 0.96: +4/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.32: -8/turn
  - ropewalk 1 0.25 -> 0.00: +12/turn
  - mansion 1 0.00 -> 1.00: -149/turn
- Model check over the last 59 turns: predicted -34/turn for the settings we ran, real -65/turn.
- Worth of one more unit per turn: labour 159.28, thread 399.96, cloth 638.89, flax fibres 473.62, garments 1848.79, nets 2835.56, beer 277.49, timber 696.90, prestige 10000.00, cash 100.00
- Orders it would set: candles buy 1 (v2 2); cured meat sell 2 (v2 none); firewood buy 4 (v2 5); fish buy 0 (v2 None); furniture buy 2 (v2 None); grain buy 9 (v2 11); light armour buy 1 (v2 None); meat buy 0 (v2 None); rope sell 2 (v2 1); thread sell 23 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.32, worth +14/turn.
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +82/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
- Trim: donate weavery 1: +16/turn (tax 18 saved).

## Chain sizing

Mode HOLD, garments sold 0.5/turn (+0.0 exported); plan makes 4.9 garments a turn.
Labour: own 500, everything else 340, chain may buy 0 -> chain allowance 160, chain plan 159 (-130 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 2.87 |
| ret | 3 | 0.91 | 0.57 |
| spin | 4 | 1.65 | 1.01 |
| weave | 3 | 0.50 | 0.19 |
| sew | 2 | 0.30 | 0.12 |

Buffers: flax fibres 33/40, thread 224/119, cloth 4/19
- chain plan needed 492 labour, budget left 160: cut to 160 (sewing capped at 0.12)

## Self-diagnosis

- R1: donations slot dry: 0.0 held, 40.0 a turn (luxury slot (+1 prestige)); our buy none, home ask 1.0 (held back: failsafe level 3: reduce-only, would buy 48 @ 1.02 (ask 1.0, cap 1.5))
- R1: fish slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask 1.68 (held back: failsafe level 3: reduce-only, would buy 14 @ 1.71 (ask 1.68, cap 2.6))
- R1: meat slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask 1.78 (held back: failsafe level 3: reduce-only, would buy 14 @ 1.81 (ask 1.78, cap 2.6))
- R1: prestige rate -5.25 a turn vs 12-turn median -1.46; likely: dry slot: donations, fish, meat
