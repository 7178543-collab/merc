# v2 shadow report

Turn 13511, 2026-10-24 08:55. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 1,098, prestige 3,583 (463 free, -0.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 71 | 0 | 7 | 0 | 0 | min_holding 60, sell 73, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 13 | 0 | 8 | 0 | 0 | stop 15, buy 1, buy @ 2.4; sell 1, sell @ 1.66 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 79 | 0 | 2 | 0 | 0 | min_holding 30, sell 3, sell @ 17.9 |
| grain | 91 | 37 | 41 | 0 | 0 | stop 148, buy 37, buy @ 3.7 |
| labour | 72 | 65 | 545 | 0 | 20 | buy 72, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 15 | 0 | 0 | 0 | 0 | min_holding 15, sell 11, sell @ 34 |
| porterage | 12 | 13 | 12 | 0 | 1 | buy 12, buy @ 1.1 |

**2 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **varnish**: net maker152202386007001 ran short of varnish (no buy order); labour need rises ~6/turn when they restart -> v2: add a varnish buy
- **varnish**: needed (0.1/turn) but there is NO buy order, stock 0.0 -> v2: add buy 1

## Waste (money lost now)

- **labour**: 20 labour expired last turn (~29 coin): holding 72 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.5 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 57

## Notes

- labour: projection runs 100 over real use lately; planning 545, not 645

## Prestige spending, cheapest coin per prestige first

890 turns left: prestige gained now converts 98.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 44.4 | 44.4 | running |
| hold banquet 4 (pies) | mansion | 18 | 46.8 | 46.8 | thin at home: hop beer, wine, pies |
| hold banquet 3 (pies) | mansion | 8 | 49.4 | 49.4 | thin at home: hop beer, pies |
| hold banquet 4 | mansion | 17.5 | 49.5 | 49.5 | thin at home: wine, hop beer, ham, stockfish |
| hold banquet 2 (pies) | mansion | 7 | 50.4 | 50.4 | thin at home: wine, pies |
| jousting 3 | arena | 230 | 51.7 | 51.8 | needs a arena (build cost 24,277); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold prayer 2 | chapel | 13 | 49.4 | 52.2 | needs a chapel (build cost 30,705); thin at home: furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 52.4 | 52.4 | thin at home: wine, cured fish |
| hold sermon 2 (candles) | church | 31 | 49.8 | 52.4 | needs a church (build cost 64,251); thin at home: furniture |
| hold banquet 3 (fish) | mansion | 7.6 | 52.5 | 52.5 | thin at home: hop beer, cured fish |
| hold banquet 2 (meat) | mansion | 6.8 | 53.1 | 53.1 | thin at home: wine, cured meat |
| hold banquet 3 (meat) | mansion | 7.6 | 53.1 | 53.1 | thin at home: hop beer, cured meat |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only 11 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only 11 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~92 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Nürnnieder | 520 | 0.13 | 0.10 (9/turn) | thread 56 (3.35->5.13), iron ore 2 (4.85->7.6), garments 4 (17.9->18.43), cloth 1 (7->7.36) | beer 6 (2.86->3.5), flax plants 2 (1.43->2.47), yarn 2 (4.03->4.16) | +102 |
| Birkeningen | 1006 | 0.30 | 0.70 (65/turn) | beer 50 (3.06->4.67), charcoal 12 (1.86->5.75), garments 4 (17.9->21.47), thread 4 (3.35->4.48) | flax plants 3 (1.68->2.47), gears 2 (59.85->60.8) | +90 |
| Caillechâtel | 488 | 0.12 | 0.20 (18/turn) | beer 25 (3.06->5.75), thread 31 (3.35->3.86), nets 6 (35->35.72) | flax fibres 9 (4.91->5.85), flax plants 6 (1.26->2.47), medicine 1 (124.95->128.25), furniture 1 (13.23->14.1) | +88 |
| Hanstein | 380 | 0.09 | 0.10 (9/turn) | thread 65 (3.35->3.99), logs 1 (3.61->5.65) | flax fibres 28 (4.75->5.85), flax plants 6 (1.19->2.47), cheese 8 (5.3->5.46), tiles 2 (3.09->4.24) | +69 |
| Dedlowe | 1146 | 0.37 | 0.10 (9/turn) | windows 1 (603.75->655.5), wine 7 (5.57->7.08), thread 6 (3.35->4.84) | flax plants 2 (1.42->2.47), lathes 1 (214.2->218.5), blades 1 (14.91->15.58) | +67 |

**Best:** Nürnnieder at about +102 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 26.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 82 @ min 3.06 | goal planner: sells 82 at 3.06 (v2 had 82 at 3.38) |
| candles | 2 @ 68.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 2 @ min 7 | goal planner: sells 2 a turn at 7, keeps 0 (no one offered it) |
| cured meat | 1 @ 29.0, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 2) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 6 | 1 @ min 1.66 | goal planner: buys 2 a turn for today's rates, keeps up to 6 (v2 had 2) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 14.4, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 2 @ min 17.9 | goal planner: sells 2 a turn at 17.9, keeps 30 (no one offered it) |
| grain | 40 @ 3.7, stop 158 |  | goal planner: buys 40 a turn for today's rates, keeps up to 158 (v2 had 79) |
| labour | 52 @ 2.2, stop - |  | goal planner: buys 52 for today's rates (v2 had 45) |
| light armour | 1 @ 82.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 9 @ min 34.0 |  |
| pasties | 3 @ 14.5, stop 11 |  | goal planner: buys 3 a turn for today's rates, keeps up to 11 (v2 had 4) |
| porterage | 12 @ 1.1, stop - |  | goal planner: buys 12 for today's rates (v2 had 12) |
| rope |  | 5 @ min 71.0 | makes 2.9, uses 0.0, holds 24 (keeps 0): sells the surplus + 2/turn of the excess |
| tar | 1 @ 11.0, stop 3 |  | uses 0.6/turn (ropewalk 1), makes 0.0, holds 2 = 3.9 turns |
| thread |  | 5 @ min 4.34 | goal planner: sells 5 a turn at 4.34, keeps 225 (no one offered it) |
| tools | 2 @ 6.2, stop 13 |  | uses 1.5/turn (retting pit 1), makes 0.0, holds 200 = 131.1 turns |
| varnish | 1 @ 17.1, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| wax | 1 @ 22.2, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had None) |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 17.5k (cash + stock at home prices); +98/turn over 6 turns, +64/turn over 24 turns.
- Limits: cash flow >= +121/turn, prestige >= -0.68/turn (values are after 240 tax a turn).
- Today's settings: value +23/turn, cash +35/turn, prestige -0.67/turn - breaks the cash floor.
- Plan: value +101/turn, cash +121/turn, prestige -0.68/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +108 vs +5, -62 vs +118, -10 vs +142.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4, garments 0.5, nets 0.0, rope 0.1.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Rouhomme: +2/turn
  - ship Flax Wyrm -> Heidlowe: +1/turn
  - sewing shop 1 0.00 -> 0.14: +28/turn
  - net maker 0.25 -> 0.62: +26/turn
  - logging camp w/ tool [split timber 1] 0.00 -> 5.42: +7/turn
  - retting pit 1 0.76 -> 0.82: +3/turn
  - logging camp w/ tool 5.00 -> 0.00: +3/turn
  - ropewalk 1 0.64 -> 0.00: -81/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.65: +85/turn
