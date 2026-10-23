# v2 shadow report

Turn 13489, 2026-10-23 10:57. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 1,854, prestige 3,607 (487 free, -1.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 100 | 0 | 4 | 0 | 0 | min_holding 60, sell 53, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 124 | 0 | 2 | 0 | 0 | min_holding 30, sell 14, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 0 | 0 | 478 | 0 | 22 | buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 34.6 |
| porterage | 10 | 10 | 8 | 0 | 2 | buy 10, buy @ 1.1 |

**0 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **linen snake**: linen snake cost 9 coin last turn (crew 0.10) and its route traded nothing (route limited by rope) -> v2: pause it (crew 0) until a route is proven to sell

## Tuning

- **flax plants**: flax plants buffer thin: 1.6 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 115

## Notes

- labour: projection runs 100 over real use lately; planning 478, not 578

## Prestige spending, cheapest coin per prestige first

912 turns left: prestige gained now converts 99.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 44.7 | 44.7 | running |
| hold banquet 4 (pies) | mansion | 18 | 47.5 | 47.5 | thin at home: hop beer, wine |
| hold banquet 3 (pies) | mansion | 8 | 48.0 | 48.0 | thin at home: hop beer, pies |
| hold banquet 2 (pies) | mansion | 7 | 50.2 | 50.2 | thin at home: wine, pies |
| hold banquet 4 | mansion | 17.5 | 50.6 | 50.6 | thin at home: wine, hop beer, ham |
| hold banquet 3 (fish) | mansion | 7.6 | 51.2 | 51.2 | thin at home: hop beer |
| jousting 3 | arena | 230 | 52.3 | 52.4 | needs a arena (build cost 24,708); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 52.5 | 52.5 | thin at home: wine |
| hold sermon 2 (candles) | church | 31 | 50.0 | 52.5 | needs a church (build cost 65,716); thin at home: candles, furniture |
| hold prayer 2 | chapel | 13 | 50.4 | 53.2 | needs a chapel (build cost 31,306); thin at home: furniture |
| hold feast 2 | townhouse | 2.6 | 51.1 | 53.9 | needs a townhouse (build cost 6,494); thin at home: wine |
| hold banquet 1 (fish) | mansion | 4.2 | 54.2 | 54.2 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 9 | 151802239 | 0.04 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only -2 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -1 a turn after crew: ship stays at 0
- best towns now: Hofkirchen +28
- Hofkirchen would trade: beer sell 40 @ 5.05, candles buy 1 @ 65.0; crew 0.3

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~95 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.30 | 0.50 (47/turn) | beer 55 (3.16->6.13), hop beer 3 (8.29->12.44), glass ingots 1 (58.8->68.4), wine 5 (5.41->7.31) | bellows 1 (214.2->260.3), candles 1 (67.2->71), acid 1 (140.7->143.45), raw cloth 1 (5.99->6.41) | +211 |
| Briclives | 1041 | 0.32 | 0.70 (66/turn) | malt 23 (4.7->8.88), jewellery 2 (96.08->110.2), casks 6 (5.62->9.97), beer 55 (3.16->3.99) | glass ingots 1 (44.1->49.4), acid 1 (140.7->143.45), canvas 1 (31.08->32.68), tools 3 (4.28->4.7) | +163 |
| Fontaux | 411 | 0.10 | 0.40 (38/turn) | thread 26 (3.53->5.65), cheese 12 (6.25->9.79), charcoal 13 (2.01->4.43), flax fibres 3 (4.55->7.79) | candles 1 (69.83->71), salt 4 (4.47->4.71) | +138 |
| Heilegg | 826 | 0.21 | 0.50 (47/turn) | wrought iron 12 (12.92->16.25), grindstones 1 (273->296.4), beer 55 (3.16->3.78), thread 12 (3.53->4.37) | canvas 7 (31.71->32.68), raw cloth 1 (5.99->6.41) | +93 |
| Magdeach | 667 | 0.17 | 0.10 (9/turn) | dye 1 (53.03->96.9), thread 6 (3.53->4.37), dyed yarn 1 (7.19->7.89), flax fibres 1 (4.55->5.03) | cured fish 11 (19.74->21.28), pies 2 (13.23->15.2), salt 4 (4.09->4.71) | +67 |

**Best:** Hofkirchen at about +211 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 26.0, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 52 @ min 3.38 |  |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 0 @ 2.2, stop - |  | uses 478.3/turn (brewery 1, flax farm 1, household), makes 500.0, holds 0 |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 11 @ min 34.0 |  |
| pasties | 3 @ 13.4, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 4.9 turns |
| porterage | 8 @ 1.1, stop - |  | uses 8.2/turn (observed), makes 0.0, holds 10 = 1.2 turns |
| rope |  | 2 @ min 72.0 |  |
| timber |  | 8 @ min 6.5 |  |
| tools | 4 @ 6.2, stop 25 |  | uses 3.0/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 65.7 turns |

## Goal: business value (shadow)
- Value now 16.1k (cash + stock at home prices); +37/turn over 6 turns, -85/turn over 24 turns.
- Limits: cash flow >= +89/turn, prestige >= -0.78/turn (after 235 tax and crew).
- Today's settings: value +114/turn, cash +320/turn, prestige -1.44/turn - breaks the prestige floor.
- Plan: value +152/turn, cash +232/turn, prestige -0.78/turn, inside both limits.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ropewalk 1 0.50 -> 1.00: +32/turn
  - net maker 0.50 -> 0.99: +6/turn
  - quarry 1 0.00 -> 0.08: +5/turn
  - logging camp w/ tool 7.00 -> 4.58: +6/turn
  - flax farm 1 3.59 -> 6.25: -21/turn
  - retting pit 1 0.64 -> 1.11: -12/turn
  - spinnery 1 1.32 -> 2.29: +32/turn
  - weavery 1 0.00 -> 0.31: -13/turn
  - sewing shop 1 0.00 -> 0.20: +42/turn
  - mansion 1 0.00 -> 0.16: -41/turn
- Model check over the last 9 turns: predicted +80/turn for the settings we ran, real +40/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.49, thread 3.68, cloth 5.92, flax fibres 4.25, garments 17.18, nets 27.72, beer 2.65, timber 4.96, prestige 59.87, cash 0.00
- Orders it would set (dry run): beer sell 53 (v2 52); porterage buy 9 (v2 8); rope sell 3 (v2 2)
- Investments:
  - Tenants L13 for 500 prestige: +75/turn (waits until 800 free (keeps 300 after))
  - +1 plot ropewalk 1 for ~2684 coin: +7/turn, payback 403 turns
  - +1 plot park 1 for ~1871 coin: +2/turn, payback 1182 turns

## Chain sizing

Mode HOLD, garments sold 1.5/turn (+0.0 exported); plan makes 0.0 garments a turn.
Labour: own 500, everything else 415, chain may buy 0 -> chain allowance 85, chain plan 152 (-6 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 3.59 | 3.47 |
| ret | 3 | 0.64 | 0.62 |
| spin | 4 | 1.32 | 1.27 |
| weave | 3 | 0.00 | 0.00 |
| sew | 2 | 0.00 | 0.00 |

Buffers: flax fibres 46/50, thread 267/147, cloth 20/0
- chain plan needed 152 labour, budget left 85: cut to 152

## Self-diagnosis

- R3: weavery 1 (weavery) finished but idle 5 turns (weave cloth 2 at 0); no planned recipe for a weavery: Taylor's call
- R3: sewing shop 1 (sewing shop) finished but idle 5 turns (sew garments 2 at 0); no planned recipe for a sewing shop: Taylor's call
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
- R7 stale ask: garments ask 20 over the market for 6 turns: the town trades ~65 a turn at 19.6, we sold 0 with 94 over what we keep; floor 20 (config sell_floor / unit cost) is at or over the market: Taylor's call
