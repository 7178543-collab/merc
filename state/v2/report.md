# v2 shadow report

Turn 13519, 2026-10-24 16:44. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 1,022, prestige 3,577 (457 free, -1.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 82, sell @ 2.98 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 5 | 2 | 5 | 0 | 0 | stop 16, buy 2, buy @ 2.4; sell 5, sell @ 1.71 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 43 | 0 | 2 | 0 | 0 | min_holding 30, sell 8, sell @ 17.8 |
| grain | 126 | 0 | 17 | 0 | 0 | buy @ 3.7 |
| labour | 10 | 10 | 510 | 84 | 0 | buy 10, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 12, sell @ 34 |
| porterage | 12 | 12 | 5 | 0 | 7 | buy 12, buy @ 1.1 |

**1 risks, 0 waste, 4 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **labour**: buying 10, short of ~94 needed -> v2: buy 94

## Tuning

- **cloth**: cloth buffer thin: 1.7 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 33
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax fibres**: flax fibres buffer thin: 1.2 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 57
- **wax**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 594, not 688

## Prestige spending, cheapest coin per prestige first

882 turns left: prestige gained now converts 98.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 45.3 | 45.3 | running |
| hold banquet 4 (pies) | mansion | 18 | 49.2 | 49.2 | thin at home: hop beer, wine, pies |
| hold banquet 3 (pies) | mansion | 8 | 49.9 | 49.9 | thin at home: hop beer, pies |
| hold banquet 2 (pies) | mansion | 7 | 50.9 | 50.9 | thin at home: wine, pies |
| jousting 3 | arena | 230 | 52.0 | 52.1 | needs a arena (build cost 24,356); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 52.6 | 52.6 | thin at home: wine, hop beer, stockfish |
| hold prayer 2 | chapel | 13 | 50.1 | 53.0 | needs a chapel (build cost 31,828); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 50.8 | 53.5 | needs a church (build cost 66,155); thin at home: candles, furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 53.7 | 53.7 | thin at home: wine |
| hold banquet 3 (fish) | mansion | 7.6 | 53.7 | 53.7 | thin at home: hop beer |
| hold banquet 3 (meat) | mansion | 7.6 | 54.8 | 54.8 | thin at home: hop beer, cured meat |
| hold banquet 2 (meat) | mansion | 6.8 | 54.9 | 54.9 | thin at home: wine, cured meat |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only -1 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -9 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~94 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Fontaux | 411 | 0.10 | 0.30 (28/turn) | cheese 18 (6.35->9.79), looms 1 (666.75->698.25), rope 2 (53.87->67.45), charcoal 11 (1.63->3.8) | casks 5 (5.62->6.65), premium ham 1 (275.1->279.3), wax 3 (22.26->23.18), candles 1 (67.73->69) | +145 |
| Rouhomme | 368 | 0.09 | 0.20 (19/turn) | rope 2 (53.87->73.15), beer 33 (2.92->3.42), charcoal 11 (1.63->3.29), iron ore 2 (4.85->8.46) | candles 1 (50.4->69), gold bars 1 (798->817), grindstones 1 (207.9->218.5), casks 5 (5.17->6.65) | +128 |
| Bedenis | 566 | 0.14 | 0.10 (9/turn) | looms 1 (666.75->726.75), rope 2 (53.87->73.62), cheese 3 (6.35->6.98) | wax 2 (21.42->23.18), candles 1 (66.67->69), casks 5 (5.88->6.65), flax fibres 3 (4.94->5.4) | +108 |
| Hofkirchen | 991 | 0.30 | 0.20 (19/turn) | rope 2 (53.87->68.88), glass ingots 2 (59.33->68.4), hop beer 4 (8.51->11.3), blades 2 (15.02->19) | wax 6 (19.84->23.18), beer 4 (2.23->3.5), tar 3 (8.98->10.54), candles 1 (67.2->69) | +103 |
| Helmgreen | 1354 | 0.48 | 0.20 (19/turn) | rope 2 (53.87->71.25), wine 8 (5.62->6.27), cloth 2 (6.95->7.46), copper ore 1 (21.63->24.51) | lathes 1 (172.2->205.2), gold bars 1 (798->817), wax 6 (21.21->23.18), casks 5 (5.04->6.65) | +96 |

**Best:** Fontaux at about +145 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 26.6, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 3.0 turns |
| beer |  | 82 @ min 2.92 | goal planner: sells 82 at 2.92 (v2 had 82 at 3.38) |
| cured meat | 1 @ 29.0, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 2) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 3 @ 2.4, stop 16 | 0 @ min 1.68 | uses 7.9/turn (brewery 1, household upkeep), makes 6.5, holds 5 = 3.3 turns |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 8 @ min 17.8 | goal planner: sells 8 at 17.8 (v2 had 8 at 20.0) |
| grain | 37 @ 3.7, stop 146 |  | goal planner: buys 37 a turn for today's rates, keeps up to 146 (v2 had 61) |
| labour | 95 @ 2.2, stop - |  | goal planner: buys 95 for today's rates (v2 had 94) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 12 @ min 34 | goal planner: sells 12 at 34 (v2 had 12 at 34.6) |
| pasties | 3 @ 14.5, stop 11 |  | goal planner: buys 3 a turn for today's rates, keeps up to 11 (v2 had 4) |
| porterage | 13 @ 1.1, stop - |  | goal planner: buys 13 for today's rates (v2 had 7) |
| rope |  | 4 @ min 72.0 | makes 2.0, uses 0.2, holds 29 (keeps 0): sells the surplus + 2/turn of the excess |
| thread |  | 8 @ min 4.12 | goal planner: sells 8 a turn at 4.12, keeps 221 (no one offered it) |
| tools | 2 @ 6.2, stop 16 |  | uses 2.0/turn (net maker152202386007001, retting pit 1), makes 0.0, holds 200 = 101.7 turns |
| varnish | 1 @ 17.1, stop 1 |  | uses 0.1/turn (net maker152202386007001), makes 0.0, holds 1 = 7.0 turns |
| wax | 1 @ ?, stop 1 |  | uses 0.1/turn (net maker152202386007001), makes 0.0, holds 0 = 1.8 turns |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 17.9k (cash + stock at home prices); +15/turn over 6 turns, +70/turn over 24 turns.
- Limits: cash flow >= +124/turn, prestige >= -0.65/turn (values are after 240 tax a turn).
- Today's settings: value +18/turn, cash +20/turn, prestige -0.64/turn - breaks the cash floor.
- Plan: value +41/turn, cash +124/turn, prestige -0.65/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -336 vs +77, +67 vs +93, +139 vs +63 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4, garments 0.5, nets 0.0, rope 0.1.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Rouhomme: +24/turn
  - ship Flax Wyrm -> Boistot: +1/turn
  - brewery 1 0.63 -> 0.56: +11/turn
  - logging camp w/ tool 5.00 -> 5.62: +0/turn
  - weavery 1 0.33 -> 0.46: -2/turn
  - retting pit 1 0.83 -> 0.71: -7/turn
  - flax farm 1 4.60 -> 4.05: +4/turn
  - spinnery 1 1.70 -> 1.45: +1/turn
