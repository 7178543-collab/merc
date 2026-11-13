# v2 shadow report

Turn 13988, 2026-11-13 05:43. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,339, prestige 3,504 (384 free, -2.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 10 | 9 | 4 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 17, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 510 | 0 | 19 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.88 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.88 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.10 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 19 labour expired last turn (~35 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: home ask 11.10 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 510, not 601

## Prestige spending, cheapest coin per prestige first

413 turns left: prestige gained now converts 87.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 53.1 | 53.1 | running |
| jousting 3 | arena | 230 | 55.9 | 56.2 | needs a arena (build cost 26,796); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 57.6 | 57.6 | thin at home: stockfish, pies, candles |
| hold banquet 1 (fish) | mansion | 4.2 | 58.2 | 58.2 |  |
| hold banquet 3 (pies) | mansion | 8 | 58.7 | 58.7 | thin at home: pies, candles |
| hold banquet 4 (premium) | mansion | 20 | 60.1 | 60.1 | thin at home: stockfish, candles |
| hold banquet 3 (fish) | mansion | 7.6 | 60.5 | 60.5 |  |
| hold banquet 2 (pies) | mansion | 7 | 60.6 | 60.6 | thin at home: pies, candles |
| hold banquet 2 (fish) | mansion | 6.8 | 60.8 | 60.8 |  |
| hold banquet 4 | mansion | 17.5 | 61.0 | 61.0 | thin at home: ham, stockfish, candles |
| jousting 2 | arena | 210 | 61.2 | 61.5 | needs a arena (build cost 26,796); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold mass 2 (premium) | cathedral | 360 | 60.6 | 63.2 | needs a cathedral (build cost 271,710); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: furniture 1 @ 13.8 (keep 145); stock: pasties 2 @ 14.8 (keep 14); best orders clear only 10 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 15.5 (keep 14); best orders clear only -4 a turn after crew: ship stays at 0
- best towns now: Disscester +16
- Disscester would trade: furniture buy 1 @ 12.4, pasties buy 2 @ 12.4; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~108 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.90 (98/turn) | timber 41 (8.72->12.54), firewood 29 (3.02->7.79), bread 156 (2.65->2.93), garments 10 (19.53->20.33) | cloth 10 (6.88->7.85), tools 10 (4.85->5.75), cheese 4 (6.51->6.7), garments 2 (22.68->23.4) | +278 |
| Fontaux | 411 | 0.12 | 0.60 (65/turn) | thread 72 (4.98->7.27), timber 27 (8.72->11.59), hides 2 (11.65->12.54), flax fibres 4 (6.05->6.32) | tools 16 (5.35->5.75) | +186 |
| Vauxvais | 204 | 0.06 | 1.00 (108/turn) | firewood 46 (3.02->5.7), beer 64 (3.91->4.66), charcoal 16 (2.58->4.69), garments 9 (19.53->20.71) | tools 14 (5.3->5.75), cheese 3 (6.41->6.7), furniture 0 (14.28->15.6), seeds 6 (2.18->2.51) | +128 |
| Neuborn | 780 | 0.23 | 1.00 (108/turn) | tackles 1 (170.1->222.3), cookware 7 (25.2->30.78), garments 10 (19.53->20.71), flax fibres 3 (6.05->7.08) | cheese 4 (5.04->6.7), hop beer 6 (9.19->9.79), dyed cloth 8 (11.34->11.59), garments 2 (23.1->23.4) | +106 |
| Nürnnieder | 520 | 0.15 | 0.10 (11/turn) | garments 10 (19.53->24.51), hides 2 (11.65->12.35), leather 1 (30.66->32.3) | looms 1 (630->693.5) | +105 |

**Best:** Grandgues at about +278 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 35.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 8 @ 3.9, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 10 = 2.3 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 72.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 22.8) |
| grain | 5 @ 3.7, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 10) |
| light armour | 1 @ 107, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 36.6) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 29.1k (cash + stock at home prices); +147/turn over 6 turns, +100/turn over 24 turns.
- Limits: cash flow >= -431/turn, prestige >= -0.35/turn (values are after 200 tax a turn).
- Today's settings: value +70/turn, cash +68/turn, prestige -2.13/turn - breaks the prestige floor.
- Plan: value -26/turn, cash -7/turn, prestige -0.35/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -10 vs +34, +305 vs +50, +286 vs +65.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Vauxvais: +0/turn
  - ship Flax Wyrm -> no route: +0/turn
  - brewery 1 0.14 -> 0.07: +13/turn
  - net maker 0.00 -> 0.29: +6/turn
  - spinnery 1 1.65 -> 1.34: +1/turn
  - retting pit 1 0.91 -> 0.84: +1/turn
  - flax farm 1 4.64 -> 4.24: -0/turn
  - weavery 1 0.50 -> 0.43: -11/turn
  - ropewalk 1 0.25 -> 0.00: -15/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.23: +21/turn
- Model check over the last 59 turns: predicted +105/turn for the settings we ran, real -18/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.96, garments 19.30, nets 30.28, beer 3.04, timber 3.41, prestige 77.01, cash 0.00
- Orders it would set: candles buy 2 (v2 None); firewood buy 1 (v2 3); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 10); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.23, worth +7/turn.
- Ship linen snake: Grandgues -> Vauxvais (+1/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1809 coin: +8/turn, payback 239 turns

## Chain sizing

Mode HOLD, garments sold 10.6/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 414 (+125 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 3.85 |
| ret | 3 | 0.91 | 0.77 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 142/77, thread 1052/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.88; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1052 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
