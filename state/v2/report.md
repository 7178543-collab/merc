# v2 shadow report

Turn 14073, 2026-11-16 18:45. Mode: handover. v2 runs: beer, cured fish, donations, firewood, fish, garments, grain, labour, meat, nets, porterage; v1 runs everything else.
Cash 9,818, prestige 3,623 (503 free, -2.7/turn).

## Items v2 runs (last turn)

| Item | Held | Bought | Used | Short | Expired | Live order |
| --- | --- | --- | --- | --- | --- | --- |
| beer | 19 | 9 | 4 | 0 | 0 | min_holding 60, sell 2, sell @ 2.96; stop 26, buy 9, buy @ 3.9 |
| cured fish | 0 | 0 | 0 | 0 | 0 | none |
| donations | 40 | 40 | 40 | 0 | 0 | stop 160, buy 40, buy @ 1 |
| firewood | 0 | 0 | 0 | 1 | 0 | stop 3, buy 1, buy @ 2.4 |
| fish | 7 | 7 | 7 | 0 | 0 | buy 7, buy @ 2.5 |
| garments | 31 | 0 | 2 | 0 | 0 | min_holding 30, sell 11, sell @ 21 |
| grain | 35 | 0 | 0 | 0 | 0 | stop 18, buy 5, buy @ 3.7 |
| labour | 29 | 29 | 504 | 0 | 25 | buy 29, buy @ 2.2 |
| meat | 1 | 1 | 1 | 0 | 0 | stop 42, buy 1, buy @ 3.02 |
| nets | 16 | 0 | 0 | 0 | 0 | min_holding 15, sell 9, sell @ 34 |
| porterage | 5 | 5 | 5 | 0 | 0 | buy 5, buy @ 1.1 |

**3 risks, 1 waste, 1 tuning** where v2 would act differently from v1.

## Risks (will stall or run out)

- **firewood**: brewery 1 ran short of firewood (buy is live (1 @ 2.4), but the home ask 2.90 is above it); labour need rises ~18/turn when they restart -> v2: raise the buy price (or ceiling) or find another source
- **firewood**: home ask 2.90 is above our ceiling 2.40 and last turn bought 0 of ~1 needed: the buy can't fill -> v2: raise the ceiling or find another source
- **firewood**: only 0.0 turns of firewood left and buying 1 (need 3) -> v2: buy 3

## Waste (money lost now)

- **labour**: 25 labour expired last turn (~47 coin): holding 29 against a ~0 buffer target -> v2: trim the buy until the stock is near 0

## Tuning

- **candles**: home ask 84.00 is above our ceiling 76.00 and last turn bought 1 of ~2 needed: the buy can't fill -> v2: raise the ceiling or find another source

## Notes

- labour: projection runs 100 over real use lately; planning 516, not 616

## Prestige spending, cheapest coin per prestige first

328 turns left: prestige gained now converts 80.7% of itself into legacy. Church contracts (best known rate, 16-38) are not in the snapshot, so they are not ranked here.

- agreed **tenants** to level 11: done - level 12 (agreed 11)
- agreed **prestige_management** to level 2: done - level 2 (agreed 2)
- agreed **apprentices** to level 2: done - level 2 (agreed 2)

| Sink | Site | Prestige/turn | Coin per prestige | With build cost | Notes |
| --- | --- | --- | --- | --- | --- |
| jousting 3 | arena | 230 | 49.6 | 50.0 | needs a arena (build cost 27,280); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| jousting 2 | arena | 210 | 54.3 | 54.8 | needs a arena (build cost 27,280); thin at home: swords, protection, light armour, plate armour; needs weaponry skill |
| maintain 1 | park | 0.5 | 55.8 | 55.8 | running |
| hold banquet 1 (fish) | mansion | 4.2 | 59.4 | 59.4 |  |
| hold banquet 2 (fish) | mansion | 6.8 | 60.4 | 60.4 | thin at home: wine, cheese |
| hold banquet 2 (pies) | mansion | 7 | 61.6 | 61.6 | thin at home: wine |
| hold banquet 2 (meat) | mansion | 6.8 | 62.9 | 62.9 | thin at home: wine, cheese |
| hold banquet 1 (meat) | mansion | 4.2 | 63.1 | 63.1 |  |
| hold banquet 4 (pies) | mansion | 18 | 64.3 | 64.3 | thin at home: hop beer, wine, stockfish |
| hold banquet 4 (premium) | mansion | 20 | 64.8 | 64.8 | thin at home: hop beer, wine, stockfish |
| hold mass 2 (premium) | cathedral | 360 | 61.4 | 65.6 | needs a cathedral (build cost 313,640); thin at home: furniture, jewellery, glassware, windows, candles, premium garments |
| hold banquet 3 (pies) | mansion | 8 | 66.4 | 66.4 | thin at home: hop beer |

