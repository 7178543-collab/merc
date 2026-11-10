# v2 shadow report

Turn 13912, 2026-11-10 01:57. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,677, prestige 3,480 (360 free, -2.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 40 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 500 | 0 | 29 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 12.40 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 29 labour expired last turn (~44 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 12.40 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +2 crew for Flax Wyrm (crew 0.04, no projection from the game)
- labour: projection runs 100 over real use lately; planning 503, not 603

## Prestige spending, cheapest coin per prestige first

489 turns left: prestige gained now converts 91.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 46.5 | 46.5 | running |
| hold banquet 4 (pies) | mansion | 18 | 54.3 | 54.3 | thin at home: pasties, ham, stockfish |
| hold banquet 1 (fish) | mansion | 4.2 | 55.8 | 55.8 | thin at home: beer |
| hold banquet 4 (premium) | mansion | 20 | 55.9 | 55.9 | thin at home: ham, stockfish, premium cheese |
| jousting 3 | arena | 230 | 56.0 | 56.3 | needs a arena (build cost 26,836); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 56.5 | 56.5 | thin at home: ham, stockfish, cheese |
| hold banquet 2 (fish) | mansion | 6.8 | 56.8 | 56.8 | thin at home: cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 57.8 | 57.8 | thin at home: cheese |
| hold banquet 3 (pies) | mansion | 8 | 59.9 | 59.9 | thin at home: pasties, cheese |
| hold banquet 2 (pies) | mansion | 7 | 60.7 | 60.7 | thin at home: pasties, cheese |
| jousting 2 | arena | 210 | 61.3 | 61.6 | needs a arena (build cost 26,836); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold feast 2 | townhouse | 2.6 | 57.1 | 65.0 | needs a townhouse (build cost 9,560) |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: pasties buy 11 @ 14.5; crew 0.1; est +38 a turn; stock: pasties 11 @ 14.5 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 16.0 (keep 14); best orders clear only -1 a turn after crew: ship stays at 0
- best towns now: Disscester +49, Friedwerp +46, Chatgnan +45, Clarfranche +43, Bedenis +40
- Disscester would trade: furniture buy 3 @ 14.6, pasties buy 10 @ 14.5; crew 0.3

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~100 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Kirchwerp | 1072 | 0.36 | 0.60 (60/turn) | furniture 10 (11.55->22.23), thread 96 (4.66->5.7), garments 10 (18.63->21.28), nails 2 (7.82->12.35) | candles 1 (77.7->85.5), dyed cloth 14 (12.08->12.73), flax fibres 27 (5.72->6.6), chisels 1 (8.4->9.59) | +213 |
| Rouhomme | 368 | 0.10 | 0.60 (60/turn) | bread 155 (2.21->3.13), furniture 10 (11.55->15.39), garments 10 (18.63->22.04), cloth 1 (6.35->7.6) | flax fibres 8 (4.94->6.6), tools 17 (4.85->5.56), bricks 1 (7.61->13.39), cloth 6 (8.56->9.25) | +205 |
| Pontmont | 341 | 0.09 | 0.70 (70/turn) | bread 155 (2.21->2.98), garments 10 (18.63->22.8), charcoal 19 (2.44->4.62), furniture 10 (11.55->14.63) | candles 1 (84->85.5), flax fibres 5 (6.3->6.6), bricks 1 (11.34->13.39), flax plants 1 (1.3->1.73) | +198 |
| Grandgues | 152 | 0.04 | 0.40 (40/turn) | charcoal 19 (2.44->6.13), beer 59 (4.16->5.18), garments 10 (18.63->21.47), furniture 10 (11.55->13.39) | cured meat 4 (26.25->27.93), tools 9 (4.83->5.56), candles 1 (80.33->85.5), bricks 1 (8.98->13.39) | +191 |
| Fontaux | 411 | 0.11 | 1.00 (100/turn) | thread 68 (4.66->5.65), bread 120 (2.21->2.98), timber 19 (8.72->12.63), charcoal 14 (2.44->3.97) | candles 0 (80.85->85.5), cured meat 2 (27.09->27.93), seeds 3 (2.54->2.94), flax plants 4 (1.47->1.73) | +183 |

**Best:** Kirchwerp at about +213 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had None) |
| beer |  | 16 @ min 3.26 | goal planner: sells 16 a turn at 3.26, keeps 60 (no one offered it) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 11.3, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 24.2) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 3) |
| light armour | 1 @ 111, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 39.2) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 27.6k (cash + stock at home prices); +248/turn over 6 turns, +182/turn over 24 turns.
- Limits: cash flow >= -320/turn, prestige >= -0.25/turn (values are after 200 tax a turn).
- Today's settings: value +94/turn, cash +77/turn, prestige -2.01/turn - breaks the prestige floor.
- Plan: value -1/turn, cash +3/turn, prestige -0.25/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +93 vs +76, +142 vs +76, -17 vs +72.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Dortgart: +4/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +8/turn
  - flax farm 1 4.64 -> 5.38: -5/turn
  - retting pit 1 0.91 -> 1.05: -1/turn
  - spinnery 1 1.65 -> 1.86: +7/turn
  - weavery 1 0.50 -> 0.60: -10/turn
  - sewing shop 1 0.30 -> 0.36: +14/turn
  - ropewalk 1 0.25 -> 0.00: -15/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.18: +25/turn
- Model check over the last 59 turns: predicted +104/turn for the settings we ran, real +68/turn.
- Worth of one more unit per turn: labour 1.55, thread 3.90, cloth 6.22, flax fibres 4.62, garments 18.00, nets 28.34, beer 2.92, timber 3.96, prestige 67.91, cash 0.00
- Orders it would set: arms buy 1 (v2 None); beer sell 16 (v2 none); cloth sell 1 (v2 none); firewood buy 2 (v2 3); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 0); labour buy 29 (v2 3); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.18, worth +10/turn.
- Ship linen snake: Grandgues -> Dortgart (+4/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +78/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1847 coin: +5/turn, payback 393 turns, doesn't pay yet (materials thin at home: limestone)

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

Buffers: flax fibres 27/77, thread 976/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask none (no sellers at home)
- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.6 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
