# v2 shadow report

Turn 14288, 2026-11-25 17:42. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 0, prestige 3,716 (596 free, -0.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 0 | 0 | 14 | 0 | 0 | sell 15, sell @ 3.88 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 0 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 0 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 0 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 0 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 0 | 9 | 9 | 0 | 0 | stop 36, buy 9, buy @ 3.7 |
| labour | 0 | 64 | 552 | 0 | 12 | buy 64, buy @ 2 |
| meat | 0 | 0 | 0 | 0 | 0 | none |
| nets | 0 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 0 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**7 risks, 0 waste, 4 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.0 turns (holds 0, next step uses 24/turn) -> v2: check the step that makes it
- **cured meat**: mansion 1 ran short of cured meat (buy is live (4 @ 29), 4 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.0 turns of cured meat left and buying 4 (need 12) -> v2: buy 12
- **firewood**: home ask 2.46 is above our ceiling 2.40 and last turn bought 4 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **flax fibres**: flax fibres buffer 0.0 turns (holds 0, next step uses 28/turn) -> v2: check the step that makes it
- **flax plants**: flax plants buffer 0.0 turns (holds 0, next step uses 73/turn) -> v2: check the step that makes it
- **thread**: thread buffer 0.0 turns (holds 0, next step uses 75/turn) -> v2: check the step that makes it

## Tuning

- **bread**: home ask 2.84 is above our ceiling 2.60 and last turn bought 5 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **candles**: home ask 96.50 is above our ceiling 76.00 and last turn bought 2 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **furniture**: home ask 15.90 is above our ceiling 15.50 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: home ask 11.40 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 107 over real use lately; planning 552, not 652

## Prestige spending, cheapest coin per prestige first

113 turns left: prestige gained now converts 43.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 59.1 | 59.1 | running |
| jousting 3 | arena | 230 | 59.5 | 61.5 | needs a arena (build cost 31,181); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 61.9 | 61.9 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 61.9 | 61.9 |  |
| hold banquet 2 (pies) | mansion | 7 | 64.5 | 64.5 |  |
| hold banquet 4 (pies) | mansion | 18 | 65.8 | 65.8 | thin at home: hop beer, stockfish |
| hold banquet 5 | mansion | 22 | 67.0 | 67.0 | thin at home: hop beer, stockfish |
| jousting 2 | arena | 210 | 65.1 | 67.4 | needs a arena (build cost 31,181); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 68.3 | 68.3 |  |
| hold banquet 4 | mansion | 17.5 | 69.3 | 69.3 | thin at home: hop beer, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 70.0 | 70.0 | thin at home: hop beer, stockfish |
| hold banquet 1 (meat) | mansion | 4.2 | 70.4 | 70.4 | running |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only -3 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only 2 a turn after crew: ship stays at 0
- best towns now: Gottweiler +28, Rotterburg +21, Darmwald +20, Bremcop +19, Arnsreuth +18
- Gottweiler would trade: candles buy 1 @ 85.0, cured meat buy 4 @ 21.0; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~127 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.50 (64/turn) | bread 177 (2.98->4.5), grain 112 (3.19->5.32), charcoal 19 (2.6->8.46), nets 1 (0->33.25) | candles 1 (91.88->96.5), cloth 3 (12.71->13.3), cured meat 4 (27.3->27.8), yarn 6 (6.56->6.79) | +649 |
| Hofkirchen | 991 | 0.40 | 1.00 (127/turn) | nets 4 (0->39.33), grain 121 (3.19->5.08), glass ingots 1 (70.88->83.6), flour 3 (22.89->29.07) | cloth 13 (10.92->13.3), flax fibres 21 (5.93->7.65), paper 3 (25.2->28.88), candles 0 (84->96.5) | +426 |
| Heilegg | 826 | 0.29 | 0.60 (76/turn) | nets 6 (0->36.1), spinning wheels 3 (315->343.9), flour 4 (22.89->29.26), leather 8 (29.82->32.3) | cloth 21 (12.18->13.3), cured meat 4 (24.78->27.8), garments 2 (25.41->30.6), copper ingots 3 (17.22->20.14) | +422 |
| Angefont | 686 | 0.23 | 0.40 (51/turn) | nets 6 (0->31.35), ploughs 5 (81.9->88.83), rope 1 (83.5->84.55) | sculptures 1 (2478->2603), thread 62 (4.94->5.95), seeds 8 (1.78->3.23), flax fibres 24 (6.93->7.65) | +400 |
| Amsdermund | 1111 | 0.48 | 0.70 (89/turn) | nets 4 (0->41.23), spinning wheels 2 (315->361), ploughs 2 (81.9->87.88), salt 3 (5.35->6.27) | cloth 24 (10.19->13.3), chisels 3 (8.4->14.44), flax fibres 17 (5.83->7.65), thread 62 (5.25->5.95) | +396 |

**Best:** Grandgues at about +649 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 15 @ min 3.88 |  |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 9) |
| candles | 3 @ 76.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 0 = 0.0 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 60) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 0.95 | goal planner: sells 2 a turn at 0.95, keeps 219 (no one offered it) |
| furniture | 2 @ 15.5, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had 3) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 29.6) |
| grain | 9 @ 3.7, stop 36 |  | goal planner: buys 9 a turn for today's rates, keeps up to 36 (v2 had 18) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 52) |
| light armour | 1 @ 112, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had 1) |
| nets |  | 9 @ min 33.2 | goal planner: sells 9 at 33.2 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 81.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 0 |

