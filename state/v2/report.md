# v2 shadow report

Turn 14268, 2026-11-24 21:44. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,109, prestige 3,718 (598 free, +1.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 47 | 0 | 19 | 0 | 0 | sell 19, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 14 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 27 | 8 | 9 | 0 | 0 | stop 33, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 553 | 0 | 11 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**0 risks, 0 waste, 5 tuning** where v2 would act differently from v1.

## Tuning

- **bread**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **cured meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 58.2 coin per prestige at mansion, vs 73.0 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 114 over real use lately; planning 555, not 669

## Prestige spending, cheapest coin per prestige first

133 turns left: prestige gained now converts 48.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 50.2 | 51.1 | needs a arena (build cost 30,318); thin at home: protection, light armour, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 53.9 | 54.8 | needs a arena (build cost 30,318); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 55.2 | 55.2 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 58.0 | 58.0 | thin at home: cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 58.2 | 58.2 |  |
| hold banquet 2 (pies) | mansion | 7 | 58.8 | 58.8 | thin at home: cheese |
| jousting 3 | arena | 230 | 59.4 | 60.9 | needs a arena (build cost 30,318); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 63.5 | 63.5 | thin at home: hop beer, stockfish |
| jousting 2 | arena | 210 | 65.0 | 66.7 | needs a arena (build cost 30,318); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 67.2 | 67.2 | thin at home: hop beer, stockfish |
| hold banquet 4 | mansion | 17.5 | 67.3 | 67.3 | thin at home: hop beer, stockfish, cheese |
| hold banquet 3 (pies) | mansion | 8 | 69.3 | 69.3 | thin at home: hop beer, cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 11 | 134102075 | 0 | - | cured meat 4, pasties 1 | -122 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: beer sell 4 @ 4.36, cured meat buy 6 @ 27.0; crew 0.1; est +21 a turn
- **Flax Wyrm** on Caillechâtel: cured meat buy 6 @ 27.8, pasties buy 1 @ 13.3; crew 0.1; est +19 a turn; stock: pasties 1 @ 13.3 (keep 14)
- best towns now: Donaunieder +53, Corstoft +52, Darmwald +50, Hanstein +48, Birkeningen +47
- Donaunieder would trade: cured meat buy 6 @ 22.0, pasties buy 1 @ 14.2; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~115 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.36 | 0.20 (23/turn) | coats 6 (101.85->126.35), glass ingots 4 (70.35->77.42), medicine 1 (132.3->148.2), beer 4 (3.4->4.69) | tools 16 (5.25->6.27), gears 2 (96.6->100.7), hop beer 6 (13.02->14.72), slaked lime 1 (8.4->15.48) | +239 |
| Brunnham | 1281 | 0.54 | 0.40 (46/turn) | nets 6 (34.2->38), medicine 1 (132.3->145.35), garments 10 (28.8->30.59), dyed cloth 13 (17.85->19.19) | windows 1 (1050->1140), tin ingots 5 (31.5->35.91), cookware 5 (21->24.13), wax 9 (27.93->29.26) | +183 |
| Pontmont | 341 | 0.10 | 0.60 (69/turn) | timber 36 (8.4->13.11), nails 9 (7.67->9.5), clay 1 (3.57->11.97), beer 4 (3.4->3.84) | thread 24 (5.25->6), tools 16 (5.25->6.27), slaked lime 1 (6.83->15.48), bricks 6 (5.25->7.98) | +181 |
| Heilegg | 826 | 0.26 | 0.40 (46/turn) | nets 6 (34.2->42.18), dyed cloth 13 (17.85->19.57), wine 16 (6.62->7.84), beer 4 (3.4->5.84) | windows 1 (1102.5->1140), coats 6 (86.1->90.72), slaked lime 1 (9.35->15.48), cured meat 1 (26.04->30.21) | +177 |
| Fulkirch | 1576 | 0.72 | 0.40 (46/turn) | glass ingots 4 (70.35->75.52), nets 6 (34.2->37.81), thread 28 (5.85->7.03) | windows 1 (1050->1140), tin ingots 3 (31.5->35.91), gears 2 (96.08->100.7), slaked lime 1 (9.03->15.48) | +155 |

**Best:** Hofkirchen at about +239 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 4 @ min 3.38 | makes 19.3, uses 19.2, holds 47 (keeps 0): sells the surplus + 4/turn of the excess |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 7) |
| candles | 2 @ 90, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 11 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 14 = 2.3 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 0.96 | goal planner: sells 2 a turn at 0.96, keeps 219 (no one offered it) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 28.0) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 14) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 55) |
| light armour | 1 @ 102, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 86.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.2k (cash + stock at home prices); -20/turn over 6 turns, -51/turn over 24 turns.
- Limits: cash flow >= -296/turn, prestige >= -1.24/turn (values are after 200 tax a turn).
- Today's settings: value -181/turn, cash -186/turn, prestige +1.22/turn.
- Plan: value +6/turn, cash +13/turn, prestige -1.24/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +124 vs -151, -336 vs -156, -155 vs -174.
- Route sales counted at most (what the ships really sold, a turn): beer 2.2, rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Donaunieder: +26/turn
  - ship Flax Wyrm -> Grandgues: +1/turn
  - mansion 1 1.00 -> 0.41: +167/turn
  - net maker 0.00 -> 0.29: +8/turn
  - flax farm 1 4.64 -> 3.96: -2/turn
  - retting pit 1 0.91 -> 0.79: +1/turn
  - spinnery 1 1.65 -> 1.34: +5/turn
  - weavery 1 0.50 -> 0.41: -6/turn
- Model check over the last 59 turns: predicted -147/turn for the settings we ran, real -24/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.38, garments 21.00, nets 33.11, beer 3.14, timber 4.09, prestige 66.75, cash 0.00
- Orders it would set: bread buy 5 (v2 7); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 5); flax plants sell 2 (v2 none); garments sell 11 (v2 10); grain buy 9 (v2 14); labour buy 64 (v2 55); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Donaunieder (+10/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Grandgues (+1/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

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

Buffers: flax fibres 87/77, thread 1050/228, cloth 72/128

## Self-diagnosis

- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
