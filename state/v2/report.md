# v2 shadow report

Turn 13765, 2026-11-03 22:22. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 8,107, prestige 3,182 (62 free, -0.3/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 14 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.4 |
| grain | 33 | 10 | 9 | 0 | 0 | stop 33, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 518 | 0 | 11 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 12.60 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Tuning

- **tar**: home ask 12.60 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 518, not 618

## Prestige spending, cheapest coin per prestige first

636 turns left: prestige gained now converts 95.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.9 | 48.9 | running |
| hold banquet 4 (pies) | mansion | 18 | 51.2 | 51.2 | thin at home: hop beer, wine, stockfish |
| jousting 3 | arena | 230 | 53.2 | 53.4 | needs a arena (build cost 25,319); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 54.1 | 54.1 | thin at home: wine, hop beer, ham, stockfish |
| hold banquet 1 (fish) | mansion | 4.2 | 54.2 | 54.2 |  |
| hold banquet 4 (premium) | mansion | 20 | 54.5 | 54.5 | thin at home: hop beer, wine, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 54.8 | 54.8 | thin at home: hop beer, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 56.8 | 56.8 | thin at home: hop beer |
| hold banquet 2 (pies) | mansion | 7 | 57.2 | 57.2 | thin at home: wine, pies |
| hold banquet 2 (fish) | mansion | 6.8 | 58.1 | 58.1 | thin at home: wine |
| jousting 2 | arena | 210 | 58.3 | 58.5 | needs a arena (build cost 25,319); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| jousting 1 | arena | 170 | 59.9 | 60.1 | needs a arena (build cost 25,319); thin at home: protection, light armour, arms; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 20 @ 13.8, pasties buy 7 @ 15.1; crew 0.2; est +258 a turn; stock: furniture 20 @ 13.8 (keep 145); stock: pasties 7 @ 15.1 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 5 @ 13.9 (keep 14); best orders clear only 14 a turn after crew: ship stays at 0
- best towns now: Chatgnan +675, Donaunieder +594, Hofkirchen +559, Amsdermund +505, Neuborn +502
- Chatgnan would trade: furniture buy 52 @ 12.4; crew 0.5

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~105 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Kirchwerp | 1072 | 0.38 | 0.40 (42/turn) | thread 36 (4.66->5.7), furniture 12 (15.75->18.24), light armour 2 (87.67->93.57), salt 18 (5.88->6.27) | cloth 11 (7.04->9.59), garments 2 (20.06->23) | +75 |
| Vauxvais | 204 | 0.06 | 0.30 (32/turn) | charcoal 18 (1.83->2.87), logs 1 (3.91->5.79), tiles 4 (2.39->3.25), wheels 1 (21.63->22.8) | bricks 13 (4.85->7.69), cloth 11 (7.61->9.59), garments 2 (20.58->23), flax fibres 8 (5.04->5.65) | +73 |
| Nürnnieder | 520 | 0.15 | 0.10 (11/turn) | coats 1 (82.42->133), tackles 2 (208.95->216.6), acid 1 (132.3->135.85), pickaxes 1 (11.76->12.25) | cloth 3 (7.88->9.59), garments 2 (21.21->23), tar 3 (10.19->11.4), flax plants 1 (1.24->1.54) | +72 |
| Grandgues | 152 | 0.04 | 0.20 (21/turn) | charcoal 18 (1.83->4.99), tiles 8 (2.39->3.36), firewood 1 (1.76->5.94), lead ore 1 (8.03->11.49) | cloth 3 (8.51->9.59), beer 4 (3.36->3.68), bricks 10 (6.72->7.69), flax plants 9 (1.4->1.54) | +71 |
| Rouhomme | 368 | 0.10 | 0.20 (21/turn) | charcoal 18 (1.83->3.44), lead ore 1 (8.03->12.06), beer 15 (3.46->3.89), grain 2 (2.52->2.81) | cloth 11 (7.35->9.59), cookware 6 (21->23.18), mouldboards 2 (37.59->40.47), flax fibres 13 (5.04->5.65) | +70 |

**Best:** Kirchwerp at about +75 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 29.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 16 @ min 3.06 | goal planner: sells 16 at 3.06 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 83.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 7.1 | goal planner: sells 1 a turn at 7.1, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 1 @ min 1.36 | goal planner: trial sale of an idle pile, 1 a turn at 1.36, keeps 219 (6 over) |
| furniture | 2 @ 15.3, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.4 | goal planner: sells 11 at 19.4 (v2 had 10 at 22.2) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 18) |
| light armour | 1 @ 85.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 37.2) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 20.0k (cash + stock at home prices); +176/turn over 6 turns, +96/turn over 24 turns.
- Limits: cash flow >= -171/turn, prestige >= +9.92/turn (values are after 200 tax a turn).
- Today's settings: value +101/turn, cash +102/turn, prestige -0.31/turn - breaks the prestige floor.
- Plan: value -139/turn, cash -136/turn, prestige +3.89/turn - could not meet the prestige floor.
- Cash check (real vs predicted cash a tick, last 3): +195 vs +99, +62 vs +98, +101 vs +101.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Etallaen: +2/turn
  - ship Flax Wyrm -> Chatgnan: +1/turn
  - net maker 0.00 -> 0.29: +3/turn
  - flax farm 1 4.64 -> 4.56: +1/turn
  - weavery 1 0.50 -> 0.61: -10/turn
  - sewing shop 1 0.30 -> 0.37: +12/turn
  - ropewalk 1 0.25 -> 0.00: -14/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.34: +17/turn
  - brewery 1 0.14 -> 0.27: -18/turn
  - mansion 1 0.00 -> 1.00: -232/turn
- Model check over the last 58 turns: predicted +70/turn for the settings we ran, real +99/turn.
- Worth of one more unit per turn: labour 1.63, thread 4.09, cloth 6.54, flax fibres 4.85, garments 18.92, nets 29.50, beer 2.80, timber 3.04, prestige 10000.00, cash 0.00
- Orders it would set: beer sell 16 (v2 15); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 5); flax plants sell 1 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 29 (v2 18); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.34, worth +14/turn.
- Ship linen snake: Grandgues -> Etallaen (+2/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Chatgnan (+1/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +82/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.3/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 505 (+216 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 6.45 |
| ret | 3 | 0.91 | 1.29 |
| spin | 4 | 1.65 | 2.28 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 249/228, cloth 81/128

## Self-diagnosis

- R5: tar buy not filling: bid 11 under the home ask 12.6 for 6 turns, bought 0.0 of 1, 0.0 held (0.0 turns); raise needs Taylor (ceiling 11.0)
