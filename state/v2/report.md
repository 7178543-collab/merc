# v2 shadow report

Turn 13884, 2026-11-08 21:11. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,967, prestige 3,535 (415 free, -2.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 8 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 9 | 9 | 9 | 0 | 0 | stop 36, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 518 | 0 | 11 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.10 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Tuning

- **tar**: home ask 11.10 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 518, not 618

## Prestige spending, cheapest coin per prestige first

517 turns left: prestige gained now converts 92.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 52.2 | 52.2 | running |
| hold banquet 4 (pies) | mansion | 18 | 55.8 | 55.8 | thin at home: hop beer, wine, ham, stockfish |
| jousting 3 | arena | 230 | 55.9 | 56.1 | needs a arena (build cost 27,232); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 58.0 | 58.0 | thin at home: wine, hop beer, ham, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 58.0 | 58.0 | thin at home: hop beer, wine, ham, stockfish |
| hold banquet 1 (fish) | mansion | 4.2 | 58.3 | 58.3 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 59.8 | 59.8 | thin at home: hop beer |
| hold banquet 2 (fish) | mansion | 6.8 | 60.3 | 60.3 | thin at home: wine |
| jousting 2 | arena | 210 | 61.2 | 61.5 | needs a arena (build cost 27,232); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 61.6 | 61.6 | thin at home: pasties, hop beer |
| hold banquet 3 (meat) | mansion | 7.6 | 63.6 | 63.6 | thin at home: hop beer, cured meat |
| hold banquet 2 (pies) | mansion | 7 | 64.1 | 64.1 | thin at home: pasties, wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 16.3 (keep 14); best orders clear only -9 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Gotthafen +367, Heidlowe +349, Brunnham +312, Essenbrucke +303, Brebronn +296
- Gotthafen would trade: furniture buy 31 @ 13.3, pasties buy 2 @ 15.3; crew 0.4

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~116 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Rouhomme | 368 | 0.11 | 1.00 (116/turn) | bread 156 (2.42->3.53), flour 4 (22.47->31.73), charcoal 19 (2.71->4.99), garments 10 (22.2->23.75) | cloth 8 (8.93->12.82), flax fibres 3 (4.94->6.25), arms 2 (30.45->30.78), dyed cloth 3 (13.65->13.77) | +247 |
| Grandgues | 152 | 0.05 | 0.60 (69/turn) | cured fish 6 (25.41->34.77), bread 156 (2.42->2.83), charcoal 19 (2.71->5.37), grain 112 (2.94->3.31) | cloth 9 (11.23->12.82), tackles 2 (161.7->169.1), salt 1 (4.79->5.56), flax plants 3 (1.54->1.68) | +245 |
| Hofkirchen | 991 | 0.36 | 1.00 (116/turn) | grain 110 (2.94->4.84), thread 43 (4.46->5.13), flour 3 (22.47->25.84), wine 4 (6.98->7.79) | cloth 20 (8.61->12.82), salt 8 (4.54->5.56), dyed cloth 2 (12.6->13.77) | +232 |
| Kirchwerp | 1072 | 0.41 | 0.40 (46/turn) | thread 82 (4.46->5.7), wine 5 (6.98->9.5), casks 2 (6.14->8.31), leather 1 (23.73->27.74) | cloth 22 (7.56->12.82), dyed cloth 3 (12.6->13.77), salt 9 (4.87->5.56) | +198 |
| Darmwald | 1022 | 0.38 | 0.50 (58/turn) | thread 75 (4.46->5.18), beer 15 (3.62->5.84), tiles 2 (3.32->8.5), hides 1 (13.12->15.01) | cloth 22 (7.56->12.82), belts 1 (26.46->29.26), dyed cloth 2 (13.02->13.77), salt 8 (5.1->5.56) | +162 |

**Best:** Rouhomme at about +247 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ ?, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 16 @ min 3.26 | goal planner: sells 16 at 3.26 (v2 had 15 at 3.52) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 81.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 12.9, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 21.6) |
| grain | 9 @ 3.7, stop 36 |  | goal planner: buys 9 a turn for today's rates, keeps up to 36 (v2 had 18) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 18) |
| light armour | 1 @ 102, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 35.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 21.9k (cash + stock at home prices); +225/turn over 6 turns, -116/turn over 24 turns.
- Limits: cash flow >= -290/turn, prestige >= -0.48/turn (values are after 200 tax a turn).
- Today's settings: value +56/turn, cash +22/turn, prestige -2.08/turn - breaks the prestige floor.
- Plan: value -3/turn, cash +53/turn, prestige -0.48/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +59 vs +57, +312 vs +39, -28 vs +16.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Gosschweig: +7/turn
  - ship Flax Wyrm -> no route: +0/turn
  - ropewalk 1 0.25 -> 0.00: +11/turn
  - net maker 0.00 -> 0.29: +11/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.06: +9/turn
  - weavery 1 0.50 -> 0.60: -2/turn
  - sewing shop 1 0.30 -> 0.36: +3/turn
  - brewery 1 0.14 -> 0.21: -7/turn
  - spinnery 1 1.65 -> 1.08: -12/turn
  - retting pit 1 0.91 -> 0.61: +10/turn
- Model check over the last 59 turns: predicted +103/turn for the settings we ran, real -28/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.62, thread 4.07, cloth 6.50, flax fibres 4.82, garments 18.80, nets 29.23, beer 2.92, timber 3.24, prestige 62.50, cash 0.00
- Orders it would set: beer sell 16 (v2 15); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 8); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 18); labour buy 29 (v2 18); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.06, worth +3/turn.
- Ship linen snake: Grandgues -> Gosschweig (+7/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +80/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1898 coin: +1/turn, payback 1983 turns, doesn't pay yet (materials thin at home: limestone)

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

Buffers: flax fibres 27/77, thread 799/228, cloth 72/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.25 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
