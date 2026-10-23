# v2 shadow report

Turn 13488, 2026-10-23 09:59. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 1,903, prestige 3,608 (488 free, -1.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 101 | 0 | 4 | 0 | 0 | min_holding 60, sell 53, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 126 | 0 | 2 | 0 | 0 | min_holding 30, sell 14, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 0 | 0 | 478 | 0 | 22 | buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 34.6 |
| porterage | 10 | 10 | 8 | 0 | 2 | buy 10, buy @ 1.1 |

**0 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **linen snake**: linen snake cost 9 coin last turn (crew 0.10) and its route traded nothing (route limited by rope) -> v2: pause it (crew 0) until a route is proven to sell

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax plants**: flax plants buffer thin: 1.6 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 115

## Notes

- labour: projection runs 100 over real use lately; planning 478, not 578

## Prestige spending, cheapest coin per prestige first

913 turns left: prestige gained now converts 99.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 45.3 | 45.3 | running |
| hold banquet 3 (pies) | mansion | 8 | 48.3 | 48.3 | thin at home: hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 48.5 | 48.5 | thin at home: hop beer, wine |
| hold banquet 3 (fish) | mansion | 7.6 | 51.4 | 51.4 | thin at home: hop beer |
| hold banquet 4 | mansion | 17.5 | 51.6 | 51.6 | thin at home: wine, hop beer, ham |
| jousting 3 | arena | 230 | 52.2 | 52.3 | needs a arena (build cost 25,289); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold sermon 2 (candles) | church | 31 | 50.1 | 52.7 | needs a church (build cost 66,700); thin at home: candles, furniture |
| hold banquet 2 (pies) | mansion | 7 | 52.9 | 52.9 | thin at home: wine, pies |
| hold prayer 2 | chapel | 13 | 50.6 | 53.5 | needs a chapel (build cost 32,607); thin at home: furniture |
| hold banquet 1 (fish) | mansion | 4.2 | 54.4 | 54.4 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 55.1 | 55.1 | thin at home: wine |
| hold sermon 2 | church | 24 | 51.7 | 55.1 | needs a church (build cost 66,700); thin at home: furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 9 | 151802239 | 0.04 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only -2 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -1 a turn after crew: ship stays at 0
- best towns now: Hofkirchen +21
- Hofkirchen would trade: beer sell 41 @ 4.84, candles buy 1 @ 65.0; crew 0.3

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~96 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.30 | 0.50 (48/turn) | beer 55 (3.16->5.89), glass ingots 1 (54.6->68.4), lathes 1 (190.05->201.4), lead ore 2 (8.87->12.92) | bellows 1 (228.9->260.3), cured meat 1 (21.42->25.65), candles 1 (67.2->71) | +188 |
| Fontaux | 411 | 0.10 | 0.30 (29/turn) | thread 26 (3.57->5.65), lathes 1 (190.05->220.4), charcoal 13 (1.97->4.58), casks 11 (5.78->6.37) | cured meat 1 (23.31->25.65), salt 4 (4.47->4.64) | +110 |
| Magdeach | 667 | 0.17 | 0.10 (10/turn) | grindstones 1 (275.1->357.2), dye 1 (53.55->64.12), nets 2 (35->37.81), lead ore 2 (8.87->11.59) | cured meat 1 (23.1->25.65), salt 4 (4.09->4.64) | +101 |
| Clairas | 374 | 0.10 | 0.10 (10/turn) | sails 2 (640.5->660.25), lathes 1 (190.05->222.3), thread 22 (3.57->4.37), acid 1 (123.9->130.15) | salt 4 (4.03->4.64), cured meat 1 (24.15->25.65), pies 1 (13.44->15.11) | +98 |
| Rouhomme | 368 | 0.09 | 0.90 (86/turn) | bread 142 (2.18->2.62), charcoal 13 (1.97->3.76), acid 1 (123.9->133.95), harnesses 1 (70.88->76) | candles 1 (50.4->71), lead bars 7 (12.08->12.63), canvas 1 (30.87->32.68), fleece 2 (6.35->6.6) | +87 |

**Best:** Hofkirchen at about +188 coin a turn.

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
| pasties | 3 @ 13.7, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 4.9 turns |
| porterage | 8 @ 1.1, stop - |  | uses 8.2/turn (observed), makes 0.0, holds 10 = 1.2 turns |
| rope |  | 2 @ min 72.0 |  |
| timber |  | 8 @ min 6.5 |  |
| tools | 4 @ 6.2, stop 25 |  | uses 3.0/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 65.7 turns |

## Goal: business value (shadow)
- Value now 16.0k (cash + stock at home prices); +46/turn over 6 turns, -93/turn over 24 turns.
- Limits: cash flow >= +87/turn, prestige >= -0.78/turn (after 235 tax and crew).
- Today's settings: value +128/turn, cash +340/turn, prestige -1.45/turn - breaks the prestige floor.
- Plan: value +185/turn, cash +260/turn, prestige -0.78/turn, inside both limits.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - logging camp w/ tool 7.00 -> 20.00: +31/turn
  - ropewalk 1 0.50 -> 1.00: +21/turn
  - quarry 1 0.00 -> 0.08: +5/turn
  - net maker 0.50 -> 1.00: +0/turn
  - flax farm 1 3.59 -> 6.50: -22/turn
  - retting pit 1 0.64 -> 1.13: -12/turn
  - spinnery 1 1.32 -> 2.33: +43/turn
  - weavery 1 0.00 -> 0.35: -16/turn
  - sewing shop 1 0.00 -> 0.22: +49/turn
  - mansion 1 0.00 -> 0.16: -43/turn
- Model check over the last 8 turns: predicted +74/turn for the settings we ran, real +33/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.51, thread 3.73, cloth 6.00, flax fibres 4.31, garments 17.41, nets 31.50, beer 2.69, timber 6.50, prestige 63.06, cash 0.00
- Orders it would set (dry run): beer sell 54 (v2 52); porterage buy 9 (v2 8); rope sell 3 (v2 2); timber sell 9 (v2 8)
- Investments:
  - Tenants L13 for 500 prestige: +76/turn (waits until 800 free (keeps 300 after))
  - +1 plot ropewalk 1 for ~2939 coin: +10/turn, payback 306 turns
  - +1 plot park 1 for ~1903 coin: +3/turn, payback 661 turns

## Chain sizing

Mode HOLD, garments sold 2.2/turn (+0.0 exported); plan makes 0.0 garments a turn.
Labour: own 500, everything else 415, chain may buy 0 -> chain allowance 85, chain plan 153 (-5 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 3.59 | 3.49 |
| ret | 3 | 0.64 | 0.62 |
| spin | 4 | 1.32 | 1.28 |
| weave | 3 | 0.00 | 0.00 |
| sew | 2 | 0.00 | 0.00 |

Buffers: flax fibres 46/50, thread 262/147, cloth 20/0
- chain plan needed 153 labour, budget left 85: cut to 153

## Self-diagnosis

- R3: weavery 1 (weavery) finished but idle 4 turns (weave cloth 2 at 0); no planned recipe for a weavery: Taylor's call
- R3: sewing shop 1 (sewing shop) finished but idle 4 turns (sew garments 2 at 0); no planned recipe for a sewing shop: Taylor's call
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
- R7 stale ask: garments ask 20 over the market for 6 turns: the town trades ~65 a turn at 19.6, we sold 0 with 96 over what we keep; floor 20 (config sell_floor / unit cost) is at or over the market: Taylor's call
