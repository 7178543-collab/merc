# v2 shadow report

Turn 13953, 2026-11-11 18:36. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,362, prestige 3,590 (470 free, -2.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 25 | 9 | 4 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 26, buy 9, buy @ 3.44 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 33 | 0 | 2 | 0 | 0 | min_holding 30, sell 10, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 18, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~77 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: +7 crew for Flax Wyrm (crew 0.13, no projection from the game)
- labour: projection runs 100 over real use lately; planning 490, not 590

## Prestige spending, cheapest coin per prestige first

448 turns left: prestige gained now converts 89.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.0 | 51.0 | running |
| hold banquet 4 (pies) | mansion | 18 | 55.8 | 55.8 | thin at home: stockfish, pies |
| jousting 3 | arena | 230 | 56.2 | 56.5 | needs a arena (build cost 27,985); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 56.7 | 56.7 |  |
| hold banquet 4 (premium) | mansion | 20 | 57.9 | 57.9 | thin at home: stockfish |
| hold banquet 4 | mansion | 17.5 | 59.0 | 59.0 | thin at home: stockfish |
| hold banquet 1 (meat) | mansion | 4.2 | 60.0 | 60.0 |  |
| jousting 2 | arena | 210 | 61.6 | 61.9 | needs a arena (build cost 27,985); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 62.9 | 62.9 | thin at home: pies |
| hold banquet 3 (fish) | mansion | 7.6 | 65.1 | 65.1 |  |
| hold sermon 2 (candles) | church | 31 | 58.8 | 65.3 | needs a church (build cost 72,501); thin at home: candles |
| hold banquet 2 (fish) | mansion | 6.8 | 66.0 | 66.0 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: furniture buy 26 @ 14.6, pasties buy 4 @ 16.0; crew 0.1; est +307 a turn; stock: furniture 26 @ 14.6 (keep 145); stock: pasties 4 @ 16.0 (keep 14)
- **Flax Wyrm** on Caillechâtel: furniture buy 19 @ 13.4, pasties buy 9 @ 15.5; crew 0.2; est +256 a turn; stock: furniture 19 @ 13.4 (keep 145); stock: pasties 9 @ 15.5 (keep 14)
- best towns now: Heidlowe +334, Donaunieder +323, Bedenis +310, Grandgues +307, Marmont +306
- Heidlowe would trade: furniture buy 26 @ 13.3, pasties buy 6 @ 14.6; crew 0.3

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~110 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Angefont | 686 | 0.20 | 0.30 (33/turn) | furniture 7 (11.97->14.06), casks 8 (6.46->7.36), thread 74 (4.66->4.89), steel ingots 1 (18.17->18.43) | flax fibres 23 (4.73->12.4), cloth 14 (8.19->10.7), cheese 7 (9.55->11.21), tools 15 (4.91->5.56) | +236 |
| Unterhufe | 595 | 0.17 | 0.20 (22/turn) | furniture 7 (11.97->17), dyed cloth 8 (12.6->14.25), ham 2 (83.48->86.92) | cloth 24 (7.14->10.7), flax fibres 14 (7.51->12.4), cheese 7 (9.13->11.21), windows 1 (572.25->584.25) | +223 |
| Kirchwerp | 1072 | 0.39 | 0.50 (55/turn) | thread 92 (4.66->5.42), furniture 7 (11.97->18.14), jewellery 2 (106.05->122.55), honey 3 (9.66->11.49) | cloth 24 (7.56->10.7), flax fibres 6 (9.03->12.4), dyed cloth 4 (9.97->10.83), garments 2 (23.1->24.2) | +187 |
| Fontaux | 411 | 0.12 | 0.50 (55/turn) | thread 92 (4.66->5.65), furniture 7 (11.97->17.39), charcoal 18 (3.07->5.84), beer 62 (3.57->3.99) | cloth 2 (9.87->10.7) | +180 |
| Rotterburg | 1056 | 0.39 | 0.20 (22/turn) | garments 10 (23.8->27.93), furniture 7 (11.97->16.91), nets 5 (38.2->40.28), wine 4 (6.98->7.89) | cloth 24 (7.19->10.7), flax fibres 6 (7.82->12.4), cheese 7 (9.4->11.21), salt 4 (4.26->4.8) | +179 |

**Best:** Angefont at about +236 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 36.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 3.56, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 25 = 6.0 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 88, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres |  | 1 @ min 8.95 | goal planner: sells 1 a turn at 8.95, keeps 85 (no one offered it) |
| flax plants |  | 2 @ min 1.18 | goal planner: sells 2 a turn at 1.18, keeps 219 (no one offered it) |
| furniture | 2 @ 11.7, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.2) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 37.2) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.4/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 25.4k (cash + stock at home prices); -610/turn over 6 turns, -200/turn over 24 turns.
- Limits: cash flow >= -223/turn, prestige >= -0.71/turn (values are after 200 tax a turn).
- Today's settings: value +41/turn, cash +110/turn, prestige -2.56/turn - breaks the prestige floor.
- Plan: value -3/turn, cash +123/turn, prestige -0.71/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +778 vs +90, +6 vs +76, +667 vs +116.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Hanbrücken: +25/turn
  - ship Flax Wyrm -> no route: +0/turn
  - brewery 1 0.14 -> 0.08: +13/turn
  - net maker 0.00 -> 0.29: +6/turn
  - ropewalk 1 0.25 -> 0.00: +8/turn
  - spinnery 1 1.65 -> 1.24: +6/turn
  - retting pit 1 0.91 -> 0.79: -7/turn
  - flax farm 1 4.64 -> 3.96: -9/turn
  - mansion 1 0.00 -> 0.44: -75/turn
- Model check over the last 60 turns: predicted +108/turn for the settings we ran, real +25/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.96, garments 19.30, nets 30.22, beer 3.01, timber 3.29, prestige 59.47, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax fibres sell 1 (v2 none); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.04, worth +2/turn.
- Ship linen snake: Grandgues -> Hanbrücken (+25/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +80/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.0/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 417 (+126 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.05 |
| ret | 3 | 0.91 | 0.81 |
| spin | 4 | 1.65 | 1.67 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 126/77, thread 1064/227, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
