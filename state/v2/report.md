# v2 shadow report

Turn 14080, 2026-11-17 01:21. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,412, prestige 3,604 (484 free, -2.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 16 | 3 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 5, buy @ 3.6 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 18, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 510 | 0 | 19 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.80 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.80 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 10.50 x8, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 19 labour expired last turn (~36 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Notes

- labour: projection runs 100 over real use lately; planning 510, not 608

## Prestige spending, cheapest coin per prestige first

321 turns left: prestige gained now converts 80.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 47.0 | 47.2 | needs a arena (build cost 28,461); thin at home: protection, light armour, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 49.9 | 50.4 | needs a arena (build cost 28,461); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 50.5 | 50.8 | needs a arena (build cost 28,461); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 2 | arena | 210 | 54.7 | 55.2 | needs a arena (build cost 28,461); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 55.2 | 55.2 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 58.7 | 58.7 | thin at home: cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 60.3 | 60.3 | thin at home: wine, cured fish |
| hold banquet 2 (pies) | mansion | 7 | 62.3 | 62.3 | thin at home: wine |
| hold banquet 4 (pies) | mansion | 18 | 63.5 | 63.5 | thin at home: hop beer, wine, ham, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 64.2 | 64.2 | thin at home: hop beer, wine, ham, stockfish |
| hold banquet 3 (fish) | mansion | 7.6 | 64.7 | 64.7 | thin at home: hop beer, cured fish |
| hold banquet 3 (pies) | mansion | 8 | 65.0 | 65.0 | thin at home: hop beer |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 15.9 (keep 14); best orders clear only -9 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 16.0 (keep 14); best orders clear only 0 a turn after crew: ship stays at 0
- best towns now: Bordees +21, Disscester +17, Hofkirchen +17
- Bordees would trade: furniture buy 1 @ 14.4, pasties buy 4 @ 13.8; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~115 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.90 (104/turn) | timber 40 (7.88->12.35), firewood 31 (2.94->6.65), charcoal 19 (2.79->4.75), bread 161 (2.6->2.93) | bricks 5 (9.35->11.97), cookware 3 (26.88->29.07), beer 4 (3.36->3.62), candles 1 (82.42->83.5) | +319 |
| Kirchwerp | 1072 | 0.41 | 0.50 (58/turn) | steel ingots 10 (19.53->26.03), lead ore 9 (6.41->10.45), lead bars 6 (10.82->13.11), blades 4 (16.91->17.86) | cloth 24 (7.98->10.3), dyed cloth 8 (12.6->16.53), flax fibres 21 (5.78->7.35), cookware 3 (23.73->29.07) | +223 |
| Amsdermund | 1111 | 0.44 | 0.40 (46/turn) | lead bars 6 (10.82->13.49), chisels 2 (12.81->13.3) | cloth 24 (6.67->10.3), dyed cloth 8 (12.5->16.53), cookware 3 (23.31->29.07), garments 2 (25.2->31.4) | +166 |
| Fontaux | 411 | 0.13 | 0.70 (81/turn) | salt 14 (5.41->7.79), garments 10 (30.8->33.44), thread 49 (5.05->5.65), timber 18 (7.88->10.64) | cookware 3 (26.67->29.07), ploughs 1 (75.08->83.12), flax plants 3 (1.08->1.42) | +151 |
| Heilegg | 826 | 0.26 | 0.60 (69/turn) | charcoal 19 (2.79->6.03), lead ore 7 (6.41->9.12), grindstones 1 (279.3->296.4), nets 5 (34.2->35.53) | dyed cloth 8 (10.08->16.53), cloth 24 (9.35->10.3), cookware 3 (23.31->29.07), garments 2 (26.25->31.4) | +148 |

**Best:** Grandgues at about +319 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 37.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 3.8, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 16 = 3.9 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 8) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 17.2, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 30.0) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 10) |
| light armour | 1 @ 106, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 34.0 |  |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 25.1k (cash + stock at home prices); +237/turn over 6 turns, +29/turn over 24 turns.
- Limits: cash flow >= -267/turn, prestige >= -0.77/turn (values are after 200 tax a turn).
- Today's settings: value +94/turn, cash +82/turn, prestige -2.63/turn - breaks the prestige floor.
- Plan: value +15/turn, cash +27/turn, prestige -0.77/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +102 vs +80, +257 vs +78, +151 vs +76.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Donaunieder: +20/turn
  - ship Flax Wyrm -> Brebronn: +2/turn
  - brewery 1 0.14 -> 0.08: +15/turn
  - spinnery 1 1.65 -> 1.39: +8/turn
  - net maker 0.00 -> 0.28: +2/turn
  - ropewalk 1 0.25 -> 0.32: -1/turn
  - flax farm 1 4.64 -> 4.37: -1/turn
  - weavery 1 0.50 -> 0.37: -21/turn
  - sewing shop 1 0.30 -> 0.23: -3/turn
  - mansion 1 0.00 -> 0.44: -83/turn
- Model check over the last 60 turns: predicted +21/turn for the settings we ran, real -27/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.80, beer 3.38, timber 3.38, prestige 65.01, cash 0.00
- Orders it would set: bread buy 5 (v2 8); cloth sell 1 (v2 none); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 10); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Donaunieder (+20/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Brebronn (+2/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new leatherworks (make leather armour 1) for ~4303 coin: +2/turn, payback 1870 turns, doesn't pay yet (materials thin at home: bricks, nails)

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

Buffers: flax fibres 87/77, thread 1052/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.8; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1052 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
