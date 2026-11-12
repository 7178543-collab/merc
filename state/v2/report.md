# v2 shadow report

Turn 13980, 2026-11-12 21:23. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,364, prestige 3,522 (402 free, -2.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 6 | 0 | 4 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 17, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 484 | 0 | 45 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**5 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **beer**: needed (4.2/turn) but there is NO buy order, stock 6.0 -> v2: add buy 5
- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 3.04 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.04 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.20 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~78 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: home ask 11.20 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 496, not 596

## Prestige spending, cheapest coin per prestige first

421 turns left: prestige gained now converts 87.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.6 | 51.6 | running |
| jousting 3 | arena | 230 | 55.1 | 55.4 | needs a arena (build cost 27,303); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 56.1 | 56.1 | thin at home: hop beer, stockfish, glassware |
| hold banquet 1 (fish) | mansion | 4.2 | 58.2 | 58.2 | thin at home: cured fish |
| hold banquet 3 (pies) | mansion | 8 | 58.3 | 58.3 | thin at home: hop beer, pies |
| hold banquet 4 (premium) | mansion | 20 | 59.0 | 59.0 | thin at home: hop beer, stockfish, glassware |
| hold banquet 4 | mansion | 17.5 | 59.2 | 59.2 | thin at home: hop beer, ham, stockfish, glassware |
| hold banquet 2 (pies) | mansion | 7 | 59.6 | 59.6 | thin at home: pies |
| hold banquet 2 (fish) | mansion | 6.8 | 60.0 | 60.0 | thin at home: cured fish |
| hold banquet 3 (fish) | mansion | 7.6 | 60.5 | 60.5 | thin at home: hop beer, cured fish |
| jousting 2 | arena | 210 | 60.3 | 60.7 | needs a arena (build cost 27,303); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold sermon 2 (candles) | church | 31 | 60.1 | 67.3 | needs a church (build cost 74,324); thin at home: jewellery, candles |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 134102075 | 0.248 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 12 @ 14.0, pasties buy 7 @ 14.2; crew 0.1; est +171 a turn; stock: furniture 12 @ 14.0 (keep 145); stock: pasties 7 @ 14.2 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 15.5 (keep 14); best orders clear only -0 a turn after crew: ship stays at 0
- best towns now: Caillechâtel +171, Donaunieder +153, Bremcop +146, Herschweig +146, Chatgnan +145
- Caillechâtel would trade: furniture buy 12 @ 14.0, pasties buy 7 @ 14.2; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~106 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 1.00 (106/turn) | firewood 33 (3.19->8.55), timber 40 (8.35->10.83), bread 154 (2.5->2.89), charcoal 19 (3.19->4.08) | cured meat 3 (24.36->27.36), flour 1 (20.68->25.08), tools 16 (5.83->5.98), raw cloth 3 (6.88->7.17) | +278 |
| Orlesailles | 1178 | 0.44 | 0.50 (53/turn) | candles 1 (66.67->77.9), premium ham 1 (258.3->264.1), acid 1 (118.65->121.6), tackles 1 (169.05->173.85) | wax 6 (19.43->23.75), spinning wheels 2 (210->220.4), dyed cloth 7 (10.5->12.73), thread 46 (5.04->5.6) | +89 |
| Blanans | 297 | 0.08 | 1.00 (106/turn) | timber 20 (8.35->11.3), firewood 21 (3.19->6.93), candles 0 (66.67->76), bread 77 (2.5->2.77) | butter 0 (61.43->80.75), dyed cloth 4 (11.23->12.73), cured meat 1 (26.04->27.36), garments 1 (23.1->24.4) | +88 |
| Chribruck | 1202 | 0.45 | 0.10 (11/turn) | tackles 1 (169.05->222.3), tapestries 1 (782.25->807.5), candles 1 (66.67->72.67), wine 7 (7.3->8.07) | cured meat 3 (25.62->27.36), garments 2 (23.73->24.4) | +86 |
| Angefont | 686 | 0.19 | 0.40 (42/turn) | candles 1 (66.67->75.05), resin 11 (3.42->3.99), cloth 1 (6.47->7.36), wheels 4 (21.63->22.23) | flax fibres 23 (5.25->6.6), dyed cloth 8 (10.71->12.73), tools 16 (4.91->5.98), thread 49 (5.25->5.6) | +86 |

**Best:** Grandgues at about +278 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 3.88, stop 9 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 6 = 1.4 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 6) |
| candles | 2 @ 65, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 2 @ min 6.95 | goal planner: sells 2 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.14 | goal planner: sells 2 a turn at 1.14, keeps 219 (no one offered it) |
| furniture | 2 @ 15.7, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.0) |
| grain | 5 @ 3.7, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 37.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.3/turn (observed), makes 0.0, holds 1 = 2.9 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.3k (cash + stock at home prices); +1/turn over 6 turns, +113/turn over 24 turns.
- Limits: cash flow >= -390/turn, prestige >= -0.42/turn (values are after 200 tax a turn).
- Today's settings: value +85/turn, cash +55/turn, prestige -2.22/turn - breaks the prestige floor.
- Plan: value +4/turn, cash +16/turn, prestige -0.42/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +151 vs +19, +178 vs +70, +56 vs +63.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> no route: +0/turn
  - ship Flax Wyrm -> no route: +0/turn
  - brewery 1 0.14 -> 0.08: +12/turn
  - net maker 0.00 -> 0.29: +6/turn
  - flax farm 1 4.64 -> 4.15: -2/turn
  - retting pit 1 0.91 -> 0.82: +1/turn
  - spinnery 1 1.65 -> 1.31: -7/turn
  - ropewalk 1 0.25 -> 0.00: -4/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.17: +16/turn
  - mansion 1 0.00 -> 0.43: -104/turn
- Model check over the last 61 turns: predicted +104/turn for the settings we ran, real +0/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.95, garments 19.30, nets 30.30, beer 3.00, timber 3.29, prestige 70.28, cash 0.00
- Orders it would set: bread buy 5 (v2 6); candles buy 2 (v2 None); cloth sell 2 (v2 none); firewood buy 1 (v2 3); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.17, worth +6/turn.
- Ship linen snake: Grandgues -> no route (+0/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1977 coin: +4/turn, payback 470 turns, doesn't pay yet

## Chain sizing

Mode HOLD, garments sold 10.5/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 409 (+121 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 3.61 |
| ret | 3 | 0.91 | 0.72 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 160/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R1: beer slot dry: 6.0 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy none, home ask 3.7 -> **buy 9 @ 3.76 (ask 3.7, cap 5.7)** (ok)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 3.04; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
