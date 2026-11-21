# v2 shadow report

Turn 14195, 2026-11-21 20:43. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,999, prestige 3,710 (590 free, +0.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 32 | 0 | 19 | 0 | 0 | min_holding 58, sell 15, sell @ 3.5 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 2 | 0 | 0 | 1 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 3 | 3 | 3 | 0 | 0 | stop 42, buy 3, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 34 | 6 | 0 | 0 | 0 | stop 35, buy 9, buy @ 3.7 |
| labour | 65 | 64 | 536 | 0 | 28 | buy 65, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 2 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **beer**: needed (19.2/turn) but there is NO buy order, stock 32.0 -> v2: add buy 39
- **firewood**: brewery 1 ran short of firewood (buy is live (4 @ 2.4), but the home ask 2.78 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.78 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Waste (money lost now)

- **labour**: 28 labour expired last turn (~56 coin): holding 65 against a ~0 buffer target -> v2: trim the buy until the stock is near 0
- **linen snake**: linen snake cost 12 coin last turn (crew 0.10) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell

## Tuning

- **bread**: home ask 3.00 is above our ceiling 2.60 and last turn bought 5 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 95 over real use lately; planning 561, not 656

## Prestige spending, cheapest coin per prestige first

206 turns left: prestige gained now converts 64.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 50.4 | 50.8 | needs a arena (build cost 28,954); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 52.8 | 53.6 | needs a arena (build cost 28,954); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 54.1 | 54.6 | needs a arena (build cost 28,954); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 2 | arena | 210 | 57.9 | 58.7 | needs a arena (build cost 28,954); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 59.4 | 59.4 | running |
| hold banquet 4 (premium) | mansion | 20 | 60.2 | 60.2 | thin at home: wine, stockfish, candles |
| hold banquet 4 (pies) | mansion | 18 | 61.1 | 61.1 | thin at home: wine, stockfish, cheese, candles |
| hold mass 2 (premium) | cathedral | 360 | 53.1 | 63.0 | needs a cathedral (build cost 307,385); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 4 | mansion | 17.5 | 65.7 | 65.7 | thin at home: wine, stockfish, cheese, candles |
| hold banquet 1 (fish) | mansion | 4.2 | 66.7 | 66.7 |  |
| hold banquet 3 (pies) | mansion | 8 | 67.8 | 67.8 | thin at home: cheese, candles |
| hold banquet 2 (pies) | mansion | 7 | 69.8 | 69.8 | thin at home: wine, cheese, candles |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 12 | 134102075 | 0 | - | pasties 6 | -74 |
| linen snake | 0.1 / 0.10 | 12 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 12.3 (keep 14); best orders clear only -6 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only 0 a turn after crew: ship stays at 0
- best towns now: Gotthafen +38, Friedwerp +36, Chatgnan +35, Bordees +35, Blanans +35
- Gotthafen would trade: cured meat buy 3 @ 30.0, furniture buy 2 @ 14.5, pasties buy 5 @ 14.9; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~126 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 1.00 (126/turn) | bread 263 (2.9->4.2), firewood 46 (2.92->9.03), charcoal 19 (2.73->7.03), thread 75 (6.75->7.03) | cheese 10 (11.03->13.96), cured meat 6 (31.5->32.4), garments 2 (32.13->34.8), dyed cloth 2 (14.7->15.39) | +673 |
| Rouhomme | 368 | 0.12 | 1.00 (126/turn) | beer 108 (4.22->5.79), bread 219 (2.9->3.8), thread 18 (6.75->7.41), flour 3 (21.63->23.75) | tools 13 (5.04->6.37), ploughs 1 (74.03->78.85), garments 1 (32.55->34.8), candles 0 (75.6->77) | +315 |
| Kirchwerp | 1072 | 0.45 | 0.50 (63/turn) | thread 78 (6.75->9.5), varnish 3 (18.59->23.75), casks 7 (7.04->9.36), wine 5 (6.88->8.79) | cheese 10 (11.34->13.96), garments 2 (24.15->34.8), jewellery 2 (73.5->79.8), tools 16 (5.25->6.37) | +285 |
| Heilegg | 826 | 0.28 | 1.00 (126/turn) | beer 130 (4.22->5.89), garments 10 (34.2->37.05), flour 4 (21.63->26.79), varnish 3 (18.59->22.99) | cloth 24 (10.5->11.8), thread 37 (6.25->6.9), tools 16 (5.25->6.37) | +269 |
| Amsdermund | 1111 | 0.48 | 0.30 (38/turn) | windows 2 (840->878.75), canvas 2 (49.98->52.25), premium cheese 3 (36.54->38), varnish 2 (18.59->20.33) | cloth 24 (7.35->11.8), cheese 10 (8.35->13.96), garments 2 (23.52->34.8), tools 16 (5.25->6.37) | +267 |

**Best:** Grandgues at about +673 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 39 @ 4.36, stop 77 |  | uses 19.2/turn (household upkeep, mansion 1), makes 0.0, holds 32 = 1.7 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 9) |
| candles | 2 @ 77.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 11 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 15 = 2.5 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 3 @ 2.5, stop - |  | goal planner: buys 3 for today's rates (v2 had 3) |
| furniture | 2 @ 17.1, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 30.0) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 0) |
| labour | 65 @ 2.2, stop - |  | goal planner: buys 65 for today's rates (v2 had 61) |
| light armour | 1 @ 104, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 44.6) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 85.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.5k (cash + stock at home prices); +77/turn over 6 turns, +104/turn over 24 turns.
- Limits: cash flow >= -375/turn, prestige >= -1.21/turn (values are after 200 tax a turn).
- Today's settings: value -156/turn, cash -150/turn, prestige +0.75/turn.
- Plan: value +18/turn, cash +24/turn, prestige -1.21/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +165 vs -160, +114 vs -168, +35 vs -151.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Heidlowe: +15/turn
  - ship Flax Wyrm -> Angefont: +6/turn
  - mansion 1 1.00 -> 0.53: +147/turn
  - net maker 0.00 -> 0.29: +7/turn
  - spinnery 1 1.65 -> 1.30: -5/turn
  - retting pit 1 0.91 -> 0.82: +2/turn
  - flax farm 1 4.64 -> 4.12: +6/turn
  - sewing shop 1 0.30 -> 0.22: -10/turn
  - weavery 1 0.50 -> 0.36: +17/turn
- Model check over the last 59 turns: predicted -127/turn for the settings we ran, real +36/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.78, beer 3.37, timber 4.23, prestige 72.68, cash 0.00
- Orders it would set: bread buy 5 (v2 9); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 2 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 0); labour buy 65 (v2 61); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Heidlowe (+14/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Angefont (+6/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~2027 coin: +3/turn, payback 631 turns, doesn't pay yet (materials thin at home: limestone)

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 419 (+130 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.17 |
| ret | 3 | 0.91 | 0.83 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 119/77, thread 1050/228, cloth 72/128

## Self-diagnosis

- R1: beer slot dry: 32.0 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy none, home ask 4.16 -> **buy 39 @ 4.24 (ask 4.16, cap 14.4)** (ok)
- R1: firewood slot dry: 2.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask 2.78; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
