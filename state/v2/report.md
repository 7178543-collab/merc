# v2 shadow report

Turn 13520, 2026-10-24 17:31. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 1,023, prestige 3,576 (456 free, -0.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 7 | 0 | 0 | min_holding 60, sell 82, sell @ 2.98 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 4 | 2 | 5 | 3 | 0 | stop 16, buy 2, buy @ 2.4; sell 5, sell @ 1.71 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 24, buy 7, buy @ 2.5 |
| garments | 41 | 0 | 2 | 0 | 0 | min_holding 30, sell 8, sell @ 17.8 |
| grain | 111 | 0 | 14 | 0 | 0 | buy @ 3.7 |
| labour | 10 | 10 | 510 | 30 | 0 | buy 10, buy @ 2 |
| meat | 6 | 6 | 6 | 0 | 0 | stop 24, buy 6, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 12, sell @ 34 |
| porterage | 12 | 12 | 7 | 0 | 5 | buy 12, buy @ 1.1 |

**2 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), 2 bought last turn); labour need rises ~82/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **labour**: buying 10, short of ~59 needed -> v2: buy 59

## Tuning

- **cloth**: cloth buffer thin: 1.5 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 33
- **flax fibres**: flax fibres buffer thin: 1.2 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 57

## Notes

- labour: projection runs 100 over real use lately; planning 559, not 659

## Prestige spending, cheapest coin per prestige first

881 turns left: prestige gained now converts 98.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 45.6 | 45.6 | running |
| hold banquet 4 (pies) | mansion | 18 | 49.4 | 49.4 | thin at home: hop beer, pies |
| hold banquet 3 (pies) | mansion | 8 | 49.9 | 49.9 | thin at home: hop beer, pies |
| hold banquet 2 (pies) | mansion | 7 | 50.5 | 50.5 | thin at home: pies |
| jousting 3 | arena | 230 | 52.0 | 52.1 | needs a arena (build cost 24,352); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 52.7 | 52.7 | thin at home: hop beer, stockfish |
| hold banquet 2 (fish) | mansion | 6.8 | 52.9 | 52.9 |  |
| hold prayer 2 | chapel | 13 | 50.1 | 53.0 | needs a chapel (build cost 31,334); thin at home: furniture |
| hold banquet 3 (fish) | mansion | 7.6 | 53.3 | 53.3 | thin at home: hop beer |
| hold sermon 2 (candles) | church | 31 | 50.8 | 53.5 | needs a church (build cost 65,839); thin at home: candles, furniture |
| hold feast 2 | townhouse | 2.6 | 51.3 | 54.3 | needs a townhouse (build cost 6,706) |
| hold banquet 2 (meat) | mansion | 6.8 | 54.5 | 54.5 | thin at home: cured meat |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only -3 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only -6 a turn after crew: ship stays at 0
- best towns now: Birkeningen +15
- Birkeningen would trade: garments sell 7 @ 23.0; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~96 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.30 | 0.40 (38/turn) | nails 15 (6.51->10.83), rope 2 (53.87->68.88), yarn 23 (3.65->5.08), glass ingots 2 (59.33->68.4) | beer 6 (2.23->3.5), casks 10 (5.72->6.65), candles 1 (67.2->69.5), cookware 4 (21->21.47) | +171 |
| Friedwerp | 684 | 0.17 | 0.10 (10/turn) | premium ham 1 (346.5->419.9), rope 2 (53.87->68.88), yarn 15 (3.65->4.8), garments 7 (17.8->19.76) | casks 5 (5->6.65), candles 1 (67.73->69.5), pasties 2 (12.29->13.2) | +142 |
| Amsdermund | 1111 | 0.36 | 0.40 (38/turn) | thread 58 (4.1->5.22), rope 2 (53.87->73.62), wine 11 (5.46->6.84), blades 2 (15.02->17.39) | casks 10 (5.78->6.65), cookware 4 (20.89->21.47), garments 2 (18.48->19.3), raw cloth 2 (5.99->6.79) | +102 |
| Rouhomme | 368 | 0.09 | 0.60 (57/turn) | bread 142 (2.08->2.62), rope 1 (53.87->70.77), charcoal 11 (1.63->3.29), iron ore 2 (4.85->8.46) | casks 10 (5.17->6.65), cookware 4 (21->21.47), lathes 1 (202.65->205.2), candles 1 (68.25->69.5) | +96 |
| Nürnnieder | 520 | 0.13 | 0.20 (19/turn) | thread 46 (4.1->5.13), rope 2 (53.87->71.25), blades 2 (15.02->17), garments 7 (17.8->18.52) | casks 7 (4.89->6.65), beer 6 (3->3.5), furniture 1 (12.39->13.8), tiles 1 (2.71->4.35) | +94 |

