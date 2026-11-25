# v2 shadow report

Turn 14286, 2026-11-25 15:31. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 0, prestige 3,716 (596 free, +1.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 0 | 39 | 19 | 0 | 0 | sell 15, sell @ 3.88 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 0 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 0 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 0 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 0 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 0 | 9 | 9 | 0 | 0 | stop 36, buy 9, buy @ 3.7 |
| labour | 0 | 64 | 561 | 0 | 3 | buy 64, buy @ 2 |
| meat | 0 | 0 | 0 | 0 | 0 | none |
| nets | 0 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 0 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**7 risks, 0 waste, 4 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.0 turns (holds 0, next step uses 24/turn) -> v2: check the step that makes it
- **cured meat**: only 0.0 turns of cured meat left and buying 4 (need 12) -> v2: buy 12
- **firewood**: home ask 2.44 is above our ceiling 2.40 and last turn bought 4 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **flax fibres**: flax fibres buffer 0.0 turns (holds 0, next step uses 28/turn) -> v2: check the step that makes it
- **flax plants**: flax plants buffer 0.0 turns (holds 0, next step uses 73/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.10 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **thread**: thread buffer 0.0 turns (holds 0, next step uses 61/turn) -> v2: check the step that makes it

## Tuning

- **bread**: home ask 2.84 is above our ceiling 2.60 and last turn bought 5 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **candles**: home ask 95.50 is above our ceiling 76.00 and last turn bought 2 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **furniture**: home ask 15.70 is above our ceiling 15.50 and last turn bought 1 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: home ask 11.10 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 112 over real use lately; planning 561, not 651

## Prestige spending, cheapest coin per prestige first

115 turns left: prestige gained now converts 43.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 50.3 | 51.4 | needs a arena (build cost 32,192); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 54.0 | 55.2 | needs a arena (build cost 32,192); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 59.1 | 59.1 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 61.1 | 61.1 |  |
| hold banquet 1 (fish) | mansion | 4.2 | 61.3 | 61.3 |  |
| jousting 3 | arena | 230 | 59.9 | 62.0 | needs a arena (build cost 32,192); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 62.8 | 62.8 | thin at home: pies |
| hold banquet 4 (pies) | mansion | 18 | 64.5 | 64.5 | thin at home: stockfish |
| hold banquet 5 | mansion | 22 | 65.9 | 65.9 | thin at home: stockfish, sculptures |
| jousting 2 | arena | 210 | 65.6 | 67.9 | needs a arena (build cost 32,192); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 68.0 | 68.0 | thin at home: stockfish |
| hold banquet 4 (premium) | mansion | 20 | 68.5 | 68.5 | thin at home: stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only -3 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only 7 a turn after crew: ship stays at 0
- best towns now: Darmwald +36, Brunnham +34, Arnsreuth +33, Heidlowe +32, Etallaen +31
- Darmwald would trade: candles buy 1 @ 87.5, cured meat buy 6 @ 22.4; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~127 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.90 (114/turn) | grain 108 (3.21->5.18), bread 178 (2.98->3.78), charcoal 20 (2.58->7.74), beer 102 (4.56->5.22) | cured meat 6 (27.93->28.8), candles 1 (91.88->95.5), axes 1 (19.64->20.52), wool 4 (12.18->12.35) | +531 |
| Dortgart | 1045 | 0.44 | 0.30 (38/turn) | glass ingots 4 (68.78->76.47), steel ingots 6 (18.38->23.18), ploughs 2 (81.9->89.77), nets 3 (35.8->37.43) | sculptures 1 (2436->2736), cloth 17 (10.29->13.2), cured meat 6 (24.78->28.8), candles 1 (89.78->95.5) | +421 |
| Vauxvais | 204 | 0.07 | 0.20 (25/turn) | garments 10 (30.6->31.73), salt 5 (5.23->6.93), limestone 2 (26.04->30.02), leather 2 (29.82->30.59) | sculptures 1 (2415->2736), cloth 16 (10.24->13.2), thread 9 (3.23->6.05), bricks 3 (4.85->8.31) | +419 |
| Bordetes | 831 | 0.29 | 1.00 (127/turn) | beer 107 (4.56->7.84), furniture 10 (16.48->21.09), charcoal 16 (2.58->6.51), cookware 3 (30.87->33.82) | cured meat 5 (25.83->28.8), candles 0 (91.88->95.5), cloth 4 (12.39->13.2) | +389 |
| Heilegg | 826 | 0.29 | 1.00 (127/turn) | wrought iron 10 (18.27->27.55), beer 117 (4.56->5.46), flour 2 (23.31->34.77), coats 4 (110.25->114) | cloth 21 (9.82->13.2), cured meat 5 (24.78->28.8), garments 1 (25.41->31), paper 3 (27.72->28.69) | +324 |

**Best:** Grandgues at about +531 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 35.8, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 0 = 0.0 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 9) |
| candles | 3 @ 76.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 0 = 0.0 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 0 = 0.0 turns |
| donations | 40 @ 1.0, stop 80 |  | goal planner: buys 40 a turn for today's rates, keeps up to 80 (v2 had 60) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 0.95 | goal planner: sells 2 a turn at 0.95, keeps 219 (no one offered it) |
| furniture | 2 @ 15.5, stop 6 |  | goal planner: buys 2 a turn for today's rates, keeps up to 6 (v2 had 3) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 29.8) |
| grain | 9 @ 3.7, stop 36 |  | goal planner: buys 9 a turn for today's rates, keeps up to 36 (v2 had 18) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 61) |
| light armour | 1 @ 112, stop 1 |  | uses 0.2/turn (household upkeep), makes 0.0, holds 0 = 0.0 turns |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 0 |

## Goal: business value (live: buys, sells, ships)
- Value now 0.0k (cash + stock at home prices); -5061/turn over 6 turns, -1265/turn over 24 turns.
- Limits: cash flow >= +167/turn, prestige >= -1.23/turn (values are after 200 tax a turn).
- Today's settings: value -184/turn, cash -184/turn, prestige +1.23/turn - breaks the cash floor.
- Plan: value +18/turn, cash +18/turn, prestige -1.23/turn - could not meet the cash floor.
- Cash check (real vs predicted cash a tick, last 3): -16 vs -162, -11215 vs -170, +0 vs -183 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): beer 1.5, rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Hofkirchen: +28/turn
  - ship Flax Wyrm -> Bordetes: +13/turn
  - mansion 1 1.00 -> 0.41: +175/turn
  - net maker 0.00 -> 0.29: +5/turn
  - brewery 1 0.14 -> 0.21: +5/turn
  - flax farm 1 4.64 -> 3.56: -11/turn
  - retting pit 1 0.91 -> 0.79: +8/turn
  - spinnery 1 1.65 -> 1.35: +10/turn
  - weavery 1 0.50 -> 0.37: -26/turn
  - sewing shop 1 0.30 -> 0.23: +34/turn
