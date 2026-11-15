# v2 shadow report

Turn 14036, 2026-11-15 05:35. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,759, prestige 3,597 (477 free, -0.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 33 | 0 | 12 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 33, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 501 | 0 | 63 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**5 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), 3 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), but the home ask 3.02 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.02 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.80 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 63 labour expired last turn (~105 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: home ask 11.80 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: +1 crew for linen snake (crew 0.01, no projection from the game)
- labour: projection runs 100 over real use lately; planning 502, not 602
- labour expiry guard: 63 bought labour expired last turn, buy 2 (not 2) this turn

## Prestige spending, cheapest coin per prestige first

365 turns left: prestige gained now converts 84.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.1 | 50.1 | running |
| jousting 3 | arena | 230 | 55.2 | 55.5 | needs a arena (build cost 26,112); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 56.3 | 56.3 |  |
| hold banquet 2 (pies) | mansion | 7 | 57.0 | 57.0 | thin at home: pasties, wine, cheese |
| hold banquet 2 (fish) | mansion | 6.8 | 57.2 | 57.2 | thin at home: wine, cured fish, cheese |
| hold banquet 4 (pies) | mansion | 18 | 58.4 | 58.4 | thin at home: hop beer, wine, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 59.9 | 59.9 | thin at home: pasties, hop beer |
| jousting 2 | arena | 210 | 60.4 | 60.8 | needs a arena (build cost 26,112); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 60.9 | 60.9 | thin at home: hop beer, wine, stockfish |
| hold banquet 3 (fish) | mansion | 7.6 | 61.3 | 61.3 | thin at home: hop beer, cured fish, cheese |
| hold banquet 2 (meat) | mansion | 6.8 | 61.5 | 61.5 | thin at home: wine, cured meat, cheese |
| hold banquet 4 | mansion | 17.5 | 61.7 | 61.7 | thin at home: wine, hop beer, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: pasties buy 11 @ 15.4; crew 0.1; est +28 a turn; stock: pasties 11 @ 15.4 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 15.4 (keep 14); best orders clear only -4 a turn after crew: ship stays at 0
- best towns now: Gottweiler +480, Gotthafen +411, Fulkirch +259, Donaunieder +254, Nürnnieder +250
- Gottweiler would trade: cured meat buy 3 @ 22.6, furniture buy 46 @ 14.6, pasties buy 3 @ 13.6; crew 0.8

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~110 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.50 (55/turn) | timber 26 (7.93->12.44), bread 159 (2.39->2.83), charcoal 19 (2.48->4.08), flour 4 (14.6->18.52) | cloth 6 (8.77->11.69), thread 14 (5.35->5.85), coats 1 (85.58->89.3), tiles 3 (3.89->4.46) | +213 |
| Fontaux | 411 | 0.12 | 0.60 (66/turn) | charcoal 19 (2.48->6.37), garments 10 (21->23.75), timber 18 (7.93->11.21), flour 3 (14.6->18.81) | thread 47 (5.25->5.85), jewellery 3 (89.78->94.52), cloth 4 (9.61->11.69), tools 16 (5.46->6.03) | +176 |
| Hofkirchen | 991 | 0.35 | 0.40 (44/turn) | furniture 18 (17.32->21.47), lead bars 9 (14.7->17.29), varnish 4 (17.12->20.33), flour 4 (14.6->19.57) | cloth 13 (7.35->11.69), flax fibres 23 (5.78->6.8), coats 1 (81.9->89.3), casks 14 (5.46->6.55) | +172 |
| Darmwald | 1022 | 0.37 | 0.70 (77/turn) | charcoal 19 (2.48->9.5), flour 3 (14.6->19.76), lead ore 1 (8.77->15.2), yarn 2 (4.2->4.64) | cloth 13 (7.72->11.69), jewellery 3 (91.88->94.52), cured meat 3 (24.15->25.6), chisels 1 (8.24->9.45) | +148 |
| Amsdermund | 1111 | 0.42 | 0.50 (55/turn) | flour 4 (14.6->24.13), lead bars 7 (14.7->16.62), wine 2 (6.51->9.5), candles 1 (77.7->79.8) | cloth 13 (7.56->11.69), spinning wheels 3 (220.5->229.9), tools 16 (4.83->6.03), casks 14 (5.35->6.55) | +145 |

**Best:** Grandgues at about +213 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 19 @ 3.46, stop 47 |  | uses 11.7/turn (household upkeep), makes 0.0, holds 33 = 2.8 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 75.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 3 @ 29.0, stop 11 |  | goal planner: buys 3 a turn for today's rates, keeps up to 11 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 16.9, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 20.4) |
| grain | 8 @ 3.7, stop 32 |  | goal planner: buys 8 a turn for today's rates, keeps up to 32 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 2) |
| light armour | 1 @ 109, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 36.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.3/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 24.0k (cash + stock at home prices); +28/turn over 6 turns, -158/turn over 24 turns.
- Limits: cash flow >= -282/turn, prestige >= -0.74/turn (values are after 200 tax a turn).
- Today's settings: value -170/turn, cash -174/turn, prestige +1.61/turn.
- Plan: value -6/turn, cash +1/turn, prestige -0.74/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -68 vs -180, -26 vs -184, -110 vs -189.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Kirchwerp: +21/turn
  - ship Flax Wyrm -> Donaunieder: +1/turn
  - mansion 1 1.00 -> 0.44: +144/turn
  - net maker 0.00 -> 0.29: +7/turn
  - flax farm 1 4.64 -> 4.14: -3/turn
  - retting pit 1 0.91 -> 0.82: -1/turn
  - spinnery 1 1.65 -> 1.31: +3/turn
  - ropewalk 1 0.25 -> 0.00: +1/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.22: +8/turn
  - sewing shop 1 0.30 -> 0.24: -5/turn
- Model check over the last 59 turns: predicted -99/turn for the settings we ran, real -86/turn.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.96, garments 19.30, nets 30.19, beer 3.01, timber 3.40, prestige 61.16, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); cured meat buy 3 (v2 12); firewood buy 2 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 8 (v2 0); labour buy 64 (v2 2); light armour buy 1 (v2 None); rope sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.22, worth +8/turn.
- Ship linen snake: Grandgues -> Kirchwerp (+9/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Donaunieder (+1/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 425 (+136 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.47 |
| ret | 3 | 0.91 | 0.89 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 98/77, thread 1064/228, cloth 72/128

## Self-diagnosis

- R1: beer slot dry: 33.1 held, 19.2 a turn (drink slot (+0.4 prestige); mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy none, home ask 3.3 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 39 @ 3.36 (ask 3.3, cap 14.4))
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask 3.02; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1064 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
