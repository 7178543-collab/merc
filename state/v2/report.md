# v2 shadow report

Turn 13829, 2026-11-06 14:49. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,766, prestige 3,279 (159 free, -0.9/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 57 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 2 | 1 | 0 | stop 16, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 34 | 9 | 0 | 0 | 0 | stop 34, buy 9, buy @ 3.7 |
| labour | 29 | 29 | 500 | 0 | 29 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (4 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.40 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 29 labour expired last turn (~48 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **bread**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.40 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 500, not 600

## Prestige spending, cheapest coin per prestige first

572 turns left: prestige gained now converts 94.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.7 | 50.7 | running |
| jousting 3 | arena | 230 | 54.1 | 54.3 | needs a arena (build cost 26,895); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 54.5 | 54.5 |  |
| hold banquet 4 (pies) | mansion | 18 | 57.0 | 57.0 | thin at home: hop beer, ham, stockfish, candles |
| hold banquet 2 (fish) | mansion | 6.8 | 59.2 | 59.2 |  |
| jousting 2 | arena | 210 | 59.2 | 59.5 | needs a arena (build cost 26,895); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 1 (meat) | mansion | 4.2 | 60.5 | 60.5 |  |
| hold banquet 4 | mansion | 17.5 | 60.5 | 60.5 | thin at home: hop beer, ham, stockfish, candles |
| hold banquet 2 (pies) | mansion | 7 | 60.9 | 60.9 | thin at home: pies, candles |
| hold banquet 4 (premium) | mansion | 20 | 61.1 | 61.1 | thin at home: hop beer, ham, stockfish, candles, premium cheese |
| hold banquet 3 (fish) | mansion | 7.6 | 61.5 | 61.5 | thin at home: hop beer |
| hold banquet 3 (pies) | mansion | 8 | 61.5 | 61.5 | thin at home: hop beer, pies, candles |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 6 @ 15.5 (keep 14); best orders clear only 10 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 5 @ 15.5 (keep 14); best orders clear only 7 a turn after crew: ship stays at 0
- best towns now: Orlesailles +50, Bordetes +47, Rouhomme +41, Toqueque +38, Bordees +36
- Orlesailles would trade: pasties buy 14 @ 13.8; crew 0.2

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~105 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Blanans | 297 | 0.08 | 0.50 (52/turn) | garments 10 (18.94->23.37), timber 27 (7.25->9.79), thread 7 (4.36->4.99), limestone 2 (19.21->23.75) | jewellery 3 (73.5->85.97), cheese 5 (7.4->9.17), flax plants 10 (1.4->1.76), cloth 8 (7.82->8) | +132 |
| Heilegg | 826 | 0.24 | 0.20 (21/turn) | garments 10 (18.94->21.66), nets 6 (33.4->35.72), yarn 14 (4.87->5.7), acid 1 (114.45->118.75) | jewellery 4 (73.5->85.97), cloth 24 (7.25->8), cheese 5 (6.72->9.17), coats 2 (72.45->75.52) | +129 |
| Kleinburgh | 1440 | 0.58 | 0.10 (10/turn) | garments 10 (18.94->28.31), cloth 1 (7.85->11.11) | jewellery 4 (80.33->85.97), cheese 5 (5.88->9.17), bellows 1 (218.4->224.2) | +128 |
| Brebronn | 862 | 0.26 | 0.40 (42/turn) | garments 10 (18.94->23.94), glass ingots 1 (64.05->65.55), nets 1 (33.4->35.34), yarn 14 (4.87->5.22) | bellows 1 (200.55->224.2), cheese 5 (5.51->9.17), flax plants 60 (0.96->1.76), jewellery 1 (72.45->85.97) | +124 |
| Neuborn | 780 | 0.22 | 1.00 (105/turn) | timber 27 (7.25->11.78), garments 10 (18.94->21.85), wine 10 (6.35->7.6), wax 2 (22.68->24.13) | jewellery 4 (78.23->85.97), flax fibres 21 (5.23->6.05), coats 2 (72.45->75.52) | +119 |

**Best:** Blanans at about +132 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 29.8, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 3.0 turns |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 4 @ 2.4, stop 14 |  | goal planner: buys 4 a turn for today's rates, keeps up to 14 (v2 had 7) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 23.4) |
| grain | 0 @ 3.7, stop 34 |  | goal planner: buys 0 a turn for today's rates, keeps up to 34 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 1 @ min 69.5 | goal planner: sells 1 a turn at 69.5, keeps 0 (no one offered it) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 24.9k (cash + stock at home prices); +218/turn over 6 turns, +197/turn over 24 turns.
- Limits: cash flow >= -240/turn, prestige >= +5.87/turn (values are after 200 tax a turn).
- Today's settings: value +72/turn, cash +71/turn, prestige -0.92/turn - breaks the prestige floor.
- Plan: value -145/turn, cash -43/turn, prestige +3.28/turn - could not meet the prestige floor.
- Cash check (real vs predicted cash a tick, last 3): +252 vs +67, -246 vs +60, -709 vs +50 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Vauxvais: +3/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +7/turn
  - weavery 1 0.50 -> 0.55: -6/turn
  - ropewalk 1 0.25 -> 0.00: -6/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.18: +15/turn
  - brewery 1 0.14 -> 0.27: -20/turn
  - spinnery 1 1.65 -> 0.88: -21/turn
  - retting pit 1 0.91 -> 0.50: -9/turn
  - flax farm 1 4.64 -> 2.50: -24/turn
- Model check over the last 62 turns: predicted +98/turn for the settings we ran, real +76/turn.
- Worth of one more unit per turn: labour 1.66, thread 4.17, cloth 6.67, flax fibres 4.94, garments 19.30, nets 29.92, beer 2.90, timber 3.46, prestige 10000.00, cash 0.00
- Orders it would set: cloth sell 1 (v2 none); firewood buy 4 (v2 7); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None); rope sell 1 (v2 none)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.18, worth +10/turn.
- Ship linen snake: Grandgues -> Vauxvais (+5/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +80/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 450 (+161 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 5.21 |
| ret | 3 | 0.91 | 1.04 |
| spin | 4 | 1.65 | 1.84 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 491/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 4 @ 2.4, home ask none (no sellers at home)
- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.05 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
