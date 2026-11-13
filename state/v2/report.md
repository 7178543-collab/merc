# v2 shadow report

Turn 13992, 2026-11-13 09:00. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,936, prestige 3,495 (375 free, -2.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 0 | 0 | 0 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 17, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 516 | 0 | 13 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 0 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 3.66 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.66 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Notes

- labour: projection runs 99 over real use lately; planning 517, not 616

## Prestige spending, cheapest coin per prestige first

409 turns left: prestige gained now converts 87.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 54.3 | 54.3 | running |
| jousting 3 | arena | 230 | 56.4 | 56.7 | needs a arena (build cost 27,017); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 57.5 | 57.5 | thin at home: hop beer, stockfish, pies, candles |
| hold banquet 3 (pies) | mansion | 8 | 58.2 | 58.2 | thin at home: hop beer, pies, candles |
| hold banquet 1 (fish) | mansion | 4.2 | 59.1 | 59.1 |  |
| hold banquet 4 (premium) | mansion | 20 | 59.1 | 59.1 | thin at home: hop beer, stockfish, candles |
| hold banquet 3 (fish) | mansion | 7.6 | 59.3 | 59.3 | thin at home: hop beer |
| hold banquet 2 (pies) | mansion | 7 | 59.4 | 59.4 | thin at home: pies, candles |
| hold banquet 2 (fish) | mansion | 6.8 | 59.5 | 59.5 |  |
| hold banquet 4 | mansion | 17.5 | 60.8 | 60.8 | thin at home: hop beer, ham, stockfish, candles |
| jousting 2 | arena | 210 | 61.7 | 62.1 | needs a arena (build cost 27,017); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold mass 2 (premium) | cathedral | 360 | 61.5 | 64.5 | needs a cathedral (build cost 308,650); thin at home: furniture, jewellery, glassware, candles, premium garments |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 11 | 134102075 | 0.084 | - | pasties 2 | -31 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~110 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 1.00 (110/turn) | timber 38 (7.88->12.35), firewood 41 (3.86->6.65), bread 140 (2.58->2.89), thread 12 (5->5.56) | dyed cloth 6 (12.92->13.77), tools 8 (4.98->5.22) | +251 |
| Unterhufe | 595 | 0.17 | 0.10 (11/turn) | cloth 30 (8.51->11.97), tapestries 1 (745.5->788.5), cheese 17 (6.3->6.51), dyed yarn 1 (5.15->6.03) | rope 1 (73.5->80.75), dyed cloth 7 (12.81->13.77), flax fibres 12 (6.04->6.85), pasties 2 (12.81->14.25) | +165 |
| Angefont | 686 | 0.20 | 0.50 (55/turn) | beer 119 (4.01->5.18), resin 8 (2.75->3.99), copper ingots 1 (15.44->16.81), rope 1 (85->85.5) | flax fibres 28 (5.25->6.85), dyed cloth 7 (12.18->13.77), honey 3 (7.04->8.93), seeds 11 (1.78->2.51) | +155 |
| Fontaux | 411 | 0.12 | 1.00 (110/turn) | beer 61 (4.01->5.32), timber 15 (7.88->11.59), thread 52 (5->5.65), flax fibres 2 (6.35->9.03) | dyed cloth 3 (12.39->13.77) | +149 |
| Etallaen | 774 | 0.23 | 0.40 (44/turn) | beer 63 (4.01->5.61), cloth 11 (8.51->10.92), nets 3 (38->40.66), hides 1 (12.6->17.39) | dyed cloth 7 (12.92->13.77), flax fibres 12 (6.14->6.85), pasties 2 (12.6->14.25), raw cloth 1 (6.72->7.17) | +116 |

**Best:** Grandgues at about +251 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 75.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 15.8, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 20.2) |
| grain | 6 @ 3.7, stop 21 |  | goal planner: buys 6 a turn for today's rates, keeps up to 21 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 17) |
| light armour | 1 @ 107, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 37.0) |
| pasties |  | 1 @ min 15.6 | goal planner: sells 1 a turn at 15.6, keeps 0 (no one offered it) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 81.5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 29.5k (cash + stock at home prices); +176/turn over 6 turns, +66/turn over 24 turns.
- Limits: cash flow >= -456/turn, prestige >= -0.31/turn (values are after 200 tax a turn).
- Today's settings: value +65/turn, cash +52/turn, prestige -2.59/turn - breaks the prestige floor.
- Plan: value -38/turn, cash -21/turn, prestige -0.31/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +286 vs +65, +138 vs +68, +229 vs +70.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Hanbrücken: +4/turn
  - ship Flax Wyrm -> Angefont: +1/turn
  - spinnery 1 1.65 -> 1.33: +6/turn
  - net maker 0.00 -> 0.29: +3/turn
  - retting pit 1 0.91 -> 0.84: +0/turn
  - flax farm 1 4.64 -> 4.18: +5/turn
  - weavery 1 0.50 -> 0.41: -6/turn
  - sewing shop 1 0.30 -> 0.24: -11/turn
  - mansion 1 0.00 -> 0.54: -116/turn
- Model check over the last 60 turns: predicted +105/turn for the settings we ran, real -26/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.96, garments 19.30, nets 30.20, beer 3.19, timber 3.38, prestige 64.39, cash 0.00
- Orders it would set: candles buy 2 (v2 None); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 6 (v2 0); labour buy 29 (v2 17); light armour buy 1 (v2 None); pasties sell 1 (v2 none)
- Ship linen snake: Grandgues -> Hanbrücken (+4/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Angefont (+1/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1791 coin: +1/turn, payback 1414 turns, doesn't pay yet (materials thin at home: limestone)

## Chain sizing

Mode HOLD, garments sold 10.4/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 414 (+125 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 3.87 |
| ret | 3 | 0.91 | 0.77 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 141/77, thread 1050/228, cloth 72/128

## Self-diagnosis

- R1: beer slot dry: 0.0 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy none, home ask 3.8 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 9 @ 3.86 (ask 3.8, cap 5.7))
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 3.66; ask over the cap 2.1 (60 coin per prestige)
