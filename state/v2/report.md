# v2 shadow report

Turn 13901, 2026-11-09 14:10. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 10,363, prestige 3,501 (381 free, -1.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.26 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 10 | 4 | 4 | 0 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 33 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 30 | 521 | 0 | 9 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 0 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 10.50 x6, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 525, not 625

## Prestige spending, cheapest coin per prestige first

500 turns left: prestige gained now converts 91.9% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.1 | 50.1 | running |
| hold banquet 4 (pies) | mansion | 18 | 54.7 | 54.7 | thin at home: hop beer, ham, stockfish, cheese |
| jousting 3 | arena | 230 | 55.3 | 55.5 | needs a arena (build cost 26,322); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 56.8 | 56.8 | thin at home: hop beer, ham, stockfish, cheese |
| hold banquet 4 (premium) | mansion | 20 | 56.9 | 56.9 | thin at home: hop beer, ham, stockfish |
| hold banquet 1 (fish) | mansion | 4.2 | 57.4 | 57.4 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 59.6 | 59.6 | thin at home: cured fish, cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 59.6 | 59.6 | thin at home: hop beer, cured fish, cheese |
| jousting 2 | arena | 210 | 60.5 | 60.8 | needs a arena (build cost 26,322); thin at home: swords, protection, coats, light armour, plate armour; needs weaponry skill |
| hold banquet 3 (pies) | mansion | 8 | 61.1 | 61.1 | thin at home: hop beer, cheese |
| hold banquet 2 (pies) | mansion | 7 | 63.3 | 63.3 | thin at home: cheese |
| hold banquet 3 (meat) | mansion | 7.6 | 64.5 | 64.5 | thin at home: hop beer, cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: furniture buy 2 @ 14.0, pasties buy 2 @ 13.6; crew 0.1; est +25 a turn; stock: furniture 2 @ 14.0 (keep 145); stock: pasties 2 @ 13.6 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Orlesailles +46, Toqueque +36, Bordetes +34, Bedenis +32, Clarfranche +30
- Orlesailles would trade: pasties buy 14 @ 14.1; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~106 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.04 | 0.90 (96/turn) | bread 154 (2.31->3.61), firewood 37 (1.98->6.46), timber 25 (8.45->9.59), bricks 3 (8.56->10.64) | thread 18 (4.96->5.2), candles 1 (81.9->83), flour 1 (23.1->23.94), salt 3 (5.51->5.56) | +319 |
| Rouhomme | 368 | 0.10 | 1.00 (106/turn) | bread 96 (2.31->4.05), firewood 23 (1.98->5.42), cloth 0 (6.61->9.36), grain 1 (2.6->4.27) | thread 30 (4.73->5.2), cookware 4 (23.31->24.13), tools 11 (4.73->5.13), candles 0 (79.8->83) | +172 |
| Gotthafen | 964 | 0.32 | 0.20 (21/turn) | garments 10 (24.2->34.96), arms 11 (32.97->37.05), cloth 1 (6.61->8.55), glass ingots 1 (55.12->57.95) | salt 9 (4.43->5.56), belts 2 (34.23->35.91), flour 1 (19.64->23.94) | +157 |
| Coburgbaum | 619 | 0.18 | 0.90 (96/turn) | garments 10 (24.2->30.02), dyed cloth 11 (12.92->15.67), firewood 16 (1.98->7.69), flax fibres 2 (5.1->7.31) | salt 9 (4.47->5.56), cloth 24 (9.5->9.75), varnish 1 (15.02->15.58) | +108 |
| Darmwald | 1022 | 0.35 | 0.20 (21/turn) | garments 10 (24.2->32.49), beer 15 (3.4->4.75), cloth 1 (6.61->10.16), thread 4 (4.54->5.37) | candles 1 (81.38->83) | +99 |

**Best:** Grandgues at about +319 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.8, stop 1 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 3.0 turns |
| beer |  | 16 @ min 3.26 | goal planner: sells 16 at 3.26 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 16 = 3.9 turns |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 4 @ 2.4, stop 16 |  | goal planner: buys 4 a turn for today's rates, keeps up to 16 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.6) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 25) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 37.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 1 = 4.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 25.2k (cash + stock at home prices); +196/turn over 6 turns, +181/turn over 24 turns.
- Limits: cash flow >= -265/turn, prestige >= -0.34/turn (values are after 200 tax a turn).
- Today's settings: value +83/turn, cash +70/turn, prestige -1.91/turn - breaks the prestige floor.
- Plan: value +5/turn, cash +102/turn, prestige -0.34/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -269 vs +50, -527 vs +58, +143 vs +63 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Karlmoor: +7/turn
  - ship Flax Wyrm -> Corstoft: +6/turn
  - net maker 0.00 -> 0.29: +8/turn
  - brewery 1 0.14 -> 0.20: -6/turn
  - weavery 1 0.50 -> 0.61: -10/turn
  - sewing shop 1 0.30 -> 0.36: +12/turn
  - ropewalk 1 0.25 -> 0.00: -4/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.22: +10/turn
  - spinnery 1 1.65 -> 1.04: -20/turn
  - retting pit 1 0.91 -> 0.59: +10/turn
- Model check over the last 59 turns: predicted +103/turn for the settings we ran, real +59/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.63, thread 4.09, cloth 6.52, flax fibres 4.85, garments 18.88, nets 29.30, beer 2.86, timber 3.33, prestige 62.35, cash 0.00
- Orders it would set: beer sell 16 (v2 15); cloth sell 1 (v2 none); firewood buy 4 (v2 8); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 29 (v2 25); light armour buy 1 (v2 None); rope sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.22, worth +9/turn.
- Ship linen snake: Grandgues -> Karlmoor (+7/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Corstoft (+6/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +81/turn, doesn't pay yet (waits until 800 free (keeps 300 after))
  - +1 plot park 1 for ~1782 coin: +1/turn, payback 2256 turns, doesn't pay yet (materials thin at home: limestone)

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

Buffers: flax fibres 27/77, thread 899/228, cloth 72/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 5.4 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
