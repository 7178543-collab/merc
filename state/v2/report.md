# v2 shadow report

Turn 14130, 2026-11-19 03:51. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,548, prestige 3,582 (462 free, -0.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 16 | 11 | 12 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 39, buy @ 3.94 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 1 | 0 | 0 | 1 | 0 | stop 7, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 34 | 0 | 0 | 0 | 0 | stop 18, buy 5, buy @ 3.7 |
| labour | 64 | 64 | 518 | 0 | 46 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), 3 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), but the home ask 2.76 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.76 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Waste (money lost now)

- **labour**: 46 labour expired last turn (~91 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 110 over real use lately; planning 528, not 638
- labour expiry guard: 46 bought labour expired last turn, buy 19 (not 28) this turn

## Prestige spending, cheapest coin per prestige first

271 turns left: prestige gained now converts 74.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 50.6 | 50.9 | needs a arena (build cost 28,899); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 54.3 | 54.7 | needs a arena (build cost 28,899); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 55.5 | 56.1 | needs a arena (build cost 28,899); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 58.3 | 58.3 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 59.1 | 59.1 |  |
| maintain 1 | park | 0.5 | 59.4 | 59.4 | running |
| hold banquet 3 (fish) | mansion | 7.6 | 61.3 | 61.3 | thin at home: hop beer |
| jousting 2 | arena | 210 | 60.8 | 61.4 | needs a arena (build cost 28,899); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 61.8 | 61.8 |  |
| hold banquet 3 (pies) | mansion | 8 | 62.0 | 62.0 | thin at home: hop beer |
| hold banquet 4 (pies) | mansion | 18 | 63.0 | 63.0 | thin at home: hop beer, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 63.4 | 63.4 | thin at home: hop beer, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.20 | 24 | 134102075 | 0.344 | - | furniture 2, pasties 2 | -61 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 11 @ 14.1; crew 0.1; est +123 a turn; stock: furniture 11 @ 14.1 (keep 145)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 16.3 (keep 14); best orders clear only -2 a turn after crew: ship stays at 0
- best towns now: Toqueque +142, Clairas +132, Vauxvais +130, Friedwerp +125, Caillechâtel +123
- Toqueque would trade: furniture buy 11 @ 12.8, pasties buy 2 @ 16.4; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~126 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 1.00 (126/turn) | bread 159 (2.77->4.26), firewood 36 (2.9->9.36), timber 25 (8.87->12.54), charcoal 19 (2.75->4.99) | acid 1 (131.25->148.2), garments 2 (33.18->37.2), candles 1 (79.28->83.5), beer 11 (3.53->3.78) | +575 |
| Helmgreen | 1354 | 0.64 | 0.30 (38/turn) | nets 5 (35.8->39.33), wine 11 (6.72->7.6), glassware 1 (83.48->85.5) | looms 1 (561.75->750.5), cloth 24 (10.71->12.8), garments 2 (28.77->37.2), dyed cloth 4 (14.6->17) | +259 |
| Hofkirchen | 991 | 0.40 | 0.40 (50/turn) | lathes 1 (182.7->214.7), flour 4 (22.26->30.78), thread 64 (5.15->5.7) | books 1 (609->669.75), cloth 24 (11.03->12.8), garments 2 (27.3->37.2), acid 1 (133.35->148.2) | +213 |
| Clairlond | 1288 | 0.60 | 0.20 (25/turn) | lathes 2 (182.7->199.5) | tapestries 1 (619.5->745.75), spinning wheels 1 (262.5->277.4), garments 2 (32.97->37.2), wax 8 (26.67->27.74) | +179 |
| Brunnham | 1281 | 0.59 | 0.30 (38/turn) | nets 6 (35.8->40.28), hides 4 (13.12->14.54) | books 1 (593.25->669.75), looms 1 (724.5->750.5), wax 12 (26.04->27.74), dyed cloth 4 (14.49->17) | +159 |

**Best:** Grandgues at about +575 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 24 @ 3.96, stop 47 |  | uses 11.7/turn (household upkeep), makes 0.0, holds 16 = 1.4 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 9) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (observed), makes 0.0, holds 3 = 0.5 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 25.8) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 19) |
| light armour | 1 @ 101, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 77.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 29.9k (cash + stock at home prices); +169/turn over 6 turns, +126/turn over 24 turns.
- Limits: cash flow >= -440/turn, prestige >= -0.67/turn (values are after 200 tax a turn).
- Today's settings: value -152/turn, cash -144/turn, prestige +1.69/turn.
- Plan: value +20/turn, cash +29/turn, prestige -0.67/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -503 vs -104, +39 vs -122, -118 vs -150.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Vauxvais: +2/turn
  - ship Flax Wyrm -> Donaunieder: +9/turn
  - mansion 1 1.00 -> 0.44: +137/turn
  - brewery 1 0.14 -> 0.08: +16/turn
  - spinnery 1 1.65 -> 1.40: +4/turn
  - retting pit 1 0.91 -> 0.79: +3/turn
  - flax farm 1 4.64 -> 3.98: +7/turn
  - net maker 0.00 -> 0.28: +1/turn
  - weavery 1 0.50 -> 0.41: -19/turn
- Model check over the last 60 turns: predicted +101/turn for the settings we ran, real +123/turn.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.38, garments 21.00, nets 32.64, beer 3.40, timber 3.58, prestige 62.88, cash 0.00
- Orders it would set: bread buy 5 (v2 9); cloth sell 1 (v2 none); firewood buy 1 (v2 3); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 64 (v2 19); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Vauxvais (+5/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Donaunieder (+4/turn over staying).
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

Buffers: flax fibres 77/77, thread 1050/228, cloth 73/128

## Self-diagnosis

- R1: beer slot dry: 16.4 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 39 @ 3.94, home ask 3.78; our bid is already at/over the ask (sellers too thin)
- R1: bread slot dry: 6.2 held, 4.2 a turn (basic food slot (+0.3 prestige)); our buy 5 @ 2.6, home ask none (no sellers at home)
- R1: firewood slot dry: 1.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.76; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
