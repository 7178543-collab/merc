# v2 shadow report

Turn 14004, 2026-11-13 21:43. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,756, prestige 3,500 (380 free, +2.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 108 | 27 | 19 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 116, buy 39, buy @ 3.76 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 4, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 22, buy 6, buy @ 3.7 |
| labour | 64 | 64 | 544 | 0 | 20 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 3.08 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.08 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 10.90 x13, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 20 labour expired last turn (~39 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 57.8 coin per prestige at mansion, vs 70.2 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **hold banquet 2 (fish)**: hold banquet 2 (fish) costs 57.6 coin per prestige at mansion, vs 70.2 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch

## Notes

- labour: projection runs 89 over real use lately; planning 544, not 632

## Prestige spending, cheapest coin per prestige first

397 turns left: prestige gained now converts 86.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 56.1 | 56.5 | needs a arena (build cost 28,925); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 57.6 | 57.6 |  |
| hold banquet 1 (fish) | mansion | 4.2 | 57.8 | 57.8 |  |
| maintain 1 | park | 0.5 | 58.5 | 58.5 | running |
| jousting 2 | arena | 210 | 61.5 | 61.9 | needs a arena (build cost 28,925); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 62.3 | 62.3 | thin at home: hop beer |
| hold banquet 2 (pies) | mansion | 7 | 62.6 | 62.6 | thin at home: pasties, pies |
| hold banquet 4 (pies) | mansion | 18 | 62.8 | 62.8 | thin at home: hop beer, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 62.9 | 62.9 | thin at home: hop beer, stockfish |
| hold mass 2 (premium) | cathedral | 360 | 60.3 | 63.1 | needs a cathedral (build cost 280,680); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |
| hold banquet 3 (pies) | mansion | 8 | 65.6 | 65.6 | thin at home: pasties, hop beer, pies |
| hold banquet 4 | mansion | 17.5 | 66.2 | 66.2 | thin at home: hop beer, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 11 | 151802239 | 0.048 | - | cured meat 6 | -141 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: cured meat buy 6 @ 23.8; crew 0.1; est +19 a turn
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 15.1 (keep 14); best orders clear only -4 a turn after crew: ship stays at 0
- best towns now: Neuborn +33, Gottweiler +32, Hofkirchen +30, Großmühle +29, Orlesailles +27
- Neuborn would trade: cured meat buy 6 @ 22.4, pasties buy 2 @ 15.9; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~118 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Fontaux | 411 | 0.13 | 0.20 (24/turn) | thread 72 (4.76->7.27), medicine 1 (135.45->182.4), malt 2 (5.93->7.98), leather 1 (23.1->25.65) | cured meat 3 (26.04->28.8), flax fibres 6 (5.35->6.45), candles 1 (85.58->87.5), garments 2 (24.78->25.2) | +237 |
| Dortdorf | 871 | 0.29 | 0.10 (12/turn) | nets 6 (35->36.86), malt 4 (5.93->6.55) | looms 1 (582.75->693.5), cured meat 6 (25.62->28.8), cookware 7 (23.94->24.7), garments 2 (23.52->25.2) | +140 |
| Kirchwerp | 1072 | 0.42 | 0.70 (82/turn) | thread 106 (4.76->5.7), lead bars 7 (16.38->20.9), cheese 11 (6.3->8.07), nets 4 (35->37.62) | garments 2 (22.26->25.2), dyed cloth 6 (11.34->12.25), hop beer 3 (10.82->12.82), cloth 24 (7.46->7.95) | +135 |
| Grandgues | 152 | 0.05 | 0.30 (35/turn) | timber 24 (9.24->12.06), charcoal 19 (2.27->3.63), leather 1 (23.1->27.93), nets 1 (35->39.9) | cured meat 6 (24.57->28.8), dyed cloth 6 (11.03->12.25), garments 2 (22.68->25.2), candles 1 (86.62->87.5) | +123 |
| Blanans | 297 | 0.09 | 0.60 (71/turn) | timber 37 (9.24->11.4), cheese 11 (6.3->7.98), limestone 3 (19.32->28.5), thread 13 (4.76->5.42) | cured meat 6 (26.67->28.8), dyed cloth 6 (11.23->12.25), cloth 15 (7.56->7.95), garments 2 (23.73->25.2) | +107 |

**Best:** Fontaux at about +237 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 35.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 20 @ 3.88, stop 77 |  | uses 19.2/turn (household upkeep, mansion 1), makes 0.0, holds 108 = 5.6 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 8) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 9 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 18 = 3.0 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 16.8, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 21.0) |
| grain | 6 @ 3.7, stop 24 |  | goal planner: buys 6 a turn for today's rates, keeps up to 24 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 44) |
| light armour | 1 @ 97.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 34.0) |
| pasties |  | 1 @ min 17.5 | goal planner: trial sale of an idle pile, 1 a turn at 17.5, keeps 0 (12 over) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 29.2k (cash + stock at home prices); -165/turn over 6 turns, +29/turn over 24 turns.
- Limits: cash flow >= -406/turn, prestige >= -0.34/turn (values are after 200 tax a turn).
- Today's settings: value -203/turn, cash -184/turn, prestige +2.11/turn.
- Plan: value -26/turn, cash -21/turn, prestige -0.34/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -114 vs -143, -87 vs -182, -214 vs -161.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Hofkirchen: -1/turn
  - ship Flax Wyrm -> Neuborn: +7/turn
  - mansion 1 1.00 -> 0.42: +147/turn
  - spinnery 1 1.65 -> 1.36: +8/turn
  - retting pit 1 0.91 -> 0.85: +1/turn
  - flax farm 1 4.64 -> 4.29: +4/turn
  - net maker 0.00 -> 0.29: +1/turn
  - weavery 1 0.50 -> 0.39: -2/turn
  - sewing shop 1 0.30 -> 0.23: +9/turn
- Model check over the last 60 turns: predicted +55/turn for the settings we ran, real +2/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.96, garments 19.30, nets 30.31, beer 3.19, timber 3.58, prestige 60.89, cash 0.00
- Orders it would set: bread buy 5 (v2 8); cloth sell 1 (v2 none); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 6 (v2 0); labour buy 64 (v2 44); light armour buy 1 (v2 None); pasties sell 1 (v2 none)
- Ship linen snake: Grandgues -> Hofkirchen (+2/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Neuborn (+2/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 419 (+130 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.16 |
| ret | 3 | 0.91 | 0.83 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 120/77, thread 1063/228, cloth 72/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 3.08; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1063 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
