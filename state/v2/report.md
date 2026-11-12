# v2 shadow report

Turn 13967, 2026-11-12 08:34. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,201, prestige 3,555 (435 free, -2.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 0 | 0 | 3 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 36 | 0 | 2 | 0 | 0 | min_holding 30, sell 10, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 18, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 511 | 0 | 18 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **beer**: needed (2.6/turn) but there is NO buy order, stock 0.0 -> v2: add buy 5
- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 4.02 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 4.02 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **labour**: 18 labour expired last turn (~30 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 511, not 607

## Prestige spending, cheapest coin per prestige first

434 turns left: prestige gained now converts 88.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.2 | 49.2 | running |
| hold banquet 4 (pies) | mansion | 18 | 53.1 | 53.1 | thin at home: pasties, ham, stockfish |
| jousting 3 | arena | 230 | 55.3 | 55.6 | needs a arena (build cost 26,613); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 56.6 | 56.6 | thin at home: pasties |
| hold banquet 4 | mansion | 17.5 | 56.6 | 56.6 | thin at home: ham, stockfish |
| hold banquet 1 (fish) | mansion | 4.2 | 57.2 | 57.2 |  |
| hold banquet 2 (pies) | mansion | 7 | 57.6 | 57.6 | thin at home: pasties |
| hold banquet 4 (premium) | mansion | 20 | 59.1 | 59.1 | thin at home: ham, stockfish, premium cheese |
| jousting 2 | arena | 210 | 60.6 | 60.9 | needs a arena (build cost 26,613); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 62.3 | 62.3 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 62.6 | 62.6 |  |
| hold banquet 1 (meat) | mansion | 4.2 | 66.2 | 66.2 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 15.9 (keep 14); best orders clear only -5 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 5 @ 15.6 (keep 14); best orders clear only 6 a turn after crew: ship stays at 0
- best towns now: Orlesailles +30, Herschweig +28, Clarfranche +20, Neuborn +16
- Orlesailles would trade: pasties buy 5 @ 10.7; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~106 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Neuborn | 780 | 0.22 | 1.00 (106/turn) | tapestries 0 (735->826.5), timber 26 (7.61->12.54), garments 9 (18.86->22.04), wine 12 (7.51->9.88) | cloth 6 (8.66->10.7), flax fibres 4 (6.77->9.5), coats 1 (74.55->79.33), seeds 7 (2.56->3.13) | +230 |
| Grandgues | 152 | 0.04 | 0.90 (95/turn) | firewood 43 (4.22->7.65), thread 14 (5.5->6.93), garments 10 (18.86->20.52), timber 26 (7.61->8.74) | cloth 11 (8.45->10.7), flax fibres 3 (7.72->9.5), cured meat 3 (23.31->23.75), jewellery 1 (114.45->114.95) | +190 |
| Angefont | 686 | 0.19 | 0.30 (32/turn) | garments 10 (18.86->20.71), yarn 6 (4.75->7.03), pies 3 (14.8->18.9), rope 1 (74.5->84.08) | cloth 14 (8.09->10.7), thread 62 (4.91->5.6), flax fibres 8 (5.51->9.5), seeds 8 (2.14->3.13) | +154 |
| Hanstein | 380 | 0.11 | 0.30 (32/turn) | garments 10 (18.86->21.28), timber 12 (7.61->10.16), steel ingots 3 (22.26->25.46), rope 1 (74.5->77.42) | cloth 16 (8.45->10.7), flax fibres 8 (5.67->9.5), thread 29 (4.68->5.6), seeds 8 (1.81->3.13) | +144 |
| Pontmont | 341 | 0.10 | 0.40 (42/turn) | limestone 4 (19.01->38), garments 10 (18.86->20.9), pies 3 (14.8->20.71), bricks 5 (8.93->12.16) | flax fibres 5 (6.51->9.5), cloth 9 (9.92->10.7), cheese 4 (6.51->7.12), wrought iron 4 (15.23->15.86) | +142 |

**Best:** Neuborn at about +230 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 35.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 3.78, stop 6 |  | uses 2.6/turn (household upkeep), makes 0.0, holds 0 = 0.0 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 87, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.14 | goal planner: sells 2 a turn at 1.14, keeps 219 (no one offered it) |
| furniture | 2 @ 14.3, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.4) |
| grain | 6 @ 3.7, stop 21 |  | goal planner: buys 6 a turn for today's rates, keeps up to 21 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 11) |
| light armour | 1 @ 108, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 36.4) |
| pasties |  | 1 @ min 13.3 | goal planner: trial sale of an idle pile, 1 a turn at 13.3, keeps 0 (9 over) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 72.5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 0 = 0.4 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 27.8k (cash + stock at home prices); +249/turn over 6 turns, -35/turn over 24 turns.
- Limits: cash flow >= -300/turn, prestige >= -0.56/turn (values are after 200 tax a turn).
- Today's settings: value +35/turn, cash +41/turn, prestige -2.83/turn - breaks the prestige floor.
- Plan: value -49/turn, cash +3/turn, prestige -0.56/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +404 vs +105, +141 vs +79, +848 vs +86.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> no route: +0/turn
  - ship Flax Wyrm -> no route: +0/turn
  - brewery 1 0.14 -> 0.09: +11/turn
  - spinnery 1 1.65 -> 1.36: +8/turn
  - ropewalk 1 0.25 -> 0.00: +13/turn
  - net maker 0.00 -> 0.29: +12/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.09: +4/turn
  - retting pit 1 0.91 -> 0.83: -2/turn
  - flax farm 1 4.64 -> 4.20: -4/turn
  - weavery 1 0.50 -> 0.59: -1/turn
- Model check over the last 61 turns: predicted +107/turn for the settings we ran, real +28/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.64, thread 4.12, cloth 6.58, flax fibres 4.88, garments 19.04, nets 29.73, beer 3.17, timber 3.26, prestige 64.71, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 6 (v2 0); labour buy 29 (v2 11); light armour buy 1 (v2 None); pasties sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.09, worth +3/turn.
- Ship linen snake: Grandgues -> no route (+0/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +81/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1802 coin: +2/turn, payback 1026 turns, doesn't pay yet

## Chain sizing

Mode HOLD, garments sold 10.0/turn (+0.0 exported); plan makes 32.4 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 406 (+116 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 3.59 |
| ret | 3 | 0.91 | 0.72 |
| spin | 4 | 1.65 | 1.67 |
| weave | 3 | 0.50 | 1.27 |
| sew | 2 | 0.30 | 0.79 |

Buffers: flax fibres 159/77, thread 1050/227, cloth 72/127

## Self-diagnosis

- R1: beer slot dry: 0.0 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy none, home ask 3.6 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 9 @ 3.66 (ask 3.6, cap 5.7))
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 4.02; ask over the cap 2.1 (60 coin per prestige)
