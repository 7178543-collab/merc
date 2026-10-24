# v2 shadow report

Turn 13504, 2026-10-24 01:01. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 876, prestige 3,589 (469 free, -0.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 68 | 0 | 7 | 0 | 0 | min_holding 60, sell 74, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 33 | 0 | 7 | 0 | 0 | stop 15, buy 1, buy @ 2.4; sell 3, sell @ 1.63 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 124 | 0 | 2 | 0 | 0 | min_holding 30, sell 35, sell @ 20 |
| grain | 107 | 32 | 37 | 0 | 0 | stop 125, buy 32, buy @ 3.7 |
| labour | 95 | 95 | 586 | 0 | 9 | buy 95, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 15 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 34 |
| porterage | 13 | 13 | 13 | 2 | 0 | buy 13, buy @ 1.1 |

**2 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **porterage**: quarry 1 ran short of porterage (buy is live (13 @ 1.1), 13 bought last turn); labour need rises ~8/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **porterage**: buying 13, short of ~15 needed -> v2: buy 15

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.3 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 70
- **flax plants**: flax plants buffer thin: 1.0 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 182

## Notes

- labour: projection runs 100 over real use lately; planning 586, not 686

## Prestige spending, cheapest coin per prestige first

897 turns left: prestige gained now converts 98.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 43.5 | 43.5 | running |
| hold banquet 4 (pies) | mansion | 18 | 48.4 | 48.4 | thin at home: hop beer, wine |
| hold banquet 3 (pies) | mansion | 8 | 48.7 | 48.7 | thin at home: hop beer, pies |
| hold banquet 2 (pies) | mansion | 7 | 50.0 | 50.0 | thin at home: wine, pies |
| jousting 3 | arena | 230 | 51.2 | 51.3 | needs a arena (build cost 23,765); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 51.7 | 51.7 | thin at home: hop beer |
| hold banquet 4 | mansion | 17.5 | 51.7 | 51.7 | thin at home: wine, hop beer, ham |
| hold banquet 2 (fish) | mansion | 6.8 | 52.0 | 52.0 | thin at home: wine |
| hold prayer 2 | chapel | 13 | 49.6 | 52.3 | needs a chapel (build cost 29,719); thin at home: furniture |
| hold banquet 3 (meat) | mansion | 7.6 | 52.7 | 52.7 | thin at home: hop beer |
| hold banquet 1 (fish) | mansion | 4.2 | 52.9 | 52.9 |  |
| hold banquet 2 (meat) | mansion | 6.8 | 53.1 | 53.1 | thin at home: wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only -1 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -1 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~91 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.29 | 0.60 (54/turn) | beer 73 (2.92->5.7), blades 2 (15.02->20.9), lead bars 5 (14.8->16.91), hop beer 2 (8.19->12.73) | premium ham 1 (388.5->419.9), harnesses 1 (53.03->66.5), steel ingots 6 (13.97->16.34), candles 1 (67.2->70) | +256 |
| Amsdermund | 1111 | 0.34 | 1.00 (91/turn) | beer 73 (2.92->4.54), thread 61 (4.66->5.22), nets 7 (35->37.43), tallow 2 (19.53->22.61) | premium ham 1 (308.7->419.9), steel ingots 4 (14.8->16.34), spinning wheels 2 (233.1->235.6) | +222 |
| Kirchwerp | 1072 | 0.33 | 0.10 (9/turn) | seeds 7 (1.92->2.85), wine 5 (6.51->7.22), potash 1 (18.48->19.95), wheels 1 (18.06->19.95) | premium ham 1 (262.5->419.9), raw cloth 1 (7.3->10.64), harnesses 1 (63.53->66.5), flax plants 2 (0.37->1.4) | +169 |
| Disscester | 1474 | 0.52 | 0.20 (18/turn) | gold ore 1 (191.1->243.2), nets 3 (35->36.67), cured meat 3 (22.26->23.37), dyed yarn 1 (6.88->7.5) | premium ham 1 (325.5->419.9), raw cloth 1 (6.51->10.64), harnesses 1 (63.53->66.5) | +145 |
| Neuborn | 780 | 0.19 | 0.30 (27/turn) | charcoal 13 (1.92->3.76), cloth 3 (7->7.89), rope 2 (74->74.58) | premium ham 1 (319.2->419.9), raw cloth 1 (6.83->10.64), casks 8 (4.35->4.8), harnesses 1 (65.1->66.5) | +112 |

**Best:** Hofkirchen at about +256 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ ?, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 4.0 turns |
| beer |  | 74 @ min 3.38 | goal planner: sells 74 (v2 had 73) |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 12 = 7.7 turns |
| cloth |  | 4 @ min 7 | goal planner: sells 4 a turn at 7, keeps 0 (no one offered it) |
| cured meat | 1 @ 29.0, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 1) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 1 @ 2.4, stop 15 | 3 @ min 1.64 | makes 6.5, uses 7.3, holds 33 (keeps 0): sells the surplus + 3/turn of the excess |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.54 | goal planner: sells 2 a turn at 1.54, keeps 274 (no one offered it) |
| garments |  | 6 @ min 18 | goal planner: sells 6 a turn at 18, keeps 30 (no one offered it) |
| grain | 37 @ 3.7, stop 148 |  | goal planner: buys 37 a turn for today's rates, keeps up to 148 (v2 had 58) |
| labour | 98 @ 2.2, stop - |  | goal planner: buys 98 for today's rates (v2 had 86) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 11 @ min 34.0 |  |
| pasties | 3 @ 14.5, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 4.9 turns |
| porterage | 16 @ 1.1, stop - |  | goal planner: buys 16 for today's rates (v2 had 15) |
| rope |  | 4 @ min 72.0 |  |
| tar | 1 @ 11.0, stop 4 |  | uses 0.9/turn (ropewalk 1), makes 0.0, holds 7 = 7.8 turns |
| thread |  | 10 @ min 4.62 | goal planner: sells 10 a turn at 4.62, keeps 249 (no one offered it) |
| tools | 3 @ 6.2, stop 17 |  | uses 2.0/turn (retting pit 1), makes 0.0, holds 200 = 98.4 turns |
| wax | 1 @ 20.2, stop 1 |  | uses 0.1/turn (net maker152202386007001), makes 0.0, holds 1 = 6.0 turns |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 16.8k (cash + stock at home prices); +107/turn over 6 turns, +41/turn over 24 turns.
- Limits: cash flow >= +130/turn, prestige >= -0.70/turn (values are after 240 tax a turn).
- Today's settings: value +118/turn, cash +272/turn, prestige -0.70/turn.
- Plan: value +226/turn, cash +270/turn, prestige -0.70/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +40 vs +264, -219 vs +303, +17 vs +194 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4, garments 0.5, nets 0.0, rope 0.1.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Vauxvais: +10/turn
  - ship Flax Wyrm -> Heidlowe: +1/turn
  - quarry 1 0.08 -> 0.00: +7/turn
  - logging camp w/ tool 5.00 -> 0.00: -2/turn
  - logging camp w/ tool [split timber 1] 0.00 -> 20.00: +21/turn
  - flax farm 1 5.83 -> 9.43: -25/turn
  - retting pit 1 1.01 -> 1.66: +12/turn
  - net maker 0.50 -> 0.00: -35/turn
  - net maker [make nets 3] 0.00 -> 1.00: +73/turn
  - spinnery 1 2.08 -> 2.94: -40/turn