- Model check over the last 25 turns: predicted +135/turn for the settings we ran, real +69/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.64, thread 4.03, cloth 6.49, flax fibres 4.63, garments 18.86, nets 30.06, beer 2.92, timber 7.21, prestige 60.98, cash 0.09
- Orders it would set: cured meat buy 1 (v2 2); grain buy 37 (v2 61); labour buy 95 (v2 94); light armour buy 1 (v2 None); pasties buy 3 (v2 4); porterage buy 13 (v2 7); thread sell 8 (v2 none)
- Ship linen snake: Grandgues -> Rouhomme (+30/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Boistot (+1/turn over staying).
- Management: ~13.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +80/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
- Trim: donate quarry 1: +21/turn (tax 20 saved).
- Trim: donate logging camp w/ tool: +18/turn (tax 20 saved).

## Chain sizing

Mode HOLD, garments sold 6.8/turn (+0.0 exported); plan makes 0.0 garments a turn.
Labour: own 500, everything else 434, chain may buy 0 -> chain allowance 66, chain plan 94 (-166 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.60 | 2.14 |
| ret | 3 | 0.83 | 0.38 |
| spin | 4 | 1.70 | 0.79 |
| weave | 3 | 0.33 | 0.00 |
| sew | 2 | 0.21 | 0.00 |

Buffers: flax fibres 34/47, thread 726/138, cloth 29/0
- chain plan needed 94 labour, budget left 66: cut to 94

## Self-diagnosis

Nothing found this run.
