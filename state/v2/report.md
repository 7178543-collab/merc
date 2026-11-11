# v2 shadow report

Turn 13947, 2026-11-11 12:22. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 7,610, prestige 3,481 (361 free, -2.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 0 | 0 | 0 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 32 | 0 | 2 | 0 | 0 | min_holding 30, sell 10, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 21, buy 6, buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 3.44 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.44 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.60 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~79 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: home ask 11.60 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 484, not 584

## Prestige spending, cheapest coin per prestige first

454 turns left: prestige gained now converts 89.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 52.2 | 52.2 | running |
| jousting 3 | arena | 230 | 56.0 | 56.3 | needs a arena (build cost 28,368); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 58.3 | 58.3 | thin at home: beer |
| hold banquet 4 (pies) | mansion | 18 | 58.4 | 58.4 | thin at home: wine, ham, stockfish, pies |
| hold banquet 4 | mansion | 17.5 | 60.7 | 60.7 | thin at home: wine, ham, stockfish, cheese |
| hold banquet 4 (premium) | mansion | 20 | 61.3 | 61.3 | thin at home: wine, ham, stockfish, premium cheese |
| jousting 2 | arena | 210 | 61.3 | 61.7 | needs a arena (build cost 28,368); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (meat) | mansion | 4.2 | 63.6 | 63.6 | thin at home: beer |
| hold banquet 3 (fish) | mansion | 7.6 | 64.7 | 64.7 | thin at home: cheese |
| hold banquet 2 (fish) | mansion | 6.8 | 66.6 | 66.6 | thin at home: wine, cheese |
| jousting 1 | arena | 170 | 66.7 | 67.1 | needs a arena (build cost 28,368); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 67.9 | 67.9 | thin at home: cheese, pies |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 7 @ 15.9 (keep 14); best orders clear only 10 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Donaunieder +312, Marmont +297, Chatgnan +292, Brebronn +272, Angefont +268
- Donaunieder would trade: furniture buy 24 @ 12.8, pasties buy 6 @ 14.0; crew 0.4

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~109 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Kirchwerp | 1072 | 0.39 | 0.50 (55/turn) | thread 92 (4.74->6.65), arms 8 (31.5->40.28), looms 1 (651->669.75), flax fibres 6 (6.4->8.55) | cloth 24 (7.56->9.2), cheese 4 (7.25->10.64), garments 18 (23.1->24.13), cured meat 6 (21->23.18) | +293 |
| Heilegg | 826 | 0.25 | 0.40 (44/turn) | arms 8 (31.5->37.62), looms 1 (651->698.25), lead ore 9 (9.35->12.25), thread 42 (4.74->5.22) | cloth 24 (7.72->9.2), cheese 4 (5.78->10.64), premium cheese 1 (36.54->37.62) | +166 |
| Clairlond | 1288 | 0.52 | 0.10 (11/turn) | wine 6 (7.35->8.5) | windows 1 (619.5->736.25), tin ingots 1 (32.97->36.29) | +116 |
| Hanstein | 380 | 0.11 | 0.10 (11/turn) | belts 5 (39.06->42.94), dyed cloth 4 (10.92->12.73), flax fibres 6 (6.4->7.27), arms 2 (31.5->32.68) | cloth 24 (6.2->9.2), tin ingots 1 (29.4->36.29), premium cheese 1 (36.33->37.62), yarn 4 (4.37->4.67) | +105 |
| Fontaux | 411 | 0.12 | 0.20 (22/turn) | flax fibres 6 (6.4->8.79), charcoal 19 (2.73->4.12), flax plants 1 (1.4->1.69), grain 2 (2.72->3.1) | windows 1 (661.5->736.25), tin ingots 1 (33.39->36.29), cloth 10 (8.93->9.2) | +100 |

**Best:** Kirchwerp at about +293 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 31.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 89.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres |  | 2 @ min 6.4 | goal planner: sells 2 a turn at 6.4, keeps 85 (no one offered it) |
| flax plants |  | 2 @ min 1.18 | goal planner: sells 2 a turn at 1.18, keeps 219 (no one offered it) |
| garments |  | 10 @ min 19.3 | goal planner: sells 10 at 19.3 (v2 had 10 at 24.8) |
| grain | 6 @ 3.7, stop 21 |  | goal planner: buys 6 a turn for today's rates, keeps up to 21 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 99, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 38.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 29.1k (cash + stock at home prices); +150/turn over 6 turns, +4/turn over 24 turns.
- Limits: cash flow >= -150/turn, prestige >= -0.25/turn (values are after 200 tax a turn).
- Today's settings: value +29/turn, cash +26/turn, prestige -2.52/turn - breaks the prestige floor.
- Plan: value -53/turn, cash +11/turn, prestige -0.25/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +67 vs +14, +150 vs +13, -6 vs +12.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Chatgnan: +8/turn
  - ship Flax Wyrm -> Disscester: +1/turn
  - brewery 1 0.14 -> 0.09: +10/turn
  - net maker 0.00 -> 0.29: +6/turn
  - ropewalk 1 0.25 -> 0.00: +6/turn
  - spinnery 1 1.65 -> 1.30: +4/turn
  - retting pit 1 0.91 -> 0.77: -5/turn
  - flax farm 1 4.64 -> 3.88: -9/turn
  - mansion 1 0.00 -> 0.54: -103/turn
- Model check over the last 60 turns: predicted +106/turn for the settings we ran, real +102/turn.
- Worth of one more unit per turn: labour 1.57, thread 3.96, cloth 6.32, flax fibres 4.70, garments 18.29, nets 28.88, beer 3.04, timber 3.33, prestige 61.99, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax fibres sell 2 (v2 none); flax plants sell 2 (v2 none); grain buy 6 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.04, worth +4/turn.
- Ship linen snake: Grandgues -> Chatgnan (+8/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Disscester (+1/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +72/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~2064 coin: +1/turn, payback 1508 turns, doesn't pay yet (materials thin at home: limestone)

## Chain sizing

Mode HOLD, garments sold 7.8/turn (+0.0 exported); plan makes 32.4 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 415 (+126 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.14 |
| ret | 3 | 0.91 | 0.83 |
| spin | 4 | 1.65 | 1.66 |
| weave | 3 | 0.50 | 1.27 |
| sew | 2 | 0.30 | 0.79 |

Buffers: flax fibres 119/77, thread 1064/226, cloth 73/127

## Self-diagnosis

- R1: beer slot dry: 0.0 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy none, home ask none (no sellers at home)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 3.44; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
