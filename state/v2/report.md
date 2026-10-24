# v2 shadow report

Turn 13516, 2026-10-24 13:48. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 1,152, prestige 3,580 (460 free, -0.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 7 | 0 | 0 | min_holding 60, sell 82, sell @ 2.98 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 2 | 0 | 6 | 1 | 0 | stop 6, buy 2, buy @ 2.4; sell 4, sell @ 1.73 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 48 | 0 | 2 | 0 | 0 | min_holding 30, sell 8, sell @ 17.8 |
| grain | 104 | 38 | 30 | 0 | 0 | stop 156, buy 39, buy @ 3.7 |
| labour | 75 | 51 | 540 | 0 | 11 | buy 75, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 15 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34 |
| porterage | 12 | 12 | 12 | 0 | 0 | buy 12, buy @ 1.1 |

**3 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~82/turn when they restart -> v2: find out why the buy isn't filling
- **varnish**: net maker152202386007001 ran short of varnish (no buy order); labour need rises ~12/turn when they restart -> v2: add a varnish buy
- **varnish**: needed (0.1/turn) but there is NO buy order, stock 0.0 -> v2: add buy 1

## Waste (money lost now)

- **labour**: buying 75, need ~40 -> v2: buy 40

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **firewood**: floor 1.73 vs home bid 1.44: barely selling (1 of 4)
- **flax fibres**: flax fibres buffer thin: 1.2 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 57

## Notes

- labour: projection runs 100 over real use lately; planning 540, not 580

## Prestige spending, cheapest coin per prestige first

885 turns left: prestige gained now converts 98.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 44.7 | 44.7 | running |
| hold banquet 4 (pies) | mansion | 18 | 48.8 | 48.8 | thin at home: hop beer, wine, pies |
| hold banquet 3 (pies) | mansion | 8 | 50.3 | 50.3 | thin at home: hop beer, pies |
| hold banquet 2 (pies) | mansion | 7 | 51.4 | 51.4 | thin at home: wine, pies |
| jousting 3 | arena | 230 | 51.7 | 51.8 | needs a arena (build cost 24,580); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 52.0 | 52.0 | thin at home: wine, hop beer, ham, stockfish |
| hold prayer 2 | chapel | 13 | 49.9 | 52.8 | needs a chapel (build cost 31,518); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 50.8 | 53.5 | needs a church (build cost 66,284); thin at home: jewellery, candles, furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 54.0 | 54.0 | thin at home: wine |
| hold banquet 3 (fish) | mansion | 7.6 | 54.1 | 54.1 | thin at home: hop beer |
| hold banquet 2 (meat) | mansion | 6.8 | 54.3 | 54.3 | thin at home: wine |
| hold banquet 3 (meat) | mansion | 7.6 | 54.3 | 54.3 | thin at home: hop beer |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only -8 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~94 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Birkeningen | 1006 | 0.30 | 0.40 (37/turn) | beer 51 (2.98->4.73), dyed cloth 2 (11.87->15.11), cloth 6 (6.95->7.93), wine 3 (5.46->7.22) | premium ham 1 (277.2->288.8), cheese 17 (5.23->6.03), tar 3 (9.97->10.83) | +99 |
| Hanbrücken | 531 | 0.13 | 0.60 (56/turn) | windows 1 (598.5->665), timber 17 (6.51->9.5), rope 2 (73->76.95), lead ore 8 (7.46->8.46) | tar 2 (10.13->10.83), fleece 1 (4.73->5.03) | +94 |
| Heilegg | 826 | 0.21 | 0.30 (28/turn) | grindstones 1 (279.3->347.7), thread 15 (4.12->4.56), wrought iron 12 (14.28->14.72), lead ore 2 (7.46->9.59) | chisels 2 (10.5->11.59), silver ore 1 (32.76->34.58), tar 1 (9.71->10.83), tools 1 (4.6->4.84) | +72 |
| Amsdermund | 1111 | 0.36 | 0.40 (37/turn) | thread 58 (4.12->5.22), wine 14 (5.46->6.7), nets 4 (35->38), lead ore 2 (7.46->10.54) | garments 2 (18.48->19.3), tin ingots 1 (34.86->36.48), tar 3 (10.03->10.83), tools 1 (4.2->4.84) | +67 |
| Neuborn | 780 | 0.20 | 0.50 (47/turn) | beer 58 (2.98->4.2), charcoal 12 (1.9->4.41), cloth 7 (6.95->7.69), wine 7 (5.46->5.89) | - | +63 |

**Best:** Birkeningen at about +99 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 27.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| candles | 2 @ 66, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 3 @ min 6.95 | goal planner: sells 3 a turn at 6.95, keeps 33 (no one offered it) |
| cured meat | 1 @ 29.0, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 2) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 6 | 4 @ min 1.73 | goal planner: buys 2 a turn for today's rates, keeps up to 6 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 7 @ min 17.8 | goal planner: sells 7 at 17.8 (v2 had 7 at 20.0) |
| grain | 39 @ 3.7, stop 155 |  | goal planner: buys 39 a turn for today's rates, keeps up to 155 (v2 had 39) |
| labour | 75 @ 2.2, stop - |  | goal planner: buys 75 for today's rates (v2 had 40) |
| light armour | 1 @ 78.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 9 @ min 34.0 |  |
| pasties | 3 @ 14.5, stop 11 |  | goal planner: buys 3 a turn for today's rates, keeps up to 11 (v2 had 4) |
| porterage | 12 @ 1.1, stop - |  | goal planner: buys 12 for today's rates (v2 had 12) |
| rope |  | 3 @ min 71.0 | makes 1.0, uses 0.0, holds 30 (keeps 0): sells the surplus + 2/turn of the excess |
| thread |  | 8 @ min 4.12 | goal planner: sells 8 a turn at 4.12, keeps 184 (no one offered it) |
| tools | 2 @ 6.2, stop 13 |  | uses 1.5/turn (retting pit 1), makes 0.0, holds 200 = 131.4 turns |
| varnish | 1 @ 17.1, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| wax | 1 @ 20.2, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had None) |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 17.7k (cash + stock at home prices); +77/turn over 6 turns, +63/turn over 24 turns.
- Limits: cash flow >= +119/turn, prestige >= -0.67/turn (values are after 240 tax a turn).
- Today's settings: value +2/turn, cash +77/turn, prestige -0.66/turn - breaks the cash floor.
- Plan: value +67/turn, cash +119/turn, prestige -0.67/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -127 vs +35, +24 vs +5, -111 vs +35.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4, garments 0.5, nets 0.0, rope 0.1.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Essenbrucke: +3/turn
  - ship Flax Wyrm -> Brunnham: -0/turn
  - ropewalk 1 0.25 -> 0.59: +40/turn
  - sewing shop 1 0.14 -> 0.21: +6/turn
  - retting pit 1 0.76 -> 0.83: +3/turn
  - logging camp w/ tool [split timber 1] 0.00 -> 2.71: +3/turn
  - logging camp w/ tool 5.00 -> 0.00: +2/turn
  - weavery 1 0.33 -> 0.38: +2/turn
  - flax farm 1 4.60 -> 4.73: +1/turn
