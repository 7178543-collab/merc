# v2 shadow report

Turn 13536, 2026-10-25 09:58. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 4,298, prestige 3,566 (446 free, -0.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 7 | 0 | 0 | min_holding 60, sell 55, sell @ 2.98 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 6 | 0 | 6 | 0 | 0 | buy @ 2.4; sell 1, sell @ 1.76 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 2, sell @ 17.9 |
| grain | 28 | 28 | 29 | 0 | 0 | stop 109, buy 28, buy @ 3.7 |
| labour | 39 | 39 | 499 | 0 | 40 | buy @ 2.2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 17 | 0 | 0 | 0 | 0 | min_holding 15, sell 13, sell @ 34 |
| porterage | 11 | 11 | 11 | 0 | 0 | buy 11, buy @ 1.1 |

**2 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.7 turns (holds 5, next step uses 7/turn) -> v2: check the step that makes it
- **grain**: only 1.0 turns of grain left and buying 28 (need 58) -> v2: buy 58

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.6 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 43

## Notes

- labour: projection runs 100 over real use lately; planning 499, not 595

## Prestige spending, cheapest coin per prestige first

865 turns left: prestige gained now converts 98.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 3 (pies) | mansion | 8 | 47.4 | 47.4 | thin at home: hop beer, pies |
| maintain 1 | park | 0.5 | 47.4 | 47.4 | running |
| hold banquet 4 (pies) | mansion | 18 | 48.6 | 48.6 | thin at home: hop beer, wine, pies |
| hold banquet 2 (pies) | mansion | 7 | 50.2 | 50.2 | thin at home: wine, pies |
| hold banquet 3 (meat) | mansion | 7.6 | 50.8 | 50.8 | thin at home: hop beer |
| hold banquet 3 (fish) | mansion | 7.6 | 51.8 | 51.8 | thin at home: hop beer |
| hold banquet 4 | mansion | 17.5 | 52.0 | 52.0 | thin at home: wine, hop beer, stockfish |
| jousting 3 | arena | 230 | 52.5 | 52.6 | needs a arena (build cost 23,895); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 52.9 | 52.9 | thin at home: wine |
| hold banquet 2 (fish) | mansion | 6.8 | 54.0 | 54.0 | thin at home: wine |
| hold prayer 2 | chapel | 13 | 51.2 | 54.1 | needs a chapel (build cost 30,094); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 52.2 | 54.8 | needs a church (build cost 61,817); thin at home: furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 134102075 | 0.06 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0.084 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: furniture buy 3 @ 13.2, pasties buy 3 @ 12.7; crew 0.1; est +48 a turn; stock: furniture 3 @ 13.2 (keep 145); stock: pasties 3 @ 12.7 (keep 14)
- **Flax Wyrm** on Caillechâtel: furniture buy 3 @ 12.8, pasties buy 1 @ 12.5; crew 0.1; est +37 a turn; stock: furniture 3 @ 12.8 (keep 145); stock: pasties 1 @ 12.5 (keep 14)
- best towns now: Friedwerp +62, Dortdorf +52, Heilegg +52, Heidlowe +51, Orlesailles +50
- Friedwerp would trade: furniture buy 3 @ 11.4, nets sell 1 @ 40.0, pasties buy 3 @ 11.4; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~98 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Herschweig | 775 | 0.20 | 0.20 (20/turn) | premium ham 1 (258.3->307.8), acid 1 (106.05->129.2), rope 1 (71->88.83), nets 4 (34.8->37.81) | salt 6 (4.03->5.56), beer 6 (2.84->3.5), thread 5 (4.26->4.88), grain 28 (2.31->2.74) | +115 |
| Marmont | 638 | 0.17 | 0.30 (29/turn) | beer 55 (3.04->4.46), premium ham 1 (258.3->281.2), rope 1 (71->75.52), hop beer 2 (7.3->8.17) | ploughs 4 (68.25->72.67), grain 28 (2.31->2.74), pasties 2 (12.92->13.6), salt 3 (5.25->5.56) | +102 |
| Fontaux | 411 | 0.11 | 0.80 (78/turn) | cheese 15 (5.99->9.79), premium ham 1 (258.3->277.4), firewood 19 (1.69->5.42), charcoal 11 (1.97->3.06) | salt 6 (4.33->5.56), mouldboards 2 (34.44->34.96), pasties 1 (13.02->13.6) | +95 |
| Rouhomme | 368 | 0.10 | 0.70 (69/turn) | bread 143 (2.16->2.77), premium ham 1 (258.3->285), beer 55 (3.04->3.42), charcoal 11 (1.97->3.29) | gears 1 (59.33->60.8), salt 2 (4.87->5.56), furniture 1 (13.44->14), resin 1 (1.53->1.88) | +91 |
| Neuborn | 780 | 0.20 | 0.50 (49/turn) | beer 55 (3.04->4.22), dye 1 (57.23->75.05), charcoal 11 (1.97->4.75), dyed cloth 2 (11.55->12.54) | flax fibres 10 (4.94->5.8), salt 3 (4.77->5.56), thread 3 (4.58->4.88) | +81 |

**Best:** Herschweig at about +115 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 27, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had None) |
| beer |  | 55 @ min 2.98 | goal planner: sells 55 at 2.98 (v2 had 55 at 3.38) |
| candles | 2 @ 66.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cured meat | 1 @ 29.0, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 2) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 0 @ 2.4, stop 13 | 1 @ min 1.76 | uses 6.3/turn (brewery 1, household upkeep), makes 6.5, holds 6 |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.36 | goal planner: sells 2 a turn at 1.36, keeps 167 (no one offered it) |
| furniture | 2 @ 14.3, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 2 @ min 17.9 | goal planner: sells 2 at 17.9 (v2 had 2 at 20.0) |
| grain | 28 @ 3.7, stop 109 |  | goal planner: buys 28 a turn for today's rates, keeps up to 109 (v2 had 58) |
| labour | 0 @ 2.2, stop - |  | goal planner: buys 0 for today's rates (v2 had 0) |
| light armour | 1 @ 88, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 13 @ min 34.0 |  |
| pasties | 3 @ 14.5, stop 11 |  | goal planner: buys 3 a turn for today's rates, keeps up to 11 (v2 had 4) |
| porterage | 11 @ 1.1, stop - |  | goal planner: buys 11 for today's rates (v2 had 11) |
| rope |  | 2 @ min 69.0 |  |
| thread |  | 13 @ min 4.5 | goal planner: sells 13 a turn at 4.5, keeps 203 (no one offered it) |
| tools | 2 @ 6.2, stop 14 |  | uses 1.7/turn (net maker152202386007001, retting pit 1), makes 0.0, holds 200 = 119.6 turns |
| varnish | 1 @ 21.6, stop 1 |  | uses 0.2/turn (net maker152202386007001), makes 0.0, holds 0 = 1.6 turns |
| wax | 1 @ 22.6, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 18.8k (cash + stock at home prices); +56/turn over 6 turns, +53/turn over 24 turns.
- Limits: cash flow >= -12/turn, prestige >= -0.61/turn (values are after 240 tax a turn).
- Today's settings: value +16/turn, cash +93/turn, prestige -0.59/turn.
- Plan: value +72/turn, cash +88/turn, prestige -0.61/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +351 vs +99, +552 vs +130, +472 vs +136.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4, nets 0.0, rope 0.1.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Cobholme: +4/turn
  - ship Flax Wyrm -> Friedwerp: +2/turn
  - logging camp w/ tool 5.00 -> 4.73: -0/turn
  - flax farm 1 3.55 -> 6.41: -17/turn
  - retting pit 1 0.62 -> 1.13: -6/turn
  - net maker 0.73 -> 0.00: -11/turn
  - net maker [make nets 2] 0.00 -> 0.83: +13/turn
  - spinnery 1 1.28 -> 2.32: -14/turn
  - ropewalk 1 0.50 -> 0.00: -119/turn
  - ropewalk 1 [make rope 2] 0.00 -> 1.00: +200/turn
