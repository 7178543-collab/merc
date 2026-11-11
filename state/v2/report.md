# v2 shadow report

Turn 13937, 2026-11-11 02:27. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 6,639, prestige 3,504 (384 free, -2.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 21 | 4 | 4 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26 |
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

**4 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.98 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.98 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~79 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: +2 crew for Flax Wyrm (crew 0.04, no projection from the game)
- labour: projection runs 100 over real use lately; planning 485, not 585

## Prestige spending, cheapest coin per prestige first

464 turns left: prestige gained now converts 90.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.9 | 51.9 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 55.5 | 55.5 |  |
| jousting 3 | arena | 230 | 56.3 | 56.6 | needs a arena (build cost 28,920); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 56.9 | 56.9 | thin at home: wine, ham, stockfish, cheese, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 58.3 | 58.3 | thin at home: cheese |
| hold banquet 4 (premium) | mansion | 20 | 58.9 | 58.9 | thin at home: wine, ham, stockfish |
| hold banquet 4 | mansion | 17.5 | 59.1 | 59.1 | thin at home: wine, ham, stockfish, cheese |
| hold banquet 2 (fish) | mansion | 6.8 | 60.0 | 60.0 | thin at home: wine, cheese |
| hold banquet 1 (meat) | mansion | 4.2 | 60.2 | 60.2 |  |
| hold banquet 3 (meat) | mansion | 7.6 | 61.2 | 61.2 | thin at home: cheese |
| jousting 2 | arena | 210 | 61.7 | 62.0 | needs a arena (build cost 28,920); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 62.8 | 62.8 | thin at home: pasties, cheese, pies |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: pasties buy 9 @ 15.9; crew 0.1; est +16 a turn; stock: pasties 9 @ 15.9 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 6 @ 16.0 (keep 14); best orders clear only 7 a turn after crew: ship stays at 0
- best towns now: Chatgnan +262, Marmont +256, Brebronn +244, Nürnnieder +242, Boistot +230
- Chatgnan would trade: furniture buy 21 @ 13.5, pasties buy 5 @ 16.4; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~107 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Amsdermund | 1111 | 0.41 | 0.40 (43/turn) | windows 1 (577.5->712.5), cured fish 7 (24.57->28.88), nets 3 (34->40.09), lead ore 2 (8.93->15.39) | cloth 24 (7.56->8.95), tools 18 (5.21->5.98), casks 14 (5.46->6.65), cheese 4 (6.62->7.55) | +229 |
| Herschweig | 775 | 0.22 | 0.20 (21/turn) | windows 1 (577.5->764.75), nets 5 (34->35.91), honey 3 (7.72->8.07), lead bars 1 (15.23->15.77) | thread 10 (4.96->5.65), tar 4 (10.34->11.4), candles 1 (87.67->88.5), cheese 4 (7.04->7.55) | +200 |
| Angefont | 686 | 0.20 | 0.40 (43/turn) | windows 1 (577.5->617.5), beer 99 (3.46->4.03), spirits 1 (9.77->10.64), casks 4 (7.51->7.98) | flax fibres 23 (4.73->6.85), thread 49 (4.87->5.65), cloth 12 (7.72->8.95), hides 4 (13.33->14.44) | +143 |
| Kirchwerp | 1072 | 0.39 | 0.30 (32/turn) | windows 1 (577.5->669.75), nets 6 (34->37.81), furniture 7 (15.65->18.24), spirits 1 (9.77->11.3) | cloth 24 (7.61->8.95), cheese 4 (6.2->7.55), garments 2 (22.68->23.2) | +143 |
| Etallaen | 774 | 0.22 | 0.80 (86/turn) | windows 1 (577.5->646), beer 99 (3.46->4.2), charcoal 19 (2.88->5.56), honey 6 (7.72->8.69) | cloth 7 (7.72->8.95), thread 11 (4.96->5.65), tiles 2 (5.25->7.98) | +136 |

**Best:** Amsdermund at about +229 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.8, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 0 = 1.0 turns |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 16 = 3.9 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres |  | 1 @ min 6.75 | goal planner: trial sale of an idle pile, 1 a turn at 6.75, keeps 85 (8 over) |
| flax plants |  | 2 @ min 1.18 | goal planner: sells 2 a turn at 1.18, keeps 219 (no one offered it) |
| garments |  | 10 @ min 19.3 | goal planner: sells 10 at 19.3 (v2 had 10 at 22.0) |
| grain | 0 @ 3.7, stop 17 |  | goal planner: buys 0 a turn for today's rates, keeps up to 17 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tapestries |  | 1 @ min 675 | goal planner: trial sale of an idle pile, 1 a turn at 675, keeps 0 (6 over) |
| tar | 1 @ 11.0, stop 2 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 29.3k (cash + stock at home prices); -291/turn over 6 turns, +71/turn over 24 turns.
- Limits: cash flow >= -110/turn, prestige >= -0.35/turn (values are after 200 tax a turn).
- Today's settings: value +1/turn, cash -61/turn, prestige -2.13/turn - breaks the prestige floor.
- Plan: value -40/turn, cash -37/turn, prestige -0.35/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -214 vs -51, -195 vs -44, -147 vs -55 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Heidlowe: +5/turn
  - ship Flax Wyrm -> no route: +0/turn
  - brewery 1 0.14 -> 0.07: +14/turn
  - net maker 0.00 -> 0.29: +6/turn
  - ropewalk 1 0.25 -> 0.00: -2/turn
  - spinnery 1 1.65 -> 1.37: +20/turn
  - retting pit 1 0.91 -> 0.78: -5/turn
  - flax farm 1 4.64 -> 3.91: -8/turn
  - mansion 1 0.00 -> 0.42: -76/turn
- Model check over the last 60 turns: predicted +106/turn for the settings we ran, real +146/turn.
- Worth of one more unit per turn: labour 1.57, thread 3.96, cloth 6.32, flax fibres 4.70, garments 18.29, nets 28.86, beer 2.96, timber 3.33, prestige 58.56, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax fibres sell 1 (v2 none); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); grain buy 5 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None); tapestries sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.04, worth +3/turn.
- Ship linen snake: Grandgues -> Heidlowe (+5/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +63/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 5.2/turn (+0.0 exported); plan makes 32.4 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 420 (+131 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.47 |
| ret | 3 | 0.91 | 0.89 |
| spin | 4 | 1.65 | 1.66 |
| weave | 3 | 0.50 | 1.26 |
| sew | 2 | 0.30 | 0.79 |

Buffers: flax fibres 92/77, thread 1064/226, cloth 73/126

## Self-diagnosis

- R1: arms slot dry: 0.5 held, 0.5 a turn (gear slot (+0.4 prestige)); our buy 1 @ 30.2, home ask 31.4 -> **buy 1 @ 32 (ask 31.4, cap 48.0)** (ok)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.98; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
