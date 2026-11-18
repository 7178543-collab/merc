# v2 shadow report

Turn 14123, 2026-11-18 20:46. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 14,867, prestige 3,588 (468 free, -2.6/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 16 | 4 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 17, buy 9, buy @ 3.8 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 34 | 0 | 0 | 0 | 0 | stop 18, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 516 | 0 | 13 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 33.6 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**2 risks, 2 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), home ask 0.00 x0, yet 0 bought last turn); labour need rises ~18/turn when they restart -> v2: find out why the buy isn't filling
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **Flax Wyrm**: Flax Wyrm cost 12 coin last turn (crew 0.10) and its route traded nothing -> v2: pause it (crew 0) until a route is proven to sell
- **labour**: 13 labour expired last turn (~26 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **firewood**: no sellers at home right now and stock is below the runway -> v2: import it or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 516, not 613

## Prestige spending, cheapest coin per prestige first

278 turns left: prestige gained now converts 75.2% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 (premium) | arena | 420 | 45.6 | 45.9 | needs a arena (build cost 28,345); thin at home: protection, premium garments, premium swords, premium armour; needs weaponry skill |
| jousting 2 (premium) | arena | 400 | 49.1 | 49.4 | needs a arena (build cost 28,345); thin at home: protection, light armour, premium swords, premium garments, premium armour; needs weaponry skill |
| jousting 3 | arena | 230 | 55.1 | 55.6 | needs a arena (build cost 28,345); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold banquet 1 (fish) | mansion | 4.2 | 58.0 | 58.0 |  |
| maintain 1 | park | 0.5 | 58.2 | 58.2 | running |
| jousting 2 | arena | 210 | 60.3 | 60.9 | needs a arena (build cost 28,345); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| hold mass 2 (premium) | cathedral | 360 | 55.8 | 61.1 | needs a cathedral (build cost 303,300); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |
| hold banquet 2 (fish) | mansion | 6.8 | 61.3 | 61.3 | thin at home: cheese |
| hold banquet 1 (meat) | mansion | 4.2 | 62.7 | 62.7 |  |
| hold banquet 4 (premium) | mansion | 20 | 64.0 | 64.0 | thin at home: stockfish |
| hold banquet 2 (meat) | mansion | 6.8 | 64.6 | 64.6 | thin at home: cheese |
| hold banquet 2 (pies) | mansion | 7 | 64.6 | 64.6 | thin at home: cheese |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.1 / 0.10 | 12 | 134102075 | 0.012 | - | - | 0 |
| linen snake | 0.0 / 0.00 | 0 | 151802239 | 0 | - | - | 0 |

## Ship plans (this turn's world prices)

- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn
- **linen snake** on Grandgues: nothing pays; crew 0.0; est +0 a turn; stock: pasties 4 @ 16.0 (keep 14); best orders clear only -0 a turn after crew: ship stays at 0
- best towns now: Amsdermund +690, Vauxvais +366, Cobholme +344, Disscester +291, Chribruck +247
- Amsdermund would trade: furniture buy 63 @ 13.7, pasties buy 3 @ 15.6; crew 1.0

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~120 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.90 (108/turn) | timber 29 (8.77->12.25), firewood 32 (3.07->6.46), charcoal 19 (2.77->5.65), bread 159 (2.67->3.04) | cheese 3 (6.88->8.84), chisels 2 (11.87->12.25), cloth 5 (11.34->11.6), flax fibres 1 (6.88->7.15) | +265 |
| Bordees | 1112 | 0.46 | 0.20 (24/turn) | cured fish 6 (24.57->30.78), cloth 7 (12.18->17.1), garments 10 (40->41.8), steel ingots 4 (15.86->16.72) | tapestries 2 (640.5->717.25), axes 1 (16.59->19.19), wrought iron 2 (16.7->18.24) | +228 |
| Amsdermund | 1111 | 0.46 | 0.40 (48/turn) | jewellery 3 (105->123.5), grain 2 (3.06->4.52) | cloth 24 (7.35->11.6), garments 2 (27.3->40.2), wax 6 (24.15->27.74), wrought iron 4 (13.76->18.24) | +228 |
| Kirchwerp | 1072 | 0.43 | 0.60 (72/turn) | jewellery 3 (105->123.5), thread 91 (4.98->5.7), wine 27 (6.72->7.84), tackles 3 (182.7->190) | garments 2 (26.67->40.2), cloth 16 (9.92->11.6), wrought iron 4 (14.7->18.24), cookware 4 (19.43->22.23) | +194 |
| Rouhomme | 368 | 0.12 | 0.60 (72/turn) | bread 159 (2.67->3.29), flour 3 (21.84->28.69), furniture 8 (14.18->16.72), casks 8 (6.35->7.79) | cloth 17 (10.29->11.6), tools 21 (4.51->5.42), garments 2 (33.39->40.2), butter 1 (71.92->76.47) | +150 |

**Best:** Grandgues at about +265 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 32.4, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 3.9, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 16 = 3.9 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 8) |
| candles | 2 @ 76.0, stop 61 |  | goal planner: buys 2 a turn for today's rates, keeps up to 61 (v2 had 2) |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| furniture | 2 @ 16.4, stop 150 |  | goal planner: buys 2 a turn for today's rates, keeps up to 150 (v2 had None) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 25.8) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 16) |
| light armour | 1 @ 105, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 33.6 | goal planner: sells 9 at 33.6 (v2 had 9 at 34.4) |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 82.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 28.4k (cash + stock at home prices); +204/turn over 6 turns, +107/turn over 24 turns.
- Limits: cash flow >= -453/turn, prestige >= -0.70/turn (values are after 200 tax a turn).
- Today's settings: value +92/turn, cash +75/turn, prestige -2.55/turn - breaks the prestige floor.
- Plan: value +22/turn, cash +32/turn, prestige -0.70/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +287 vs +60, +114 vs +78, +306 vs +85.
- Route sales counted at most (what the ships really sold, a turn): none.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Karlmoor: +8/turn
  - ship Flax Wyrm -> Angefont: +2/turn
  - brewery 1 0.14 -> 0.08: +15/turn
  - spinnery 1 1.65 -> 1.41: +3/turn
  - retting pit 1 0.91 -> 0.80: +2/turn
  - net maker 0.00 -> 0.28: +2/turn
  - flax farm 1 4.64 -> 4.01: +6/turn
  - ropewalk 1 0.25 -> 0.31: +2/turn
  - sewing shop 1 0.30 -> 0.25: -26/turn
  - weavery 1 0.50 -> 0.40: -2/turn
- Model check over the last 60 turns: predicted +127/turn for the settings we ran, real +125/turn.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.38, garments 21.00, nets 32.76, beer 3.28, timber 3.92, prestige 60.34, cash 0.00
- Orders it would set: bread buy 5 (v2 8); cloth sell 1 (v2 none); firewood buy 1 (v2 3); furniture buy 2 (v2 None); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 16); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Karlmoor (+8/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Angefont (+2/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +87/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 8.7/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 429 (+138 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.73 |
| ret | 3 | 0.91 | 0.95 |
| spin | 4 | 1.65 | 1.67 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 73/77, thread 1050/227, cloth 72/128

## Self-diagnosis

- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask none (no sellers at home)
