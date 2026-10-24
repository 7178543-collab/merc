# v2 shadow report

Turn 13515, 2026-10-24 12:27. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 1,263, prestige 3,581 (461 free, -0.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 7 | 0 | 0 | min_holding 60, sell 82, sell @ 2.98 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 8 | 0 | 6 | 2 | 0 | stop 6, buy 2, buy @ 2.4; sell 1, sell @ 1.71 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 52 | 0 | 2 | 0 | 0 | min_holding 30, sell 10, sell @ 17.8 |
| grain | 95 | 38 | 27 | 0 | 0 | stop 150, buy 38, buy @ 3.7 |
| labour | 51 | 73 | 536 | 0 | 37 | buy 51, buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 15 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34 |
| porterage | 12 | 12 | 12 | 0 | 0 | buy 12, buy @ 1.1 |

**3 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), home ask 1.52 x3, yet 0 bought last turn); labour need rises ~82/turn when they restart -> v2: find out why the buy isn't filling
- **varnish**: net maker152202386007001 ran short of varnish (no buy order); labour need rises ~6/turn when they restart -> v2: add a varnish buy
- **varnish**: needed (0.1/turn) but there is NO buy order, stock 0.0 -> v2: add buy 1

## Waste (money lost now)

- **labour**: 37 labour expired last turn (~55 coin): holding 51 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.2 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 57
- **tar**: home ask 12.10 is above our ceiling 11.00 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 536, not 626
- labour expiry guard: 37 bought labour expired last turn, buy 36 (not 36) this turn

## Prestige spending, cheapest coin per prestige first

886 turns left: prestige gained now converts 98.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 44.7 | 44.7 | running |
| hold banquet 4 (pies) | mansion | 18 | 49.0 | 49.0 | thin at home: hop beer, wine, ham, pies |
| hold banquet 2 (pies) | mansion | 7 | 50.6 | 50.6 | thin at home: wine, pies |
| hold banquet 3 (pies) | mansion | 8 | 50.7 | 50.7 | thin at home: hop beer, pies |
| hold banquet 4 | mansion | 17.5 | 52.1 | 52.1 | thin at home: wine, hop beer, ham, stockfish |
| jousting 3 | arena | 230 | 51.9 | 52.1 | needs a arena (build cost 23,963); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold prayer 2 | chapel | 13 | 49.9 | 52.7 | needs a chapel (build cost 30,558); thin at home: furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 52.8 | 52.8 | thin at home: wine |
| hold banquet 2 (meat) | mansion | 6.8 | 53.6 | 53.6 | thin at home: wine |
| hold banquet 3 (fish) | mansion | 7.6 | 53.9 | 53.9 | thin at home: hop beer |
| hold sermon 2 (candles) | church | 31 | 51.3 | 53.9 | needs a church (build cost 64,879); thin at home: jewellery, furniture |
| hold banquet 1 (fish) | mansion | 4.2 | 54.2 | 54.2 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only -7 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -8 a turn after crew: ship stays at 0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~94 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Birkeningen | 1006 | 0.30 | 0.50 (47/turn) | beer 50 (2.98->4.89), garments 5 (17.8->25.27), dyed cloth 2 (11.76->17.48), wine 5 (5.72->7.22) | gears 2 (60.38->61.27) | +119 |
| Fontaux | 411 | 0.10 | 0.30 (28/turn) | thread 65 (4.12->4.94), charcoal 12 (1.9->3.5), flax fibres 2 (5.1->7.74), iron ore 2 (4.87->7.17) | grindstones 1 (210->222.3), furniture 1 (14.38->14.8) | +74 |
| Neuborn | 780 | 0.20 | 0.50 (47/turn) | beer 51 (2.98->4.22), acid 1 (109.2->120.65), charcoal 12 (1.9->4.16), yarn 5 (4.56->5.27) | tools 1 (4.62->4.98) | +65 |
| Hanbrücken | 531 | 0.13 | 0.50 (47/turn) | looms 1 (661.5->693.5), timber 17 (6.56->9.26), rope 2 (73->76.95), lead ore 10 (7.19->8.46) | lathes 1 (197.4->205.2), furniture 1 (13.65->14.8), tools 1 (4.73->4.98) | +63 |
| Dedlowe | 1146 | 0.37 | 0.10 (9/turn) | windows 1 (598.5->655.5), wine 3 (5.72->7.03) | blades 1 (14.7->15.86) | +53 |

