# v2 shadow report

Turn 14128, 2026-11-19 01:09. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,627, prestige 3,582 (462 free, -0.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 17 | 12 | 12 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 39, buy @ 3.94 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 1 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 34 | 0 | 0 | 0 | 0 | stop 18, buy 5, buy @ 3.7 |
| labour | 64 | 64 | 526 | 0 | 38 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**5 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), 3 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), home ask 2.36 x2, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: only 0.9 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.10 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 38 labour expired last turn (~75 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: home ask 11.10 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +1 crew for Flax Wyrm (crew 0.01, no projection from the game)
- labour: projection runs 100 over real use lately; planning 526, not 603

## Prestige spending, cheapest coin per prestige first

273 turns left: prestige gained now converts 74.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 53.3 | 53.8 | needs a arena (build cost 28,594); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 58.0 | 58.0 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 58.8 | 58.8 |  |
| jousting 2 | arena | 210 | 58.4 | 59.0 | needs a arena (build cost 28,594); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 59.4 | 59.4 | running |
| hold banquet 2 (pies) | mansion | 7 | 61.7 | 61.7 |  |
| hold banquet 2 (meat) | mansion | 6.8 | 62.7 | 62.7 |  |
| hold banquet 1 (meat) | mansion | 4.2 | 63.4 | 63.4 | running |
| hold banquet 4 (pies) | mansion | 18 | 63.4 | 63.4 | thin at home: hop beer, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 63.8 | 63.8 | thin at home: hop beer, stockfish |
| hold banquet 3 (fish) | mansion | 7.6 | 64.3 | 64.3 | thin at home: hop beer |
| hold banquet 3 (pies) | mansion | 8 | 65.1 | 65.1 | thin at home: hop beer |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.10 | 12 | 134102075 | 0 | - | furniture 19 | -270 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 21 @ 14.1; crew 0.2; est +233 a turn; stock: furniture 21 @ 14.1 (keep 145)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: candles 1 @ 77.5 (keep 12); stock: pasties 2 @ 16.3 (keep 14); best orders clear only 5 a turn after crew: ship stays at 0
- best towns now: Vauxvais +333, Fulkirch +325, Amsdermund +324, Cobholme +287, Clairas +284
- Vauxvais would trade: candles buy 1 @ 73.0, furniture buy 26 @ 14.0, pasties buy 2 @ 15.7; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~126 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 1.00 (126/turn) | firewood 44 (2.48->8.88), bread 147 (2.69->3.76), timber 26 (8.61->12.25), charcoal 17 (2.79->5.84) | dyed cloth 5 (15.23->16.05), garments 1 (32.55->35), flax fibres 2 (7.46->8.93), wool 1 (13.55->14.91) | +527 |
| Fontaux | 411 | 0.14 | 0.90 (113/turn) | thread 48 (5.5->7.27), garments 10 (26.4->34.2), timber 40 (8.61->12.44), glassware 2 (82.95->90.25) | flax fibres 4 (7.04->8.93), yarn 1 (6.77->9.79), wrought iron 1 (15.12->16.72), cured meat 3 (23.31->23.6) | +274 |
| Clarfranche | 1484 | 0.73 | 0.20 (25/turn) | garments 10 (26.4->38.38), tackles 1 (159.6->179.55), raw cloth 1 (8.82->9.88) | yarn 10 (4.68->9.79), cookware 4 (17.12->23.18), axes 2 (14.38->17.76), wool 2 (12.08->14.91) | +206 |
| Bordetes | 831 | 0.29 | 0.10 (13/turn) | garments 10 (26.4->38), premium garments 1 (157.5->195.7), lathes 1 (199.5->222.3), nails 19 (7.98->8.31) | flax fibres 4 (7.09->8.93), casks 10 (5.17->5.84) | +178 |
| Großaue | 1136 | 0.50 | 0.40 (50/turn) | raw cloth 15 (8.82->10.64) | cloth 24 (8.29->12.2), yarn 9 (6.25->9.79), dyed cloth 6 (13.55->16.05), garments 2 (30.24->35) | +166 |

**Best:** Grandgues at about +527 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 31.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 24 @ 3.96, stop 47 |  | uses 11.7/turn (household upkeep), makes 0.0, holds 17 = 1.4 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 6) |
| candles | 2 @ 76.0, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had 2) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 3 @ 29.0, stop 11 |  | goal planner: buys 3 a turn for today's rates, keeps up to 11 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 16.1, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 25.8) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 26) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.6) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 29.1k (cash + stock at home prices); +237/turn over 6 turns, +99/turn over 24 turns.
- Limits: cash flow >= -443/turn, prestige >= -0.68/turn (values are after 200 tax a turn).
- Today's settings: value -130/turn, cash -122/turn, prestige +1.69/turn.
- Plan: value +38/turn, cash +48/turn, prestige -0.68/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +316 vs +75, +159 vs -140, -503 vs -104.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Toqueque: +1/turn
  - ship Flax Wyrm -> no route: -0/turn
  - mansion 1 1.00 -> 0.44: +133/turn
  - brewery 1 0.14 -> 0.08: +15/turn
  - spinnery 1 1.65 -> 1.42: +10/turn
  - net maker 0.00 -> 0.28: +1/turn
  - retting pit 1 0.91 -> 0.80: -1/turn
  - flax farm 1 4.64 -> 4.04: +7/turn
  - ropewalk 1 0.25 -> 0.32: -2/turn
  - sewing shop 1 0.30 -> 0.24: -7/turn
- Model check over the last 60 turns: predicted +114/turn for the settings we ran, real +112/turn.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.38, garments 21.00, nets 32.69, beer 3.25, timber 3.53, prestige 60.38, cash 0.00
- Orders it would set: bread buy 5 (v2 6); cloth sell 1 (v2 none); cured meat buy 3 (v2 12); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 64 (v2 26); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Toqueque (+1/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
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

Buffers: flax fibres 70/77, thread 1063/228, cloth 72/128

## Self-diagnosis

- R1: beer slot dry: 16.8 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 39 @ 3.94, home ask 3.78; our bid is already at/over the ask (sellers too thin)
- R1: firewood slot dry: 1.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.36; our bid is already at/over the ask (sellers too thin)
- R2: spinnery 1 blocked by thread space: 1063 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
