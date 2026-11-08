# v2 shadow report

Turn 13876, 2026-11-08 13:02. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,363, prestige 3,552 (432 free, +72.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 7 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 9 | 9 | 9 | 0 | 0 | stop 36, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 518 | 0 | 11 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: home ask 2.66 is above our ceiling 2.40 and last turn bought 4 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.30 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Tuning

- **tar**: home ask 11.30 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 518, not 618

## Prestige spending, cheapest coin per prestige first

525 turns left: prestige gained now converts 92.8% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 52.2 | 52.2 | running |
| jousting 3 | arena | 230 | 55.2 | 55.4 | needs a arena (build cost 25,842); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 55.9 | 55.9 |  |
| hold banquet 4 (pies) | mansion | 18 | 56.4 | 56.4 | thin at home: wine, ham, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 59.1 | 59.1 | thin at home: wine, ham, stockfish |
| hold banquet 4 | mansion | 17.5 | 59.3 | 59.3 | thin at home: wine, ham, stockfish |
| jousting 2 | arena | 210 | 60.4 | 60.7 | needs a arena (build cost 25,842); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (meat) | mansion | 4.2 | 61.1 | 61.1 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 61.3 | 61.3 | thin at home: wine |
| hold banquet 3 (pies) | mansion | 8 | 62.3 | 62.3 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 62.4 | 62.4 |  |
| hold banquet 2 (pies) | mansion | 7 | 63.4 | 63.4 | thin at home: wine |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 16.4 (keep 14); best orders clear only -1 a turn after crew: ship stays at 0
- best towns now: Chatgnan +448, Donaunieder +352, Essenbrucke +327, Clairlond +275, Fulkirch +244
- Chatgnan would trade: furniture buy 39 @ 13.8; crew 0.4

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~108 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.90 (97/turn) | firewood 32 (2.79->6.03), arms 7 (28.14->34.2), bread 150 (2.54->2.85), charcoal 19 (2.58->3.91) | dyed cloth 8 (10.08->12.16), candles 1 (76.65->82.5), cheese 3 (7.77->8.36), salt 6 (5.25->5.56) | +203 |
| Rouhomme | 368 | 0.11 | 1.00 (108/turn) | grain 84 (3.07->3.61), charcoal 14 (2.58->4.58), bread 115 (2.54->2.94), leather 0 (23.73->30.4) | cloth 12 (7.61->8.4), dyed cloth 5 (10.5->12.16), thread 37 (4.94->5.25), ploughs 0 (67.2->76) | +119 |
| Fontaux | 411 | 0.12 | 1.00 (108/turn) | thread 52 (4.5->5.65), garments 7 (26.8->29.26), firewood 15 (2.79->7.22), arms 3 (28.14->30.4) | candles 0 (76.65->82.5), cheese 2 (6.56->8.36), flax fibres 9 (5.51->5.95), salt 7 (5.1->5.56) | +107 |
| Hofkirchen | 991 | 0.34 | 0.40 (43/turn) | thread 56 (4.5->5.7), lead bars 8 (18.38->20.71), arms 7 (28.14->30.78), nets 6 (33.8->36.29) | cheese 3 (5.78->8.36), candles 1 (77.7->82.5), garments 2 (24.99->27), nails 2 (5.83->6.84) | +97 |
| Neuborn | 780 | 0.22 | 1.00 (108/turn) | timber 20 (7.46->12.54), charcoal 13 (2.58->5.84), beer 10 (3.3->4.94), hinges 0 (47.67->59.85) | garments 1 (24.57->27), candles 0 (80.33->82.5), nails 0 (6.25->6.84), salt 2 (5.3->5.56) | +89 |

**Best:** Grandgues at about +203 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 28.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 16 @ min 3.26 | goal planner: sells 16 at 3.26 (v2 had 15 at 3.38) |
| bread | 5 @ 2.5, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had None) |
| candles | 2 @ 78.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 16.9, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 25.2) |
| grain | 9 @ 3.7, stop 36 |  | goal planner: buys 9 a turn for today's rates, keeps up to 36 (v2 had 18) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 18) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 20.9k (cash + stock at home prices); -85/turn over 6 turns, -92/turn over 24 turns.
- Limits: cash flow >= -265/turn, prestige >= -0.55/turn (values are after 200 tax a turn).
- Today's settings: value +68/turn, cash +53/turn, prestige +72.83/turn.
- Plan: value +375/turn, cash +209/turn, prestige +64.83/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +157 vs +72, +461 vs +60, +115 vs +67.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Gosschweig: +7/turn
  - ship Flax Wyrm -> Clairlond: +2/turn
  - park 1 16.00 -> 0.00: +50/turn
  - flax farm 1 4.64 -> 6.79: +24/turn
  - net maker [make nets 1] 0.00 -> 0.38: +18/turn
  - retting pit 1 0.91 -> 1.33: +10/turn
  - spinnery 1 1.65 -> 2.34: +54/turn
  - weavery 1 0.50 -> 1.17: +45/turn
  - sewing shop 1 0.30 -> 0.71: +91/turn
  - ropewalk 1 0.25 -> 0.00: -13/turn
- Model check over the last 59 turns: predicted +103/turn for the settings we ran, real -26/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 0.99, thread 2.54, cloth 4.03, flax fibres 3.10, garments 11.61, nets 18.91, beer 2.40, timber 3.22, prestige 0.00, cash 0.00
- Orders it would set: beer sell 16 (v2 15); bread buy 5 (v2 None); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 8); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 18); labour buy 29 (v2 18)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.14, worth +18/turn.
- Recipe: net maker make nets 3 -> make nets 1 at 0.38, worth +19/turn.
- Ship linen snake: Grandgues -> Gosschweig (+7/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Clairlond (+2/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +50/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
- Trim: donate park 1: +96/turn (tax 96 saved).

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 430 (+141 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.75 |
| ret | 3 | 0.91 | 0.95 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 709/228, cloth 72/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.0 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
