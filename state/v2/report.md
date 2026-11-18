# v2 shadow report

Turn 14107, 2026-11-18 04:08. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,478, prestige 3,581 (461 free, -2.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 17 | 4 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 9, buy @ 3.8 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 2 | 2 | 2 | 1 | 0 | stop 7, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 61 | 0 | 2 | 0 | 0 | min_holding 75, sell 11, sell @ 21 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 18, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 511 | 0 | 18 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), 2 bought last turn); labour need rises ~18/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **firewood**: only 0.6 turns of firewood left and buying 2 (need 7) -> v2: buy 7

## Waste (money lost now)

- **labour**: 18 labour expired last turn (~32 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **candles**: home ask 83.50 is above our ceiling 76.00 and last turn bought 0 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 511, not 611

## Prestige spending, cheapest coin per prestige first

294 turns left: prestige gained now converts 77.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 52.3 | 52.8 | needs a arena (build cost 27,476); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 54.0 | 54.0 | running |
| jousting 2 | arena | 210 | 57.3 | 57.8 | needs a arena (build cost 27,476); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 58.6 | 58.6 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 60.3 | 60.3 | thin at home: hop beer, cheese |
| hold banquet 2 (fish) | mansion | 6.8 | 61.1 | 61.1 | thin at home: cheese |
| hold banquet 3 (pies) | mansion | 8 | 61.1 | 61.1 | thin at home: hop beer, cheese |
| hold mass 2 (premium) | cathedral | 360 | 57.4 | 62.2 | needs a cathedral (build cost 306,510); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 1 (meat) | mansion | 4.2 | 63.1 | 63.1 |  |
| hold banquet 3 (meat) | mansion | 7.6 | 63.1 | 63.1 | thin at home: hop beer, cheese |
| hold banquet 2 (pies) | mansion | 7 | 63.2 | 63.2 | thin at home: cheese |
| hold banquet 4 (premium) | mansion | 20 | 63.8 | 63.8 | thin at home: hop beer, stockfish, premium ham |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 15.3 (keep 14); best orders clear only -1 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Hofkirchen +515, Gotthafen +479, Fulkirch +293, Boistot +292, Cobholme +287
- Hofkirchen would trade: candles buy 3 @ 76.5, furniture buy 43 @ 13.9, pasties buy 6 @ 15.9; crew 0.7

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~115 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Kirchwerp | 1072 | 0.41 | 0.50 (57/turn) | looms 1 (640.5->755.25), jewellery 13 (102.9->104.5), lead ore 7 (6.98->10.45), honey 8 (9.35->10.16) | garments 19 (26.25->32.3), flax fibres 23 (5.62->7.55), canvas 4 (37.38->40.66), dyed cloth 4 (13.23->14.91) | +298 |
| Fontaux | 411 | 0.13 | 0.80 (92/turn) | beer 66 (4.03->5.84), thread 58 (5.5->7.27), timber 30 (7.88->11.88), rope 1 (73.5->75.52) | cloth 5 (10.08->10.9), flax fibres 2 (5.83->7.55), candles 1 (82.42->83.5), garments 19 (32.13->32.3) | +266 |
| Grandgues | 152 | 0.05 | 1.00 (115/turn) | timber 29 (7.88->11.21), firewood 34 (2.33->5.79), bread 161 (2.48->2.85), charcoal 19 (2.9->4.94) | dyed cloth 4 (11.03->14.91), bricks 3 (8.35->10.07), candles 1 (82.42->83.5), dyed yarn 1 (4.83->5.46) | +258 |
| Bremcop | 1326 | 0.57 | 0.30 (34/turn) | looms 1 (640.5->679.25), nets 6 (34.2->36.67), gold ore 1 (155.4->164.35), rope 1 (73.5->77.9) | garments 19 (22.26->32.3), butter 3 (75.6->78.85), candles 1 (80.85->83.5), casks 9 (4.85->6.08) | +238 |
| Amsdermund | 1111 | 0.44 | 0.40 (46/turn) | windows 1 (840->855), jewellery 8 (102.9->104.5), wine 10 (7.88->9.12), tackles 1 (152.25->155.8) | garments 19 (27.3->32.3), cloth 24 (7.35->10.9), tools 21 (4.83->5.51), chisels 2 (8.4->10.36) | +211 |

**Best:** Kirchwerp at about +298 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 4.02, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 76.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 8 = 5.7 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 3 @ 2.4, stop 11 |  | goal planner: buys 3 a turn for today's rates, keeps up to 11 (v2 had 7) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 33.0) |
| grain | 5 @ 3.7, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 11) |
| light armour | 1 @ 102, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 71.5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 27.8k (cash + stock at home prices); +206/turn over 6 turns, +174/turn over 24 turns.
- Limits: cash flow >= -395/turn, prestige >= -0.67/turn (values are after 200 tax a turn).
- Today's settings: value +100/turn, cash +82/turn, prestige -2.45/turn - breaks the prestige floor.
- Plan: value +26/turn, cash +37/turn, prestige -0.67/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +526 vs +75, +273 vs +74, +66 vs +80.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Calange: +10/turn
  - ship Flax Wyrm -> Arnsreuth: +0/turn
  - brewery 1 0.14 -> 0.07: +15/turn
  - spinnery 1 1.65 -> 1.57: +4/turn
  - net maker 0.00 -> 0.28: +4/turn
  - ropewalk 1 0.25 -> 0.32: +2/turn
  - flax farm 1 4.64 -> 4.56: +0/turn
  - mansion 1 0.00 -> 0.42: -101/turn
- Model check over the last 60 turns: predicted +125/turn for the settings we ran, real +66/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.80, thread 4.52, cloth 7.22, flax fibres 5.36, garments 20.90, nets 32.54, beer 3.32, timber 3.38, prestige 62.72, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 3 (v2 7); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 11); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Calange (+10/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Arnsreuth (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 8.5/turn (+0.0 exported); plan makes 38.5 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 495 (+206 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 5.37 |
| ret | 3 | 0.91 | 1.07 |
| spin | 4 | 1.65 | 1.90 |
| weave | 3 | 0.50 | 1.50 |
| sew | 2 | 0.30 | 0.94 |

Buffers: flax fibres 76/85, thread 1048/250, cloth 72/150

## Self-diagnosis

- R1: firewood slot dry: 2.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 3 @ 2.4, home ask 2.22; our bid is already at/over the ask (sellers too thin)
