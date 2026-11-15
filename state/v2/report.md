# v2 shadow report

Turn 14052, 2026-11-15 21:08. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,208, prestige 3,560 (440 free, -2.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 11 | 9 | 4 | 0 | 0 | min_holding 60, sell 5, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 40 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21.2 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 21, buy 6, buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 3.00 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.00 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.50 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~78 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: home ask 11.50 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +6 crew for Flax Wyrm (crew 0.12, no projection from the game)
- labour: +1 crew for linen snake (crew 0.02, no projection from the game)
- labour: projection runs 100 over real use lately; planning 491, not 591

## Prestige spending, cheapest coin per prestige first

349 turns left: prestige gained now converts 82.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.3 | 51.3 | running |
| jousting 3 | arena | 230 | 54.4 | 54.8 | needs a arena (build cost 26,601); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 55.6 | 55.6 |  |
| hold banquet 4 (pies) | mansion | 18 | 57.1 | 57.1 | thin at home: pasties, ham, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 59.8 | 59.8 | thin at home: pasties |
| hold banquet 2 (pies) | mansion | 7 | 60.0 | 60.0 | thin at home: pasties |
| jousting 2 | arena | 210 | 59.6 | 60.0 | needs a arena (build cost 26,601); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 60.1 | 60.1 | thin at home: ham, stockfish |
| hold banquet 1 (meat) | mansion | 4.2 | 60.2 | 60.2 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 60.9 | 60.9 | thin at home: cured fish |
| hold banquet 4 (premium) | mansion | 20 | 61.7 | 61.7 | thin at home: ham, stockfish |
| hold mass 2 (premium) | cathedral | 360 | 58.5 | 61.9 | needs a cathedral (build cost 284,505); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 21 @ 14.0, pasties buy 3 @ 14.3; crew 0.2; est +253 a turn; stock: furniture 21 @ 14.0 (keep 145); stock: pasties 3 @ 14.3 (keep 14)
- **linen snake** on Grandgues: pasties buy 14 @ 15.4; crew 0.1; est +38 a turn; stock: pasties 14 @ 15.4 (keep 14)
- best towns now: Amsdermund +593, Chatgnan +500, Gotthafen +452, Bedenis +438, Vauxvais +396
- Amsdermund would trade: furniture buy 57 @ 14.3; crew 0.9

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~107 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.90 (96/turn) | timber 46 (7.82->12.73), firewood 34 (3.15->6.32), charcoal 19 (2.77->5.27), furniture 12 (12.18->14.15) | dyed cloth 4 (11.87->12.92), candles 1 (84.53->87), cheese 4 (6.67->7.03), tiles 3 (3.89->4.62) | +334 |
| Darmwald | 1022 | 0.35 | 0.70 (75/turn) | charcoal 19 (2.77->7.27), furniture 12 (12.18->13.77), nets 4 (34.8->36.1) | windows 1 (714->840.75), cloth 24 (7.35->8.8), candles 1 (82.95->87), dyed cloth 1 (10.5->12.92) | +192 |
| Caillechâtel | 488 | 0.14 | 0.10 (11/turn) | garments 11 (23.2->24.32) | windows 1 (672->840.75), seeds 12 (1.77->2.58), cloth 9 (8.35->8.8), thread 8 (4.83->5.3) | +188 |
| Kirchwerp | 1072 | 0.39 | 0.40 (43/turn) | arms 8 (32.97->40.28), furniture 12 (12.18->16.53), honey 7 (8.24->9.69), resin 4 (2.48->3.93) | cloth 24 (7.56->8.8), ploughs 3 (73.5->80.27), dyed cloth 4 (10.92->12.92), cheese 4 (6.04->7.03) | +139 |
| Calange | 218 | 0.06 | 0.20 (21/turn) | tapestries 1 (782.25->817), furniture 12 (12.18->14.25), beer 92 (3.15->3.44), casks 10 (6.35->7.22) | cloth 24 (7.35->8.8), thread 13 (4.47->5.3), medicine 1 (130.2->139.65), seeds 2 (2.29->2.58) | +133 |

**Best:** Grandgues at about +334 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 2 @ min 2.96 | goal planner: sells 2 a turn at 2.96, keeps 60 (no one offered it) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 11.9, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21.2 | goal planner: sells 11 at 21.2 (v2 had 10 at 22.6) |
| grain | 0 @ 3.7, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 35 |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 34.0 |  |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.5/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 23.7k (cash + stock at home prices); +21/turn over 6 turns, -24/turn over 24 turns.
- Limits: cash flow >= -259/turn, prestige >= -0.59/turn (values are after 200 tax a turn).
- Today's settings: value +58/turn, cash +34/turn, prestige -2.41/turn - breaks the prestige floor.
- Plan: value +7/turn, cash +27/turn, prestige -0.59/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +91 vs +52, -6 vs +44, +105 vs +27.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Toqueque: +5/turn
  - ship Flax Wyrm -> Pontmont: +0/turn
  - brewery 1 0.14 -> 0.01: +23/turn
  - net maker 0.00 -> 0.29: +10/turn
  - ropewalk 1 0.25 -> 0.00: +5/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.07: +16/turn
  - flax farm 1 4.64 -> 4.19: -1/turn
  - retting pit 1 0.91 -> 0.84: -0/turn
  - weavery 1 0.50 -> 0.58: -10/turn
  - spinnery 1 1.65 -> 1.33: -12/turn
- Model check over the last 59 turns: predicted -117/turn for the settings we ran, real -105/turn.
- Worth of one more unit per turn: labour 1.71, thread 4.30, cloth 6.86, flax fibres 5.09, garments 19.86, nets 31.20, beer 3.00, timber 3.35, prestige 65.97, cash 0.00
- Orders it would set: beer sell 2 (v2 none); cloth sell 1 (v2 none); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.07, worth +4/turn.
- Ship linen snake: Grandgues -> Toqueque (+5/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Pontmont (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +81/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1727 coin: +1/turn, payback 1293 turns, doesn't pay yet (materials thin at home: limestone)

## Chain sizing

Mode HOLD, garments sold 9.3/turn (+0.0 exported); plan makes 32.4 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 411 (+122 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 3.99 |
| ret | 3 | 0.91 | 0.80 |
| spin | 4 | 1.65 | 1.65 |
| weave | 3 | 0.50 | 1.26 |
| sew | 2 | 0.30 | 0.79 |

Buffers: flax fibres 127/77, thread 1064/225, cloth 72/126

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 3.0; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
