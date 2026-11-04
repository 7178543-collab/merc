# v2 shadow report

Turn 13774, 2026-11-04 07:57. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 7,097, prestige 3,227 (107 free, -0.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 14 | 3 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.4 |
| grain | 33 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 30 | 30 | 530 | 5 | 0 | buy 30, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **labour**: buying 30, short of ~123 needed -> v2: buy 123

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Prestige spending, cheapest coin per prestige first

627 turns left: prestige gained now converts 95.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 47.4 | 47.4 | running |
| hold banquet 4 (pies) | mansion | 18 | 50.3 | 50.3 | thin at home: hop beer, stockfish |
| hold banquet 4 | mansion | 17.5 | 53.0 | 53.0 | thin at home: hop beer, ham, stockfish |
| hold banquet 2 (pies) | mansion | 7 | 53.3 | 53.3 | thin at home: pies |
| jousting 3 | arena | 230 | 53.1 | 53.3 | needs a arena (build cost 25,681); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 53.4 | 53.4 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 53.9 | 53.9 |  |
| hold banquet 4 (premium) | mansion | 20 | 53.9 | 53.9 | thin at home: hop beer, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 54.9 | 54.9 | thin at home: hop beer, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 56.6 | 56.6 | thin at home: hop beer |
| jousting 2 | arena | 210 | 58.1 | 58.4 | needs a arena (build cost 25,681); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 2 (meat) | mansion | 6.8 | 59.1 | 59.1 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.20 | 19 | 134102075 | 0.284 | - | furniture 20, pasties 1 | -277 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 20 @ 14.3, pasties buy 1 @ 13.7; crew 0.2; est +226 a turn; stock: furniture 20 @ 14.3 (keep 145); stock: pasties 1 @ 13.7 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 14.0 (keep 14); best orders clear only -6 a turn after crew: ship stays at 0
- best towns now: Hofkirchen +484, Etallaen +474, Angefont +464, Amsdermund +446, Bordetes +433
- Hofkirchen would trade: furniture buy 41 @ 13.2, pasties buy 1 @ 12.6; crew 0.6

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~106 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Dortgart | 1045 | 0.37 | 0.20 (21/turn) | wrought iron 5 (14.49->21.66), cured fish 5 (22.68->25.46), garments 10 (18.44->19.19), tools 16 (5.06->5.56) | tapestries 1 (593.25->646), cloth 12 (7.46->11.78), garments 2 (21.42->24.4), candles 1 (79.28->82) | +158 |
| Großaue | 1136 | 0.42 | 0.10 (11/turn) | garments 10 (18.44->26.22), wine 14 (6.09->6.84) | cloth 11 (8.09->11.78), tackles 1 (163.8->187.15), gears 1 (49.98->52.72), hinges 1 (33.81->36.86) | +141 |
| Neuborn | 780 | 0.22 | 0.10 (11/turn) | acid 1 (130.2->133), flax fibres 2 (4.84->5.65) | cloth 14 (6.88->11.78), silver bars 1 (245.7->307.8), garments 2 (20.37->24.4), leather 1 (24.36->26.98) | +139 |
| Caillechâtel | 488 | 0.14 | 0.20 (21/turn) | cured fish 3 (22.68->24.51), garments 10 (18.44->19), yarn 3 (4.05->4.35) | spinning wheels 1 (158.55->216.6), cloth 13 (7.88->11.78), garments 2 (21.21->24.4), bricks 4 (5.62->8.98) | +121 |
| Großmühle | 751 | 0.21 | 0.10 (11/turn) | garments 10 (18.44->21.66), cured fish 5 (22.68->24.32), flax fibres 2 (4.84->5.46) | cloth 14 (7.67->11.78), thread 22 (3.44->4.78), leather 1 (26.04->26.98), candles 1 (81.38->82) | +117 |

**Best:** Dortgart at about +158 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| beer |  | 16 @ min 3.06 | goal planner: sells 16 at 3.06 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| cloth |  | 1 @ min 7.1 | goal planner: sells 1 a turn at 7.1, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 19.4 | goal planner: sells 11 at 19.4 (v2 had 10 at 23.8) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 123) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 37.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 79.0) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 0 = 0.2 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 19.9k (cash + stock at home prices); -79/turn over 6 turns, +111/turn over 24 turns.
- Limits: cash flow >= -129/turn, prestige >= +8.03/turn (values are after 200 tax a turn).
- Today's settings: value +101/turn, cash +95/turn, prestige -0.94/turn - breaks the prestige floor.
- Plan: value -127/turn, cash -118/turn, prestige +3.26/turn - could not meet the prestige floor.
- Cash check (real vs predicted cash a tick, last 3): -116 vs +88, +13 vs +96, -121 vs +99 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Toqueque: +5/turn
  - ship Flax Wyrm -> Brunnham: +0/turn
  - net maker 0.00 -> 0.29: +9/turn
  - flax farm 1 4.64 -> 4.30: +0/turn
  - retting pit 1 0.91 -> 0.86: +0/turn
  - spinnery 1 1.65 -> 1.51: +1/turn
  - weavery 1 0.50 -> 0.61: -4/turn
  - sewing shop 1 0.30 -> 0.37: +7/turn
  - brewery 1 0.14 -> 0.24: -16/turn
  - mansion 1 0.00 -> 1.00: -230/turn
- Model check over the last 59 turns: predicted +79/turn for the settings we ran, real +82/turn.
- Worth of one more unit per turn: labour 1.58, thread 4.01, cloth 6.38, flax fibres 4.83, garments 18.43, nets 28.65, beer 2.87, timber 3.40, prestige 10000.00, cash 0.00
- Orders it would set: beer sell 16 (v2 15); cloth sell 1 (v2 none); firewood buy 4 (v2 5); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 29 (v2 123); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Toqueque (+7/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Brunnham (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +79/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.3/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 482 (+193 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 5.94 |
| ret | 3 | 0.91 | 1.19 |
| spin | 4 | 1.65 | 2.10 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 336/228, cloth 79/128

## Self-diagnosis

- R1: arms slot dry: 0.0 held, 0.5 a turn (gear slot (+0.4 prestige)); our buy 1 @ 26.4, home ask 29.8 (held back: quiet hours (23:00-07:00 Toronto): reduce-only, would buy 1 @ 30.4 (ask 29.8, cap 48.0))
