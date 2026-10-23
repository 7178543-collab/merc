# v2 shadow report

Turn 13502, 2026-10-23 23:26. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 948, prestige 3,590 (470 free, -0.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 7 | 0 | 0 | min_holding 60, sell 69, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 34 | 0 | 7 | 0 | 0 | stop 28, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 128 | 0 | 2 | 0 | 0 | min_holding 30, sell 35, sell @ 20 |
| grain | 116 | 0 | 33 | 0 | 0 | stop 124, buy 31, buy @ 3.7 |
| labour | 111 | 43 | 532 | 0 | 11 | buy 111, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34 |
| porterage | 10 | 10 | 10 | 2 | 0 | buy 10, buy @ 1.1 |

**3 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **porterage**: logging camp w/ tool ran short of porterage (buy is live (10 @ 1.1), 10 bought last turn); labour need rises ~4/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **porterage**: buying 10, short of ~12 needed -> v2: buy 12
- **wax**: net maker152202386007001 ran short of wax (buy is live (1 @ 23.2), home ask 19.40 x2, yet 0 bought last turn); labour need rises ~12/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: buying 111, need ~38 -> v2: buy 38

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.6 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 57
- **flax plants**: flax plants buffer thin: 1.0 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 182

## Notes

- labour: projection runs 106 over real use lately; planning 538, not 644

## Prestige spending, cheapest coin per prestige first

899 turns left: prestige gained now converts 98.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 43.8 | 43.8 | running |
| hold banquet 4 (pies) | mansion | 18 | 47.8 | 47.8 | thin at home: hop beer, wine |
| hold banquet 3 (pies) | mansion | 8 | 48.7 | 48.7 | thin at home: hop beer, pies |
| hold banquet 2 (pies) | mansion | 7 | 50.7 | 50.7 | thin at home: wine, pies |
| hold banquet 4 | mansion | 17.5 | 51.1 | 51.1 | thin at home: wine, hop beer, ham |
| jousting 3 | arena | 230 | 51.1 | 51.3 | needs a arena (build cost 23,897); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 52.5 | 52.5 | thin at home: hop beer |
| hold prayer 2 | chapel | 13 | 50.2 | 53.0 | needs a chapel (build cost 29,898); thin at home: furniture |
| hold banquet 3 (meat) | mansion | 7.6 | 53.1 | 53.1 | thin at home: hop beer, cured meat |
| hold banquet 2 (fish) | mansion | 6.8 | 53.4 | 53.4 | thin at home: wine |
| hold banquet 1 (fish) | mansion | 4.2 | 53.5 | 53.5 |  |
| hold banquet 2 (meat) | mansion | 6.8 | 54.0 | 54.0 | thin at home: wine, cured meat |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 9 | 134102075 | 0.2 | beer 21 | furniture 6 | -31 |
| linen snake | 0.1 / 0.10 | 9 | 151802239 | 0.096 | - | furniture 6 | -82 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only -8 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -1 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~91 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.29 | 0.50 (46/turn) | beer 63 (2.94->5.65), hop beer 3 (8.03->12.44), blades 2 (15.02->20.52), lead bars 5 (15.02->16.72) | harnesses 1 (52.5->66.5), premium ham 1 (323.4->336.3), gold ore 1 (149.1->161.5), steel ingots 5 (14.6->15.2) | +207 |
| Vauxvais | 204 | 0.05 | 0.20 (18/turn) | lead ore 10 (10.45->12.35), wax 2 (20.37->27.17), beer 62 (2.94->3.25), tin ingots 1 (41.79->48.45) | premium ham 1 (291.9->336.3), thread 18 (4.41->4.68), pasties 2 (11.65->13.4), candles 1 (68.25->70) | +105 |
| Briclives | 1041 | 0.31 | 0.60 (55/turn) | beer 63 (2.94->4.89), flour 2 (19.43->23.18), pasties 1 (12.3->15.2), wheels 1 (18.06->19.95) | chisels 2 (8.4->12.25), belts 1 (28.35->29.45) | +91 |
| Bedenis | 566 | 0.14 | 0.10 (9/turn) | pasties 1 (12.3->14.34), dyed yarn 1 (5.67->6.37), rope 3 (74->74.58), wheels 1 (18.06->19.19) | premium ham 1 (260.4->336.3), candles 1 (66.67->70), belts 1 (27.3->29.45), chisels 1 (9.66->12.25) | +88 |
| Fontaux | 411 | 0.10 | 0.80 (73/turn) | bread 138 (2.07->2.53), charcoal 13 (1.92->4.18), casks 4 (6.09->9.5), beer 57 (2.94->3.19) | premium ham 1 (317.1->336.3), harnesses 1 (61.43->66.5), candles 1 (67.73->70) | +87 |

**Best:** Hofkirchen at about +207 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 27.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 64 @ min 3.38 |  |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 12 = 7.7 turns |
| cured meat | 1 @ 21.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had None) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 7 @ 2.4, stop 28 |  | uses 6.8/turn (brewery 1, household upkeep), makes 0.0, holds 34 = 5.0 turns |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| grain | 32 @ 3.7, stop 125 |  | goal planner: buys 32 a turn for today's rates, keeps up to 125 (v2 had 41) |
| labour | 36 @ 2.2, stop - |  | goal planner: buys 36 for today's rates (v2 had 38) |
| light armour | 1 @ 78, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 9 @ min 34.0 |  |
| pasties | 3 @ 14.5, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 13 = 4.8 turns |
| porterage | 13 @ 1.1, stop - |  | goal planner: buys 13 for today's rates (v2 had 12) |
| rope |  | 4 @ min 72.0 |  |
| tar | 1 @ 8.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had None) |
| tools | 3 @ 6.2, stop 5 |  | uses 2.0/turn (retting pit 1), makes 0.0, holds 200 = 98.4 turns |
| wax | 1 @ 20.2, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 16.5k (cash + stock at home prices); +46/turn over 6 turns, +46/turn over 24 turns.
- Limits: cash flow >= +127/turn, prestige >= -0.71/turn (values are after 240 tax a turn).
- Today's settings: value +84/turn, cash +306/turn, prestige -0.71/turn.
- Plan: value +187/turn, cash +270/turn, prestige -0.71/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -199 vs +322, +140 vs +238, -89 vs +264.
- Route sales counted at most (what the ships really sold, a turn): garments 0.5, nets 0.0, rope 0.1.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Nürnnieder: +2/turn
  - ship Flax Wyrm -> Vauxvais: +2/turn
  - flax farm 1 4.66 -> 7.71: +32/turn
  - brewery 1 0.50 -> 0.56: +6/turn
  - quarry 1 0.00 -> 0.08: +4/turn
  - logging camp w/ tool 5.00 -> 20.00: +3/turn
  - retting pit 1 1.01 -> 1.36: -0/turn
  - spinnery 1 1.70 -> 2.21: +1/turn
  - sewing shop 1 0.00 -> 0.09: -6/turn
  - weavery 1 0.00 -> 0.15: +20/turn
