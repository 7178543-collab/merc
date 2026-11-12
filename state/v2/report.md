# v2 shadow report

Turn 13975, 2026-11-12 16:14. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,893, prestige 3,533 (413 free, -2.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 9 | 0 | 1 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 26, buy 9, buy @ 3.86 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 35 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 18, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 12.00 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~78 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 12.00 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +2 crew for Flax Wyrm (crew 0.03, no projection from the game)
- labour: projection runs 100 over real use lately; planning 485, not 585

## Prestige spending, cheapest coin per prestige first

426 turns left: prestige gained now converts 88.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.3 | 51.3 | running |
| hold banquet 4 (pies) | mansion | 18 | 54.0 | 54.0 | thin at home: hop beer, ham, stockfish |
| jousting 3 | arena | 230 | 55.0 | 55.3 | needs a arena (build cost 27,110); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 56.1 | 56.1 | thin at home: hop beer, ham, stockfish |
| hold banquet 3 (fish) | mansion | 7.6 | 57.4 | 57.4 | thin at home: hop beer, cured fish, cheese |
| hold banquet 2 (fish) | mansion | 6.8 | 58.0 | 58.0 | thin at home: cured fish, cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 58.5 | 58.5 | thin at home: cured fish |
| hold banquet 4 (premium) | mansion | 20 | 58.5 | 58.5 | thin at home: hop beer, ham, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 58.7 | 58.7 | thin at home: hop beer, pies |
| hold banquet 2 (pies) | mansion | 7 | 60.2 | 60.2 | thin at home: cheese, pies |
| jousting 2 | arena | 210 | 60.2 | 60.6 | needs a arena (build cost 27,110); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (meat) | mansion | 7.6 | 66.1 | 66.1 | thin at home: hop beer, cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 7 @ 14.2, pasties buy 2 @ 14.2; crew 0.1; est +84 a turn; stock: furniture 7 @ 14.2 (keep 145); stock: pasties 2 @ 14.2 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 15.5 (keep 14); best orders clear only -4 a turn after crew: ship stays at 0
- best towns now: Großmühle +91, Bedenis +86, Caillechâtel +84, Unterhufe +84, Herschweig +82
- Großmühle would trade: furniture buy 7 @ 13.6, pasties buy 2 @ 12.8; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~106 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Blanans | 297 | 0.08 | 0.70 (74/turn) | timber 40 (7.61->10.54), limestone 4 (19.74->38.19) | dyed cloth 6 (11.23->16.91), charcoal 19 (2.71->3.46), jewellery 1 (122.85->124.45), cloth 12 (7.56->7.7) | +169 |
| Vauxvais | 204 | 0.06 | 0.10 (11/turn) | windows 1 (735->779), wax 17 (26.25->27.17) | tapestries 1 (630->688.75), dyed cloth 6 (12.18->16.91), cured meat 3 (24.15->25.65), thread 17 (5.35->5.65) | +158 |
| Hanstein | 380 | 0.11 | 0.20 (21/turn) | timber 11 (7.61->10.26), hides 1 (12.18->12.73) | thread 31 (4.2->5.65), dyed cloth 6 (12.5->16.91), flax fibres 12 (5.51->7.1), flax plants 34 (1.32->1.84) | +117 |
| Hofkirchen | 991 | 0.33 | 0.40 (42/turn) | canvas 3 (43.05->44.65), wine 6 (6.88->7.55), chisels 2 (10.19->11.11), grain 2 (2.74->3.63) | dyed cloth 6 (11.97->16.91), gold ore 1 (147->166.25), jewellery 2 (115.5->124.45), flax fibres 23 (5.78->7.1) | +102 |
| Großaue | 1136 | 0.42 | 0.20 (21/turn) | windows 1 (735->807.5), lead ore 4 (9.24->11.69), wine 2 (6.88->7.93) | dyed cloth 6 (13.23->16.91), thread 14 (4.73->5.65), flax fibres 4 (5.99->7.1), nails 3 (6.62->7.31) | +102 |

**Best:** Blanans at about +169 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 90.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 2 @ min 6.95 | goal planner: sells 2 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.14 | goal planner: sells 2 a turn at 1.14, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 21.6) |
| grain | 6 @ 3.7, stop 21 |  | goal planner: buys 6 a turn for today's rates, keeps up to 21 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 109, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 38.4) |
| pasties |  | 1 @ min 15.9 | goal planner: trial sale of an idle pile, 1 a turn at 15.9, keeps 0 (12 over) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.9k (cash + stock at home prices); +95/turn over 6 turns, +155/turn over 24 turns.
- Limits: cash flow >= -371/turn, prestige >= -0.47/turn (values are after 200 tax a turn).
- Today's settings: value +49/turn, cash +22/turn, prestige -2.76/turn - breaks the prestige floor.
- Plan: value -68/turn, cash -65/turn, prestige -0.47/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +150 vs +2, +88 vs +15, +125 vs +22.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Clarfranche: +6/turn
  - ship Flax Wyrm -> Großmühle: +0/turn
  - net maker 0.00 -> 0.29: +6/turn
  - spinnery 1 1.65 -> 1.33: -2/turn
  - retting pit 1 0.91 -> 0.83: +1/turn
  - flax farm 1 4.64 -> 4.17: +4/turn
  - weavery 1 0.50 -> 0.41: -6/turn
  - sewing shop 1 0.30 -> 0.24: -11/turn
  - ropewalk 1 0.25 -> 0.00: -20/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.24: +25/turn
- Model check over the last 61 turns: predicted +105/turn for the settings we ran, real +15/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.95, garments 19.30, nets 30.18, beer 3.10, timber 3.26, prestige 68.07, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 2 (v2 none); firewood buy 1 (v2 3); flax plants sell 2 (v2 none); garments sell 11 (v2 10); grain buy 6 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None); pasties sell 1 (v2 none); rope sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.24, worth +9/turn.
- Ship linen snake: Grandgues -> Clarfranche (+5/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Großmühle (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1865 coin: +3/turn, payback 602 turns, doesn't pay yet

## Chain sizing

Mode HOLD, garments sold 10.1/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 410 (+119 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 3.70 |
| ret | 3 | 0.91 | 0.74 |
| spin | 4 | 1.65 | 1.67 |
| weave | 3 | 0.50 | 1.27 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 150/77, thread 1064/227, cloth 73/127

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
- R5: tar buy not filling: bid 11 under the home ask 12.0 for 3 turns, bought 0.0 of 1, 0.0 held (0.0 turns); raise needs Taylor (ceiling 11.0)