**Best:** Birkeningen at about +119 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 25.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| candles | 2 @ 66, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 7 | goal planner: sells 1 a turn at 7, keeps 33 (no one offered it) |
| cured meat | 1 @ 29.0, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 1) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 6 | 4 @ min 1.73 | goal planner: buys 2 a turn for today's rates, keeps up to 6 (v2 had 2) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 8 @ min 17.8 | goal planner: sells 8 at 17.8 (v2 had 8 at 20.0) |
| grain | 39 @ 3.7, stop 156 |  | goal planner: buys 39 a turn for today's rates, keeps up to 156 (v2 had 44) |
| labour | 73 @ 2.2, stop - |  | goal planner: buys 73 for today's rates (v2 had 36) |
| light armour | 1 @ 85.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 9 @ min 34.0 |  |
| pasties | 3 @ 14.5, stop 11 |  | goal planner: buys 3 a turn for today's rates, keeps up to 11 (v2 had 4) |
| porterage | 12 @ 1.1, stop - |  | goal planner: buys 12 for today's rates (v2 had 12) |
| rope |  | 5 @ min 71.0 | makes 2.9, uses 0.0, holds 30 (keeps 0): sells the surplus + 2/turn of the excess |
| tar | 2 @ 11.0, stop 3 |  | uses 0.6/turn (ropewalk 1), makes 0.0, holds 0 = 0.0 turns |
| thread |  | 8 @ min 4.12 | goal planner: sells 8 a turn at 4.12, keeps 225 (no one offered it) |
| tools | 2 @ 6.2, stop 13 |  | uses 1.5/turn (retting pit 1), makes 0.0, holds 199 = 131.1 turns |
| varnish | 1 @ 17.1, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| wax | 1 @ 20.4, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had None) |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 17.9k (cash + stock at home prices); +95/turn over 6 turns, +67/turn over 24 turns.
- Limits: cash flow >= +114/turn, prestige >= -0.67/turn (values are after 240 tax a turn).
- Today's settings: value +21/turn, cash +35/turn, prestige -0.66/turn - breaks the cash floor.
- Plan: value +69/turn, cash +114/turn, prestige -0.67/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -10 vs +142, -127 vs +35, +24 vs +5.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4, garments 0.5, nets 0.0, rope 0.1.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Essenbrucke: +2/turn
  - ship Flax Wyrm -> Brunnham: +0/turn
  - net maker 0.25 -> 0.56: +18/turn
  - logging camp w/ tool 5.00 -> 0.00: +4/turn
  - logging camp w/ tool [split timber 1] 0.00 -> 3.12: +3/turn
  - retting pit 1 0.76 -> 0.86: +0/turn
  - flax farm 1 4.60 -> 4.90: +2/turn
  - spinnery 1 1.70 -> 1.77: +0/turn
  - weavery 1 0.23 -> 0.33: -5/turn
  - ropewalk 1 0.64 -> 0.00: -69/turn
- Model check over the last 21 turns: predicted +146/turn for the settings we ran, real +77/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.50, thread 3.75, cloth 6.00, flax fibres 4.41, garments 17.37, nets 27.66, beer 2.62, timber 5.25, prestige 54.63, cash 0.01
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); grain buy 39 (v2 44); labour buy 73 (v2 36); light armour buy 1 (v2 None); pasties buy 3 (v2 4); thread sell 8 (v2 none); wax buy 1 (v2 None)
- Recipe: logging camp w/ tool cut firewood 1 -> split timber 1 at 3.12, worth +3/turn.
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.64, worth +25/turn.
- Ship linen snake: Grandgues -> Essenbrucke (+3/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Brunnham (+1/turn over staying).
- Management: ~13.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +75/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
- Trim: donate quarry 1: +19/turn (tax 20 saved).
- Trim: donate logging camp w/ tool: +17/turn (tax 20 saved).
- Trim: donate weavery 1: +12/turn (tax 18 saved).

## Chain sizing

Mode HOLD, garments sold 5.1/turn (+0.0 exported); plan makes 0.0 garments a turn.
Labour: own 500, everything else 432, chain may buy 0 -> chain allowance 68, chain plan 109 (-131 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.60 | 2.47 |
| ret | 3 | 0.76 | 0.44 |
| spin | 4 | 1.70 | 0.91 |
| weave | 3 | 0.23 | 0.00 |
| sew | 2 | 0.14 | 0.00 |

Buffers: flax fibres 36/51, thread 649/151, cloth 34/0
- chain plan needed 109 labour, budget left 68: cut to 109

## Self-diagnosis

Nothing found this run.
