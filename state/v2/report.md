# v2 shadow report

Turn 13769, 2026-11-04 02:49. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 7,596, prestige 3,231 (111 free, +50.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 15 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.4 |
| grain | 33 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 30 | 29 | 529 | 11 | 0 | buy 30, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **labour**: buying 30, short of ~40 needed -> v2: buy 40

## Tuning

- **bread**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 540, not 640

## Prestige spending, cheapest coin per prestige first

632 turns left: prestige gained now converts 95.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.3 | 48.3 | running |
| hold banquet 4 (pies) | mansion | 18 | 50.1 | 50.1 | thin at home: hop beer, stockfish, candles |
| hold banquet 4 | mansion | 17.5 | 52.8 | 52.8 | thin at home: hop beer, ham, stockfish, candles |
| jousting 3 | arena | 230 | 52.7 | 52.9 | needs a arena (build cost 25,834); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 53.2 | 53.2 | thin at home: hop beer, pies, candles |
| hold banquet 1 (fish) | mansion | 4.2 | 53.6 | 53.6 |  |
| hold banquet 4 (premium) | mansion | 20 | 53.8 | 53.8 | thin at home: hop beer, stockfish, candles |
| hold banquet 3 (fish) | mansion | 7.6 | 54.6 | 54.6 | thin at home: hop beer |
| hold banquet 2 (pies) | mansion | 7 | 55.6 | 55.6 | thin at home: pies, candles |
| hold banquet 2 (fish) | mansion | 6.8 | 56.2 | 56.2 |  |
| hold prayer 2 | chapel | 13 | 53.2 | 57.5 | needs a chapel (build cost 31,660); thin at home: furniture |
| hold sermon 2 (candles) | church | 31 | 53.9 | 57.9 | needs a church (build cost 67,438); thin at home: candles, furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.2 / 0.20 | 20 | 134102075 | 0.376 | - | furniture 19, pasties 5 | -323 |
| linen snake | 0.1 / 0.01 | 1 | 151802239 | 0.072 | - | pasties 5 | -68 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 19 @ 13.8, pasties buy 1 @ 14.9; crew 0.2; est +223 a turn; stock: furniture 19 @ 13.8 (keep 145); stock: pasties 1 @ 14.9 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 14.0 (keep 14); best orders clear only -5 a turn after crew: ship stays at 0
- best towns now: Hofkirchen +547, Chatgnan +545, Amsdermund +488, Bordetes +468, Angefont +423
- Hofkirchen would trade: furniture buy 46 @ 13.2; crew 0.6

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~101 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Gottweiler | 1135 | 0.40 | 0.30 (30/turn) | tapestries 1 (745.5->802.75), salt 4 (5.78->8.88), butter 1 (64.58->66.02) | looms 1 (640.5->712.5), garments 20 (20.06->23.75), cloth 23 (7.56->8.35), gears 1 (56.7->65.08) | +218 |
| Arnsreuth | 921 | 0.28 | 0.20 (20/turn) | cured fish 4 (22.68->24.13), pickaxes 1 (9.66->10.92), cloth 1 (6.34->6.65) | looms 1 (551.25->712.5), garments 16 (22.68->23.75), cloth 24 (7.56->8.35), canvas 1 (29.4->32.11) | +194 |
| Rouhomme | 368 | 0.10 | 0.70 (71/turn) | charcoal 19 (1.81->3.52), bread 149 (2.23->2.6), beer 15 (3.12->3.48), cheese 15 (6.56->6.7) | looms 1 (630->712.5), garments 20 (21.63->23.75), flax fibres 13 (4.94->5.95), casks 2 (3.51->6.65) | +181 |
| Heilegg | 826 | 0.23 | 0.50 (50/turn) | charcoal 19 (1.81->4.8), wrought iron 13 (14.38->15.58), cured fish 4 (22.68->25.65), butter 1 (64.58->70.3) | garments 20 (20.48->23.75), looms 1 (661.5->712.5), cloth 24 (7.46->8.35), casks 2 (5.99->6.65) | +180 |
| Kirchwerp | 1072 | 0.36 | 0.60 (61/turn) | leather 1 (25.83->32.3), lead bars 2 (12.29->14.25), pickaxes 2 (9.66->10.83), charcoal 19 (1.81->4.75) | looms 1 (640.5->712.5), garments 20 (20.37->23.75), cloth 24 (7.04->8.35), slaked lime 5 (8.4->10.54) | +170 |

**Best:** Gottweiler at about +218 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 29.8, stop 1 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 3.0 turns |
| beer |  | 16 @ min 3.06 | goal planner: sells 16 at 3.06 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| cloth |  | 1 @ min 7.1 | goal planner: sells 1 a turn at 7.1, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 19.4 | goal planner: sells 11 at 19.4 (v2 had 10 at 20.0) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 30 @ 2.2, stop - |  | goal planner: buys 30 for today's rates (v2 had 40) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 37.2) |
| pasties |  | 2 @ min 12.5 | goal planner: trial sale of an idle pile, 2 a turn at 12.5, keeps 0 (13 over) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 at 69.5 (v2 had 1 at 79.0) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (ropewalk 1), makes 0.0, holds 1 = 3.1 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 20.4k (cash + stock at home prices); +146/turn over 6 turns, +165/turn over 24 turns.
- Limits: cash flow >= -150/turn, prestige >= +7.89/turn (values are after 200 tax a turn).
- Today's settings: value +92/turn, cash +88/turn, prestige +58.00/turn.
- Plan: value +398/turn, cash +272/turn, prestige +50.00/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +82 vs +112, -278 vs +111, -280 vs +104 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Donaunieder: +0/turn
  - ship Flax Wyrm -> no route: +0/turn
  - park 1 16.00 -> 0.00: +47/turn
  - flax farm 1 4.64 -> 8.07: +19/turn
  - retting pit 1 0.91 -> 1.61: +32/turn
  - spinnery 1 1.65 -> 2.85: +87/turn
  - net maker [make nets 1] 0.00 -> 0.38: +32/turn
  - weavery 1 0.50 -> 0.71: +19/turn
  - sewing shop 1 0.30 -> 0.37: +33/turn
  - ropewalk 1 0.25 -> 0.00: -44/turn
- Model check over the last 58 turns: predicted +68/turn for the settings we ran, real +88/turn.
- Worth of one more unit per turn: labour 0.93, thread 2.35, cloth 3.75, flax fibres 2.80, garments 10.83, nets 17.57, beer 2.15, timber 3.00, prestige 0.00, cash 0.00
- Orders it would set: beer sell 16 (v2 15); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 5); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 30 (v2 40); light armour buy 1 (v2 None); pasties sell 2 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 1.00, worth +37/turn.
- Recipe: net maker make nets 3 -> make nets 1 at 0.38, worth +21/turn.
- Ship linen snake: Grandgues -> Donaunieder (+0/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +47/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - new chandlery (make candles 1) for ~5020 coin: +31/turn, payback 164 turns, doesn't pay yet (materials thin at home: bricks, nails)
- Trim: donate park 1: +96/turn (tax 96 saved).

## Chain sizing

Mode HOLD, garments sold 10.4/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 491 (+202 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 6.15 |
| ret | 3 | 0.91 | 1.23 |
| spin | 4 | 1.65 | 2.17 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 292/228, cloth 80/128

## Self-diagnosis

Nothing found this run.
