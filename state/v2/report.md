# v2 shadow report

Turn 14124, 2026-11-18 21:53. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 15,183, prestige 3,586 (466 free, -2.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 16 | 4 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 9, buy @ 3.8 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 34 | 0 | 0 | 0 | 0 | stop 18, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 510 | 0 | 19 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **beer**: only 0.8 turns of beer left and buying 9 (need 39) -> v2: buy 39
- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 11.00 x17, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 19 labour expired last turn (~39 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 520, not 620

## Prestige spending, cheapest coin per prestige first

277 turns left: prestige gained now converts 75.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 49.5 | 49.8 | needs a arena (build cost 28,920); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 53.2 | 53.5 | needs a arena (build cost 28,920); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 54.2 | 54.7 | needs a arena (build cost 28,920); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 58.3 | 58.3 |  |
| maintain 1 | park | 0.5 | 58.5 | 58.5 | running |
| jousting 2 | arena | 210 | 59.4 | 60.0 | needs a arena (build cost 28,920); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold mass 2 (premium) | cathedral | 360 | 56.1 | 61.5 | needs a cathedral (build cost 305,370); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |
| hold banquet 2 (fish) | mansion | 6.8 | 62.1 | 62.1 | thin at home: cheese |
| hold banquet 3 (pies) | mansion | 8 | 62.9 | 62.9 | thin at home: hop beer, cheese |
| hold banquet 1 (meat) | mansion | 4.2 | 63.2 | 63.2 | running |
| hold banquet 3 (fish) | mansion | 7.6 | 63.2 | 63.2 | thin at home: hop beer, cheese |
| hold banquet 4 (premium) | mansion | 20 | 63.4 | 63.4 | thin at home: hop beer, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: candles 2 @ 77.5 (keep 12); best orders clear only 13 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 5 @ 16.0 (keep 14); best orders clear only 2 a turn after crew: ship stays at 0
- best towns now: Amsdermund +689, Fulkirch +319, Clairlond +299, Cobholme +298, Bordees +274
- Amsdermund would trade: furniture buy 63 @ 13.7, pasties buy 3 @ 15.6; crew 1.0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~121 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 1.00 (121/turn) | timber 30 (8.24->12.25), firewood 33 (3.07->6.03), charcoal 19 (2.77->5.61), bread 160 (2.77->3.06) | cheese 3 (6.93->8.5), chisels 1 (12.29->14.44), yarn 1 (6.88->9.21), tools 15 (5.67->5.79) | +256 |
| Fontaux | 411 | 0.13 | 0.60 (72/turn) | thread 54 (4.98->7.27), timber 26 (8.24->12.44), furniture 8 (14.18->17.67), premium ham 1 (243.6->250.8) | tools 22 (5.35->5.79), pasties 3 (11.87->13.49), cheese 3 (7.25->8.5), garments 2 (38.85->40.4) | +238 |
| Großaue | 1136 | 0.47 | 0.20 (24/turn) | leather 1 (23.31->30.4), raw cloth 17 (8.82->9.4), nets 1 (35.4->37.05), wine 5 (6.77->7.36) | cloth 24 (6.67->11), garments 2 (29.82->40.4), yarn 5 (6.25->9.21), chisels 1 (10.92->14.44) | +138 |
| Kirchwerp | 1072 | 0.43 | 0.50 (60/turn) | thread 94 (4.98->5.7), wine 24 (6.77->7.84), leather 1 (23.31->32.3), lead ore 1 (8.14->10.45) | garments 2 (26.67->40.4), wrought iron 9 (14.7->17.67), cookware 4 (19.43->22.04), cloth 16 (10.08->11) | +132 |
| Rouhomme | 368 | 0.12 | 0.60 (72/turn) | bread 160 (2.77->3.31), flour 3 (22.47->28.88), furniture 8 (14.18->16.15), casks 5 (6.35->7.69) | tools 22 (4.51->5.79), garments 2 (32.97->40.4), cloth 17 (10.4->11), cheese 3 (7.25->8.5) | +129 |

**Best:** Grandgues at about +256 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 39 @ 4.06, stop 77 |  | uses 19.2/turn (household upkeep, mansion 1), makes 0.0, holds 16 = 0.8 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 9) |
| candles | 2 @ 76.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 7 = 4.7 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 3 @ 29.0, stop 11 |  | goal planner: buys 3 a turn for today's rates, keeps up to 11 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 16.1, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 25.8) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 20) |
| light armour | 1 @ 100, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.9k (cash + stock at home prices); +248/turn over 6 turns, +106/turn over 24 turns.
- Limits: cash flow >= -466/turn, prestige >= -0.69/turn (values are after 200 tax a turn).
- Today's settings: value -148/turn, cash -140/turn, prestige +1.66/turn.
- Plan: value +18/turn, cash +27/turn, prestige -0.69/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +114 vs +78, +306 vs +85, +316 vs +75.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Karlmoor: +12/turn
  - ship Flax Wyrm -> Angefont: +4/turn
  - mansion 1 1.00 -> 0.44: +132/turn
  - brewery 1 0.14 -> 0.08: +15/turn
  - spinnery 1 1.65 -> 1.41: +4/turn
  - retting pit 1 0.91 -> 0.80: +2/turn
  - flax farm 1 4.64 -> 3.99: +8/turn
  - net maker 0.00 -> 0.28: +1/turn
  - ropewalk 1 0.25 -> 0.31: -1/turn
  - sewing shop 1 0.30 -> 0.25: -11/turn
- Model check over the last 60 turns: predicted +127/turn for the settings we ran, real +124/turn.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.77, beer 3.25, timber 3.98, prestige 60.53, cash 0.00
- Orders it would set: bread buy 5 (v2 9); cloth sell 1 (v2 none); cured meat buy 3 (v2 12); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 64 (v2 20); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Karlmoor (+18/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Angefont (+4/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 9.5/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 430 (+141 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.75 |
| ret | 3 | 0.91 | 0.95 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 72/77, thread 1052/228, cloth 72/128

## Self-diagnosis

- R1: beer slot dry: 16.1 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 9 @ 3.8, home ask 3.88 -> **buy 39 @ 3.94 (ask 3.88, cap 14.4)** (ok)
- R1: cured meat slot dry: 0.8 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 3 @ 29, home ask 23.6; our bid is already at/over the ask (sellers too thin)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1052 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
