# v2 shadow report

Turn 13955, 2026-11-11 20:56. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,616, prestige 3,585 (465 free, -2.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 22 | 5 | 4 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 26, buy 9, buy @ 3.44 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 33 | 0 | 2 | 0 | 0 | min_holding 30, sell 10, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 18, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 12.00 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~77 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 12.00 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +6 crew for Flax Wyrm (crew 0.12, no projection from the game)
- labour: +2 crew for linen snake (crew 0.05, no projection from the game)
- labour: projection runs 100 over real use lately; planning 492, not 592

## Prestige spending, cheapest coin per prestige first

446 turns left: prestige gained now converts 89.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.7 | 50.7 | running |
| jousting 3 | arena | 230 | 55.1 | 55.4 | needs a arena (build cost 27,157); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 55.6 | 55.6 | thin at home: ham, stockfish |
| hold banquet 1 (fish) | mansion | 4.2 | 57.0 | 57.0 |  |
| hold banquet 4 (premium) | mansion | 20 | 58.3 | 58.3 | thin at home: ham, stockfish, premium cheese |
| hold banquet 4 | mansion | 17.5 | 58.8 | 58.8 | thin at home: ham, stockfish |
| jousting 2 | arena | 210 | 60.4 | 60.7 | needs a arena (build cost 27,157); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (meat) | mansion | 4.2 | 62.0 | 62.0 |  |
| hold banquet 3 (pies) | mansion | 8 | 63.0 | 63.0 | thin at home: pies |
| hold banquet 2 (fish) | mansion | 6.8 | 64.5 | 64.5 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 64.7 | 64.7 |  |
| hold banquet 2 (pies) | mansion | 7 | 65.8 | 65.8 | thin at home: pies |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: furniture buy 27 @ 14.6, pasties buy 6 @ 15.9; crew 0.1; est +326 a turn; stock: furniture 27 @ 14.6 (keep 145); stock: pasties 6 @ 15.9 (keep 14)
- **Flax Wyrm** on Caillechâtel: furniture buy 20 @ 14.0, pasties buy 6 @ 14.4; crew 0.2; est +254 a turn; stock: furniture 20 @ 14.0 (keep 145); stock: pasties 6 @ 14.4 (keep 14)
- best towns now: Vauxvais +331, Grandgues +326, Heidlowe +320, Amsdermund +307, Chatgnan +302
- Vauxvais would trade: furniture buy 27 @ 14.6, pasties buy 6 @ 15.1; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~107 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Unterhufe | 595 | 0.17 | 0.20 (21/turn) | looms 1 (588->669.75), furniture 8 (12.08->15.86), garments 10 (19.22->20.9), slaked lime 2 (7.77->9.31) | cloth 23 (6.67->10.2), flax fibres 22 (6.88->8.85), thread 47 (4.68->5.15), butter 1 (72.45->79.33) | +259 |
| Angefont | 686 | 0.20 | 0.30 (32/turn) | looms 1 (588->617.5), furniture 8 (12.08->15.11), garments 10 (19.22->20.9), casks 9 (6.2->6.93) | flax fibres 23 (5.04->8.85), cloth 14 (8.24->10.2), tools 15 (5.17->5.56), chisels 1 (8.61->8.93) | +173 |
| Fontaux | 411 | 0.12 | 0.20 (21/turn) | thread 92 (4.66->5.65), furniture 8 (12.08->17.95), wine 19 (6.41->7.74), salt 6 (6.14->7.79) | ham 1 (83.48->88.35), chisels 1 (7.88->8.93) | +166 |
| Helmgreen | 1354 | 0.55 | 0.30 (32/turn) | tapestries 1 (687.75->788.5), garments 10 (19.22->21.47), wine 19 (6.41->7.74), looms 1 (588->593.75) | cloth 16 (8.82->10.2), flax fibres 9 (6.67->8.85), cheese 6 (8.29->9.17), resin 1 (2.37->5.56) | +158 |
| Bordetes | 831 | 0.25 | 0.20 (21/turn) | cured fish 7 (24.57->34.2), furniture 8 (12.08->15.58), garments 10 (19.22->20.71), casks 4 (6.2->7.08) | cloth 23 (7.56->10.2), garments 2 (23.1->24) | +156 |

**Best:** Unterhufe at about +259 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 36.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 3.66, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 22 = 5.2 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 87.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax fibres |  | 3 @ min 8.75 | goal planner: sells 3 a turn at 8.75, keeps 85 (no one offered it) |
| flax plants |  | 2 @ min 1.18 | goal planner: sells 2 a turn at 1.18, keeps 219 (no one offered it) |
| furniture | 2 @ 16, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.4) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 101, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 37.2) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.5/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 25.8k (cash + stock at home prices); -617/turn over 6 turns, -199/turn over 24 turns.
- Limits: cash flow >= -234/turn, prestige >= -0.69/turn (values are after 200 tax a turn).
- Today's settings: value +40/turn, cash +119/turn, prestige -2.54/turn - breaks the prestige floor.
- Plan: value -7/turn, cash +119/turn, prestige -0.69/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +667 vs +116, +160 vs +110, +94 vs +121.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Calange: +18/turn
  - ship Flax Wyrm -> Clairas: +0/turn
  - brewery 1 0.14 -> 0.08: +12/turn
  - net maker 0.00 -> 0.29: +7/turn
  - ropewalk 1 0.25 -> 0.00: +8/turn
  - spinnery 1 1.65 -> 1.24: +2/turn
  - retting pit 1 0.91 -> 0.80: -3/turn
  - flax farm 1 4.64 -> 4.01: -10/turn
  - mansion 1 0.00 -> 0.44: -76/turn
- Model check over the last 60 turns: predicted +108/turn for the settings we ran, real +29/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.95, garments 19.30, nets 30.12, beer 3.01, timber 3.29, prestige 60.03, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); flax fibres sell 3 (v2 none); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.04, worth +2/turn.
- Ship linen snake: Grandgues -> Calange (+18/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Clairas (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +81/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.0/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 415 (+124 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 3.94 |
| ret | 3 | 0.91 | 0.79 |
| spin | 4 | 1.65 | 1.67 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 134/77, thread 1064/227, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
