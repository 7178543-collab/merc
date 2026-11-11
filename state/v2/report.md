# v2 shadow report

Turn 13951, 2026-11-11 16:26. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 8,690, prestige 3,595 (475 free, -2.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 19 | 9 | 4 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 26, buy 9, buy @ 3.44 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 32 | 0 | 2 | 0 | 0 | min_holding 30, sell 10, sell @ 19.3 |
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

- **labour**: 45 labour expired last turn (~78 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: +6 crew for Flax Wyrm (crew 0.13, no projection from the game)
- labour: projection runs 100 over real use lately; planning 490, not 590

## Prestige spending, cheapest coin per prestige first

450 turns left: prestige gained now converts 89.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.3 | 51.3 | running |
| hold banquet 4 (pies) | mansion | 18 | 54.0 | 54.0 | thin at home: ham, stockfish, pies |
| jousting 3 | arena | 230 | 55.8 | 56.1 | needs a arena (build cost 28,764); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 56.6 | 56.6 | thin at home: ham, stockfish, premium cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 56.7 | 56.7 | thin at home: beer |
| hold banquet 4 | mansion | 17.5 | 57.2 | 57.2 | thin at home: ham, stockfish, cheese |
| hold banquet 3 (pies) | mansion | 8 | 60.4 | 60.4 | thin at home: cheese, pies |
| hold banquet 1 (meat) | mansion | 4.2 | 60.6 | 60.6 | thin at home: beer |
| jousting 2 | arena | 210 | 61.1 | 61.5 | needs a arena (build cost 28,764); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold sermon 2 (candles) | church | 31 | 57.4 | 64.1 | needs a church (build cost 74,947); thin at home: candles |
| hold banquet 3 (fish) | mansion | 7.6 | 64.7 | 64.7 | thin at home: cheese |
| hold banquet 2 (pies) | mansion | 7 | 66.7 | 66.7 | thin at home: cheese, pies |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 19 @ 14.1, pasties buy 9 @ 15.9; crew 0.2; est +238 a turn; stock: furniture 19 @ 14.1 (keep 145); stock: pasties 9 @ 15.9 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 16.0 (keep 14); best orders clear only 0 a turn after crew: ship stays at 0
- best towns now: Marmont +300, Hofkirchen +295, Großmühle +292, Chatgnan +292, Heidlowe +291
- Marmont would trade: furniture buy 25 @ 13.5; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~111 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Bordetes | 831 | 0.26 | 0.50 (56/turn) | cured fish 7 (24.57->33.63), furniture 7 (11.87->15.77), charcoal 19 (3->6.03), candles 1 (64.05->81.22) | cloth 23 (7.56->12), slaked lime 1 (6.83->11.59), garments 2 (23.1->24.8) | +223 |
| Kirchwerp | 1072 | 0.40 | 0.60 (67/turn) | thread 92 (4.66->5.7), candles 1 (64.05->85.5), furniture 7 (11.87->15.2), flax fibres 7 (6.4->8.17) | cloth 24 (7.56->12), garments 2 (23.1->24.8), slaked lime 1 (8.4->11.59), cured meat 2 (22.05->22.99) | +207 |
| Heilegg | 826 | 0.25 | 0.60 (67/turn) | candles 1 (64.05->79.8), charcoal 19 (3->5.37), lead ore 6 (9.35->11.59), varnish 3 (19.01->20.9) | cloth 24 (7.72->12), cookware 7 (20.48->25.65), cheese 7 (7.19->11.02), garments 2 (22.68->24.8) | +199 |
| Fontaux | 411 | 0.12 | 0.90 (100/turn) | thread 92 (4.66->5.65), charcoal 18 (3->5.56), bread 135 (2.44->2.93), candles 1 (64.05->79.33) | cloth 5 (9.5->12), cheese 7 (9.4->11.02), pasties 1 (12.08->14.25), slaked lime 1 (9.71->11.59) | +194 |
| Grandgues | 152 | 0.04 | 0.50 (56/turn) | bread 161 (2.44->2.83), charcoal 19 (3->4.52), candles 1 (64.05->80.75), bricks 6 (7.14->9.97) | cloth 11 (7.67->12), slaked lime 1 (9.03->11.59), tiles 2 (4.18->5.46), casks 1 (5.93->6.65) | +181 |

**Best:** Bordetes at about +223 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 35.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 3.78, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 19 = 4.4 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 62.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres |  | 4 @ min 7.15 | goal planner: trial sale of an idle pile, 4 a turn at 7.15, keeps 85 (41 over) |
| flax plants |  | 2 @ min 1.18 | goal planner: sells 2 a turn at 1.18, keeps 219 (no one offered it) |
| furniture | 2 @ 11.6, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.8) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 109, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 37.2) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.4/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 25.1k (cash + stock at home prices); -661/turn over 6 turns, -218/turn over 24 turns.
- Limits: cash flow >= -195/turn, prestige >= -0.73/turn (values are after 200 tax a turn).
- Today's settings: value +73/turn, cash +76/turn, prestige -2.59/turn - breaks the prestige floor.
- Plan: value +24/turn, cash +88/turn, prestige -0.73/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +10 vs +28, +115 vs +57, +778 vs +90.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> no route: +0/turn
  - ship Flax Wyrm -> no route: +0/turn
  - brewery 1 0.14 -> 0.08: +13/turn
  - net maker 0.00 -> 0.29: +6/turn
  - ropewalk 1 0.25 -> 0.00: +8/turn
  - spinnery 1 1.65 -> 1.25: -2/turn
  - retting pit 1 0.91 -> 0.76: -5/turn
  - flax farm 1 4.64 -> 3.85: -10/turn
  - mansion 1 0.00 -> 0.44: -76/turn
- HAND-OVER: goal planner: model check failed 3 runs in a row, buys handed back to the old rules.
- Model check over the last 59 turns: predicted +107/turn for the settings we ran, real +29/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.95, garments 19.30, nets 30.13, beer 3.02, timber 3.31, prestige 60.36, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax fibres sell 4 (v2 none); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.04, worth +2/turn.
- Ship linen snake: Grandgues -> no route (+0/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +80/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.1/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 417 (+126 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.07 |
| ret | 3 | 0.91 | 0.81 |
| spin | 4 | 1.65 | 1.67 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 126/77, thread 1064/227, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
