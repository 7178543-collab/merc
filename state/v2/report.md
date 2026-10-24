# v2 shadow report

Turn 13518, 2026-10-24 15:23. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 883, prestige 3,578 (458 free, -0.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 47 | 0 | 7 | 0 | 0 | min_holding 60, sell 82, sell @ 2.98 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 12 | 0 | 2 | 5 | 0 | stop 16, buy 2, buy @ 2.4; sell 4, sell @ 1.74 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 45 | 0 | 2 | 0 | 0 | min_holding 30, sell 9, sell @ 17.8 |
| grain | 143 | 39 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 10 | 95 | 512 | 0 | 83 | buy 10, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34 |
| porterage | 12 | 12 | 12 | 0 | 0 | buy 12, buy @ 1.1 |

**1 risks, 1 waste, 4 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), home ask 1.74 x7, yet 0 bought last turn); labour need rises ~82/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 83 labour expired last turn (~126 coin): holding 10 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **cloth**: cloth buffer thin: 1.9 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 33
- **firewood**: floor 1.74 vs home bid 1.51: barely selling (0 of 4)
- **flax fibres**: flax fibres buffer thin: 1.2 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 57
- **wax**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 594, not 694
- labour expiry guard: 83 bought labour expired last turn, buy 12 (not 94) this turn

## Prestige spending, cheapest coin per prestige first

883 turns left: prestige gained now converts 98.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 45.0 | 45.0 | running |
| hold banquet 4 (pies) | mansion | 18 | 49.1 | 49.1 | thin at home: hop beer, wine, ham, pies |
| hold banquet 3 (pies) | mansion | 8 | 49.8 | 49.8 | thin at home: hop beer, pies |
| hold banquet 2 (pies) | mansion | 7 | 50.6 | 50.6 | thin at home: wine, pies |
| jousting 3 | arena | 230 | 51.7 | 51.8 | needs a arena (build cost 24,118); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 52.5 | 52.5 | thin at home: wine, hop beer, ham, stockfish |
| hold prayer 2 | chapel | 13 | 50.0 | 52.9 | needs a chapel (build cost 31,460); thin at home: furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 53.2 | 53.2 | thin at home: wine |
| hold banquet 3 (fish) | mansion | 7.6 | 53.4 | 53.4 | thin at home: hop beer |
| hold sermon 2 (candles) | church | 31 | 50.8 | 53.4 | needs a church (build cost 66,077); thin at home: candles, furniture |
| jousting 1 | arena | 170 | 53.4 | 53.6 | needs a arena (build cost 24,118); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 54.9 | 54.9 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only -1 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~94 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Darmwald | 1022 | 0.31 | 0.70 (66/turn) | grindstones 1 (277.2->475), charcoal 12 (1.94->5.46), light armour 2 (77.7->79.8), grain 11 (2.42->3.12) | raw cloth 2 (6.83->7.31) | +196 |
| Fontaux | 411 | 0.10 | 0.30 (28/turn) | cheese 21 (6.25->9.79), looms 1 (661.5->703), garments 7 (17.8->21.28), thread 65 (4.12->4.5) | candles 1 (66.67->69.5), raw cloth 2 (6.98->7.31) | +175 |
| Hofkirchen | 991 | 0.30 | 0.20 (19/turn) | glass ingots 2 (59.33->68.4), flax fibres 3 (5.05->10.16), blades 4 (15.75->19), lead bars 5 (16.17->18.52) | wax 7 (19.84->21.66), beer 6 (2.23->3.5), candles 1 (67.2->69.5), copper ingots 3 (12.08->13.21) | +99 |
| Amsdermund | 1111 | 0.36 | 0.40 (38/turn) | thread 61 (4.12->5.22), wine 9 (5.57->6.74), light armour 2 (77.7->80.27), blades 4 (15.75->16.25) | raw cloth 2 (5.99->7.31), wrought iron 7 (12.39->12.82), candles 1 (68.78->69.5), tools 1 (4.28->4.7) | +57 |
| Nürnnieder | 520 | 0.13 | 0.20 (19/turn) | thread 56 (4.12->5.13), garments 7 (17.8->18.71), wine 9 (5.57->5.7) | candles 1 (66.15->69.5), wax 4 (20.89->21.66), furniture 1 (12.92->14), tiles 2 (3.26->4.99) | +57 |

