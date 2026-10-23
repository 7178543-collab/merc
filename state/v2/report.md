# v2 shadow report

Turn 13499, 2026-10-23 20:12. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 1,096, prestige 3,593 (473 free, -1.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 87 | 0 | 4 | 0 | 0 | min_holding 60, sell 136, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 38 | 19 | 11 | 0 | 0 | stop 44, buy 14, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 135 | 0 | 2 | 0 | 0 | min_holding 30, sell 35, sell @ 20 |
| grain | 183 | 117 | 65 | 0 | 0 | stop 260, buy 104, buy @ 3.7 |
| labour | 348 | 269 | 740 | 0 | 29 | buy 372, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34 |
| porterage | 12 | 12 | 12 | 7 | 0 | buy 20, buy @ 1.1 |

**6 risks, 3 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (6 @ 29), home ask 21.20 x5, yet 0 bought last turn); labour need rises ~5/turn when they restart -> v2: find out why the buy isn't filling
- **flax plants**: retting pit 1 ran short of flax plants (buy is live (no volume cap @ 2.04), home ask 1.63 x2, yet 0 bought last turn); labour need rises ~44/turn when they restart -> v2: find out why the buy isn't filling
- **porterage**: logging camp w/ tool, quarry 1 ran short of porterage (buy is live (20 @ 1.1), 12 bought last turn); labour need rises ~69/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **porterage**: buying 20, short of ~22 needed -> v2: buy 22
- **wax**: net maker152202386007001 ran short of wax (no buy order); labour need rises ~12/turn when they restart -> v2: add a wax buy
- **wax**: needed (0.1/turn) but there is NO buy order, stock 0.0 -> v2: add buy 1

## Waste (money lost now)

- **Flax Wyrm**: Flax Wyrm cost 9 coin last turn (crew 0.10) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell
- **labour**: 29 labour expired last turn (~42 coin): holding 348 against a ~0 buffer target -> v2: trim the buy until the stock is near 0
- **linen snake**: linen snake cost 9 coin last turn (crew 0.10) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell

## Tuning

- **cloth**: cloth buffer thin: 1.7 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 53
- **grain**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 134 over real use lately; planning 750, not 884

## Prestige spending, cheapest coin per prestige first

902 turns left: prestige gained now converts 98.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 44.1 | 44.1 | running |
| hold banquet 4 (pies) | mansion | 18 | 47.6 | 47.6 | thin at home: hop beer, wine |
| hold banquet 3 (pies) | mansion | 8 | 47.8 | 47.8 | thin at home: hop beer, pies |
| hold banquet 2 (pies) | mansion | 7 | 49.4 | 49.4 | thin at home: wine, pies |
| hold banquet 4 | mansion | 17.5 | 50.9 | 50.9 | thin at home: wine, hop beer, ham |
| hold banquet 3 (fish) | mansion | 7.6 | 51.2 | 51.2 | thin at home: hop beer |
| hold banquet 3 (meat) | mansion | 7.6 | 51.8 | 51.8 | thin at home: hop beer |
| jousting 3 | arena | 230 | 51.9 | 52.0 | needs a arena (build cost 23,912); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 52.1 | 52.1 | thin at home: wine |
| hold banquet 2 (meat) | mansion | 6.8 | 52.8 | 52.8 | thin at home: wine |
| hold prayer 2 | chapel | 13 | 50.1 | 52.8 | needs a chapel (build cost 30,014); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 50.3 | 52.8 | needs a church (build cost 64,328); thin at home: candles, furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 9 | 134102075 | 0.028 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 9 | 151802239 | 0.02 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: candles buy 1 @ 68.0, furniture buy 1 @ 14.2; crew 0.1; est +25 a turn; stock: candles 1 @ 68.0 (keep 12); stock: furniture 1 @ 14.2 (keep 145)
- **Flax Wyrm** on Caillechâtel: candles buy 1 @ 71.0, furniture buy 1 @ 12.7, tar buy 1 @ 7.75; crew 0.1; est +24 a turn; stock: candles 1 @ 71.0 (keep 12); stock: furniture 1 @ 12.7 (keep 145)
- best towns now: Donaunieder +69, Amsdermund +67, Friedwerp +48, Hofkirchen +48, Briclives +41
- Donaunieder would trade: furniture buy 6 @ 13.4; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~92 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.29 | 1.00 (92/turn) | beer 137 (3.16->5.32), lead ore 2 (10.19->13.59), wine 4 (5.51->6.51), yarn 5 (4.22->4.94) | furniture 1 (12.18->14.2), garments 2 (18.9->19.5), harnesses 1 (53.55->55.57) | +229 |
| Briclives | 1041 | 0.31 | 0.80 (73/turn) | beer 95 (3.16->5.42), malt 3 (7.25->12.25), rope 1 (75->82.17), cured meat 6 (22.26->23.37) | chisels 2 (8.61->12.54), nails 17 (4.79->5.13) | +184 |
| Cobholme | 1564 | 0.57 | 0.20 (18/turn) | sails 2 (603.75->655.5), wine 4 (5.51->8.64), hides 1 (12.6->14.25), pasties 2 (13.65->15.58) | - | +103 |
| Heilegg | 826 | 0.21 | 1.00 (92/turn) | beer 137 (3.16->3.97), grindstones 1 (281.4->296.4), chisels 4 (14.18->15.96), wine 4 (5.51->6.79) | jewellery 3 (80.85->82.65), harnesses 1 (53.03->55.57), garments 2 (18.69->19.5), silver ore 1 (34.44->36.1) | +83 |
| Arnsreuth | 921 | 0.26 | 0.10 (9/turn) | garments 12 (18.3->23.37), glass ingots 2 (58.28->59.85), wine 3 (5.51->6.13), potash 1 (18.48->19) | glassware 1 (38.43->46.36), harnesses 1 (47.88->55.57) | +73 |

