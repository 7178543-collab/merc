# v2 shadow report

Turn 13781, 2026-11-04 14:31. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 7,453, prestige 3,222 (102 free, -0.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 15 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.4 |
| grain | 33 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 525 | 0 | 4 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **labour**: buying 29, short of ~125 needed -> v2: buy 125

## Prestige spending, cheapest coin per prestige first

620 turns left: prestige gained now converts 95.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.6 | 48.6 | running |
| hold banquet 4 (pies) | mansion | 18 | 51.6 | 51.6 | thin at home: pasties, hop beer, stockfish, pies |
| hold banquet 2 (fish) | mansion | 6.8 | 52.8 | 52.8 |  |
| jousting 3 | arena | 230 | 53.0 | 53.2 | needs a arena (build cost 25,000); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 53.7 | 53.7 |  |
| hold banquet 4 | mansion | 17.5 | 54.1 | 54.1 | thin at home: hop beer, ham, stockfish |
| hold banquet 2 (pies) | mansion | 7 | 54.4 | 54.4 | thin at home: pasties, pies |
| hold banquet 4 (premium) | mansion | 20 | 54.8 | 54.8 | thin at home: hop beer, stockfish |
| hold banquet 3 (fish) | mansion | 7.6 | 56.0 | 56.0 | thin at home: hop beer |
| hold banquet 2 (meat) | mansion | 6.8 | 56.3 | 56.3 |  |
| hold banquet 3 (pies) | mansion | 8 | 56.5 | 56.5 | thin at home: pasties, hop beer, pies |
| jousting 2 | arena | 210 | 58.0 | 58.2 | needs a arena (build cost 25,000); thin at home: swords, protection, coats, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 12.6 (keep 14); best orders clear only 9 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 15.5 (keep 14); best orders clear only 0 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~99 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.50 (50/turn) | bread 153 (2.16->2.66), timber 26 (7.14->9.07), limestone 3 (16.8->21.47), thread 13 (4.48->4.94) | bricks 5 (6.46->9.4), yarn 4 (4.77->6.03), casks 1 (5.83->6.65), flax fibres 3 (5.57->5.85) | +138 |
| Fontaux | 411 | 0.11 | 0.90 (89/turn) | garments 10 (22.2->25.46), wine 16 (5.88->7.74), timber 16 (7.14->10.36), bread 148 (2.16->2.58) | yarn 9 (4.66->6.03), premium axes 1 (33.18->40.28), leather 1 (26.04->28.12), blades 1 (11.34->12.25) | +120 |
| Kleinburgh | 1440 | 0.55 | 0.30 (30/turn) | premium ham 1 (252->309.7), dyed cloth 5 (10.82->12.92), tools 20 (5.35->6.08), nets 2 (34.4->35.91) | cookware 7 (20.06->21.85), yarn 4 (3.82->6.03), spinning wheels 1 (210->216.6), jewellery 2 (75.08->76) | +91 |
| Gottweiler | 1135 | 0.39 | 0.10 (10/turn) | tapestries 1 (798->864.5), nets 1 (34.4->36.1), salt 2 (4.89->5.94), wine 3 (5.88->6.46) | ploughs 1 (63.53->76), garments 2 (20.27->22.4), yarn 2 (4.66->6.03), casks 1 (5.3->6.65) | +84 |
| Rouhomme | 368 | 0.10 | 0.60 (59/turn) | bread 153 (2.16->2.72), cheese 13 (5.99->6.22), harnesses 2 (41.37->42.75), honey 2 (9.24->10.26) | flax fibres 13 (4.94->5.85), yarn 5 (4.56->6.03), bricks 4 (6.46->9.4), garments 2 (21.42->22.4) | +71 |

**Best:** Grandgues at about +138 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 29.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 16 @ min 3.06 | goal planner: sells 16 at 3.06 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 77.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 2 @ min 7.05 | goal planner: sells 2 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 1 @ min 1.28 | goal planner: sells 1 a turn at 1.28, keeps 219 (no one offered it) |
| furniture | 2 @ 15.7, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.4 | goal planner: sells 11 at 19.4 (v2 had 10 at 21.6) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 125) |
| light armour | 1 @ 90.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 79.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 20.4k (cash + stock at home prices); +136/turn over 6 turns, +86/turn over 24 turns.
- Limits: cash flow >= -144/turn, prestige >= +8.24/turn (values are after 200 tax a turn).
- Today's settings: value +85/turn, cash +77/turn, prestige -0.51/turn - breaks the prestige floor.
- Plan: value -133/turn, cash -68/turn, prestige +3.69/turn - could not meet the prestige floor.
- Cash check (real vs predicted cash a tick, last 3): -9 vs +106, +71 vs +82, +202 vs +74.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Clairlond: +1/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +8/turn
  - ropewalk 1 0.25 -> 0.18: +7/turn
  - sewing shop 1 0.30 -> 0.36: -2/turn
  - weavery 1 0.50 -> 0.61: +4/turn
  - spinnery 1 1.65 -> 1.20: -15/turn
  - retting pit 1 0.91 -> 0.68: +5/turn
  - flax farm 1 4.64 -> 3.44: +8/turn
  - brewery 1 0.14 -> 0.27: -16/turn
- Model check over the last 59 turns: predicted +104/turn for the settings we ran, real +98/turn.
- Worth of one more unit per turn: labour 1.62, thread 4.07, cloth 6.50, flax fibres 4.82, garments 18.80, nets 29.20, beer 2.85, timber 3.06, prestige 10000.00, cash 0.00
- Orders it would set: beer sell 16 (v2 15); candles buy 2 (v2 None); cloth sell 2 (v2 none); firewood buy 4 (v2 5); flax plants sell 1 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 29 (v2 125); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Clairlond (+1/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +81/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

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

Buffers: flax fibres 27/77, thread 357/228, cloth 75/128

## Self-diagnosis

Nothing found this run.
