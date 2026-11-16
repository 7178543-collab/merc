# v2 shadow report

Turn 14058, 2026-11-16 03:28. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,763, prestige 3,546 (426 free, -2.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 8 | 4 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 7, buy @ 3.6 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 7, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 35 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21.2 |
| grain | 35 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 29 | 29 | 516 | 0 | 13 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), but the home ask 2.94 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.94 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Tuning

- **beer**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 516, not 616

## Prestige spending, cheapest coin per prestige first

343 turns left: prestige gained now converts 82.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.8 | 49.8 | running |
| jousting 3 | arena | 230 | 52.6 | 53.0 | needs a arena (build cost 26,195); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 | arena | 210 | 57.6 | 58.0 | needs a arena (build cost 26,195); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 58.8 | 58.8 | thin at home: beer, cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 60.1 | 60.1 | thin at home: cured fish |
| hold banquet 2 (pies) | mansion | 7 | 60.3 | 60.3 |  |
| hold banquet 3 (pies) | mansion | 8 | 61.4 | 61.4 | thin at home: hop beer |
| hold mass 2 (premium) | cathedral | 360 | 59.0 | 62.8 | needs a cathedral (build cost 307,240); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 3 (fish) | mansion | 7.6 | 63.0 | 63.0 | thin at home: hop beer, cured fish |
| hold banquet 2 (meat) | mansion | 6.8 | 63.2 | 63.2 |  |
| hold banquet 1 (meat) | mansion | 4.2 | 63.3 | 63.3 | thin at home: beer |
| hold banquet 4 (premium) | mansion | 20 | 63.5 | 63.5 | thin at home: hop beer, ham, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 10 | 151802239 | 0.156 | - | pasties 12 | -192 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 22 @ 13.3, pasties buy 1 @ 14.8; crew 0.2; est +272 a turn; stock: furniture 22 @ 13.3 (keep 145); stock: pasties 1 @ 14.8 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 16.4 (keep 14); best orders clear only -5 a turn after crew: ship stays at 0
- best towns now: Amsdermund +537, Gotthafen +465, Vauxvais +386, Fulkirch +279, Caillechâtel +272
- Amsdermund would trade: furniture buy 53 @ 14.5; crew 0.9

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~104 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 1.00 (104/turn) | timber 41 (7.77->12.63), firewood 31 (3.09->5.84), furniture 7 (11.76->17), charcoal 17 (2.94->5.13) | beer 135 (3.36->3.82), ham 0 (112.35->132.05), dyed cloth 2 (11.34->13.21), cheese 3 (6.72->7.46) | +408 |
| Blanans | 297 | 0.08 | 0.60 (62/turn) | looms 1 (588->650.75), bread 162 (2.37->2.79), furniture 8 (11.76->14.34), rope 1 (74.5->82.17) | ham 1 (115.5->132.05), garments 2 (23.1->24.6), dyed cloth 3 (12.6->13.21), logs 3 (5.21->7.22) | +143 |
| Birkeningen | 1006 | 0.34 | 0.20 (21/turn) | looms 1 (588->669.75), garments 10 (22.4->24.89), wine 6 (6.62->7.93), arms 4 (32.34->33.25) | ham 1 (111.3->132.05), tackles 1 (154.35->163.4), tar 4 (10.24->11.4), thread 7 (4.47->5.15) | +139 |
| Brunnham | 1281 | 0.49 | 0.20 (21/turn) | looms 1 (588->665), nets 6 (34.6->38.19), rope 1 (74.5->75.52) | ham 1 (113.4->132.05), salt 11 (4.33->5.56), cheese 4 (6.14->7.46), cookware 3 (21->22.42) | +124 |
| Großaue | 1136 | 0.41 | 0.30 (31/turn) | looms 1 (588->655.5), thread 27 (4.78->5.51), malt 2 (6.98->10.54), garments 10 (22.4->23.18) | ham 1 (112.35->132.05), cheese 4 (5.67->7.46), lead bars 7 (11.65->12.44), dyed cloth 3 (12.5->13.21) | +116 |

**Best:** Grandgues at about +408 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.2, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 4.0 turns |
| beer | 9 @ ?, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 8 = 2.0 turns |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21.2 | goal planner: sells 11 at 21.2 (v2 had 10 at 21.8) |
| grain | 0 @ 3.7, stop 18 |  | goal planner: buys 0 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 16) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 34.0 |  |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 72.5) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.3/turn (ropewalk 1), makes 0.0, holds 0 = 1.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 24.4k (cash + stock at home prices); +105/turn over 6 turns, +7/turn over 24 turns.
- Limits: cash flow >= -240/turn, prestige >= -0.53/turn (values are after 200 tax a turn).
- Today's settings: value +73/turn, cash +27/turn, prestige -2.34/turn - breaks the prestige floor.
- Plan: value +30/turn, cash +36/turn, prestige -0.53/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +20 vs +31, -612 vs +31, +85 vs +9 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Vauxvais: +7/turn
  - ship Flax Wyrm -> Angefont: +0/turn
  - net maker 0.00 -> 0.29: +11/turn
  - ropewalk 1 0.25 -> 0.00: +11/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.07: +12/turn
  - brewery 1 0.14 -> 0.08: +10/turn
  - spinnery 1 1.65 -> 1.41: +3/turn
  - flax farm 1 4.64 -> 4.43: -0/turn
  - sewing shop 1 0.30 -> 0.40: -4/turn
  - weavery 1 0.50 -> 0.66: +13/turn
- Model check over the last 59 turns: predicted -93/turn for the settings we ran, real -89/turn.
- Worth of one more unit per turn: labour 1.66, thread 4.17, cloth 6.66, flax fibres 4.95, garments 19.27, nets 30.31, beer 2.96, timber 3.33, prestige 59.69, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 16); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.07, worth +3/turn.
- Ship linen snake: Grandgues -> Vauxvais (+7/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Angefont (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +82/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new leatherworks (make leather armour 1) for ~3715 coin: +1/turn, payback 3642 turns, doesn't pay yet (materials thin at home: nails)

## Chain sizing

Mode HOLD, garments sold 11.3/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 415 (+125 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 3.97 |
| ret | 3 | 0.91 | 0.79 |
| spin | 4 | 1.65 | 1.67 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 133/77, thread 1050/227, cloth 72/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.94; ask over the cap 2.1 (60 coin per prestige)
