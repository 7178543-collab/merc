# v2 shadow report

Turn 13784, 2026-11-04 17:54. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 7,558, prestige 3,320 (200 free, -1.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 14 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.4 |
| grain | 33 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 525 | 0 | 4 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**1 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 104 over real use lately; planning 525, not 625

## Prestige spending, cheapest coin per prestige first

617 turns left: prestige gained now converts 95.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.0 | 48.0 | running |
| hold banquet 4 (pies) | mansion | 18 | 51.0 | 51.0 | thin at home: hop beer, stockfish, pies |
| hold banquet 2 (fish) | mansion | 6.8 | 52.9 | 52.9 |  |
| hold banquet 1 (fish) | mansion | 4.2 | 53.5 | 53.5 |  |
| hold banquet 4 | mansion | 17.5 | 53.6 | 53.6 | thin at home: hop beer, ham, stockfish |
| hold banquet 2 (pies) | mansion | 7 | 53.8 | 53.8 | thin at home: pies |
| jousting 3 | arena | 230 | 54.5 | 54.7 | needs a arena (build cost 25,635); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 55.6 | 55.6 | thin at home: hop beer, stockfish, premium cheese |
| hold banquet 3 (pies) | mansion | 8 | 55.9 | 55.9 | thin at home: hop beer, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 56.2 | 56.2 | thin at home: hop beer |
| hold banquet 2 (meat) | mansion | 6.8 | 56.8 | 56.8 |  |
| hold banquet 1 (meat) | mansion | 4.2 | 58.8 | 58.8 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 14.4 (keep 14); best orders clear only -1 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 15.6 (keep 14); best orders clear only 0 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~99 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.40 (39/turn) | arms 5 (31.08->36.29), bread 152 (2.39->2.66), timber 22 (7.72->9.07), cured fish 7 (22.68->24.7) | bricks 2 (7.19->10.16) | +106 |
| Briclives | 1041 | 0.34 | 0.40 (39/turn) | ham 1 (72.98->80.75), blades 5 (15.02->16.62), wool 2 (8.93->10.07), gears 1 (58.28->59.85) | grindstones 2 (241.5->271.7), garments 18 (20.27->21.85), cookware 7 (20.79->21.85), malt 8 (3.84->4.8) | +86 |
| Heilegg | 826 | 0.22 | 0.20 (20/turn) | wine 18 (5.78->6.93), arms 6 (31.08->33.25), rope 1 (81->86.92), paper 2 (19.64->19.95) | garments 18 (19.43->21.85), premium cheese 4 (28.35->30.97), thread 27 (4.62->4.98), candles 1 (79.28->79.5) | +85 |
| Hanstein | 380 | 0.10 | 0.30 (30/turn) | timber 14 (7.72->10.54), firewood 1 (1.62->4.8), paper 2 (19.64->19.76) | thread 62 (4.16->4.98), flax fibres 26 (4.81->5.3), premium cheese 4 (29.19->30.97), bricks 2 (6.93->10.16) | +84 |
| Fulkirch | 1576 | 0.62 | 0.30 (30/turn) | premium ham 1 (258.3->285), thread 21 (4.58->5.7), nets 6 (34.8->37.62), wine 6 (5.78->6.46) | garments 18 (19.74->21.85), premium cheese 4 (29.4->30.97), candles 1 (78.75->79.5) | +75 |

**Best:** Grandgues at about +106 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 31.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 16 @ min 3.06 | goal planner: sells 16 at 3.06 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 76.0, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had 2) |
| cloth |  | 2 @ min 7.05 | goal planner: sells 2 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 1 @ min 1.27 | goal planner: sells 1 a turn at 1.27, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.4 | goal planner: sells 11 at 19.4 (v2 had 10 at 21.8) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 25) |
| light armour | 1 @ 92, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 79.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 17.7k (cash + stock at home prices); -393/turn over 6 turns, -50/turn over 24 turns.
- Limits: cash flow >= -148/turn, prestige >= +4.17/turn (values are after 200 tax a turn).
- Today's settings: value +83/turn, cash +80/turn, prestige -1.00/turn - breaks the prestige floor.
- Plan: value -140/turn, cash -131/turn, prestige +3.20/turn - could not meet the prestige floor.
- Cash check (real vs predicted cash a tick, last 3): +72 vs +77, -117 vs +72, +150 vs +69.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Vauxvais: +2/turn
  - ship Flax Wyrm -> Unterhufe: +1/turn
  - net maker 0.00 -> 0.29: +8/turn
  - flax farm 1 4.64 -> 4.27: +0/turn
  - spinnery 1 1.65 -> 1.54: -2/turn
  - sewing shop 1 0.30 -> 0.37: -2/turn
  - weavery 1 0.50 -> 0.62: +5/turn
  - brewery 1 0.14 -> 0.27: -17/turn
  - mansion 1 0.00 -> 1.00: -221/turn
- Model check over the last 60 turns: predicted +103/turn for the settings we ran, real +40/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.60, thread 4.02, cloth 6.42, flax fibres 4.76, garments 18.57, nets 28.90, beer 2.75, timber 3.44, prestige 10000.00, cash 0.00
- Orders it would set: beer sell 16 (v2 15); cloth sell 2 (v2 none); firewood buy 4 (v2 5); flax plants sell 1 (v2 none); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 29 (v2 25); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Vauxvais (+2/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Unterhufe (+1/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +80/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 478 (+190 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 5.87 |
| ret | 3 | 0.91 | 1.17 |
| spin | 4 | 1.65 | 2.07 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 352/228, cloth 73/128

## Self-diagnosis

Nothing found this run.
