# v2 shadow report

Turn 14154, 2026-11-20 03:35. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 12,917, prestige 3,626 (506 free, +1.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 20 | 39 | 19 | 0 | 0 | stop 60, buy 39, buy @ 4.78 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 34 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 65 | 65 | 519 | 0 | 46 | buy 65, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.90 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.90 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.20 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 46 labour expired last turn (~94 coin): holding 65 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **beer**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.20 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 94 over real use lately; planning 524, not 619
- labour expiry guard: 46 bought labour expired last turn, buy 19 (not 24) this turn

## Prestige spending, cheapest coin per prestige first

247 turns left: prestige gained now converts 71.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 51.0 | 51.3 | needs a arena (build cost 28,418); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 52.5 | 53.1 | needs a arena (build cost 28,418); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 54.8 | 55.1 | needs a arena (build cost 28,418); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 57.6 | 57.6 | thin at home: cheese, pies |
| hold banquet 2 (pies) | mansion | 7 | 57.9 | 57.9 | thin at home: wine, cheese, pies |
| hold banquet 4 (pies) | mansion | 18 | 58.1 | 58.1 | thin at home: wine, stockfish, cheese |
| jousting 2 | arena | 210 | 57.5 | 58.2 | needs a arena (build cost 28,418); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 60.6 | 60.6 | running |
| hold banquet 4 (premium) | mansion | 20 | 61.5 | 61.5 | thin at home: wine, stockfish |
| hold banquet 2 (fish) | mansion | 6.8 | 62.9 | 62.9 | thin at home: wine, cheese |
| hold banquet 4 | mansion | 17.5 | 63.2 | 63.2 | thin at home: wine, stockfish, cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 63.8 | 63.8 | thin at home: beer |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: cured meat buy 6 @ 20.4, pasties buy 5 @ 15.9; crew 0.1; est +44 a turn; stock: pasties 5 @ 15.9 (keep 14)
- **Flax Wyrm** on Caillechâtel: beer buy 19 @ 3.78, cured meat buy 4 @ 22.8, pasties buy 2 @ 12.3; crew 0.1; est +36 a turn; stock: pasties 2 @ 12.3 (keep 14)
- best towns now: Cobholme +357, Fulkirch +331, Nürnnieder +236, Bedenis +234, Clairlond +223
- Cobholme would trade: furniture buy 40 @ 14.2; crew 1.0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~131 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Kirchwerp | 1072 | 0.47 | 0.40 (52/turn) | swords 3 (275.1->351.5), arms 7 (33.81->40.28), candles 2 (59.85->72.2), nets 6 (36.8->40.28) | canvas 7 (37.38->39.71), cheese 6 (6.62->8.69), cloth 3 (12.08->14.1), garments 2 (31.5->34.4) | +370 |
| Grandgues | 152 | 0.05 | 0.40 (52/turn) | bread 235 (3.02->4.01), thread 92 (6.05->6.84), tiles 4 (3.78->7.17), candles 2 (59.85->64.12) | cured meat 6 (21->27.4), cheese 6 (6.77->8.69), cloth 4 (12.39->14.1), casks 4 (7.88->8.55) | +363 |
| Amsdermund | 1111 | 0.50 | 0.40 (52/turn) | flour 4 (20.79->27.74), nets 6 (36.8->39.71), candles 2 (59.85->65.08), pies 1 (15.02->20.14) | cloth 24 (9.71->14.1), cured meat 6 (21->27.4), casks 6 (5.35->8.55), cheese 6 (6.3->8.69) | +215 |
| Heilegg | 826 | 0.30 | 0.20 (26/turn) | candles 2 (59.85->71.25), flour 4 (20.79->26.79), pies 2 (15.02->18.52), tallow 1 (18.69->23.56) | cloth 24 (10.24->14.1), salt 9 (3.89->5.56), cheese 6 (6.62->8.69), cured meat 6 (25.2->27.4) | +190 |
| Fontaux | 411 | 0.14 | 1.00 (131/turn) | thread 56 (6.05->7.27), timber 34 (9.35->12.44), candles 2 (59.85->73.15), nets 6 (36.8->38.76) | cured meat 4 (23.31->27.4), cheese 6 (7.25->8.69), tools 18 (6.62->7.17), casks 6 (7.35->8.55) | +188 |

**Best:** Kirchwerp at about +370 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.8, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 4.0 turns |
| beer | 39 @ ?, stop 77 |  | uses 19.2/turn (household upkeep, mansion 1), makes 0.0, holds 20 = 1.0 turns |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 16 = 3.9 turns |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 8 = 1.3 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 33.2) |
| grain | 0 @ 3.7, stop 18 |  | goal planner: buys 0 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 19) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 35.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 29.4k (cash + stock at home prices); +102/turn over 6 turns, -19/turn over 24 turns.
- Limits: cash flow >= -372/turn, prestige >= -0.86/turn (values are after 200 tax a turn).
- Today's settings: value -102/turn, cash -110/turn, prestige +1.48/turn.
- Plan: value +78/turn, cash +84/turn, prestige -0.86/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -383 vs -169, -644 vs -178, +113 vs -178 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship Flax Wyrm -> no route: +0/turn
  - mansion 1 1.00 -> 0.44: +130/turn
  - brewery 1 0.14 -> 0.08: +12/turn
  - ropewalk 1 0.25 -> 0.16: +11/turn
  - spinnery 1 1.65 -> 1.30: +10/turn
  - net maker 0.00 -> 0.29: +4/turn
  - retting pit 1 0.91 -> 0.82: +3/turn
  - flax farm 1 4.64 -> 4.14: +6/turn
- Model check over the last 59 turns: predicted -6/turn for the settings we ran, real +67/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.66, beer 3.53, timber 3.69, prestige 58.25, cash 0.00
- Orders it would set: candles buy 2 (v2 None); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 64 (v2 19); light armour buy 1 (v2 None); rope sell 1 (v2 none)
- Ship linen snake: stays on Grandgues (worth +16/turn).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +88/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 426 (+137 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.53 |
| ret | 3 | 0.91 | 0.91 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 94/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R1: cured meat slot dry: 7.7 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 4 @ 27.2, home ask 27.4 -> **buy 12 @ 28 (ask 27.4, cap 42.0)** (ok)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.9; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
- R5: tar buy not filling: bid 11 under the home ask 11.2 for 4 turns, bought 0.0 of 1, 0.0 held (0.0 turns); raise needs Taylor (ceiling 11.0)
