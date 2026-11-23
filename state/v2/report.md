# v2 shadow report

Turn 14224, 2026-11-23 01:58. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,482, prestige 3,681 (561 free, -0.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 76 | 0 | 12 | 0 | 0 | min_holding 58, sell 15, sell @ 3.88 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 7 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 20 | 9 | 9 | 0 | 0 | stop 36, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 546 | 0 | 18 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 2 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (12 @ 32.8), 3 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 10.60 x18, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **Flax Wyrm**: Flax Wyrm cost 10 coin last turn (crew 0.10) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell
- **labour**: 18 labour expired last turn (~30 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **cured meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 57.5 coin per prestige at mansion, vs 72.4 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch

## Notes

- labour: projection runs 100 over real use lately; planning 548, not 648

## Prestige spending, cheapest coin per prestige first

177 turns left: prestige gained now converts 58.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.2 | 49.2 | running |
| jousting 3 (premium) | arena | 420 | 48.9 | 49.4 | needs a arena (build cost 26,403); thin at home: protection, light armour, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 49.6 | 50.5 | needs a arena (build cost 26,403); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 52.5 | 53.1 | needs a arena (build cost 26,403); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 2 | arena | 210 | 54.3 | 55.3 | needs a arena (build cost 26,403); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 57.5 | 57.5 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 60.0 | 60.0 | thin at home: wine |
| hold banquet 2 (pies) | mansion | 7 | 62.8 | 62.8 | thin at home: wine, pies |
| hold banquet 4 (pies) | mansion | 18 | 63.8 | 63.8 | thin at home: hop beer, wine, stockfish |
| hold banquet 5 | mansion | 22 | 64.6 | 64.6 | thin at home: hop beer, wine, stockfish, sculptures |
| hold banquet 4 (premium) | mansion | 20 | 65.6 | 65.6 | thin at home: hop beer, wine, stockfish |
| jousting 1 | arena | 170 | 65.6 | 66.8 | needs a arena (build cost 26,403); thin at home: protection, light armour, arms; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 10 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: beer sell 9 @ 7.5, cured meat buy 3 @ 33.2; crew 0.1; est +36 a turn
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only 7 a turn after crew: ship stays at 0
- best towns now: Clairas +131, Bedenis +128, Clairlond +120, Chatgnan +111, Dortgart +104
- Clairas would trade: cured meat buy 3 @ 27.6, furniture buy 6 @ 14.0, pasties buy 9 @ 14.3; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~104 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.80 (83/turn) | firewood 36 (2.5->10.16), thread 81 (5.85->7.03), timber 28 (8.09->11.3), beer 9 (3.07->7.6) | bricks 10 (7.09->10.36), garments 2 (28.98->30.2), leather 1 (29.61->30.59), tools 6 (5.62->5.79) | +569 |
| Hofkirchen | 991 | 0.33 | 0.30 (31/turn) | swords 3 (268.8->286.9), nets 6 (37.4->44.65), wheels 3 (24.36->37.05), glass ingots 1 (52.5->75.52) | dyed cloth 6 (9.97->15.11), garments 2 (25.2->30.2), tools 18 (5.15->5.79), cured meat 4 (29.61->31.16) | +243 |
| Rotterburg | 1056 | 0.37 | 0.30 (31/turn) | furniture 8 (17.12->20.33), glass ingots 1 (52.5->63.65), nets 3 (37.4->40.28), hides 1 (14.38->18.62) | cloth 24 (7.25->10.2), dyed cloth 9 (10.71->15.11), lathes 1 (185.85->207.1), garments 2 (25.62->30.2) | +166 |
| Clairas | 374 | 0.10 | 1.00 (104/turn) | firewood 28 (2.5->6.65), glass ingots 1 (52.5->60.32), nets 3 (37.4->39.9), cheese 8 (7.19->7.55) | cloth 24 (8.4->10.2), thread 45 (5.62->6.05), cured meat 6 (28.56->31.16), garments 2 (24.57->30.2) | +133 |
| Kirchwerp | 1072 | 0.38 | 0.30 (31/turn) | glass ingots 1 (52.5->84.08), ploughs 1 (85.05->114), light armour 2 (98.7->101.65), arms 7 (33.39->34.58) | lathes 1 (179.55->207.1), tools 18 (4.3->5.79), garments 2 (24.15->30.2), nails 14 (5.78->6.55) | +133 |

**Best:** Grandgues at about +569 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 10 @ min 3.28 | goal planner: sells 10 at 3.28 (v2 had 10 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 83.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (observed), makes 0.0, holds 5 = 0.8 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 16.7, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 25.8) |
| grain | 9 @ 3.7, stop 33 |  | goal planner: buys 9 a turn for today's rates, keeps up to 33 (v2 had 18) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 48) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 36.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 31.3k (cash + stock at home prices); -16/turn over 6 turns, +30/turn over 24 turns.
- Limits: cash flow >= -437/turn, prestige >= -1.09/turn (values are after 200 tax a turn).
- Today's settings: value -171/turn, cash -169/turn, prestige +1.39/turn.
- Plan: value +23/turn, cash +30/turn, prestige -1.09/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +24 vs -190, +93 vs -184, +11 vs -165.
- Route sales counted at most (what the ships really sold, a turn): beer 1.5.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Donaunieder: +39/turn
  - ship Flax Wyrm -> Darmwald: +10/turn
  - mansion 1 1.00 -> 0.41: +176/turn
  - net maker 0.00 -> 0.29: +7/turn
  - spinnery 1 1.65 -> 1.57: +4/turn
  - flax farm 1 4.64 -> 4.80: -1/turn
  - sewing shop 1 0.30 -> 0.36: -10/turn
  - weavery 1 0.50 -> 0.60: +16/turn
- Model check over the last 59 turns: predicted -152/turn for the settings we ran, real +63/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.64, thread 4.12, cloth 6.58, flax fibres 4.89, garments 19.04, nets 30.26, beer 3.13, timber 3.49, prestige 70.38, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 8); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 18); labour buy 64 (v2 48); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Donaunieder (+25/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Darmwald (+6/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +82/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1886 coin: +5/turn, payback 411 turns, doesn't pay yet (materials thin at home: limestone)

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

Buffers: flax fibres 85/77, thread 1061/228, cloth 72/128

## Self-diagnosis

- R1: cured meat slot dry: 5.0 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 12 @ 32.8, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1061 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
