# v2 shadow report

Turn 13503, 2026-10-24 00:33. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 859, prestige 3,589 (469 free, -0.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 69 | 0 | 7 | 0 | 0 | min_holding 60, sell 74, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 34 | 0 | 7 | 0 | 0 | stop 15, buy 1, buy @ 2.4; sell 3, sell @ 1.63 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 126 | 0 | 2 | 0 | 0 | min_holding 30, sell 35, sell @ 20 |
| grain | 111 | 31 | 37 | 0 | 0 | stop 125, buy 32, buy @ 3.7 |
| labour | 95 | 111 | 596 | 0 | 15 | buy 95, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 34 |
| porterage | 13 | 13 | 13 | 2 | 0 | buy 13, buy @ 1.1 |

**2 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **porterage**: quarry 1 ran short of porterage (buy is live (13 @ 1.1), 13 bought last turn); labour need rises ~8/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **porterage**: buying 13, short of ~15 needed -> v2: buy 15

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.3 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 70
- **flax plants**: flax plants buffer thin: 1.0 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 182

## Notes

- labour: +5 crew for Flax Wyrm (crew 0.10, no projection from the game)
- labour: +5 crew for linen snake (crew 0.10, no projection from the game)
- labour: projection runs 100 over real use lately; planning 596, not 696

## Prestige spending, cheapest coin per prestige first

898 turns left: prestige gained now converts 98.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 43.8 | 43.8 | running |
| hold banquet 3 (pies) | mansion | 8 | 48.4 | 48.4 | thin at home: hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 48.6 | 48.6 | thin at home: hop beer, wine |
| jousting 3 | arena | 230 | 51.2 | 51.3 | needs a arena (build cost 24,673); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 51.7 | 51.7 | thin at home: wine, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 51.7 | 51.7 | thin at home: hop beer |
| hold banquet 4 | mansion | 17.5 | 51.9 | 51.9 | thin at home: wine, hop beer, ham |
| hold banquet 3 (meat) | mansion | 7.6 | 52.5 | 52.5 | thin at home: hop beer |
| hold prayer 2 | chapel | 13 | 50.2 | 53.1 | needs a chapel (build cost 31,048); thin at home: furniture |
| hold banquet 1 (fish) | mansion | 4.2 | 53.2 | 53.2 |  |
| hold sermon 2 (candles) | church | 31 | 51.6 | 54.2 | needs a church (build cost 65,560); thin at home: candles, furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 54.3 | 54.3 | thin at home: wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.10 | 9 | 134102075 | 0 | - | furniture 6 | -76 |
| linen snake | 0.0 / 0.10 | 9 | 151802239 | 0 | - | furniture 6 | -82 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only 1 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -1 a turn after crew: ship stays at 0
- best towns now: Hofkirchen +16
- Hofkirchen would trade: beer sell 9 @ 5.25, candles buy 1 @ 65.0, furniture buy 1 @ 12.3, garments buy 2 @ 17.9; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~91 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.29 | 0.60 (55/turn) | beer 73 (2.92->5.7), blades 2 (15.02->20.9), lead bars 5 (14.8->16.91), hop beer 2 (8.19->12.73) | premium ham 1 (388.5->419.9), harnesses 1 (53.03->66.5), steel ingots 6 (13.97->16.34), candles 1 (67.2->70) | +254 |
| Amsdermund | 1111 | 0.35 | 1.00 (91/turn) | beer 73 (2.92->4.54), thread 59 (4.66->5.22), nets 7 (35->37.43), tallow 2 (19.53->22.61) | premium ham 1 (308.7->419.9), steel ingots 4 (14.8->16.34), spinning wheels 2 (233.1->235.6) | +223 |
| Kirchwerp | 1072 | 0.33 | 0.10 (9/turn) | seeds 7 (1.92->2.85), wine 5 (6.51->7.22), potash 1 (18.48->19.95), wheels 1 (18.06->19.95) | premium ham 1 (262.5->419.9), raw cloth 1 (7.3->10.64), harnesses 1 (63.53->66.5), flax plants 2 (0.37->1.4) | +169 |
| Disscester | 1474 | 0.52 | 0.20 (18/turn) | gold ore 1 (191.1->243.2), nets 3 (35->36.67), cured meat 3 (22.26->23.37), dyed yarn 1 (6.88->7.5) | premium ham 1 (325.5->419.9), raw cloth 1 (6.51->10.64), harnesses 1 (63.53->66.5) | +145 |
| Neuborn | 780 | 0.19 | 0.30 (27/turn) | charcoal 13 (1.92->3.76), cloth 3 (7->7.89), rope 2 (74->74.58) | premium ham 1 (319.2->419.9), raw cloth 1 (6.83->10.64), casks 8 (4.35->4.8), harnesses 1 (65.1->66.5) | +112 |

**Best:** Hofkirchen at about +254 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 26.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had None) |
| beer |  | 74 @ min 3.38 | goal planner: sells 74 (v2 had 73) |
| cured meat | 1 @ 21.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had None) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 15 | 3 @ min 1.63 | makes 6.5, uses 7.3, holds 34 (keeps 0): sells the surplus + 3/turn of the excess |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.47 | goal planner: sells 2 a turn at 1.47, keeps 274 (no one offered it) |
| grain | 37 @ 3.7, stop 147 |  | goal planner: buys 37 a turn for today's rates, keeps up to 147 (v2 had 56) |
| labour | 98 @ 2.2, stop - |  | goal planner: buys 98 for today's rates (v2 had 96) |
| light armour | 1 @ 76.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| limestone |  | 1 @ min 17.3 | goal planner: sells 1 a turn at 17.3, keeps 153 (no one offered it) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 11 @ min 34.0 |  |
| pasties | 3 @ 14.5, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 4.9 turns |
| porterage | 16 @ 1.1, stop - |  | goal planner: buys 16 for today's rates (v2 had 15) |
| rope |  | 4 @ min 72.0 |  |
| tar | 1 @ 11.0, stop 4 |  | uses 1.0/turn (ropewalk 1), makes 0.0, holds 8 = 7.9 turns |
| thread |  | 10 @ min 4.62 | goal planner: sells 10 a turn at 4.62, keeps 249 (no one offered it) |
| tools | 3 @ 6.2, stop 17 |  | uses 2.0/turn (retting pit 1), makes 0.0, holds 200 = 98.4 turns |
| wax | 1 @ 20.2, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 16.8k (cash + stock at home prices); +107/turn over 6 turns, +41/turn over 24 turns.
- Limits: cash flow >= +131/turn, prestige >= -0.71/turn (values are after 240 tax a turn).
- Today's settings: value +116/turn, cash +194/turn, prestige -0.70/turn.
- Plan: value +181/turn, cash +253/turn, prestige -0.71/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +140 vs +238, +40 vs +264, -219 vs +303.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4, garments 0.5, nets 0.0, rope 0.1.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Vauxvais: +10/turn
  - ship Flax Wyrm -> Chatgnan: +1/turn
  - logging camp w/ tool 5.00 -> 20.00: +3/turn
  - sewing shop 1 0.00 -> 0.07: -5/turn
  - weavery 1 0.00 -> 0.12: +16/turn
  - flax farm 1 5.83 -> 7.39: -7/turn
  - retting pit 1 1.01 -> 1.29: +17/turn
  - net maker 0.50 -> 0.00: -35/turn
  - net maker [make nets 3] 0.00 -> 1.00: +71/turn
  - ropewalk 1 0.87 -> 0.00: -143/turn
