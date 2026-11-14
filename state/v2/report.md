# v2 shadow report

Turn 14020, 2026-11-14 13:36. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,687, prestige 3,525 (405 free, -0.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 108 | 25 | 12 | 0 | 0 | min_holding 60, sell 8, sell @ 3.26; stop 116, buy 39, buy @ 3.76 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 5, buy 2, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 529 | 0 | 35 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.4 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**4 risks, 1 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), 3 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **firewood**: brewery 1 ran short of firewood (buy is live (2 @ 2.4), but the home ask 3.56 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 3.56 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 10.80 x12, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 35 labour expired last turn (~62 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Notes

- labour: projection runs 99 over real use lately; planning 541, not 640
- labour expiry guard: 35 bought labour expired last turn, buy 30 (not 41) this turn

## Prestige spending, cheapest coin per prestige first

381 turns left: prestige gained now converts 85.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 53.4 | 53.4 | running |
| jousting 3 | arena | 230 | 55.6 | 56.0 | needs a arena (build cost 26,751); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 58.7 | 58.7 |  |
| hold banquet 2 (pies) | mansion | 7 | 59.2 | 59.2 | thin at home: wine, pies |
| hold banquet 2 (fish) | mansion | 6.8 | 60.2 | 60.2 | thin at home: wine, cured fish |
| hold banquet 4 (pies) | mansion | 18 | 61.3 | 61.3 | thin at home: hop beer, wine, stockfish, pies |
| jousting 2 | arena | 210 | 60.9 | 61.3 | needs a arena (build cost 26,751); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (premium) | mansion | 20 | 62.5 | 62.5 | thin at home: hop beer, wine, stockfish |
| hold mass 2 (premium) | cathedral | 360 | 61.0 | 64.1 | needs a cathedral (build cost 297,150); thin at home: furniture, jewellery, glassware, candles, premium garments |
| hold banquet 3 (pies) | mansion | 8 | 64.5 | 64.5 | thin at home: hop beer, pies |
| hold banquet 4 | mansion | 17.5 | 64.9 | 64.9 | thin at home: wine, hop beer, ham, stockfish |
| hold banquet 2 (meat) | mansion | 6.8 | 65.2 | 65.2 | thin at home: wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.10 | 11 | 151802239 | 0.124 | - | cured meat 5, pasties 7 | -220 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 15.1 (keep 14); best orders clear only -1 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 15.6 (keep 14); best orders clear only 3 a turn after crew: ship stays at 0
- best towns now: Herschweig +20, Gotthafen +19, Hofkirchen +18, Brebronn +17, Unterhufe +16
- Herschweig would trade: cured meat buy 3 @ 22.4, furniture buy 1 @ 14.2, pasties buy 1 @ 14.5; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~110 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.70 (77/turn) | timber 42 (8.03->11.88), firewood 29 (3.74->6.55), charcoal 19 (2.54->3.42), pasties 1 (13.2->14.25) | cured meat 3 (24.15->27), cloth 7 (8.4->8.65), garments 2 (22.47->23) | +194 |
| Blanans | 297 | 0.09 | 0.70 (77/turn) | timber 42 (8.03->12.44), cheese 11 (7.72->10.64), bricks 5 (5.93->8.64), nets 6 (36.6->37.24) | cloth 12 (7.88->8.65), dyed cloth 3 (10.71->12.82), cured meat 3 (25.2->27), garments 2 (22.68->23) | +190 |
| Fontaux | 411 | 0.12 | 0.80 (88/turn) | thread 79 (4.74->5.65), charcoal 19 (2.54->5.22), timber 23 (8.03->10.45), bricks 4 (5.93->8.79) | belts 1 (24.78->32.11), cured meat 3 (24.36->27), dyed cloth 3 (10.82->12.82), cloth 5 (8.29->8.65) | +133 |
| Nürnnieder | 520 | 0.15 | 0.20 (22/turn) | thread 70 (4.74->5.22), garments 10 (20.8->22.99), tapestries 1 (777->798), cheese 4 (7.72->12.63) | furniture 9 (14.6->16.53), cured meat 3 (24.78->27), cloth 6 (8.14->8.65), seeds 1 (2.1->2.58) | +120 |
| Clairlond | 1288 | 0.52 | 0.40 (44/turn) | garments 10 (20.8->29.07), varnish 2 (17.12->20.9) | furniture 9 (13.02->16.53), tools 26 (5.46->6.32), butter 1 (70.35->78.38), dyed cloth 3 (11.45->12.82) | +115 |

**Best:** Grandgues at about +194 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 15 @ 3.88, stop 60 |  | uses 15.0/turn (household upkeep), makes 0.0, holds 108 = 7.2 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 87.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 | off | a building is stalled on cured meat: no sell until it runs again |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 20.2) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 30) |
| light armour | 1 @ 101, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.4 | goal planner: sells 9 at 31.4 (v2 had 9 at 35.6) |
| pasties |  | 2 @ min 12.5 | goal planner: sells 2 a turn at 12.5, keeps 0 (no one offered it) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 26.8k (cash + stock at home prices); -107/turn over 6 turns, -158/turn over 24 turns.
- Limits: cash flow >= -320/turn, prestige >= -0.44/turn (values are after 200 tax a turn).
- Today's settings: value -188/turn, cash -164/turn, prestige +1.98/turn.
- Plan: value -23/turn, cash -6/turn, prestige -0.44/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +27 vs -150, +125 vs -158, -280 vs -164.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Brebronn: +0/turn
  - ship Flax Wyrm -> Bremcop: +6/turn
  - mansion 1 1.00 -> 0.43: +149/turn
  - net maker 0.00 -> 0.29: +6/turn
  - spinnery 1 1.65 -> 1.34: -0/turn
  - retting pit 1 0.91 -> 0.83: +1/turn
  - flax farm 1 4.64 -> 3.94: +6/turn
  - weavery 1 0.50 -> 0.40: -7/turn
  - sewing shop 1 0.30 -> 0.23: +8/turn
- Model check over the last 59 turns: predicted -25/turn for the settings we ran, real +7/turn.
- Worth of one more unit per turn: labour 1.66, thread 4.18, cloth 6.67, flax fibres 4.95, garments 19.30, nets 30.28, beer 3.21, timber 3.44, prestige 60.36, cash 0.00
- Orders it would set: candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 2 (v2 3); garments sell 11 (v2 10); grain buy 9 (v2 0); labour buy 64 (v2 30); light armour buy 1 (v2 None); pasties sell 2 (v2 none)
- Ship linen snake: Grandgues -> Brebronn (+2/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Bremcop (+6/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 422 (+133 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.34 |
| ret | 3 | 0.91 | 0.87 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 107/77, thread 1058/228, cloth 72/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask 3.56; ask over the cap 2.1 (60 coin per prestige)
- R1: prestige rate -0.12 a turn vs 12-turn median +2.00; likely: dry slot: firewood
- R2: spinnery 1 blocked by thread space: 1058 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
