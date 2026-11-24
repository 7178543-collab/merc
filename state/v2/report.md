# v2 shadow report

Turn 14264, 2026-11-24 17:21. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,540, prestige 3,714 (594 free, +1.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 37 | 0 | 19 | 0 | 0 | sell 3, sell @ 3.34 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 14 | 4 | 4 | 0 | 0 | stop 14, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 35 | 9 | 9 | 0 | 0 | stop 36, buy 10, buy @ 3.7 |
| labour | 64 | 64 | 564 | 5 | 0 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**0 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Tuning

- **cured meat**: home ask 29.20 is above our ceiling 29.00 and last turn bought 3 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 55.7 coin per prestige at mansion, vs 68.3 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch

## Notes

- labour: projection runs 110 over real use lately; planning 569, not 655

## Prestige spending, cheapest coin per prestige first

137 turns left: prestige gained now converts 49.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 53.7 | 53.7 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 55.7 | 55.7 |  |
| maintain 2 | park | 2 | 56.1 | 56.1 | thin at home: sculptures |
| hold banquet 2 (fish) | mansion | 6.8 | 57.0 | 57.0 | thin at home: wine |
| jousting 3 | arena | 230 | 57.6 | 59.0 | needs a arena (build cost 28,054); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 59.1 | 59.1 | thin at home: wine |
| hold banquet 5 | mansion | 22 | 59.4 | 59.4 | thin at home: hop beer, wine, stockfish, sculptures |
| hold banquet 4 (pies) | mansion | 18 | 62.0 | 62.0 | thin at home: hop beer, wine, stockfish |
| jousting 2 | arena | 210 | 63.1 | 64.6 | needs a arena (build cost 28,054); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 65.5 | 65.5 | thin at home: wine, hop beer, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 65.8 | 65.8 | thin at home: hop beer, wine, stockfish |
| hold banquet 2 (meat) | mansion | 6.8 | 66.9 | 66.9 | thin at home: wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 11 | 151802239 | 0 | - | cured meat 6, pasties 1 | -154 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: cured meat buy 6 @ 24.6, pasties buy 1 @ 16.4; crew 0.1; est +20 a turn; stock: pasties 1 @ 16.4 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 11.5 (keep 14); best orders clear only 9 a turn after crew: ship stays at 0
- best towns now: Donaunieder +34, Heidlowe +31, Darmwald +30, Bremcop +30, Dortdorf +28
- Donaunieder would trade: cured meat buy 6 @ 21.8; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~112 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Heilegg | 826 | 0.25 | 0.70 (78/turn) | wrought iron 10 (17.85->27.55), garments 10 (28.6->33.06), cloth 17 (10.34->12.16), yarn 27 (5.99->6.93) | paper 13 (25.2->26.03), cured meat 6 (28.35->29.2), tools 17 (5.88->6.27) | +226 |
| Hofkirchen | 991 | 0.35 | 0.50 (56/turn) | wheels 4 (25.2->37.05), garments 10 (28.6->32.87), nets 6 (35.6->39.33), ploughs 5 (82.42->88.35) | cured meat 6 (24.99->29.2), tools 17 (5.25->6.27), copper ingots 2 (15.96->18.81), fleece 8 (8.4->9.07) | +185 |
| Amsdermund | 1111 | 0.42 | 0.50 (56/turn) | medicine 1 (135.45->161.5), gears 2 (88.2->95), yarn 23 (5.99->6.74), pies 4 (20.89->23.75) | cloth 24 (7.72->9.85), thread 23 (4.41->6.05), cured meat 6 (25.41->29.2), leather 1 (22.68->29.64) | +176 |
| Pontmont | 341 | 0.10 | 0.60 (67/turn) | timber 37 (8.03->11.3), coats 4 (90.3->95.95), nets 3 (35.6->38), clay 1 (4.14->11.97) | thread 18 (5.25->6.05), cloth 10 (8.77->9.85), tools 17 (5.83->6.27), fleece 2 (7.61->9.07) | +141 |
| Grandgues | 152 | 0.04 | 0.20 (22/turn) | timber 25 (8.03->10.45), jewellery 3 (97.65->104.5), belts 1 (36.75->40.09), flax fibres 4 (6.35->6.65) | cured meat 6 (25.41->29.2), thread 50 (5.67->6.05), garments 2 (24.36->30), grain 8 (2.54->3.06) | +132 |

**Best:** Heilegg at about +226 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 3 @ min 3.32 | goal planner: sells 3 at 3.32 (v2 had 3 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 86, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 9 = 1.6 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 14 |  | goal planner: buys 4 a turn for today's rates, keeps up to 14 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 0.96 | goal planner: sells 2 a turn at 0.96, keeps 219 (no one offered it) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 27.8) |
| grain | 10 @ 3.7, stop 36 |  | uses 9.0/turn (brewery 1), makes 0.0, holds 35 = 3.9 turns |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 69) |
| light armour | 1 @ 99.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.6) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 85.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.4k (cash + stock at home prices); -4/turn over 6 turns, -49/turn over 24 turns.
- Limits: cash flow >= -314/turn, prestige >= -1.23/turn (values are after 200 tax a turn).
- Today's settings: value -148/turn, cash -148/turn, prestige +1.23/turn.
- Plan: value +26/turn, cash +32/turn, prestige -1.23/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +173 vs -138, -153 vs -143, -22 vs -146.
- Route sales counted at most (what the ships really sold, a turn): beer 2.2, rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Donaunieder: +13/turn
  - ship Flax Wyrm -> Nürnnieder: +1/turn
  - mansion 1 1.00 -> 0.41: +152/turn
  - spinnery 1 1.65 -> 1.32: -1/turn
  - retting pit 1 0.91 -> 0.80: +1/turn
  - flax farm 1 4.64 -> 3.54: +12/turn
- Model check over the last 59 turns: predicted -149/turn for the settings we ran, real -4/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.38, garments 21.00, nets 33.60, beer 3.16, timber 3.44, prestige 63.21, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 5); flax plants sell 2 (v2 none); garments sell 11 (v2 10); labour buy 64 (v2 69); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Donaunieder (+5/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Nürnnieder (+1/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +85/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new chandlery (make candles 2) for ~5034 coin: +1/turn, payback 3463 turns, doesn't pay yet (materials thin at home: bricks, nails)

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

- R1: beer slot dry: 37.2 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy none, home ask 3.36 -> **buy 39 @ 3.42 (ask 3.36, cap 14.4)** (ok)
- R2: spinnery 1 blocked by thread space: 1060 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
