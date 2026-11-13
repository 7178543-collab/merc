# v2 shadow report

Turn 13997, 2026-11-13 14:38. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,987, prestige 3,487 (367 free, +2.2/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 59 | 39 | 19 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 116, buy 39, buy @ 3.76 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 21, buy 6, buy @ 3.7 |
| labour | 64 | 64 | 546 | 0 | 18 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: only 0.5 turns of cured meat left and buying 4 (need 12) -> v2: buy 12
- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.46 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.46 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **labour**: 18 labour expired last turn (~33 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **cured meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 107 over real use lately; planning 546, not 629

## Prestige spending, cheapest coin per prestige first

404 turns left: prestige gained now converts 86.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 54.9 | 54.9 | running |
| jousting 3 | arena | 230 | 55.9 | 56.3 | needs a arena (build cost 27,938); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 60.0 | 60.0 | thin at home: cured fish |
| jousting 2 | arena | 210 | 61.3 | 61.6 | needs a arena (build cost 27,938); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 62.1 | 62.1 | thin at home: cured fish |
| hold banquet 4 (premium) | mansion | 20 | 63.1 | 63.1 | thin at home: hop beer, stockfish, candles |
| hold banquet 2 (pies) | mansion | 7 | 63.2 | 63.2 | thin at home: pies, candles |
| hold banquet 4 (pies) | mansion | 18 | 63.2 | 63.2 | thin at home: hop beer, stockfish, pies, candles |
| hold mass 2 (premium) | cathedral | 360 | 61.1 | 64.2 | needs a cathedral (build cost 310,510); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 3 (pies) | mansion | 8 | 66.8 | 66.8 | thin at home: hop beer, pies, candles |
| hold banquet 4 | mansion | 17.5 | 66.9 | 66.9 | thin at home: hop beer, stockfish, candles |
| hold banquet 3 (fish) | mansion | 7.6 | 67.5 | 67.5 | thin at home: hop beer, cured fish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: cured meat buy 6 @ 23.8, pasties buy 3 @ 15.8; crew 0.1; est +62 a turn; stock: pasties 3 @ 15.8 (keep 14)
- **Flax Wyrm** on Caillechâtel: cured meat buy 2 @ 24.8, pasties buy 3 @ 13.9; crew 0.1; est +23 a turn; stock: pasties 3 @ 13.9 (keep 14)
- best towns now: Neuborn +76, Gottweiler +72, Hofkirchen +72, Großmühle +71, Orlesailles +70
- Neuborn would trade: cured meat buy 6 @ 22.4, pasties buy 3 @ 14.1; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~113 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 1.00 (113/turn) | firewood 43 (2.58->6.65), timber 36 (8.51->12.35), windows 0 (787.5->817), bread 136 (2.6->2.93) | cured meat 1 (24.57->31.16), tar 5 (9.87->11.4), tools 7 (4.94->5.27), cheese 5 (6.41->6.7) | +314 |
| Amsdermund | 1111 | 0.43 | 0.80 (91/turn) | beer 77 (3.99->6.17), wine 11 (7.51->9.5), nets 6 (38->40.66), honey 7 (8.14->9.4) | cloth 23 (7.56->8.8), casks 18 (5.46->7.12), cured meat 2 (26.67->31.16), cookware 4 (24.15->25.46) | +197 |
| Vauxvais | 204 | 0.06 | 1.00 (113/turn) | firewood 51 (2.58->5.7), charcoal 18 (2.29->4.01), lead ore 5 (7.4->8.55), premium cheese 1 (30.87->33.82) | cured meat 2 (25.83->31.16), cloth 19 (8.24->8.8), premium steel 1 (38.43->45.79), thread 18 (4.73->4.94) | +130 |
| Herschweig | 775 | 0.23 | 0.20 (23/turn) | beer 46 (3.99->6.51) | cloth 24 (8.09->8.8), cured meat 2 (25.62->31.16), flax fibres 11 (5.83->6.7), tar 3 (9.82->11.4) | +124 |
| Hanstein | 380 | 0.12 | 0.40 (45/turn) | charcoal 16 (2.29->4.5), garments 10 (22->23.37), timber 12 (8.51->11.3), rope 1 (76.5->77.42) | casks 14 (5.99->7.12), cured meat 2 (24.57->31.16), seeds 17 (1.77->2.51), dyed cloth 7 (11.34->12.54) | +110 |

**Best:** Grandgues at about +314 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 36.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 29 @ 3.98, stop 77 |  | uses 19.2/turn (household upkeep, mansion 1), makes 0.0, holds 59 = 3.1 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 6) |
| candles | 2 @ 78.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (mansion 1), makes 0.0, holds 3 = 0.5 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 15.6, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 21.4) |
| grain | 5 @ 3.7, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 46) |
| light armour | 1 @ 107, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 37.0) |
| pasties |  | 1 @ min 17.2 | goal planner: sells 1 a turn at 17.2, keeps 0 (no one offered it) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 74.5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 0 = 1.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.0k (cash + stock at home prices); +89/turn over 6 turns, +62/turn over 24 turns.
- Limits: cash flow >= -458/turn, prestige >= -0.28/turn (values are after 200 tax a turn).
- Today's settings: value -175/turn, cash -146/turn, prestige +2.18/turn.
- Plan: value -5/turn, cash +11/turn, prestige -0.28/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +29 vs -126, -154 vs -144, -141 vs -157.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Neuborn: +7/turn
  - ship Flax Wyrm -> no route: +0/turn
  - mansion 1 1.00 -> 0.41: +140/turn
  - brewery 1 0.14 -> 0.07: +14/turn
  - spinnery 1 1.65 -> 1.37: +6/turn
  - net maker 0.00 -> 0.29: +2/turn
  - flax farm 1 4.64 -> 4.33: -1/turn
  - weavery 1 0.50 -> 0.40: -7/turn
  - sewing shop 1 0.30 -> 0.23: +11/turn
  - ropewalk 1 0.25 -> 0.00: -23/turn
- Model check over the last 60 turns: predicted +88/turn for the settings we ran, real +12/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.96, garments 19.30, nets 30.27, beer 3.14, timber 3.44, prestige 60.73, cash 0.00
- Orders it would set: bread buy 5 (v2 6); candles buy 2 (v2 None); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 64 (v2 46); light armour buy 1 (v2 None); pasties sell 1 (v2 none); rope sell 2 (v2 1)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.30, worth +8/turn.
- Ship linen snake: Grandgues -> Neuborn (+3/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 417 (+128 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.04 |
| ret | 3 | 0.91 | 0.81 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 129/77, thread 1050/228, cloth 72/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.46; ask over the cap 2.1 (60 coin per prestige)
