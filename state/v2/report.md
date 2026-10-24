# v2 shadow report

Turn 13505, 2026-10-24 02:02. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 871, prestige 3,588 (468 free, -0.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 67 | 0 | 7 | 0 | 0 | min_holding 60, sell 74, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 32 | 0 | 7 | 0 | 0 | stop 15, buy 1, buy @ 2.4; sell 3, sell @ 1.64 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 116 | 0 | 2 | 0 | 0 | min_holding 30, sell 6, sell @ 18 |
| grain | 102 | 32 | 37 | 0 | 0 | stop 125, buy 32, buy @ 3.7 |
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
- **flax plants**: flax plants buffer thin: 1.1 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 182

## Notes

- labour: projection runs 100 over real use lately; planning 586, not 686

## Prestige spending, cheapest coin per prestige first

896 turns left: prestige gained now converts 98.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 43.5 | 43.5 | running |
| hold banquet 4 (pies) | mansion | 18 | 50.2 | 50.2 | thin at home: hop beer, wine, candles |
| hold banquet 3 (pies) | mansion | 8 | 50.3 | 50.3 | thin at home: hop beer, pies, candles |
| jousting 3 | arena | 230 | 51.2 | 51.3 | needs a arena (build cost 23,956); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 51.4 | 51.4 | thin at home: wine, pies, candles |
| hold prayer 2 | chapel | 13 | 49.3 | 52.1 | needs a chapel (build cost 30,263); thin at home: furniture |
| hold banquet 3 (fish) | mansion | 7.6 | 52.6 | 52.6 | thin at home: hop beer |
| hold banquet 2 (fish) | mansion | 6.8 | 53.0 | 53.0 | thin at home: wine |
| hold banquet 1 (fish) | mansion | 4.2 | 53.1 | 53.1 |  |
| hold banquet 3 (meat) | mansion | 7.6 | 53.4 | 53.4 | thin at home: hop beer |
| hold banquet 4 | mansion | 17.5 | 53.5 | 53.5 | thin at home: wine, hop beer, ham, candles |
| hold banquet 2 (meat) | mansion | 6.8 | 53.9 | 53.9 | thin at home: wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only -3 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -1 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~91 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.29 | 0.60 (54/turn) | beer 73 (2.92->5.84), lead bars 5 (14.91->16.91), blades 1 (15.33->20.9), hop beer 1 (8.4->12.73) | candles 1 (67.2->70), garments 2 (17.85->19.4), spinning wheels 1 (241.5->243.2) | +198 |
| Amsdermund | 1111 | 0.34 | 1.00 (91/turn) | beer 73 (2.92->4.37), thread 62 (4.66->5.22), nets 3 (35->37.43), tallow 2 (19.74->22.8) | tin ingots 1 (31.29->34.58) | +86 |
| Caillechâtel | 488 | 0.12 | 0.20 (18/turn) | beer 38 (2.92->5.27), wine 3 (5.72->6.22), wrought iron 1 (12.71->12.82) | jewellery 1 (91.88->92.62), raw cloth 1 (6.3->7.08), furniture 1 (13.23->13.9) | +75 |
| Rouhomme | 368 | 0.09 | 1.00 (91/turn) | beer 66 (2.92->3.42), bread 129 (2.31->2.68), charcoal 11 (1.61->3.31), timber 17 (6.77->8.64) | candles 0 (68.25->70), flax fibres 6 (5.35->5.6) | +65 |
| Fontaux | 411 | 0.10 | 0.40 (36/turn) | salt 12 (5.04->7.79), charcoal 13 (1.61->4.27), firewood 2 (1.61->6.13), wine 5 (5.72->6.13) | candles 1 (67.73->70), raw cloth 2 (6.46->7.08) | +60 |

**Best:** Hofkirchen at about +198 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 27.8, stop 1 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 3.0 turns |
| beer |  | 73 @ min 3.38 |  |
| cloth |  | 4 @ min 7 | goal planner: sells 4 a turn at 7, keeps 0 (no one offered it) |
| cured meat | 1 @ 29.0, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 1) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 1 @ 2.4, stop 15 | 3 @ min 1.64 | makes 6.5, uses 7.3, holds 32 (keeps 0): sells the surplus + 3/turn of the excess |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 1 @ min 1.4 | goal planner: sells 1 a turn at 1.4, keeps 274 (no one offered it) |
| garments |  | 6 @ min 19 | goal planner: sells 6 a turn at 19, keeps 30 (no one offered it) |
| grain | 37 @ 3.7, stop 146 |  | goal planner: buys 37 a turn for today's rates, keeps up to 146 (v2 had 60) |
| labour | 98 @ 2.2, stop - |  | goal planner: buys 98 for today's rates (v2 had 86) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 11 @ min 34.0 |  |
| pasties | 3 @ 14.5, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 5.0 turns |
| porterage | 16 @ 1.1, stop - |  | goal planner: buys 16 for today's rates (v2 had 15) |
| rope |  | 6 @ min 72.0 | goal planner: sells 6 (v2 had 5) |
| tar | 1 @ 11.0, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 1) |
| thread |  | 13 @ min 4.56 | goal planner: sells 13 a turn at 4.56, keeps 249 (no one offered it) |
| tools | 3 @ 6.2, stop 17 |  | uses 2.0/turn (retting pit 1), makes 0.0, holds 200 = 98.4 turns |
| wax | 1 @ 20.2, stop 1 |  | uses 0.1/turn (net maker152202386007001), makes 0.0, holds 1 = 5.0 turns |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 16.4k (cash + stock at home prices); +43/turn over 6 turns, +26/turn over 24 turns.
- Limits: cash flow >= +130/turn, prestige >= -0.70/turn (values are after 240 tax a turn).
- Today's settings: value +132/turn, cash +362/turn, prestige -0.70/turn.
- Plan: value +244/turn, cash +361/turn, prestige -0.70/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -219 vs +303, +17 vs +194, -5 vs +272 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4, garments 0.5, nets 0.0, rope 0.1.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Vauxvais: +13/turn
  - net maker 0.50 -> 1.00: +31/turn
  - ropewalk 1 0.87 -> 1.00: +7/turn
  - quarry 1 0.08 -> 0.00: +7/turn
  - logging camp w/ tool 5.00 -> 0.00: -3/turn
  - logging camp w/ tool [split timber 1] 0.00 -> 20.00: +28/turn
  - flax farm 1 5.83 -> 9.77: -39/turn
  - retting pit 1 1.01 -> 1.73: +18/turn
  - spinnery 1 2.08 -> 3.14: -31/turn
  - weavery 1 0.00 -> 0.88: -28/turn
