# v2 shadow report

Turn 14251, 2026-11-24 04:38. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,287, prestige 3,698 (578 free, +1.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 43 | 23 | 19 | 0 | 0 | stop 116, buy 39, buy @ 3.82 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 12 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 7 | 7 | 7 | 2 | 0 | stop 25, buy 7, buy @ 3.7 |
| labour | 65 | 65 | 565 | 5 | 0 | buy 65, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **grain**: brewery 1 ran short of grain (buy is live (7 @ 3.7), 7 bought last turn); labour need rises ~18/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **grain**: only 0.8 turns of grain left and buying 7 (need 18) -> v2: buy 18

## Tuning

- **fish**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **hold banquet 2 (fish)**: hold banquet 2 (fish) costs 55.4 coin per prestige at mansion, vs 65.6 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch

## Notes

- labour: projection runs 116 over real use lately; planning 570, not 648

## Prestige spending, cheapest coin per prestige first

150 turns left: prestige gained now converts 52.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 48.1 | 49.3 | needs a arena (build cost 26,803); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 50.4 | 50.4 | running |
| jousting 2 | arena | 210 | 52.7 | 54.0 | needs a arena (build cost 26,803); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 55.4 | 55.4 |  |
| hold banquet 1 (fish) | mansion | 4.2 | 56.2 | 56.2 | thin at home: beer |
| hold banquet 2 (pies) | mansion | 7 | 60.4 | 60.4 |  |
| hold banquet 2 (meat) | mansion | 6.8 | 62.7 | 62.7 |  |
| hold banquet 5 | mansion | 22 | 63.5 | 63.5 | thin at home: hop beer, stockfish, sculptures |
| maintain 2 | park | 2 | 63.6 | 63.6 | thin at home: sculptures |
| hold banquet 4 (pies) | mansion | 18 | 64.6 | 64.6 | thin at home: hop beer, stockfish |
| hold banquet 1 (meat) | mansion | 4.2 | 65.6 | 65.6 | running; thin at home: beer |
| hold banquet 3 (fish) | mansion | 7.6 | 67.7 | 67.7 | thin at home: hop beer |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 10 | 134102075 | 0 | - | cured meat 3, pasties 1 | -92 |
| linen snake | 0.1 / 0.10 | 10 | 151802239 | 0 | - | cured meat 6 | -142 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: cured meat buy 6 @ 25.0, pasties buy 3 @ 12.3; crew 0.1; est +19 a turn; stock: pasties 3 @ 12.3 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 14.5 (keep 14); best orders clear only 3 a turn after crew: ship stays at 0
- best towns now: Darmwald +29, Donaunieder +29, Rotterburg +24, Grandgues +19, Helmgreen +19
- Darmwald would trade: cured meat buy 6 @ 21.4, pasties buy 3 @ 16.2; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~107 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.50 (54/turn) | bread 172 (2.54->3.57), garments 10 (30->36.48), nets 3 (35.6->42.56), timber 25 (8.24->9.4) | tools 20 (5.12->7.22), bricks 7 (7.46->9.5), dyed cloth 5 (14.7->15.77), cured meat 6 (25.83->26.6) | +337 |
| Rouhomme | 368 | 0.10 | 0.90 (96/turn) | grain 143 (3.07->3.84), garments 10 (30->36.48), bread 172 (2.54->2.94), axes 2 (14.18->17.67) | tools 41 (5.99->7.22), bricks 21 (5.41->9.5), thread 29 (5.57->6.05), cookware 5 (24.99->26.79) | +297 |
| Kirchwerp | 1072 | 0.39 | 0.60 (64/turn) | canvas 6 (41.79->57), casks 11 (6.51->9.36), paper 8 (25.83->28.88), axes 4 (14.18->17) | cloth 15 (7.35->10.2), cookware 5 (21->26.79), dyed cloth 5 (9.97->15.77), garments 2 (24.15->30.6) | +285 |
| Pontmont | 341 | 0.10 | 0.50 (54/turn) | timber 24 (8.24->14.06), tiles 7 (3.17->7.74), raw cloth 9 (9.35->11.4), furniture 8 (16.07->17.76) | tools 41 (5.78->7.22), bricks 14 (5.67->9.5), thread 35 (5.57->6.05), garments 2 (28.35->30.6) | +274 |
| Bedenis | 566 | 0.16 | 0.70 (75/turn) | cloth 17 (10.71->17.1), garments 10 (30->35.34), axes 3 (14.18->17.39), cured meat 1 (24.17->27.74) | tools 41 (5.62->7.22), bricks 11 (5.25->9.5), thread 21 (5.57->6.05), yarn 13 (4.98->5.42) | +266 |

**Best:** Grandgues at about +337 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 37 @ 4.1, stop 77 |  | uses 19.2/turn (household upkeep, mansion 1), makes 0.0, holds 43 = 2.2 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 89.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 7 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 22 = 3.7 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 14 |  | goal planner: buys 4 a turn for today's rates, keeps up to 14 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 29.2) |
| grain | 18 @ 3.7, stop 36 |  | uses 9.0/turn (observed), makes 0.0, holds 7 = 0.8 turns |
| labour | 65 @ 2.2, stop - |  | goal planner: buys 65 for today's rates (v2 had 70) |
| light armour | 1 @ 95, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.6) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 85.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 31.5k (cash + stock at home prices); +37/turn over 6 turns, +15/turn over 24 turns.
- Limits: cash flow >= -345/turn, prestige >= -1.16/turn (values are after 200 tax a turn).
- Today's settings: value -145/turn, cash -137/turn, prestige +1.32/turn.
- Plan: value +26/turn, cash +37/turn, prestige -1.16/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -243 vs -120, +24 vs -141, -143 vs -144.
- Route sales counted at most (what the ships really sold, a turn): beer 2.2, rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Darmwald: +17/turn
  - ship Flax Wyrm -> Essenbrucke: +2/turn
  - mansion 1 1.00 -> 0.41: +145/turn
  - brewery 1 0.14 -> 0.08: +9/turn
  - net maker [make nets 1] 0.00 -> 0.38: +5/turn
  - spinnery 1 1.65 -> 1.57: +3/turn
  - sewing shop 1 0.30 -> 0.36: -11/turn
  - weavery 1 0.50 -> 0.60: +14/turn
- Model check over the last 59 turns: predicted -155/turn for the settings we ran, real +21/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.68, thread 4.22, cloth 6.74, flax fibres 5.00, garments 19.51, nets 31.61, beer 3.04, timber 3.42, prestige 62.30, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 5); garments sell 11 (v2 10); labour buy 65 (v2 70); light armour buy 1 (v2 None)
- Recipe: net maker make nets 3 -> make nets 1 at 0.38, worth +3/turn.
- Ship linen snake: Grandgues -> Darmwald (+6/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Essenbrucke (+2/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +84/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new chandlery (make candles 2) for ~5329 coin: +10/turn, payback 536 turns, doesn't pay yet (materials thin at home: bricks, nails)

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

Buffers: flax fibres 85/77, thread 1060/228, cloth 72/128

## Self-diagnosis

- R2: spinnery 1 blocked by thread space: 1060 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
