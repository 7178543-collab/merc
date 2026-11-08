# v2 shadow report

Turn 13871, 2026-11-08 08:40. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,026, prestige 3,486 (366 free, -1.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 15, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 7 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 9 | 9 | 9 | 0 | 0 | stop 36, buy 9, buy @ 3.7 |
| labour | 29 | 30 | 518 | 0 | 12 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Tuning

- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 102 over real use lately; planning 518, not 618

## Prestige spending, cheapest coin per prestige first

530 turns left: prestige gained now converts 93.0% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.3 | 51.3 | running |
| jousting 3 | arena | 230 | 54.5 | 54.7 | needs a arena (build cost 24,828); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 55.6 | 55.6 |  |
| hold banquet 4 (pies) | mansion | 18 | 56.1 | 56.1 | thin at home: pasties, hop beer, wine, ham, stockfish |
| hold banquet 4 | mansion | 17.5 | 58.2 | 58.2 | thin at home: wine, hop beer, ham, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 58.2 | 58.2 | thin at home: hop beer, wine, ham, stockfish |
| jousting 2 | arena | 210 | 59.7 | 59.9 | needs a arena (build cost 24,828); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 60.2 | 60.2 | thin at home: wine |
| hold banquet 3 (fish) | mansion | 7.6 | 60.3 | 60.3 | thin at home: hop beer |
| hold banquet 1 (meat) | mansion | 4.2 | 60.9 | 60.9 | thin at home: cured meat |
| hold banquet 3 (meat) | mansion | 7.6 | 63.7 | 63.7 | thin at home: hop beer, cured meat |
| hold banquet 2 (meat) | mansion | 6.8 | 64.0 | 64.0 | thin at home: wine, cured meat |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 5 @ 16.4 (keep 14); best orders clear only 2 a turn after crew: ship stays at 0
- best towns now: Bordetes +31, Donaunieder +22, Rotterburg +16
- Bordetes would trade: pasties buy 14 @ 15.9; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~107 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 1.00 (107/turn) | firewood 34 (2.14->4.73), charcoal 19 (2.18->4.27), timber 23 (7.56->9.59), bellows 1 (206.85->222.3) | candles 1 (76.65->80.5), garments 22 (25.62->25.84), wool 2 (12.81->14.72), cloth 9 (7.98->8.4) | +179 |
| Rouhomme | 368 | 0.10 | 0.50 (54/turn) | bellows 1 (206.85->245.1), hinges 1 (37.17->61.27), charcoal 19 (2.18->3.69), grain 101 (2.81->3.08) | garments 22 (24.36->25.84), cloth 15 (7.25->8.4), tools 16 (4.51->5.08), dyed cloth 4 (11.55->13.21) | +148 |
| Pontmont | 341 | 0.10 | 0.80 (86/turn) | grain 101 (2.81->3.38), charcoal 19 (2.18->4.75), bellows 1 (206.85->231.8), bread 151 (2.71->3.06) | candles 1 (77.7->80.5), chisels 1 (7.19->8.03) | +128 |
| Bremcop | 1326 | 0.53 | 0.30 (32/turn) | bellows 1 (206.85->228), nets 6 (33.6->37.62), beer 15 (3.26->4.69), flour 1 (17.22->23.75) | garments 22 (22.68->25.84), candles 1 (73.5->80.5), wool 2 (12.18->14.72), nails 2 (5.72->6.6) | +114 |
| Fontaux | 411 | 0.12 | 1.00 (107/turn) | charcoal 13 (2.18->5.56), firewood 16 (2.14->7.36), bellows 0 (206.85->239.4), timber 17 (7.56->9.69) | garments 16 (24.99->25.84), candles 0 (77.17->80.5), wool 0 (11.87->14.72), flax plants 2 (1.25->1.51) | +114 |

**Best:** Grandgues at about +179 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 28.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 15 @ min 3.26 | goal planner: sells 15 at 3.26 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 15, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 26.4) |
| grain | 9 @ 3.7, stop 36 |  | goal planner: buys 9 a turn for today's rates, keeps up to 36 (v2 had 18) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 18) |
| light armour | 1 @ 95.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 22.4k (cash + stock at home prices); +199/turn over 6 turns, -2/turn over 24 turns.
- Limits: cash flow >= -209/turn, prestige >= -0.28/turn (values are after 200 tax a turn).
- Today's settings: value +89/turn, cash +72/turn, prestige -1.84/turn - breaks the prestige floor.
- Plan: value +16/turn, cash +17/turn, prestige -0.28/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +53 vs +64, +52 vs +61, +235 vs +67.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Etallaen: +4/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +7/turn
  - weavery 1 0.50 -> 0.43: -6/turn
  - spinnery 1 1.65 -> 1.34: -7/turn
  - retting pit 1 0.91 -> 0.76: +5/turn
  - flax farm 1 4.64 -> 3.82: -5/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.23: -15/turn
  - ropewalk 1 0.25 -> 0.00: +21/turn
  - mansion 1 0.00 -> 0.37: -79/turn
- Model check over the last 59 turns: predicted +103/turn for the settings we ran, real +14/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.17, cloth 6.67, flax fibres 4.94, garments 19.30, nets 29.96, beer 2.90, timber 3.24, prestige 61.37, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 4 (v2 8); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 18); labour buy 29 (v2 18); light armour buy 1 (v2 None); rope sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.23, worth +9/turn.
- Ship linen snake: Grandgues -> Etallaen (+4/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

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

Buffers: flax fibres 27/77, thread 653/228, cloth 72/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 5.75 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
