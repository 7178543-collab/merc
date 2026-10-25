# v2 shadow report

Turn 13532, 2026-10-25 05:02. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 2,894, prestige 3,568 (448 free, -0.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 7 | 0 | 0 | min_holding 60, sell 55, sell @ 2.98 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 9 | 0 | 6 | 0 | 0 | buy @ 2.4; sell 1, sell @ 1.75 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 7, sell @ 17.8 |
| grain | 32 | 28 | 29 | 0 | 0 | stop 109, buy 28, buy @ 3.7 |
| labour | 6 | 6 | 501 | 0 | 5 | buy 6, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34 |
| porterage | 11 | 11 | 11 | 0 | 0 | buy 11, buy @ 1.1 |

**1 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: sewing shop 1 ran short of cloth (no buy order); labour need rises ~32/turn when they restart -> v2: add a cloth buy

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.6 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 43

## Notes

- labour: projection runs 100 over real use lately; planning 502, not 601

## Prestige spending, cheapest coin per prestige first

869 turns left: prestige gained now converts 98.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 46.5 | 46.5 | running |
| hold banquet 3 (pies) | mansion | 8 | 49.9 | 49.9 | thin at home: hop beer, pies |
| hold banquet 4 (pies) | mansion | 18 | 50.3 | 50.3 | thin at home: hop beer, wine, pies |
| hold banquet 2 (pies) | mansion | 7 | 51.5 | 51.5 | thin at home: wine, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 52.3 | 52.3 | thin at home: hop beer, cured fish |
| jousting 3 | arena | 230 | 52.6 | 52.7 | needs a arena (build cost 24,397); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 53.1 | 53.1 | thin at home: wine, cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 53.7 | 53.7 | thin at home: cured fish |
| hold banquet 4 | mansion | 17.5 | 53.8 | 53.8 | thin at home: wine, hop beer, stockfish |
| hold banquet 3 (meat) | mansion | 7.6 | 54.3 | 54.3 | thin at home: hop beer |
| hold banquet 2 (meat) | mansion | 6.8 | 55.3 | 55.3 | thin at home: wine |
| hold prayer 2 | chapel | 13 | 53.5 | 56.5 | needs a chapel (build cost 30,776); thin at home: garments, furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: candles buy 1 @ 67.0, furniture buy 1 @ 13.2, rope sell 2 @ 80.0; crew 0.1; est +23 a turn
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only 9 a turn after crew: ship stays at 0
- best towns now: Etallaen +24, Grandgues +23, Vauxvais +21, Hanbrücken +18
- Etallaen would trade: candles buy 1 @ 62.0, rope sell 2 @ 78.5; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~96 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.60 (58/turn) | firewood 29 (1.84->4.22), timber 17 (6.77->8.84), rope 2 (68.5->78.38), charcoal 11 (2.01->3.78) | candles 1 (69.3->77.5), mouldboards 1 (31.5->33.25), furniture 1 (13.65->14.6), flax plants 1 (1.33->1.43) | +106 |
| Bordetes | 831 | 0.22 | 0.30 (29/turn) | raw cloth 15 (7.4->13.01), gold ore 1 (143.85->153.9), rope 2 (68.5->70.3), charcoal 11 (2.01->3.84) | candles 1 (69.3->77.5), garments 2 (19.11->19.4), mouldboards 1 (32.55->33.25), tools 1 (4.47->4.82) | +103 |
| Neuborn | 780 | 0.20 | 0.70 (67/turn) | gold ore 1 (143.85->193.8), garments 3 (17.9->23.18), charcoal 11 (2.01->4.75), cookware 5 (23.52->25.46) | mouldboards 1 (24.36->33.25), flax fibres 15 (5.06->5.5), gears 2 (60.9->61.75) | +100 |
| Darmwald | 1022 | 0.32 | 0.20 (19/turn) | grindstones 1 (258.3->364.8), potash 1 (14.38->17.29), malt 1 (5.72->6.89), rope 2 (68.5->69.35) | candles 1 (72.45->77.5) | +98 |
| Fontaux | 411 | 0.10 | 0.80 (77/turn) | cookware 5 (23.52->26.22), gold ore 1 (143.85->154.85), jewellery 1 (110.25->118.75), firewood 19 (1.84->5.32) | candles 1 (69.3->77.5), cheese 9 (5.25->5.56), furniture 1 (13.86->14.6) | +62 |

**Best:** Grandgues at about +106 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 28.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 55 @ min 2.98 | goal planner: sells 55 at 2.98 (v2 had 55 at 3.38) |
| cured meat | 1 @ 29.0, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 2) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 0 @ 2.4, stop 13 | 1 @ min 1.75 | uses 6.3/turn (brewery 1, household upkeep), makes 6.5, holds 9 |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 14.2, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| grain | 27 @ 3.7, stop 108 |  | goal planner: buys 27 a turn for today's rates, keeps up to 108 (v2 had 58) |
| labour | 12 @ 2.2, stop - |  | goal planner: buys 12 for today's rates (v2 had 2) |
| light armour | 1 @ 86.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 12 @ min 34 | goal planner: sells 12 at 34 (v2 had 12 at 34.6) |
| pasties | 3 @ 14.5, stop 11 |  | goal planner: buys 3 a turn for today's rates, keeps up to 11 (v2 had 4) |
| porterage | 11 @ 1.1, stop - |  | goal planner: buys 11 for today's rates (v2 had 11) |
| rope |  | 3 @ min 67.5 |  |
| thread |  | 3 @ min 4.5 | goal planner: sells 3 a turn at 4.5, keeps 206 (no one offered it) |
| tools | 2 @ 6.2, stop 13 |  | uses 1.5/turn (net maker152202386007001, retting pit 1), makes 0.0, holds 199 = 129.9 turns |
| varnish | 1 @ 20.4, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| wax | 1 @ 21.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 18.5k (cash + stock at home prices); +117/turn over 6 turns, +51/turn over 24 turns.
- Limits: cash flow >= +46/turn, prestige >= -0.62/turn (values are after 240 tax a turn).
- Today's settings: value +30/turn, cash +130/turn, prestige -0.60/turn.
- Plan: value +60/turn, cash +74/turn, prestige -0.62/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +303 vs -59, +514 vs -53, +351 vs +99.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4, garments 0.3, nets 0.0, rope 0.1.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Magdeach: +10/turn
  - net maker 0.50 -> 0.69: +3/turn
  - sewing shop 1 0.21 -> 0.10: +9/turn
  - ropewalk 1 0.50 -> 0.80: +2/turn
  - logging camp w/ tool 5.00 -> 4.71: +0/turn
  - flax farm 1 3.55 -> 5.43: -17/turn
  - retting pit 1 0.62 -> 0.95: -4/turn
  - spinnery 1 1.28 -> 1.96: +31/turn
