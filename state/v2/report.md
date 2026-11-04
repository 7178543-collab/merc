# v2 shadow report

Turn 13770, 2026-11-04 03:55. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 7,480, prestige 3,230 (110 free, +49.4/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 15 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.4 |
| grain | 33 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 30 | 30 | 530 | 5 | 0 | buy 30, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **labour**: buying 30, short of ~35 needed -> v2: buy 35

## Tuning

- **bread**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 535, not 635

## Prestige spending, cheapest coin per prestige first

631 turns left: prestige gained now converts 95.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.7 | 47.7 | running |
| hold banquet 4 (pies) | mansion | 18 | 51.0 | 51.0 | thin at home: hop beer, stockfish |
| jousting 3 | arena | 230 | 52.8 | 52.9 | needs a arena (build cost 25,710); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 53.5 | 53.5 |  |
| hold banquet 4 | mansion | 17.5 | 53.7 | 53.7 | thin at home: hop beer, ham, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 54.5 | 54.5 | thin at home: hop beer, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 54.7 | 54.7 | thin at home: hop beer, pies |
| hold banquet 2 (pies) | mansion | 7 | 55.2 | 55.2 | thin at home: pies |
| hold banquet 2 (fish) | mansion | 6.8 | 55.8 | 55.8 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 56.2 | 56.2 | thin at home: hop beer |
| jousting 2 | arena | 210 | 57.8 | 58.0 | needs a arena (build cost 25,710); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold sermon 2 (candles) | church | 31 | 54.4 | 58.4 | needs a church (build cost 66,776); thin at home: candles, furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.20 | 20 | 134102075 | 0.316 | - | furniture 19, pasties 1 | -264 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 19 @ 13.9, pasties buy 2 @ 14.0; crew 0.2; est +227 a turn; stock: furniture 19 @ 13.9 (keep 145); stock: pasties 2 @ 14.0 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 14.0 (keep 14); best orders clear only -0 a turn after crew: ship stays at 0
- best towns now: Hofkirchen +534, Angefont +477, Amsdermund +476, Bordetes +472, Etallaen +472
- Hofkirchen would trade: furniture buy 45 @ 13.2; crew 0.6

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~100 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.50 (50/turn) | charcoal 19 (2.16->4.6), timber 20 (6.98->8.88), bread 150 (2.23->2.49), firewood 1 (1.64->6.08) | bricks 2 (6.62->10.92), cloth 7 (7.77->8.25), candles 1 (84->85) | +104 |
| Fontaux | 411 | 0.11 | 1.00 (100/turn) | charcoal 17 (2.16->5.37), timber 15 (6.98->9.79), bread 140 (2.23->2.66), cookware 5 (25.83->27.74) | belts 1 (23.31->24.32), candles 1 (84.53->85) | +86 |
| Neuborn | 780 | 0.21 | 0.40 (40/turn) | charcoal 19 (2.16->6.08), tallow 1 (19.43->21.28) | cloth 24 (6.88->8.25), garments 2 (20.37->25.8) | +80 |
| Heilegg | 826 | 0.23 | 0.50 (50/turn) | charcoal 19 (2.16->4.94), cured fish 3 (22.68->26.98), wrought iron 5 (14.38->15.58), logs 1 (3.84->11.02) | cloth 24 (7.14->8.25), garments 2 (20.48->25.8), candles 1 (77.7->85), hop beer 1 (8.14->8.79) | +78 |
| Blanans | 297 | 0.08 | 0.60 (60/turn) | timber 25 (6.98->8.64), charcoal 19 (2.16->3.29), limestone 3 (19.43->23.75), firewood 1 (1.64->5.89) | cloth 24 (7.3->8.25), garments 2 (20.37->25.8), bricks 2 (6.51->10.92), candles 1 (82.42->85) | +69 |

**Best:** Grandgues at about +104 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 30.2, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 1 = 2.0 turns |
| beer |  | 16 @ min 2.72 | goal planner: sells 16 at 2.72 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| cloth |  | 1 @ min 7.1 | goal planner: sells 1 a turn at 7.1, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 19.4 | goal planner: sells 11 at 19.4 (v2 had 10 at 20.4) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 35) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 37.2) |
| pasties |  | 1 @ min 12.5 | goal planner: trial sale of an idle pile, 1 a turn at 12.5, keeps 0 (12 over) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 79.0) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 1 = 2.4 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 18.8k (cash + stock at home prices); -122/turn over 6 turns, +91/turn over 24 turns.
- Limits: cash flow >= -145/turn, prestige >= +7.91/turn (values are after 200 tax a turn).
- Today's settings: value +77/turn, cash +72/turn, prestige +49.45/turn.
- Plan: value +382/turn, cash +253/turn, prestige +41.45/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -278 vs +111, -280 vs +104, -116 vs +88 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Dortdorf: +10/turn
  - ship Flax Wyrm -> Donaunieder: +0/turn
  - park 1 16.00 -> 0.00: +46/turn
  - flax farm 1 4.64 -> 8.07: +18/turn
  - retting pit 1 0.91 -> 1.61: +33/turn
  - spinnery 1 1.65 -> 2.85: +87/turn
  - net maker [make nets 1] 0.00 -> 0.38: +32/turn
  - weavery 1 0.50 -> 0.72: +18/turn
  - sewing shop 1 0.30 -> 0.37: +34/turn
  - ropewalk 1 0.25 -> 0.00: -42/turn
- Model check over the last 59 turns: predicted +69/turn for the settings we ran, real +60/turn.
- Worth of one more unit per turn: labour 0.92, thread 2.33, cloth 3.71, flax fibres 2.77, garments 10.73, nets 17.41, beer 2.27, timber 3.40, prestige 0.00, cash 0.00
- Orders it would set: beer sell 16 (v2 15); cloth sell 1 (v2 none); firewood buy 4 (v2 5); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 29 (v2 35); light armour buy 1 (v2 None); pasties sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 1.00, worth +36/turn.
- Recipe: net maker make nets 3 -> make nets 1 at 0.38, worth +22/turn.
- Ship linen snake: Grandgues -> Dortdorf (+10/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Donaunieder (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +46/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new chandlery (make candles 1) for ~5071 coin: +42/turn, payback 120 turns, doesn't pay yet (materials thin at home: bricks, nails)
- Trim: donate park 1: +96/turn (tax 96 saved).

## Chain sizing

Mode HOLD, garments sold 10.4/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 489 (+201 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 6.11 |
| ret | 3 | 0.91 | 1.22 |
| spin | 4 | 1.65 | 2.16 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 300/228, cloth 80/128

## Self-diagnosis

- R5: arms buy not filling: bid 26.4 under the home ask 28.8 for 3 turns, bought 0.0 of 1, 1.0 held (2.0 turns)
