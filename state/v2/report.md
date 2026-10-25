# v2 shadow report

Turn 13527, 2026-10-25 00:00. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 989, prestige 3,571 (451 free, -1.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 82, sell @ 2.98 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 4 | 0 | 6 | 0 | 0 | stop 6, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 33 | 0 | 2 | 0 | 0 | min_holding 30, sell 7, sell @ 17.8 |
| grain | 30 | 10 | 24 | 0 | 0 | stop 145, buy 10, buy @ 3.7 |
| labour | 24 | 24 | 524 | 75 | 0 | buy 24, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 12, sell @ 34 |
| porterage | 13 | 13 | 5 | 0 | 8 | buy 13, buy @ 1.1 |

**3 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.2 turns (holds 2, next step uses 17/turn) -> v2: check the step that makes it
- **grain**: only 0.7 turns of grain left and buying 10 (need 83) -> v2: buy 83
- **labour**: buying 24, short of ~99 needed -> v2: buy 99

## Tuning

- **firewood**: we make 0/turn more than we use but there is no sell order -> v2: sell 0
- **flax fibres**: flax fibres buffer thin: 1.2 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 57
- **flax plants**: flax plants buffer thin: 2.0 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 149

## Notes

- labour: projection runs 139 over real use lately; planning 599, not 665

## Prestige spending, cheapest coin per prestige first

874 turns left: prestige gained now converts 98.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 46.8 | 46.8 | running |
| hold banquet 4 (pies) | mansion | 18 | 49.4 | 49.4 | thin at home: hop beer, wine, pies |
| hold banquet 3 (pies) | mansion | 8 | 50.2 | 50.2 | thin at home: hop beer, pies |
| hold banquet 2 (pies) | mansion | 7 | 51.1 | 51.1 | thin at home: wine, pies |
| hold banquet 4 | mansion | 17.5 | 52.7 | 52.7 | thin at home: wine, hop beer, stockfish |
| jousting 3 | arena | 230 | 52.6 | 52.7 | needs a arena (build cost 25,041); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold prayer 2 | chapel | 13 | 50.0 | 53.0 | needs a chapel (build cost 31,816); thin at home: furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 53.3 | 53.3 | thin at home: wine |
| hold banquet 2 (meat) | mansion | 6.8 | 53.3 | 53.3 | thin at home: wine |
| hold banquet 3 (fish) | mansion | 7.6 | 53.4 | 53.4 | thin at home: hop beer |
| hold banquet 3 (meat) | mansion | 7.6 | 53.4 | 53.4 | thin at home: hop beer |
| hold sermon 2 (candles) | church | 31 | 51.9 | 54.6 | needs a church (build cost 65,973); thin at home: jewellery, candles, furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0.032 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only 3 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -1 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~97 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.30 | 0.20 (19/turn) | windows 1 (504->641.25), wrought iron 7 (14.18->17.39), glass ingots 2 (59.85->68.4), salt 16 (4.3->4.73) | jewellery 2 (98.17->99.75), beer 4 (2.29->3.5), candles 1 (71.4->74), garments 2 (18.9->19.3) | +183 |
| Heilegg | 826 | 0.22 | 0.20 (19/turn) | grindstones 1 (270.9->347.7), windows 1 (504->570), nets 6 (35.6->37.43) | candles 1 (72.98->74), silver ore 1 (34.65->36.1) | +136 |
| Rotterburg | 1056 | 0.34 | 0.10 (10/turn) | windows 1 (504->622.25), nets 4 (35.6->36.48), garments 6 (17.8->18.14), hides 1 (14.28->15.01) | candles 1 (69.83->74) | +120 |
| Kirchwerp | 1072 | 0.35 | 0.20 (19/turn) | windows 1 (504->589), glass ingots 2 (59.85->68.88), lead ore 1 (8.82->19.95), salt 21 (4.3->4.75) | nails 13 (5.41->5.98), garments 2 (18.9->19.3), tools 1 (4.28->4.64) | +114 |
| Brunnham | 1281 | 0.46 | 0.20 (19/turn) | windows 1 (504->603.25), nets 6 (35.6->38.57), garments 6 (17.8->18.9), steel ingots 1 (13.97->14.44) | candles 1 (67.2->74) | +111 |

**Best:** Hofkirchen at about +183 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 26.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 82 @ min 2.98 | goal planner: sells 82 at 2.98 (v2 had 82 at 3.38) |
| cured meat | 1 @ 29.0, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 2) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 6 | 0 @ min 1.72 | goal planner: buys 2 a turn for today's rates, keeps up to 6 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 13.2, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 7 @ min 17.8 | goal planner: sells 7 at 17.8 (v2 had 6 at 20.0) |
| grain | 30 @ 3.7, stop 119 |  | goal planner: buys 30 a turn for today's rates, keeps up to 119 (v2 had 83) |
| labour | 95 @ 2.2, stop - |  | goal planner: buys 95 for today's rates (v2 had 99) |
| light armour | 1 @ 84.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 12 @ min 34 | goal planner: sells 12 at 34 (v2 had 12 at 34.6) |
| pasties | 3 @ 14.5, stop 11 |  | goal planner: buys 3 a turn for today's rates, keeps up to 11 (v2 had 4) |
| porterage | 13 @ 1.1, stop - |  | goal planner: buys 13 for today's rates (v2 had 12) |
| rope |  | 4 @ min 66.5 | makes 2.0, uses 0.2, holds 32 (keeps 0): sells the surplus + 3/turn of the excess |
| thread |  | 10 @ min 4.1 | goal planner: sells 10 a turn at 4.1, keeps 221 (no one offered it) |
| tools | 2 @ 6.2, stop 16 |  | uses 2.0/turn (net maker152202386007001, retting pit 1), makes 0.0, holds 200 = 101.8 turns |
| varnish | 1 @ 21.4, stop 1 |  | uses 0.1/turn (net maker152202386007001), makes 0.0, holds 0 = 2.2 turns |
| wax | 1 @ 20.8, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 18.0k (cash + stock at home prices); -36/turn over 6 turns, +61/turn over 24 turns.
- Limits: cash flow >= +125/turn, prestige >= -0.63/turn (values are after 240 tax a turn).
- Today's settings: value -23/turn, cash -59/turn, prestige -0.62/turn - breaks the cash floor.
- Plan: value +29/turn, cash +125/turn, prestige -0.63/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -167 vs +11, -144 vs +6, +293 vs -37.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4, garments 0.5, nets 0.0, rope 0.1.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Rouhomme: +0/turn
  - brewery 1 0.63 -> 0.45: +30/turn
  - logging camp w/ tool 5.00 -> 0.00: +2/turn
  - logging camp w/ tool [split timber 1] 0.00 -> 1.67: +2/turn
  - sewing shop 1 0.21 -> 0.15: -1/turn
  - spinnery 1 1.70 -> 1.18: -16/turn
  - retting pit 1 0.83 -> 0.57: +7/turn
  - flax farm 1 4.60 -> 3.31: +12/turn
  - ropewalk 1 0.50 -> 0.00: -11/turn
  - ropewalk 1 [make rope 2] 0.00 -> 0.31: +18/turn
