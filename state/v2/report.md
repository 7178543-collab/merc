# v2 shadow report

Turn 14168, 2026-11-20 17:28. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,833, prestige 3,742 (622 free, +1.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 49 | 0 | 19 | 0 | 0 | sell 5, sell @ 4.54 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 4 | 4 | 4 | 0 | 0 | stop 14, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 13 | 5 | 9 | 0 | 0 | stop 20, buy 5, buy @ 3.7 |
| labour | 64 | 64 | 537 | 0 | 27 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: only 0.8 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **firewood**: home ask 2.64 is above our ceiling 2.40 and last turn bought 4 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 12.10 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 27 labour expired last turn (~56 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: home ask 2.76 is above our ceiling 2.60 and last turn bought 0 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: home ask 12.10 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +5 crew for Flax Wyrm (crew 0.10, no projection from the game)
- labour: +1 crew for linen snake (crew 0.01, no projection from the game)
- labour: projection runs 100 over real use lately; planning 537, not 635

## Prestige spending, cheapest coin per prestige first

233 turns left: prestige gained now converts 69.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 51.3 | 51.7 | needs a arena (build cost 29,077); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 53.3 | 54.0 | needs a arena (build cost 29,077); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 55.2 | 55.6 | needs a arena (build cost 29,077); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 2 | arena | 210 | 58.4 | 59.1 | needs a arena (build cost 29,077); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 61.2 | 61.2 | running |
| hold banquet 4 (pies) | mansion | 18 | 61.6 | 61.6 | thin at home: ham, stockfish, cheese, candles |
| hold banquet 4 (premium) | mansion | 20 | 62.2 | 62.2 | thin at home: ham, stockfish, candles |
| hold mass 2 (premium) | cathedral | 360 | 55.0 | 62.5 | needs a cathedral (build cost 305,830); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 3 (pies) | mansion | 8 | 63.5 | 63.5 | thin at home: cheese, candles |
| hold banquet 2 (pies) | mansion | 7 | 63.9 | 63.9 | thin at home: cheese, candles |
| hold banquet 4 | mansion | 17.5 | 66.2 | 66.2 | thin at home: ham, stockfish, cheese, candles |
| hold banquet 2 (meat) | mansion | 6.8 | 67.9 | 67.9 | thin at home: cured meat, cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: beer sell 4 @ 7.55, cured meat buy 6 @ 24.6, pasties buy 9 @ 15.5; crew 0.1; est +40 a turn; stock: pasties 9 @ 15.5 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 14.9 (keep 14); best orders clear only -0 a turn after crew: ship stays at 0
- best towns now: Angefont +230, Disscester +228, Friedwerp +227, Gotthafen +215, Brunnham +201
- Angefont would trade: furniture buy 19 @ 14.5, pasties buy 9 @ 15.6; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~131 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Bordetes | 831 | 0.30 | 0.10 (13/turn) | tackles 1 (181.65->224.2), garments 10 (34.4->36.86), salt 10 (5.72->7.12), beer 4 (4.66->7.6) | cured fish 5 (29.4->34.2), cheese 8 (6.46->8.84), premium cheese 2 (31.29->36.1), cloth 4 (11.13->13) | +145 |
| Heilegg | 826 | 0.30 | 0.30 (39/turn) | nets 5 (42.2->45.98), wine 15 (6.72->7.84), leather 1 (25.41->32.3), flax fibres 4 (6.55->7.98) | cured fish 5 (28.35->34.2), cheese 8 (6.3->8.84), garments 2 (28.35->36.8), yarn 25 (6.77->7.41) | +135 |
| Caillechâtel | 488 | 0.17 | 0.20 (26/turn) | flax fibres 5 (6.55->7.79), wool 6 (10.92->11.49), flax plants 1 (1.54->2.41), flour 1 (21->23.37) | cloth 24 (9.29->13), thread 18 (6.3->7.2), cheese 8 (7.25->8.84), cured fish 5 (32.55->34.2) | +134 |
| Amsdermund | 1111 | 0.50 | 0.40 (52/turn) | casks 12 (7.93->9.5), malt 2 (7.72->8.93) | cured fish 5 (26.04->34.2), cured meat 6 (21->26.6), garments 2 (26.88->36.8), cheese 8 (6.88->8.84) | +132 |
| Grandgues | 152 | 0.05 | 0.50 (65/turn) | firewood 27 (2.77->7.03), charcoal 19 (2.79->4.33), beer 4 (4.66->7.31), bricks 5 (6.51->7.6) | cheese 8 (6.98->8.84), garments 2 (29.61->36.8), cured meat 6 (25.41->26.6), dyed cloth 1 (16.7->16.91) | +131 |

**Best:** Bordetes at about +145 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 37.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 4 @ min 4.54 | makes 19.3, uses 19.2, holds 49 (keeps 0): sells the surplus + 4/turn of the excess |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 9) |
| candles | 2 @ 76.0, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had 2) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 5 = 0.8 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 14 |  | goal planner: buys 4 a turn for today's rates, keeps up to 14 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 16.6, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 33.4) |
| grain | 6 @ 3.7, stop 21 |  | goal planner: buys 6 a turn for today's rates, keeps up to 21 (v2 had 18) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 37) |
| light armour | 1 @ 110, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 41.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.4/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 27.8k (cash + stock at home prices); +101/turn over 6 turns, -26/turn over 24 turns.
- Limits: cash flow >= -285/turn, prestige >= -1.34/turn (values are after 200 tax a turn).
- Today's settings: value -148/turn, cash -164/turn, prestige +1.10/turn.
- Plan: value +61/turn, cash +67/turn, prestige -1.34/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -45 vs -163, +128 vs -156, +34 vs -166.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Rotterburg: +22/turn
  - ship Flax Wyrm -> Nürnnieder: +4/turn
  - mansion 1 1.00 -> 0.42: +151/turn
  - brewery 1 0.14 -> 0.08: +14/turn
  - net maker 0.00 -> 0.29: +7/turn
  - ropewalk 1 0.25 -> 0.00: +2/turn
  - spinnery 1 1.65 -> 1.28: +20/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.13: +3/turn
  - retting pit 1 0.91 -> 0.81: +3/turn
  - flax farm 1 4.64 -> 4.07: +7/turn
- Model check over the last 59 turns: predicted -61/turn for the settings we ran, real -6/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.81, beer 3.55, timber 3.87, prestige 64.62, cash 0.00
- Orders it would set: bread buy 5 (v2 9); cloth sell 1 (v2 none); firewood buy 4 (v2 8); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 6 (v2 18); labour buy 64 (v2 37); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.13, worth +2/turn.
- Ship linen snake: Grandgues -> Rotterburg (+9/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Nürnnieder (+3/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +87/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 423 (+134 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.36 |
| ret | 3 | 0.91 | 0.87 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 105/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R1: bread slot dry: 5.4 held, 4.2 a turn (basic food slot (+0.3 prestige)); our buy 5 @ 2.6, home ask 2.76 -> **buy 9 @ 2.82 (ask 2.76, cap 4.3)** (ok)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
