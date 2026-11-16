# v2 shadow report

Turn 14078, 2026-11-16 23:10. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,004, prestige 3,609 (489 free, -2.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 18 | 0 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 5, buy @ 3.64 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 18, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 511 | 0 | 18 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.84 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.84 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **labour**: 18 labour expired last turn (~34 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Notes

- labour: projection runs 103 over real use lately; planning 511, not 611

## Prestige spending, cheapest coin per prestige first

323 turns left: prestige gained now converts 80.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 50.0 | 50.4 | needs a arena (build cost 28,809); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| jousting 2 | arena | 210 | 54.7 | 55.2 | needs a arena (build cost 28,809); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 55.8 | 55.8 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 58.4 | 58.4 | thin at home: cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 60.6 | 60.6 | thin at home: wine, cured fish |
| hold banquet 2 (pies) | mansion | 7 | 61.5 | 61.5 | thin at home: wine |
| hold banquet 3 (pies) | mansion | 8 | 64.1 | 64.1 | thin at home: hop beer |
| hold banquet 4 (premium) | mansion | 20 | 64.1 | 64.1 | thin at home: hop beer, wine, stockfish |
| hold banquet 4 (pies) | mansion | 18 | 64.2 | 64.2 | thin at home: hop beer, wine, stockfish |
| hold banquet 3 (fish) | mansion | 7.6 | 64.9 | 64.9 | thin at home: hop beer, cured fish |
| hold banquet 1 (meat) | mansion | 4.2 | 65.5 | 65.5 |  |
| hold banquet 2 (meat) | mansion | 6.8 | 65.9 | 65.9 | thin at home: wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 15.9 (keep 14); best orders clear only -9 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 16.3 (keep 14); best orders clear only -6 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~116 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 1.00 (116/turn) | timber 41 (7.82->12.35), firewood 32 (2.98->6.65), looms 1 (588->650.75), charcoal 19 (2.37->4.75) | bricks 6 (8.82->11.4), cloth 4 (9.5->10), thread 35 (5.46->5.55), tools 6 (5.12->5.42) | +345 |
| Amsdermund | 1111 | 0.44 | 0.40 (46/turn) | chisels 2 (11.34->13.3) | cloth 24 (6.67->10), dyed cloth 12 (12.6->17.95), garments 2 (22.47->31.2), flax fibres 12 (5.78->7.25) | +173 |
| Kirchwerp | 1072 | 0.42 | 0.50 (58/turn) | lead ore 9 (6.62->10.45) | dyed cloth 12 (10.92->17.95), cloth 24 (7.98->10), flax fibres 22 (5.78->7.25), ploughs 2 (73.5->83.12) | +171 |
| Birkeningen | 1006 | 0.38 | 1.00 (116/turn) | looms 1 (588->674.5), beer 54 (3.61->5.27), charcoal 19 (2.37->5.94), nets 5 (34.6->36.29) | medicine 1 (142.8->157.7), jewellery 1 (89.25->92.62), cookware 3 (24.36->25.46) | +164 |
| Blanans | 297 | 0.09 | 0.20 (23/turn) | looms 1 (588->622.25), limestone 2 (23.1->30.02), rope 1 (79->84.55), salt 3 (5.41->6.79) | dyed cloth 7 (13.12->17.95), premium ham 1 (239.4->260.3), tapestries 1 (771.75->793.25), bricks 11 (7.93->11.4) | +151 |

**Best:** Grandgues at about +345 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 3.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 18 = 4.2 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 89.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 17, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 30.2) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 11) |
| light armour | 1 @ 102, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 34.0 |  |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 77.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 24.6k (cash + stock at home prices); +248/turn over 6 turns, +20/turn over 24 turns.
- Limits: cash flow >= -250/turn, prestige >= -0.79/turn (values are after 200 tax a turn).
- Today's settings: value +91/turn, cash +78/turn, prestige -2.66/turn - breaks the prestige floor.
- Plan: value +9/turn, cash +17/turn, prestige -0.79/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +122 vs +84, -174 vs +85, +102 vs +80.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Donaunieder: +28/turn
  - ship Flax Wyrm -> Rouhomme: +0/turn
  - brewery 1 0.14 -> 0.08: +15/turn
  - spinnery 1 1.65 -> 1.39: +8/turn
  - net maker 0.00 -> 0.28: +1/turn
  - flax farm 1 4.64 -> 4.37: -0/turn
  - ropewalk 1 0.25 -> 0.32: -1/turn
  - weavery 1 0.50 -> 0.37: -19/turn
  - sewing shop 1 0.30 -> 0.23: -5/turn
  - mansion 1 0.00 -> 0.45: -84/turn
- Model check over the last 60 turns: predicted +14/turn for the settings we ran, real -47/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.38, garments 21.00, nets 32.80, beer 3.24, timber 3.35, prestige 65.09, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 11); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Donaunieder (+28/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Rouhomme (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new leatherworks (make leather armour 1) for ~4162 coin: +2/turn, payback 2450 turns, doesn't pay yet (materials thin at home: bricks, nails)

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 430 (+141 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.75 |
| ret | 3 | 0.91 | 0.95 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 92/77, thread 1050/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.84; ask over the cap 2.1 (60 coin per prestige)
