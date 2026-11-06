# v2 shadow report

Turn 13830, 2026-11-06 15:54. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,958, prestige 3,278 (158 free, -1.0/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 53 | 0 | 4 | 0 | 0 | min_holding 60, sell 16, sell @ 3.06 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 80, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 14, buy 4, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 19.3 |
| grain | 34 | 0 | 0 | 0 | 0 | buy @ 3.7 |
| labour | 29 | 29 | 500 | 0 | 29 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 31.8 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 2 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (4 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **flax fibres**: flax fibres buffer 1.0 turns (holds 27, next step uses 28/turn) -> v2: check the step that makes it
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), but the home ask 11.40 is above it); labour need rises ~7/turn when they restart -> v2: raise the buy price (or ceiling) or find another source

## Waste (money lost now)

- **labour**: 29 labour expired last turn (~48 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: home ask 11.40 is above our ceiling 11.00 and last turn bought 0 of ~0 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 500, not 600

## Prestige spending, cheapest coin per prestige first

571 turns left: prestige gained now converts 94.3% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| maintain 1 | park | 0.5 | 50.4 | 50.4 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 54.4 | 54.4 |  |
| jousting 3 | arena | 230 | 54.2 | 54.4 | needs a arena (build cost 26,136); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 4 (pies) | mansion | 18 | 56.4 | 56.4 | thin at home: wine, ham, stockfish, pies, candles |
| hold banquet 2 (fish) | mansion | 6.8 | 57.3 | 57.3 | thin at home: wine |
| hold banquet 2 (pies) | mansion | 7 | 59.3 | 59.3 | thin at home: wine, pies, candles |
| hold banquet 3 (fish) | mansion | 7.6 | 59.6 | 59.6 |  |
| jousting 2 | arena | 210 | 59.4 | 59.6 | needs a arena (build cost 26,136); thin at home: swords, protection, coats, plate armour; needs weaponry skill |
| hold banquet 4 | mansion | 17.5 | 59.7 | 59.7 | thin at home: wine, ham, stockfish, candles |
| hold banquet 1 (meat) | mansion | 4.2 | 60.1 | 60.1 |  |
| hold banquet 3 (pies) | mansion | 8 | 60.1 | 60.1 | thin at home: pies, candles |
| hold banquet 4 (premium) | mansion | 20 | 60.4 | 60.4 | thin at home: wine, ham, stockfish, candles, premium cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: pasties buy 8 @ 15.6; crew 0.1; est +16 a turn; stock: pasties 8 @ 15.6 (keep 14)
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 5 @ 15.5 (keep 14); best orders clear only 6 a turn after crew: ship stays at 0
- best towns now: Rouhomme +65, Orlesailles +53, Toqueque +38, Bordees +36, Bordetes +32
- Rouhomme would trade: pasties buy 14 @ 13.5; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~105 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Fontaux | 411 | 0.12 | 0.70 (74/turn) | garments 10 (18.98->27.55), thread 57 (4.38->5.65), timber 27 (7.25->11.3), charcoal 17 (2.96->4.6) | candles 1 (86.62->104.5), flax fibres 5 (5.23->6.05), dyed yarn 1 (4.94->5.56) | +256 |
| Bedenis | 566 | 0.16 | 0.10 (11/turn) | garments 10 (18.98->34.01), nets 3 (33.8->34.2) | candles 1 (84.53->104.5), flax fibres 6 (4.94->6.05), dyed yarn 1 (4.2->5.56), canvas 1 (30.24->30.97) | +170 |
| Gotthafen | 964 | 0.32 | 0.20 (21/turn) | garments 10 (18.98->24.32), nets 2 (33.8->36.48), casks 6 (6.62->7.41) | looms 1 (546->593.75), candles 1 (83.48->104.5), cloth 24 (7.3->8.4), dyed yarn 1 (4.14->5.56) | +142 |
| Clarfranche | 1484 | 0.61 | 0.10 (11/turn) | garments 10 (18.98->31.16) | candles 1 (86.1->104.5), chisels 2 (6.2->7.89), blades 2 (11.23->12.16), dyed yarn 1 (4.09->5.56) | +139 |
| Hanstein | 380 | 0.11 | 0.40 (42/turn) | timber 15 (7.25->11.69), garments 10 (18.98->22.23), nets 3 (33.8->37.81), mouldboards 1 (34.65->44.84) | candles 1 (80.33->104.5), flax fibres 12 (5.21->6.05), flax plants 29 (1.31->1.77) | +139 |

**Best:** Fontaux at about +256 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 31.2, stop 2 |  | uses 0.5/turn (household upkeep), makes 0.0, holds 2 = 4.0 turns |
| beer |  | 16 @ min 3.06 | goal planner: sells 16 a turn at 3.06, keeps 60 (no one offered it) |
| bread | 5 @ 2.6, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 17 = 4.0 turns |
| cloth |  | 1 @ min 7.05 | goal planner: sells 1 a turn at 7.05, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 80 |  | uses 40.0/turn (household upkeep), makes 0.0, holds 40 = 1.0 turns |
| firewood | 2 @ 2.4, stop 5 |  | goal planner: buys 2 a turn for today's rates, keeps up to 5 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| flax plants |  | 2 @ min 1.21 | goal planner: sells 2 a turn at 1.21, keeps 219 (no one offered it) |
| garments |  | 11 @ min 19.3 | goal planner: sells 11 at 19.3 (v2 had 10 at 24.2) |
| grain | 0 @ 3.7, stop 34 |  | goal planner: buys 0 a turn for today's rates, keeps up to 34 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 0) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 31.8 | goal planner: sells 9 at 31.8 (v2 had 9 at 34.0) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | uses 0.2/turn (observed), makes 0.0, holds 0 = 0.0 turns |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 24.5k (cash + stock at home prices); +157/turn over 6 turns, +170/turn over 24 turns.
- Limits: cash flow >= -248/turn, prestige >= +5.91/turn (values are after 200 tax a turn).
- Today's settings: value +77/turn, cash +77/turn, prestige -0.99/turn - breaks the prestige floor.
- Plan: value -138/turn, cash -32/turn, prestige +3.21/turn - could not meet the prestige floor.
- Cash check (real vs predicted cash a tick, last 3): -246 vs +60, -709 vs +50, +192 vs +71 - FAILED: the goal only cuts until a tick passes.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Vauxvais: +23/turn
  - ship Flax Wyrm -> no route: +0/turn
  - net maker 0.00 -> 0.29: +8/turn
  - ropewalk 1 0.25 -> 0.00: -5/turn
  - ropewalk 1 [make rope 1] 0.00 -> 0.15: +17/turn
  - weavery 1 0.50 -> 0.56: -8/turn
  - brewery 1 0.14 -> 0.27: -20/turn
  - spinnery 1 1.65 -> 0.87: -26/turn
  - retting pit 1 0.91 -> 0.49: -7/turn
  - flax farm 1 4.64 -> 2.50: -24/turn
- Model check over the last 62 turns: predicted +98/turn for the settings we ran, real +66/turn.
- Worth of one more unit per turn: labour 1.66, thread 4.17, cloth 6.67, flax fibres 4.94, garments 19.30, nets 29.84, beer 2.90, timber 3.10, prestige 10000.00, cash 0.00
- Orders it would set: beer sell 16 (v2 none); cloth sell 1 (v2 none); firewood buy 2 (v2 3); flax plants sell 2 (v2 none); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 9 (v2 0); labour buy 29 (v2 0); light armour buy 1 (v2 None)
- Recipe: ropewalk 1 make rope 2 -> make rope 1 at 0.15, worth +9/turn.
- Ship linen snake: Grandgues -> Vauxvais (+25/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> no route (+0/turn over staying).
- Management: ~11.39 of 17 used.
- Investments:
  - Tenants L13 for 500 prestige: +80/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 447 (+158 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 5.16 |
| ret | 3 | 0.91 | 1.03 |
| spin | 4 | 1.65 | 1.82 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 27/77, thread 502/228, cloth 73/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 2 @ 2.4, home ask none (no sellers at home)
- R5: flax fibres buy not filling: bid 5.05 under the home ask 6.05 for 6 turns, bought 0.0 of 1, 27.3 held (1.0 turns); raise needs Taylor (ceiling None)
