# v2 shadow report

Turn 14252, 2026-11-24 05:44. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,095, prestige 3,699 (579 free, +1.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 54 | 7 | 19 | 0 | 0 | stop 116, buy 39, buy @ 3.82 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 13 | 4 | 4 | 0 | 0 | stop 14, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 18 | 7 | 7 | 2 | 0 | stop 36, buy 18, buy @ 3.7 |
| labour | 65 | 65 | 545 | 0 | 20 | buy 65, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **grain**: brewery 1 ran short of grain (buy is live (18 @ 3.7), 7 bought last turn); labour need rises ~18/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 9.80 x12, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 20 labour expired last turn (~34 coin): holding 65 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **hold banquet 2 (fish)**: hold banquet 2 (fish) costs 56.0 coin per prestige at mansion, vs 67.2 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 116 over real use lately; planning 545, not 652

## Prestige spending, cheapest coin per prestige first

149 turns left: prestige gained now converts 52.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 46.5 | 47.1 | needs a arena (build cost 26,791); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 47.6 | 48.7 | needs a arena (build cost 26,791); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 49.9 | 50.6 | needs a arena (build cost 26,791); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 50.7 | 50.7 | running |
| jousting 2 | arena | 210 | 52.1 | 53.4 | needs a arena (build cost 26,791); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 56.0 | 56.0 |  |
| hold banquet 1 (fish) | mansion | 4.2 | 56.1 | 56.1 | thin at home: beer |
| hold banquet 2 (pies) | mansion | 7 | 59.1 | 59.1 | thin at home: pies |
| maintain 2 | park | 2 | 63.7 | 63.7 | thin at home: sculptures |
| hold banquet 5 | mansion | 22 | 63.8 | 63.8 | thin at home: hop beer, stockfish, sculptures |
| hold banquet 2 (meat) | mansion | 6.8 | 64.5 | 64.5 | thin at home: cured meat |
| hold banquet 4 (pies) | mansion | 18 | 65.0 | 65.0 | thin at home: hop beer, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 10 | 151802239 | 0 | - | cured meat 6, pasties 3 | -178 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 13.8 (keep 14); best orders clear only 11 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 15.3 (keep 14); best orders clear only 10 a turn after crew: ship stays at 0
- best towns now: Donaunieder +27, Darmwald +24, Großmühle +24, Birkeningen +22, Dedlowe +21
- Donaunieder would trade: cured meat buy 6 @ 22.4, pasties buy 1 @ 14.4; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~108 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Pontmont | 341 | 0.10 | 0.50 (54/turn) | timber 25 (8.03->13.87), axes 4 (9.82->18.43), tiles 7 (3.17->8.74), furniture 8 (16.07->17.67) | tools 42 (5.78->7.5), bricks 20 (5.3->9.31), thread 19 (5.57->6.05), garments 2 (28.35->31.4) | +330 |
| Kirchwerp | 1072 | 0.39 | 0.60 (65/turn) | canvas 5 (41.79->52.25), tackles 2 (154.35->171), axes 4 (9.82->16.91), casks 11 (6.51->9.36) | cloth 16 (7.93->10.4), cookware 5 (21->26.79), dyed cloth 5 (9.97->15.77), cheese 14 (5.1->6.46) | +304 |
| Rouhomme | 368 | 0.11 | 0.60 (65/turn) | garments 10 (30.6->36.1), yarn 12 (6.56->9.79), axes 4 (9.82->17.57), cloth 13 (10.92->12.35) | tools 42 (5.78->7.5), bricks 21 (5.21->9.31), thread 29 (5.57->6.05), cookware 5 (24.99->26.79) | +294 |
| Bedenis | 566 | 0.16 | 0.60 (65/turn) | cloth 18 (10.92->15.67), garments 10 (30.6->36.67), axes 3 (9.82->17.39), nets 4 (35.8->37.43) | tools 42 (5.83->7.5), bricks 10 (5.25->9.31), flax fibres 8 (5.88->7.15), thread 20 (5.57->6.05) | +271 |
| Friedwerp | 684 | 0.20 | 0.30 (32/turn) | axes 4 (9.82->16.25), nets 5 (35.8->39.14), tackles 2 (154.35->159.6), gears 1 (88.2->95) | tools 36 (5.04->7.5), flax fibres 24 (5.35->7.15), cloth 10 (7.35->10.4), cured meat 6 (25.83->27.8) | +235 |

**Best:** Pontmont at about +330 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 31 @ 4.04, stop 77 |  | uses 19.2/turn (household upkeep, mansion 1), makes 0.0, holds 54 = 2.8 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 90.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 7 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 22 = 3.7 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 14 |  | goal planner: buys 4 a turn for today's rates, keeps up to 14 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 29.8) |
| grain | 18 @ 3.7, stop 36 |  | uses 9.0/turn (observed), makes 0.0, holds 18 = 2.0 turns |
| labour | 65 @ 2.2, stop - |  | goal planner: buys 65 for today's rates (v2 had 45) |
| light armour | 1 @ 95, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 31.5k (cash + stock at home prices); +40/turn over 6 turns, +11/turn over 24 turns.
- Limits: cash flow >= -337/turn, prestige >= -1.16/turn (values are after 200 tax a turn).
- Today's settings: value -145/turn, cash -137/turn, prestige +1.31/turn.
- Plan: value +28/turn, cash +41/turn, prestige -1.16/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +24 vs -141, -143 vs -144, -192 vs -137.
- Route sales counted at most (what the ships really sold, a turn): beer 2.2, rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Darmwald: +16/turn
  - ship Flax Wyrm -> Großaue: +8/turn
  - mansion 1 1.00 -> 0.41: +143/turn
  - brewery 1 0.14 -> 0.08: +11/turn
  - net maker [make nets 2] 0.00 -> 0.33: +5/turn
  - spinnery 1 1.65 -> 1.55: +4/turn
  - flax farm 1 4.64 -> 3.14: +0/turn
  - sewing shop 1 0.30 -> 0.36: -12/turn
  - weavery 1 0.50 -> 0.60: +13/turn
- Model check over the last 59 turns: predicted -155/turn for the settings we ran, real +15/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.69, thread 4.25, cloth 6.78, flax fibres 5.04, garments 19.62, nets 31.72, beer 3.05, timber 3.42, prestige 62.12, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 5); garments sell 11 (v2 10); labour buy 65 (v2 45); light armour buy 1 (v2 None); rope sell 1 (v2 none)
- Recipe: net maker make nets 3 -> make nets 2 at 0.33, worth +3/turn.
- Ship linen snake: Grandgues -> Darmwald (+7/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Großaue (+8/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +84/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

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

Buffers: flax fibres 85/77, thread 1062/228, cloth 73/128

## Self-diagnosis

- R2: spinnery 1 blocked by thread space: 1062 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
- R5: beer buy not filling: bid 3.82 under the home ask 3.86 for 3 turns, bought 7.0 of 39, 54.0 held (2.8 turns); raise needs Taylor (ceiling None)
