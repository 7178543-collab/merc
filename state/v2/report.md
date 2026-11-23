# v2 shadow report

Turn 14242, 2026-11-23 19:33. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,381, prestige 3,686 (566 free, +1.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 19 | 0 | 0 | min_holding 58, sell 1, sell @ 3.16 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 9 | 4 | 4 | 0 | 0 | stop 14, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 12 | 6 | 9 | 0 | 0 | stop 22, buy 6, buy @ 3.7 |
| labour | 64 | 64 | 553 | 0 | 11 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**1 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 9.70 x14, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Tuning

- **cured meat**: home ask 29.60 is above our ceiling 29.00 and last turn bought 0 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 54.7 coin per prestige at mansion, vs 66.0 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch

## Notes

- labour: projection runs 106 over real use lately; planning 557, not 663

## Prestige spending, cheapest coin per prestige first

159 turns left: prestige gained now converts 55.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 47.3 | 48.3 | needs a arena (build cost 25,967); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 3 (premium) | arena | 420 | 49.0 | 49.5 | needs a arena (build cost 25,967); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 50.1 | 50.1 | running |
| jousting 2 | arena | 210 | 51.8 | 52.9 | needs a arena (build cost 25,967); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 52.7 | 53.2 | needs a arena (build cost 25,967); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 54.7 | 54.7 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 58.4 | 58.4 |  |
| hold banquet 2 (pies) | mansion | 7 | 61.9 | 61.9 |  |
| hold banquet 4 (pies) | mansion | 18 | 63.1 | 63.1 | thin at home: hop beer, stockfish |
| hold banquet 5 | mansion | 22 | 64.2 | 64.2 | thin at home: hop beer, stockfish, sculptures |
| jousting 1 | arena | 170 | 64.4 | 65.7 | needs a arena (build cost 25,967); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 1 (meat) | mansion | 4.2 | 66.0 | 66.0 | running; thin at home: cured meat |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 10 | 151802239 | 0 | - | cured meat 3 | -67 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: cured meat buy 6 @ 23.0; crew 0.1; est +30 a turn
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 14.2 (keep 14); best orders clear only 9 a turn after crew: ship stays at 0
- best towns now: Kirchwerp +51, Gottweiler +44, Cobholme +32, Grandgues +30, Vauxvais +24
- Kirchwerp would trade: cured meat buy 6 @ 20.4, pasties buy 2 @ 16.2; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~105 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Pontmont | 341 | 0.10 | 0.90 (94/turn) | timber 39 (7.51->11.78), beer 84 (3.21->3.84), paper 4 (21.21->30.4), tackles 2 (154.35->166.25) | bricks 12 (7.35->10.07), thread 35 (5.57->5.9), tools 19 (5.25->5.75), flax fibres 6 (6.98->7.5) | +292 |
| Grandgues | 152 | 0.04 | 0.70 (74/turn) | firewood 34 (2.18->5.79), charcoal 19 (2.35->4.8), timber 27 (7.51->8.79), paper 3 (21.21->25.08) | bricks 19 (5.67->10.07), cured meat 6 (23.73->29.6), thread 28 (5.35->5.9), raw cloth 2 (7.25->7.84) | +276 |
| Hanstein | 380 | 0.11 | 1.00 (105/turn) | timber 17 (7.51->12.35), charcoal 19 (2.35->5.27), tackles 2 (154.35->163.4), firewood 16 (2.18->6.32) | thread 19 (4.56->5.9), cured meat 6 (25.83->29.6), flax fibres 9 (5.72->7.5), garments 2 (26.25->26.8) | +192 |
| Bremcop | 1326 | 0.52 | 0.20 (21/turn) | gears 2 (88.2->142.5), tackles 2 (154.35->164.35), paper 4 (21.21->23.37), leather 2 (29.82->31.73) | lathes 1 (175.35->218.5), yarn 7 (3.72->5.42), cured meat 6 (27.72->29.6), garments 2 (25.2->26.8) | +187 |
| Friedwerp | 684 | 0.19 | 0.30 (32/turn) | tackles 2 (154.35->207.1), beer 56 (3.21->4.48), paper 4 (21.21->23.37), tiles 1 (3.36->7.84) | cured meat 6 (26.46->29.6), axes 2 (16.59->17.86), tools 19 (5.46->5.75), malt 2 (5.23->6.32) | +187 |

**Best:** Pontmont at about +292 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 28.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had None) |
| beer |  | 1 @ min 3.02 | goal planner: sells 1 at 3.02 (v2 had 0 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 83.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 9 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 19 = 3.2 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 14 |  | goal planner: buys 4 a turn for today's rates, keeps up to 14 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 15.9, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 25.8) |
| grain | 6 @ 3.7, stop 22 |  | goal planner: buys 6 a turn for today's rates, keeps up to 22 (v2 had 18) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 57) |
| light armour | 1 @ 101, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 40.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 31.5k (cash + stock at home prices); -18/turn over 6 turns, +3/turn over 24 turns.
- Limits: cash flow >= -391/turn, prestige >= -1.11/turn (values are after 200 tax a turn).
- Today's settings: value -121/turn, cash -120/turn, prestige +1.38/turn.
- Plan: value +44/turn, cash +49/turn, prestige -1.11/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -52 vs -116, -20 vs -113, -63 vs -117.
- Route sales counted at most (what the ships really sold, a turn): beer 2.0, rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Calange: +0/turn
  - ship Flax Wyrm -> Fontaux: +5/turn
  - mansion 1 1.00 -> 0.41: +137/turn
  - brewery 1 0.14 -> 0.08: +10/turn
  - net maker [make nets 1] 0.00 -> 0.38: +5/turn
  - spinnery 1 1.65 -> 1.57: +4/turn
  - sewing shop 1 0.30 -> 0.36: -7/turn
  - weavery 1 0.50 -> 0.60: +10/turn
- Model check over the last 59 turns: predicted -156/turn for the settings we ran, real +44/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.67, thread 4.20, cloth 6.70, flax fibres 4.97, garments 19.39, nets 31.42, beer 2.99, timber 3.22, prestige 59.04, cash 0.00
- Orders it would set: arms buy 1 (v2 None); beer sell 1 (v2 0); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 8); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 6 (v2 18); labour buy 64 (v2 57); light armour buy 1 (v2 None)
- Recipe: net maker make nets 3 -> make nets 1 at 0.38, worth +3/turn.
- Ship linen snake: Grandgues -> Calange (+10/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Fontaux (+2/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new chandlery (make candles 2) for ~5089 coin: +2/turn, payback 2573 turns, doesn't pay yet (materials thin at home: bricks, nails)

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

Buffers: flax fibres 86/77, thread 1054/228, cloth 73/128

## Self-diagnosis

- R2: spinnery 1 blocked by thread space: 1054 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
