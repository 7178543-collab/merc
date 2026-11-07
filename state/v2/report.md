# v2 shadow report

Turn 13839, 2026-11-07 00:59. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,287, prestige 3,389 (269 free, -1.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 15 | 0 | 4 | 0 | 0 | min_holding 60, sell 15, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 4, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 34 | 0 | 0 | 0 | 0 | stop 29, buy 8, buy @ 3.7 |
| labour | 29 | 29 | 503 | 0 | 26 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 4 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.30 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 26 labour expired last turn (~42 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.30 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 503, not 600

## Prestige spending, cheapest coin per prestige first

562 turns left: prestige gained now converts 94.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.9 | 48.9 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 53.7 | 53.7 |  |
| jousting 3 | arena | 230 | 54.3 | 54.5 | needs a arena (build cost 26,548); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 54.7 | 54.7 | thin at home: ham, stockfish, cheese, pies |
| hold banquet 3 (pies) | mansion | 8 | 57.3 | 57.3 | thin at home: cheese, pies |
| hold banquet 2 (pies) | mansion | 7 | 57.4 | 57.4 | thin at home: cheese, pies |
| hold banquet 4 | mansion | 17.5 | 58.3 | 58.3 | thin at home: ham, stockfish, cheese |
| hold banquet 2 (fish) | mansion | 6.8 | 58.4 | 58.4 | thin at home: cheese |
| hold banquet 1 (meat) | mansion | 4.2 | 58.8 | 58.8 |  |
| hold banquet 4 (premium) | mansion | 20 | 59.0 | 59.0 | thin at home: ham, stockfish, premium cheese |
| jousting 2 | arena | 210 | 59.5 | 59.7 | needs a arena (build cost 26,548); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 59.9 | 59.9 | thin at home: cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 5 @ 15.5 (keep 14); best orders clear only 6 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 5 @ 15.4 (keep 14); best orders clear only 7 a turn after crew: ship stays at 0
- best towns now: Bordees +21, Bedenis +17, Clarfranche +16, Clairlond +16, Corstoft +16
- Bordees would trade: pasties buy 5 @ 12.5; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~108 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Neuborn | 780 | 0.23 | 1.00 (108/turn) | timber 28 (7.3->12.25), gold ore 1 (154.35->183.35), furniture 12 (16.07->17.86), raw cloth 3 (7.51->9.07) | garments 20 (23.52->26.22), cloth 13 (8.19->11.7), cheese 6 (5.25->7.93), cured meat 14 (21->22.04) | +219 |
| Fontaux | 411 | 0.12 | 0.60 (65/turn) | thread 56 (4.66->7.27), furniture 12 (16.07->18.52), timber 24 (7.3->9.97), glass ingots 1 (56.18->57.95) | cloth 6 (9.55->11.7), cheese 6 (6.2->7.93), steel ingots 1 (12.92->15.01), gears 1 (70.35->71.72) | +205 |
| Rotterburg | 1056 | 0.38 | 0.20 (22/turn) | glass ingots 1 (56.18->58.9) | cloth 24 (7.19->11.7), garments 20 (23.94->26.22), cheese 5 (6.3->7.93), salt 4 (4.07->5.27) | +150 |
| Vauxvais | 204 | 0.06 | 0.20 (22/turn) | premium cheese 1 (32.13->34.01), logs 1 (3.93->5.89) | cloth 17 (7.88->11.7), bricks 8 (4.85->9.4), thread 31 (4.43->5.1), cheese 6 (6.3->7.93) | +138 |
| Angefont | 686 | 0.20 | 0.30 (32/turn) | premium cheese 1 (32.13->37.24), glass ingots 1 (56.18->59.85), thread 56 (4.66->4.89), wool 2 (9.19->9.45) | cloth 18 (8.61->11.7), garments 20 (23.52->26.22), flax fibres 27 (4.73->5.65), cheese 6 (6.93->7.93) | +134 |

**Best:** Neuborn at about +219 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 26.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 11 @ min 3.06 | goal planner: sells 11 a turn at 3.06, keeps 60 (no one offered it) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 15.7, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 21.0) |
| grain | 8 @ 3.7, stop 29 |  | goal planner: buys 8 a turn for today's rates, keeps up to 29 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 3) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 22.0k (cash + stock at home prices); +159/turn over 6 turns, -1/turn over 24 turns.
- Limits: cash flow >= -262/turn, prestige >= +1.27/turn (values are after 200 tax a turn).
- Today's settings: value +53/turn, cash +23/turn, prestige -1.55/turn - breaks the prestige floor.
- Plan: value -74/turn, cash -65/turn, prestige +1.27/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +150 vs +51, +178 vs +48, -3 vs +16.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Brunnham: +4/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.28: +8/turn
  - ropewalk 1 0.25 -> 0.00: +5/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.11: +12/turn
  - flax farm 1 4.64 -> 3.86: -2/turn
  - retting pit 1 0.91 -> 0.79: -0/turn
  - spinnery 1 1.65 -> 1.39: +4/turn
  - weavery 1 0.50 -> 0.61: -5/turn
  - sewing shop 1 0.30 -> 0.36: +7/turn
- Model check over the last 60 turns: predicted +97/turn for the settings we ran, real +32/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.63, thread 4.14, cloth 6.58, flax fibres 4.97, garments 19.00, nets 29.51, beer 3.14, timber 3.40, prestige 58.23, cash 0.00
- Orders it would set: beer sell 11 (v2 none); cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 8 (v2 0); labour buy 29 (v2 3); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.11, worth +5/turn.
- Ship linen snake: Grandgues -> Brunnham (+4/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +81/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 436 (+147 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.90 |
| ret | 3 | 0.91 | 0.98 |
| spin | 4 | 1.65 | 1.73 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 556/228, cloth 72/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
- R5: flax fibres buy not filling: bid 5.05 under the home ask 5.65 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
