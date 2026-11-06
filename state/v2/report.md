# v2 shadow report

Turn 13823, 2026-11-06 08:10. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,538, prestige 3,284 (164 free, -0.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 14 | 4 | 4 | 0 | 0 | stop 14, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 36 | 9 | 9 | 0 | 0 | stop 36, buy 11, buy @ 3.7 |
| labour | 29 | 29 | 518 | 0 | 11 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.30 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Tuning

- **tar**: home ask 11.30 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 518, not 618

## Prestige spending, cheapest coin per prestige first

578 turns left: prestige gained now converts 94.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.5 | 49.5 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 54.2 | 54.2 |  |
| jousting 3 | arena | 230 | 54.2 | 54.4 | needs a arena (build cost 25,129); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 56.9 | 56.9 | thin at home: hop beer, wine, stockfish, candles |
| hold banquet 1 (meat) | mansion | 4.2 | 58.2 | 58.2 |  |
| hold banquet 3 (pies) | mansion | 8 | 59.3 | 59.3 | thin at home: hop beer, pies, candles |
| hold banquet 4 (premium) | mansion | 20 | 59.5 | 59.5 | thin at home: hop beer, wine, stockfish, candles |
| jousting 2 | arena | 210 | 59.4 | 59.6 | needs a arena (build cost 25,129); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 60.9 | 60.9 | thin at home: wine, hop beer, ham, stockfish, candles |
| hold banquet 3 (fish) | mansion | 7.6 | 61.1 | 61.1 | thin at home: hop beer |
| hold sermon 2 (candles) | church | 31 | 56.8 | 61.1 | needs a church (build cost 65,165); thin at home: jewellery, candles, furniture |
| hold banquet 2 (fish) | mansion | 6.8 | 61.4 | 61.4 | thin at home: wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 15.0 (keep 14); best orders clear only 5 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 5 @ 15.0 (keep 14); best orders clear only 9 a turn after crew: ship stays at 0
- best towns now: Orlesailles +52, Angefont +48, Donaunieder +40, Fulkirch +35, Bordetes +29
- Orlesailles would trade: pasties buy 14 @ 13.7; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~103 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.30 (31/turn) | charcoal 19 (2.42->6.41), timber 24 (7.3->10.45), nets 4 (34.6->37.62), firewood 1 (2.2->6.98) | garments 2 (22.05->23.6), jewellery 1 (75.6->78.38), flax fibres 4 (5.88->6.2), nails 4 (5.99->6.37) | +156 |
| Fontaux | 411 | 0.11 | 0.70 (72/turn) | garments 10 (23.2->28.31), timber 25 (7.3->10.92), charcoal 17 (2.42->4.54), wheels 1 (17.12->20.52) | flax fibres 9 (5.41->6.2), cloth 3 (8.29->8.5) | +127 |
| Neuborn | 780 | 0.21 | 0.60 (62/turn) | charcoal 19 (2.42->6.65), cured fish 3 (22.68->25.08), honey 3 (7.82->9.97), wheels 1 (17.12->21.28) | cloth 24 (6.46->8.5), flax fibres 21 (5.3->6.2), raw cloth 2 (5.88->6.6), flax plants 3 (1.35->1.82) | +125 |
| Blanans | 297 | 0.08 | 0.60 (62/turn) | timber 25 (7.3->10.07), charcoal 19 (2.42->4.75), limestone 2 (15.75->23.75), medicine 1 (162.75->168.15) | cloth 21 (7.35->8.5), cheese 4 (6.72->9.17), jewellery 1 (75.6->78.38), flax plants 3 (1.4->1.82) | +124 |
| Hanstein | 380 | 0.10 | 0.60 (62/turn) | timber 20 (7.3->11.4), limestone 2 (15.75->31.73), charcoal 19 (2.42->4.08), garments 10 (23.2->23.75) | cheese 4 (6.2->9.17), flax fibres 13 (5.3->6.2), seeds 12 (1.81->2.32), yarn 1 (3.59->3.82) | +123 |

**Best:** Grandgues at about +156 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.2, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 3.0 turns |
| beer |  | 16 @ min 3.06 | goal planner: sells 16 at 3.06 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 22.6) |
| grain | 9 @ 3.7, stop 33 |  | goal planner: buys 9 a turn for today's rates, keeps up to 33 (v2 had 10) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 18) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 23.6k (cash + stock at home prices); +153/turn over 6 turns, +174/turn over 24 turns.
- Limits: cash flow >= -272/turn, prestige >= +5.67/turn (values are after 200 tax a turn).
- Today's settings: value +92/turn, cash +85/turn, prestige -0.82/turn - breaks the prestige floor.
- Plan: value -133/turn, cash -50/turn, prestige +3.38/turn - could not meet the prestige floor.
- Cash check (real vs predicted cash a tick, last 3): +79 vs +107, -95 vs +99, -325 vs +96 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Donaunieder: +18/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.19: +5/turn
  - sewing shop 1 0.30 -> 0.36: -8/turn
  - weavery 1 0.50 -> 0.60: +9/turn
  - ropewalk 1 0.25 -> 0.00: -9/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.23: +13/turn
  - spinnery 1 1.65 -> 1.09: -16/turn
  - retting pit 1 0.91 -> 0.62: +12/turn
  - brewery 1 0.14 -> 0.27: -21/turn
- Model check over the last 61 turns: predicted +98/turn for the settings we ran, real +68/turn.
- Worth of one more unit per turn: labour 1.65, thread 4.14, cloth 6.62, flax fibres 4.91, garments 19.15, nets 29.81, beer 2.96, timber 3.13, prestige 10000.00, cash 0.00
- Orders it would set: beer sell 16 (v2 15); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 5); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 10); labour buy 29 (v2 18); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.23, worth +11/turn.
- Ship linen snake: Grandgues -> Donaunieder (+18/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +82/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 464 (+175 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 5.53 |
| ret | 3 | 0.91 | 1.11 |
| spin | 4 | 1.65 | 1.95 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 424/228, cloth 73/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.2 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
