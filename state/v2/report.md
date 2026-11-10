# v2 shadow report

Turn 13926, 2026-11-10 15:55. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,998, prestige 3,451 (331 free, -1.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 19 | 9 | 4 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 26, buy 9, buy @ 3.36 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 4, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 27, buy 7, buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~73 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **flax fibres**: flax fibres buffer thin: 1.8 turns (target 2) -> v2: lift the maker's rate or hold back sales until it reaches 56
- **tar**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: +2 crew for Flax Wyrm (crew 0.04, no projection from the game)
- labour: projection runs 100 over real use lately; planning 486, not 586

## Prestige spending, cheapest coin per prestige first

475 turns left: prestige gained now converts 90.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.0 | 48.0 | running |
| hold banquet 4 (pies) | mansion | 18 | 54.5 | 54.5 | thin at home: hop beer, ham, stockfish |
| hold banquet 1 (fish) | mansion | 4.2 | 54.7 | 54.7 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 55.1 | 55.1 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 55.8 | 55.8 | thin at home: hop beer |
| hold banquet 4 (premium) | mansion | 20 | 56.3 | 56.3 | thin at home: hop beer, ham, stockfish |
| hold banquet 4 | mansion | 17.5 | 56.9 | 56.9 | thin at home: hop beer, ham, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 58.8 | 58.8 | thin at home: hop beer |
| jousting 3 | arena | 230 | 58.5 | 58.8 | needs a arena (build cost 25,644); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 59.5 | 59.5 |  |
| hold feast 2 | townhouse | 2.6 | 55.4 | 61.8 | needs a townhouse (build cost 7,518) |
| hold banquet 2 (meat) | mansion | 6.8 | 62.4 | 62.4 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: pasties buy 10 @ 15.5; crew 0.1; est +24 a turn; stock: pasties 10 @ 15.5 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 6 @ 15.8 (keep 14); best orders clear only 9 a turn after crew: ship stays at 0
- best towns now: Herschweig +258, Marmont +220, Clairlond +211, Clairas +210, Friedwerp +206
- Herschweig would trade: furniture buy 17 @ 14.2, pasties buy 14 @ 13.1; crew 0.3

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~101 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.60 (60/turn) | bread 149 (2.56->3.61), timber 36 (7.88->10.83), tools 12 (6.72->7.74), tapestries 1 (609->617.5) | furniture 7 (16.07->17), copper ingots 1 (18.79->19.19) | +258 |
| Corstoft | 1496 | 0.59 | 0.30 (30/turn) | tapestries 1 (609->622.25), nets 6 (36.4->38.57), wax 4 (22.89->24.51), hop beer 1 (9.5->13.11) | windows 1 (582.75->745.75), candles 1 (78.23->85), furniture 7 (14.49->17), yarn 1 (4.49->5.08) | +190 |
| Brebronn | 862 | 0.25 | 0.10 (10/turn) | nets 5 (36.4->40.66) | sails 1 (840->978.5), bellows 1 (224.7->243.2), cured meat 8 (22.05->24.7), copper ingots 1 (17.54->19.19) | +190 |
| Etallaen | 774 | 0.21 | 1.00 (101/turn) | bread 135 (2.56->3.8), tapestries 0 (609->665), nets 3 (36.4->41.42), cheese 7 (6.88->7.89) | thread 8 (4.96->5.6), flax fibres 12 (4.94->5.6), spirits 0 (10.5->12.44) | +176 |
| Vauxvais | 204 | 0.06 | 0.30 (30/turn) | bread 149 (2.56->3.29), flour 3 (23.73->29.64), nets 6 (36.4->37.05), cheese 5 (6.88->7.27) | thread 12 (4.3->5.6), windows 1 (735->745.75), flax fibres 8 (4.94->5.6), tools 18 (5.51->5.79) | +145 |

**Best:** Grandgues at about +258 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 31.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had None) |
| beer | 5 @ 3.48, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 19 = 4.4 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 87, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 4 |  | goal planner: buys 1 a turn for today's rates, keeps up to 4 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.4) |
| grain | 7 @ 3.7, stop 27 |  | goal planner: buys 7 a turn for today's rates, keeps up to 27 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 101, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 35.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.4k (cash + stock at home prices); +351/turn over 6 turns, +226/turn over 24 turns.
- Limits: cash flow >= -333/turn, prestige >= -0.13/turn (values are after 200 tax a turn).
- Today's settings: value +41/turn, cash -3/turn, prestige -1.87/turn - breaks the prestige floor.
- Plan: value -24/turn, cash -20/turn, prestige -0.13/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +47 vs +25, +76 vs +9, +24 vs -3.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Corstoft: +9/turn
  - ship Flax Wyrm -> Marmont: +3/turn
  - net maker 0.00 -> 0.19: +5/turn
  - sewing shop 1 0.30 -> 0.36: -5/turn
  - weavery 1 0.50 -> 0.61: +7/turn
  - ropewalk 1 0.25 -> 0.00: +13/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.08: +8/turn
  - flax farm 1 4.64 -> 3.67: -6/turn
  - retting pit 1 0.91 -> 0.73: +1/turn
  - spinnery 1 1.65 -> 1.29: +6/turn
- Model check over the last 59 turns: predicted +107/turn for the settings we ran, real +154/turn.
- Worth of one more unit per turn: labour 1.60, thread 4.02, cloth 6.42, flax fibres 4.76, garments 18.57, nets 29.12, beer 2.93, timber 3.38, prestige 62.95, cash 0.00
- Orders it would set: arms buy 1 (v2 None); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax plants sell 2 (v2 none); garments sell 11 (v2 10); grain buy 7 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.08, worth +4/turn.
- Ship linen snake: Grandgues -> Corstoft (+9/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Marmont (+3/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +79/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1664 coin: +1/turn, payback 1130 turns, doesn't pay yet (materials thin at home: limestone)

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

Buffers: flax fibres 51/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
- R5: flax fibres buy not filling: bid 5.05 under the home ask 5.6 for 6 turns, bought 0.0 of 1, 50.6 held (2.2 turns); raise needs Taylor (ceiling None)
