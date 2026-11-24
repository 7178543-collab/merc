# v2 shadow report

Turn 14267, 2026-11-24 20:39. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,264, prestige 3,717 (597 free, +0.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 66 | 17 | 15 | 0 | 0 | sell 6, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 14 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 27 | 2 | 9 | 0 | 0 | stop 31, buy 8, buy @ 3.7 |
| labour | 64 | 64 | 540 | 0 | 24 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 6 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (12 @ 29.8), but the home ask 31.20 is above it); labour need rises ~35/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 10.90 x7, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 24 labour expired last turn (~45 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **cured meat**: home ask 31.20 is above our ceiling 29.00 and last turn bought 1 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **fish**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 58.1 coin per prestige at mansion, vs 70.0 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **hold banquet 2 (fish)**: hold banquet 2 (fish) costs 58.1 coin per prestige at mansion, vs 70.0 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **hold banquet 2 (pies)**: hold banquet 2 (pies) costs 59.2 coin per prestige at mansion, vs 70.0 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch

## Notes

- labour: projection runs 114 over real use lately; planning 540, not 653

## Prestige spending, cheapest coin per prestige first

134 turns left: prestige gained now converts 49.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 50.4 | 51.2 | needs a arena (build cost 29,738); thin at home: protection, light armour, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 54.1 | 54.9 | needs a arena (build cost 29,738); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 55.2 | 55.2 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 58.1 | 58.1 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 58.1 | 58.1 |  |
| hold banquet 2 (pies) | mansion | 7 | 59.2 | 59.2 |  |
| jousting 3 | arena | 230 | 59.7 | 61.2 | needs a arena (build cost 29,738); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 62.2 | 62.2 | thin at home: hop beer, stockfish |
| hold banquet 5 | mansion | 22 | 64.0 | 64.0 | thin at home: hop beer, stockfish, sculptures |
| hold banquet 4 | mansion | 17.5 | 65.7 | 65.7 | thin at home: hop beer, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 66.0 | 66.0 | thin at home: hop beer, stockfish |
| jousting 2 | arena | 210 | 65.4 | 67.0 | needs a arena (build cost 29,738); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 11 | 151802239 | 0 | - | pasties 1 | -15 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: cured meat buy 4 @ 27.6, furniture buy 1 @ 13.9, pasties buy 1 @ 11.6; crew 0.1; est +23 a turn; stock: furniture 1 @ 13.9 (keep 145); stock: pasties 1 @ 11.6 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 16.2 (keep 14); best orders clear only 15 a turn after crew: ship stays at 0
- best towns now: Donaunieder +42, Cobholme +42, Nürnnieder +38, Bremcop +38, Dortgart +36
- Donaunieder would trade: cured meat buy 4 @ 22.0, furniture buy 1 @ 14.6, pasties buy 1 @ 14.1; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~116 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Heilegg | 826 | 0.26 | 0.30 (35/turn) | nets 6 (15.69->41.99), wrought iron 14 (17.64->27.55), wine 16 (6.62->8.17), beer 9 (3.26->5.32) | windows 1 (1002.75->1235), cured meat 4 (27.09->31.2), paper 5 (25.2->26.03), slaked lime 1 (9.77->13.11) | +605 |
| Heidlowe | 662 | 0.20 | 0.30 (35/turn) | nets 5 (15.69->37.24), medicine 1 (135.45->151.05), beer 9 (3.26->3.7) | windows 1 (987->1235), cloth 24 (8.87->10.2), cured meat 4 (24.36->31.2), thread 51 (5.41->6.05) | +468 |
| Hofkirchen | 991 | 0.36 | 0.50 (58/turn) | coats 7 (100.28->126.35), glass ingots 4 (70.88->76), medicine 1 (135.45->148.2), beer 9 (3.26->4.67) | windows 1 (1113->1235), silver bars 1 (270.9->298.3), cured meat 4 (26.04->31.2), thread 25 (5.21->6.05) | +440 |
| Brunnham | 1281 | 0.55 | 0.40 (46/turn) | nets 6 (15.69->37.05), dyed cloth 14 (17.85->19.19), garments 10 (28.8->30.4), medicine 1 (135.45->144.4) | windows 1 (1050->1235), cookware 5 (19.95->25.84), silver bars 1 (275.1->298.3), cured meat 4 (25.83->31.2) | +438 |
| Arnsreuth | 921 | 0.32 | 0.10 (12/turn) | nets 4 (15.69->37.43), dyed cloth 10 (17.85->22.8), cloth 6 (10.71->12.44) | windows 1 (1018.5->1235), cured meat 4 (23.94->31.2), slaked lime 1 (9.19->13.11), tin ingots 1 (33.6->35.91) | +384 |

**Best:** Heilegg at about +605 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 19 @ min 3.38 | makes 19.3, uses 4.2, holds 66 (keeps 0): sells the surplus + 4/turn of the excess |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 87, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (observed), makes 0.0, holds 10 = 1.7 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 0.96 | goal planner: sells 2 a turn at 0.96, keeps 219 (no one offered it) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 28.0) |
| grain | 9 @ 3.7, stop 33 |  | goal planner: buys 9 a turn for today's rates, keeps up to 33 (v2 had 14) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 40) |
| light armour | 1 @ 101, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.2k (cash + stock at home prices); -44/turn over 6 turns, -45/turn over 24 turns.
- Limits: cash flow >= -303/turn, prestige >= -1.24/turn (values are after 200 tax a turn).
- Today's settings: value -174/turn, cash -174/turn, prestige +1.22/turn.
- Plan: value +7/turn, cash +14/turn, prestige -1.24/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -64 vs -148, +124 vs -151, -336 vs -156.
- Route sales counted at most (what the ships really sold, a turn): beer 2.2, rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Donaunieder: +24/turn
  - ship Flax Wyrm -> Nürnnieder: +1/turn
  - mansion 1 1.00 -> 0.42: +164/turn
  - spinnery 1 1.65 -> 1.29: -1/turn
  - retting pit 1 0.91 -> 0.77: +2/turn
  - flax farm 1 4.64 -> 3.83: +10/turn
- Model check over the last 59 turns: predicted -147/turn for the settings we ran, real -15/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.38, garments 21.00, nets 18.18, beer 3.20, timber 3.87, prestige 66.10, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 5); flax plants sell 2 (v2 none); garments sell 11 (v2 10); grain buy 9 (v2 14); labour buy 64 (v2 40); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Donaunieder (+9/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Nürnnieder (+2/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +86/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

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

Buffers: flax fibres 86/77, thread 1061/228, cloth 73/128

## Self-diagnosis

- R1: cured meat slot dry: 10.0 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 12 @ 29.8, home ask 31.2 -> **buy 12 @ 31.8 (ask 31.2, cap 42.0)** (ok)
- R2: spinnery 1 blocked by thread space: 1061 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
