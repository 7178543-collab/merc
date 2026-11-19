# v2 shadow report

Turn 14145, 2026-11-19 18:36. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,518, prestige 3,643 (523 free, -1.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 33 | 10 | 12 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 47, buy 12, buy @ 3.48 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 34 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 64 | 64 | 501 | 0 | 63 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**6 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (4 @ 29), 3 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.7 turns of cured meat left and buying 4 (need 12) -> v2: buy 12
- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.76 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.76 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.70 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 63 labour expired last turn (~123 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: home ask 11.70 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +1 crew for linen snake (crew 0.01, no projection from the game)
- labour: projection runs 100 over real use lately; planning 508, not 608
- labour expiry guard: 63 bought labour expired last turn, buy 2 (not 8) this turn

## Prestige spending, cheapest coin per prestige first

256 turns left: prestige gained now converts 72.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 54.8 | 55.4 | needs a arena (build cost 27,931); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 58.4 | 58.4 |  |
| hold banquet 3 (pies) | mansion | 8 | 58.4 | 58.4 | thin at home: pies |
| maintain 1 | park | 0.5 | 58.8 | 58.8 | running |
| hold banquet 4 (pies) | mansion | 18 | 59.2 | 59.2 | thin at home: stockfish |
| hold banquet 2 (pies) | mansion | 7 | 59.3 | 59.3 | thin at home: pies |
| hold banquet 2 (fish) | mansion | 6.8 | 60.1 | 60.1 |  |
| jousting 2 | arena | 210 | 60.0 | 60.7 | needs a arena (build cost 27,931); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 60.9 | 60.9 |  |
| hold banquet 4 (premium) | mansion | 20 | 61.8 | 61.8 | thin at home: stockfish, premium cheese |
| hold mass 2 (premium) | cathedral | 360 | 55.9 | 62.1 | needs a cathedral (build cost 303,000); thin at home: jewellery, glassware, windows, candles, premium garments |
| hold banquet 4 | mansion | 17.5 | 63.5 | 63.5 | thin at home: ham, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: pasties buy 13 @ 16.4; crew 0.1; est +20 a turn; stock: pasties 13 @ 16.4 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 15.5 (keep 14); best orders clear only -5 a turn after crew: ship stays at 0
- best towns now: Angefont +579, Cobholme +364, Fulkirch +305, Brunnham +285, Clairlond +250
- Angefont would trade: cured meat buy 3 @ 21.4, furniture buy 50 @ 14.4, pasties buy 8 @ 15.3; crew 0.5

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~124 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.70 (87/turn) | timber 29 (8.35->12.25), glassware 9 (89.25->97.85), thread 92 (5.5->6.27), bread 208 (3.38->3.76) | bellows 1 (254.1->285), paper 2 (21->23.94), flax fibres 1 (8.56->10.7), flax plants 2 (1.59->1.84) | +403 |
| Amsdermund | 1111 | 0.47 | 0.80 (100/turn) | furniture 24 (16.59->20.9), thread 61 (5.5->6.65), belts 3 (38.22->46.36), hides 4 (13.76->19.38) | flax fibres 10 (5.62->10.7), cloth 24 (10.13->11.9), garments 2 (25.2->35), cured meat 3 (21->25.4) | +287 |
| Fontaux | 411 | 0.14 | 0.90 (112/turn) | thread 92 (5.5->7.27), timber 40 (8.35->12.16), candles 3 (59.85->69.35), nets 5 (36.8->38.38) | flax fibres 4 (8.87->10.7), cured meat 3 (24.36->25.4) | +275 |
| Kirchwerp | 1072 | 0.45 | 1.00 (124/turn) | furniture 21 (16.59->20.71), thread 83 (5.5->6.32), candles 2 (59.85->69.83), blades 1 (20.68->33.25) | flax fibres 11 (6.72->10.7), garments 1 (27.3->35), lathes 0 (189->195.7), wrought iron 0 (15.44->16.15) | +233 |
| Hofkirchen | 991 | 0.39 | 0.40 (50/turn) | nets 6 (36.8->41.61), candles 3 (59.85->66.02), blades 2 (20.68->28.5), casks 5 (6.56->8.55) | flax fibres 23 (6.3->10.7), cloth 23 (10.19->11.9), garments 2 (31.5->35), coats 3 (81.9->84.08) | +193 |

**Best:** Grandgues at about +403 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 35.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 19 @ 3.8, stop 47 |  | uses 11.7/turn (household upkeep), makes 0.0, holds 33 = 2.9 turns |
| bread | 5 @ 3.3, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had None) |
| candles | 2 @ 58.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 4 @ 29.0, stop 14 |  | goal planner: buys 4 a turn for today's rates, keeps up to 14 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 16.2, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 33.0) |
| grain | 6 @ 3.7, stop 21 |  | goal planner: buys 6 a turn for today's rates, keeps up to 21 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 2) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 35.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.5k (cash + stock at home prices); +33/turn over 6 turns, +35/turn over 24 turns.
- Limits: cash flow >= -438/turn, prestige >= -0.93/turn (values are after 200 tax a turn).
- Today's settings: value -119/turn, cash -122/turn, prestige +0.98/turn.
- Plan: value +38/turn, cash +41/turn, prestige -0.93/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -244 vs -151, -110 vs -158, +46 vs -121.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Gottweiler: +22/turn
  - ship Flax Wyrm -> Bordees: +1/turn
  - mansion 1 1.00 -> 0.55: +111/turn
  - spinnery 1 1.65 -> 1.33: +10/turn
  - net maker 0.00 -> 0.29: +3/turn
  - retting pit 1 0.91 -> 0.78: -0/turn
  - flax farm 1 4.64 -> 3.93: +7/turn
  - weavery 1 0.50 -> 0.43: -11/turn
- Model check over the last 59 turns: predicted +37/turn for the settings we ran, real +71/turn.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.38, garments 21.00, nets 32.75, beer 3.52, timber 3.58, prestige 63.93, cash 0.00
- Orders it would set: bread buy 5 (v2 None); candles buy 2 (v2 None); cloth sell 1 (v2 none); cured meat buy 4 (v2 12); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 6 (v2 0); labour buy 64 (v2 2); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Gottweiler (+12/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Bordees (+1/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

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

Buffers: flax fibres 93/77, thread 1064/228, cloth 72/128

## Self-diagnosis

- R1: cured meat slot dry: 4.0 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 4 @ 29, home ask 25.4; our bid is already at/over the ask (sellers too thin)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.76; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
