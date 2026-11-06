# v2 shadow report

Turn 13819, 2026-11-06 04:53. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,192, prestige 3,287 (167 free, -0.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 14 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 33 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 518 | 0 | 11 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.30 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.30 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 518, not 618

## Prestige spending, cheapest coin per prestige first

582 turns left: prestige gained now converts 94.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.1 | 50.1 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 54.1 | 54.1 |  |
| hold banquet 4 (pies) | mansion | 18 | 54.6 | 54.6 | thin at home: wine, ham, stockfish, cheese, pies, candles |
| jousting 3 | arena | 230 | 54.6 | 54.8 | needs a arena (build cost 27,083); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 57.8 | 57.8 | thin at home: wine, ham, stockfish, cheese, candles |
| hold banquet 2 (fish) | mansion | 6.8 | 58.4 | 58.4 | thin at home: wine, cheese |
| hold banquet 4 (premium) | mansion | 20 | 58.4 | 58.4 | thin at home: wine, ham, stockfish, candles, premium cheese |
| hold banquet 1 (meat) | mansion | 4.2 | 59.3 | 59.3 |  |
| hold banquet 2 (pies) | mansion | 7 | 59.6 | 59.6 | thin at home: wine, cheese, pies, candles |
| hold sermon 2 (candles) | church | 31 | 55.2 | 59.7 | needs a church (build cost 68,754); thin at home: jewellery, candles, furniture |
| jousting 2 | arena | 210 | 59.8 | 60.0 | needs a arena (build cost 27,083); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 60.6 | 60.6 | thin at home: cheese, pies, candles |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 3 @ 14.2 (keep 14); best orders clear only 4 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 16.0 (keep 14); best orders clear only 1 a turn after crew: ship stays at 0
- best towns now: Rouhomme +65, Orlesailles +51, Donaunieder +42, Angefont +41, Toqueque +39
- Rouhomme would trade: pasties buy 12 @ 12.6; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~103 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.20 (21/turn) | timber 25 (7.04->10.54), wine 7 (5.78->6.55), leather 1 (23.94->27.93), firewood 1 (1.98->6.03) | dyed cloth 5 (11.45->13.01), cheese 4 (7.35->9.17) | +102 |
| Amsdermund | 1111 | 0.39 | 0.70 (72/turn) | limestone 3 (18.06->52.25), wine 8 (5.78->7.03), acid 1 (114.45->120.65), pasties 5 (14.91->16.72) | cloth 24 (6.51->7.55), cheese 4 (6.2->9.17), copper ingots 1 (18.17->18.71), malt 1 (5.25->6.17) | +101 |
| Gottweiler | 1135 | 0.41 | 0.20 (21/turn) | gears 1 (54.08->58.9), nets 3 (36->38), wine 8 (5.78->6.55), leather 1 (23.94->26.6) | silver bars 1 (273->311.6), spinning wheels 1 (195.3->209), cheese 4 (6.3->9.17), ploughs 1 (62.48->74.1) | +85 |
| Bordetes | 831 | 0.24 | 0.20 (21/turn) | tiles 3 (3.34->11.4), cured fish 4 (22.68->24.13), leather 1 (23.94->26.41), gears 1 (54.08->55.1) | spinning wheels 1 (193.2->209), dyed cloth 5 (10.4->13.01), cheese 4 (6.2->9.17), cloth 24 (7.04->7.55) | +76 |
| Hanstein | 380 | 0.10 | 0.40 (41/turn) | timber 14 (7.04->10.07), limestone 3 (18.06->27.36), nets 6 (36->36.86), steel ingots 2 (17.96->18.81) | cheese 4 (6.14->9.17), dyed cloth 5 (11.13->13.01), seeds 13 (1.8->2.32), flax plants 35 (1.42->1.63) | +69 |

**Best:** Grandgues at about +102 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 31.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 16 @ min 3.06 | goal planner: sells 16 at 3.06 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 73.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 14.4, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 21.8) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 18) |
| light armour | 1 @ 92.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 35.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 22.9k (cash + stock at home prices); +187/turn over 6 turns, +159/turn over 24 turns.
- Limits: cash flow >= -300/turn, prestige >= +5.53/turn (values are after 200 tax a turn).
- Today's settings: value +101/turn, cash +99/turn, prestige -0.84/turn - breaks the prestige floor.
- Plan: value -132/turn, cash -129/turn, prestige +3.36/turn - could not meet the prestige floor.
- Cash check (real vs predicted cash a tick, last 3): +28 vs +102, +69 vs +103, +79 vs +107.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> no route: +0/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +5/turn
  - retting pit 1 0.91 -> 0.70: -12/turn
  - flax farm 1 4.64 -> 3.55: +8/turn
  - weavery 1 0.50 -> 0.27: -16/turn
  - brewery 1 0.14 -> 0.27: -19/turn
  - sewing shop 1 0.30 -> 0.15: +1/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.30: -11/turn
  - ropewalk 1 0.25 -> 0.00: +16/turn
- Model check over the last 62 turns: predicted +97/turn for the settings we ran, real +68/turn.
- Worth of one more unit per turn: labour 1.66, thread 4.17, cloth 6.67, flax fibres 4.94, garments 19.30, nets 30.06, beer 2.88, timber 3.46, prestige 10000.00, cash 0.00
- Orders it would set: beer sell 16 (v2 15); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 5); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 29 (v2 18); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.30, worth +13/turn.
- Ship linen snake: Grandgues -> no route (+0/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 473 (+184 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 5.74 |
| ret | 3 | 0.91 | 1.15 |
| spin | 4 | 1.65 | 2.03 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 379/228, cloth 73/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 5.5 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
- R5: tar buy not filling: bid 11 under the home ask 11.3 for 6 turns, bought 0.0 of 1, 0.0 held (0.0 turns); raise needs Taylor (ceiling 11.0)
