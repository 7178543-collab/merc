# v2 shadow report

Turn 14274, 2026-11-25 03:58. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,747, prestige 3,723 (603 free, -0.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 74 | 0 | 13 | 0 | 0 | sell 3, sell @ 3.88; stop 116, buy 39, buy @ 4.14 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 15 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 28 | 9 | 9 | 0 | 0 | stop 35, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 549 | 0 | 15 | buy 64, buy @ 2.2 |
| meat | 0 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), 3 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12

## Waste (money lost now)

- **labour**: 15 labour expired last turn (~29 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 113 over real use lately; planning 549, not 646

## Prestige spending, cheapest coin per prestige first

127 turns left: prestige gained now converts 47.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 59.1 | 59.1 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 59.4 | 59.4 |  |
| hold banquet 1 (fish) | mansion | 4.2 | 61.3 | 61.3 |  |
| jousting 3 | arena | 230 | 59.9 | 61.6 | needs a arena (build cost 30,750); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 61.7 | 61.7 |  |
| hold banquet 2 (meat) | mansion | 6.8 | 65.8 | 65.8 |  |
| hold banquet 4 (pies) | mansion | 18 | 65.8 | 65.8 | thin at home: hop beer, stockfish |
| hold banquet 5 | mansion | 22 | 66.9 | 66.9 | thin at home: hop beer, stockfish, sculptures |
| jousting 2 | arena | 210 | 65.6 | 67.5 | needs a arena (build cost 30,750); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 68.3 | 68.3 | thin at home: hop beer, stockfish |
| hold banquet 4 | mansion | 17.5 | 69.7 | 69.7 | thin at home: hop beer, ham, stockfish |
| hold banquet 1 (meat) | mansion | 4.2 | 69.8 | 69.8 | running |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 15.3 (keep 14); best orders clear only -2 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -3 a turn after crew: ship stays at 0
- best towns now: Orlesailles +53, Heilegg +50, Bordetes +35, Dortgart +28, Rouhomme +27
- Orlesailles would trade: cured meat buy 3 @ 24.4, pasties buy 6 @ 9.6; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~124 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Bordetes | 831 | 0.29 | 0.50 (62/turn) | silver bars 1 (289.8->345.8), charcoal 19 (2.31->5.98), beer 12 (4->5.75), rope 1 (79->92.62) | sculptures 1 (2478->2736), dyed cloth 8 (14.8->16.62), thread 2 (5.25->5.55) | +371 |
| Kirchwerp | 1072 | 0.45 | 0.50 (62/turn) | tools 22 (6.51->11.21), glass ingots 2 (69.83->114), garments 10 (30.2->38), wine 16 (6.46->10.54) | cured meat 3 (24.57->27.4), cookware 4 (25.2->26.98), tin ingots 2 (33.81->35.91) | +353 |
| Hofkirchen | 991 | 0.39 | 0.50 (62/turn) | coats 6 (102.9->126.35), glass ingots 2 (69.83->92.15), ploughs 5 (82.95->90.25), furniture 15 (16.38->18.62) | cookware 4 (24.78->26.98), hop beer 6 (13.33->15.2), cloth 21 (11.45->12), tin ingots 2 (33.81->35.91) | +235 |
| Grandgues | 152 | 0.05 | 0.50 (62/turn) | bread 182 (2.73->3.59), charcoal 19 (2.31->4.8), wine 12 (6.46->8.79), beer 12 (4->5.46) | garments 2 (29.61->30.6), candles 1 (91.35->92) | +228 |
| Rouhomme | 368 | 0.12 | 0.20 (25/turn) | thread 53 (5.3->7.41), wine 39 (6.46->8.79), rope 1 (79->84.55), limestone 1 (21.84->28.5) | dyed cloth 8 (15.44->16.62), cookware 4 (24.99->26.98), candles 1 (86.62->92), bricks 6 (5.51->8.41) | +226 |

**Best:** Bordetes at about +371 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 31.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 20 @ min 3.88 | makes 19.3, uses 4.2, holds 74 (keeps 0): sells the surplus + 5/turn of the excess |
| bread | 5 @ 2.66, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 3 @ 29.0, stop 11 |  | goal planner: buys 3 a turn for today's rates, keeps up to 11 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 0.96 | goal planner: sells 2 a turn at 0.96, keeps 219 (no one offered it) |
| furniture | 2 @ 16, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 29.4) |
| grain | 9 @ 3.7, stop 35 |  | goal planner: buys 9 a turn for today's rates, keeps up to 35 (v2 had 14) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 49) |
| light armour | 1 @ 100, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 77.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 29.8k (cash + stock at home prices); -70/turn over 6 turns, -68/turn over 24 turns.
- Limits: cash flow >= -281/turn, prestige >= -1.26/turn (values are after 200 tax a turn).
- Today's settings: value -181/turn, cash -177/turn, prestige +1.18/turn.
- Plan: value +11/turn, cash +17/turn, prestige -1.26/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -103 vs -181, +22 vs -196, -138 vs -187.
- Route sales counted at most (what the ships really sold, a turn): beer 2.3, rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Donaunieder: +49/turn
  - ship Flax Wyrm -> Calange: +7/turn
  - mansion 1 1.00 -> 0.42: +169/turn
  - net maker 0.00 -> 0.28: +7/turn
  - spinnery 1 1.65 -> 1.34: -0/turn
  - retting pit 1 0.91 -> 0.80: +3/turn
  - flax farm 1 4.64 -> 4.02: +8/turn
  - sewing shop 1 0.30 -> 0.25: -7/turn
  - weavery 1 0.50 -> 0.40: +12/turn
- Model check over the last 59 turns: predicted -147/turn for the settings we ran, real -59/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 33.05, beer 3.26, timber 3.60, prestige 65.89, cash 0.00
- Orders it would set: bread buy 5 (v2 None); cloth sell 1 (v2 none); cured meat buy 3 (v2 12); firewood buy 4 (v2 5); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 14); labour buy 64 (v2 49); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Donaunieder (+38/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Calange (+7/turn over staying).
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

Buffers: flax fibres 85/77, thread 1050/228, cloth 72/128

## Self-diagnosis

Nothing found this run.
