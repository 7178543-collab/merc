# v2 shadow report

Turn 14112, 2026-11-18 09:36. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,600, prestige 3,617 (497 free, -2.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 16 | 4 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 9, buy @ 3.8 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 34 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 29 | 29 | 511 | 0 | 18 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.86 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.86 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **labour**: 18 labour expired last turn (~32 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **candles**: home ask 83.50 is above our ceiling 76.00 and last turn bought 1 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 511, not 611

## Prestige spending, cheapest coin per prestige first

289 turns left: prestige gained now converts 76.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 53.2 | 53.7 | needs a arena (build cost 26,024); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 53.7 | 53.7 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 58.8 | 58.8 |  |
| jousting 2 | arena | 210 | 58.3 | 58.8 | needs a arena (build cost 26,024); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (meat) | mansion | 4.2 | 60.4 | 60.4 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 61.1 | 61.1 |  |
| hold banquet 2 (meat) | mansion | 6.8 | 61.9 | 61.9 |  |
| hold mass 2 (premium) | cathedral | 360 | 57.2 | 61.9 | needs a cathedral (build cost 289,380); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |
| hold banquet 3 (fish) | mansion | 7.6 | 62.4 | 62.4 | thin at home: hop beer |
| hold banquet 3 (meat) | mansion | 7.6 | 63.1 | 63.1 | thin at home: hop beer |
| hold banquet 3 (pies) | mansion | 8 | 63.2 | 63.2 | thin at home: hop beer |
| hold banquet 2 (pies) | mansion | 7 | 63.4 | 63.4 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: candles buy 2 @ 78.0, pasties buy 9 @ 15.5; crew 0.1; est +43 a turn; stock: candles 2 @ 78.0 (keep 12); stock: pasties 9 @ 15.5 (keep 14)
- **Flax Wyrm** on Caillechâtel: candles buy 2 @ 78.0, pasties buy 2 @ 16.4; crew 0.1; est +17 a turn; stock: candles 2 @ 78.0 (keep 12); stock: pasties 2 @ 16.4 (keep 14)
- best towns now: Amsdermund +695, Gotthafen +448, Vauxvais +387, Donaunieder +339, Cobholme +323
- Amsdermund would trade: furniture buy 63 @ 13.7, pasties buy 3 @ 16.0; crew 1.0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~114 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.80 (91/turn) | timber 31 (7.88->12.44), firewood 34 (3->6.27), limestone 5 (15.33->24.7), charcoal 19 (2.96->4.54) | bricks 4 (8.03->11.49), cloth 4 (9.66->11), premium ham 1 (283.5->288.8), candles 1 (81.38->83.5) | +275 |
| Cobholme | 1564 | 0.71 | 0.30 (34/turn) | garments 10 (26.4->36.48), cured fish 7 (24.57->28.12), cured meat 3 (23.73->28.88), rope 1 (72->79.33) | swords 2 (212.1->233.7), tin ingots 3 (26.25->29.83) | +177 |
| Fontaux | 411 | 0.12 | 0.90 (102/turn) | thread 43 (5.5->7.27), timber 37 (7.88->11.59), furniture 7 (16.17->18.43), dyed cloth 5 (12.71->13.77) | candles 1 (80.85->83.5), flax fibres 21 (7.09->7.45), resin 3 (2.96->3.7), flax plants 5 (1.56->1.87) | +173 |
| Essenbrucke | 584 | 0.18 | 0.20 (23/turn) | nets 1 (35->38.95), dyed cloth 1 (12.71->13.3) | windows 1 (719.25->807.5), cloth 14 (8.24->11), cookware 4 (21.21->23.56), garments 2 (27.72->30.2) | +156 |
| Hofkirchen | 991 | 0.36 | 0.40 (45/turn) | lathes 1 (182.7->197.6), gold ore 1 (147->156.75), tackles 2 (158.55->163.4), dyed cloth 5 (12.71->13.11) | cloth 24 (9.13->11), flax fibres 28 (5.62->7.45), thread 25 (4.7->5.75), premium ham 1 (273->288.8) | +152 |

**Best:** Grandgues at about +275 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.8, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 4.0 turns |
| beer | 5 @ 4.04, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 16 = 3.9 turns |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 16 = 3.9 turns |
| candles | 2 @ 76.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 8 = 5.3 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 10 @ min 21 | goal planner: sells 10 at 21 (v2 had 10 at 25.8) |
| grain | 0 @ 3.7, stop 19 |  | goal planner: buys 0 a turn for today's rates, keeps up to 19 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 11) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 70.0) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 1 = 4.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 26.1k (cash + stock at home prices); -125/turn over 6 turns, +66/turn over 24 turns.
- Limits: cash flow >= -358/turn, prestige >= -0.82/turn (values are after 200 tax a turn).
- Today's settings: value +80/turn, cash +51/turn, prestige -2.70/turn - breaks the prestige floor.
- Plan: value +13/turn, cash +22/turn, prestige -0.82/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -716 vs +79, -451 vs +86, +224 vs +66 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Donaunieder: +22/turn
  - ship Flax Wyrm -> no route: +0/turn
  - brewery 1 0.14 -> 0.08: +14/turn
  - net maker 0.00 -> 0.28: +4/turn
  - spinnery 1 1.65 -> 1.46: +3/turn
  - retting pit 1 0.91 -> 0.84: +1/turn
  - flax farm 1 4.64 -> 4.23: +3/turn
  - ropewalk 1 0.25 -> 0.31: -0/turn
  - mansion 1 0.00 -> 0.45: -100/turn
- Model check over the last 60 turns: predicted +126/turn for the settings we ran, real +39/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.79, thread 4.50, cloth 7.18, flax fibres 5.33, garments 20.78, nets 32.50, beer 3.35, timber 3.38, prestige 59.29, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 1 (v2 3); furniture buy 2 (v2 None); grain buy 5 (v2 0); labour buy 29 (v2 11); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Donaunieder (+22/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 4.8/turn (+0.0 exported); plan makes 32.4 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 423 (+134 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.69 |
| ret | 3 | 0.91 | 0.94 |
| spin | 4 | 1.65 | 1.65 |
| weave | 3 | 0.50 | 1.26 |
| sew | 2 | 0.30 | 0.79 |

Buffers: flax fibres 76/77, thread 1050/225, cloth 72/126

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.86; ask over the cap 2.1 (60 coin per prestige)