## Ships (last turn, real)

| Ship | Crew set / ran | Running cost | Route | Trips | Sold there | Bought there | Trade value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Flax Wyrm | 0.0 / 0.00 | 0 | 134102075 | 0 | - | - | 0 |
| linen snake | 0.1 / 0.00 | 0 | 151802239 | 0.116 | - | - | 0 |

## Ship plans (this turn's world prices)

- **linen snake** on Grandgues: beer buy 4 @ 3.22, candles buy 9 @ 78.0, pasties buy 4 @ 16.0; crew 0.1; est +108 a turn; stock: candles 9 @ 78.0 (keep 12); stock: pasties 4 @ 16.0 (keep 14)
- **Flax Wyrm** on Caillechâtel: nothing pays; crew 0.0; est +0 a turn; stock: furniture 1 @ 14.1 (keep 145); stock: pasties 2 @ 14.8 (keep 14); best orders clear only 9 a turn after crew: ship stays at 0
- best towns now: Brunnham +124, Chribruck +113, Gosschweig +109, Amsdermund +109, Grandgues +108
- Brunnham would trade: candles buy 9 @ 76.5, pasties buy 4 @ 15.1; crew 0.1

## Ship routes at today's world prices (estimate, per turn)

61 towns in range by sea. A snekkja on a route: 250 units a trip, 3000 moves a turn at full crew, running cost ~115 coin a turn at full crew (crew is sized to the cargo, floor 0.10). Markets: up to 30% of what each town trades a turn, 5% slippage each way.

| Town | Moves | Ship cost per size unit | Crew | Out per turn (sell there) | Back per turn (buy there) | Net/turn |
| --- | --- | --- | --- | --- | --- | --- |
| Grandgues | 152 | 0.05 | 0.80 (92/turn) | timber 30 (7.98->12.25), firewood 33 (3.04->6.6), charcoal 19 (2.5->5.03), limestone 3 (18.9->23.18) | tools 7 (4.62->5.89), bricks 1 (7.61->11.4), cloth 4 (8.82->9.5), beer 4 (3.36->3.88) | +244 |
| Vauxvais | 204 | 0.06 | 1.00 (115/turn) | wax 13 (27.3->30.02), firewood 49 (3.04->5.65), charcoal 17 (2.5->4.75), lead ore 3 (7.4->8.36) | windows 0 (750.75->855), dyed cloth 10 (13.97->15.39), garments 1 (25.2->29.6), tools 16 (5.3->5.89) | +243 |
| Birkeningen | 1006 | 0.37 | 0.10 (12/turn) | lead bars 4 (12.18->13.49), arms 2 (31.29->33.25), nets 6 (34.4->35.53), wine 4 (7.4->8.17) | windows 1 (661.5->855), blades 4 (13.55->14.72), hop beer 1 (9.45->10.83) | +207 |
| Amsdermund | 1111 | 0.44 | 0.40 (46/turn) | jewellery 8 (99.75->104.5), hides 5 (13.02->15.58), wine 4 (7.4->9.5), lead ore 1 (7.4->11.11) | cloth 24 (5.78->9.5), dyed cloth 11 (12.6->15.39), windows 1 (840->855), tools 18 (4.83->5.89) | +200 |
| Hofkirchen | 991 | 0.36 | 0.50 (58/turn) | lead bars 6 (12.18->14.06), jewellery 8 (99.75->100.7), lead ore 3 (7.4->10.36) | windows 1 (803.25->855), dyed cloth 11 (11.97->15.39), cloth 24 (7.82->9.5), flax fibres 26 (5.78->7.15) | +172 |

**Best:** Grandgues at about +244 coin a turn.

## v2 orders

