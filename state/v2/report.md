# v2 shadow report

Turn 13844, 2026-11-07 05:26. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,751, prestige 3,382 (262 free, -1.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 12 | 9 | 4 | 0 | 0 | min_holding 60, sell 11, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 34 | 0 | 0 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 506 | 0 | 23 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), but the home ask 3.54 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.54 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 10.70 x25, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 23 labour expired last turn (~38 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Notes

- labour: projection runs 100 over real use lately; planning 507, not 607

## Prestige spending, cheapest coin per prestige first

557 turns left: prestige gained now converts 93.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.5 | 49.5 | running |
| jousting 3 | arena | 230 | 53.5 | 53.7 | needs a arena (build cost 26,013); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 53.8 | 53.8 |  |
| hold banquet 4 (pies) | mansion | 18 | 53.8 | 53.8 | thin at home: wine, ham, stockfish, cheese |
| hold banquet 2 (fish) | mansion | 6.8 | 54.7 | 54.7 | thin at home: wine, cheese |
| hold banquet 2 (pies) | mansion | 7 | 55.9 | 55.9 | thin at home: pasties, wine, cheese |
| hold banquet 4 | mansion | 17.5 | 56.9 | 56.9 | thin at home: wine, ham, stockfish, cheese |
| hold banquet 3 (pies) | mansion | 8 | 57.2 | 57.2 | thin at home: pasties, cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 57.5 | 57.5 | thin at home: cheese |
| hold banquet 4 (premium) | mansion | 20 | 58.1 | 58.1 | thin at home: wine, ham, stockfish |
| hold banquet 2 (meat) | mansion | 6.8 | 58.4 | 58.4 | thin at home: wine, cheese |
| jousting 2 | arena | 210 | 58.5 | 58.8 | needs a arena (build cost 26,013); thin at home: swords, protection, coats, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 15.3 (keep 14); best orders clear only 4 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 15.5 (keep 14); best orders clear only 3 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~103 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.33 | 0.90 (93/turn) | beer 116 (3.46->5.32), garments 10 (18.79->21.47), lead bars 9 (19.84->20.71), wine 4 (6.14->7.36) | flax fibres 27 (5.17->5.95), candles 1 (79.8->83.5), nails 5 (5.57->6.46), cured meat 9 (21->21.85) | +195 |
| Etallaen | 774 | 0.21 | 0.50 (52/turn) | beer 91 (3.46->4.54), garments 10 (18.79->22.04), cured meat 4 (24.57->28.5), cured fish 6 (24.15->26.22) | silver bars 1 (296.1->313.5), candles 1 (78.75->83.5), thread 10 (4.73->5.35), flax fibres 4 (4.96->5.95) | +159 |
| Grandgues | 152 | 0.04 | 0.30 (31/turn) | beer 116 (3.46->4.14), garments 10 (18.79->22.23), timber 29 (7.19->8.64), nets 4 (32.2->34.96) | candles 1 (76.65->83.5), thread 23 (5.12->5.35), yarn 3 (4.81->5.13), cheese 5 (6.14->6.27) | +157 |
| Fontaux | 411 | 0.11 | 1.00 (103/turn) | timber 18 (7.19->11.59), thread 36 (4.66->5.65), garments 7 (18.79->22.8), beer 38 (3.46->3.97) | - | +126 |
| Hanstein | 380 | 0.10 | 0.30 (31/turn) | garments 10 (18.79->22.42), timber 14 (7.19->10.36), wool 5 (9.66->10.83), nets 3 (32.2->33.06) | acid 2 (109.2->119.7), thread 35 (5->5.35), bricks 4 (5.88->8.98), seeds 12 (1.82->2.32) | +107 |

**Best:** Hofkirchen at about +195 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 30.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 8 @ min 3.06 | goal planner: sells 8 a turn at 3.06, keeps 60 (no one offered it) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 12.8, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.8) |
| grain | 8 @ 3.7, stop 29 |  | goal planner: buys 8 a turn for today's rates, keeps up to 29 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 7) |
| light armour | 1 @ 95, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 22.1k (cash + stock at home prices); +124/turn over 6 turns, -44/turn over 24 turns.
- Limits: cash flow >= -281/turn, prestige >= +1.59/turn (values are after 200 tax a turn).
- Today's settings: value +73/turn, cash +60/turn, prestige -1.52/turn - breaks the prestige floor.
- Plan: value -77/turn, cash -62/turn, prestige +1.59/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +123 vs +29, +52 vs +53, +100 vs +46.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.28: +8/turn
  - ropewalk 1 0.25 -> 0.19: +6/turn
  - flax farm 1 4.64 -> 4.22: -1/turn
  - retting pit 1 0.91 -> 0.84: -1/turn
  - spinnery 1 1.65 -> 1.49: +4/turn
  - sewing shop 1 0.30 -> 0.36: -8/turn
  - weavery 1 0.50 -> 0.61: +9/turn
  - mansion 1 0.00 -> 0.74: -168/turn
- Model check over the last 61 turns: predicted +97/turn for the settings we ran, real +73/turn.
- Worth of one more unit per turn: labour 1.65, thread 4.19, cloth 6.66, flax fibres 5.03, garments 19.24, nets 29.80, beer 3.07, timber 3.08, prestige 58.15, cash 0.00
- Orders it would set: beer sell 8 (v2 none); cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 8 (v2 0); labour buy 29 (v2 7); light armour buy 1 (v2 None)
- Ship linen snake: stays on Grandgues (worth +10/turn).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +82/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 435 (+146 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.89 |
| ret | 3 | 0.91 | 0.98 |
| spin | 4 | 1.65 | 1.72 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 560/228, cloth 72/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 3.54; ask over the cap 2.1 (60 coin per prestige)
- R5: flax fibres buy not filling: bid 5.05 under the home ask 5.95 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
