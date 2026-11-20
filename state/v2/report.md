# v2 shadow report

Turn 14170, 2026-11-20 19:40. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,123, prestige 3,741 (621 free, -1.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 38 | 0 | 12 | 0 | 0 | sell 18, sell @ 4.5 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 4 | 4 | 4 | 0 | 0 | stop 14, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 7 | 6 | 9 | 0 | 0 | stop 22, buy 6, buy @ 3.7 |
| labour | 64 | 64 | 519 | 0 | 45 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), 3 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **grain**: only 0.8 turns of grain left and buying 6 (need 18) -> v2: buy 18
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.30 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~91 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.30 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +1 crew for linen snake (crew 0.01, no projection from the game)
- labour: projection runs 100 over real use lately; planning 519, not 616

## Prestige spending, cheapest coin per prestige first

231 turns left: prestige gained now converts 68.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 48.5 | 48.9 | needs a arena (build cost 29,953); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 52.2 | 52.6 | needs a arena (build cost 29,953); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 52.4 | 53.1 | needs a arena (build cost 29,953); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 | arena | 210 | 57.4 | 58.2 | needs a arena (build cost 29,953); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 60.5 | 60.5 | thin at home: hop beer, cheese, candles |
| hold banquet 4 (pies) | mansion | 18 | 60.5 | 60.5 | thin at home: hop beer, stockfish, candles |
| maintain 1 | park | 0.5 | 60.6 | 60.6 | running |
| hold banquet 4 (premium) | mansion | 20 | 60.9 | 60.9 | thin at home: hop beer, stockfish, candles |
| hold banquet 2 (pies) | mansion | 7 | 62.6 | 62.6 | thin at home: cheese, candles |
| hold mass 2 (premium) | cathedral | 360 | 54.9 | 62.6 | needs a cathedral (build cost 308,600); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 4 | mansion | 17.5 | 64.7 | 64.7 | thin at home: hop beer, stockfish, cheese, candles |
| hold banquet 3 (meat) | mansion | 7.6 | 67.1 | 67.1 | thin at home: hop beer, cured meat, cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: cured meat buy 3 @ 24.8, pasties buy 11 @ 16.0; crew 0.1; est +26 a turn; stock: pasties 11 @ 16.0 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 13.1 (keep 14); best orders clear only -1 a turn after crew: ship stays at 0
- best towns now: Blanans +241, Chatgnan +234, Friedwerp +228, Angefont +223, Heilegg +219
- Blanans would trade: cured meat buy 3 @ 25.0, furniture buy 18 @ 14.4, pasties buy 11 @ 16.0; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~131 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Heilegg | 826 | 0.30 | 0.20 (26/turn) | flax fibres 4 (6.5->13.21), nets 6 (42.4->45.98), salt 4 (5.88->8.98), flax plants 1 (1.51->4.27) | dyed cloth 8 (10.08->17.48), cured fish 6 (28.35->35.15), garments 2 (28.35->35.4), arms 2 (31.29->33.82) | +181 |
| Kirchwerp | 1072 | 0.47 | 0.40 (52/turn) | swords 1 (237.3->334.4), casks 14 (7.19->9.36), fleece 3 (11.03->11.59), wool 7 (10.92->11.4) | garments 2 (24.15->35.4), dyed cloth 8 (14.7->17.48), cured meat 3 (22.05->27), nails 6 (5.57->6.89) | +180 |
| Fontaux | 411 | 0.14 | 1.00 (131/turn) | flour 2 (20.48->30.4), thread 43 (6.8->7.27), timber 15 (8.82->11.78), garments 7 (35.2->37.05) | cured fish 4 (24.57->35.15), cloth 8 (11.55->13.4), dyed cloth 5 (17.01->17.48), tools 10 (6.62->6.98) | +145 |
| Caillechâtel | 488 | 0.17 | 0.20 (26/turn) | wool 6 (10.92->11.4), flax plants 1 (1.51->2.3) | cloth 24 (10.03->13.4), looms 1 (687.75->741), thread 19 (6.09->6.95), tools 15 (6.51->6.98) | +142 |
| Unterhufe | 595 | 0.21 | 0.30 (39/turn) | thread 47 (6.8->7.93), limestone 2 (17.22->30.02) | cured fish 5 (27.93->35.15), yarn 19 (6.35->7.5), beer 11 (3.53->4.6), tools 15 (6.3->6.98) | +140 |

**Best:** Heilegg at about +181 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ ?, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 17 @ min 4.44 | makes 19.3, uses 4.2, holds 38 (keeps 0): sells the surplus + 2/turn of the excess |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 6) |
| candles | 2 @ 70.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (observed), makes 0.0, holds 3 = 0.5 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 14 |  | goal planner: buys 4 a turn for today's rates, keeps up to 14 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 16.8, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 34.2) |
| grain | 6 @ 3.7, stop 23 |  | goal planner: buys 6 a turn for today's rates, keeps up to 23 (v2 had 18) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 19) |
| light armour | 1 @ 108, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 41.2) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 27.8k (cash + stock at home prices); +49/turn over 6 turns, -23/turn over 24 turns.
- Limits: cash flow >= -297/turn, prestige >= -1.34/turn (values are after 200 tax a turn).
- Today's settings: value -152/turn, cash -167/turn, prestige +1.09/turn.
- Plan: value +57/turn, cash +63/turn, prestige -1.34/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +34 vs -166, +153 vs -164, +137 vs -168.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Rotterburg: +23/turn
  - ship Flax Wyrm -> Nürnnieder: +2/turn
  - mansion 1 1.00 -> 0.42: +152/turn
  - ropewalk 1 0.25 -> 0.11: +12/turn
  - spinnery 1 1.65 -> 1.28: +14/turn
  - brewery 1 0.14 -> 0.09: +12/turn
  - net maker 0.00 -> 0.29: +5/turn
  - retting pit 1 0.91 -> 0.81: +3/turn
  - flax farm 1 4.64 -> 4.06: +6/turn
- Model check over the last 59 turns: predicted -71/turn for the settings we ran, real +27/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.74, beer 3.56, timber 4.43, prestige 64.95, cash 0.00
- Orders it would set: bread buy 5 (v2 6); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 8); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 6 (v2 18); labour buy 64 (v2 19); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Rotterburg (+10/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Nürnnieder (+1/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +87/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 422 (+133 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.32 |
| ret | 3 | 0.91 | 0.86 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 109/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R1: beer slot dry: 38.2 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy none, home ask 4.6 -> **buy 39 @ 4.68 (ask 4.6, cap 14.4)** (ok)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
