# v2 shadow report

Turn 13933, 2026-11-10 22:04. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 7,401, prestige 3,438 (318 free, -1.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 25 | 4 | 4 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 26, buy 9, buy @ 3.36 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 61 | 0 | 2 | 0 | 0 | min_holding 70, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 10, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.64 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.64 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 13.00 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~75 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: home ask 13.00 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +2 crew for Flax Wyrm (crew 0.03, no projection from the game)
- labour: projection runs 100 over real use lately; planning 485, not 585

## Prestige spending, cheapest coin per prestige first

468 turns left: prestige gained now converts 90.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.8 | 49.8 | running |
| hold banquet 4 (pies) | mansion | 18 | 54.9 | 54.9 | thin at home: ham, stockfish |
| hold banquet 1 (fish) | mansion | 4.2 | 55.0 | 55.0 |  |
| jousting 3 | arena | 230 | 55.0 | 55.3 | needs a arena (build cost 26,640); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 56.3 | 56.3 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 56.4 | 56.4 |  |
| hold banquet 4 (premium) | mansion | 20 | 57.2 | 57.2 | thin at home: ham, stockfish |
| hold banquet 4 | mansion | 17.5 | 57.4 | 57.4 | thin at home: ham, stockfish |
| hold banquet 3 (meat) | mansion | 7.6 | 59.0 | 59.0 | thin at home: cured meat |
| hold banquet 3 (pies) | mansion | 8 | 59.2 | 59.2 | thin at home: pies |
| hold banquet 1 (meat) | mansion | 4.2 | 59.3 | 59.3 |  |
| hold banquet 2 (meat) | mansion | 6.8 | 59.4 | 59.4 | thin at home: cured meat |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: pasties buy 9 @ 15.9; crew 0.1; est +17 a turn; stock: pasties 9 @ 15.9 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 6 @ 16.0 (keep 14); best orders clear only 7 a turn after crew: ship stays at 0
- best towns now: Herschweig +305, Bedenis +233, Großmühle +231, Essenbrucke +230, Marmont +224
- Herschweig would trade: furniture buy 18 @ 13.0, pasties buy 14 @ 12.1; crew 0.3

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~103 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Fontaux | 411 | 0.11 | 1.00 (103/turn) | thread 82 (4.74->5.65), windows 0 (714->783.75), bread 129 (2.77->3.4), gold ore 0 (147->161.5) | flax fibres 10 (5.67->6.7), jewellery 0 (102.38->107.35) | +214 |
| Kirchwerp | 1072 | 0.37 | 0.70 (72/turn) | arms 13 (31.08->36.29), thread 92 (4.74->5.7), nets 6 (31.8->37.05), garments 10 (18.27->20.71) | flax fibres 23 (5.78->6.7), garments 2 (23.1->24.4), cured meat 2 (21->22.42), axes 1 (16.8->17.39) | +180 |
| Hofkirchen | 991 | 0.33 | 0.40 (41/turn) | thread 84 (4.74->5.7), nets 6 (31.8->39.14), gold ore 1 (147->178.6), garments 10 (18.27->20.9) | flax fibres 23 (5.78->6.7), jewellery 2 (103.95->107.35), blades 3 (14.7->15.58), furniture 1 (13.86->16.7) | +175 |
| Amsdermund | 1111 | 0.39 | 0.40 (41/turn) | nets 5 (31.8->38), garments 10 (18.27->20.9), gold ore 1 (147->165.3), cured fish 8 (24.57->26.22) | spinning wheels 3 (220.5->239.4), cloth 24 (6.41->7.7), casks 5 (5.46->6.65), flax fibres 15 (5.78->6.7) | +152 |
| Heilegg | 826 | 0.23 | 0.10 (10/turn) | gold ore 1 (147->191.9), nets 5 (31.8->38.38), garments 10 (18.27->20.33), lead ore 2 (7.3->12.25) | spinning wheels 3 (233.1->239.4), jewellery 2 (100.8->107.35), garments 2 (22.68->24.4) | +135 |

**Best:** Fontaux at about +214 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 29.8, stop 1 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 3.0 turns |
| beer | 5 @ 3.46, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 25 = 6.0 turns |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| cloth |  | 2 @ min 6.95 | goal planner: sells 2 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.18 | goal planner: sells 2 a turn at 1.18, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 22.8) |
| grain | 0 @ 3.7, stop 18 |  | goal planner: buys 0 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tapestries |  | 1 @ min 775 | goal planner: trial sale of an idle pile, 1 a turn at 775, keeps 0 (6 over) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.8k (cash + stock at home prices); +63/turn over 6 turns, +144/turn over 24 turns.
- Limits: cash flow >= -142/turn, prestige >= -0.08/turn (values are after 200 tax a turn).
- Today's settings: value +18/turn, cash -41/turn, prestige -1.80/turn - breaks the prestige floor.
- Plan: value -25/turn, cash -20/turn, prestige -0.08/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +24 vs -3, +46 vs -14, -3631 vs -23 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Corstoft: +12/turn
  - ship Flax Wyrm -> Essenbrucke: +1/turn
  - brewery 1 0.14 -> 0.08: +12/turn
  - net maker 0.00 -> 0.27: +6/turn
  - ropewalk 1 0.25 -> 0.00: +8/turn
  - weavery 1 0.50 -> 0.59: +1/turn
  - flax farm 1 4.64 -> 3.67: -4/turn
  - retting pit 1 0.91 -> 0.73: -5/turn
  - spinnery 1 1.65 -> 1.29: -13/turn
  - mansion 1 0.00 -> 0.41: -68/turn
- Model check over the last 60 turns: predicted +106/turn for the settings we ran, real +132/turn.
- Worth of one more unit per turn: labour 1.66, thread 4.17, cloth 6.66, flax fibres 4.94, garments 19.27, nets 29.98, beer 2.91, timber 3.33, prestige 58.22, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 2 (v2 none); firewood buy 1 (v2 3); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None); tapestries sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.03, worth +3/turn.
- Ship linen snake: Grandgues -> Corstoft (+12/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Essenbrucke (+1/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +79/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 9.3/turn (+0.0 exported); plan makes 36.9 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 478 (+189 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 5.21 |
| ret | 3 | 0.91 | 1.04 |
| spin | 4 | 1.65 | 1.84 |
| weave | 3 | 0.50 | 1.45 |
| sew | 2 | 0.30 | 0.90 |

Buffers: flax fibres 77/83, thread 1064/244, cloth 73/145

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.64; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
