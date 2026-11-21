# v2 shadow report

Turn 14177, 2026-11-21 02:39. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,200, prestige 3,734 (614 free, -1.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 92 | 0 | 12 | 0 | 0 | min_holding 58, sell 17, sell @ 3.88 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 6 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 21 | 7 | 9 | 0 | 0 | stop 36, buy 17, buy @ 3.7 |
| labour | 64 | 64 | 519 | 0 | 45 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), 3 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **firewood**: home ask 2.66 is above our ceiling 2.40 and last turn bought 4 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.30 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~92 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **grain**: home ask 3.78 is above our ceiling 3.70 and last turn bought 7 of ~9 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.30 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +2 crew for Flax Wyrm (crew 0.03, no projection from the game)
- labour: +1 crew for linen snake (crew 0.01, no projection from the game)
- labour: projection runs 100 over real use lately; planning 521, not 621
- labour expiry guard: 45 bought labour expired last turn, buy 20 (not 21) this turn

## Prestige spending, cheapest coin per prestige first

224 turns left: prestige gained now converts 67.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 47.9 | 48.3 | needs a arena (build cost 29,329); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 51.6 | 52.0 | needs a arena (build cost 29,329); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 52.8 | 53.6 | needs a arena (build cost 29,329); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 | arena | 210 | 57.9 | 58.7 | needs a arena (build cost 29,329); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 60.1 | 60.1 | thin at home: hop beer, wine, stockfish, cheese, candles |
| maintain 1 | park | 0.5 | 61.2 | 61.2 | running |
| hold banquet 4 (premium) | mansion | 20 | 61.3 | 61.3 | thin at home: hop beer, wine, stockfish, candles |
| hold banquet 3 (pies) | mansion | 8 | 63.4 | 63.4 | thin at home: hop beer, cheese, candles |
| hold mass 2 (premium) | cathedral | 360 | 55.1 | 63.6 | needs a cathedral (build cost 317,300); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 4 | mansion | 17.5 | 64.3 | 64.3 | thin at home: wine, hop beer, ham, stockfish, cheese, candles |
| hold banquet 2 (pies) | mansion | 7 | 67.0 | 67.0 | thin at home: wine, cheese, candles |
| hold banquet 1 (meat) | mansion | 4.2 | 71.6 | 71.6 | running |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: pasties buy 9 @ 15.1; crew 0.1; est +21 a turn; stock: pasties 9 @ 15.1 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only 3 a turn after crew: ship stays at 0
- best towns now: Blanans +235, Großmühle +197, Clairlond +178, Dortgart +176, Gotthafen +165
- Blanans would trade: cured meat buy 3 @ 25.0, furniture buy 14 @ 12.6, grain buy 8 @ 2.8, pasties buy 13 @ 15.9; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~131 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.60 (79/turn) | charcoal 19 (2.79->5.94), thread 92 (6.6->7.03), firewood 33 (2.79->5.37), beer 10 (4->4.75) | cloth 10 (11.13->13.2), cured meat 3 (25.83->28.2), cured fish 3 (32.13->32.87), wrought iron 1 (16.38->16.91) | +162 |
| Amsdermund | 1111 | 0.50 | 0.30 (39/turn) | swords 1 (273->300.2), raw cloth 4 (8.82->10.45), casks 7 (6.56->7.84), tallow 1 (24.36->26.6) | cloth 24 (10.71->13.2), cured meat 3 (21->28.2), cheese 5 (7.77->10.16), cured fish 3 (28.77->32.87) | +125 |
| Blanans | 297 | 0.10 | 0.20 (26/turn) | nets 2 (44->51.77), flour 1 (21.42->23.18), raw cloth 4 (8.82->9.26), dyed yarn 1 (4.91->5.13) | cloth 24 (11.13->13.2), cured fish 3 (23.52->32.87), cheese 5 (8.87->10.16), cured meat 3 (25.83->28.2) | +106 |
| Clairas | 374 | 0.13 | 0.20 (26/turn) | malt 4 (8.51->9.88), dyed yarn 1 (4.91->5.37), logs 2 (8.4->11.02), nets 3 (44->44.27) | cloth 24 (10.19->13.2), cheese 5 (7.98->10.16), cured fish 3 (29.82->32.87), yarn 25 (6.14->6.6) | +102 |
| Nürnnieder | 520 | 0.18 | 0.20 (26/turn) | bricks 1 (6.25->11.4), dyed yarn 1 (4.91->6.84), nets 2 (44->45.41), leather 1 (31.92->33.63) | cloth 24 (10.5->13.2), beer 11 (3.28->4.42), cured fish 3 (29.4->32.87), garments 2 (27.72->31) | +101 |

**Best:** Grandgues at about +162 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 31.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 17 @ min 3.88 | makes 19.3, uses 4.2, holds 92 (keeps 58): sells the surplus + 2/turn of the excess |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 7) |
| candles | 2 @ 70.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (observed), makes 0.0, holds 3 = 0.5 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 16.2, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 29.8) |
| grain | 17 @ 3.7, stop 36 |  | uses 9.0/turn (brewery 1), makes 0.0, holds 21 = 2.4 turns |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 20) |
| light armour | 1 @ 110, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 42.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 27.8k (cash + stock at home prices); -36/turn over 6 turns, -115/turn over 24 turns.
- Limits: cash flow >= -300/turn, prestige >= -1.31/turn (values are after 200 tax a turn).
- Today's settings: value -169/turn, cash -185/turn, prestige +1.12/turn.
- Plan: value +53/turn, cash +58/turn, prestige -1.31/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -61 vs -173, +48 vs -189, +74 vs -179.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Amsdermund: +24/turn
  - ship Flax Wyrm -> Blanans: +5/turn
  - mansion 1 1.00 -> 0.42: +163/turn
  - ropewalk 1 0.25 -> 0.05: +8/turn
  - spinnery 1 1.65 -> 1.22: +28/turn
  - net maker 0.00 -> 0.29: +4/turn
  - retting pit 1 0.91 -> 0.77: +3/turn
  - flax farm 1 4.64 -> 3.89: +10/turn
  - brewery 1 [brew mead 1] 0.00 -> 0.15: -35/turn
  - brewery 1 0.14 -> 0.00: +38/turn
- Model check over the last 59 turns: predicted -102/turn for the settings we ran, real +7/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.61, beer 3.50, timber 3.87, prestige 65.06, cash 0.00
- Orders it would set: bread buy 5 (v2 7); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 8); furniture buy 2 (v2 None); garments sell 11 (v2 10); labour buy 64 (v2 20); light armour buy 1 (v2 None)
- Recipe: brewery 1 brew beer 1 -> brew mead 1 at 0.15, worth +10/turn.
- Ship linen snake: Grandgues -> Amsdermund (+10/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Blanans (+4/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +87/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 419 (+130 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.14 |
| ret | 3 | 0.91 | 0.83 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 121/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
