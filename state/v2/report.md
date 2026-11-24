# v2 shadow report

Turn 14269, 2026-11-24 22:50. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,826, prestige 3,719 (599 free, +0.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 40 | 0 | 18 | 0 | 0 | sell 4, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 14 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 28 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 564 | 10 | 0 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**1 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **labour**: buying 64, short of ~74 needed -> v2: buy 74

## Tuning

- **bread**: home ask 2.82 is above our ceiling 2.60 and last turn bought 0 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 60.2 coin per prestige at mansion, vs 71.8 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch

## Notes

- labour: projection runs 114 over real use lately; planning 574, not 654

## Prestige spending, cheapest coin per prestige first

132 turns left: prestige gained now converts 48.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 47.1 | 48.0 | needs a arena (build cost 30,438); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 50.7 | 51.6 | needs a arena (build cost 30,438); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 56.4 | 56.4 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 57.6 | 57.6 | thin at home: cheese |
| maintain 2 | park | 2 | 57.8 | 57.8 | thin at home: sculptures |
| hold banquet 2 (pies) | mansion | 7 | 58.7 | 58.7 | thin at home: cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 60.2 | 60.2 |  |
| hold banquet 5 | mansion | 22 | 60.5 | 60.5 | thin at home: hop beer, stockfish, sculptures |
| jousting 3 | arena | 230 | 59.3 | 60.9 | needs a arena (build cost 30,438); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 63.1 | 63.1 | thin at home: hop beer, stockfish |
| hold banquet 2 (meat) | mansion | 6.8 | 66.6 | 66.6 | thin at home: cured meat, cheese |
| jousting 2 | arena | 210 | 64.9 | 66.6 | needs a arena (build cost 30,438); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 11 | 134102075 | 0 | - | cured meat 6, pasties 1 | -179 |
| linen snake | 0.1 / 0.10 | 11 | 151802239 | 0 | beer 4 | cured meat 6 | -152 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 13.3 (keep 14); best orders clear only 1 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only 3 a turn after crew: ship stays at 0
- best towns now: Donaunieder +32, Darmwald +30, Rotterburg +28, Cobholme +28, Hanstein +26
- Donaunieder would trade: cured meat buy 5 @ 22.0, pasties buy 1 @ 14.3; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~116 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Kirchwerp | 1072 | 0.42 | 0.40 (46/turn) | glass ingots 2 (70.88->114), garments 10 (28.8->36.1), canvas 4 (42.63->47.5), tar 9 (10.71->12.35) | tin ingots 5 (33.39->35.91), windows 1 (1071->1083), slaked lime 1 (8.4->17.95), nails 6 (6.09->6.93) | +225 |
| Fulkirch | 1576 | 0.73 | 0.70 (81/turn) | thread 90 (5.85->7.03), nets 6 (34.6->38), glass ingots 2 (70.88->75.52) | windows 3 (1039.5->1083), tin ingots 5 (31.5->35.91), cured meat 5 (25.83->29.6), slaked lime 1 (8.98->17.95) | +219 |
| Bremcop | 1326 | 0.57 | 0.30 (35/turn) | garments 10 (28.8->29.83), nets 1 (34.6->36.48) | windows 2 (1002.75->1083), cured meat 5 (23.52->29.6), yarn 30 (5.46->6.37), slaked lime 1 (10.13->17.95) | +202 |
| Pontmont | 341 | 0.11 | 0.60 (70/turn) | timber 37 (8.4->13.21), clay 1 (3.74->11.97), nails 9 (7.77->8.22) | tools 16 (5.25->6.51), thread 24 (5.25->5.95), slaked lime 1 (6.83->17.95), bricks 6 (5.25->8.12) | +174 |
| Brunnham | 1281 | 0.55 | 0.40 (46/turn) | garments 10 (28.8->31.73), nets 6 (34.6->38), dyed cloth 14 (17.75->19.19), wine 41 (6.56->7.17) | windows 2 (1050->1083), tin ingots 4 (31.5->35.91), cookware 5 (21->24.13), cured meat 5 (26.04->29.6) | +173 |

**Best:** Kirchwerp at about +225 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 3 @ min 3.96 | makes 19.3, uses 19.2, holds 40 (keeps 0): sells the surplus + 3/turn of the excess |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 9) |
| candles | 2 @ 90.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 8 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 21 = 3.6 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 0.96 | goal planner: sells 2 a turn at 0.96, keeps 219 (no one offered it) |
| furniture | 2 @ 16, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 28.0) |
| grain | 9 @ 3.7, stop 36 |  | goal planner: buys 9 a turn for today's rates, keeps up to 36 (v2 had 14) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 74) |
| light armour | 1 @ 101, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 85.5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.1k (cash + stock at home prices); -37/turn over 6 turns, -46/turn over 24 turns.
- Limits: cash flow >= -284/turn, prestige >= -1.25/turn (values are after 200 tax a turn).
- Today's settings: value -184/turn, cash -175/turn, prestige +1.21/turn.
- Plan: value +6/turn, cash +22/turn, prestige -1.25/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -336 vs -156, -155 vs -174, -283 vs -186.
- Route sales counted at most (what the ships really sold, a turn): beer 2.2, rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Nürnnieder: +14/turn
  - ship Flax Wyrm -> Fontaux: +13/turn
  - mansion 1 1.00 -> 0.41: +170/turn
  - net maker 0.00 -> 0.28: +7/turn
  - flax farm 1 4.64 -> 4.00: -0/turn
  - retting pit 1 0.91 -> 0.80: +1/turn
  - spinnery 1 1.65 -> 1.34: +7/turn
  - weavery 1 0.50 -> 0.40: -6/turn
  - sewing shop 1 0.30 -> 0.25: +12/turn
- Model check over the last 59 turns: predicted -147/turn for the settings we ran, real -33/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.38, garments 21.00, nets 33.30, beer 3.19, timber 3.42, prestige 67.16, cash 0.00
- Orders it would set: bread buy 5 (v2 9); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 5); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 14); labour buy 64 (v2 74); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Nürnnieder (+12/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Fontaux (+1/turn over staying).
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

Buffers: flax fibres 86/77, thread 1064/228, cloth 72/128

## Self-diagnosis

- R1: bread slot dry: 8.0 held, 4.2 a turn (basic food slot (+0.3 prestige)); our buy 5 @ 2.6, home ask 2.82 -> **buy 9 @ 2.88 (ask 2.82, cap 4.3)** (ok)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
