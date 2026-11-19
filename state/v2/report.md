# v2 shadow report

Turn 14147, 2026-11-19 20:52. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,701, prestige 3,643 (523 free, -0.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 5 | 0 | 14 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 47, buy 39, buy @ 3.68 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 1 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 34 | 0 | 0 | 0 | 0 | stop 19, buy 5, buy @ 3.7 |
| labour | 64 | 64 | 507 | 0 | 57 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**6 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), 4 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.78 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.78 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.9 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 10.90 x8, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 57 labour expired last turn (~116 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **beer**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 507, not 597
- labour expiry guard: 57 bought labour expired last turn, buy 7 (not 7) this turn

## Prestige spending, cheapest coin per prestige first

254 turns left: prestige gained now converts 72.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 47.6 | 47.9 | needs a arena (build cost 28,357); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 51.2 | 51.6 | needs a arena (build cost 28,357); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 51.8 | 52.4 | needs a arena (build cost 28,357); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 | arena | 210 | 56.8 | 57.4 | needs a arena (build cost 28,357); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 58.9 | 58.9 |  |
| hold banquet 2 (pies) | mansion | 7 | 59.6 | 59.6 |  |
| hold banquet 4 (pies) | mansion | 18 | 59.8 | 59.8 | thin at home: stockfish |
| hold banquet 2 (fish) | mansion | 6.8 | 60.0 | 60.0 | thin at home: cheese |
| maintain 1 | park | 0.5 | 60.6 | 60.6 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 60.9 | 60.9 | thin at home: beer |
| hold banquet 3 (fish) | mansion | 7.6 | 61.0 | 61.0 | thin at home: cheese |
| hold banquet 4 (premium) | mansion | 20 | 62.0 | 62.0 | thin at home: stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0.2 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: cured meat buy 4 @ 24.2, pasties buy 14 @ 16.0; crew 0.1; est +38 a turn; stock: pasties 14 @ 16.0 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 11.5 (keep 14); best orders clear only 13 a turn after crew: ship stays at 0
- best towns now: Angefont +604, Cobholme +360, Fulkirch +322, Disscester +242, Clairlond +231
- Angefont would trade: cured meat buy 4 @ 22.4, furniture buy 49 @ 14.1, pasties buy 14 @ 15.5; crew 0.5

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~128 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.60 (76/turn) | bread 217 (3.09->3.76), timber 40 (9.13->12.35), thread 92 (5.5->6.27), flour 4 (23.31->28.5) | cured meat 4 (24.99->26.6), yarn 6 (8.03->8.74) | +324 |
| Rouhomme | 368 | 0.12 | 0.80 (102/turn) | bread 217 (3.09->4.07), thread 60 (5.5->6.27), flour 4 (23.31->32.68), nets 6 (36.8->38.57) | tools 17 (6.3->6.65), blades 1 (20.79->22.99), cured meat 4 (25.83->26.6) | +231 |
| Fontaux | 411 | 0.14 | 0.70 (89/turn) | thread 92 (5.5->7.27), timber 30 (9.13->12.44), candles 1 (61.95->69.35), tar 7 (11.45->12.25) | cured meat 4 (24.36->26.6), plate armour 1 (1323->1330), ploughs 1 (69.83->76), yarn 2 (7.04->8.74) | +223 |
| Kirchwerp | 1072 | 0.46 | 0.90 (115/turn) | dyed cloth 11 (22.89->27.36), thread 92 (5.5->6.32), pasties 7 (15.33->21.09), furniture 13 (16.8->20.33) | garments 2 (27.3->35), flax fibres 13 (7.61->8.65), lathes 1 (189->195.7), cured meat 4 (25.41->26.6) | +211 |
| Heilegg | 826 | 0.29 | 0.30 (38/turn) | wrought iron 8 (18.69->27.55), casks 6 (6.77->10.73), candles 1 (61.95->72.2), varnish 10 (17.12->18.43) | yarn 28 (7.35->8.74), garments 2 (31.5->35), cured meat 4 (24.99->26.6), flax fibres 2 (7.77->8.65) | +159 |

**Best:** Grandgues at about +324 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 35.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 30 @ ?, stop 60 |  | uses 15.0/turn (household upkeep), makes 0.0, holds 5 = 0.3 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 8) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (observed), makes 0.0, holds 3 = 0.5 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 16.5, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 33.4) |
| grain | 5 @ 3.7, stop 19 |  | goal planner: buys 5 a turn for today's rates, keeps up to 19 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 7) |
| light armour | 1 @ 101, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 35.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.6k (cash + stock at home prices); +32/turn over 6 turns, +5/turn over 24 turns.
- Limits: cash flow >= -446/turn, prestige >= -0.93/turn (values are after 200 tax a turn).
- Today's settings: value -155/turn, cash -159/turn, prestige +1.38/turn.
- Plan: value +35/turn, cash +38/turn, prestige -0.93/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +46 vs -121, +3 vs -122, +180 vs -140.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Hofkirchen: +18/turn
  - ship Flax Wyrm -> Amsdermund: +5/turn
  - mansion 1 1.00 -> 0.45: +139/turn
  - brewery 1 0.14 -> 0.08: +15/turn
  - spinnery 1 1.65 -> 1.33: +11/turn
  - ropewalk 1 0.25 -> 0.18: +10/turn
  - net maker 0.00 -> 0.29: +5/turn
  - retting pit 1 0.91 -> 0.80: +1/turn
  - flax farm 1 4.64 -> 4.00: +7/turn
- Model check over the last 59 turns: predicted +26/turn for the settings we ran, real +68/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.65, beer 3.43, timber 3.69, prestige 63.65, cash 0.00
- Orders it would set: bread buy 5 (v2 8); cloth sell 1 (v2 none); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 64 (v2 7); light armour buy 1 (v2 None); rope sell 1 (v2 none)
- Ship linen snake: Grandgues -> Hofkirchen (+10/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Amsdermund (+2/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +89/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 425 (+136 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.48 |
| ret | 3 | 0.91 | 0.90 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 97/77, thread 1064/228, cloth 72/128

## Self-diagnosis

- R1: beer slot dry: 5.0 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 39 @ 3.68, home ask none (no sellers at home)
- R1: firewood slot dry: 1.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.78; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
