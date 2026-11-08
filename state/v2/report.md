# v2 shadow report

Turn 13868, 2026-11-08 05:18. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 8,687, prestige 3,492 (372 free, -1.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 15, sell @ 3.28 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 6 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 7 | 6 | 6 | 3 | 0 | stop 27, buy 7, buy @ 3.7 |
| labour | 30 | 29 | 512 | 0 | 17 | buy 30, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**5 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: home ask 2.68 is above our ceiling 2.40 and last turn bought 4 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **grain**: brewery 1 ran short of grain (buy is live (7 @ 3.7), 6 bought last turn); labour need rises ~18/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **grain**: only 0.8 turns of grain left and buying 7 (need 18) -> v2: buy 18
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 17 labour expired last turn (~28 coin): holding 30 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **tar**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 514, not 614

## Prestige spending, cheapest coin per prestige first

533 turns left: prestige gained now converts 93.1% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 51.3 | 51.3 | running |
| jousting 3 | arena | 230 | 53.8 | 54.1 | needs a arena (build cost 24,892); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 54.7 | 54.7 | thin at home: hop beer, wine, ham, stockfish, cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 55.4 | 55.4 |  |
| hold banquet 4 (premium) | mansion | 20 | 57.0 | 57.0 | thin at home: hop beer, wine, ham, stockfish |
| hold banquet 4 | mansion | 17.5 | 57.5 | 57.5 | thin at home: wine, hop beer, ham, stockfish, cheese |
| jousting 2 | arena | 210 | 59.0 | 59.2 | needs a arena (build cost 24,892); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 1 (meat) | mansion | 4.2 | 59.8 | 59.8 | thin at home: cured meat |
| hold banquet 2 (fish) | mansion | 6.8 | 61.3 | 61.3 | thin at home: wine, cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 61.6 | 61.6 | thin at home: hop beer, cheese |
| hold banquet 3 (pies) | mansion | 8 | 61.9 | 61.9 | thin at home: hop beer, cheese |
| hold sermon 2 (candles) | church | 31 | 58.6 | 63.3 | needs a church (build cost 65,408); thin at home: candles, furniture |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Amsdermund +19
- Amsdermund would trade: pasties buy 13 @ 15.8; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~107 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.90 (97/turn) | bread 151 (2.37->2.93), timber 24 (8.24->10.92), charcoal 19 (2.81->3.88), firewood 34 (2.81->4.5) | tapestries 1 (703.5->736.25), cloth 8 (8.03->8.8), candles 1 (77.7->81), flax plants 3 (1.07->1.62) | +197 |
| Helmgreen | 1354 | 0.55 | 0.20 (21/turn) | acid 1 (141.75->146.3), hides 1 (10.61->12.82) | tapestries 1 (588->736.25), candles 1 (75.08->81), raw cloth 5 (7.25->8.5), thread 21 (4.33->5.05) | +163 |
| Etallaen | 774 | 0.22 | 0.60 (64/turn) | cured fish 8 (24.57->34.2), coats 1 (85.05->133), grain 99 (3->3.5), cookware 4 (24.78->25.84) | cloth 7 (7.35->8.8), candles 1 (73.5->81), cheese 3 (8.4->9.17), wrought iron 1 (14.07->15.01) | +145 |
| Bedenis | 566 | 0.16 | 0.10 (11/turn) | nets 4 (33.6->34.39), flax fibres 2 (5.55->6.37), lead ore 2 (10.82->12.16) | tapestries 1 (624.75->736.25), cloth 13 (7.88->8.8), candles 1 (78.23->81), dyed cloth 2 (11.55->13.01) | +131 |
| Hofkirchen | 991 | 0.34 | 0.80 (86/turn) | grain 99 (3->4.1), flax fibres 2 (5.55->10.16), spirits 2 (10.03->11.69), paper 8 (23.31->23.94) | cloth 24 (8.03->8.8), cheese 3 (5.78->9.17), rope 7 (79.8->81.7), candles 1 (73.5->81) | +97 |

**Best:** Grandgues at about +197 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 29.6, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 5) |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| furniture | 2 @ 14.9, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 22.4) |
| grain | 9 @ 3.7, stop 33 |  | goal planner: buys 9 a turn for today's rates, keeps up to 33 (v2 had 18) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 14) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 21.4k (cash + stock at home prices); +57/turn over 6 turns, -30/turn over 24 turns.
- Limits: cash flow >= -195/turn, prestige >= -0.30/turn (values are after 200 tax a turn).
- Today's settings: value +79/turn, cash +64/turn, prestige -1.87/turn - breaks the prestige floor.
- Plan: value +11/turn, cash +13/turn, prestige -0.30/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -38 vs +58, +90 vs +61, +56 vs +61.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Etallaen: +1/turn
  - ship Flax Wyrm -> Chatgnan: +0/turn
  - net maker 0.00 -> 0.29: +7/turn
  - spinnery 1 1.65 -> 1.37: -7/turn
  - retting pit 1 0.91 -> 0.78: +4/turn
  - flax farm 1 4.64 -> 3.91: +7/turn
  - weavery 1 0.50 -> 0.42: -13/turn
  - sewing shop 1 0.30 -> 0.25: -6/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.27: -17/turn
  - ropewalk 1 0.25 -> 0.00: +19/turn
- Model check over the last 58 turns: predicted +103/turn for the settings we ran, real -5/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.17, cloth 6.67, flax fibres 4.94, garments 19.30, nets 29.91, beer 3.02, timber 3.33, prestige 59.52, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 4 (v2 8); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 18); labour buy 29 (v2 14); light armour buy 1 (v2 None); rope sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.27, worth +11/turn.
- Ship linen snake: Grandgues -> Etallaen (+6/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Chatgnan (+0/turn over staying).
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

Buffers: flax fibres 27/77, thread 620/228, cloth 72/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 5.8 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
