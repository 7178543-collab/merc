# v2 shadow report

Turn 14279, 2026-11-25 08:21. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,871, prestige 3,719 (599 free, -0.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 64 | 0 | 12 | 0 | 0 | sell 22, sell @ 3.78 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 14 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | stop 42, buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 28 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 64 | 64 | 556 | 0 | 8 | buy 64, buy @ 2.2 |
| meat | 0 | 0 | 0 | 0 | 0 | none |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), 3 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **labour**: buying 64, short of ~74 needed -> v2: buy 74

## Tuning

- **bread**: home ask 2.82 is above our ceiling 2.60 and last turn bought 0 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 574, not 674

## Prestige spending, cheapest coin per prestige first

122 turns left: prestige gained now converts 45.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 50.3 | 51.3 | needs a arena (build cost 30,913); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 54.0 | 55.0 | needs a arena (build cost 30,913); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 59.3 | 59.3 | thin at home: wine, cheese |
| jousting 3 | arena | 230 | 57.5 | 59.3 | needs a arena (build cost 30,913); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 59.4 | 59.4 | running |
| hold banquet 2 (pies) | mansion | 7 | 59.9 | 59.9 | thin at home: wine, cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 61.1 | 61.1 |  |
| hold banquet 4 (pies) | mansion | 18 | 63.6 | 63.6 | thin at home: hop beer, wine, stockfish |
| jousting 2 | arena | 210 | 63.0 | 65.0 | needs a arena (build cost 30,913); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 5 | mansion | 22 | 65.1 | 65.1 | thin at home: hop beer, wine, stockfish, sculptures |
| hold banquet 2 (meat) | mansion | 6.8 | 66.5 | 66.5 | thin at home: wine, cheese |
| hold banquet 4 (premium) | mansion | 20 | 66.8 | 66.8 | thin at home: hop beer, wine, stockfish, premium cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 12 | 134102075 | 0 | - | pasties 3 | -45 |
| linen snake | 0.1 / 0.10 | 12 | 151802239 | 0 | beer 15 | cured meat 3 | -26 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: beer sell 12 @ 6.05, pasties buy 5 @ 16.4; crew 0.1; est +22 a turn; stock: pasties 5 @ 16.4 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 6 @ 15.1 (keep 14); best orders clear only 10 a turn after crew: ship stays at 0
- best towns now: Bordetes +68, Orlesailles +61, Heilegg +61, Großmühle +43, Darmwald +37
- Bordetes would trade: beer sell 12 @ 6.9, cured meat buy 3 @ 25.4, pasties buy 8 @ 13.9; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~125 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.50 (62/turn) | bread 184 (2.96->4.56), charcoal 20 (2.44->5.94), beer 12 (3.9->6.84), timber 20 (9.03->11.11) | cloth 8 (10.92->11.6), candles 1 (90.83->91.5), fleece 7 (9.24->9.4), flax fibres 2 (6.3->6.5) | +434 |
| Clarfranche | 1484 | 0.72 | 0.40 (50/turn) | chisels 4 (13.65->16.53), raw cloth 1 (7.93->12.92), rope 1 (84.5->87.88), premium cheese 2 (35.07->36.1) | sculptures 1 (2373->2736), tools 19 (5.25->6.27), cured meat 3 (25.41->28), butter 2 (80.33->83.6) | +370 |
| Disscester | 1474 | 0.72 | 0.40 (50/turn) | ham 1 (98.7->108.3), garments 10 (30->31.35), nets 2 (35.8->37.81), premium cheese 2 (35.07->36.1) | sculptures 1 (2394->2736), medicine 1 (152.25->157.7), lathes 1 (203.7->214.7), fleece 7 (8.24->9.4) | +351 |
| Bedenis | 566 | 0.19 | 0.20 (25/turn) | garments 10 (30->36.67), dyed cloth 3 (20.68->22.8), cloth 7 (12.18->13.11), premium cheese 2 (35.07->36.1) | sculptures 1 (2478->2736), wine 4 (5.23->6.6), seeds 5 (1.94->2.58), canvas 1 (36.33->36.86) | +337 |
| Amsdermund | 1111 | 0.47 | 0.50 (62/turn) | jewellery 4 (97.12->123.5), flour 3 (19.64->38), spinning wheels 1 (315->345.8), leather 8 (29.82->32.3) | cloth 24 (9.61->11.6), thread 62 (5.25->6.1), lathes 1 (187.95->214.7), cured meat 3 (24.78->28) | +303 |

**Best:** Grandgues at about +434 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 19 @ min 3.8 | makes 19.3, uses 4.2, holds 64 (keeps 0): sells the surplus + 4/turn of the excess |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 9) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 3 @ 29.0, stop 10 |  | goal planner: buys 3 a turn for today's rates, keeps up to 10 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 0.95 | goal planner: sells 2 a turn at 0.95, keeps 219 (no one offered it) |
| furniture | 2 @ 15.9, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 29.2) |
| grain | 9 @ 3.7, stop 36 |  | goal planner: buys 9 a turn for today's rates, keeps up to 36 (v2 had 14) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 74) |
| light armour | 1 @ 100, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 82.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 30.4k (cash + stock at home prices); +129/turn over 6 turns, -42/turn over 24 turns.
- Limits: cash flow >= -286/turn, prestige >= -1.24/turn (values are after 200 tax a turn).
- Today's settings: value -174/turn, cash -168/turn, prestige +1.20/turn.
- Plan: value +18/turn, cash +26/turn, prestige -1.24/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -19 vs -156, +118 vs -155, +129 vs -141.
- Route sales counted at most (what the ships really sold, a turn): beer 1.9, rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Etallaen: +14/turn
  - ship Flax Wyrm -> Birkeningen: +11/turn
  - mansion 1 1.00 -> 0.42: +172/turn
  - spinnery 1 1.65 -> 1.35: +5/turn
  - retting pit 1 0.91 -> 0.80: +2/turn
  - flax farm 1 4.64 -> 3.98: +8/turn
  - net maker 0.00 -> 0.28: -3/turn
  - sewing shop 1 0.30 -> 0.23: -9/turn
  - weavery 1 0.50 -> 0.38: +11/turn
- Model check over the last 58 turns: predicted -145/turn for the settings we ran, real -24/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 33.24, beer 3.23, timber 3.69, prestige 66.60, cash 0.00
- Orders it would set: bread buy 5 (v2 9); cloth sell 1 (v2 none); cured meat buy 3 (v2 12); firewood buy 4 (v2 5); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 14); labour buy 64 (v2 74); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Etallaen (+7/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Birkeningen (+4/turn over staying).
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

Buffers: flax fibres 81/77, thread 1049/228, cloth 73/128

## Self-diagnosis

- R1: bread slot dry: 8.0 held, 4.2 a turn (basic food slot (+0.3 prestige)); our buy 5 @ 2.6, home ask 2.82 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 9 @ 2.88 (ask 2.82, cap 4.3))
- R1: meat slot dry: 0.0 held, 7.0 a turn (fine food slot (+0.3 prestige)); our buy none, home ask none (no sellers at home)
