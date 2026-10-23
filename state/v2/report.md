# v2 shadow report

Turn 13486, 2026-10-23 07:15. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 1,751, prestige 3,611 (491 free, -1.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 104 | 0 | 4 | 0 | 0 | min_holding 60, sell 53, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 131 | 0 | 2 | 0 | 0 | min_holding 30, sell 14, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 0 | 0 | 478 | 0 | 22 | buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 34.6 |
| porterage | 10 | 10 | 8 | 0 | 2 | buy 10, buy @ 1.1 |

**0 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **linen snake**: linen snake cost 10 coin last turn (crew 0.10) and its route traded nothing (route limited by rope) -> v2: pause it (crew 0) until a route is proven to sell

## Tuning

- **flax plants**: flax plants buffer thin: 1.6 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 115

## Notes

- labour: projection runs 100 over real use lately; planning 478, not 578

## Prestige spending, cheapest coin per prestige first

915 turns left: prestige gained now converts 99.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 46.5 | 46.5 | running |
| hold banquet 3 (pies) | mansion | 8 | 49.9 | 49.9 | thin at home: hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 50.0 | 50.0 | thin at home: hop beer |
| jousting 3 | arena | 230 | 52.3 | 52.4 | needs a arena (build cost 24,397); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold sermon 2 (candles) | church | 31 | 50.1 | 52.6 | needs a church (build cost 64,327); thin at home: candles, furniture |
| hold banquet 3 (fish) | mansion | 7.6 | 53.2 | 53.2 | thin at home: hop beer, cured fish |
| hold banquet 4 | mansion | 17.5 | 53.3 | 53.3 | thin at home: hop beer, ham |
| hold prayer 2 | chapel | 13 | 50.7 | 53.5 | needs a chapel (build cost 30,606); thin at home: furniture |
| hold banquet 2 (pies) | mansion | 7 | 54.1 | 54.1 | thin at home: pies |
| hold banquet 1 (fish) | mansion | 4.2 | 54.7 | 54.7 |  |
| hold sermon 2 | church | 24 | 51.7 | 55.0 | needs a church (build cost 64,327); thin at home: furniture |
| jousting 1 | arena | 170 | 56.3 | 56.4 | needs a arena (build cost 24,397); thin at home: protection, light armour, arms; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 10 | 151802239 | 0.04 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only -3 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -4 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~98 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.31 | 0.50 (49/turn) | beer 55 (3.16->5.65), seeds 3 (1.78->2.66), thread 6 (3.66->4.14), yarn 6 (4.54->4.94) | cured meat 4 (22.26->25.27), candles 1 (67.2->71.5), arms 3 (23.1->24.7), casks 7 (5.72->6.55) | +124 |
| Nürnnieder | 520 | 0.14 | 0.10 (10/turn) | acid 1 (152.25->201.4), ham 1 (77.17->84.08), iron ore 2 (4.77->7.6), thread 6 (3.66->4.22) | looms 1 (561.75->570), candles 1 (66.67->71.5), casks 6 (6.09->6.55), cured meat 3 (24.78->25.27) | +79 |
| Brunnham | 1281 | 0.46 | 0.30 (29/turn) | gold ore 1 (196.35->216.6), lead ore 3 (8.72->13.77), nets 8 (35->36.48), honey 3 (8.09->9.03) | premium ham 1 (285.6->305.9), cured meat 4 (22.68->25.27), casks 7 (4.87->6.55), candles 1 (67.2->71.5) | +67 |
| Neuborn | 780 | 0.20 | 0.30 (29/turn) | beer 55 (3.16->4.24), thread 5 (3.66->6.37), flax fibres 1 (4.68->9.79), nails 1 (5.57->6.46) | cheese 11 (4.94->5.7), casks 7 (5.78->6.55), garments 2 (19.43->19.7) | +65 |
| Marmont | 638 | 0.17 | 0.10 (10/turn) | lead ore 1 (8.72->10.54) | looms 1 (508.2->570), cured meat 3 (24.36->25.27) | +57 |

**Best:** Hofkirchen at about +124 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 52 @ min 3.38 |  |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 12 = 7.7 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 0 @ 2.2, stop - |  | uses 478.3/turn (brewery 1, flax farm 1, household), makes 500.0, holds 0 |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 11 @ min 34.0 |  |
| pasties | 3 @ 13.5, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 13 = 4.7 turns |
| porterage | 8 @ 1.1, stop - |  | uses 8.2/turn (observed), makes 0.0, holds 10 = 1.2 turns |
| rope |  | 2 @ min 76.5 |  |
| timber |  | 8 @ min 6.5 |  |
| tools | 4 @ 6.2, stop 25 |  | uses 3.0/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 65.8 turns |

## Goal: business value (shadow)
- Value now 15.6k (cash + stock at home prices); -24/turn over 6 turns, -112/turn over 24 turns.
- Limits: cash flow >= +94/turn, prestige >= -0.80/turn (after 236 tax and crew).
- Today's settings: value +99/turn, cash +302/turn, prestige -1.46/turn - breaks the prestige floor.
- Plan: value +102/turn, cash +320/turn, prestige -0.80/turn, inside both limits.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - net maker 0.50 -> 1.00: +20/turn
  - logging camp w/ tool 7.00 -> 2.92: +9/turn
  - quarry 1 0.00 -> 0.08: +5/turn
  - flax farm 1 3.59 -> 4.22: -6/turn
  - retting pit 1 0.64 -> 0.75: -1/turn
  - spinnery 1 1.32 -> 1.55: +0/turn
  - weavery 1 0.00 -> 0.07: -4/turn
  - mansion 1 0.00 -> 0.16: -42/turn
- Model check: not enough runs yet (needs 6 turns of goal history).
- Worth of one more unit per turn: labour 1.55, thread 3.83, cloth 6.15, flax fibres 4.42, garments 17.86, nets 34.60, beer 2.73, timber 5.14, prestige 61.83, cash 0.00
- Orders it would set (dry run): beer sell 54 (v2 52); porterage buy 9 (v2 8); rope sell 3 (v2 2)
- Investments:
  - Tenants L13 for 500 prestige: +77/turn (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1863 coin: +2/turn, payback 1119 turns

## Chain sizing

Mode HOLD, garments sold 4.2/turn (+0.0 exported); plan makes 0.0 garments a turn.
Labour: own 500, everything else 415, chain may buy 0 -> chain allowance 85, chain plan 155 (-3 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 3.59 | 3.53 |
| ret | 3 | 0.64 | 0.63 |
| spin | 4 | 1.32 | 1.29 |
| weave | 3 | 0.00 | 0.00 |
| sew | 2 | 0.00 | 0.00 |

Buffers: flax fibres 46/50, thread 253/147, cloth 20/0
- chain plan needed 155 labour, budget left 85: cut to 155

## Self-diagnosis

- R3: weavery 1 (weavery) finished but idle 2 turns (weave cloth 2 at 0); no planned recipe for a weavery: Taylor's call
- R3: sewing shop 1 (sewing shop) finished but idle 2 turns (sew garments 2 at 0); no planned recipe for a sewing shop: Taylor's call
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
- R7 stale ask: garments ask 20 over the market for 5 turns: the town trades ~64 a turn at 19.7, we sold 0 with 101 over what we keep; floor 20 (config sell_floor / unit cost) is at or over the market: Taylor's call
