# v2 shadow report

Turn 14284, 2026-11-25 13:19. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,215, prestige 3,715 (595 free, -1.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 40 | 0 | 8 | 0 | 0 | sell 17, sell @ 3.88; stop 116, buy 39, buy @ 4.34 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 15 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 28 | 9 | 9 | 0 | 0 | stop 36, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 546 | 0 | 18 | buy 64, buy @ 2.2 |
| meat | 0 | 0 | 0 | 0 | 0 | none |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (4 @ 29), 3 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.7 turns of cured meat left and buying 4 (need 12) -> v2: buy 12

## Waste (money lost now)

- **labour**: 18 labour expired last turn (~35 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: home ask 11.20 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 107 over real use lately; planning 546, not 652

## Prestige spending, cheapest coin per prestige first

117 turns left: prestige gained now converts 44.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 50.6 | 51.7 | needs a arena (build cost 32,098); thin at home: protection, light armour, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 54.3 | 55.4 | needs a arena (build cost 32,098); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 59.7 | 59.7 | running |
| jousting 3 | arena | 230 | 59.3 | 61.3 | needs a arena (build cost 32,098); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 61.4 | 61.4 |  |
| hold banquet 1 (fish) | mansion | 4.2 | 62.0 | 62.0 |  |
| hold banquet 2 (pies) | mansion | 7 | 62.5 | 62.5 |  |
| hold banquet 4 (pies) | mansion | 18 | 65.8 | 65.8 | thin at home: hop beer, stockfish |
| jousting 2 | arena | 210 | 64.9 | 67.1 | needs a arena (build cost 32,098); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 68.7 | 68.7 |  |
| hold banquet 4 (premium) | mansion | 20 | 69.0 | 69.0 | thin at home: hop beer, stockfish |
| hold banquet 4 | mansion | 17.5 | 69.7 | 69.7 | thin at home: hop beer, stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: beer sell 14 @ 6.9, cured meat buy 3 @ 27.0; crew 0.1; est +30 a turn
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 13.8 (keep 14); best orders clear only 8 a turn after crew: ship stays at 0
- best towns now: Bordetes +80, Heilegg +58, Großmühle +53, Darmwald +40, Hofkirchen +40
- Bordetes would trade: beer sell 14 @ 7.8, cured meat buy 3 @ 26.6, pasties buy 8 @ 14.4; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~127 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Pontmont | 341 | 0.12 | 0.60 (76/turn) | timber 35 (8.45->15.58), garments 10 (31.4->36.86), paper 14 (28.14->30.4), cookware 4 (30.45->35.91) | fleece 4 (9.4->12.92), thread 20 (5.25->6.05), butter 1 (69.83->76), bricks 8 (5.25->8.17) | +339 |
| Hofkirchen | 991 | 0.40 | 0.60 (76/turn) | tools 26 (6.83->9.5), ploughs 4 (81.9->92.15), canvas 4 (40.53->44.84), furniture 15 (16.48->18.62) | cloth 17 (7.93->12.4), coats 3 (89.25->97.85), fleece 7 (11.03->12.92), candles 1 (84->92) | +240 |
| Grandgues | 152 | 0.05 | 0.30 (38/turn) | charcoal 20 (2.56->7.31), cured fish 8 (25.62->30.59), beer 14 (4->6.84), wine 14 (7.19->9.5) | fleece 3 (9.82->12.92), thread 62 (5.93->6.05), cured meat 3 (27.93->29) | +239 |
| Heilegg | 826 | 0.29 | 0.40 (51/turn) | flour 3 (21.21->38), jewellery 2 (100.28->116.85), coats 4 (109.2->114), leather 8 (29.82->32.3) | cloth 23 (10.29->12.4), fleece 12 (11.03->12.92), cured meat 3 (24.78->29), cheese 5 (5.72->6.51) | +231 |
| Nürnnieder | 520 | 0.18 | 0.20 (25/turn) | leather 8 (29.82->32.3), rope 1 (84->96.9) | cloth 24 (7.35->12.4), fleece 16 (9.19->12.92), cured meat 3 (24.15->29), garments 2 (28.14->31.6) | +222 |

**Best:** Pontmont at about +339 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 35.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 20 @ min 3.88 | makes 19.3, uses 0.8, holds 40 (keeps 0): sells the surplus + 2/turn of the excess |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 9) |
| candles | 2 @ 94, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 12 @ 29.0, stop 24 |  | uses 6.0/turn (observed), makes 0.0, holds 4 = 0.7 turns |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 0.95 | goal planner: sells 2 a turn at 0.95, keeps 219 (no one offered it) |
| furniture | 2 @ 16.1, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 30.6) |
| grain | 9 @ 3.7, stop 36 |  | goal planner: buys 9 a turn for today's rates, keeps up to 36 (v2 had 13) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 46) |
| light armour | 1 @ 95, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 81.5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.4k (cash + stock at home prices); -28/turn over 6 turns, -0/turn over 24 turns.
- Limits: cash flow >= -301/turn, prestige >= -1.23/turn (values are after 200 tax a turn).
- Today's settings: value -176/turn, cash -170/turn, prestige +0.74/turn.
- Plan: value -9/turn, cash +0/turn, prestige -1.23/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -10 vs -162, +40 vs -166, -16 vs -162.
- Route sales counted at most (what the ships really sold, a turn): beer 1.8, rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Etallaen: +17/turn
  - ship Flax Wyrm -> Hofkirchen: +5/turn
  - mansion 1 1.00 -> 0.53: +141/turn
  - brewery 1 0.14 -> 0.20: +4/turn
  - net maker 0.00 -> 0.28: +3/turn
  - flax farm 1 4.64 -> 3.87: -3/turn
  - retting pit 1 0.91 -> 0.77: +2/turn
  - spinnery 1 1.65 -> 1.32: +11/turn
  - sewing shop 1 0.30 -> 0.21: -9/turn
  - weavery 1 0.50 -> 0.35: +16/turn
- Model check over the last 59 turns: predicted -145/turn for the settings we ran, real -15/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 33.23, beer 3.23, timber 3.62, prestige 67.09, cash 0.00
- Orders it would set: bread buy 5 (v2 9); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 5); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 13); labour buy 64 (v2 46); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Etallaen (+11/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Hofkirchen (+5/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 430 (+141 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.75 |
| ret | 3 | 0.91 | 0.95 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 86/77, thread 1050/228, cloth 72/128

## Self-diagnosis

- R1: cured meat slot dry: 4.0 held, 6.0 a turn (mansion 1 hold banquet 1 (meat) (+4.2 prestige)); our buy 4 @ 29, home ask 29.0; our bid is already at/over the ask (sellers too thin)
- R1: meat slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask none (no sellers at home)
- R5: tar buy not filling: bid 11 under the home ask 11.2 for 4 turns, bought 0.0 of 1, 0.5 held (1.8 turns); raise needs Taylor (ceiling 11.0)
