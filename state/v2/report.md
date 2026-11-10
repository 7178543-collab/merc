# v2 shadow report

Turn 13925, 2026-11-10 14:49. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,974, prestige 3,453 (333 free, -1.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 14 | 9 | 4 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 26, buy 9, buy @ 3.36 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 32, buy 8, buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 4 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~74 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax fibres**: flax fibres buffer thin: 1.7 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 56
- **tar**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: +6 crew for Flax Wyrm (crew 0.11, no projection from the game)
- labour: projection runs 100 over real use lately; planning 489, not 589

## Prestige spending, cheapest coin per prestige first

476 turns left: prestige gained now converts 90.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.6 | 48.6 | running |
| hold banquet 4 (pies) | mansion | 18 | 54.8 | 54.8 | thin at home: hop beer, ham, stockfish, cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 54.9 | 54.9 | thin at home: beer |
| hold banquet 4 (premium) | mansion | 20 | 56.5 | 56.5 | thin at home: hop beer, ham, stockfish |
| hold banquet 2 (fish) | mansion | 6.8 | 57.1 | 57.1 | thin at home: cheese |
| hold banquet 4 | mansion | 17.5 | 57.5 | 57.5 | thin at home: hop beer, ham, stockfish, cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 58.0 | 58.0 | thin at home: hop beer, cheese |
| jousting 3 | arena | 230 | 58.6 | 58.9 | needs a arena (build cost 26,500); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 59.7 | 59.7 | thin at home: hop beer, cheese |
| hold banquet 2 (pies) | mansion | 7 | 60.5 | 60.5 | thin at home: cheese |
| hold feast 2 | townhouse | 2.6 | 55.5 | 62.4 | needs a townhouse (build cost 8,090) |
| hold banquet 1 (meat) | mansion | 4.2 | 64.1 | 64.1 | thin at home: beer |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: pasties buy 10 @ 15.1; crew 0.1; est +28 a turn; stock: pasties 10 @ 15.1 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Bedenis +215, Chatgnan +206, Marmont +202, Großmühle +197, Clairlond +183
- Bedenis would trade: furniture buy 15 @ 14.0, pasties buy 12 @ 14.8; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~103 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.50 (51/turn) | bread 148 (2.33->3.61), timber 37 (7.88->10.73), garments 10 (18.04->21.47), tools 17 (6.62->7.36) | candles 1 (86.1->87.5), cloth 12 (8.4->8.45), copper ingots 1 (18.69->19.19) | +298 |
| Etallaen | 774 | 0.21 | 1.00 (103/turn) | beer 36 (3.46->6.79), bread 98 (2.33->3.21), garments 6 (18.04->21.85), clay 2 (4.91->19) | flax fibres 10 (4.94->6.8), candles 0 (81.9->87.5), thread 6 (4.96->5.6), cloth 4 (8.19->8.45) | +199 |
| Pontmont | 341 | 0.09 | 1.00 (103/turn) | bread 123 (2.33->3.19), garments 8 (18.04->21.47), timber 30 (7.88->9.97), cured meat 4 (28.56->31.92) | cloth 8 (7.67->8.45), copper ingots 0 (17.75->19.19), flax fibres 2 (6.46->6.8) | +157 |
| Vauxvais | 204 | 0.06 | 0.30 (31/turn) | bread 148 (2.33->3.1), flour 4 (22.68->25.46) | flax fibres 7 (4.94->6.8), thread 9 (4.73->5.6), cloth 8 (7.67->8.45), candles 1 (82.95->87.5) | +130 |
| Angefont | 686 | 0.19 | 0.40 (41/turn) | garments 10 (18.04->21.28), charcoal 19 (2.81->5.32), salt 9 (5.3->5.84), cloth 1 (6.12->6.84) | flax fibres 23 (4.73->6.8), cloth 20 (7.67->8.45), thread 49 (5.3->5.6), dyed cloth 2 (11.97->12.25) | +111 |

**Best:** Grandgues at about +298 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 6 @ 3.88, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 14 = 3.3 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 15, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.4) |
| grain | 7 @ 3.7, stop 27 |  | goal planner: buys 7 a turn for today's rates, keeps up to 27 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 101, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 36.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.4/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.2k (cash + stock at home prices); +318/turn over 6 turns, +217/turn over 24 turns.
- Limits: cash flow >= -332/turn, prestige >= -0.14/turn (values are after 200 tax a turn).
- Today's settings: value +44/turn, cash -3/turn, prestige -1.87/turn - breaks the prestige floor.
- Plan: value -19/turn, cash -16/turn, prestige -0.14/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +146 vs +17, +47 vs +25, +76 vs +9.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Corstoft: +11/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +7/turn
  - ropewalk 1 0.25 -> 0.00: +2/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.09: +17/turn
  - flax farm 1 4.64 -> 3.91: -4/turn
  - retting pit 1 0.91 -> 0.78: -3/turn
  - spinnery 1 1.65 -> 1.37: +8/turn
  - sewing shop 1 0.30 -> 0.36: -4/turn
  - weavery 1 0.50 -> 0.61: +9/turn
- Model check over the last 59 turns: predicted +107/turn for the settings we ran, real +151/turn.
- Worth of one more unit per turn: labour 1.62, thread 4.11, cloth 6.54, flax fibres 4.95, garments 18.89, nets 29.88, beer 3.02, timber 3.83, prestige 63.14, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 7 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.09, worth +5/turn.
- Ship linen snake: Grandgues -> Corstoft (+11/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +80/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1853 coin: +1/turn, payback 1461 turns, doesn't pay yet (materials thin at home: limestone)

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

Buffers: flax fibres 47/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.8 for 6 turns, bought 0.0 of 1, 46.7 held (2.0 turns); raise needs Taylor (ceiling None)
