# v2 shadow report

Turn 13954, 2026-11-11 19:42. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,522, prestige 3,587 (467 free, -2.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 26 | 6 | 4 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 26, buy 9, buy @ 3.44 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 33 | 0 | 2 | 0 | 0 | min_holding 30, sell 10, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 18, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.10 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~77 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.10 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +7 crew for Flax Wyrm (crew 0.13, no projection from the game)
- labour: +2 crew for linen snake (crew 0.05, no projection from the game)
- labour: projection runs 100 over real use lately; planning 493, not 593

## Prestige spending, cheapest coin per prestige first

447 turns left: prestige gained now converts 89.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.0 | 51.0 | running |
| jousting 3 | arena | 230 | 54.8 | 55.1 | needs a arena (build cost 27,859); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 55.5 | 55.5 | thin at home: ham, stockfish, pies |
| hold banquet 1 (fish) | mansion | 4.2 | 56.7 | 56.7 |  |
| hold banquet 4 (premium) | mansion | 20 | 57.5 | 57.5 | thin at home: ham, stockfish |
| hold banquet 4 | mansion | 17.5 | 58.1 | 58.1 | thin at home: ham, stockfish |
| hold banquet 1 (meat) | mansion | 4.2 | 60.3 | 60.3 |  |
| jousting 2 | arena | 210 | 60.0 | 60.4 | needs a arena (build cost 27,859); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 64.2 | 64.2 |  |
| hold banquet 3 (pies) | mansion | 8 | 64.5 | 64.5 | thin at home: pies |
| hold banquet 2 (fish) | mansion | 6.8 | 65.3 | 65.3 |  |
| hold sermon 2 (candles) | church | 31 | 59.5 | 66.1 | needs a church (build cost 72,979); thin at home: candles, furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: furniture buy 27 @ 14.6, pasties buy 3 @ 16.0; crew 0.1; est +316 a turn; stock: furniture 27 @ 14.6 (keep 145); stock: pasties 3 @ 16.0 (keep 14)
- **Flax Wyrm** on Caillechâtel: furniture buy 19 @ 13.8, pasties buy 6 @ 14.5; crew 0.2; est +244 a turn; stock: furniture 19 @ 13.8 (keep 145); stock: pasties 6 @ 14.5 (keep 14)
- best towns now: Vauxvais +337, Heidlowe +336, Grandgues +316, Amsdermund +308, Chatgnan +298
- Vauxvais would trade: furniture buy 27 @ 14.6, pasties buy 7 @ 14.7; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~108 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Fontaux | 411 | 0.12 | 1.00 (108/turn) | thread 92 (4.66->5.65), charcoal 18 (3.11->5.94), wine 17 (6.46->7.74), bread 134 (2.44->2.91) | flax fibres 20 (7.93->8.95) | +196 |
| Rotterburg | 1056 | 0.38 | 0.20 (22/turn) | garments 10 (23->27.74), dyed cloth 4 (12.81->14.54), nets 3 (38.2->40.28), wine 13 (6.46->7.12) | cloth 24 (7.19->9.95), acid 1 (115.5->150.1), flax fibres 8 (7.46->8.95), cookware 5 (25.62->26.79) | +165 |
| Angefont | 686 | 0.20 | 0.30 (32/turn) | casks 11 (6.25->7.22), thread 65 (4.66->4.89), copper ingots 1 (15.33->16.72) | flax fibres 23 (5.04->8.95), cloth 14 (8.03->9.95), acid 1 (140.7->150.1), tools 15 (4.91->5.65) | +142 |
| Grandgues | 152 | 0.04 | 0.50 (54/turn) | bread 163 (2.44->2.83), charcoal 19 (3.11->4.94), timber 27 (7.67->8.74), ham 1 (81.9->90.25) | cloth 11 (7.67->9.95), acid 1 (137.55->150.1), cheese 5 (9.08->9.97), candles 1 (85.05->86.5) | +142 |
| Kirchwerp | 1072 | 0.39 | 0.50 (54/turn) | thread 92 (4.66->5.42), flax fibres 7 (7.4->8.98), ham 1 (81.9->85.5), pasties 3 (13.97->15.2) | cloth 24 (7.56->9.95), acid 1 (126->150.1), dyed cloth 11 (9.97->11.4), garments 2 (23.1->23.8) | +129 |

**Best:** Fontaux at about +196 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 36.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 3.56, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 26 = 6.2 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres |  | 3 @ min 8.85 | goal planner: sells 3 a turn at 8.85, keeps 85 (no one offered it) |
| flax plants |  | 2 @ min 1.18 | goal planner: sells 2 a turn at 1.18, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 22.4) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 101, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 37.2) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.5/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 25.8k (cash + stock at home prices); -609/turn over 6 turns, -197/turn over 24 turns.
- Limits: cash flow >= -230/turn, prestige >= -0.70/turn (values are after 200 tax a turn).
- Today's settings: value +39/turn, cash +121/turn, prestige -2.55/turn - breaks the prestige floor.
- Plan: value -4/turn, cash +123/turn, prestige -0.70/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +6 vs +76, +667 vs +116, +160 vs +110.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Calange: +17/turn
  - brewery 1 0.14 -> 0.08: +13/turn
  - net maker 0.00 -> 0.29: +7/turn
  - ropewalk 1 0.25 -> 0.00: +8/turn
  - spinnery 1 1.65 -> 1.24: +3/turn
  - retting pit 1 0.91 -> 0.80: -3/turn
  - flax farm 1 4.64 -> 4.01: -10/turn
  - mansion 1 0.00 -> 0.44: -73/turn
- Model check over the last 60 turns: predicted +108/turn for the settings we ran, real +30/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.95, garments 19.30, nets 30.09, beer 3.01, timber 3.29, prestige 58.59, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax fibres sell 3 (v2 none); flax plants sell 2 (v2 none); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.04, worth +2/turn.
- Ship linen snake: Grandgues -> Calange (+17/turn over staying).
- Ship Flax Wyrm: stays on Caillechâtel (worth +1/turn).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +81/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.0/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 416 (+125 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.00 |
| ret | 3 | 0.91 | 0.80 |
| spin | 4 | 1.65 | 1.67 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 130/77, thread 1064/227, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
