# v2 shadow report

Turn 13959, 2026-11-12 00:40. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,749, prestige 3,575 (455 free, -2.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 14 | 9 | 4 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 26, buy 9, buy @ 3.44 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 34 | 0 | 2 | 0 | 0 | min_holding 30, sell 10, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 18, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.60 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~76 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.60 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +6 crew for Flax Wyrm (crew 0.12, no projection from the game)
- labour: +2 crew for linen snake (crew 0.04, no projection from the game)
- labour: projection runs 100 over real use lately; planning 492, not 592

## Prestige spending, cheapest coin per prestige first

442 turns left: prestige gained now converts 89.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.1 | 50.1 | running |
| jousting 3 | arena | 230 | 54.9 | 55.2 | needs a arena (build cost 26,461); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 55.4 | 55.4 | thin at home: wine, ham, stockfish, pies |
| hold banquet 1 (fish) | mansion | 4.2 | 56.8 | 56.8 |  |
| hold banquet 4 (premium) | mansion | 20 | 58.4 | 58.4 | thin at home: wine, ham, stockfish |
| hold banquet 4 | mansion | 17.5 | 58.5 | 58.5 | thin at home: wine, ham, stockfish |
| jousting 2 | arena | 210 | 60.1 | 60.4 | needs a arena (build cost 26,461); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 60.8 | 60.8 | thin at home: pies |
| hold banquet 1 (meat) | mansion | 4.2 | 61.0 | 61.0 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 61.2 | 61.2 | thin at home: wine |
| hold banquet 2 (pies) | mansion | 7 | 61.9 | 61.9 | thin at home: wine, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 62.3 | 62.3 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: furniture buy 25 @ 14.6, pasties buy 4 @ 15.4; crew 0.1; est +298 a turn; stock: furniture 25 @ 14.6 (keep 145); stock: pasties 4 @ 15.4 (keep 14)
- **Flax Wyrm** on Caillechâtel: furniture buy 20 @ 13.8, pasties buy 6 @ 12.1; crew 0.2; est +272 a turn; stock: furniture 20 @ 13.8 (keep 145); stock: pasties 6 @ 12.1 (keep 14)
- best towns now: Bedenis +312, Donaunieder +303, Grandgues +298, Heidlowe +286, Brebronn +285
- Bedenis would trade: furniture buy 25 @ 14.1, pasties buy 8 @ 15.7; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~106 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Essenbrucke | 584 | 0.17 | 0.30 (32/turn) | beer 41 (3.68->5.42), dyed cloth 13 (11.45->14.06), garments 10 (19.09->22.23), lead ore 9 (9.13->12.92) | thread 18 (3.84->5.55), cloth 9 (8.14->9.95), jewellery 1 (87.15->95.95), honey 3 (10.5->12.06) | +224 |
| Darmwald | 1022 | 0.35 | 0.70 (74/turn) | beer 85 (3.68->5.51), garments 10 (19.09->22.99), lead ore 3 (9.13->13.59), wine 3 (6.25->8.69) | honey 3 (11.34->12.06), resin 1 (4.16->5.22) | +146 |
| Großaue | 1136 | 0.42 | 0.30 (32/turn) | thread 28 (5.5->8.12), garments 10 (19.09->22.23), nets 4 (37.8->40.85), wine 5 (6.25->7.93) | cloth 24 (8.14->9.95), honey 1 (9.77->12.06), yarn 2 (3.78->4.29) | +146 |
| Neuborn | 780 | 0.22 | 1.00 (106/turn) | timber 24 (7.46->13.3), garments 6 (19.09->20.71), tin ingots 2 (35.07->38.76), furniture 6 (16.7->17.86) | cloth 12 (6.88->9.95), cookware 2 (25.83->27.74), honey 2 (10.82->12.06), garments 1 (23.1->23.6) | +129 |
| Coburgbaum | 619 | 0.18 | 1.00 (106/turn) | garments 9 (19.09->24.51), bread 113 (2.37->3.15), lead bars 5 (14.49->15.67), timber 10 (7.46->10.45) | cloth 10 (7.93->9.95), flour 3 (17.85->22.42), honey 2 (9.13->12.06), flax fibres 2 (6.09->6.65) | +128 |

**Best:** Essenbrucke at about +224 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 36.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 85.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres |  | 2 @ min 6.25 | goal planner: sells 2 a turn at 6.25, keeps 85 (no one offered it) |
| flax plants |  | 2 @ min 1.18 | goal planner: sells 2 a turn at 1.18, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.0) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 104, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 36.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.5/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 26.4k (cash + stock at home prices); +166/turn over 6 turns, -203/turn over 24 turns.
- Limits: cash flow >= -240/turn, prestige >= -0.64/turn (values are after 200 tax a turn).
- Today's settings: value +44/turn, cash +116/turn, prestige -2.49/turn - breaks the prestige floor.
- Plan: value -6/turn, cash +120/turn, prestige -0.64/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +90 vs +118, -50 vs +110, +51 vs +116.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Essenbrucke: +1/turn
  - ship Flax Wyrm -> no route: +0/turn
  - brewery 1 0.14 -> 0.08: +13/turn
  - net maker 0.00 -> 0.29: +7/turn
  - ropewalk 1 0.25 -> 0.00: +9/turn
  - flax farm 1 4.64 -> 3.86: -2/turn
  - retting pit 1 0.91 -> 0.77: -2/turn
  - spinnery 1 1.65 -> 1.25: -16/turn
  - mansion 1 0.00 -> 0.44: -74/turn
- Model check over the last 61 turns: predicted +107/turn for the settings we ran, real +27/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.95, garments 19.30, nets 30.20, beer 3.07, timber 3.19, prestige 59.40, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax fibres sell 2 (v2 none); flax plants sell 2 (v2 none); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.04, worth +2/turn.
- Ship linen snake: Grandgues -> Essenbrucke (+2/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +80/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.0/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 410 (+120 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 3.73 |
| ret | 3 | 0.91 | 0.75 |
| spin | 4 | 1.65 | 1.67 |
| weave | 3 | 0.50 | 1.27 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 149/77, thread 1064/227, cloth 73/127

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
