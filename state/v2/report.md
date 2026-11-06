# v2 shadow report

Turn 13838, 2026-11-06 23:53. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,290, prestige 3,391 (271 free, -1.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 19 | 0 | 4 | 0 | 0 | min_holding 60, sell 15, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 34 | 0 | 0 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 507 | 0 | 22 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **labour**: 22 labour expired last turn (~35 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 507, not 603

## Prestige spending, cheapest coin per prestige first

563 turns left: prestige gained now converts 94.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.2 | 49.2 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 53.7 | 53.7 |  |
| jousting 3 | arena | 230 | 54.3 | 54.6 | needs a arena (build cost 26,915); thin at home: swords, protection, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 55.1 | 55.1 | thin at home: ham, stockfish, cheese |
| hold banquet 2 (fish) | mansion | 6.8 | 57.5 | 57.5 | thin at home: cheese |
| hold banquet 4 | mansion | 17.5 | 58.1 | 58.1 | thin at home: ham, stockfish, cheese |
| hold banquet 1 (meat) | mansion | 4.2 | 58.6 | 58.6 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 59.0 | 59.0 | thin at home: cheese |
| hold banquet 4 (premium) | mansion | 20 | 59.0 | 59.0 | thin at home: ham, stockfish, premium cheese |
| hold banquet 3 (pies) | mansion | 8 | 59.3 | 59.3 | thin at home: cheese |
| hold banquet 2 (pies) | mansion | 7 | 59.5 | 59.5 | thin at home: cheese |
| jousting 2 | arena | 210 | 59.5 | 59.8 | needs a arena (build cost 26,915); thin at home: swords, protection, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 15.5 (keep 14); best orders clear only 3 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 15.1 (keep 14); best orders clear only 5 a turn after crew: ship stays at 0
- best towns now: Boistot +18
- Boistot would trade: pasties buy 4 @ 11.8; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~105 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Neuborn | 780 | 0.22 | 1.00 (105/turn) | timber 27 (7.3->12.25), furniture 12 (12.5->16.62), rope 1 (80->90.25), cookware 9 (27.3->28.12) | garments 21 (23.52->26.41), cloth 24 (8.09->9.8), cured meat 17 (21->22.04), flax fibres 19 (5.25->6.05) | +235 |
| Fontaux | 411 | 0.12 | 0.60 (63/turn) | thread 47 (4.48->7.27), furniture 12 (12.5->17.48), timber 25 (7.3->10.26), glass ingots 1 (51.87->58.9) | cloth 8 (8.82->9.8), flax fibres 11 (5.51->6.05), cheese 4 (6.25->6.89), gears 1 (70.88->71.72) | +232 |
| Etallaen | 774 | 0.22 | 0.80 (84/turn) | beer 79 (3.46->5.32), furniture 12 (12.5->14.91), cured fish 6 (24.36->25.27), timber 9 (7.3->10.92) | garments 21 (25.62->26.41), candles 1 (77.17->84.5), flax fibres 9 (4.94->6.05), gears 1 (65.1->71.72) | +175 |
| Angefont | 686 | 0.19 | 0.30 (32/turn) | jewellery 5 (81.9->91.67), casks 7 (5.88->8.41), furniture 12 (12.5->13.96), glass ingots 1 (51.87->59.38) | garments 21 (24.57->26.41), flax fibres 27 (4.73->6.05), cloth 12 (8.72->9.8), tallow 1 (21->22.99) | +156 |
| Heilegg | 826 | 0.24 | 0.30 (32/turn) | lead ore 4 (12.18->18.05), furniture 12 (12.5->14.25), nets 6 (32.2->34.2), glass ingots 1 (51.87->58.9) | garments 21 (23.1->26.41), flax fibres 23 (5.25->6.05), candles 1 (79.28->84.5), cheese 4 (6.3->6.89) | +134 |

**Best:** Neuborn at about +235 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 31.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 3.46, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 19 = 4.5 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 16.7, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 22.0) |
| grain | 8 @ 3.7, stop 29 |  | goal planner: buys 8 a turn for today's rates, keeps up to 29 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 7) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 78.0) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 0 = 0.4 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 21.3k (cash + stock at home prices); +18/turn over 6 turns, -21/turn over 24 turns.
- Limits: cash flow >= -262/turn, prestige >= +1.21/turn (values are after 200 tax a turn).
- Today's settings: value +47/turn, cash +16/turn, prestige -1.56/turn - breaks the prestige floor.
- Plan: value -74/turn, cash -11/turn, prestige +1.21/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -13 vs +64, +150 vs +51, +178 vs +48.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Brunnham: +6/turn
  - ship Flax Wyrm -> Vauxvais: +1/turn
  - net maker 0.00 -> 0.29: +8/turn
  - ropewalk 1 0.25 -> 0.00: +7/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.09: +13/turn
  - weavery 1 0.50 -> 0.60: -10/turn
  - sewing shop 1 0.30 -> 0.36: +11/turn
  - spinnery 1 1.65 -> 1.10: -16/turn
  - retting pit 1 0.91 -> 0.62: +4/turn
  - flax farm 1 4.64 -> 3.03: -17/turn
- Model check over the last 61 turns: predicted +98/turn for the settings we ran, real +22/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.59, thread 4.03, cloth 6.41, flax fibres 4.85, garments 18.52, nets 28.81, beer 3.10, timber 3.53, prestige 57.74, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 8 (v2 0); labour buy 29 (v2 7); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.09, worth +5/turn.
- Ship linen snake: Grandgues -> Brunnham (+6/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Vauxvais (+1/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +79/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 437 (+148 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.93 |
| ret | 3 | 0.91 | 0.99 |
| spin | 4 | 1.65 | 1.74 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 550/228, cloth 72/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.05 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