- Model check over the last 22 turns: predicted +143/turn for the settings we ran, real +69/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.62, thread 4.03, cloth 6.46, flax fibres 4.73, garments 18.71, nets 29.71, beer 2.82, timber 5.66, prestige 57.02, cash 0.09
- Orders it would set: candles buy 2 (v2 None); cloth sell 3 (v2 none); cured meat buy 1 (v2 2); firewood buy 2 (v2 3); labour buy 75 (v2 40); light armour buy 1 (v2 None); pasties buy 3 (v2 4); thread sell 8 (v2 none); wax buy 1 (v2 None)
- Recipe: logging camp w/ tool cut firewood 1 -> split timber 1 at 2.71, worth +4/turn.
- Ship linen snake: Grandgues -> Essenbrucke (+4/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Brunnham (+0/turn over staying).
- Management: ~13.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +76/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
- Trim: donate quarry 1: +20/turn (tax 20 saved).
- Trim: donate logging camp w/ tool: +18/turn (tax 20 saved).
- Trim: donate weavery 1: +11/turn (tax 18 saved).

## Chain sizing

Mode HOLD, garments sold 5.9/turn (+0.0 exported); plan makes 1.6 garments a turn.
Labour: own 500, everything else 427, chain may buy 0 -> chain allowance 73, chain plan 73 (-174 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.60 | 1.50 |
| ret | 3 | 0.76 | 0.27 |
| spin | 4 | 1.70 | 0.55 |
| weave | 3 | 0.33 | 0.01 |
| sew | 2 | 0.14 | 0.04 |

Buffers: flax fibres 33/41, thread 675/120, cloth 38/7
- chain plan needed 423 labour, budget left 73: cut to 73 (sewing capped at 0.04)

## Self-diagnosis

- R1: firewood slot dry: 2.5 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask none (no sellers at home)
