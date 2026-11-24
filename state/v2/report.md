# v2 shadow report

Turn 14265, 2026-11-24 18:27. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,476, prestige 3,716 (596 free, +1.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 53 | 0 | 19 | 0 | 0 | sell 3, sell @ 3.32; stop 116, buy 39, buy @ 3.42 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 14 | 4 | 4 | 0 | 0 | stop 14, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 35 | 9 | 9 | 0 | 0 | stop 36, buy 10, buy @ 3.7 |
| labour | 64 | 64 | 555 | 0 | 9 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**0 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Tuning

- **cured meat**: home ask 29.20 is above our ceiling 29.00 and last turn bought 0 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 56.9 coin per prestige at mansion, vs 69.0 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **hold banquet 2 (fish)**: hold banquet 2 (fish) costs 57.6 coin per prestige at mansion, vs 69.0 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch

## Notes

- labour: projection runs 110 over real use lately; planning 559, not 669

## Prestige spending, cheapest coin per prestige first

136 turns left: prestige gained now converts 49.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 54.3 | 54.3 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 56.9 | 56.9 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 57.6 | 57.6 |  |
| jousting 3 | arena | 230 | 57.8 | 59.2 | needs a arena (build cost 28,341); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 59.6 | 59.6 |  |
| hold banquet 4 (pies) | mansion | 18 | 62.8 | 62.8 | thin at home: hop beer, stockfish |
| hold banquet 5 | mansion | 22 | 64.5 | 64.5 | thin at home: hop beer, stockfish, sculptures |
| jousting 2 | arena | 210 | 63.3 | 64.9 | needs a arena (build cost 28,341); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 66.1 | 66.1 | thin at home: hop beer, stockfish |
| hold banquet 4 | mansion | 17.5 | 66.4 | 66.4 | thin at home: hop beer, stockfish |
| hold banquet 2 (meat) | mansion | 6.8 | 67.0 | 67.0 |  |
| hold banquet 1 (meat) | mansion | 4.2 | 69.0 | 69.0 | running |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 11 | 151802239 | 0 | - | cured meat 6, pasties 1 | -154 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: cured meat buy 6 @ 24.6, pasties buy 1 @ 16.4; crew 0.1; est +19 a turn; stock: pasties 1 @ 16.4 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 11.5 (keep 14); best orders clear only 9 a turn after crew: ship stays at 0
- best towns now: Dortdorf +42, Darmwald +39, Donaunieder +38, Bremcop +32, Heidlowe +29
- Dortdorf would trade: cured meat buy 6 @ 21.2, pasties buy 1 @ 14.3; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~114 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Vauxvais | 204 | 0.06 | 0.20 (23/turn) | windows 1 (1018.5->1453.5), limestone 4 (20.48->34.39), salt 6 (5.25->6.93), wax 2 (31.71->33.06) | thread 22 (5.46->6.05), cured meat 3 (26.46->29.2), bricks 5 (4.85->7.55), seeds 5 (1.94->3.23) | +538 |
| Amsdermund | 1111 | 0.43 | 0.40 (45/turn) | medicine 1 (144.9->161.5), flour 2 (19.64->25.46), casks 10 (6.51->7.69), pies 1 (19.95->23.75) | cloth 24 (7.77->10), thread 23 (4.37->6.05), leather 3 (22.68->30.4), cured meat 6 (25.2->29.2) | +156 |
| Hofkirchen | 991 | 0.36 | 0.50 (57/turn) | wheels 4 (25.41->37.05), garments 10 (28.4->32.87), canvas 5 (42.21->43.89), flour 2 (19.64->24.13) | cured meat 6 (25.62->29.2), tools 17 (5.25->6.13), thread 62 (5.57->6.05), flax fibres 24 (5.62->6.6) | +152 |
| Rotterburg | 1056 | 0.40 | 0.20 (23/turn) | yarn 18 (6.51->9.31), garments 10 (28.4->29.45), nets 4 (35.6->36.86), dyed yarn 2 (6.93->7.36) | cloth 24 (6.93->10), cured meat 5 (24.36->29.2) | +136 |
| Hanstein | 380 | 0.12 | 0.50 (57/turn) | timber 19 (7.98->13.87), nets 4 (35.6->38), charcoal 17 (2.12->3.17), firewood 1 (2.02->5.75) | cured meat 5 (23.31->29.2), cloth 5 (8.14->10), thread 12 (5.46->6.05), seeds 4 (2.25->3.23) | +136 |

**Best:** Vauxvais at about +538 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 5 @ min 3.38 | makes 19.3, uses 19.2, holds 53 (keeps 0): sells the surplus + 4/turn of the excess |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 87, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 9 = 1.6 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 0.96 | goal planner: sells 2 a turn at 0.96, keeps 219 (no one offered it) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 27.6) |
| grain | 8 @ 3.7, stop 29 |  | goal planner: buys 8 a turn for today's rates, keeps up to 29 (v2 had 10) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 59) |
| light armour | 1 @ 99.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.6) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 85.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.4k (cash + stock at home prices); -4/turn over 6 turns, -49/turn over 24 turns.
- Limits: cash flow >= -312/turn, prestige >= -1.23/turn (values are after 200 tax a turn).
- Today's settings: value -153/turn, cash -151/turn, prestige +1.23/turn.
- Plan: value +22/turn, cash +30/turn, prestige -1.23/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -153 vs -143, -22 vs -146, -64 vs -148.
- Route sales counted at most (what the ships really sold, a turn): beer 2.2, rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Dortdorf: +19/turn
  - ship Flax Wyrm -> Nürnnieder: +2/turn
  - mansion 1 1.00 -> 0.41: +156/turn
  - spinnery 1 1.65 -> 1.32: -1/turn
  - retting pit 1 0.91 -> 0.79: +1/turn
  - flax farm 1 4.64 -> 3.55: +12/turn
- Model check over the last 59 turns: predicted -149/turn for the settings we ran, real -4/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.38, garments 21.00, nets 33.60, beer 3.26, timber 3.42, prestige 63.59, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 5); flax plants sell 2 (v2 none); garments sell 11 (v2 10); grain buy 8 (v2 10); labour buy 64 (v2 59); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Dortdorf (+7/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Nürnnieder (+2/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +85/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new chandlery (make candles 2) for ~5019 coin: +3/turn, payback 1438 turns, doesn't pay yet (materials thin at home: bricks, nails)

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

Buffers: flax fibres 85/77, thread 1050/228, cloth 73/128

## Self-diagnosis

- R1: cured meat slot dry: 9.3 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 3 @ 29, home ask 29.2 -> **buy 12 @ 29.8 (ask 29.2, cap 42.0)** (ok)
- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
