# v2 shadow report

Turn 13998, 2026-11-13 15:44. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,495, prestige 3,488 (368 free, +0.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 83 | 39 | 15 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 116, buy 39, buy @ 3.76 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 17, buy 5, buy @ 3.7 |
| labour | 64 | 64 | 543 | 0 | 21 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (4 @ 32.8), but the home ask 34.00 is above it); labour need rises ~35/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 12.30 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 21 labour expired last turn (~40 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **cured meat**: home ask 34.00 is above our ceiling 29.00 and last turn bought 4 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 12.30 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +5 crew for Flax Wyrm (crew 0.10, no projection from the game)
- labour: +5 crew for linen snake (crew 0.10, no projection from the game)
- labour: projection runs 107 over real use lately; planning 543, not 642

## Prestige spending, cheapest coin per prestige first

403 turns left: prestige gained now converts 86.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 55.5 | 55.5 | running |
| jousting 3 | arena | 230 | 56.0 | 56.4 | needs a arena (build cost 29,375); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 60.4 | 60.4 | thin at home: cured fish |
| jousting 2 | arena | 210 | 61.3 | 61.7 | needs a arena (build cost 29,375); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 61.9 | 61.9 | thin at home: cured fish |
| hold banquet 2 (pies) | mansion | 7 | 62.4 | 62.4 | thin at home: pies, candles |
| hold banquet 4 (pies) | mansion | 18 | 64.5 | 64.5 | thin at home: hop beer, stockfish, pies, candles |
| hold banquet 4 (premium) | mansion | 20 | 64.5 | 64.5 | thin at home: hop beer, stockfish, candles |
| hold mass 2 (premium) | cathedral | 360 | 62.0 | 65.1 | needs a cathedral (build cost 320,320); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 4 | mansion | 17.5 | 68.4 | 68.4 | thin at home: hop beer, stockfish, candles |
| jousting 1 | arena | 170 | 68.3 | 68.8 | needs a arena (build cost 29,375); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 69.0 | 69.0 | thin at home: hop beer, pies, candles |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 11 | 134102075 | 0 | - | cured meat 2, pasties 1 | -64 |
| linen snake | 0.1 / 0.10 | 11 | 151802239 | 0 | - | cured meat 6 | -141 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: cured meat buy 4 @ 23.8, pasties buy 2 @ 16.4; crew 0.1; est +35 a turn; stock: pasties 2 @ 16.4 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 14.5 (keep 14); best orders clear only 11 a turn after crew: ship stays at 0
- best towns now: Neuborn +43, Gottweiler +41, Großmühle +41, Brebronn +41, Karlmoor +40
- Neuborn would trade: cured meat buy 4 @ 22.4, pasties buy 2 @ 15.1; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~114 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 1.00 (114/turn) | firewood 48 (3.3->6.65), timber 26 (8.93->12.06), looms 1 (588->612.75), bread 151 (2.56->2.72) | cured meat 4 (24.57->34), tools 9 (4.94->5.32), garments 2 (22.68->23.6), cheese 3 (6.41->6.55) | +228 |
| Heidlowe | 662 | 0.20 | 0.20 (23/turn) | looms 1 (588->684), lead ore 9 (7.35->11.3), honey 5 (8.24->8.79), flour 1 (17.22->19.19) | cured meat 4 (25.41->34), premium steel 2 (39.48->45.79), cookware 4 (22.89->25.65), jewellery 2 (102.9->108.3) | +192 |
| Rotterburg | 1056 | 0.40 | 0.20 (23/turn) | looms 1 (588->703), hides 3 (13.33->17.48), tackles 1 (187.95->195.7) | cured meat 4 (26.25->34), cloth 24 (7.25->8.15), garments 2 (21.84->23.6), hop beer 2 (10.45->12.82) | +175 |
| Pontmont | 341 | 0.10 | 0.60 (68/turn) | looms 1 (588->665), bricks 10 (6.98->11.4), clay 4 (4.51->11.69), paper 3 (23.1->26.6) | cured meat 4 (26.46->34), garments 2 (22.89->23.6) | +154 |
| Kirchwerp | 1072 | 0.41 | 0.70 (79/turn) | thread 97 (4.82->5.7), looms 1 (588->622.25), butter 1 (81.38->99.75), lead ore 10 (7.35->10.45) | cured meat 4 (26.25->34), dyed cloth 7 (11.34->12.54), cloth 24 (7.56->8.15), cookware 4 (24.36->25.65) | +151 |

**Best:** Grandgues at about +228 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 36.0, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 4.0 turns |
| beer | 15 @ 3.98, stop 60 |  | uses 15.0/turn (household upkeep), makes 0.0, holds 83 = 5.5 turns |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 16 = 3.8 turns |
| cured meat | 12 @ 29.0, stop 24 | off | a building is stalled on cured meat: no sell until it runs again |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 20.6) |
| grain | 0 @ 3.7, stop 17 |  | goal planner: buys 0 a turn for today's rates, keeps up to 17 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 43) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 36.6) |
| pasties |  | 1 @ min 15.5 | goal planner: sells 1 a turn at 15.5, keeps 0 (no one offered it) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.2k (cash + stock at home prices); +47/turn over 6 turns, +80/turn over 24 turns.
- Limits: cash flow >= -437/turn, prestige >= -0.28/turn (values are after 200 tax a turn).
- Today's settings: value -181/turn, cash -147/turn, prestige +2.17/turn.
- Plan: value -10/turn, cash +10/turn, prestige -0.28/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -154 vs -144, -141 vs -157, -492 vs -146 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Neuborn: +7/turn
  - ship Flax Wyrm -> Großmühle: +1/turn
  - mansion 1 1.00 -> 0.42: +140/turn
  - brewery 1 0.14 -> 0.07: +15/turn
  - spinnery 1 1.65 -> 1.37: +5/turn
  - net maker 0.00 -> 0.29: +2/turn
  - flax farm 1 4.64 -> 4.33: -1/turn
  - weavery 1 0.50 -> 0.40: -4/turn
  - sewing shop 1 0.30 -> 0.23: +8/turn
  - ropewalk 1 0.25 -> 0.00: -23/turn
- Model check over the last 60 turns: predicted +83/turn for the settings we ran, real +11/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.95, garments 19.30, nets 30.30, beer 3.19, timber 3.83, prestige 60.93, cash 0.00
- Orders it would set: candles buy 2 (v2 None); firewood buy 1 (v2 3); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 64 (v2 43); light armour buy 1 (v2 None); pasties sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.30, worth +9/turn.
- Ship linen snake: Grandgues -> Neuborn (+3/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Großmühle (+1/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 418 (+129 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.08 |
| ret | 3 | 0.91 | 0.82 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 126/77, thread 1055/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1055 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
