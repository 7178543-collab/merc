# v2 shadow report

Turn 13780, 2026-11-04 13:26. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 7,251, prestige 3,223 (103 free, -0.5/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 60 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 15 | 4 | 4 | 0 | 0 | stop 15, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.4 |
| grain | 33 | 9 | 9 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 522 | 0 | 7 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 0 waste, 0 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **labour**: buying 29, short of ~125 needed -> v2: buy 125
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 9.80 x11, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Prestige spending, cheapest coin per prestige first

621 turns left: prestige gained now converts 95.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 48.3 | 48.3 | running |
| hold banquet 4 (pies) | mansion | 18 | 51.6 | 51.6 | thin at home: pasties, hop beer, stockfish, pies |
| jousting 3 | arena | 230 | 52.9 | 53.1 | needs a arena (build cost 24,891); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 53.5 | 53.5 |  |
| hold banquet 1 (fish) | mansion | 4.2 | 53.6 | 53.6 |  |
| hold banquet 4 | mansion | 17.5 | 54.2 | 54.2 | thin at home: hop beer, ham, stockfish |
| hold banquet 2 (pies) | mansion | 7 | 54.5 | 54.5 | thin at home: pasties, pies |
| hold banquet 4 (premium) | mansion | 20 | 54.6 | 54.6 | thin at home: hop beer, stockfish |
| hold banquet 3 (pies) | mansion | 8 | 56.4 | 56.4 | thin at home: pasties, hop beer, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 56.6 | 56.6 | thin at home: hop beer |
| hold banquet 2 (meat) | mansion | 6.8 | 57.2 | 57.2 |  |
| jousting 2 | arena | 210 | 58.0 | 58.2 | needs a arena (build cost 24,891); thin at home: swords, protection, coats, plate armour; needs weaponry skill |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 2 @ 13.3 (keep 14); best orders clear only 1 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~99 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Fontaux | 411 | 0.11 | 0.90 (89/turn) | garments 10 (18.29->23.56), thread 38 (4.44->5.65), wine 21 (5.88->7.74), bread 147 (2.18->2.66) | yarn 11 (4.56->4.94), blades 1 (10.45->12.25), casks 2 (6.09->6.65) | +169 |
| Grandgues | 152 | 0.04 | 0.40 (39/turn) | bread 153 (2.18->2.66), premium cheese 3 (27.72->33.63), wine 10 (5.88->6.37), wrought iron 5 (14.8->15.58) | bricks 6 (6.46->9.79), candles 1 (77.17->83), casks 2 (5.78->6.65), yarn 4 (4.58->4.94) | +120 |
| Calange | 218 | 0.06 | 0.10 (10/turn) | cheese 10 (6.51->10.07), garments 10 (18.29->20.71), tools 15 (5.3->5.7), cloth 1 (6.19->6.98) | thread 14 (3.21->4.52), bricks 2 (6.67->9.79), candles 1 (81.38->83), casks 2 (5.51->6.65) | +90 |
| Heilegg | 826 | 0.22 | 1.00 (99/turn) | bellows 1 (206.85->228), bread 127 (2.18->3.1), wine 11 (5.88->7.12), nets 5 (34.4->35.15) | garments 1 (18.9->22.4), candles 0 (79.28->83), casks 1 (5.51->6.65) | +88 |
| Bedenis | 566 | 0.15 | 0.10 (10/turn) | bellows 2 (206.85->233.7) | lead bars 15 (9.87->11.3), garments 2 (20.79->22.4), yarn 7 (4.33->4.94), candles 1 (81.38->83) | +74 |

**Best:** Fontaux at about +169 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 27.4, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 3.0 turns |
| beer |  | 16 @ min 3.06 | goal planner: sells 16 at 3.06 (v2 had 15 at 3.38) |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| cloth |  | 2 @ min 7.05 | goal planner: sells 2 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 4 @ 2.4, stop 15 |  | goal planner: buys 4 a turn for today's rates, keeps up to 15 (v2 had 5) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 19.4 | goal planner: sells 11 at 19.4 (v2 had 10 at 21.6) |
| grain | 9 @ 3.7, stop 34 |  | goal planner: buys 9 a turn for today's rates, keeps up to 34 (v2 had 11) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 125) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 1 = 4.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 20.4k (cash + stock at home prices); +136/turn over 6 turns, +86/turn over 24 turns.
- Limits: cash flow >= -135/turn, prestige >= +8.21/turn (values are after 200 tax a turn).
- Today's settings: value +82/turn, cash +74/turn, prestige -0.52/turn - breaks the prestige floor.
- Plan: value -134/turn, cash -67/turn, prestige +3.68/turn - could not meet the prestige floor.
- Cash check (real vs predicted cash a tick, last 3): -121 vs +99, -9 vs +106, +71 vs +82 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship Flax Wyrm -> Chatgnan: +2/turn
  - net maker 0.00 -> 0.29: +8/turn
  - ropewalk 1 0.25 -> 0.18: +7/turn
  - sewing shop 1 0.30 -> 0.36: -2/turn
  - weavery 1 0.50 -> 0.60: +4/turn
  - retting pit 1 0.91 -> 0.68: -14/turn
  - flax farm 1 4.64 -> 3.31: +13/turn
  - spinnery 1 1.65 -> 1.20: -3/turn
  - brewery 1 0.14 -> 0.27: -10/turn
  - mansion 1 0.00 -> 1.00: -219/turn
- HAND-OVER: goal planner: model check held 12 runs, it now runs 'invest' live.
- Model check over the last 59 turns: predicted +104/turn for the settings we ran, real +98/turn.
- Worth of one more unit per turn: labour 1.61, thread 4.09, cloth 6.50, flax fibres 4.92, garments 18.77, nets 29.32, beer 2.75, timber 3.10, prestige 10000.00, cash 0.00
- Orders it would set: beer sell 16 (v2 15); cloth sell 2 (v2 none); firewood buy 4 (v2 5); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 11); labour buy 29 (v2 125); light armour buy 1 (v2 None)
- Ship linen snake: stays on Grandgues (worth +8/turn).
- Ship Flax Wyrm: Caillechâtel -> Chatgnan (+2/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +80/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 477 (+188 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 5.83 |
| ret | 3 | 0.91 | 1.17 |
| spin | 4 | 1.65 | 2.06 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 360/228, cloth 76/128

## Self-diagnosis

Nothing found this run.
