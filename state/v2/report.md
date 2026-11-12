# v2 shadow report

Turn 13969, 2026-11-12 10:46. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,286, prestige 3,549 (429 free, -2.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 0 | 0 | 0 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 36 | 0 | 2 | 0 | 0 | min_holding 30, sell 10, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 21, buy 6, buy @ 3.7 |
| labour | 29 | 29 | 500 | 0 | 29 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **labour**: 29 labour expired last turn (~48 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 511, not 611

## Prestige spending, cheapest coin per prestige first

432 turns left: prestige gained now converts 88.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.9 | 48.9 | running |
| hold banquet 4 (pies) | mansion | 18 | 54.7 | 54.7 | thin at home: pasties, ham, stockfish, glassware |
| jousting 3 | arena | 230 | 55.0 | 55.3 | needs a arena (build cost 25,796); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 57.4 | 57.4 |  |
| hold banquet 4 | mansion | 17.5 | 57.5 | 57.5 | thin at home: ham, stockfish, glassware |
| hold banquet 2 (pies) | mansion | 7 | 58.7 | 58.7 | thin at home: pasties |
| hold banquet 3 (pies) | mansion | 8 | 59.1 | 59.1 | thin at home: pasties |
| hold banquet 2 (fish) | mansion | 6.8 | 59.3 | 59.3 | thin at home: cured fish |
| hold banquet 4 (premium) | mansion | 20 | 60.1 | 60.1 | thin at home: ham, stockfish, glassware |
| jousting 2 | arena | 210 | 60.3 | 60.6 | needs a arena (build cost 25,796); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 60.7 | 60.7 | thin at home: cured fish |
| hold prayer 2 | chapel | 13 | 59.7 | 66.5 | needs a chapel (build cost 32,741); thin at home: furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 2 @ 13.3, pasties buy 5 @ 14.0; crew 0.1; est +40 a turn; stock: furniture 2 @ 13.3 (keep 145); stock: pasties 5 @ 14.0 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 5 @ 15.5 (keep 14); best orders clear only 7 a turn after crew: ship stays at 0
- best towns now: Amsdermund +42, Caillechâtel +40, Friedwerp +39, Donaunieder +37, Essenbrucke +36
- Amsdermund would trade: furniture buy 2 @ 13.7, pasties buy 5 @ 13.6; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~104 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Darmwald | 1022 | 0.34 | 0.80 (83/turn) | beer 101 (3.89->5.18), garments 10 (18.81->23.18), malt 1 (7.4->14.25), arms 2 (35.49->37.05) | cloth 14 (7.35->10.5), jewellery 1 (118.65->151.05), cured meat 3 (22.05->24.13), butter 1 (80.33->81.7) | +187 |
| Amsdermund | 1111 | 0.39 | 0.30 (31/turn) | cured fish 7 (24.57->30.59), garments 10 (18.81->20.52), nets 5 (37.4->40.09), honey 8 (10.29->11.59) | cloth 24 (7.56->10.5), jewellery 1 (115.5->151.05), flax fibres 12 (5.78->7.85), tools 14 (5.17->6.03) | +186 |
| Kirchwerp | 1072 | 0.37 | 0.40 (41/turn) | garments 10 (18.81->20.33), honey 6 (10.29->12.06) | cloth 24 (7.56->10.5), flax fibres 25 (5.78->7.85), jewellery 1 (120.75->151.05), tools 14 (4.62->6.03) | +168 |
| Chribruck | 1202 | 0.45 | 0.20 (21/turn) | tapestries 1 (735->802.75), windows 1 (766.5->831.25), garments 10 (18.81->22.04), wine 5 (6.98->8.07) | cloth 7 (9.13->10.5), candles 1 (87.15->88.5) | +161 |
| Blanans | 297 | 0.08 | 0.60 (62/turn) | timber 37 (7.56->9.97), limestone 2 (17.22->31.92), garments 10 (18.81->20.71), canvas 4 (43.26->43.7) | jewellery 1 (113.4->151.05), cloth 13 (7.93->10.5), flax plants 6 (1.54->2.28), flax fibres 3 (7.14->7.85) | +157 |

**Best:** Darmwald at about +187 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 35.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.14 | goal planner: sells 2 a turn at 1.14, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 22.8) |
| grain | 6 @ 3.7, stop 21 |  | goal planner: buys 6 a turn for today's rates, keeps up to 21 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 11) |
| light armour | 1 @ 109, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 36.4) |
| pasties |  | 1 @ min 12.9 | goal planner: trial sale of an idle pile, 1 a turn at 12.9, keeps 0 (9 over) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 78.5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 1 = 3.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.3k (cash + stock at home prices); +343/turn over 6 turns, -34/turn over 24 turns.
- Limits: cash flow >= -345/turn, prestige >= -0.54/turn (values are after 200 tax a turn).
- Today's settings: value +36/turn, cash -8/turn, prestige -2.86/turn - breaks the prestige floor.
- Plan: value -66/turn, cash -63/turn, prestige -0.54/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +848 vs +86, +718 vs +41, +366 vs -12.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Cobholme: +6/turn
  - net maker 0.00 -> 0.29: +7/turn
  - spinnery 1 1.65 -> 1.41: +2/turn
  - ropewalk 1 0.25 -> 0.00: +9/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.14: +7/turn
  - flax farm 1 4.64 -> 4.34: -4/turn
  - weavery 1 0.50 -> 0.59: -10/turn
  - sewing shop 1 0.30 -> 0.36: +12/turn
  - mansion 1 0.00 -> 0.55: -139/turn
- Model check over the last 61 turns: predicted +106/turn for the settings we ran, real +11/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.63, thread 4.10, cloth 6.54, flax fibres 4.86, garments 18.93, nets 29.59, beer 3.04, timber 3.24, prestige 65.02, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax plants sell 2 (v2 none); garments sell 11 (v2 10); grain buy 6 (v2 0); labour buy 29 (v2 11); light armour buy 1 (v2 None); pasties sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.14, worth +6/turn.
- Ship linen snake: Grandgues -> Cobholme (+5/turn over staying).
- Ship Flax Wyrm: stays on Caillechâtel (worth +2/turn).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +81/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1894 coin: +2/turn, payback 919 turns, doesn't pay yet

## Chain sizing

Mode HOLD, garments sold 10.0/turn (+0.0 exported); plan makes 32.4 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 407 (+117 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 3.63 |
| ret | 3 | 0.91 | 0.73 |
| spin | 4 | 1.65 | 1.67 |
| weave | 3 | 0.50 | 1.27 |
| sew | 2 | 0.30 | 0.79 |

Buffers: flax fibres 155/77, thread 1050/227, cloth 72/127

## Self-diagnosis

- R1: beer slot dry: 0.0 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy none, home ask 3.7 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 9 @ 3.76 (ask 3.7, cap 5.7))
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