**Best:** Darmwald at about +196 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 27.2, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 4.0 turns |
| beer | 7 @ 3.66, stop 27 |  | uses 6.5/turn (household upkeep, mansion 1), makes 0.0, holds 47 = 7.2 turns |
| cured meat | 1 @ 29.0, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 2) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 2 @ 2.4, stop 16 | 5 @ min 1.71 | uses 7.6/turn (household upkeep), makes 6.5, holds 12 = 11.7 turns |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 8 @ min 17.8 | goal planner: sells 8 at 17.8 (v2 had 8 at 20.0) |
| grain | 18 @ 3.7, stop 70 |  | uses 17.5/turn (observed), makes 0.0, holds 143 = 8.2 turns |
| labour | 95 @ 2.2, stop - |  | goal planner: buys 95 for today's rates (v2 had 12) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 12 @ min 34.0 |  |
| pasties | 3 @ 14.5, stop 11 |  | goal planner: buys 3 a turn for today's rates, keeps up to 11 (v2 had 4) |
| porterage | 13 @ 1.1, stop - |  | goal planner: buys 13 for today's rates (v2 had 5) |
| rope |  | 4 @ min 71.0 | makes 2.0, uses 0.2, holds 31 (keeps 0): sells the surplus + 2/turn of the excess |
| thread |  | 9 @ min 4.12 | goal planner: sells 9 a turn at 4.12, keeps 221 (no one offered it) |
| tools | 2 @ 6.2, stop 4 |  | uses 2.0/turn (net maker152202386007001, retting pit 1), makes 0.0, holds 199 = 101.5 turns |
| varnish | 1 @ 17.1, stop 1 |  | uses 0.1/turn (net maker152202386007001), makes 0.0, holds 1 = 7.0 turns |
| wax | 1 @ ?, stop 1 |  | uses 0.1/turn (net maker152202386007001), makes 0.0, holds 0 = 1.8 turns |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 17.8k (cash + stock at home prices); +40/turn over 6 turns, +65/turn over 24 turns.
- Limits: cash flow >= +130/turn, prestige >= -0.66/turn (values are after 240 tax a turn).
- Today's settings: value +31/turn, cash +63/turn, prestige -0.76/turn - breaks the prestige floor and cash floor.
- Plan: value +43/turn, cash +130/turn, prestige -0.66/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -111 vs +35, -336 vs +77, +67 vs +93 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4, garments 0.5, nets 0.0, rope 0.1.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Brunnham: +3/turn
  - brewery 1 0.63 -> 0.58: +8/turn
  - ropewalk 1 0.50 -> 0.55: +6/turn
  - logging camp w/ tool 5.00 -> 5.50: +0/turn
  - retting pit 1 0.83 -> 0.75: -3/turn
  - flax farm 1 4.60 -> 4.30: +2/turn
  - spinnery 1 1.70 -> 1.54: +1/turn
  - weavery 1 0.33 -> 0.43: -5/turn
- Model check over the last 24 turns: predicted +137/turn for the settings we ran, real +65/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.64, thread 4.03, cloth 6.49, flax fibres 4.64, garments 18.85, nets 30.04, beer 2.92, timber 7.16, prestige 60.32, cash 0.08
- Orders it would set: cured meat buy 1 (v2 2); grain buy 37 (v2 18); labour buy 95 (v2 12); light armour buy 1 (v2 None); pasties buy 3 (v2 4); porterage buy 13 (v2 5); thread sell 9 (v2 none)
- Ship linen snake: Grandgues -> Brunnham (+8/turn over staying).
- Ship Flax Wyrm: stays on Caillechâtel (worth +3/turn).
- Management: ~13.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +79/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
- Trim: donate quarry 1: +21/turn (tax 20 saved).
- Trim: donate logging camp w/ tool: +18/turn (tax 20 saved).

## Chain sizing

Mode HOLD, garments sold 6.7/turn (+0.0 exported); plan makes 0.0 garments a turn.
Labour: own 500, everything else 434, chain may buy 0 -> chain allowance 66, chain plan 94 (-166 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.60 | 2.14 |
| ret | 3 | 0.83 | 0.38 |
| spin | 4 | 1.70 | 0.79 |
| weave | 3 | 0.33 | 0.00 |
| sew | 2 | 0.21 | 0.00 |

Buffers: flax fibres 34/47, thread 690/138, cloth 32/0
- chain plan needed 94 labour, budget left 66: cut to 94

## Self-diagnosis

Nothing found this run.