- Model check over the last 10 turns: predicted +169/turn for the settings we ran, real +14/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.45, thread 3.58, cloth 5.75, flax fibres 4.12, garments 16.70, nets 35.00, beer 2.67, timber 6.45, prestige 52.49, cash 0.00
- Orders it would set: cloth sell 4 (v2 none); flax plants sell 1 (v2 none); furniture buy 2 (v2 None); garments sell 6 (v2 none); grain buy 37 (v2 60); labour buy 98 (v2 86); light armour buy 1 (v2 None); porterage buy 16 (v2 15); rope sell 6 (v2 5); thread sell 13 (v2 none)
- Recipe: logging camp w/ tool cut firewood 1 -> split timber 1 at 20.00, worth +28/turn.
- Ship linen snake: Grandgues -> Vauxvais (+13/turn over staying).
- Ship Flax Wyrm: stays on Caillechâtel (worth +1/turn).
- Management: ~13.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +72/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot net maker for ~1408 coin: +32/turn, payback 44 turns
  - +1 plot ropewalk 1 for ~2738 coin: +21/turn, payback 132 turns
  - new jeweller (make jewellery 1) for ~4715 coin: +20/turn, payback 240 turns, doesn't pay yet (materials thin at home: bricks, nails, tiles)
- Trim: donate quarry 1: +20/turn (tax 20 saved).

## Chain sizing

Mode HOLD, garments sold 0.0/turn (+0.0 exported); plan makes 0.0 garments a turn.
Labour: own 500, everything else 443, chain may buy 0 -> chain allowance 57, chain plan 166 (-85 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.83 | 3.79 |
| ret | 3 | 1.01 | 0.67 |
| spin | 4 | 2.08 | 1.39 |
| weave | 3 | 0.00 | 0.00 |
| sew | 2 | 0.00 | 0.00 |

Buffers: flax fibres 46/64, thread 495/190, cloth 40/0
- chain plan needed 166 labour, budget left 57: cut to 166

## Self-diagnosis

- R7 stale ask: firewood ask 1.64 over the market for 3 turns: the town trades ~105 a turn at 1.52, we sold 0 with 32 over what we keep -> **sell price 1.64 -> 1.61 (last trade 1.52, floor 1.61)** (ok)
