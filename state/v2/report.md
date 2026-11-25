# v2 shadow report

Turn 14287, 2026-11-25 16:36. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 0, prestige 3,716 (596 free, +0.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 0 | 0 | 17 | 0 | 0 | sell 15, sell @ 3.88 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 0 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 0 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 0 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 0 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 0 | 9 | 9 | 0 | 0 | stop 36, buy 9, buy @ 3.7 |
| labour | 0 | 64 | 551 | 0 | 13 | buy 64, buy @ 2 |
| meat | 0 | 0 | 0 | 0 | 0 | none |
| nets | 0 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 0 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**7 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.0 turns (holds 0, next step uses 24/turn) -> v2: check the step that makes it
- **cured meat**: mansion 1 ran short of cured meat (buy is live (4 @ 29), 4 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.0 turns of cured meat left and buying 4 (need 12) -> v2: buy 12
- **firewood**: home ask 2.44 is above our ceiling 2.40 and last turn bought 4 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **flax fibres**: flax fibres buffer 0.0 turns (holds 0, next step uses 28/turn) -> v2: check the step that makes it
- **flax plants**: flax plants buffer 0.0 turns (holds 0, next step uses 73/turn) -> v2: check the step that makes it
- **thread**: thread buffer 0.0 turns (holds 0, next step uses 75/turn) -> v2: check the step that makes it

## Tuning

- **bread**: home ask 2.84 is above our ceiling 2.60 and last turn bought 5 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **candles**: home ask 93.50 is above our ceiling 76.00 and last turn bought 2 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **furniture**: home ask 15.70 is above our ceiling 15.50 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 112 over real use lately; planning 551, not 652

## Prestige spending, cheapest coin per prestige first

114 turns left: prestige gained now converts 43.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 50.4 | 51.6 | needs a arena (build cost 32,424); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 54.1 | 55.3 | needs a arena (build cost 32,424); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 59.1 | 59.1 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 61.9 | 61.9 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 62.1 | 62.1 |  |
| jousting 3 | arena | 230 | 60.1 | 62.2 | needs a arena (build cost 32,424); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 64.4 | 64.4 |  |
| hold banquet 4 (pies) | mansion | 18 | 66.0 | 66.0 | thin at home: hop beer, stockfish |
| hold banquet 5 | mansion | 22 | 67.1 | 67.1 | thin at home: hop beer, stockfish |
| jousting 2 | arena | 210 | 65.8 | 68.1 | needs a arena (build cost 32,424); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 68.8 | 68.8 |  |
| hold banquet 4 (premium) | mansion | 20 | 69.2 | 69.2 | thin at home: hop beer, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only 3 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -1 a turn after crew: ship stays at 0
- best towns now: Gottweiler +34, Helmgreen +28, Darmwald +23, Heidlowe +22, Bremcop +22
- Gottweiler would trade: candles buy 1 @ 85.0, cured meat buy 5 @ 20.8; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~127 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 1.00 (127/turn) | bread 178 (2.98->4.27), grain 111 (3.21->4.46), charcoal 19 (2.6->8.07), firewood 31 (2.56->5.7) | axes 1 (19.64->20.9), candles 1 (92.4->93.5), cured meat 5 (27.72->28), thread 62 (5.99->6.05) | +528 |
| Heilegg | 826 | 0.29 | 0.60 (76/turn) | wrought iron 12 (18.59->27.55), spinning wheels 3 (315->332.5), casks 10 (6.51->8.84), leather 8 (29.82->32.3) | cloth 22 (10.24->13.8), cured meat 5 (24.78->28), garments 2 (25.41->31.2), copper ingots 3 (15.44->18.52) | +351 |
| Fulkirch | 1576 | 0.80 | 0.40 (51/turn) | spinning wheels 3 (315->334.4), glass ingots 3 (70.88->75.05), paper 7 (32.55->34.2), nets 6 (35.8->37.81) | sculptures 1 (2394->2603), cloth 21 (10.82->13.8), garments 2 (26.04->31.2), candles 1 (89.78->93.5) | +308 |
| Hofkirchen | 991 | 0.40 | 1.00 (127/turn) | grain 122 (3.21->5.32), tools 20 (6.83->8.55), nets 2 (35.8->38.95), glass ingots 2 (70.88->72.67) | cloth 13 (10.82->13.8), paper 6 (25.2->28.88), fleece 5 (10.71->12.63), candles 0 (84->93.5) | +288 |
| Amsdermund | 1111 | 0.48 | 0.70 (89/turn) | spinning wheels 2 (315->349.6), nets 6 (35.8->40.85), glass ingots 3 (70.88->75.05), salt 7 (5.15->6.22) | cloth 24 (10.13->13.8), thread 62 (5.25->6.05), fleece 6 (9.45->12.63), paper 9 (26.88->28.88) | +279 |

**Best:** Grandgues at about +528 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.6, stop 1 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 0 = 0.0 turns |
| beer |  | 15 @ min 3.88 |  |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 9) |
| candles | 3 @ 76.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 0 = 0.0 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| donations | 40 @ 1.0, stop 80 |  | goal planner: buys 40 a turn for today's rates, keeps up to 80 (v2 had 60) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 0.95 | goal planner: sells 2 a turn at 0.95, keeps 219 (no one offered it) |
| furniture | 2 @ 15.5, stop 6 |  | goal planner: buys 2 a turn for today's rates, keeps up to 6 (v2 had 3) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 30.0) |
| grain | 9 @ 3.7, stop 36 |  | goal planner: buys 9 a turn for today's rates, keeps up to 36 (v2 had 18) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 51) |
| light armour | 1 @ 112, stop 1 |  | uses 0.2/turn (household upkeep), makes 0.0, holds 0 = 0.0 turns |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 81.5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 0 |

## Goal: business value (live: buys, sells, ships)
- Value now 0.0k (cash + stock at home prices); -5064/turn over 6 turns, -1265/turn over 24 turns.
- Limits: cash flow >= +167/turn, prestige >= -1.23/turn (values are after 200 tax a turn).
- Today's settings: value -176/turn, cash -176/turn, prestige +1.22/turn - breaks the cash floor.
- Plan: value +25/turn, cash +25/turn, prestige -1.23/turn - could not meet the cash floor.
- Cash check (real vs predicted cash a tick, last 3): -11215 vs -170, +0 vs -183, +0 vs -184 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): beer 1.5, rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Etallaen: +12/turn
  - ship Flax Wyrm -> Donaunieder: +11/turn
  - mansion 1 1.00 -> 0.41: +172/turn
  - net maker 0.00 -> 0.29: +5/turn
  - brewery 1 0.14 -> 0.21: +5/turn
  - flax farm 1 4.64 -> 3.88: -4/turn
  - retting pit 1 0.91 -> 0.78: -0/turn
  - spinnery 1 1.65 -> 1.33: +10/turn
  - weavery 1 0.50 -> 0.35: -34/turn
  - sewing shop 1 0.30 -> 0.22: +44/turn