- Model check over the last 37 turns: predicted +109/turn for the settings we ran, real +62/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.55, thread 3.82, cloth 6.15, flax fibres 4.40, garments 17.85, nets 28.40, beer 2.76, timber 2.88, prestige 54.48, cash 0.00
- Orders it would set: cured meat buy 1 (v2 2); furniture buy 2 (v2 None); grain buy 27 (v2 58); labour buy 12 (v2 2); light armour buy 1 (v2 None); pasties buy 3 (v2 4); thread sell 3 (v2 none)
- Ship linen snake: Grandgues -> Magdeach (+3/turn over staying).
- Ship Flax Wyrm: stays on Caillechâtel (worth +16/turn).
- Management: ~13.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +78/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
- Trim: donate quarry 1: +19/turn (tax 20 saved).
- Trim: donate logging camp w/ tool: +18/turn (tax 20 saved).

## Chain sizing

Mode HOLD, garments sold 7.3/turn (+0.0 exported); plan makes 30.3 garments a turn.
Labour: own 500, everything else 409, chain may buy 350 -> chain allowance 441, chain plan 440 (+238 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 3.55 | 5.39 |
| ret | 3 | 0.62 | 0.96 |
| spin | 4 | 1.28 | 1.97 |
| weave | 3 | 0.22 | 1.19 |
| sew | 2 | 0.21 | 0.74 |

Buffers: flax fibres 35/87, thread 798/257, cloth 0/119
- chain plan needed 465 labour, budget left 441: cut to 441 (sewing capped at 0.74)

## Self-diagnosis

Nothing found this run.
