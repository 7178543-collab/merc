# v2 shadow report

Turn 13817, 2026-11-06 02:42. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,044, prestige 3,289 (169 free, -0.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 14 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 33 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 518 | 0 | 11 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 12.20 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 12.20 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 518, not 618

## Prestige spending, cheapest coin per prestige first

584 turns left: prestige gained now converts 94.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.8 | 49.8 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 54.0 | 54.0 |  |
| hold banquet 4 (pies) | mansion | 18 | 54.2 | 54.2 | thin at home: hop beer, wine, ham, stockfish, cheese |
| jousting 3 | arena | 230 | 54.9 | 55.1 | needs a arena (build cost 25,906); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 57.5 | 57.5 | thin at home: wine, hop beer, ham, stockfish, cheese |
| hold banquet 2 (fish) | mansion | 6.8 | 57.6 | 57.6 | thin at home: wine, cheese |
| hold banquet 4 (premium) | mansion | 20 | 57.9 | 57.9 | thin at home: hop beer, wine, ham, stockfish, premium cheese |
| hold banquet 2 (pies) | mansion | 7 | 58.3 | 58.3 | thin at home: wine, cheese, pies |
| hold banquet 1 (meat) | mansion | 4.2 | 59.2 | 59.2 |  |
| hold sermon 2 (candles) | church | 31 | 55.2 | 59.5 | needs a church (build cost 66,185); thin at home: jewellery, candles, furniture |
| hold feast 2 | townhouse | 2.6 | 54.3 | 59.6 | needs a townhouse (build cost 7,643); thin at home: wine |
| jousting 2 | arena | 210 | 60.1 | 60.4 | needs a arena (build cost 25,906); thin at home: swords, protection, coats, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 14.1 (keep 14); best orders clear only -6 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 16.0 (keep 14); best orders clear only 1 a turn after crew: ship stays at 0
- best towns now: Rouhomme +57, Orlesailles +52, Heilegg +39, Fulkirch +35, Bordetes +29
- Rouhomme would trade: pasties buy 14 @ 14.1; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~104 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Bordetes | 831 | 0.24 | 0.20 (21/turn) | tiles 4 (3.34->11.21), garments 10 (18.82->20.33), coats 1 (66.15->76.47), hop beer 3 (11.45->14.82) | dyed cloth 17 (10.4->12.82), cloth 24 (7.04->8.15), cheese 4 (6.2->8.6), tackles 1 (181.65->188.1) | +127 |
| Neuborn | 780 | 0.22 | 1.00 (104/turn) | bread 145 (2.25->3.17), garments 9 (18.82->19.38), coats 0 (66.15->67.45), grain 1 (2.62->3.65) | cloth 21 (6.46->8.15), dyed cloth 8 (10.71->12.82), cheese 3 (5.25->8.6), raw cloth 0 (5.88->6.13) | +104 |
| Amsdermund | 1111 | 0.39 | 0.40 (41/turn) | limestone 2 (17.96->49.4), garments 10 (18.82->22.23), wine 5 (5.72->6.22), gold ore 1 (197.4->199.5) | cloth 24 (6.51->8.15), cheese 4 (6.2->8.6), thread 17 (4.51->5.1) | +103 |
| Pontmont | 341 | 0.09 | 0.20 (21/turn) | coats 1 (66.15->71.25), hinges 1 (37.59->42.75), garments 10 (18.82->19.19), nails 5 (6.41->6.65) | lead bars 9 (11.55->15.01), dyed cloth 17 (11.34->12.82), cloth 24 (7.35->8.15), cheese 4 (6.3->8.6) | +99 |
| Rouhomme | 368 | 0.10 | 0.60 (62/turn) | bread 160 (2.25->2.77), coats 1 (66.15->71.72), nails 7 (6.41->7.08), garments 10 (18.82->19.19) | cloth 24 (7.25->8.15), dyed cloth 12 (11.23->12.82), cheese 4 (6.46->8.6), candles 1 (79.8->84) | +98 |

**Best:** Bordetes at about +127 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 31.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 16 @ min 3.06 | goal planner: sells 16 at 3.06 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 13.8, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 21.8) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 18) |
| light armour | 1 @ 93, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 36.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 22.7k (cash + stock at home prices); +208/turn over 6 turns, +158/turn over 24 turns.
- Limits: cash flow >= -294/turn, prestige >= +5.46/turn (values are after 200 tax a turn).
- Today's settings: value +101/turn, cash +103/turn, prestige -0.85/turn - breaks the prestige floor.
- Plan: value -136/turn, cash -133/turn, prestige +3.35/turn - could not meet the prestige floor.
- Cash check (real vs predicted cash a tick, last 3): +107 vs +110, +87 vs +104, +28 vs +102.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Vauxvais: +1/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +3/turn
  - flax farm 1 4.64 -> 4.57: +0/turn
  - sewing shop 1 0.30 -> 0.36: -6/turn
  - weavery 1 0.50 -> 0.60: +8/turn
  - ropewalk 1 0.25 -> 0.00: -17/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.32: +18/turn
  - brewery 1 0.14 -> 0.27: -22/turn
  - mansion 1 0.00 -> 1.00: -222/turn
- Model check over the last 62 turns: predicted +97/turn for the settings we ran, real +70/turn.
- Worth of one more unit per turn: labour 1.66, thread 4.17, cloth 6.66, flax fibres 4.94, garments 19.27, nets 29.94, beer 2.96, timber 3.12, prestige 10000.00, cash 0.00
- Orders it would set: beer sell 16 (v2 15); cloth sell 1 (v2 none); firewood buy 4 (v2 5); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 29 (v2 18); light armour buy 1 (v2 None); rope sell 2 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.32, worth +14/turn.
- Ship linen snake: Grandgues -> Vauxvais (+1/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 477 (+188 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 5.84 |
| ret | 3 | 0.91 | 1.17 |
| spin | 4 | 1.65 | 2.06 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 356/228, cloth 73/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 5.45 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
- R5: tar buy not filling: bid 11 under the home ask 12.2 for 6 turns, bought 0.0 of 1, 0.0 held (0.0 turns); raise needs Taylor (ceiling 11.0)
