# v2 shadow report

Turn 14142, 2026-11-19 15:18. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,827, prestige 3,646 (526 free, -0.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 46 | 11 | 12 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 47, buy 12, buy @ 3.48 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 1 | 1 | 1 | 0 | stop 1, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 34 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 64 | 64 | 501 | 0 | 63 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**6 risks, 1 waste, 6 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), 3 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.80 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.80 is above our ceiling 2.40 and last turn bought 1 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 5) -> v2: buy 5
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.70 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 63 labour expired last turn (~123 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: home ask 3.16 is above our ceiling 2.60 and last turn bought 5 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **cured meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 57.5 coin per prestige at mansion, vs 68.1 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **hold banquet 3 (pies)**: hold banquet 3 (pies) costs 57.1 coin per prestige at mansion, vs 68.1 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.70 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +1 crew for linen snake (crew 0.02, no projection from the game)
- labour: projection runs 100 over real use lately; planning 502, not 602
- labour expiry guard: 63 bought labour expired last turn, buy 2 (not 2) this turn

## Prestige spending, cheapest coin per prestige first

259 turns left: prestige gained now converts 72.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 49.9 | 50.2 | needs a arena (build cost 27,850); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 53.6 | 54.0 | needs a arena (build cost 27,850); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 54.0 | 54.6 | needs a arena (build cost 27,850); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 57.1 | 57.1 |  |
| hold banquet 1 (fish) | mansion | 4.2 | 57.5 | 57.5 |  |
| maintain 1 | park | 0.5 | 57.6 | 57.6 | running |
| hold banquet 3 (fish) | mansion | 7.6 | 58.2 | 58.2 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 58.3 | 58.3 |  |
| hold banquet 2 (pies) | mansion | 7 | 58.4 | 58.4 |  |
| hold banquet 4 (pies) | mansion | 18 | 59.1 | 59.1 | thin at home: stockfish |
| jousting 2 | arena | 210 | 59.2 | 59.8 | needs a arena (build cost 27,850); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 60.0 | 60.0 | thin at home: stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: cured meat buy 3 @ 24.6, pasties buy 14 @ 16.4; crew 0.1; est +36 a turn; stock: pasties 14 @ 16.4 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; best orders clear only 2 a turn after crew: ship stays at 0
- best towns now: Gotthafen +512, Cobholme +365, Fulkirch +315, Brunnham +289, Clairlond +232
- Gotthafen would trade: cured meat buy 3 @ 23.8, furniture buy 44 @ 13.7, pasties buy 3 @ 15.1; crew 0.6

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~123 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.70 (86/turn) | timber 41 (9.5->12.63), thread 92 (5.5->6.51), bread 192 (3.32->3.76), charcoal 19 (2.65->5.03) | - | +306 |
| Rouhomme | 368 | 0.12 | 0.50 (61/turn) | glassware 4 (82.95->114), thread 61 (5.5->6.84), garments 10 (31.6->33.25), tar 4 (12.29->14.25) | copper ingots 1 (15.44->16.15), honey 1 (8.56->8.98), salt 3 (5.41->5.56) | +225 |
| Gottweiler | 1135 | 0.48 | 0.20 (25/turn) | garments 10 (31.6->34.39), nets 6 (36.8->40.66), blades 3 (20.58->25.08), dyed cloth 13 (19.43->20.33) | ham 2 (59.85->115.9), cloth 21 (10.4->12.3), premium ham 1 (228.9->237.5), raw cloth 2 (10.19->14.15) | +220 |
| Fontaux | 411 | 0.14 | 0.60 (74/turn) | thread 92 (5.5->7.27), timber 28 (9.5->12.54), dyed cloth 4 (19.43->22.8), salt 3 (6.35->7.79) | raw cloth 2 (11.03->14.15), premium cheese 1 (28.98->31.54), pasties 3 (11.97->12.73), copper ingots 1 (15.65->16.15) | +208 |
| Großaue | 1136 | 0.48 | 0.20 (25/turn) | nets 3 (36.8->39.33), blades 2 (20.58->23.18), jewellery 1 (119.7->123.5) | plate armour 1 (1302->1387), cloth 24 (8.98->12.3), raw cloth 2 (10.71->14.15), fleece 3 (10.71->12.63) | +169 |

**Best:** Grandgues at about +306 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 35.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 12 @ 3.48, stop 47 |  | uses 11.7/turn (household upkeep), makes 0.0, holds 46 = 4.0 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 9) |
| candles | 2 @ 74.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (observed), makes 0.0, holds 3 = 0.5 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 17.4, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 30.8) |
| grain | 0 @ 3.7, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 34 |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 2) |
| light armour | 1 @ 101, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 35.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.4k (cash + stock at home prices); -3/turn over 6 turns, +41/turn over 24 turns.
- Limits: cash flow >= -451/turn, prestige >= -0.94/turn (values are after 200 tax a turn).
- Today's settings: value -149/turn, cash -151/turn, prestige +1.40/turn.
- Plan: value +32/turn, cash +36/turn, prestige -0.94/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -113 vs -142, +9 vs -133, +137 vs -136.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Amsdermund: +19/turn
  - ship Flax Wyrm -> Gotthafen: +1/turn
  - mansion 1 1.00 -> 0.44: +136/turn
  - brewery 1 0.14 -> 0.01: +21/turn
  - net maker 0.00 -> 0.29: +8/turn
  - spinnery 1 1.65 -> 1.40: +2/turn
  - retting pit 1 0.91 -> 0.80: +2/turn
  - flax farm 1 4.64 -> 4.01: +7/turn
- Model check over the last 59 turns: predicted +48/turn for the settings we ran, real +80/turn.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.66, beer 3.32, timber 3.69, prestige 63.22, cash 0.00
- Orders it would set: bread buy 5 (v2 9); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 2 (v2 5); furniture buy 2 (v2 None); garments sell 11 (v2 10); labour buy 64 (v2 2); light armour buy 1 (v2 None); rope sell 1 (v2 none)
- Ship linen snake: Grandgues -> Amsdermund (+9/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Gotthafen (+1/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +88/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

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

Buffers: flax fibres 88/77, thread 1064/228, cloth 72/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask 2.8; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
