# v2 shadow report

Turn 13999, 2026-11-13 16:50. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,309, prestige 3,490 (370 free, +2.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 100 | 39 | 19 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 116, buy 39, buy @ 3.76 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 64 | 64 | 532 | 0 | 32 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 3.12 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.12 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.20 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 32 labour expired last turn (~59 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **cured meat**: home ask 30.00 is above our ceiling 29.00 and last turn bought 4 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.20 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +0 crew for linen snake (crew 0.01, no projection from the game)
- labour: projection runs 100 over real use lately; planning 532, not 619
- labour expiry guard: 32 bought labour expired last turn, buy 32 (not 32) this turn

## Prestige spending, cheapest coin per prestige first

402 turns left: prestige gained now converts 86.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 55.2 | 55.2 | running |
| jousting 3 | arena | 230 | 55.7 | 56.1 | needs a arena (build cost 29,190); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| jousting 2 | arena | 210 | 61.0 | 61.4 | needs a arena (build cost 29,190); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 61.6 | 61.6 | thin at home: pies, candles |
| hold banquet 4 (pies) | mansion | 18 | 63.0 | 63.0 | thin at home: hop beer, stockfish, pies, candles |
| hold banquet 4 (premium) | mansion | 20 | 63.1 | 63.1 | thin at home: hop beer, stockfish, candles |
| hold mass 2 (premium) | cathedral | 360 | 61.3 | 64.5 | needs a cathedral (build cost 319,470); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 3 (pies) | mansion | 8 | 66.8 | 66.8 | thin at home: hop beer, pies, candles |
| hold banquet 4 | mansion | 17.5 | 66.8 | 66.8 | thin at home: hop beer, stockfish, candles |
| hold banquet 2 (fish) | mansion | 6.8 | 67.1 | 67.1 | thin at home: cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 67.3 | 67.3 | thin at home: cured fish |
| jousting 1 | arena | 170 | 68.9 | 69.3 | needs a arena (build cost 29,190); thin at home: protection, light armour, arms; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: cured meat buy 6 @ 23.8, pasties buy 3 @ 15.4; crew 0.1; est +37 a turn; stock: pasties 3 @ 15.4 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 14.0 (keep 14); best orders clear only 9 a turn after crew: ship stays at 0
- best towns now: Neuborn +45, Hofkirchen +44, Gottweiler +44, Großmühle +43, Karlmoor +43
- Neuborn would trade: cured meat buy 6 @ 22.4, pasties buy 3 @ 15.5; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~112 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.60 (67/turn) | timber 27 (9.29->12.06), firewood 34 (3.28->6.17), wine 10 (6.93->7.69), casks 3 (6.93->7.98) | cured meat 6 (24.57->30), cured fish 7 (26.46->28.12), garments 2 (22.68->24.2), tools 8 (4.91->5.32) | +173 |
| Vauxvais | 204 | 0.06 | 0.20 (22/turn) | flour 6 (22.68->32.11), charcoal 19 (2.29->4.01), glassware 2 (88.73->92.15), beer 3 (3.7->4.56) | cured fish 7 (24.15->28.12), cured meat 6 (25.41->30), flax fibres 12 (5.78->6.65), furniture 1 (13.65->15.4) | +153 |
| Hanstein | 380 | 0.11 | 0.40 (45/turn) | charcoal 16 (2.29->4.41), timber 12 (9.29->11.49), tallow 1 (21.63->25.84) | cured meat 6 (24.36->30), cured fish 5 (24.57->28.12), seeds 17 (1.8->2.51), dyed cloth 7 (11.45->12.54) | +108 |
| Kirchwerp | 1072 | 0.40 | 0.60 (67/turn) | thread 101 (4.78->5.7), lead ore 10 (7.51->10.45), flax fibres 2 (5.95->8.31), pickaxes 1 (13.23->15.2) | cured meat 6 (25.83->30), dyed cloth 7 (11.34->12.54), cloth 24 (7.56->8.1), garments 2 (22.26->24.2) | +105 |
| Essenbrucke | 584 | 0.17 | 0.10 (11/turn) | tapestries 1 (750.75->807.5), lead ore 4 (7.51->8.88), beer 3 (3.7->4.31), tallow 1 (21.63->22.8) | cured meat 6 (25.83->30), dyed cloth 7 (11.13->12.54), flax fibres 11 (6.04->6.65), steel ingots 1 (15.12->16.62) | +96 |

**Best:** Grandgues at about +173 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 36.0, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 3.0 turns |
| beer | 20 @ 3.98, stop 77 |  | uses 19.2/turn (household upkeep, mansion 1), makes 0.0, holds 100 = 5.2 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 7) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 9 = 1.5 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.0) |
| grain | 0 @ 3.7, stop 17 |  | goal planner: buys 0 a turn for today's rates, keeps up to 17 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 32) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 37.4) |
| pasties |  | 1 @ min 15.5 | goal planner: sells 1 a turn at 15.5, keeps 0 (no one offered it) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 29.7k (cash + stock at home prices); -128/turn over 6 turns, +35/turn over 24 turns.
- Limits: cash flow >= -430/turn, prestige >= -0.29/turn (values are after 200 tax a turn).
- Today's settings: value -174/turn, cash -143/turn, prestige +2.16/turn.
- Plan: value -4/turn, cash +13/turn, prestige -0.29/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -141 vs -157, -492 vs -146, -186 vs -147 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Neuborn: +7/turn
  - ship Flax Wyrm -> Vauxvais: +1/turn
  - mansion 1 1.00 -> 0.42: +140/turn
  - brewery 1 0.14 -> 0.07: +15/turn
  - spinnery 1 1.65 -> 1.37: +5/turn
  - net maker 0.00 -> 0.29: +2/turn
  - flax farm 1 4.64 -> 4.33: -1/turn
  - weavery 1 0.50 -> 0.40: -4/turn
  - sewing shop 1 0.30 -> 0.23: +8/turn
  - ropewalk 1 0.25 -> 0.00: -25/turn
- Model check over the last 60 turns: predicted +79/turn for the settings we ran, real +10/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.95, garments 19.30, nets 30.26, beer 3.18, timber 3.46, prestige 60.87, cash 0.00
- Orders it would set: bread buy 5 (v2 7); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 64 (v2 32); light armour buy 1 (v2 None); pasties sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.30, worth +9/turn.
- Ship linen snake: Grandgues -> Neuborn (+3/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Vauxvais (+1/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 418 (+129 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.10 |
| ret | 3 | 0.91 | 0.82 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 125/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 3.12; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
