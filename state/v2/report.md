# v2 shadow report

Turn 13497, 2026-10-23 18:41. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 1,500, prestige 3,596 (476 free, -1.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 83 | 0 | 4 | 0 | 0 | min_holding 60, sell 119, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 22 | 6 | 9 | 0 | 0 | stop 40, buy 19, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 121 | 0 | 2 | 0 | 0 | min_holding 30, sell 24, sell @ 20 |
| grain | 82 | 27 | 46 | 0 | 0 | stop 234, buy 64, buy @ 3.7 |
| labour | 205 | 88 | 588 | 114 | 0 | buy 202, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 34 |
| porterage | 5 | 5 | 5 | 1 | 0 | buy 12, buy @ 1.1 |

**1 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **porterage**: flax farm 1 ran short of porterage (buy is live (12 @ 1.1), 5 bought last turn); knock-on: retting pit 1 (no flax plants); labour need rises ~93/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it

## Tuning

- **limestone**: we make 1/turn more than we use but there is no sell order -> v2: sell 1

## Notes

- labour: projection runs 100 over real use lately; planning 702, not 768

## Prestige spending, cheapest coin per prestige first

904 turns left: prestige gained now converts 98.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 43.2 | 43.2 | running |
| hold banquet 3 (pies) | mansion | 8 | 47.5 | 47.5 | thin at home: hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 47.5 | 47.5 | thin at home: hop beer, wine |
| hold banquet 2 (pies) | mansion | 7 | 50.0 | 50.0 | thin at home: wine, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 50.4 | 50.4 | thin at home: hop beer |
| hold banquet 4 | mansion | 17.5 | 50.6 | 50.6 | thin at home: wine, hop beer, ham |
| jousting 3 | arena | 230 | 51.4 | 51.5 | needs a arena (build cost 23,441); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 52.0 | 52.0 | thin at home: wine |
| hold prayer 2 | chapel | 13 | 49.6 | 52.3 | needs a chapel (build cost 29,563); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 49.9 | 52.4 | needs a church (build cost 63,738); thin at home: candles, furniture |
| hold banquet 3 (meat) | mansion | 7.6 | 52.7 | 52.7 | thin at home: hop beer |
| hold banquet 1 (fish) | mansion | 4.2 | 53.3 | 53.3 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 134102075 | 0.144 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0.128 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 9 @ 12.7; crew 0.1; est +114 a turn; stock: furniture 9 @ 12.7 (keep 145)
- **linen snake** on Grandgues: furniture buy 8 @ 13.7; crew 0.1; est +93 a turn; stock: furniture 8 @ 13.7 (keep 145)
- best towns now: Bedenis +142, Heidlowe +139, Hofkirchen +138, Toqueque +136, Bordees +131
- Bedenis would trade: furniture buy 10 @ 11.3; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~90 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.28 | 0.70 (63/turn) | beer 97 (3.16->5.42), thread 6 (3.36->4.2), flax fibres 3 (5.2->6.17), wine 5 (6.14->6.55) | salt 4 (4.09->5.56), harnesses 1 (51.45->55.57), candles 1 (67.2->70), pasties 2 (13.02->14) | +181 |
| Briclives | 1041 | 0.31 | 0.80 (72/turn) | beer 97 (3.16->5.03), tackles 1 (159.6->177.65), flour 2 (19.53->23.18), thread 2 (3.36->4.1) | flax plants 1 (1.25->1.89), tools 1 (4.28->4.7) | +138 |
| Fontaux | 411 | 0.10 | 0.30 (27/turn) | thread 59 (3.36->4.58), charcoal 13 (1.65->3.82), coats 2 (76.65->83.6), firewood 1 (1.54->6.32) | salt 4 (4.54->5.56), candles 1 (67.73->70) | +105 |
| Vauxvais | 204 | 0.05 | 0.10 (9/turn) | bellows 1 (312.9->370.5), thread 26 (3.36->3.93), scythes 2 (27.09->31.35), mouldboards 2 (28.98->30.97) | salt 4 (4.64->5.56), thread 28 (4.39->4.56), candles 1 (68.25->70), pasties 2 (13.02->14) | +91 |
| Hanstein | 380 | 0.09 | 0.30 (27/turn) | thread 72 (3.36->4.35), charcoal 13 (1.65->2.74), lead ore 3 (10.71->12.25), timber 2 (6.1->8.46) | salt 4 (4.41->5.56), cheese 11 (5.25->5.61), pasties 2 (12.71->14), beer 4 (3.07->3.5) | +89 |

**Best:** Hofkirchen at about +181 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 119 @ min 3.38 |  |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 19 @ 2.4, stop 40 |  | uses 10.0/turn (brewery 1, household upkeep), makes 0.0, holds 22 = 2.2 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| garments |  | 24 @ min 20.0 | makes 4.4, uses 2.1, holds 121 (keeps 30): sells the surplus + 22/turn of the excess |
| grain | 117 @ 3.7, stop 234 |  | uses 58.5/turn (brewery 1), makes 0.0, holds 82 = 1.4 turns |
| labour | 202 @ 2.2, stop - |  | uses 701.9/turn (brewery 1, household, logging camp w/ tool), makes 500.0, holds 205 = 1.0 turns |
| limestone |  | 1 @ min 17.1 |  |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 11 @ min 34.0 |  |
| pasties | 3 @ 14.5, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 13 = 4.8 turns |
| porterage | 12 @ 1.1, stop - |  | uses 11.7/turn (observed), makes 0.0, holds 5 = 0.4 turns |
| rope |  | 4 @ min 75.0 |  |
| timber |  | 10 @ min 6.5 | makes 8.4, uses 0.0, holds 376 (keeps 350): sells the surplus + 1/turn of the excess |
| tools | 2 @ 6.2, stop 14 |  | uses 1.8/turn (logging camp w/ tool), makes 0.0, holds 199 = 113.8 turns |

## Goal: business value (shadow)
- no plan: goal plan failed: KeyError: 'value'

## Chain sizing

Mode HOLD, garments sold 0.0/turn (+0.0 exported); plan makes 0.0 garments a turn.
Labour: own 500, everything else 508, chain may buy 0 -> chain allowance 0, chain plan 200 (-96 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.42 | 4.56 |
| ret | 3 | 1.12 | 0.81 |
| spin | 4 | 1.98 | 1.67 |
| weave | 3 | 0.50 | 0.00 |
| sew | 2 | 0.11 | 0.00 |

Buffers: flax fibres 48/69, thread 413/202, cloth 43/0
- chain plan needed 200 labour, budget left 0: cut to 200

## Self-diagnosis

- R7 stale ask: garments ask 20 over the market for 6 turns: the town trades ~61 a turn at 19.5, we sold 0 with 91 over what we keep; floor 20 (config sell_floor / unit cost) is at or over the market: Taylor's call
- R7 stale ask: timber ask 6.5 over the market for 5 turns: the town trades ~82 a turn at 6.15, we sold 0 with 26 over what we keep; floor 6.5 (config sell_floor / unit cost) is at or over the market: Taylor's call
