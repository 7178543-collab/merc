# v2 shadow report

Turn 13534, 2026-10-25 07:52. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 3,918, prestige 3,567 (447 free, -0.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 7 | 0 | 0 | min_holding 60, sell 55, sell @ 2.98 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 8 | 0 | 6 | 0 | 0 | buy @ 2.4; sell 1, sell @ 1.75 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 2, sell @ 17.9 |
| grain | 30 | 27 | 29 | 0 | 0 | stop 109, buy 28, buy @ 3.7 |
| labour | 0 | 0 | 491 | 0 | 9 | buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 15 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34 |
| porterage | 11 | 11 | 11 | 0 | 0 | buy 11, buy @ 1.1 |

**2 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.5 turns (holds 4, next step uses 7/turn) -> v2: check the step that makes it
- **wax**: net maker152202386007001 ran short of wax (buy is live (1 @ 21), home ask 20.20 x7, yet 0 bought last turn); labour need rises ~12/turn when they restart -> v2: find out why the buy isn't filling

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.6 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 43

## Notes

- labour: projection runs 100 over real use lately; planning 494, not 594

## Prestige spending, cheapest coin per prestige first

867 turns left: prestige gained now converts 98.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.4 | 47.4 | running |
| hold banquet 3 (pies) | mansion | 8 | 49.9 | 49.9 | thin at home: hop beer, pies, candles |
| hold banquet 4 (pies) | mansion | 18 | 50.1 | 50.1 | thin at home: hop beer, wine, pies, candles |
| hold banquet 2 (pies) | mansion | 7 | 51.1 | 51.1 | thin at home: wine, pies, candles |
| jousting 3 | arena | 230 | 52.6 | 52.7 | needs a arena (build cost 24,379); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 53.6 | 53.6 | thin at home: wine, hop beer, stockfish, candles |
| hold banquet 3 (fish) | mansion | 7.6 | 54.1 | 54.1 | thin at home: hop beer |
| hold banquet 3 (meat) | mansion | 7.6 | 54.2 | 54.2 | thin at home: hop beer |
| hold banquet 2 (fish) | mansion | 6.8 | 54.6 | 54.6 | thin at home: wine |
| hold banquet 2 (meat) | mansion | 6.8 | 54.7 | 54.7 | thin at home: wine |
| hold prayer 2 | chapel | 13 | 52.0 | 54.9 | needs a chapel (build cost 30,516); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 53.0 | 55.6 | needs a church (build cost 62,904); thin at home: candles, furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only -2 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -3 a turn after crew: ship stays at 0
- best towns now: Hanbrücken +18
- Hanbrücken would trade: pasties buy 2 @ 9.9, rope sell 2 @ 80.5; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~98 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Heilegg | 826 | 0.22 | 0.10 (10/turn) | grindstones 1 (256.2->347.7) | premium cheese 1 (28.56->37.24), potash 2 (16.59->18.52), pasties 2 (11.87->13.5), flax fibres 4 (5.17->5.8) | +99 |
| Grandgues | 152 | 0.04 | 0.60 (59/turn) | firewood 29 (1.84->4.31), charcoal 11 (2.01->4.48), wrought iron 7 (14.38->15.67), bricks 6 (4.43->5.84) | premium cheese 1 (24.36->37.24), mouldboards 2 (31.71->34.58), pasties 2 (12.08->13.5), potash 2 (17.43->18.52) | +92 |
| Fontaux | 411 | 0.11 | 0.80 (78/turn) | cheese 10 (6.14->9.79), cookware 4 (23.52->25.84), firewood 19 (1.84->5.32), charcoal 11 (2.01->3.15) | premium cheese 1 (27.51->37.24), mouldboards 2 (33.81->34.58) | +64 |
| Rouhomme | 368 | 0.10 | 0.70 (69/turn) | bread 142 (2.16->2.75), beer 55 (3.04->3.42), charcoal 11 (2.01->3.31), iron ore 2 (5.06->6.98) | gears 1 (60.38->61.27), lead bars 11 (12.08->12.25), furniture 1 (13.44->14), tools 1 (4.51->4.76) | +62 |
| Marmont | 638 | 0.17 | 0.20 (20/turn) | beer 55 (3.04->4.2), rope 2 (69.5->75.05), honey 2 (7.67->8.31), garments 1 (17.9->18.52) | ploughs 1 (66.15->72.67) | +61 |

**Best:** Heilegg at about +99 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 27, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had None) |
| beer |  | 55 @ min 2.98 | goal planner: sells 55 at 2.98 (v2 had 55 at 3.38) |
| candles | 1 @ 68, stop 61 |  | goal planner: buys 1 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 3 @ min 7.25 | goal planner: sells 3 a turn at 7.25, keeps 23 (no one offered it) |
| cured meat | 1 @ 29.0, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 2) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 0 @ 2.4, stop 13 | 1 @ min 1.76 | uses 6.3/turn (brewery 1, household upkeep), makes 6.5, holds 8 |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.38 | goal planner: sells 2 a turn at 1.38, keeps 167 (no one offered it) |
| furniture | 2 @ 14.3, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 2 @ min 17.9 | goal planner: sells 2 at 17.9 (v2 had 2 at 20.0) |
| grain | 28 @ 3.7, stop 109 |  | goal planner: buys 28 a turn for today's rates, keeps up to 109 (v2 had 58) |
| labour | 0 @ 2.2, stop - |  | goal planner: buys 0 for today's rates (v2 had 0) |
| light armour | 1 @ 87.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 9 @ min 34 | goal planner: sells 9 at 34 (v2 had 9 at 34.6) |
| pasties | 4 @ 14.5, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 11 = 3.9 turns |
| porterage | 11 @ 1.1, stop - |  | goal planner: buys 11 for today's rates (v2 had 11) |
| rope |  | 2 @ min 67.5 |  |
| thread |  | 12 @ min 4.5 | goal planner: sells 12 a turn at 4.5, keeps 206 (no one offered it) |
| tools | 2 @ 6.2, stop 13 |  | uses 1.5/turn (retting pit 1), makes 0.0, holds 199 = 129.9 turns |
| varnish | 1 @ 20.6, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| wax | 1 @ 21.2, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 18.8k (cash + stock at home prices); +92/turn over 6 turns, +64/turn over 24 turns.
- Limits: cash flow >= +3/turn, prestige >= -0.61/turn (values are after 240 tax a turn).
- Today's settings: value +18/turn, cash +109/turn, prestige -0.59/turn.
- Plan: value +71/turn, cash +89/turn, prestige -0.61/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +351 vs +99, +552 vs +130, +472 vs +136.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4, nets 0.0, rope 0.1.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Hanbrücken: +4/turn
  - ship Flax Wyrm -> Brebronn: +1/turn
  - net maker 0.50 -> 0.73: +12/turn
  - logging camp w/ tool 5.00 -> 4.72: -0/turn
  - weavery 1 0.22 -> 0.13: -9/turn
  - flax farm 1 3.55 -> 6.01: -10/turn
  - retting pit 1 0.62 -> 1.05: -6/turn
  - spinnery 1 1.28 -> 2.17: -29/turn
  - ropewalk 1 0.50 -> 0.00: -117/turn
  - ropewalk 1 [make rope 2] 0.00 -> 0.99: +202/turn