- Model check over the last 9 turns: predicted +174/turn for the settings we ran, real +59/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.46, thread 3.61, cloth 5.80, flax fibres 4.17, garments 16.83, nets 35.00, beer 2.53, timber 5.99, prestige 51.50, cash 0.00
- Orders it would set: arms buy 1 (v2 None); beer sell 74 (v2 73); cured meat buy 1 (v2 None); flax plants sell 2 (v2 none); grain buy 37 (v2 56); labour buy 98 (v2 96); light armour buy 1 (v2 None); limestone sell 1 (v2 none); porterage buy 16 (v2 15); thread sell 10 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 1.00, worth +72/turn.
- Recipe: net maker make nets 2 -> make nets 3 at 1.00, worth +40/turn.
- Ship linen snake: Grandgues -> Vauxvais (+11/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Chatgnan (+1/turn over staying).
- Management: ~13.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +73/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot net maker for ~1289 coin: +31/turn, payback 42 turns
  - new jeweller (make jewellery 1) for ~4461 coin: +29/turn, payback 154 turns, doesn't pay yet (materials thin at home: bricks, tiles)
- Trim: donate quarry 1: +16/turn (tax 20 saved).
- Trim: donate weavery 1: +16/turn (tax 18 saved).
- Trim: donate logging camp w/ tool: +15/turn (tax 20 saved).

## Chain sizing

Mode HOLD, garments sold 0.0/turn (+0.0 exported); plan makes 0.0 garments a turn.
Labour: own 500, everything else 443, chain may buy 0 -> chain allowance 57, chain plan 174 (-78 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.83 | 3.95 |
| ret | 3 | 1.01 | 0.70 |
| spin | 4 | 2.08 | 1.45 |
| weave | 3 | 0.00 | 0.00 |
| sew | 2 | 0.00 | 0.00 |

Buffers: flax fibres 46/64, thread 459/190, cloth 44/0
- chain plan needed 173 labour, budget left 57: cut to 173

## Self-diagnosis

- R7 stale ask: garments ask 20 over the market for 6 turns: the town trades ~59 a turn at 19.5, we sold 0 with 96 over what we keep; floor 20 (config sell_floor / unit cost) is at or over the market: Taylor's call