- Model check over the last 42 turns: predicted +100/turn for the settings we ran, real +62/turn.
- Worth of one more unit per turn: labour 1.58, thread 3.89, cloth 6.26, flax fibres 4.47, garments 18.19, nets 29.00, beer 2.82, timber 3.04, prestige 53.51, cash 0.00
- Orders it would set: arms buy 1 (v2 None); candles buy 2 (v2 None); cured meat buy 1 (v2 2); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); grain buy 28 (v2 58); light armour buy 1 (v2 None); pasties buy 3 (v2 4); thread sell 13 (v2 none)
- Recipe: ropewalk 1 make rope 1 -> make rope 2 at 1.00, worth +48/turn.
- Recipe: net maker make nets 3 -> make nets 2 at 0.83, worth +18/turn.
- Ship linen snake: Grandgues -> Cobholme (+4/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Friedwerp (+2/turn over staying).
- Management: ~13.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +79/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot ropewalk 1 for ~2904 coin: +2/turn, payback 1192 turns, doesn't pay yet
- Trim: donate quarry 1: +19/turn (tax 20 saved).
- Trim: donate logging camp w/ tool: +17/turn (tax 20 saved).
- Trim: donate weavery 1: +13/turn (tax 18 saved).

## Chain sizing

Mode HOLD, garments sold 5.2/turn (+0.0 exported); plan makes 29.1 garments a turn.
Labour: own 500, everything else 415, chain may buy 350 -> chain allowance 435, chain plan 435 (+258 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 3.55 | 5.46 |
| ret | 3 | 0.62 | 0.97 |
| spin | 4 | 1.28 | 2.00 |
| weave | 3 | 0.13 | 1.14 |
| sew | 2 | 0.09 | 0.71 |

Buffers: flax fibres 35/88, thread 735/260, cloth 5/114
- chain plan needed 471 labour, budget left 435: cut to 435 (sewing capped at 0.71)

## Self-diagnosis

Nothing found this run.
