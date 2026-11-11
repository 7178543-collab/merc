# v2 shadow report

Turn 13935, 2026-11-11 00:16. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 6,981, prestige 3,508 (388 free, +71.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 26 | 5 | 4 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 26, buy 9, buy @ 3.36 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 12 | 0 | 0 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.48 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.48 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~77 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: +2 crew for Flax Wyrm (crew 0.04, no projection from the game)
- labour: projection runs 100 over real use lately; planning 485, not 585

## Prestige spending, cheapest coin per prestige first

466 turns left: prestige gained now converts 90.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.7 | 50.7 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 55.2 | 55.2 |  |
| hold banquet 4 (pies) | mansion | 18 | 55.6 | 55.6 | thin at home: ham, stockfish, pies |
| jousting 3 | arena | 230 | 55.4 | 55.7 | needs a arena (build cost 28,538); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 56.0 | 56.0 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 56.9 | 56.9 |  |
| hold banquet 4 | mansion | 17.5 | 58.0 | 58.0 | thin at home: ham, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 58.4 | 58.4 | thin at home: ham, stockfish, premium cheese |
| hold banquet 3 (meat) | mansion | 7.6 | 59.6 | 59.6 |  |
| hold banquet 3 (pies) | mansion | 8 | 59.6 | 59.6 | thin at home: pies |
| hold banquet 1 (meat) | mansion | 4.2 | 60.7 | 60.7 |  |
| hold banquet 2 (meat) | mansion | 6.8 | 60.9 | 60.9 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: pasties buy 9 @ 15.5; crew 0.1; est +20 a turn; stock: pasties 9 @ 15.5 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 7 @ 16.0 (keep 14); best orders clear only 10 a turn after crew: ship stays at 0
- best towns now: Großmühle +258, Unterhufe +252, Marmont +243, Clairlond +220, Großaue +215
- Großmühle would trade: furniture buy 20 @ 13.5, pasties buy 6 @ 15.4; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~105 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.33 | 0.50 (52/turn) | nets 6 (31.8->39.9), thread 92 (4.88->5.7), flax fibres 10 (6.75->10.16), grain 2 (2.8->5.27) | tapestries 2 (672->679.25), candles 1 (84.53->88), blades 3 (14.7->15.67), casks 11 (6.14->6.98) | +143 |
| Kirchwerp | 1072 | 0.38 | 0.40 (42/turn) | thread 92 (4.88->5.7), nets 6 (31.8->37.62), grain 2 (2.8->3.61), spirits 1 (12.5->13.3) | tapestries 2 (651->679.25), flax fibres 17 (5.78->6.85), candles 1 (84->88), cookware 3 (25.83->26.41) | +136 |
| Heidlowe | 662 | 0.18 | 0.30 (31/turn) | nets 6 (31.8->40.47), beer 50 (3.46->4.48), cheese 9 (7.09->7.69) | candles 1 (84.53->88), gold ore 1 (185.85->190), tiles 2 (3.63->7.22), tar 6 (10.71->11.4) | +96 |
| Pontmont | 341 | 0.10 | 1.00 (105/turn) | timber 37 (7.82->9.97), cheese 9 (7.09->8.6), nets 4 (31.8->34.58), bread 146 (2.54->2.87) | gold ore 2 (185.85->190), cloth 11 (7.35->7.7), flax fibres 6 (6.14->6.85), cookware 3 (25.62->26.41) | +80 |
| Fontaux | 411 | 0.12 | 1.00 (105/turn) | bread 86 (2.54->3.23), thread 57 (4.88->5.32), firewood 13 (2.6->6.74), nets 3 (31.8->34.39) | copper ingots 0 (18.9->19.57) | +77 |

**Best:** Hofkirchen at about +143 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.0, stop 1 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 3.0 turns |
| beer | 5 @ 3.46, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 26 = 6.1 turns |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| cloth |  | 2 @ min 6.95 | goal planner: sells 2 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 1 @ 2.4, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.18 | goal planner: sells 2 a turn at 1.18, keeps 219 (no one offered it) |
| garments |  | 12 @ min 19.3 | goal planner: sells 12 at 19.3 (v2 had 12 at 22.4) |
| grain | 0 @ 3.7, stop 6 |  | goal planner: buys 0 a turn for today's rates, keeps up to 6 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tapestries |  | 1 @ min 695 | goal planner: trial sale of an idle pile, 1 a turn at 695, keeps 0 (6 over) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.7k (cash + stock at home prices); -238/turn over 6 turns, +57/turn over 24 turns.
- Limits: cash flow >= -124/turn, prestige >= -0.37/turn (values are after 200 tax a turn).
- Today's settings: value +30/turn, cash -44/turn, prestige +71.56/turn.
- Plan: value +332/turn, cash +99/turn, prestige +63.56/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -3631 vs -23, -206 vs -41, -214 vs -51 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Brunnham: +8/turn
  - ship Flax Wyrm -> Herschweig: +3/turn
  - park 1 16.00 -> 0.00: +49/turn
  - flax farm 1 4.64 -> 11.00: +23/turn
  - retting pit 1 0.91 -> 2.18: +93/turn
  - net maker [make nets 1] 0.00 -> 0.38: +17/turn
  - ropewalk 1 0.25 -> 0.00: +13/turn
  - brewery 1 0.14 -> 0.03: -1/turn
  - spinnery 1 1.65 -> 2.67: -51/turn
  - ropewalk 1 [make rope 1] 0.00 -> 1.00: +150/turn
- Model check over the last 59 turns: predicted +106/turn for the settings we ran, real +134/turn.
- Worth of one more unit per turn: labour 0.87, thread 2.34, cloth 3.66, flax fibres 3.04, garments 10.44, nets 17.19, beer 2.26, timber 3.33, prestige 0.00, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 2 (v2 none); firewood buy 1 (v2 3); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); grain buy 2 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None); tapestries sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 1.00, worth +9/turn.
- Recipe: net maker make nets 3 -> make nets 1 at 0.38, worth +21/turn.
- Ship linen snake: Grandgues -> Brunnham (+8/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Herschweig (+3/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +44/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot flax farm 1 for ~501 coin: +2/turn, payback 265 turns, doesn't pay yet
- Trim: donate park 1: +96/turn (tax 96 saved).

## Chain sizing

Mode HOLD, garments sold 6.9/turn (+0.0 exported); plan makes 33.2 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 435 (+146 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.81 |
| ret | 3 | 0.91 | 0.96 |
| spin | 4 | 1.65 | 1.70 |
| weave | 3 | 0.50 | 1.30 |
| sew | 2 | 0.30 | 0.81 |

Buffers: flax fibres 85/78, thread 1064/230, cloth 73/130

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.48; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
