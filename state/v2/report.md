# v2 shadow report

Turn 14114, 2026-11-18 11:47. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,668, prestige 3,612 (492 free, -2.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 16 | 4 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 9, buy @ 3.8 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 34 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 29 | 29 | 516 | 0 | 13 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Tuning

- **bread**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **candles**: home ask 82.00 is above our ceiling 76.00 and last turn bought 0 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 516, not 616

## Prestige spending, cheapest coin per prestige first

287 turns left: prestige gained now converts 76.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 41.4 | 41.7 | needs a arena (build cost 26,188); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 44.7 | 44.9 | needs a arena (build cost 26,188); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 53.1 | 53.1 | running |
| jousting 3 | arena | 230 | 53.0 | 53.5 | needs a arena (build cost 26,188); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 58.6 | 58.6 | thin at home: cured fish |
| jousting 2 | arena | 210 | 58.1 | 58.6 | needs a arena (build cost 26,188); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 60.1 | 60.1 | thin at home: cured fish |
| hold banquet 1 (meat) | mansion | 4.2 | 60.4 | 60.4 |  |
| hold banquet 2 (meat) | mansion | 6.8 | 61.0 | 61.0 |  |
| hold banquet 2 (pies) | mansion | 7 | 62.1 | 62.1 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 62.1 | 62.1 | thin at home: hop beer, cured fish |
| hold banquet 3 (pies) | mansion | 8 | 62.6 | 62.6 | thin at home: hop beer |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 11 | 151802239 | 0.128 | - | candles 2, pasties 8 | -286 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: candles 2 @ 78.0 (keep 12); best orders clear only 12 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Gotthafen +448, Hofkirchen +398, Bordees +356, Fulkirch +300, Cobholme +276
- Gotthafen would trade: furniture buy 42 @ 14.4, pasties buy 3 @ 14.9; crew 0.6

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~113 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 1.00 (113/turn) | firewood 33 (3.07->6.65), timber 31 (8.93->11.11), bread 161 (2.52->2.94), limestone 3 (13.76->24.7) | swords 2 (241.5->256.5), bricks 4 (7.98->10.16), cloth 4 (10.24->11), cheese 5 (6.35->6.46) | +292 |
| Gottweiler | 1135 | 0.44 | 0.40 (45/turn) | wrought iron 10 (18.69->23.56), tools 27 (5.99->7.03), nets 3 (35->38), furniture 8 (15.65->17.95) | glassware 4 (71.92->84.08), cloth 24 (8.82->11), swords 3 (241.5->256.5), wax 4 (26.88->28.5) | +212 |
| Amsdermund | 1111 | 0.43 | 0.30 (34/turn) | nets 6 (35->40.09), furniture 8 (15.65->20.33) | cloth 24 (7.35->11), swords 3 (241.5->256.5), wax 9 (24.36->28.5), garments 2 (27.3->29) | +207 |
| Hofkirchen | 991 | 0.36 | 0.40 (45/turn) | nets 6 (35->37.81), wine 3 (7.25->7.98) | glassware 4 (65.1->84.08), flax fibres 28 (5.62->7.55), cloth 24 (9.61->11), wax 9 (26.25->28.5) | +181 |
| Kirchwerp | 1072 | 0.41 | 0.20 (23/turn) | wrought iron 12 (18.69->27.55), nails 11 (8.09->9.5), lead ore 4 (6.56->10.45), leather 1 (29.82->32.3) | wax 11 (26.25->28.5), garments 2 (26.67->29), cookware 4 (21.63->22.23), salt 4 (3.89->4.64) | +147 |

**Best:** Grandgues at about +292 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 4.04, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 16 = 3.8 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 76.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 10 = 6.7 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 10 @ min 21 | goal planner: sells 10 at 21 (v2 had 10 at 25.8) |
| grain | 5 @ 3.7, stop 19 |  | goal planner: buys 5 a turn for today's rates, keeps up to 19 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 16) |
| light armour | 1 @ 102, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 74.5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 26.3k (cash + stock at home prices); -151/turn over 6 turns, +62/turn over 24 turns.
- Limits: cash flow >= -361/turn, prestige >= -0.80/turn (values are after 200 tax a turn).
- Today's settings: value +73/turn, cash +41/turn, prestige -2.67/turn - breaks the prestige floor.
- Plan: value +11/turn, cash +20/turn, prestige -0.80/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +224 vs +66, +32 vs +51, +36 vs +40.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Donaunieder: +22/turn
  - ship Flax Wyrm -> Brebronn: +2/turn
  - brewery 1 0.14 -> 0.08: +14/turn
  - net maker 0.00 -> 0.28: +4/turn
  - ropewalk 1 0.25 -> 0.33: +3/turn
  - spinnery 1 1.65 -> 1.47: -1/turn
  - retting pit 1 0.91 -> 0.84: +1/turn
  - flax farm 1 4.64 -> 4.23: +3/turn
  - weavery 1 0.50 -> 0.43: -8/turn
  - mansion 1 0.00 -> 0.45: -100/turn
- Model check over the last 60 turns: predicted +126/turn for the settings we ran, real +32/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.77, thread 4.45, cloth 7.10, flax fibres 5.27, garments 20.55, nets 32.12, beer 3.35, timber 3.92, prestige 59.42, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 1 (v2 3); grain buy 5 (v2 0); labour buy 29 (v2 16); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Donaunieder (+22/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Brebronn (+2/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 4.1/turn (+0.0 exported); plan makes 32.4 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 423 (+134 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.68 |
| ret | 3 | 0.91 | 0.94 |
| spin | 4 | 1.65 | 1.65 |
| weave | 3 | 0.50 | 1.26 |
| sew | 2 | 0.30 | 0.79 |

Buffers: flax fibres 74/77, thread 1049/225, cloth 73/126

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