- Model check over the last 9 turns: predicted +172/turn for the settings we ran, real +59/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.45, thread 3.58, cloth 5.75, flax fibres 4.12, garments 16.70, nets 35.00, beer 2.53, timber 6.05, prestige 51.40, cash 0.00
- Orders it would set: beer sell 74 (v2 73); cloth sell 4 (v2 none); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 6 (v2 none); grain buy 37 (v2 58); labour buy 98 (v2 86); light armour buy 1 (v2 None); porterage buy 16 (v2 15); thread sell 10 (v2 none)
- Recipe: logging camp w/ tool cut firewood 1 -> split timber 1 at 20.00, worth +21/turn.
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 1.00, worth +71/turn.
- Recipe: net maker make nets 2 -> make nets 3 at 1.00, worth +42/turn.
- Ship linen snake: Grandgues -> Vauxvais (+10/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Heidlowe (+1/turn over staying).
- Management: ~13.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +72/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new jeweller (make jewellery 1) for ~4590 coin: +33/turn, payback 141 turns, doesn't pay yet (materials thin at home: bricks, nails, tiles)
  - +1 plot net maker for ~1347 coin: +32/turn, payback 42 turns
- Trim: donate quarry 1: +20/turn (tax 20 saved).

## Chain sizing

Mode HOLD, garments sold 0.0/turn (+0.0 exported); plan makes 0.0 garments a turn.
Labour: own 500, everything else 443, chain may buy 0 -> chain allowance 57, chain plan 169 (-82 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.83 | 3.86 |
| ret | 3 | 1.01 | 0.69 |
| spin | 4 | 2.08 | 1.41 |
| weave | 3 | 0.00 | 0.00 |
| sew | 2 | 0.00 | 0.00 |

Buffers: flax fibres 46/64, thread 481/190, cloth 44/0
- chain plan needed 169 labour, budget left 57: cut to 169

## Self-diagnosis

Nothing found this run.
