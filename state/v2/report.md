# v2 shadow report

Turn 13931, 2026-11-10 20:56. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 7,821, prestige 3,442 (322 free, -1.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 26 | 4 | 4 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 26, buy 9, buy @ 3.36 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 41 | 0 | 2 | 0 | 0 | min_holding 70, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 17 | 0 | 0 | 0 | 0 | min_holding 15, sell 10, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~74 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: +2 crew for Flax Wyrm (crew 0.04, no projection from the game)
- labour: projection runs 100 over real use lately; planning 486, not 586

## Prestige spending, cheapest coin per prestige first

470 turns left: prestige gained now converts 90.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.2 | 49.2 | running |
| hold banquet 2 (fish) | mansion | 6.8 | 54.1 | 54.1 |  |
| hold banquet 1 (fish) | mansion | 4.2 | 54.8 | 54.8 |  |
| hold banquet 4 (pies) | mansion | 18 | 54.8 | 54.8 | thin at home: ham, stockfish |
| hold banquet 3 (fish) | mansion | 7.6 | 55.4 | 55.4 |  |
| jousting 3 | arena | 230 | 55.1 | 55.4 | needs a arena (build cost 27,892); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 56.7 | 56.7 | thin at home: ham, stockfish |
| hold banquet 4 | mansion | 17.5 | 57.1 | 57.1 | thin at home: ham, stockfish |
| hold banquet 2 (meat) | mansion | 6.8 | 57.6 | 57.6 |  |
| hold banquet 3 (meat) | mansion | 7.6 | 58.5 | 58.5 |  |
| hold banquet 2 (pies) | mansion | 7 | 59.1 | 59.1 |  |
| hold banquet 3 (pies) | mansion | 8 | 59.3 | 59.3 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nets sell 1 @ 38.8, pasties buy 8 @ 15.9; crew 0.1; est +16 a turn; stock: pasties 8 @ 15.9 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 6 @ 16.2 (keep 14); best orders clear only 6 a turn after crew: ship stays at 0
- best towns now: Bedenis +246, Herschweig +246, Essenbrucke +237, Marmont +228, Unterhufe +226
- Bedenis would trade: furniture buy 18 @ 14.2, pasties buy 13 @ 15.3; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~102 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Vauxvais | 204 | 0.06 | 0.40 (41/turn) | bread 149 (2.56->3.91), nets 4 (14.44->34.01), flour 4 (26.25->31.16), charcoal 17 (2.79->3.89) | tapestries 2 (719.25->769.5), tools 24 (5.35->5.94), flax fibres 11 (4.83->5.9), garments 14 (23.73->24.51) | +442 |
| Heidlowe | 662 | 0.18 | 0.10 (10/turn) | nets 6 (14.44->38.57) | tapestries 2 (635.25->769.5), coats 2 (88.73->91.2), candles 1 (85.58->88.5), tar 10 (10.71->11.4) | +422 |
| Kirchwerp | 1072 | 0.37 | 0.40 (41/turn) | nets 6 (14.44->37.05), arms 13 (31.08->40.28), lead ore 10 (7.77->10.45), steel ingots 3 (17.75->18.24) | tapestries 3 (719.25->769.5), garments 14 (23.1->24.51), axes 1 (16.8->17.39) | +409 |
| Grandgues | 152 | 0.04 | 0.50 (51/turn) | nets 4 (14.44->35.91), timber 24 (7.77->11.78), charcoal 19 (2.79->4.33), bread 149 (2.56->2.79) | tapestries 3 (703.5->769.5), cloth 11 (7.61->8), candles 1 (87.15->88.5) | +405 |
| Hofkirchen | 991 | 0.32 | 0.20 (20/turn) | nets 6 (14.44->36.67), lead bars 6 (14.6->15.48), grain 2 (2.7->4.43), lead ore 1 (7.77->10.83) | tapestries 3 (703.5->769.5), garments 14 (23.31->24.51), candles 1 (84.53->88.5), coats 2 (88.73->91.2) | +353 |

**Best:** Vauxvais at about +442 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 31.0, stop 1 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 3.0 turns |
| beer | 5 @ 3.46, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 26 = 6.1 turns |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 16 = 3.9 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.18 | goal planner: sells 2 a turn at 1.18, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.6) |
| grain | 0 @ 3.7, stop 20 |  | goal planner: buys 0 a turn for today's rates, keeps up to 20 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 10 @ min 31.4 | goal planner: sells 10 at 31.4 (v2 had 10 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tapestries |  | 1 @ min 785 | goal planner: trial sale of an idle pile, 1 a turn at 785, keeps 0 (6 over) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 31.1k (cash + stock at home prices); +108/turn over 6 turns, +208/turn over 24 turns.
- Limits: cash flow >= -159/turn, prestige >= -0.09/turn (values are after 200 tax a turn).
- Today's settings: value +10/turn, cash -50/turn, prestige -1.82/turn - breaks the prestige floor.
- Plan: value -38/turn, cash -36/turn, prestige -0.09/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +24 vs -3, +46 vs -14, -3631 vs -23 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Corstoft: +14/turn
  - ship Flax Wyrm -> Karlmoor: +7/turn
  - brewery 1 0.14 -> 0.09: +11/turn
  - flax farm 1 4.64 -> 3.59: -6/turn
  - retting pit 1 0.91 -> 0.71: -3/turn
  - sewing shop 1 0.30 -> 0.36: -6/turn
  - weavery 1 0.50 -> 0.61: +7/turn
  - ropewalk 1 0.25 -> 0.00: +11/turn
  - spinnery 1 1.65 -> 1.26: +7/turn
  - mansion 1 0.00 -> 0.41: -70/turn
- Model check over the last 60 turns: predicted +107/turn for the settings we ran, real +145/turn.
- Worth of one more unit per turn: labour 1.56, thread 3.96, cloth 6.30, flax fibres 4.77, garments 18.19, nets 15.84, beer 2.93, timber 3.33, prestige 58.62, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None); tapestries sell 1 (v2 none)
- Ship linen snake: Grandgues -> Corstoft (+14/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Karlmoor (+7/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +70/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

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

Buffers: flax fibres 70/87, thread 1064/255, cloth 73/155
- chain plan needed 540 labour, budget left 510: cut to 510 (sewing capped at 0.97)

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.55 for 6 turns, bought 0.0 of 1, 69.6 held (3.0 turns); raise needs Taylor (ceiling None)
