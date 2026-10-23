# v2 shadow report

Turn 13500, 2026-10-23 21:03. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 897, prestige 3,592 (472 free, -1.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 87 | 0 | 4 | 0 | 0 | min_holding 60, sell 66, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 43 | 18 | 7 | 0 | 0 | stop 44, buy 14, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 133 | 0 | 2 | 0 | 0 | min_holding 30, sell 35, sell @ 20 |
| grain | 151 | 108 | 33 | 0 | 0 | stop 103, buy 26, buy @ 3.7 |
| labour | 47 | 348 | 544 | 0 | 304 | buy 47, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34 |
| porterage | 10 | 12 | 9 | 0 | 3 | buy 10, buy @ 1.1 |

**2 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **wax**: net maker152202386007001 ran short of wax (no buy order); labour need rises ~12/turn when they restart -> v2: add a wax buy
- **wax**: needed (0.1/turn) but there is NO buy order, stock 0.0 -> v2: add buy 1

## Waste (money lost now)

- **labour**: 304 labour expired last turn (~447 coin): holding 47 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **candles**: home ask 71.50 is above our ceiling 70.00 and last turn bought 0 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **flax fibres**: flax fibres buffer thin: 1.4 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 57
- **flax plants**: flax plants buffer thin: 1.5 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 149

## Notes

- labour: projection runs 106 over real use lately; planning 548, not 654
- labour expiry guard: 304 bought labour expired last turn, buy 45 (not 48) this turn

## Prestige spending, cheapest coin per prestige first

901 turns left: prestige gained now converts 98.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 44.1 | 44.1 | running |
| hold banquet 4 (pies) | mansion | 18 | 48.2 | 48.2 | thin at home: hop beer, wine |
| hold banquet 3 (pies) | mansion | 8 | 48.5 | 48.5 | thin at home: hop beer, pies |
| hold banquet 2 (pies) | mansion | 7 | 51.3 | 51.3 | thin at home: wine, pies |
| hold banquet 4 | mansion | 17.5 | 51.4 | 51.4 | thin at home: wine, hop beer, ham |
| jousting 3 | arena | 230 | 51.9 | 52.1 | needs a arena (build cost 23,922); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 52.2 | 52.2 | thin at home: hop beer |
| hold banquet 3 (meat) | mansion | 7.6 | 52.6 | 52.6 | thin at home: hop beer |
| hold prayer 2 | chapel | 13 | 50.1 | 52.9 | needs a chapel (build cost 30,006); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 50.5 | 53.0 | needs a church (build cost 64,375); thin at home: candles, furniture |
| hold banquet 1 (fish) | mansion | 4.2 | 53.8 | 53.8 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 54.0 | 54.0 | thin at home: wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 9 | 134102075 | 0.028 | - | furniture 1 | -12 |
| linen snake | 0.1 / 0.10 | 9 | 151802239 | 0.02 | - | furniture 1 | -14 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only -7 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -2 a turn after crew: ship stays at 0
- best towns now: Briclives +18, Hofkirchen +17
- Briclives would trade: beer sell 26 @ 4.82, rope sell 1 @ 85.0; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~92 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Briclives | 1041 | 0.31 | 0.60 (55/turn) | beer 68 (3.16->5.42), malt 3 (7.25->12.25), rope 1 (75->82.17), cured meat 6 (22.26->23.37) | chisels 2 (8.61->12.54), nails 17 (4.79->5.13) | +141 |
| Hofkirchen | 991 | 0.29 | 0.60 (55/turn) | beer 68 (3.16->5.32), lead ore 2 (10.19->13.59), wine 4 (5.51->6.51), yarn 5 (4.22->4.94) | furniture 1 (12.18->14.2), garments 2 (18.9->19.5), harnesses 1 (53.55->55.57) | +117 |
| Cobholme | 1564 | 0.57 | 0.20 (18/turn) | sails 2 (603.75->655.5), wine 4 (5.51->8.64), pasties 1 (12.3->15.58), hides 1 (12.6->14.25) | - | +103 |
| Etallaen | 774 | 0.19 | 0.10 (9/turn) | flour 1 (19.43->22.61), butter 1 (65.1->66.5), flax plants 4 (1.44->2.05), wine 4 (5.51->5.75) | spinning wheels 2 (210->237.5), furniture 1 (12.71->14.2) | +56 |
| Heilegg | 826 | 0.21 | 0.70 (64/turn) | beer 68 (3.16->3.97), grindstones 1 (281.4->296.4), chisels 4 (14.18->15.96), wine 4 (5.51->6.79) | jewellery 3 (80.85->82.65), harnesses 1 (53.03->55.57), garments 2 (18.69->19.5), silver ore 1 (34.44->36.1) | +55 |

**Best:** Briclives at about +141 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 66 @ min 3.38 |  |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 12 = 7.7 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 28 |  | uses 6.8/turn (brewery 1, household upkeep), makes 0.0, holds 43 = 6.4 turns |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| grain | 29 @ 3.7, stop 113 |  | goal planner: buys 29 a turn for today's rates, keeps up to 113 (v2 had 33) |
| labour | 47 @ 2.2, stop - |  | goal planner: buys 47 for today's rates (v2 had 45) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 9 @ min 34.0 |  |
| pasties | 3 @ 14.5, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 5.0 turns |
| porterage | 10 @ 1.1, stop - |  | goal planner: buys 10 for today's rates (v2 had 9) |
| rope |  | 4 @ min 71.0 |  |
| tar | 2 @ 11.0, stop 5 |  | uses 1.1/turn (ropewalk 1), makes 0.0, holds 9 = 8.6 turns |
| timber |  | 11 @ min 6.5 | makes 8.4, uses 0.0, holds 394 (keeps 350): sells the surplus + 3/turn of the excess |
| tools | 4 @ 6.2, stop 28 |  | uses 3.4/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 58.4 turns |
| wax | 1 @ 23.0, stop 1 |  | uses 0.1/turn (observed), makes 0.0, holds 0 = 0.0 turns |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 16.3k (cash + stock at home prices); -3/turn over 6 turns, +37/turn over 24 turns.
- Limits: cash flow >= +129/turn, prestige >= -0.72/turn (values are after 240 tax a turn).
- Today's settings: value +103/turn, cash +238/turn, prestige -1.37/turn - breaks the prestige floor.
- Plan: value +158/turn, cash +262/turn, prestige -0.72/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -217 vs +316, -187 vs +377, -199 vs +322 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): garments 0.5, nets 0.0, rope 0.1.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Toqueque: +4/turn
  - ship Flax Wyrm -> Heidlowe: +2/turn
  - ropewalk 1 1.00 -> 0.87: +17/turn
  - logging camp w/ tool 7.00 -> 0.00: +8/turn
  - logging camp w/ tool [cut firewood 1] 0.00 -> 20.00: +16/turn
  - quarry 1 0.00 -> 0.08: +4/turn
  - sewing shop 1 0.00 -> 0.11: -8/turn
  - weavery 1 0.00 -> 0.18: +6/turn
  - flax farm 1 4.66 -> 6.24: -9/turn
  - retting pit 1 0.83 -> 1.09: +8/turn
