# v2 shadow report

Turn 13779, 2026-11-04 12:20. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 7,180, prestige 3,223 (103 free, -0.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 15 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.4 |
| grain | 33 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 529 | 1 | 0 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **labour**: buying 29, short of ~127 needed -> v2: buy 127

## Prestige spending, cheapest coin per prestige first

622 turns left: prestige gained now converts 95.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.0 | 48.0 | running |
| hold banquet 4 (pies) | mansion | 18 | 51.2 | 51.2 | thin at home: hop beer, ham, stockfish, pies |
| jousting 3 | arena | 230 | 52.8 | 53.0 | needs a arena (build cost 24,768); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 53.5 | 53.5 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 53.7 | 53.7 |  |
| hold banquet 4 | mansion | 17.5 | 53.9 | 53.9 | thin at home: hop beer, ham, stockfish |
| hold banquet 2 (pies) | mansion | 7 | 54.2 | 54.2 | thin at home: pies |
| hold banquet 4 (premium) | mansion | 20 | 54.3 | 54.3 | thin at home: hop beer, ham, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 55.9 | 55.9 | thin at home: hop beer, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 56.6 | 56.6 | thin at home: hop beer |
| hold banquet 2 (meat) | mansion | 6.8 | 57.9 | 57.9 |  |
| jousting 2 | arena | 210 | 57.8 | 58.0 | needs a arena (build cost 24,768); thin at home: swords, protection, coats, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 10 | 134102075 | 0.056 | - | furniture 2, pasties 2 | -52 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 13.3 (keep 14); best orders clear only -4 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 15.4 (keep 14); best orders clear only -6 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~98 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Marmont | 638 | 0.17 | 0.30 (30/turn) | garments 10 (18.3->19.57), premium cheese 2 (27.51->30.78), premium axes 1 (30.87->32.87), cloth 1 (6.2->7.27) | tapestries 2 (609->665), yarn 19 (4.18->6.08), bricks 5 (5.62->9.59), furniture 1 (13.76->15.3) | +164 |
| Grandgues | 152 | 0.04 | 0.40 (39/turn) | bread 153 (2.18->2.62), timber 26 (7.98->9.45), nets 2 (36->39.52), gears 1 (54.08->60.32) | bricks 5 (6.46->9.59), yarn 4 (4.58->6.08), flax fibres 9 (5.1->5.5), casks 1 (5.25->6.6) | +123 |
| Fontaux | 411 | 0.11 | 0.90 (89/turn) | garments 10 (18.3->22.8), wine 16 (5.93->7.74), bread 147 (2.18->2.66), arms 2 (27.93->29.64) | yarn 9 (4.56->6.08), jewellery 1 (71.4->75.52), leather 1 (26.04->28.12), casks 1 (6.09->6.6) | +117 |
| Calange | 218 | 0.06 | 0.10 (10/turn) | cheese 10 (6.56->9.07), tools 14 (5.06->5.65), premium axes 1 (30.87->35.72), garments 10 (18.3->18.71) | thread 15 (2.94->4.6), leather 1 (22.47->28.12), yarn 3 (4.35->6.08), bricks 2 (6.67->9.59) | +90 |
| Rouhomme | 368 | 0.10 | 0.60 (59/turn) | bread 153 (2.18->2.7), paper 3 (23.52->27.74), premium axes 1 (30.87->34.77), garments 10 (18.3->18.71) | yarn 9 (4.81->6.08), flax fibres 13 (4.94->5.5), cookware 6 (22.05->22.8), bricks 4 (7.14->9.59) | +89 |

**Best:** Marmont at about +164 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 27.8, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 4.0 turns |
| beer |  | 16 @ min 3.06 | goal planner: sells 16 at 3.06 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| cloth |  | 2 @ min 7.1 | goal planner: sells 2 a turn at 7.1, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 19.4 | goal planner: sells 11 at 19.4 (v2 had 10 at 21.8) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 127) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 35.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 80.5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.3/turn (ropewalk 1), makes 0.0, holds 0 = 0.5 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 20.1k (cash + stock at home prices); +146/turn over 6 turns, +86/turn over 24 turns.
- Limits: cash flow >= -133/turn, prestige >= +8.19/turn (values are after 200 tax a turn).
- Today's settings: value +93/turn, cash +82/turn, prestige -0.52/turn - breaks the prestige floor.
- Plan: value -125/turn, cash -63/turn, prestige +3.68/turn - could not meet the prestige floor.
- Cash check (real vs predicted cash a tick, last 3): +13 vs +96, -121 vs +99, -9 vs +106 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Calange: +0/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +8/turn
  - ropewalk 1 0.25 -> 0.18: +7/turn
  - sewing shop 1 0.30 -> 0.36: -2/turn
  - weavery 1 0.50 -> 0.61: +5/turn
  - spinnery 1 1.65 -> 1.21: -15/turn
  - retting pit 1 0.91 -> 0.69: +5/turn
  - flax farm 1 4.64 -> 3.45: +10/turn
  - brewery 1 0.14 -> 0.27: -15/turn
- Model check over the last 60 turns: predicted +96/turn for the settings we ran, real +97/turn.
- Worth of one more unit per turn: labour 1.60, thread 4.06, cloth 6.46, flax fibres 4.89, garments 18.66, nets 29.00, beer 2.73, timber 3.17, prestige 10000.00, cash 0.00
- Orders it would set: beer sell 16 (v2 15); candles buy 2 (v2 None); cloth sell 2 (v2 none); firewood buy 4 (v2 5); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 29 (v2 127); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Calange (+1/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +80/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 478 (+189 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 5.85 |
| ret | 3 | 0.91 | 1.17 |
| spin | 4 | 1.65 | 2.07 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 355/228, cloth 77/128

## Self-diagnosis

Nothing found this run.
