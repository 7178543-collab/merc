# v2 shadow report

Turn 14103, 2026-11-18 00:26. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,172, prestige 3,591 (471 free, -2.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 17 | 5 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 9, buy @ 3.8 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 18, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 511 | 0 | 18 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.92 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.92 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **labour**: 18 labour expired last turn (~32 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Notes

- labour: projection runs 100 over real use lately; planning 511, not 611

## Prestige spending, cheapest coin per prestige first

298 turns left: prestige gained now converts 77.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 52.8 | 53.2 | needs a arena (build cost 28,156); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 54.0 | 54.0 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 58.1 | 58.1 |  |
| jousting 2 | arena | 210 | 57.8 | 58.3 | needs a arena (build cost 28,156); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 59.9 | 59.9 | thin at home: wine |
| hold banquet 3 (pies) | mansion | 8 | 60.8 | 60.8 | thin at home: hop beer, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 60.9 | 60.9 | thin at home: hop beer |
| hold banquet 2 (pies) | mansion | 7 | 61.0 | 61.0 | thin at home: wine, pies |
| hold banquet 1 (meat) | mansion | 4.2 | 61.9 | 61.9 |  |
| hold banquet 2 (meat) | mansion | 6.8 | 62.5 | 62.5 | thin at home: wine |
| hold banquet 3 (meat) | mansion | 7.6 | 63.3 | 63.3 | thin at home: hop beer |
| hold mass 2 (premium) | cathedral | 360 | 59.2 | 63.9 | needs a cathedral (build cost 302,975); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 15.3 (keep 14); best orders clear only -1 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Amsdermund +714, Gotthafen +463, Cobholme +358, Fulkirch +271, Marmont +266
- Amsdermund would trade: furniture buy 65 @ 13.7, pasties buy 1 @ 16.2; crew 1.0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~114 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.90 (103/turn) | timber 26 (7.98->12.63), firewood 33 (3.07->6.65), bread 161 (2.52->2.83), charcoal 19 (3.02->4.35) | ham 3 (123.9->134.9), bricks 6 (7.4->12.06), coats 1 (72.98->77.42), candles 1 (84->87.5) | +293 |
| Unterhufe | 595 | 0.18 | 0.40 (46/turn) | rope 1 (72->75.52), chisels 1 (12.29->14.63), swords 1 (281.4->283.1) | looms 1 (582.75->693.5), cloth 22 (8.98->10.8), flax fibres 18 (6.67->7.9), furniture 7 (15.44->17.29) | +190 |
| Fontaux | 411 | 0.12 | 0.70 (80/turn) | beer 69 (3.95->5.37), timber 30 (7.98->11.49), rope 1 (72->75.05), honey 1 (9.66->10.36) | ham 3 (126->134.9), thread 44 (5.04->5.3), bricks 6 (8.82->12.06), flax fibres 5 (6.83->7.9) | +179 |
| Kirchwerp | 1072 | 0.41 | 1.00 (114/turn) | light armour 4 (98.7->112.1), jewellery 12 (101.85->104.5), beer 62 (3.95->4.94), lead ore 7 (7.25->10.45) | flax fibres 25 (5.62->7.9), ham 0 (126->134.9), tools 19 (5.02->5.79), garments 1 (26.25->30.2) | +175 |
| Herschweig | 775 | 0.24 | 0.10 (11/turn) | nets 6 (34.2->35.91), wine 3 (7.46->8.26) | looms 1 (556.5->693.5), ham 1 (129.15->134.9), candles 1 (83.48->87.5), furniture 7 (15.86->17.29) | +157 |

**Best:** Grandgues at about +293 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 3.94, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 29.0) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 11) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 70.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 26.8k (cash + stock at home prices); +207/turn over 6 turns, +71/turn over 24 turns.
- Limits: cash flow >= -382/turn, prestige >= -0.71/turn (values are after 200 tax a turn).
- Today's settings: value +94/turn, cash +74/turn, prestige -2.57/turn - breaks the prestige floor.
- Plan: value +19/turn, cash +26/turn, prestige -0.71/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +376 vs +70, +528 vs +75, +526 vs +75.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Gosschweig: +7/turn
  - ship Flax Wyrm -> Friedwerp: +1/turn
  - brewery 1 0.14 -> 0.08: +13/turn
  - spinnery 1 1.65 -> 1.59: +4/turn
  - net maker 0.00 -> 0.28: +4/turn
  - ropewalk 1 0.25 -> 0.31: +2/turn
  - weavery 1 0.50 -> 0.58: -7/turn
  - sewing shop 1 0.30 -> 0.36: +10/turn
  - mansion 1 0.00 -> 0.44: -101/turn
- Model check over the last 60 turns: predicted +126/turn for the settings we ran, real +48/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.80, thread 4.52, cloth 7.22, flax fibres 5.36, garments 20.90, nets 32.66, beer 3.19, timber 3.42, prestige 60.22, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 1 (v2 3); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 11); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Gosschweig (+8/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Friedwerp (+1/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 39.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 510 (+221 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 5.52 |
| ret | 3 | 0.91 | 1.10 |
| spin | 4 | 1.65 | 1.95 |
| weave | 3 | 0.50 | 1.55 |
| sew | 2 | 0.30 | 0.97 |

Buffers: flax fibres 79/87, thread 1049/255, cloth 72/155
- chain plan needed 585 labour, budget left 510: cut to 510 (sewing capped at 0.97)

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.92; ask over the cap 2.1 (60 coin per prestige)
