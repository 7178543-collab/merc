# v2 shadow report

Turn 14257, 2026-11-24 10:06. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,543, prestige 3,706 (586 free, +1.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 62 | 0 | 19 | 0 | 0 | sell 6, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 13 | 4 | 4 | 0 | 0 | stop 14, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 26 | 0 | 9 | 0 | 0 | stop 36, buy 18, buy @ 3.7 |
| labour | 64 | 64 | 557 | 0 | 7 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**1 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 9.80 x11, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Tuning

- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 55.6 coin per prestige at mansion, vs 66.2 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **hold banquet 2 (fish)**: hold banquet 2 (fish) costs 56.1 coin per prestige at mansion, vs 66.2 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch

## Notes

- labour: projection runs 116 over real use lately; planning 557, not 664

## Prestige spending, cheapest coin per prestige first

144 turns left: prestige gained now converts 51.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 54.0 | 54.0 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 55.6 | 55.6 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 56.1 | 56.1 |  |
| jousting 3 | arena | 230 | 57.0 | 58.2 | needs a arena (build cost 27,401); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 59.5 | 59.5 | thin at home: pies |
| hold banquet 4 (pies) | mansion | 18 | 63.0 | 63.0 | thin at home: hop beer, stockfish |
| jousting 2 | arena | 210 | 62.4 | 63.8 | needs a arena (build cost 27,401); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 64.3 | 64.3 |  |
| hold banquet 5 | mansion | 22 | 64.4 | 64.4 | thin at home: hop beer, stockfish, sculptures |
| hold banquet 1 (meat) | mansion | 4.2 | 66.2 | 66.2 | running |
| hold banquet 4 | mansion | 17.5 | 66.4 | 66.4 | thin at home: hop beer, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 66.6 | 66.6 | thin at home: hop beer, stockfish, premium cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 10 | 134102075 | 0 | - | pasties 1 | -13 |
| linen snake | 0.1 / 0.10 | 10 | 151802239 | 0 | - | cured meat 6 | -141 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 12.6 (keep 14); best orders clear only -5 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 15.6 (keep 14); best orders clear only 15 a turn after crew: ship stays at 0
- best towns now: Donaunieder +26, Fontaux +18, Helmgreen +18, Orlesailles +18, Rotterburg +16
- Donaunieder would trade: cured meat buy 6 @ 22.4, pasties buy 1 @ 12.5; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~115 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Heilegg | 826 | 0.26 | 0.80 (92/turn) | coats 7 (95.55->114), gears 2 (88.2->142.5), garments 10 (27.2->34.77), nets 4 (35.8->43.51) | tools 16 (6.46->7.93), wool 16 (10.13->11.59), slaked lime 1 (6.62->14.54) | +507 |
| Kirchwerp | 1072 | 0.41 | 0.60 (69/turn) | garments 10 (27.2->38), belts 12 (35.7->38.38), gears 2 (88.2->92.62), tar 11 (10.29->11.49) | cloth 24 (7.77->11.2), cookware 5 (21->26.79), tools 16 (6.67->7.93), slaked lime 1 (8.4->14.54) | +265 |
| Bedenis | 566 | 0.17 | 0.50 (57/turn) | garments 10 (27.2->37.43), cloth 13 (11.76->17.1), nets 3 (35.8->38.38), clay 1 (3.74->11.97) | tools 16 (5.62->7.93), thread 18 (5.46->6.05), slaked lime 1 (8.98->14.54), casks 3 (4.77->5.84) | +230 |
| Hofkirchen | 991 | 0.36 | 0.30 (34/turn) | furniture 6 (13.65->18.62), nets 6 (35.8->39.33), resin 3 (4.2->8.22), glass ingots 1 (68.78->74.1) | cloth 20 (7.35->11.2), tools 16 (5.04->7.93), cookware 5 (24.78->26.79), cured meat 6 (25.41->27.4) | +219 |
| Vauxvais | 204 | 0.06 | 0.30 (34/turn) | bread 157 (2.56->3.32), beer 5 (3.36->4.75), garments 10 (27.2->27.55), flax fibres 2 (5.17->5.42) | bricks 17 (4.83->8.84), tools 16 (5.46->7.93), cured meat 4 (24.57->27.4), slaked lime 1 (8.93->14.54) | +213 |

**Best:** Heilegg at about +507 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 5 @ min 3.34 | goal planner: sells 5 at 3.34 (v2 had 5 at 3.38) |
| candles | 2 @ 91, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 10 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 17 = 2.9 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 14 |  | goal planner: buys 4 a turn for today's rates, keeps up to 14 (v2 had 6) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 13.3, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 26.4) |
| grain | 14 @ 3.7, stop 36 |  | uses 9.0/turn (brewery 1), makes 0.0, holds 26 = 2.9 turns |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 57) |
| light armour | 1 @ 95, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.6k (cash + stock at home prices); -148/turn over 6 turns, -30/turn over 24 turns.
- Limits: cash flow >= -314/turn, prestige >= -1.19/turn (values are after 200 tax a turn).
- Today's settings: value -154/turn, cash -156/turn, prestige +1.28/turn.
- Plan: value +21/turn, cash +27/turn, prestige -1.19/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -20 vs -137, -259 vs -146, -75 vs -133.
- Route sales counted at most (what the ships really sold, a turn): beer 2.2, rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Angefont: +7/turn
  - ship Flax Wyrm -> Donaunieder: +14/turn
  - mansion 1 1.00 -> 0.41: +146/turn
  - brewery 1 0.14 -> 0.08: +10/turn
  - spinnery 1 1.65 -> 1.36: +1/turn
  - retting pit 1 0.91 -> 0.81: +2/turn
  - flax farm 1 4.64 -> 2.98: -5/turn
- Model check over the last 58 turns: predicted -154/turn for the settings we ran, real +1/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.38, garments 21.00, nets 33.60, beer 3.05, timber 3.56, prestige 63.14, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 6); furniture buy 2 (v2 None); garments sell 11 (v2 10); labour buy 64 (v2 57); light armour buy 1 (v2 None); rope sell 1 (v2 none)
- Ship linen snake: Grandgues -> Angefont (+11/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Donaunieder (+5/turn over staying).
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

Buffers: flax fibres 88/77, thread 1057/228, cloth 73/128

## Self-diagnosis

- R2: spinnery 1 blocked by thread space: 1057 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
