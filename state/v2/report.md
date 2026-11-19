# v2 shadow report

Turn 14138, 2026-11-19 11:31. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,664, prestige 3,650 (530 free, -1.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 46 | 12 | 12 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 47, buy 12, buy @ 3.62 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 34 | 0 | 0 | 0 | 0 | stop 19, buy 5, buy @ 3.7 |
| labour | 64 | 64 | 501 | 0 | 63 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**6 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), 3 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.76 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.76 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.90 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 63 labour expired last turn (~118 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **candles**: home ask 78.50 is above our ceiling 76.00 and last turn bought 1 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: home ask 11.90 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 501, not 601

## Prestige spending, cheapest coin per prestige first

263 turns left: prestige gained now converts 73.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 49.8 | 50.1 | needs a arena (build cost 27,238); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 53.4 | 53.7 | needs a arena (build cost 27,238); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 53.4 | 53.9 | needs a arena (build cost 27,238); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 56.1 | 56.1 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 56.8 | 56.8 |  |
| hold banquet 4 (pies) | mansion | 18 | 58.2 | 58.2 | thin at home: hop beer, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 59.0 | 59.0 | thin at home: hop beer, cheese |
| jousting 2 | arena | 210 | 58.5 | 59.1 | needs a arena (build cost 27,238); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 60.0 | 60.0 | thin at home: hop beer, cheese |
| hold banquet 2 (fish) | mansion | 6.8 | 60.4 | 60.4 | thin at home: cheese |
| hold banquet 2 (pies) | mansion | 7 | 61.2 | 61.2 | thin at home: cheese |
| hold banquet 4 (premium) | mansion | 20 | 61.3 | 61.3 | thin at home: hop beer, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: candles buy 1 @ 75.5, pasties buy 10 @ 16.4; crew 0.1; est +27 a turn; stock: candles 1 @ 75.5 (keep 12); stock: pasties 10 @ 16.4 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 16.0 (keep 14); best orders clear only -5 a turn after crew: ship stays at 0
- best towns now: Gotthafen +498, Cobholme +372, Fulkirch +337, Brunnham +332, Disscester +222
- Gotthafen would trade: furniture buy 44 @ 13.8, pasties buy 4 @ 15.1; crew 0.6

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~120 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Heilegg | 826 | 0.27 | 0.30 (36/turn) | coats 5 (89.25->114), wrought iron 11 (19.01->27.55), casks 15 (6.88->9.17), wine 21 (6.72->7.98) | furniture 1 (17.96->20), raw cloth 3 (9.77->10.16) | +278 |
| Bordees | 1112 | 0.46 | 0.20 (24/turn) | books 1 (624.75->712.5), lathes 2 (182.7->193.8), thread 8 (5.5->6.98) | tapestries 1 (635.25->745.75), ploughs 3 (74.55->83.12), furniture 1 (14.6->20), candles 1 (75.6->78.5) | +235 |
| Grandgues | 152 | 0.05 | 0.50 (60/turn) | timber 40 (8.56->12.35), thread 92 (5.5->6.27), charcoal 19 (2.69->4.84), canvas 2 (42.84->43.7) | cheese 3 (6.72->7.55), garments 2 (32.97->34.2), candles 1 (78.23->78.5), raw cloth 3 (9.97->10.16) | +226 |
| Fontaux | 411 | 0.13 | 1.00 (120/turn) | thread 92 (5.5->7.27), timber 40 (8.56->11.49), nets 6 (35.8->36.67), beer 68 (3.49->3.78) | cheese 3 (6.62->7.55), cloth 18 (11.65->11.8), cured meat 3 (24.99->25.4) | +198 |
| Disscester | 1474 | 0.69 | 0.40 (48/turn) | premium ham 1 (262.5->267.9), nets 1 (35.8->38.19), dyed yarn 1 (5->5.89) | looms 1 (577.5->750.5), ploughs 4 (72.98->83.12), garments 2 (30.24->34.2), furniture 1 (14.38->20) | +197 |

**Best:** Heilegg at about +278 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 13 @ 3.48, stop 47 |  | uses 11.7/turn (household upkeep), makes 0.0, holds 46 = 4.0 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 7) |
| candles | 2 @ 76.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 11 = 7.3 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (observed), makes 0.0, holds 3 = 0.5 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 32.4) |
| grain | 0 @ 3.7, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 34 |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 1) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.2k (cash + stock at home prices); +4/turn over 6 turns, +68/turn over 24 turns.
- Limits: cash flow >= -444/turn, prestige >= -0.96/turn (values are after 200 tax a turn).
- Today's settings: value -136/turn, cash -129/turn, prestige +1.02/turn.
- Plan: value +9/turn, cash +18/turn, prestige -0.96/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -319 vs -134, -29 vs -146, -113 vs -142.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Fulkirch: +8/turn
  - ship Flax Wyrm -> Donaunieder: +6/turn
  - mansion 1 1.00 -> 0.53: +113/turn
  - brewery 1 0.14 -> 0.01: +17/turn
  - net maker 0.00 -> 0.28: +5/turn
  - spinnery 1 1.65 -> 1.41: -0/turn
  - retting pit 1 0.91 -> 0.80: +2/turn
  - flax farm 1 4.64 -> 4.01: +7/turn
  - weavery 1 0.50 -> 0.44: -10/turn
- Model check over the last 59 turns: predicted +67/turn for the settings we ran, real +53/turn.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.80, beer 3.32, timber 3.50, prestige 63.21, cash 0.00
- Orders it would set: bread buy 5 (v2 7); cloth sell 1 (v2 none); firewood buy 1 (v2 3); garments sell 11 (v2 10); labour buy 64 (v2 1); light armour buy 1 (v2 None); rope sell 2 (v2 none)
- Ship linen snake: Grandgues -> Fulkirch (+11/turn over staying).
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

Buffers: flax fibres 77/77, thread 1064/228, cloth 72/128

## Self-diagnosis

- R1: bread slot dry: 0.0 held, 4.2 a turn (basic food slot (+0.3 prestige)); our buy 5 @ 2.6, home ask none (no sellers at home)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.76; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
