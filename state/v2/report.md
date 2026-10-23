# v2 shadow report

Turn 13490, 2026-10-23 11:58. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 2,028, prestige 3,605 (485 free, -1.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 99 | 0 | 4 | 0 | 0 | min_holding 60, sell 53, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 122 | 0 | 2 | 0 | 0 | min_holding 30, sell 14, sell @ 20 |
| grain | 104 | 26 | 26 | 0 | 0 | stop 104, buy 27, buy @ 3.7 |
| labour | 0 | 0 | 473 | 0 | 27 | buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 34.6 |
| porterage | 10 | 10 | 8 | 0 | 2 | buy 10, buy @ 1.1 |

**0 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **linen snake**: linen snake cost 9 coin last turn (crew 0.10) and its route traded nothing (route limited by rope) -> v2: pause it (crew 0) until a route is proven to sell

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax plants**: flax plants buffer thin: 1.6 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 111

## Notes

- labour: projection runs 100 over real use lately; planning 473, not 573

## Prestige spending, cheapest coin per prestige first

911 turns left: prestige gained now converts 99.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 44.7 | 44.7 | running |
| hold banquet 4 (pies) | mansion | 18 | 47.4 | 47.4 | thin at home: hop beer, wine |
| hold banquet 3 (pies) | mansion | 8 | 47.5 | 47.5 | thin at home: hop beer, pies |
| hold banquet 2 (pies) | mansion | 7 | 49.5 | 49.5 | thin at home: wine, pies |
| hold banquet 4 | mansion | 17.5 | 50.6 | 50.6 | thin at home: wine, hop beer, ham |
| hold banquet 3 (fish) | mansion | 7.6 | 51.1 | 51.1 | thin at home: hop beer |
| hold prayer 2 | chapel | 13 | 48.5 | 51.4 | needs a chapel (build cost 31,510); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 49.0 | 51.6 | needs a church (build cost 65,960); thin at home: candles, furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 52.4 | 52.4 | thin at home: wine |
| jousting 3 | arena | 230 | 52.3 | 52.4 | needs a arena (build cost 24,808); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold feast 2 | townhouse | 2.6 | 50.7 | 53.5 | needs a townhouse (build cost 6,478); thin at home: wine |
| hold sermon 2 | church | 24 | 50.1 | 53.5 | needs a church (build cost 65,960); thin at home: furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 9 | 151802239 | 0.04 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -1 a turn after crew: ship stays at 0
- best towns now: Hofkirchen +38
- Hofkirchen would trade: beer sell 38 @ 5.3, candles buy 1 @ 65.0, garments buy 2 @ 18.4; crew 0.3

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~93 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.29 | 0.50 (47/turn) | beer 55 (3.16->6.41), hop beer 3 (8.24->12.44), wine 5 (5.35->7.55), axes 2 (18.9->20.52) | bellows 1 (224.7->264.1), acid 1 (140.7->144.4), candles 1 (67.2->70.5), gears 2 (60.38->61.27) | +221 |
| Birkeningen | 1006 | 0.30 | 0.40 (37/turn) | charcoal 13 (1.97->5.84), malt 1 (4.01->6.32), tools 10 (4.5->5.03), wine 2 (5.35->6.79) | windows 2 (470.4->517.75), lathes 1 (237.3->243.2) | +121 |
| Briclives | 1041 | 0.32 | 0.60 (56/turn) | malt 9 (4.01->11.97), beer 55 (3.16->4.16), casks 4 (5.19->8.69), rope 1 (74.5->81.22) | lathes 1 (235.2->243.2), acid 1 (139.65->144.4), glass ingots 1 (49.98->52.72), fleece 1 (6.35->6.98) | +113 |
| Fontaux | 411 | 0.10 | 0.40 (37/turn) | cheese 14 (6.25->9.79), thread 24 (4.66->5.65), charcoal 13 (1.97->3.48), flax fibres 3 (4.76->8.03) | tin ingots 1 (33.18->38.95), lathes 1 (239.4->243.2), fleece 1 (6.35->6.98), wool 1 (7.67->7.84) | +108 |
| Cobholme | 1564 | 0.58 | 0.30 (28/turn) | sails 1 (609->674.5), cured fish 3 (25.41->30.21), cheese 5 (6.25->8.93), wine 5 (5.35->7.12) | - | +86 |

**Best:** Hofkirchen at about +221 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 52 @ min 3.38 |  |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 12 = 7.7 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | uses 7.0/turn (household upkeep), makes 0.0, holds 7 = 1.0 turns |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 0 @ 2.2, stop - |  | uses 472.6/turn (brewery 1, flax farm 1, household), makes 500.0, holds 0 |
| meat | 6 @ 3.02, stop - |  | uses 6.0/turn (household upkeep), makes 0.0, holds 6 = 1.0 turns |
| nets |  | 11 @ min 34.0 |  |
| pasties | 3 @ 14.0, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 5.0 turns |
| porterage | 8 @ 1.1, stop - |  | uses 8.1/turn (observed), makes 0.0, holds 10 = 1.2 turns |
| rope |  | 2 @ min 72.5 |  |
| timber |  | 8 @ min 6.5 |  |
| tools | 3 @ 6.2, stop 24 |  | uses 3.0/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 66.6 turns |

## Goal: business value (shadow)
- Value now 16.2k (cash + stock at home prices); +99/turn over 6 turns, -92/turn over 24 turns.
- Limits: cash flow >= +82/turn, prestige >= -0.77/turn (after 235 tax and crew).
- Today's settings: value +121/turn, cash +314/turn, prestige -1.43/turn - breaks the prestige floor.
- Plan: value +156/turn, cash +356/turn, prestige -0.77/turn, inside both limits.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ropewalk 1 0.50 -> 1.00: +22/turn
  - quarry 1 0.00 -> 0.08: +6/turn
  - logging camp w/ tool 7.00 -> 4.58: +5/turn
  - net maker 0.50 -> 0.97: +4/turn
  - flax farm 1 3.47 -> 5.38: -14/turn
  - retting pit 1 0.62 -> 0.96: -5/turn
  - spinnery 1 1.27 -> 1.97: +54/turn
  - mansion 1 0.00 -> 0.16: -38/turn
- Model check over the last 10 turns: predicted +84/turn for the settings we ran, real +46/turn.
- Worth of one more unit per turn: labour 1.49, thread 3.68, cloth 5.92, flax fibres 4.25, garments 16.74, nets 27.72, beer 2.65, timber 4.96, prestige 55.61, cash 0.00
- Orders it would set (dry run): beer sell 53 (v2 52); porterage buy 9 (v2 8); rope sell 3 (v2 2)
- Investments:
  - Tenants L13 for 500 prestige: +75/turn (waits until 800 free (keeps 300 after))
  - +1 plot ropewalk 1 for ~2768 coin: +39/turn, payback 71 turns

## Chain sizing

Mode HOLD, garments sold 0.8/turn (+0.0 exported); plan makes 0.8 garments a turn.
Labour: own 500, everything else 415, chain may buy 350 -> chain allowance 435, chain plan 156 (+3 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 3.47 | 3.49 |
| ret | 3 | 0.62 | 0.62 |
| spin | 4 | 1.27 | 1.28 |
| weave | 3 | 0.00 | 0.00 |
| sew | 2 | 0.00 | 0.02 |

Buffers: flax fibres 46/51, thread 269/150, cloth 20/3

## Self-diagnosis

- R3: weavery 1 (weavery) finished but idle 6 turns (weave cloth 2 at 0); no planned recipe for a weavery: Taylor's call
- R3: sewing shop 1 (sewing shop) finished but idle 6 turns (sew garments 2 at 0); no planned recipe for a sewing shop: Taylor's call
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
- R7 stale ask: garments ask 20 over the market for 6 turns: the town trades ~65 a turn at 18.6, we sold 0 with 92 over what we keep; floor 20 (config sell_floor / unit cost) is at or over the market: Taylor's call
