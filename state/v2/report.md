# v2 shadow report

Turn 13812, 2026-11-05 21:04. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,478, prestige 3,293 (173 free, -0.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 15 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 33 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 525 | 0 | 4 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**1 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it

## Tuning

- **tar**: home ask 11.80 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 525, not 625

## Prestige spending, cheapest coin per prestige first

589 turns left: prestige gained now converts 94.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.1 | 50.1 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 54.1 | 54.1 |  |
| hold banquet 4 (pies) | mansion | 18 | 54.8 | 54.8 | thin at home: hop beer, wine, ham, stockfish, cheese |
| jousting 3 | arena | 230 | 54.7 | 54.9 | needs a arena (build cost 25,642); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 55.7 | 55.7 | thin at home: wine, cheese |
| hold banquet 2 (pies) | mansion | 7 | 56.0 | 56.0 | thin at home: wine, cheese |
| hold sermon 2 (candles) | church | 31 | 52.6 | 56.8 | needs a church (build cost 65,383); thin at home: candles, furniture |
| hold prayer 2 | chapel | 13 | 52.8 | 57.2 | needs a chapel (build cost 30,274) |
| hold banquet 1 (meat) | mansion | 4.2 | 58.0 | 58.0 |  |
| hold banquet 4 | mansion | 17.5 | 58.0 | 58.0 | thin at home: wine, hop beer, ham, stockfish, cheese |
| hold sermon 2 | church | 24 | 52.7 | 58.1 | needs a church (build cost 65,383); thin at home: furniture |
| hold banquet 2 (meat) | mansion | 6.8 | 58.3 | 58.3 | thin at home: wine, cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: pasties buy 6 @ 14.3; crew 0.1; est +17 a turn; stock: pasties 6 @ 14.3 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 15.9 (keep 14); best orders clear only 2 a turn after crew: ship stays at 0
- best towns now: Bedenis +56, Heilegg +47, Orlesailles +38, Fulkirch +33, Donaunieder +33
- Bedenis would trade: pasties buy 14 @ 14.2; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~103 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hanbrücken | 531 | 0.15 | 0.30 (31/turn) | garments 10 (19.6->24.89), charcoal 18 (2.14->3.84), mouldboards 1 (34.23->35.72) | candles 1 (70.35->81), cloth 24 (7.19->7.65), yarn 6 (2.84->4.12), cheese 4 (5.67->6.22) | +87 |
| Grandgues | 152 | 0.04 | 0.30 (31/turn) | charcoal 18 (2.14->5.13), timber 25 (7.93->9.4), logs 1 (3.93->10.54), limestone 2 (18.59->21.47) | bricks 4 (6.25->7.79), candles 1 (80.33->81), cheese 4 (6.09->6.22), harnesses 1 (44.1->44.27) | +83 |
| Vauxvais | 204 | 0.06 | 0.20 (21/turn) | charcoal 15 (2.14->3.59), beer 15 (3.3->4.35), cured fish 4 (22.68->24.13), limestone 1 (18.59->23.37) | thread 31 (4.73->5.15), bricks 4 (4.85->7.79), candles 1 (77.7->81), lead bars 5 (14.28->14.82) | +68 |
| Unterhufe | 595 | 0.16 | 0.10 (10/turn) | dyed cloth 13 (10.71->15.67), casks 2 (5.41->6.32), mouldboards 1 (34.23->34.58) | thread 13 (4.81->5.15), candles 1 (79.8->81), flax fibres 6 (5.1->5.6), yarn 5 (3.74->4.12) | +66 |
| Pontmont | 341 | 0.09 | 0.10 (10/turn) | garments 10 (19.6->24.32), beer 15 (3.3->3.84), slaked lime 2 (13.97->16.72) | bricks 4 (5.25->7.79), candles 1 (78.75->81), chisels 1 (7.3->7.65), pasties 1 (12.18->12.82) | +61 |

**Best:** Hanbrücken at about +87 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.8, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 4.0 turns |
| beer |  | 16 @ min 3.06 | goal planner: sells 16 at 3.06 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 16 = 3.9 turns |
| cloth |  | 2 @ min 7.05 | goal planner: sells 2 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 20.0) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 25) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 36.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 83.0) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 0 = 2.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 21.4k (cash + stock at home prices); +213/turn over 6 turns, +149/turn over 24 turns.
- Limits: cash flow >= -270/turn, prestige >= +5.28/turn (values are after 200 tax a turn).
- Today's settings: value +98/turn, cash +102/turn, prestige -0.87/turn - breaks the prestige floor.
- Plan: value -131/turn, cash -125/turn, prestige +3.33/turn - could not meet the prestige floor.
- Cash check (real vs predicted cash a tick, last 3): +47 vs +108, -146 vs +105, +55 vs +96 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Dortdorf: +4/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +3/turn
  - retting pit 1 0.91 -> 0.71: -13/turn
  - flax farm 1 4.64 -> 3.59: +9/turn
  - spinnery 1 1.65 -> 1.26: -15/turn
  - brewery 1 0.14 -> 0.27: -1/turn
  - ropewalk 1 0.25 -> 0.00: -13/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.34: +13/turn
  - weavery 1 0.50 -> 0.25: -29/turn
- Model check over the last 62 turns: predicted +97/turn for the settings we ran, real +70/turn.
- Worth of one more unit per turn: labour 1.66, thread 4.17, cloth 6.67, flax fibres 4.94, garments 19.30, nets 30.00, beer 2.87, timber 3.13, prestige 10000.00, cash 0.00
- Orders it would set: beer sell 16 (v2 15); cloth sell 2 (v2 none); firewood buy 4 (v2 5); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 29 (v2 25); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.34, worth +13/turn.
- Ship linen snake: Grandgues -> Dortdorf (+8/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 484 (+195 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 5.99 |
| ret | 3 | 0.91 | 1.20 |
| spin | 4 | 1.65 | 2.11 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 325/228, cloth 73/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 5.6 for 5 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
