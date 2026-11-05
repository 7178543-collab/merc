# v2 shadow report

Turn 13796, 2026-11-05 05:56. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 8,951, prestige 3,308 (188 free, -0.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 14 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.4 |
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
- **tar**: home ask 11.10 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 525, not 618

## Prestige spending, cheapest coin per prestige first

605 turns left: prestige gained now converts 95.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.7 | 47.7 | running |
| jousting 3 | arena | 230 | 53.3 | 53.5 | needs a arena (build cost 26,140); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 54.2 | 54.2 | thin at home: pasties, wine, cheese, candles |
| hold banquet 4 (pies) | mansion | 18 | 55.1 | 55.1 | thin at home: wine, ham, stockfish, cheese, candles |
| hold banquet 2 (fish) | mansion | 6.8 | 56.1 | 56.1 | thin at home: wine, cured fish, cheese |
| hold banquet 2 (meat) | mansion | 6.8 | 56.7 | 56.7 | thin at home: wine, cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 57.4 | 57.4 |  |
| hold feast 2 | townhouse | 2.6 | 53.0 | 57.8 | needs a townhouse (build cost 7,258); thin at home: wine |
| hold banquet 4 | mansion | 17.5 | 58.0 | 58.0 | thin at home: wine, ham, stockfish, cheese, candles |
| hold banquet 4 (premium) | mansion | 20 | 58.2 | 58.2 | thin at home: wine, ham, stockfish, candles |
| hold sermon 2 (candles) | church | 31 | 54.3 | 58.5 | needs a church (build cost 66,617); thin at home: jewellery, candles, furniture |
| jousting 2 | arena | 210 | 58.4 | 58.6 | needs a arena (build cost 26,140); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 13.7 (keep 14); best orders clear only 6 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 15.9 (keep 14); best orders clear only -1 a turn after crew: ship stays at 0
- best towns now: Cobholme +64, Hofkirchen +47, Heilegg +43, Großmühle +35, Friedwerp +30
- Cobholme would trade: pasties buy 9 @ 9.55; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~99 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Fontaux | 411 | 0.11 | 0.60 (59/turn) | thread 29 (4.6->7.27), timber 20 (7.25->10.73), charcoal 18 (2.09->4.26), hinges 1 (44.73->47.5) | garments 17 (21.42->22.04), yarn 2 (4.6->8.41), salt 4 (4.39->5.56) | +163 |
| Grandgues | 152 | 0.04 | 0.30 (30/turn) | charcoal 19 (2.09->4.94), timber 22 (7.25->9.03), limestone 2 (17.12->21.47), raw cloth 3 (7.04->9.12) | tapestries 1 (792.75->812.25), yarn 2 (4.66->8.41), garments 17 (21.63->22.04), candles 2 (65.1->66.5) | +135 |
| Vauxvais | 204 | 0.05 | 0.20 (20/turn) | charcoal 19 (2.09->4.01), wax 5 (23.94->27.17), butter 1 (74.03->85.02), firewood 1 (1.65->3.8) | garments 17 (20.27->22.04), thread 37 (4.49->5.25), yarn 2 (4.01->8.41), salt 4 (4.68->5.56) | +125 |
| Neuborn | 780 | 0.21 | 0.50 (49/turn) | charcoal 19 (2.09->6.55), furniture 12 (13.55->15.96), beer 15 (3.28->3.91), butter 1 (74.03->77.9) | garments 17 (20.27->22.04), thread 13 (4.43->5.25), yarn 2 (4.56->8.41), salt 3 (5.3->5.56) | +123 |
| Boistot | 1230 | 0.44 | 0.20 (20/turn) | - | tapestries 1 (703.5->812.25), garments 17 (21->22.04), yarn 2 (4.26->8.41), axes 2 (16.8->18.05) | +119 |

**Best:** Fontaux at about +163 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 38.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 16 @ min 3.06 | goal planner: sells 16 at 3.06 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 15, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.4 | goal planner: sells 11 at 19.4 (v2 had 10 at 21.4) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 25) |
| light armour | 1 @ 84, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 81.0) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 19.4k (cash + stock at home prices); +99/turn over 6 turns, +11/turn over 24 turns.
- Limits: cash flow >= -206/turn, prestige >= +4.68/turn (values are after 200 tax a turn).
- Today's settings: value +111/turn, cash +117/turn, prestige -0.94/turn - breaks the prestige floor.
- Plan: value -119/turn, cash -115/turn, prestige +3.26/turn - could not meet the prestige floor.
- Cash check (real vs predicted cash a tick, last 3): +110 vs +112, +170 vs +97, +50 vs +115.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship Flax Wyrm -> Karlmoor: +2/turn
  - net maker 0.00 -> 0.29: +3/turn
  - flax farm 1 4.64 -> 4.71: -1/turn
  - sewing shop 1 0.30 -> 0.36: -3/turn
  - weavery 1 0.50 -> 0.61: +6/turn
  - ropewalk 1 0.25 -> 0.00: -15/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.35: +18/turn
  - brewery 1 0.14 -> 0.27: -20/turn
  - mansion 1 0.00 -> 1.00: -220/turn
- Model check over the last 60 turns: predicted +96/turn for the settings we ran, real +39/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.59, thread 3.99, cloth 6.38, flax fibres 4.73, garments 18.45, nets 28.82, beer 2.88, timber 3.13, prestige 10000.00, cash 0.00
- Orders it would set: beer sell 16 (v2 15); firewood buy 4 (v2 5); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 29 (v2 25); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.35, worth +17/turn.
- Ship linen snake: stays on Grandgues (worth +7/turn).
- Ship Flax Wyrm: Caillechâtel -> Karlmoor (+2/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +79/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 482 (+193 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 5.94 |
| ret | 3 | 0.91 | 1.19 |
| spin | 4 | 1.65 | 2.10 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 336/228, cloth 72/128

## Self-diagnosis

Nothing found this run.
