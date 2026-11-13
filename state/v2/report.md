# v2 shadow report

Turn 14005, 2026-11-13 22:48. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 13,593, prestige 3,503 (383 free, +2.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 108 | 28 | 19 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 116, buy 39, buy @ 3.76 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 4, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 24, buy 6, buy @ 3.7 |
| labour | 64 | 64 | 532 | 0 | 32 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 3.16 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.16 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **labour**: 32 labour expired last turn (~62 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: home ask 2.62 is above our ceiling 2.60 and last turn bought 5 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 57.4 coin per prestige at mansion, vs 67.9 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **hold banquet 2 (fish)**: hold banquet 2 (fish) costs 57.6 coin per prestige at mansion, vs 67.9 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch

## Notes

- labour: projection runs 88 over real use lately; planning 563, not 651
- labour expiry guard: 32 bought labour expired last turn, buy 32 (not 63) this turn

## Prestige spending, cheapest coin per prestige first

396 turns left: prestige gained now converts 86.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 56.3 | 56.6 | needs a arena (build cost 28,073); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 57.4 | 57.4 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 57.6 | 57.6 |  |
| maintain 1 | park | 0.5 | 57.6 | 57.6 | running |
| hold banquet 2 (pies) | mansion | 7 | 59.5 | 59.5 |  |
| jousting 2 | arena | 210 | 61.6 | 62.0 | needs a arena (build cost 28,073); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold mass 2 (premium) | cathedral | 360 | 60.0 | 62.8 | needs a cathedral (build cost 274,850); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |
| hold banquet 4 (pies) | mansion | 18 | 62.9 | 62.9 | thin at home: hop beer, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 63.5 | 63.5 | thin at home: hop beer, stockfish |
| hold banquet 3 (fish) | mansion | 7.6 | 64.2 | 64.2 | thin at home: hop beer |
| hold banquet 3 (pies) | mansion | 8 | 64.6 | 64.6 | thin at home: hop beer |
| hold banquet 2 (meat) | mansion | 6.8 | 65.7 | 65.7 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 11 | 151802239 | 0.048 | - | cured meat 6 | -140 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 15.0 (keep 14); best orders clear only -4 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only 11 a turn after crew: ship stays at 0
- best towns now: Neuborn +23, Kirchwerp +23, Gottweiler +22, Großmühle +21, Hofkirchen +21
- Neuborn would trade: cured meat buy 6 @ 22.4, pasties buy 2 @ 16.4; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~116 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Kirchwerp | 1072 | 0.42 | 0.70 (81/turn) | nets 4 (16.09->37.62), lead bars 6 (15.33->22.8), thread 78 (4.74->5.7), cheese 27 (7.51->8.64) | garments 20 (22.26->23.94), cured meat 6 (23.52->27.2), dyed cloth 7 (10.71->12.06), cookware 4 (24.15->25.46) | +264 |
| Hofkirchen | 991 | 0.37 | 0.40 (46/turn) | nets 6 (16.09->37.43), flax fibres 6 (5.63->7.65), thread 66 (4.74->5.22), premium ham 1 (252->256.5) | garments 20 (21.63->23.94), cured meat 6 (24.15->27.2), cheese 10 (4.73->6.08), cookware 4 (22.89->25.46) | +235 |
| Dortdorf | 871 | 0.29 | 0.20 (23/turn) | nets 6 (16.09->38), lead ore 8 (7.46->9.21) | looms 1 (614.25->693.5), cookware 4 (23.73->25.46), cheese 10 (5.57->6.08), cured meat 6 (26.25->27.2) | +218 |
| Blanans | 297 | 0.09 | 0.60 (70/turn) | nets 5 (16.09->35.91), timber 38 (8.93->11.49), limestone 3 (18.06->28.5), thread 11 (4.74->5.51) | garments 20 (23.1->23.94), cloth 14 (7.56->8), dyed cloth 6 (11.13->12.06), cured meat 6 (26.46->27.2) | +214 |
| Grandgues | 152 | 0.05 | 0.30 (35/turn) | timber 32 (8.93->12.06), nets 2 (16.09->35.15), charcoal 19 (2.25->3.55), lead ore 3 (7.46->9.31) | garments 20 (22.68->23.94), cured meat 6 (24.36->27.2), dyed cloth 7 (11.34->12.06), tools 9 (5.35->5.7) | +201 |

**Best:** Kirchwerp at about +264 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 35.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 20 @ 3.88, stop 77 |  | uses 19.2/turn (household upkeep, mansion 1), makes 0.0, holds 108 = 5.6 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 9) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 9 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 18 = 3.0 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 16.3, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 21.2) |
| grain | 0 @ 3.7, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 35 |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 32) |
| light armour | 1 @ 105, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 34.0) |
| pasties |  | 1 @ min 13.3 | goal planner: sells 1 a turn at 13.3, keeps 0 (no one offered it) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 74.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.8k (cash + stock at home prices); -148/turn over 6 turns, +33/turn over 24 turns.
- Limits: cash flow >= -400/turn, prestige >= -0.34/turn (values are after 200 tax a turn).
- Today's settings: value -210/turn, cash -180/turn, prestige +2.10/turn.
- Plan: value -38/turn, cash -26/turn, prestige -0.34/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -87 vs -182, -214 vs -161, -163 vs -184.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Brebronn: -3/turn
  - ship Flax Wyrm -> Neuborn: +8/turn
  - mansion 1 1.00 -> 0.42: +147/turn
  - brewery 1 0.14 -> 0.00: +6/turn
  - spinnery 1 1.65 -> 1.33: +5/turn
  - brewery 1 [brew beer 2] 0.00 -> 0.10: +3/turn
  - retting pit 1 0.91 -> 0.84: +2/turn
  - flax farm 1 4.64 -> 4.20: +5/turn
- Model check over the last 60 turns: predicted +50/turn for the settings we ran, real +0/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.20, cloth 6.68, flax fibres 5.05, garments 19.30, nets 16.80, beer 3.14, timber 3.53, prestige 60.36, cash 0.00
- Orders it would set: bread buy 5 (v2 9); cloth sell 1 (v2 none); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); labour buy 64 (v2 32); light armour buy 1 (v2 None); pasties sell 1 (v2 none); rope sell 2 (v2 1)
- Recipe: brewery 1 brew beer 1 -> brew beer 2 at 0.10, worth +5/turn.
- Ship linen snake: Grandgues -> Brebronn (+2/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Neuborn (+3/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +81/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 419 (+130 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.13 |
| ret | 3 | 0.91 | 0.83 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 123/77, thread 1050/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 3.16; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
