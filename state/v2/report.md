# v2 shadow report

Turn 13506, 2026-10-24 03:28. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 1,007, prestige 3,587 (467 free, -0.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 66 | 0 | 7 | 0 | 0 | min_holding 60, sell 73, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 28 | 0 | 7 | 0 | 0 | stop 15, buy 1, buy @ 2.4; sell 3, sell @ 1.61 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 106 | 0 | 2 | 0 | 0 | min_holding 30, sell 8, sell @ 19 |
| grain | 97 | 32 | 37 | 0 | 0 | stop 125, buy 32, buy @ 3.7 |
| labour | 35 | 95 | 586 | 0 | 9 | buy 35, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 34 |
| porterage | 13 | 13 | 13 | 2 | 0 | buy 13, buy @ 1.1 |

**2 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **labour**: buying 35, short of ~95 needed -> v2: buy 95
- **porterage**: quarry 1 ran short of porterage (buy is live (13 @ 1.1), 13 bought last turn); labour need rises ~8/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.3 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 70
- **flax plants**: flax plants buffer thin: 1.1 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 182

## Notes

- labour: projection runs 100 over real use lately; planning 595, not 695

## Prestige spending, cheapest coin per prestige first

895 turns left: prestige gained now converts 98.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 43.5 | 43.5 | running |
| hold banquet 4 (pies) | mansion | 18 | 49.9 | 49.9 | thin at home: hop beer, wine |
| hold banquet 3 (pies) | mansion | 8 | 50.4 | 50.4 | thin at home: hop beer, pies |
| hold banquet 2 (pies) | mansion | 7 | 51.4 | 51.4 | thin at home: wine, pies |
| jousting 3 | arena | 230 | 51.3 | 51.5 | needs a arena (build cost 23,924); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold prayer 2 | chapel | 13 | 49.3 | 52.1 | needs a chapel (build cost 30,443); thin at home: furniture |
| hold banquet 3 (fish) | mansion | 7.6 | 52.5 | 52.5 | thin at home: hop beer |
| hold banquet 2 (fish) | mansion | 6.8 | 52.8 | 52.8 | thin at home: wine |
| hold banquet 1 (fish) | mansion | 4.2 | 53.1 | 53.1 |  |
| hold banquet 4 | mansion | 17.5 | 53.2 | 53.2 | thin at home: wine, hop beer, ham |
| hold banquet 3 (meat) | mansion | 7.6 | 53.7 | 53.7 | thin at home: hop beer |
| hold banquet 2 (meat) | mansion | 6.8 | 54.2 | 54.2 | thin at home: wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only 13 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only 4 a turn after crew: ship stays at 0
- best towns now: Bremcop +32, Hofkirchen +22, Cobholme +15
- Bremcop would trade: candles buy 1 @ 69.0, rope sell 5 @ 80.0; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~91 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.29 | 0.60 (54/turn) | beer 73 (2.98->6.41), tallow 2 (19.84->24.13), thread 6 (3.39->4.26), blades 1 (12.5->14.54) | candles 1 (67.2->81), garments 2 (18.38->19.2) | +229 |
| Rouhomme | 368 | 0.09 | 0.80 (73/turn) | bread 142 (2.06->2.72), beer 73 (2.98->3.42), charcoal 12 (1.58->3.29), yarn 6 (4.75->6.41) | candles 1 (71.4->81), lathes 1 (202.65->210.9), flax fibres 7 (5.35->5.8) | +128 |
| Caillechâtel | 488 | 0.12 | 0.20 (18/turn) | beer 31 (2.98->5.65), thread 25 (3.39->4.05), blades 1 (12.5->19.38), fleece 2 (6.98->7.41) | candles 1 (69.83->81), flax fibres 9 (5.19->5.8), grain 36 (2.31->2.64) | +114 |
| Chribruck | 1202 | 0.39 | 0.70 (63/turn) | beer 70 (2.98->4.5), thread 9 (3.39->4.94), wool 5 (8.87->11.11), nets 2 (35->38.57) | candles 1 (69.83->81) | +94 |
| Hanstein | 380 | 0.09 | 0.40 (36/turn) | thread 62 (3.39->4.07), charcoal 12 (1.58->2.55), timber 12 (7.09->8.74), cloth 2 (7->7.22) | flax fibres 32 (5.02->5.8), candles 1 (75.08->81), flax plants 90 (1.25->1.5), cheese 8 (5.3->5.61) | +75 |

**Best:** Hofkirchen at about +229 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 73 @ min 3.38 |  |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 12 = 7.7 turns |
| cloth |  | 3 @ min 7.25 | goal planner: trial sale of an idle pile, 3 a turn at 7.25, keeps 0 (36 over) |
| cured meat | 1 @ 29.0, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 1) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 1 @ 2.4, stop 2 | 2 @ min 1.65 | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 7 @ min 19 | goal planner: trial sale of an idle pile, 7 a turn at 19, keeps 30 (76 over) |
| grain | 37 @ 3.7, stop 148 |  | goal planner: buys 37 a turn for today's rates, keeps up to 148 (v2 had 63) |
| labour | 98 @ 2.2, stop - |  | goal planner: buys 98 for today's rates (v2 had 95) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 11 @ min 34.0 |  |
| pasties | 3 @ 14.5, stop 10 |  | goal planner: buys 3 a turn for today's rates, keeps up to 10 (v2 had 3) |
| porterage | 16 @ 1.1, stop - |  | goal planner: buys 16 for today's rates (v2 had 6) |
| rope |  | 5 @ min 72.0 | makes 3.9, uses 0.0, holds 19 (keeps 0): sells the surplus + 1/turn of the excess |
| tar | 1 @ 11.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| thread |  | 21 @ min 4.5 | goal planner: trial sale of an idle pile, 21 a turn at 4.5, keeps 249 (251 over) |
| tools | 3 @ 6.2, stop 17 |  | uses 2.0/turn (retting pit 1), makes 0.0, holds 200 = 98.4 turns |
| wax | 1 @ 22.6, stop 1 |  | uses 0.1/turn (net maker152202386007001), makes 0.0, holds 0 = 4.0 turns |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 16.9k (cash + stock at home prices); +102/turn over 6 turns, +52/turn over 24 turns.
- Limits: cash flow >= +125/turn, prestige >= -0.70/turn (values are after 240 tax a turn).
- Today's settings: value +19/turn, cash +5/turn, prestige -0.69/turn - breaks the cash floor.
- Plan: value +106/turn, cash +127/turn, prestige -0.70/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +17 vs +194, -5 vs +272, +136 vs +22 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4, garments 0.5, nets 0.0, rope 0.1.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Vauxvais: +10/turn
  - ship Flax Wyrm -> Rouhomme: +3/turn
  - spinnery 1 2.08 -> 1.60: +18/turn
  - logging camp w/ tool [split timber 1] 0.00 -> 7.40: +11/turn
  - ropewalk 1 0.87 -> 0.69: +8/turn
  - quarry 1 0.08 -> 0.01: +6/turn
  - retting pit 1 1.01 -> 0.78: +3/turn
  - flax farm 1 5.83 -> 4.36: +10/turn
  - logging camp w/ tool 5.00 -> 0.00: -2/turn
  - weavery 1 0.00 -> 0.12: -6/turn
