# v2 shadow report

Turn 13766, 2026-11-03 23:28. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 8,071, prestige 3,182 (62 free, -0.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 14 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.4 |
| grain | 33 | 6 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 518 | 0 | 11 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.90 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Tuning

- **tar**: home ask 11.90 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +7 crew for Flax Wyrm (crew 0.13, no projection from the game)
- labour: projection runs 100 over real use lately; planning 525, not 625

## Prestige spending, cheapest coin per prestige first

635 turns left: prestige gained now converts 95.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.6 | 48.6 | running |
| hold banquet 4 (pies) | mansion | 18 | 51.3 | 51.3 | thin at home: hop beer, stockfish, candles |
| jousting 3 | arena | 230 | 53.4 | 53.6 | needs a arena (build cost 24,903); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 54.1 | 54.1 |  |
| hold banquet 4 | mansion | 17.5 | 54.2 | 54.2 | thin at home: hop beer, ham, stockfish, candles |
| hold banquet 4 (premium) | mansion | 20 | 54.5 | 54.5 | thin at home: hop beer, stockfish, candles |
| hold banquet 3 (pies) | mansion | 8 | 55.0 | 55.0 | thin at home: hop beer, pies, candles |
| hold banquet 3 (fish) | mansion | 7.6 | 57.1 | 57.1 | thin at home: hop beer |
| hold banquet 2 (pies) | mansion | 7 | 57.3 | 57.3 | thin at home: pies, candles |
| hold banquet 2 (fish) | mansion | 6.8 | 58.2 | 58.2 |  |
| jousting 2 | arena | 210 | 58.5 | 58.7 | needs a arena (build cost 24,903); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| jousting 1 | arena | 170 | 60.0 | 60.2 | needs a arena (build cost 24,903); thin at home: protection, light armour, arms; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 20 @ 13.8, pasties buy 2 @ 14.0; crew 0.2; est +241 a turn; stock: furniture 20 @ 13.8 (keep 145); stock: pasties 2 @ 14.0 (keep 14)
- **linen snake** on Grandgues: pasties buy 6 @ 13.9; crew 0.1; est +20 a turn; stock: pasties 6 @ 13.9 (keep 14)
- best towns now: Chatgnan +539, Pontmont +528, Amsdermund +508, Bordetes +485, Heilegg +483
- Chatgnan would trade: furniture buy 46 @ 13.8; crew 0.4

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~102 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Heilegg | 826 | 0.23 | 0.60 (61/turn) | looms 1 (614.25->698.25), grindstones 1 (241.5->296.4), cured fish 7 (22.68->25.65), charcoal 18 (2.1->4.05) | cloth 21 (7.46->8.8), thread 39 (4.62->5.05), garments 2 (20.48->23.4), cookware 7 (23.1->23.94) | +196 |
| Grandgues | 152 | 0.04 | 0.50 (51/turn) | charcoal 18 (2.1->6.08), bread 149 (2.23->2.41), limestone 3 (17.22->21.47), timber 25 (7.93->8.88) | bricks 8 (6.72->8.12), wine 12 (6.25->6.6), beer 4 (3.36->3.84), cloth 5 (8.29->8.8) | +115 |
| Hanstein | 380 | 0.10 | 0.40 (41/turn) | timber 16 (7.93->11.21), chisels 2 (8.56->9.79), logs 1 (3.91->6.98), tiles 4 (2.1->3.34) | cloth 24 (7.25->8.8), gold ore 1 (147->179.55), garments 2 (20.89->23.4), thread 49 (4.85->5.05) | +115 |
| Blanans | 297 | 0.08 | 0.70 (72/turn) | bread 149 (2.23->2.56), charcoal 18 (2.1->3.29), limestone 3 (17.22->23.75), tiles 4 (2.1->3.84) | cloth 24 (7.3->8.8), gold ore 1 (158.55->179.55), garments 2 (20.37->23.4), mouldboards 3 (38.22->40.28) | +115 |
| Neuborn | 780 | 0.21 | 0.50 (51/turn) | charcoal 18 (2.1->5.65), tools 20 (5.25->5.7), acid 1 (132.3->133), beer 15 (3.46->3.91) | cloth 24 (6.67->8.8), thread 14 (4.3->5.05), garments 2 (20.37->23.4), cheese 10 (6.41->6.84) | +101 |

**Best:** Heilegg at about +196 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 28.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 16 @ min 3.06 | goal planner: sells 16 at 3.06 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 79, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 7.1 | goal planner: sells 1 a turn at 7.1, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 1 @ min 1.34 | goal planner: trial sale of an idle pile, 1 a turn at 1.34, keeps 219 (7 over) |
| furniture | 2 @ 15.3, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.4 | goal planner: sells 11 at 19.4 (v2 had 10 at 22.4) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 25) |
| light armour | 1 @ 88.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 37.2) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.4/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 20.0k (cash + stock at home prices); +176/turn over 6 turns, +96/turn over 24 turns.
- Limits: cash flow >= -170/turn, prestige >= +9.93/turn (values are after 200 tax a turn).
- Today's settings: value +110/turn, cash +111/turn, prestige -0.31/turn - breaks the prestige floor.
- Plan: value -126/turn, cash -121/turn, prestige +3.89/turn - could not meet the prestige floor.
- Cash check (real vs predicted cash a tick, last 3): +62 vs +98, +101 vs +101, -36 vs +102.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Herschweig: +1/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +3/turn
  - flax farm 1 4.64 -> 4.56: +1/turn
  - sewing shop 1 0.30 -> 0.37: -9/turn
  - weavery 1 0.50 -> 0.61: +11/turn
  - ropewalk 1 0.25 -> 0.00: -14/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.34: +17/turn
  - brewery 1 0.14 -> 0.27: -17/turn
  - mansion 1 0.00 -> 1.00: -228/turn
- Model check over the last 58 turns: predicted +71/turn for the settings we ran, real +99/turn.
- Worth of one more unit per turn: labour 1.62, thread 4.07, cloth 6.50, flax fibres 4.82, garments 18.80, nets 29.26, beer 2.79, timber 3.06, prestige 10000.00, cash 0.00
- Orders it would set: beer sell 16 (v2 15); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 5); flax plants sell 1 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 29 (v2 25); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.34, worth +15/turn.
- Ship linen snake: Grandgues -> Herschweig (+1/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +81/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.3/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 505 (+216 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 6.45 |
| ret | 3 | 0.91 | 1.29 |
| spin | 4 | 1.65 | 2.28 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 260/228, cloth 81/128

## Self-diagnosis

- R5: tar buy not filling: bid 11 under the home ask 11.9 for 6 turns, bought 0.0 of 1, 0.0 held (0.0 turns); raise needs Taylor (ceiling 11.0)
