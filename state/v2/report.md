# v2 shadow report

Turn 13859, 2026-11-07 20:14. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,388, prestige 3,358 (238 free, -1.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 29 | 6 | 4 | 0 | 0 | min_holding 60, sell 3, sell @ 3.06; stop 17, buy 8, buy @ 3.56 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 4 | 4 | 4 | 0 | 0 | stop 13, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 32 | 0 | 9 | 0 | 0 | stop 32, buy 8, buy @ 3.7 |
| labour | 29 | 29 | 525 | 0 | 4 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: home ask 2.72 is above our ceiling 2.40 and last turn bought 4 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it

## Tuning

- **tar**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 525, not 624

## Prestige spending, cheapest coin per prestige first

542 turns left: prestige gained now converts 93.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.5 | 49.5 | running |
| jousting 3 | arena | 230 | 53.5 | 53.7 | needs a arena (build cost 24,958); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 54.6 | 54.6 | thin at home: wine, ham, stockfish, cheese, candles |
| hold banquet 1 (fish) | mansion | 4.2 | 55.4 | 55.4 |  |
| hold banquet 1 (meat) | mansion | 4.2 | 57.3 | 57.3 |  |
| hold banquet 4 | mansion | 17.5 | 57.5 | 57.5 | thin at home: wine, ham, stockfish, cheese, candles |
| hold banquet 4 (premium) | mansion | 20 | 57.5 | 57.5 | thin at home: wine, ham, stockfish, candles, premium cheese |
| hold banquet 2 (fish) | mansion | 6.8 | 58.0 | 58.0 | thin at home: wine, cheese |
| jousting 2 | arena | 210 | 58.5 | 58.8 | needs a arena (build cost 24,958); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 59.1 | 59.1 | thin at home: wine, cheese |
| hold banquet 2 (pies) | mansion | 7 | 60.1 | 60.1 | thin at home: wine, cheese, candles |
| hold banquet 3 (pies) | mansion | 8 | 60.5 | 60.5 | thin at home: cheese, candles |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 14.3 (keep 14); best orders clear only -6 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~104 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Essenbrucke | 584 | 0.16 | 0.10 (10/turn) | dyed cloth 28 (13.23->19.19), garments 10 (18.97->22.8), pies 2 (19.95->20.52) | chisels 1 (6.98->7.84), yarn 3 (4.39->4.8), casks 6 (5.62->5.98), pasties 1 (14.49->15.29) | +201 |
| Bordetes | 831 | 0.24 | 0.20 (21/turn) | dyed cloth 28 (13.23->15.77), garments 10 (18.97->22.8), flour 2 (21.84->28.88), wine 4 (6.09->7.74) | flax fibres 2 (5.93->6.45) | +121 |
| Hanstein | 380 | 0.11 | 0.30 (31/turn) | garments 10 (18.97->22.04), timber 14 (8.14->11.4), limestone 1 (15.86->20.33) | cloth 14 (7.09->9), thread 43 (4.73->5.3), flax fibres 17 (5.67->6.45), cheese 7 (6.46->7.84) | +118 |
| Hofkirchen | 991 | 0.33 | 1.00 (104/turn) | bread 90 (2.31->4.05), lead ore 5 (13.86->19.38), blades 0 (14.7->17.1), leather 0 (23.73->25.46) | flax fibres 15 (5.17->6.45), cheese 4 (5.78->7.84), dyed cloth 5 (10.82->11.69), cloth 14 (8.56->9) | +116 |
| Pontmont | 341 | 0.10 | 0.20 (21/turn) | garments 10 (18.97->26.41), charcoal 19 (2.75->4.31), pasties 2 (17.22->22.04), raw cloth 3 (6.98->7.69) | thread 31 (5.1->5.3), cheese 7 (7.46->7.84), cloth 12 (8.72->9), spirits 1 (9.19->9.97) | +108 |

**Best:** Essenbrucke at about +201 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 30.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 15 @ min 3.46 |  |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 74.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 15, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 24.2) |
| grain | 8 @ 3.7, stop 32 |  | goal planner: buys 8 a turn for today's rates, keeps up to 32 (v2 had 12) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 25) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 78.0) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 0 = 0.8 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 24.5k (cash + stock at home prices); +163/turn over 6 turns, +140/turn over 24 turns.
- Limits: cash flow >= -350/turn, prestige >= +2.60/turn (values are after 200 tax a turn).
- Today's settings: value +80/turn, cash +63/turn, prestige -1.19/turn - breaks the prestige floor.
- Plan: value -99/turn, cash -93/turn, prestige +2.60/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +124 vs +62, +235 vs +68, +24 vs +68.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> no route: +0/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +3/turn
  - flax farm 1 4.64 -> 4.73: -0/turn
  - sewing shop 1 0.30 -> 0.36: -10/turn
  - weavery 1 0.50 -> 0.61: +12/turn
  - ropewalk 1 0.25 -> 0.00: -14/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.38: +17/turn
  - mansion 1 0.00 -> 0.90: -191/turn
- HAND-OVER: goal planner: model check held 12 runs, it now runs 'rates' live.
- Model check over the last 61 turns: predicted +104/turn for the settings we ran, real +80/turn.
- Worth of one more unit per turn: labour 1.65, thread 4.14, cloth 6.62, flax fibres 4.91, garments 19.15, nets 29.69, beer 3.00, timber 3.08, prestige 55.31, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 8); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 8 (v2 12); labour buy 29 (v2 25); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.38, worth +14/turn.
- Ship linen snake: Grandgues -> no route (+0/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +82/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 441 (+152 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 5.03 |
| ret | 3 | 0.91 | 1.01 |
| spin | 4 | 1.65 | 1.77 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 530/228, cloth 72/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.45 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
