# v2 shadow report

Turn 14285, 2026-11-25 14:25. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 0, prestige 3,714 (594 free, -0.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 0 | 39 | 14 | 0 | 0 | sell 17, sell @ 3.88; stop 116, buy 39, buy @ 4.34 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 0 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 0 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 0 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 0 | 9 | 9 | 0 | 0 | stop 36, buy 9, buy @ 3.7 |
| labour | 0 | 64 | 557 | 0 | 7 | buy 64, buy @ 2 |
| meat | 0 | 0 | 0 | 0 | 0 | none |
| nets | 0 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 0 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**7 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.0 turns (holds 0, next step uses 24/turn) -> v2: check the step that makes it
- **cured meat**: mansion 1 ran short of cured meat (buy is live (4 @ 29), but the home ask 29.80 is above it); labour need rises ~35/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **cured meat**: only 0.0 turns of cured meat left and buying 4 (need 12) -> v2: buy 12
- **firewood**: home ask 2.46 is above our ceiling 2.40 and last turn bought 4 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **flax fibres**: flax fibres buffer 0.0 turns (holds 0, next step uses 28/turn) -> v2: check the step that makes it
- **flax plants**: flax plants buffer 0.0 turns (holds 0, next step uses 73/turn) -> v2: check the step that makes it
- **thread**: thread buffer 0.0 turns (holds 0, next step uses 75/turn) -> v2: check the step that makes it

## Tuning

- **candles**: home ask 92.50 is above our ceiling 76.00 and last turn bought 0 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **cured meat**: home ask 29.80 is above our ceiling 29.00 and last turn bought 4 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **hold banquet 2 (fish)**: hold banquet 2 (fish) costs 60.9 coin per prestige at mansion, vs 71.8 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch

## Notes

- labour: projection runs 107 over real use lately; planning 562, not 669

## Prestige spending, cheapest coin per prestige first

116 turns left: prestige gained now converts 44.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 50.6 | 51.7 | needs a arena (build cost 32,352); thin at home: protection, light armour, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 54.3 | 55.4 | needs a arena (build cost 32,352); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| maintain 2 | park | 2 | 58.8 | 58.8 | thin at home: sculptures |
| maintain 1 | park | 0.5 | 59.4 | 59.4 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 60.9 | 60.9 |  |
| hold banquet 1 (fish) | mansion | 4.2 | 61.4 | 61.4 |  |
| hold banquet 5 | mansion | 22 | 61.8 | 61.8 | thin at home: hop beer, stockfish, sculptures |
| hold banquet 2 (pies) | mansion | 7 | 61.9 | 61.9 |  |
| jousting 3 | arena | 230 | 60.3 | 62.3 | needs a arena (build cost 32,352); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 64.7 | 64.7 | thin at home: hop beer, stockfish |
| jousting 2 | arena | 210 | 66.0 | 68.3 | needs a arena (build cost 32,352); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 68.4 | 68.4 | thin at home: hop beer, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 12 | 151802239 | 0 | - | cured meat 3 | -80 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only -7 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only 3 a turn after crew: ship stays at 0
- best towns now: Birkeningen +25, Darmwald +24, Etallaen +22, Bremcop +22, Rotterburg +21
- Birkeningen would trade: candles buy 1 @ 85.5, cured meat buy 4 @ 22.6; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~126 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.90 (114/turn) | grain 106 (3.4->5.03), bread 179 (2.65->3.34), charcoal 20 (2.58->7.36), firewood 26 (2.58->6.27) | cured meat 4 (27.93->29.8), fleece 2 (10.45->13.01), thread 62 (5.93->6.05), candles 1 (92.4->92.5) | +530 |
| Pontmont | 341 | 0.12 | 0.50 (63/turn) | timber 34 (8.45->15.58), cured fish 13 (24.57->26.41), candles 4 (97.12->98.8), rope 1 (84->87.88) | spinning wheels 2 (315->326.8), fleece 6 (9.5->13.01), thread 18 (5.25->6.05), bricks 8 (5.25->8.26) | +286 |
| Rotterburg | 1056 | 0.44 | 0.30 (38/turn) | furniture 14 (16.17->20.14), glass ingots 4 (68.25->76.95), dyed yarn 2 (6.77->7.46) | looms 1 (651->741), cloth 24 (9.82->12.7), cured meat 4 (23.73->29.8), fleece 7 (9.92->13.01) | +251 |
| Heilegg | 826 | 0.29 | 0.70 (89/turn) | flour 3 (22.26->38), coats 4 (109.2->114), limestone 2 (24.99->44.84), glass ingots 4 (68.25->72.67) | cloth 24 (10.4->12.7), cured meat 4 (24.78->29.8), fleece 7 (10.71->13.01), garments 2 (25.41->31.8) | +231 |
| Hofkirchen | 991 | 0.40 | 1.00 (126/turn) | grain 106 (3.4->4.89), tools 16 (6.83->9.5), furniture 9 (16.17->19.19), canvas 2 (42.42->46.55) | cloth 11 (8.14->12.7), candles 0 (73.5->92.5), fleece 4 (10.61->13.01), paper 1 (25.2->28.12) | +216 |

**Best:** Grandgues at about +530 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 36.0, stop 1 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 0 = 0.0 turns |
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
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 30.4) |
| grain | 9 @ 3.7, stop 36 |  | goal planner: buys 9 a turn for today's rates, keeps up to 36 (v2 had 18) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 62) |
| light armour | 1 @ 112, stop 1 |  | uses 0.2/turn (household upkeep), makes 0.0, holds 0 = 0.0 turns |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 77.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| timber | 1 @ 8.6, stop 1 |  | uses 0.0/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 0 |

