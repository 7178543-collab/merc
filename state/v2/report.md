# v2 shadow report

Turn 13855, 2026-11-07 16:57. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,000, prestige 3,363 (243 free, -1.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 9 | 1 | 4 | 0 | 0 | min_holding 60, sell 3, sell @ 3.06; stop 26, buy 9, buy @ 3.56 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 2 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 34 | 0 | 0 | 0 | 0 | stop 31, buy 8, buy @ 3.7 |
| labour | 29 | 29 | 507 | 0 | 22 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it

## Waste (money lost now)

- **labour**: 22 labour expired last turn (~36 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **beer**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 507, not 606

## Prestige spending, cheapest coin per prestige first

546 turns left: prestige gained now converts 93.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.1 | 50.1 | running |
| hold banquet 4 (pies) | mansion | 18 | 53.5 | 53.5 | thin at home: wine, ham, stockfish, cheese |
| jousting 3 | arena | 230 | 54.2 | 54.4 | needs a arena (build cost 25,873); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 55.2 | 55.2 | thin at home: beer |
| hold banquet 4 | mansion | 17.5 | 56.9 | 56.9 | thin at home: wine, ham, stockfish, cheese |
| hold banquet 3 (pies) | mansion | 8 | 57.1 | 57.1 | thin at home: pasties, cheese |
| hold banquet 4 (premium) | mansion | 20 | 57.5 | 57.5 | thin at home: wine, ham, stockfish, premium cheese |
| hold banquet 2 (fish) | mansion | 6.8 | 58.2 | 58.2 | thin at home: wine, cheese |
| hold banquet 2 (pies) | mansion | 7 | 58.2 | 58.2 | thin at home: pasties, wine, cheese |
| hold banquet 1 (meat) | mansion | 4.2 | 58.3 | 58.3 | thin at home: beer |
| hold banquet 3 (fish) | mansion | 7.6 | 59.1 | 59.1 | thin at home: cheese |
| jousting 2 | arena | 210 | 59.4 | 59.6 | needs a arena (build cost 25,873); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 16.0 (keep 14); best orders clear only -2 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 9 @ 16.3 (keep 14); best orders clear only 13 a turn after crew: ship stays at 0
- best towns now: Rouhomme +27, Blanans +22, Hanstein +17
- Rouhomme would trade: pasties buy 9 @ 14.7; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~105 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hanstein | 380 | 0.11 | 0.40 (42/turn) | timber 15 (7.25->11.49), charcoal 19 (2.46->3.57), nets 2 (33.6->33.82), tallow 1 (19.64->19.95) | cloth 23 (7.51->9.2), cheese 5 (7.19->9.21), thread 43 (4.96->5.3), acid 1 (108.15->111.15) | +112 |
| Etallaen | 774 | 0.22 | 0.10 (10/turn) | cured fish 6 (25.41->32.68), gold ore 1 (152.25->174.8), nets 6 (33.6->35.72), rope 1 (80->89.77) | cloth 6 (7.35->9.2), candles 1 (78.23->85), flax fibres 6 (5.67->6.2), gears 1 (69.83->71.72) | +101 |
| Neuborn | 780 | 0.22 | 1.00 (105/turn) | firewood 13 (2.48->11.4), charcoal 7 (2.46->6.74), mouldboards 0 (38.22->41.99), gold ore 0 (152.25->155.8) | cloth 7 (6.67->9.2), tapestries 0 (630->660.25), cheese 1 (5.41->9.21), dyed cloth 3 (10.08->11.69) | +100 |
| Bordetes | 831 | 0.24 | 0.20 (21/turn) | medicine 1 (158.55->189.05), dyed cloth 15 (13.12->14.91), cured meat 6 (23.31->25.65), wine 4 (6.09->7.46) | candles 1 (79.28->85), cheese 5 (8.24->9.21), cloth 7 (8.51->9.2), gears 1 (68.25->71.72) | +84 |
| Fontaux | 411 | 0.12 | 1.00 (105/turn) | firewood 16 (2.48->7.5), timber 19 (7.25->10.07), charcoal 13 (2.46->4.39), garments 7 (24.4->26.22) | gears 0 (66.15->71.72), candles 0 (80.85->85), malt 0 (4.58->5.32), flax plants 0 (0.91->1.52) | +82 |

**Best:** Hanstein at about +112 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 29.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 8 @ ?, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 9 = 2.2 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 15, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.8) |
| grain | 8 @ 3.7, stop 31 |  | goal planner: buys 8 a turn for today's rates, keeps up to 31 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 7) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 78.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 23.8k (cash + stock at home prices); +164/turn over 6 turns, -21/turn over 24 turns.
- Limits: cash flow >= -333/turn, prestige >= +2.39/turn (values are after 200 tax a turn).
- Today's settings: value +77/turn, cash +60/turn, prestige -1.42/turn - breaks the prestige floor.
- Plan: value -107/turn, cash -101/turn, prestige +2.39/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +70 vs +66, +158 vs +61, +124 vs +62.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Hofkirchen: +6/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +3/turn
  - ropewalk 1 0.25 -> 0.33: +3/turn
  - spinnery 1 1.65 -> 1.35: -7/turn
  - retting pit 1 0.91 -> 0.77: +3/turn
  - flax farm 1 4.64 -> 3.87: +6/turn
  - weavery 1 0.50 -> 0.31: -41/turn
  - sewing shop 1 0.30 -> 0.18: -9/turn
  - mansion 1 0.00 -> 0.91: -145/turn
- Model check over the last 61 turns: predicted +103/turn for the settings we ran, real +75/turn.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.95, garments 19.30, nets 29.86, beer 3.02, timber 3.49, prestige 56.35, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 2 (v2 3); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 8 (v2 0); labour buy 29 (v2 7); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Hofkirchen (+6/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 440 (+151 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.99 |
| ret | 3 | 0.91 | 1.00 |
| spin | 4 | 1.65 | 1.76 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 537/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 2.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask none (no sellers at home)
- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.2 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
