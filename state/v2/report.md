# v2 shadow report

Turn 13934, 2026-11-10 23:10. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 7,195, prestige 3,437 (317 free, -1.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 26 | 4 | 4 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 26, buy 9, buy @ 3.36 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 70 | 0 | 2 | 0 | 0 | min_holding 70, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.50 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.50 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~78 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: +2 crew for Flax Wyrm (crew 0.04, no projection from the game)
- labour: projection runs 100 over real use lately; planning 485, not 585

## Prestige spending, cheapest coin per prestige first

467 turns left: prestige gained now converts 90.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.0 | 51.0 | running |
| hold banquet 4 (pies) | mansion | 18 | 55.1 | 55.1 | thin at home: ham, stockfish |
| jousting 3 | arena | 230 | 54.9 | 55.2 | needs a arena (build cost 27,988); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 55.3 | 55.3 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 56.0 | 56.0 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 56.4 | 56.4 |  |
| hold banquet 4 | mansion | 17.5 | 57.5 | 57.5 | thin at home: ham, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 58.0 | 58.0 | thin at home: ham, stockfish |
| hold banquet 3 (meat) | mansion | 7.6 | 59.0 | 59.0 |  |
| hold banquet 3 (pies) | mansion | 8 | 59.4 | 59.4 | thin at home: pies |
| hold banquet 2 (meat) | mansion | 6.8 | 59.7 | 59.7 |  |
| hold banquet 1 (meat) | mansion | 4.2 | 60.0 | 60.0 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: pasties buy 9 @ 15.5; crew 0.1; est +20 a turn; stock: pasties 9 @ 15.5 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 7 @ 16.0 (keep 14); best orders clear only 10 a turn after crew: ship stays at 0
- best towns now: Herschweig +264, Bedenis +255, Marmont +253, Friedwerp +249, Essenbrucke +237
- Herschweig would trade: furniture buy 15 @ 12.5, pasties buy 11 @ 11.9; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~106 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Heidlowe | 662 | 0.19 | 0.30 (32/turn) | garments 10 (18.31->22.61), nets 4 (31.8->39.52), beer 50 (3.46->4.35), cheese 6 (6.98->7.5) | tiles 3 (3.53->7.46), tar 10 (10.71->11.4), candles 1 (84.53->86.5), copper ingots 1 (18.59->19.57) | +112 |
| Kirchwerp | 1072 | 0.38 | 0.70 (74/turn) | thread 92 (4.88->5.7), nets 6 (31.8->37.05), garments 10 (18.31->20.71), lead ore 10 (7.35->10.45) | flax fibres 22 (5.78->6.75), candles 1 (84->86.5), copper ingots 1 (17.85->19.57), cured meat 2 (21->22.23) | +110 |
| Hofkirchen | 991 | 0.33 | 0.70 (74/turn) | thread 80 (4.88->5.7), nets 6 (31.8->36.86), garments 10 (18.31->20.52), grain 2 (2.76->5.13) | flax fibres 23 (5.78->6.75), furniture 14 (13.97->15.58), cloth 24 (7.56->8), blades 3 (14.7->15.77) | +110 |
| Brebronn | 862 | 0.26 | 0.20 (21/turn) | garments 10 (18.31->21.66), nets 4 (31.8->37.05), thread 18 (4.88->5.22), cheese 6 (6.98->7.46) | tapestries 1 (630->660.25), casks 8 (4.98->6.84), tiles 3 (3.97->7.46), candles 1 (84.53->86.5) | +101 |
| Heilegg | 826 | 0.24 | 0.20 (21/turn) | nets 4 (31.8->44.27), lead ore 5 (7.35->12.82), garments 10 (18.31->20.33), grain 2 (2.76->3.61) | cloth 24 (7.35->8), garments 2 (22.68->23.4), thread 34 (5->5.25) | +99 |

**Best:** Heidlowe at about +112 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer | 5 @ 3.46, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 26 = 6.2 turns |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.18 | goal planner: sells 2 a turn at 1.18, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 22.8) |
| grain | 0 @ 3.7, stop 17 |  | goal planner: buys 0 a turn for today's rates, keeps up to 17 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tapestries |  | 1 @ min 765 | goal planner: trial sale of an idle pile, 1 a turn at 765, keeps 0 (6 over) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.9k (cash + stock at home prices); +56/turn over 6 turns, +138/turn over 24 turns.
- Limits: cash flow >= -133/turn, prestige >= -0.07/turn (values are after 200 tax a turn).
- Today's settings: value +9/turn, cash -51/turn, prestige -1.79/turn - breaks the prestige floor.
- Plan: value -31/turn, cash -25/turn, prestige -0.07/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +46 vs -14, -3631 vs -23, -206 vs -41 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Essenbrucke: +7/turn
  - ship Flax Wyrm -> Brunnham: +3/turn
  - brewery 1 0.14 -> 0.07: +14/turn
  - net maker 0.00 -> 0.28: +6/turn
  - ropewalk 1 0.25 -> 0.00: +8/turn
  - weavery 1 0.50 -> 0.56: +2/turn
  - flax farm 1 4.64 -> 3.62: -4/turn
  - retting pit 1 0.91 -> 0.72: -5/turn
  - spinnery 1 1.65 -> 1.27: -17/turn
  - mansion 1 0.00 -> 0.41: -68/turn
- Model check over the last 60 turns: predicted +106/turn for the settings we ran, real +135/turn.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.95, garments 19.30, nets 30.08, beer 2.99, timber 3.33, prestige 58.52, cash 0.00
- Orders it would set: arms buy 1 (v2 None); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.04, worth +3/turn.
- Ship linen snake: Grandgues -> Essenbrucke (+7/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Brunnham (+3/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +79/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 8.5/turn (+0.0 exported); plan makes 34.4 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 450 (+161 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.95 |
| ret | 3 | 0.91 | 0.99 |
| spin | 4 | 1.65 | 1.75 |
| weave | 3 | 0.50 | 1.35 |
| sew | 2 | 0.30 | 0.84 |

Buffers: flax fibres 81/80, thread 1064/235, cloth 73/135

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.5; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
