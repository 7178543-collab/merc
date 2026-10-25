# v2 shadow report

Turn 13530, 2026-10-25 03:52. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 2,158, prestige 3,570 (450 free, -0.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 7 | 0 | 0 | min_holding 60, sell 56, sell @ 2.98 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 10 | 3 | 6 | 0 | 0 | buy @ 2.4; sell 1, sell @ 1.75 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 7, sell @ 17.8 |
| grain | 33 | 29 | 29 | 0 | 0 | stop 115, buy 29, buy @ 3.7 |
| labour | 12 | 1 | 494 | 0 | 7 | buy 12, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 15 | 0 | 0 | 0 | 0 | min_holding 15, sell 12, sell @ 34 |
| porterage | 11 | 13 | 11 | 0 | 2 | buy 11, buy @ 1.1 |

**2 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: sewing shop 1 ran short of cloth (no buy order); labour need rises ~32/turn when they restart -> v2: add a cloth buy
- **varnish**: net maker152202386007001 ran short of varnish (buy is live (1 @ 17.1), but the home ask 19.30 is above it); labour need rises ~12/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.6 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 43

## Notes

- labour: projection runs 138 over real use lately; planning 494, not 589

## Prestige spending, cheapest coin per prestige first

871 turns left: prestige gained now converts 98.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 46.5 | 46.5 | running |
| hold banquet 4 (pies) | mansion | 18 | 49.3 | 49.3 | thin at home: hop beer, wine, pies |
| hold banquet 3 (pies) | mansion | 8 | 49.4 | 49.4 | thin at home: hop beer, pies |
| hold banquet 2 (pies) | mansion | 7 | 50.1 | 50.1 | thin at home: wine, pies |
| jousting 3 | arena | 230 | 52.7 | 52.8 | needs a arena (build cost 24,545); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 52.9 | 52.9 | thin at home: wine, hop beer, stockfish |
| hold prayer 2 | chapel | 13 | 50.5 | 53.4 | needs a chapel (build cost 31,276); thin at home: furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 53.9 | 53.9 | thin at home: wine |
| hold banquet 3 (fish) | mansion | 7.6 | 54.0 | 54.0 | thin at home: hop beer |
| hold sermon 2 (candles) | church | 31 | 51.7 | 54.3 | needs a church (build cost 64,207); thin at home: jewellery, candles, furniture |
| hold banquet 2 (meat) | mansion | 6.8 | 54.5 | 54.5 | thin at home: wine |
| hold banquet 3 (meat) | mansion | 7.6 | 54.5 | 54.5 | thin at home: hop beer |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only 7 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only 1 a turn after crew: ship stays at 0
- best towns now: Vauxvais +28, Marmont +25, Dortdorf +21, Hanbrücken +16, Brunnham +16
- Vauxvais would trade: candles buy 1 @ 66.0, furniture buy 1 @ 13.1, pasties buy 2 @ 11.9, rope sell 3 @ 77.5; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~97 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Fontaux | 411 | 0.11 | 0.90 (87/turn) | thread 63 (4.5->5.65), gold ore 1 (147->155.8), firewood 19 (1.84->5.32), lathes 1 (201.6->209) | candles 1 (67.2->76), cheese 8 (5.41->5.56), cloth 1 (7.25->7.7), furniture 1 (13.76->14.5) | +105 |
| Neuborn | 780 | 0.20 | 0.50 (48/turn) | gold ore 1 (147->171), beer 55 (3.14->3.91), charcoal 11 (1.96->4.75), garments 3 (17.8->21.09) | gears 1 (56.18->61.75), cheese 8 (4.83->5.56), flax fibres 17 (5.06->5.6) | +79 |
| Grandgues | 152 | 0.04 | 0.60 (58/turn) | firewood 29 (1.84->4.31), timber 20 (7.51->9.03), charcoal 11 (1.96->3.52), bricks 6 (4.89->5.84) | candles 1 (69.3->76), mouldboards 2 (31.5->32.49), furniture 1 (13.65->14.5), flax plants 3 (1.49->1.62) | +79 |
| Bordetes | 831 | 0.22 | 0.30 (29/turn) | raw cloth 7 (7.51->11.97), rope 3 (69.5->71.72), gold ore 1 (147->152), salt 2 (4.56->6.74) | candles 1 (69.3->76), cloth 11 (7.25->7.7), garments 2 (19.11->19.4) | +55 |
| Marmont | 638 | 0.17 | 0.30 (29/turn) | rope 3 (69.5->75.52), beer 55 (3.14->3.55), malt 1 (5.62->7.6), garments 3 (17.8->18.34) | ploughs 3 (67.2->72.2), candles 1 (69.3->76), cloth 11 (7.51->7.7), furniture 1 (13.65->14.5) | +40 |

**Best:** Fontaux at about +105 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 27.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 55 @ min 2.98 | goal planner: sells 55 at 2.98 (v2 had 55 at 3.38) |
| cured meat | 1 @ 29.0, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 1) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 0 @ 2.4, stop 13 | 1 @ min 1.75 | uses 6.3/turn (brewery 1, household upkeep), makes 6.5, holds 10 |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| grain | 28 @ 3.7, stop 109 |  | goal planner: buys 28 a turn for today's rates, keeps up to 109 (v2 had 58) |
| labour | 12 @ 2.2, stop - |  | goal planner: buys 12 for today's rates (v2 had 0) |
| light armour | 1 @ 86, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 9 @ min 34 | goal planner: sells 9 at 34 (v2 had 9 at 34.6) |
| pasties | 3 @ 14.5, stop 11 |  | goal planner: buys 3 a turn for today's rates, keeps up to 11 (v2 had 4) |
| porterage | 11 @ 1.1, stop - |  | goal planner: buys 11 for today's rates (v2 had 11) |
| rope |  | 3 @ min 67.5 | makes 2.0, uses 0.0, holds 19 (keeps 0): sells the surplus + 1/turn of the excess |
| thread |  | 12 @ min 4.1 | goal planner: sells 12 a turn at 4.1, keeps 206 (no one offered it) |
| tools | 2 @ 6.2, stop 11 |  | uses 1.4/turn (retting pit 1), makes 0.0, holds 199 = 146.5 turns |
| varnish | 1 @ 20.2, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| wax | 1 @ 20.8, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 18.5k (cash + stock at home prices); +115/turn over 6 turns, +56/turn over 24 turns.
- Limits: cash flow >= +77/turn, prestige >= -0.62/turn (values are after 240 tax a turn).
- Today's settings: value +20/turn, cash +135/turn, prestige -0.60/turn.
- Plan: value +52/turn, cash +77/turn, prestige -0.62/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +303 vs -59, +514 vs -53, +351 vs +99.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4, garments 0.3, nets 0.0, rope 0.1.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Brunnham: +1/turn
  - ship Flax Wyrm -> Magdeach: +4/turn
  - net maker 0.50 -> 0.71: +5/turn
  - logging camp w/ tool 5.00 -> 4.71: +0/turn
  - weavery 1 0.22 -> 0.15: -5/turn
  - sewing shop 1 0.21 -> 0.05: -2/turn
  - flax farm 1 3.55 -> 4.79: +12/turn
  - retting pit 1 0.62 -> 0.84: -5/turn
  - spinnery 1 1.28 -> 1.72: +5/turn
  - ropewalk 1 0.50 -> 0.00: -82/turn
