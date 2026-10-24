# v2 shadow report

Turn 13517, 2026-10-24 14:03. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 816, prestige 3,579 (459 free, -0.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 54 | 0 | 7 | 0 | 0 | min_holding 60, sell 82, sell @ 2.98 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 6 | 0 | 2 | 5 | 0 | stop 6, buy 2, buy @ 2.4; sell 4, sell @ 1.73 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 47 | 0 | 2 | 0 | 0 | min_holding 30, sell 7, sell @ 17.8 |
| grain | 143 | 39 | 0 | 0 | 0 | stop 155, buy 39, buy @ 3.7 |
| labour | 95 | 75 | 500 | 0 | 75 | buy 95, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 15 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34 |
| porterage | 12 | 12 | 12 | 0 | 0 | buy 12, buy @ 1.1 |

**2 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), home ask 1.51 x5, yet 0 bought last turn); labour need rises ~82/turn when they restart -> v2: find out why the buy isn't filling
- **varnish**: net maker152202386007001 ran short of varnish (buy is live (1 @ 17.1), home ask 16.30 x1, yet 0 bought last turn); labour need rises ~12/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 75 labour expired last turn (~113 coin): holding 95 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.2 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 57

## Notes

- labour: projection runs 100 over real use lately; planning 512, not 612
- labour expiry guard: 75 bought labour expired last turn, buy 0 (not 12) this turn

## Prestige spending, cheapest coin per prestige first

884 turns left: prestige gained now converts 98.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 45.0 | 45.0 | running |
| hold banquet 4 (pies) | mansion | 18 | 49.4 | 49.4 | thin at home: hop beer, ham, pies |
| hold banquet 3 (pies) | mansion | 8 | 49.9 | 49.9 | thin at home: hop beer, pies |
| hold banquet 2 (pies) | mansion | 7 | 50.6 | 50.6 | thin at home: pies |
| jousting 3 | arena | 230 | 51.7 | 51.9 | needs a arena (build cost 23,879); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 52.8 | 52.8 | thin at home: hop beer, ham, stockfish |
| hold prayer 2 | chapel | 13 | 49.9 | 52.8 | needs a chapel (build cost 30,782); thin at home: furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 53.4 | 53.4 |  |
| hold sermon 2 (candles) | church | 31 | 50.8 | 53.4 | needs a church (build cost 65,523); thin at home: candles, furniture |
| hold banquet 3 (fish) | mansion | 7.6 | 53.7 | 53.7 | thin at home: hop beer |
| jousting 1 | arena | 170 | 53.5 | 53.7 | needs a arena (build cost 23,879); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 54.4 | 54.4 |  |

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
| Hanbrücken | 531 | 0.13 | 0.60 (57/turn) | windows 1 (598.5->665), timber 17 (6.51->9.5), rope 2 (73->76.95), lead ore 8 (7.46->8.46) | tar 2 (10.13->10.83), fleece 1 (4.73->5.03) | +94 |
| Heilegg | 826 | 0.21 | 0.30 (28/turn) | grindstones 1 (279.3->347.7), thread 15 (4.12->4.56), wrought iron 12 (14.28->14.72), lead ore 2 (7.46->9.59) | chisels 2 (10.5->11.59), silver ore 1 (32.76->34.58), tar 1 (9.71->10.83), tools 1 (4.6->4.84) | +72 |
| Amsdermund | 1111 | 0.36 | 0.40 (38/turn) | thread 58 (4.12->5.22), wine 14 (5.46->6.7), nets 4 (35->38), lead ore 2 (7.46->10.54) | garments 2 (18.48->19.3), tin ingots 1 (34.86->36.48), tar 3 (10.03->10.83), tools 1 (4.2->4.84) | +67 |
| Birkeningen | 1006 | 0.31 | 0.40 (38/turn) | beer 51 (3.68->4.73), dyed cloth 2 (11.87->15.11), wine 3 (5.46->7.22), thread 5 (4.12->4.94) | premium ham 1 (277.2->288.8), cheese 17 (5.23->6.03), tar 3 (9.97->10.83) | +60 |
| Nürnnieder | 520 | 0.13 | 0.10 (9/turn) | thread 57 (4.12->5.13), garments 7 (18.1->18.81), wine 4 (5.46->5.61) | steel ingots 1 (12.92->13.68) | +55 |

