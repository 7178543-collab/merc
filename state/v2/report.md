# v2 shadow report

Turn 14146, 2026-11-19 19:41. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,521, prestige 3,643 (523 free, -0.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 19 | 0 | 14 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 47, buy 12, buy @ 3.48 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 34 | 0 | 0 | 0 | 0 | stop 21, buy 6, buy @ 3.7 |
| labour | 64 | 64 | 507 | 0 | 57 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**6 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (4 @ 29), 4 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.7 turns of cured meat left and buying 4 (need 12) -> v2: buy 12
- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.74 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.74 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.40 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 57 labour expired last turn (~121 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.40 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +1 crew for linen snake (crew 0.01, no projection from the game)
- labour: projection runs 100 over real use lately; planning 508, not 608
- labour expiry guard: 57 bought labour expired last turn, buy 7 (not 8) this turn

## Prestige spending, cheapest coin per prestige first

255 turns left: prestige gained now converts 72.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 51.9 | 52.5 | needs a arena (build cost 28,352); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 | arena | 210 | 56.8 | 57.4 | needs a arena (build cost 28,352); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 58.3 | 58.3 |  |
| hold banquet 2 (pies) | mansion | 7 | 58.4 | 58.4 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 58.8 | 58.8 |  |
| hold banquet 1 (fish) | mansion | 4.2 | 59.0 | 59.0 |  |
| hold banquet 4 (pies) | mansion | 18 | 59.1 | 59.1 | thin at home: stockfish |
| hold banquet 3 (fish) | mansion | 7.6 | 60.5 | 60.5 |  |
| maintain 1 | park | 0.5 | 60.6 | 60.6 | running |
| hold banquet 4 (premium) | mansion | 20 | 61.3 | 61.3 | thin at home: stockfish |
| hold mass 2 (premium) | cathedral | 360 | 56.1 | 62.3 | needs a cathedral (build cost 305,100); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |
| hold banquet 4 | mansion | 17.5 | 63.3 | 63.3 | thin at home: stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: pasties buy 14 @ 16.4; crew 0.1; est +22 a turn; stock: pasties 14 @ 16.4 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- best towns now: Angefont +580, Cobholme +361, Fulkirch +314, Disscester +246, Clairlond +229
- Angefont would trade: cured meat buy 4 @ 22.4, furniture buy 49 @ 14.3, pasties buy 11 @ 15.4; crew 0.5

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~127 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Fontaux | 411 | 0.14 | 1.00 (127/turn) | thread 92 (5.5->7.27), timber 37 (8.35->12.25), beer 87 (3.8->4.41), nets 6 (36.8->38.57) | swords 1 (228.9->233.7), cured meat 4 (24.99->25.4) | +274 |
| Kirchwerp | 1072 | 0.46 | 0.70 (89/turn) | furniture 22 (16.59->20.52), wine 12 (6.93->9.36), dyed cloth 11 (22.26->24.32), pasties 7 (15.33->19) | garments 2 (27.3->34.6), bellows 1 (270.9->285), lathes 1 (189->195.7), wrought iron 1 (15.44->16.15) | +187 |
| Rouhomme | 368 | 0.12 | 1.00 (127/turn) | bread 177 (3.11->3.97), thread 50 (5.5->6.27), timber 25 (8.35->11.4), nets 5 (36.8->38.57) | tools 14 (6.3->6.6) | +165 |
| Grandgues | 152 | 0.05 | 0.50 (64/turn) | timber 30 (8.35->11.4), thread 92 (5.5->6.27), bread 213 (3.11->3.32), nets 2 (36.8->40.28) | - | +164 |
| Amsdermund | 1111 | 0.48 | 0.80 (102/turn) | furniture 22 (16.59->20.9), casks 10 (6.72->8.79), belts 4 (38.22->39.9), thread 71 (5.5->6.03) | cloth 24 (10.19->11.9), cured meat 4 (21->25.4), flax fibres 9 (5.62->8), garments 2 (30.24->34.6) | +142 |

**Best:** Fontaux at about +274 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 35.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 29 @ 3.8, stop 57 |  | uses 14.2/turn (household upkeep), makes 0.0, holds 19 = 1.3 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 6) |
| candles | 2 @ 63.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 3 @ 29.0, stop 11 |  | goal planner: buys 3 a turn for today's rates, keeps up to 11 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 16.2, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 33.2) |
| grain | 0 @ 3.7, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 34 |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 7) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 35.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.4k (cash + stock at home prices); -92/turn over 6 turns, +0/turn over 24 turns.
- Limits: cash flow >= -438/turn, prestige >= -0.93/turn (values are after 200 tax a turn).
- Today's settings: value -137/turn, cash -140/turn, prestige +1.38/turn.
- Plan: value +57/turn, cash +59/turn, prestige -0.93/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -110 vs -158, +46 vs -121, +3 vs -122.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Amsdermund: +19/turn
  - ship Flax Wyrm -> Bordees: +2/turn
  - mansion 1 1.00 -> 0.45: +138/turn
  - brewery 1 0.14 -> 0.00: +20/turn
  - spinnery 1 1.65 -> 1.33: +11/turn
  - ropewalk 1 0.25 -> 0.20: +8/turn
  - net maker 0.00 -> 0.29: +4/turn
  - retting pit 1 0.91 -> 0.79: +2/turn
  - flax farm 1 4.64 -> 3.97: +1/turn
  - brewery 1 [brew mead 1] 0.00 -> 0.09: +5/turn
- Model check over the last 59 turns: predicted +33/turn for the settings we ran, real +72/turn.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.62, beer 3.47, timber 3.58, prestige 63.82, cash 0.00
- Orders it would set: bread buy 5 (v2 6); candles buy 2 (v2 None); cloth sell 1 (v2 none); cured meat buy 3 (v2 12); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); labour buy 64 (v2 7); light armour buy 1 (v2 None); rope sell 1 (v2 none)
- Recipe: brewery 1 brew beer 1 -> brew mead 1 at 0.09, worth +2/turn.
- Ship linen snake: Grandgues -> Amsdermund (+8/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Bordees (+2/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +89/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 425 (+137 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.50 |
| ret | 3 | 0.91 | 0.90 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 95/77, thread 1064/228, cloth 72/128

## Self-diagnosis

- R1: beer slot dry: 19.2 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 12 @ 3.48, home ask 3.62 -> **buy 39 @ 3.68 (ask 3.62, cap 14.4)** (ok)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.74; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
