# v2 shadow report

Turn 13923, 2026-11-10 12:23. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,851, prestige 3,457 (337 free, -2.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 0 | 0 | 0 | 0 | 0 | min_holding 60, sell 16, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 12.40 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~73 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax fibres**: flax fibres buffer thin: 1.4 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 56
- **tar**: home ask 12.40 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +2 crew for Flax Wyrm (crew 0.03, no projection from the game)
- labour: projection runs 100 over real use lately; planning 485, not 585

## Prestige spending, cheapest coin per prestige first

478 turns left: prestige gained now converts 90.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.0 | 48.0 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 54.2 | 54.2 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 54.3 | 54.3 | thin at home: cheese |
| hold banquet 4 (pies) | mansion | 18 | 54.7 | 54.7 | thin at home: ham, stockfish, pies |
| hold banquet 4 (premium) | mansion | 20 | 56.3 | 56.3 | thin at home: ham, stockfish |
| hold banquet 3 (fish) | mansion | 7.6 | 56.5 | 56.5 | thin at home: cheese |
| hold banquet 4 | mansion | 17.5 | 56.8 | 56.8 | thin at home: ham, stockfish |
| jousting 3 | arena | 230 | 57.2 | 57.5 | needs a arena (build cost 26,512); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 60.2 | 60.2 | thin at home: pies |
| hold banquet 3 (pies) | mansion | 8 | 60.7 | 60.7 | thin at home: pies |
| hold feast 2 | townhouse | 2.6 | 56.2 | 62.6 | needs a townhouse (build cost 7,618) |
| hold banquet 2 (meat) | mansion | 6.8 | 62.8 | 62.8 | thin at home: cured meat, cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 12 @ 13.2, pasties buy 4 @ 15.1; crew 0.1; est +163 a turn; stock: furniture 12 @ 13.2 (keep 145); stock: pasties 4 @ 15.1 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Essenbrucke +183, Bedenis +179, Caillechâtel +163, Chatgnan +159, Marmont +156
- Essenbrucke would trade: furniture buy 12 @ 12.8, pasties buy 9 @ 14.4; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~102 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.50 (51/turn) | bread 152 (2.5->3.61), cured fish 7 (24.57->29.07), furniture 10 (11.97->13.77), flax fibres 7 (6.2->6.55) | cloth 12 (8.51->8.85), hop beer 5 (8.82->9.07), copper ingots 1 (18.69->19.19) | +201 |
| Etallaen | 774 | 0.21 | 1.00 (102/turn) | beer 38 (3.46->7.12), bread 108 (2.5->3.25), furniture 7 (11.97->13.77), dyed cloth 2 (12.08->13.59) | flax fibres 11 (4.94->6.75), cloth 5 (8.4->8.85), thread 5 (4.73->5.22), wrought iron 2 (16.28->17.29) | +171 |
| Pontmont | 341 | 0.09 | 0.60 (61/turn) | bread 152 (2.5->3.27), furniture 10 (11.97->15.2), bricks 6 (8.29->12.63), casks 2 (7.61->10.36) | cloth 20 (7.67->8.85), wax 1 (20.68->22.8), garments 2 (25.41->26.2) | +150 |
| Neuborn | 780 | 0.21 | 1.00 (102/turn) | bread 66 (2.5->4.18), timber 15 (8.93->13.3), flour 0 (22.47->30.21), wine 3 (6.14->7.5) | cloth 10 (7.67->8.85), garments 0 (23.73->26.2), thread 5 (4.66->5.22), copper ingots 0 (18.27->19.19) | +117 |
| Heilegg | 826 | 0.23 | 0.60 (61/turn) | beer 54 (3.46->4.56), furniture 10 (11.97->15.01), lead ore 7 (9.29->11.97), gold ore 2 (175.35->179.55) | cloth 24 (7.56->8.85), garments 2 (24.78->26.2), salt 4 (4.2->4.89), cookware 3 (24.99->25.27) | +107 |

**Best:** Grandgues at about +201 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 8 @ min 3.26 | goal planner: sells 8 a turn at 3.26, keeps 60 (no one offered it) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 85, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 11.7, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 25.4) |
| grain | 8 @ 3.7, stop 32 |  | goal planner: buys 8 a turn for today's rates, keeps up to 32 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 101, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 36.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 29.4k (cash + stock at home prices); +169/turn over 6 turns, +184/turn over 24 turns.
- Limits: cash flow >= -327/turn, prestige >= -0.16/turn (values are after 200 tax a turn).
- Today's settings: value +68/turn, cash +25/turn, prestige -2.40/turn - breaks the prestige floor.
- Plan: value -14/turn, cash -11/turn, prestige -0.45/turn - could not meet the prestige floor.
- Cash check (real vs predicted cash a tick, last 3): +3 vs +44, -28 vs +34, +146 vs +17.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Donaunieder: +29/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +8/turn
  - ropewalk 1 0.25 -> 0.00: -0/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.10: +17/turn
  - flax farm 1 4.64 -> 3.94: -3/turn
  - retting pit 1 0.91 -> 0.78: -5/turn
  - spinnery 1 1.65 -> 1.38: +10/turn
  - sewing shop 1 0.30 -> 0.36: -8/turn
  - weavery 1 0.50 -> 0.60: +11/turn
- Model check over the last 58 turns: predicted +106/turn for the settings we ran, real +141/turn.
- Worth of one more unit per turn: labour 1.60, thread 4.06, cloth 6.46, flax fibres 4.89, garments 18.66, nets 29.26, beer 2.88, timber 3.40, prestige 10000.00, cash 0.00
- Orders it would set: beer sell 8 (v2 none); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 2 (v2 3); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 8 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.10, worth +6/turn.
- Ship linen snake: Grandgues -> Donaunieder (+29/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +79/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

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

Buffers: flax fibres 39/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R1: beer slot dry: 0.0 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy none, home ask 3.3 -> **buy 9 @ 3.36 (ask 3.3, cap 5.7)** (ok)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.95 for 6 turns, bought 0.0 of 1, 39.1 held (1.6 turns); raise needs Taylor (ceiling None)
