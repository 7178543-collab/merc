# v2 shadow report

Turn 13528, 2026-10-25 01:23. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 1,292, prestige 3,571 (451 free, -0.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 7 | 0 | 0 | min_holding 60, sell 82, sell @ 2.98 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 6 | 2 | 4 | 4 | 0 | stop 6, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 33 | 0 | 2 | 0 | 0 | min_holding 30, sell 7, sell @ 17.8 |
| grain | 33 | 10 | 7 | 0 | 0 | stop 145, buy 10, buy @ 3.7 |
| labour | 20 | 24 | 524 | 2 | 0 | buy 20, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 12, sell @ 34 |
| porterage | 13 | 13 | 12 | 0 | 1 | buy 13, buy @ 1.1 |

**3 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cloth**: cloth buffer 0.0 turns (holds 0, next step uses 17/turn) -> v2: check the step that makes it
- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), 2 bought last turn); labour need rises ~82/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **labour**: buying 20, short of ~55 needed -> v2: buy 55

## Tuning

- **flax fibres**: flax fibres buffer thin: 1.2 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 57
- **flax plants**: flax plants buffer thin: 2.0 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 149

## Notes

- labour: projection runs 139 over real use lately; planning 555, not 694

## Prestige spending, cheapest coin per prestige first

873 turns left: prestige gained now converts 98.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 46.8 | 46.8 | running |
| hold banquet 4 (pies) | mansion | 18 | 49.6 | 49.6 | thin at home: hop beer, wine, pies |
| hold banquet 3 (pies) | mansion | 8 | 50.2 | 50.2 | thin at home: hop beer, pies |
| hold banquet 2 (pies) | mansion | 7 | 51.1 | 51.1 | thin at home: wine, pies |
| jousting 3 | arena | 230 | 52.6 | 52.7 | needs a arena (build cost 25,178); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 53.0 | 53.0 | thin at home: wine, hop beer, stockfish |
| hold prayer 2 | chapel | 13 | 50.2 | 53.3 | needs a chapel (build cost 32,027); thin at home: furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 53.8 | 53.8 | thin at home: wine |
| hold banquet 3 (fish) | mansion | 7.6 | 53.8 | 53.8 | thin at home: hop beer |
| hold banquet 2 (meat) | mansion | 6.8 | 54.5 | 54.5 | thin at home: wine |
| hold banquet 3 (meat) | mansion | 7.6 | 54.5 | 54.5 | thin at home: hop beer |
| hold sermon 2 (candles) | church | 31 | 52.1 | 54.8 | needs a church (build cost 66,516); thin at home: jewellery, candles, furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only 2 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -1 a turn after crew: ship stays at 0
- best towns now: Vauxvais +31, Marmont +19, Fontaux +19
- Vauxvais would trade: candles buy 1 @ 66.0, pasties buy 2 @ 11.9, rope sell 4 @ 77.5; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~97 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Bordetes | 831 | 0.22 | 0.20 (19/turn) | rope 1 (69.5->80.75), raw cloth 3 (7.51->11.02), charcoal 10 (1.99->3.82) | lathes 1 (176.4->195.7), spinning wheels 1 (202.65->218.5), premium ham 1 (262.5->271.7), cookware 2 (21->23.37) | +70 |
| Großaue | 1136 | 0.38 | 1.00 (97/turn) | bread 78 (2.31->4.14), rope 1 (69.5->71.72), scythes 0 (24.99->26.03) | cookware 1 (20.89->23.37), copper ingots 1 (11.76->12.35) | +59 |
| Hofkirchen | 991 | 0.31 | 0.20 (19/turn) | wrought iron 10 (13.97->17.1), seeds 6 (2.27->3.65), yarn 4 (4.16->5.08), iron ore 1 (4.98->7.6) | jewellery 3 (97.65->102.6), cookware 2 (21->23.37), beer 6 (2.62->3.5), candles 1 (71.4->72.5) | +58 |
| Grandgues | 152 | 0.04 | 0.20 (19/turn) | charcoal 10 (1.99->3.67), timber 18 (7.51->8.69), firewood 3 (1.61->4.31), rope 3 (69.5->69.83) | jewellery 3 (98.17->102.6), cookware 2 (21.42->23.37), candles 1 (69.3->72.5), lathes 1 (192.15->195.7) | +55 |
| Amsdermund | 1111 | 0.37 | 0.10 (10/turn) | rope 2 (69.5->82.65) | jewellery 3 (93.98->102.6), cookware 2 (20.48->23.37), mouldboards 1 (31.29->31.73), tools 1 (4.2->4.7) | +49 |

