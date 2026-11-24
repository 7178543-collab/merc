# v2 shadow report

Turn 14259, 2026-11-24 12:18. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,448, prestige 3,708 (588 free, +1.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 53 | 0 | 19 | 0 | 0 | sell 5, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 13 | 4 | 4 | 0 | 0 | stop 14, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 35 | 14 | 9 | 0 | 0 | stop 36, buy 12, buy @ 3.7 |
| labour | 64 | 64 | 564 | 5 | 0 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**0 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Tuning

- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 57.5 coin per prestige at mansion, vs 67.9 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **hold banquet 2 (fish)**: hold banquet 2 (fish) costs 55.3 coin per prestige at mansion, vs 67.9 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 110 over real use lately; planning 569, not 655

## Prestige spending, cheapest coin per prestige first

142 turns left: prestige gained now converts 51.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 54.0 | 54.0 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 55.3 | 55.3 |  |
| hold banquet 1 (fish) | mansion | 4.2 | 57.5 | 57.5 |  |
| hold banquet 2 (pies) | mansion | 7 | 59.1 | 59.1 |  |
| jousting 3 | arena | 230 | 58.1 | 59.4 | needs a arena (build cost 27,521); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 62.6 | 62.6 | thin at home: hop beer, stockfish |
| hold banquet 2 (meat) | mansion | 6.8 | 63.2 | 63.2 |  |
| hold banquet 5 | mansion | 22 | 64.2 | 64.2 | thin at home: hop beer, stockfish, sculptures |
| jousting 2 | arena | 210 | 63.6 | 65.0 | needs a arena (build cost 27,521); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 65.8 | 65.8 | thin at home: hop beer, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 66.2 | 66.2 | thin at home: hop beer, stockfish, premium cheese |
| hold banquet 1 (meat) | mansion | 4.2 | 67.9 | 67.9 | running |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 11 | 151802239 | 0 | - | bread 2, cured meat 6, grain 1, pasties 2 | -172 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: bread buy 4 @ 1.45, cured meat buy 6 @ 24.6, grain buy 8 @ 2.18; crew 0.1; est +19 a turn
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 11.9 (keep 14); best orders clear only 6 a turn after crew: ship stays at 0
- best towns now: Donaunieder +33, Darmwald +30, Birkeningen +28, Orlesailles +26, Brebronn +24
- Donaunieder would trade: cured meat buy 6 @ 22.4, pasties buy 1 @ 12.1; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~115 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.36 | 0.40 (46/turn) | jewellery 3 (86.62->114), garments 10 (26.4->32.3), nets 6 (35.4->39.33), glass ingots 1 (69.3->82.17) | cloth 21 (7.35->11.8), tools 57 (5.25->7.12), dyed cloth 8 (11.55->14.91), cured meat 6 (25.41->28.6) | +417 |
| Chatgnan | 728 | 0.22 | 0.20 (23/turn) | garments 10 (26.4->26.98), copper ingots 4 (18.27->18.9) | sculptures 1 (2394->2717), tools 23 (5.93->7.12), cloth 8 (10.24->11.8), tin ingots 1 (31.71->35.72) | +353 |
| Pontmont | 341 | 0.10 | 0.60 (69/turn) | timber 25 (8.45->13.21), cured fish 8 (24.36->27.36), furniture 15 (14.91->16.53), resin 3 (4.22->8.03) | tools 57 (5.72->7.12), tin ingots 2 (27.3->35.72), thread 22 (5.46->6.05), bricks 8 (5.25->8.22) | +262 |
| Amsdermund | 1111 | 0.44 | 0.50 (58/turn) | nets 6 (35.4->39.9), gears 2 (88.2->95), furniture 15 (14.91->17.1), chisels 1 (11.45->17.1) | cloth 24 (7.35->11.8), dyed cloth 8 (9.97->14.91), cookware 5 (22.05->28.5), cured meat 6 (26.46->28.6) | +229 |
| Heilegg | 826 | 0.26 | 0.70 (81/turn) | garments 10 (26.4->33.82), cured fish 9 (24.36->28.88), charcoal 16 (1.93->5.27), nets 6 (35.4->38.95) | tools 57 (6.46->7.12), cured meat 6 (27.72->28.6) | +218 |

**Best:** Hofkirchen at about +417 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 4 @ min 3.88 | goal planner: sells 4 at 3.88 (v2 had 4 at 4.06) |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| candles | 2 @ 82, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 11 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 14 = 2.4 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 14 |  | goal planner: buys 4 a turn for today's rates, keeps up to 14 (v2 had 6) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 14.5, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 25.8) |
| grain | 10 @ 3.7, stop 36 |  | uses 9.0/turn (brewery 1), makes 0.0, holds 35 = 3.9 turns |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 69) |
| light armour | 1 @ 95, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 85.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.4k (cash + stock at home prices); -182/turn over 6 turns, -33/turn over 24 turns.
- Limits: cash flow >= -310/turn, prestige >= -1.20/turn (values are after 200 tax a turn).
- Today's settings: value -144/turn, cash -145/turn, prestige +1.27/turn.
- Plan: value +31/turn, cash +36/turn, prestige -1.20/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -75 vs -133, +82 vs -156, -177 vs -143.
- Route sales counted at most (what the ships really sold, a turn): beer 2.2, rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Birkeningen: +4/turn
  - ship Flax Wyrm -> Grandgues: +4/turn
  - mansion 1 1.00 -> 0.41: +148/turn
  - spinnery 1 1.65 -> 1.40: +1/turn
  - retting pit 1 0.91 -> 0.83: +1/turn
  - flax farm 1 4.64 -> 3.37: +11/turn
  - weavery 1 0.50 -> 0.58: -9/turn
  - sewing shop 1 0.30 -> 0.36: +9/turn
- Model check over the last 59 turns: predicted -153/turn for the settings we ran, real -1/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.80, thread 4.56, cloth 7.26, flax fibres 5.47, garments 20.97, nets 33.60, beer 3.01, timber 3.58, prestige 62.60, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 6); furniture buy 2 (v2 None); garments sell 11 (v2 10); labour buy 64 (v2 69); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Birkeningen (+1/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Grandgues (+3/turn over staying).
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

Buffers: flax fibres 87/77, thread 1060/228, cloth 73/128

## Self-diagnosis

- R2: spinnery 1 blocked by thread space: 1060 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
