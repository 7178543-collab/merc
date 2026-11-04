# v2 shadow report

Turn 13772, 2026-11-04 05:00. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 7,205, prestige 3,229 (109 free, -0.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 15 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.4 |
| grain | 33 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 529 | 6 | 0 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **labour**: buying 29, short of ~35 needed -> v2: buy 35

## Notes

- labour: projection runs 100 over real use lately; planning 535, not 635

## Prestige spending, cheapest coin per prestige first

629 turns left: prestige gained now converts 95.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.7 | 47.7 | running |
| hold banquet 4 (pies) | mansion | 18 | 50.6 | 50.6 | thin at home: hop beer, stockfish |
| jousting 3 | arena | 230 | 53.0 | 53.2 | needs a arena (build cost 25,239); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 53.3 | 53.3 | thin at home: hop beer, ham, stockfish |
| hold banquet 1 (fish) | mansion | 4.2 | 53.5 | 53.5 |  |
| hold banquet 4 (premium) | mansion | 20 | 54.2 | 54.2 | thin at home: hop beer, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 54.3 | 54.3 | thin at home: hop beer, pies |
| hold banquet 2 (pies) | mansion | 7 | 54.9 | 54.9 | thin at home: pies |
| hold banquet 2 (fish) | mansion | 6.8 | 55.4 | 55.4 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 55.9 | 55.9 | thin at home: hop beer |
| hold banquet 1 (meat) | mansion | 4.2 | 57.8 | 57.8 |  |
| jousting 2 | arena | 210 | 58.0 | 58.2 | needs a arena (build cost 25,239); thin at home: swords, protection, coats, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.20 | 19 | 134102075 | 0.328 | - | furniture 19, pasties 1 | -264 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 19 @ 13.9, pasties buy 1 @ 13.8; crew 0.2; est +223 a turn; stock: furniture 19 @ 13.9 (keep 145); stock: pasties 1 @ 13.8 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 14.0 (keep 14); best orders clear only -5 a turn after crew: ship stays at 0
- best towns now: Hofkirchen +508, Angefont +469, Amsdermund +464, Bordetes +448, Donaunieder +314
- Hofkirchen would trade: furniture buy 43 @ 13.2; crew 0.6

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~99 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Blanans | 297 | 0.08 | 1.00 (99/turn) | bread 150 (2.21->2.53), timber 25 (6.98->8.69), thread 7 (4.66->6.37), charcoal 19 (2.31->3.31) | garments 21 (20.37->25.46), cloth 24 (7.3->8.15), bricks 1 (7.25->11.69), pies 2 (13.65->14.72) | +185 |
| Neuborn | 780 | 0.21 | 0.40 (40/turn) | charcoal 19 (2.31->6.13), cured fish 4 (22.68->23.94), tallow 1 (19.64->21.28), beer 15 (2.72->3.13) | garments 21 (20.37->25.46), cloth 24 (6.88->8.15) | +174 |
| Pontmont | 341 | 0.09 | 0.10 (10/turn) | beer 15 (2.72->4.33), paper 2 (21->22.61), flour 1 (17.12->18.71), pasties 1 (12.5->14.25) | garments 21 (20.48->25.46), cloth 20 (7.3->8.15), gold ore 1 (141.75->157.7), candles 1 (81.9->82.5) | +162 |
| Heilegg | 826 | 0.23 | 0.50 (50/turn) | cured fish 7 (22.68->25.65), charcoal 19 (2.31->4.89), logs 1 (3.82->11.21), pasties 1 (12.5->14.25) | garments 21 (20.48->25.46), cloth 24 (7.14->8.15), casks 2 (5.51->6.08), flax fibres 4 (5.35->5.85) | +156 |
| Bordetes | 831 | 0.23 | 0.40 (40/turn) | charcoal 19 (2.31->5.56), paper 2 (21->22.61), premium cheese 1 (26.67->27.36) | garments 21 (20.37->25.46), cloth 24 (7.3->8.15), gold ore 1 (149.1->157.7) | +154 |

**Best:** Blanans at about +185 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 30.8, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 0 = 0.0 turns |
| beer |  | 16 @ min 3.06 | goal planner: sells 16 at 3.06 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 16 = 3.9 turns |
| cloth |  | 1 @ min 7.1 | goal planner: sells 1 a turn at 7.1, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 19.4 | goal planner: sells 11 at 19.4 (v2 had 10 at 26.4) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 30 @ 2.2, stop - |  | goal planner: buys 30 for today's rates (v2 had 35) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 37.2) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 79.0) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 0 = 1.3 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 19.1k (cash + stock at home prices); -139/turn over 6 turns, +97/turn over 24 turns.
- Limits: cash flow >= -134/turn, prestige >= +7.95/turn (values are after 200 tax a turn).
- Today's settings: value +102/turn, cash +96/turn, prestige -0.55/turn - breaks the prestige floor.
- Plan: value -116/turn, cash -109/turn, prestige +3.65/turn - could not meet the prestige floor.
- Cash check (real vs predicted cash a tick, last 3): -278 vs +111, -280 vs +104, -116 vs +88 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Boistot: +6/turn
  - ship Flax Wyrm -> Donaunieder: +0/turn
  - net maker 0.00 -> 0.29: +9/turn
  - flax farm 1 4.64 -> 4.32: +1/turn
  - spinnery 1 1.65 -> 1.55: -1/turn
  - sewing shop 1 0.30 -> 0.37: -5/turn
  - weavery 1 0.50 -> 0.61: +8/turn
  - ropewalk 1 0.25 -> 0.00: -9/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.26: +12/turn
  - brewery 1 0.14 -> 0.24: -14/turn
- Model check over the last 59 turns: predicted +74/turn for the settings we ran, real +63/turn.
- Worth of one more unit per turn: labour 1.60, thread 4.02, cloth 6.42, flax fibres 4.76, garments 18.57, nets 28.80, beer 2.76, timber 2.99, prestige 10000.00, cash 0.00
- Orders it would set: beer sell 16 (v2 15); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 5); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 30 (v2 35); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.26, worth +12/turn.
- Ship linen snake: Grandgues -> Boistot (+6/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Donaunieder (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +80/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.4/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 486 (+197 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 6.03 |
| ret | 3 | 0.91 | 1.21 |
| spin | 4 | 1.65 | 2.13 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 318/228, cloth 79/128

## Self-diagnosis

- R1: arms slot dry: 0.0 held, 0.5 a turn (gear slot (+0.4 prestige)); our buy 1 @ 26.4, home ask 29.4 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 1 @ 30 (ask 29.4, cap 48.0))
- R7 stale ask: flax plants ask 1.35 over the market for 3 turns: the town trades ~7 a turn at 1.3, we sold 0 with 15 over what we keep -> **sell price 1.35 -> 1.31 (last trade 1.3, floor 1.25)** (ok)
