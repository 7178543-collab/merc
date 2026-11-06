# v2 shadow report

Turn 13816, 2026-11-06 01:36. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 11,016, prestige 3,290 (170 free, -0.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 61 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 14 | 3 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 33 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 518 | 0 | 11 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.70 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Tuning

- **tar**: home ask 11.70 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 518, not 618

## Prestige spending, cheapest coin per prestige first

585 turns left: prestige gained now converts 94.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.1 | 50.1 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 54.1 | 54.1 |  |
| hold banquet 4 (pies) | mansion | 18 | 54.8 | 54.8 | thin at home: hop beer, wine, ham, stockfish, cheese |
| jousting 3 | arena | 230 | 54.5 | 54.8 | needs a arena (build cost 25,680); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 57.1 | 57.1 | thin at home: wine, cheese |
| hold banquet 2 (pies) | mansion | 7 | 57.8 | 57.8 | thin at home: wine, cheese, pies |
| hold banquet 4 | mansion | 17.5 | 58.0 | 58.0 | thin at home: wine, hop beer, ham, stockfish, cheese |
| hold banquet 4 (premium) | mansion | 20 | 58.5 | 58.5 | thin at home: hop beer, wine, ham, stockfish, premium cheese |
| hold banquet 1 (meat) | mansion | 4.2 | 59.3 | 59.3 |  |
| hold sermon 2 (candles) | church | 31 | 55.1 | 59.3 | needs a church (build cost 65,736); thin at home: candles, furniture |
| hold feast 2 | townhouse | 2.6 | 54.4 | 59.7 | needs a townhouse (build cost 7,778); thin at home: wine |
| jousting 2 | arena | 210 | 59.7 | 60.0 | needs a arena (build cost 25,680); thin at home: swords, protection, coats, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 15.6 (keep 14); best orders clear only -4 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 16.0 (keep 14); best orders clear only 1 a turn after crew: ship stays at 0
- best towns now: Orlesailles +58, Rouhomme +53, Donaunieder +42, Toqueque +40, Fulkirch +34
- Orlesailles would trade: pasties buy 14 @ 13.3; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~104 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Kirchwerp | 1072 | 0.38 | 0.30 (31/turn) | furniture 12 (14.18->17.1), garments 10 (18.79->20.71), yarn 6 (3.76->5.08) | dyed cloth 29 (10.4->14.82), cloth 24 (7.35->8.35), belts 2 (32.76->38.38), cheese 4 (6.2->8.26) | +194 |
| Hofkirchen | 991 | 0.33 | 0.30 (31/turn) | garments 10 (18.79->19.57), grain 2 (2.62->3.34) | dyed cloth 29 (10.29->14.82), cloth 24 (7.04->8.35), medicine 1 (133.35->146.3), cheese 4 (4.94->8.26) | +187 |
| Rouhomme | 368 | 0.10 | 0.70 (73/turn) | charcoal 18 (2.05->4.67), bread 160 (2.25->2.75), garments 10 (18.79->19.76), nails 7 (6.51->7.08) | dyed cloth 12 (11.23->14.82), cloth 24 (7.25->8.35), belts 2 (32.97->38.38), cheese 4 (6.51->8.26) | +175 |
| Heilegg | 826 | 0.24 | 0.30 (31/turn) | cured fish 5 (22.68->23.56), yarn 6 (3.76->4.07) | dyed cloth 29 (10.71->14.82), cloth 24 (7.04->8.35), thread 49 (4.49->5.1), belts 2 (34.65->38.38) | +175 |
| Bordetes | 831 | 0.24 | 0.20 (21/turn) | tiles 4 (3.3->11.21), hop beer 3 (12.29->14.82), garments 10 (18.79->19.57), yarn 3 (3.76->4.01) | dyed cloth 22 (10.4->14.82), cloth 24 (7.04->8.35), belts 2 (34.23->38.38), cheese 4 (6.2->8.26) | +168 |

**Best:** Kirchwerp at about +194 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.8, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
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
| light armour | 1 @ 92.5, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 36.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 22.4k (cash + stock at home prices); +123/turn over 6 turns, +149/turn over 24 turns.
- Limits: cash flow >= -292/turn, prestige >= +5.42/turn (values are after 200 tax a turn).
- Today's settings: value +99/turn, cash +102/turn, prestige -0.85/turn - breaks the prestige floor.
- Plan: value -136/turn, cash -132/turn, prestige +3.35/turn - could not meet the prestige floor.
- Cash check (real vs predicted cash a tick, last 3): +263 vs +109, +107 vs +110, +87 vs +104.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Vauxvais: +3/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +3/turn
  - retting pit 1 0.91 -> 0.67: -15/turn
  - flax farm 1 4.64 -> 3.47: +12/turn
  - brewery 1 0.14 -> 0.27: -22/turn
  - spinnery 1 1.65 -> 1.18: -3/turn
  - ropewalk 1 0.25 -> 0.00: -21/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.35: +24/turn
  - sewing shop 1 [bind garments 3] 0.00 -> 0.30: -37/turn
- HAND-OVER: goal planner: model check held 12 runs, it now runs 'rates' live.
- Model check over the last 61 turns: predicted +97/turn for the settings we ran, real +66/turn.
- Worth of one more unit per turn: labour 1.58, thread 3.96, cloth 6.33, flax fibres 4.69, garments 19.30, nets 28.58, beer 2.88, timber 3.19, prestige 10000.00, cash 0.00
- Orders it would set: beer sell 16 (v2 15); cloth sell 1 (v2 none); firewood buy 4 (v2 5); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 29 (v2 18); light armour buy 1 (v2 None); rope sell 2 (v2 none)
- Recipe: sewing shop 1 sew garments 2 -> bind garments 3 at 0.30, worth +27/turn.
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.35, worth +33/turn.
- Ship linen snake: Grandgues -> Vauxvais (+4/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +70/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
- Trim: donate weavery 1: +17/turn (tax 18 saved).

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 480 (+191 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 5.90 |
| ret | 3 | 0.91 | 1.18 |
| spin | 4 | 1.65 | 2.08 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 345/228, cloth 73/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 5.45 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
- R5: tar buy not filling: bid 11 under the home ask 11.7 for 6 turns, bought 0.0 of 1, 0.0 held (0.0 turns); raise needs Taylor (ceiling 11.0)
