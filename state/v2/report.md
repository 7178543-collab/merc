# v2 shadow report

Turn 13773, 2026-11-04 06:47. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 7,218, prestige 3,228 (108 free, -0.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 14 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.4 |
| grain | 33 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 30 | 29 | 529 | 6 | 0 | buy 30, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **labour**: buying 30, short of ~35 needed -> v2: buy 35

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 535, not 635

## Prestige spending, cheapest coin per prestige first

628 turns left: prestige gained now converts 95.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.4 | 47.4 | running |
| hold banquet 4 (pies) | mansion | 18 | 50.5 | 50.5 | thin at home: stockfish |
| jousting 3 | arena | 230 | 52.9 | 53.1 | needs a arena (build cost 26,676); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 53.2 | 53.2 | thin at home: ham, stockfish |
| hold banquet 1 (fish) | mansion | 4.2 | 53.4 | 53.4 |  |
| hold banquet 2 (pies) | mansion | 7 | 53.8 | 53.8 | thin at home: pies |
| hold banquet 4 (premium) | mansion | 20 | 54.1 | 54.1 | thin at home: stockfish |
| hold banquet 2 (fish) | mansion | 6.8 | 54.4 | 54.4 |  |
| hold banquet 3 (pies) | mansion | 8 | 54.9 | 54.9 | thin at home: pies |
| hold banquet 3 (fish) | mansion | 7.6 | 56.6 | 56.6 |  |
| jousting 2 | arena | 210 | 57.9 | 58.1 | needs a arena (build cost 26,676); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 58.6 | 58.6 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.20 | 19 | 134102075 | 0.332 | - | furniture 19, pasties 1 | -264 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 20 @ 14.6, pasties buy 1 @ 13.7; crew 0.2; est +221 a turn; stock: furniture 20 @ 14.6 (keep 145); stock: pasties 1 @ 13.7 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 14.0 (keep 14); best orders clear only -5 a turn after crew: ship stays at 0
- best towns now: Hofkirchen +508, Angefont +465, Amsdermund +464, Etallaen +452, Bordetes +448
- Hofkirchen would trade: furniture buy 43 @ 13.2; crew 0.6

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~100 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.50 (50/turn) | charcoal 19 (2.29->6.22), bread 152 (2.21->2.56), timber 21 (7.82->8.88), cured fish 6 (22.68->23.37) | medicine 1 (158.55->171), bricks 5 (6.51->8.98), casks 1 (5.78->6.65), copper ingots 3 (15.75->16.05) | +148 |
| Fontaux | 411 | 0.11 | 1.00 (100/turn) | charcoal 17 (2.29->5.84), wine 14 (6.3->7.74), bread 142 (2.21->2.66), cookware 5 (25.41->28.69) | bronze ingots 1 (19.01->22.23), casks 1 (6.2->6.65), leather 1 (26.04->26.6) | +119 |
| Vauxvais | 204 | 0.05 | 0.20 (20/turn) | charcoal 19 (2.29->2.89), herbs 1 (31.08->32.87), logs 1 (3.82->6.7), cloth 1 (6.27->7.03) | bricks 13 (4.85->8.98), garments 2 (20.58->28.4), acid 1 (123.9->137.75), flax fibres 9 (4.94->5.8) | +99 |
| Hofkirchen | 991 | 0.31 | 0.20 (20/turn) | beer 15 (2.74->4.35), glass ingots 2 (64.05->68.4), herbs 1 (31.08->38), grain 2 (2.48->3.42) | hop beer 9 (7.51->10.45), garments 2 (19.95->28.4), cloth 17 (7.14->8.35), acid 1 (133.35->137.75) | +98 |
| Blanans | 297 | 0.08 | 0.60 (60/turn) | bread 152 (2.21->2.53), charcoal 19 (2.29->3.31), honey 3 (8.61->10.26), herbs 1 (31.08->34.96) | cloth 24 (7.3->8.35), garments 2 (20.37->28.4), tackles 2 (180.6->188.1), bricks 4 (6.41->8.98) | +93 |

**Best:** Grandgues at about +148 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 16 @ min 3.06 | goal planner: sells 16 at 3.06 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| cloth |  | 1 @ min 7.1 | goal planner: sells 1 a turn at 7.1, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 19.4 | goal planner: sells 11 at 19.4 (v2 had 10 at 25.8) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 30 @ 2.2, stop - |  | goal planner: buys 30 for today's rates (v2 had 35) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 37.2) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 78.0) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 0 = 0.8 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 19.5k (cash + stock at home prices); -111/turn over 6 turns, +100/turn over 24 turns.
- Limits: cash flow >= -134/turn, prestige >= +7.99/turn (values are after 200 tax a turn).
- Today's settings: value +107/turn, cash +99/turn, prestige -0.95/turn - breaks the prestige floor.
- Plan: value -115/turn, cash -106/turn, prestige +3.25/turn - could not meet the prestige floor.
- Cash check (real vs predicted cash a tick, last 3): -280 vs +104, -116 vs +88, +13 vs +96 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Amsdermund: +15/turn
  - ship Flax Wyrm -> Donaunieder: +1/turn
  - net maker 0.00 -> 0.29: +9/turn
  - flax farm 1 4.64 -> 4.22: +0/turn
  - spinnery 1 1.65 -> 1.52: -2/turn
  - sewing shop 1 0.30 -> 0.37: -6/turn
  - weavery 1 0.50 -> 0.61: +9/turn
  - ropewalk 1 0.25 -> 0.00: -6/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.23: +12/turn
  - brewery 1 0.14 -> 0.24: -16/turn
- Model check over the last 58 turns: predicted +78/turn for the settings we ran, real +76/turn.
- Worth of one more unit per turn: labour 1.58, thread 3.97, cloth 6.34, flax fibres 4.70, garments 18.34, nets 28.47, beer 2.87, timber 3.35, prestige 10000.00, cash 0.00
- Orders it would set: beer sell 16 (v2 15); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 5); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 30 (v2 35); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.23, worth +12/turn.
- Ship linen snake: Grandgues -> Amsdermund (+15/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Donaunieder (+1/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +79/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.3/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 484 (+195 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 5.98 |
| ret | 3 | 0.91 | 1.20 |
| spin | 4 | 1.65 | 2.11 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 328/228, cloth 79/128

## Self-diagnosis

- R1: arms slot dry: 0.0 held, 0.5 a turn (gear slot (+0.4 prestige)); our buy 1 @ 26.4, home ask 29.6 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 1 @ 30.2 (ask 29.6, cap 48.0))
