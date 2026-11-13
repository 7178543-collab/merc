# v2 shadow report

Turn 13990, 2026-11-13 07:54. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,707, prestige 3,500 (380 free, -2.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 1 | 0 | 4 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 17, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **beer**: needed (4.2/turn) but there is NO buy order, stock 1.2 -> v2: add buy 9
- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 10.20 x5, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~82 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 99 over real use lately; planning 497, not 596

## Prestige spending, cheapest coin per prestige first

411 turns left: prestige gained now converts 87.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 53.4 | 53.4 | running |
| jousting 3 | arena | 230 | 55.3 | 55.7 | needs a arena (build cost 28,193); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 57.4 | 57.4 | thin at home: stockfish, pies, candles |
| hold banquet 3 (pies) | mansion | 8 | 58.1 | 58.1 | thin at home: pies, candles |
| hold banquet 1 (fish) | mansion | 4.2 | 59.0 | 59.0 | thin at home: beer |
| hold banquet 3 (fish) | mansion | 7.6 | 59.1 | 59.1 |  |
| hold banquet 2 (pies) | mansion | 7 | 59.5 | 59.5 | thin at home: pies, candles |
| hold banquet 2 (fish) | mansion | 6.8 | 59.6 | 59.6 |  |
| hold banquet 4 (premium) | mansion | 20 | 59.9 | 59.9 | thin at home: stockfish, candles |
| hold banquet 4 | mansion | 17.5 | 60.7 | 60.7 | thin at home: ham, stockfish, candles |
| jousting 2 | arena | 210 | 60.6 | 61.0 | needs a arena (build cost 28,193); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold mass 2 (premium) | cathedral | 360 | 61.3 | 64.3 | needs a cathedral (build cost 313,950); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 134102075 | 0.068 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 3 @ 13.8, pasties buy 3 @ 15.3; crew 0.1; est +38 a turn; stock: furniture 3 @ 13.8 (keep 145); stock: pasties 3 @ 15.3 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 16.0 (keep 14); best orders clear only -2 a turn after crew: ship stays at 0
- best towns now: Disscester +47, Coburgbaum +46, Gosschweig +45, Vauxvais +42, Hofkirchen +41
- Disscester would trade: furniture buy 3 @ 12.2, pasties buy 4 @ 12.4; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~109 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 1.00 (109/turn) | timber 42 (7.88->12.44), firewood 44 (2.86->6.7), bread 154 (2.56->2.85), garments 10 (19.63->20.52) | tools 9 (4.81->5.79), dyed cloth 8 (13.12->13.87), axes 1 (20.06->21.66), salt 1 (5.51->5.56) | +330 |
| Fontaux | 411 | 0.12 | 0.90 (98/turn) | beer 90 (3.91->5.13), timber 22 (7.88->11.69), thread 73 (4.96->5.65), garments 10 (19.63->22.42) | axes 3 (19.84->21.66), dyed cloth 2 (12.5->13.87), tools 16 (5.67->5.79) | +223 |
| Clairlond | 1288 | 0.52 | 0.10 (11/turn) | premium cheese 3 (33.39->36.86), garments 10 (19.63->20.9) | windows 1 (598.5->788.5), dyed cloth 8 (12.39->13.87), axes 3 (18.69->21.66), raw cloth 1 (6.3->7.17) | +219 |
| Vauxvais | 204 | 0.06 | 1.00 (109/turn) | beer 52 (3.91->5.22), firewood 36 (2.86->5.7), charcoal 13 (2.52->4.66), garments 7 (19.63->20.71) | windows 0 (777->788.5), dyed cloth 5 (13.02->13.87), flax fibres 8 (6.2->6.85), tools 11 (5.35->5.79) | +158 |
| Arnsreuth | 921 | 0.30 | 0.10 (11/turn) | garments 10 (19.63->24.51), arms 2 (35.49->40.28), wool 4 (10.92->11.97), cloth 1 (7.7->8.6) | windows 1 (735->788.5), axes 3 (17.96->21.66), dyed cloth 7 (12.5->13.87), salt 3 (4.77->5.56) | +131 |

**Best:** Grandgues at about +330 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 35.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 9 @ 4.64, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 1 = 0.3 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 74, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 15.8, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 22.8) |
| grain | 5 @ 3.7, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 107, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 37.0) |
| pasties |  | 1 @ min 15.8 | goal planner: sells 1 a turn at 15.8, keeps 0 (no one offered it) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 29.8k (cash + stock at home prices); +239/turn over 6 turns, +107/turn over 24 turns.
- Limits: cash flow >= -446/turn, prestige >= -0.33/turn (values are after 200 tax a turn).
- Today's settings: value +70/turn, cash +68/turn, prestige -2.11/turn - breaks the prestige floor.
- Plan: value -26/turn, cash -10/turn, prestige -0.33/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +286 vs +65, +138 vs +68, +229 vs +70.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Corstoft: +1/turn
  - ship Flax Wyrm -> no route: +0/turn
  - brewery 1 0.14 -> 0.07: +14/turn
  - net maker 0.00 -> 0.29: +6/turn
  - spinnery 1 1.65 -> 1.35: +1/turn
  - retting pit 1 0.91 -> 0.85: +1/turn
  - flax farm 1 4.64 -> 4.25: +1/turn
  - weavery 1 0.50 -> 0.43: -10/turn
  - mansion 1 0.00 -> 0.42: -119/turn
- Model check over the last 60 turns: predicted +105/turn for the settings we ran, real -13/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.96, garments 19.30, nets 30.25, beer 3.16, timber 4.00, prestige 77.70, cash 0.00
- Orders it would set: candles buy 2 (v2 None); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None); pasties sell 1 (v2 none); rope sell 1 (v2 none)
- Ship linen snake: Grandgues -> Corstoft (+1/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1958 coin: +8/turn, payback 247 turns, doesn't pay yet

## Chain sizing

Mode HOLD, garments sold 10.5/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 414 (+125 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 3.86 |
| ret | 3 | 0.91 | 0.77 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 142/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R1: beer slot dry: 1.2 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy none, home ask 4.42 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 9 @ 4.5 (ask 4.42, cap 5.7))
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
