# v2 shadow report

Turn 13874, 2026-11-08 11:57. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,760, prestige 3,481 (361 free, -1.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 15, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 7 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 9 | 9 | 9 | 0 | 0 | stop 36, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 518 | 0 | 11 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: home ask 2.68 is above our ceiling 2.40 and last turn bought 4 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Tuning

- **grain**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 102 over real use lately; planning 518, not 618

## Prestige spending, cheapest coin per prestige first

527 turns left: prestige gained now converts 92.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.9 | 51.9 | running |
| jousting 3 | arena | 230 | 54.4 | 54.6 | needs a arena (build cost 25,612); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 55.8 | 55.8 |  |
| hold banquet 4 (pies) | mansion | 18 | 55.9 | 55.9 | thin at home: wine, ham, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 58.4 | 58.4 | thin at home: wine, ham, stockfish |
| hold banquet 4 | mansion | 17.5 | 58.6 | 58.6 | thin at home: wine, ham, stockfish |
| jousting 2 | arena | 210 | 59.5 | 59.8 | needs a arena (build cost 25,612); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 60.6 | 60.6 | thin at home: wine |
| hold banquet 3 (fish) | mansion | 7.6 | 60.8 | 60.8 |  |
| hold banquet 1 (meat) | mansion | 4.2 | 61.1 | 61.1 |  |
| hold banquet 3 (pies) | mansion | 8 | 62.3 | 62.3 |  |
| hold banquet 2 (pies) | mansion | 7 | 64.2 | 64.2 | thin at home: wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 16.2 (keep 14); best orders clear only -8 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 5 @ 16.4 (keep 14); best orders clear only 2 a turn after crew: ship stays at 0
- best towns now: Bordetes +28, Donaunieder +24, Brunnham +23, Brebronn +22, Orlesailles +22
- Bordetes would trade: pasties buy 14 @ 16.1; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~108 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.90 (97/turn) | firewood 32 (2.81->5.75), charcoal 19 (2.62->4.31), bricks 5 (7.19->10.73), bread 149 (2.62->2.83) | dyed cloth 7 (10.08->12.25), candles 1 (76.65->82.5), cloth 9 (8.51->8.8), salt 7 (5.35->5.56) | +156 |
| Kirchwerp | 1072 | 0.39 | 0.40 (43/turn) | thread 72 (4.66->5.7), tackles 1 (177.45->207.1), glassware 5 (66.67->71.25), flour 2 (20.37->28.5) | candles 1 (75.6->82.5), garments 2 (24.57->27), nails 3 (5.62->6.79) | +120 |
| Hofkirchen | 991 | 0.34 | 0.40 (43/turn) | thread 61 (4.66->5.7), nets 6 (33.8->36.29), flour 2 (20.37->27.17), arms 2 (28.98->32.11) | candles 1 (77.17->82.5), cheese 4 (5.78->7.12), garments 2 (25.2->27), nails 3 (5.62->6.79) | +89 |
| Neuborn | 780 | 0.23 | 1.00 (108/turn) | timber 21 (7.51->12.54), charcoal 12 (2.62->5.94), beer 10 (3.28->4.8), seeds 8 (2.29->3.32) | cloth 16 (8.4->8.8), garments 1 (24.78->27), raw cloth 1 (6.72->7.22), salt 2 (5.3->5.56) | +84 |
| Rouhomme | 368 | 0.11 | 0.20 (22/turn) | charcoal 19 (2.62->4.31), copper ingots 1 (14.6->16.25), lead bars 7 (18.38->18.71), fleece 1 (9.5->10.54) | cloth 16 (7.25->8.8), dyed cloth 7 (10.5->12.25), garments 2 (24.36->27), cookware 6 (23.31->24.13) | +74 |

**Best:** Grandgues at about +156 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 28.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 16 @ min 3.26 | goal planner: sells 16 at 3.26 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 16.5, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 25.8) |
| grain | 9 @ 3.7, stop 36 |  | goal planner: buys 9 a turn for today's rates, keeps up to 36 (v2 had 18) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 18) |
| light armour | 1 @ 95.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 23.0k (cash + stock at home prices); +272/turn over 6 turns, -1/turn over 24 turns.
- Limits: cash flow >= -240/turn, prestige >= -0.25/turn (values are after 200 tax a turn).
- Today's settings: value +74/turn, cash +60/turn, prestige -1.81/turn - breaks the prestige floor.
- Plan: value +5/turn, cash +93/turn, prestige -0.25/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +157 vs +72, +461 vs +60, +115 vs +67.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Brunnham: +7/turn
  - ship Flax Wyrm -> Clairlond: +2/turn
  - net maker 0.00 -> 0.29: +7/turn
  - ropewalk 1 0.25 -> 0.00: -7/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.19: +16/turn
  - sewing shop 1 0.30 -> 0.36: -10/turn
  - weavery 1 0.50 -> 0.61: +10/turn
  - spinnery 1 1.65 -> 1.07: -17/turn
  - retting pit 1 0.91 -> 0.61: +11/turn
  - flax farm 1 4.64 -> 3.06: -18/turn
- Model check over the last 59 turns: predicted +103/turn for the settings we ran, real +16/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.65, thread 4.19, cloth 6.67, flax fibres 5.04, garments 19.27, nets 30.00, beer 3.14, timber 3.22, prestige 59.84, cash 0.00
- Orders it would set: beer sell 16 (v2 15); cloth sell 1 (v2 none); firewood buy 4 (v2 8); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 18); labour buy 29 (v2 18); light armour buy 1 (v2 None); rope sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.19, worth +7/turn.
- Ship linen snake: Grandgues -> Brunnham (+7/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Clairlond (+2/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 430 (+141 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.75 |
| ret | 3 | 0.91 | 0.95 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 687/228, cloth 72/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 5.95 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
