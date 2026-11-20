# v2 shadow report

Turn 14169, 2026-11-20 18:34. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,986, prestige 3,742 (622 free, +0.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 49 | 0 | 16 | 0 | 0 | sell 4, sell @ 4.54 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 4 | 4 | 4 | 0 | 0 | stop 14, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 10 | 5 | 9 | 0 | 0 | stop 21, buy 6, buy @ 3.7 |
| labour | 64 | 64 | 529 | 0 | 35 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), 3 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **firewood**: home ask 2.64 is above our ceiling 2.40 and last turn bought 4 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.20 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 35 labour expired last turn (~71 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **arms**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **bread**: home ask 3.14 is above our ceiling 2.60 and last turn bought 0 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: home ask 11.20 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +1 crew for linen snake (crew 0.01, no projection from the game)
- labour: projection runs 100 over real use lately; planning 529, not 620

## Prestige spending, cheapest coin per prestige first

232 turns left: prestige gained now converts 68.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 48.8 | 49.2 | needs a arena (build cost 29,159); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 52.5 | 52.9 | needs a arena (build cost 29,159); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 52.9 | 53.6 | needs a arena (build cost 29,159); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 | arena | 210 | 58.0 | 58.7 | needs a arena (build cost 29,159); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 61.2 | 61.2 | running |
| hold banquet 4 (pies) | mansion | 18 | 61.4 | 61.4 | thin at home: stockfish, candles |
| hold banquet 4 (premium) | mansion | 20 | 62.1 | 62.1 | thin at home: stockfish, candles |
| hold mass 2 (premium) | cathedral | 360 | 54.9 | 62.4 | needs a cathedral (build cost 305,360); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 3 (pies) | mansion | 8 | 62.6 | 62.6 | thin at home: cheese, candles |
| hold banquet 2 (pies) | mansion | 7 | 63.2 | 63.2 | thin at home: cheese, candles |
| hold banquet 4 | mansion | 17.5 | 65.7 | 65.7 | thin at home: stockfish, cheese, candles |
| hold banquet 2 (meat) | mansion | 6.8 | 67.9 | 67.9 | thin at home: cured meat, cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: cured meat buy 4 @ 24.8, pasties buy 7 @ 15.4; crew 0.1; est +18 a turn; stock: pasties 7 @ 15.4 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 15.4 (keep 14); best orders clear only -10 a turn after crew: ship stays at 0
- best towns now: Blanans +239, Angefont +236, Friedwerp +209, Disscester +202, Dortgart +176
- Blanans would trade: beer sell 7 @ 5.6, cured meat buy 4 @ 24.8, furniture buy 17 @ 13.9, pasties buy 10 @ 16.0; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~132 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Heilegg | 826 | 0.30 | 0.30 (40/turn) | flax fibres 3 (6.45->11.3), nets 4 (42.4->45.98), wine 13 (6.67->7.41), wool 8 (10.92->11.78) | dyed cloth 9 (10.08->17.1), cured fish 4 (26.25->32.68), cloth 24 (12.92->14.1), garments 2 (28.35->36.4) | +167 |
| Clairas | 374 | 0.13 | 0.20 (26/turn) | flax fibres 5 (6.45->6.84), clay 1 (4.37->9.79) | cloth 24 (11.03->14.1), yarn 20 (5.99->7.41), dyed cloth 3 (10.5->17.1), garments 2 (30.03->36.4) | +154 |
| Kirchwerp | 1072 | 0.48 | 0.40 (53/turn) | canvas 4 (47.04->52.25), casks 14 (7.3->9.36), rope 2 (90.83->95.95), wool 4 (10.92->12.73) | garments 2 (24.15->36.4), cured meat 4 (21->26.4), dyed cloth 9 (14.7->17.1), chisels 4 (8.4->10.26) | +132 |
| Herschweig | 775 | 0.27 | 0.30 (40/turn) | jewellery 2 (98.17->99.75), wine 3 (6.67->7.46), wool 4 (10.92->11.49), beer 7 (4.62->5.22) | cloth 18 (10.5->14.1), yarn 25 (6.3->7.41), thread 25 (6.35->7.35), garments 2 (30.87->36.4) | +131 |
| Unterhufe | 595 | 0.21 | 0.40 (53/turn) | limestone 2 (17.22->29.83), wine 5 (6.67->7.27), malt 1 (8.09->8.64) | cloth 24 (12.71->14.1), premium ham 1 (218.4->235.6), yarn 25 (6.51->7.41), cured fish 4 (28.14->32.68) | +131 |

**Best:** Heilegg at about +167 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ ?, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 18 @ min 4.5 | makes 19.3, uses 4.2, holds 49 (keeps 0): sells the surplus + 3/turn of the excess |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 8) |
| candles | 2 @ 70.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (observed), makes 0.0, holds 3 = 0.5 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 14 |  | goal planner: buys 4 a turn for today's rates, keeps up to 14 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 16.8, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 34.6) |
| grain | 6 @ 3.7, stop 22 |  | goal planner: buys 6 a turn for today's rates, keeps up to 22 (v2 had 18) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 29) |
| light armour | 1 @ 108, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 41.2) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 27.9k (cash + stock at home prices); +85/turn over 6 turns, -30/turn over 24 turns.
- Limits: cash flow >= -291/turn, prestige >= -1.34/turn (values are after 200 tax a turn).
- Today's settings: value -151/turn, cash -168/turn, prestige +1.09/turn.
- Plan: value +59/turn, cash +63/turn, prestige -1.34/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +128 vs -156, +34 vs -166, +153 vs -164.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Rotterburg: +23/turn
  - ship Flax Wyrm -> Nürnnieder: +2/turn
  - mansion 1 1.00 -> 0.42: +152/turn
  - brewery 1 0.14 -> 0.08: +13/turn
  - ropewalk 1 0.25 -> 0.11: +13/turn
  - spinnery 1 1.65 -> 1.28: +15/turn
  - net maker 0.00 -> 0.29: +5/turn
  - retting pit 1 0.91 -> 0.81: +3/turn
  - flax farm 1 4.64 -> 4.07: +7/turn
- Model check over the last 59 turns: predicted -66/turn for the settings we ran, real +30/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.55, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.74, beer 3.55, timber 3.87, prestige 64.94, cash 0.00
- Orders it would set: bread buy 5 (v2 8); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 8); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 6 (v2 18); labour buy 64 (v2 29); light armour buy 1 (v2 None)
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
| flax | 11 | 4.64 | 4.34 |
| ret | 3 | 0.91 | 0.87 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 107/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
