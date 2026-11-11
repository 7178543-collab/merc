# v2 shadow report

Turn 13948, 2026-11-11 13:28. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 7,788, prestige 3,478 (358 free, -2.5/turn).

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

**3 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.40 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~79 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.40 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 484, not 584

## Prestige spending, cheapest coin per prestige first

453 turns left: prestige gained now converts 89.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.9 | 51.9 | running |
| jousting 3 | arena | 230 | 56.1 | 56.4 | needs a arena (build cost 28,406); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 56.6 | 56.6 |  |
| hold banquet 4 (pies) | mansion | 18 | 57.7 | 57.7 | thin at home: wine, ham, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 60.9 | 60.9 | thin at home: wine, ham, stockfish, premium cheese |
| hold banquet 4 | mansion | 17.5 | 61.0 | 61.0 | thin at home: wine, ham, stockfish |
| jousting 2 | arena | 210 | 61.5 | 61.8 | needs a arena (build cost 28,406); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (meat) | mansion | 4.2 | 62.6 | 62.6 |  |
| hold banquet 3 (pies) | mansion | 8 | 65.4 | 65.4 | thin at home: pies |
| hold banquet 3 (fish) | mansion | 7.6 | 66.6 | 66.6 |  |
| jousting 1 | arena | 170 | 67.0 | 67.4 | needs a arena (build cost 28,406); thin at home: protection, light armour, arms; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 68.0 | 68.0 | thin at home: wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 7 @ 15.9 (keep 14); best orders clear only 10 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 8 @ 16.4 (keep 14); best orders clear only 9 a turn after crew: ship stays at 0
- best towns now: Donaunieder +325, Marmont +323, Chatgnan +308, Brebronn +299, Heidlowe +282
- Donaunieder would trade: furniture buy 25 @ 12.8, pasties buy 6 @ 14.0; crew 0.4

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~111 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Kirchwerp | 1072 | 0.40 | 0.90 (100/turn) | thread 92 (4.72->6.65), arms 5 (32.97->40.28), beer 59 (3.55->4.5), flax fibres 6 (6.6->7.98) | cloth 24 (7.56->11.6), cheese 12 (7.46->11.97), cured meat 6 (21->23.18), garments 2 (23.1->25.2) | +333 |
| Fontaux | 411 | 0.12 | 0.50 (55/turn) | thread 90 (4.72->5.65), beer 59 (3.55->4.8), charcoal 19 (2.79->4.73), flax fibres 6 (6.6->8.17) | cloth 9 (9.24->11.6), ham 1 (78.23->98.8), gold ore 1 (145.95->161.5), cheese 12 (11.03->11.97) | +230 |
| Heilegg | 826 | 0.25 | 0.60 (66/turn) | thread 46 (4.72->5.22), arms 5 (32.97->34.96), lead ore 8 (9.61->11.3), charcoal 19 (2.79->4.89) | cloth 24 (7.72->11.6), cheese 12 (5.78->11.97), cookware 3 (20.48->23.75), garments 2 (22.89->25.2) | +202 |
| Brebronn | 862 | 0.27 | 0.40 (44/turn) | nets 3 (40.4->41.04) | cloth 24 (7.82->11.6), cheese 12 (6.41->11.97), wrought iron 3 (11.03->16.05), tools 15 (4.77->5.61) | +177 |
| Friedwerp | 684 | 0.20 | 0.10 (11/turn) | cured fish 3 (24.57->26.41), thread 8 (4.72->5.22), dyed yarn 1 (5.15->5.51) | cloth 24 (8.24->11.6), cheese 12 (7.3->11.97), ham 1 (83.48->98.8), furniture 1 (15.33->17) | +153 |

**Best:** Kirchwerp at about +333 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 89.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres |  | 2 @ min 6.4 | goal planner: sells 2 a turn at 6.4, keeps 85 (no one offered it) |
| flax plants |  | 2 @ min 1.18 | goal planner: sells 2 a turn at 1.18, keeps 219 (no one offered it) |
| garments |  | 10 @ min 19.3 | goal planner: sells 10 at 19.3 (v2 had 10 at 24.4) |
| grain | 0 @ 3.7, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 35 |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 98.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 39.2) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 29.0k (cash + stock at home prices); +139/turn over 6 turns, +2/turn over 24 turns.
- Limits: cash flow >= -158/turn, prestige >= -0.24/turn (values are after 200 tax a turn).
- Today's settings: value +26/turn, cash +28/turn, prestige -2.50/turn - breaks the prestige floor.
- Plan: value -50/turn, cash +14/turn, prestige -0.24/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +150 vs +13, -6 vs +12, +177 vs +26.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Angefont: +23/turn
  - ship Flax Wyrm -> Essenbrucke: +3/turn
  - brewery 1 0.14 -> 0.00: +24/turn
  - net maker 0.00 -> 0.29: +6/turn
  - ropewalk 1 0.25 -> 0.00: +7/turn
  - flax farm 1 4.64 -> 3.99: -2/turn
  - retting pit 1 0.91 -> 0.79: -2/turn
  - brewery 1 [brew beer 2] 0.00 -> 0.08: -12/turn
  - spinnery 1 1.65 -> 1.34: -6/turn
  - mansion 1 0.00 -> 0.54: -99/turn
- Model check over the last 60 turns: predicted +106/turn for the settings we ran, real +101/turn.
- Worth of one more unit per turn: labour 1.57, thread 3.96, cloth 6.32, flax fibres 4.70, garments 18.29, nets 28.95, beer 3.02, timber 3.33, prestige 60.75, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax fibres sell 2 (v2 none); flax plants sell 2 (v2 none); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Recipe: brewery 1 brew beer 1 -> brew beer 2 at 0.08, worth +4/turn.
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.04, worth +3/turn.
- Ship linen snake: Grandgues -> Angefont (+23/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Essenbrucke (+3/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +72/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~2078 coin: +1/turn, payback 2776 turns, doesn't pay yet (materials thin at home: limestone)

## Chain sizing

Mode HOLD, garments sold 7.8/turn (+0.0 exported); plan makes 32.4 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 414 (+125 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.11 |
| ret | 3 | 0.91 | 0.82 |
| spin | 4 | 1.65 | 1.66 |
| weave | 3 | 0.50 | 1.27 |
| sew | 2 | 0.30 | 0.79 |

Buffers: flax fibres 120/77, thread 1064/226, cloth 73/127

## Self-diagnosis

- R1: beer slot dry: 0.0 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy none, home ask 3.38 -> **buy 9 @ 3.44 (ask 3.38, cap 5.7)** (ok)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
