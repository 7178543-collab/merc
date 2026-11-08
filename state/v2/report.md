# v2 shadow report

Turn 13880, 2026-11-08 17:44. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,777, prestige 3,543 (423 free, -2.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 8 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 9 | 9 | 9 | 0 | 0 | stop 36, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 518 | 0 | 11 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.50 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Tuning

- **tar**: home ask 11.50 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 518, not 618

## Prestige spending, cheapest coin per prestige first

521 turns left: prestige gained now converts 92.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 52.8 | 52.8 | running |
| hold banquet 4 (pies) | mansion | 18 | 55.2 | 55.2 | thin at home: pasties, ham, stockfish |
| jousting 3 | arena | 230 | 55.7 | 55.9 | needs a arena (build cost 26,028); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 56.6 | 56.6 |  |
| hold banquet 4 | mansion | 17.5 | 57.8 | 57.8 | thin at home: ham, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 57.8 | 57.8 | thin at home: ham, stockfish |
| hold banquet 1 (meat) | mansion | 4.2 | 60.5 | 60.5 |  |
| jousting 2 | arena | 210 | 61.0 | 61.3 | needs a arena (build cost 26,028); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (fish) | mansion | 7.6 | 61.5 | 61.5 |  |
| hold banquet 3 (pies) | mansion | 8 | 61.5 | 61.5 | thin at home: pasties |
| hold banquet 2 (fish) | mansion | 6.8 | 62.3 | 62.3 |  |
| hold sermon 2 (candles) | church | 31 | 58.5 | 63.6 | needs a church (build cost 66,991); thin at home: candles |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Gotthafen +375, Essenbrucke +313, Brebronn +291, Brunnham +279, Toqueque +238
- Gotthafen would trade: furniture buy 32 @ 13.4, pasties buy 1 @ 15.7; crew 0.4

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~109 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.90 (98/turn) | bread 155 (2.44->3.12), firewood 32 (2.52->6.46), timber 33 (8.4->10.26), cured fish 7 (25.2->29.64) | spinning wheels 1 (205.8->212.8), acid 1 (131.25->136.8), tools 9 (4.58->5.13), flax fibres 4 (5.83->6) | +315 |
| Hofkirchen | 991 | 0.34 | 1.00 (109/turn) | grain 107 (2.92->4.48), thread 50 (3.92->5.7), garments 9 (19.6->21.85), nets 5 (33.8->36.29) | acid 0 (133.35->136.8), cloth 21 (8.29->8.75), salt 8 (4.83->5.56), candles 0 (73.5->75.5) | +213 |
| Rouhomme | 368 | 0.11 | 0.90 (98/turn) | grain 118 (2.92->3.82), bread 155 (2.44->3.04), garments 10 (19.6->21.85), thread 19 (3.92->4.94) | tools 17 (4.51->5.13), flax fibres 2 (4.94->6), salt 5 (5.08->5.56), candles 1 (74.55->75.5) | +187 |
| Fontaux | 411 | 0.12 | 0.80 (88/turn) | thread 78 (3.92->5.65), garments 10 (19.6->22.99), firewood 21 (2.52->7.08), flax fibres 2 (5.8->6.22) | salt 9 (4.66->5.56), flax plants 5 (1.33->1.66) | +186 |
| Kirchwerp | 1072 | 0.39 | 0.50 (55/turn) | thread 78 (3.92->5.7), garments 10 (19.6->22.04), wine 10 (7.51->9.59), casks 5 (6.98->8.31) | cloth 24 (7.56->8.75), acid 1 (129.15->136.8), garments 2 (24.57->25.8), salt 9 (4.98->5.56) | +185 |

**Best:** Grandgues at about +315 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 28.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 16 @ min 3.26 | goal planner: sells 16 at 3.26 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 12.8, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 25.2) |
| grain | 9 @ 3.7, stop 36 |  | goal planner: buys 9 a turn for today's rates, keeps up to 36 (v2 had 18) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 18) |
| light armour | 1 @ 102, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 21.1k (cash + stock at home prices); -309/turn over 6 turns, -120/turn over 24 turns.
- Limits: cash flow >= -282/turn, prestige >= -0.51/turn (values are after 200 tax a turn).
- Today's settings: value +65/turn, cash +39/turn, prestige -2.13/turn - breaks the prestige floor.
- Plan: value +11/turn, cash +56/turn, prestige -0.51/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +74 vs +60, +2 vs +57, +59 vs +57.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Corstoft: +10/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +7/turn
  - ropewalk 1 0.25 -> 0.00: -2/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.10: +14/turn
  - weavery 1 0.50 -> 0.61: -7/turn
  - sewing shop 1 0.30 -> 0.36: +13/turn
  - brewery 1 0.14 -> 0.20: -9/turn
  - spinnery 1 1.65 -> 1.07: -10/turn
  - retting pit 1 0.91 -> 0.61: +10/turn
- Model check over the last 58 turns: predicted +104/turn for the settings we ran, real -37/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.58, thread 4.01, cloth 6.38, flax fibres 4.83, garments 18.44, nets 28.86, beer 2.90, timber 3.31, prestige 57.52, cash 0.00
- Orders it would set: beer sell 16 (v2 15); cloth sell 1 (v2 none); firewood buy 4 (v2 8); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 18); labour buy 29 (v2 18); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.10, worth +5/turn.
- Ship linen snake: Grandgues -> Corstoft (+12/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +79/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

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

Buffers: flax fibres 27/77, thread 754/228, cloth 72/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.0 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
