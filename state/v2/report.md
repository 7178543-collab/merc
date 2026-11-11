# v2 shadow report

Turn 13950, 2026-11-11 15:40. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 7,913, prestige 3,597 (477 free, -2.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 14 | 9 | 4 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 26, buy 9, buy @ 3.44 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 1, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 32 | 0 | 2 | 0 | 0 | min_holding 30, sell 10, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | buy @ 3.7 |
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

- labour: +2 crew for Flax Wyrm (crew 0.03, no projection from the game)
- labour: projection runs 100 over real use lately; planning 485, not 585

## Prestige spending, cheapest coin per prestige first

451 turns left: prestige gained now converts 89.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.6 | 51.6 | running |
| hold banquet 4 (pies) | mansion | 18 | 54.3 | 54.3 | thin at home: hop beer, ham, stockfish, cheese, pies |
| jousting 3 | arena | 230 | 55.7 | 56.0 | needs a arena (build cost 28,909); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 56.7 | 56.7 | thin at home: hop beer, ham, stockfish |
| hold banquet 1 (fish) | mansion | 4.2 | 56.8 | 56.8 | thin at home: beer |
| hold banquet 4 | mansion | 17.5 | 57.5 | 57.5 | thin at home: hop beer, ham, stockfish, cheese |
| jousting 2 | arena | 210 | 61.0 | 61.3 | needs a arena (build cost 28,909); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (meat) | mansion | 4.2 | 61.5 | 61.5 | thin at home: beer |
| hold banquet 3 (pies) | mansion | 8 | 61.6 | 61.6 | thin at home: hop beer, cheese, pies |
| hold sermon 2 (candles) | church | 31 | 57.4 | 64.1 | needs a church (build cost 75,814); thin at home: jewellery, candles |
| hold banquet 3 (fish) | mansion | 7.6 | 66.2 | 66.2 | thin at home: hop beer, cheese |
| hold banquet 2 (pies) | mansion | 7 | 67.6 | 67.6 | thin at home: cheese, pies |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 19 @ 13.6, pasties buy 7 @ 15.5; crew 0.2; est +244 a turn; stock: furniture 19 @ 13.6 (keep 145); stock: pasties 7 @ 15.5 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 16.0 (keep 14); best orders clear only -6 a turn after crew: ship stays at 0
- best towns now: Chatgnan +327, Marmont +310, Etallaen +308, Heidlowe +295, Amsdermund +270
- Chatgnan would trade: furniture buy 26 @ 13.1, pasties buy 6 @ 16.3; crew 0.3

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~114 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.50 (57/turn) | timber 37 (7.72->9.79), candles 2 (59.85->80.75), bread 160 (2.46->2.72), thread 7 (4.66->6.98) | cloth 11 (7.67->12.25), cheese 5 (9.77->11.78), slaked lime 4 (8.93->10.36), tiles 3 (4.2->5.46) | +206 |
| Großaue | 1136 | 0.45 | 0.20 (23/turn) | candles 2 (59.85->80.27), lead ore 2 (9.35->18.62), dyed cloth 6 (11.55->13.21), wine 3 (7.51->9.03) | cloth 15 (7.51->12.25), cheese 5 (6.77->11.78), bellows 1 (226.8->243.2), cookware 5 (22.26->24.89) | +185 |
| Kirchwerp | 1072 | 0.41 | 0.50 (57/turn) | candles 2 (59.85->79.8), thread 92 (4.66->5.42), arms 6 (33.81->36.29), flax fibres 7 (6.9->8.22) | cloth 15 (7.56->12.25), cheese 5 (7.4->11.78), slaked lime 4 (8.4->10.36), cured meat 2 (22.05->23.56) | +174 |
| Bordetes | 831 | 0.26 | 0.10 (11/turn) | candles 2 (59.85->81.7), cured fish 7 (24.57->30.78), wheels 3 (24.99->25.84), steel ingots 1 (15.12->15.86) | cloth 15 (7.56->12.25), slaked lime 3 (6.83->10.36), garments 2 (23.1->24.2) | +160 |
| Großmühle | 751 | 0.23 | 0.10 (11/turn) | candles 2 (59.85->76), dyed cloth 6 (11.55->11.78) | bellows 1 (184.8->243.2), cloth 15 (8.51->12.25), cheese 5 (8.4->11.78), raw cloth 1 (5.41->7.17) | +158 |

**Best:** Grandgues at about +206 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 6 @ 3.78, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 14 = 3.3 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 58.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres |  | 2 @ min 6.4 | goal planner: sells 2 a turn at 6.4, keeps 85 (no one offered it) |
| flax plants |  | 2 @ min 1.18 | goal planner: sells 2 a turn at 1.18, keeps 219 (no one offered it) |
| furniture | 2 @ 15.2, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 22.6) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 104, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 38.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 25.1k (cash + stock at home prices); -671/turn over 6 turns, -221/turn over 24 turns.
- Limits: cash flow >= -163/turn, prestige >= -0.74/turn (values are after 200 tax a turn).
- Today's settings: value +76/turn, cash +90/turn, prestige -2.60/turn - breaks the prestige floor.
- Plan: value +24/turn, cash +89/turn, prestige -0.74/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +177 vs +26, +10 vs +28, +115 vs +57.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Calange: +6/turn
  - ship Flax Wyrm -> no route: +0/turn
  - brewery 1 0.14 -> 0.08: +13/turn
  - net maker 0.00 -> 0.29: +6/turn
  - ropewalk 1 0.25 -> 0.00: +7/turn
  - spinnery 1 1.65 -> 1.25: -3/turn
  - retting pit 1 0.91 -> 0.76: -5/turn
  - flax farm 1 4.64 -> 3.85: -9/turn
  - mansion 1 0.00 -> 0.44: -78/turn
- Model check over the last 59 turns: predicted +106/turn for the settings we ran, real +28/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.95, garments 19.30, nets 30.25, beer 3.02, timber 3.31, prestige 61.21, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax fibres sell 2 (v2 none); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.04, worth +2/turn.
- Ship linen snake: Grandgues -> Calange (+6/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +80/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.1/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 417 (+127 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.09 |
| ret | 3 | 0.91 | 0.82 |
| spin | 4 | 1.65 | 1.67 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 124/77, thread 1064/227, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
