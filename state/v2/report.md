# v2 shadow report

Turn 13919, 2026-11-10 08:00. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,642, prestige 3,466 (346 free, -1.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 10 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 29 | 29 | 500 | 0 | 29 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), but the home ask 3.02 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.02 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 12.20 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 29 labour expired last turn (~43 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: home ask 12.20 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +2 crew for Flax Wyrm (crew 0.05, no projection from the game)
- labour: projection runs 100 over real use lately; planning 501, not 601

## Prestige spending, cheapest coin per prestige first

482 turns left: prestige gained now converts 91.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 45.3 | 45.3 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 53.5 | 53.5 |  |
| hold banquet 1 (fish) | mansion | 4.2 | 53.6 | 53.6 |  |
| jousting 3 | arena | 230 | 54.0 | 54.2 | needs a arena (build cost 24,452); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 54.6 | 54.6 | thin at home: hop beer |
| hold banquet 4 (pies) | mansion | 18 | 54.7 | 54.7 | thin at home: hop beer, ham, stockfish, pies |
| hold banquet 4 (premium) | mansion | 20 | 55.8 | 55.8 | thin at home: hop beer, ham, stockfish, premium cheese |
| hold banquet 4 | mansion | 17.5 | 56.1 | 56.1 | thin at home: hop beer, ham, stockfish |
| jousting 2 | arena | 210 | 59.1 | 59.4 | needs a arena (build cost 24,452); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 60.1 | 60.1 |  |
| hold banquet 3 (meat) | mansion | 7.6 | 60.5 | 60.5 | thin at home: hop beer |
| hold banquet 3 (pies) | mansion | 8 | 61.6 | 61.6 | thin at home: pasties, hop beer, pies |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: pasties buy 11 @ 14.5; crew 0.1; est +39 a turn; stock: pasties 11 @ 14.5 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 5 @ 16.2 (keep 14); best orders clear only 4 a turn after crew: ship stays at 0
- best towns now: Bedenis +136, Essenbrucke +134, Dortgart +128, Disscester +126, Großmühle +124
- Bedenis would trade: furniture buy 9 @ 14.5, pasties buy 10 @ 15.1; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~95 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Fontaux | 411 | 0.10 | 1.00 (95/turn) | thread 70 (4.72->7.27), bread 128 (2.14->3.1), timber 20 (7.67->10.45), charcoal 15 (2.96->5.27) | candles 0 (79.8->84.5), bricks 0 (11.45->15.67), flax plants 4 (1.49->1.75), yarn 3 (4.81->4.99) | +338 |
| Pontmont | 341 | 0.09 | 1.00 (95/turn) | garments 7 (17.95->29.26), bread 118 (2.14->3.12), timber 27 (7.67->9.97), gold ore 0 (150.15->182.4) | flax fibres 2 (6.41->7.2), pickaxes 0 (9.61->10.73), flax plants 0 (1.58->1.75) | +252 |
| Rouhomme | 368 | 0.09 | 0.50 (48/turn) | bread 154 (2.14->2.98), garments 10 (17.95->22.61), thread 24 (4.72->6.27), hinges 1 (38.22->43.7) | tools 17 (4.89->5.56), blades 4 (13.65->15.67), bricks 1 (6.14->15.67), cloth 12 (7.25->7.75) | +214 |
| Etallaen | 774 | 0.20 | 1.00 (95/turn) | bread 85 (2.14->3.32), beer 31 (3.46->5.46), garments 5 (17.95->21.85), charcoal 11 (2.96->5.89) | nets 7 (34.65->37.81), bricks 0 (9.29->15.67), candles 0 (81.9->84.5), yarn 1 (4.62->4.99) | +193 |
| Blanans | 297 | 0.07 | 1.00 (95/turn) | garments 9 (17.95->24.32), bread 140 (2.14->2.62), limestone 5 (17.22->23.75), hinges 0 (38.22->49.88) | jewellery 0 (73.5->101.65), bricks 0 (9.13->15.67), dyed cloth 1 (12.81->14.15), flax plants 8 (1.35->1.75) | +172 |

**Best:** Fontaux at about +338 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.2, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 3.0 turns |
| beer | 8 @ 3.5, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 10 = 2.5 turns |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| cloth |  | 2 @ min 6.95 | goal planner: sells 2 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 24.4) |
| grain | 0 @ 3.7, stop 34 |  | goal planner: buys 0 a turn for today's rates, keeps up to 34 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 1) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 37.6) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.4k (cash + stock at home prices); +136/turn over 6 turns, +183/turn over 24 turns.
- Limits: cash flow >= -318/turn, prestige >= -0.19/turn (values are after 200 tax a turn).
- Today's settings: value +78/turn, cash +49/turn, prestige -1.94/turn - breaks the prestige floor.
- Plan: value +5/turn, cash +8/turn, prestige -0.19/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +89 vs +75, +74 vs +68, -635 vs +63 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Gosschweig: +9/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +9/turn
  - sewing shop 1 0.30 -> 0.36: -3/turn
  - weavery 1 0.50 -> 0.60: +7/turn
  - ropewalk 1 0.25 -> 0.00: +2/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.15: +9/turn
  - flax farm 1 4.64 -> 5.30: -4/turn
  - retting pit 1 0.91 -> 1.04: +2/turn
  - spinnery 1 1.65 -> 1.83: +6/turn
- Model check over the last 59 turns: predicted +105/turn for the settings we ran, real +64/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.51, thread 3.79, cloth 6.06, flax fibres 4.49, garments 17.53, nets 27.49, beer 2.71, timber 3.31, prestige 60.25, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 2 (v2 none); firewood buy 2 (v2 3); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 0); labour buy 29 (v2 1); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.15, worth +11/turn.
- Ship linen snake: Grandgues -> Gosschweig (+9/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +75/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1593 coin: +1/turn, payback 1079 turns, doesn't pay yet (materials thin at home: limestone)

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 430 (+141 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.75 |
| ret | 3 | 0.91 | 0.95 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 1054/228, cloth 74/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask 3.02; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1054 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
- R5: flax fibres buy not filling: bid 5.05 under the home ask 7.1 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
