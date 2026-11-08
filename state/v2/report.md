# v2 shadow report

Turn 13877, 2026-11-08 14:24. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,642, prestige 3,550 (430 free, -2.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 7 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 9 | 9 | 9 | 0 | 0 | stop 36, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 518 | 0 | 11 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.30 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Tuning

- **tar**: home ask 11.30 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 518, not 618

## Prestige spending, cheapest coin per prestige first

524 turns left: prestige gained now converts 92.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 52.2 | 52.2 | running |
| hold banquet 4 (pies) | mansion | 18 | 55.5 | 55.5 | thin at home: wine, ham, stockfish |
| jousting 3 | arena | 230 | 55.4 | 55.6 | needs a arena (build cost 26,442); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 55.9 | 55.9 |  |
| hold banquet 4 (premium) | mansion | 20 | 58.0 | 58.0 | thin at home: wine, ham, stockfish |
| hold banquet 4 | mansion | 17.5 | 58.1 | 58.1 | thin at home: wine, ham, stockfish |
| hold banquet 1 (meat) | mansion | 4.2 | 60.7 | 60.7 | thin at home: cured meat |
| jousting 2 | arena | 210 | 60.6 | 60.9 | needs a arena (build cost 26,442); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 61.9 | 61.9 | thin at home: wine |
| hold banquet 3 (fish) | mansion | 7.6 | 62.6 | 62.6 |  |
| hold banquet 3 (pies) | mansion | 8 | 62.7 | 62.7 |  |
| hold sermon 2 (candles) | church | 31 | 57.9 | 62.9 | needs a church (build cost 67,681); thin at home: furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 16.4 (keep 14); best orders clear only -1 a turn after crew: ship stays at 0
- best towns now: Chatgnan +465, Gotthafen +344, Donaunieder +330, Essenbrucke +311, Clairlond +289
- Chatgnan would trade: furniture buy 39 @ 13.7, pasties buy 5 @ 16.4; crew 0.4

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~108 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Fontaux | 411 | 0.12 | 0.80 (86/turn) | garments 10 (19.42->30.02), thread 75 (4.38->5.65), firewood 21 (2.25->6.74), hop beer 1 (11.23->14.15) | salt 7 (4.54->5.56), axes 1 (18.17->19.57), malt 1 (8.14->9.31), flax plants 2 (1.21->1.61) | +223 |
| Pontmont | 341 | 0.10 | 0.80 (86/turn) | bread 151 (2.5->3.12), grain 114 (2.96->3.46), garments 10 (19.42->22.8), rope 3 (84->91.2) | malt 1 (7.3->9.31), salt 7 (5.3->5.56) | +191 |
| Grandgues | 152 | 0.04 | 0.70 (75/turn) | firewood 31 (2.25->6.55), bread 151 (2.5->2.83), furniture 9 (12.92->16.15), garments 10 (19.42->21.47) | salt 4 (5.02->5.56), axes 1 (19.01->19.57), cloth 9 (8.29->8.4), flour 1 (19.95->20.9) | +187 |
| Rouhomme | 368 | 0.11 | 0.80 (86/turn) | grain 114 (2.96->3.78), bread 151 (2.5->2.98), garments 10 (19.42->21.85), furniture 9 (12.92->15.2) | cookware 6 (23.31->24.13), garments 2 (24.78->25.4), flax fibres 3 (5.72->6) | +151 |
| Heilegg | 826 | 0.24 | 0.20 (22/turn) | garments 10 (19.42->22.99), nets 6 (33.8->38), casks 6 (6.56->9.17), hides 3 (11.55->12.35) | premium cheese 2 (21.63->30.59), cloth 24 (7.56->8.4), cookware 6 (21.63->24.13), cheese 4 (5.78->7.12) | +122 |

**Best:** Fontaux at about +223 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 31.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 16 @ min 3.26 | goal planner: sells 16 at 3.26 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 71.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 12.6, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 24.8) |
| grain | 9 @ 3.7, stop 36 |  | goal planner: buys 9 a turn for today's rates, keeps up to 36 (v2 had 18) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 18) |
| light armour | 1 @ 98.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 20.5k (cash + stock at home prices); -309/turn over 6 turns, -127/turn over 24 turns.
- Limits: cash flow >= -277/turn, prestige >= -0.54/turn (values are after 200 tax a turn).
- Today's settings: value +80/turn, cash +60/turn, prestige -2.16/turn - breaks the prestige floor.
- Plan: value +16/turn, cash +79/turn, prestige -0.54/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +461 vs +60, +115 vs +67, +279 vs +53.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> no route: +0/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +7/turn
  - ropewalk 1 0.25 -> 0.00: -6/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.15: +20/turn
  - sewing shop 1 0.30 -> 0.36: -8/turn
  - weavery 1 0.50 -> 0.60: +8/turn
  - brewery 1 0.14 -> 0.20: -8/turn
  - spinnery 1 1.65 -> 1.06: -11/turn
  - retting pit 1 0.91 -> 0.60: +9/turn
- Model check over the last 59 turns: predicted +103/turn for the settings we ran, real -37/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.57, thread 3.98, cloth 6.33, flax fibres 4.79, garments 18.27, nets 28.64, beer 2.89, timber 3.33, prestige 59.65, cash 0.00
- Orders it would set: beer sell 16 (v2 15); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 8); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 18); labour buy 29 (v2 18); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.15, worth +7/turn.
- Ship linen snake: Grandgues -> no route (+0/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +78/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

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

Buffers: flax fibres 27/77, thread 721/228, cloth 72/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.0 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
