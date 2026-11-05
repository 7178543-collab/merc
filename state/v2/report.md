# v2 shadow report

Turn 13801, 2026-11-05 10:18. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,491, prestige 3,303 (183 free, -0.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 15 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.4 |
| grain | 34 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 529 | 0 | 0 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 10.00 x3, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Tuning

- **grain**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 530, not 630

## Prestige spending, cheapest coin per prestige first

600 turns left: prestige gained now converts 95.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.4 | 47.4 | running |
| hold banquet 4 (pies) | mansion | 18 | 55.9 | 55.9 | thin at home: pasties, wine, ham, stockfish, cheese, candles |
| jousting 3 | arena | 230 | 55.8 | 56.0 | needs a arena (build cost 25,513); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 56.4 | 56.4 | thin at home: pasties, wine, cheese, candles |
| hold sermon 2 (candles) | church | 31 | 52.2 | 56.4 | needs a church (build cost 65,912); thin at home: candles, furniture |
| hold prayer 2 | chapel | 13 | 52.3 | 56.5 | needs a chapel (build cost 29,501); thin at home: furniture |
| hold sermon 2 | church | 24 | 52.5 | 57.9 | needs a church (build cost 65,912); thin at home: furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 58.0 | 58.0 | thin at home: wine, cheese |
| hold banquet 2 (meat) | mansion | 6.8 | 58.1 | 58.1 | thin at home: wine, cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 58.6 | 58.6 |  |
| hold feast 2 | townhouse | 2.6 | 53.9 | 58.6 | needs a townhouse (build cost 7,009); thin at home: wine |
| hold banquet 4 | mansion | 17.5 | 58.7 | 58.7 | thin at home: wine, ham, stockfish, cheese, candles |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 10 | 134102075 | 0.06 | - | pasties 2 | -28 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 14.7 (keep 14); best orders clear only 3 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 16.2 (keep 14); best orders clear only 1 a turn after crew: ship stays at 0
- best towns now: Heilegg +54, Vauxvais +48, Disscester +42, Brunnham +34, Dortdorf +33
- Heilegg would trade: pasties buy 12 @ 13.6; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~98 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.40 (39/turn) | charcoal 19 (2.1->6.27), timber 28 (6.98->9.36), limestone 4 (16.48->21.47), butter 2 (76.12->81.22) | wool 1 (8.93->11.49), slaked lime 5 (15.75->16.34), salt 4 (5.25->5.56), cloth 7 (7.56->7.6) | +156 |
| Bordetes | 831 | 0.23 | 0.60 (59/turn) | cured fish 9 (27.09->33.63), dyed cloth 12 (10.92->12.35), charcoal 19 (2.1->4.56), mouldboards 1 (35.07->43.13) | wool 1 (8.93->11.49), cloth 24 (7.35->7.6), salt 4 (5.08->5.56), garments 2 (20.16->20.4) | +104 |
| Hanstein | 380 | 0.10 | 0.50 (49/turn) | timber 14 (6.98->9.69), charcoal 19 (2.1->3.53), yarn 9 (4.83->5.94), butter 2 (76.12->78.85) | grain 81 (2.35->2.77), ham 2 (75.08->76.95), wool 1 (9.13->11.49), cured meat 4 (22.05->22.61) | +84 |
| Unterhufe | 595 | 0.15 | 0.10 (10/turn) | dyed cloth 12 (10.92->14.54), nets 6 (34.8->37.05), premium ham 1 (258.3->267.9), garments 10 (18.14->19) | salt 4 (4.98->5.56), wool 1 (9.4->11.49), yarn 5 (3.72->4.18), resin 1 (1.44->2.13) | +78 |
| Heilegg | 826 | 0.22 | 0.40 (39/turn) | casks 1 (5.35->9.17), nets 6 (34.8->35.72) | cured meat 17 (20.27->22.61), thread 60 (4.33->4.88), slaked lime 5 (14.18->16.34), cheese 4 (4.91->5.98) | +75 |

**Best:** Grandgues at about +156 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 16 @ min 3.06 | goal planner: sells 16 at 3.06 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 73.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 1 @ min 1.25 | goal planner: sells 1 a turn at 1.25, keeps 219 (no one offered it) |
| furniture | 2 @ 14.4, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.4 | goal planner: sells 11 at 19.4 (v2 had 10 at 20.0) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 30) |
| light armour | 1 @ 91, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 19.8k (cash + stock at home prices); +103/turn over 6 turns, +4/turn over 24 turns.
- Limits: cash flow >= -229/turn, prestige >= +4.87/turn (values are after 200 tax a turn).
- Today's settings: value +102/turn, cash +111/turn, prestige -0.92/turn - breaks the prestige floor.
- Plan: value -134/turn, cash -125/turn, prestige +3.28/turn - could not meet the prestige floor.
- Cash check (real vs predicted cash a tick, last 3): +148 vs +115, +123 vs +113, +71 vs +114.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Dedlowe: +6/turn
  - ship Flax Wyrm -> Bedenis: +2/turn
  - net maker 0.00 -> 0.29: +4/turn
  - flax farm 1 4.64 -> 4.42: +1/turn
  - sewing shop 1 0.30 -> 0.36: -3/turn
  - weavery 1 0.50 -> 0.61: +6/turn
  - brewery 1 0.14 -> 0.27: -21/turn
  - mansion 1 0.00 -> 1.00: -224/turn
- Model check over the last 60 turns: predicted +97/turn for the settings we ran, real +37/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.58, thread 3.97, cloth 6.34, flax fibres 4.70, garments 18.34, nets 28.63, beer 2.94, timber 2.99, prestige 10000.00, cash 0.00
- Orders it would set: beer sell 16 (v2 15); candles buy 2 (v2 None); firewood buy 4 (v2 5); flax plants sell 1 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 29 (v2 30); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Dedlowe (+6/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Bedenis (+2/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +79/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 481 (+192 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 5.92 |
| ret | 3 | 0.91 | 1.18 |
| spin | 4 | 1.65 | 2.09 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 339/228, cloth 73/128

## Self-diagnosis

Nothing found this run.