**Best:** Hofkirchen at about +229 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 28.0, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 4 = 7.0 turns |
| beer |  | 136 @ min 3.38 |  |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 10 = 6.7 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 14 @ 2.4, stop 44 |  | uses 10.8/turn (brewery 1, household upkeep), makes 0.0, holds 38 = 3.5 turns |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 35 @ min 20.0 | makes 13.7, uses 2.1, holds 135 (keeps 30): sells the surplus + 23/turn of the excess |
| grain | 104 @ 3.7, stop 260 |  | uses 65.0/turn (brewery 1), makes 0.0, holds 183 = 2.8 turns |
| labour | 372 @ 2.2, stop - |  | goal planner: buys 372 for today's rates (v2 had 250) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 9 @ min 34.0 |  |
| pasties | 4 @ 14.5, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 11 = 3.9 turns |
| porterage | 24 @ 1.1, stop - |  | goal planner: buys 24 for today's rates (v2 had 22) |
| rope |  | 5 @ min 73.0 | goal planner: sells 5 (v2 had 4) |
| tar | 2 @ 11.0, stop 5 |  | uses 1.1/turn (ropewalk 1), makes 0.0, holds 9 = 7.7 turns |
| tools | 4 @ 6.2, stop 31 |  | uses 3.8/turn (observed), makes 0.0, holds 196 = 51.5 turns |
| wax | 1 @ 22.6, stop 1 |  | uses 0.1/turn (observed), makes 0.0, holds 0 = 0.0 turns |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 16.1k (cash + stock at home prices); -20/turn over 6 turns, +35/turn over 24 turns.
- Limits: cash flow >= +121/turn, prestige >= -0.72/turn (values are after 240 tax a turn).
- Today's settings: value -202/turn, cash -349/turn, prestige -0.72/turn - breaks the cash floor.
- Plan: value +168/turn, cash +248/turn, prestige -0.72/turn, inside both limits.
- Route sales counted at most (what the ships really sold, a turn): garments 0.5, nets 0.0, rope 0.1.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Pontmont: +1/turn
  - ship Flax Wyrm -> Bordetes: +1/turn
  - brewery 1 1.00 -> 0.46: +131/turn
  - sewing shop 1 0.33 -> 0.12: +60/turn
  - retting pit 1 1.75 -> 1.19: +51/turn
  - logging camp w/ tool 13.67 -> 0.00: +22/turn
  - spinnery 1 2.48 -> 2.22: +20/turn
  - logging camp w/ tool [cut firewood 1] 0.00 -> 20.00: +17/turn
  - weavery 1 0.37 -> 0.19: +17/turn
  - quarry 1 0.24 -> 0.08: +10/turn
- Model check: not enough runs yet (needs 6 turns of goal history).
- Worth of one more unit per turn: labour 1.47, thread 3.63, cloth 5.84, flax fibres 4.20, garments 16.95, nets 35.00, beer 2.74, timber 6.39, prestige 55.83, cash 0.00
- Orders it would set: labour buy 372 (v2 250); porterage buy 24 (v2 22); rope sell 5 (v2 4)
- Recipe: logging camp w/ tool split timber 2 -> cut firewood 1 at 20.00, worth +17/turn.
- Recipe: net maker make nets 2 -> make nets 3 at 1.00, worth +36/turn.
- Ship linen snake: Grandgues -> Pontmont (+1/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Bordetes (+1/turn over staying).
- Management: ~13.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +73/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot net maker for ~1352 coin: +29/turn, payback 46 turns
  - new weaponsmith (forge arms 1) for ~2644 coin: +15/turn, payback 178 turns, doesn't pay yet (materials thin at home: bricks)
- Trim: donate quarry 1: +15/turn (tax 20 saved).
- Trim: donate weavery 1: +15/turn (tax 18 saved).

## Chain sizing

Mode HOLD, garments sold 0.0/turn (+0.0 exported); plan makes 0.0 garments a turn.
Labour: own 500, everything else 560, chain may buy 0 -> chain allowance 0, chain plan 204 (-207 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 8.47 | 4.66 |
| ret | 3 | 1.75 | 0.83 |
| spin | 4 | 2.48 | 1.70 |
| weave | 3 | 0.37 | 0.00 |
| sew | 2 | 0.33 | 0.00 |

Buffers: flax fibres 39/69, thread 406/204, cloth 45/0
- chain plan needed 204 labour, budget left 0: cut to 204

## Self-diagnosis

- R7 stale ask: cured meat ask 24 over the market for 3 turns: the town trades ~4 a turn at 21.2, we sold 0 with 9 over what we keep; floor 24.42 (config sell_floor / unit cost) is at or over the market: Taylor's call
- R7 stale ask: garments ask 20 over the market for 6 turns: the town trades ~60 a turn at 19.5, we sold 0 with 105 over what we keep; floor 20 (config sell_floor / unit cost) is at or over the market: Taylor's call
- R7 stale ask: timber ask 6.5 over the market for 6 turns: the town trades ~81 a turn at 6.17, we sold 0 with 36 over what we keep; floor 6.5 (config sell_floor / unit cost) is at or over the market: Taylor's call
