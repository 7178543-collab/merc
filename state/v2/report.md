# v2 shadow report

Turn 14253, 2026-11-24 06:49. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,075, prestige 3,701 (581 free, +1.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 81 | 15 | 19 | 0 | 0 | stop 116, buy 39, buy @ 3.82 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 13 | 4 | 4 | 0 | 0 | stop 14, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 27 | 18 | 9 | 0 | 0 | stop 36, buy 18, buy @ 3.7 |
| labour | 65 | 65 | 547 | 0 | 18 | buy 65, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**0 risks, 1 waste, 4 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **labour**: 18 labour expired last turn (~32 coin): holding 65 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **beer**: we make 0/turn more than we use but there is no sell order -> v2: sell 0
- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 56.5 coin per prestige at mansion, vs 69.2 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **hold banquet 2 (fish)**: hold banquet 2 (fish) costs 56.2 coin per prestige at mansion, vs 69.2 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 116 over real use lately; planning 548, not 664

## Prestige spending, cheapest coin per prestige first

148 turns left: prestige gained now converts 52.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 49.1 | 49.8 | needs a arena (build cost 26,916); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 51.9 | 51.9 | running |
| jousting 2 (premium) | arena | 400 | 52.8 | 53.4 | needs a arena (build cost 26,916); thin at home: protection, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 54.8 | 55.9 | needs a arena (build cost 26,916); thin at home: swords, protection, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 56.2 | 56.2 |  |
| hold banquet 1 (fish) | mansion | 4.2 | 56.5 | 56.5 |  |
| hold banquet 2 (pies) | mansion | 7 | 59.7 | 59.7 |  |
| jousting 2 | arena | 210 | 60.0 | 61.2 | needs a arena (build cost 26,916); thin at home: swords, protection, plate armour; needs weaponry skill |
| hold banquet 5 | mansion | 22 | 64.0 | 64.0 | thin at home: hop beer, stockfish, sculptures |
| maintain 2 | park | 2 | 64.1 | 64.1 | thin at home: sculptures |
| hold banquet 4 (pies) | mansion | 18 | 65.2 | 65.2 | thin at home: hop beer, stockfish |
| hold banquet 2 (meat) | mansion | 6.8 | 66.1 | 66.1 | thin at home: cured meat |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: cured meat buy 4 @ 22.4, pasties buy 2 @ 13.8; crew 0.1; est +25 a turn; stock: pasties 2 @ 13.8 (keep 14)
- **linen snake** on Grandgues: cured meat buy 6 @ 25.0, grain buy 8 @ 2.28, pasties buy 2 @ 15.9; crew 0.1; est +21 a turn; stock: pasties 2 @ 15.9 (keep 14)
- best towns now: Donaunieder +38, Großmühle +35, Birkeningen +32, Bremcop +28, Darmwald +28
- Donaunieder would trade: cured meat buy 6 @ 22.4, pasties buy 2 @ 14.1; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~110 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.35 | 0.40 (44/turn) | nets 6 (15.4->40.85), axes 4 (6.77->17.1), furniture 6 (16.07->23.94), jewellery 4 (98.17->104.5) | tools 37 (5.04->7.79), cloth 24 (7.35->10.5), dyed cloth 6 (11.55->16.62), cured meat 6 (25.62->28.8) | +535 |
| Bedenis | 566 | 0.17 | 0.60 (66/turn) | nets 4 (15.4->37.24), garments 10 (30.8->35.72), axes 3 (6.77->17.39), clay 3 (4.14->11.97) | plate armour 1 (1365->1596), tools 37 (5.62->7.79), wine 34 (5.25->5.7), bricks 11 (5.25->9.4) | +513 |
| Kirchwerp | 1072 | 0.40 | 0.60 (66/turn) | nets 6 (15.4->36.67), canvas 6 (41.58->57), paper 14 (23.31->28.31), axes 4 (6.77->16.91) | cloth 18 (7.61->10.5), dyed cloth 6 (10.45->16.62), cookware 5 (21->26.79), cheese 15 (5.1->6.46) | +511 |
| Pontmont | 341 | 0.10 | 0.60 (66/turn) | timber 37 (8.03->14.06), nets 6 (15.4->41.23), tiles 2 (3.36->8.93), resin 3 (4.18->6.51) | tools 37 (5.78->7.79), bricks 10 (5.25->9.4), thread 25 (5.57->6.05), garments 2 (28.35->31.4) | +454 |
| Clairlond | 1288 | 0.52 | 0.40 (44/turn) | nets 4 (15.4->37.05), garments 10 (30.8->38), axes 4 (6.77->15.96), cloth 1 (10.3->13.01) | tools 37 (4.87->7.79), plate armour 1 (1522.5->1596), wrought iron 1 (9.82->16.34), cured meat 6 (27.3->28.8) | +361 |

**Best:** Hofkirchen at about +535 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 7 @ min 3.72 | makes 19.3, uses 19.2, holds 81 (keeps 0): sells the surplus + 7/turn of the excess |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 10 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 16 = 2.7 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 14 |  | goal planner: buys 4 a turn for today's rates, keeps up to 14 (v2 had 6) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 30.0) |
| grain | 14 @ 3.7, stop 36 |  | uses 9.0/turn (brewery 1), makes 0.0, holds 27 = 3.0 turns |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 48) |
| light armour | 1 @ 95, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.2) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 85.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 31.6k (cash + stock at home prices); +63/turn over 6 turns, +13/turn over 24 turns.
- Limits: cash flow >= -336/turn, prestige >= -1.17/turn (values are after 200 tax a turn).
- Today's settings: value -141/turn, cash -146/turn, prestige +1.30/turn.
- Plan: value +27/turn, cash +30/turn, prestige -1.17/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -143 vs -144, -192 vs -137, -20 vs -137.
- Route sales counted at most (what the ships really sold, a turn): beer 2.2, rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Rotterburg: +2/turn
  - ship Flax Wyrm -> Cobholme: +6/turn
  - mansion 1 1.00 -> 0.41: +142/turn
  - brewery 1 0.14 -> 0.08: +9/turn
  - ropewalk 1 0.25 -> 0.19: +6/turn
  - spinnery 1 1.65 -> 1.39: +2/turn
  - retting pit 1 0.91 -> 0.82: +2/turn
  - flax farm 1 4.64 -> 4.15: +4/turn
  - weavery 1 0.50 -> 0.60: -10/turn
  - sewing shop 1 0.30 -> 0.36: +14/turn
- Model check over the last 59 turns: predicted -155/turn for the settings we ran, real +16/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.73, thread 4.35, cloth 6.94, flax fibres 5.15, garments 20.08, nets 17.38, beer 3.02, timber 3.42, prestige 59.03, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 4 (v2 6); garments sell 11 (v2 10); labour buy 64 (v2 48); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Rotterburg (+4/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Cobholme (+7/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +82/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new chandlery (make candles 2) for ~5218 coin: +12/turn, payback 428 turns, doesn't pay yet (materials thin at home: bricks, nails)

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

Buffers: flax fibres 86/77, thread 1050/228, cloth 73/128

## Self-diagnosis

- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
