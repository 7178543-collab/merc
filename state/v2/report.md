# v2 shadow report

Turn 13498, 2026-10-23 19:53. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 1,283, prestige 3,595 (475 free, -0.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 84 | 0 | 7 | 0 | 0 | min_holding 60, sell 119, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 31 | 7 | 10 | 0 | 0 | stop 40, buy 15, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 123 | 0 | 2 | 0 | 0 | min_holding 30, sell 25, sell @ 20 |
| grain | 140 | 27 | 58 | 0 | 0 | stop 234, buy 106, buy @ 3.7 |
| labour | 269 | 205 | 659 | 0 | 46 | buy 314, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 34 |
| porterage | 12 | 5 | 5 | 7 | 0 | buy 12, buy @ 1.1 |

**2 risks, 2 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **porterage**: logging camp w/ tool, flax farm 1, quarry 1 ran short of porterage (buy is live (12 @ 1.1), 5 bought last turn); knock-on: retting pit 1 (no flax plants); labour need rises ~163/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **porterage**: buying 12, short of ~17 needed -> v2: buy 17

## Waste (money lost now)

- **labour**: 46 labour expired last turn (~67 coin): holding 269 against a ~0 buffer target -> v2: trim the buy until the stock is near 0
- **linen snake**: linen snake cost 9 coin last turn (crew 0.10) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell

## Notes

- labour: projection runs 100 over real use lately; planning 740, not 840
- labour expiry guard: 46 bought labour expired last turn, buy 159 (not 240) this turn

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
| hold prayer 2 | chapel | 13 | 49.8 | 52.6 | needs a chapel (build cost 29,643); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 50.0 | 52.6 | needs a church (build cost 63,844); thin at home: candles, furniture |
| hold banquet 1 (fish) | mansion | 4.2 | 52.9 | 52.9 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 9 | 134102075 | 0.136 | - | furniture 9 | -112 |
| linen snake | 0.1 / 0.10 | 9 | 151802239 | 0.112 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 8 @ 12.7, tar buy 1 @ 7.55; crew 0.1; est +102 a turn; stock: furniture 8 @ 12.7 (keep 145)
- **linen snake** on Grandgues: furniture buy 7 @ 13.7; crew 0.1; est +80 a turn; stock: furniture 7 @ 13.7 (keep 145)
- best towns now: Hofkirchen +126, Heidlowe +109, Chatgnan +105, Toqueque +105, Etallaen +104
- Hofkirchen would trade: beer sell 23 @ 5.05, furniture buy 8 @ 12.0; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~91 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Briclives | 1041 | 0.31 | 0.80 (73/turn) | beer 95 (3.16->5.22), flour 2 (19.43->22.8), nets 1 (35->36.29), dyed yarn 1 (5.78->6.22) | belts 2 (27.72->30.02), flax plants 1 (1.26->1.92) | +137 |
| Vauxvais | 204 | 0.05 | 0.10 (9/turn) | bellows 1 (312.9->421.8), scythes 2 (27.3->31.35), dyed yarn 1 (5.78->6.79) | premium ham 1 (285.6->290.7), candles 1 (68.25->70), thread 18 (4.41->4.56), tiles 2 (2.58->3.53) | +122 |
| Hofkirchen | 991 | 0.29 | 1.00 (91/turn) | beer 52 (3.16->5.51), bread 62 (2.05->2.94), lead ore 0 (10.71->13.49), dyed yarn 0 (5.78->7.22) | harnesses 0 (53.03->55.57), furniture 0 (12.39->13.8) | +98 |
| Rouhomme | 368 | 0.09 | 0.90 (82/turn) | bread 143 (2.05->2.62), charcoal 12 (1.63->3.31), beer 121 (3.16->3.42), cloth 10 (7.25->7.98) | flax fibres 7 (5.35->5.85), slaked lime 1 (6.83->7.6), flax plants 1 (1.44->1.92) | +76 |
| Dedlowe | 1146 | 0.36 | 0.10 (9/turn) | dyed yarn 1 (5.78->7.17), nets 3 (35->36.1), pasties 1 (12.3->13.87) | windows 1 (464.1->527.25), glass ingots 1 (44.1->46.17) | +61 |

**Best:** Briclives at about +137 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 133 @ min 3.38 |  |
| candles | 2 @ 70.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 12 = 7.7 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 18 @ 2.4, stop 44 |  | uses 10.8/turn (brewery 1, household upkeep), makes 0.0, holds 31 = 2.9 turns |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 29 @ min 20.0 | makes 10.2, uses 2.1, holds 123 (keeps 30): sells the surplus + 21/turn of the excess |
| grain | 125 @ 3.7, stop 260 |  | uses 65.0/turn (brewery 1), makes 0.0, holds 140 = 2.2 turns |
| labour | 270 @ 2.2, stop - |  | goal planner: buys 270 for today's rates (v2 had 159) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 11 @ min 34.0 |  |
| pasties | 3 @ 14.5, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 14 = 4.9 turns |
| porterage | 18 @ 1.1, stop - |  | goal planner: buys 18 for today's rates (v2 had 17) |
| rope |  | 5 @ min 74.0 | goal planner: sells 5 (v2 had 4) |
| tar | 2 @ 11.0, stop 5 |  | uses 1.1/turn (ropewalk 1), makes 0.0, holds 10 = 8.7 turns |
| tools | 4 @ 6.2, stop 31 |  | uses 3.8/turn (observed), makes 0.0, holds 199 = 52.5 turns |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 16.1k (cash + stock at home prices); -20/turn over 6 turns, +35/turn over 24 turns.
- Limits: cash flow >= +113/turn, prestige >= -0.73/turn (values are after 240 tax a turn).
- Today's settings: value +211/turn, cash +377/turn, prestige -0.72/turn.
- Plan: value +296/turn, cash +375/turn, prestige -0.73/turn, inside both limits.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Briclives: +103/turn
  - ship Flax Wyrm -> Grandgues: +17/turn
  - logging camp w/ tool 8.75 -> 20.00: +23/turn
  - sewing shop 1 0.25 -> 0.33: -7/turn
  - weavery 1 0.37 -> 0.76: +1/turn
  - net maker 0.50 -> 0.00: -6/turn
  - net maker [make nets 2] 0.00 -> 1.00: +16/turn
  - flax farm 1 6.78 -> 11.00: -16/turn
  - retting pit 1 1.12 -> 2.10: -20/turn
  - spinnery 1 1.98 -> 3.96: +94/turn
- Model check: not enough runs yet (needs 6 turns of goal history).
- Worth of one more unit per turn: labour 1.45, thread 3.81, cloth 5.98, flax fibres 4.80, garments 17.16, nets 35.00, beer 3.15, timber 5.54, prestige 54.23, cash 0.00
- Orders it would set: labour buy 270 (v2 159); porterage buy 18 (v2 17); rope sell 5 (v2 4)
- Recipe: net maker make nets 1 -> make nets 2 at 1.00, worth +33/turn.
- Ship linen snake: Grandgues -> Briclives (+92/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Grandgues (+7/turn over staying).
- Management: ~13.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +72/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new chandlery (make candles 2) for ~3951 coin: +47/turn, payback 84 turns, doesn't pay yet (materials thin at home: bricks)
  - +1 plot ropewalk 1 for ~2685 coin: +44/turn, payback 60 turns
  - +1 plot net maker for ~1349 coin: +24/turn, payback 57 turns
  - +1 plot brewery 1 for ~2924 coin: +11/turn, payback 263 turns, doesn't pay yet (materials thin at home: bricks)
  - +1 plot flax farm 1 for ~432 coin: +4/turn, payback 122 turns

## Chain sizing

Mode HOLD, garments sold 0.0/turn (+0.0 exported); plan makes 0.0 garments a turn.
Labour: own 500, everything else 544, chain may buy 0 -> chain allowance 0, chain plan 202 (-123 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 6.78 | 4.60 |
| ret | 3 | 1.12 | 0.82 |
| spin | 4 | 1.98 | 1.68 |
| weave | 3 | 0.37 | 0.00 |
| sew | 2 | 0.25 | 0.00 |

Buffers: flax fibres 44/69, thread 404/202, cloth 53/0
- chain plan needed 202 labour, budget left 0: cut to 202

## Self-diagnosis

- R7 stale ask: garments ask 20 over the market for 6 turns: the town trades ~61 a turn at 19.6, we sold 0 with 93 over what we keep; floor 20 (config sell_floor / unit cost) is at or over the market: Taylor's call
- R7 stale ask: timber ask 6.5 over the market for 6 turns: the town trades ~81 a turn at 6.15, we sold 0 with 26 over what we keep; floor 6.5 (config sell_floor / unit cost) is at or over the market: Taylor's call
