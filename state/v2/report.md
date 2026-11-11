# v2 shadow report

Turn 13956, 2026-11-11 21:59. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,658, prestige 3,582 (462 free, -2.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 18 | 0 | 4 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 26, buy 9, buy @ 3.44 |
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
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.20 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~76 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.20 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +6 crew for Flax Wyrm (crew 0.13, no projection from the game)
- labour: +3 crew for linen snake (crew 0.05, no projection from the game)
- labour: projection runs 100 over real use lately; planning 493, not 593

## Prestige spending, cheapest coin per prestige first

445 turns left: prestige gained now converts 89.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.1 | 50.1 | running |
| hold banquet 4 (pies) | mansion | 18 | 55.1 | 55.1 | thin at home: ham, stockfish, pies |
| jousting 3 | arena | 230 | 55.3 | 55.6 | needs a arena (build cost 26,603); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 56.8 | 56.8 |  |
| hold banquet 4 | mansion | 17.5 | 58.2 | 58.2 | thin at home: ham, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 58.2 | 58.2 | thin at home: ham, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 60.4 | 60.4 | thin at home: pies |
| jousting 2 | arena | 210 | 60.6 | 60.9 | needs a arena (build cost 26,603); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (meat) | mansion | 4.2 | 61.0 | 61.0 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 61.5 | 61.5 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 61.9 | 61.9 |  |
| hold banquet 2 (pies) | mansion | 7 | 62.2 | 62.2 | thin at home: pies |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 20 @ 13.9, pasties buy 5 @ 14.4; crew 0.2; est +251 a turn; stock: furniture 20 @ 13.9 (keep 145); stock: pasties 5 @ 14.4 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 5 @ 16.0 (keep 14); best orders clear only 4 a turn after crew: ship stays at 0
- best towns now: Chatgnan +338, Vauxvais +331, Heidlowe +318, Hofkirchen +313, Brebronn +304
- Chatgnan would trade: furniture buy 27 @ 13.4, pasties buy 7 @ 16.3; crew 0.3

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~106 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Brebronn | 862 | 0.26 | 0.30 (32/turn) | garments 10 (19.2->21.85), nets 2 (38.2->43.51) | flax fibres 23 (5.3->8.75), cloth 20 (7.88->10), cheese 5 (7.25->9.97), steel ingots 3 (20.06->21.85) | +160 |
| Essenbrucke | 584 | 0.17 | 0.20 (21/turn) | dyed cloth 23 (12.08->14.34), garments 10 (19.2->21.85), beer 39 (3.68->4.41), slaked lime 1 (7.61->8.69) | thread 46 (3.99->4.74), tackles 1 (156.45->170.05), cheese 5 (8.03->9.97), cloth 2 (8.29->10) | +147 |
| Kleinburgh | 1440 | 0.59 | 0.20 (21/turn) | garments 10 (19.2->28.5) | cloth 24 (7.56->10), cookware 5 (26.04->26.79), flax fibres 1 (6.2->8.75), steel ingots 1 (20.89->21.85) | +133 |
| Unterhufe | 595 | 0.17 | 0.20 (21/turn) | garments 10 (19.2->20.9), slaked lime 1 (7.61->8.74) | cloth 19 (6.93->10), flax fibres 23 (6.35->8.75), cheese 5 (9.19->9.97), steel ingots 2 (20.27->21.85) | +127 |
| Angefont | 686 | 0.19 | 0.30 (32/turn) | garments 10 (19.2->20.9), thread 64 (4.66->4.89), casks 7 (6.2->6.79) | flax fibres 23 (5.04->8.75), cloth 14 (8.24->10), cheese 5 (9.13->9.97), seeds 7 (2.27->3.13) | +126 |

**Best:** Brebronn at about +160 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 36.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 3.66, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 18 = 4.2 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres |  | 3 @ min 8.65 | goal planner: sells 3 a turn at 8.65, keeps 85 (no one offered it) |
| flax plants |  | 2 @ min 1.18 | goal planner: sells 2 a turn at 1.18, keeps 219 (no one offered it) |
| furniture | 2 @ 15.8, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.4) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 105, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 37.2) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.5/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 25.6k (cash + stock at home prices); +190/turn over 6 turns, -228/turn over 24 turns.
- Limits: cash flow >= -236/turn, prestige >= -0.68/turn (values are after 200 tax a turn).
- Today's settings: value +38/turn, cash +118/turn, prestige -2.52/turn - breaks the prestige floor.
- Plan: value -8/turn, cash +119/turn, prestige -0.68/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +160 vs +110, +94 vs +121, +42 vs +118.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Hofkirchen: +6/turn
  - ship Flax Wyrm -> Chatgnan: +0/turn
  - brewery 1 0.14 -> 0.08: +12/turn
  - net maker 0.00 -> 0.29: +7/turn
  - ropewalk 1 0.25 -> 0.00: +7/turn
  - spinnery 1 1.65 -> 1.24: +2/turn
  - retting pit 1 0.91 -> 0.79: -4/turn
  - flax farm 1 4.64 -> 3.98: -10/turn
  - mansion 1 0.00 -> 0.44: -74/turn
- Model check over the last 61 turns: predicted +108/turn for the settings we ran, real +23/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.95, garments 19.30, nets 30.24, beer 3.01, timber 3.26, prestige 59.19, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax fibres sell 3 (v2 none); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.04, worth +2/turn.
- Ship linen snake: Grandgues -> Hofkirchen (+6/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Chatgnan (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +80/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.0/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 414 (+123 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 3.89 |
| ret | 3 | 0.91 | 0.78 |
| spin | 4 | 1.65 | 1.67 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 138/77, thread 1064/227, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
