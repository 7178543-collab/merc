# v2 shadow report

Turn 14213, 2026-11-22 14:57. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,606, prestige 3,682 (562 free, +1.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 59 | 0 | 19 | 0 | 0 | min_holding 58, sell 10, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 6 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 3 | 3 | 3 | 0 | 0 | stop 42, buy 3, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 20 | 9 | 9 | 0 | 0 | stop 36, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 553 | 0 | 11 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**0 risks, 0 waste, 4 tuning** where v2 would act differently from v1.

## Tuning

- **cured meat**: home ask 35.20 is above our ceiling 29.00 and last turn bought 7 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **fish**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 57.8 coin per prestige at mansion, vs 75.2 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch

## Notes

- labour: projection runs 100 over real use lately; planning 564, not 664

## Prestige spending, cheapest coin per prestige first

188 turns left: prestige gained now converts 61.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 49.2 | 50.1 | needs a arena (build cost 28,432); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 53.1 | 53.1 | running |
| jousting 2 | arena | 210 | 53.9 | 54.9 | needs a arena (build cost 28,432); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 57.8 | 57.8 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 64.2 | 64.2 | thin at home: cheese |
| hold banquet 4 (pies) | mansion | 18 | 64.4 | 64.4 | thin at home: stockfish, cheese, pies |
| hold banquet 2 (pies) | mansion | 7 | 64.7 | 64.7 | thin at home: cheese, pies |
| hold banquet 5 | mansion | 22 | 64.7 | 64.7 | thin at home: pies, stockfish, cheese, sculptures |
| hold banquet 4 (premium) | mansion | 20 | 66.0 | 66.0 | thin at home: stockfish, premium cheese |
| hold mass 2 (premium) | cathedral | 360 | 54.4 | 67.1 | needs a cathedral (build cost 311,160); thin at home: furniture, jewellery, glassware, windows, premium garments |
| hold banquet 4 | mansion | 17.5 | 68.7 | 68.7 | thin at home: stockfish, cheese |
| maintain 2 | park | 2 | 70.5 | 70.5 | thin at home: sculptures |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 14.4 (keep 14); best orders clear only -2 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 16.0 (keep 14); best orders clear only 7 a turn after crew: ship stays at 0
- best towns now: Pontmont +39, Friedwerp +34, Gotthafen +33, Birkeningen +31, Hanstein +29
- Pontmont would trade: cured meat buy 6 @ 28.4, pasties buy 2 @ 14.2; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~114 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 1.00 (114/turn) | bread 199 (2.62->4.35), firewood 34 (2.07->11.78), beer 66 (4.07->5.65), timber 25 (9.03->11.88) | bricks 5 (8.66->10.64), flax fibres 3 (7.98->9.45), flax plants 11 (2.14->2.58), cured meat 4 (34.44->35.2) | +844 |
| Rouhomme | 368 | 0.11 | 0.90 (102/turn) | bread 259 (2.62->3.72), flour 8 (19.11->26.03), rope 1 (88->95), seeds 8 (2.96->3.46) | bricks 24 (4.56->10.64), tools 18 (4.73->5.65), cloth 10 (10.71->11.5), dyed cloth 8 (14.7->15.39) | +376 |
| Bordetes | 831 | 0.26 | 1.00 (114/turn) | beer 37 (4.07->7.6), bread 112 (2.62->3.8), cured fish 1 (24.57->28.5), wine 5 (6.62->7.55) | cloth 6 (10.5->11.5), cured meat 2 (34.02->35.2), dyed cloth 4 (14.7->15.39), flax fibres 0 (8.51->9.45) | +181 |
| Heilegg | 826 | 0.26 | 0.30 (34/turn) | flour 10 (19.11->26.79), nets 4 (37.4->45.03), cured fish 9 (24.57->25.65), lead ore 2 (7.88->10.54) | cloth 24 (10.5->11.5), cured meat 6 (32.13->35.2), cookware 5 (21->23.75), thread 30 (6.25->6.85) | +175 |
| Hofkirchen | 991 | 0.36 | 0.50 (57/turn) | nets 6 (37.4->44.27), ploughs 5 (81.9->90.25), resin 2 (2.07->4.27), yarn 17 (6.3->6.84) | lathes 2 (189->212.8), cured meat 5 (30.45->35.2), jewellery 2 (73.5->81.22), thread 34 (6.3->6.85) | +172 |

**Best:** Grandgues at about +844 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 36.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 6 = 1.0 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 3 @ 2.5, stop - |  | goal planner: buys 3 for today's rates (v2 had 3) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 25.8) |
| grain | 9 @ 3.7, stop 36 |  | goal planner: buys 9 a turn for today's rates, keeps up to 36 (v2 had 9) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 64) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 36.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 85.5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 33.1k (cash + stock at home prices); +364/turn over 6 turns, +129/turn over 24 turns.
- Limits: cash flow >= -442/turn, prestige >= -1.09/turn (values are after 200 tax a turn).
- Today's settings: value -193/turn, cash -191/turn, prestige +1.10/turn.
- Plan: value -8/turn, cash -4/turn, prestige -1.09/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +224 vs -179, -44 vs -176, -100 vs -186.
- Route sales counted at most (what the ships really sold, a turn): beer 1.2.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Pontmont: +27/turn
  - ship Flax Wyrm -> Blanans: +6/turn
  - mansion 1 1.00 -> 0.48: +168/turn
  - net maker 0.00 -> 0.29: +4/turn
  - ropewalk 1 0.25 -> 0.31: +2/turn
  - flax farm 1 4.64 -> 4.98: -1/turn
  - retting pit 1 0.91 -> 0.99: +6/turn
  - weavery 1 0.50 -> 0.58: -6/turn
  - sewing shop 1 0.30 -> 0.36: +10/turn
- Model check over the last 59 turns: predicted -140/turn for the settings we ran, real +66/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.77, thread 4.45, cloth 7.11, flax fibres 5.28, garments 20.55, nets 32.21, beer 3.19, timber 4.25, prestige 75.91, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 4 (v2 8); garments sell 11 (v2 10); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Pontmont (+11/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Blanans (+6/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +88/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1972 coin: +5/turn, payback 365 turns, doesn't pay yet (materials thin at home: limestone)

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 430 (+141 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.75 |
| ret | 3 | 0.91 | 0.95 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 86/77, thread 1050/228, cloth 72/128

## Self-diagnosis

- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
