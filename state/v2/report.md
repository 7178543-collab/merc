# v2 shadow report

Turn 13493, 2026-10-23 14:04. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 2,374, prestige 3,601 (481 free, -1.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 95 | 0 | 4 | 0 | 0 | min_holding 60, sell 53, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 116 | 0 | 2 | 0 | 0 | min_holding 30, sell 14, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 0 | 0 | 473 | 0 | 27 | buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 34.6 |
| porterage | 10 | 10 | 8 | 0 | 2 | buy 10, buy @ 1.1 |

**0 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **linen snake**: linen snake cost 9 coin last turn (crew 0.10) and its route traded nothing (route limited by rope) -> v2: pause it (crew 0) until a route is proven to sell

## Tuning

- **flax plants**: flax plants buffer thin: 1.6 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 111

## Notes

- labour: projection runs 100 over real use lately; planning 473, not 573

## Prestige spending, cheapest coin per prestige first

908 turns left: prestige gained now converts 98.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 44.4 | 44.4 | running |
| hold banquet 3 (pies) | mansion | 8 | 47.0 | 47.0 | thin at home: hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 47.7 | 47.7 | thin at home: hop beer |
| hold banquet 2 (pies) | mansion | 7 | 50.1 | 50.1 | thin at home: pies |
| hold banquet 3 (fish) | mansion | 7.6 | 50.9 | 50.9 | thin at home: hop beer |
| hold banquet 4 | mansion | 17.5 | 51.0 | 51.0 | thin at home: hop beer, ham |
| jousting 3 | arena | 230 | 52.3 | 52.4 | needs a arena (build cost 24,469); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (meat) | mansion | 7.6 | 52.8 | 52.8 | thin at home: hop beer |
| hold sermon 2 (candles) | church | 31 | 50.3 | 52.8 | needs a church (build cost 65,504); thin at home: candles, furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 53.2 | 53.2 |  |
| hold prayer 2 | chapel | 13 | 50.7 | 53.6 | needs a chapel (build cost 31,044); thin at home: furniture |
| hold banquet 1 (fish) | mansion | 4.2 | 53.9 | 53.9 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 9 | 151802239 | 0.04 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -1 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~93 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Cobholme | 1564 | 0.58 | 0.30 (28/turn) | sails 1 (603.75->674.5), rope 2 (54.73->78.38), candles 2 (74.03->82.17), wine 5 (5.35->8.55) | gears 1 (56.7->61.75) | +152 |
| Briclives | 1041 | 0.32 | 0.60 (56/turn) | malt 7 (6.51->13.01), rope 2 (54.73->72.67), beer 54 (3.16->4.37), cheese 10 (6.35->7.03) | dyed cloth 1 (11.97->12.44), tools 2 (4.26->4.62) | +116 |
| Hofkirchen | 991 | 0.29 | 0.50 (46/turn) | rope 2 (54.73->70.3), beer 54 (3.16->4.26), flax plants 7 (1.26->3.89), wine 5 (5.35->7.55) | bellows 1 (254.1->262.2), acid 1 (139.65->142.5), candles 1 (67.2->70.5), gears 2 (60.38->61.75) | +105 |
| Fontaux | 411 | 0.10 | 0.20 (19/turn) | rope 2 (54.73->67.92), charcoal 13 (1.99->4.16), flax fibres 3 (5.5->7.93), tools 14 (4.48->4.89) | gold bars 1 (798->817), candles 1 (67.73->70.5), cheese 10 (5.35->5.7), dyed cloth 1 (11.45->12.44) | +91 |
| Amsdermund | 1111 | 0.35 | 0.70 (65/turn) | rope 2 (54.73->71.72), beer 54 (3.16->4.46), wine 5 (5.35->7.74), nets 6 (35->37.05) | spirits 3 (15.75->17.1), acid 1 (140.7->142.5), garments 2 (18.9->19.6) | +89 |

**Best:** Cobholme at about +152 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 52 @ min 3.38 |  |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 0 @ 2.2, stop - |  | uses 472.6/turn (brewery 1, flax farm 1, household), makes 500.0, holds 0 |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 11 @ min 34.0 |  |
| pasties | 3 @ 13.3, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 4.9 turns |
| porterage | 8 @ 1.1, stop - |  | uses 8.1/turn (observed), makes 0.0, holds 10 = 1.2 turns |
| rope |  | 2 @ min 72.5 |  |
| timber |  | 9 @ min 6.5 |  |
| tools | 3 @ 6.2, stop 24 |  | uses 3.0/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 66.6 turns |

## Goal: business value (shadow)
- Value now 16.2k (cash + stock at home prices); +93/turn over 6 turns, -81/turn over 24 turns.
- Limits: cash flow >= +68/turn, prestige >= -0.75/turn (after 235 tax and crew).
- Today's settings: value +119/turn, cash +279/turn, prestige -1.41/turn - breaks the prestige floor.
- Plan: value +151/turn, cash +210/turn, prestige -0.75/turn, inside both limits.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ropewalk 1 0.50 -> 0.93: +23/turn
  - quarry 1 0.00 -> 0.08: +6/turn
  - net maker 0.50 -> 0.92: +5/turn
  - logging camp w/ tool 7.00 -> 6.32: +2/turn
  - sewing shop 1 0.00 -> 0.13: -9/turn
  - weavery 1 0.00 -> 0.20: +4/turn
  - flax farm 1 3.47 -> 5.97: -16/turn
  - retting pit 1 0.62 -> 1.06: -4/turn
  - spinnery 1 1.27 -> 2.07: +55/turn
  - mansion 1 0.00 -> 0.16: -37/turn
- Model check over the last 12 turns: predicted +89/turn for the settings we ran, real +40/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.48, thread 3.66, cloth 5.88, flax fibres 4.23, garments 17.06, nets 27.53, beer 2.60, timber 4.93, prestige 53.92, cash 0.00
- Orders it would set (dry run): beer sell 53 (v2 52); porterage buy 9 (v2 8); rope sell 3 (v2 2)
- Investments:
  - Tenants L13 for 500 prestige: +74/turn (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 0.0/turn (+0.0 exported); plan makes 22.6 garments a turn.
Labour: own 500, everything else 415, chain may buy 350 -> chain allowance 435, chain plan 435 (+282 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 3.47 | 6.44 |
| ret | 3 | 0.62 | 1.14 |
| spin | 4 | 1.27 | 2.36 |
| weave | 3 | 0.00 | 0.89 |
| sew | 2 | 0.00 | 0.55 |

Buffers: flax fibres 46/80, thread 275/236, cloth 19/89
- chain plan needed 557 labour, budget left 435: cut to 435 (sewing capped at 0.55)

## Self-diagnosis

- R3: weavery 1 (weavery) finished but idle 6 turns (weave cloth 2 at 0); no planned recipe for a weavery: Taylor's call
- R3: sewing shop 1 (sewing shop) finished but idle 6 turns (sew garments 2 at 0); no planned recipe for a sewing shop: Taylor's call
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
- R7 stale ask: garments ask 20 over the market for 6 turns: the town trades ~64 a turn at 19.8, we sold 0 with 86 over what we keep; floor 20 (config sell_floor / unit cost) is at or over the market: Taylor's call
