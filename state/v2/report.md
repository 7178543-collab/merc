# v2 shadow report

Turn 13837, 2026-11-06 22:48. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,112, prestige 3,393 (273 free, -1.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 23 | 0 | 4 | 0 | 0 | min_holding 60, sell 15, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 34 | 0 | 0 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 512 | 0 | 17 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **labour**: 17 labour expired last turn (~27 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 512, not 612

## Prestige spending, cheapest coin per prestige first

564 turns left: prestige gained now converts 94.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.2 | 49.2 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 53.7 | 53.7 |  |
| jousting 3 | arena | 230 | 54.5 | 54.7 | needs a arena (build cost 25,966); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 55.3 | 55.3 | thin at home: ham, stockfish, cheese, pies |
| hold banquet 2 (fish) | mansion | 6.8 | 57.5 | 57.5 | thin at home: cheese |
| hold banquet 4 | mansion | 17.5 | 57.6 | 57.6 | thin at home: ham, stockfish, cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 57.8 | 57.8 | thin at home: cheese |
| hold banquet 1 (meat) | mansion | 4.2 | 58.3 | 58.3 |  |
| hold banquet 4 (premium) | mansion | 20 | 58.7 | 58.7 | thin at home: ham, stockfish |
| jousting 2 | arena | 210 | 59.6 | 59.9 | needs a arena (build cost 25,966); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 3 (meat) | mansion | 7.6 | 60.6 | 60.6 | thin at home: cheese |
| hold banquet 2 (meat) | mansion | 6.8 | 60.7 | 60.7 | thin at home: cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 10 | 151802239 | 0.132 | - | pasties 9 | -139 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 15.5 (keep 14); best orders clear only -0 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 16.0 (keep 14); best orders clear only -2 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~104 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Fontaux | 411 | 0.12 | 0.60 (63/turn) | thread 47 (4.24->7.27), timber 24 (7.93->11.4), wool 1 (6.83->11.69), nets 2 (32.2->33.06) | cloth 7 (8.35->9.55), cheese 7 (6.25->6.98), flax fibres 3 (4.94->5.85), copper ingots 1 (17.85->18.71) | +194 |
| Neuborn | 780 | 0.22 | 1.00 (104/turn) | timber 27 (7.93->12.25), nets 1 (32.2->38), seeds 12 (2.65->3.32), wine 12 (7.3->7.6) | garments 21 (23.52->26.79), cloth 24 (7.88->9.55), cheese 7 (5.25->6.98), cured meat 17 (21->21.66) | +165 |
| Etallaen | 774 | 0.22 | 0.40 (42/turn) | beer 73 (3.46->5.32), wool 1 (6.83->9.17), casks 2 (5.88->6.65), grain 2 (2.56->3.5) | gears 1 (66.67->71.72), flax fibres 7 (4.94->5.85) | +117 |
| Clarfranche | 1484 | 0.61 | 0.40 (42/turn) | nets 6 (32.2->36.67), jewellery 5 (79.8->83.12), lead ore 3 (13.23->18.62), paper 1 (19.84->21.09) | garments 21 (23.1->26.79), cloth 16 (8.61->9.55), cheese 7 (6.09->6.98), pies 2 (15.02->16.91) | +115 |
| Bremcop | 1326 | 0.52 | 0.20 (21/turn) | nets 6 (32.2->36.29), thread 17 (4.24->4.94), wool 1 (6.83->7.84) | garments 21 (23.1->26.79), gears 1 (66.67->71.72), cheese 7 (6.35->6.98) | +93 |

**Best:** Fontaux at about +194 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 27.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 3.46, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 23 = 5.5 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 16.7, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 24.4) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 12) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 79.5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.3/turn (ropewalk 1), makes 0.0, holds 0 = 1.2 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 21.5k (cash + stock at home prices); -470/turn over 6 turns, -13/turn over 24 turns.
- Limits: cash flow >= -255/turn, prestige >= +1.14/turn (values are after 200 tax a turn).
- Today's settings: value +62/turn, cash +48/turn, prestige -1.57/turn - breaks the prestige floor.
- Plan: value -51/turn, cash +71/turn, prestige +1.14/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +64 vs +68, -13 vs +64, +150 vs +51.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Brunnham: +6/turn
  - ship Flax Wyrm -> Clairlond: +3/turn
  - net maker 0.00 -> 0.29: +8/turn
  - ropewalk 1 0.25 -> 0.00: +7/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.08: +12/turn
  - weavery 1 0.50 -> 0.60: -10/turn
  - sewing shop 1 0.30 -> 0.36: +12/turn
  - brewery 1 0.14 -> 0.19: -10/turn
  - spinnery 1 1.65 -> 1.00: -16/turn
  - retting pit 1 0.91 -> 0.57: +2/turn
- Model check over the last 60 turns: predicted +97/turn for the settings we ran, real +25/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.58, thread 3.96, cloth 6.33, flax fibres 4.69, garments 18.30, nets 28.45, beer 2.85, timber 3.21, prestige 56.16, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 2 (v2 3); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 0); labour buy 29 (v2 12); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.08, worth +5/turn.
- Ship linen snake: Grandgues -> Brunnham (+6/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Clairlond (+3/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +78/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 436 (+147 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.91 |
| ret | 3 | 0.91 | 0.98 |
| spin | 4 | 1.65 | 1.73 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 553/228, cloth 72/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask none (no sellers at home)
- R5: flax fibres buy not filling: bid 5.05 under the home ask 5.85 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
