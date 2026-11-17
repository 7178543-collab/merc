# v2 shadow report

Turn 14090, 2026-11-17 11:22. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,737, prestige 3,627 (507 free, -2.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 0 | 0 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 5, buy @ 3.56 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 35 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 29 | 29 | 511 | 0 | 18 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.70 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.70 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **labour**: 18 labour expired last turn (~32 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **furniture**: home ask 15.70 is above our ceiling 15.50 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 511, not 611

## Prestige spending, cheapest coin per prestige first

311 turns left: prestige gained now converts 79.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 51.1 | 51.6 | needs a arena (build cost 29,067); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 53.1 | 53.1 | running |
| jousting 2 | arena | 210 | 56.0 | 56.5 | needs a arena (build cost 29,067); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 58.6 | 58.6 | thin at home: cured fish |
| hold banquet 1 (meat) | mansion | 4.2 | 62.2 | 62.2 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 63.2 | 63.2 | thin at home: hop beer, cured fish |
| hold banquet 3 (pies) | mansion | 8 | 63.2 | 63.2 | thin at home: hop beer |
| hold mass 2 (premium) | cathedral | 360 | 59.6 | 64.3 | needs a cathedral (build cost 323,050); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 3 (meat) | mansion | 7.6 | 65.3 | 65.3 | thin at home: hop beer |
| hold banquet 4 (premium) | mansion | 20 | 66.3 | 66.3 | thin at home: hop beer, wine, stockfish, premium ham |
| hold banquet 4 (pies) | mansion | 18 | 67.2 | 67.2 | thin at home: hop beer, wine, stockfish |
| hold banquet 2 (fish) | mansion | 6.8 | 68.2 | 68.2 | thin at home: wine, cured fish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 15.9 (keep 14); best orders clear only -2 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Amsdermund +674, Hofkirchen +536, Gotthafen +452, Bordees +392, Fulkirch +389
- Amsdermund would trade: furniture buy 62 @ 13.7; crew 1.0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~113 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.90 (102/turn) | timber 24 (8.09->12.54), firewood 35 (2.84->6.74), charcoal 19 (3.04->5.03), bread 160 (2.79->3.1) | wine 4 (7.25->10.45), cloth 2 (8.87->10.7), beer 4 (3.46->3.74), resin 4 (3.3->3.42) | +291 |
| Kirchwerp | 1072 | 0.41 | 0.60 (68/turn) | grindstones 1 (226.8->269.8), lead ore 8 (5.88->10.45), wheels 1 (24.57->38), paper 6 (26.04->26.98) | garments 19 (26.25->29.83), cloth 24 (8.09->10.7), flax fibres 28 (5.78->7.65), dyed cloth 7 (12.6->15.67) | +261 |
| Heidlowe | 662 | 0.20 | 0.40 (45/turn) | looms 1 (635.25->660.25), lead ore 2 (5.88->9.45), wrought iron 5 (19.01->20.14), grindstones 1 (226.8->233.7) | tapestries 1 (624.75->798), bricks 7 (6.41->12.92), wine 4 (7.82->10.45), cheese 9 (6.3->7.17) | +256 |
| Amsdermund | 1111 | 0.43 | 0.50 (56/turn) | copper ingots 1 (18.69->20.52), leather 1 (29.61->30.59) | cloth 24 (5.72->10.7), garments 19 (26.25->29.83), dyed cloth 7 (12.6->15.67), tools 16 (4.83->5.98) | +233 |
| Großmühle | 751 | 0.23 | 0.30 (34/turn) | cloth 1 (10.6->11.02) | tapestries 1 (619.5->798), bricks 4 (5.57->12.92), cheese 9 (5.83->7.17), wine 4 (7.72->10.45) | +207 |

**Best:** Grandgues at about +291 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.0, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 4.0 turns |
| beer | 9 @ 3.92, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 0 = 0.0 turns |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 15.5, stop 6 |  | uses 1.4/turn (household upkeep), makes 0.0, holds 11 = 8.1 turns |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 30.6) |
| grain | 0 @ 3.7, stop 18 |  | goal planner: buys 0 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 11) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.2) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 79.0) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 0 = 1.8 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 24.8k (cash + stock at home prices); +144/turn over 6 turns, +115/turn over 24 turns.
- Limits: cash flow >= -281/turn, prestige >= -0.86/turn (values are after 200 tax a turn).
- Today's settings: value +110/turn, cash +95/turn, prestige -2.75/turn - breaks the prestige floor.
- Plan: value +32/turn, cash +44/turn, prestige -0.86/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -103 vs +79, +14 vs +89, +2 vs +74 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Donaunieder: +20/turn
  - ship Flax Wyrm -> Brebronn: +1/turn
  - brewery 1 0.14 -> 0.08: +13/turn
  - spinnery 1 1.65 -> 1.57: +5/turn
  - net maker 0.00 -> 0.28: +4/turn
  - flax farm 1 4.64 -> 4.78: -1/turn
  - weavery 1 0.50 -> 0.59: -7/turn
  - sewing shop 1 0.30 -> 0.36: +11/turn
  - mansion 1 0.00 -> 0.45: -104/turn
- Model check over the last 60 turns: predicted +79/turn for the settings we ran, real +16/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.77, thread 4.45, cloth 7.10, flax fibres 5.27, garments 20.55, nets 32.25, beer 3.17, timber 3.46, prestige 60.50, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 11); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Donaunieder (+20/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Brebronn (+1/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +89/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new leatherworks (make leather armour 1) for ~4263 coin: +2/turn, payback 2547 turns, doesn't pay yet (materials thin at home: bricks, nails)

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 430 (+141 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.75 |
| ret | 3 | 0.91 | 0.95 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 88/77, thread 1050/228, cloth 73/128

## Self-diagnosis

- R1: beer slot dry: 0.2 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy 5 @ 3.56, home ask 3.74 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 9 @ 3.8 (ask 3.74, cap 5.7))
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.7; ask over the cap 2.1 (60 coin per prestige)
