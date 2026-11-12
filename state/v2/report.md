# v2 shadow report

Turn 13979, 2026-11-12 20:17. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,308, prestige 3,524 (404 free, -2.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 10 | 0 | 4 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 32 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 17, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 3.26 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.26 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.50 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~77 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.50 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +4 crew for Flax Wyrm (crew 0.08, no projection from the game)
- labour: projection runs 100 over real use lately; planning 487, not 587

## Prestige spending, cheapest coin per prestige first

422 turns left: prestige gained now converts 88.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.0 | 51.0 | running |
| hold banquet 4 (pies) | mansion | 18 | 51.9 | 51.9 | thin at home: hop beer, ham, stockfish, pies |
| hold banquet 4 | mansion | 17.5 | 54.0 | 54.0 | thin at home: hop beer, ham, stockfish, cheese |
| jousting 3 | arena | 230 | 55.3 | 55.6 | needs a arena (build cost 27,201); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 56.7 | 56.7 | thin at home: hop beer, ham, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 57.6 | 57.6 | thin at home: hop beer, cheese, pies |
| hold banquet 1 (fish) | mansion | 4.2 | 58.3 | 58.3 | thin at home: cured fish |
| hold banquet 2 (pies) | mansion | 7 | 58.5 | 58.5 | thin at home: cheese, pies |
| hold banquet 2 (fish) | mansion | 6.8 | 58.9 | 58.9 | thin at home: cured fish, cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 59.6 | 59.6 | thin at home: hop beer, cured fish, cheese |
| jousting 2 | arena | 210 | 60.6 | 60.9 | needs a arena (build cost 27,201); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold sermon 2 (candles) | church | 31 | 57.6 | 64.8 | needs a church (build cost 73,812); thin at home: candles |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 11 @ 14.0, pasties buy 6 @ 14.2; crew 0.1; est +154 a turn; stock: furniture 11 @ 14.0 (keep 145); stock: pasties 6 @ 14.2 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 15.5 (keep 14); best orders clear only -0 a turn after crew: ship stays at 0
- best towns now: Caillechâtel +154, Gottweiler +141, Boistot +138, Gosschweig +136, Brebronn +134
- Caillechâtel would trade: furniture buy 11 @ 14.0, pasties buy 6 @ 14.2; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~106 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.70 (74/turn) | firewood 33 (3.42->8.03), timber 40 (7.61->10.64), furniture 14 (12.18->16.15), candles 1 (59.85->74.58) | cured meat 3 (24.15->27.55), flour 2 (20.37->23.56), flax plants 11 (1.35->1.72), flax fibres 2 (6.41->7.6) | +297 |
| Blanans | 297 | 0.08 | 1.00 (106/turn) | timber 25 (7.61->11.3), firewood 26 (3.42->7.17), furniture 8 (12.18->15.11), candles 0 (59.85->78.85) | cloth 7 (7.56->8.25), cured meat 1 (24.99->27.55), flax fibres 3 (6.93->7.6), charcoal 11 (2.62->3.42) | +143 |
| Kirchwerp | 1072 | 0.38 | 0.50 (53/turn) | furniture 14 (12.18->17), candles 1 (59.85->80.75), honey 6 (10.4->13.21), chisels 10 (10.5->12.06) | flax fibres 8 (5.78->7.6), belts 6 (32.55->34.58), cloth 24 (7.56->8.25), cured meat 3 (25.83->27.55) | +134 |
| Orlesailles | 1178 | 0.44 | 0.50 (53/turn) | candles 1 (59.85->78.38), premium ham 1 (252->262.2), acid 1 (115.5->121.6), tackles 1 (169.05->173.85) | looms 1 (630->693.5), wax 6 (19.32->23.94), flax fibres 7 (5.99->7.6), thread 46 (5.04->5.55) | +126 |
| Hanstein | 380 | 0.11 | 0.30 (32/turn) | candles 1 (59.85->75.52), furniture 8 (12.18->14.63), timber 11 (7.61->10.54) | flax fibres 11 (4.64->7.6), yarn 12 (3.28->4.24), seeds 8 (1.81->3.13), cured meat 3 (24.78->27.55) | +122 |

**Best:** Grandgues at about +297 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 7) |
| candles | 2 @ 65, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.14 | goal planner: sells 2 a turn at 1.14, keeps 219 (no one offered it) |
| furniture | 2 @ 11.9, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 22.8) |
| grain | 5 @ 3.7, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 109, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 37.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.4k (cash + stock at home prices); +3/turn over 6 turns, +124/turn over 24 turns.
- Limits: cash flow >= -388/turn, prestige >= -0.43/turn (values are after 200 tax a turn).
- Today's settings: value +92/turn, cash +63/turn, prestige -2.23/turn - breaks the prestige floor.
- Plan: value +8/turn, cash +16/turn, prestige -0.43/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +125 vs +22, +151 vs +19, +178 vs +70.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> no route: +0/turn
  - ship Flax Wyrm -> no route: +0/turn
  - brewery 1 0.14 -> 0.08: +12/turn
  - net maker 0.00 -> 0.29: +6/turn
  - spinnery 1 1.65 -> 1.33: -1/turn
  - retting pit 1 0.91 -> 0.84: +1/turn
  - flax farm 1 4.64 -> 4.22: -2/turn
  - weavery 1 0.50 -> 0.44: -9/turn
  - ropewalk 1 0.25 -> 0.00: -16/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.22: +23/turn
- Model check over the last 61 turns: predicted +104/turn for the settings we ran, real -0/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.95, garments 19.30, nets 30.31, beer 3.02, timber 3.26, prestige 69.21, cash 0.00
- Orders it would set: bread buy 5 (v2 7); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.22, worth +8/turn.
- Ship linen snake: Grandgues -> no route (+0/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1956 coin: +4/turn, payback 533 turns, doesn't pay yet

## Chain sizing

Mode HOLD, garments sold 10.3/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 409 (+119 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 3.63 |
| ret | 3 | 0.91 | 0.73 |
| spin | 4 | 1.65 | 1.67 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 158/77, thread 1064/227, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 3.26; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
