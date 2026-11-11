# v2 shadow report

Turn 13938, 2026-11-11 03:32. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 6,676, prestige 3,502 (382 free, -2.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 17 | 0 | 4 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.96 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.96 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~80 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: +2 crew for Flax Wyrm (crew 0.04, no projection from the game)
- labour: projection runs 100 over real use lately; planning 485, not 585

## Prestige spending, cheapest coin per prestige first

463 turns left: prestige gained now converts 90.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 52.2 | 52.2 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 55.4 | 55.4 |  |
| jousting 3 | arena | 230 | 56.1 | 56.4 | needs a arena (build cost 29,014); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 57.3 | 57.3 | thin at home: wine, ham, stockfish, cheese, pies, candles |
| hold banquet 4 (premium) | mansion | 20 | 59.6 | 59.6 | thin at home: wine, ham, stockfish, candles |
| hold banquet 4 | mansion | 17.5 | 60.1 | 60.1 | thin at home: wine, ham, stockfish, cheese, candles |
| hold banquet 1 (meat) | mansion | 4.2 | 60.3 | 60.3 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 60.8 | 60.8 | thin at home: cheese |
| jousting 2 | arena | 210 | 61.4 | 61.8 | needs a arena (build cost 29,014); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 62.1 | 62.1 | thin at home: wine, cheese |
| hold banquet 3 (pies) | mansion | 8 | 63.1 | 63.1 | thin at home: cheese, pies, candles |
| hold banquet 3 (meat) | mansion | 7.6 | 63.9 | 63.9 | thin at home: cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 19 @ 14.6, pasties buy 10 @ 15.9; crew 0.2; est +233 a turn; stock: furniture 19 @ 14.6 (keep 145); stock: pasties 10 @ 15.9 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 6 @ 16.4 (keep 14); best orders clear only 4 a turn after crew: ship stays at 0
- best towns now: Marmont +271, Dortgart +261, Brebronn +253, Gotthafen +245, Clairlond +242
- Marmont would trade: furniture buy 22 @ 13.1; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~108 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Kirchwerp | 1072 | 0.39 | 0.50 (54/turn) | thread 92 (4.9->5.7), nets 6 (34.6->38.95), fleece 1 (8.4->12.35), premium cheese 1 (34.44->39.14) | cheese 7 (6.2->8.74), cloth 24 (7.35->8.25), flax fibres 9 (5.78->6.75), garments 2 (22.68->24) | +101 |
| Amsdermund | 1111 | 0.41 | 0.20 (22/turn) | cured fish 8 (24.57->30.4), nets 5 (34.6->40.09), tallow 1 (18.06->24.51), wool 6 (9.82->11.21) | cheese 7 (6.62->8.74), tools 17 (5.19->6.03), flax fibres 10 (5.78->6.75), garments 2 (22.89->24) | +97 |
| Angefont | 686 | 0.20 | 0.30 (32/turn) | beer 62 (3.46->4.18), casks 7 (7.3->7.93), tallow 1 (18.06->19.57) | flax fibres 23 (4.73->6.75), thread 49 (4.81->5.4), cheese 7 (7.98->8.74), cloth 12 (7.72->8.25) | +92 |
| Friedwerp | 684 | 0.20 | 0.30 (32/turn) | windows 1 (624.75->669.75), nets 3 (34.6->37.24), beer 57 (3.46->3.97), cured fish 3 (24.57->26.03) | cheese 7 (6.93->8.74), cloth 20 (7.56->8.25), garments 2 (21.42->24), tiles 2 (5.15->8.22) | +90 |
| Hanstein | 380 | 0.11 | 0.80 (86/turn) | premium ham 1 (252->262.2), timber 10 (7.77->10.07), nets 2 (34.6->37.62), tallow 1 (18.06->20.71) | thread 31 (3.82->5.4), cheese 7 (6.98->8.74), tiles 2 (4.73->8.22), garments 2 (23.1->24) | +90 |

**Best:** Kirchwerp at about +101 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 3.46, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.1 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres |  | 1 @ min 6.65 | goal planner: trial sale of an idle pile, 1 a turn at 6.65, keeps 85 (11 over) |
| flax plants |  | 2 @ min 1.18 | goal planner: sells 2 a turn at 1.18, keeps 219 (no one offered it) |
| garments |  | 10 @ min 19.3 | goal planner: sells 10 at 19.3 (v2 had 10 at 23.0) |
| grain | 5 @ 3.7, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 108, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tapestries |  | 1 @ min 665 | goal planner: trial sale of an idle pile, 1 a turn at 665, keeps 0 (6 over) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 29.5k (cash + stock at home prices); -203/turn over 6 turns, +76/turn over 24 turns.
- Limits: cash flow >= -112/turn, prestige >= -0.34/turn (values are after 200 tax a turn).
- Today's settings: value -2/turn, cash -69/turn, prestige -2.12/turn - breaks the prestige floor.
- Plan: value -40/turn, cash -36/turn, prestige -0.34/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -195 vs -44, -147 vs -55, +37 vs -61.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Nürnnieder: +5/turn
  - ship Flax Wyrm -> Marmont: +2/turn
  - brewery 1 0.14 -> 0.07: +15/turn
  - net maker 0.00 -> 0.29: +6/turn
  - ropewalk 1 0.25 -> 0.00: +10/turn
  - spinnery 1 1.65 -> 1.40: +10/turn
  - retting pit 1 0.91 -> 0.79: -1/turn
  - flax farm 1 4.64 -> 3.98: -8/turn
  - mansion 1 0.00 -> 0.42: -80/turn
- Model check over the last 60 turns: predicted +106/turn for the settings we ran, real +148/turn.
- Worth of one more unit per turn: labour 1.58, thread 3.96, cloth 6.32, flax fibres 4.70, garments 18.30, nets 28.78, beer 2.99, timber 3.33, prestige 58.66, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax fibres sell 1 (v2 none); flax plants sell 2 (v2 none); grain buy 5 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None); tapestries sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.04, worth +3/turn.
- Ship linen snake: Grandgues -> Nürnnieder (+5/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Marmont (+2/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +64/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 4.5/turn (+0.0 exported); plan makes 32.4 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 418 (+129 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.41 |
| ret | 3 | 0.91 | 0.88 |
| spin | 4 | 1.65 | 1.65 |
| weave | 3 | 0.50 | 1.26 |
| sew | 2 | 0.30 | 0.79 |

Buffers: flax fibres 96/77, thread 1064/225, cloth 73/126

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.96; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
