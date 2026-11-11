# v2 shadow report

Turn 13936, 2026-11-11 01:20. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 6,786, prestige 3,506 (386 free, -2.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 26 | 4 | 4 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 26, buy 9, buy @ 3.36 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 1, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 22 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.94 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.94 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~79 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: +2 crew for Flax Wyrm (crew 0.04, no projection from the game)
- labour: projection runs 100 over real use lately; planning 485, not 585

## Prestige spending, cheapest coin per prestige first

465 turns left: prestige gained now converts 90.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.9 | 51.9 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 55.5 | 55.5 |  |
| jousting 3 | arena | 230 | 55.6 | 55.9 | needs a arena (build cost 28,856); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 56.6 | 56.6 | thin at home: wine, ham, stockfish |
| hold banquet 2 (fish) | mansion | 6.8 | 57.5 | 57.5 | thin at home: wine |
| hold banquet 3 (fish) | mansion | 7.6 | 57.7 | 57.7 |  |
| hold banquet 4 | mansion | 17.5 | 58.9 | 58.9 | thin at home: wine, ham, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 59.3 | 59.3 | thin at home: wine, ham, stockfish |
| hold banquet 1 (meat) | mansion | 4.2 | 60.2 | 60.2 |  |
| hold banquet 3 (meat) | mansion | 7.6 | 60.7 | 60.7 |  |
| hold banquet 2 (meat) | mansion | 6.8 | 60.8 | 60.8 | thin at home: wine |
| jousting 2 | arena | 210 | 60.9 | 61.2 | needs a arena (build cost 28,856); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: pasties buy 9 @ 15.5; crew 0.1; est +20 a turn; stock: pasties 9 @ 15.5 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 7 @ 16.0 (keep 14); best orders clear only 10 a turn after crew: ship stays at 0
- best towns now: Calange +282, Marmont +276, Clairlond +245, Boistot +235, Fulkirch +232
- Calange would trade: furniture buy 22 @ 13.1; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~107 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.34 | 0.40 (43/turn) | thread 72 (4.88->5.7), flax fibres 9 (6.1->10.16), nets 6 (33.6->39.14), grain 2 (2.78->5.32) | candles 1 (84.53->90), cloth 24 (7.56->8.05), nails 3 (6.35->6.89), tiles 2 (3.72->7.6) | +109 |
| Heidlowe | 662 | 0.19 | 0.30 (32/turn) | beer 51 (3.46->4.39), nets 5 (33.6->39.14), garments 10 (22.8->23.94), cheese 8 (7.09->7.74) | candles 1 (84.53->90), flax fibres 8 (5.83->6.8), tiles 2 (3.65->7.6), gold ore 1 (185.85->190) | +88 |
| Grandgues | 152 | 0.04 | 0.20 (21/turn) | nets 6 (33.6->39.33), timber 27 (7.77->9.4), cheese 9 (7.09->7.6), flax plants 1 (1.4->1.51) | cloth 11 (7.4->8.05), tiles 2 (5.21->7.6), candles 1 (88.2->90), furniture 13 (16.48->16.81) | +84 |
| Pontmont | 341 | 0.10 | 0.60 (64/turn) | timber 38 (7.77->9.97), cheese 9 (7.09->9.69), limestone 1 (21.63->28.31), nets 4 (33.6->34.39) | cloth 11 (7.35->8.05), gold ore 1 (185.85->190), tiles 2 (5.15->7.6), flax fibres 4 (6.2->6.8) | +76 |
| Chribruck | 1202 | 0.46 | 0.10 (11/turn) | coats 1 (91.35->142.5), nets 5 (33.6->38.38), honey 3 (7.93->9.12) | candles 1 (85.05->90) | +72 |

**Best:** Hofkirchen at about +109 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.6, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 1 = 2.0 turns |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 16 = 3.9 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.18 | goal planner: sells 2 a turn at 1.18, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 22.2) |
| grain | 0 @ 3.7, stop 17 |  | goal planner: buys 0 a turn for today's rates, keeps up to 17 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tapestries |  | 1 @ min 685 | goal planner: trial sale of an idle pile, 1 a turn at 685, keeps 0 (6 over) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 29.1k (cash + stock at home prices); -248/turn over 6 turns, +65/turn over 24 turns.
- Limits: cash flow >= -116/turn, prestige >= -0.36/turn (values are after 200 tax a turn).
- Today's settings: value +4/turn, cash -55/turn, prestige -2.14/turn - breaks the prestige floor.
- Plan: value -41/turn, cash -38/turn, prestige -0.36/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -206 vs -41, -214 vs -51, -195 vs -44 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Marmont: +8/turn
  - ship Flax Wyrm -> Calange: +1/turn
  - brewery 1 0.14 -> 0.07: +14/turn
  - net maker 0.00 -> 0.29: +6/turn
  - ropewalk 1 0.25 -> 0.00: +9/turn
  - spinnery 1 1.65 -> 1.34: +5/turn
  - retting pit 1 0.91 -> 0.76: -5/turn
  - flax farm 1 4.64 -> 3.83: -9/turn
  - mansion 1 0.00 -> 0.42: -72/turn
- Model check over the last 60 turns: predicted +107/turn for the settings we ran, real +137/turn.
- Worth of one more unit per turn: labour 1.58, thread 3.96, cloth 6.32, flax fibres 4.70, garments 18.30, nets 28.68, beer 2.95, timber 3.33, prestige 58.52, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax plants sell 2 (v2 none); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None); tapestries sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.04, worth +3/turn.
- Ship linen snake: Grandgues -> Marmont (+8/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Calange (+1/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +70/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 6.1/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 430 (+141 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.75 |
| ret | 3 | 0.91 | 0.95 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 89/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.94; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
