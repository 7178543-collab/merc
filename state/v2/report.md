# v2 shadow report

Turn 13873, 2026-11-08 10:51. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,644, prestige 3,483 (363 free, -1.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 15, sell @ 3.26 |
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

**2 risks, 0 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **grain**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 102 over real use lately; planning 518, not 618

## Prestige spending, cheapest coin per prestige first

528 turns left: prestige gained now converts 92.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.6 | 51.6 | running |
| jousting 3 | arena | 230 | 54.1 | 54.3 | needs a arena (build cost 26,304); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 56.0 | 56.0 | thin at home: ham, stockfish, cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 58.1 | 58.1 | thin at home: cured fish |
| hold banquet 4 | mansion | 17.5 | 58.4 | 58.4 | thin at home: ham, stockfish, cheese |
| hold banquet 4 (premium) | mansion | 20 | 58.5 | 58.5 | thin at home: ham, stockfish, premium cheese |
| jousting 2 | arena | 210 | 59.2 | 59.5 | needs a arena (build cost 26,304); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (meat) | mansion | 4.2 | 61.8 | 61.8 |  |
| hold banquet 3 (fish) | mansion | 7.6 | 62.2 | 62.2 | thin at home: cured fish, cheese |
| hold banquet 2 (fish) | mansion | 6.8 | 62.6 | 62.6 | thin at home: cured fish, cheese |
| hold banquet 3 (pies) | mansion | 8 | 62.8 | 62.8 | thin at home: cheese |
| hold banquet 3 (meat) | mansion | 7.6 | 64.4 | 64.4 | thin at home: cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 5 @ 16.4 (keep 14); best orders clear only 2 a turn after crew: ship stays at 0
- best towns now: Bordetes +30, Donaunieder +24, Rotterburg +18
- Bordetes would trade: pasties buy 13 @ 15.8; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~107 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.70 (75/turn) | firewood 33 (2.69->5.42), charcoal 19 (2.14->4.31), bricks 7 (7.14->10.16), timber 24 (7.51->8.69) | candles 1 (75.6->82), cloth 9 (8.19->8.7), cheese 3 (7.56->8.31), garments 2 (26.46->26.8) | +147 |
| Kirchwerp | 1072 | 0.39 | 0.60 (64/turn) | thread 71 (4.72->5.7), wine 15 (6.72->9.79), tackles 1 (177.45->207.1), casks 13 (6.88->8.31) | candles 1 (79.28->82), nails 3 (5.51->6.7), garments 2 (25.83->26.8) | +143 |
| Arnsreuth | 921 | 0.30 | 0.20 (21/turn) | looms 1 (598.5->693.5), wine 15 (6.72->8.22), glass ingots 1 (52.29->60.32), yarn 2 (5.57->5.94) | candles 1 (77.7->82), salt 7 (4.7->5.56), cheese 3 (7.09->8.31), cloth 21 (8.35->8.7) | +129 |
| Pontmont | 341 | 0.10 | 0.70 (75/turn) | charcoal 19 (2.14->4.75), bread 150 (2.6->3.06), cured meat 4 (26.25->31.92), coats 1 (66.67->81.7) | candles 1 (77.7->82), cloth 12 (8.45->8.7), gold ore 1 (142.8->145.35), garments 2 (26.46->26.8) | +111 |
| Rouhomme | 368 | 0.10 | 0.40 (43/turn) | grain 103 (3.17->3.59), charcoal 19 (2.14->4.05), coats 1 (66.67->74.1), fleece 2 (9.4->11.02) | cloth 16 (7.25->8.7), dyed cloth 7 (10.13->12.16), tools 17 (4.51->5.13), garments 2 (24.36->26.8) | +106 |

**Best:** Grandgues at about +147 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 29.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 15 @ min 3.26 | goal planner: sells 15 at 3.26 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 16.1, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 25.8) |
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
- Value now 22.8k (cash + stock at home prices); +255/turn over 6 turns, -1/turn over 24 turns.
- Limits: cash flow >= -235/turn, prestige >= -0.26/turn (values are after 200 tax a turn).
- Today's settings: value +82/turn, cash +67/turn, prestige -1.82/turn - breaks the prestige floor.
- Plan: value +9/turn, cash +11/turn, prestige -0.26/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +235 vs +67, +157 vs +72, +461 vs +60.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Brunnham: +2/turn
  - ship Flax Wyrm -> Essenbrucke: +1/turn
  - net maker 0.00 -> 0.29: +7/turn
  - weavery 1 0.50 -> 0.43: -6/turn
  - spinnery 1 1.65 -> 1.32: -8/turn
  - retting pit 1 0.91 -> 0.75: +5/turn
  - flax farm 1 4.64 -> 3.76: -8/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.21: -13/turn
  - ropewalk 1 0.25 -> 0.00: +20/turn
  - mansion 1 0.00 -> 0.37: -77/turn
- Model check over the last 59 turns: predicted +103/turn for the settings we ran, real +17/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.17, cloth 6.67, flax fibres 4.94, garments 19.30, nets 29.97, beer 3.10, timber 3.58, prestige 60.62, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 4 (v2 8); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 18); labour buy 29 (v2 18); light armour buy 1 (v2 None); rope sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.21, worth +8/turn.
- Ship linen snake: Grandgues -> Brunnham (+2/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Essenbrucke (+1/turn over staying).
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

Buffers: flax fibres 27/77, thread 676/228, cloth 72/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 5.65 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
