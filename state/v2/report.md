# v2 shadow report

Turn 13494, 2026-10-23 15:55. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
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

**0 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Waste (money lost now)

- **linen snake**: linen snake cost 9 coin last turn (crew 0.10) and its route traded nothing (route limited by rope) -> v2: pause it (crew 0) until a route is proven to sell

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
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
| hold sermon 2 (candles) | church | 31 | 49.7 | 52.2 | needs a church (build cost 63,330); thin at home: candles, furniture |
| jousting 3 | arena | 230 | 52.1 | 52.2 | needs a arena (build cost 23,578); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (meat) | mansion | 7.6 | 52.4 | 52.4 | thin at home: hop beer |
| hold prayer 2 | chapel | 13 | 50.0 | 52.7 | needs a chapel (build cost 29,566); thin at home: furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 53.0 | 53.0 |  |
| hold banquet 1 (fish) | mansion | 4.2 | 53.7 | 53.7 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 9 | 151802239 | 0.04 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -0 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~92 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.29 | 0.50 (46/turn) | beer 54 (3.16->4.89), wrought iron 6 (12.71->16.62), glass ingots 2 (57.23->68.4), wine 8 (6.14->7.46) | acid 1 (136.5->140.6), gears 2 (60.38->61.75), salt 4 (4.07->4.71) | +126 |
| Rouhomme | 368 | 0.09 | 0.50 (46/turn) | looms 1 (682.5->741), charcoal 13 (1.69->3.29), thread 7 (3.36->5.03), beer 54 (3.16->3.42) | spinning wheels 1 (222.6->235.6), lead bars 8 (12.08->12.92), wheels 3 (17.64->19.19), candles 1 (68.78->70.5) | +117 |
| Gosschweig | 1099 | 0.35 | 0.20 (18/turn) | garments 6 (18.4->24.13), flour 2 (19.53->28.5), wax 4 (20.79->23.56), cheese 8 (6.3->7.65) | premium ham 1 (260.4->294.5), candles 1 (63.53->70.5), spirits 1 (14.91->17.1) | +109 |
| Briclives | 1041 | 0.32 | 0.60 (55/turn) | beer 54 (3.16->4.6), soap 1 (91.88->122.55), malt 6 (6.83->11.11), arms 10 (26.46->27.74) | tools 2 (4.26->4.74) | +97 |
| Cobholme | 1564 | 0.58 | 0.20 (18/turn) | thread 14 (3.36->4.67), candles 1 (74.03->79.33), rope 2 (74.5->77.42), cheese 5 (6.3->7.03) | windows 1 (489.3->522.5), gears 1 (53.55->61.75) | +59 |

**Best:** Hofkirchen at about +126 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 52 @ min 3.38 |  |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 12 = 7.7 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 7 @ 2.4, stop 24 |  | uses 6.0/turn (brewery 1, household upkeep), makes 0.0, holds 23 = 3.9 turns |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| grain | 27 @ 3.7, stop 104 |  | uses 26.0/turn (brewery 1), makes 0.0, holds 104 = 4.0 turns |
| labour | 0 @ 2.2, stop - |  | goal planner: buys 0 for today's rates (v2 had 0) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 11 @ min 34.0 |  |
| pasties | 3 @ 13.4, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 4.9 turns |
| porterage | 9 @ 1.1, stop - |  | goal planner: buys 9 for today's rates (v2 had 8) |
| rope |  | 3 @ min 72.5 | goal planner: sells 3 (v2 had 2) |
| timber |  | 10 @ min 6.5 | makes 8.4, uses 0.0, holds 376 (keeps 350): sells the surplus + 1/turn of the excess |
| tools | 3 @ 6.2, stop 24 |  | uses 3.0/turn (logging camp w/ tool, retting pit 1), makes 0.0, holds 199 = 66.6 turns |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 16.2k (cash + stock at home prices); +35/turn over 6 turns, -39/turn over 24 turns.
- Limits: cash flow >= +68/turn, prestige >= -0.75/turn (values are after 240 tax a turn).
- Today's settings: value +153/turn, cash +357/turn, prestige -1.40/turn - breaks the prestige floor.
- Plan: value +432/turn, cash +531/turn, prestige -0.75/turn, inside both limits.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Hofkirchen: +24/turn
  - ship Flax Wyrm -> Kirchwerp: +3/turn
  - brewery 1 0.40 -> 1.00: +148/turn
  - ropewalk 1 0.50 -> 1.00: +18/turn
  - net maker 0.50 -> 0.00: -5/turn
  - net maker [make nets 2] 0.00 -> 1.00: +13/turn
  - logging camp w/ tool 7.00 -> 0.00: -6/turn
  - logging camp w/ tool [cut firewood 1] 0.00 -> 20.00: +23/turn
  - sewing shop 1 0.00 -> 0.11: -9/turn
  - weavery 1 0.00 -> 0.65: -11/turn
- Model check: not enough runs yet (needs 6 turns of goal history).
- Worth of one more unit per turn: labour 1.46, thread 3.87, cloth 6.06, flax fibres 4.45, garments 17.34, nets 33.81, beer 3.50, timber 6.25, prestige 54.67, cash 0.00
- Orders it would set: porterage buy 9 (v2 8); rope sell 3 (v2 2)
- Recipe: logging camp w/ tool split timber 2 -> cut firewood 1 at 20.00, worth +23/turn.
- Recipe: net maker make nets 1 -> make nets 2 at 1.00, worth +32/turn.
- Ship linen snake: Grandgues -> Hofkirchen (+124/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Kirchwerp (+41/turn over staying).
- Management: ~13.78 of 17 used.
- Investments:
  - new chandlery (make candles 2) for ~3950 coin: +77/turn, payback 51 turns
  - Tenants L13 for 500 prestige: +73/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot brewery 1 for ~2909 coin: +61/turn, payback 47 turns
  - new bloomery (smelt iron 1) for ~2575 coin: +47/turn, payback 55 turns
  - +1 plot ropewalk 1 for ~2637 coin: +28/turn, payback 96 turns
  - new guardhouse (protect 1 (armour)) for ~7900 coin: +20/turn, payback 390 turns, doesn't pay yet
- Trim: donate quarry 1: +20/turn (tax 20 saved).

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

- R7 stale ask: garments ask 20 over the market for 6 turns: the town trades ~63 a turn at 19.6, we sold 0 with 84 over what we keep; floor 20 (config sell_floor / unit cost) is at or over the market: Taylor's call
