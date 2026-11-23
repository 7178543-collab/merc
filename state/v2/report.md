# v2 shadow report

Turn 14239, 2026-11-23 16:16. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,516, prestige 3,682 (562 free, +1.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 68 | 0 | 19 | 0 | 0 | min_holding 58, sell 1, sell @ 3.16 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 9 | 4 | 4 | 0 | 0 | stop 14, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 6 | 7 | 7 | 2 | 0 | stop 23, buy 6, buy @ 3.7 |
| labour | 65 | 64 | 559 | 0 | 5 | buy 65, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **grain**: brewery 1 ran short of grain (buy is live (6 @ 3.7), 7 bought last turn); labour need rises ~18/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **grain**: only 0.7 turns of grain left and buying 6 (need 18) -> v2: buy 18

## Tuning

- **beer**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **hold banquet 2 (fish)**: hold banquet 2 (fish) costs 57.6 coin per prestige at mansion, vs 69.2 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch

## Notes

- labour: projection runs 97 over real use lately; planning 571, not 668

## Prestige spending, cheapest coin per prestige first

162 turns left: prestige gained now converts 55.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.5 | 49.5 | running |
| jousting 3 | arena | 230 | 48.8 | 49.8 | needs a arena (build cost 25,753); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 3 (premium) | arena | 420 | 49.5 | 50.0 | needs a arena (build cost 25,753); thin at home: protection, light armour, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 53.1 | 53.7 | needs a arena (build cost 25,753); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 2 | arena | 210 | 53.5 | 54.6 | needs a arena (build cost 25,753); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 57.6 | 57.6 |  |
| hold banquet 1 (fish) | mansion | 4.2 | 57.7 | 57.7 | thin at home: beer |
| hold banquet 2 (pies) | mansion | 7 | 60.9 | 60.9 |  |
| hold banquet 4 (pies) | mansion | 18 | 62.8 | 62.8 | thin at home: hop beer, stockfish |
| hold banquet 5 | mansion | 22 | 64.0 | 64.0 | thin at home: hop beer, stockfish, sculptures |
| hold banquet 4 (premium) | mansion | 20 | 65.8 | 65.8 | thin at home: hop beer, stockfish, premium cheese |
| hold banquet 4 | mansion | 17.5 | 66.1 | 66.1 | thin at home: hop beer, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 10 | 134102075 | 0 | - | cured meat 4, pasties 3 | -148 |
| linen snake | 0.1 / 0.10 | 10 | 151802239 | 0 | - | cured meat 5, pasties 1 | -117 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: cured meat buy 6 @ 21.6, pasties buy 1 @ 16.4; crew 0.1; est +39 a turn; stock: pasties 1 @ 16.4 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 14.8 (keep 14); best orders clear only -0 a turn after crew: ship stays at 0
- best towns now: Gottweiler +42, Grandgues +39, Hanbrücken +24, Heidlowe +19, Friedwerp +17
- Gottweiler would trade: cured meat buy 6 @ 21.4, pasties buy 1 @ 14.9; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~105 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Brebronn | 862 | 0.26 | 0.70 (73/turn) | cloth 24 (10.82->12.82), tiles 3 (3.38->12.54), honey 1 (4.2->8.03), glass ingots 1 (66.67->67.92) | flax plants 72 (0.47->2.14), thread 62 (4.56->6.1), flax fibres 16 (5.57->7.5), cured meat 4 (27.51->29.4) | +259 |
| Grandgues | 152 | 0.04 | 0.80 (84/turn) | charcoal 19 (2.07->4.39), firewood 38 (2.18->4.35), timber 27 (7.56->9.03), ploughs 2 (77.17->83.12) | cured meat 6 (22.26->29.4), bricks 13 (6.2->9.97), thread 50 (5.57->6.1), flax plants 7 (1.99->2.14) | +218 |
| Pontmont | 341 | 0.10 | 0.70 (73/turn) | timber 40 (7.56->11.02), wrought iron 4 (18.69->27.55), paper 5 (26.46->30.4), thread 8 (5.85->7.6) | bricks 11 (7.14->9.97), flax fibres 5 (5.78->7.5), cloth 4 (8.93->10.3), flax plants 1 (1.59->2.14) | +194 |
| Hofkirchen | 991 | 0.33 | 0.30 (31/turn) | arms 9 (29.19->32.68), seeds 8 (2.44->6.17), glass ingots 2 (66.67->75.52), ploughs 2 (77.17->85.5) | lathes 2 (198.45->218.5), jewellery 4 (74.03->79.33), cloth 24 (9.61->10.3), tools 18 (5.04->5.7) | +163 |
| Neuborn | 780 | 0.22 | 1.00 (105/turn) | grain 18 (3->6.17), bread 33 (2.48->4.43), firewood 7 (2.18->12.73), timber 4 (7.56->14.44) | cloth 1 (7.56->10.3), garments 0 (24.36->27.2), fleece 0 (8.14->9.12) | +158 |

**Best:** Brebronn at about +259 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 29.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 24 @ ?, stop 77 |  | uses 19.2/turn (household upkeep, mansion 1), makes 0.0, holds 68 = 3.5 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 83.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 7 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 22 = 3.7 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 14 |  | goal planner: buys 4 a turn for today's rates, keeps up to 14 (v2 had 7) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 15.8, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 25.8) |
| grain | 18 @ 3.7, stop 36 |  | uses 9.0/turn (observed), makes 0.0, holds 6 = 0.7 turns |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 71) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 41.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 84.5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.8k (cash + stock at home prices); +1/turn over 6 turns, -96/turn over 24 turns.
- Limits: cash flow >= -396/turn, prestige >= -1.09/turn (values are after 200 tax a turn).
- Today's settings: value -110/turn, cash -116/turn, prestige +1.40/turn.
- Plan: value +57/turn, cash +62/turn, prestige -1.09/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -238 vs -174, -368 vs -114, -100 vs -123.
- Route sales counted at most (what the ships really sold, a turn): beer 2.0, rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Gottweiler: -3/turn
  - ship Flax Wyrm -> Kleinburgh: +12/turn
  - mansion 1 1.00 -> 0.41: +134/turn
  - net maker 0.00 -> 0.24: +8/turn
  - spinnery 1 1.65 -> 1.51: +4/turn
  - flax farm 1 4.64 -> 4.47: -1/turn
  - brewery 1 0.14 -> 0.00: -2/turn
  - brewery 1 [brew mead 1] 0.00 -> 0.12: +15/turn
  - sewing shop 1 0.30 -> 0.36: -11/turn
  - weavery 1 0.50 -> 0.60: +14/turn
- Model check over the last 59 turns: predicted -157/turn for the settings we ran, real +49/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.65, thread 4.15, cloth 6.62, flax fibres 4.92, garments 19.16, nets 33.60, beer 2.56, timber 3.24, prestige 55.24, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 7); furniture buy 2 (v2 None); garments sell 11 (v2 10); labour buy 64 (v2 71); light armour buy 1 (v2 None)
- Recipe: brewery 1 brew beer 1 -> brew mead 1 at 0.12, worth +15/turn.
- Ship linen snake: Grandgues -> Gottweiler (+1/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Kleinburgh (+12/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +82/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

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

Buffers: flax fibres 85/77, thread 1050/228, cloth 72/128

## Self-diagnosis

- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
