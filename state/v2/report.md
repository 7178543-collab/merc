# v2 shadow report

Turn 14153, 2026-11-20 02:27. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,804, prestige 3,624 (504 free, -3.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 32 | 0 | 0 | 15 | 0 | stop 60, buy 39, buy @ 4.78 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 34 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 65 | 65 | 484 | 0 | 81 | buy 65, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.84 is above it); knock-on: mansion 1 (no beer); labour need rises ~53/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.84 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.30 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 81 labour expired last turn (~168 coin): holding 65 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: home ask 2.88 is above our ceiling 2.60 and last turn bought 0 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.30 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 94 over real use lately; planning 524, not 619
- labour expiry guard: 81 bought labour expired last turn, buy 0 (not 24) this turn

## Prestige spending, cheapest coin per prestige first

248 turns left: prestige gained now converts 71.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 51.0 | 51.4 | needs a arena (build cost 28,638); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 52.6 | 53.2 | needs a arena (build cost 28,638); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 54.8 | 55.2 | needs a arena (build cost 28,638); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 2 | arena | 210 | 57.6 | 58.3 | needs a arena (build cost 28,638); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 60.7 | 60.7 | thin at home: stockfish, cheese, candles |
| hold banquet 2 (pies) | mansion | 7 | 60.8 | 60.8 | thin at home: cheese, pies, candles |
| hold banquet 3 (pies) | mansion | 8 | 61.6 | 61.6 | thin at home: cheese, pies, candles |
| hold banquet 2 (fish) | mansion | 6.8 | 61.8 | 61.8 | thin at home: cheese |
| maintain 1 | park | 0.5 | 61.8 | 61.8 | running |
| hold banquet 4 (premium) | mansion | 20 | 62.9 | 62.9 | thin at home: stockfish, candles |
| hold banquet 1 (fish) | mansion | 4.2 | 63.6 | 63.6 | thin at home: beer |
| hold banquet 3 (fish) | mansion | 7.6 | 64.4 | 64.4 | thin at home: cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 12.3 (keep 14); best orders clear only -7 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 15.9 (keep 14); best orders clear only -1 a turn after crew: ship stays at 0
- best towns now: Cobholme +354, Fulkirch +318, Großmühle +236, Nürnnieder +211, Clairlond +190
- Cobholme would trade: furniture buy 40 @ 14.2; crew 1.0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~134 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.40 (54/turn) | bread 231 (3.02->4.33), thread 92 (6.3->6.84), pies 2 (14.38->19), tiles 3 (3.68->6.55) | cured meat 5 (20.16->23.56), cloth 4 (12.08->15.7), cheese 6 (6.77->8.26), yarn 2 (7.98->9.79) | +383 |
| Heilegg | 826 | 0.30 | 0.30 (40/turn) | flour 4 (21->26.79), pies 2 (14.38->19.19), wine 9 (6.51->7.65), beer 2 (4.78->6.32) | cloth 24 (10.34->15.7), yarn 28 (7.46->9.79), tools 27 (6.41->7.12), salt 7 (3.89->5.56) | +249 |
| Amsdermund | 1111 | 0.51 | 0.50 (67/turn) | nets 6 (36.8->40.09), pies 2 (14.38->20.14), hides 4 (13.76->15.86) | cloth 24 (9.77->15.7), garments 2 (25.83->33.6), dyed cloth 3 (14.91->19.95), yarn 5 (7.3->9.79) | +235 |
| Großaue | 1136 | 0.53 | 0.20 (27/turn) | malt 2 (7.09->11.97), flax fibres 4 (6.17->7.98), wine 2 (6.51->7.22) | cloth 24 (10.03->15.7), ham 2 (96.6->116.85), yarn 6 (6.56->9.79), cheese 6 (5.72->8.26) | +220 |
| Dedlowe | 1146 | 0.53 | 0.70 (94/turn) | nets 2 (36.8->41.23), pies 1 (14.38->17.29) | cloth 24 (10.92->15.7), yarn 29 (6.41->9.79), garments 2 (27.93->33.6), beer 52 (3.4->4.54) | +209 |

**Best:** Grandgues at about +383 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 35.6, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 3.0 turns |
| beer | 29 @ 5.1, stop 60 |  | uses 15.0/turn (household upkeep), makes 0.0, holds 32 = 2.1 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 7) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 32.4) |
| grain | 0 @ 3.7, stop 22 |  | goal planner: buys 0 a turn for today's rates, keeps up to 22 (v2 had 0) |
| labour | 65 @ 2.2, stop - |  | goal planner: buys 65 for today's rates (v2 had 0) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 35.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.7k (cash + stock at home prices); +347/turn over 6 turns, +25/turn over 24 turns.
- Limits: cash flow >= -367/turn, prestige >= -0.85/turn (values are after 200 tax a turn).
- Today's settings: value -167/turn, cash -177/turn, prestige +0.96/turn.
- Plan: value -2/turn, cash +3/turn, prestige -0.85/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -158 vs -164, -383 vs -169, -644 vs -178 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Donaunieder: +12/turn
  - ship Flax Wyrm -> no route: +0/turn
  - mansion 1 1.00 -> 0.57: +115/turn
  - ropewalk 1 0.25 -> 0.16: +11/turn
  - spinnery 1 1.65 -> 1.28: +12/turn
  - retting pit 1 0.91 -> 0.81: +3/turn
  - flax farm 1 4.64 -> 4.08: +7/turn
  - net maker 0.00 -> 0.29: +2/turn
  - weavery 1 0.50 -> 0.43: -17/turn
- Model check over the last 59 turns: predicted -2/turn for the settings we ran, real +91/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.55, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.67, beer 3.38, timber 3.69, prestige 65.79, cash 0.00
- Orders it would set: bread buy 5 (v2 7); cured meat buy 4 (v2 None); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 6 (v2 0); labour buy 65 (v2 0); light armour buy 1 (v2 None); rope sell 1 (v2 none)
- Ship linen snake: Grandgues -> Donaunieder (+12/turn over staying).
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

Buffers: flax fibres 92/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R1: beer slot dry: 32.0 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 39 @ 4.78, home ask 4.86 (held back: acted on beer at turn 14152 (one action per 2 turns))
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.84; ask over the cap 2.1 (60 coin per prestige)
- R1: prestige rate -3.24 a turn vs 12-turn median -1.13; likely: dry slot: beer, firewood
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
- R5: tar buy not filling: bid 11 under the home ask 11.3 for 3 turns, bought 0.0 of 1, 0.0 held (0.0 turns); raise needs Taylor (ceiling 11.0)