- Model check over the last 17 turns: predicted +154/turn for the settings we ran, real +76/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.50, thread 3.75, cloth 6.00, flax fibres 4.41, garments 17.37, nets 27.76, beer 2.62, timber 5.25, prestige 52.81, cash 0.01
- Orders it would set: candles buy 2 (v2 None); cloth sell 2 (v2 none); cured meat buy 1 (v2 2); furniture buy 2 (v2 None); garments sell 2 (v2 none); grain buy 40 (v2 79); labour buy 52 (v2 45); light armour buy 1 (v2 None); pasties buy 3 (v2 4); thread sell 5 (v2 none)
- Recipe: logging camp w/ tool cut firewood 1 -> split timber 1 at 5.42, worth +7/turn.
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.65, worth +29/turn.
- Ship linen snake: Grandgues -> Rouhomme (+2/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Heidlowe (+1/turn over staying).
- Management: ~13.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +74/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
- Trim: donate quarry 1: +20/turn (tax 20 saved).
- Trim: donate weavery 1: +15/turn (tax 18 saved).
- Trim: donate logging camp w/ tool: +13/turn (tax 20 saved).
- Trim: donate sewing shop 1: +10/turn (tax 12 saved).

## Chain sizing

Mode HOLD, garments sold 2.3/turn (+0.0 exported); plan makes 0.0 garments a turn.
Labour: own 500, everything else 432, chain may buy 0 -> chain allowance 68, chain plan 109 (-110 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.60 | 2.47 |
| ret | 3 | 0.76 | 0.44 |
| spin | 4 | 1.70 | 0.91 |
| weave | 3 | 0.23 | 0.00 |
| sew | 2 | 0.00 | 0.00 |

Buffers: flax fibres 45/51, thread 611/151, cloth 38/0
- chain plan needed 109 labour, budget left 68: cut to 109

## Self-diagnosis

Nothing found this run.