| Item | v2 buy | v2 sell | Why |
| --- | --- | --- | --- |
| arms | 1 @ 31.2, stop 2 |  | goal planner: buys 1 a turn for today's rates, keeps up to 2 (v2 had 1) |
| beer | 5 @ 4.06, stop 17 |  | uses 4.2/turn (household upkeep), makes 0.0, holds 19 = 4.4 turns |
| bread | 5 @ 2.6, stop 17 |  | goal planner: buys 5 a turn for today's rates, keeps up to 17 (v2 had 8) |
| candles | 3 @ 76.0, stop 6 |  | uses 1.5/turn (household upkeep), makes 0.0, holds 2 = 1.7 turns |
| cloth |  | 1 @ min 6.95 | goal planner: sells 1 a turn at 6.95, keeps 72 (no one offered it) |
| donations | 40 @ 1.0, stop 160 |  | goal planner: buys 40 a turn for today's rates, keeps up to 160 (v2 had 40) |
| firewood | 1 @ 2.4, stop 3 |  | goal planner: buys 1 a turn for today's rates, keeps up to 3 (v2 had 3) |
| fish | 7 @ 2.5, stop - |  | goal planner: buys 7 for today's rates (v2 had 7) |
| garments |  | 11 @ min 21 | goal planner: sells 11 at 21 (v2 had 10 at 28.6) |
| grain | 5 @ 3.7, stop 18 |  | goal planner: buys 5 a turn for today's rates, keeps up to 18 (v2 had 0) |
| labour | 29 @ 2.2, stop - |  | goal planner: buys 29 for today's rates (v2 had 16) |
| light armour | 1 @ 96, stop 10 |  | goal planner: buys 1 a turn for today's rates, keeps up to 10 (v2 had None) |
| meat | 1 @ 3.02, stop - |  | goal planner: buys 1 for today's rates (v2 had 1) |
| nets |  | 9 @ min 34.0 |  |
| porterage | 5 @ 1.1, stop - |  | goal planner: buys 5 for today's rates (v2 had 5) |
| rope |  | 2 @ min 69.5 | goal planner: sells 2 at 69.5 (v2 had 1 at 77.0) |
| tar | 1 @ 11.0, stop 1 |  | goal planner: buys 1 a turn for today's rates, keeps up to 1 (v2 had 1) |
| tools | 0 @ 6.2, stop - |  | uses 0.0/turn (observed), makes 0.0, holds 101 |

## Goal: business value (live: buys, sells, ships)
- Value now 23.6k (cash + stock at home prices); +291/turn over 6 turns, -8/turn over 24 turns.
- Limits: cash flow >= -242/turn, prestige >= -0.85/turn (values are after 200 tax a turn).
- Today's settings: value +97/turn, cash +84/turn, prestige -2.73/turn - breaks the prestige floor.
- Plan: value +20/turn, cash +26/turn, prestige -0.85/turn, inside both limits.
- Cash check (real vs predicted cash a tick, last 3): +416 vs +81, -2 vs +76, +351 vs +81.
- Route sales counted at most (what the ships really sold, a turn): rope 0.0.
- Changes, each priced on top of the one before (value/turn, limits aside):
  - ship linen snake -> Calange: +9/turn
  - ship Flax Wyrm -> Marmont: +1/turn
  - brewery 1 0.14 -> 0.08: +15/turn
  - spinnery 1 1.65 -> 1.37: +7/turn
  - net maker 0.00 -> 0.30: +3/turn
  - retting pit 1 0.91 -> 0.86: +1/turn
  - flax farm 1 4.64 -> 4.29: +3/turn
  - weavery 1 0.50 -> 0.39: -23/turn
  - sewing shop 1 0.30 -> 0.24: -6/turn
  - mansion 1 0.00 -> 0.45: -79/turn
- Model check over the last 59 turns: predicted -7/turn for the settings we ran, real -64/turn - OFF, trust the plan less.
- Worth of one more unit per turn: labour 1.81, thread 4.54, cloth 7.26, flax fibres 5.39, garments 21.00, nets 32.75, beer 3.37, timber 3.42, prestige 63.24, cash 0.00
- Orders it would set: bread buy 5 (v2 8); cloth sell 1 (v2 none); firewood buy 1 (v2 3); garments sell 11 (v2 10); grain buy 5 (v2 0); labour buy 29 (v2 16); light armour buy 1 (v2 None); rope sell 2 (v2 1)
- Ship linen snake: Grandgues -> Calange (+9/turn over staying).
- Ship Flax Wyrm: Caillechâtel -> Marmont (+1/turn over staying).
- Management: ~11.39 of 18 used.
- Investments:
  - Tenants L13 for 500 prestige: +90/turn, doesn't pay yet (waits until 800 free (keeps 300 after))

## Chain sizing

Mode HOLD, garments sold 10.5/turn (+0.0 exported); plan makes 32.8 garments a turn.
Labour: own 500, everything else 340, chain may buy 350 -> chain allowance 510, chain plan 423 (+134 vs now).

| Step | Plots | Now | Plan |
| --- | --- | --- | --- |
| flax | 11 | 4.64 | 4.36 |
| ret | 3 | 0.91 | 0.87 |
| spin | 4 | 1.65 | 1.68 |
| weave | 3 | 0.50 | 1.28 |
| sew | 2 | 0.30 | 0.80 |

Buffers: flax fibres 106/77, thread 1050/228, cloth 72/128

## Self-diagnosis

- R1: candles slot dry: 2.5 held, 1.5 a turn (luxury slot (+3 prestige)); our buy 3 @ 85.5, home ask 84.0; our bid is already at/over the ask (sellers too thin)
- R1: firewood slot dry: 0.0 held, 2.8 a turn (heating slot (+0.1 prestige)); our buy 1 @ 2.4, home ask 2.9; ask over the cap 2.1 (60 coin per prestige)
- R2: spinnery 1 blocked by thread space: 1050 held of 1084 capacity, we make 82.5 a turn; no buy on it: add a sell order or more capacity for thread