- Model check over the last 40 turns: predicted +104/turn for the settings we ran, real +65/turn.
- Worth of one more unit per turn: labour 1.58, thread 3.89, cloth 6.26, flax fibres 4.48, garments 18.19, nets 28.89, beer 2.80, timber 2.87, prestige 54.87, cash 0.00
- Orders it would set: arms buy 1 (v2 None); candles buy 1 (v2 None); cloth sell 3 (v2 none); cured meat buy 1 (v2 2); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); grain buy 28 (v2 58); light armour buy 1 (v2 None); thread sell 12 (v2 none)
- Recipe: ropewalk 1 make rope 1 -> make rope 2 at 0.99, worth +45/turn.
- Ship linen snake: Grandgues -> Hanbrücken (+3/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Brebronn (+1/turn over staying).
- Management: ~13.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +79/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
- Trim: donate quarry 1: +19/turn (tax 20 saved).
- Trim: donate logging camp w/ tool: +17/turn (tax 20 saved).
- Trim: donate weavery 1: +12/turn (tax 18 saved).

## Chain sizing

Mode HOLD, garments sold 6.2/turn (+0.0 exported); plan makes 30.3 garments a turn.
Labour: own 500, everything else 409, chain may buy 350 -> chain allowance 441, chain plan 440 (+256 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 3.55 | 5.39 |
| ret | 3 | 0.62 | 0.96 |
| spin | 4 | 1.28 | 1.97 |
| weave | 3 | 0.22 | 1.19 |
| sew | 2 | 0.09 | 0.74 |

Buffers: flax fibres 35/87, thread 776/257, cloth 4/119
- chain plan needed 464 labour, budget left 441: cut to 441 (sewing capped at 0.74)

## Self-diagnosis

Nothing found this run.
