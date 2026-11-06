# v2 shadow report

Turn 13827, 2026-11-06 12:37. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,720, prestige 3,281 (161 free, -0.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 6 | 0 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 34 | 11 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 518 | 0 | 11 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: home ask 2.62 is above our ceiling 2.40 and last turn bought 0 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.30 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Tuning

- **tar**: home ask 11.30 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +1 crew for linen snake (crew 0.01, no projection from the game)
- labour: projection runs 100 over real use lately; planning 519, not 619

## Prestige spending, cheapest coin per prestige first

574 turns left: prestige gained now converts 94.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.1 | 50.1 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 54.3 | 54.3 | thin at home: cured fish |
| jousting 3 | arena | 230 | 54.1 | 54.3 | needs a arena (build cost 26,084); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 55.9 | 55.9 | thin at home: hop beer, wine, ham, stockfish |
| hold banquet 4 | mansion | 17.5 | 59.2 | 59.2 | thin at home: wine, hop beer, ham, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 59.4 | 59.4 | thin at home: hop beer, wine, ham, stockfish |
| hold banquet 1 (meat) | mansion | 4.2 | 59.5 | 59.5 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 59.5 | 59.5 | thin at home: wine, cured fish |
| jousting 2 | arena | 210 | 59.3 | 59.5 | needs a arena (build cost 26,084); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 60.8 | 60.8 | thin at home: wine |
| hold banquet 3 (pies) | mansion | 8 | 60.8 | 60.8 | thin at home: hop beer |
| hold sermon 2 (candles) | church | 31 | 57.0 | 61.3 | needs a church (build cost 65,533); thin at home: candles, furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: pasties buy 8 @ 15.4; crew 0.1; est +18 a turn; stock: pasties 8 @ 15.4 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 15.6 (keep 14); best orders clear only -1 a turn after crew: ship stays at 0
- best towns now: Bremcop +56, Orlesailles +52, Angefont +44, Bordees +37, Fulkirch +34
- Bremcop would trade: pasties buy 11 @ 11.9; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~104 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.60 (63/turn) | firewood 28 (2.75->7.79), timber 24 (7.3->9.69), mouldboards 1 (34.65->43.13), flour 3 (19.84->22.04) | tapestries 1 (714->798), cheese 4 (6.46->8.31), candles 1 (81.38->85.5), casks 1 (6.35->6.65) | +256 |
| Magdeach | 667 | 0.19 | 0.60 (63/turn) | tools 15 (5.35->5.98), timber 18 (7.3->10.16) | tapestries 2 (677.25->798), cheese 4 (7.46->8.31), casks 1 (5.57->6.65), nails 3 (6.41->6.6) | +246 |
| Herschweig | 775 | 0.22 | 0.10 (10/turn) | garments 10 (24->25.46), nets 2 (34.2->35.53) | tapestries 1 (609->798), cheese 4 (5.78->8.31), candles 1 (80.33->85.5), leather 1 (21.63->23.37) | +212 |
| Helmgreen | 1354 | 0.53 | 0.10 (10/turn) | cloth 1 (7.1->8.41), nets 1 (34.2->35.91), tallow 1 (22.68->23.75) | tapestries 2 (698.25->798), cheese 4 (6.56->8.31), candles 1 (82.42->85.5), casks 1 (5.46->6.65) | +204 |
| Hofkirchen | 991 | 0.33 | 0.40 (42/turn) | yarn 15 (4.64->5.7), nets 6 (34.2->36.29), mouldboards 1 (34.65->38.95) | tapestries 2 (745.5->798), cloth 21 (7.25->8.3), cheese 4 (5.78->8.31), coats 2 (71.4->75.52) | +169 |

**Best:** Grandgues at about +256 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 16 @ min 3.06 | goal planner: sells 16 at 3.06 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 14.7, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.4) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 19) |
| light armour | 1 @ 94, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 23.6k (cash + stock at home prices); +78/turn over 6 turns, +153/turn over 24 turns.
- Limits: cash flow >= -280/turn, prestige >= +5.80/turn (values are after 200 tax a turn).
- Today's settings: value +74/turn, cash +60/turn, prestige -0.81/turn - breaks the prestige floor.
- Plan: value -146/turn, cash -49/turn, prestige +3.39/turn - could not meet the prestige floor.
- Cash check (real vs predicted cash a tick, last 3): -239 vs +87, +37 vs +89, +252 vs +67.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Donaunieder: +9/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +7/turn
  - ropewalk 1 0.25 -> 0.00: -14/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.21: +21/turn
  - brewery 1 0.14 -> 0.27: -20/turn
  - spinnery 1 1.65 -> 0.92: -23/turn
  - retting pit 1 0.91 -> 0.52: -10/turn
  - flax farm 1 4.64 -> 2.60: -22/turn
  - mansion 1 0.00 -> 1.00: -163/turn
- Model check over the last 62 turns: predicted +99/turn for the settings we ran, real +59/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.17, cloth 6.67, flax fibres 4.94, garments 19.30, nets 30.06, beer 2.90, timber 3.13, prestige 10000.00, cash 0.00
- Orders it would set: beer sell 16 (v2 15); cloth sell 1 (v2 none); firewood buy 4 (v2 8); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 29 (v2 19); light armour buy 1 (v2 None); rope sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.21, worth +10/turn.
- Ship linen snake: Grandgues -> Donaunieder (+9/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +82/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 454 (+165 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 5.31 |
| ret | 3 | 0.91 | 1.06 |
| spin | 4 | 1.65 | 1.88 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 468/228, cloth 73/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 5.95 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
