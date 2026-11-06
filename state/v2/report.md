# v2 shadow report

Turn 13824, 2026-11-06 09:21. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,670, prestige 3,283 (163 free, -0.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 14 | 3 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 33 | 11 | 9 | 0 | 0 | stop 33, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 518 | 0 | 11 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.80 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.80 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 518, not 618

## Prestige spending, cheapest coin per prestige first

577 turns left: prestige gained now converts 94.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.5 | 49.5 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 54.2 | 54.2 |  |
| jousting 3 | arena | 230 | 54.1 | 54.3 | needs a arena (build cost 25,473); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 54.4 | 54.4 | thin at home: ham, stockfish, candles |
| hold banquet 4 | mansion | 17.5 | 57.7 | 57.7 | thin at home: ham, stockfish, candles |
| hold banquet 1 (meat) | mansion | 4.2 | 58.2 | 58.2 |  |
| hold banquet 4 (premium) | mansion | 20 | 58.5 | 58.5 | thin at home: ham, stockfish, candles, premium cheese |
| jousting 2 | arena | 210 | 59.3 | 59.5 | needs a arena (build cost 25,473); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 60.2 | 60.2 | thin at home: candles |
| hold banquet 2 (fish) | mansion | 6.8 | 60.6 | 60.6 |  |
| hold banquet 2 (pies) | mansion | 7 | 61.0 | 61.0 | thin at home: candles |
| hold sermon 2 (candles) | church | 31 | 57.5 | 61.8 | needs a church (build cost 64,872); thin at home: candles, furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: pasties buy 11 @ 15.6; crew 0.1; est +26 a turn; stock: pasties 11 @ 15.6 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 15.0 (keep 14); best orders clear only 5 a turn after crew: ship stays at 0
- best towns now: Herschweig +56, Orlesailles +52, Donaunieder +42, Angefont +40, Fulkirch +35
- Herschweig would trade: pasties buy 10 @ 12.3; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~103 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hanstein | 380 | 0.10 | 0.50 (52/turn) | tapestries 1 (614.25->684), timber 25 (8.14->11.59), limestone 1 (17.22->31.92), nets 5 (34.6->35.34) | cheese 5 (6.2->9.17), flax plants 31 (1.5->2.08), seeds 12 (1.78->2.32), flax fibres 13 (5.41->5.85) | +162 |
| Donaunieder | 985 | 0.32 | 0.10 (10/turn) | tapestries 1 (614.25->622.25), ham 1 (79.8->85.5), gears 1 (60.38->61.75) | candles 8 (59.33->69.83), cookware 6 (20.58->24.13), cheese 5 (6.2->9.17), cloth 9 (7.35->8.45) | +132 |
| Hofkirchen | 991 | 0.33 | 0.60 (62/turn) | tapestries 1 (614.25->669.75), yarn 8 (4.43->5.7), nets 6 (34.6->36.29), mouldboards 1 (34.65->38.95) | cloth 24 (7.14->8.45), cheese 5 (5.93->9.17), garments 20 (21.84->22.61), flax plants 64 (1.35->2.08) | +131 |
| Amsdermund | 1111 | 0.39 | 0.50 (52/turn) | tapestries 1 (614.25->665), limestone 3 (17.22->41.04), ham 1 (79.8->82.65), honey 3 (7.98->8.84) | garments 20 (21->22.61), cheese 5 (6.14->9.17), cloth 16 (7.35->8.45), nails 2 (5.83->6.32) | +124 |
| Fontaux | 411 | 0.11 | 0.90 (93/turn) | tapestries 1 (614.25->660.25), garments 10 (23.8->28.31), timber 25 (8.14->10.73), bread 128 (2.54->2.93) | flax fibres 6 (4.94->5.85), flax plants 4 (1.72->2.08), tallow 1 (22.47->23.37) | +123 |

**Best:** Hanstein at about +162 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.0, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 4.0 turns |
| beer |  | 16 @ min 3.06 | goal planner: sells 16 at 3.06 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.2) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 18) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 23.6k (cash + stock at home prices); +156/turn over 6 turns, +164/turn over 24 turns.
- Limits: cash flow >= -278/turn, prestige >= +5.70/turn (values are after 200 tax a turn).
- Today's settings: value +93/turn, cash +87/turn, prestige -0.82/turn - breaks the prestige floor.
- Plan: value -131/turn, cash -44/turn, prestige +3.38/turn - could not meet the prestige floor.
- Cash check (real vs predicted cash a tick, last 3): -95 vs +99, -325 vs +96, +132 vs +85 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Donaunieder: +21/turn
  - ship Flax Wyrm -> Calange: +1/turn
  - net maker 0.00 -> 0.29: +7/turn
  - ropewalk 1 0.25 -> 0.00: -18/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.24: +21/turn
  - brewery 1 0.14 -> 0.27: -20/turn
  - spinnery 1 1.65 -> 0.98: -19/turn
  - retting pit 1 0.91 -> 0.56: +2/turn
  - flax farm 1 4.64 -> 2.81: -25/turn
  - mansion 1 0.00 -> 1.00: -173/turn
- Model check over the last 62 turns: predicted +99/turn for the settings we ran, real +67/turn.
- Worth of one more unit per turn: labour 1.66, thread 4.17, cloth 6.67, flax fibres 4.94, garments 19.30, nets 29.96, beer 2.88, timber 3.24, prestige 10000.00, cash 0.00
- Orders it would set: beer sell 16 (v2 15); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 5); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 29 (v2 18); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.24, worth +11/turn.
- Ship linen snake: Grandgues -> Donaunieder (+21/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Calange (+1/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 461 (+172 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 5.48 |
| ret | 3 | 0.91 | 1.10 |
| spin | 4 | 1.65 | 1.93 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 435/228, cloth 73/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 5.85 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
