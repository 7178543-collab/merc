# v2 shadow report

Turn 14150, 2026-11-19 23:03. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,991, prestige 3,634 (514 free, -3.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 0 | 0 | 0 | 15 | 0 | stop 77, buy 39, buy @ 3.68 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 7, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 34 | 0 | 0 | 0 | 0 | stop 19, buy 5, buy @ 3.7 |
| labour | 65 | 65 | 516 | 0 | 49 | buy 65, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), but the home ask 2.74 is above it); knock-on: mansion 1 (no beer); labour need rises ~53/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.74 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Waste (money lost now)

- **labour**: 49 labour expired last turn (~102 coin): holding 65 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **beer**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 516, not 610
- labour expiry guard: 49 bought labour expired last turn, buy 16 (not 16) this turn

## Prestige spending, cheapest coin per prestige first

251 turns left: prestige gained now converts 71.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 50.7 | 51.1 | needs a arena (build cost 28,521); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 52.0 | 52.6 | needs a arena (build cost 28,521); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 54.5 | 54.8 | needs a arena (build cost 28,521); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 2 | arena | 210 | 57.0 | 57.6 | needs a arena (build cost 28,521); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 59.2 | 59.2 | thin at home: cheese, pies |
| hold banquet 2 (fish) | mansion | 6.8 | 59.9 | 59.9 | thin at home: cheese |
| hold banquet 3 (pies) | mansion | 8 | 60.6 | 60.6 | thin at home: pies |
| hold banquet 4 (pies) | mansion | 18 | 61.2 | 61.2 | thin at home: stockfish, pies |
| maintain 1 | park | 0.5 | 62.4 | 62.4 | running |
| hold banquet 3 (fish) | mansion | 7.6 | 62.7 | 62.7 | thin at home: cheese |
| hold banquet 4 (premium) | mansion | 20 | 63.5 | 63.5 | thin at home: stockfish |
| hold banquet 2 (meat) | mansion | 6.8 | 63.7 | 63.7 | thin at home: cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 12 | 151802239 | 0.144 | - | pasties 4 | -66 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 12.0 (keep 14); best orders clear only -7 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Angefont +570, Cobholme +347, Fulkirch +297, Großmühle +249, Clairlond +217
- Angefont would trade: furniture buy 49 @ 14.0, pasties buy 6 @ 15.8; crew 0.4

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~141 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Rouhomme | 368 | 0.14 | 0.80 (113/turn) | bread 224 (3.09->4.54), thread 59 (5.75->6.79), flour 3 (23.94->33.82), nets 6 (36.8->39.14) | tools 20 (6.3->6.93), candles 1 (75.6->81.5), butter 1 (69.83->74.58), cookware 4 (24.15->24.51) | +363 |
| Amsdermund | 1111 | 0.54 | 0.90 (127/turn) | thread 73 (5.75->6.65), jewellery 2 (112.35->123.5), furniture 8 (16.7->20.9), nets 6 (36.8->39.9) | dyed cloth 13 (14.7->21.85), cloth 24 (10.03->12.4), beer 66 (3.26->4.62), garments 2 (28.35->36) | +282 |
| Grandgues | 152 | 0.06 | 0.40 (56/turn) | timber 36 (8.56->12.16), thread 91 (5.75->6.27), charcoal 19 (2.42->4.46), nets 2 (36.8->40.85) | cookware 4 (23.52->24.51), candles 1 (78.23->81.5), cloth 8 (11.97->12.4), garments 2 (35.49->36) | +189 |
| Kirchwerp | 1072 | 0.51 | 0.80 (113/turn) | steel ingots 7 (19.43->25.27), thread 91 (5.75->6.65), furniture 8 (16.7->22.61), pasties 7 (15.33->18.62) | garments 2 (27.3->36), axes 3 (17.85->19.19), belts 6 (32.55->33.82), lathes 1 (189->195.7) | +167 |
| Heilegg | 826 | 0.32 | 0.20 (28/turn) | wrought iron 7 (19.53->27.55), varnish 9 (17.12->18.62), rope 1 (73.5->84.08), cured fish 7 (24.57->25.65) | dyed cloth 13 (17.01->21.85), garments 2 (33.39->36), tools 20 (6.41->6.93), cloth 19 (12.08->12.4) | +154 |

**Best:** Rouhomme at about +363 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had None) |
| beer | 30 @ ?, stop 60 |  | uses 15.0/turn (household upkeep), makes 0.0, holds 0 = 0.0 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 6) |
| cured meat | 4 @ 25, stop 14 |  | goal planner: buys 4 a turn for today's rates, keeps up to 14 (v2 had None) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 17, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 33.8) |
| grain | 6 @ 3.7, stop 22 |  | goal planner: buys 6 a turn for today's rates, keeps up to 22 (v2 had 0) |
| labour | 65 @ 2.2, stop - |  | goal planner: buys 65 for today's rates (v2 had 16) |
| light armour | 1 @ 101, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 35.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 73.5) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.3/turn (ropewalk 1), makes 0.0, holds 0 = 0.3 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 29.4k (cash + stock at home prices); +143/turn over 6 turns, +10/turn over 24 turns.
- Limits: cash flow >= -416/turn, prestige >= -0.89/turn (values are after 200 tax a turn).
- Today's settings: value -153/turn, cash -164/turn, prestige +0.91/turn.
- Plan: value +31/turn, cash -208/turn, prestige -0.89/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +3 vs -122, +180 vs -140, -168 vs -159.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Angefont: +7/turn
  - ship Flax Wyrm -> no route: +0/turn
  - mansion 1 1.00 -> 0.57: +110/turn
  - sewing shop 1 0.30 -> 0.11: +20/turn
  - weavery 1 0.50 -> 0.81: +15/turn
  - ropewalk 1 0.25 -> 0.00: +12/turn
  - spinnery 1 1.65 -> 1.39: +10/turn
  - retting pit 1 0.91 -> 0.80: +1/turn
  - flax farm 1 4.64 -> 4.01: +7/turn
- HAND-OVER: goal planner: model check failed 3 runs in a row, rates handed back to the old rules.
- Model check over the last 59 turns: predicted +17/turn for the settings we ran, real +78/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 2.02, thread 5.07, cloth 8.10, flax fibres 6.00, garments 23.44, nets 33.60, beer 3.58, timber 3.69, prestige 65.11, cash 0.00
- Orders it would set: arms buy 1 (v2 None); bread buy 5 (v2 6); cured meat buy 4 (v2 None); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 6 (v2 0); labour buy 65 (v2 16); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Angefont (+7/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +101/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 426 (+137 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.53 |
| ret | 3 | 0.91 | 0.91 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 93/77, thread 1050/228, cloth 73/128

## Self-diagnosis

- R1: beer slot dry: 0.0 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 30 @ 3.68, home ask none (no sellers at home)
- R1: cured meat slot dry: 10.7 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 4 @ 25, home ask 24.4; our bid is already at/over the ask (sellers too thin)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.74; ask over the cap 2.1 (60 coin per prestige)
- R1: prestige rate -3.29 a turn vs 12-turn median -1.10; likely: dry slot: beer, cured meat, firewood; mansion 1 projected 0 (beer)
