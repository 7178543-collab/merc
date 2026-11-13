# v2 shadow report

Turn 13987, 2026-11-13 04:37. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,053, prestige 3,506 (386 free, -2.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 14 | 9 | 4 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 26, buy 9, buy @ 3.76 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 20, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 511 | 0 | 18 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 3.06 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.06 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **labour**: 18 labour expired last turn (~32 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 103 over real use lately; planning 511, not 610

## Prestige spending, cheapest coin per prestige first

414 turns left: prestige gained now converts 87.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 53.1 | 53.1 | running |
| jousting 3 | arena | 230 | 56.0 | 56.3 | needs a arena (build cost 26,930); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 57.5 | 57.5 | thin at home: stockfish, candles |
| hold banquet 1 (fish) | mansion | 4.2 | 58.1 | 58.1 |  |
| hold banquet 3 (pies) | mansion | 8 | 59.6 | 59.6 | thin at home: pies, candles |
| hold banquet 4 (premium) | mansion | 20 | 60.0 | 60.0 | thin at home: stockfish, candles |
| hold banquet 3 (fish) | mansion | 7.6 | 60.3 | 60.3 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 60.6 | 60.6 |  |
| hold banquet 4 | mansion | 17.5 | 60.7 | 60.7 | thin at home: ham, stockfish, candles |
| hold banquet 2 (pies) | mansion | 7 | 61.4 | 61.4 | thin at home: pies, candles |
| jousting 2 | arena | 210 | 61.3 | 61.7 | needs a arena (build cost 26,930); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold mass 2 (premium) | cathedral | 360 | 60.7 | 63.4 | needs a cathedral (build cost 289,300); thin at home: furniture, jewellery, glassware, candles, premium garments |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 14.8 (keep 14); best orders clear only -3 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 16.0 (keep 14); best orders clear only -5 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~108 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Gotthafen | 964 | 0.33 | 0.20 (22/turn) | windows 1 (614.25->712.5), garments 10 (23.8->26.03), lead bars 7 (15.12->16.15), lead ore 6 (8.82->11.02) | looms 1 (540.75->693.5), lathes 1 (191.1->275.5), butter 1 (67.73->75.05), jewellery 2 (116.55->117.8) | +362 |
| Grandgues | 152 | 0.04 | 0.80 (87/turn) | timber 39 (8.72->12.44), firewood 29 (3.21->7.5), windows 1 (614.25->665), bread 156 (2.52->2.93) | cloth 10 (6.88->7.8), tools 8 (4.6->5.27), ham 1 (85.58->89.3), garments 2 (22.68->24.2) | +333 |
| Kirchwerp | 1072 | 0.39 | 0.60 (65/turn) | windows 1 (614.25->712.5), thread 91 (4.98->5.7), wheels 2 (23.94->38), casks 12 (6.72->8.31) | dyed cloth 8 (11.34->12.73), cheese 3 (5.1->6.27), garments 2 (22.68->24.2) | +176 |
| Heilegg | 826 | 0.25 | 0.70 (76/turn) | windows 1 (614.25->679.25), nets 5 (36.8->42.75), lead ore 9 (8.82->11.4), beer 101 (3.89->4.48) | lathes 1 (245.7->275.5), dyed cloth 8 (11.03->12.73), cloth 24 (7.35->7.8), garments 2 (22.89->24.2) | +164 |
| Corstoft | 1496 | 0.63 | 0.20 (22/turn) | windows 1 (614.25->774.25), garments 10 (23.8->25.46), leather 3 (28.35->30.02) | - | +160 |

**Best:** Gotthafen at about +362 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 35.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 71, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.2) |
| grain | 5 @ 3.7, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 11) |
| light armour | 1 @ 107, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 35.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 74.5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.9k (cash + stock at home prices); +149/turn over 6 turns, +112/turn over 24 turns.
- Limits: cash flow >= -419/turn, prestige >= -0.36/turn (values are after 200 tax a turn).
- Today's settings: value +68/turn, cash +65/turn, prestige -2.14/turn - breaks the prestige floor.
- Plan: value -21/turn, cash -2/turn, prestige -0.36/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +215 vs +33, -10 vs +34, +305 vs +50.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Marmont: +0/turn
  - ship Flax Wyrm -> no route: +0/turn
  - brewery 1 0.14 -> 0.07: +14/turn
  - ropewalk 1 0.25 -> 0.20: +7/turn
  - net maker 0.00 -> 0.29: +6/turn
  - spinnery 1 1.65 -> 1.33: +2/turn
  - retting pit 1 0.91 -> 0.84: +2/turn
  - flax farm 1 4.64 -> 4.22: -5/turn
  - weavery 1 0.50 -> 0.44: -8/turn
  - mansion 1 0.00 -> 0.42: -110/turn
- Model check over the last 58 turns: predicted +105/turn for the settings we ran, real -22/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.96, garments 19.30, nets 30.16, beer 3.15, timber 3.44, prestige 75.09, cash 0.00
- Orders it would set: candles buy 2 (v2 None); firewood buy 1 (v2 3); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 11); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Marmont (+1/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1811 coin: +7/turn, payback 274 turns, doesn't pay yet

## Chain sizing

Mode HOLD, garments sold 10.7/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 413 (+124 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 3.82 |
| ret | 3 | 0.91 | 0.76 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 145/77, thread 1050/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 3.06; ask over the cap 2.1 (60 coin per prestige)
