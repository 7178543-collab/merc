# v2 shadow report

Turn 14137, 2026-11-19 10:25. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,777, prestige 3,652 (532 free, -0.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 47 | 20 | 12 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 47, buy 12, buy @ 3.72 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 34 | 0 | 0 | 0 | 0 | stop 19, buy 5, buy @ 3.7 |
| labour | 64 | 64 | 515 | 0 | 49 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**6 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), 3 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.78 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.78 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.70 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 49 labour expired last turn (~91 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.70 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 106 over real use lately; planning 515, not 601

## Prestige spending, cheapest coin per prestige first

264 turns left: prestige gained now converts 73.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 50.0 | 50.3 | needs a arena (build cost 27,178); thin at home: protection, light armour, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 53.8 | 54.1 | needs a arena (build cost 27,178); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 54.3 | 54.8 | needs a arena (build cost 27,178); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 55.8 | 55.8 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 56.9 | 56.9 |  |
| hold banquet 4 (pies) | mansion | 18 | 59.2 | 59.2 | thin at home: ham, stockfish, cheese |
| hold banquet 2 (fish) | mansion | 6.8 | 59.9 | 59.9 | thin at home: cheese |
| jousting 2 | arena | 210 | 59.5 | 60.1 | needs a arena (build cost 27,178); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 60.7 | 60.7 | thin at home: cheese |
| hold banquet 2 (pies) | mansion | 7 | 61.0 | 61.0 | thin at home: cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 61.4 | 61.4 | thin at home: cheese |
| hold banquet 4 (premium) | mansion | 20 | 62.1 | 62.1 | thin at home: ham, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 15.3 (keep 14); best orders clear only -8 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 9 @ 16.3 (keep 14); best orders clear only 11 a turn after crew: ship stays at 0
- best towns now: Gotthafen +502, Hofkirchen +470, Cobholme +354, Fulkirch +339, Brunnham +292
- Gotthafen would trade: furniture buy 44 @ 13.7, pasties buy 4 @ 15.1; crew 0.6

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~119 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.70 (83/turn) | thread 102 (4.98->6.46), timber 39 (8.19->12.54), bread 169 (3->3.76), garments 10 (26.4->29.64) | cheese 3 (6.72->7.46), hop beer 2 (8.66->9.5), cloth 7 (11.55->11.6), garments 2 (32.97->33.2) | +471 |
| Fontaux | 411 | 0.13 | 0.60 (72/turn) | thread 102 (4.98->7.27), garments 10 (26.4->34.2), timber 28 (8.19->12.44), seeds 3 (2.75->3.17) | swords 2 (228.9->237.5), jewellery 6 (98.7->99.75), cheese 3 (6.56->7.46), cured meat 3 (24.78->25.4) | +387 |
| Heilegg | 826 | 0.27 | 0.30 (36/turn) | wrought iron 12 (19.01->27.55), coats 4 (91.88->110.2), garments 10 (26.4->30.97), casks 17 (6.77->9.17) | dyed cloth 3 (16.7->18.05), hop beer 2 (8.77->9.5) | +280 |
| Unterhufe | 595 | 0.19 | 0.10 (12/turn) | rope 2 (88.73->106.4), nets 6 (35.8->40.09), thread 34 (4.98->5.61) | tapestries 1 (677.25->745.75), looms 1 (708.75->750.5), cloth 24 (10.61->11.6), dyed cloth 3 (16.28->18.05) | +211 |
| Rouhomme | 368 | 0.12 | 1.00 (119/turn) | garments 10 (26.4->31.54), thread 21 (4.98->7.46), bread 169 (3->3.52), timber 28 (8.19->10.83) | cheese 3 (7.25->7.46) | +163 |

**Best:** Grandgues at about +471 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 12 @ 3.62, stop 47 |  | uses 11.7/turn (household upkeep), makes 0.0, holds 47 = 4.0 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 9) |
| candles | 2 @ 76.0, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had 2) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 3 @ 29.0, stop 11 |  | goal planner: buys 3 a turn for today's rates, keeps up to 11 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 25.8) |
| grain | 5 @ 3.7, stop 19 |  | goal planner: buys 5 a turn for today's rates, keeps up to 19 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 15) |
| light armour | 1 @ 104, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 27.9k (cash + stock at home prices); -410/turn over 6 turns, +60/turn over 24 turns.
- Limits: cash flow >= -449/turn, prestige >= -0.96/turn (values are after 200 tax a turn).
- Today's settings: value -149/turn, cash -142/turn, prestige +1.34/turn.
- Plan: value +12/turn, cash +20/turn, prestige -0.96/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +160 vs -147, -319 vs -134, -29 vs -146.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Angefont: +4/turn
  - ship Flax Wyrm -> Donaunieder: +8/turn
  - mansion 1 1.00 -> 0.45: +132/turn
  - brewery 1 0.14 -> 0.08: +16/turn
  - net maker 0.00 -> 0.28: +4/turn
  - spinnery 1 1.65 -> 1.40: -2/turn
  - retting pit 1 0.91 -> 0.79: +2/turn
  - flax farm 1 4.64 -> 3.98: +7/turn
  - weavery 1 0.50 -> 0.41: -16/turn
- Model check over the last 59 turns: predicted +71/turn for the settings we ran, real +55/turn.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.70, beer 3.43, timber 3.51, prestige 63.59, cash 0.00
- Orders it would set: bread buy 5 (v2 9); cloth sell 1 (v2 none); cured meat buy 3 (v2 12); firewood buy 1 (v2 3); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 64 (v2 15); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Angefont (+5/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Donaunieder (+3/turn over staying).
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

Buffers: flax fibres 73/77, thread 1064/228, cloth 72/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.78; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