**Best:** Hanbrücken at about +94 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 24.4, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 3.0 turns |
| beer | 7 @ 3.66, stop 27 |  | uses 6.5/turn (household upkeep, mansion 1), makes 0.0, holds 54 = 8.2 turns |
| cured meat | 1 @ 29.0, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 2) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 2 @ 2.4, stop 16 | 4 @ min 1.74 | uses 7.6/turn (household upkeep), makes 6.5, holds 6 = 6.1 turns |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 9 @ min 17.8 | goal planner: sells 9 at 17.8 (v2 had 9 at 20.0) |
| grain | 0 @ 3.7, stop 150 |  | goal planner: buys 0 a turn for today's rates, keeps up to 150 (v2 had 0) |
| labour | 95 @ 2.2, stop - |  | goal planner: buys 95 for today's rates (v2 had 0) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 9 @ min 34.0 |  |
| pasties | 3 @ 14.5, stop 11 |  | goal planner: buys 3 a turn for today's rates, keeps up to 11 (v2 had 4) |
| porterage | 13 @ 1.1, stop - |  | goal planner: buys 13 for today's rates (v2 had 12) |
| rope |  | 4 @ min 71.0 | makes 2.0, uses 0.0, holds 31 (keeps 0): sells the surplus + 2/turn of the excess |
| thread |  | 8 @ min 4.12 | goal planner: sells 8 a turn at 4.12, keeps 221 (no one offered it) |
| tools | 2 @ 6.2, stop 16 |  | uses 2.0/turn (retting pit 1), makes 0.0, holds 199 = 101.5 turns |
| varnish | 1 @ 17.1, stop 1 |  | uses 0.1/turn (observed), makes 0.0, holds 1 = 8.0 turns |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 18.1k (cash + stock at home prices); +130/turn over 6 turns, +76/turn over 24 turns.
- Limits: cash flow >= +133/turn, prestige >= -0.66/turn (values are after 240 tax a turn).
- Today's settings: value +42/turn, cash +93/turn, prestige -0.76/turn - breaks the prestige floor and cash floor.
- Plan: value +55/turn, cash +133/turn, prestige -0.66/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +24 vs +5, -111 vs +35, -336 vs +77 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4, garments 0.5, nets 0.0, rope 0.1.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Essenbrucke: +3/turn
  - ship Flax Wyrm -> Brunnham: +0/turn
  - ropewalk 1 0.50 -> 0.59: +9/turn
  - weavery 1 0.33 -> 0.38: +2/turn
  - logging camp w/ tool 5.00 -> 5.61: +0/turn
  - flax farm 1 4.60 -> 4.44: -1/turn
  - retting pit 1 0.83 -> 0.78: +0/turn
  - spinnery 1 1.70 -> 1.60: +0/turn
- Model check over the last 22 turns: predicted +140/turn for the settings we ran, real +83/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.64, thread 4.03, cloth 6.49, flax fibres 4.64, garments 18.84, nets 29.97, beer 2.93, timber 7.09, prestige 59.01, cash 0.09
- Orders it would set: candles buy 2 (v2 None); cured meat buy 1 (v2 2); grain buy 38 (v2 0); labour buy 95 (v2 0); light armour buy 1 (v2 None); pasties buy 3 (v2 4); porterage buy 13 (v2 12); thread sell 8 (v2 none); wax buy 1 (v2 None)
- Ship linen snake: Grandgues -> Essenbrucke (+4/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Brunnham (+0/turn over staying).
- Management: ~13.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +78/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
- Trim: donate quarry 1: +21/turn (tax 20 saved).
- Trim: donate logging camp w/ tool: +20/turn (tax 20 saved).

## Chain sizing

Mode HOLD, garments sold 5.9/turn (+0.0 exported); plan makes 0.0 garments a turn.
Labour: own 500, everything else 434, chain may buy 0 -> chain allowance 66, chain plan 94 (-166 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.60 | 2.14 |
| ret | 3 | 0.83 | 0.38 |
| spin | 4 | 1.70 | 0.79 |
| weave | 3 | 0.33 | 0.00 |
| sew | 2 | 0.21 | 0.00 |

Buffers: flax fibres 34/47, thread 687/138, cloth 35/0
- chain plan needed 94 labour, budget left 66: cut to 94

## Self-diagnosis

Nothing found this run.
