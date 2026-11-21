# v2 shadow report

Turn 14178, 2026-11-21 03:44. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,135, prestige 3,734 (614 free, -1.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 82 | 0 | 12 | 0 | 0 | min_holding 58, sell 17, sell @ 3.88 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 6 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 29 | 18 | 9 | 0 | 0 | stop 36, buy 17, buy @ 3.7 |
| labour | 64 | 64 | 519 | 0 | 45 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 4 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), but the home ask 29.40 is above it); labour need rises ~35/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **firewood**: home ask 2.62 is above our ceiling 2.40 and last turn bought 4 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.30 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 45 labour expired last turn (~93 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: home ask 2.74 is above our ceiling 2.60 and last turn bought 0 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **cured meat**: home ask 29.40 is above our ceiling 29.00 and last turn bought 3 of ~6 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.30 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +2 crew for Flax Wyrm (crew 0.04, no projection from the game)
- labour: projection runs 100 over real use lately; planning 521, not 621
- labour expiry guard: 45 bought labour expired last turn, buy 20 (not 21) this turn

## Prestige spending, cheapest coin per prestige first

223 turns left: prestige gained now converts 67.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 51.0 | 51.4 | needs a arena (build cost 29,126); thin at home: protection, light armour, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 53.0 | 53.7 | needs a arena (build cost 29,126); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 54.9 | 55.3 | needs a arena (build cost 29,126); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 2 | arena | 210 | 58.0 | 58.8 | needs a arena (build cost 29,126); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 59.5 | 59.5 | thin at home: hop beer, wine, stockfish, cheese, candles |
| hold banquet 4 (premium) | mansion | 20 | 60.6 | 60.6 | thin at home: hop beer, wine, stockfish, candles |
| maintain 1 | park | 0.5 | 61.8 | 61.8 | running |
| hold banquet 3 (pies) | mansion | 8 | 62.0 | 62.0 | thin at home: hop beer, cheese, candles |
| hold mass 2 (premium) | cathedral | 360 | 55.1 | 63.6 | needs a cathedral (build cost 315,990); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 4 | mansion | 17.5 | 63.8 | 63.8 | thin at home: wine, hop beer, ham, stockfish, cheese, candles |
| hold banquet 2 (pies) | mansion | 7 | 67.5 | 67.5 | thin at home: wine, cheese, candles |
| hold banquet 1 (fish) | mansion | 4.2 | 71.0 | 71.0 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: cured meat buy 3 @ 27.4, pasties buy 11 @ 15.6; crew 0.1; est +29 a turn; stock: pasties 11 @ 15.6 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; best orders clear only 6 a turn after crew: ship stays at 0
- best towns now: Blanans +235, Gotthafen +174, Heidlowe +170, Disscester +164, Clairlond +163
- Blanans would trade: cured meat buy 3 @ 25.2, furniture buy 14 @ 12.7, grain buy 8 @ 2.76, pasties buy 13 @ 16.0; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~132 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.90 (119/turn) | charcoal 19 (2.79->6.03), firewood 33 (2.75->5.7), thread 92 (6.6->7.03), bread 256 (2.88->3.13) | cloth 10 (11.13->13.1), cured meat 3 (25.62->29.4), furniture 1 (16.07->16.9) | +209 |
| Calange | 218 | 0.08 | 0.10 (13/turn) | thread 26 (6.6->8.31), garments 10 (30.4->32.11), flax fibres 5 (6.35->7.36), cookware 12 (23.52->23.75) | cloth 18 (11.23->13.1), swords 1 (214.2->220.4), cured fish 3 (26.25->28.12), cured meat 3 (27.51->29.4) | +118 |
| Clairas | 374 | 0.13 | 0.20 (26/turn) | dyed cloth 4 (18.79->20.71), malt 3 (8.4->9.45) | cloth 24 (10.13->13.1), cheese 12 (8.09->11.02), thread 33 (6.56->6.95), cured meat 3 (28.14->29.4) | +117 |
| Pontmont | 341 | 0.12 | 0.60 (79/turn) | cookware 12 (23.52->25.46), timber 25 (8.93->11.4), charcoal 19 (2.79->3.97), beer 9 (4->4.58) | cheese 12 (7.35->11.02), tools 15 (5.78->6.17), cured meat 3 (28.56->29.4), garments 2 (30.45->31) | +102 |
| Kirchwerp | 1072 | 0.47 | 0.60 (79/turn) | flax fibres 7 (6.35->8.69), butter 7 (81.38->84.08), casks 5 (6.88->9.36), tiles 7 (3.57->9.26) | cloth 17 (10.5->13.1), garments 2 (26.67->31), dyed cloth 5 (14.7->16.25), cured meat 3 (27.09->29.4) | +99 |

**Best:** Grandgues at about +209 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 31.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had None) |
| beer |  | 16 @ min 3.88 |  |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 9) |
| candles | 2 @ 70.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (observed), makes 0.0, holds 3 = 0.5 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 29.6) |
| grain | 13 @ 3.7, stop 36 |  | uses 9.0/turn (brewery 1), makes 0.0, holds 29 = 3.2 turns |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 20) |
| light armour | 1 @ 111, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 43.6) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.0k (cash + stock at home prices); +9/turn over 6 turns, -54/turn over 24 turns.
- Limits: cash flow >= -297/turn, prestige >= -1.31/turn (values are after 200 tax a turn).
- Today's settings: value -169/turn, cash -187/turn, prestige +1.13/turn.
- Plan: value +53/turn, cash +55/turn, prestige -1.31/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +48 vs -189, +74 vs -179, -65 vs -185.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Amsdermund: +20/turn
  - ship Flax Wyrm -> Blanans: +8/turn
  - mansion 1 1.00 -> 0.42: +166/turn
  - ropewalk 1 0.25 -> 0.07: +9/turn
  - spinnery 1 1.65 -> 1.22: +25/turn
  - net maker 0.00 -> 0.29: +5/turn
  - retting pit 1 0.91 -> 0.77: +4/turn
  - flax farm 1 4.64 -> 3.89: +9/turn
  - brewery 1 [brew mead 1] 0.00 -> 0.17: -38/turn
  - brewery 1 0.14 -> 0.00: +39/turn
- Model check over the last 59 turns: predicted -107/turn for the settings we ran, real +11/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.62, beer 3.49, timber 3.83, prestige 64.72, cash 0.00
- Orders it would set: arms buy 1 (v2 None); bread buy 5 (v2 9); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 8); garments sell 11 (v2 10); labour buy 64 (v2 20); light armour buy 1 (v2 None)
- Recipe: brewery 1 brew beer 1 -> brew mead 1 at 0.17, worth +12/turn.
- Ship linen snake: Grandgues -> Amsdermund (+8/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Blanans (+6/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +87/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 418 (+129 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.11 |
| ret | 3 | 0.91 | 0.82 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 123/77, thread 1064/228, cloth 73/128

## Self-diagnosis

- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
- R5: bread buy not filling: bid 2.6 under the home ask 2.74 for 3 turns, bought 0.0 of 5, 8.4 held (2.0 turns)
