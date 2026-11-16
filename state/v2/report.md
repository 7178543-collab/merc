# v2 shadow report

Turn 14074, 2026-11-16 19:53. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,940, prestige 3,620 (500 free, -2.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 23 | 9 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 26, buy 9, buy @ 3.9 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 1 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 18, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 516 | 0 | 13 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: only 0.9 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Tuning

- **bread**: home ask 2.84 is above our ceiling 2.60 and last turn bought 5 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **candles**: home ask 86.50 is above our ceiling 76.00 and last turn bought 0 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 516, not 616

## Prestige spending, cheapest coin per prestige first

327 turns left: prestige gained now converts 80.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 49.4 | 49.8 | needs a arena (build cost 27,114); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 | arena | 210 | 54.1 | 54.6 | needs a arena (build cost 27,114); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 55.8 | 55.8 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 59.2 | 59.2 | thin at home: cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 60.1 | 60.1 | thin at home: wine, cured fish, cheese |
| hold banquet 2 (pies) | mansion | 7 | 61.8 | 61.8 | thin at home: wine, cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 63.4 | 63.4 | thin at home: hop beer, cured fish, cheese |
| hold banquet 4 (pies) | mansion | 18 | 63.4 | 63.4 | thin at home: hop beer, wine, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 63.8 | 63.8 | thin at home: hop beer, cheese |
| hold banquet 2 (meat) | mansion | 6.8 | 63.9 | 63.9 | thin at home: wine, cheese |
| hold banquet 4 (premium) | mansion | 20 | 64.0 | 64.0 | thin at home: hop beer, wine, stockfish |
| hold banquet 1 (meat) | mansion | 4.2 | 64.6 | 64.6 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 11 | 151802239 | 0.116 | - | candles 2, pasties 4 | -220 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: furniture 1 @ 14.5 (keep 145); stock: pasties 1 @ 14.8 (keep 14); best orders clear only 5 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 16.4 (keep 14); best orders clear only -8 a turn after crew: ship stays at 0
- best towns now: Amsdermund +120, Fulkirch +102, Brunnham +99, Bremcop +98, Chribruck +98
- Amsdermund would trade: candles buy 7 @ 71.0; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~115 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.80 (92/turn) | timber 35 (8.35->12.25), firewood 33 (2.48->6.6), charcoal 19 (2.86->4.94), limestone 3 (16.8->23.18) | dyed cloth 5 (14.6->19.19), tools 7 (4.85->5.61), bricks 1 (8.14->12.73), candles 1 (82.95->86.5) | +291 |
| Unterhufe | 595 | 0.18 | 0.30 (34/turn) | thread 85 (4.92->6.27), copper ingots 1 (15.23->15.48), garments 10 (26.4->26.6) | flax fibres 28 (4.81->7.25), premium ham 1 (224.7->260.3), dyed cloth 4 (16.8->19.19), candles 1 (79.8->86.5) | +218 |
| Amsdermund | 1111 | 0.44 | 0.40 (46/turn) | jewellery 6 (99.75->104.5), hides 4 (13.23->15.48), lead ore 1 (6.83->11.11), premium garments 1 (120.75->123.5) | cloth 24 (5.78->9.6), dyed cloth 6 (12.6->19.19), candles 1 (73.5->86.5), wax 4 (21.63->24.7) | +210 |
| Etallaen | 774 | 0.24 | 0.20 (23/turn) | garments 10 (26.4->35.53), cloth 12 (10.08->17.1), wool 2 (11.23->16.15) | dyed cloth 4 (16.59->19.19), flax fibres 8 (5.93->7.25), candles 1 (84->86.5), bricks 1 (7.14->12.73) | +194 |
| Vauxvais | 204 | 0.06 | 1.00 (115/turn) | firewood 54 (2.48->5.7), wax 11 (27.51->30.02), charcoal 19 (2.86->4.75), lead ore 4 (6.83->8.36) | dyed cloth 6 (14.28->19.19), flax fibres 6 (5.88->7.25), candles 1 (80.33->86.5), garments 2 (26.46->29) | +193 |

**Best:** Grandgues at about +291 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 4.04, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 23 = 5.6 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 9) |
| candles | 3 @ 76.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 4 = 2.7 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 16.1, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 23.0) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 16) |
| light armour | 1 @ 101, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 34.0 |  |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 77.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 23.7k (cash + stock at home prices); +225/turn over 6 turns, +4/turn over 24 turns.
- Limits: cash flow >= -247/turn, prestige >= -0.83/turn (values are after 200 tax a turn).
- Today's settings: value +79/turn, cash +66/turn, prestige -2.71/turn - breaks the prestige floor.
- Plan: value +1/turn, cash +9/turn, prestige -0.83/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -2 vs +76, +351 vs +81, +122 vs +84.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Amsdermund: +14/turn
  - ship Flax Wyrm -> Rouhomme: +0/turn
  - brewery 1 0.14 -> 0.08: +15/turn
  - spinnery 1 1.65 -> 1.38: +7/turn
  - net maker 0.00 -> 0.28: +1/turn
  - flax farm 1 4.64 -> 4.32: -0/turn
  - weavery 1 0.50 -> 0.38: -22/turn
  - sewing shop 1 0.30 -> 0.24: -6/turn
  - mansion 1 0.00 -> 0.45: -79/turn
- Model check over the last 60 turns: predicted -5/turn for the settings we ran, real -62/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.55, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.70, beer 3.38, timber 3.41, prestige 63.29, cash 0.00
- Orders it would set: bread buy 5 (v2 9); cloth sell 1 (v2 none); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 16); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Amsdermund (+14/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Rouhomme (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.4/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 423 (+134 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.40 |
| ret | 3 | 0.91 | 0.88 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 103/77, thread 1050/228, cloth 72/128

## Self-diagnosis

- R1: firewood slot dry: 1.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
