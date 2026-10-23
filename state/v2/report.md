# v2 shadow report

Turn 13484, 2026-10-23 05:57. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 1,617, prestige 3,614 (494 free, -1.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 106 | 0 | 4 | 0 | 0 | min_holding 60, sell 53, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 135 | 0 | 2 | 0 | 0 | min_holding 30, sell 14, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 187 | 187 | 478 | 0 | 209 | buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 34.6 |
| porterage | 10 | 10 | 8 | 0 | 2 | buy 10, buy @ 1.1 |

**0 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **linen snake**: linen snake cost 10 coin last turn (crew 0.10) and its route traded nothing (route limited by rope) -> v2: pause it (crew 0) until a route is proven to sell

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax plants**: flax plants buffer thin: 1.6 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 115

## Notes

- labour: projection runs 75 over real use lately; planning 503, not 578
- labour expiry guard: 209 bought labour expired last turn, buy 0 (not 3) this turn

## Prestige spending, cheapest coin per prestige first

917 turns left: prestige gained now converts 99.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.3 | 48.3 | running |
| hold banquet 3 (pies) | mansion | 8 | 49.7 | 49.7 | thin at home: pasties, hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 49.7 | 49.7 | thin at home: pasties, hop beer, wine |
| hold banquet 3 (fish) | mansion | 7.6 | 52.5 | 52.5 | thin at home: hop beer |
| hold banquet 4 | mansion | 17.5 | 52.8 | 52.8 | thin at home: wine, hop beer, ham |
| hold sermon 2 (candles) | church | 31 | 50.6 | 53.2 | needs a church (build cost 64,835); thin at home: candles, furniture |
| jousting 3 | arena | 230 | 53.1 | 53.3 | needs a arena (build cost 24,803); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold prayer 2 | chapel | 13 | 51.1 | 53.9 | needs a chapel (build cost 31,182); thin at home: furniture |
| hold banquet 1 (fish) | mansion | 4.2 | 54.5 | 54.5 |  |
| hold banquet 2 (pies) | mansion | 7 | 54.6 | 54.6 | thin at home: pasties, wine, pies |
| hold sermon 2 | church | 24 | 52.2 | 55.4 | needs a church (build cost 64,835); thin at home: furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 56.6 | 56.6 | thin at home: wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 10 | 151802239 | 0.04 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only -6 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -2 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~100 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.32 | 0.50 (50/turn) | beer 55 (3.16->5.08), glass ingots 2 (55.12->68.4), thread 6 (3.77->4.56), flax fibres 3 (4.68->5.79) | blades 2 (11.97->12.73), candles 1 (71.4->72.5), cheese 10 (5.35->5.75), garments 2 (19.32->19.8) | +104 |
| Heilegg | 826 | 0.23 | 0.40 (40/turn) | beer 55 (3.16->4.16), grindstones 1 (281.4->296.4), thread 11 (3.77->4.54), ham 1 (60.38->62.7) | premium ham 1 (279.3->307.8), cheese 10 (5.41->5.75), canvas 7 (31.08->31.54) | +75 |
| Gotthafen | 964 | 0.30 | 0.20 (20/turn) | medicine 1 (140.7->187.15), grindstones 1 (281.4->298.3), lead ore 2 (8.72->13.01), tools 16 (4.54->4.94) | wine 6 (5.83->6.55), candles 1 (70.35->72.5) | +69 |
| Amsdermund | 1111 | 0.38 | 0.90 (90/turn) | limestone 1 (21->52.25), acid 1 (151.2->166.25), beer 55 (3.16->4.07), herbs 2 (37.8->41.8) | chisels 2 (13.12->13.77) | +66 |
| Clairas | 374 | 0.10 | 0.10 (10/turn) | sails 1 (609->660.25), thread 16 (3.77->4.29), acid 1 (151.2->154.85), mouldboards 1 (31.08->31.73) | candles 1 (67.73->72.5), wine 4 (6.41->6.55) | +62 |

**Best:** Hofkirchen at about +104 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 52 @ min 3.38 |  |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 12 = 7.7 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 0 @ 2.2, stop - |  | uses 503.3/turn (brewery 1, flax farm 1, household), makes 500.0, holds 187 = 57.0 turns |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 11 @ min 34.0 |  |
| pasties | 3 @ 13.3, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 4.9 turns |
| porterage | 8 @ 1.1, stop - |  | uses 8.2/turn (observed), makes 0.0, holds 10 = 1.2 turns |
| rope |  | 2 @ min 76.5 |  |
| timber |  | 8 @ min 6.5 |  |
| tools | 4 @ 6.2, stop 25 |  | uses 3.0/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 65.8 turns |

## Goal: business value (shadow)
- Value now 15.6k (cash + stock at home prices); +35/turn over 6 turns, -116/turn over 24 turns.
- Limits: cash flow >= +99/turn, prestige >= -0.81/turn (after 236 tax and crew).
- Today's settings: value +97/turn, cash +303/turn, prestige -1.48/turn - breaks the prestige floor.
- Plan: value +99/turn, cash +324/turn, prestige -0.81/turn, inside both limits.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - net maker 0.50 -> 1.00: +19/turn
  - logging camp w/ tool 7.00 -> 2.88: +10/turn
  - quarry 1 0.00 -> 0.08: +5/turn
  - flax farm 1 3.59 -> 3.93: -3/turn
  - retting pit 1 0.64 -> 0.74: -3/turn
  - spinnery 1 1.32 -> 1.53: -0/turn
  - weavery 1 0.00 -> 0.08: -4/turn
  - mansion 1 0.00 -> 0.16: -40/turn
- Model check: not enough runs yet (needs 6 turns of goal history).
- Worth of one more unit per turn: labour 1.61, thread 3.97, cloth 6.39, flax fibres 4.58, garments 18.55, nets 34.60, beer 2.81, timber 5.29, prestige 58.32, cash 0.00
- Orders it would set (dry run): beer sell 54 (v2 52); porterage buy 9 (v2 8); rope sell 3 (v2 2)
- Investments:
  - Tenants L13 for 500 prestige: +79/turn (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 4.2/turn (+0.0 exported); plan makes 0.0 garments a turn.
Labour: own 500, everything else 415, chain may buy 0 -> chain allowance 85, chain plan 157 (+0 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 3.59 | 3.57 |
| ret | 3 | 0.64 | 0.64 |
| spin | 4 | 1.32 | 1.31 |
| weave | 3 | 0.00 | 0.00 |
| sew | 2 | 0.00 | 0.00 |

Buffers: flax fibres 46/50, thread 244/147, cloth 21/0
- chain plan needed 157 labour, budget left 85: cut to 157

## Self-diagnosis

- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
- R7 stale ask: garments ask 20 over the market for 4 turns: the town trades ~64 a turn at 19.8, we sold 0 with 105 over what we keep; floor 20 (config sell_floor / unit cost) is at or over the market: Taylor's call
