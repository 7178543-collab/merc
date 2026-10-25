# v2 shadow report

Turn 13548, 2026-10-25 21:58. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 2,012, prestige 3,575 (455 free, -2.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 54 | 0 | 7 | 0 | 0 | min_holding 60, sell 55, sell @ 2.98 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 6 | 0 | 1 | 4 | 0 | buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 2, sell @ 17.9 |
| grain | 87 | 0 | 0 | 0 | 0 | stop 81, buy 21, buy @ 3.7 |
| labour | 0 | 0 | 463 | 0 | 37 | buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 15 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 33.6 |
| porterage | 14 | 14 | 13 | 0 | 1 | buy 14, buy @ 1.1 |

**3 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: sewing shop 1 ran short of cloth (no buy order); labour need rises ~14/turn when they restart -> v2: add a cloth buy
- **firewood**: brewery 1 ran short of firewood (buy is live (no volume cap @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~57/turn when they restart -> v2: find out why the buy isn't filling
- **pasties**: only 0.8 turns of pasties left and buying 2 (need 5) -> v2: buy 5

## Tuning

- **flax plants**: flax plants buffer thin: 1.3 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 201
- **tar**: home ask 12.60 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **varnish**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 124 over real use lately; planning 463, not 573

## Prestige spending, cheapest coin per prestige first

853 turns left: prestige gained now converts 98.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 46.2 | 46.2 | running |
| hold banquet 3 (pies) | mansion | 8 | 47.4 | 47.4 | thin at home: hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 48.4 | 48.4 | thin at home: hop beer, wine, pies |
| hold banquet 2 (pies) | mansion | 7 | 50.1 | 50.1 | thin at home: wine, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 50.2 | 50.2 | thin at home: hop beer |
| hold banquet 3 (meat) | mansion | 7.6 | 51.4 | 51.4 | thin at home: hop beer, cured meat |
| hold banquet 4 | mansion | 17.5 | 51.8 | 51.8 | thin at home: wine, hop beer, ham, stockfish |
| hold banquet 2 (fish) | mansion | 6.8 | 52.1 | 52.1 | thin at home: wine |
| jousting 3 | arena | 230 | 52.9 | 53.1 | needs a arena (build cost 24,478); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 53.5 | 53.5 | thin at home: wine, cured meat |
| hold prayer 2 | chapel | 13 | 50.8 | 53.8 | needs a chapel (build cost 30,742) |
| hold sermon 2 (candles) | church | 31 | 51.6 | 54.3 | needs a church (build cost 62,969); thin at home: jewellery, candles, furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only -8 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -6 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~96 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Darmwald | 1022 | 0.32 | 0.20 (19/turn) | raw cloth 28 (7.14->11.59), tackles 1 (181.65->195.7), garments 1 (17.61->27.74), thread 26 (4.28->4.73) | pasties 2 (12.92->13.9) | +142 |
| Coburgbaum | 619 | 0.16 | 0.30 (29/turn) | furniture 12 (11.55->15.11), charcoal 11 (1.96->3.8), glass ingots 1 (60.38->65.08), resin 3 (2.31->2.7) | candles 1 (67.73->69), mouldboards 2 (32.34->33.06) | +42 |
| Grandgues | 152 | 0.04 | 0.30 (29/turn) | cookware 16 (23.73->24.89), charcoal 11 (1.96->2.81), tools 16 (4.18->4.6), timber 23 (6.77->7.5) | candles 1 (68.25->69), casks 2 (4.35->4.73), herbs 2 (37.8->38.19), pasties 2 (13.44->13.9) | +39 |
| Karlmoor | 787 | 0.20 | 0.20 (19/turn) | furniture 12 (11.55->13.49), salt 13 (4.79->5.7), tools 9 (4.18->4.67), nets 2 (35.8->37.24) | candles 1 (68.25->69), premium cheese 1 (28.98->30.21), beer 6 (3.26->3.68) | +31 |
| Clarfranche | 1484 | 0.56 | 0.20 (19/turn) | lead bars 8 (15.54->17.67), tackles 1 (181.65->195.7), spinning wheels 2 (252->256.5), scythes 1 (24.15->25.46) | gears 2 (55.65->58.42), nails 2 (4.94->5.94) | +30 |

**Best:** Darmwald at about +142 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| cured meat | 1 @ 29.0, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 2) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 0 @ 2.4, stop 10 |  | uses 4.8/turn (household upkeep), makes 6.5, holds 6 |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| grain | 29 @ 3.7, stop 115 |  | goal planner: buys 29 a turn for today's rates, keeps up to 115 (v2 had 43) |
| labour | 0 @ 2.2, stop - |  | goal planner: buys 0 for today's rates (v2 had 0) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 10 @ min 33.6 | goal planner: sells 10 at 33.6 (v2 had 10 at 34.8) |
| pasties | 2 @ 14.5, stop 6 |  | goal planner: buys 2 a turn for today's rates, keeps up to 6 (v2 had 5) |
| porterage | 14 @ 1.1, stop - |  | goal planner: buys 14 for today's rates (v2 had 13) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 74.0) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 0 = 2.0 turns |
| thread |  | 18 @ min 4.28 | goal planner: sells 18 a turn at 4.28, keeps 180 (no one offered it) |
| tools | 3 @ 6.2, stop 21 |  | uses 2.5/turn (net maker152202386007001, retting pit 1), makes 0.0, holds 200 = 79.3 turns |
| varnish | 1 @ ?, stop 1 |  | uses 0.1/turn (net maker152202386007001), makes 0.0, holds 1 = 4.4 turns |
| wax | 1 @ 23.0, stop 1 |  | uses 0.1/turn (net maker152202386007001), makes 0.0, holds 1 = 7.3 turns |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 18.2k (cash + stock at home prices); -59/turn over 6 turns, +16/turn over 24 turns.
- Limits: cash flow >= +83/turn, prestige >= -0.64/turn (values are after 220 tax a turn).
- Today's settings: value +96/turn, cash +39/turn, prestige -2.11/turn - breaks the prestige floor and cash floor.
- Plan: value +112/turn, cash +112/turn, prestige -0.64/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -44 vs +43, -198 vs +55, -337 vs +55 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Vauxvais: +3/turn
  - ship Flax Wyrm -> Orlesailles: +2/turn
  - ropewalk 1 0.25 -> 0.70: +44/turn
  - spinnery 1 1.59 -> 2.10: +18/turn
  - retting pit 1 1.12 -> 1.03: +7/turn
  - logging camp w/ tool 5.00 -> 3.75: +1/turn
  - net maker 0.23 -> 0.00: +0/turn
  - weavery 1 0.13 -> 0.26: +10/turn
  - sewing shop 1 0.09 -> 0.15: +13/turn
  - mansion 1 0.15 -> 0.50: -77/turn
- Model check over the last 54 turns: predicted +106/turn for the settings we ran, real +36/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.54, thread 3.79, cloth 6.10, flax fibres 4.36, garments 17.73, nets 16.11, beer 2.81, timber 3.17, prestige 54.85, cash 0.00
- Orders it would set: arms buy 1 (v2 None); cured meat buy 1 (v2 2); furniture buy 2 (v2 None); grain buy 29 (v2 43); light armour buy 1 (v2 None); pasties buy 2 (v2 5); porterage buy 14 (v2 13); rope sell 2 (v2 1); thread sell 18 (v2 none)
- Ship linen snake: Grandgues -> Vauxvais (+3/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Orlesailles (+2/turn over staying).
- Management: ~12.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +77/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new chandlery (make candles 2) for ~4108 coin: +8/turn, payback 511 turns, doesn't pay yet (materials thin at home: bricks, nails)
- Trim: donate logging camp w/ tool: +17/turn (tax 20 saved).

## Chain sizing

Mode HOLD, garments sold 1.3/turn (+0.0 exported); plan makes 32.0 garments a turn.
Labour: own 500, everything else 394, chain may buy 350 -> chain allowance 456, chain plan 403 (+161 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.88 | 3.63 |
| ret | 3 | 1.12 | 0.65 |
| spin | 4 | 1.59 | 1.72 |
| weave | 3 | 0.13 | 1.25 |
| sew | 2 | 0.09 | 0.78 |

Buffers: flax fibres 158/79, thread 1051/232, cloth 0/125

## Self-diagnosis

- R2: spinnery 1 blocked by thread space: 1051 held of 1084 capacity, we make 79.8 a turn; no buy on it: add a sell order or more capacity for thread
