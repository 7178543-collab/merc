# v2 shadow report

Turn 13822, 2026-11-06 07:04. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,863, prestige 3,285 (165 free, -0.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 15 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
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
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.20 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.20 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 518, not 618

## Prestige spending, cheapest coin per prestige first

579 turns left: prestige gained now converts 94.5% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 49.8 | 49.8 | running |
| jousting 3 | arena | 230 | 54.0 | 54.2 | needs a arena (build cost 25,367); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 54.3 | 54.3 |  |
| hold banquet 4 (pies) | mansion | 18 | 56.9 | 56.9 | thin at home: hop beer, wine, stockfish, cheese, pies, candles |
| hold banquet 1 (meat) | mansion | 4.2 | 58.3 | 58.3 |  |
| hold banquet 4 (premium) | mansion | 20 | 59.2 | 59.2 | thin at home: hop beer, wine, stockfish, candles |
| jousting 2 | arena | 210 | 59.1 | 59.4 | needs a arena (build cost 25,367); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 60.1 | 60.1 | thin at home: hop beer, cheese, pies, candles |
| hold sermon 2 (candles) | church | 31 | 56.0 | 60.3 | needs a church (build cost 64,561); thin at home: candles, furniture |
| hold banquet 4 | mansion | 17.5 | 60.7 | 60.7 | thin at home: wine, hop beer, ham, stockfish, cheese, candles |
| hold banquet 3 (fish) | mansion | 7.6 | 61.3 | 61.3 | thin at home: hop beer, cheese |
| hold banquet 2 (fish) | mansion | 6.8 | 62.2 | 62.2 | thin at home: wine, cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 15.0 (keep 14); best orders clear only 5 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 16.0 (keep 14); best orders clear only 1 a turn after crew: ship stays at 0
- best towns now: Orlesailles +55, Rouhomme +46, Angefont +44, Fulkirch +35, Donaunieder +29
- Orlesailles would trade: pasties buy 14 @ 13.5; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~104 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Brebronn | 862 | 0.26 | 0.30 (31/turn) | tapestries 1 (645.75->807.5), steel ingots 3 (17.54->19.19), cured fish 5 (22.68->23.75) | cheese 6 (5.04->9.17), dyed cloth 7 (11.23->14.15), flax fibres 21 (4.54->5.75), flax plants 16 (0.96->1.68) | +229 |
| Kleinburgh | 1440 | 0.58 | 0.20 (21/turn) | tapestries 1 (645.75->798), steel ingots 3 (17.54->21.66), malt 2 (6.72->9.03) | cheese 6 (6.83->9.17), jewellery 5 (76.65->79.33), dyed cloth 6 (12.5->14.15), gears 1 (66.67->69.83) | +190 |
| Großaue | 1136 | 0.41 | 0.10 (10/turn) | tapestries 1 (645.75->802.75), pasties 1 (15.65->24.7) | dyed cloth 7 (11.76->14.15), axes 1 (13.23->19.57), gears 1 (66.15->69.83) | +183 |
| Hanbrücken | 531 | 0.15 | 0.10 (10/turn) | tapestries 1 (645.75->798) | dyed cloth 7 (11.23->14.15), cheese 1 (6.2->9.17), slaked lime 1 (9.45->11.97), axes 1 (19.21->19.57) | +168 |
| Kirchwerp | 1072 | 0.37 | 0.20 (21/turn) | tapestries 1 (645.75->712.5), yarn 10 (4.49->5.08) | jewellery 8 (73.5->79.33), dyed cloth 7 (10.4->14.15), cheese 6 (6.2->9.17), gears 1 (64.05->69.83) | +159 |

**Best:** Brebronn at about +229 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 34.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer |  | 16 @ min 3.06 | goal planner: sells 16 at 3.06 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| candles | 2 @ 73.5, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had None) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 14 |  | goal planner: buys 4 a turn for today's rates, keeps up to 14 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 14.9, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 22.6) |
| grain | 11 @ 3.7, stop 36 |  | uses 9.0/turn (brewery 1), makes 0.0, holds 33 = 3.7 turns |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 18) |
| light armour | 1 @ 92, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 23.1k (cash + stock at home prices); +174/turn over 6 turns, +159/turn over 24 turns.
- Limits: cash flow >= -286/turn, prestige >= +5.63/turn (values are after 200 tax a turn).
- Today's settings: value +98/turn, cash +96/turn, prestige -0.83/turn - breaks the prestige floor.
- Plan: value -127/turn, cash -47/turn, prestige +3.37/turn - could not meet the prestige floor.
- Cash check (real vs predicted cash a tick, last 3): +69 vs +103, +79 vs +107, -95 vs +99.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Hanbrücken: +2/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.19: +5/turn
  - brewery 1 0.14 -> 0.00: -6/turn
  - brewery 1 [brew beer 2] 0.00 -> 0.15: +10/turn
  - sewing shop 1 0.30 -> 0.36: -7/turn
  - weavery 1 0.50 -> 0.60: +8/turn
  - ropewalk 1 0.25 -> 0.00: -13/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.26: +15/turn
  - spinnery 1 1.65 -> 1.13: -16/turn
- Model check over the last 62 turns: predicted +98/turn for the settings we ran, real +68/turn.
- Worth of one more unit per turn: labour 1.66, thread 4.17, cloth 6.66, flax fibres 4.94, garments 19.27, nets 30.00, beer 3.32, timber 3.22, prestige 10000.00, cash 0.00
- Orders it would set: beer sell 16 (v2 15); candles buy 2 (v2 None); cloth sell 1 (v2 none); firewood buy 4 (v2 5); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); labour buy 29 (v2 18); light armour buy 1 (v2 None); rope sell 1 (v2 none)
- Recipe: brewery 1 brew beer 1 -> brew beer 2 at 0.15, worth +15/turn.
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.26, worth +11/turn.
- Ship linen snake: Grandgues -> Hanbrücken (+2/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 466 (+177 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 5.58 |
| ret | 3 | 0.91 | 1.12 |
| spin | 4 | 1.65 | 1.97 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 412/228, cloth 73/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.0 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
