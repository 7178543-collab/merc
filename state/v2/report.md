# v2 shadow report

Turn 14000, 2026-11-13 17:55. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,195, prestige 3,492 (372 free, +2.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 108 | 39 | 19 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 116, buy 39, buy @ 3.76 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 64 | 64 | 519 | 0 | 45 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 3.26 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.26 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 10.90 x13, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~86 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Notes

- labour: projection runs 99 over real use lately; planning 532, not 631
- labour expiry guard: 45 bought labour expired last turn, buy 19 (not 32) this turn

## Prestige spending, cheapest coin per prestige first

401 turns left: prestige gained now converts 86.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 56.7 | 56.7 | running |
| jousting 3 | arena | 230 | 56.4 | 56.8 | needs a arena (build cost 30,177); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (pies) | mansion | 7 | 60.4 | 60.4 | thin at home: pies, candles |
| jousting 2 | arena | 210 | 61.8 | 62.2 | needs a arena (build cost 30,177); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 63.4 | 63.4 | thin at home: hop beer, stockfish, pies, candles |
| hold banquet 4 (premium) | mansion | 20 | 63.7 | 63.7 | thin at home: hop beer, stockfish, candles |
| hold mass 2 (premium) | cathedral | 360 | 61.0 | 64.2 | needs a cathedral (build cost 324,270); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 2 (fish) | mansion | 6.8 | 64.7 | 64.7 | thin at home: cured fish |
| hold banquet 2 (meat) | mansion | 6.8 | 65.1 | 65.1 | thin at home: cured meat |
| hold banquet 1 (fish) | mansion | 4.2 | 65.9 | 65.9 | thin at home: cured fish |
| hold banquet 3 (pies) | mansion | 8 | 66.8 | 66.8 | thin at home: hop beer, pies, candles |
| hold banquet 1 (meat) | mansion | 4.2 | 67.2 | 67.2 | running |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0.084 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: cured meat buy 6 @ 23.8, pasties buy 4 @ 15.8; crew 0.1; est +20 a turn; stock: pasties 4 @ 15.8 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 14.0 (keep 14); best orders clear only 8 a turn after crew: ship stays at 0
- best towns now: Gottweiler +30, Neuborn +29, Orlesailles +28, Großmühle +28, Karlmoor +24
- Gottweiler would trade: cured meat buy 6 @ 23.4, pasties buy 4 @ 13.9; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~115 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.90 (103/turn) | timber 28 (9.19->12.06), firewood 35 (3.42->5.79), bread 149 (2.6->2.91), charcoal 19 (2.25->3.7) | cured fish 6 (27.09->31.35), cured meat 6 (24.57->26.8), dyed cloth 6 (10.92->12.16), tools 8 (4.94->5.37) | +191 |
| Nürnnieder | 520 | 0.16 | 0.10 (11/turn) | thread 44 (4.78->5.22), jewellery 1 (113.4->115.9), malt 2 (8.03->9.4), cookware 2 (27.93->28.69) | looms 1 (630->693.5), cured fish 6 (25.41->31.35), cured meat 6 (25.62->26.8), furniture 1 (15.12->16.2) | +119 |
| Hanstein | 380 | 0.12 | 0.40 (46/turn) | charcoal 16 (2.25->4.52), nets 5 (37.8->39.52), timber 12 (9.19->11.4), acid 1 (133.35->137.75) | cured fish 5 (25.2->31.35), seeds 21 (1.8->2.58), cured meat 6 (24.78->26.8), cheese 4 (5.67->6.08) | +95 |
| Vauxvais | 204 | 0.06 | 0.20 (23/turn) | charcoal 19 (2.25->4.01), flour 5 (22.47->24.89), beer 3 (3.66->4.1), wine 4 (6.88->7.27) | cured fish 6 (23.94->31.35), cured meat 6 (25.62->26.8), tools 17 (5.15->5.37), seeds 4 (1.94->2.58) | +84 |
| Blanans | 297 | 0.09 | 0.50 (57/turn) | timber 35 (9.19->11.21), cheese 8 (6.88->8.07), honey 3 (8.19->9.45), casks 3 (6.93->7.69) | cured fish 6 (25.62->31.35), cloth 13 (7.56->8.05), garments 2 (22.89->23.8) | +80 |

**Best:** Grandgues at about +191 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 35.8, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 4.0 turns |
| beer | 20 @ 3.88, stop 77 |  | uses 19.2/turn (household upkeep, mansion 1), makes 0.0, holds 108 = 5.6 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 7) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 6 = 1.0 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 21.6) |
| grain | 0 @ 3.7, stop 18 |  | goal planner: buys 0 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 19) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 36.8) |
| pasties |  | 1 @ min 15.5 | goal planner: sells 1 a turn at 15.5, keeps 0 (no one offered it) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.3/turn (observed), makes 0.0, holds 1 = 3.3 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 29.5k (cash + stock at home prices); -178/turn over 6 turns, +53/turn over 24 turns.
- Limits: cash flow >= -425/turn, prestige >= -0.30/turn (values are after 200 tax a turn).
- Today's settings: value -189/turn, cash -163/turn, prestige +2.15/turn.
- Plan: value -13/turn, cash +3/turn, prestige -0.30/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -492 vs -146, -186 vs -147, -114 vs -143 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Neuborn: +7/turn
  - ship Flax Wyrm -> Herschweig: +2/turn
  - mansion 1 1.00 -> 0.42: +141/turn
  - brewery 1 0.14 -> 0.08: +15/turn
  - net maker 0.00 -> 0.29: +6/turn
  - spinnery 1 1.65 -> 1.36: +4/turn
  - retting pit 1 0.91 -> 0.85: +2/turn
  - flax farm 1 4.64 -> 4.29: +4/turn
  - weavery 1 0.50 -> 0.42: -3/turn
  - sewing shop 1 0.30 -> 0.25: +7/turn
- Model check over the last 60 turns: predicted +74/turn for the settings we ran, real +8/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.20, cloth 6.68, flax fibres 5.05, garments 19.30, nets 30.32, beer 3.23, timber 3.51, prestige 60.99, cash 0.00
- Orders it would set: bread buy 5 (v2 7); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 64 (v2 19); light armour buy 1 (v2 None); pasties sell 1 (v2 none)
- Ship linen snake: Grandgues -> Neuborn (+3/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Herschweig (+2/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 418 (+129 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.07 |
| ret | 3 | 0.91 | 0.81 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 127/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 3.26; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