- Model check over the last 7 turns: predicted +183/turn for the settings we ran, real +46/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.46, thread 3.61, cloth 5.80, flax fibres 4.17, garments 16.83, nets 35.00, beer 2.53, timber 5.94, prestige 51.50, cash 0.00
- Orders it would set: cured meat buy 1 (v2 None); grain buy 32 (v2 41); labour buy 36 (v2 38); light armour buy 1 (v2 None); porterage buy 13 (v2 12); tar buy 1 (v2 None)
- Recipe: net maker make nets 2 -> make nets 3 at 1.00, worth +41/turn.
- Ship linen snake: Grandgues -> Nürnnieder (+2/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Vauxvais (+3/turn over staying).
- Management: ~13.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +73/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new chandlery (make candles 2) for ~3927 coin: +41/turn, payback 96 turns, doesn't pay yet (materials thin at home: bricks)
  - +1 plot net maker for ~1283 coin: +35/turn, payback 36 turns
  - new jeweller (make jewellery 1) for ~4427 coin: +20/turn, payback 217 turns, doesn't pay yet (materials thin at home: bricks, tiles)
- Trim: donate quarry 1: +16/turn (tax 20 saved).
- Trim: donate weavery 1: +16/turn (tax 18 saved).
- Trim: donate logging camp w/ tool: +15/turn (tax 20 saved).

## Chain sizing

Mode HOLD, garments sold 0.0/turn (+0.0 exported); plan makes 0.0 garments a turn.
Labour: own 500, everything else 426, chain may buy 0 -> chain allowance 74, chain plan 178 (-31 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.66 | 4.05 |
| ret | 3 | 1.01 | 0.72 |
| spin | 4 | 1.70 | 1.48 |
| weave | 3 | 0.00 | 0.00 |
| sew | 2 | 0.00 | 0.00 |

Buffers: flax fibres 46/64, thread 438/190, cloth 44/0
- chain plan needed 178 labour, budget left 74: cut to 178

## Self-diagnosis

- R7 stale ask: garments ask 20 over the market for 6 turns: the town trades ~58 a turn at 19.5, we sold 0 with 98 over what we keep; floor 20 (config sell_floor / unit cost) is at or over the market: Taylor's call
