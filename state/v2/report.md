# v2 shadow report

Turn 13498, 2026-10-23 19:03. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 1,283, prestige 3,595 (475 free, -0.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 84 | 0 | 7 | 0 | 0 | min_holding 60, sell 119, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 31 | 7 | 10 | 0 | 0 | stop 40, buy 19, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 123 | 0 | 2 | 0 | 0 | min_holding 30, sell 24, sell @ 20 |
| grain | 140 | 27 | 58 | 0 | 0 | stop 234, buy 117, buy @ 3.7 |
| labour | 269 | 205 | 659 | 0 | 46 | buy 269, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 34 |
| porterage | 12 | 5 | 5 | 7 | 0 | buy 12, buy @ 1.1 |

**1 risks, 2 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **porterage**: logging camp w/ tool, flax farm 1, quarry 1 ran short of porterage (buy is live (12 @ 1.1), 5 bought last turn); knock-on: retting pit 1 (no flax plants); labour need rises ~123/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it

## Waste (money lost now)

- **labour**: 46 labour expired last turn (~67 coin): holding 269 against a ~0 buffer target -> v2: trim the buy until the stock is near 0
- **linen snake**: linen snake cost 9 coin last turn (crew 0.10) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell

## Notes

- labour: projection runs 100 over real use lately; planning 693, not 793
- labour expiry guard: 46 bought labour expired last turn, buy 159 (not 193) this turn

## Prestige spending, cheapest coin per prestige first

903 turns left: prestige gained now converts 98.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 43.5 | 43.5 | running |
| hold banquet 3 (pies) | mansion | 8 | 47.2 | 47.2 | thin at home: hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 48.0 | 48.0 | thin at home: hop beer, wine |
| hold banquet 3 (fish) | mansion | 7.6 | 50.0 | 50.0 | thin at home: hop beer |
| hold banquet 2 (pies) | mansion | 7 | 50.4 | 50.4 | thin at home: wine, pies |
| hold banquet 4 | mansion | 17.5 | 51.2 | 51.2 | thin at home: wine, hop beer, ham |
| jousting 3 | arena | 230 | 51.4 | 51.5 | needs a arena (build cost 23,659); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (meat) | mansion | 7.6 | 52.0 | 52.0 | thin at home: hop beer |
| hold banquet 2 (fish) | mansion | 6.8 | 52.3 | 52.3 | thin at home: wine |
| hold prayer 2 | chapel | 13 | 49.8 | 52.5 | needs a chapel (build cost 29,643); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 50.0 | 52.6 | needs a church (build cost 63,844); thin at home: candles, furniture |
| hold banquet 1 (fish) | mansion | 4.2 | 52.9 | 52.9 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 9 | 134102075 | 0.144 | - | furniture 9 | -112 |
| linen snake | 0.1 / 0.10 | 9 | 151802239 | 0.128 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 8 @ 12.7; crew 0.1; est +100 a turn; stock: furniture 8 @ 12.7 (keep 145)
- **linen snake** on Grandgues: furniture buy 7 @ 13.7; crew 0.1; est +80 a turn; stock: furniture 7 @ 13.7 (keep 145)
- best towns now: Bedenis +127, Hofkirchen +124, Heidlowe +109, Toqueque +107, Etallaen +104
- Bedenis would trade: furniture buy 9 @ 11.3; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~91 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.29 | 0.90 (82/turn) | beer 121 (3.16->5.42), thread 6 (3.36->4.2), flax fibres 3 (5.2->6.17), wine 5 (6.14->6.55) | salt 4 (4.09->5.56), harnesses 1 (51.45->55.57), candles 1 (67.2->70), pasties 2 (13.02->14) | +218 |
| Briclives | 1041 | 0.31 | 0.80 (73/turn) | beer 103 (3.16->5.03), tackles 1 (159.6->177.65), flour 2 (19.53->23.18), thread 2 (3.36->4.1) | flax plants 1 (1.25->1.89), tools 1 (4.28->4.7) | +148 |
| Vauxvais | 204 | 0.05 | 0.10 (9/turn) | bellows 1 (312.9->370.5), thread 26 (3.36->3.93), scythes 2 (27.09->31.35), mouldboards 2 (28.98->30.97) | salt 4 (4.64->5.56), thread 28 (4.39->4.56), candles 1 (68.25->70), pasties 2 (13.02->14) | +92 |
| Rouhomme | 368 | 0.09 | 0.90 (82/turn) | bread 143 (2.06->2.6), charcoal 13 (1.65->3.27), beer 121 (3.16->3.42), iron ore 2 (4.83->8.46) | wheels 3 (17.64->19.38), flax fibres 7 (5.35->5.8), salt 2 (4.96->5.56), slaked lime 1 (6.83->7.6) | +91 |
| Fontaux | 411 | 0.10 | 0.30 (27/turn) | thread 33 (3.36->4.58), charcoal 13 (1.65->3.82), coats 2 (76.65->83.6), firewood 2 (1.54->6.32) | salt 4 (4.54->5.56), candles 1 (67.73->70) | +80 |

**Best:** Hofkirchen at about +218 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 119 @ min 3.38 |  |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 12 = 7.7 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 15 @ 2.4, stop 40 |  | uses 10.0/turn (brewery 1, household upkeep), makes 0.0, holds 31 = 3.1 turns |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 25 @ min 20.0 | makes 4.4, uses 2.1, holds 123 (keeps 30): sells the surplus + 23/turn of the excess |
| grain | 106 @ 3.7, stop 234 |  | uses 58.5/turn (brewery 1), makes 0.0, holds 140 = 2.4 turns |
| labour | 195 @ 2.2, stop - |  | goal planner: buys 195 for today's rates (v2 had 159) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 11 @ min 34.0 |  |
| pasties | 3 @ 14.5, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 4.9 turns |
| porterage | 13 @ 1.1, stop - |  | goal planner: buys 13 for today's rates (v2 had 12) |
| rope |  | 5 @ min 74.0 | goal planner: sells 5 (v2 had 4) |
| tar | 2 @ 11.0, stop 5 |  | uses 1.1/turn (ropewalk 1), makes 0.0, holds 10 = 8.7 turns |
| tools | 4 @ 6.2, stop 28 |  | uses 3.4/turn (observed), makes 0.0, holds 199 = 58.4 turns |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 16.1k (cash + stock at home prices); -19/turn over 6 turns, +43/turn over 24 turns.
- Limits: cash flow >= +113/turn, prestige >= -0.73/turn (values are after 240 tax a turn).
- Today's settings: value +184/turn, cash +326/turn, prestige -0.72/turn.
- Plan: value +349/turn, cash +517/turn, prestige -0.73/turn, inside both limits.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Fontaux: +11/turn
  - spinnery 1 1.98 -> 3.36: +18/turn
  - flax farm 1 5.42 -> 11.00: +11/turn
  - retting pit 1 1.12 -> 1.94: +65/turn
  - brewery 1 0.90 -> 1.00: +5/turn
  - net maker 0.50 -> 0.00: -12/turn
  - net maker [make nets 2] 0.00 -> 1.00: +24/turn
  - weavery 1 0.37 -> 0.00: -8/turn
  - sewing shop 1 0.11 -> 0.00: +8/turn
  - logging camp w/ tool 7.00 -> 0.00: -14/turn
- Model check: not enough runs yet (needs 6 turns of goal history).
- Worth of one more unit per turn: labour 1.45, thread 3.91, cloth 6.67, flax fibres 5.10, garments 17.64, nets 35.00, beer 3.05, timber 6.45, prestige 54.59, cash 0.00
- Orders it would set: labour buy 195 (v2 159); porterage buy 13 (v2 12); rope sell 5 (v2 4)
- Recipe: logging camp w/ tool split timber 2 -> cut firewood 1 at 20.00, worth +56/turn.
- Recipe: weavery 1 weave cloth 2 -> weave cloth 2 (yarn) at 0.04, worth +2/turn.
- Recipe: net maker make nets 1 -> make nets 2 at 1.00, worth +30/turn.
- Ship linen snake: Grandgues -> Fontaux (+57/turn over staying).
- Ship Flax Wyrm: stays on Caillechâtel (worth +50/turn).
- Management: ~13.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +73/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new chandlery (make candles 2) for ~3951 coin: +68/turn, payback 58 turns, doesn't pay yet (materials thin at home: bricks)
  - +1 plot ropewalk 1 for ~2685 coin: +25/turn, payback 108 turns
  - +1 plot net maker for ~1349 coin: +20/turn, payback 66 turns
  - +1 plot flax farm 1 for ~432 coin: +5/turn, payback 79 turns
- Trim: donate weavery 1: +16/turn (tax 18 saved).
- Trim: donate quarry 1: +15/turn (tax 20 saved).
- Trim: donate sewing shop 1: +12/turn (tax 12 saved).

## Chain sizing

Mode HOLD, garments sold 0.0/turn (+0.0 exported); plan makes 0.0 garments a turn.
Labour: own 500, everything else 508, chain may buy 0 -> chain allowance 0, chain plan 202 (-85 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 5.42 | 4.60 |
| ret | 3 | 1.12 | 0.82 |
| spin | 4 | 1.98 | 1.68 |
| weave | 3 | 0.37 | 0.00 |
| sew | 2 | 0.11 | 0.00 |

Buffers: flax fibres 44/69, thread 404/202, cloth 53/0
- chain plan needed 202 labour, budget left 0: cut to 202

## Self-diagnosis

- R7 stale ask: garments ask 20 over the market for 6 turns: the town trades ~61 a turn at 19.6, we sold 0 with 93 over what we keep; floor 20 (config sell_floor / unit cost) is at or over the market: Taylor's call
- R7 stale ask: timber ask 6.5 over the market for 6 turns: the town trades ~81 a turn at 6.15, we sold 0 with 26 over what we keep; floor 6.5 (config sell_floor / unit cost) is at or over the market: Taylor's call
