# v2 shadow report

Turn 13499, 2026-10-23 20:04. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 1,096, prestige 3,593 (473 free, -1.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 87 | 0 | 4 | 0 | 0 | min_holding 60, sell 133, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 38 | 19 | 11 | 0 | 0 | stop 44, buy 18, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 135 | 0 | 2 | 0 | 0 | min_holding 30, sell 29, sell @ 20 |
| grain | 183 | 117 | 65 | 0 | 0 | stop 260, buy 125, buy @ 3.7 |
| labour | 348 | 269 | 740 | 0 | 29 | buy 348, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 34 |
| porterage | 12 | 12 | 12 | 7 | 0 | buy 12, buy @ 1.1 |

**6 risks, 3 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (6 @ 29), home ask 21.20 x6, yet 0 bought last turn); labour need rises ~5/turn when they restart -> v2: find out why the buy isn't filling
- **flax plants**: retting pit 1 ran short of flax plants (buy is live (no volume cap @ 2.04), home ask 1.63 x2, yet 0 bought last turn); labour need rises ~35/turn when they restart -> v2: find out why the buy isn't filling
- **porterage**: logging camp w/ tool, quarry 1 ran short of porterage (buy is live (12 @ 1.1), 12 bought last turn); labour need rises ~60/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **porterage**: buying 12, short of ~19 needed -> v2: buy 19
- **wax**: net maker152202386007001 ran short of wax (no buy order); labour need rises ~6/turn when they restart -> v2: add a wax buy
- **wax**: needed (0.1/turn) but there is NO buy order, stock 0.0 -> v2: add buy 1

## Waste (money lost now)

- **Flax Wyrm**: Flax Wyrm cost 9 coin last turn (crew 0.10) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell
- **labour**: 29 labour expired last turn (~42 coin): holding 348 against a ~0 buffer target -> v2: trim the buy until the stock is near 0
- **linen snake**: linen snake cost 9 coin last turn (crew 0.10) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell

## Tuning

- **cloth**: cloth buffer thin: 1.7 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 53

## Notes

- labour: projection runs 134 over real use lately; planning 740, not 847

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
| Flax Wyrm | 0.1 / 0.10 | 9 | 134102075 | 0.136 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 9 | 151802239 | 0.112 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: candles buy 1 @ 70.0, furniture buy 1 @ 12.7, tar buy 1 @ 7.55; crew 0.1; est +26 a turn; stock: candles 1 @ 70.0 (keep 12); stock: furniture 1 @ 12.7 (keep 145)
- **linen snake** on Grandgues: candles buy 1 @ 68.5, furniture buy 1 @ 13.7; crew 0.1; est +25 a turn; stock: candles 1 @ 68.5 (keep 12); stock: furniture 1 @ 13.7 (keep 145)
- best towns now: Donaunieder +88, Arnsreuth +51, Hofkirchen +49, Friedwerp +41, Briclives +37
- Donaunieder would trade: furniture buy 7 @ 12.5; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~92 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Briclives | 1041 | 0.31 | 0.80 (73/turn) | beer 95 (3.16->5.22), flour 2 (19.43->22.8), nets 1 (35->36.29), dyed yarn 1 (5.78->6.22) | belts 2 (27.72->30.02), flax plants 1 (1.26->1.92) | +137 |
| Vauxvais | 204 | 0.05 | 0.10 (9/turn) | bellows 1 (312.9->421.8), scythes 2 (27.3->31.35), dyed yarn 1 (5.78->6.79) | premium ham 1 (285.6->290.7), candles 1 (68.25->70), thread 18 (4.41->4.56), tiles 2 (2.58->3.53) | +122 |
| Hofkirchen | 991 | 0.29 | 1.00 (92/turn) | beer 59 (3.16->5.51), bread 62 (2.05->2.94), lead ore 0 (10.71->13.49), dyed yarn 0 (5.78->7.22) | harnesses 0 (53.03->55.57), furniture 0 (12.39->13.8) | +110 |
| Arnsreuth | 921 | 0.26 | 0.20 (18/turn) | garments 19 (18.3->22.42), glass ingots 2 (57.75->59.85), flax fibres 3 (5.8->6.6), butter 2 (64.58->65.55) | harnesses 1 (44.1->55.57), slaked lime 1 (6.09->7.6), steel ingots 1 (13.33->14.72), flax plants 1 (1.32->1.92) | +83 |
| Rouhomme | 368 | 0.09 | 0.90 (83/turn) | bread 143 (2.05->2.62), charcoal 12 (1.63->3.31), beer 137 (3.16->3.42), firewood 3 (1.59->5.13) | flax fibres 7 (5.35->5.85), slaked lime 1 (6.83->7.6), flax plants 1 (1.44->1.92) | +78 |