- Model check over the last 59 turns: predicted -145/turn for the settings we ran, real -527/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 182.65, thread 459.15, cloth 733.13, flax fibres 544.64, garments 2121.00, nets 3355.80, beer 327.18, timber -0.00, prestige 6778.60, cash 100.00
- Orders it would set: bread buy 5 (v2 9); cloth sell 1 (v2 none); donations buy 40 (v2 60); firewood buy 4 (v2 8); flax plants sell 2 (v2 none); furniture buy 2 (v2 3); garments sell 11 (v2 10); grain buy 9 (v2 18); labour buy 64 (v2 61); meat buy 0 (v2 None)
- Ship linen snake: Grandgues -> Hofkirchen (+26/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Bordetes (+9/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 0.0 garments a turn.
Labour: own 500, everything else 375, chain may buy 0 -> chain allowance 125, chain plan 125 (-164 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 2.83 |
| ret | 3 | 0.91 | 0.57 |
| spin | 4 | 1.65 | 1.00 |
| weave | 3 | 0.50 | 0.00 |
| sew | 2 | 0.30 | 0.00 |

Buffers: flax fibres 0/34, thread 0/100, cloth 0/0
- chain plan needed 511 labour, budget left 125: cut to 125 (sewing capped at 0.00)

## Self-diagnosis

- R1: arms slot dry: 0.0 held, 0.5 a turn (gear slot (+0.4 prestige)); our buy 1 @ 35.8, home ask 34.2; our bid is already at/over the ask (sellers too thin)
- R1: beer slot dry: 0.0 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy none, home ask 4.34; 5% of cash does not buy one at 4.42
- R1: furniture slot dry: 0.0 held, 1.4 a turn (household slot (+0.4 prestige)); our buy 2 @ 15.5, home ask 15.7; 5% of cash does not buy one at 16
- R1: garments slot dry: 0.0 held, 2.1 a turn (clothing slot (+1.2 prestige)); our buy none, home ask 31.0; 5% of cash does not buy one at 31.6
- R1: meat slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 0 held of 0 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
- R6 data sanity: cash read 0 while the storehouse holds goods: business read broken?
