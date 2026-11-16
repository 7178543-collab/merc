# v2 shadow report

Turn 14059, 2026-11-16 04:33. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,093, prestige 3,544 (424 free, -2.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 4 | 0 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 7, buy @ 3.6 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 34 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21.2 |
| grain | 35 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 29 | 29 | 520 | 0 | 9 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.94 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.94 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.30 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Tuning

- **beer**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.30 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +10 crew for Flax Wyrm (crew 0.20, no projection from the game)
- labour: projection runs 100 over real use lately; planning 520, not 611

## Prestige spending, cheapest coin per prestige first

342 turns left: prestige gained now converts 82.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.8 | 49.8 | running |
| jousting 3 | arena | 230 | 52.2 | 52.6 | needs a arena (build cost 25,947); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 | arena | 210 | 57.2 | 57.6 | needs a arena (build cost 25,947); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 59.5 | 59.5 | thin at home: cured fish |
| hold banquet 1 (fish) | mansion | 4.2 | 60.0 | 60.0 | thin at home: beer, cured fish |
| hold banquet 2 (pies) | mansion | 7 | 60.2 | 60.2 |  |
| hold banquet 2 (meat) | mansion | 6.8 | 62.2 | 62.2 |  |
| hold banquet 3 (pies) | mansion | 8 | 62.2 | 62.2 | thin at home: hop beer |
| hold mass 2 (premium) | cathedral | 360 | 59.1 | 62.8 | needs a cathedral (build cost 301,420); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 3 (fish) | mansion | 7.6 | 63.5 | 63.5 | thin at home: hop beer, cured fish |
| hold banquet 4 (premium) | mansion | 20 | 63.6 | 63.6 | thin at home: hop beer, ham, stockfish |
| hold banquet 1 (meat) | mansion | 4.2 | 63.9 | 63.9 | thin at home: beer |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.20 | 20 | 134102075 | 0 | - | furniture 18, pasties 1 | -259 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 22 @ 13.9; crew 0.2; est +254 a turn; stock: furniture 22 @ 13.9 (keep 145)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 16.1 (keep 14); best orders clear only -5 a turn after crew: ship stays at 0
- best towns now: Amsdermund +579, Gotthafen +468, Heidlowe +390, Bedenis +388, Vauxvais +388
- Amsdermund would trade: furniture buy 53 @ 13.7; crew 0.9

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~104 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 1.00 (104/turn) | timber 41 (7.72->12.63), bread 148 (2.33->2.77), firewood 31 (3.09->5.75), charcoal 17 (2.96->5.18) | beer 118 (3.36->4.12), ham 0 (112.35->132.05), dyed cloth 1 (11.34->13.39), cheese 2 (6.72->7.5) | +447 |
| Pontmont | 341 | 0.10 | 1.00 (104/turn) | firewood 25 (3.09->8.07), bread 77 (2.33->3.1), looms 0 (651->674.5), tiles 4 (4.39->6.6) | ham 0 (119.7->132.05), beer 61 (3.89->4.12), cookware 1 (21->22.23), logs 1 (4.2->7.22) | +123 |
| Gotthafen | 964 | 0.32 | 0.10 (10/turn) | garments 10 (22.8->30.59), nets 3 (34.6->38.57), leather 1 (23.1->24.51), wine 3 (6.46->7.22) | ham 1 (109.2->132.05), yarn 6 (3.68->4.8), cheese 3 (6.3->7.5), dyed cloth 2 (11.97->13.39) | +121 |
| Fontaux | 411 | 0.11 | 1.00 (104/turn) | timber 9 (7.72->11.78), firewood 11 (3.09->8.36), thread 23 (4.78->5.65), charcoal 9 (2.96->5.13) | ham 0 (112.35->132.05), cheese 1 (7.25->7.5) | +105 |
| Darmwald | 1022 | 0.35 | 0.70 (73/turn) | charcoal 19 (2.96->7.31), nets 4 (34.6->38.76), leather 1 (23.1->32.3), arms 5 (32.76->34.58) | ham 1 (110.25->132.05), salt 12 (4.66->5.56), garments 2 (21.63->24.8), cheese 3 (6.3->7.5) | +97 |

**Best:** Grandgues at about +447 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.6, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 3.0 turns |
| beer | 9 @ ?, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 4 = 1.0 turns |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21.2 | goal planner: sells 11 at 21.2 (v2 had 10 at 22.2) |
| grain | 0 @ 3.7, stop 18 |  | goal planner: buys 0 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 20) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 34.0 |  |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 24.4k (cash + stock at home prices); +49/turn over 6 turns, +15/turn over 24 turns.
- Limits: cash flow >= -212/turn, prestige >= -0.52/turn (values are after 200 tax a turn).
- Today's settings: value +75/turn, cash +31/turn, prestige -2.33/turn - breaks the prestige floor.
- Plan: value +32/turn, cash +37/turn, prestige -0.52/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -612 vs +31, +85 vs +9, -670 vs +27 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Vauxvais: +6/turn
  - ship Flax Wyrm -> Bordetes: +0/turn
  - net maker 0.00 -> 0.39: +15/turn
  - brewery 1 0.14 -> 0.08: +10/turn
  - ropewalk 1 0.25 -> 0.00: +10/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.11: +9/turn
  - spinnery 1 1.65 -> 1.48: +4/turn
  - sewing shop 1 0.30 -> 0.39: -5/turn
  - weavery 1 0.50 -> 0.66: +14/turn
  - mansion 1 0.00 -> 0.43: -101/turn
- Model check over the last 59 turns: predicted -87/turn for the settings we ran, real -87/turn.
- Worth of one more unit per turn: labour 1.66, thread 4.17, cloth 6.66, flax fibres 4.94, garments 19.27, nets 30.33, beer 3.12, timber 3.31, prestige 59.69, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 20); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.11, worth +4/turn.
- Ship linen snake: Grandgues -> Vauxvais (+6/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Bordetes (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new leatherworks (make leather armour 1) for ~3703 coin: +7/turn, payback 515 turns, doesn't pay yet (materials thin at home: nails)

## Chain sizing

Mode HOLD, garments sold 11.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 416 (+125 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.01 |
| ret | 3 | 0.91 | 0.80 |
| spin | 4 | 1.65 | 1.67 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 130/77, thread 1053/227, cloth 72/128

## Self-diagnosis

- R1: beer slot dry: 4.0 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy 7 @ 3.6, home ask none (no sellers at home)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.94; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1053 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
