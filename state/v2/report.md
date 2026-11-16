# v2 shadow report

Turn 14070, 2026-11-16 15:56. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,010, prestige 3,632 (512 free, -2.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 1 | 0 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 26, buy 9, buy @ 3.42 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 18, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 521 | 0 | 8 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 5 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Tuning

- **bread**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **candles**: home ask 86.50 is above our ceiling 76.00 and last turn bought 0 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 521, not 621

## Prestige spending, cheapest coin per prestige first

331 turns left: prestige gained now converts 81.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 49.2 | 49.7 | needs a arena (build cost 28,112); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 54.0 | 54.0 | running |
| jousting 2 | arena | 210 | 53.9 | 54.4 | needs a arena (build cost 28,112); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 58.8 | 58.8 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 61.1 | 61.1 | thin at home: wine |
| hold banquet 2 (pies) | mansion | 7 | 61.3 | 61.3 | thin at home: wine |
| hold banquet 1 (meat) | mansion | 4.2 | 62.4 | 62.4 |  |
| hold banquet 2 (meat) | mansion | 6.8 | 63.5 | 63.5 | thin at home: wine |
| hold banquet 4 (pies) | mansion | 18 | 64.5 | 64.5 | thin at home: hop beer, wine, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 64.7 | 64.7 | thin at home: hop beer |
| hold banquet 4 (premium) | mansion | 20 | 64.8 | 64.8 | thin at home: hop beer, wine, stockfish, premium ham |
| hold mass 2 (premium) | cathedral | 360 | 60.7 | 64.8 | needs a cathedral (build cost 312,200); thin at home: furniture, jewellery, glassware, candles, premium garments |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 11 | 134102075 | 0.056 | - | pasties 2 | -30 |
| linen snake | 0.1 / 0.10 | 11 | 151802239 | 0.076 | - | pasties 3 | -48 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: furniture 1 @ 13.9 (keep 145); stock: pasties 1 @ 16.1 (keep 14); best orders clear only 4 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 16.2 (keep 14); best orders clear only -9 a turn after crew: ship stays at 0
- best towns now: Brunnham +99, Chribruck +99, Gosschweig +98, Bremcop +90, Blanans +86
- Brunnham would trade: candles buy 8 @ 76.5, pasties buy 1 @ 15.1; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~113 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.70 (79/turn) | timber 31 (8.19->12.25), firewood 33 (3.15->6.32), charcoal 19 (2.86->5.94), nets 2 (34.6->39.33) | acid 1 (131.25->149.15), bricks 16 (7.46->8.88), tools 7 (5->5.98), cloth 4 (8.4->9.5) | +269 |
| Vauxvais | 204 | 0.06 | 1.00 (113/turn) | wax 13 (27.3->30.02), charcoal 19 (2.86->4.8), firewood 54 (3.15->5.51), rope 1 (77.5->79.33) | dyed cloth 15 (13.55->19.95), tools 17 (5.15->5.98), acid 1 (140.7->149.15), cloth 9 (8.93->9.5) | +223 |
| Heilegg | 826 | 0.26 | 0.50 (56/turn) | charcoal 19 (2.86->6.03), garments 10 (26.4->27.93), nets 6 (34.6->36.48), flour 2 (19.53->23.94) | dyed cloth 16 (13.23->19.95), cloth 24 (7.72->9.5), acid 1 (136.5->149.15), candles 1 (82.42->86.5) | +209 |
| Amsdermund | 1111 | 0.43 | 0.30 (34/turn) | paper 5 (24.15->29.26), malt 2 (5.93->8.93), flour 2 (19.53->23.75), hides 1 (11.87->14.34) | dyed cloth 16 (13.86->19.95), glassware 3 (94.5->106.4), cloth 24 (7.98->9.5), tools 17 (4.83->5.98) | +209 |
| Pontmont | 341 | 0.10 | 1.00 (113/turn) | firewood 31 (3.15->9.5), jewellery 2 (100.28->107.35), charcoal 11 (2.86->4.45), rope 0 (77.5->80.27) | dyed cloth 9 (15.96->19.95), spinning wheels 1 (210->220.4), bricks 4 (6.14->8.88), cloth 4 (9.13->9.5) | +191 |

**Best:** Grandgues at about +269 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 9 @ 4.02, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 1 = 0.1 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 7) |
| candles | 3 @ 76.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 4 = 2.7 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 15.8, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 25.8) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 21) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 34.0 |  |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 75.5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 22.5k (cash + stock at home prices); +183/turn over 6 turns, -46/turn over 24 turns.
- Limits: cash flow >= -209/turn, prestige >= -0.88/turn (values are after 200 tax a turn).
- Today's settings: value +87/turn, cash +75/turn, prestige -2.77/turn - breaks the prestige floor.
- Plan: value +10/turn, cash +18/turn, prestige -0.88/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +266 vs +62, +416 vs +81, -2 vs +76.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Gosschweig: +11/turn
  - ship Flax Wyrm -> Blanans: +0/turn
  - brewery 1 0.14 -> 0.08: +13/turn
  - net maker 0.00 -> 0.28: +6/turn
  - spinnery 1 1.65 -> 1.59: +2/turn
  - retting pit 1 0.91 -> 0.99: -1/turn
  - flax farm 1 4.64 -> 4.93: +1/turn
  - sewing shop 1 0.30 -> 0.39: -13/turn
  - weavery 1 0.50 -> 0.62: +17/turn
  - mansion 1 0.00 -> 0.45: -105/turn
- Model check over the last 59 turns: predicted -21/turn for the settings we ran, real -86/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.80, thread 4.52, cloth 7.22, flax fibres 5.36, garments 20.90, nets 32.62, beer 3.24, timber 3.80, prestige 60.99, cash 0.00
- Orders it would set: bread buy 5 (v2 7); cloth sell 1 (v2 none); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 21); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Gosschweig (+11/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Blanans (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.7/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 421 (+132 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.27 |
| ret | 3 | 0.91 | 0.85 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 113/78, thread 1050/228, cloth 72/128

## Self-diagnosis

- R1: beer slot dry: 0.6 held, 4.2 a turn (drink slot (+0.4 prestige)); our buy 9 @ 3.42, home ask 3.84 -> **buy 9 @ 3.9 (ask 3.84, cap 5.7)** (ok)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