**Best:** Hofkirchen at about +171 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 26.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| cured meat | 1 @ 29.0, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 2) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 3 @ 2.4, stop 16 | 4 @ min 1.66 | uses 7.9/turn (household upkeep), makes 6.5, holds 4 = 2.7 turns |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 14.1, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 8 @ min 17.8 | goal planner: sells 8 at 17.8 (v2 had 8 at 20.0) |
| grain | 37 @ 3.7, stop 145 |  | goal planner: buys 37 a turn for today's rates, keeps up to 145 (v2 had 15) |
| labour | 95 @ 2.2, stop - |  | goal planner: buys 95 for today's rates (v2 had 59) |
| light armour | 1 @ 79, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 6 @ 3.02, stop - |  | goal planner: buys 6 for today's rates (v2 had 6) |
| nets |  | 12 @ min 34 | goal planner: sells 12 at 34 (v2 had 12 at 34.6) |
| pasties | 3 @ 14.5, stop 11 |  | goal planner: buys 3 a turn for today's rates, keeps up to 11 (v2 had 4) |
| porterage | 13 @ 1.1, stop - |  | goal planner: buys 13 for today's rates (v2 had 12) |
| rope |  | 4 @ min 72.0 | makes 2.0, uses 0.2, holds 28 (keeps 0): sells the surplus + 2/turn of the excess |
| thread |  | 7 @ min 4.1 | goal planner: sells 7 a turn at 4.1, keeps 221 (no one offered it) |
| tools | 2 @ 6.2, stop 16 |  | uses 2.0/turn (net maker152202386007001, retting pit 1), makes 0.0, holds 200 = 101.8 turns |
| varnish | 1 @ 17.1, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| wax | 1 @ 21.2, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |

## Goal: business value (live: rates, buys, sells, ships, invest, trim)
- Value now 18.0k (cash + stock at home prices); +49/turn over 6 turns, +77/turn over 24 turns.
- Limits: cash flow >= +124/turn, prestige >= -0.65/turn (values are after 240 tax a turn).
- Today's settings: value +14/turn, cash +11/turn, prestige -0.64/turn - breaks the cash floor.
- Plan: value +41/turn, cash +124/turn, prestige -0.65/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +67 vs +93, +139 vs +63, +1 vs +20.
- Route sales counted at most (what the ships really sold, a turn): beer 0.4, garments 0.5, nets 0.0, rope 0.1.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Boistot: +6/turn
  - brewery 1 0.63 -> 0.55: +13/turn
  - weavery 1 0.33 -> 0.45: +2/turn
  - logging camp w/ tool 5.00 -> 5.58: +0/turn
  - retting pit 1 0.83 -> 0.69: -10/turn
  - flax farm 1 4.60 -> 3.96: +5/turn
  - spinnery 1 1.70 -> 1.42: +3/turn
- Model check over the last 26 turns: predicted +132/turn for the settings we ran, real +69/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.64, thread 4.03, cloth 6.49, flax fibres 4.63, garments 18.85, nets 29.81, beer 2.90, timber 7.12, prestige 60.09, cash 0.07
- Orders it would set: cured meat buy 1 (v2 2); furniture buy 2 (v2 None); grain buy 37 (v2 15); labour buy 95 (v2 59); light armour buy 1 (v2 None); pasties buy 3 (v2 4); porterage buy 13 (v2 12); thread sell 7 (v2 none)
- Ship linen snake: Grandgues -> Boistot (+7/turn over staying).
- Ship Flax Wyrm: stays on Caillechâtel (worth +7/turn).
- Management: ~13.78 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +80/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
- Trim: donate quarry 1: +21/turn (tax 20 saved).
- Trim: donate logging camp w/ tool: +18/turn (tax 20 saved).

## Chain sizing

Mode HOLD, garments sold 6.8/turn (+0.0 exported); plan makes 0.0 garments a turn.
Labour: own 500, everything else 434, chain may buy 0 -> chain allowance 66, chain plan 94 (-166 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.60 | 2.14 |
| ret | 3 | 0.83 | 0.38 |
| spin | 4 | 1.70 | 0.79 |
| weave | 3 | 0.33 | 0.00 |
| sew | 2 | 0.21 | 0.00 |

Buffers: flax fibres 34/47, thread 763/138, cloth 25/0
- chain plan needed 94 labour, budget left 66: cut to 94

## Self-diagnosis

- R1: firewood slot dry: 3.7 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 3 @ 2.4, home ask 1.71; our bid is already at/over the ask (sellers too thin)
