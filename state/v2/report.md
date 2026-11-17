# v2 shadow report

Turn 14092, 2026-11-17 13:24. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,759, prestige 3,620 (500 free, -3.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 9 | 0 | 0 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 9, buy @ 3.8 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 21, buy 6, buy @ 3.7 |
| labour | 29 | 29 | 517 | 0 | 12 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 0 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.90 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.90 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 10.50 x5, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Notes

- labour: projection runs 100 over real use lately; planning 517, not 610

## Prestige spending, cheapest coin per prestige first

309 turns left: prestige gained now converts 78.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 51.3 | 51.7 | needs a arena (build cost 27,941); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 53.1 | 53.1 | running |
| jousting 2 | arena | 210 | 56.1 | 56.7 | needs a arena (build cost 27,941); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 58.6 | 58.6 | thin at home: cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 61.7 | 61.7 | thin at home: hop beer, cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 62.0 | 62.0 | thin at home: cured fish |
| hold banquet 1 (meat) | mansion | 4.2 | 62.2 | 62.2 |  |
| hold banquet 3 (pies) | mansion | 8 | 62.9 | 62.9 | thin at home: hop beer |
| hold banquet 3 (meat) | mansion | 7.6 | 63.9 | 63.9 | thin at home: hop beer |
| hold banquet 4 (premium) | mansion | 20 | 64.1 | 64.1 | thin at home: hop beer, stockfish, premium ham |
| hold banquet 4 (pies) | mansion | 18 | 64.2 | 64.2 | thin at home: hop beer, stockfish |
| hold banquet 2 (meat) | mansion | 6.8 | 64.4 | 64.4 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.20 | 21 | 134102075 | 0.308 | - | furniture 17, pasties 1 | -262 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 18 @ 14.6, pasties buy 2 @ 16.3; crew 0.2; est +195 a turn; stock: furniture 18 @ 14.6 (keep 145); stock: pasties 2 @ 16.3 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Amsdermund +674, Nürnnieder +480, Gotthafen +452, Vauxvais +404, Fulkirch +385
- Amsdermund would trade: furniture buy 62 @ 13.7; crew 1.0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~113 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.90 (102/turn) | timber 30 (8.45->12.63), firewood 35 (3.04->7.03), charcoal 19 (2.5->4.94), bread 160 (2.77->3.13) | wool 1 (12.39->19.38), bricks 3 (10.34->13.3), candles 1 (85.05->89.5), flax fibres 2 (6.46->7.5) | +296 |
| Hofkirchen | 991 | 0.36 | 0.70 (79/turn) | jewellery 21 (96.6->100.7), looms 1 (588->617.5), lathes 2 (192.15->199.5) | flax fibres 28 (5.62->7.5), dyed cloth 7 (12.6->15.67), garments 2 (26.25->33.2), thread 18 (4.43->5.3) | +226 |
| Clarfranche | 1484 | 0.66 | 0.30 (34/turn) | jewellery 4 (96.6->120.65), windows 1 (829.5->888.25), looms 1 (588->612.75), nets 4 (35.2->37.43) | cloth 12 (9.19->10.8), wool 1 (11.13->19.38), garments 2 (29.19->33.2), candles 1 (86.1->89.5) | +208 |
| Kirchwerp | 1072 | 0.41 | 0.70 (79/turn) | thread 100 (5->5.7), looms 1 (588->612.75), wheels 1 (24.57->34.58), lead ore 7 (7.72->10.45) | cloth 24 (8.77->10.8), flax fibres 28 (5.62->7.5), dyed cloth 7 (12.6->15.67), garments 2 (26.25->33.2) | +202 |
| Fontaux | 411 | 0.12 | 0.70 (79/turn) | thread 44 (5->7.27), timber 23 (8.45->11.49), salt 13 (5.78->7.79), arms 3 (33.18->35.34) | bricks 8 (9.08->13.3), ploughs 1 (70.35->77.42), candles 1 (88.73->89.5) | +178 |

**Best:** Grandgues at about +296 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 33.2) |
| grain | 6 @ 3.7, stop 21 |  | goal planner: buys 6 a turn for today's rates, keeps up to 21 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 17) |
| light armour | 1 @ 101, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.2) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 25.0k (cash + stock at home prices); +139/turn over 6 turns, +128/turn over 24 turns.
- Limits: cash flow >= -282/turn, prestige >= -0.84/turn (values are after 200 tax a turn).
- Today's settings: value +104/turn, cash +87/turn, prestige -3.22/turn - breaks the prestige floor.
- Plan: value -3/turn, cash +7/turn, prestige -0.84/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +2 vs +74, +179 vs +95, -156 vs +84.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Amsdermund: +9/turn
  - spinnery 1 1.65 -> 1.57: +4/turn
  - net maker 0.00 -> 0.28: +4/turn
  - flax farm 1 4.64 -> 4.80: -2/turn
  - weavery 1 0.50 -> 0.59: -7/turn
  - sewing shop 1 0.30 -> 0.36: +11/turn
  - mansion 1 0.00 -> 0.57: -131/turn
- Model check over the last 60 turns: predicted +85/turn for the settings we ran, real +22/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.77, thread 4.45, cloth 7.10, flax fibres 5.27, garments 20.55, nets 32.03, beer 3.17, timber 3.46, prestige 60.51, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 1 (v2 3); garments sell 11 (v2 10); grain buy 6 (v2 0); labour buy 29 (v2 17); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Amsdermund (+9/turn over staying).
- Ship Flax Wyrm: stays on Caillechâtel (worth +1/turn).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +89/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new leatherworks (make leather armour 1) for ~4340 coin: +2/turn, payback 2775 turns, doesn't pay yet (materials thin at home: bricks, nails)

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

Buffers: flax fibres 85/77, thread 1058/228, cloth 72/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.9; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1058 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