- Model check over the last 11 turns: predicted +165/turn for the settings we ran, real +63/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.45, thread 3.58, cloth 5.75, flax fibres 4.12, garments 16.71, nets 26.67, beer 2.66, timber 5.08, prestige 52.44, cash 0.00
- Orders it would set: arms buy 1 (v2 None); cloth sell 3 (v2 none); furniture buy 2 (v2 None); garments sell 7 (v2 none); grain buy 37 (v2 63); labour buy 98 (v2 95); light armour buy 1 (v2 None); porterage buy 16 (v2 6); thread sell 21 (v2 none)
- Recipe: logging camp w/ tool cut firewood 1 -> split timber 1 at 7.40, worth +11/turn.
- Recipe: net maker make nets 2 -> make nets 3 at 0.70, worth +26/turn.
- Ship linen snake: Grandgues -> Vauxvais (+13/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Rouhomme (+1/turn over staying).
- Management: ~13.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +72/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new chandlery (make tallow candles 2) for ~4026 coin: +1/turn, payback 3775 turns, doesn't pay yet (materials thin at home: bricks, nails)
- Trim: donate quarry 1: +20/turn (tax 20 saved).
- Trim: donate weavery 1: +16/turn (tax 18 saved).
- Trim: donate sewing shop 1: +10/turn (tax 12 saved).

## Chain sizing

Mode HOLD, garments sold 0.0/turn (+0.0 exported); plan makes 0.0 garments a turn.
Labour: own 500, everything else 443, chain may buy 0 -> chain allowance 57, chain plan 165 (-86 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.83 | 3.77 |
| ret | 3 | 1.01 | 0.67 |
| spin | 4 | 2.08 | 1.38 |
| weave | 3 | 0.00 | 0.00 |
| sew | 2 | 0.00 | 0.00 |

Buffers: flax fibres 47/64, thread 499/190, cloth 36/0
- chain plan needed 166 labour, budget left 57: cut to 166

## Self-diagnosis

Nothing found this run.
