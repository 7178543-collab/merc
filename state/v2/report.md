# v2 shadow report

Turn 14057, 2026-11-16 02:22. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,678, prestige 3,549 (429 free, -2.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 12 | 0 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 7, buy @ 3.6 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 1 | 1 | 1 | 0 | stop 7, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 36 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21.2 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 17, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 506 | 0 | 23 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 2 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), but the home ask 3.00 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.00 is above our ceiling 2.40 and last turn bought 1 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 2 (need 5) -> v2: buy 5

## Waste (money lost now)

- **labour**: 23 labour expired last turn (~39 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0
- **linen snake**: linen snake cost 10 coin last turn (crew 0.10) and its route traded nothing (route limited by pasties space) -> v2: pause it (crew 0) until a route is proven to sell

## Tuning

- **beer**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.50 is above our ceiling 11.00 and last turn bought 1 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 526, not 626

## Prestige spending, cheapest coin per prestige first

344 turns left: prestige gained now converts 82.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.1 | 50.1 | running |
| jousting 3 | arena | 230 | 56.8 | 57.2 | needs a arena (build cost 26,253); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 57.5 | 57.5 | thin at home: beer, cured fish |
| hold banquet 3 (pies) | mansion | 8 | 59.4 | 59.4 | thin at home: hop beer, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 59.8 | 59.8 | thin at home: hop beer, cured fish |
| hold banquet 2 (fish) | mansion | 6.8 | 60.1 | 60.1 | thin at home: cured fish |
| hold banquet 2 (pies) | mansion | 7 | 61.4 | 61.4 | thin at home: pies |
| jousting 2 | arena | 210 | 62.2 | 62.6 | needs a arena (build cost 26,253); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 63.0 | 63.0 | thin at home: hop beer, ham, stockfish |
| hold banquet 1 (meat) | mansion | 4.2 | 63.4 | 63.4 | thin at home: beer |
| hold banquet 3 (meat) | mansion | 7.6 | 63.7 | 63.7 | thin at home: hop beer |
| hold mass 2 (premium) | cathedral | 360 | 59.8 | 63.7 | needs a cathedral (build cost 310,960); thin at home: furniture, jewellery, glassware, candles, premium garments |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.20 | 20 | 134102075 | 0.376 | - | furniture 22, pasties 1 | -324 |
| linen snake | 0.1 / 0.10 | 10 | 151802239 | 0.168 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: pasties buy 13 @ 15.9; crew 0.1; est +28 a turn; stock: pasties 13 @ 15.9 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 15.6 (keep 14); best orders clear only -7 a turn after crew: ship stays at 0
- best towns now: Chatgnan +532, Bedenis +430, Disscester +332, Boistot +301, Fulkirch +298
- Chatgnan would trade: furniture buy 44 @ 13.9, pasties buy 9 @ 16.3; crew 0.4

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~105 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 1.00 (105/turn) | timber 46 (7.77->12.73), firewood 35 (3.15->5.98), charcoal 19 (3.07->5.18), bread 162 (2.35->2.58) | swords 1 (231->340.1), ham 1 (111.3->132.05), tackles 1 (155.4->171), tiles 4 (4.3->6.65) | +476 |
| Heilegg | 826 | 0.24 | 0.80 (84/turn) | charcoal 19 (3.07->5.98), nets 6 (34.6->37.43), wine 14 (6.67->7.84), beer 81 (3.8->4.35) | swords 1 (231->340.1), ham 1 (109.2->132.05), tools 15 (5.25->6.84), cloth 24 (7.82->8.55) | +228 |
| Hanbrücken | 531 | 0.15 | 0.60 (63/turn) | timber 25 (7.77->12.06), nets 4 (34.6->36.29), flax plants 1 (1.23->2.79), wine 4 (6.67->7.08) | swords 1 (226.8->340.1), ham 1 (109.2->132.05), tackles 1 (155.4->171), casks 3 (5.15->6.17) | +219 |
| Amsdermund | 1111 | 0.40 | 0.30 (31/turn) | wine 14 (6.67->8.5), wool 5 (10.29->11.21), nets 5 (34.6->35.53) | swords 1 (231->340.1), tools 15 (4.83->6.84), ham 1 (111.3->132.05), cloth 24 (7.35->8.55) | +200 |
| Gotthafen | 964 | 0.32 | 0.10 (10/turn) | garments 10 (24.4->29.07), arms 3 (30.87->36.67), nets 1 (34.6->39.52), wine 3 (6.67->7.22) | swords 1 (247.8->340.1), ham 1 (109.2->132.05), cloth 12 (7.56->8.55), cheese 4 (6.25->7.41) | +191 |

**Best:** Grandgues at about +476 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 30.8, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 3.0 turns |
| beer | 7 @ ?, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 12 = 3.0 turns |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 16 = 3.9 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 2 @ 2.4, stop 7 |  | goal planner: buys 2 a turn for today's rates, keeps up to 7 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21.2 | goal planner: sells 11 at 21.2 (v2 had 10 at 23.8) |
| grain | 0 @ 3.7, stop 18 |  | goal planner: buys 0 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 26) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 34.0 |  |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 74.0 |  |
| tar | 1 @ 11.0, stop 2 |  | uses 0.4/turn (ropewalk 1), makes 0.0, holds 1 = 1.5 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 24.5k (cash + stock at home prices); +125/turn over 6 turns, +4/turn over 24 turns.
- Limits: cash flow >= -237/turn, prestige >= -0.54/turn (values are after 200 tax a turn).
- Today's settings: value +57/turn, cash +9/turn, prestige -2.32/turn - breaks the prestige floor.
- Plan: value +19/turn, cash +23/turn, prestige -0.54/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +187 vs +44, +20 vs +31, -612 vs +31 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Hanstein: +17/turn
  - ship Flax Wyrm -> Bedenis: +0/turn
  - brewery 1 0.14 -> 0.08: +12/turn
  - net maker 0.00 -> 0.29: +11/turn
  - ropewalk 1 0.25 -> 0.00: +14/turn
  - spinnery 1 1.65 -> 1.39: +11/turn
  - flax farm 1 4.64 -> 4.34: -5/turn
  - sewing shop 1 0.30 -> 0.40: -2/turn
  - weavery 1 0.50 -> 0.66: +15/turn
  - mansion 1 0.00 -> 0.42: -101/turn
- Model check over the last 59 turns: predicted -98/turn for the settings we ran, real -97/turn.
- Worth of one more unit per turn: labour 1.67, thread 4.20, cloth 6.70, flax fibres 4.97, garments 19.39, nets 30.55, beer 2.98, timber 3.33, prestige 61.29, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 2 (v2 5); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 26); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.05, worth +3/turn.
- Ship linen snake: Grandgues -> Hanstein (+17/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Bedenis (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 11.4/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 414 (+124 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 3.92 |
| ret | 3 | 0.91 | 0.78 |
| spin | 4 | 1.65 | 1.67 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 136/77, thread 1050/227, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask 3.0; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
