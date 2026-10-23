# v2 shadow report

Turn 13494, 2026-10-23 15:03. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 2,366, prestige 3,600 (480 free, -1.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 94 | 0 | 4 | 0 | 0 | min_holding 60, sell 53, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 23 | 6 | 6 | 0 | 0 | stop 24, buy 7, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 114 | 0 | 2 | 0 | 0 | min_holding 30, sell 14, sell @ 20 |
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

907 turns left: prestige gained now converts 98.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 43.8 | 43.8 | running |
| hold banquet 3 (pies) | mansion | 8 | 46.9 | 46.9 | thin at home: hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 47.8 | 47.8 | thin at home: hop beer |
| hold banquet 2 (pies) | mansion | 7 | 49.9 | 49.9 | thin at home: pies |
| hold banquet 3 (fish) | mansion | 7.6 | 50.7 | 50.7 | thin at home: hop beer |
| hold banquet 4 | mansion | 17.5 | 51.1 | 51.1 | thin at home: hop beer, ham |
| jousting 3 | arena | 230 | 52.1 | 52.2 | needs a arena (build cost 24,414); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold sermon 2 (candles) | church | 31 | 49.7 | 52.3 | needs a church (build cost 65,090); thin at home: candles, furniture |
| hold banquet 3 (meat) | mansion | 7.6 | 52.4 | 52.4 | thin at home: hop beer |
| hold prayer 2 | chapel | 13 | 50.0 | 52.8 | needs a chapel (build cost 30,666); thin at home: furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 53.0 | 53.0 |  |
| hold banquet 1 (fish) | mansion | 4.2 | 53.7 | 53.7 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 9 | 151802239 | 0.04 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -1 a turn after crew: ship stays at 0
- best towns now: Hofkirchen +17, Bordetes +15
- Hofkirchen would trade: beer sell 34 @ 4.84, candles buy 1 @ 65.0, garments buy 2 @ 18.7; crew 0.3

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~92 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.29 | 0.60 (55/turn) | beer 54 (3.16->4.8), grindstones 1 (208.95->254.6), wine 8 (6.09->7.55), thread 6 (3.36->4.16) | acid 1 (137.55->141.55), candles 1 (67.2->70.5), gears 2 (60.38->61.75), garments 2 (19.32->20) | +120 |
| Heilegg | 826 | 0.21 | 0.70 (65/turn) | grindstones 1 (208.95->296.4), beer 54 (3.16->3.88), thread 13 (3.36->4.48), grain 8 (2.26->2.94) | garments 2 (19.32->20), silver ore 1 (34.23->36.48) | +114 |
| Briclives | 1041 | 0.32 | 0.70 (65/turn) | beer 54 (3.16->4.48), malt 7 (6.51->10.54), arms 6 (24.99->27.17), grindstones 1 (208.95->224.2) | tools 2 (4.26->4.72) | +85 |
| Rotterburg | 1056 | 0.32 | 0.30 (28/turn) | sails 1 (588->612.75), grindstones 1 (208.95->235.6), tackles 1 (180.6->195.7), glass ingots 2 (56.7->62.7) | garments 2 (18.9->20) | +73 |
| Amsdermund | 1111 | 0.35 | 0.70 (65/turn) | grindstones 1 (208.95->250.8), wine 8 (6.09->7.69), beer 54 (3.16->4.03), lead ore 2 (9.35->14.54) | spirits 4 (15.75->17.1), garments 2 (18.9->20), acid 1 (140.7->141.55) | +73 |

**Best:** Hofkirchen at about +120 coin a turn.

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
| pasties | 3 @ 13.4, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 4.9 turns |
| porterage | 8 @ 1.1, stop - |  | uses 8.1/turn (observed), makes 0.0, holds 10 = 1.2 turns |
| rope |  | 2 @ min 72.5 |  |
| timber |  | 10 @ min 6.5 | makes 8.4, uses 0.0, holds 376 (keeps 350): sells the surplus + 1/turn of the excess |
| tools | 3 @ 6.2, stop 24 |  | uses 3.0/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 66.6 turns |

## Goal: business value (shadow)
- Value now 16.3k (cash + stock at home prices); +59/turn over 6 turns, -54/turn over 24 turns.
- Limits: cash flow >= +68/turn, prestige >= -0.75/turn (values are after 240 tax a turn).
- Today's settings: value +148/turn, cash +336/turn, prestige -1.40/turn - breaks the prestige floor.
- Plan: value +458/turn, cash +667/turn, prestige -0.75/turn, inside both limits.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Hofkirchen: +39/turn
  - ship Flax Wyrm -> Kirchwerp: +1/turn
  - brewery 1 0.40 -> 1.00: +154/turn
  - ropewalk 1 0.50 -> 1.00: +17/turn
  - quarry 1 0.00 -> 0.08: +5/turn
  - net maker 0.50 -> 0.00: -5/turn
  - net maker [make nets 2] 0.00 -> 1.00: +13/turn
  - logging camp w/ tool 7.00 -> 0.00: -8/turn
  - logging camp w/ tool [cut firewood 1] 0.00 -> 20.00: +17/turn
  - weavery 1 0.00 -> 1.00: -27/turn
- Model check over the last 13 turns: predicted +95/turn for the settings we ran, real +44/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.46, thread 4.25, cloth 6.44, flax fibres 4.97, garments 17.64, nets 33.43, beer 3.50, timber 6.15, prestige 56.47, cash 0.00
- Orders it would set (dry run): porterage buy 9 (v2 8); rope sell 3 (v2 2)
- Recipe: logging camp w/ tool split timber 2 -> cut firewood 1 at 20.00, worth +17/turn.
- Recipe: net maker make nets 1 -> make nets 2 at 1.00, worth +23/turn.
- Ship linen snake: Grandgues -> Hofkirchen (+120/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Kirchwerp (+46/turn over staying).
- Management: ~13.78 of 17 used.
- Investments:
  - +1 plot brewery 1 for ~2887 coin: +79/turn, payback 37 turns
  - new brewery (brew beer 1) for ~2887 coin: +79/turn, payback 37 turns
  - Tenants L13 for 500 prestige: +73/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new chandlery (make candles 2) for ~3930 coin: +72/turn, payback 55 turns
  - new bloomery (smelt iron 1) for ~2567 coin: +39/turn, payback 67 turns
  - +1 plot ropewalk 1 for ~2611 coin: +23/turn, payback 116 turns
- Trim: donate quarry 1: +15/turn (tax 20 saved).
- Trim: donate sewing shop 1: +12/turn (tax 12 saved).

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

Buffers: flax fibres 46/80, thread 277/236, cloth 19/89
- chain plan needed 557 labour, budget left 435: cut to 435 (sewing capped at 0.55)

## Self-diagnosis

- R3: weavery 1 (weavery) finished but idle 6 turns (weave cloth 2 at 0); no planned recipe for a weavery: Taylor's call
- R3: sewing shop 1 (sewing shop) finished but idle 6 turns (sew garments 2 at 0); no planned recipe for a sewing shop: Taylor's call
- R3: mansion 1 (mansion) finished but idle 6 turns (hold banquet 1 (meat) at 0); no planned recipe for a mansion: Taylor's call
- R3: quarry 1 (quarry) finished but idle 6 turns (extract stone 1 at 0); no planned recipe for a quarry: Taylor's call
- R7 stale ask: garments ask 20 over the market for 6 turns: the town trades ~63 a turn at 19.6, we sold 0 with 84 over what we keep; floor 20 (config sell_floor / unit cost) is at or over the market: Taylor's call
