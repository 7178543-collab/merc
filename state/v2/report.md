# v2 shadow report

Turn 13777, 2026-11-04 10:08. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 6,885, prestige 3,224 (104 free, -0.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 14 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.4 |
| grain | 33 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 30 | 29 | 529 | 1 | 0 | buy 30, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **labour**: buying 30, short of ~130 needed -> v2: buy 130

## Prestige spending, cheapest coin per prestige first

624 turns left: prestige gained now converts 95.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.0 | 48.0 | running |
| hold banquet 4 (pies) | mansion | 18 | 50.2 | 50.2 | thin at home: hop beer, stockfish, pies |
| hold banquet 4 | mansion | 17.5 | 52.7 | 52.7 | thin at home: hop beer, ham, stockfish |
| jousting 3 | arena | 230 | 52.9 | 53.1 | needs a arena (build cost 24,958); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 53.5 | 53.5 |  |
| hold banquet 2 (pies) | mansion | 7 | 53.7 | 53.7 | thin at home: pies |
| hold banquet 4 (premium) | mansion | 20 | 53.8 | 53.8 | thin at home: hop beer, stockfish |
| hold banquet 2 (fish) | mansion | 6.8 | 53.9 | 53.9 |  |
| hold banquet 3 (pies) | mansion | 8 | 55.3 | 55.3 | thin at home: hop beer, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 56.7 | 56.7 | thin at home: hop beer |
| jousting 2 | arena | 210 | 58.0 | 58.2 | needs a arena (build cost 24,958); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| jousting 1 | arena | 170 | 58.2 | 58.5 | needs a arena (build cost 24,958); thin at home: protection, light armour, arms; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 10 | 134102075 | 0.136 | - | furniture 7, pasties 2 | -119 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: furniture 1 @ 14.6 (keep 145); stock: pasties 1 @ 13.7 (keep 14); best orders clear only 7 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 13.9 (keep 14); best orders clear only -5 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~99 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.50 (50/turn) | bread 153 (2.18->2.62), timber 25 (6.98->9.36), ham 1 (70.35->76.47), logs 1 (3.8->8.12) | bricks 6 (6.46->9.26), mouldboards 1 (31.92->38), dyed cloth 4 (11.97->13.3), cloth 9 (7.51->7.95) | +138 |
| Bordees | 1112 | 0.38 | 0.20 (20/turn) | grindstones 1 (224.7->248.9), belts 1 (30.66->31.73), cloth 1 (6.21->6.6), premium cheese 1 (27.09->27.74) | tapestries 1 (598.5->665), dyed cloth 4 (10.4->13.3), garments 2 (20.37->23.4), flax fibres 9 (4.94->5.9) | +96 |
| Fontaux | 411 | 0.11 | 0.90 (89/turn) | wine 23 (6.09->7.74), bread 144 (2.18->2.66), timber 16 (6.98->9.59), firewood 1 (1.72->6.74) | premium ham 1 (228.9->241.3), garments 2 (21.84->23.4), belts 1 (22.26->24.13), dyed cloth 2 (12.29->13.3) | +90 |
| Heilegg | 826 | 0.23 | 1.00 (99/turn) | garments 7 (18.33->22.42), grindstones 0 (224.7->258.4), cured fish 10 (22.68->24.13), wine 12 (6.09->6.84) | cloth 18 (7.14->7.95), dyed cloth 3 (10.82->13.3) | +90 |
| Blanans | 297 | 0.08 | 0.50 (50/turn) | timber 25 (6.98->8.98), thread 7 (4.52->6.37), honey 3 (8.77->12.16), nets 3 (37.2->38.76) | cloth 24 (7.3->7.95), dyed cloth 4 (10.4->13.3), garments 2 (20.37->23.4), bricks 6 (7.25->9.26) | +84 |

**Best:** Grandgues at about +138 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 16 @ min 3.06 | goal planner: sells 16 at 3.06 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 16 = 3.9 turns |
| cloth |  | 1 @ min 7.1 | goal planner: sells 1 a turn at 7.1, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 19.4 | goal planner: sells 11 at 19.4 (v2 had 10 at 22.8) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 130) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 36.2) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 79.0) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.3/turn (ropewalk 1), makes 0.0, holds 1 = 2.5 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 19.7k (cash + stock at home prices); -121/turn over 6 turns, +90/turn over 24 turns.
- Limits: cash flow >= -120/turn, prestige >= +8.15/turn (values are after 200 tax a turn).
- Today's settings: value +106/turn, cash +100/turn, prestige -0.93/turn - breaks the prestige floor.
- Plan: value -121/turn, cash -111/turn, prestige +3.27/turn - could not meet the prestige floor.
- Cash check (real vs predicted cash a tick, last 3): +13 vs +96, -121 vs +99, -9 vs +106 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Donaunieder: +1/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +8/turn
  - ropewalk 1 0.25 -> 0.20: +6/turn
  - flax farm 1 4.64 -> 4.26: +0/turn
  - retting pit 1 0.91 -> 0.85: -1/turn
  - spinnery 1 1.65 -> 1.50: +3/turn
  - sewing shop 1 0.30 -> 0.36: -5/turn
  - weavery 1 0.50 -> 0.61: +7/turn
  - brewery 1 0.14 -> 0.27: -20/turn
- Model check over the last 59 turns: predicted +84/turn for the settings we ran, real +85/turn.
- Worth of one more unit per turn: labour 1.60, thread 4.06, cloth 6.46, flax fibres 4.89, garments 18.66, nets 29.20, beer 2.87, timber 2.99, prestige 10000.00, cash 0.00
- Orders it would set: beer sell 16 (v2 15); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 5); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 29 (v2 130); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Donaunieder (+1/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +80/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 477 (+188 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 5.84 |
| ret | 3 | 0.91 | 1.17 |
| spin | 4 | 1.65 | 2.06 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 357/228, cloth 78/128

## Self-diagnosis

Nothing found this run.
