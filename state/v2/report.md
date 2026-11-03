# v2 shadow report

Turn 13762, 2026-11-03 19:06. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 7,749, prestige 3,183 (63 free, -0.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 15 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.4 |
| grain | 33 | 6 | 9 | 0 | 0 | stop 33, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 518 | 0 | 11 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 12.60 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Tuning

- **tar**: home ask 12.60 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 518, not 618

## Prestige spending, cheapest coin per prestige first

639 turns left: prestige gained now converts 96.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 4 (pies) | mansion | 18 | 49.8 | 49.8 | thin at home: wine, stockfish |
| maintain 1 | park | 0.5 | 49.8 | 49.8 | running |
| hold banquet 4 | mansion | 17.5 | 52.5 | 52.5 | thin at home: wine, ham, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 53.2 | 53.2 | thin at home: wine, stockfish, premium cheese, premium ham |
| hold banquet 3 (pies) | mansion | 8 | 53.3 | 53.3 | thin at home: pies |
| jousting 3 | arena | 230 | 53.7 | 53.9 | needs a arena (build cost 25,324); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 54.3 | 54.3 | thin at home: wine, pies |
| hold banquet 3 (meat) | mansion | 7.6 | 58.4 | 58.4 |  |
| hold banquet 2 (meat) | mansion | 6.8 | 59.0 | 59.0 | thin at home: wine |
| jousting 2 | arena | 210 | 58.8 | 59.0 | needs a arena (build cost 25,324); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 59.4 | 59.4 |  |
| hold banquet 1 (meat) | mansion | 4.2 | 59.8 | 59.8 |  |

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
| arms | 1 @ 29.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had None) |
| beer |  | 16 @ min 3.06 | goal planner: sells 16 at 3.06 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 84, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 7.1 | goal planner: sells 1 a turn at 7.1, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 15.2, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.4 | goal planner: sells 11 at 19.4 (v2 had 10 at 22.2) |
| grain | 11 @ 3.7, stop 36 |  | uses 9.0/turn (brewery 1), makes 0.0, holds 33 = 3.6 turns |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 18) |
| light armour | 1 @ 88, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 37.2) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 19.4k (cash + stock at home prices); +175/turn over 6 turns, +90/turn over 24 turns.
- Limits: cash flow >= -156/turn, prestige >= +9.88/turn (values are after 200 tax a turn).
- Today's settings: value +97/turn, cash +99/turn, prestige -0.32/turn - breaks the prestige floor.
- Plan: value -133/turn, cash -131/turn, prestige +3.88/turn - could not meet the prestige floor.
- Cash check (real vs predicted cash a tick, last 3): +150 vs +86, +153 vs +86, +160 vs +85.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - net maker 0.00 -> 0.29: +3/turn
  - flax farm 1 4.64 -> 4.57: +1/turn
  - brewery 1 0.14 -> 0.00: -5/turn
  - sewing shop 1 0.30 -> 0.36: -5/turn
  - weavery 1 0.50 -> 0.59: +7/turn
  - brewery 1 [brew beer 2] 0.00 -> 0.25: -10/turn
  - ropewalk 1 0.25 -> 0.00: -13/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.35: +16/turn
  - mansion 1 0.00 -> 1.00: -225/turn
- Model check over the last 59 turns: predicted +75/turn for the settings we ran, real +105/turn.
- Worth of one more unit per turn: labour 1.66, thread 4.17, cloth 6.66, flax fibres 4.94, garments 19.27, nets 29.91, beer 2.79, timber 3.04, prestige 10000.00, cash 0.00
- Orders it would set: arms buy 1 (v2 None); beer sell 16 (v2 15); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 5); furniture buy 2 (v2 None); garments sell 11 (v2 10); labour buy 29 (v2 18); light armour buy 1 (v2 None)
- Recipe: brewery 1 brew beer 1 -> brew beer 2 at 0.25, worth +18/turn.
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.35, worth +12/turn.
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.1/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 505 (+216 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 6.45 |
| ret | 3 | 0.91 | 1.29 |
| spin | 4 | 1.65 | 2.28 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 215/228, cloth 81/128

## Self-diagnosis

- R5: tar buy not filling: bid 11 under the home ask 12.6 for 4 turns, bought 0.0 of 1, 0.0 held (0.0 turns); raise needs Taylor (ceiling 11.0)