- Model check: not enough runs yet (needs 6 turns of goal history).
- Worth of one more unit per turn: labour 1.47, thread 3.63, cloth 5.84, flax fibres 4.20, garments 16.95, nets 35.00, beer 2.61, timber 6.04, prestige 55.33, cash 0.00
- Orders it would set: arms buy 1 (v2 None); furniture buy 2 (v2 None); grain buy 29 (v2 33); labour buy 47 (v2 45); light armour buy 1 (v2 None); porterage buy 10 (v2 9)
- Recipe: logging camp w/ tool split timber 2 -> cut firewood 1 at 20.00, worth +16/turn.
- Recipe: net maker make nets 2 -> make nets 3 at 1.00, worth +40/turn.
- Ship linen snake: Grandgues -> Toqueque (+5/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Heidlowe (+2/turn over staying).
- Management: ~13.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +74/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot net maker for ~1304 coin: +34/turn, payback 39 turns
  - new weaponsmith (forge arms 1) for ~2609 coin: +17/turn, payback 150 turns, doesn't pay yet (materials thin at home: bricks)
- Trim: donate quarry 1: +16/turn (tax 20 saved).
- Trim: donate weavery 1: +15/turn (tax 18 saved).

## Chain sizing

Mode HOLD, garments sold 0.0/turn (+0.0 exported); plan makes 0.0 garments a turn.
Labour: own 500, everything else 442, chain may buy 0 -> chain allowance 58, chain plan 203 (+0 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.66 | 4.63 |
| ret | 3 | 0.83 | 0.82 |
| spin | 4 | 1.70 | 1.69 |
| weave | 3 | 0.00 | 0.00 |
| sew | 2 | 0.00 | 0.00 |

Buffers: flax fibres 39/69, thread 412/204, cloth 44/0
- chain plan needed 203 labour, budget left 58: cut to 203

## Self-diagnosis

- R7 stale ask: garments ask 20 over the market for 6 turns: the town trades ~59 a turn at 19.5, we sold 0 with 103 over what we keep; floor 20 (config sell_floor / unit cost) is at or over the market: Taylor's call
- R7 stale ask: timber ask 6.5 over the market for 6 turns: the town trades ~80 a turn at 6.1, we sold 0 with 44 over what we keep; floor 6.5 (config sell_floor / unit cost) is at or over the market: Taylor's call