## Goal: business value (live: buys, sells, ships)
- Value now 0.0k (cash + stock at home prices); -5078/turn over 6 turns, -1267/turn over 24 turns.
- Limits: cash flow >= +167/turn, prestige >= -1.23/turn (values are after 200 tax a turn).
- Today's settings: value -182/turn, cash -182/turn, prestige +1.22/turn - breaks the cash floor.
- Plan: value +19/turn, cash +19/turn, prestige -1.23/turn - could not meet the cash floor.
- Cash check (real vs predicted cash a tick, last 3): +0 vs -183, +0 vs -184, +0 vs -176.
- Route sales counted at most (what the ships really sold, a turn): beer 1.5, rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Hofkirchen: +6/turn
  - ship Flax Wyrm -> Bordetes: +11/turn
  - mansion 1 1.00 -> 0.42: +172/turn
  - brewery 1 0.14 -> 0.23: +6/turn
  - flax farm 1 4.64 -> 3.71: -7/turn
  - retting pit 1 0.91 -> 0.74: -1/turn
  - spinnery 1 1.65 -> 1.27: +21/turn
  - weavery 1 0.50 -> 0.43: -11/turn
- Model check over the last 59 turns: predicted -146/turn for the settings we ran, real -530/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 182.67, thread 459.08, cloth 733.09, flax fibres 544.35, garments 2121.00, nets 1836.34, beer 326.37, timber -0.00, prestige 6691.75, cash 100.00
- Orders it would set: bread buy 5 (v2 9); cloth sell 1 (v2 none); donations buy 40 (v2 60); firewood buy 4 (v2 8); flax plants sell 2 (v2 none); furniture buy 2 (v2 3); garments sell 11 (v2 10); grain buy 9 (v2 18); labour buy 64 (v2 52); meat buy 0 (v2 None)
- Ship linen snake: Grandgues -> Hofkirchen (+7/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Bordetes (+9/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new chandlery (make candles 1) for ~5553 coin: +13/turn, payback 438 turns, doesn't pay yet (materials thin at home: bricks, nails)

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

- R1: arms slot dry: 0.0 held, 0.5 a turn (gear slot (+0.4 prestige)); our buy 1 @ 34.6, home ask 33.0; our bid is already at/over the ask (sellers too thin)
- R1: beer slot dry: 0.0 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy none, home ask 4.02; 5% of cash does not buy one at 4.1
- R1: furniture slot dry: 0.0 held, 1.4 a turn (household slot (+0.4 prestige)); our buy 2 @ 15.5, home ask 15.9; 5% of cash does not buy one at 16.2
- R1: garments slot dry: 0.0 held, 2.1 a turn (clothing slot (+1.2 prestige)); our buy none, home ask 30.6; 5% of cash does not buy one at 31.2
- R1: meat slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask 2.24; 5% of cash does not buy one at 2.28
- R6 data sanity: cash read 0 while the storehouse holds goods: business read broken?
