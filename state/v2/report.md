# v2 shadow report

Turn 14087, 2026-11-17 08:05. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,824, prestige 3,635 (515 free, -2.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 13 | 5 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 5, buy @ 3.56 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 18, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.66 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.66 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.40 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~80 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: home ask 11.40 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +1 crew for linen snake (crew 0.01, no projection from the game)
- labour: projection runs 100 over real use lately; planning 484, not 584

## Prestige spending, cheapest coin per prestige first

314 turns left: prestige gained now converts 79.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 50.0 | 50.4 | needs a arena (build cost 29,011); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 53.1 | 53.1 | running |
| jousting 2 | arena | 210 | 54.7 | 55.2 | needs a arena (build cost 29,011); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 58.4 | 58.4 | thin at home: cured fish |
| hold banquet 3 (pies) | mansion | 8 | 60.8 | 60.8 | thin at home: hop beer |
| hold banquet 3 (fish) | mansion | 7.6 | 61.1 | 61.1 | thin at home: hop beer, cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 61.4 | 61.4 | thin at home: wine, cured fish |
| hold banquet 1 (meat) | mansion | 4.2 | 62.6 | 62.6 |  |
| hold banquet 2 (pies) | mansion | 7 | 62.7 | 62.7 | thin at home: wine |
| hold banquet 4 (pies) | mansion | 18 | 62.7 | 62.7 | thin at home: hop beer, wine, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 62.7 | 62.7 | thin at home: hop beer, wine, stockfish |
| hold mass 2 (premium) | cathedral | 360 | 59.1 | 63.4 | needs a cathedral (build cost 302,360); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: pasties buy 11 @ 16.0; crew 0.1; est +20 a turn; stock: pasties 11 @ 16.0 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 16.3 (keep 14); best orders clear only -9 a turn after crew: ship stays at 0
- best towns now: Amsdermund +685, Hofkirchen +503, Bordees +386, Bedenis +358, Heidlowe +315
- Amsdermund would trade: furniture buy 63 @ 13.7; crew 1.0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~115 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.36 | 0.60 (69/turn) | tapestries 1 (603.75->783.75), swords 1 (200.55->222.3), lathes 1 (183.75->205.2) | cloth 24 (7.67->11.9), dyed cloth 7 (13.65->17.67), tools 15 (5.15->6.79), flax fibres 23 (5.78->7.2) | +399 |
| Amsdermund | 1111 | 0.44 | 0.40 (46/turn) | tapestries 1 (603.75->703), swords 1 (200.55->235.6), paper 6 (26.04->28.31), fleece 2 (8.29->9.03) | cloth 24 (5.72->11.9), dyed cloth 7 (12.6->17.67), wrought iron 7 (13.65->16.15), cheese 8 (5.99->7.12) | +350 |
| Kirchwerp | 1072 | 0.41 | 0.60 (69/turn) | tapestries 1 (603.75->750.5), swords 1 (200.55->250.8), wrought iron 9 (18.38->23.75), lead bars 6 (14.18->20.9) | flax fibres 23 (5.78->7.2), tools 15 (5.57->6.79), cured meat 6 (21->22.99), garments 2 (26.25->29.2) | +347 |
| Hanstein | 380 | 0.12 | 0.60 (69/turn) | tapestries 1 (603.75->793.25), timber 33 (8.03->11.59), salt 2 (5.78->8.31), flax fibres 3 (6.85->7.27) | cloth 24 (11.03->11.9), bricks 5 (7.72->13.01), dyed cloth 5 (15.12->17.67), raw cloth 2 (5.93->9.31) | +321 |
| Grandgues | 152 | 0.05 | 0.90 (103/turn) | firewood 34 (2.79->6.7), timber 24 (8.03->11.59), tapestries 1 (603.75->669.75), charcoal 19 (3.09->4.94) | dyed cloth 7 (16.7->17.67), garments 2 (27.3->29.2), raw cloth 4 (8.61->9.31), beer 4 (3.36->3.64) | +297 |

**Best:** Hofkirchen at about +399 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 7 @ 3.82, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 13 = 3.0 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 83, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 15.5, stop 6 |  | uses 1.4/turn (household upkeep), makes 0.0, holds 12 = 8.3 turns |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 28.2) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 105, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.2) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 24.3k (cash + stock at home prices); -128/turn over 6 turns, +141/turn over 24 turns.
- Limits: cash flow >= -284/turn, prestige >= -0.90/turn (values are after 200 tax a turn).
- Today's settings: value +98/turn, cash +79/turn, prestige -2.79/turn - breaks the prestige floor.
- Plan: value +20/turn, cash +27/turn, prestige -0.90/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +101 vs +73, +160 vs +66, -153 vs +72.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Amsdermund: +3/turn
  - ship Flax Wyrm -> Nürnnieder: +1/turn
  - brewery 1 0.14 -> 0.08: +13/turn
  - net maker 0.00 -> 0.28: +4/turn
  - ropewalk 1 0.25 -> 0.32: +2/turn
  - retting pit 1 0.91 -> 0.98: -0/turn
  - flax farm 1 4.64 -> 4.93: +3/turn
  - weavery 1 0.50 -> 0.59: -6/turn
  - sewing shop 1 0.30 -> 0.37: +9/turn
  - mansion 1 0.00 -> 0.45: -105/turn
- Model check over the last 60 turns: predicted +57/turn for the settings we ran, real +2/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.77, thread 4.45, cloth 7.10, flax fibres 5.27, garments 20.55, nets 32.27, beer 3.18, timber 3.44, prestige 61.10, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None); rope sell 2 (v2 none)
- Ship linen snake: Grandgues -> Amsdermund (+4/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Nürnnieder (+1/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +88/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new leatherworks (make leather armour 1) for ~4278 coin: +2/turn, payback 1905 turns, doesn't pay yet (materials thin at home: bricks, nails)

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

Buffers: flax fibres 87/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.66; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
