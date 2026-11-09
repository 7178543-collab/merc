# v2 shadow report

Turn 13900, 2026-11-09 13:04. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,220, prestige 3,503 (383 free, -1.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 10 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 33 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 30 | 30 | 530 | 5 | 0 | buy 30, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **labour**: buying 30, short of ~35 needed -> v2: buy 35

## Notes

- labour: projection runs 100 over real use lately; planning 535, not 632

## Prestige spending, cheapest coin per prestige first

501 turns left: prestige gained now converts 91.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.2 | 49.2 | running |
| hold banquet 4 (pies) | mansion | 18 | 55.2 | 55.2 | thin at home: ham, stockfish, cheese |
| jousting 3 | arena | 230 | 55.2 | 55.4 | needs a arena (build cost 26,744); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 57.1 | 57.1 | thin at home: ham, stockfish, premium cheese |
| hold banquet 4 | mansion | 17.5 | 57.3 | 57.3 | thin at home: ham, stockfish, cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 58.7 | 58.7 | thin at home: cured fish |
| jousting 2 | arena | 210 | 60.4 | 60.7 | needs a arena (build cost 26,744); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 61.7 | 61.7 | thin at home: cured fish, cheese |
| hold banquet 2 (fish) | mansion | 6.8 | 62.2 | 62.2 | thin at home: cured fish, cheese |
| hold banquet 3 (pies) | mansion | 8 | 62.5 | 62.5 | thin at home: cheese |
| hold banquet 1 (meat) | mansion | 4.2 | 64.2 | 64.2 |  |
| hold banquet 3 (meat) | mansion | 7.6 | 65.2 | 65.2 | thin at home: cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.20 | 20 | 134102075 | 0.32 | - | furniture 19 | -267 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Orlesailles +92, Bordetes +34, Clarfranche +30, Bedenis +27, Essenbrucke +26
- Orlesailles would trade: pasties buy 14 @ 10.8; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~105 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.90 (94/turn) | firewood 36 (2.03->6.22), bread 154 (2.33->2.98), timber 24 (7.46->9.59), tackles 1 (200.55->210.9) | flour 4 (22.89->25.27), thread 19 (5->5.2), candles 1 (81.9->82), salt 5 (5.46->5.56) | +242 |
| Rouhomme | 368 | 0.10 | 1.00 (105/turn) | bread 90 (2.33->3.91), tapestries 1 (624.75->650.75), firewood 22 (2.03->5.84), grain 1 (2.64->4.03) | thread 26 (4.87->5.2), tools 10 (4.51->5.08), cheese 2 (6.51->7.5), candles 0 (79.8->82) | +181 |
| Etallaen | 774 | 0.22 | 0.50 (52/turn) | tapestries 2 (624.75->665), clay 4 (4.91->19), nets 6 (38.4->39.14), grain 2 (2.64->3.4) | cheese 5 (6.46->7.5), flax fibres 6 (4.94->6), thread 15 (4.73->5.2), candles 1 (79.8->82) | +120 |
| Hanbrücken | 531 | 0.15 | 0.60 (63/turn) | timber 26 (7.46->12.92), nets 4 (38.4->41.42), tallow 1 (22.68->26.79), hides 1 (11.03->11.88) | rope 1 (72.45->78.38), salt 6 (4.6->5.56), cloth 7 (9.35->10), cheese 2 (6.46->7.5) | +116 |
| Brunnham | 1281 | 0.49 | 0.30 (32/turn) | tapestries 1 (624.75->684), nets 6 (38.4->42.94), lead ore 5 (12.18->15.96), hides 1 (11.03->13.96) | cookware 7 (21.63->24.13), salt 6 (3.68->5.56), candles 1 (79.8->82), garments 2 (25.2->26.2) | +115 |

**Best:** Grandgues at about +242 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 16 @ min 3.26 | goal planner: sells 16 at 3.26 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.6) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 35) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 37.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 80.5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 0 = 0.4 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 25.0k (cash + stock at home prices); +187/turn over 6 turns, +169/turn over 24 turns.
- Limits: cash flow >= -259/turn, prestige >= -0.35/turn (values are after 200 tax a turn).
- Today's settings: value +79/turn, cash +63/turn, prestige -1.92/turn - breaks the prestige floor.
- Plan: value +3/turn, cash +94/turn, prestige -0.35/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -17 vs +35, -269 vs +50, -527 vs +58 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Gosschweig: +6/turn
  - ship Flax Wyrm -> Essenbrucke: +3/turn
  - net maker 0.00 -> 0.29: +8/turn
  - brewery 1 0.14 -> 0.20: -6/turn
  - ropewalk 1 0.25 -> 0.00: -9/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.19: +17/turn
  - weavery 1 0.50 -> 0.61: -10/turn
  - sewing shop 1 0.30 -> 0.36: +12/turn
  - spinnery 1 1.65 -> 1.05: -20/turn
  - retting pit 1 0.91 -> 0.59: +10/turn
- Model check over the last 58 turns: predicted +103/turn for the settings we ran, real +56/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.62, thread 4.07, cloth 6.50, flax fibres 4.82, garments 18.80, nets 29.29, beer 2.85, timber 3.19, prestige 61.97, cash 0.00
- Orders it would set: arms buy 1 (v2 None); beer sell 16 (v2 15); cloth sell 1 (v2 none); firewood buy 4 (v2 8); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 29 (v2 35); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.19, worth +9/turn.
- Ship linen snake: Grandgues -> Gosschweig (+6/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Essenbrucke (+3/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +81/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~2006 coin: +1/turn, payback 2864 turns, doesn't pay yet (materials thin at home: limestone)

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 430 (+141 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.75 |
| ret | 3 | 0.91 | 0.95 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 893/228, cloth 72/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 5.4 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
