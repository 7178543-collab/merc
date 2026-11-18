# v2 shadow report

Turn 14118, 2026-11-18 15:19. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,530, prestige 3,601 (481 free, -2.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 16 | 4 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 9, buy @ 3.8 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 34 | 0 | 0 | 0 | 0 | stop 18, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 516 | 0 | 13 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.42 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.42 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **labour**: 13 labour expired last turn (~26 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **candles**: home ask 80.50 is above our ceiling 76.00 and last turn bought 0 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 516, not 616

## Prestige spending, cheapest coin per prestige first

283 turns left: prestige gained now converts 75.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 49.4 | 49.6 | needs a arena (build cost 27,046); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 53.0 | 53.3 | needs a arena (build cost 27,046); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 53.8 | 54.3 | needs a arena (build cost 27,046); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 56.4 | 56.4 | running |
| jousting 2 | arena | 210 | 58.9 | 59.5 | needs a arena (build cost 27,046); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 59.6 | 59.6 |  |
| hold mass 2 (premium) | cathedral | 360 | 55.5 | 60.5 | needs a cathedral (build cost 296,080); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |
| hold banquet 2 (fish) | mansion | 6.8 | 61.8 | 61.8 | thin at home: cheese |
| hold banquet 1 (meat) | mansion | 4.2 | 62.4 | 62.4 |  |
| hold banquet 4 (premium) | mansion | 20 | 63.0 | 63.0 | thin at home: stockfish, premium ham |
| hold banquet 2 (meat) | mansion | 6.8 | 63.6 | 63.6 | thin at home: cheese |
| hold banquet 2 (pies) | mansion | 7 | 63.7 | 63.7 | thin at home: cheese, pies |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 11 | 151802239 | 0.032 | - | candles 3, pasties 1 | -249 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 16.4 (keep 14); best orders clear only -9 a turn after crew: ship stays at 0
- best towns now: Amsdermund +649, Bordees +445, Gotthafen +441, Boistot +413, Vauxvais +370
- Amsdermund would trade: candles buy 4 @ 76.5, furniture buy 55 @ 13.7, pasties buy 1 @ 15.1; crew 0.9

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~119 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.80 (95/turn) | firewood 32 (2.54->6.84), timber 30 (7.88->11.4), charcoal 19 (3.07->5.22), limestone 3 (16.59->24.7) | dyed cloth 7 (10.08->13.11), cloth 3 (10.24->11), beer 4 (3.49->3.72), leather 1 (22.68->23.37) | +246 |
| Fontaux | 411 | 0.13 | 0.80 (95/turn) | beer 69 (3.91->5.18), timber 28 (7.88->12.16), arms 3 (32.76->35.53), wine 19 (7.35->7.74) | cloth 6 (9.13->11), garments 2 (31.5->32.6), resin 2 (3.36->3.7) | +166 |
| Amsdermund | 1111 | 0.45 | 0.40 (47/turn) | jewellery 5 (96.6->104.5) | cloth 24 (7.35->11), thread 29 (4.51->5.5), garments 2 (27.3->32.6), wax 4 (25.2->27.74) | +163 |
| Rotterburg | 1056 | 0.42 | 0.20 (24/turn) | lathes 1 (182.7->201.4), acid 1 (113.4->122.55), jewellery 5 (96.6->98.8), nets 6 (35.4->37.81) | cloth 24 (7.25->11), garments 2 (28.14->32.6), candles 1 (79.8->80.5) | +134 |
| Angefont | 686 | 0.22 | 0.30 (36/turn) | beer 69 (3.91->4.99), garments 10 (31.4->32.11), rope 1 (81.5->85.02) | flax fibres 28 (5.04->7), cloth 17 (10.24->11), cheese 8 (6.62->7.31), flax plants 30 (1.31->1.83) | +112 |

**Best:** Grandgues at about +246 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 3.9, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 16 = 3.9 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 7) |
| candles | 2 @ 76.0, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had 2) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 10 @ min 21 | goal planner: sells 10 at 21 (v2 had 10 at 31.6) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 16) |
| light armour | 1 @ 102, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 79.5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 27.4k (cash + stock at home prices); +212/turn over 6 turns, +88/turn over 24 turns.
- Limits: cash flow >= -397/turn, prestige >= -0.76/turn (values are after 200 tax a turn).
- Today's settings: value +87/turn, cash +50/turn, prestige -2.62/turn - breaks the prestige floor.
- Plan: value +22/turn, cash +32/turn, prestige -0.76/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +145 vs +44, +363 vs +47, -0 vs +46.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Essenbrucke: +2/turn
  - ship Flax Wyrm -> Amsdermund: +2/turn
  - brewery 1 0.14 -> 0.08: +14/turn
  - spinnery 1 1.65 -> 1.42: +4/turn
  - retting pit 1 0.91 -> 0.80: +2/turn
  - net maker 0.00 -> 0.28: +1/turn
  - flax farm 1 4.64 -> 4.03: +6/turn
  - ropewalk 1 0.25 -> 0.32: -1/turn
  - sewing shop 1 0.30 -> 0.24: -16/turn
  - weavery 1 0.50 -> 0.39: -2/turn
- Model check over the last 60 turns: predicted +126/turn for the settings we ran, real +50/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.38, garments 21.00, nets 32.78, beer 3.22, timber 3.38, prestige 60.14, cash 0.00
- Orders it would set: bread buy 5 (v2 7); cloth sell 1 (v2 none); firewood buy 1 (v2 3); grain buy 5 (v2 0); labour buy 29 (v2 16); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Essenbrucke (+4/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Amsdermund (+2/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 4.9/turn (+0.0 exported); plan makes 32.4 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 423 (+134 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.69 |
| ret | 3 | 0.91 | 0.94 |
| spin | 4 | 1.65 | 1.65 |
| weave | 3 | 0.50 | 1.26 |
| sew | 2 | 0.30 | 0.79 |

Buffers: flax fibres 74/77, thread 1050/225, cloth 72/126

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.42; ask over the cap 2.1 (60 coin per prestige)
- R7 stale ask: limestone ask 16.4 over the market for 6 turns: the town trades ~6 a turn at 15.8, we sold 0 with 46 over what we keep; floor 21.73 (config sell_floor / unit cost) is at or over the market: Taylor's call
