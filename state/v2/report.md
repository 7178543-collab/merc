# v2 shadow report

Turn 13906, 2026-11-09 19:38. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,150, prestige 3,492 (372 free, -1.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 6 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 35 | 9 | 9 | 0 | 0 | stop 36, buy 11, buy @ 3.7 |
| labour | 29 | 29 | 518 | 0 | 11 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: home ask 2.62 is above our ceiling 2.40 and last turn bought 4 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Tuning

- **tar**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 518, not 618

## Prestige spending, cheapest coin per prestige first

495 turns left: prestige gained now converts 91.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.6 | 48.6 | running |
| hold banquet 4 (pies) | mansion | 18 | 55.1 | 55.1 | thin at home: hop beer, ham, stockfish, cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 57.1 | 57.1 |  |
| hold banquet 4 (premium) | mansion | 20 | 57.4 | 57.4 | thin at home: hop beer, ham, stockfish |
| hold banquet 4 | mansion | 17.5 | 57.6 | 57.6 | thin at home: hop beer, ham, stockfish, cheese |
| jousting 3 | arena | 230 | 59.6 | 59.9 | needs a arena (build cost 26,274); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 60.2 | 60.2 | thin at home: cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 61.1 | 61.1 | thin at home: hop beer, cheese |
| hold banquet 3 (pies) | mansion | 8 | 61.4 | 61.4 | thin at home: pasties, hop beer, cheese |
| hold banquet 2 (pies) | mansion | 7 | 62.6 | 62.6 | thin at home: pasties, cheese |
| hold feast 2 | townhouse | 2.6 | 58.6 | 65.0 | needs a townhouse (build cost 7,814) |
| jousting 2 | arena | 210 | 65.3 | 65.6 | needs a arena (build cost 26,274); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: furniture 1 @ 13.6 (keep 145); stock: pasties 2 @ 16.0 (keep 14); best orders clear only 8 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 16.0 (keep 14); best orders clear only 1 a turn after crew: ship stays at 0
- best towns now: Bedenis +31, Rotterburg +28, Essenbrucke +28, Clairlond +27, Clarfranche +27
- Bedenis would trade: pasties buy 9 @ 14.3; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~104 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Rouhomme | 368 | 0.10 | 0.80 (84/turn) | bread 155 (2.27->3.32), charcoal 18 (1.93->6.08), furniture 11 (12.5->15.2), malt 3 (4.47->6.46) | thread 45 (4.73->5.25), cookware 7 (24.36->26.41), cheese 4 (6.51->7.89), garments 2 (25.2->27.8) | +267 |
| Grandgues | 152 | 0.04 | 0.80 (84/turn) | firewood 38 (2.75->7.03), charcoal 18 (1.93->5.03), timber 22 (8.56->10.36), cured fish 6 (25.41->27.74) | coats 1 (93.45->98.8), hinges 1 (44.73->48.92), cheese 4 (7.25->7.89), candles 1 (81.9->82.5) | +248 |
| Kirchwerp | 1072 | 0.38 | 0.90 (94/turn) | thread 91 (4.66->5.7), furniture 11 (12.5->16.05), arms 6 (33.18->36.29), lead bars 3 (13.23->17.39) | coats 1 (75.6->98.8), cloth 24 (8.45->9.75), cheese 4 (5.1->7.89), garments 2 (24.36->27.8) | +189 |
| Clairas | 374 | 0.10 | 0.30 (31/turn) | medicine 2 (144.9->155.8), charcoal 18 (1.93->3.74), lead bars 6 (13.23->15.01), malt 3 (4.47->6.51) | plate armour 1 (1270.5->1330), coats 1 (87.15->98.8), salt 17 (4.98->5.56), dyed cloth 5 (10.5->12.06) | +171 |
| Fontaux | 411 | 0.12 | 1.00 (104/turn) | thread 44 (4.66->5.65), charcoal 8 (1.93->5.65), timber 11 (8.56->12.44), firewood 11 (2.75->6.84) | salt 8 (5.12->5.56), hinges 0 (47.25->48.92), belts 1 (35.07->35.34), candles 0 (81.9->82.5) | +118 |

**Best:** Rouhomme at about +267 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 16 @ min 3.26 | goal planner: sells 16 at 3.26 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 12.2, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 26.8) |
| grain | 10 @ 3.7, stop 36 |  | uses 9.0/turn (brewery 1), makes 0.0, holds 35 = 3.9 turns |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 18) |
| light armour | 1 @ 100, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 38.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 26.2k (cash + stock at home prices); +161/turn over 6 turns, +188/turn over 24 turns.
- Limits: cash flow >= -298/turn, prestige >= -0.30/turn (values are after 200 tax a turn).
- Today's settings: value +109/turn, cash +106/turn, prestige -1.87/turn - breaks the prestige floor.
- Plan: value +27/turn, cash +30/turn, prestige -0.30/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +144 vs +88, +177 vs +92, +133 vs +95.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Corstoft: +3/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +8/turn
  - spinnery 1 1.65 -> 1.55: -0/turn
  - flax farm 1 4.64 -> 4.42: -1/turn
  - brewery 1 0.14 -> 0.00: -9/turn
  - brewery 1 [brew beer 2] 0.00 -> 0.16: +18/turn
  - weavery 1 0.50 -> 0.60: -10/turn
  - sewing shop 1 0.30 -> 0.36: +12/turn
  - ropewalk 1 0.25 -> 0.00: -11/turn
- Model check over the last 59 turns: predicted +103/turn for the settings we ran, real +63/turn.
- Worth of one more unit per turn: labour 1.62, thread 4.07, cloth 6.50, flax fibres 4.83, garments 18.81, nets 29.30, beer 3.26, timber 3.38, prestige 66.57, cash 0.00
- Orders it would set: beer sell 16 (v2 15); cloth sell 1 (v2 none); firewood buy 4 (v2 8); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); labour buy 29 (v2 18); light armour buy 1 (v2 None)
- Recipe: brewery 1 brew beer 1 -> brew beer 2 at 0.16, worth +19/turn.
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.27, worth +11/turn.
- Ship linen snake: Grandgues -> Corstoft (+7/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +81/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1971 coin: +3/turn, payback 660 turns, doesn't pay yet (materials thin at home: limestone)

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

Buffers: flax fibres 27/77, thread 908/228, cloth 73/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.1 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
