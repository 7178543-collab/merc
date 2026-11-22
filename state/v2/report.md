# v2 shadow report

Turn 14212, 2026-11-22 13:52. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,706, prestige 3,681 (561 free, -3.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 63 | 0 | 4 | 0 | 0 | min_holding 58, sell 10, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 5 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 3 | 3 | 3 | 0 | 0 | stop 42, buy 3, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 19 | 9 | 9 | 0 | 0 | stop 36, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 530 | 0 | 34 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 7 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (12 @ 33.6), but the home ask 33.80 is above it); labour need rises ~35/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.30 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 34 labour expired last turn (~62 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **cured meat**: home ask 33.80 is above our ceiling 29.00 and last turn bought 0 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **fish**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 60.1 coin per prestige at mansion, vs 77.5 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **hold banquet 2 (fish)**: hold banquet 2 (fish) costs 65.0 coin per prestige at mansion, vs 77.5 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **tar**: home ask 11.30 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 558, not 658
- labour expiry guard: 34 bought labour expired last turn, buy 30 (not 58) this turn

## Prestige spending, cheapest coin per prestige first

189 turns left: prestige gained now converts 61.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 50.0 | 50.8 | needs a arena (build cost 28,487); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 54.0 | 54.0 | running |
| jousting 2 | arena | 210 | 54.7 | 55.7 | needs a arena (build cost 28,487); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 60.1 | 60.1 |  |
| hold banquet 4 (pies) | mansion | 18 | 64.3 | 64.3 | thin at home: hop beer, stockfish, pies |
| hold banquet 5 | mansion | 22 | 64.5 | 64.5 | thin at home: pies, hop beer, stockfish, sculptures |
| hold banquet 2 (pies) | mansion | 7 | 64.7 | 64.7 | thin at home: pies |
| hold banquet 2 (fish) | mansion | 6.8 | 65.0 | 65.0 |  |
| hold banquet 4 (premium) | mansion | 20 | 66.0 | 66.0 | thin at home: hop beer, stockfish, premium cheese |
| hold mass 2 (premium) | cathedral | 360 | 54.2 | 66.3 | needs a cathedral (build cost 301,760); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |
| hold banquet 4 | mansion | 17.5 | 68.9 | 68.9 | thin at home: hop beer, stockfish |
| hold mass 3 | cathedral | 460 | 60.0 | 69.5 | needs a cathedral (build cost 301,760); thin at home: coats, jewellery, glassware, candles, windows, sculptures, furniture, tapestries, books |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 11 | 151802239 | 0 | beer 15 | pasties 2 | 6 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 12.7 (keep 14); best orders clear only -5 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 16.0 (keep 14); best orders clear only 1 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~115 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 1.00 (115/turn) | bread 217 (2.62->4.41), firewood 37 (2.08->11.97), timber 26 (9.29->12.06), beer 12 (3.34->5.61) | cheese 6 (9.24->12.25), flax plants 14 (2.04->2.96), bricks 5 (8.61->10.54), furniture 8 (15.75->16.62) | +842 |
| Rouhomme | 368 | 0.11 | 0.90 (103/turn) | bread 261 (2.62->3.82), flour 4 (19.84->25.46), wine 14 (6.62->6.93), seeds 8 (3.04->3.52) | bricks 18 (4.68->10.54), cheese 8 (9.45->12.25), tools 18 (4.73->5.61), dyed cloth 10 (14.7->15.48) | +370 |
| Heidlowe | 662 | 0.20 | 0.40 (46/turn) | nets 6 (37.4->40.28), acid 1 (134.4->147.25), wine 14 (6.62->7.69), beer 15 (3.34->4.24) | cheese 8 (6.83->12.25), thread 45 (5.72->6.75), tackles 1 (154.35->171.95), flax plants 19 (1.83->2.96) | +184 |
| Heilegg | 826 | 0.26 | 0.40 (46/turn) | nets 5 (37.4->45.6), flour 4 (19.84->27.55), cured fish 10 (24.57->26.03), butter 3 (76.12->78.85) | cheese 8 (9.03->12.25), cloth 24 (10.5->11.2), jewellery 2 (77.17->80.75), cookware 6 (21->22.23) | +169 |
| Hofkirchen | 991 | 0.36 | 0.40 (46/turn) | nets 6 (37.4->44.27), beer 15 (3.34->4.73), yarn 18 (6.14->6.84), grain 1 (2.26->4.31) | cheese 8 (6.83->12.25), lathes 2 (189->207.1), jewellery 2 (73.5->80.75), cloth 24 (10.5->11.2) | +165 |

**Best:** Grandgues at about +842 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 35.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 15 @ min 3.38 |  |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 9) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 3 @ 29.0, stop 12 |  | goal planner: buys 3 a turn for today's rates, keeps up to 12 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 3 @ 2.5, stop - |  | goal planner: buys 3 for today's rates (v2 had 3) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 25.8) |
| grain | 9 @ 3.7, stop 36 |  | goal planner: buys 9 a turn for today's rates, keeps up to 36 (v2 had 9) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 30) |
| light armour | 1 @ 108, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 36.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 33.2k (cash + stock at home prices); +378/turn over 6 turns, +135/turn over 24 turns.
- Limits: cash flow >= -446/turn, prestige >= -1.09/turn (values are after 200 tax a turn).
- Today's settings: value -191/turn, cash -186/turn, prestige +1.08/turn.
- Plan: value -11/turn, cash -5/turn, prestige -1.09/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +131 vs -158, +224 vs -179, -44 vs -176.
- Route sales counted at most (what the ships really sold, a turn): beer 1.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Blanans: +5/turn
  - ship Flax Wyrm -> Vauxvais: +3/turn
  - mansion 1 1.00 -> 0.48: +164/turn
  - net maker 0.00 -> 0.29: +4/turn
  - ropewalk 1 0.25 -> 0.31: +2/turn
  - flax farm 1 4.64 -> 4.98: -0/turn
  - retting pit 1 0.91 -> 0.99: +6/turn
  - weavery 1 0.50 -> 0.58: -7/turn
  - sewing shop 1 0.30 -> 0.36: +10/turn
- Model check over the last 59 turns: predicted -139/turn for the settings we ran, real +44/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.80, thread 4.52, cloth 7.22, flax fibres 5.36, garments 20.90, nets 33.02, beer 3.24, timber 4.12, prestige 74.85, cash 0.00
- Orders it would set: bread buy 5 (v2 9); cloth sell 1 (v2 none); cured meat buy 3 (v2 12); firewood buy 4 (v2 8); garments sell 11 (v2 10); labour buy 64 (v2 30); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Blanans (+7/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Vauxvais (+4/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1990 coin: +4/turn, payback 450 turns, doesn't pay yet (materials thin at home: limestone)

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

Buffers: flax fibres 85/77, thread 1058/228, cloth 72/128

## Self-diagnosis

- R1: cured meat slot dry: 7.0 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 12 @ 33.6, home ask 33.8 (held back: acted on cured meat at turn 14211 (one action per 2 turns))
- R2: spinnery 1 blocked by thread space: 1058 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
