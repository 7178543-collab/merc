# v2 shadow report

Turn 14179, 2026-11-21 04:50. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,250, prestige 3,733 (613 free, -1.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 74 | 0 | 12 | 0 | 0 | min_holding 58, sell 16, sell @ 3.88 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 6 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 33 | 17 | 9 | 0 | 0 | stop 36, buy 13, buy @ 3.7 |
| labour | 64 | 64 | 519 | 0 | 45 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), 3 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **firewood**: home ask 2.64 is above our ceiling 2.40 and last turn bought 4 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.20 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~91 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: home ask 2.72 is above our ceiling 2.60 and last turn bought 0 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **fish**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.20 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +2 crew for Flax Wyrm (crew 0.05, no projection from the game)
- labour: projection runs 100 over real use lately; planning 522, not 622
- labour expiry guard: 45 bought labour expired last turn, buy 20 (not 22) this turn

## Prestige spending, cheapest coin per prestige first

222 turns left: prestige gained now converts 67.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 50.9 | 51.3 | needs a arena (build cost 28,986); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 52.7 | 53.4 | needs a arena (build cost 28,986); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 54.7 | 55.2 | needs a arena (build cost 28,986); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 2 | arena | 210 | 57.7 | 58.5 | needs a arena (build cost 28,986); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 60.0 | 60.0 | thin at home: hop beer, wine, ham, stockfish, cheese, pies, candles |
| maintain 1 | park | 0.5 | 60.6 | 60.6 | running |
| hold banquet 4 (premium) | mansion | 20 | 60.7 | 60.7 | thin at home: hop beer, wine, ham, stockfish, candles |
| hold mass 2 (premium) | cathedral | 360 | 54.7 | 63.3 | needs a cathedral (build cost 315,400); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 3 (pies) | mansion | 8 | 63.8 | 63.8 | thin at home: hop beer, cheese, pies, candles |
| hold banquet 4 | mansion | 17.5 | 64.3 | 64.3 | thin at home: wine, hop beer, ham, stockfish, cheese, candles |
| hold banquet 2 (pies) | mansion | 7 | 67.5 | 67.5 | thin at home: wine, cheese, pies, candles |
| hold banquet 1 (fish) | mansion | 4.2 | 70.1 | 70.1 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 15.8 (keep 14); best orders clear only -0 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only 1 a turn after crew: ship stays at 0
- best towns now: Blanans +232, Vauxvais +206, Großaue +170, Angefont +164, Gotthafen +164
- Blanans would trade: cured meat buy 3 @ 25.4, furniture buy 14 @ 12.6, grain buy 8 @ 2.7, pasties buy 13 @ 16.0; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~128 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.60 (77/turn) | charcoal 19 (2.77->6.08), firewood 33 (2.77->5.7), thread 92 (6.65->7.03), wine 6 (7.93->9.4) | cloth 9 (11.13->11.9), cured meat 3 (25.62->27.8), wrought iron 2 (16.17->17) | +168 |
| Amsdermund | 1111 | 0.49 | 0.20 (26/turn) | jewellery 3 (98.17->123.5), canvas 3 (47.04->52.25), tallow 1 (19.11->26.6), casks 6 (6.62->7.84) | cured meat 3 (21.21->27.8), cloth 24 (10.82->11.9), nails 7 (5.51->6.89), axes 4 (17.85->18.9) | +140 |
| Heilegg | 826 | 0.29 | 0.20 (26/turn) | garments 10 (30.4->37.81), tallow 1 (19.11->32.68), acid 1 (135.45->141.55), nets 6 (44.8->46.36) | cheese 5 (9.13->10.83), cured meat 3 (24.78->27.8) | +116 |
| Fontaux | 411 | 0.14 | 0.30 (38/turn) | thread 57 (6.65->7.27), casks 6 (6.62->9.5), charcoal 19 (2.77->4.5), arms 3 (31.92->33.06) | cheese 5 (7.25->10.83), cured fish 3 (24.57->28.12), cloth 4 (11.23->11.9) | +101 |
| Brunnham | 1281 | 0.60 | 0.30 (38/turn) | tackles 1 (181.65->212.8), dyed cloth 14 (19.64->21.85), nets 6 (44.8->49.4), garments 10 (30.4->31.35) | cheese 5 (9.08->10.83), glassware 2 (65.1->66.5) | +81 |

**Best:** Grandgues at about +168 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 31.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 15 @ min 3.88 |  |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 9) |
| candles | 2 @ 70.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (observed), makes 0.0, holds 3 = 0.5 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 16.3, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 29.6) |
| grain | 11 @ 3.7, stop 36 |  | uses 9.0/turn (brewery 1), makes 0.0, holds 33 = 3.7 turns |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 20) |
| light armour | 1 @ 111, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 43.6) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 27.9k (cash + stock at home prices); -21/turn over 6 turns, -78/turn over 24 turns.
- Limits: cash flow >= -302/turn, prestige >= -1.30/turn (values are after 200 tax a turn).
- Today's settings: value -167/turn, cash -188/turn, prestige +1.13/turn.
- Plan: value +53/turn, cash +54/turn, prestige -1.30/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +74 vs -179, -65 vs -185, +114 vs -187.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Amsdermund: +21/turn
  - ship Flax Wyrm -> Blanans: +7/turn
  - mansion 1 1.00 -> 0.42: +165/turn
  - ropewalk 1 0.25 -> 0.07: +8/turn
  - spinnery 1 1.65 -> 1.21: +25/turn
  - net maker 0.00 -> 0.29: +4/turn
  - retting pit 1 0.91 -> 0.77: +3/turn
  - flax farm 1 4.64 -> 3.87: +9/turn
  - brewery 1 [brew mead 1] 0.00 -> 0.18: -36/turn
  - brewery 1 0.14 -> 0.00: +38/turn
- Model check over the last 59 turns: predicted -111/turn for the settings we ran, real +5/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.60, beer 3.49, timber 3.83, prestige 64.72, cash 0.00
- Orders it would set: bread buy 5 (v2 9); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 8); furniture buy 2 (v2 None); garments sell 11 (v2 10); labour buy 64 (v2 20); light armour buy 1 (v2 None)
- Recipe: brewery 1 brew beer 1 -> brew mead 1 at 0.18, worth +13/turn.
- Ship linen snake: Grandgues -> Amsdermund (+9/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Blanans (+5/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +88/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 418 (+129 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.09 |
| ret | 3 | 0.91 | 0.82 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 125/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R1: bread slot dry: 4.2 held, 4.2 a turn (basic food slot (+0.3 prestige)); our buy 5 @ 2.6, home ask 2.72 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 9 @ 2.78 (ask 2.72, cap 4.3))
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