**Best:** Bordetes at about +70 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 26, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had None) |
| cured meat | 1 @ 29.0, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 2) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 3 @ 2.4, stop 16 |  | uses 7.9/turn (household upkeep), makes 6.5, holds 6 = 4.8 turns |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 13.8, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 7 @ min 17.8 | goal planner: sells 7 at 17.8 (v2 had 6 at 20.0) |
| grain | 29 @ 3.7, stop 115 |  | goal planner: buys 29 a turn for today's rates, keeps up to 115 (v2 had 63) |
| labour | 95 @ 2.2, stop - |  | goal planner: buys 95 for today's rates (v2 had 55) |
| light armour | 1 @ 85, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 12 @ min 34 | goal planner: sells 12 at 34 (v2 had 12 at 34.6) |
| pasties | 4 @ 14.5, stop 12 |  | uses 2.8/turn (household upkeep), makes 0.0, holds 11 = 3.8 turns |
| porterage | 13 @ 1.1, stop - |  | goal planner: buys 13 for today's rates (v2 had 5) |
| rope |  | 4 @ min 67.5 | makes 2.0, uses 0.2, holds 28 (keeps 0): sells the surplus + 2/turn of the excess |
| thread |  | 11 @ min 4.1 | goal planner: sells 11 a turn at 4.1, keeps 221 (no one offered it) |
| tools | 2 @ 6.2, stop 16 |  | uses 2.0/turn (net maker152202386007001, retting pit 1), makes 0.0, holds 200 = 101.8 turns |
| varnish | 1 @ 21.4, stop 1 |  | uses 0.1/turn (net maker152202386007001), makes 0.0, holds 0 = 1.4 turns |
| wax | 1 @ 20.8, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 18.4k (cash + stock at home prices); +91/turn over 6 turns, +84/turn over 24 turns.
- Limits: cash flow >= +113/turn, prestige >= -0.63/turn (values are after 240 tax a turn).
- Today's settings: value -16/turn, cash -53/turn, prestige -0.61/turn - breaks the cash floor.
- Plan: value +35/turn, cash +113/turn, prestige -0.63/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -144 vs +6, +293 vs -37, +303 vs -59.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4, garments 0.5, nets 0.0, rope 0.1.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Brunnham: -0/turn
  - brewery 1 0.63 -> 0.44: +32/turn
  - logging camp w/ tool 5.00 -> 4.87: +0/turn
  - sewing shop 1 0.21 -> 0.12: -6/turn
  - weavery 1 0.33 -> 0.26: +4/turn
  - spinnery 1 1.70 -> 1.27: -8/turn
  - retting pit 1 0.83 -> 0.62: +6/turn
  - flax farm 1 4.60 -> 3.55: +8/turn
  - ropewalk 1 0.50 -> 0.00: -30/turn
  - ropewalk 1 [make rope 2] 0.00 -> 0.31: +32/turn
- Model check over the last 34 turns: predicted +118/turn for the settings we ran, real +63/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.63, thread 4.01, cloth 6.46, flax fibres 4.62, garments 18.76, nets 29.84, beer 2.90, timber 2.95, prestige 57.36, cash 0.05
- Orders it would set: arms buy 1 (v2 None); cured meat buy 1 (v2 2); furniture buy 2 (v2 None); garments sell 7 (v2 6); grain buy 29 (v2 63); labour buy 95 (v2 55); light armour buy 1 (v2 None); porterage buy 13 (v2 5); thread sell 11 (v2 none)
- Recipe: ropewalk 1 make rope 1 -> make rope 2 at 0.31, worth +3/turn.
- Recipe: net maker make nets 3 -> make nets 2 at 0.67, worth +18/turn.
- Ship linen snake: Grandgues -> Brunnham (+3/turn over staying).
- Ship Flax Wyrm: stays on Caillechâtel (worth +6/turn).
- Management: ~13.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +80/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
- Trim: donate quarry 1: +20/turn (tax 20 saved).
- Trim: donate logging camp w/ tool: +18/turn (tax 20 saved).

## Chain sizing

Mode HOLD, garments sold 7.8/turn (+0.0 exported); plan makes 0.0 garments a turn.
Labour: own 500, everything else 434, chain may buy 0 -> chain allowance 66, chain plan 94 (-166 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.60 | 2.14 |
| ret | 3 | 0.83 | 0.38 |
| spin | 4 | 1.70 | 0.79 |
| weave | 3 | 0.33 | 0.00 |
| sew | 2 | 0.21 | 0.00 |

Buffers: flax fibres 36/47, thread 855/138, cloth 0/0
- chain plan needed 94 labour, budget left 66: cut to 94

## Self-diagnosis

- R5: varnish buy not filling: bid 17.1 under the home ask 20.4 for 5 turns, bought 0.0 of 1, 0.2 held (1.5 turns); raise needs Taylor (ceiling None)
