# v2 shadow report

Turn 14183, 2026-11-21 08:06. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,629, prestige 3,725 (605 free, -1.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 59 | 0 | 12 | 0 | 0 | min_holding 58, sell 15, sell @ 3.88 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 7 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 0 | 0 | 0 | 0 | 0 | none |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 35 | 9 | 9 | 0 | 0 | stop 36, buy 10, buy @ 3.7 |
| labour | 64 | 64 | 519 | 0 | 45 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (4 @ 29), but the home ask 29.40 is above it); labour need rises ~35/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **cured meat**: only 0.0 turns of cured meat left and buying 4 (need 12) -> v2: buy 12
- **firewood**: home ask 2.66 is above our ceiling 2.40 and last turn bought 4 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.30 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~94 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **cured meat**: home ask 29.40 is above our ceiling 29.00 and last turn bought 3 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.30 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 519, not 614

## Prestige spending, cheapest coin per prestige first

218 turns left: prestige gained now converts 66.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 52.8 | 53.5 | needs a arena (build cost 29,688); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 | arena | 210 | 57.8 | 58.6 | needs a arena (build cost 29,688); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 61.4 | 61.4 | thin at home: hop beer, wine, stockfish, candles, premium cheese |
| hold banquet 4 (pies) | mansion | 18 | 61.7 | 61.7 | thin at home: hop beer, wine, stockfish, cheese, candles |
| maintain 1 | park | 0.5 | 62.4 | 62.4 | running |
| hold mass 2 (premium) | cathedral | 360 | 54.7 | 63.6 | needs a cathedral (build cost 318,380); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 3 (pies) | mansion | 8 | 65.8 | 65.8 | thin at home: hop beer, cheese, candles |
| hold banquet 4 | mansion | 17.5 | 66.9 | 66.9 | thin at home: wine, hop beer, ham, stockfish, cheese, candles |
| hold banquet 2 (pies) | mansion | 7 | 67.8 | 67.8 | thin at home: wine, cheese, candles |
| hold banquet 1 (fish) | mansion | 4.2 | 70.6 | 70.6 |  |
| hold banquet 1 (meat) | mansion | 4.2 | 73.6 | 73.6 | running |
| jousting 1 | arena | 170 | 74.8 | 75.8 | needs a arena (build cost 29,688); thin at home: protection, light armour, arms; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: cured meat buy 3 @ 27.4, pasties buy 11 @ 16.0; crew 0.1; est +25 a turn; stock: pasties 11 @ 16.0 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -1 a turn after crew: ship stays at 0
- best towns now: Blanans +202, Vauxvais +155, Heidlowe +153, Boistot +143, Brebronn +139
- Blanans would trade: cured meat buy 3 @ 26.6, furniture buy 12 @ 12.7, grain buy 8 @ 2.6, pasties buy 13 @ 16.0; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~130 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.90 (117/turn) | bread 258 (3.07->3.93), firewood 34 (2.79->6.89), charcoal 19 (2.84->6.46), thread 92 (6.7->7.03) | cured meat 3 (26.46->29.4), wool 2 (11.34->12.35), cloth 3 (11.34->11.4) | +365 |
| Amsdermund | 1111 | 0.49 | 0.30 (39/turn) | hides 1 (11.55->20.71) | cloth 24 (7.35->11.4), cheese 5 (8.77->12.44), cured meat 3 (24.78->29.4), tackles 2 (178.5->184.3) | +141 |
| Hanstein | 380 | 0.13 | 0.20 (26/turn) | charcoal 18 (2.84->4.07), limestone 1 (19.64->28.31), malt 1 (7.61->8.88), leather 1 (29.82->30.21) | thread 49 (5->6.85), cheese 5 (8.35->12.44), flax fibres 10 (6.14->8), cured meat 3 (28.14->29.4) | +140 |
| Kirchwerp | 1072 | 0.47 | 0.30 (39/turn) | garments 10 (31.6->37.62), honey 4 (8.87->13.21), casks 6 (6.72->9.36), flax fibres 7 (7.95->9.97) | cloth 24 (10.5->11.4), chisels 4 (8.4->9.79), cookware 5 (21->22.23) | +115 |
| Brebronn | 862 | 0.32 | 0.20 (26/turn) | dyed cloth 13 (20.48->23.37) | cloth 24 (9.08->11.4), cheese 5 (5.78->12.44), cured meat 3 (27.09->29.4), furniture 1 (14.49->16.3) | +110 |

**Best:** Grandgues at about +365 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 15 @ min 3.88 |  |
| bread | 5 @ 2.98, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had None) |
| candles | 2 @ 70.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| furniture | 2 @ 16.7, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 30.8) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 10) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 19) |
| light armour | 1 @ 109, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 44.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.2k (cash + stock at home prices); +134/turn over 6 turns, +101/turn over 24 turns.
- Limits: cash flow >= -318/turn, prestige >= -1.27/turn (values are after 200 tax a turn).
- Today's settings: value -155/turn, cash -179/turn, prestige +0.47/turn.
- Plan: value +29/turn, cash +33/turn, prestige -1.27/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +114 vs -187, +86 vs -188, +156 vs -198.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Amsdermund: +5/turn
  - ship Flax Wyrm -> Blanans: +5/turn
  - mansion 1 1.00 -> 0.59: +122/turn
  - ropewalk 1 0.25 -> 0.07: +8/turn
  - spinnery 1 1.65 -> 1.19: +32/turn
  - retting pit 1 0.91 -> 0.76: +2/turn
  - brewery 1 0.14 -> 0.20: +2/turn
  - flax farm 1 4.64 -> 3.80: +11/turn
  - net maker 0.00 -> 0.29: +0/turn
  - weavery 1 0.50 -> 0.44: -4/turn
- Model check over the last 59 turns: predicted -126/turn for the settings we ran, real -3/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.61, beer 3.42, timber 3.76, prestige 65.66, cash 0.00
- Orders it would set: bread buy 5 (v2 None); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 8); fish buy 0 (v2 None); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 10); labour buy 64 (v2 19); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Amsdermund (+3/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Blanans (+6/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 416 (+127 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 3.99 |
| ret | 3 | 0.91 | 0.80 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 132/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R1: bread slot dry: 5.0 held, 4.2 a turn (basic food slot (+0.3 prestige)); our buy 5 @ 2.98, home ask 2.92; our bid is already at/over the ask (sellers too thin)
- R1: cured meat slot dry: 0.0 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 4 @ 29, home ask 29.4 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 12 @ 30 (ask 29.4, cap 42.0))
- R1: fish slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