## Goal: business value (live: buys, sells, ships)
- Value now 0.0k (cash + stock at home prices); -5065/turn over 6 turns, -1270/turn over 24 turns.
- Limits: cash flow >= +167/turn, prestige >= -1.23/turn (values are after 200 tax a turn).
- Today's settings: value -183/turn, cash -183/turn, prestige +1.23/turn - breaks the cash floor.
- Plan: value +18/turn, cash +18/turn, prestige -1.23/turn - could not meet the cash floor.
- Cash check (real vs predicted cash a tick, last 3): +40 vs -166, -16 vs -162, -11215 vs -170 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): beer 1.5, rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Etallaen: +25/turn
  - ship Flax Wyrm -> Bordetes: +4/turn
  - mansion 1 1.00 -> 0.42: +175/turn
  - net maker 0.00 -> 0.29: +5/turn
  - brewery 1 0.14 -> 0.20: +3/turn
  - flax farm 1 4.64 -> 3.54: -10/turn
  - retting pit 1 0.91 -> 0.79: +9/turn
  - spinnery 1 1.65 -> 1.35: +8/turn
  - weavery 1 0.50 -> 0.38: -22/turn
  - sewing shop 1 0.30 -> 0.23: +30/turn
- Model check over the last 59 turns: predicted -145/turn for the settings we ran, real -525/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 182.66, thread 459.12, cloth 733.11, flax fibres 544.50, garments 2121.00, nets 3354.16, beer 335.74, timber -0.00, prestige 6816.09, cash 100.00
- Orders it would set: bread buy 5 (v2 9); cloth sell 1 (v2 none); donations buy 40 (v2 60); firewood buy 4 (v2 8); flax plants sell 2 (v2 none); furniture buy 2 (v2 3); garments sell 11 (v2 10); grain buy 9 (v2 18); labour buy 64 (v2 62); meat buy 0 (v2 None)
- Ship linen snake: Grandgues -> Etallaen (+14/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Bordetes (+6/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~2265 coin: +1/turn, payback 3681 turns, doesn't pay yet (materials thin at home: limestone)

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
- R1: candles slot dry: 0.0 held, 1.5 a turn (luxury slot (+3 prestige)); our buy 2 @ 94, home ask 92.5; our bid is already at/over the ask (sellers too thin)
- R1: garments slot dry: 0.0 held, 2.1 a turn (clothing slot (+1.2 prestige)); our buy none, home ask 32.0; 5% of cash does not buy one at 32.6
- R1: meat slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask 2.3; 5% of cash does not buy one at 2.34
- R6 data sanity: cash read 0 while the storehouse holds goods: business read broken?
