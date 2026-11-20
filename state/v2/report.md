# v2 shadow report

Turn 14152, 2026-11-20 01:14. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,449, prestige 3,628 (508 free, -3.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 0 | 0 | 0 | 15 | 0 | stop 60, buy 30, buy @ 3.68 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 34 | 0 | 0 | 0 | 0 | stop 22, buy 6, buy @ 3.7 |
| labour | 65 | 65 | 493 | 0 | 72 | buy 65, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.78 is above it); knock-on: mansion 1 (no beer); labour need rises ~53/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.78 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.50 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 72 labour expired last turn (~152 coin): holding 65 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: home ask 2.90 is above our ceiling 2.60 and last turn bought 0 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.50 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 493, not 584

## Prestige spending, cheapest coin per prestige first

249 turns left: prestige gained now converts 71.4% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 47.8 | 48.1 | needs a arena (build cost 28,731); thin at home: protection, light armour, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 51.4 | 51.8 | needs a arena (build cost 28,731); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 52.2 | 52.9 | needs a arena (build cost 28,731); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 | arena | 210 | 57.2 | 57.9 | needs a arena (build cost 28,731); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 60.3 | 60.3 | thin at home: stockfish, cheese |
| hold banquet 2 (pies) | mansion | 7 | 60.5 | 60.5 | thin at home: cheese |
| hold banquet 3 (pies) | mansion | 8 | 61.3 | 61.3 | thin at home: cheese |
| hold banquet 2 (fish) | mansion | 6.8 | 61.5 | 61.5 | thin at home: cheese |
| hold banquet 4 (premium) | mansion | 20 | 62.5 | 62.5 | thin at home: stockfish |
| maintain 1 | park | 0.5 | 63.0 | 63.0 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 63.9 | 63.9 | thin at home: beer |
| hold banquet 3 (fish) | mansion | 7.6 | 63.9 | 63.9 | thin at home: cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 12.2 (keep 14); best orders clear only 6 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 15.7 (keep 14); best orders clear only -4 a turn after crew: ship stays at 0
- best towns now: Angefont +508, Gotthafen +480, Cobholme +351, Chatgnan +234, Clairlond +222
- Angefont would trade: furniture buy 44 @ 13.8, pasties buy 3 @ 16.0; crew 0.4

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~137 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.06 | 0.60 (82/turn) | bread 229 (3.04->3.91), beer 60 (4.94->7.12), thread 99 (6.05->6.84), timber 33 (9.4->10.83) | cloth 5 (11.97->16.7), cured meat 4 (20.27->23.56), candles 1 (76.65->82), cheese 3 (6.77->7.79) | +444 |
| Rouhomme | 368 | 0.14 | 1.00 (137/turn) | beer 60 (4.94->7.84), flour 3 (21->37.81), nets 6 (36.8->39.14), thread 58 (6.05->6.27) | cloth 21 (13.76->16.7), candles 1 (73.5->82), tools 15 (6.3->6.98), garments 2 (31.29->34.6) | +312 |
| Amsdermund | 1111 | 0.52 | 0.50 (69/turn) | blades 5 (20.06->22.61), nets 6 (36.8->39.33), thread 53 (6.05->6.65) | cloth 24 (9.82->16.7), garments 2 (25.2->34.6), axes 3 (17.85->22.42), candles 1 (73.5->82) | +236 |
| Heilegg | 826 | 0.31 | 0.40 (55/turn) | beer 60 (4.94->6.37), wine 9 (6.56->7.79), rope 3 (86.62->88.83), salt 4 (6.41->7.5) | cloth 24 (10.5->16.7), jewellery 4 (100.8->103.55), garments 2 (31.92->34.6), tools 15 (6.41->6.98) | +233 |
| Blanans | 297 | 0.11 | 0.30 (41/turn) | beer 60 (4.94->6.84), nets 6 (36.8->39.9), limestone 4 (18.17->24.89), dyed cloth 5 (22.05->23.37) | cloth 24 (13.12->16.7), axes 3 (21.63->22.42), copper ore 1 (26.67->28.88), garments 2 (34.23->34.6) | +232 |

**Best:** Grandgues at about +444 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 35.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 30 @ 4.92, stop 60 |  | uses 15.0/turn (household upkeep), makes 0.0, holds 0 = 0.0 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 9) |
| cured meat | 4 @ 27.2, stop 14 |  | goal planner: buys 4 a turn for today's rates, keeps up to 14 (v2 had None) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 16, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 32.8) |
| grain | 6 @ 3.7, stop 22 |  | goal planner: buys 6 a turn for today's rates, keeps up to 22 (v2 had 0) |
| labour | 65 @ 2.2, stop - |  | goal planner: buys 65 for today's rates (v2 had 0) |
| light armour | 1 @ 105, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 35.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.7k (cash + stock at home prices); +353/turn over 6 turns, +67/turn over 24 turns.
- Limits: cash flow >= -394/turn, prestige >= -0.87/turn (values are after 200 tax a turn).
- Today's settings: value -169/turn, cash -178/turn, prestige +0.95/turn.
- Plan: value -0/turn, cash +6/turn, prestige -0.87/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -168 vs -159, -158 vs -164, -383 vs -169.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Vauxvais: +5/turn
  - ship Flax Wyrm -> no route: +0/turn
  - mansion 1 1.00 -> 0.57: +115/turn
  - ropewalk 1 0.25 -> 0.16: +11/turn
  - spinnery 1 1.65 -> 1.29: +12/turn
  - retting pit 1 0.91 -> 0.80: +5/turn
  - flax farm 1 4.64 -> 4.02: +7/turn
  - net maker 0.00 -> 0.29: +2/turn
  - weavery 1 0.50 -> 0.43: -18/turn
- Model check over the last 59 turns: predicted +8/turn for the settings we ran, real +95/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.55, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.64, beer 3.38, timber 3.69, prestige 65.78, cash 0.00
- Orders it would set: bread buy 5 (v2 9); cured meat buy 4 (v2 None); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 6 (v2 0); labour buy 65 (v2 0); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Vauxvais (+5/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 430 (+141 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.75 |
| ret | 3 | 0.91 | 0.95 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 90/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R1: beer slot dry: 0.0 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 30 @ 3.68, home ask 4.7 -> **buy 39 @ 4.78 (ask 4.7, cap 14.4)** (ok)
- R1: bread slot dry: 6.6 held, 4.2 a turn (basic food slot (+0.3 prestige)); our buy 5 @ 2.6, home ask 2.9 -> **buy 9 @ 2.96 (ask 2.9, cap 4.3)** (ok)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.78; ask over the cap 2.1 (60 coin per prestige)
- R1: prestige rate -3.25 a turn vs 12-turn median -1.13; likely: dry slot: beer, bread, firewood; mansion 1 projected 0 (beer)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
