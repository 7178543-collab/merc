# v2 shadow report

Turn 14151, 2026-11-20 00:09. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,832, prestige 3,631 (511 free, -3.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 0 | 0 | 0 | 15 | 0 | stop 60, buy 30, buy @ 3.68 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 34 | 0 | 0 | 0 | 0 | stop 22, buy 6, buy @ 3.7 |
| labour | 65 | 65 | 507 | 0 | 58 | buy 65, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 4 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.74 is above it); knock-on: mansion 1 (no beer); labour need rises ~53/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.74 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 12.00 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 58 labour expired last turn (~122 coin): holding 65 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **beer**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **hold banquet 2 (fish)**: hold banquet 2 (fish) costs 60.3 coin per prestige at mansion, vs 72.7 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 12.00 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 507, not 593
- labour expiry guard: 58 bought labour expired last turn, buy 7 (not 7) this turn

## Prestige spending, cheapest coin per prestige first

250 turns left: prestige gained now converts 71.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 50.6 | 51.0 | needs a arena (build cost 28,604); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 51.8 | 52.4 | needs a arena (build cost 28,604); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 54.4 | 54.7 | needs a arena (build cost 28,604); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 2 | arena | 210 | 56.8 | 57.4 | needs a arena (build cost 28,604); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 59.6 | 59.6 | thin at home: pies |
| hold banquet 4 (pies) | mansion | 18 | 60.2 | 60.2 | thin at home: stockfish |
| hold banquet 2 (fish) | mansion | 6.8 | 60.3 | 60.3 |  |
| hold banquet 3 (pies) | mansion | 8 | 61.0 | 61.0 | thin at home: pies |
| maintain 1 | park | 0.5 | 62.4 | 62.4 | running |
| hold banquet 4 (premium) | mansion | 20 | 63.2 | 63.2 | thin at home: stockfish, premium ham |
| hold banquet 3 (fish) | mansion | 7.6 | 63.3 | 63.3 |  |
| hold mass 2 (premium) | cathedral | 360 | 57.2 | 63.7 | needs a cathedral (build cost 307,760); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 12.2 (keep 14); best orders clear only -1 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 16.4 (keep 14); best orders clear only -9 a turn after crew: ship stays at 0
- best towns now: Angefont +529, Gotthafen +478, Cobholme +347, Chatgnan +231, Clairlond +212
- Angefont would trade: furniture buy 46 @ 13.8, pasties buy 2 @ 15.9; crew 0.4

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~141 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Heidlowe | 662 | 0.25 | 0.30 (42/turn) | nets 5 (36.8->40.47), dyed cloth 4 (21->22.8), wrought iron 1 (18.17->24.89), blades 4 (19.95->21.28) | cloth 24 (11.13->18.9), copper ingots 7 (16.91->28.5), beer 43 (3.76->4.99), cured meat 7 (21.63->23.75) | +358 |
| Amsdermund | 1111 | 0.54 | 0.40 (56/turn) | blades 7 (19.95->22.61), nets 6 (36.8->40.28) | cloth 24 (9.92->18.9), copper ingots 3 (15.12->28.5), garments 2 (25.2->35.4), axes 3 (17.85->22.23) | +350 |
| Rouhomme | 368 | 0.14 | 0.80 (113/turn) | bread 227 (3.07->4.37), jewellery 2 (115.5->123.5), nets 6 (36.8->38.76), pies 2 (18.79->21.28) | cloth 20 (13.76->18.9), candles 1 (73.5->82.5), garments 2 (32.55->35.4), seeds 3 (1.94->2.58) | +344 |
| Fulkirch | 1576 | 0.89 | 0.30 (42/turn) | blades 7 (19.95->22.61), nets 6 (36.8->39.71) | cloth 23 (9.77->18.9), copper ingots 8 (14.8->28.5), garments 2 (30.24->35.4), candles 1 (77.7->82.5) | +328 |
| Dedlowe | 1146 | 0.56 | 0.60 (84/turn) | nets 4 (36.8->42.56), wrought iron 8 (18.17->18.81), salt 4 (6.2->6.79) | cloth 24 (11.34->18.9), copper ingots 8 (15.54->28.5), beer 50 (3.4->4.99), garments 2 (30.87->35.4) | +327 |

**Best:** Heidlowe at about +358 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 30 @ ?, stop 60 |  | uses 15.0/turn (household upkeep), makes 0.0, holds 0 = 0.0 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 8) |
| cured meat | 4 @ 26.2, stop 14 |  | goal planner: buys 4 a turn for today's rates, keeps up to 14 (v2 had None) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 16.3, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 34.2) |
| grain | 6 @ 3.7, stop 22 |  | goal planner: buys 6 a turn for today's rates, keeps up to 22 (v2 had 0) |
| labour | 65 @ 2.2, stop - |  | goal planner: buys 65 for today's rates (v2 had 7) |
| light armour | 1 @ 101, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 35.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.3k (cash + stock at home prices); +315/turn over 6 turns, +34/turn over 24 turns.
- Limits: cash flow >= -410/turn, prestige >= -0.88/turn (values are after 200 tax a turn).
- Today's settings: value -155/turn, cash -169/turn, prestige +0.93/turn.
- Plan: value +32/turn, cash -204/turn, prestige -0.88/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +180 vs -140, -168 vs -159, -158 vs -164.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Vauxvais: +5/turn
  - ship Flax Wyrm -> no route: +0/turn
  - mansion 1 1.00 -> 0.57: +115/turn
  - sewing shop 1 0.30 -> 0.11: +21/turn
  - weavery 1 0.50 -> 0.80: +15/turn
  - ropewalk 1 0.25 -> 0.02: +11/turn
  - spinnery 1 1.65 -> 1.40: +10/turn
  - retting pit 1 0.91 -> 0.79: -1/turn
  - flax farm 1 4.64 -> 3.98: +8/turn
- Model check over the last 59 turns: predicted +12/turn for the settings we ran, real +90/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 2.02, thread 5.07, cloth 8.10, flax fibres 6.01, garments 23.44, nets 33.60, beer 3.57, timber 3.69, prestige 66.81, cash 0.00
- Orders it would set: bread buy 5 (v2 8); cured meat buy 4 (v2 None); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 6 (v2 0); labour buy 65 (v2 7); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Vauxvais (+13/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +101/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

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

Buffers: flax fibres 91/77, thread 1058/228, cloth 73/128

## Self-diagnosis

- R1: beer slot dry: 0.0 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 30 @ 3.68, home ask none (no sellers at home)
- R1: cured meat slot dry: 10.7 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 4 @ 26.2, home ask 25.6; our bid is already at/over the ask (sellers too thin)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.74; ask over the cap 2.1 (60 coin per prestige)
- R1: prestige rate -3.27 a turn vs 12-turn median -1.13; likely: dry slot: beer, cured meat, firewood; mansion 1 projected 0 (beer)
- R2: spinnery 1 blocked by thread space: 1058 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