**Best:** Briclives at about +137 coin a turn.

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
| labour | 291 @ 2.2, stop - |  | goal planner: buys 291 for today's rates (v2 had 240) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 9 @ min 34.0 |  |
| pasties | 4 @ 14.5, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 11 = 3.9 turns |
| porterage | 20 @ 1.1, stop - |  | goal planner: buys 20 for today's rates (v2 had 19) |
| rope |  | 5 @ min 73.0 | goal planner: sells 5 (v2 had 4) |
| tar | 2 @ 11.0, stop 5 |  | uses 1.1/turn (ropewalk 1), makes 0.0, holds 9 = 7.7 turns |
| tools | 5 @ 6.2, stop 35 |  | uses 4.3/turn (observed), makes 0.0, holds 196 = 45.4 turns |
| wax | 1 @ 22.6, stop 1 |  | uses 0.1/turn (observed), makes 0.0, holds 0 = 0.0 turns |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 16.1k (cash + stock at home prices); -20/turn over 6 turns, +35/turn over 24 turns.
- Limits: cash flow >= +121/turn, prestige >= -0.72/turn (values are after 240 tax a turn).
- Today's settings: value +198/turn, cash +311/turn, prestige -0.72/turn.
- Plan: value +282/turn, cash +363/turn, prestige -0.72/turn, inside both limits.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Briclives: +99/turn
  - ship Flax Wyrm -> Grandgues: -21/turn
  - logging camp w/ tool 10.94 -> 20.00: +18/turn
  - net maker 0.25 -> 1.00: +11/turn
  - weavery 1 0.37 -> 0.76: -0/turn
  - spinnery 1 1.98 -> 4.00: +11/turn
  - flax farm 1 6.78 -> 11.00: -7/turn
  - retting pit 1 1.40 -> 2.14: +53/turn
- Model check: not enough runs yet (needs 6 turns of goal history).
- Worth of one more unit per turn: labour 1.47, thread 3.93, cloth 6.14, flax fibres 5.07, garments 17.53, nets 35.00, beer 3.15, timber 6.27, prestige 57.39, cash 0.00
- Orders it would set: labour buy 291 (v2 240); porterage buy 20 (v2 19); rope sell 5 (v2 4)
- Ship linen snake: Grandgues -> Briclives (+92/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Grandgues (+6/turn over staying).
- Management: ~13.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +74/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot ropewalk 1 for ~2692 coin: +42/turn, payback 64 turns
  - new chandlery (make candles 2) for ~3964 coin: +30/turn, payback 133 turns, doesn't pay yet (materials thin at home: bricks)
  - +1 plot net maker for ~1352 coin: +23/turn, payback 60 turns
  - +1 plot brewery 1 for ~2934 coin: +9/turn, payback 337 turns, doesn't pay yet (materials thin at home: bricks)
  - +1 plot flax farm 1 for ~434 coin: +4/turn, payback 111 turns

## Chain sizing

Mode HOLD, garments sold 0.0/turn (+0.0 exported); plan makes 0.0 garments a turn.
Labour: own 500, everything else 545, chain may buy 0 -> chain allowance 0, chain plan 189 (-155 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 6.78 | 4.30 |
| ret | 3 | 1.40 | 0.77 |
| spin | 4 | 1.98 | 1.58 |
| weave | 3 | 0.37 | 0.00 |
| sew | 2 | 0.33 | 0.00 |

Buffers: flax fibres 39/66, thread 406/193, cloth 45/0
- chain plan needed 189 labour, budget left 0: cut to 189

## Self-diagnosis

- R7 stale ask: cured meat ask 24 over the market for 3 turns: the town trades ~4 a turn at 21.2, we sold 0 with 9 over what we keep; floor 24.42 (config sell_floor / unit cost) is at or over the market: Taylor's call
- R7 stale ask: garments ask 20 over the market for 6 turns: the town trades ~60 a turn at 19.5, we sold 0 with 105 over what we keep; floor 20 (config sell_floor / unit cost) is at or over the market: Taylor's call
- R7 stale ask: timber ask 6.5 over the market for 6 turns: the town trades ~81 a turn at 6.17, we sold 0 with 36 over what we keep; floor 6.5 (config sell_floor / unit cost) is at or over the market: Taylor's call
