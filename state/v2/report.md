# v2 shadow report

Turn 13961, 2026-11-12 02:51. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,882, prestige 3,570 (450 free, -2.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 6 | 0 | 4 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26 |
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

**4 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **beer**: needed (4.2/turn) but there is NO buy order, stock 5.6 -> v2: add buy 5
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

440 turns left: prestige gained now converts 89.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.1 | 50.1 | running |
| hold banquet 4 (pies) | mansion | 18 | 55.3 | 55.3 | thin at home: wine, stockfish |
| jousting 3 | arena | 230 | 55.1 | 55.4 | needs a arena (build cost 26,912); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 56.8 | 56.8 |  |
| hold banquet 3 (pies) | mansion | 8 | 58.8 | 58.8 |  |
| hold banquet 4 | mansion | 17.5 | 59.0 | 59.0 | thin at home: wine, ham, stockfish |
| hold banquet 2 (pies) | mansion | 7 | 59.2 | 59.2 | thin at home: wine |
| hold banquet 4 (premium) | mansion | 20 | 59.2 | 59.2 | thin at home: wine, stockfish |
| jousting 2 | arena | 210 | 60.4 | 60.7 | needs a arena (build cost 26,912); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (meat) | mansion | 4.2 | 61.0 | 61.0 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 61.4 | 61.4 | thin at home: wine |
| hold banquet 3 (fish) | mansion | 7.6 | 62.8 | 62.8 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: furniture buy 24 @ 14.6, pasties buy 4 @ 16.0; crew 0.1; est +284 a turn; stock: furniture 24 @ 14.6 (keep 145); stock: pasties 4 @ 16.0 (keep 14)
- **Flax Wyrm** on Caillechâtel: furniture buy 20 @ 14.6, pasties buy 1 @ 12.4; crew 0.2; est +221 a turn; stock: furniture 20 @ 14.6 (keep 145); stock: pasties 1 @ 12.4 (keep 14)
- best towns now: Donaunieder +293, Bedenis +292, Angefont +289, Grandgues +284, Heidlowe +272
- Donaunieder would trade: furniture buy 24 @ 13.0, pasties buy 3 @ 14.0; crew 0.4

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~107 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Neuborn | 780 | 0.22 | 1.00 (107/turn) | timber 26 (7.46->13.3), tin ingots 4 (35.07->38.76), nets 2 (36.2->38.95), pies 2 (17.54->19.95) | cloth 18 (7.04->11.3), cookware 3 (25.62->30.78), thread 10 (5->5.6), cheese 3 (6.77->7.12) | +190 |
| Pontmont | 341 | 0.10 | 0.30 (32/turn) | limestone 3 (17.22->38), pies 3 (17.54->21.28), clay 2 (5.23->11.97), nets 6 (36.2->37.43) | cloth 16 (8.14->11.3), cookware 4 (24.15->30.78), butter 1 (77.17->89.77), belts 5 (35.28->35.91) | +158 |
| Kleinburgh | 1440 | 0.60 | 0.30 (32/turn) | garments 10 (22.4->29.64), nets 2 (36.2->37.43) | cloth 16 (7.56->11.3), cookware 4 (27.3->30.78), butter 1 (80.33->89.77), belts 1 (27.72->35.91) | +150 |
| Heilegg | 826 | 0.24 | 0.20 (21/turn) | nets 4 (36.2->39.71), pies 6 (17.54->19.95), hop beer 3 (10.4->11.11), slaked lime 1 (7.61->8.88) | cloth 24 (7.35->11.3), cookware 4 (25.83->30.78), thread 28 (5.15->5.6), garments 2 (22.89->24) | +140 |
| Bordetes | 831 | 0.25 | 0.10 (11/turn) | cheese 15 (10.08->13.3), pies 4 (17.54->20.33) | cloth 23 (7.56->11.3), belts 5 (35.28->35.91), garments 2 (23.1->24) | +135 |

**Best:** Neuborn at about +190 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 35.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 3.66, stop 9 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 6 = 1.3 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 85.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres |  | 2 @ min 5.95 | goal planner: sells 2 a turn at 5.95, keeps 85 (no one offered it) |
| flax plants |  | 2 @ min 1.18 | goal planner: sells 2 a turn at 1.18, keeps 219 (no one offered it) |
| furniture | 2 @ 16.3, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.4) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 99.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 35.2) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.5/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 26.3k (cash + stock at home prices); +96/turn over 6 turns, -113/turn over 24 turns.
- Limits: cash flow >= -245/turn, prestige >= -0.62/turn (values are after 200 tax a turn).
- Today's settings: value +43/turn, cash +83/turn, prestige -2.46/turn - breaks the prestige floor.
- Plan: value -5/turn, cash +88/turn, prestige -0.62/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +51 vs +116, +47 vs +116, +86 vs +114.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Essenbrucke: +2/turn
  - ship Flax Wyrm -> no route: +0/turn
  - brewery 1 0.14 -> 0.08: +14/turn
  - net maker 0.00 -> 0.29: +7/turn
  - ropewalk 1 0.25 -> 0.00: +9/turn
  - flax farm 1 4.64 -> 3.83: -0/turn
  - retting pit 1 0.91 -> 0.76: -2/turn
  - spinnery 1 1.65 -> 1.25: -18/turn
  - mansion 1 0.00 -> 0.44: -74/turn
- Model check over the last 61 turns: predicted +107/turn for the settings we ran, real +19/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.95, garments 19.30, nets 30.09, beer 3.15, timber 3.62, prestige 59.66, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax fibres sell 2 (v2 none); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.04, worth +2/turn.
- Ship linen snake: Grandgues -> Essenbrucke (+2/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +80/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.0/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 409 (+118 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 3.65 |
| ret | 3 | 0.91 | 0.73 |
| spin | 4 | 1.65 | 1.67 |
| weave | 3 | 0.50 | 1.27 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 155/77, thread 1064/227, cloth 73/127

## Self-diagnosis

- R1: beer slot dry: 5.6 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy none, home ask 3.5 -> **buy 9 @ 3.56 (ask 3.5, cap 5.7)** (ok)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
