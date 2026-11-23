# v2 shadow report

Turn 14235, 2026-11-23 12:38. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,348, prestige 3,680 (560 free, -2.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 75 | 0 | 4 | 0 | 0 | min_holding 58, sell 1, sell @ 3.16 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 7 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 7 | 8 | 8 | 1 | 0 | stop 26, buy 7, buy @ 3.7 |
| labour | 64 | 64 | 514 | 0 | 50 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), but the home ask 31.60 is above it); labour need rises ~35/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **cured meat**: only 0.0 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **grain**: brewery 1 ran short of grain (buy is live (7 @ 3.7), 8 bought last turn); labour need rises ~18/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **grain**: only 0.8 turns of grain left and buying 7 (need 18) -> v2: buy 18

## Waste (money lost now)

- **labour**: 50 labour expired last turn (~81 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **cured meat**: home ask 31.60 is above our ceiling 29.00 and last turn bought 0 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **hold banquet 2 (fish)**: hold banquet 2 (fish) costs 58.1 coin per prestige at mansion, vs 71.9 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch

## Notes

- labour: projection runs 106 over real use lately; planning 524, not 630
- labour expiry guard: 50 bought labour expired last turn, buy 15 (not 24) this turn

## Prestige spending, cheapest coin per prestige first

166 turns left: prestige gained now converts 56.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.9 | 48.9 | running |
| maintain 2 | park | 2 | 48.9 | 48.9 | thin at home: sculptures |
| jousting 3 (premium) | arena | 420 | 52.3 | 52.8 | needs a arena (build cost 25,955); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 54.6 | 55.6 | needs a arena (build cost 25,955); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 56.1 | 56.7 | needs a arena (build cost 25,955); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 57.4 | 57.4 | thin at home: beer |
| hold banquet 2 (fish) | mansion | 6.8 | 58.1 | 58.1 |  |
| hold banquet 5 | mansion | 22 | 60.1 | 60.1 | thin at home: hop beer, stockfish, sculptures |
| jousting 2 | arena | 210 | 59.8 | 60.9 | needs a arena (build cost 25,955); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 63.5 | 63.5 |  |
| hold banquet 4 (pies) | mansion | 18 | 64.5 | 64.5 | thin at home: hop beer, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 66.6 | 66.6 | thin at home: hop beer, stockfish, premium cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 10 | 151802239 | 0 | beer 14 | pasties 2 | 19 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 15.4 (keep 14); best orders clear only -7 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only 12 a turn after crew: ship stays at 0
- best towns now: Bordetes +55
- Bordetes would trade: beer sell 14 @ 8.25, pasties buy 1 @ 15.1; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~106 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Vauxvais | 204 | 0.06 | 0.50 (53/turn) | grain 141 (3.04->4.12), bread 171 (2.52->2.96), rope 1 (72.5->85.02), flour 3 (16.8->19.95) | cloth 10 (8.72->11.1), thread 6 (3.09->6.4), bricks 5 (6.72->9.36), flax fibres 6 (6.3->7.35) | +282 |
| Grandgues | 152 | 0.04 | 0.60 (64/turn) | timber 28 (7.77->9.97), beer 14 (3.52->5.22), charcoal 19 (2.6->4.05), jewellery 4 (100.28->104.5) | thread 62 (5.46->6.4), cured meat 7 (21->27.74), bricks 10 (7.4->9.36), dyed cloth 6 (15.44->16.15) | +267 |
| Hanstein | 380 | 0.11 | 1.00 (106/turn) | timber 18 (7.77->11.69), firewood 16 (2.18->6.84), charcoal 17 (2.6->4.71), rope 1 (72.5->79.8) | thread 20 (5.25->6.4), cloth 19 (10.03->11.1), flax fibres 9 (5.67->7.35), wool 13 (10.08->10.64) | +161 |
| Pontmont | 341 | 0.10 | 0.60 (64/turn) | timber 31 (7.77->11.3), cured fish 8 (24.57->32.3), clay 2 (4.14->11.97), flour 3 (16.8->20.14) | flax fibres 6 (6.3->7.35), cloth 8 (10.71->11.1), flax plants 1 (1.72->2) | +159 |
| Angefont | 686 | 0.19 | 0.40 (42/turn) | rope 1 (72.5->87.88), logs 2 (5.35->11.3), flour 2 (16.8->18.9) | thread 62 (5.25->6.4), flax fibres 24 (5.57->7.35), cloth 24 (10.03->11.1), tools 17 (5.41->6.08) | +145 |

**Best:** Vauxvais at about +282 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 30.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 83.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 3 @ 29.0, stop 10 |  | goal planner: buys 3 a turn for today's rates, keeps up to 10 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 15.6, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 27.2) |
| grain | 8 @ 3.7, stop 29 |  | goal planner: buys 8 a turn for today's rates, keeps up to 29 (v2 had 18) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 15) |
| light armour | 1 @ 101, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 41.2) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 70.5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 31.7k (cash + stock at home prices); +73/turn over 6 turns, -30/turn over 24 turns.
- Limits: cash flow >= -431/turn, prestige >= -1.08/turn (values are after 200 tax a turn).
- Today's settings: value -166/turn, cash -165/turn, prestige +1.38/turn.
- Plan: value +31/turn, cash +36/turn, prestige -1.08/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +70 vs -161, +175 vs -141, +188 vs -170.
- Route sales counted at most (what the ships really sold, a turn): beer 1.8, rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Bordetes: +4/turn
  - ship Flax Wyrm -> Grandgues: +2/turn
  - mansion 1 1.00 -> 0.41: +169/turn
  - net maker 0.00 -> 0.29: +10/turn
  - spinnery 1 1.65 -> 1.49: +3/turn
  - flax farm 1 4.64 -> 4.46: -1/turn
  - weavery 1 0.50 -> 0.60: -9/turn
  - sewing shop 1 0.30 -> 0.36: +13/turn
- Model check over the last 59 turns: predicted -157/turn for the settings we ran, real +72/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.63, thread 4.10, cloth 6.54, flax fibres 4.86, garments 18.93, nets 30.12, beer 2.98, timber 3.33, prestige 69.37, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); cured meat buy 3 (v2 12); firewood buy 4 (v2 8); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 8 (v2 18); labour buy 64 (v2 15); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Bordetes (+4/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Grandgues (+4/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +81/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1870 coin: +4/turn, payback 442 turns, doesn't pay yet (materials thin at home: limestone)

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

Buffers: flax fibres 86/77, thread 1050/228, cloth 73/128

## Self-diagnosis

- R1: cured meat slot dry: 0.0 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 3 @ 29, home ask 31.6 -> **buy 12 @ 32.2 (ask 31.6, cap 42.0)** (ok)
- R1: prestige rate -2.81 a turn vs 12-turn median +1.03; likely: dry slot: cured meat; mansion 1 projected 0 (cured meat)
- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
