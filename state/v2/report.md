# v2 shadow report

Turn 13891, 2026-11-09 04:00. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,222, prestige 3,521 (401 free, -2.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 9 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 28 | 9 | 9 | 0 | 0 | stop 36, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 518 | 0 | 11 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 11.00 x13, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Notes

- labour: projection runs 100 over real use lately; planning 525, not 625

## Prestige spending, cheapest coin per prestige first

510 turns left: prestige gained now converts 92.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 52.5 | 52.5 | running |
| jousting 3 | arena | 230 | 55.2 | 55.5 | needs a arena (build cost 27,656); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 59.0 | 59.0 | thin at home: cured fish, cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 59.4 | 59.4 | thin at home: cured fish |
| hold banquet 4 (pies) | mansion | 18 | 59.5 | 59.5 | thin at home: wine, stockfish |
| hold banquet 2 (fish) | mansion | 6.8 | 60.0 | 60.0 | thin at home: wine, cured fish, cheese |
| hold banquet 3 (pies) | mansion | 8 | 60.0 | 60.0 | thin at home: pasties |
| hold banquet 4 (premium) | mansion | 20 | 60.0 | 60.0 | thin at home: wine, stockfish, premium cheese |
| jousting 2 | arena | 210 | 60.5 | 60.7 | needs a arena (build cost 27,656); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 62.6 | 62.6 | thin at home: pasties, wine, cheese |
| hold banquet 3 (meat) | mansion | 7.6 | 62.6 | 62.6 | thin at home: cheese |
| hold banquet 4 | mansion | 17.5 | 63.0 | 63.0 | thin at home: wine, ham, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 16.0 (keep 14); best orders clear only 0 a turn after crew: ship stays at 0
- best towns now: Donaunieder +314, Brunnham +307, Heidlowe +299, Clairlond +294, Essenbrucke +289
- Donaunieder would trade: furniture buy 28 @ 13.6; crew 0.4

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~112 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.80 (89/turn) | firewood 36 (2.12->5.98), timber 28 (7.56->11.4), charcoal 19 (2.62->4.89), bricks 5 (7.25->10.54) | cloth 9 (8.72->10.6), thread 21 (5.19->5.4), cookware 3 (26.67->27.74), casks 2 (6.3->6.65) | +282 |
| Rotterburg | 1056 | 0.39 | 0.20 (22/turn) | wine 12 (6.83->8.55), nets 1 (37.2->39.9), dyed yarn 2 (5.19->5.94) | garments 20 (20.48->27.93), cloth 24 (7.09->10.6), cookware 3 (23.94->27.74), salt 9 (4.03->5.56) | +257 |
| Etallaen | 774 | 0.23 | 0.20 (22/turn) | nets 6 (37.2->41.23), beer 15 (3.52->4.62), mouldboards 1 (35.07->41.42), hinges 1 (37.17->40.28) | garments 20 (24.99->27.93), cloth 16 (7.35->10.6), spinning wheels 1 (193.2->216.6), thread 31 (4.73->5.4) | +193 |
| Kirchwerp | 1072 | 0.40 | 0.60 (67/turn) | thread 88 (4.64->5.7), furniture 12 (16.48->20.14), hinges 1 (37.17->47.5), butter 1 (88.73->95.95) | garments 20 (24.57->27.93), ham 1 (108.15->118.75), axes 2 (17.75->19.76), cookware 3 (27.09->27.74) | +181 |
| Amsdermund | 1111 | 0.42 | 0.60 (67/turn) | furniture 12 (16.48->20.71), cured meat 8 (27.72->30.59), hinges 1 (37.17->51.3), thread 57 (4.64->5.22) | garments 20 (24.57->27.93), cloth 7 (8.66->10.6), ham 1 (111.3->118.75), hop beer 1 (5.78->8.69) | +166 |

**Best:** Grandgues at about +282 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 16 @ min 3.26 | goal planner: sells 16 at 3.26 (v2 had 15 at 3.42) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 83, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 15.3, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 25.8) |
| grain | 14 @ 3.7, stop 36 |  | uses 9.0/turn (brewery 1), makes 0.0, holds 28 = 3.1 turns |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 25) |
| light armour | 1 @ 99.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 37.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 23.5k (cash + stock at home prices); +163/turn over 6 turns, +91/turn over 24 turns.
- Limits: cash flow >= -301/turn, prestige >= -0.42/turn (values are after 200 tax a turn).
- Today's settings: value +59/turn, cash +18/turn, prestige -2.01/turn - breaks the prestige floor.
- Plan: value +8/turn, cash +9/turn, prestige -0.42/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +74 vs +22, -115 vs +20, +98 vs +9.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Etallaen: +11/turn
  - ship Flax Wyrm -> no route: +0/turn
  - ropewalk 1 0.25 -> 0.03: +12/turn
  - net maker 0.00 -> 0.29: +16/turn
  - spinnery 1 1.65 -> 1.26: -2/turn
  - retting pit 1 0.91 -> 0.71: -3/turn
  - flax farm 1 4.64 -> 3.58: -13/turn
  - brewery 1 [brew beer 2] 0.00 -> 0.19: -1/turn
  - brewery 1 0.14 -> 0.00: -3/turn
  - mansion 1 0.00 -> 0.38: -69/turn
- Model check over the last 59 turns: predicted +103/turn for the settings we ran, real -14/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.17, cloth 6.67, flax fibres 4.94, garments 19.30, nets 29.93, beer 2.73, timber 3.24, prestige 61.32, cash 0.00
- Orders it would set: beer sell 16 (v2 15); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 8); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); labour buy 29 (v2 25); light armour buy 1 (v2 None)
- Recipe: brewery 1 brew beer 1 -> brew beer 2 at 0.19, worth +19/turn.
- Ship linen snake: Grandgues -> Etallaen (+11/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +80/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 430 (+141 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.75 |
| ret | 3 | 0.91 | 0.95 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 878/228, cloth 72/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.15 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
