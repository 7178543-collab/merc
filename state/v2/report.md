# v2 shadow report

Turn 13863, 2026-11-08 00:56. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 8,484, prestige 3,501 (381 free, -1.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 75 | 0 | 4 | 0 | 0 | min_holding 60, sell 15, sell @ 3.38 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 4 | 4 | 4 | 0 | 0 | stop 13, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 12 | 0 | 9 | 0 | 0 | stop 8, buy 2, buy @ 3.7 |
| labour | 29 | 29 | 518 | 0 | 11 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 0 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: home ask 2.66 is above our ceiling 2.40 and last turn bought 4 of ~4 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 12.60 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Tuning

- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 12.60 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 518, not 618

## Prestige spending, cheapest coin per prestige first

538 turns left: prestige gained now converts 93.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.1 | 50.1 | running |
| jousting 3 | arena | 230 | 54.1 | 54.3 | needs a arena (build cost 24,984); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 54.9 | 54.9 | thin at home: pasties, ham, stockfish, cheese |
| hold banquet 1 (fish) | mansion | 4.2 | 55.1 | 55.1 |  |
| hold banquet 1 (meat) | mansion | 4.2 | 56.6 | 56.6 |  |
| hold banquet 4 | mansion | 17.5 | 58.0 | 58.0 | thin at home: ham, stockfish, cheese |
| hold banquet 4 (premium) | mansion | 20 | 58.4 | 58.4 | thin at home: ham, stockfish, premium cheese |
| jousting 2 | arena | 210 | 59.3 | 59.5 | needs a arena (build cost 24,984); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 61.3 | 61.3 | thin at home: cheese |
| hold banquet 2 (meat) | mansion | 6.8 | 62.0 | 62.0 | thin at home: cheese |
| hold banquet 3 (pies) | mansion | 8 | 62.2 | 62.2 | thin at home: pasties, cheese |
| hold banquet 2 (pies) | mansion | 7 | 62.9 | 62.9 | thin at home: pasties, cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn
- best towns now: Neuborn +38, Kleinburgh +19
- Neuborn would trade: pasties buy 11 @ 14.5; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~106 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Hofkirchen | 991 | 0.34 | 0.80 (85/turn) | grain 98 (2.75->4.14), yarn 10 (4.33->5.94), nets 6 (33.6->35.91), lead ore 2 (14.18->19) | cheese 7 (5.78->9.59), candles 1 (73.5->81), flax fibres 23 (5.62->6.45), garments 2 (22.68->24.4) | +143 |
| Rouhomme | 368 | 0.10 | 0.40 (42/turn) | grain 98 (2.75->3.44), beer 16 (2.96->3.53), thread 16 (4.74->5.03), blades 1 (17.75->19) | cheese 7 (7.09->9.59), lead bars 6 (15.33->18.14), tools 16 (4.51->5.37), cloth 10 (8.72->9.3) | +115 |
| Grandgues | 152 | 0.04 | 0.80 (85/turn) | timber 30 (8.24->10.26), charcoal 19 (2.79->4.2), wine 15 (6.3->6.89), beer 16 (2.96->3.5) | cheese 7 (7.51->9.59), cloth 7 (8.29->9.3), candles 1 (77.7->81), flour 2 (15.96->17.2) | +112 |
| Hanstein | 380 | 0.11 | 0.30 (32/turn) | nets 5 (33.6->35.53), raw cloth 2 (7.04->7.93), limestone 1 (15.75->20.52) | cloth 24 (8.14->9.3), flax fibres 17 (5.25->6.45), cheese 6 (6.98->9.59), thread 44 (4.47->4.9) | +93 |
| Amsdermund | 1111 | 0.40 | 0.30 (32/turn) | wine 15 (6.3->9.5), nets 3 (33.6->35.15), yarn 3 (4.33->5.32) | cheese 7 (6.72->9.59), cloth 12 (7.88->9.3), tools 16 (4.58->5.37), flax fibres 16 (5.46->6.45) | +86 |

**Best:** Hofkirchen at about +143 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 30.8, stop 1 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 3.0 turns |
| beer |  | 15 @ min 3.28 | goal planner: sells 15 at 3.28 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 4 @ 2.4, stop 14 |  | goal planner: buys 4 a turn for today's rates, keeps up to 14 (v2 had 8) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.2) |
| grain | 6 @ 3.7, stop 21 |  | goal planner: buys 6 a turn for today's rates, keeps up to 21 (v2 had 18) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 18) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 21.0k (cash + stock at home prices); -540/turn over 6 turns, -45/turn over 24 turns.
- Limits: cash flow >= -187/turn, prestige >= -0.34/turn (values are after 200 tax a turn).
- Today's settings: value +69/turn, cash +54/turn, prestige -1.92/turn - breaks the prestige floor.
- Plan: value +9/turn, cash +13/turn, prestige -0.34/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): -2439 vs +54, -6 vs +52, +1 vs +46 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Etallaen: +6/turn
  - ship Flax Wyrm -> no route: +0/turn
  - brewery 1 0.14 -> 0.08: +11/turn
  - net maker 0.00 -> 0.29: +3/turn
  - spinnery 1 1.65 -> 1.41: -4/turn
  - retting pit 1 0.91 -> 0.80: +4/turn
  - flax farm 1 4.64 -> 4.04: +4/turn
  - weavery 1 0.50 -> 0.41: -20/turn
  - sewing shop 1 0.30 -> 0.24: -5/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.32: -16/turn
- Model check over the last 61 turns: predicted +103/turn for the settings we ran, real +16/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.66, thread 4.17, cloth 6.67, flax fibres 4.94, garments 19.30, nets 30.00, beer 2.91, timber 3.29, prestige 55.69, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 4 (v2 8); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 6 (v2 18); labour buy 29 (v2 18); light armour buy 1 (v2 None); rope sell 2 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.32, worth +11/turn.
- Ship linen snake: Grandgues -> Etallaen (+6/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +83/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 435 (+146 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.87 |
| ret | 3 | 0.91 | 0.97 |
| spin | 4 | 1.65 | 1.72 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 564/228, cloth 72/128

## Self-diagnosis

- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.45 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
- R5: tar buy not filling: bid 11 under the home ask 12.6 for 4 turns, bought 0.0 of 1, 0.0 held (0.0 turns); raise needs Taylor (ceiling 11.0)
