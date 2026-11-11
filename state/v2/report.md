# v2 shadow report

Turn 13939, 2026-11-11 04:38. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 6,594, prestige 3,500 (380 free, -2.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 13 | 0 | 4 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 17, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.96 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.96 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 12.10 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~79 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: home ask 12.10 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +7 crew for Flax Wyrm (crew 0.14, no projection from the game)
- labour: projection runs 100 over real use lately; planning 491, not 591

## Prestige spending, cheapest coin per prestige first

462 turns left: prestige gained now converts 90.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 52.5 | 52.5 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 55.6 | 55.6 |  |
| jousting 3 | arena | 230 | 56.1 | 56.4 | needs a arena (build cost 29,156); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 57.6 | 57.6 | thin at home: wine, ham, stockfish, cheese, pies |
| hold banquet 4 (premium) | mansion | 20 | 59.7 | 59.7 | thin at home: wine, ham, stockfish |
| hold banquet 4 | mansion | 17.5 | 60.4 | 60.4 | thin at home: wine, ham, stockfish, cheese |
| hold banquet 1 (meat) | mansion | 4.2 | 61.4 | 61.4 |  |
| jousting 2 | arena | 210 | 61.4 | 61.7 | needs a arena (build cost 29,156); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 61.9 | 61.9 | thin at home: cheese |
| hold banquet 2 (fish) | mansion | 6.8 | 63.1 | 63.1 | thin at home: wine, cheese |
| hold banquet 3 (pies) | mansion | 8 | 63.9 | 63.9 | thin at home: cheese, pies |
| hold banquet 3 (meat) | mansion | 7.6 | 65.7 | 65.7 | thin at home: cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 19 @ 14.6, pasties buy 10 @ 15.9; crew 0.2; est +232 a turn; stock: furniture 19 @ 14.6 (keep 145); stock: pasties 10 @ 15.9 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Marmont +271, Chatgnan +264, Brebronn +260, Clairlond +247, Hofkirchen +247
- Marmont would trade: furniture buy 22 @ 13.1; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~108 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Darmwald | 1022 | 0.36 | 0.70 (76/turn) | beer 74 (3.57->6.37), garments 10 (18.88->25.08), tapestries 1 (698.25->722), nets 4 (34.2->38) | cheese 5 (7.09->9.21), candles 1 (86.62->87.5), wheels 1 (19.01->20.33) | +255 |
| Kleinburgh | 1440 | 0.60 | 0.20 (22/turn) | tapestries 1 (698.25->817), garments 10 (18.88->25.46), nets 4 (34.2->37.62), coats 1 (100.28->105.45) | acid 1 (117.6->122.55), candles 1 (86.62->87.5) | +197 |
| Etallaen | 774 | 0.23 | 0.50 (54/turn) | garments 10 (18.88->28.69), nets 6 (34.2->39.14), charcoal 19 (2.44->5.56), wine 5 (7.3->8.69) | spirits 1 (10.5->12.54), cloth 7 (8.03->8.35), tiles 1 (5.25->8.5) | +157 |
| Kirchwerp | 1072 | 0.39 | 0.60 (65/turn) | thread 92 (4.92->5.7), furniture 10 (15.65->20.33), nets 6 (34.2->38.95), garments 10 (18.88->20.33) | cheese 7 (6.2->9.21), cloth 24 (7.35->8.35), flax fibres 9 (5.78->6.65), raw cloth 1 (4.6->6.41) | +151 |
| Gotthafen | 964 | 0.33 | 0.10 (11/turn) | garments 10 (18.88->28.31), nets 5 (34.2->40.09), glassware 1 (71.4->82.65), lead bars 5 (14.91->15.29) | cheese 6 (7.77->9.21), salt 4 (4.45->4.94) | +136 |

**Best:** Darmwald at about +255 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 89.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres |  | 2 @ min 6.5 | goal planner: trial sale of an idle pile, 2 a turn at 6.5, keeps 85 (15 over) |
| flax plants |  | 2 @ min 1.18 | goal planner: sells 2 a turn at 1.18, keeps 219 (no one offered it) |
| furniture | 2 @ 15.2, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 10 @ min 19.3 | goal planner: sells 10 at 19.3 (v2 had 10 at 22.4) |
| grain | 5 @ 3.7, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 108, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tapestries |  | 1 @ min 655 | goal planner: trial sale of an idle pile, 1 a turn at 655, keeps 0 (6 over) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.4/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 29.1k (cash + stock at home prices); -298/turn over 6 turns, +50/turn over 24 turns.
- Limits: cash flow >= -108/turn, prestige >= -0.33/turn (values are after 200 tax a turn).
- Today's settings: value -1/turn, cash -70/turn, prestige -2.11/turn - breaks the prestige floor.
- Plan: value -41/turn, cash -38/turn, prestige -0.33/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -147 vs -55, +37 vs -61, -82 vs -68.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Brunnham: +3/turn
  - ship Flax Wyrm -> no route: +0/turn
  - brewery 1 0.14 -> 0.07: +15/turn
  - net maker 0.00 -> 0.19: +4/turn
  - ropewalk 1 0.25 -> 0.00: +4/turn
  - spinnery 1 1.65 -> 1.42: +16/turn
  - retting pit 1 0.91 -> 0.81: -1/turn
  - flax farm 1 4.64 -> 4.05: -7/turn
  - mansion 1 0.00 -> 0.42: -82/turn
- Model check over the last 60 turns: predicted +106/turn for the settings we ran, real +135/turn.
- Worth of one more unit per turn: labour 1.57, thread 3.96, cloth 6.32, flax fibres 4.70, garments 18.29, nets 28.67, beer 3.02, timber 3.33, prestige 58.75, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax fibres sell 2 (v2 none); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); grain buy 5 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None); tapestries sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.02, worth +2/turn.
- Ship linen snake: Grandgues -> Brunnham (+3/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +59/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 4.5/turn (+0.0 exported); plan makes 32.4 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 417 (+129 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.36 |
| ret | 3 | 0.91 | 0.87 |
| spin | 4 | 1.65 | 1.65 |
| weave | 3 | 0.50 | 1.26 |
| sew | 2 | 0.30 | 0.79 |

Buffers: flax fibres 100/77, thread 1064/225, cloth 73/126

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.96; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
