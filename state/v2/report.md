# v2 shadow report

Turn 14234, 2026-11-23 11:33. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,160, prestige 3,683 (563 free, -2.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 77 | 0 | 4 | 0 | 0 | min_holding 58, sell 1, sell @ 3.16 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 7 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 8 | 8 | 8 | 1 | 0 | stop 31, buy 8, buy @ 3.7 |
| labour | 64 | 65 | 526 | 0 | 39 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**5 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), but the home ask 31.20 is above it); labour need rises ~35/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **cured meat**: only 0.0 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **grain**: brewery 1 ran short of grain (buy is live (8 @ 3.7), 8 bought last turn); labour need rises ~18/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **grain**: only 0.9 turns of grain left and buying 8 (need 18) -> v2: buy 18
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 9.95 x12, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 39 labour expired last turn (~64 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **cured meat**: home ask 31.20 is above our ceiling 29.00 and last turn bought 0 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 57.3 coin per prestige at mansion, vs 69.5 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **hold banquet 2 (fish)**: hold banquet 2 (fish) costs 59.0 coin per prestige at mansion, vs 69.5 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch

## Notes

- labour: projection runs 106 over real use lately; planning 526, not 614
- labour expiry guard: 39 bought labour expired last turn, buy 26 (not 26) this turn

## Prestige spending, cheapest coin per prestige first

167 turns left: prestige gained now converts 56.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.9 | 48.9 | running |
| jousting 3 (premium) | arena | 420 | 52.0 | 52.5 | needs a arena (build cost 26,007); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 54.2 | 55.2 | needs a arena (build cost 26,007); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 55.8 | 56.3 | needs a arena (build cost 26,007); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 57.3 | 57.3 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 59.0 | 59.0 |  |
| jousting 2 | arena | 210 | 59.4 | 60.4 | needs a arena (build cost 26,007); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| maintain 2 | park | 2 | 61.1 | 61.1 | thin at home: sculptures |
| hold banquet 2 (pies) | mansion | 7 | 62.7 | 62.7 |  |
| hold banquet 5 | mansion | 22 | 63.1 | 63.1 | thin at home: hop beer, stockfish, sculptures |
| hold banquet 4 (pies) | mansion | 18 | 64.7 | 64.7 | thin at home: hop beer, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 66.5 | 66.5 | thin at home: hop beer, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 10 | 151802239 | 0 | beer 10 | - | 35 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: beer sell 14 @ 5.4, pasties buy 2 @ 13.4; crew 0.1; est +23 a turn; stock: pasties 2 @ 13.4 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 15.1 (keep 14); best orders clear only -3 a turn after crew: ship stays at 0
- best towns now: Bordetes +58, Fontaux +27, Grandgues +23
- Bordetes would trade: beer sell 14 @ 8.1, pasties buy 2 @ 15.1; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~106 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Unterhufe | 595 | 0.17 | 0.30 (32/turn) | rope 1 (76.12->80.75), resin 3 (1.9->3.02) | sails 1 (871.5->1083), flax fibres 23 (6.46->8.2), cloth 24 (9.55->11), tools 17 (5.62->6.74) | +300 |
| Vauxvais | 204 | 0.06 | 0.20 (21/turn) | grain 145 (3.07->4.01), rope 1 (76.12->86.92), beer 14 (2.94->3.8), flour 3 (16.8->19.38) | sails 1 (1034.25->1083), thread 9 (3.09->6.1), cloth 10 (8.35->11), tools 17 (5.78->6.74) | +299 |
| Rouhomme | 368 | 0.10 | 0.40 (42/turn) | grain 161 (3.07->3.76), cheese 15 (6.2->8.5), flour 3 (16.8->20.9), rope 1 (76.12->85.5) | tools 17 (4.73->6.74), flax fibres 17 (6.3->8.2), bricks 11 (5.25->9.5), thread 27 (5.57->6.1) | +245 |
| Arnsreuth | 921 | 0.29 | 0.30 (32/turn) | glass ingots 2 (66.67->69.83), hides 1 (10.92->14.72), leather 2 (27.93->29.26), resin 1 (1.9->3.15) | sails 1 (887.25->1083), flax fibres 28 (7.09->8.2), lathes 1 (205.8->218.5), cloth 15 (10.5->11) | +236 |
| Grandgues | 152 | 0.04 | 0.60 (63/turn) | timber 29 (7.82->9.97), beer 14 (2.94->5.22), charcoal 19 (2.62->3.93), flour 3 (16.8->19.76) | thread 50 (5.41->6.1), lathes 2 (205.8->218.5), cured meat 7 (24.78->27.74), bricks 11 (7.14->9.5) | +234 |

**Best:** Unterhufe at about +300 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 29.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had None) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 83.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 3 @ 29.0, stop 10 |  | goal planner: buys 3 a turn for today's rates, keeps up to 10 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 15.6, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 26.2) |
| grain | 7 @ 3.7, stop 26 |  | goal planner: buys 7 a turn for today's rates, keeps up to 26 (v2 had 18) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 26) |
| light armour | 1 @ 101, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 40.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 31.2k (cash + stock at home prices); -4/turn over 6 turns, -35/turn over 24 turns.
- Limits: cash flow >= -423/turn, prestige >= -1.10/turn (values are after 200 tax a turn).
- Today's settings: value -171/turn, cash -170/turn, prestige +1.37/turn.
- Plan: value +24/turn, cash +34/turn, prestige -1.10/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +156 vs -159, +70 vs -161, +175 vs -141.
- Route sales counted at most (what the ships really sold, a turn): beer 1.6, rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Bordetes: +4/turn
  - ship Flax Wyrm -> Fontaux: +3/turn
  - mansion 1 1.00 -> 0.41: +166/turn
  - net maker 0.00 -> 0.29: +10/turn
  - spinnery 1 1.65 -> 1.47: +4/turn
  - flax farm 1 4.64 -> 4.41: -1/turn
  - weavery 1 0.50 -> 0.60: -8/turn
  - sewing shop 1 0.30 -> 0.36: +13/turn
- Model check over the last 58 turns: predicted -157/turn for the settings we ran, real +66/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.63, thread 4.10, cloth 6.54, flax fibres 4.86, garments 18.93, nets 30.15, beer 2.99, timber 3.35, prestige 68.83, cash 0.00
- Orders it would set: arms buy 1 (v2 None); candles buy 2 (v2 None); cloth sell 1 (v2 none); cured meat buy 3 (v2 12); firewood buy 4 (v2 8); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 7 (v2 18); labour buy 64 (v2 26); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Bordetes (+4/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Fontaux (+4/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +81/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1856 coin: +4/turn, payback 468 turns, doesn't pay yet (materials thin at home: limestone)

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

Buffers: flax fibres 84/77, thread 1062/228, cloth 72/128

## Self-diagnosis

- R1: cured meat slot dry: 0.0 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 3 @ 29, home ask 31.2 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 12 @ 31.8 (ask 31.2, cap 42.0))
- R1: prestige rate -2.83 a turn vs 12-turn median +1.03; likely: dry slot: cured meat; mansion 1 projected 0 (cured meat)
- R2: spinnery 1 blocked by thread space: 1062 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
