# v2 shadow report

Turn 14136, 2026-11-19 09:20. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,806, prestige 3,652 (532 free, -0.8/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 47 | 24 | 12 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 47, buy 24, buy @ 3.78 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 30 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 34 | 0 | 0 | 0 | 0 | stop 19, buy 5, buy @ 3.7 |
| labour | 64 | 64 | 526 | 0 | 38 | buy 64, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**6 risks, 1 waste, 3 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **cured meat**: mansion 1 ran short of cured meat (buy is live (3 @ 29), 3 bought last turn); labour need rises ~35/turn when they restart -> v2: the buy is too small for the stalled buildings: raise it
- **cured meat**: only 0.5 turns of cured meat left and buying 3 (need 12) -> v2: buy 12
- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.82 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.82 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3
- **tar**: ropewalk 1 ran short of tar (buy is live (1 @ 11), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~7/turn when they restart -> v2: find out why the buy isn't filling

## Waste (money lost now)

- **labour**: 38 labour expired last turn (~72 coin): holding 64 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **candles**: home ask 84.00 is above our ceiling 76.00 and last turn bought 0 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **meat**: no sellers at home right now and stock is below the runway -> v2: import it or find another source
- **tar**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 106 over real use lately; planning 526, not 615
- labour expiry guard: 38 bought labour expired last turn, buy 26 (not 26) this turn

## Prestige spending, cheapest coin per prestige first

265 turns left: prestige gained now converts 73.6% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 50.1 | 50.4 | needs a arena (build cost 27,280); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 53.8 | 54.1 | needs a arena (build cost 27,280); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 54.1 | 54.6 | needs a arena (build cost 27,280); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 56.4 | 56.4 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 57.5 | 57.5 |  |
| hold banquet 4 (pies) | mansion | 18 | 59.1 | 59.1 | thin at home: stockfish, cheese, pies |
| jousting 2 | arena | 210 | 59.2 | 59.8 | needs a arena (build cost 27,280); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 2 (fish) | mansion | 6.8 | 59.9 | 59.9 | thin at home: cheese |
| hold banquet 3 (pies) | mansion | 8 | 60.6 | 60.6 | thin at home: cheese, pies |
| hold banquet 3 (fish) | mansion | 7.6 | 61.0 | 61.0 | thin at home: cheese |
| hold banquet 2 (pies) | mansion | 7 | 61.3 | 61.3 | thin at home: cheese, pies |
| hold banquet 4 (premium) | mansion | 20 | 62.2 | 62.2 | thin at home: stockfish |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: pasties 1 @ 15.9 (keep 14); best orders clear only -9 a turn after crew: ship stays at 0
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 8 @ 16.2 (keep 14); best orders clear only 10 a turn after crew: ship stays at 0
- best towns now: Amsdermund +680, Gotthafen +498, Hofkirchen +466, Brunnham +377, Cobholme +350
- Amsdermund would trade: candles buy 1 @ 76.5, furniture buy 65 @ 14.3; crew 1.0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~120 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.90 (108/turn) | timber 39 (8.19->12.44), thread 97 (4.98->6.27), firewood 31 (2.96->6.13), charcoal 19 (2.75->5.27) | cheese 3 (6.72->7.31), wax 5 (27.72->28.12), cloth 8 (11.34->11.5), garments 2 (33.39->34) | +434 |
| Clarfranche | 1484 | 0.70 | 0.10 (12/turn) | garments 10 (26.4->35.72) | looms 1 (556.5->750.5), candles 1 (76.12->84), furniture 1 (16.7->21) | +282 |
| Fontaux | 411 | 0.13 | 0.70 (84/turn) | thread 97 (4.98->7.27), timber 29 (8.19->12.35), salt 4 (5.83->7.79), flax fibres 8 (5.88->6.27) | cheese 3 (6.62->7.31), cured meat 3 (24.57->25.4) | +277 |
| Rouhomme | 368 | 0.12 | 1.00 (120/turn) | bread 150 (2.65->3.42), thread 21 (4.98->7.93), timber 31 (8.19->11.02), garments 9 (26.4->28.5) | tools 17 (5.06->5.32), garments 1 (32.97->34) | +219 |
| Marmont | 638 | 0.20 | 0.10 (12/turn) | garments 10 (26.4->35.91), thread 13 (4.98->6.79), raw cloth 1 (10.29->15.2) | ploughs 5 (74.03->83.12), candles 1 (78.75->84), furniture 1 (15.65->21) | +164 |

**Best:** Grandgues at about +434 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 33.0, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 12 @ 3.72, stop 47 |  | uses 11.7/turn (household upkeep), makes 0.0, holds 47 = 4.0 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 9) |
| candles | 2 @ 76.0, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had 2) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| cured meat | 3 @ 29.0, stop 11 |  | goal planner: buys 3 a turn for today's rates, keeps up to 11 (v2 had 12) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 25.8) |
| grain | 5 @ 3.7, stop 19 |  | goal planner: buys 5 a turn for today's rates, keeps up to 19 (v2 had 0) |
| labour | 64 @ 2.2, stop - |  | goal planner: buys 64 for today's rates (v2 had 26) |
| light armour | 1 @ 104, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.8) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.1k (cash + stock at home prices); -296/turn over 6 turns, +84/turn over 24 turns.
- Limits: cash flow >= -450/turn, prestige >= -0.97/turn (values are after 200 tax a turn).
- Today's settings: value -154/turn, cash -146/turn, prestige +1.33/turn.
- Plan: value +7/turn, cash +16/turn, prestige -0.97/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +87 vs -159, +160 vs -147, -319 vs -134.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Brunnham: +12/turn
  - ship Flax Wyrm -> Gotthafen: +1/turn
  - mansion 1 1.00 -> 0.45: +133/turn
  - brewery 1 0.14 -> 0.08: +14/turn
  - net maker 0.00 -> 0.28: +4/turn
  - spinnery 1 1.65 -> 1.40: -3/turn
  - retting pit 1 0.91 -> 0.79: +4/turn
  - flax farm 1 4.64 -> 3.99: +7/turn
  - sewing shop 1 0.30 -> 0.25: -8/turn
  - weavery 1 0.50 -> 0.40: +6/turn
- Model check over the last 59 turns: predicted +76/turn for the settings we ran, real +63/turn.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.71, beer 3.24, timber 3.51, prestige 62.94, cash 0.00
- Orders it would set: bread buy 5 (v2 9); cloth sell 1 (v2 none); cured meat buy 3 (v2 12); firewood buy 1 (v2 3); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 64 (v2 26); light armour buy 1 (v2 None)
- Ship linen snake: Grandgues -> Brunnham (+16/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Gotthafen (+1/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.2/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 375, chain may buy 350 -> chain allowance 475, chain plan 430 (+141 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.75 |
| ret | 3 | 0.91 | 0.95 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 72/77, thread 1055/228, cloth 72/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.82; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1055 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
