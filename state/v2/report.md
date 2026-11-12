# v2 shadow report

Turn 13978, 2026-11-12 19:11. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,130, prestige 3,526 (406 free, -2.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 14 | 9 | 4 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 33 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 17, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 4.18 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 4.18 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.30 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~79 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: home ask 11.30 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +3 crew for Flax Wyrm (crew 0.07, no projection from the game)
- labour: projection runs 100 over real use lately; planning 487, not 587

## Prestige spending, cheapest coin per prestige first

423 turns left: prestige gained now converts 88.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 4 (pies) | mansion | 18 | 51.2 | 51.2 | thin at home: hop beer, ham, stockfish, pies |
| maintain 1 | park | 0.5 | 51.9 | 51.9 | running |
| hold banquet 4 | mansion | 17.5 | 53.2 | 53.2 | thin at home: hop beer, ham, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 56.0 | 56.0 | thin at home: hop beer, ham, stockfish |
| jousting 3 | arena | 230 | 56.0 | 56.3 | needs a arena (build cost 27,591); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 57.3 | 57.3 | thin at home: hop beer, pies |
| hold banquet 1 (fish) | mansion | 4.2 | 58.5 | 58.5 | thin at home: cured fish |
| hold banquet 2 (pies) | mansion | 7 | 58.5 | 58.5 | thin at home: pies |
| hold banquet 2 (fish) | mansion | 6.8 | 58.6 | 58.6 | thin at home: cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 59.0 | 59.0 | thin at home: hop beer, cured fish |
| jousting 2 | arena | 210 | 61.3 | 61.6 | needs a arena (build cost 27,591); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold sermon 2 (candles) | church | 31 | 59.1 | 66.4 | needs a church (build cost 75,348); thin at home: candles |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 11 @ 14.1, pasties buy 5 @ 14.2; crew 0.1; est +148 a turn; stock: furniture 11 @ 14.1 (keep 145); stock: pasties 5 @ 14.2 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 5 @ 15.4 (keep 14); best orders clear only 7 a turn after crew: ship stays at 0
- best towns now: Caillechâtel +148, Vauxvais +147, Brebronn +134, Herschweig +134, Unterhufe +133
- Caillechâtel would trade: furniture buy 11 @ 14.1, pasties buy 5 @ 14.2; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~107 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.80 (86/turn) | firewood 38 (4.39->7.41), timber 40 (8.45->10.26), candles 1 (59.85->74.58), charcoal 19 (3.76->4.43) | cured meat 3 (23.94->26.79), jewellery 2 (111.3->114.95), tools 10 (5.57->6.13), flax fibres 8 (7.04->7.4) | +161 |
| Orlesailles | 1178 | 0.44 | 0.50 (54/turn) | candles 1 (59.85->76.95), copper ingots 1 (15.44->17.76), dyed yarn 2 (5.51->6.08) | looms 1 (630->693.5), wax 5 (19.21->23.75), thread 43 (5.04->5.7), tools 15 (5.15->6.13) | +126 |
| Blanans | 297 | 0.09 | 1.00 (107/turn) | timber 25 (8.45->11.02), limestone 1 (20.68->38.19), candles 0 (59.85->78.85), firewood 26 (4.39->7.31) | tapestries 1 (588->612.75), cloth 7 (7.56->8.7), butter 1 (81.9->84.55), cured meat 1 (25.2->26.79) | +125 |
| Kirchwerp | 1072 | 0.39 | 0.40 (43/turn) | candles 1 (59.85->80.75), honey 8 (10.4->13.21), casks 12 (6.51->8.31), chisels 6 (10.5->11.78) | cloth 24 (7.56->8.7), tools 15 (5.02->6.13), flax fibres 10 (5.78->7.4), rope 7 (82.95->85.02) | +109 |
| Angefont | 686 | 0.20 | 0.30 (32/turn) | candles 1 (59.85->76), copper ingots 1 (15.44->17.95), casks 9 (6.51->6.98), resin 7 (3.44->3.99) | flax fibres 23 (5.25->7.4), thread 49 (4.89->5.7), cloth 20 (8.14->8.7), cured meat 3 (25.2->26.79) | +105 |

**Best:** Grandgues at about +161 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 35.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 58.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.14 | goal planner: sells 2 a turn at 1.14, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 21.6) |
| grain | 5 @ 3.7, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 110, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 37.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 29.1k (cash + stock at home prices); +119/turn over 6 turns, +156/turn over 24 turns.
- Limits: cash flow >= -380/turn, prestige >= -0.44/turn (values are after 200 tax a turn).
- Today's settings: value +95/turn, cash +70/turn, prestige -2.24/turn - breaks the prestige floor.
- Plan: value +9/turn, cash +17/turn, prestige -0.44/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +88 vs +15, +125 vs +22, +151 vs +19.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Vauxvais: +1/turn
  - ship Flax Wyrm -> no route: +0/turn
  - brewery 1 0.14 -> 0.08: +13/turn
  - net maker 0.00 -> 0.29: +6/turn
  - spinnery 1 1.65 -> 1.35: +1/turn
  - retting pit 1 0.91 -> 0.85: +1/turn
  - flax farm 1 4.64 -> 4.25: +0/turn
  - weavery 1 0.50 -> 0.42: -13/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.24: -21/turn
  - ropewalk 1 0.25 -> 0.00: +26/turn
- Model check over the last 61 turns: predicted +104/turn for the settings we ran, real +13/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.95, garments 19.30, nets 30.30, beer 3.08, timber 3.26, prestige 70.01, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax plants sell 2 (v2 none); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None); rope sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.24, worth +10/turn.
- Ship linen snake: Grandgues -> Vauxvais (+2/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1956 coin: +4/turn, payback 481 turns, doesn't pay yet

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 409 (+119 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 3.65 |
| ret | 3 | 0.91 | 0.73 |
| spin | 4 | 1.65 | 1.67 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 156/77, thread 1064/227, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 4.18; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
- R5: tar buy not filling: bid 11 under the home ask 11.3 for 5 turns, bought 0.0 of 1, 0.0 held (0.0 turns); raise needs Taylor (ceiling 11.0)