- Model check over the last 32 turns: predicted +120/turn for the settings we ran, real +55/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.60, thread 4.00, cloth 6.40, flax fibres 4.68, garments 18.55, nets 29.59, beer 2.87, timber 5.61, prestige 55.17, cash 0.04
- Orders it would set: cured meat buy 1 (v2 2); firewood buy 2 (v2 3); furniture buy 2 (v2 None); garments sell 7 (v2 6); grain buy 30 (v2 83); labour buy 95 (v2 99); light armour buy 1 (v2 None); pasties buy 3 (v2 4); porterage buy 13 (v2 12); thread sell 10 (v2 none)
- Recipe: logging camp w/ tool cut firewood 1 -> split timber 1 at 1.67, worth +2/turn.
- Recipe: ropewalk 1 make rope 1 -> make rope 2 at 0.31, worth +2/turn.
- Recipe: net maker make nets 3 -> make nets 2 at 0.63, worth +16/turn.
- Ship linen snake: Grandgues -> Rouhomme (+2/turn over staying).
- Ship Flax Wyrm: stays on Caillechâtel (worth +5/turn).
- Management: ~13.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +80/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
- Trim: donate quarry 1: +20/turn (tax 20 saved).
- Trim: donate logging camp w/ tool: +19/turn (tax 20 saved).

## Chain sizing

Mode HOLD, garments sold 8.6/turn (+0.0 exported); plan makes 0.0 garments a turn.
Labour: own 500, everything else 434, chain may buy 0 -> chain allowance 66, chain plan 94 (-166 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.60 | 2.14 |
| ret | 3 | 0.83 | 0.38 |
| spin | 4 | 1.70 | 0.79 |
| weave | 3 | 0.33 | 0.00 |
| sew | 2 | 0.21 | 0.00 |

Buffers: flax fibres 36/47, thread 852/138, cloth 2/0
- chain plan needed 94 labour, budget left 66: cut to 94

## Self-diagnosis

- R1: firewood slot dry: 3.7 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask 1.77; our bid is already at/over the ask (sellers too thin)
- R5: varnish buy not filling: bid 17.1 under the home ask 20.4 for 4 turns, bought 0.0 of 1, 0.3 held (2.3 turns); raise needs Taylor (ceiling None)
