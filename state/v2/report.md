# v2 shadow report

Turn 14011, 2026-11-14 04:51. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,845, prestige 3,514 (394 free, +2.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 108 | 22 | 19 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 116, buy 39, buy @ 3.76 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 33, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 546 | 0 | 18 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**1 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 18 labour expired last turn (~34 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.20 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 99 over real use lately; planning 546, not 645

## Prestige spending, cheapest coin per prestige first

390 turns left: prestige gained now converts 85.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 56.4 | 56.4 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 58.2 | 58.2 | thin at home: cured fish |
| hold banquet 2 (pies) | mansion | 7 | 58.2 | 58.2 |  |
| jousting 3 | arena | 230 | 57.9 | 58.3 | needs a arena (build cost 29,355); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 58.5 | 58.5 | thin at home: hop beer, stockfish |
| hold banquet 1 (fish) | mansion | 4.2 | 59.5 | 59.5 | thin at home: cured fish |
| hold banquet 4 (premium) | mansion | 20 | 60.4 | 60.4 | thin at home: hop beer, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 61.6 | 61.6 | thin at home: hop beer |
| hold banquet 4 | mansion | 17.5 | 61.7 | 61.7 | thin at home: hop beer, ham, stockfish |
| hold banquet 2 (meat) | mansion | 6.8 | 62.8 | 62.8 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 62.9 | 62.9 | thin at home: hop beer, cured fish |
| hold mass 2 (premium) | cathedral | 360 | 60.7 | 63.9 | needs a cathedral (build cost 318,430); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: cured meat buy 6 @ 23.2, pasties buy 5 @ 16.0; crew 0.1; est +19 a turn; stock: pasties 5 @ 16.0 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 15.1 (keep 14); best orders clear only 4 a turn after crew: ship stays at 0
- best towns now: Großmühle +27, Hofkirchen +25, Essenbrucke +24, Etallaen +23, Gottweiler +22
- Großmühle would trade: cured meat buy 6 @ 23.2, pasties buy 5 @ 14.4; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~116 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.60 (70/turn) | timber 26 (8.14->11.97), firewood 34 (3.32->5.75), looms 1 (588->617.5), casks 4 (6.67->7.65) | cloth 10 (7.93->9.05), cured meat 6 (23.94->25.8), candles 1 (86.62->88.5), garments 2 (22.47->23.2) | +175 |
| Coburgbaum | 619 | 0.19 | 0.80 (93/turn) | bread 152 (2.6->4.01), lead ore 1 (8.93->10.54), premium cheese 1 (29.82->30.59), beer 3 (3.66->4.08) | cloth 13 (7.77->9.05), cured meat 4 (23.52->25.8), candles 1 (86.1->88.5), salt 3 (5.04->5.56) | +154 |
| Hanstein | 380 | 0.12 | 0.40 (46/turn) | looms 1 (588->669.75), charcoal 16 (2.6->4.43), dyed cloth 14 (10.61->11.02), timber 11 (8.14->10.16) | windows 1 (771.75->788.5), seeds 18 (1.84->2.58), cloth 12 (8.45->9.05), cured meat 6 (24.57->25.8) | +139 |
| Heilegg | 826 | 0.26 | 0.50 (58/turn) | looms 1 (588->636.5), charcoal 19 (2.6->5.37), acid 1 (115.5->122.55), lead ore 7 (8.93->10.54) | cloth 24 (7.72->9.05), cheese 12 (5.3->6.74), cured meat 6 (24.15->25.8), salt 3 (3.89->5.56) | +119 |
| Etallaen | 774 | 0.24 | 0.10 (12/turn) | looms 1 (588->669.75), dyed cloth 11 (10.61->12.06), garments 10 (21.4->22.61), grain 2 (3->3.52) | cloth 11 (8.03->9.05), candles 1 (84->88.5), cured meat 5 (24.78->25.8), seeds 1 (2.1->2.58) | +118 |

**Best:** Grandgues at about +175 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 20 @ 3.88, stop 77 |  | uses 19.2/turn (household upkeep, mansion 1), makes 0.0, holds 108 = 5.6 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 7) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 7 = 1.2 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres |  | 2 @ min 5.5 | goal planner: sells 2 a turn at 5.5, keeps 85 (no one offered it) |
| furniture | 2 @ 16.1, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 20.8) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 46) |
| light armour | 1 @ 102, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 37.8) |
| pasties |  | 1 @ min 13.3 | goal planner: sells 1 a turn at 13.3, keeps 0 (no one offered it) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 81.0) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 0 = 0.8 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 27.6k (cash + stock at home prices); -196/turn over 6 turns, -53/turn over 24 turns.
- Limits: cash flow >= -369/turn, prestige >= -0.39/turn (values are after 200 tax a turn).
- Today's settings: value -183/turn, cash -158/turn, prestige +2.04/turn.
- Plan: value -15/turn, cash -3/turn, prestige -0.39/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -105 vs -161, -237 vs -161, -70 vs -168.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Donaunieder: +3/turn
  - ship Flax Wyrm -> Unterhufe: +1/turn
  - mansion 1 1.00 -> 0.42: +151/turn
  - net maker 0.00 -> 0.29: +3/turn
  - spinnery 1 1.65 -> 1.35: +2/turn
  - retting pit 1 0.91 -> 0.83: +3/turn
  - flax farm 1 4.64 -> 4.19: +5/turn
  - ropewalk 1 0.25 -> 0.00: -11/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.30: +11/turn
  - weavery 1 0.50 -> 0.37: -11/turn
- Model check over the last 60 turns: predicted +18/turn for the settings we ran, real +46/turn.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.96, garments 19.30, nets 30.29, beer 3.19, timber 3.49, prestige 59.99, cash 0.00
- Orders it would set: bread buy 5 (v2 7); cloth sell 1 (v2 none); firewood buy 2 (v2 3); flax fibres sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 0); labour buy 64 (v2 46); light armour buy 1 (v2 None); pasties sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.30, worth +10/turn.
- Ship linen snake: Grandgues -> Donaunieder (+2/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Unterhufe (+1/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 421 (+132 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.27 |
| ret | 3 | 0.91 | 0.85 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 112/77, thread 1050/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask none (no sellers at home)
- R5: tar buy not filling: bid 11 under the home ask 11.2 for 5 turns, bought 0.0 of 1, 0.2 held (0.8 turns); raise needs Taylor (ceiling 11.0)
