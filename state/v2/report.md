# v2 shadow report

Turn 14082, 2026-11-17 03:43. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,595, prestige 3,599 (479 free, -2.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 17 | 5 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 5, buy @ 3.6 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 1 | 1 | 1 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 18, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 511 | 0 | 18 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.72 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.72 is above our ceiling 2.40 and last turn bought 1 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.5 turns of firewood left and buying 1 (need 5) -> v2: buy 5

## Waste (money lost now)

- **labour**: 18 labour expired last turn (~33 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Notes

- labour: projection runs 100 over real use lately; planning 511, not 611

## Prestige spending, cheapest coin per prestige first

319 turns left: prestige gained now converts 79.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 49.3 | 49.5 | needs a arena (build cost 27,858); thin at home: protection, light armour, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 50.1 | 50.5 | needs a arena (build cost 27,858); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 52.9 | 53.2 | needs a arena (build cost 27,858); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 54.6 | 54.6 | running |
| jousting 2 | arena | 210 | 54.8 | 55.3 | needs a arena (build cost 27,858); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 58.2 | 58.2 | thin at home: cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 58.8 | 58.8 | thin at home: wine, cured fish |
| hold banquet 2 (pies) | mansion | 7 | 61.0 | 61.0 | thin at home: wine |
| hold banquet 2 (meat) | mansion | 6.8 | 62.6 | 62.6 | thin at home: wine |
| hold banquet 1 (meat) | mansion | 4.2 | 63.5 | 63.5 |  |
| hold banquet 4 (premium) | mansion | 20 | 63.6 | 63.6 | thin at home: hop beer, wine, stockfish |
| hold banquet 4 (pies) | mansion | 18 | 63.7 | 63.7 | thin at home: hop beer, wine, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 15.9 (keep 14); best orders clear only -8 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 6 @ 16.0 (keep 14); best orders clear only 6 a turn after crew: ship stays at 0
- best towns now: Orlesailles +24, Heidlowe +21, Rouhomme +20, Hofkirchen +18, Herschweig +18
- Orlesailles would trade: pasties buy 6 @ 12.9; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~115 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.90 (104/turn) | timber 38 (8.24->12.35), firewood 31 (2.86->6.65), bread 161 (2.58->3.06), charcoal 19 (2.81->4.75) | bricks 5 (9.71->12.92), flax fibres 6 (6.77->7.55), candles 1 (81.9->82.5), thread 26 (5.46->5.55) | +328 |
| Fontaux | 411 | 0.13 | 0.70 (80/turn) | thread 48 (5.05->7.27), garments 10 (28.6->37.81), salt 16 (5.51->7.79), flour 3 (17.54->26.22) | tools 16 (5.15->6.03), bricks 7 (10.13->12.92) | +314 |
| Kirchwerp | 1072 | 0.41 | 0.60 (69/turn) | thread 91 (5.05->5.7), lead ore 9 (6.2->10.45), honey 9 (8.56->10.26), leather 1 (29.61->32.3) | cloth 24 (7.98->10.5), dyed cloth 8 (12.6->17), flax fibres 20 (5.78->7.55), garments 2 (25.2->29.2) | +171 |
| Amsdermund | 1111 | 0.44 | 0.30 (34/turn) | chisels 6 (12.29->13.3), flour 3 (17.54->21.47), tackles 1 (177.45->179.55) | cloth 24 (6.67->10.5), medicine 1 (131.25->157.7), dyed cloth 8 (13.44->17), candles 1 (73.5->82.5) | +166 |
| Pontmont | 341 | 0.10 | 1.00 (115/turn) | firewood 24 (2.86->9.5), bread 76 (2.58->3.1), tiles 0 (2.71->8.6), tar 0 (10.92->15.2) | bricks 5 (9.4->12.92), tools 7 (5.15->6.03), cookware 1 (21->24.13), slaked lime 1 (6.83->7.5) | +136 |

**Best:** Grandgues at about +328 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 35.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 3.62, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 7) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 7 |  | goal planner: buys 2 a turn for today's rates, keeps up to 7 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 16.8, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 27.8) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 11) |
| light armour | 1 @ 105, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 77.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 25.6k (cash + stock at home prices); +226/turn over 6 turns, +48/turn over 24 turns.
- Limits: cash flow >= -275/turn, prestige >= -0.75/turn (values are after 200 tax a turn).
- Today's settings: value +86/turn, cash +73/turn, prestige -2.57/turn - breaks the prestige floor.
- Plan: value +12/turn, cash +24/turn, prestige -0.75/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +151 vs +76, +18 vs +82, +164 vs +69.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Donaunieder: +20/turn
  - ship Flax Wyrm -> Hofkirchen: +0/turn
  - brewery 1 0.14 -> 0.08: +16/turn
  - spinnery 1 1.65 -> 1.39: +8/turn
  - net maker 0.00 -> 0.27: +1/turn
  - ropewalk 1 0.25 -> 0.32: -1/turn
  - flax farm 1 4.64 -> 4.37: -2/turn
  - weavery 1 0.50 -> 0.37: -21/turn
  - sewing shop 1 0.30 -> 0.23: -2/turn
  - mansion 1 0.00 -> 0.43: -78/turn
- Model check over the last 60 turns: predicted +37/turn for the settings we ran, real +22/turn.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.86, beer 3.38, timber 3.42, prestige 63.27, cash 0.00
- Orders it would set: bread buy 5 (v2 7); cloth sell 1 (v2 none); firewood buy 2 (v2 5); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 11); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Donaunieder (+20/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Hofkirchen (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new leatherworks (make leather armour 1) for ~4241 coin: +2/turn, payback 2054 turns, doesn't pay yet (materials thin at home: bricks, nails)

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

Buffers: flax fibres 85/77, thread 1050/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 1.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask 2.72; ask over the cap 2.1 (60 coin per prestige)
