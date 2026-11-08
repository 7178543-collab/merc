# v2 shadow report

Turn 13878, 2026-11-08 15:33. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,715, prestige 3,548 (428 free, -2.1/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 7 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 9 | 9 | 9 | 0 | 0 | stop 36, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 518 | 0 | 11 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.30 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Tuning

- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.30 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 518, not 618

## Prestige spending, cheapest coin per prestige first

523 turns left: prestige gained now converts 92.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 52.8 | 52.8 | running |
| hold banquet 4 (pies) | mansion | 18 | 55.5 | 55.5 | thin at home: wine, ham, stockfish |
| jousting 3 | arena | 230 | 55.7 | 55.9 | needs a arena (build cost 26,566); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 56.0 | 56.0 |  |
| hold banquet 4 (premium) | mansion | 20 | 58.2 | 58.2 | thin at home: wine, ham, stockfish |
| hold banquet 4 | mansion | 17.5 | 58.3 | 58.3 | thin at home: wine, ham, stockfish |
| hold banquet 1 (meat) | mansion | 4.2 | 60.2 | 60.2 |  |
| jousting 2 | arena | 210 | 61.0 | 61.3 | needs a arena (build cost 26,566); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 61.8 | 61.8 | thin at home: pasties |
| hold sermon 2 (candles) | church | 31 | 57.2 | 62.2 | needs a church (build cost 67,370) |
| hold banquet 2 (fish) | mansion | 6.8 | 62.4 | 62.4 | thin at home: wine |
| hold banquet 3 (fish) | mansion | 7.6 | 62.8 | 62.8 |  |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 16.4 (keep 14); best orders clear only -1 a turn after crew: ship stays at 0
- best towns now: Angefont +452, Chatgnan +436, Gotthafen +347, Essenbrucke +324, Brebronn +274
- Angefont would trade: furniture buy 42 @ 14.6; crew 0.4

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~109 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Fontaux | 411 | 0.12 | 0.90 (98/turn) | thread 76 (4.32->5.65), garments 10 (19.46->28.5), firewood 21 (2.18->6.93), glass ingots 2 (57.75->58.9) | salt 10 (4.51->5.56), axes 1 (18.17->20.71), flax plants 2 (1.21->1.61) | +211 |
| Pontmont | 341 | 0.10 | 0.60 (65/turn) | garments 10 (19.46->25.84), bread 151 (2.48->3.13), cured meat 6 (24.78->28.12), rope 2 (84->91.2) | malt 3 (7.35->8.93), salt 10 (5.19->5.56), wine 22 (6.83->6.93) | +201 |
| Rouhomme | 368 | 0.11 | 0.80 (87/turn) | grain 115 (2.92->3.76), bread 151 (2.48->3), garments 10 (19.46->21.85), thread 18 (4.32->5.42) | wine 22 (6.41->6.93), tools 17 (4.51->5.03), salt 3 (5.12->5.56), cloth 13 (8.56->8.7) | +175 |
| Grandgues | 152 | 0.04 | 0.90 (98/turn) | firewood 31 (2.18->6.46), garments 10 (19.46->21.47), beer 15 (3.26->3.91), thread 20 (4.32->4.69) | wine 22 (6.77->6.93), flour 2 (20.06->21.28), salt 3 (4.96->5.56), malt 1 (7.82->8.93) | +157 |
| Darmwald | 1022 | 0.36 | 0.60 (65/turn) | garments 10 (19.46->24.89), thread 76 (4.32->4.89), beer 15 (3.26->4.75), glass ingots 2 (57.75->63.65) | cloth 24 (7.56->8.7), axes 1 (19.43->20.71) | +126 |

**Best:** Fontaux at about +211 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 16 @ min 3.26 | goal planner: sells 16 at 3.26 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 12.6, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 24.4) |
| grain | 9 @ 3.7, stop 36 |  | goal planner: buys 9 a turn for today's rates, keeps up to 36 (v2 had 18) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 18) |
| light armour | 1 @ 102, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 20.7k (cash + stock at home prices); -358/turn over 6 turns, -121/turn over 24 turns.
- Limits: cash flow >= -280/turn, prestige >= -0.53/turn (values are after 200 tax a turn).
- Today's settings: value +78/turn, cash +57/turn, prestige -2.15/turn - breaks the prestige floor.
- Plan: value +19/turn, cash +93/turn, prestige -0.53/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +115 vs +67, +279 vs +53, +74 vs +60.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Caillechâtel: +0/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +7/turn
  - ropewalk 1 0.25 -> 0.00: +2/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.14: +14/turn
  - brewery 1 0.14 -> 0.20: -8/turn
  - sewing shop 1 0.30 -> 0.36: -9/turn
  - weavery 1 0.50 -> 0.60: +9/turn
  - spinnery 1 1.65 -> 1.06: -11/turn
  - retting pit 1 0.91 -> 0.60: +10/turn
- Model check over the last 59 turns: predicted +103/turn for the settings we ran, real -38/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.58, thread 3.98, cloth 6.35, flax fibres 4.72, garments 18.38, nets 28.62, beer 2.88, timber 3.33, prestige 57.19, cash 0.00
- Orders it would set: beer sell 16 (v2 15); cloth sell 1 (v2 none); firewood buy 4 (v2 8); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 18); labour buy 29 (v2 18); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.14, worth +7/turn.
- Ship linen snake: Grandgues -> Caillechâtel (+1/turn over staying).
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

Buffers: flax fibres 27/77, thread 732/228, cloth 72/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.0 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
