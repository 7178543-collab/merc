# v2 shadow report

Turn 14190, 2026-11-21 15:56. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,316, prestige 3,714 (594 free, -1.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 58 | 0 | 12 | 0 | 0 | min_holding 58, sell 15, sell @ 3.8 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 5 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 5 | 3 | 3 | 0 | 0 | stop 42, buy 5, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 36 | 9 | 9 | 0 | 0 | stop 36, buy 10, buy @ 3.7 |
| labour | 64 | 64 | 526 | 0 | 38 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 4 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (12 @ 30.6), but the home ask 31.60 is above it); labour need rises ~35/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.62 is above our ceiling 2.40 and last turn bought 4 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Waste (money lost now)

- **labour**: 38 labour expired last turn (~77 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: home ask 3.00 is above our ceiling 2.60 and last turn bought 5 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **cured meat**: home ask 31.60 is above our ceiling 29.00 and last turn bought 3 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **fish**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 64.2 coin per prestige at mansion, vs 75.8 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch

## Notes

- labour: projection runs 114 over real use lately; planning 526, not 629

## Prestige spending, cheapest coin per prestige first

211 turns left: prestige gained now converts 65.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 52.8 | 53.6 | needs a arena (build cost 29,390); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| jousting 2 | arena | 210 | 57.8 | 58.7 | needs a arena (build cost 29,390); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 60.4 | 60.4 | thin at home: wine, stockfish, candles |
| hold banquet 4 (pies) | mansion | 18 | 60.5 | 60.5 | thin at home: wine, stockfish, cheese, candles |
| maintain 1 | park | 0.5 | 60.6 | 60.6 | running |
| hold mass 2 (premium) | cathedral | 360 | 52.5 | 61.1 | needs a cathedral (build cost 283,850); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |
| hold banquet 1 (fish) | mansion | 4.2 | 64.2 | 64.2 |  |
| hold banquet 4 | mansion | 17.5 | 65.5 | 65.5 | thin at home: wine, ham, stockfish, cheese, candles |
| hold banquet 3 (pies) | mansion | 8 | 65.7 | 65.7 | thin at home: cheese, pies, candles |
| hold banquet 2 (pies) | mansion | 7 | 67.8 | 67.8 | thin at home: wine, cheese, pies, candles |
| hold banquet 2 (fish) | mansion | 6.8 | 73.2 | 73.2 | thin at home: wine, cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 74.4 | 74.4 | thin at home: cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 15.4 (keep 14); best orders clear only 1 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only 2 a turn after crew: ship stays at 0
- best towns now: Blanans +83, Clairlond +64, Bordees +62, Orlesailles +61, Cobholme +57
- Blanans would trade: cured meat buy 3 @ 28.2, furniture buy 5 @ 12.7, pasties buy 6 @ 16.1; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~127 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Kirchwerp | 1072 | 0.46 | 0.70 (89/turn) | glassware 8 (78.23->106.4), thread 78 (7->9.5), furniture 8 (16.28->23.94), casks 9 (6.83->9.36) | cloth 18 (10.5->11.4), garments 2 (28.14->31.8), chisels 1 (8.4->8.88) | +492 |
| Grandgues | 152 | 0.05 | 0.90 (114/turn) | firewood 37 (2.75->8.12), bread 255 (3.15->3.76), glassware 4 (78.23->104.5), charcoal 19 (2.88->6.51) | cheese 10 (11.65->13.96), cloth 6 (8.87->11.4), cured meat 3 (27.72->31.6), wrought iron 2 (16.38->16.43) | +475 |
| Rouhomme | 368 | 0.12 | 0.90 (114/turn) | glassware 4 (78.23->102.6), bread 255 (3.15->3.88), garments 10 (31.6->32.49), rope 1 (84.5->90.72) | tools 16 (5.25->6.46), cheese 10 (12.39->13.96), wrought iron 2 (15.65->16.43) | +237 |
| Fontaux | 411 | 0.14 | 0.70 (89/turn) | thread 69 (7->8.41), charcoal 19 (2.88->4.94), flax fibres 7 (7->8.17), timber 21 (8.72->11.02) | cheese 10 (6.98->13.96), nets 2 (36.12->43.51), cured fish 7 (22.68->23.75), pasties 1 (12.6->13.59) | +205 |
| Heilegg | 826 | 0.29 | 0.80 (102/turn) | varnish 7 (17.12->22.99), butter 5 (78.23->85.5), charcoal 19 (2.88->6.7), flour 4 (22.89->30.97) | garments 2 (29.61->31.8), cured meat 3 (30.66->31.6) | +162 |

**Best:** Kirchwerp at about +492 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 31.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had None) |
| beer |  | 15 @ min 3.74 |  |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 9) |
| candles | 2 @ 70.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 3 @ 2.5, stop - |  | goal planner: buys 3 for today's rates (v2 had 3) |
| furniture | 2 @ 15.9, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 30.8) |
| grain | 9 @ 3.7, stop 33 |  | goal planner: buys 9 a turn for today's rates, keeps up to 33 (v2 had 10) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 26) |
| light armour | 1 @ 109, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 44.6) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 82.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.2k (cash + stock at home prices); +206/turn over 6 turns, +105/turn over 24 turns.
- Limits: cash flow >= -347/turn, prestige >= -1.22/turn (values are after 200 tax a turn).
- Today's settings: value -150/turn, cash -164/turn, prestige +0.93/turn.
- Plan: value +49/turn, cash +55/turn, prestige -1.22/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -24 vs -189, +72 vs -191, +228 vs -186.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Clarfranche: +3/turn
  - ship Flax Wyrm -> Blanans: +2/turn
  - mansion 1 1.00 -> 0.49: +152/turn
  - ropewalk 1 0.25 -> 0.12: +13/turn
  - spinnery 1 1.65 -> 1.23: +13/turn
  - retting pit 1 0.91 -> 0.78: +4/turn
  - flax farm 1 4.64 -> 3.94: +6/turn
  - net maker 0.00 -> 0.29: -0/turn
  - weavery 1 0.50 -> 0.42: -5/turn
- Model check over the last 59 turns: predicted -129/turn for the settings we ran, real -3/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.38, garments 21.00, nets 32.66, beer 3.40, timber 4.39, prestige 67.39, cash 0.00
- Orders it would set: arms buy 1 (v2 None); bread buy 5 (v2 9); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 8); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 10); labour buy 64 (v2 26); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Clarfranche (+2/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Blanans (+2/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~2049 coin: +1/turn, payback 3669 turns, doesn't pay yet (materials thin at home: limestone)

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 417 (+128 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.05 |
| ret | 3 | 0.91 | 0.81 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 128/77, thread 1050/228, cloth 73/128

## Self-diagnosis

- R1: cured meat slot dry: 0.0 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 12 @ 30.6, home ask 31.6 -> **buy 12 @ 32.2 (ask 31.6, cap 42.0)** (ok)
- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
