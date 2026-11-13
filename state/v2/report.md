# v2 shadow report

Turn 14002, 2026-11-13 19:01. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,057, prestige 3,496 (376 free, +2.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 107 | 27 | 19 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 116, buy 39, buy @ 3.76 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 64 | 64 | 551 | 0 | 13 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 3.08 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.08 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **labour**: 13 labour expired last turn (~25 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **cured meat**: home ask 31.60 is above our ceiling 29.00 and last turn bought 4 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **hold banquet 1 (fish)**: hold banquet 1 (fish) costs 57.5 coin per prestige at mansion, vs 74.1 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch
- **hold banquet 2 (fish)**: hold banquet 2 (fish) costs 56.1 coin per prestige at mansion, vs 74.1 for the running hold banquet 1 (meat) -> v2: check it is unlocked, then switch

## Notes

- labour: projection runs 107 over real use lately; planning 551, not 651

## Prestige spending, cheapest coin per prestige first

399 turns left: prestige gained now converts 86.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| hold banquet 2 (fish) | mansion | 6.8 | 56.1 | 56.1 |  |
| hold banquet 1 (fish) | mansion | 4.2 | 57.5 | 57.5 |  |
| jousting 3 | arena | 230 | 57.1 | 57.5 | needs a arena (build cost 29,088); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 57.6 | 57.6 | running |
| hold banquet 2 (pies) | mansion | 7 | 60.1 | 60.1 | thin at home: pies |
| hold banquet 3 (fish) | mansion | 7.6 | 63.0 | 63.0 | thin at home: hop beer |
| jousting 2 | arena | 210 | 62.6 | 63.0 | needs a arena (build cost 29,088); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 63.3 | 63.3 | thin at home: hop beer, stockfish, pies |
| hold banquet 4 (premium) | mansion | 20 | 63.6 | 63.6 | thin at home: hop beer, stockfish |
| hold mass 2 (premium) | cathedral | 360 | 60.5 | 63.6 | needs a cathedral (build cost 315,630); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 3 (pies) | mansion | 8 | 65.6 | 65.6 | thin at home: hop beer, pies |
| hold banquet 4 | mansion | 17.5 | 66.9 | 66.9 | thin at home: hop beer, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 11 | 151802239 | 0.096 | - | cured meat 6 | -141 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: cured meat buy 6 @ 23.8, pasties buy 2 @ 15.9; crew 0.1; est +54 a turn; stock: pasties 2 @ 15.9 (keep 14)
- **Flax Wyrm** on Caillechâtel: cured meat buy 3 @ 25.2, pasties buy 2 @ 14.0; crew 0.1; est +24 a turn; stock: pasties 2 @ 14.0 (keep 14)
- best towns now: Neuborn +62, Karlmoor +62, Orlesailles +61, Friedwerp +61, Hofkirchen +60
- Neuborn would trade: cured meat buy 6 @ 22.4, pasties buy 2 @ 15.8; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~116 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.40 (46/turn) | timber 22 (9.13->12.06), bread 148 (2.71->2.93), charcoal 19 (2.79->3.76), casks 4 (6.77->8.55) | cured meat 4 (24.57->28.69), dyed cloth 6 (10.82->12.06), garments 2 (22.68->24.6), tools 8 (5.06->5.46) | +117 |
| Orlesailles | 1178 | 0.48 | 0.20 (23/turn) | cured fish 6 (25.41->29.45), rope 1 (75.5->84.08), pickaxes 1 (10.34->11.3) | looms 1 (630->693.5), dyed cloth 6 (10.08->12.06), cured meat 4 (26.25->28.69), candles 1 (86.1->88.5) | +100 |
| Pontmont | 341 | 0.10 | 0.40 (46/turn) | cured fish 6 (25.41->30.4), bricks 9 (6.88->11.59), clay 4 (4.54->11.69), rope 1 (75.5->79.8) | cookware 4 (22.05->24.13), cured meat 4 (26.67->28.69), garments 2 (22.89->24.6), tools 17 (5.25->5.46) | +87 |
| Kirchwerp | 1072 | 0.42 | 0.40 (46/turn) | thread 91 (4.84->5.7), resin 5 (2.86->3.93), malt 2 (6.25->7.31), salt 4 (5.78->6.27) | stockfish 1 (115.5->132.05), cured meat 4 (25.41->28.69), garments 2 (22.26->24.6), dyed cloth 6 (11.34->12.06) | +73 |
| Calange | 218 | 0.07 | 0.20 (23/turn) | wrought iron 4 (17.54->26.6), premium ham 1 (252->260.3), charcoal 19 (2.79->3.63), limestone 2 (23.73->29.26) | cured meat 4 (25.83->28.69), seeds 3 (1.94->2.58), garments 2 (24.15->24.6), flax fibres 1 (5.93->6.5) | +73 |

**Best:** Grandgues at about +117 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 35.8, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 4.0 turns |
| beer | 20 @ 3.88, stop 77 |  | uses 19.2/turn (household upkeep, mansion 1), makes 0.0, holds 107 = 5.6 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 9) |
| cloth |  | 2 @ min 6.95 | goal planner: sells 2 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 13 = 2.2 turns |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 21.6) |
| grain | 0 @ 3.7, stop 19 |  | goal planner: buys 0 a turn for today's rates, keeps up to 19 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 51) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 34.0) |
| pasties |  | 1 @ min 15.5 | goal planner: sells 1 a turn at 15.5, keeps 0 (no one offered it) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 74.0) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.3/turn (ropewalk 1), makes 0.0, holds 0 = 1.3 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 29.4k (cash + stock at home prices); -161/turn over 6 turns, +12/turn over 24 turns.
- Limits: cash flow >= -419/turn, prestige >= -0.32/turn (values are after 200 tax a turn).
- Today's settings: value -205/turn, cash -183/turn, prestige +2.13/turn.
- Plan: value -27/turn, cash -12/turn, prestige -0.32/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -492 vs -146, -186 vs -147, -114 vs -143 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Neuborn: +6/turn
  - ship Flax Wyrm -> no route: +0/turn
  - mansion 1 1.00 -> 0.42: +143/turn
  - brewery 1 0.14 -> 0.08: +14/turn
  - ropewalk 1 0.25 -> 0.18: +8/turn
  - spinnery 1 1.65 -> 1.29: +6/turn
  - retting pit 1 0.91 -> 0.82: +3/turn
  - flax farm 1 4.64 -> 4.11: +4/turn
- Model check over the last 60 turns: predicted +70/turn for the settings we ran, real +20/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.96, garments 19.30, nets 16.71, beer 3.18, timber 3.51, prestige 60.86, cash 0.00
- Orders it would set: bread buy 5 (v2 9); candles buy 2 (v2 None); cloth sell 2 (v2 none); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 64 (v2 51); light armour buy 1 (v2 None); pasties sell 1 (v2 none)
- Ship linen snake: Grandgues -> Neuborn (+3/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +81/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 418 (+129 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.08 |
| ret | 3 | 0.91 | 0.82 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 126/77, thread 1050/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 3.08; ask over the cap 2.1 (60 coin per prestige)