- Model check over the last 58 turns: predicted -146/turn for the settings we ran, real -539/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 182.70, thread 458.98, cloth 733.03, flax fibres 543.91, garments 2121.00, nets 3350.11, beer 327.23, timber -0.00, prestige 6602.74, cash 100.00
- Orders it would set: bread buy 5 (v2 9); cloth sell 1 (v2 none); donations buy 40 (v2 60); firewood buy 4 (v2 8); flax plants sell 2 (v2 none); furniture buy 2 (v2 3); garments sell 11 (v2 10); grain buy 9 (v2 18); labour buy 64 (v2 51); meat buy 0 (v2 None)
- Ship linen snake: Grandgues -> Etallaen (+9/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Donaunieder (+5/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new leatherworks (make leather armour 1) for ~4124 coin: +9/turn, payback 437 turns, doesn't pay yet (materials thin at home: nails)

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

- R1: beer slot dry: 0.0 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy none, home ask 4.28; 5% of cash does not buy one at 4.36
- R1: furniture slot dry: 0.0 held, 1.4 a turn (household slot (+0.4 prestige)); our buy 2 @ 15.5, home ask 15.7; 5% of cash does not buy one at 16
- R1: garments slot dry: 0.0 held, 2.1 a turn (clothing slot (+1.2 prestige)); our buy none, home ask 31.2; 5% of cash does not buy one at 31.8
- R1: meat slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 0 held of 0 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
- R6 data sanity: cash read 0 while the storehouse holds goods: business read broken?