- Model check over the last 36 turns: predicted +114/turn for the settings we ran, real +63/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.65, thread 4.07, cloth 6.55, flax fibres 4.67, garments 19.02, nets 30.19, beer 2.94, timber 2.98, prestige 58.10, cash 0.07
- Orders it would set: grain buy 28 (v2 58); labour buy 12 (v2 0); light armour buy 1 (v2 None); pasties buy 3 (v2 4); thread sell 12 (v2 none)
- Recipe: ropewalk 1 make rope 1 -> make rope 2 at 0.62, worth +20/turn.
- Ship linen snake: Grandgues -> Brunnham (+5/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Magdeach (+4/turn over staying).
- Management: ~13.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +78/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
- Trim: donate quarry 1: +19/turn (tax 20 saved).
- Trim: donate logging camp w/ tool: +18/turn (tax 20 saved).
- Trim: donate weavery 1: +11/turn (tax 18 saved).

## Chain sizing

Mode HOLD, garments sold 7.7/turn (+0.0 exported); plan makes 30.3 garments a turn.
Labour: own 500, everything else 409, chain may buy 350 -> chain allowance 441, chain plan 440 (+238 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 3.55 | 5.39 |
| ret | 3 | 0.62 | 0.96 |
| spin | 4 | 1.28 | 1.97 |
| weave | 3 | 0.22 | 1.19 |
| sew | 2 | 0.21 | 0.74 |

Buffers: flax fibres 36/87, thread 823/257, cloth 0/119
- chain plan needed 465 labour, budget left 441: cut to 441 (sewing capped at 0.74)

## Self-diagnosis

- R5: varnish buy not filling: bid 17.1 under the home ask 19.3 for 6 turns, bought 0.0 of 1, 0.0 held (0.0 turns) (held back: ship trade good (v2 ships own it): finding only)
