# v2 shadow report

Turn 14060, 2026-11-16 05:39. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 8,766, prestige 3,541 (421 free, -2.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 0 | 0 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 7, buy @ 3.6 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 33 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21.2 |
| grain | 35 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 29 | 29 | 501 | 0 | 28 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.20 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 28 labour expired last turn (~47 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **beer**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.20 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +6 crew for Flax Wyrm (crew 0.12, no projection from the game)
- labour: projection runs 100 over real use lately; planning 501, not 589

## Prestige spending, cheapest coin per prestige first

341 turns left: prestige gained now converts 81.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 49.3 | 49.7 | needs a arena (build cost 28,099); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 50.1 | 50.1 | running |
| jousting 2 | arena | 210 | 54.0 | 54.5 | needs a arena (build cost 28,099); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 58.6 | 58.6 | thin at home: beer, cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 58.6 | 58.6 | thin at home: cured fish |
| hold banquet 2 (pies) | mansion | 7 | 60.4 | 60.4 |  |
| hold banquet 2 (meat) | mansion | 6.8 | 61.3 | 61.3 |  |
| hold banquet 1 (meat) | mansion | 4.2 | 62.7 | 62.7 | thin at home: beer |
| hold banquet 3 (fish) | mansion | 7.6 | 63.0 | 63.0 | thin at home: hop beer, cured fish |
| hold banquet 3 (pies) | mansion | 8 | 63.1 | 63.1 | thin at home: hop beer |
| hold mass 2 (premium) | cathedral | 360 | 59.3 | 63.2 | needs a cathedral (build cost 311,650); thin at home: furniture, jewellery, glassware, candles, premium garments |
| jousting 1 | arena | 170 | 63.5 | 64.1 | needs a arena (build cost 28,099); thin at home: protection, light armour, arms; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 22 @ 13.3, pasties buy 1 @ 15.1; crew 0.2; est +271 a turn; stock: furniture 22 @ 13.3 (keep 145); stock: pasties 1 @ 15.1 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 15.9 (keep 14); best orders clear only 0 a turn after crew: ship stays at 0
- best towns now: Amsdermund +509, Vauxvais +389, Friedwerp +319, Boistot +301, Clairlond +279
- Amsdermund would trade: furniture buy 49 @ 14.3; crew 0.8

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~105 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 1.00 (105/turn) | timber 42 (7.77->12.54), firewood 31 (3.07->5.79), furniture 9 (11.55->15.67), charcoal 17 (3.09->5.18) | beer 65 (3.38->4.16), ham 0 (110.25->132.05), dyed cloth 2 (11.34->13.96), candles 0 (78.23->84) | +431 |
| Kirchwerp | 1072 | 0.38 | 0.40 (42/turn) | furniture 10 (11.55->15.96), leather 1 (24.36->32.3), looms 1 (588->598.5), resin 6 (2.39->3.93) | cloth 24 (7.51->8.9), ham 1 (112.35->132.05), ploughs 3 (73.5->83.12), salt 13 (4.45->5.56) | +146 |
| Gotthafen | 964 | 0.32 | 0.20 (21/turn) | garments 10 (21.6->31.73), furniture 10 (11.55->13.87), nets 2 (34.4->35.53), wine 3 (6.41->7.17) | ham 1 (111.3->132.05), cheese 3 (6.25->7.55), salt 7 (4.77->5.56), yarn 5 (3.95->4.94) | +143 |
| Großaue | 1136 | 0.41 | 0.20 (21/turn) | looms 1 (588->655.5), garments 10 (21.6->23.18), malt 2 (6.98->11.11), leather 1 (24.36->29.83) | ham 1 (118.65->132.05), ploughs 3 (75.08->83.12), copper ore 1 (20.06->28.88), dyed cloth 3 (11.87->13.96) | +141 |
| Pontmont | 341 | 0.10 | 1.00 (105/turn) | firewood 25 (3.07->8.07), bread 77 (2.33->3.1), furniture 4 (11.55->14.25), tiles 4 (3.72->6.6) | ham 0 (121.8->132.05), beer 34 (3.89->4.16), cookware 1 (21->22.04), copper ore 0 (25.62->28.88) | +130 |

**Best:** Grandgues at about +431 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.0, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 4.0 turns |
| beer | 8 @ ?, stop 16 |  | uses 4.0/turn (household upkeep), makes 0.0, holds 0 = 0.0 turns |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21.0 | goal planner: sells 11 (v2 had 10) |
| grain | 0 @ 3.7, stop 20 |  | goal planner: buys 0 a turn for today's rates, keeps up to 20 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 1) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 34.0 |  |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.4/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 24.6k (cash + stock at home prices); +36/turn over 6 turns, +24/turn over 24 turns.
- Limits: cash flow >= -199/turn, prestige >= -0.51/turn (values are after 200 tax a turn).
- Today's settings: value +67/turn, cash +30/turn, prestige -2.72/turn - breaks the prestige floor.
- Plan: value -6/turn, cash +1/turn, prestige -0.51/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +85 vs +9, -670 vs +27, -328 vs +31 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Vauxvais: +7/turn
  - ship Flax Wyrm -> Brunnham: +0/turn
  - net maker 0.00 -> 0.33: +12/turn
  - brewery 1 0.14 -> 0.09: +10/turn
  - spinnery 1 1.65 -> 1.47: +4/turn
  - ropewalk 1 0.25 -> 0.00: +11/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.13: +6/turn
  - sewing shop 1 0.30 -> 0.39: -8/turn
  - weavery 1 0.50 -> 0.65: +16/turn
  - mansion 1 0.00 -> 0.53: -126/turn
- Model check over the last 58 turns: predicted -81/turn for the settings we ran, real -85/turn.
- Worth of one more unit per turn: labour 1.67, thread 4.20, cloth 6.70, flax fibres 4.98, garments 19.39, nets 30.49, beer 3.13, timber 3.60, prestige 61.53, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 1); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.13, worth +4/turn.
- Ship linen snake: Grandgues -> Vauxvais (+7/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Brunnham (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +84/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 11.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 417 (+128 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.04 |
| ret | 3 | 0.91 | 0.81 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 128/77, thread 1064/228, cloth 72/128

## Self-diagnosis

- R1: beer slot dry: 0.0 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy 7 @ 3.6, home ask none (no sellers at home)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
