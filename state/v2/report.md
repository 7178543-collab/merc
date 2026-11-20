# v2 shadow report

Turn 14173, 2026-11-20 22:52. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,922, prestige 3,738 (618 free, -1.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 119 | 33 | 12 | 0 | 0 | sell 17, sell @ 4.44 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 6 | 4 | 4 | 0 | 0 | stop 14, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 18 | 7 | 7 | 2 | 0 | stop 36, buy 18, buy @ 3.7 |
| labour | 64 | 64 | 515 | 0 | 49 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**5 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), 3 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **firewood**: home ask 2.72 is above our ceiling 2.40 and last turn bought 4 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **grain**: brewery 1 ran short of grain (buy is live (18 @ 3.7), 7 bought last turn); labour need rises ~18/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.40 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 49 labour expired last turn (~104 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: home ask 2.80 is above our ceiling 2.60 and last turn bought 0 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: home ask 11.40 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +1 crew for linen snake (crew 0.02, no projection from the game)
- labour: projection runs 100 over real use lately; planning 520, not 620
- labour expiry guard: 49 bought labour expired last turn, buy 16 (not 20) this turn

## Prestige spending, cheapest coin per prestige first

228 turns left: prestige gained now converts 68.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 51.7 | 52.4 | needs a arena (build cost 28,911); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 | arena | 210 | 56.7 | 57.4 | needs a arena (build cost 28,911); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 58.0 | 58.0 | thin at home: wine, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 60.4 | 60.4 | thin at home: wine, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 61.6 | 61.6 |  |
| hold banquet 4 | mansion | 17.5 | 61.6 | 61.6 | thin at home: wine, ham, stockfish |
| hold banquet 2 (pies) | mansion | 7 | 61.8 | 61.8 | thin at home: wine, cheese |
| hold mass 2 (premium) | cathedral | 360 | 55.0 | 62.9 | needs a cathedral (build cost 306,540); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |
| maintain 1 | park | 0.5 | 63.0 | 63.0 | running |
| hold banquet 2 (meat) | mansion | 6.8 | 67.6 | 67.6 | thin at home: wine, cheese |
| hold banquet 3 (meat) | mansion | 7.6 | 68.8 | 68.8 | thin at home: cheese |
| hold banquet 1 (meat) | mansion | 4.2 | 69.4 | 69.4 | running |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: beer sell 13 @ 4.9, pasties buy 12 @ 16.0; crew 0.1; est +29 a turn; stock: pasties 12 @ 16.0 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 15.1 (keep 14); best orders clear only 2 a turn after crew: ship stays at 0
- best towns now: Blanans +266, Clairlond +200, Cobholme +188, Dortgart +188, Brunnham +176
- Blanans would trade: cured meat buy 3 @ 24.4, furniture buy 17 @ 12.4, pasties buy 13 @ 16.0; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~134 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Caillechâtel | 488 | 0.17 | 0.10 (13/turn) | garments 10 (31.4->32.49) | cloth 24 (8.72->13.4), thread 20 (6.14->7.05), acid 1 (110.25->118.75), candles 1 (72.45->81) | +152 |
| Fontaux | 411 | 0.15 | 0.40 (54/turn) | garments 10 (31.4->35.72), nets 6 (43->49.88), thread 69 (6.95->7.27), flour 2 (21.63->26.79) | cured fish 3 (24.57->33.63), steel ingots 3 (16.7->17.29) | +144 |
| Grandgues | 152 | 0.05 | 0.60 (81/turn) | firewood 36 (2.86->5.79), charcoal 19 (2.77->4.99), beer 13 (4->4.75), flax fibres 6 (6.4->6.98) | cloth 7 (11.76->13.4), malt 3 (7.93->9.03), candles 1 (79.28->81), garments 2 (31.71->32.6) | +111 |
| Helmgreen | 1354 | 0.69 | 0.50 (67/turn) | - | cloth 21 (9.61->13.4), yarn 26 (6.04->7.12), thread 24 (6.04->7.05), acid 1 (111.3->118.75) | +107 |
| Vauxvais | 204 | 0.07 | 0.10 (13/turn) | raw cloth 4 (10.29->15.2), flour 2 (21.63->26.79), flax fibres 6 (6.4->7.17), cloth 1 (12.7->12.92) | thread 19 (3.09->7.05), malt 3 (7.46->9.03), grain 7 (3.02->3.44), steel ingots 3 (16.7->17.29) | +106 |

**Best:** Caillechâtel at about +152 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 4 @ min 4 | goal planner: sells 4 a turn at 4, keeps 58 (no one offered it) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 9) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 3 @ 29.0, stop 11 |  | goal planner: buys 3 a turn for today's rates, keeps up to 11 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 17.3, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 27.4) |
| grain | 7 @ 3.7, stop 26 |  | goal planner: buys 7 a turn for today's rates, keeps up to 26 (v2 had 18) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 16) |
| light armour | 1 @ 106, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 41.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.1k (cash + stock at home prices); +71/turn over 6 turns, -56/turn over 24 turns.
- Limits: cash flow >= -288/turn, prestige >= -1.33/turn (values are after 200 tax a turn).
- Today's settings: value -177/turn, cash -189/turn, prestige +1.10/turn.
- Plan: value +38/turn, cash +39/turn, prestige -1.33/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -142 vs -167, +1 vs -169, -61 vs -173.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Donaunieder: +8/turn
  - ship Flax Wyrm -> Amsdermund: +15/turn
  - mansion 1 1.00 -> 0.42: +155/turn
  - net maker 0.00 -> 0.29: +7/turn
  - ropewalk 1 0.25 -> 0.05: +15/turn
  - spinnery 1 1.65 -> 1.24: +14/turn
  - retting pit 1 0.91 -> 0.78: +4/turn
  - flax farm 1 4.64 -> 3.94: +10/turn
- Model check over the last 59 turns: predicted -84/turn for the settings we ran, real +25/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.80, thread 4.57, cloth 7.27, flax fibres 5.48, garments 21.00, nets 32.66, beer 3.43, timber 3.80, prestige 64.40, cash 0.00
- Orders it would set: beer sell 4 (v2 none); bread buy 5 (v2 9); cloth sell 1 (v2 none); cured meat buy 3 (v2 12); firewood buy 4 (v2 8); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 7 (v2 18); labour buy 64 (v2 16); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Donaunieder (+14/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Amsdermund (+6/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +86/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 421 (+132 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.24 |
| ret | 3 | 0.91 | 0.85 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 114/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R1: bread slot dry: 7.4 held, 4.2 a turn (basic food slot (+0.3 prestige)); our buy 5 @ 2.6, home ask 2.8 -> **buy 9 @ 2.86 (ask 2.8, cap 4.3)** (ok)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
