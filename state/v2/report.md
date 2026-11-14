# v2 shadow report

Turn 14028, 2026-11-14 21:56. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,517, prestige 3,601 (481 free, +1.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 38 | 0 | 19 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 545 | 0 | 19 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **beer**: needed (19.2/turn) but there is NO buy order, stock 37.7 -> v2: add buy 39
- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.20 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 19 labour expired last turn (~34 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.20 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 545, not 620

## Prestige spending, cheapest coin per prestige first

373 turns left: prestige gained now converts 84.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 53.1 | 53.1 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 55.9 | 55.9 |  |
| jousting 3 | arena | 230 | 56.0 | 56.4 | needs a arena (build cost 26,974); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 57.5 | 57.5 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 58.0 | 58.0 |  |
| hold banquet 3 (pies) | mansion | 8 | 60.0 | 60.0 | thin at home: hop beer |
| hold banquet 4 (pies) | mansion | 18 | 60.7 | 60.7 | thin at home: hop beer, ham, stockfish |
| hold banquet 3 (fish) | mansion | 7.6 | 61.4 | 61.4 | thin at home: hop beer |
| jousting 2 | arena | 210 | 61.3 | 61.7 | needs a arena (build cost 26,974); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (meat) | mansion | 4.2 | 62.7 | 62.7 | running |
| hold banquet 2 (meat) | mansion | 6.8 | 63.0 | 63.0 |  |
| hold banquet 4 (premium) | mansion | 20 | 63.7 | 63.7 | thin at home: hop beer, ham, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: cured meat buy 6 @ 23.0, pasties buy 3 @ 15.1; crew 0.1; est +16 a turn; stock: pasties 3 @ 15.1 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 15.4 (keep 14); best orders clear only 4 a turn after crew: ship stays at 0
- best towns now: Hofkirchen +662, Amsdermund +632, Chatgnan +474, Cobholme +308, Boistot +269
- Hofkirchen would trade: cured meat buy 6 @ 22.6, furniture buy 63 @ 14.6; crew 0.9

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~111 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.90 (100/turn) | timber 37 (7.98->11.97), firewood 28 (2.69->6.7), bread 157 (2.48->2.87), thread 19 (4.66->5.98) | tools 23 (5.99->7.12), cloth 6 (8.24->10.5), cured meat 6 (23.73->25.6), garments 2 (22.47->23) | +325 |
| Amsdermund | 1111 | 0.42 | 0.40 (45/turn) | wine 14 (6.98->9.5), nets 5 (34.6->38.19), pasties 6 (14.7->17.39), grain 2 (2.88->4.46) | cloth 24 (7.35->10.5), tools 28 (4.83->7.12), casks 17 (5.35->6.65), hop beer 2 (7.98->9.69) | +182 |
| Kirchwerp | 1072 | 0.40 | 0.60 (67/turn) | thread 94 (4.66->5.56), nets 6 (34.6->37.62), wax 9 (23.94->24.7), arms 6 (32.13->33.25) | cloth 24 (7.56->10.5), tools 28 (5.83->7.12), dyed cloth 10 (10.92->12.44), garments 2 (22.05->23) | +168 |
| Darmwald | 1022 | 0.37 | 0.80 (89/turn) | charcoal 19 (2.71->8.6), garments 10 (22->25.46), nets 4 (34.6->37.81), thread 4 (4.66->5.7) | cloth 24 (8.03->10.5), cured meat 6 (24.15->25.6), candles 1 (85.58->89) | +161 |
| Vauxvais | 204 | 0.06 | 1.00 (111/turn) | firewood 39 (2.69->5.7), charcoal 15 (2.71->4.62), axes 3 (23.1->29.45), bread 130 (2.48->2.75) | tools 23 (5.3->7.12), cloth 11 (9.35->10.5), flax fibres 5 (6.04->6.55), blades 1 (14.38->15.2) | +161 |

**Best:** Grandgues at about +325 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 39 @ 3.46, stop 77 |  | uses 19.2/turn (household upkeep, mansion 1), makes 0.0, holds 38 = 2.0 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 91, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 3 = 0.5 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 17.9, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 20.6) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 45) |
| light armour | 1 @ 107, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 34.0) |
| pasties |  | 1 @ min 12.3 | goal planner: sells 1 a turn at 12.3, keeps 0 (no one offered it) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 24.6k (cash + stock at home prices); +55/turn over 6 turns, -188/turn over 24 turns.
- Limits: cash flow >= -313/turn, prestige >= -0.75/turn (values are after 200 tax a turn).
- Today's settings: value -191/turn, cash -174/turn, prestige +1.60/turn.
- Plan: value -34/turn, cash -20/turn, prestige -0.75/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +108 vs -167, -213 vs -177, -50 vs -169.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Brunnham: +3/turn
  - ship Flax Wyrm -> Hofkirchen: +5/turn
  - mansion 1 1.00 -> 0.44: +143/turn
  - spinnery 1 1.65 -> 1.36: +5/turn
  - retting pit 1 0.91 -> 0.85: +1/turn
  - flax farm 1 4.64 -> 4.29: +3/turn
  - net maker 0.00 -> 0.29: -1/turn
  - ropewalk 1 0.25 -> 0.00: -11/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.33: +10/turn
  - sewing shop 1 0.30 -> 0.20: -17/turn
- Model check over the last 59 turns: predicted -66/turn for the settings we ran, real -63/turn.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.95, garments 19.30, nets 30.26, beer 3.10, timber 3.92, prestige 59.39, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 2 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 0); labour buy 64 (v2 45); light armour buy 1 (v2 None); pasties sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.33, worth +11/turn.
- Ship linen snake: Grandgues -> Brunnham (+6/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Hofkirchen (+2/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

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

Buffers: flax fibres 87/77, thread 1052/228, cloth 72/128

## Self-diagnosis

- R1: beer slot dry: 37.7 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy none, home ask 3.3 -> **buy 39 @ 3.36 (ask 3.3, cap 14.4)** (ok)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1052 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
